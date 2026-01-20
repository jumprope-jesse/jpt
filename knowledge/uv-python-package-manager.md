# uv - Fast Python Package Manager

## Overview
uv is an extremely fast Python package installer and project manager written in Rust, developed by Astral (makers of ruff and ty). It streamlines Python installation, dependency management, and virtual environment handling.

## Key Benefits
- **Speed**: Significantly faster than pip/poetry/pipenv due to Rust implementation
- **Simplified management**: Handles Python installation, virtual environments, and dependencies in one tool
- **Consistent environments**: Ensures reproducible setups across machines and teams
- **uvx for one-off runs**: Run tools like Jupyter Lab or linters without permanent installation

## Quick Start
```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create a new project
uv init my-project
cd my-project

# Add dependencies
uv add requests pandas

# Run a script
uv run python script.py

# One-off tool execution (no install)
uvx ruff check .
uvx ty check
uvx jupyter lab
```

## Common Commands
```bash
# Create virtual environment
uv venv

# Install from requirements.txt
uv pip install -r requirements.txt

# Sync project dependencies
uv sync

# Add dev dependencies
uv add --dev pytest

# Lock dependencies
uv lock

# Pin Python version for project
uv python pin 3.12.9
```

## pyproject.toml Example
```toml
[project]
name = "my_project"
version = "1.0.0"
requires-python = ">=3.9,<3.13"
dependencies = [
  "astropy>=5.0.0",
  "pandas>=1.0.0,<2.0",
]
```

## uvx Examples (One-off Tool Execution)
```bash
# Quick IPython with pandas for data exploration
uvx --with pandas,pyarrow ipython

# Start Jupyter Lab without project setup
uvx jupyter lab

# Run ruff linter
uvx ruff check .
```

## Project Configuration
uv uses `pyproject.toml` for project configuration, compatible with PEP 517/518/621 standards.

## Links
- Documentation: https://docs.astral.sh/uv/
- Source: https://emily.space/posts/251023-uv

## Docker/Container Usage

Using uv in Dockerized Flask/Django apps can yield ~10x speed improvements over pip.

### Dockerfile Setup

```dockerfile
# Install uv binaries from official image
COPY --from=ghcr.io/astral-sh/uv:0.7.13 /uv /uvx /usr/local/bin/

# Copy dependency files (instead of requirements.txt)
COPY --chown=python:python pyproject.toml uv.lock* ./

# Environment variables
ENV UV_COMPILE_BYTECODE=1 \
    UV_PROJECT_ENVIRONMENT="/home/python/.local"
```

Key environment variables:
- `UV_COMPILE_BYTECODE=1` - Pre-compile Python bytecode for faster startup
- `UV_PROJECT_ENVIRONMENT` - Skip venv creation, install directly to specified path

### Install Script for Docker

```bash
#!/usr/bin/env bash
set -o errexit
set -o pipefail

# Ensure we always have an up to date lock file
if ! test -f uv.lock || ! uv lock --check 2>/dev/null; then
  uv lock
fi

# Use the existing lock file exactly as defined
uv sync --frozen --no-install-project
```

Flags explained:
- `--frozen` - Don't modify the lock file, use it exactly as-is
- `--no-install-project` - Skip installing your code as a package (typical for web apps)

### Migration from pip

1. Create `pyproject.toml` with your dependencies
2. Delete `requirements.txt`
3. Update Dockerfile to copy uv binaries and set env vars
4. Replace pip install commands with uv sync

### Useful Container Commands

```bash
# Lock dependencies (generates/updates uv.lock)
uv lock

# Check if lock file is up to date
uv lock --check

# Sync dependencies from lock file
uv sync --frozen

# Check for outdated packages
uv pip list --outdated
```

Source: https://nickjanetakis.com/blog/switching-pip-to-uv-in-a-dockerized-flask-or-django-app

## Juvio - Reproducible Jupyter Notebooks with uv

Juvio is a Jupyter kernel that brings uv's dependency management directly into notebooks, making them reproducible and Git-friendly.

### Key Features
- **Inline dependency management**: Dependencies tracked in the notebook itself (no separate requirements.txt)
- **Automatic environment setup**: Ephemeral environments created per notebook
- **Git-friendly format**: Uses jupytext-like format for cleaner diffs
- **PEP 723 compliant**: Follows Python inline dependency standards

### Installation
```bash
pip install juvio
jupyter labextension enable juvio-frontend
```

### Usage
In a Juvio notebook, install packages with:
```python
%juvio install pandas numpy matplotlib
```

