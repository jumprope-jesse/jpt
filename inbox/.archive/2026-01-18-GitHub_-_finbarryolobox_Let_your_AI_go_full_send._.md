---
type: link
source: notion
url: https://github.com/finbarr/yolobox
notion_type: Software Repo
tags: ['Running']
created: 2026-01-12T21:36:00.000Z
---

# GitHub - finbarr/yolobox: Let your AI go full send. Your home directory stays home.

## Overview (from Notion)
- AI Empowerment: Leverage AI without the fear of accidental data loss, allowing for more experimental coding and creativity.
- Sandboxing: The containerization approach protects your home directory, letting you focus on innovation without the usual risks.
- Quick Iteration: Speed up development cycles by running AI tools without prompts, which can help in rapidly prototyping ideas.
- Sustainability: Use eco-friendly practices with tools that respect your environment, aligning with modern values.
- Remote Work Integration: Adapt to working from home or various locations while ensuring your data is secure and your productivity is high.
- Encouraging Learning: Simplifies the process of learning and experimenting with new technologies, making it accessible for personal or professional growth.
- Alternative Perspectives: Consider the balance between automation and the need for human oversight; while AI can enhance productivity, it’s crucial to remain engaged and aware of its limitations.

## AI Summary (from Notion)
Yolobox allows AI coding agents to run in a safe container, preventing accidental modifications to the home directory. It mounts the project directory, grants full permissions within the container, and includes essential tools and AI CLIs. Users can easily install and configure Yolobox, which supports various runtime environments and offers commands for running AI agents without permission prompts. It protects the home directory and sensitive data while allowing full functionality within the sandboxed environment.

## Content (from Notion)

```plain text
██╗   ██╗ ██████╗ ██╗      ██████╗ ██████╗  ██████╗ ██╗  ██╗
╚██╗ ██╔╝██╔═══██╗██║     ██╔═══██╗██╔══██╗██╔═══██╗╚██╗██╔╝
 ╚████╔╝ ██║   ██║██║     ██║   ██║██████╔╝██║   ██║ ╚███╔╝
  ╚██╔╝  ██║   ██║██║     ██║   ██║██╔══██╗██║   ██║ ██╔██╗
   ██║   ╚██████╔╝███████╗╚██████╔╝██████╔╝╚██████╔╝██╔╝ ██╗
   ╚═╝    ╚═════╝ ╚══════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝

```

Let your AI go full send. Your home directory stays home.

Run Claude Code, Codex, or any AI coding agent in "yolo mode" without nuking your home directory.

## The Problem

AI coding agents are incredibly powerful when you let them run commands without asking permission. But one misinterpreted prompt and rm -rf ~ later, you're restoring from backup (yea right, as if you have backups lol).

## The Solution

yolobox runs your AI agent inside a container where:

- ✅ Your project directory is mounted at /workspace
- ✅ The agent has full permissions and sudo inside the container
- ✅ Your home directory is NOT mounted (unless you explicitly opt in)
- ✅ Persistent volumes keep tools and configs across sessions
The AI can go absolutely wild inside the sandbox. Your actual home directory? Untouchable.

## Quick Start

```plain text
# Install (requires Go)
curl -fsSL https://raw.githubusercontent.com/finbarr/yolobox/master/install.sh | bash

# Or clone and build
git clone https://github.com/finbarr/yolobox.git
cd yolobox
make install
```

Then from any project:

```plain text
cd /path/to/your/project
yolobox
```

You're now in a sandboxed shell. Run claude and let it rip.

## What's in the Box?

The base image comes batteries-included:

- AI CLIs: Claude Code, Gemini CLI, OpenAI Codex (all aliased to run in full-auto mode!)
- Node.js 22 + npm/yarn/pnpm
- Python 3 + pip + venv
- Build tools: make, cmake, gcc
- Git + GitHub CLI
- Common utilities: ripgrep, fd, fzf, jq, vim
Need something else? You have sudo.

## AI CLIs Run in YOLO Mode

Inside yolobox, the AI CLIs are aliased to skip all permission prompts:

No confirmations, no guardrails—just pure unfiltered AI, the way nature intended.

## Commands

```plain text
yolobox                     # Drop into interactive shell
yolobox run <cmd...>        # Run a single command
yolobox run claude          # Run Claude Code in sandbox
yolobox upgrade             # Update binary and pull latest image
yolobox config              # Show resolved configuration
yolobox reset --force       # Delete volumes (fresh start)
yolobox version             # Show version
yolobox help                # Show help
```

## Flags

## Auto-Forwarded Environment Variables

These are automatically passed into the container if set:

- ANTHROPIC_API_KEY
- OPENAI_API_KEY
- GITHUB_TOKEN / GH_TOKEN
- OPENROUTER_API_KEY
- GEMINI_API_KEY
## Configuration

Create ~/.config/yolobox/config.toml for global defaults:

```plain text
runtime = "docker"
image = "ghcr.io/finbarr/yolobox:latest"
ssh_agent = true
```

Or .yolobox.toml in your project for project-specific settings:

```plain text
mounts = ["../shared-libs:/libs:ro"]
env = ["DEBUG=1"]
no_network = true
```

Priority: CLI flags > project config > global config > defaults.

> 

## Runtime Support

- macOS: Docker Desktop, OrbStack, or Colima
- Linux: Docker or Podman
> 

## Threat Model

What yolobox protects:

- Your home directory from accidental deletion
- Your SSH keys, credentials, and dotfiles
- Other projects on your machine
What yolobox does NOT protect:

- Your project directory (it's mounted read-write by default)
- Network access (use -no-network for paranoid mode)
- The container itself (the AI has root via sudo)
For extra paranoia, use --readonly-project to mount your project read-only. Outputs go to /output.

## Building the Base Image

```plain text
make image
```

This builds yolobox/base:latest locally.

## Why "yolobox"?

Because you want to tell your AI agent "just do it" without consequences. YOLO, but in a box.

## License

MIT


