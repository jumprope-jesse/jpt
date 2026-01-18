---
type: link
source: notion
url: https://github.com/ludo-technologies/pyscn
notion_type: Software Repo
tags: ['Running']
created: 2025-10-05T18:25:00.000Z
---

# GitHub - ludo-technologies/pyscn: pyscn - An Intelligent Python Code Quality Analyzer

## Overview (from Notion)
- pyscn can simplify your code quality management, helping you maintain clean, efficient code as your startup grows.
- The CFG-based dead code detection feature can save time by identifying unreachable code, enhancing productivity during busy development cycles.
- Integration with CI/CD pipelines allows for continuous quality checks, ensuring your team adheres to best practices without slowing down development.
- The tool's ability to analyze cyclomatic complexity can help you break down complex functions, making your codebase easier to manage and understand, especially valuable when juggling family and work.
- The minimalist design and ease of use align with a busy lifestyle, allowing you to focus on what really matters—building your company while keeping your codebase healthy.
- Consider the balance between automation and hands-on coding; while tools like pyscn are invaluable, they should complement, not replace, your coding intuition.
- Embracing such tools can foster a culture of quality within your team, reflecting your commitment to excellence in both your personal and professional life.

## AI Summary (from Notion)
pyscn is a Python code quality analyzer that performs structural analysis to maintain codebases. It features dead code detection, clone detection, coupling metrics, and cyclomatic complexity analysis. Users can run analyses with commands like pyscn analyze for comprehensive reports or pyscn check for quick quality checks. Installation can be done via pipx or by building from source, and it supports CI/CD integration for automated quality checks.

## Content (from Notion)

# pyscn - Python Code Quality Analyzer

## pyscn is a code quality analyzer for Python vibe coders.

Building with Cursor, Claude, or ChatGPT? pyscn performs structural analysis to keep your codebase maintainable.

## Quick Start

```plain text
# Run analysis without installation
uvx pyscn analyze .
# or
pipx run pyscn analyze .
```

## Demo

## Features

- 🔍 CFG-based dead code detection – Find unreachable code after exhaustive if-elif-else chains
- 📋 Clone detection with APTED + LSH – Identify refactoring opportunities with tree edit distance
- 🔗 Coupling metrics (CBO) – Track architecture quality and module dependencies
- 📊 Cyclomatic complexity analysis – Spot functions that need breaking down
100,000+ lines/sec • Built with Go + tree-sitter

## Common Commands

### pyscn analyze

Run comprehensive analysis with HTML report

```plain text
pyscn analyze .                              # All analyses with HTML report
pyscn analyze --json .                       # Generate JSON report
pyscn analyze --select complexity .          # Only complexity analysis
pyscn analyze --select deps .                # Only dependency analysis
pyscn analyze --select complexity,deps,deadcode . # Multiple analyses
```

### pyscn check

Fast CI-friendly quality gate

```plain text
pyscn check .                      # Quick pass/fail check
pyscn check --max-complexity 15 .  # Custom thresholds
```

### pyscn init

Create configuration file

```plain text
pyscn init                         # Generate .pyscn.toml
```

> 

## Configuration

Create a .pyscn.toml file or add [tool.pyscn] to your pyproject.toml:

```plain text
# .pyscn.toml
[complexity]
max_complexity = 15

[dead_code]
min_severity = "warning"

[output]
directory = "reports"
```

> 

## Installation

```plain text
# Install with pipx (recommended)
pipx install pyscn

# Or run directly with uvx
uvx pyscn
```

## CI/CD Integration

```plain text
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

## Documentation

📚 Development Guide • Architecture • Testing

## License

MIT License — see LICENSE

Built with ❤️ using Go and tree-sitter


