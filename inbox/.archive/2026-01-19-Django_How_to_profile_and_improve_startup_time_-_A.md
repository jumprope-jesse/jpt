---
type: link
source: notion
url: https://adamj.eu/tech/2023/03/02/django-profile-and-improve-import-time/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-02-14T15:50:00.000Z
---

# Django: How to profile and improve startup time - Adam Johnson

## AI Summary (from Notion)
- Importance of Startup Time: The startup time of a Django project significantly affects the development experience, especially during management commands and server reloads.

- Profiling Tools:
- -X importtime: A built-in Python profiler introduced in Python 3.7 that times and reports module import durations.
- importtime-waterfall: A tool that visualizes import times using HAR files, allowing for easier identification of slow imports.
- cProfile: A traditional profiler for detailed function call timing, useful for identifying bottlenecks in imports.

- Improvement Techniques:
- Upgrade Python: Moving to newer Python versions can yield performance improvements, with Python 3.11 being significantly faster.
- Remove Unused Code: Eliminating dead code or dependencies can lead to immediate performance gains.
- Defer Imports: Lazy loading of modules to reduce startup time, particularly for infrequently used features.

- Common Pitfalls:
- Import-Time Database Queries: Running database queries at import time can slow down startup. Use lazy loading or caching strategies.
- Code Generation Overhead: Be cautious with tools that generate code at import time, as they can add significant delays.

- Advanced Strategies:
- Monkey-Patching: A controversial technique where you modify third-party library behavior to optimize performance.
- Forking CPython for Strict Modules: A method employed by Instagram to enforce stricter import-time behavior, reducing unnecessary overhead.

- Takeaway: Improving startup time is often a cumulative effort requiring multiple strategies, as no single change typically solves the problem. Regular profiling and refactoring are essential for maintaining optimal performance.

## Content (from Notion)

A waterfall, as used several times in this post.

Your Django project’s startup time impacts how smooth it is to work with. Django has to restart your project every time you run a management command and when runserver reloads. This involves importing all your apps, and thus all the modules that they import.

As you add more code and dependencies to your project, you may notice its startup time increasing. Development can slow down to a crawl; reports of 10 second startup times are, sadly, not unusual.

In this post, we’ll cover tools for profiling startup time, and tactics for reducing it.

## How to profile startup time

Here are several tools for profiling startup time.

### X importtime: Python’s import profiler

Python 3.7 introduced the -X importtime option, a specialized profiler that times all imports. It prints a table to stderr, summarizing microsecond timing information for each imported module:

```plain text
$ python -X importtime -c 'import django'
import time: self [us] | cumulative | imported package
import time:       136 |        136 |   _io
import time:        20 |         20 |   marshal
import time:       256 |        256 |   posix
import time:       261 |        672 | _frozen_importlib_external
...
import time:       499 |       6898 |     subprocess
import time:       309 |        309 |           weakref
import time:        60 |         60 |               org
import time:        10 |         70 |             org.python
import time:         7 |         77 |           org.python.core
import time:       187 |        572 |         copy
import time:       228 |        799 |       django.utils.functional
import time:       183 |        982 |     django.utils.regex_helper
import time:       340 |      12228 |   django.utils.version
import time:       206 |      12434 | django

```

This table totals 72 rows, snipped with ... to keep the blog post readable.

Read from the bottom-up to see the “import tree”:

- Running the code in the django module itself takes 206 microseconds (its self time).
- Cumulatively, all the imports required for django take 12434 microseconds.
- The last module that django imported was django.utils.version. This took 340 microseconds inside itself, and a cumulative 12228 microseconds in its imports.
- Continuing up, you can see other modules as they were imported: django.utils.regex_helper, django.utils.functional, copy, etc.
### importtime-waterfall: Make pretty charts from X importtime

The raw data from -X importtime is useful, but reading through a table of numbers doesn’t make it easy to spot the slow modules. This is where the importtime-waterfall tool by Anthony Sottile can help. It wraps python -X importtime to capture the data, and can output it as an HAR (HTTP Archive) file.

The HAR format is designed for profiles of HTTP requests made by a website, but it neatly doubles up for containing module import times as fake “requests“. There are then many viewers you can use to read the data in a waterfall chart.

