# CodeWeaver - Codebase to Markdown Docs

*Source: https://tesserato.web.app/posts/2025-02-12-CodeWeaver-launch/ - Added: 2026-01-18*

CLI tool that generates a single Markdown document from a codebase. Useful for sharing codebases with AI/ML tools or collaborators.

## Install

```bash
go install github.com/tesserato/CodeWeaver@latest
```

## Usage

```bash
# Document current directory
codeweaver

# Specify input/output
codeweaver -dir=my_project -output=project_docs.md

# Ignore patterns (regex, comma-separated)
codeweaver -ignore="\.log,temp,build,node_modules" -output=code_overview.md

# Track what's included/excluded
codeweaver -ignore="node_modules" -included-paths-file=included.txt -excluded-paths-file=excluded.txt
```

## What It Does

- Recursively scans directory structure
- Creates tree-like hierarchy in Markdown
- Embeds file contents in syntax-highlighted code blocks
- Flexible regex-based ignore patterns (defaults to ignoring `.git.*`)

## Use Cases

- Share codebase context with AI coding assistants
- Generate project documentation
- Code review preparation
- Onboarding documentation

GitHub: https://github.com/tesserato/CodeWeaver
