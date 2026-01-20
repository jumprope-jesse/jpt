# Devbox - Isolated Development Environments

Devbox is a CLI tool from Jetify for creating isolated, reproducible development environments.

## What It Does

- Creates per-project shells with specific tool versions
- Uses Nix Package Registry (400k+ packages) under the hood but abstracts the complexity
- Defines environment in `devbox.json` - similar to package.json but for system-level tools
- No virtualization layer = fast file system and commands

## Key Benefits

- **Team consistency**: Everyone gets exact same tool versions via devbox.json
- **No conflicts**: Different projects can use different versions of same tool
- **Clean laptop**: Try tools without polluting system, remove when done
- **Portable**: Same definition works for local shell, devcontainer, Docker, cloud

## Quick Start

```bash
# Install
curl -fsSL https://get.jetify.com/devbox | bash

# In a project
devbox init
devbox add python@3.11 nodejs@20
devbox shell  # enter isolated environment
```

## How It Compares

- **vs Docker**: Faster for local dev (no virtualization), but can export to Dockerfile for prod
- **vs Homebrew/apt**: Isolated per-project, not global
- **vs asdf/mise**: Similar concept but uses Nix packages, more comprehensive
- **vs raw Nix**: Much simpler UX, same power

## Resources

- Repo: https://github.com/jetify-com/devbox
- Docs: https://www.jetify.com/devbox/docs/
- Discord: Jetify Discord has #devbox channel
