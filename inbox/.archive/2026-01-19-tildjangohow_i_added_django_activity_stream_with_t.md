---
type: link
source: notion
url: https://github.com/williln/til/blob/main/django/how_i_added_django_activity_stream_with_test.md
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-03-29T12:37:00.000Z
---

# til/django/how_i_added_django_activity_stream_with_test.md at main · williln/til · GitHub

## AI Summary (from Notion)
- Project Overview: The document outlines the setup of django-activity-stream for tracking actions in an ecommerce site.
- Use Cases:
- Helps staff access recently-accessed objects.
- Allows customers to view recently-viewed items.
- Installation Steps:
- Install django-activity-stream[jsonfield].
- Add actstream to INSTALLED_APPS.
- Configure ACTSTREAM_SETTINGS in settings.py.
- Model Registration:
- Models need to be registered for tracking; done in apps.py.
- Signal Setup:
- A signal is created to track model changes (post_save).
- This signal sends an action whenever a MyModel object is created or edited.
- Testing:
- A simple pytest-style test is provided to verify that the signal works as intended, ensuring that the action is called correctly.
- Interesting Fact: The document highlights the flexibility in settings for django-activity-stream that may differ from the documentation based on options used.

## Content (from Notion)

# How I set up django-activity-stream, including a simple test

## Links

- django-activity-stream Documentation
- django-activity-stream on GitHub
## Notes

My use case is an ecommerce site. I'll be using django-activity-stream to help me:

- Help staff access their most-recently-accessed objects
- Help customers see their recently-viewed items
## Installation and Setup

1. Install django-activity-stream[jsonfield] (I went ahead and included the jsonfield option as I'll be using it later)
1. Add actstream to INSTALLED_APPS
1. I already had a SITE_ID
1. I did not add the URLs because I don't currently want a publicly-available stream
1. Add the activity stream settings (note: these were a little different than the docs. I'm not sure if that is because I used [jsonfield], or another reason. These settings are what worked for me with no errors.)
```plain text
# settings.py
ACTSTREAM_SETTINGS = {
    "MANAGER": "actstream.managers.ActionManager",
    "FETCH_RELATIONS": True,
}
```

## Register models with django-activity-stream

You have to register the models that you will want to track.

In the app that contained the model(s) I wanted to track, I opened apps.py:

```plain text
# my_app/apps.py
from __future__ import annotations
from django.apps import AppConfig

class MyAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "my_objects"

    def ready(self):
        # django-activity-stream stuff
        from actstream import registry
        # Add this line to register the model with django-activity-stream
        registry.register(self.get_model("MyModel"))
```

Now the model is registered with django-activity-stream

## Use django-activity-stream to track model changes

See Generating Actions in the docs for more info.

I chose to set up a simple signal as a proof-of-concept.

1. Create my_app/signals.py:
```plain text
# my_app/signals.py
from __future__ import annotations

from actstream import action
from django.db.models.signals import post_save

from my_app.models import MyModel


def mymodel_handler(sender, instance, created, **kwargs):
    if created:
        verb = "was added"
    else:
        verb = "was edited"
    action.send(instance, verb=verb)


post_save.connect(mymodel_handler, sender=MyModel)
```

1. Import the signals in the app config:
```plain text
# my_app/apps.py
class MyAppConfig(AppConfig):
    def ready(self):
        # Add this line
        import my_app.signals # noqa

        from actstream import registry
        registry.register(self.get_model("MyModel"))
```

Now, any time a MyModel object is created or edited, a signal will fire. That signal will call action.send() to create a record of that action using django-activity-stream.

## Test the signal

Example pytest-style test:

```plain text
from __future__ import annotations

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

There are probably other ways to test this as well.


