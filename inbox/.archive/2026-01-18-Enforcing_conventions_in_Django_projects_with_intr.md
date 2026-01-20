---
type: link
source: notion
url: https://lukeplant.me.uk/blog/posts/enforcing-conventions-in-django-projects-with-introspection/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-04-03T02:22:00.000Z
---

# Enforcing conventions in Django projects with introspection - lukeplant.me.uk

## Overview (from Notion)
- Naming conventions in software projects can significantly reduce maintenance overhead, which is crucial when juggling family and work.
- Introspection in Python allows for automated checks, potentially saving time and reducing errors—important for a busy life.
- The proposed naming convention (e.g., _at for timestamps) reflects English grammar, making it intuitive and easier to remember—helpful when balancing multiple responsibilities.
- Encourages a culture of consistency in coding, which can lead to better teamwork and less confusion, essential for leading a company.
- An alternative viewpoint may be to prioritize flexibility over strict conventions, allowing for creative solutions but risking inconsistency.
- This approach can also spark conversations about work-life balance, as clear structures in code can lead to clearer structures in managing family and work commitments.

## AI Summary (from Notion)
Naming conventions in Django projects can reduce maintenance issues. Using Python's introspection capabilities, the post discusses enforcing naming conventions for DateField and DateTimeField to avoid confusion. It suggests specific suffixes for field names and outlines tools like Django's system checks framework to automate these checks, ultimately promoting better coding practices and reducing errors.

## Content (from Notion)

Naming conventions can make a big difference to the maintenance issues in software projects. This post is about how we can use the great introspection capabilities in Python to help enforce naming conventions in Django projects.

Contents

- The problem: DateField and DateTimeField confusion
-  
- The solution
- Output
- Conclusion
Let’s start with an example problem and the naming convention we’re going to use to solve it. There are many other applications of the techniques here, but it helps to have something concrete.

## The problem: DateField and DateTimeField confusion

Over several projects I’ve found that inconsistent or bad naming of DateField and DateTimeField fields can cause various problems.

First, poor naming means that you can confuse them for each other, and this can easily trip you up. In Python, datetime is a subclass of date, so if you use a field called created_date assuming it holds a date when it actually holds a datetime, it might be not obvious initially that you are mishandling the value, but you’ll often have subtle problems down the line.

Second, sometimes you have a field named like expired which is actually the timestamp of when the record expired, but it could easily be confused for a boolean field.

Third, not having a strong convention, or having multiple conventions, leads to unnecessary time wasted on decisions that could have been made once.

Finally, inconsistency in naming is just confusing and ugly for developers, and often for users further down the line, because names tend to leak.

Even if you do have an established convention, it’s possible for people not to know. It’s also very easy for people to change a field’s type between date and datetime without also changing the name. So merely having the convention is not enough, it needs to be enforced.

Note 
If you want to change the name and type of a field (or any other atribute), and want the data to preserve data as much as possible, you usually need to do it in two stages or more depending on your needs, and always check the migrations created – otherwise Django’s migration framework will just see one field removed and a completely different one added, and generate migrations that will destroy your data.

For this specific example, the convention I quite like is:

- field names should end with _at for timestamp fields that use DateTimeField, like expires_at or deleted_at.
- field names should end with _on or _date for fields that use DateField, like issued_on or birth_date.
This is based on the English grammar rule that we use “on” for dates but “at” for times – “on the 25th March”, but “at 7:00 pm” – and conveniently it also needs very few letters and tends to read well in code. The _date suffix is also helpful in various contexts where _on seems very unnatural. You might want different conventions, of course.

To get our convention to be enforced with automated checks we need a few tools.

## The tools

### Introspection

Introspection means the ability to use code to inspect code, and typically we’re talking about doing this when our code is already running, from within the same program and using the same programming language.

In Python, this starts from simple things like isintance() and type() to check the type of an object, to things like hasattr() to check for the presence of attributes and many other more advanced techniques, including the inspect module and many of the metaprogramming dunder methods.

### Django app and model introspection

Django is just Python, so you can use all normal Python introspection techniques. In addition, there is a formally documented and supported set of functions and methods for introspecting Django apps and models, such as the apps module and the Model _meta API.

### Django checks framework

The third main tool we’re going to use in this solution is Django’s system checks framework, which allows us to run certain kinds of checks, at both “warning” and “error” level. This is the least important tool, and we could in fact switch it out for something else like a unit test.

## The solution

It’s easiest to present the code, and then discuss it:

```plain text
from django.apps import apps
from django.conf import settings
from django.core.checks import Tags, Warning, register


@register()
def check_date_fields(app_configs, **kwargs):
    exceptions = [
        # This field is provided by Django's AbstractBaseUser, we don't control it
        # and we’ll break things if we change it:
        "accounts.User.last_login",
    ]
    from django.db.models import DateField, DateTimeField

    errors = []
    for field in get_first_party_fields():
        field_name = field.name
        model = field.model

        if f"{model._meta.app_label}.{model.__name__}.{field_name}" in exceptions:
            continue

        # Order of checks here is important, because DateTimeField inherits from DateField

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


def get_first_party_apps() -> list[AppConfig]:
    return [app_config for app_config in apps.get_app_configs() if is_first_party_app(app_config)]


def is_first_party_app(app_config: AppConfig) -> bool:
    if app_config.module.__name__ in settings.FIRST_PARTY_APPS:
        return True
    app_config_class = app_config.__class__
    if f"{app_config_class.__module__}.{app_config_class.__name__}" in settings.FIRST_PARTY_APPS:
        return True
    return False

```

We start here with some imports and registration, as documented in the “System checks” docs. You’ll need to place this code somewhere that will be loaded when your application is loaded.

Our checking function defines some allowed exceptions, because there are some things out of our control, or there might be other reasons. It also mentions the exceptions mechanism in the warning message. You might want a different mechanism here, but I think having some way of dealing with exceptions, and advertising its existence in the warnings, is often pretty important. Otherwise, you can end up with worse consequences when people just slavishly follow rules. Notice how in the exception list above I’ve given a comment detailing why the exception is there though – this helps to establish a precedent that exceptions should be justified, and the justification should be there in the code.

We then loop through all “first party” model fields, looking for DateTimeField and DateField instances. This is done using our get_first_party_fields() utility, which is defined in terms of get_first_party_apps(), which in turn depends on:

- the get_app_configs() function.
- the AppConfig.get_models() method
- the _meta get_fields() method
-   
The id values passed to Warning here are examples – you should change according to your needs. You might also choose to use Error instead of Warning.

## Output

When you run manage.py check, you’ll then get output like:

```plain text
 System check identified some issues:

 WARNINGS:
 myapp.MyModel.created: (conventions.E001) MyModel.created field expected to end with `_at`,
 or be added to the exceptions in this check.

 System check identified 1 issue (0 silenced).

```

As mentioned, you might instead want to run this kind of check as a unit test.

## Conclusion

There are many variations on this technique that can be used to great effect in Django or other Python projects. Very often you will be able to play around with a REPL to do the introspection you need.

Where it is possible, I find doing this far more effective than attempting to document things and relying on people reading and remembering those docs. Every time I’m tripped up by bad names, or when good names or a strong convention could have helped me, I try to think about how I could push people towards a good convention automatically – while also giving a thought to unintended bad consequences of doing that prematurely or too forcefully.

## You may also like: §


