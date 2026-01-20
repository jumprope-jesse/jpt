---
type: link
source: notion
url: https://adamj.eu/tech/2024/03/23/django-optimizing-system-checks/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-03-24T04:54:00.000Z
---

# Django: Write-up on optimizing the system check framework - Adam Johnson

## AI Summary (from Notion)
- Optimization of System Check Framework: The write-up focuses on profiling and optimizing the Django system check framework to improve its speed, addressing the common perception that it is slow.

- Performance Improvements: Recent optimizations have reduced the runtime of system checks from 37ms to 18ms, approximately a 50% reduction, even for projects with a considerable number of models and lines of code.

- Benchmarking: A django-asv benchmark was created to continuously track performance over time, indicating significant improvements, including a drop from ~21ms to ~4ms for specific checks.

- Key Optimizations:
- URL Checks: Major improvements were made in URL checks by eliminating redundant checks and preventing unnecessary regular expression compilations.
- Caching: Implementing caching for frequently accessed properties significantly improved performance for various model attributes.
- Profiling: Utilized cProfile and other profiling tools to identify slow functions and optimize them, leading to more efficient code paths.

- Collaboration and Community Contribution: The author has contributed to the Django community by creating benchmarks and optimizing existing checks, as well as proposing structural changes for further efficiency.

- Limitations: The author acknowledges that the optimizations focused on individual functions rather than a holistic view of the checks, which may present further opportunities for improvement.

- Call for Further Collaboration: The author expresses openness to consulting on similar optimization projects and encourages contributions from the community.

- Related Work: The write-up links to the author’s book and previous posts on optimizing Django and Python performance, inviting readers to explore more resources.

## Content (from Notion)

Streamlining the Django.

Django’s system check framework provides fantastic protection for configuration mishaps. It’s like a targeted linter that runs when you start Django commands. It takes advantage of runtime setup to inspect the true state rather than infer it from the source.

I love the system check framework: I have contributed to several built-in checks, maintain a package of extra checks, and have a whole chapter on it in Boost Your Django DX.

Unfortunately, the framework has gained a reputation for being slow, at least on larger projects. For example, Jeff Triplett recently tooted:

> My #Django magic wand would disable checks running on all the things by default unless explicitly turned called or turned on.

I’ve heard and seen similar advice from others. Anders Hovmöller’s package django-fastdev goes as far as monkey-patching checks to run in a separate thread, so they don’t block runserver startup.

I always felt dismayed by this observation. It doesn’t seem right that the checks should take so long since most of them do fast things like isinstance() or comparing strings.

Recently, I found some time to dig into profiling and optimizing the system checks. These optimizations are all committed to Django’s main branch and will be released in Django 5.1 later this year. They take running checks on an example client project from 37ms to 18ms, a 50% reduction in runtime. (That’s with all modules imported. I covered optimizing import time in a previous post.)

The example project is not particularly large, with 118 models and 50k lines of Python. Still, the savings should scale to bigger projects because checks generally take time proportional to the number of objects such as models, template libraries, etc.

This post covers the work I did on this project, detailing some of the optimizations. By the way, a running theme was “it me”—several of the slower checks were ones I worked on—woops! At least I have improved my profiling and coding skills since and now had this opportunity to optimize them for everyone.

## Adding a django-asv benchmark

On my first optimization ticket, Simon Charette requested that I also create a benchmark in Django ASV. This project is Django’s continuous benchmarking suite that tracks its performance over time, using the asv (airspeed velocity) tool.

I eventually did this in django-asv PR #80, albeit after a few of my optimizations were merged. The benchmark runs all checks, including deployment and database ones:

```plain text
from django.core.checks import run_checks

from ...utils import bench_setup


class SystemChecks:
    def setup(self):
        bench_setup(migrate=True)

    def time_checks(self):
        run_checks(include_deployment_checks=True, databases=("default",))

```

