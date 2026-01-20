# Django Startup Time Profiling and Optimization

Source: https://adamj.eu/tech/2023/03/02/django-profile-and-improve-import-time/

## Why It Matters

Django startup time affects development experience - every `manage.py` command and `runserver` reload requires importing all apps and dependencies. Reports of 10+ second startup times are not unusual in large projects.

## Profiling Tools

### 1. Python's `-X importtime` (Built-in, Python 3.7+)

Specialized profiler that times all imports:

```bash
python -X importtime -c 'import django'
```

Outputs a table to stderr with microsecond timing:
- **self [us]**: Time executing the module's code
- **cumulative**: Total time including all imports
- Read bottom-up to see import tree

### 2. importtime-waterfall (Recommended)

By Anthony Sottile. Wraps `-X importtime` and outputs HAR (HTTP Archive) files for visualization:

```bash
pip install importtime-waterfall
importtime-waterfall --har django > django.har
```

View with HTTP Archive Viewer (http://www.softwareishard.com/blog/har-viewer/) - drop HAR file onto webpage.

**Key insight**: "Receiving" time (grey) = module self-time. High receiving time = good optimization target.

**Warning**: Timings are wrong by 1000x (microseconds displayed as milliseconds). Use for relative comparison only.

### 3. Profiling Your Django Project

Create `it.py` (import time) wrapper next to `manage.py`:

```python
import os
import django
from django.urls import resolve

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "example.settings")
django.setup()
resolve("/")  # Forces URLconf loading
```

Then profile:

```bash
python -m it  # Test it works
importtime-waterfall --har it > it.har
```

### 4. cProfile for Detailed Function Profiling

When you can't spot why an import is slow:

```bash
python -m cProfile -o module.prof -m module.name
pip install gprof2dot
gprof2dot module.prof | dot -Tsvg -o module.svg
open -a Firefox module.svg
```

Graph shows:
- Red boxes = hot paths (most time)
- Blue boxes = cold paths (least time)
- Arrows point from callers to callees

Useful for finding patterns like "regex compilation taking 28% of import time".

## Optimization Techniques (Ordered by Utility)

### 1. Upgrade Python

Python 3.11+ is ~25% faster than 3.10 (Faster CPython project). Do this first before chasing individual module optimizations.

Requires Django 4.1+.

### 2. Remove Unused Code

Dead features and unused dependencies are easy wins. Look for dead weight in import waterfall.

### 3. Swap Packages for Leaner Alternatives

Example: `statistics.linear_regression()` instead of importing numpy for one function.

### 4. Replace Third-Party Service Packages

Official SDK packages often cover all endpoints and are slow. Consider calling APIs directly with `urllib3`.

Example: Official Dropbox package took 400ms to import, but project only used 2 endpoints.

### 5. Copy Relevant Bits

If importing a large library for a few functions, copy them into your project.

Example from article:
```python
# Before: imports entire distutils (26ms)
from distutils.util import strtobool

# After: inline the logic (0ms import overhead)
show_referral_banner = request.GET.get("referred", "false") == "true"
```

### 6. Remove Duplicate Packages

Projects often accumulate multiple packages with identical functionality (e.g., three ISO date parsing libraries).

### 7. Avoid Import-Time Database Queries

**Bad pattern:**
```python
COUNTRIES = dict(Country.objects.values_list("id", "name"))
```

Database queries at import time are slow and create stale data bugs. Use lazy loading or caching instead.

### 8. Defer Imports

Move imports inside functions/methods for infrequently-used features:

```python
def rarely_called_view(request):
    from heavy.library import Thing  # Only import when called
    ...
```

### 9. Avoid Code Generation at Import Time

Tools that generate code at import (e.g., some ORMs, serializers) add significant delays.

## Advanced Techniques

### Monkey-Patching Third-Party Libraries

Controversial but effective - modify third-party library behavior to optimize performance.

### Forking CPython for Strict Modules

Instagram's approach - enforce stricter import-time behavior to reduce unnecessary overhead. Advanced technique.

## Key Insights

- Startup time is usually "many drops in the bucket" - no single import dominates
- Improvement requires piecewise targeted changes across many modules
- Django's lazy patterns (like lazy regex compilation) are good examples to follow
- Regular profiling + refactoring needed to maintain optimal performance

## Related Django Tools

- Django Debug Toolbar - Runtime performance
- django-silk - Request/response profiling
- django-chronos - Page load time overlay
