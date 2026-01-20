---
type: link
source: notion
url: https://nickjanetakis.com/blog/switching-pip-to-uv-in-a-dockerized-flask-or-django-app
notion_type: Tech Deep Dive
tags: ['Running']
created: 2025-06-24T12:19:00.000Z
---

# Switching pip to uv in a Dockerized Flask / Django App — Nick Janetakis

## Overview (from Notion)
- Switching to uv can significantly improve the efficiency of your Flask or Django applications, potentially freeing up more time for family or personal pursuits.
- The approach reduces the complexity of managing dependencies with a simplified pyproject.toml, allowing for easier project management.
- Emphasizes the importance of running applications as a non-root user, enhancing security—a vital consideration for any software engineer or business founder.
- The use of cutting-edge tools like uv, which is built on Rust, reflects a trend toward performance optimization that can keep your skills relevant in a competitive tech landscape.
- It showcases a shift from traditional Python dependency management (like requirements.txt) to a more modern, tree-structured approach, highlighting the evolution of software development practices.
- Consider the sustainability aspect: uv promotes efficient use of resources, which aligns with a growing interest in eco-friendly practices in tech.
- Alternate view: While uv offers speed and efficiency, it might introduce a learning curve or complexity that could be daunting for some developers accustomed to traditional methods.
- The insights shared also resonate with the startup culture in NYC, where innovation and efficiency are crucial for managing fast-paced business growth.

## AI Summary (from Notion)
Switching from pip to uv in Dockerized Flask or Django apps can lead to significant performance improvements. Key steps include creating a pyproject.toml for dependencies, installing uv binaries, setting environment variables, and using uv commands for dependency management. The process emphasizes avoiding virtual environments and running as a non-root user, with scripts provided for installation and management of dependencies.

## Content (from Notion)

## I noticed about a 10x speed up across a number of projects, we'll avoid using a venv and run things as a non-root user too.

Prefer video? Here is it on YouTube.

I was surprised at how painless it was to switch things over. You can see the git diffs to make the change for both of my example Flask and Django projects. In this post we’ll go into more detail about these changes and how to use a few uv commands.

Let’s start with defining our project’s dependencies.

You can create a pyproject.toml file and delete your requirements.txt after you’ve entered your project’s dependencies and their versions into pyproject.toml.

You only need to add your top level dependencies, uv will make a lock file for you automatically which is somewhat comparable to what pip freeze would produce except uv’s lock file has proper dependency trees and is way better.

Here’s a very small diff that shows an example of what to do, adjust it as needed:

```plain text
# pyproject.toml
+[project]
+dependencies = [
+  "redis==5.2.1",
+]
# requirements.txt
-redis==5.2.1

```

It’s important that these steps happen in order. For example you’ll want the environment variables defined before you install your dependencies.

### Install uv

```plain text
+COPY --from=ghcr.io/astral-sh/uv:0.7.13 /uv /uvx /usr/local/bin/

```

- Ensure both uv and uvx binaries are installed on your system’s path
### Dependency Files

```plain text
-COPY --chown=python:python requirements*.txt ./
+COPY --chown=python:python pyproject.toml uv.lock* ./

```

- Reference uv’s dependency related files instead
### Environment Variables

```plain text
+ENV \
+  UV_COMPILE_BYTECODE=1 \
+  UV_PROJECT_ENVIRONMENT="/home/python/.local" \

```

- UV_COMPILE_BYTECODE
- UV_PROJECT_ENVIRONMENT instructs uv to not make a virtual environment (venv)
### Dependency Install Commands

```plain text
-RUN chmod 0755 bin/* && bin/pip3-install
+RUN chmod 0755 bin/* && bin/uv-install

```

In both cases I extracted their install commands to a separate script so it’s easy to either run at build time in the Dockerfile (as seen above), or by running it as a command at run-time to make sure your lock file gets updated on your host machine through a volume.

In any case, both solutions are just shell scripts. Here’s the one for uv with comments:

```plain text
#!/usr/bin/env bash
set -o errexit
set -o pipefail
# Ensure we always have an up to date lock file.
if ! test -f uv.lock || ! uv lock --check 2>/dev/null; then
  uv lock
fi
# Use the existing lock file exactly how it is defined.
uv sync --frozen --no-install-project

```

There’s a few ways to use uv, such as using its pip sub-command but I like using sync since it’s the “uv way” of doing things. The pip sub-command is there to help create a mental model of how uv works, or continue using pip’s commands through uv if you prefer.

The --frozen flag ensures the lock file doesn’t get updated. That’s exactly what we want because we expect the lock file to have a complete list of exact versions we want to use for all dependencies that get installed.

The --no-install-project flag skips installing your code as a Python package. Since we have a pyproject.toml with a project defined the default behavior is to install it as a package.

For a typical web app, you usually have your project’s dependencies and that’s it. Your project isn’t an installable project in itself. However, if you do have that use case feel free to remove this flag! You can think of this as using --editable . with pip.

If you’re using my example starter app, it comes with a few run script shortcuts. They’re shortcut shell scripts to run certain commands in a container:

- ./run deps:install
- ./run deps:install --no-build
- ./run uv [...]
- ./run uv:outdated
The video below goes over the diffs together and runs some of the above commands.

- 0:17 – TL;DR on uv
- 1:36 – pyproject.toml to replace requirements.txt
- 3:05 – Dockerfile: install uv
- 3:56 – Dockerfile: dependency files
- 4:50 – Dockerfile: env vars
- 6:46 – Dockerfile: uv lock / sync
- 10:22 – Quick recap
- 10:44 – One way to update a package
- 11:41 – Checking for outdated packages
- 13:29 – Using uv add to add or update packages
- 15:27 – Adding a new package at its latest version
- 16:12 – Removing a package
Did you switch to uv, how did it go? Let me know below.