You can see it running on the django-asv benchmark grid, under “system_check_benchmarks”. It looks pretty flat, though, because there’s a fair amount of noise between runs, and the history doesn’t go back to before my first, most significant optimizations. But I did run it on older commits locally and got this nice graph:

django-asv benchmark for system checks showing steep drop

That’s a drop from ~21ms to ~4ms, a ~80% saving, due to optimizing the URL handler check, as covered shortly. The benchmark is slightly biased towards looking good because it registers many URLconfs, but you may see something similar in a real project.

## Profiling the checks

To measure where the slowness lay in the system check framework, I used good ol’ cProfile, the “default” profiler built into Python. Whilst it has some per-function overhead, that has been reduced drastically in Python 3.12 as it now uses sys.monitoring, the “low impact monitoring” API introduced by PEP 669.

For convenience, I ran cProfile via IPython’s %prun magic using the below commands. I unregistered checks from third-party packages to focus on Django core.

```plain text
In [1]: from django.core.checks import run_checks, registry

In [2]: for func in list(registry.registry.registered_checks):
   ...:     if not func.__module__.startswith('django.'):
   ...:         registry.registry.registered_checks.discard(func)
   ...:

In [3]: %prun -D profile -s cumtime run_checks(include_deployment_checks=True)

```

Sometimes, I only profiled a second run of checks:

```plain text
In [3]: run_checks(include_deployment_checks=True)

In [4]: %prun -D profile -s cumtime run_checks(include_deployment_checks=True)

```

This allowed me to eliminate the startup cost of importing modules.

And sometimes, when looking at faster checks, I profiled a loop of many runs:

```plain text
In [4]: %prun -D profile -s cumtime [run_checks(include_deployment_checks=True) for _ in range(100)]

```

Looping reduces the effects of noise and scales up timings, which cProfile only displays in milliseconds.

I visualized the profiles with grpof2dot, which graphs functions with shading depending on their share of the runtime cost. I used variants on this command pipeline:

```plain text
$ gprof2dot -n 0.1 -f pstats profile | dot -Tsvg -o profile.svg

```

Here’s a snippet of one of those graphs:

grpof2dot graph of Django’s run_checks() function

(Click to enlarge.)

The red node represents run_checks(), with 99.71% of the runtime (there’s a slight overhead from IPython). It points to blue nodes representing some of the costlier checks it calls directly, with slower functions shaded lighter. I like using this visualization to zoom in on “hot spots“ quickly.

## Optimizing the URL checks

I found two optimizations for URLconf checks and a bonus general optimization.

### Error handler signature check

This one is a bit embarrassing. A few years ago, I accidentally added a check that ran many times instead of once.

In 2018, I proposed and implemented Ticket #29642 with a check that covers the signatures of custom error handler views. These are views that you reference from your root URLconf by string path, like handler400 for bad requests:

```plain text
from django.urls import include, path

urlpatterns = [
    # ...
]

handler400 = "example.core.views.errors.bad_request"

```

The check ensures that handler functions have a correct signature because it’s easy to get it wrong and hard to test them (as I’d experienced).

Unfortunately, I created the check function within the URLResolver class, which represents not only the root URLconf, but also nested URLconfs added with include(). So the check was repeated for each URLconf, completely unnecessarily, since handlers only exist in the root URLconf. (This also meant any failures would be displayed many times.)

In Ticket #35229 I corrected this oversight. The check function now runs once, only looking at the root URLconf. This change yielded a saving of 13% of the total check runtime for the example project but much more for the django-asv benchmark, as covered above.

### Preventing regular expression compilation

Whether you use path() or re_path(), Django’s URL resolution is based on regular expressions. Compiling a regular expression is relatively slow, so Django defers that work until needed. However, with profiling, I found that some URL system checks unnecessarily forced this compilation, taking ~10% of the total runtime. This work was nearly always wasted since most Django commands don’t need regular expressions compiled.

I opened Ticket #35250 to optimize these checks. It was a slightly complicated PR involving descriptors, so I won’t describe it much here. But there was part of it that I’d like to highlight.

