# Django Sentry Initialization

Source: https://blog.bmispelon.rocks/articles/2024/2024-04-06-sentry-initialization-in-a-django-project.html

## The Problem

Initializing Sentry in `settings.py` (per official docs) means it catches errors everywhere - including the Django shell. This leads to noise from:
- `SyntaxError` from typos in shell
- `SystemExit` when exiting shell

## Entry Point Analysis

| Entry Point | Web Workers | Management Commands | Celery Workers | Scripts |
|-------------|-------------|---------------------|----------------|---------|
| settings.py | ✅ | ✅ | ✅ | ✅ |
| wsgi.py | ✅ | ❌ | ❌ | ❌ |
| manage.py | ❌ | ✅ | ❌ | ❌ |

No single entry point covers "web + celery but not shell."

## Solution: Conditional Initialization

Check the running command and skip Sentry for shell:

```python
import sys
import sentry_sdk

# Exclude shell commands from Sentry reporting
SHELL_COMMANDS = ["shell", "shell_plus", "dbshell"]

if sys.argv[1:2] and sys.argv[1] not in SHELL_COMMANDS:
    sentry_sdk.init(
        dsn="...",
        # other config
    )
```

The `sys.argv[1:2]` slice safely gets the command name without IndexError.

## Related Reading

- Adam Johnson: [How to Check the Running Django Command](https://adamj.eu/tech/)
