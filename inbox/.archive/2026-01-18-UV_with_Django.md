---
type: link
source: notion
url: https://blog.pecar.me/uv-with-django
notion_type: Software Repo
tags: ['Running']
created: 2024-09-15T21:55:00.000Z
---

# UV with Django

## Overview (from Notion)
- Tech Adoption: Embracing tools like uv can streamline your development process, allowing more time for family and personal interests.
- Django Projects: Building or maintaining Django applications can enhance your skills, making you more competitive in the tech landscape of NYC.
- Community Engagement: The Python community's collaboration and innovation can inspire you to connect with other developers or even mentor aspiring engineers.
- Work-Life Balance: Using efficient tools means less time troubleshooting and more time for family activities, a crucial aspect of parenthood.
- Sustainable Practices: Consider how the eco-friendly aspects of new technology align with family values and the environment for future generations.
- Continuous Learning: Engaging with evolving tech like uv keeps your skills fresh and relevant, essential in a fast-paced industry.
- Alternate Views: Some may argue that relying on new tools can complicate development instead of simplifying it; weigh the pros and cons based on your specific needs and projects.

## AI Summary (from Notion)
The uv package manager, recently updated to version 0.4.0, simplifies project management for Python, including Django applications. It allows users to create new projects, manage dependencies, and install development tools easily. Users can initialize a project, add Django, and run commands with simplified aliases. Additionally, it supports switching between package versions for testing, making it a valuable tool for Python developers.

## Content (from Notion)

Astral made a huge summer splash in the Python community last week when they released uv 0.3.0.

## What is uv?

uv is a Python package manager written in rust that has just gained the ability to be a project management tool (like Pipenv/PDM), tool management (pipx), python installer (pyenv), and more!

I was very eager to try it out on my Django projects, but the init rial 0.3.0 release was designed for managing installable Python packages, so there were a few rough edges when using it to manage Django app dependencies. Only a week later, these issues have been addressed, defaults were switched around, and uv 0.4.0 now supports Python projects like your Django application out of the box!

## Using uv to create a new Django project

First, we’ll need to get uv. See the official docs for all the installation options, but the easiest way to get it on Linux and MacOS is to run:

```plain text
curl -LsSf https://astral.sh/uv/install.sh | sh

```

Now that we have uv, we can use it to start a new project with:

```plain text
❯ uv init hello-django
Initialized project `hello-django` at `/Users/anze/Coding/hello-Django`

```

Make sure you are using uv 0.4.0 or newer; older versions will presume you are creating an installable Python package, and you'll see "error: Failed to prepare distributions" errors when trying to run your project. You can upgrade your uv version by running the install command above.

You can now cd into the hello-django folder and see that uv created three files for us:

```plain text
README.md
hello.py # we won't need this so feel free to rm it.
pyproject.toml

```

The pyproject.toml file is the most interesting one since it defines two important properties: requires-python and dependencies. The former defines which Python version we will be using, and the latter defines the project dependencies.

```plain text
[project]
name = "hello-django"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.12"dependencies = []

```

Our Django projects won’t really care about the name, version, description, and readme properties, so just leave them as is.

Speaking of project dependencies. It’s about time we install Django with uv add django!

```plain text
❯ uv add django
Using Python 3.12.5
Creating virtualenv at: .venv
Resolved 5 packages in 186ms
Prepared 3 packages in 3ms
Installed 3 packages in 235ms
 + asgiref==3.8.1
 + django==5.1
 + sqlparse==0.5.1

```

We can see that uv created a virtual environment (.venv folder), and installed Django with its two dependencies (asgiref and sqlparse). If we inspect the pyproject.toml file, we can see that Django was added to the dependencies list:

```plain text
...
dependencies = [
    "django>=5.1",]

```

The Django version has no upper bonds, so we can easily upgrade it when newer versions of Django come out (using uv lock --upgrade).

This doesn’t mean our current dependencies aren’t locked tight. Our whole dependency tree has its versions specified in the uv.lock file. The lock file is a cross-platform lock file, so it should be safe to install on any operating system!

Now that we have Django installed, we can run Django’s startproject command:

```plain text
uv run django-admin startproject hello .

```

This initialized our Django project, including the manage.py file, hello/settings.py, etc.

We can start the Django development server with the following:

```plain text
uv run manage.py runserver

```

## Using uv with an existing Django project

If you already have a Django project, you can still use the uv init command to switch to uv.

```plain text
cd to_existing_project
❯ uv init .
Initialized project `hello-django` at `/Users/anze/Coding/blog/hello-django`

```

If your project already has a pyproject.toml file defined the command might fail with:

```plain text
error: Project is already initialized in `/Users/anze/Coding/blog/hello-django`

```

In that case, you’ll need to add a project table to your pyproject.toml file:

```plain text
[project]
name = "hello-django"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.12"dependencies = []

```

And now, you should be able to add your existing dependencies to the pyproject.toml, either manually or with the uv add command. After all the dependencies are specified in pyproject.toml you can run uv sync to make sure everything is installed in your environment.

## Installing dev dependencies

uv also supports installing development dependencies:

```plain text
❯ uv add --dev pytest pytest-django
Resolved 11 packages in 8ms
Prepared 5 packages in 0.91ms
Installed 5 packages in 12ms
 + iniconfig==2.0.0
 + packaging==24.1
 + pluggy==1.5.0
 + pytest==8.3.2
 + pytest-django==4.8.0

```

You can now run your tests with

```plain text
uv run pytest

```

The dev dependencies are saved in the tool.uv.dev-dependencies list in your pyproject.toml:

```plain text
[tool.uv]
dev-dependencies = [
    "pytest>=8.3.2",    "pytest-django>=4.8.0",]

```

When deploying your Django application to production, you can avoid installing dev dependencies by running:

```plain text
❯ uv sync --no-dev
Resolved 11 packages in 2ms
Uninstalled 5 packages in 35ms
 - iniconfig==2.0.0
 - packaging==24.1
 - pluggy==1.5.0
 - pytest==8.3.2
 - pytest-django==4.8.0

```

## Avoiding uv run

Writing uv run gets very old very fast, but there are a few options to make the experience a bit nicer.

### 1. Aliases

You can alias uv run to something shorter like uvr:

```plain text
alias uvr="uv run"

```

Or for Django use cases, you can define uvm like so:

```plain text
alias uvm="uv run python manage.py"

```

So that you can run the manage.py file with only three letters:

```plain text
uvm runserver

```

### 2. Adjusting the shebang line in manage.py

You can change the #!/usr/bin/env python at the top of manage.py into #!/usr/bin/env -S uv run to force invocations to use uv run.

```plain text
./manage.py runserver

```

I learned about this trick from Jeff Triplett’s blog Python UV run with shebangs. 💚

## Using uv run --with

uv run has another trick up its sleeve: an optional --with parameter that allows you to run your project with a different package version. This is super useful if you want to quickly verify if your project works with a newer (or older) version of Django:

```plain text
❯ uv run python manage.py version
5.1
❯ uv run --with 'django<5' manage.py version
4.2.15
❯ uv run --with 'django<5' pytest # to run your tests on the latest 4.x version

```

## Fin

This is a really exciting time for Python and Python packaging! If you want to learn more about uv check out the following links:

- The official documentation
- Simon Willison wrote some notes on uv
- Jeff Triplet also wrote about the uv updates
If you have any other tricks or ideas to simplify your Django workflows, let me know, and I’ll add your suggestions to the blog post!


