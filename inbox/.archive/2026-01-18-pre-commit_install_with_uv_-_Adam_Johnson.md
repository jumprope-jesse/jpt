---
type: link
source: notion
url: https://adamj.eu/tech/2025/05/07/pre-commit-install-uv/?utm_campaign=Django%2BNewsletter&utm_medium=rss&utm_source=Django_Newsletter_284
notion_type: Software Repo
tags: ['Running']
created: 2025-05-09T10:51:00.000Z
---

# pre-commit: install with uv - Adam Johnson

## Overview (from Notion)
- The article discusses the installation of pre-commit, a tool that automates tasks in Git, which can save you time and reduce errors in your coding workflow.
- Utilizing tools like uv for managing Python environments can streamline your development process, allowing you to focus more on building products and less on setup.
- The emphasis on collaboration and community in software development highlights the importance of sharing knowledge and tools with others, which can foster innovation.
- The author’s personal touch and informal tone might resonate with the challenges of balancing work and family, making tech more approachable.
- Consider the implications of using automation tools: they can enhance productivity but also require staying updated with best practices and managing dependencies effectively.
- Alternate views could include skepticism about over-reliance on tools, emphasizing the importance of understanding the underlying processes and not losing sight of foundational skills.
- The call to commit early and often can be a metaphor for both work and personal life — embracing regular progress in projects and relationships.

## AI Summary (from Notion)
Install pre-commit using the uv tool for easier management of Python environments. Follow the command $ uv tool install pre-commit --with pre-commit-uv for installation and $ uv tool upgrade pre-commit for upgrades. This setup simplifies the process of using Python-based hooks in Git.

## Content (from Notion)

A bird with a pre-commit-hook-shaped beak.

pre-commit is my favourite Git-integrated “run things on commit” tool. It acts as a kind of package manager, installing tools as necessary from their Git repositories. This makes it fairly easy to set up: all you need to install is pre-commit itself, and it takes things from there.

That said, pre-commit’s install guide is not the friendliest, particularly to developers who don’t use Python. The guide only covers installation with Python’s default installer tool, Pip, and the rather unconventional zipapp alternative. Both of these methods are a bit annoying as they require a working Python installation and virtual environment, entailing manual upgrades of those tools too.

Enter uv (pronounced “uhv”), a new Python environment manager. Since its release last year, it has made the Pythonsphere go wild, seeing massive adoption. That’s because it simplifies a lot of workflows, including managing development tools like pre-commit. Once you have uv, it can manage Python versions and virtual environments for you, swiftly and smoothly.

I now recommend you install pre-commit using uv’s tool mechanism, using this command:

```plain text
$ uv tool install pre-commit --with pre-commit-uv

```

Running it, you’ll see output describing the installation process:

```plain text
$ uv tool install pre-commit --with pre-commit-uv
Resolved 11 packages in 1ms
Installed 11 packages in 8ms
...
Installed 1 executable: pre-commit

```

This will put the pre-commit executable in ~/.local/bin or similar (per the documentation). You should then be able to run it from anywhere:

```plain text
$ pre-commit --version
pre-commit 4.2.0 (pre-commit-uv=4.1.4, uv=0.7.2)

```

The install command also adds pre-commit-uv, a plugin that patches pre-commit to use uv to install Python-based tools. This drastically speeds up using Python-based hooks, a common use case. (Unfortunately, it seems pre-commit itself won’t be adding uv support.)

With pre-commit installed globally, you can now install its Git hook in relevant repositories per usual:

```plain text
$ cd myrepo

$ pre-commit install
pre-commit installed at .git/hooks/pre-commit

```

```plain text
$ pre-commit run --all-files
[INFO] Installing environment for https://github.com/pre-commit/pre-commit-hooks.
[INFO] Once installed this environment will be reused.
[INFO] This may take a few minutes...
[INFO] Using pre-commit with uv 0.7.2 via pre-commit-uv 4.1.4
check for added large files..............................................Passed
check for merge conflicts................................................Passed
trim trailing whitespace.................................................Passed

```

## Upgrade pre-commit

To upgrade pre-commit installed this way, run:

```plain text
$ uv tool upgrade pre-commit

```

For example:

```plain text
$ uv tool upgrade pre-commit
Updated pre-commit v4.1.0 -> v4.2.0
 - pre-commit==4.1.0
 + pre-commit==4.2.0
Installed 1 executable: pre-commit

```

This command upgrades pre-commit and all of its dependencies, in its managed environment. For more information, see the uv tool upgrade documentation.

## Fin

May you commit early and often,

—Adam

Learn more about pre-commit in my Git DX book.

Subscribe via RSS, Twitter, Mastodon, or email:

Your email address:

One summary email a week, no spam, I pinky promise.

Related posts:

- Python: my new uv setup for development
- pre-commit: Block files based on name with a custom “fail” hook
- Git: How to skip hooks

