---
type: link
source: notion
url: https://github.com/smithclay/claudetainer
notion_type: Software Repo
tags: ['Running']
created: 2025-08-18T00:35:00.000Z
---

# GitHub - smithclay/claudetainer: Opinionated developer workflows for using Claude Code anywhere—even your phone

## Overview (from Notion)
- Claudetainer offers a streamlined way to code from anywhere, including mobile, which can help you balance work with family life by allowing flexibility in your schedule.
- The auto-configured environment means you can quickly set up projects, saving time that can be spent with your kids or on personal pursuits.
- Its integration with tools like Docker and mobile-friendly features enable efficient remote work, which can be especially useful in a fast-paced city like New York.
- The emphasis on community and sharing configurations through GitHub can enhance collaboration with your team, making it easier to manage projects while nurturing a supportive work culture.
- Unique aspects include specialized sub-agents for coding without a keyboard, which could revolutionize how you approach coding tasks when multitasking or on the go.
- Consider alternate views on the reliance on mobile coding—while it offers flexibility, it may blur the lines between work and personal life, potentially impacting family time if not managed carefully.

## AI Summary (from Notion)
Claudetainer is a tool that enables mobile-friendly coding with auto-configured Claude Code in an isolated Docker container. It supports multiple programming languages, offers instant setup, and allows coding from anywhere with features like SSH access, push notifications, and specialized sub-agents for enhanced productivity. Installation is straightforward, and it includes essential commands for project management and remote development.

## Content (from Notion)

# claudetainer 📦 🤖

> 

Claude Code automatically configured with a persistent shell session, hooks, slash commands, and specialized sub-agents designed for coding without a keyboard. Everything runs in an isolated Docker container.

## Quick Start (Recommended)

Get up and running in under 2 minutes on Linux, macOS or WSL:

```plain text
# 1. Add the tap and install
brew tap smithclay/tap
brew install claudetainer

cd ~/your-project

# 2. Initialize your project with a language preset (go, node, python, rust)
claudetainer init python

# 3. Start the container
claudetainer up

# 4. Connect to the container full tooling and terminal multiplexer (default password is: vscode)
claudetainer ssh

# 5. (Inside the ssh session) Start Claude Code: all hooks and slash commands automatically load in a nice zellij UI.
claude
```

You now have a fully configured Claude Code development environment with specialized sub-agents, automated quality control, slash commands, and team workflows.

## Why Claudetainer?

- 🚀 Instant Setup - Auto-detects your language (Python, Node.js, Go, Rust, Shell) and configures everything
- 📱 Code Anywhere - SSH + terminal multiplexer designed for mobile coding (yes, even from your iPhone)
- 🔧 Smart Tooling - Claude Code with specialized sub-agents, automatic quality control, and useful tools like ccusage and gitui
- 📬 Stay Connected - Push notifications so you know when Claude needs attention
- 🏗️ Team Ready - Share configurations via GitHub repos
## Requirements

- Docker - For container isolation
- DevContainer CLI - npm install -g @devcontainers/cli
- git - For GitHub preset support (optional)
## Installation

macOS & Linux (Recommended):

```plain text
# Add the tap (one-time setup)
brew tap smithclay/tap
brew install claudetainer

# Install dependencies
brew install node
npm install -g @devcontainers/cli
```

Other systems: Direct download or dev container feature

## Language Support

Auto-detects and configures for:

- Python (requirements.txt, pyproject.toml) → black, flake8, autopep8
- Node.js (package.json) → eslint, prettier, TypeScript support
- Go (go.mod) → gofmt, golangci-lint
- Rust (Cargo.toml) → rustfmt, clippy
- Shell (.sh files) → shellcheck, shfmt
Don't see your language? Create custom presets or request new ones.

## Essential Commands

```plain text
# Project setup
claudetainer init [language]    # Auto-detects language if not specified
claudetainer up                 # Start container

# Connect and use
claudetainer ssh                # Connect with terminal multiplexer
claude                          # Start Claude Code (inside container)

# Management
claudetainer list               # List running containers
claudetainer doctor             # Health check and troubleshooting
claudetainer rm -f              # Clean removal
```

## Remote Development

Connect from anywhere with persistent sessions:

```plain text
claudetainer mosh                # MOSH + Zellij/tmux multiplexer (better for mobile)
# Password: vscode (change via container config)
```

Includes mobile-optimized layouts and push notifications so you can code from your phone effectively.

## Advanced Configuration

- GitHub Presets - Share team configurations
- Custom Layouts - Terminal multiplexer customization
- CLI Reference - Complete command documentation
- Troubleshooting - Detailed problem solving
## Contributing

Want to improve claudetainer? Check out our development guide for:

- Architecture deep-dive
- Creating new presets
- Testing strategies
- Contribution workflow
## License

MIT License - see LICENSE for details.

## Acknowledgements

Many of the original hooks and commands came from sources elsewhere in the Claude Code community, specificaly:

- https://github.com/Veraticus/nix-config/tree/main/home-manager/claude-code
- https://github.com/AizenvoltPrime/claude-setup
Huge thanks to both of those people.