Dependencies are tracked automatically, environments are reproducible, and notebooks stay Git-clean.

### Links
- Source: https://github.com/OKUA1/juvio

## Installing CLI Tools with uv

Use `uv tool install` to globally install Python CLI tools without managing virtual environments manually.

### pre-commit (Recommended Setup)

```bash
# Install pre-commit with uv acceleration plugin
uv tool install pre-commit --with pre-commit-uv

# Verify installation
pre-commit --version
# pre-commit 4.2.0 (pre-commit-uv=4.1.4, uv=0.7.2)

# Upgrade later
uv tool upgrade pre-commit
```

The `--with pre-commit-uv` flag adds a plugin that patches pre-commit to use uv for installing Python-based hooks, drastically speeding up hook installation.

### Other CLI Tools

```bash
# Install any Python CLI tool globally
uv tool install httpie
uv tool install black
uv tool install mypy

# Upgrade a tool
uv tool upgrade <tool-name>

# List installed tools
uv tool list
```

Tools are installed to `~/.local/bin` (or similar per platform).

Source: https://adamj.eu/tech/2025/05/07/pre-commit-install-uv/

## Checking for Outdated Packages

### With uv (preferred)
```bash
# List outdated packages in current environment
uv pip list --outdated
```

### With req-update-check (for requirements.txt)

For legacy projects still using requirements.txt, `req-update-check` shows update severity:

```bash
pip install req-update-check
req-update-check requirements.txt
```

Output shows major/minor/patch classification with links to changelogs:
```
requests: 2.28.0 -> 2.31.0 [minor]
    Pypi page: https://pypi.python.org/project/requests/
    Homepage: https://requests.readthedocs.io
    Changelog: https://requests.readthedocs.io/en/latest/community/updates/#release-history
```

Features:
- Update severity display (major/minor/patch)
- Package homepage and changelog links
- File caching for faster repeated checks
- Ignores pre-release versions

Source: https://github.com/ontherivt/req-update-check

## Django Projects with uv

uv works well for Django applications (as of v0.4.0+). Django apps aren't installable packages, so use the default `uv init` behavior.

### New Django Project

```bash
# Initialize project
uv init hello-django
cd hello-django

# Add Django
uv add django

# Create Django project structure
uv run django-admin startproject hello .

# Run dev server
uv run manage.py runserver
```

### Existing Django Project

```bash
cd existing-project
uv init .

# If pyproject.toml already exists, add [project] table manually:
# [project]
# name = "my-project"
# version = "0.1.0"
# requires-python = ">=3.12"
# dependencies = []

# Add dependencies
uv add django celery redis
uv sync
```

### Dev Dependencies

```bash
# Add test tools as dev deps
uv add --dev pytest pytest-django

# Run tests
uv run pytest

# Production install (skip dev deps)
uv sync --no-dev
```

### Avoiding `uv run` Repetition

**Option 1: Shell aliases**
```bash
alias uvr="uv run"
alias uvm="uv run python manage.py"
# Now: uvm runserver
```

**Option 2: Modify manage.py shebang**
```python
#!/usr/bin/env -S uv run
```
Then run directly: `./manage.py runserver`

### Testing Against Different Django Versions

```bash
# Check current version
uv run manage.py version
# 5.1

# Test with Django 4.x
uv run --with 'django<5' manage.py version
# 4.2.15

# Run tests against older Django
uv run --with 'django<5' pytest
```

Source: https://blog.pecar.me/uv-with-django

## Why uv Solves Python Packaging

The two main difficulties in Python packaging:

1. **Bootstrapping** - How do beginners even get started? python.org? Anaconda? System package manager?
2. **Activation** - Virtual environment lifecycle is confusing for newcomers

uv solves both:
- **No Python dependency**: Standalone binaries install on any OS without Python
- **`uv python` manages versions**: No need for pyenv, deadsnakes, or conda
- **`uv tool` manages CLI tools**: Replaces pipx/fades
- **`uv run` executes without activation**: No manual venv lifecycle

The answer to "how do I get started with Python" is now simply: **install uv**.

### uv vs Conda

While conda saved Python when installing packages on Windows was painful, the ecosystem has moved on:
- Most packages now publish precompiled wheels for all platforms
- pip/conda interoperability issues were never fully resolved
- Conda may now be an "advanced tool" rather than beginner recommendation

Source: https://dev.to/astrojuanlu/python-packaging-is-great-now-uv-is-all-you-need-4i2d (2024)

