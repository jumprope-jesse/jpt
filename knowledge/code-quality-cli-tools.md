# Code Quality CLI Tools

Command-line tools for linting, formatting, security scanning, and maintaining code quality across multiple languages.

---

## Qlty CLI

**URL:** https://github.com/qltysh/qlty
**Type:** CLI (Rust-based)
**License:** Fair Source (BSL 1.1, transitions to open source)
**Added:** 2026-01-18

### Overview

Qlty CLI is a universal code quality tool that aggregates 70+ static analysis tools across 40+ languages into a single unified interface. It handles linting, auto-formatting, maintainability metrics, and security scanning.

### Key Features

- **Universal Linting** - Support for 70+ linters across 40+ languages via plugins
- **Auto-Formatting** - Unified formatting commands across all languages
- **Security Scanning** - Identifies vulnerabilities and security issues
- **Maintainability Metrics** - Code quality metrics for C#, Go, Java, JavaScript, Kotlin, PHP, Python, Ruby, Rust, TypeScript
- **Simple Configuration** - Single `.qlty/qlty.toml` config file, auto-generated based on languages detected
- **Git Integration** - Works with Git workflows for commit/push-time checks

### Installation

```bash
# macOS/Linux
curl https://qlty.sh | bash

# Windows
powershell -c "iwr https://qlty.sh | iex"

# Docker
# Also available on GHCR (runs natively, not via Docker)
```

### Usage

```bash
# Initialize in a repo
cd my_repo/
qlty init

# Run linting
qlty check

# Auto-format
qlty fmt

# Enable a plugin
qlty plugins enable <NAME>
```

### Ecosystem

Part of the broader Qlty Software platform:
- **Qlty CLI** - The command-line tool
- **Qlty Cloud** - Automated code review and quality trends
- **VS Code Extension** - IDE integration
- **GitHub Action** - CI workflow integration
- **Browser Extensions** - Adds coverage data to GitHub.com

### Why It's Interesting

- **Polyglot teams** - One tool to rule all languages instead of configuring eslint, black, rustfmt, etc. separately
- **Written in Rust** - Fast native performance, runs linters natively (not via Docker)
- **Free for all use** - No limits on contributors, works for commercial projects
- **Plugin architecture** - Easy to extend with new linters via TOML definitions

### Considerations

- Fair Source license (BSL 1.1) means it's not fully open source initially
- Adding yet another meta-linter to the toolchain has overhead
- May not have all the customization options of individual tools
- Requires initial setup time to configure properly

### See Also

- Compare with: pre-commit, trunk.io, MegaLinter, super-linter

---

## Trunk Check

**URL:** https://trunk.io
**Type:** CLI + Cloud Platform
**Added:** 2026-01-19

### Overview

Trunk Check is a meta-linter that runs multiple code quality tools with a focus on incremental adoption for existing codebases. It implements "Hold the Line" - running linters only on changed code to avoid overwhelming teams with legacy issues.

### Key Adoption Strategies

**The Challenge:** Teams avoid linters because:
- Enabling tools on old codebases creates overwhelming backlogs
- Disabling all errors loses visibility into code quality
- Code formatters mess up git-blame history
- Stopping development to fix everything is impractical

**Hold the Line Solution:**
- Linters run only on new changes, not old code
- Works at individual line level, not just file level
- Allows gradual improvement without eating the elephant all at once
- Consistent across all wrapped tools

### Git Blame Preservation

When running formatters across entire codebase, use `.git-blame-ignore-revs`:

```bash
# Reformat codebase
trunk fmt --all
git commit -m 'reformat code'

# Get commit hash
HASH=$(git log -1 --format="%H")

# Add to ignore file
echo "$HASH" >> .git-blame-ignore-revs
git add .git-blame-ignore-revs
git commit -m 'add git blame ignore file'

# Configure git to always use it
git config blame.ignoreRevsFile .git-blame-ignore-revs
```

Trunk Check automatically adds this config. GitHub also respects `.git-blame-ignore-revs`.

### Incremental Rollout Patterns

For existing codebases:

1. **Partial Scope** - Run on subset of codebase (UI only, changed files only)
   - Problem: Changing one line means fixing entire file

2. **Downgrade Severity** - Treat errors as warnings initially
   - Problem: Must remember to increase strictness later

3. **Development Freeze** - Stop and fix everything
   - Problem: High cost, no forward progress

4. **Hold the Line** (Recommended) - Only check new code
   - Gradual improvement over time
   - Technical debt addressed when touching files anyway
   - No blocking of current development

### Why It's Interesting

- **Solves adoption barrier** - Teams can start with messy codebases
- **One consistent interface** - Manage settings for all tools in one place
- **Line-level precision** - More granular than file-level checking
- **Git-aware** - Built-in support for preserving code history

### Use Cases

- Converting CoffeeScript to TypeScript incrementally
- Adding TypeScript types to React JS code line-by-line
- Introducing linters to legacy projects
- Enforcing consistency across multi-repo organizations

### Considerations

- Another layer of abstraction over underlying tools
- May not expose all options of wrapped linters
- Commercial offering with free tier

---

## deptry

**URL:** https://github.com/fpgmaas/deptry
**Type:** CLI (Python + Rust)
**License:** Open Source
**Added:** 2026-01-19

### Overview

deptry is a Python dependency checker that finds unused, missing, or transitive dependencies in Python projects. As of v0.14.0 (March 2024), it uses Rust for parsing ASTs and extracting imports, delivering significant performance improvements for large projects.

### Key Features

- **Dependency Analysis** - Detects unused dependencies, missing dependencies, and transitive dependencies
- **Fast Performance** - Rust-based AST parsing for speed (major improvement in v0.14.0)
- **Multi-Platform** - ABI3 wheels for Linux (x86_64, aarch64), macOS (x86_64, Apple Silicon), Windows (x64)
- **Configurable** - Supports pyproject.toml configuration
- **CI-Friendly** - Designed for pre-commit hooks and CI pipelines

### Installation

```bash
pip install deptry
# or
pipx install deptry
```

### Usage

```bash
# Check dependencies in current project
deptry .

# Check specific directory
deptry src/

# With configuration
deptry --config pyproject.toml .
```

### v0.14.0 Improvements (March 2024)

- **Speed boost** - Rust replaces Python for AST parsing
- **Better error reporting** - More verbose messages with source file/line when files can't be read
- **Improved accuracy** - Column identifiers now point to correct positions in import statements
- **Cross-platform wheels** - Pre-built binaries for major platforms instead of single wheel

### Why It's Interesting

- **Clean dependencies** - Helps maintain lean requirements.txt/pyproject.toml files
- **Catches transitive deps** - Finds when you're importing packages you didn't explicitly declare
- **Performance** - Rust internals make it fast enough for large monorepos
- **Pre-commit integration** - Run before commits to prevent dependency drift

### Use Cases

- Finding and removing unused dependencies before deployment
- Validating Docker image builds have correct dependencies
- Cleaning up legacy projects with bloated requirements files
- CI/CD gates to enforce clean dependency management

### Related Tools

- **pipdeptree** - Visualizes dependency trees
- **pip-audit** - Security vulnerability scanning
- **poetry** - Dependency management with lock files
- **pip-tools** - Compile requirements from .in files
