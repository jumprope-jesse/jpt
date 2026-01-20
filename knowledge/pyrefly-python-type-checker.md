# Pyrefly - Fast Python Type Checker & LSP

## Overview
Pyrefly is a fast Python type checker and language server from Facebook/Meta, designed for large codebase performance and rich IDE features. Currently in alpha.

## Quick Start
```bash
# Install from PyPI (Python 3.8+)
pip install pyrefly

# Run type checking
pyrefly check

# Check specific file
pyrefly check myfile.py
```

## Key Features
- **Speed at scale**: Multi-threaded type checking, aggressive incremental updates
- **LSP support**: Autocomplete, hover, go-to definition, diagnostics
- **Modern typing**: Broad PEP coverage, generics, protocols
- **CLI workflow**: Simple `pyrefly check` for CI usage

## Typical Use Cases
- **Local dev**: Run LSP in editor for instant feedback
- **CI pipelines**: Enforce typing in PRs with fast checks
- **Large repos**: Benefit from parallelism and incremental caching

## Integration Strategy
1. **Shadow run first**: Add non-blocking CI job on a subset
2. **Directory opt-in**: Start strict mode on a few apps, expand as issues decline
3. **Allowlist approach**: Include list of packages/modules, move to default-on later
4. **Keep old checker**: Retain mypy/pyright for A/B comparison during trial

## Links
- Website: https://pyrefly.org
- GitHub: https://github.com/facebook/pyrefly
- PyPI: https://pypi.org/project/pyrefly

## Related Tools
- **ty**: Fast type checker from Astral (Rust-based)
- **mypy**: Traditional Python type checker
- **pyright**: Microsoft's Python type checker