RoutePattern is Django’s internal class for URLs created with path(). It takes the route, like /books/<int:book_id>/. It converts the route into a regular expression and a dict of converter classes, with the function _route_to_regex(), which returns both values in a tuple.

Since the introduction of RoutePattern in Django 2.0, this class has called _route_to_regex() in two places:

```plain text
class RoutePattern(CheckURLMixin):
    ...

    def __init__(self, route, name=None, is_endpoint=False):
        ...
        self.converters = _route_to_regex(str(route), is_endpoint)[1]

    ...

    def _compile(self, route):
        return re.compile(_route_to_regex(route, self._is_endpoint)[0])

```

Calling the conversion function twice but only storing one return value at a time is wasteful when both could be stored. It seems this was introduced accidentally to handle translated URLs, which do require a recompile. But for the typical case of non-translated URLs, we can avoid half the calls to _route_to_regex() by storing both values in __init__():

```plain text
class RoutePattern(CheckURLMixin):
    ...

    def __init__(self, route, name=None, is_endpoint=False):
        ...
        self._regex, self.converters = _route_to_regex(str(route), is_endpoint)
        ...

```

Together, these optimizations dropped the URL checks to ~1% of the total runtime, about a 10⨉ improvement.

### Optimizing _route_to_regex()

As part of the previous ticket, I looked inside _route_to_regex() and noticed some opportunities for optimization. I made these changes in Ticket #35252, making it about ~50% faster.

The PR included several minor optimizations that added up. One more significant data-oriented optimization was adding caching with @functools.lru_cache:

```plain text
+@functools.lru_cache
 def _route_to_regex(route, is_endpoint):

```

This surprised me. On the face of it, you might think that URL routes tend to be unique, so a cache wouldn’t be used much. But in reality, there tends to be a lot of repetition, which I discovered when investigating all the calls within my example project. That makes this a data-oriented optimization, guided by looking at the data flowing through the system.

To see the data, I patched the function to display all given routes at exit:

```plain text
all_routes = []

import atexit, pprint


@atexit.register
def print_routes():
    pprint.pprint(all_routes)


def _route_to_regex(route, is_endpoint):
    ...
    all_routes.append(route)
    ...

```

atexit runs a function at process exit, and pprint does pretty-printing so the list shows up one item per line.

The list showed a lot of repetitive blocks like:

```plain text
...
'',
'add/',
'<path:object_id>/history/',
'<path:object_id>/delete/',
'<path:object_id>/change/',
'<path:object_id>/',
'core/comment/',
'',
'add/',
'<path:object_id>/history/',
'<path:object_id>/delete/',
'<path:object_id>/change/',
'<path:object_id>/',
'core/category/',
...

```

I recognized these as coming from ModelAdmin.get_urls(), which creates the same URLs for each registered model:

```plain text
def get_urls(self):
    ...

    return [
        path("", ...),
        path("add/", ...),
        ...,
        path("<path:object_id>/history/", ...),
        path("<path:object_id>/delete/", ...),
        path("<path:object_id>/change/", ...),
        # For backwards compatibility (was the change url before 1.9)
        path("<path:object_id>/", ...),
    ]

```

So that’s one common source of repetition, scaling with the number of admin-registered models.

I also saw some repetition from the project’s URLs, particularly of '' (the empty string) and sub-paths like login/ (the project has several role-specific login pages). Projects will have more or less repetition depending on how their URLs are structured.

## Optimizing some Model._meta attributes

Model._meta contains metadata for a model class derived from the class Meta definition. Despite the underscore prefix, it has a public, documented API, as well as many private attributes.

In several cases, profiling revealed that computing some private Model._meta attributes took significant time, slowing the system checks that used them. Optimizing the relevant functions sped up all code paths using the attributes, including the relevant system checks.

### Model._meta.verbose_name_raw

