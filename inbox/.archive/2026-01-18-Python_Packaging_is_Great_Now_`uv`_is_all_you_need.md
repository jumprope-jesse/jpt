---
type: link
source: notion
url: https://dev.to/astrojuanlu/python-packaging-is-great-now-uv-is-all-you-need-4i2d
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-08-18T08:30:00.000Z
---

# Python Packaging is Great Now: `uv` is all you need - DEV Community

## AI Summary (from Notion)
- Overview of Python Packaging: The article discusses the evolution of Python packaging, highlighting improvements over the last eight years.

- Main Challenges: Identified difficulties for beginners:
- Bootstrapping: Getting started with Python installations.
- Activation: Understanding virtual environments (venvs).

- Introduction of uv:
- Released on February 15th, 2024, uv simplifies dependency management and project setup.
- It is a comprehensive package manager that does not depend on Python itself.

- Key Features of uv:
- Manages Python versions without needing OS-specific tools.
- Centralizes tool management, reducing the need for tools like pipx.
- Simplifies project initialization and dependency addition.
- Creates lock files for dependencies and can generate requirements.txt.

- Example Workflow:
- Demonstrates creating a project and adding dependencies using uv commands.

- Reflections on Virtual Environments:
- The author agrees with the idea that Python may move away from traditional activation methods used in virtual environments.

- Comparison with Conda:
- Discusses the benefits of uv over Conda and suggests that Conda may be less relevant for beginners in 2024.

- Conclusion:
- Highlights uv as a promising tool for Python packaging, addressing several longstanding issues and improving user experience.
- The author expresses strong support for using uv moving forward.

## Content (from Notion)

Cover image for Python Packaging is Great Now: `uv` is all you need

The title of this post is a reference to Glyph's Python Packaging is Good Now. I think it's safe to say that, in these 8 years, we've gone from "Good" to "Great". Keep reading for my reasoning.

## What makes Python packaging hard for beginners?

I contend that the two main difficulties for Python packaging are

- Bootstrapping, i.e. how to even get started!
- Activation, i.e. how venvs in Python work.
Bootstrapping was an often neglected problem. Should we tell people to install Python from https://python.org? The Anaconda distribution? How do we stop folks from using their system package manager and risk breaking everything?

And don't forget the whole virtual environment lifecycle. It's so crazy how numb I've become to it as a long time Python user, but every time I have to explain it I see my students faces and I think "this is not okay".

Sure, there are other problems, like how to build and publish distributable packages. But I contend these don't affect most Python beginners. Plus, they are in the process of being addressed as well. Read on.

## Enter uv

On February 15th, Astral released uv and I jumped ship immediately. As part of my job I routinely have to install lots of potentially conflicting dependencies, and uv was an immediate relief.

But the interesting thing is that now uv has gone well beyond its initial "faster pip" phase and it's fulfilling its promise of being "a comprehensive Python project and package manager that's fast, reliable, and easy to use".

Going back to the bootstrapping and activation problems that I mentioned at the very beginning, how does uv solve them? Consider this:

- uv does not depend on Python itself. Precompiled, standalone binaries can be easily installed on Linux, macOS and Windows.
- uv python manages Python versions! No need to resort to OS-specific mechanisms, like pyenv, deadsnakes, or to heavyweight tools like conda.
- uv tool manages tools in centralized environments! No more need for pipx or fades.
- uv init creates a barebones pyproject.toml using hatchling as build backend and a working src-layout with an empty README and a dummy module. 
- uv add adds dependencies to pyproject.toml, creates a venv if one didn't exist, and installs them!
- uv lock creates a lock file with all your dependencies, which you can then use in uv sync. 
- uv run executes scripts and commands, again without explicitly activating environments!
Essentially, this:

```plain text
$ mkdir uv-playground
$ cd uv-playground
$ uv init
warning: `uv init` is experimental and may change without warning
Initialized project `uv-playground`
$ uv add click
warning: `uv add` is experimental and may change without warning
Using Python 3.12.3 interpreter at: /usr/bin/python3
Creating virtualenv at: .venv
Resolved 3 packages in 66ms
   Built uv-playground @ file:///tmp/uv-playground
Prepared 2 packages in 430ms
Installed 2 packages in 0.62ms
 + click==8.1.7
 + uv-playground==0.1.0 (from file:///tmp/uv-playground)
$ tree
.
├── pyproject.toml
├── README.md
├── src
│   └── uv_playground
│       ├── __init__.py
└── uv.lock

3 directories, 4 files
$ uv run python -c "from uv_playground import hello; print(hello())"
warning: `uv run` is experimental and may change without warning
Hello from uv-playground!

```

Therefore, to the question "how do I get started learning Python on my computer", now you can universally respond: "install uv".

## Some reflections

On the topic of virtual environments, I essentially agree with Armin when he says

> 

I also notice that uv init chose hatchling. I always had a slight preference towards PDM, but I think this might be a point of no return.

It took Leah and contributors a lot of work to come up with this decision diagram for the PyOpenSci packaging guide. But the fact that now there's a baseline that folks can change in case they have more specific needs (for example, a Meson or scikit-build capable build backend) again provides for a much better Developer Experience.

## On conda

The topic of conda vs pip is another common source of confusion. I was a conda user and fan since day 1, and it effectively saved Python from a very clear death at a time when it was very difficult to just install stuff on Windows.

In the years that followed, I often referred to the old blog post by Jake VanderPlas explaining the differences, but it looks like a lost cause by now.

The interoperability problems between pip and conda were never fully addressed, and while I think the Pixi folks are doing a fantastic job, I think in the long run uv will win.

I fully acknowledge that conda packages are better structured around the notion of non-Python code, and that the current world of "fat wheels on PyPI" is clearly a suboptimal solution. But the whole ecosystem has moved in that direction: most packages now publish precompiled wheels for a rich variety of platforms.

In other words: conda might not be as useful in 2024 as it was in 2014, and it might be time to stop teaching it to beginners and deem it an advanced tool.

## Conclusion

The reason it's a bit too early is that some of these uv commands are still experimental and might evolve in the future. But for the first time ever, I clearly see a workflow tool that is standards-compliant, comprehensive, free of bootstrapping problems, carefully designed, and that can win.

Which is what many Python packaging critics wanted all along, right? Not having to choose from many different tools. But I think uv went well beyond that and solved other Developer Experience issues, for which I'm happy and thankful.

I am effectively using uv for everything and I am not looking back. I will continue recommending this tool to everyone, continue talking about it, and hope that it becomes more widespread.


