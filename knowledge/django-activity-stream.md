# django-activity-stream

Activity feeds for Django - tracking user actions like "User X did Y to Z".

**Repo:** https://github.com/justquick/django-activity-stream
**Docs:** https://django-activity-stream.readthedocs.io/

## Use Cases

- Staff accessing recently-accessed objects
- Users seeing their recently-viewed items
- Activity feeds ("John commented on your post")
- Action history for any model

## vs django-auditlog

- **auditlog**: Compliance/debugging - what changed, when, by whom
- **activity-stream**: User-facing activity feeds - "User did action on object"

## Installation

```bash
pip install django-activity-stream[jsonfield]
```

```python
# settings.py
INSTALLED_APPS = [
    ...
    'actstream',
]

ACTSTREAM_SETTINGS = {
    "MANAGER": "actstream.managers.ActionManager",
    "FETCH_RELATIONS": True,
}
```

## Register Models

```python
# my_app/apps.py
from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = "my_app"

    def ready(self):
        from actstream import registry
        registry.register(self.get_model("MyModel"))
```

## Track Actions with Signals

```python
# my_app/signals.py
from actstream import action
from django.db.models.signals import post_save
from my_app.models import MyModel

def mymodel_handler(sender, instance, created, **kwargs):
    verb = "was added" if created else "was edited"
    action.send(instance, verb=verb)

post_save.connect(mymodel_handler, sender=MyModel)
```

Import signals in apps.py:

```python
# my_app/apps.py
def ready(self):
    import my_app.signals  # noqa
    from actstream import registry
    registry.register(self.get_model("MyModel"))
```

## Testing the Signal

```python
from unittest.mock import patch
from actstream import action
from my_app.models import MyModel

def test_mymodel_handler(db):
    with patch.object(action, "send") as mock_send:
        MyModel.objects.create(name="Test")
        mock_send.assert_called_once()
        _, kwargs = mock_send.call_args
        assert kwargs["verb"] == "was added"
```

## Notes

- URL routes optional - skip if you don't need public activity streams
- Settings may differ slightly from docs when using `[jsonfield]` option
- Actions stored with actor, verb, target pattern

Source: https://github.com/williln/til/blob/main/django/how_i_added_django_activity_stream_with_test.md