In Ticket #35232, I optimized the verbose_name_raw attribute. Two minor changes saved nearly ~15% of the total runtime for system checks (benchmarked after applying other optimizations). This property computed the untranslated version of verbose_name:

```plain text
from django.utils.translation import override


class Options:  # The class for Model._meta
    ...

    @property
    def verbose_name_raw(self):
        """Return the untranslated verbose name."""
        with override(None):
            return str(self.verbose_name)

```

I made two optimizations:

1. Caching with @cached_property, since the property was accessed five times per model and the result never changed.
1. A fast path for when verbose_name is a plain string, avoiding the relatively slow translation.override() call.
It now looks like:

```plain text
from django.utils.functional import cached_property
from django.utils.translation import override


class Options:
    ...

    @cached_property
    def verbose_name_raw(self):
        """Return the untranslated verbose name."""
        if isinstance(self.verbose_name, str):
            return self.verbose_name
        with override(None):
            return str(self.verbose_name)

```

### Model._meta._property_names

Nearly seven years ago, in Ticket #28269, I fixed a bug in this cached property, but my PR made it unnecessarily slow. It appeared in my profiling of system checks, and so in Ticket #35270, I optimized it. This change saved ~4% of the total runtime (benchmarked after applying other optimizations).

Model._meta._property_names contains a set of names of all the @property-decorated functions on the class. Django uses it internally to make Model(some_property=something) work. Previously, this set was computed by looping over all names defined in the class, getting them with inspect.getattr_static(), and checking if they are a property:

```plain text
import inspect


class Options:
    ...

    @cached_property
    def _property_names(self):
        """Return a set of the names of the properties defined on the model."""
        names = []
        for name in dir(self.model):
            attr = inspect.getattr_static(self.model, name)
            if isinstance(attr, property):
                names.append(name)
        return frozenset(names)

```

getattr_static() is a “cautious” version of getattr() that avoids triggering any kind of “magic” like __getattribute__(). I added the use of getattr_static() in the old ticket to solve a bug with instance-only attributes. But unfortunately, it’s slow compared to vanilla attribute access due to the bunch of stuff it does to preserve that “caution”:

```plain text
In [1]: import inspect

In [2]: %timeit getattr(int, "__str__")
24.8 ns ± 0.331 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)

In [3]: %timeit inspect.getattr_static(int, "__str__")
496 ns ± 6.22 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)

```

Looking at the function again, I determined a different way of achieving the same result. It’s possible to skip getattr() and its “static” variant by reading attributes from the __dict__ of the class, merging those of its ancestors:

```plain text
class Options:
    ...

    @cached_property
    def _property_names(self):
        """Return a set of the names of the properties defined on the model."""
        names = set()
        seen = set()
        for klass in self.model.__mro__:
            names |= {
                name
                for name, value in klass.__dict__.items()
                if isinstance(value, property) and name not in seen
            }
            seen |= set(klass.__dict__)
        return frozenset(names)

```

My initial optimized implementation had a bug that Sage Abdullah caught, reported in Ticket #35301, and summarily fixed by myself. This is thanks to Wagtail being tested with Django’s main branch. Hooray for early testing!

### Model._meta.get_parent_list()

In Ticket #35241, I optimized this function call by turning it into a cached property. It’s a straightforward optimization, with some extra backwards compatibility concerns, but saved ~1% from the total runtime. Caching is indeed a mighty lever.

## Optimizing some model Field attributes

Like the above, I optimized some attributes on the model Field class, related classes, and some check functions using field attributes. Mostly, the optimizations are related to adding caching or using plain attributes instead of properties. I won’t detail any of them here, but here are the related tickets:

- Ticket #35230 - Cache ForeignObjectRel.get_accessor_name().
- Ticket #35236 - Access Field.attname and Field.column directly.
- Ticket #35246 - Make Field.unique a plain attribute.
- Ticket #35266 - Optimize RelatedField._check_clashes().
- Ticket #35285 - Optimize ForeignObject._check_unique_target.
Each yielded a slight improvement, reducing the total runtime between 1% and 5%, but they add up!