To make a HAR file with importtime-waterfall, install it in your virtual environment, and then invoke it with --har and the module name to profile:

```plain text
$ importtime-waterfall --har django > django.har

```

You can then visualize this file with one of many HAR viewer tools. The one linked in the docs is the HTTP Archive Viewer by Jan Odvarko. Drop the file directly onto its web page to view it as a waterfall chart:

HAR Viewer showing timeline for Django

(Click to enlarge.)

Each module has two timings, expanded on hover:

- “Waiting” time (purple): the time spent waiting for dependencies to import
- “Receiving” time (grey): the time spent executing the code in the module (“self” time)
Modules with high “Receiving” time are normally the most susceptible to optimization.

Beware: the timings are wrong by a factor of 1000. This is because python -X importtime records in microseconds, but HAR files only support integer milliseconds. Rather than lose precision, importtime-waterfall multiplies timings by 1000. Use the waterfall chart to compare relative values, rather than absolute ones.

The example makes it clear that when running import django, most of the time is spent actually importing the subprocess module.

### Run importtime-waterfall on your project

importtime-waterfall can only profile a module import, and not a full command, like ./manage.py runserver. So to profile a Django project, you’ll need to create a short module that initializes your project at import time. Let’s look at doing so with an example project that reproduces a performance problem I recently encountered.

Below is a template. Put it in a file like it.py (standing for import time) next to your manage.py, and update the os.environ line to point to your settings file.

```plain text
import os

import django
from django.urls import resolve

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "example.settings")
django.setup()
resolve("/")

```

django.setup() initializes Django for your project, loads all apps and their models, and eventually calls all AppConfig.ready() methods. This is normally done automatically in manage.py and your ASGI/WSGI entrypoint.

The resolve() call forces Django to load your full URLconf and all referred-to modules. Django loads URLs and views lazily, but you probably care about profiling their import time too, at least to improve runserver restart time.

Test the wrapper module with:

```plain text
$ python -m it

```

If it succeeds with no output then it works fine. But if it fails, you may need to adapt it. For example, on one project I profiled, the resolve() line needed a different URL, since there was no root URL at /.

With the wrapper module working, run importtime-waterfall like so:

```plain text
$ importtime-waterfall --har it > it.har

```

The output HAR file will have a lot of entries. For the example project with one app, I got 503 imported modules; on a large client project, I found 4403.

Here’s a subsection of the example project’s profile:

HAR Viewer showing the timeline for example project, with ``views`` module importing ``distutils``.

(Click to enlarge.)

This screenshot shows example.views importing distutils.util, and that takes about 26 milliseconds (26 seconds / 1000). distutils is suspect because it’s used for creating Python packages, and rarely needed at runtime. (It’s also deprecated and slated for removal in Python 3.12.)

Let’s take a look at what example.views imports from distutils:

```plain text
from distutils.util import strtobool


def index(request):
    show_referral_banner = strtobool(request.GET.get("referred", "false"))
    ...

```

Ah, only the strtobool() function. This casts strings like "True" or "0" to booleans. The function is not really related to packaging, but simply an internal convenience function, that happens to do something required in this view.

Imagine that after examining the project’s code, you determine that the referred query parameter will only ever be "true" or "false". So you don’t need the complexity of strtobool(), and all the modules it drags in with it. Instead, you can directly compare with "true":

```plain text
def index(request):
    show_referral_banner = request.GET.get("referred", "false") == "true"
    ...

```

After removing the distutils import and re-profiling, the example project drops from 503 to 409 modules, with a 24% / 26 millisecond time saving. Not bad.

### cProfile: More detailed profiling

It’s often not so easy to spot why an import is slow. Modules with a high “self” time have module-level code that takes a while, but it may be unclear what’s taking time. To determine what’s slow, you can use a “traditional” profiler that captures the runtime of each function call.

A simple but effective combo is Python’s built-in profiler module cProfile, along with the visualization conversion tool gprof2dot. cProfile times each function execution, and gprof2dot outputs a graph of time spent per function, with colourization of the “hot paths”. Here’s a quick run-through of using those.

First, profile the problematic module with cProfile’s -o option to save the output file, and -m option to select the module:

```plain text
$ python -m cProfile -o example_views.prof -m example.views

```

(Using the slow version of example.views that still imports distutils.)

