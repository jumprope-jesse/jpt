# Django System Check Framework Optimization

Source: [Adam Johnson - Django: Write-up on optimizing the system check framework](https://adamj.eu/tech/2024/03/23/django-optimizing-system-checks/)

## Overview

Django's system check framework gained a reputation for being slow on larger projects. Adam Johnson's optimization work (released in Django 5.1) reduced check runtime by ~50% (37ms to 18ms on a 118-model project).

## Profiling Approach

### Using cProfile with IPython

```python
# Basic profiling
%prun -D profile -s cumtime run_checks(include_deployment_checks=True)

# Profile second run to eliminate import costs
run_checks(include_deployment_checks=True)
%prun -D profile -s cumtime run_checks(include_deployment_checks=True)

# Loop for faster checks (reduces noise, scales timings)
%prun -D profile -s cumtime [run_checks(include_deployment_checks=True) for _ in range(100)]
```

### Visualizing with gprof2dot

```bash
gprof2dot -n 0.1 -f pstats profile | dot -Tsvg -o profile.svg
```

### Data-Oriented Profiling

Patch functions to log data at exit to understand repetition patterns:

```python
all_routes = []

import atexit, pprint

@atexit.register
def print_routes():
    pprint.pprint(all_routes)

def _route_to_regex(route, is_endpoint):
    all_routes.append(route)
    # ...
```

## Key Optimizations

### 1. URL Checks (~13% + ~10% savings)

**Error handler signature check** - Was running once per URLconf instead of once total (handlers only exist in root URLconf).

**Preventing regex compilation** - URL checks were forcing regex compilation when most commands don't need it. Fixed with lazy descriptors.

**Caching `_route_to_regex()`** - Despite routes seeming unique, there's repetition (e.g., ModelAdmin creates same URL patterns for each model). Added `@functools.lru_cache`.

### 2. Model._meta Attributes

**`verbose_name_raw`** (~15% savings):
- Added `@cached_property` (accessed 5x per model)
- Fast path for plain strings (avoids `translation.override()`)

```python
@cached_property
def verbose_name_raw(self):
    if isinstance(self.verbose_name, str):
        return self.verbose_name
    with override(None):
        return str(self.verbose_name)
```

**`_property_names`** (~4% savings):
- Replaced slow `inspect.getattr_static()` (~496ns) with direct `__dict__` access (~25ns)

```python
@cached_property
def _property_names(self):
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

**`get_parent_list()`** (~1% savings) - Converted to cached property.

### 3. Field Attributes

- Cache `ForeignObjectRel.get_accessor_name()`
- Access `Field.attname` and `Field.column` directly
- Make `Field.unique` a plain attribute
- Optimize `RelatedField._check_clashes()`
- Optimize `ForeignObject._check_unique_target`

### 4. Admin Action Checks (~1% savings)

**Combine check functions** - Two checks both called `_get_base_actions()`, merged to call once.

**Lazy default computation**:
```python
# Before: eager default always computed
return getattr(func, "short_description", capfirst(name.replace("_", " ")))

# After: try-except, compute only if needed
try:
    return func.short_description
except AttributeError:
    return capfirst(name.replace("_", " "))
```

## General Patterns

1. **Caching is powerful** - `@cached_property` and `@lru_cache` for repeated computations
2. **Avoid unnecessary work** - Don't compute defaults that are rarely used
3. **Look at data flow** - Log actual values to find repetition patterns
4. **Check scope** - Ensure checks run at the right level (once vs per-object)
5. **Avoid slow stdlib functions** - `inspect.getattr_static()` is 20x slower than direct `__dict__` access

## Tools

- **cProfile** - Built-in Python profiler (much faster in Python 3.12+ via PEP 669)
- **gprof2dot** - Visualize profiles as call graphs
- **django-asv** - Django's continuous benchmarking suite
- **IPython %prun** - Convenient profiling magic command

## Related

- [Django: How to profile and improve startup time](https://adamj.eu/tech/)
- [Python: Profile a section of code with cProfile](https://adamj.eu/tech/)
- Adam Johnson's book: "Boost Your Django DX"
