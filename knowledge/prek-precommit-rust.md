# prek - Fast Pre-commit Alternative in Rust

## Overview
prek is a reimagined version of pre-commit, built in Rust. It's designed as a faster, dependency-free, drop-in replacement for pre-commit while providing additional features.

**Status**: Not production-ready yet, but already adopted by Airflow, PDM, basedpyright, OpenLineage, and Authlib.

## Key Features
- Single binary with no dependencies (no Python runtime required)
- ~10x faster than pre-commit, uses 1/3 of disk space
- Fully compatible with existing `.pre-commit-config.yaml` files
- Integrates with uv for Python virtual environments
- Shared toolchains between hooks (Python, Node.js, Go, Rust, Ruby)
- Built-in implementations of common hooks (faster than Python counterparts)
- Parallel repository cloning and hook installation

## Currently Supported Languages
- python, node, go, docker, docker-image, pygrep, system, script, fail

## Installation
```bash
# Standalone installer (can self-update)
# Check repo for latest install script

# Via Homebrew
brew install j178/tap/prek

# Via Cargo
cargo install prek

# Via PyPI
pip install prek

# Self-update
prek self update
```

## Migration from pre-commit
1. Install prek
2. Replace `pre-commit` with `prek` in your commands
3. Your existing `.pre-commit-config.yaml` works unchanged

```bash
# Same usage pattern
prek run
prek run <hook_id>
prek install
prek list  # Lists all hooks with descriptions
```

## Why Faster?
- Rust implementation
- Redesigned hook environment management - toolchains shared between hooks
- Parallel repository cloning and installation
- Uses uv for Python virtualenvs (inherits uv's speed)
- Built-in common hooks written in Rust

## Commands
```bash
prek run              # Run all hooks
prek run <hook_id>    # Run specific hook (with shell completion)
prek list             # List available hooks, IDs, and descriptions
prek install          # Install git hooks
prek self update      # Update prek itself
```

## Links
- GitHub: https://github.com/j178/prek

## Related
- uv: Used for Python virtualenv management
- pre-commit: The original tool this replaces
