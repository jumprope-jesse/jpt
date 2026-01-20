# pyscn - Python Code Quality Analyzer

## Overview
pyscn is a structural code quality analyzer for Python, particularly useful for AI-assisted "vibe coding" with tools like Cursor, Claude, or ChatGPT. It performs deep structural analysis to keep codebases maintainable.

Built with Go + tree-sitter for speed (100,000+ lines/sec).

## Quick Start
```bash
# Run without installation
uvx pyscn analyze .
pipx run pyscn analyze .

# Install
pipx install pyscn
```

## Key Features
- **CFG-based dead code detection** - Find unreachable code after exhaustive if-elif-else chains
- **Clone detection with APTED + LSH** - Identify refactoring opportunities using tree edit distance
- **Coupling metrics (CBO)** - Track architecture quality and module dependencies
- **Cyclomatic complexity analysis** - Spot functions that need breaking down

## Common Commands
```bash
# Comprehensive analysis with HTML report
pyscn analyze .
pyscn analyze --json .
pyscn analyze --select complexity .
pyscn analyze --select complexity,deps,deadcode .

# Fast CI quality gate
pyscn check .
pyscn check --max-complexity 15 .

# Create config
pyscn init
```

## Configuration
Create `.pyscn.toml` or add `[tool.pyscn]` to `pyproject.toml`:
```toml
[complexity]
max_complexity = 15

[dead_code]
min_severity = "warning"

[output]
directory = "reports"
```

## CI/CD Integration
```yaml
# .github/workflows/code-quality.yml
name: Code Quality
on: [push, pull_request]

jobs:
  quality-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install pyscn
      - name: Quick quality check
        run: pyscn check .
      - name: Generate detailed report
        run: pyscn analyze --json --select complexity,deadcode,deps src/
      - name: Upload report
        uses: actions/upload-artifact@v4
        with:
          name: code-quality-report
          path: .pyscn/reports/
```

## Related Tools
- **ty**: Fast Python type checker (Astral)
- **ruff**: Fast Python linter (Astral)
- **radon**: Python complexity metrics
- **vulture**: Dead code finder (simpler than pyscn)

## Links
- GitHub: https://github.com/ludo-technologies/pyscn
