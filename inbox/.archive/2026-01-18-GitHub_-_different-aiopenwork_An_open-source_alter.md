---
type: link
source: notion
url: https://github.com/different-ai/openwork
notion_type: Software Repo
tags: ['Running']
created: 2026-01-16T05:38:00.000Z
---

# GitHub - different-ai/openwork: An open-source alternative to Claude Cowork, powered by OpenCode

## Overview (from Notion)
- OpenWork offers a user-friendly interface for managing complex workflows, making it easier to juggle work and family life.
- Its extensibility allows you to customize tools that fit your specific needs, whether at home or in your startup.
- The focus on local and remote capabilities means you can work flexibly, adapting to your role as a parent while maintaining productivity.
- The integration of real-time updates could help you stay on top of tasks without overwhelming yourself.
- Unique features like permission management can help in collaborative environments, making it easier to share tasks with your team while keeping your home life organized.
- An alternative viewpoint: while the promise of "agentic work" is appealing, it might also lead to expectations of constant connectivity and performance—balancing work and family time is crucial.

## AI Summary (from Notion)
OpenWork is an extensible, open-source desktop app designed for knowledge workers, facilitating a guided workflow without the need for a command-line interface. It includes features such as session management, real-time updates, permission handling, and a skills manager for plugins. The app can run locally or connect to remote servers, aiming to streamline workflows and enhance productivity.

## Content (from Notion)

# OpenWork

OpenWork is an extensible, open-source “Claude Work” style system for knowledge workers.

It’s a native desktop app that runs OpenCode under the hood, but presents it as a clean, guided workflow:

- pick a workspace
- start a run
- watch progress + plan updates
- approve permissions when needed
- reuse what works (templates + skills)
The goal: make “agentic work” feel like a product, not a terminal.

## Quick start

Download the dmg here https://github.com/different-ai/openwork/releases (or install from source below)

## Why

Knowledge workers don’t want to learn a CLI, fight config sprawl, or rebuild the same workflows in every repo. OpenWork is designed to be:

- Extensible: skill and opencode plugins are installable modules.
- Auditable: show what happened, when, and why.
- Permissioned: access to privileged flows.
- Local/Remote: OpenWork works locally as well as can connect to remote servers.
## What’s Included (v0.1)

- Host mode: start opencode serve locally in a chosen folder.
- Client mode: connect to an existing OpenCode server by URL.
- Sessions: create/select sessions and send prompts.
- Live streaming: SSE /event subscription for realtime updates.
- Execution plan: render OpenCode todos as a timeline.
- Permissions: surface permission requests and reply (allow once / always / deny).
- Templates: save and re-run common workflows (stored locally).
- Skills manager: 
## Skill Manager

## Works on local computer or servers

## Quick Start

### Requirements

- Node.js + pnpm
- Rust toolchain (for Tauri): cargo, rustc
- OpenCode CLI installed and available on PATH: opencode
### Install

```plain text
pnpm install
```

### Run (Desktop)

```plain text
pnpm dev
```

### Run (Web UI only)

```plain text
pnpm dev:web
```

## Architecture (high-level)

- In Host mode, OpenWork spawns: 
- The UI uses @opencode-ai/sdk/v2/client to: 
## Folder Picker

The folder picker uses the Tauri dialog plugin. Capability permissions are defined in:

- src-tauri/capabilities/default.json
## OpenPackage Notes

If opkg is not installed globally, OpenWork falls back to:

```plain text
pnpm dlx opkg install <package>
```

## OpenCode Plugins

Plugins are the native way to extend OpenCode. OpenWork now manages them from the Skills tab by reading and writing opencode.json.

- Project scope: <workspace>/opencode.json
- Global scope: ~/.config/opencode/opencode.json (or $XDG_CONFIG_HOME/opencode/opencode.json)
You can still edit opencode.json manually; OpenWork uses the same format as the OpenCode CLI:

```plain text
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": ["opencode-wakatime"]
}
```

## Useful Commands

```plain text
pnpm typecheck
pnpm build:web
pnpm test:e2e
```

## Security Notes

- OpenWork hides model reasoning and sensitive tool metadata by default.
- Host mode binds to 127.0.0.1 by default.
## License

TBD.


