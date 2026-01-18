# ty - Fast Python Type Checker

## Overview
ty is an extremely fast Python type checker written in Rust, developed by Astral (makers of uv and ruff).

## Quick Start
```bash
# Run with uvx (no installation needed)
uvx ty check

# Check specific file
uvx ty check example.py
```

## Key Features
- Written in Rust for performance
- Auto-discovers virtual environments via `VIRTUAL_ENV` or `.venv` in project root
- Works with `pyproject.toml` projects automatically
- Online playground available for testing

## Virtual Environment Discovery
ty automatically finds installed packages in:
1. Active virtual environment (via `VIRTUAL_ENV` env var)
2. `.venv` directory in project root or working directory

For non-virtual environments, use `--python` flag to specify the target path.

## Common Issues
- If you get a cascade of errors with `venv` module, add the venv directory to `.gitignore` or `.ignore`

## Links
- Documentation: https://docs.astral.sh/ty/
- Part of Astral ecosystem (uv, ruff)

## Related Tools
- **uv**: Fast Python package installer and resolver (also from Astral)
- **ruff**: Fast Python linter (also from Astral)
- **mypy**: Traditional Python type checker
- **pyright**: Microsoft's Python type checker
