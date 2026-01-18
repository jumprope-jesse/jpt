# Django Reliable Signals

Source: https://hakibenita.com/django-reliable-signals

## The Problem

Django signals are useful for decoupling modules but have reliability issues:

1. **Circular dependencies** - Direct module references create import cycles
2. **Exception propagation** - Receiver errors can fail the sender
3. **Transaction coupling** - Signals sent inside transactions can:
   - Hold locks during slow receiver execution
   - Fail to notify receivers if sender rolls back
   - Execute receivers before data is committed (race conditions)

## Standard Solutions and Their Tradeoffs

### Polling/Scheduled Tasks
- Reliable but introduces delays
- Good for non-time-critical workflows
- Example: Django management command that queries for pending work

### send_robust()
- Doesn't propagate exceptions from receivers
- Still executes immediately (blocking)
- Still has transaction timing issues

### on_commit()
- Ensures signal sent only after transaction commits
- But if server crashes after commit, before signal send - signal is lost

## Reliable Signals with Django Tasks Framework

Django 6.0 introduces a Tasks Framework that enables reliable signal delivery using database-backed queues.

### Key Concept
1. Send signal inside database transaction
2. Enqueue a task for each receiver (stored in same transaction)
3. If sender rolls back, tasks roll back too
4. Worker processes execute tasks after sender commits
5. Failed tasks can be retried

### Implementation

```python
# reliable_signal/__init__.py
from django.dispatch import Signal as DjangoSignal
from django.dispatch.dispatcher import NO_RECEIVERS
from django_tasks import task
import importlib

def callable_to_qualname(f):
    """Return the <module>::<qualname> identifier of a function."""
    return f'{f.__module__}::{f.__qualname__}'

def qualname_to_callable(qualname):
    """Get a callable from its <module>::<qualname> identifier."""
    module_name, func_qualname = qualname.split('::', 1)
    module = importlib.import_module(module_name)
    obj = module
    for attr in func_qualname.split('.'):
        obj = getattr(obj, attr)
    return obj

@task()
def execute_task_signal_receiver(*, receiver_qualname: str, named: dict):
    receiver = qualname_to_callable(receiver_qualname)
    receiver(signal=None, sender=None, **named)

class Signal(DjangoSignal):
    def send_reliable(self, sender, **named):
        if not self.receivers:
            return
        if self.sender_receivers_cache.get(sender) is NO_RECEIVERS:
            return
        sync_receivers, async_receivers = self._live_receivers(sender)
        for receiver in sync_receivers:
            execute_task_signal_receiver.enqueue(
                receiver_qualname=callable_to_qualname(receiver),
                named=named,
            )
```

### Setup

```python
# settings.py
INSTALLED_APPS = [
    # ...
    'django_tasks',
    'django_tasks.backends.database',
]

TASKS = {
    "default": {
        "BACKEND": "django_tasks.backends.database.DatabaseBackend",
        "ENQUEUE_ON_COMMIT": False,
    }
}
```

Run worker: `./manage.py db_worker`

### Testing

Use `ImmediateBackend` for synchronous execution in tests:

```python
from django.test import TestCase, override_settings

@override_settings(TASKS={'default': {'BACKEND': 'django.tasks.backends.immediate.ImmediateBackend'}})
class OrderTestCase(TestCase):
    def test_order_happy_path(self):
        # Tasks execute immediately during tests
        pass
```

## Limitations

1. **Arguments must be JSON-serializable** - No complex objects
2. **Async receivers not supported** - sync_receivers only
3. **PostgreSQL required** - For database backend
4. **Worker process needed** - Additional infrastructure

## Signal Naming Best Practice

Name signals for what happened, not what should happen:
- Good: `payment_process_completed`
- Bad: `complete_order`

This keeps modules truly decoupled - senders shouldn't know how receivers use their signals.

## Related

- Django Tasks Framework: https://docs.djangoproject.com/en/6.0/topics/tasks/
- django-tasks: https://github.com/realsuayip/django-tasks
- Haki Benita's blog: https://hakibenita.com/
