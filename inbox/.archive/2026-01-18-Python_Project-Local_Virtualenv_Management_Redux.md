---
type: link
source: notion
url: https://hynek.me/articles/python-virtualenv-redux/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-04-03T13:47:00.000Z
---

# Python Project-Local Virtualenv Management Redux

## AI Summary (from Notion)
- Project Overview: The document is an update on managing local virtual environments in Python projects, reflecting on advancements since the author's first entry on the topic.

- Key Tools:
- direnv: A tool for managing environment variables which executes a .envrc file upon entering a directory.
- uv: A newer tool that enhances the virtual environment creation process, faster than traditional methods like virtualenv.
- PDM: A package dependency manager that supports virtual environment management and is used for pinned applications.

- Virtual Environment Management:
- The author prefers to store project virtual environments in a directory called .venv.
- For unpinned packages, the author uses a .python-version-default file to manage Python versions.

- Cross-Platform Development: The author discusses the challenges of developing on an ARM Mac for Intel Linux and the need for cross-platform lock files, leading to the adoption of PDM.

- Bonus Tips:
- Fish shell function provided for recreating virtual environments quickly.
- Using GitHub Actions and GitLab CI for automated Python version management based on pyproject.toml.

- Philosophy: The author emphasizes minimizing the cognitive load by automating environment setup, advocating for tools that streamline development workflows.

- Historical Context: The document acknowledges the rapidly changing landscape of Python packaging and tools, suggesting that the information may evolve quickly.

## Content (from Notion)

One of my first TIL entries was about how you can imitate Node’s node_modules semantics in Python on UNIX-like operating systems. A lot has happened since then (to the better!) and it’s time for an update. direnv still rocks, though.

One major thing that happened to Python is uv (have you seen my video about it?) and another thing that “happened” to me is an ARM-based computer and my need to run Python both in Intel and ARM mode which somewhat complicated my life (see also How to Automatically Switch to Rosetta With Fish and Direnv).

I have also embraced the emerging standard of putting a project’s virtual environment into an in-project directory called .venv.

What hasn’t changed is my enthusiasm for direnv. Boardly speaking, direnv will execute a file called .envrc when you enter a directory. It’s a much more powerful version of venerable .env files (that it can load, too) and I really like it as glue between non-overbearing tools.

With Astral releasing uv and taking over Rye, I think it’s fair to say that Python packaging and project workflow tools have entered an exciting, transitional period. So, it’s unclear how well this post will age. But in the worst case, it will be a historical record once we’re all riding unicorns through the sky.

I’m not trying to be prescriptive and instead explain the context in which I’m building my workflows. It’s perfectly possible my workflows are a bad fit for you. But my core believe is that I shouldn’t have to remember anything because I forget everything all the time.

## Python Installations

Nowadays, I get as many binary Python installers directly from https://www.python.org/downloads/ as I can, because they’re universal2 builds with a special command that always runs in Intel mode (for example, python3.12-intel64) and that makes creating Intel-based virtual environments less error-prone. As Glyph said: Get Your Mac Python From Python.org.

I fill in the missing ones – that I need for my open-source projects – using one of the installers for Gregory Szorc’s python-build-standalone. They lag too much behind the official releases for production use, but they’re wonderful for driving tox and Nox.

On Linux, we use deadsnakes for everything.

I use different mechanisms to manage the virtual environments depending on whether I’m developing a package without strict pinning or an application with strict pinning.

## Unpinned Package

I’m aware that it makes sense to pin your development and test dependencies for a stable CI, too.

However, I don’t have a project with enough churn and dependency-caused breakage to avoid the sad look of a commit history consisting of 99% Dependabot updates.

To me, this is the pragmatic trade-off where I just pin or fix when I encounter problems.

While direnv has built-in support for the standard library’s venv module, it’s glacial. virtualenv is much faster, but uv is faster, still.

Unlike applications, my packages usually support more than one Python version. To have one canonical place to store the currently default development version of a package, I’ve started adding a .python-version-default file to my projects that contains the version I want to use.

Then, I add the following to the project’s .envrc:

```plain text
test -d .venv || uv venv --python $(cat .python-version-default)
source .venv/bin/activate

```

direnv ensures the virtual environment exists and is active whenever I enter the directory: test -d .venv checks if .venv is an existing directory and if not, it creates it using uv venv for whatever the version in .python-version-default is.

The nice thing is that I can use the same file in GitHub Actions as an input to setup-python:

```plain text
- uses: actions/setup-python@v5with:cache: pippython-version-file: .python-version-default
```

### Bonus Tip

Here’s a Fish shell function to recreate the virtual environment if needed:

```plain text
function ,repypkg
    rm -rf .tox .nox .venv
    # Ensure .venv exists
    direnv exec . python -m site
    uv pip install --editable .[dev]
end

```

Given how fast uv is, this is also the best way to update all dependencies. For structlog, it takes about 600ms with a hot cache.

Sidenote: I use direnv exec instead of direnv reload because the latter seems to run asynchronously and uv pip install fails with No such file or directory (os error 2).

## Pinned Application

Due to developing on an ARM Mac for Intel Linux, I need cross-platform lock files, which rules out the otherwise excellent pip-tools, as well as pip-tools-adjacent tools like Rye and uv.

Since I’ve had bad experiences with the alternatives, I’ve settled on PDM, which I’m generally very happy with.

PDM has support for virtual environment management built-in and I use it straight in my .envrc:

```plain text
eval $(pdm venv activate)

```

### Bonus Tip

We use GitLab CI to build our Python Docker containers, and I extract the correct Python version by configuring requires-python in the project’s pyproject.toml:

```plain text
[project]
name = "some-app"
requires-python = "~=3.12.0"

```

This way, I can extract that string in the CI configuration in .gitlab-ci.yml:

```plain text
# ...build:stage: buildonly: [main]script:- export PY=$(sed -nE 's/^requires-python = "~=(3\.[0-9]+)\.0"$/python\1/p' pyproject.toml)# PY is something like `python3.12` now,# and you can pass it as an ENV into `docker build`.
```

I could do the same operation in my .envrc, but why not extract the command line from .gitlab-ci.yml and eval it instead?

```plain text
eval "$(sed -nE 's/^.*- (export PY=.*)/\1/p' .gitlab-ci.yml)"

```

Now, I have a shell variable PY with a version like python3.12 based on metadata from pyproject.toml with no duplication. As a bonus, it also verifies that the version extraction in CI actually works.

Locally, I use that variable when I want to recreate the project’s virtual environment:

```plain text
rm -rf .venv
pdm venv create $(command -v $PY)
pdm use -i .venv/bin/python
pdm sync --dev

```

Check out TIL: which is not POSIX if you’re irritated by the command -v.


