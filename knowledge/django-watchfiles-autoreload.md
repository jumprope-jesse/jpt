# django-watchfiles - Efficient Runserver Autoreloading

Source: https://adamj.eu/tech/2025/09/22/introducing-django-watchfiles/

## What is it?

django-watchfiles integrates the `watchfiles` library with Django's runserver autoreloader. It replaces the default polling-based file watching with OS-native file watching APIs, making autoreloads faster and more efficient.

## The Problem with Default Autoreloader

Django's default `StatReloader` constantly polls the filesystem for changes. This:
- Uses significant CPU (~10% every other second on a medium-sized project)
- Drains laptop battery when developing unplugged
- Can be slower and less reliable than native file watching

## How watchfiles Works

- Uses Rust-powered `watchfiles` library (by Samuel Colvin, author of Pydantic)
- Wraps OS-specific file watching APIs (cross-platform)
- Notifies only when files actually change, no polling
- Nearly 0% CPU usage during idle

## Installation

```bash
pip install django-watchfiles
```

```python
# settings.py
INSTALLED_APPS = [
    # ...
    "django_watchfiles",
]
```

## Verification

When runserver starts, you'll see `WatchfilesReloader` instead of `StatReloader`:

```
$ ./manage.py runserver
Watching for file changes with WatchfilesReloader
```

## Comparison with Watchman

Django has a built-in Watchman integration, but:
- Requires installing and running a separate Watchman server
- The Python client `pywatchman` was broken on Python 3.10 for 2.5 years
- More infrastructure to maintain

django-watchfiles is simpler - just a pip install and settings change.

## Performance

On a medium-sized project (385K lines, 206 packages) on M1 MacBook:
- Default reloader: ~10% CPU every other second
- django-watchfiles: ~0% CPU

## Author

Created by Adam Johnson, with contributions from Tom Forbes (author of Django's Watchman integration). First stable release in 2024.

## Related

- [watchfiles](https://github.com/samuelcolvin/watchfiles) - Underlying Rust-powered library
- [Boost Your Django DX](https://adamj.eu/books/boost-your-django-dx/) - Adam Johnson's book