This option profiles the whole module and its imports. To profile a limited section like a few class definitions, see the snippet in my post Profile a section of code with cProfile.

Then install the yelp fork of gprof2dot (which runs on new Pythons), and pipe its output into dot from Graphviz:

```plain text
$ gprof2dot example_views.prof | dot -Tsvg -o example_views.svg

```

If you don’t have dot installed, you can instead copy and paste the output into Graphviz Online, and download the SVG.

You can then open the SVG in your browser, for example with Firefox on macOS:

```plain text
$ open -a Firefox example_views.svg

```

The centre of the chart looks like this, when zoomed out:

Graph of time spent per function in example project, full zoomed out diagram

(Click to enlarge.)

The chart tends to be huge-mongous. Each box represents a function or module-level execution, and there can be a lot of them. Red boxes have the most execution time and blue ones have the least, with green ones in the middle. Arrows point from callers to callees.

Look for red or green boxes as the “hot spots” in the program. Zoom in on suspect areas and trace execution to try and understand what’s going on.

After a little inspection of the example graph, I found this fairly well-called function in teal:

Graph of time spent per function in the example project, full zoomed out diagram, focusing on regex compilation taking 28%.

(Click to enlarge.)

The first line in each box is the final name in the module path, line number, and function or class name. You can hover over this for the browser’s label that shows the full module path. Very useful for boxes with a module labelled something unspecific like __init__.

In the above screenshot, I’ve added a simulated label to show that the __init__ module in question is from Python’s re module. The function is compile, which compiles a regular expression string. So we can see that 21 milliseconds, almost the entire import time of distutils, is from dependencies creating regular expression objects. (The boxes pointing to compile come from functions in setuptools and logging.)

Regular expression compilation is often expensive—at the end of the day, it is another programming language. To avoid import time cost, Django mostly uses a lazy regular expression wrapper that compiles on first use. Looking at this graph, it might make sense to use a similar pattern in logging or setuptools.

## Ways to improve startup time

Slow startup time is often a “many drops in the bucket” situation. There’s no single module import that dominates startup time. Instead, lots of little things add up to slowness.

Correspondingly, improving startup time normally takes a bunch of piecewise targeted changes. Here are some techniques that can help, roughly ordered by their approximate utility. Enjoy!

### Upgrade Python

Upgrading Python is groundwork for any optimization effort. Python keeps getting faster, especially with the focus of the Faster CPython project from Python 3.11+.

Python 3.11 is ~25% faster than Python 3.10, and Python 3.12 promises to be notably faster again. Before you chase the harder gains from improving individual modules, upgrade to Python 3.11+, which requires Django 4.1+. (If only there were a tool to help you upgrade Django….)

### Remove unused code

Removing old features or dependencies will provide the easiest wins. When looking through your import waterfall, first look for the dead weight that you can cut, particularly unused dependencies.

### Swap packages for leaner alternatives

Sometimes your code uses a huge package where smaller alternatives exist. For example, if you’re importing numpy for only one linear regression function, statistics.linear_regression() in the standard library is a faster-to-import alternative, albeit less flexible.

### Consider swapping out third-party services’ packages

Third-party services’ official packages are often worth avoiding. These packages are normally slow to import because they cover all possible API endpoints and use cases. You might be better off calling their API directly, say with urllib3. Not only is this faster to import, it can be more robust in the long term as you aren’t dependent on their package being maintained.

For example, I once saw that the official Dropbox package took ~400ms to import, on a project that only used two endpoints. Replacing the package with custom functions would save almost all of that time.

### Copy relevant bits into your project

If you’re importing a large library for a few small classes or functions, consider including custom versions of those things in your project. For example, in the real world strtobool() case, I couldn’t determine which strings needed to be supported, so I copied the function from distutils into the project.

### Remove duplicate packages

Sometimes projects grow to use packages with identical functionality. For example, one project I worked on used three different ISO date parsing packages, when only one would do. (Or maybe none, if the standard library’s limited datetime.fromisoformat() would work.)

### Avoid import-time database queries

It is particularly slow to run database queries at import time. They’re also a potential source of bugs since data fetched at startup can go stale.

One pattern is to preload some rarely-changing data:

```plain text
COUNTRIES = dict(Country.objects.values_list("id", "name"))

```


