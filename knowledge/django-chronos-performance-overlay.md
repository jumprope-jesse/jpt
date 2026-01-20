# django-chronos - Page Load Time Overlay

Source: https://github.com/djpeacher/django-chronos

## What is it?

Django middleware that displays page load times and query counts directly in the browser. Shows a stats overlay in the bottom-left corner of your pages during development.

## Installation

```bash
pip install django-chronos
```

```python
# settings.py
INSTALLED_APPS = [
    # ... your other apps
    'django_chronos',
]

MIDDLEWARE = [
    'django_chronos.middleware.ChronosStartMiddleware',  # Must be first
    # ... your other middleware
    'django_chronos.middleware.ChronosEndMiddleware',    # Must be last
]
```

## Configuration

### CHRONOS_SHOW_IN_PRODUCTION (default: False)

Controls whether stats are shown in production (DEBUG=False). In production, stats only show to superusers.

```python
CHRONOS_SHOW_IN_PRODUCTION = True
```

### CHRONOS_SWAP_METHOD (default: 'prepend')

How stats are inserted into the response:
- `'prepend'`: Insert before the target
- `'append'`: Insert after the target
- `'replace'`: Replace the target with stats

### CHRONOS_SWAP_TARGET (default: '</body>')

String in response where stats will be inserted. Stats won't display if string doesn't exist.

### Customizing Display

Override the template by creating `chronos/chronos.html` in your Django project.

Available context variables:
- `middleware_cpu_time`, `middleware_sql_time`, `middleware_sql_count`, `middleware_total_time`
- `view_cpu_time`, `view_sql_time`, `view_sql_count`, `view_total_time`
- `total_cpu_time`, `total_sql_time`, `total_sql_count`, `total_time`

Note: In production, `*_sql_time` and `*_sql_count` are zero. Wrap in `{% if debug %}` blocks.

## Use Case

Quick visibility into page performance during development without opening devtools. Good for catching N+1 query issues and slow middleware.

## License

MIT License

## Related

- Django Debug Toolbar - More comprehensive debugging
- django-silk - Request/response profiling
