---
type: link
source: notion
url: https://pypi.org/project/django-fastdev/
notion_type: Software Repo
tags: ['Running']
created: 2024-03-24T04:55:00.000Z
---

# django-fastdev · PyPI

## AI Summary (from Notion)
- Project Title: django-fastdev
- Purpose: Enhances the development experience for Django apps by providing better error handling and faster startup.
- Creation Date: March 24, 2024
- Status: Not started
- Key Features:
- Improves error messages for non-existent template variables.
- Provides clearer feedback for NoReverseMatch errors in URL routing.
- Flags non-space text outside blocks when extending templates.
- Identifies invalid block names in template inheritance.
- Enhances error messages for reverse URL lookups and QuerySet.get() calls.
- Validates clean_* methods in forms to catch spelling errors.
- Reduces runserver startup time by moving initial model checks to a separate thread.
- Installation: Can be installed via pip and requires adding to INSTALLED_APPS in settings.py.
- License: BSD License
- Author: Anders Hovmöller

## Content (from Notion)

### Navigation

-  Project description 
-  Release history 
-  Download files 
### Project links

### Statistics

View statistics for this project via Libraries.io, or by using our public dataset on Google BigQuery

### Meta

License: BSD License (BSD)

Author: Anders Hovmöller

Tags  django

### Classifiers

- Development Status 
- Intended Audience 
- License 
- Natural Language 
- Programming Language 
## Project description

django-fastdev is an app that makes it faster and more fun to develop Django apps.

## Features

### Error on non-existent template variables

Django templates by default hide errors, and when it does show an error it’s often not very helpful. This app will change this so that if you do:

```plain text
{{ does_not_exist }}
```

instead of rendering that as an empty string, this app will give you an error message:

```plain text
does_not_exist does not exist in context. Available top level variables:

    DEFAULT_MESSAGE_LEVELS
    False
    None
    True
    bar
    csrf_token
    foo
    messages
    perms
    request
    user
```

There are more specialized error messages for when you try to access the contents of a dict, and attributes of an object a few levels deep like foo.bar.baz (where baz doesn’t exist).

By default, django-fastdev only checks templates that exist within your project directory. If you want it to check ALL templates, including stock django templates and templates from third party libraries, add FASTDEV_STRICT_TEMPLATE_CHECKING = True to your project settings.py.

### NoReverseMatch errors

Have you ever gotten this error?

```plain text
django.urls.exceptions.NoReverseMatch: Reverse for 'view-name' with arguments '('',)' not found. 1 pattern(s) tried:
```

It’s because you have {% url 'view-name' does_not_exist %}. Django sees does_not_exist and evaluates it to the empty string because it doesn’t exist. So that’s why you get an error message that makes no sense. django-fastdev will make your code crash on the actual error: does_not_exist doesn’t exist.

### Error if you have non-space text outside a block when extending

A common mistake for beginners that can be hard to spot is when they do:

```plain text
<html>
    {% extends "something.html" %}
    stuff here
</html>
```

Django silently throws away stuff here and </html>. django-fastdev makes this an error.

### Error on invalid block names when using {% extends "..." %}

If you have a base template:

```plain text
<html>
    <body>
        {% block content %}{% endblock %}
    </body>
</html>
```

and then write a template like this:

```plain text
{% extends "base.html" %}

{% block contents %}
    hello!
{% endblock %}
```

Django will silently throw away hello! because you wrote contents instead of content. django-fastdev will turn this into an error which lists the invalid and valid block names in alphabetical order.

### Better error messages for reverse

The standard error message for a bad reverse()/{% url %} are rather sparse. django-fastdev improves them by listing valid patterns so you can easily see the problem.

### Better error messages for QuerySet.get()

The error message for QuerySet.get() is improved to give you the query parameters that resulted in the exception.

### Validate clean_* methods

A common mistake is to make a form clean method and make a spelling error. By default Django just won’t call the function. With django-fastdev you will get an error message telling you that your clean method doesn’t match anything.

This is also very useful during refactoring. Renaming a field is a lot safer as if you forget to rename the clean method django-fastdev will tell you!

### Faster startup

The initial model checks can be quite slow on big projects. django-fastdev will move these checks to a separate thread, so the runserver startup time is lowered, so you don’t have to wait for the runserver restart as long.

## Usage

First install: pip install django-fastdev

In settings.py add django_fastdev to INSTALLED_APPS:

```plain text
 INSTALLED_APPS = [     # ...     'django_fastdev',]
```

Enjoy a nicer Django experience!

## License

BSD


