# Django Introspection for Enforcing Conventions

Source: https://lukeplant.me.uk/blog/posts/enforcing-conventions-in-django-projects-with-introspection/

Use Python introspection + Django's system checks framework to automatically enforce naming conventions.

## Example: DateField vs DateTimeField Naming

Problem: Inconsistent naming causes confusion (datetime is a subclass of date, so misuse isn't immediately obvious).

Convention:
- `DateTimeField` → names end with `_at` (e.g., `expires_at`, `deleted_at`)
- `DateField` → names end with `_on` or `_date` (e.g., `issued_on`, `birth_date`)

Based on English grammar: "on the 25th March" vs "at 7:00 pm"

## Implementation

```python
from django.apps import apps
from django.conf import settings
from django.core.checks import Tags, Warning, register


@register()
def check_date_fields(app_configs, **kwargs):
    exceptions = [
        # Django's AbstractBaseUser provides this, we can't change it
        "accounts.User.last_login",
    ]
    from django.db.models import DateField, DateTimeField

    errors = []
    for field in get_first_party_fields():
        field_name = field.name
        model = field.model

        if f"{model._meta.app_label}.{model.__name__}.{field_name}" in exceptions:
            continue

        # Order matters: DateTimeField inherits from DateField
        if isinstance(field, DateTimeField):
            if not field_name.endswith("_at"):
                errors.append(
                    Warning(
                        f"{model.__name__}.{field_name} field expected to end with `_at`, "
                        + "or be added to the exceptions in this check.",
                        obj=field,
                        id="conventions.E001",
                    )
                )
        elif isinstance(field, DateField):
            if not (field_name.endswith("_date") or field_name.endswith("_on")):
                errors.append(
                    Warning(
                        f"{model.__name__}.{field_name} field expected to end with `_date` or `_on`, "
                        + "or be added to the exceptions in this check.",
                        obj=field,
                        id="conventions.E002",
                    )
                )
    return errors


def get_first_party_fields():
    for app_config in get_first_party_apps():
        for model in app_config.get_models():
            yield from model._meta.get_fields()


def get_first_party_apps():
    return [app_config for app_config in apps.get_app_configs()
            if is_first_party_app(app_config)]


def is_first_party_app(app_config) -> bool:
    if app_config.module.__name__ in settings.FIRST_PARTY_APPS:
        return True
    app_config_class = app_config.__class__
    if f"{app_config_class.__module__}.{app_config_class.__name__}" in settings.FIRST_PARTY_APPS:
        return True
    return False
```

## Key Introspection APIs

- `apps.get_app_configs()` - Get all registered Django apps
- `app_config.get_models()` - Get all models in an app
- `model._meta.get_fields()` - Get all fields on a model
- `isinstance(field, FieldClass)` - Check field type

## Design Principles

1. **Include exceptions mechanism** - Some things are out of your control (e.g., Django's built-in fields)
2. **Document exceptions in code** - Comment why each exception exists
3. **Mention exceptions in warnings** - Tell developers how to add justified exceptions
4. **Filter to first-party apps** - Don't check third-party code you can't change

## Output

```
System check identified some issues:

WARNINGS:
myapp.MyModel.created: (conventions.E001) MyModel.created field expected to end with `_at`,
or be added to the exceptions in this check.

System check identified 1 issue (0 silenced).
```

## Other Applications

This pattern works for enforcing any convention you can introspect:
- Field naming patterns
- Model structure requirements
- Permission naming
- URL patterns
- Any code convention that can be checked programmatically

Better than documentation because it's automated and runs on every `manage.py check`.