## Historical Context: Rye (uv's Predecessor)

Before uv, Armin Ronacher created **Rye** as a "Cargo for Python" experiment. Rye bundled:
- pyenv-like Python version management
- pip-like dependency management
- pipx-like isolated tool installations
- Automatic virtual environment creation

**Why Rye was superseded by uv:**
- Relied on static Python builds, causing pain with C extensions (e.g., uWSGI)
- Custom toolchain registration was buggy
- Couldn't fully replace pyenv for projects needing compiled extensions
- Early-stage with rough edges

uv addressed these issues with better architecture and Astral's resources. If you see Rye mentioned in older articles, just use uv instead.

Source: https://burakku.com/blog/rye-test-and-python-tools/ (April 2024)

## direnv Integration for Automatic Virtual Environments

Use direnv to automatically activate project virtual environments when entering directories. This removes the cognitive load of remembering to activate venvs.

### Setup for Unpinned Packages

For packages that support multiple Python versions, create a `.python-version-default` file:

```bash
# .python-version-default
3.12
```

Then add to `.envrc`:
```bash
test -d .venv || uv venv --python $(cat .python-version-default)
source .venv/bin/activate
```

This creates the venv if missing and activates it on directory entry.

### GitHub Actions Integration

Use the same version file in CI:
```yaml
- uses: actions/setup-python@v5
  with:
    cache: pip
    python-version-file: .python-version-default
```

### Quick Venv Recreation (Fish shell)

```fish
function ,repypkg
    rm -rf .tox .nox .venv
    # Ensure .venv exists
    direnv exec . python -m site
    uv pip install --editable .[dev]
end
```

With uv's speed, full recreation with hot cache takes ~600ms.

### Setup for Pinned Applications (PDM)

For apps needing cross-platform lock files, PDM works well with direnv:

```bash
# .envrc
eval $(pdm venv activate)
```

### Extracting Python Version from pyproject.toml

For CI systems, extract `requires-python` to avoid version duplication:

```toml
# pyproject.toml
[project]
requires-python = "~=3.12.0"
```

```bash
# In GitLab CI
export PY=$(sed -nE 's/^requires-python = "~=(3\.[0-9]+)\.0"$/python\1/p' pyproject.toml)
```

### Getting Python Binaries

- **macOS**: Use python.org universal2 builds - they include `python3.12-intel64` for Intel mode
- **Linux**: Use deadsnakes PPA
- **Gap filling**: Gregory Szorc's python-build-standalone for tox/Nox runners

Source: https://hynek.me/articles/python-virtualenv-redux/

## macOS Python Installation Best Practices

### Why python.org is Best for macOS

The official python.org builds are recommended for most macOS users:

1. **Universal2 binaries**: Work on both Intel and Apple Silicon, unlike Homebrew/pyenv builds
2. **Framework builds**: Include macOS-specific features for GUI apps, scripting, etc.
3. **Core team expertise**: CPython maintainers know the build options best
4. **No surprise upgrades**: Unlike Homebrew which may upgrade Python during any `brew` operation

### Auto-Update with mopup

python.org builds don't auto-update for security patches. Use `mopup` to fix this:

```bash
pip install mopup
# Then periodically run:
mopup
# Installs security updates with just an admin password prompt
```

### Enforce Virtual Environments

Prevent accidental global pip installs by adding to `~/.pip/pip.conf`:

```ini
[install]
require-virtualenv = true
```

### What NOT to Use

| Option | Problem |
|--------|---------|
| **Homebrew Python** | Single-arch builds, may upgrade unexpectedly on any brew operation |
| **pyenv** | Single-arch, no Framework builds (breaks macOS app features) |
| **/usr/bin/python3** | Just a shim to Xcode tools, not a real Python—upgrades tied to Xcode |
| **Conda** | Overkill unless you need cross-platform team consistency; pip/wheels now cover most data science needs |

**Bottom line**: For most macOS dev work, use python.org + mopup + uv.

Source: https://blog.glyph.im/2023/08/get-your-mac-python-from-python-dot-org.html (Glyph Lefkowitz, Twisted creator)

## Related Tools
- **ruff**: Fast Python linter (also from Astral)
- **ty**: Fast Python type checker (also from Astral)
- **prek**: Fast pre-commit alternative (uses uv for Python envs)
- **juvio**: uv-powered Jupyter kernel for reproducible notebooks
- **direnv**: Auto-loads .envrc files on directory entry, pairs well with uv
- **mopup**: Auto-update python.org installations with security patches