## Optimizing the admin actions checks

The admin has a lot of system checks, but I found they were generally fast. Two did stand out on my profiles though: the checks for admin actions. I optimized them in Ticket #35237 to yield a ~1% improvement on the total runtime with two changes.

First, I combined the checks into one function. Previously, each check function would fetch the list of actions with obj._get_base_actions():

```plain text
def _check_action_permission_methods(self, obj):
    ...
    actions = obj._get_base_actions()
    ...


def _check_actions_uniqueness(self, obj):
    ...
    names = collections.Counter(name for _, name, _ in obj._get_base_actions())
    ...

```

After I merged them, the actions are retrieved only once:

```plain text
def _check_actions(self, obj):
    actions = obj._get_base_actions()
    ...

```

A simple way to halve some work.

Second, I optimized ModelAdmin._get_action_description(), the slowest function in the call tree under _get_base_actions(). Previously, the function used getattr() with an eagerly computed default:

```plain text
@staticmethod
def _get_action_description(func, name):
    return getattr(func, "short_description", capfirst(name.replace("_", " ")))

```

The string manipulation in capfirst() and name.replace() is fairly fast, but it’s not free, about 613ns on my machine. Given that most action functions have a description, especially the default one delete_selected this work was nearly always wasted.

I changed the function to use a try-except, computing a default name only if needed:

```plain text
@staticmethod
def _get_action_description(func, name):
    try:
        return func.short_description
    except AttributeError:
        return capfirst(name.replace("_", " "))

```

## Check “push down” proposals

Along the way, I made two extra tickets proposing restructuring some existing system checks. Many system checks have a pattern where the top-level check function loops over objects and calls their individual check() methods, such as the database backend checks:

```plain text
def check_database_backends(databases=None, **kwargs):
    if databases is None:
        return []
    issues = []
    for alias in databases:
        conn = connections[alias]
        issues.extend(conn.validation.check(**kwargs))
    return issues

```

I noticed that checks for cache and template backends didn’t follow that pattern. Instead, some top-level check functions loop through all backends to perform backend-specific checks. For example, see this cache backend check:

```plain text
def check_file_based_cache_is_absolute(app_configs, **kwargs):
    errors = []
    for alias, config in settings.CACHES.items():
        cache = caches[alias]
        if not isinstance(cache, FileBasedCache):
            continue
        ...

```

The checks waste a smidgen of time running, particularly when they compute some data before looping. However, they waste substantially more time and memory by importing otherwise unused parts of the framework. Most notably, the template checks force importing Django’s Template Language, even though using another backend such as Jinja is pretty common.

I proposed these two tickets to “push down” the check functions to the backend classes:

- Push cache backend checks down to backend classes.
- Push templates checks down to backend engine classes.
I’m glad two other contributors have jumped in to work on them.

## Fin

Well, that’s the end of my write-up for this work. I hope you have learned some things and enjoy the faster system checks.

It’s worth noting how I was limited here:

- I only focused on optimising a single function at a time. I believe there are further savings from looking at checks holistically, possibly precomputing some data used in multiple checks.
- I only benchmarked a relatively small project. This was due to having few big clients at current. I would be interested to see profiles from more extensive projects, even those as big as a Kraken 😉
- I only worked on core Django. My example project used Wagtail and django-debug-toolbar. I saw some of their checks took a significant chunk of the total runtime but did not have time to work on them.
I am open to consulting on similar optimization projects, open source or not.

Enjoy the faster checks,

—Adam

Newly updated: my book Boost Your Django DX now covers Django 5.0 and Python 3.12.

Subscribe via RSS, Twitter, Mastodon, or email:

Your email address:

One summary email a week, no spam, I pinky promise.

Related posts:

- Django: How to profile and improve startup time
- Python: Profile a section of code with cProfile
- Django: Clean up unused code with Vulture
Tags: django

© 2024 All rights reserved. Code samples are public domain unless otherwise noted.


