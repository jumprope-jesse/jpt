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

## Related Tools
- **ruff**: Fast Python linter (also from Astral)
- **ty**: Fast Python type checker (also from Astral)
