---
type: link
source: notion
url: https://github.com/built-by-as/FleetCode
notion_type: Software Repo
tags: ['Running']
created: 2025-10-09T03:30:00.000Z
---

# built-by-as/FleetCode: Light-weight control pane to run CLI coding agents(Claude Code, Codex) in parallel

## Overview (from Notion)
- FleetCode enables multitasking with coding agents, ideal for managing multiple projects or learning new technologies while balancing family life.
- The isolation of git worktrees means you can experiment without the fear of affecting your main projects, promoting a safer learning environment.
- The persistent sessions feature allows you to pick up coding sessions whenever you have a spare moment, fitting into a busy schedule.
- Terminal theming can make your coding environment more enjoyable and reduce eye strain, especially important during long hours of work.
- The ability to configure setup commands may streamline your workflow, allowing you to automate routine tasks and focus on coding.
- Consider the balance between using advanced tools like FleetCode and maintaining simplicity; sometimes, less is more.
- Explore alternative methods of collaboration with your coding team; FleetCode enhances solo work, but think about integrating team tools for joint projects.

## AI Summary (from Notion)
FleetCode is a desktop terminal application that allows users to run multiple CLI coding agents (Claude, Codex) in isolated git worktrees. Key features include persistent sessions, customizable terminal themes, and session management. It requires Node.js and Git for installation, and sessions can be created and managed easily. Troubleshooting tips for macOS and Claude Code are also provided.

## Content (from Notion)

# FleetCode

A desktop terminal application for running multiple CLI coding agents simultaneously, each in isolated git worktrees.

## Features

- Multiple Sessions: Run multiple coding agent sessions (Claude, Codex) in parallel
- Git Worktree Isolation: Each session runs in its own git worktree, keeping work isolated
- Persistent Sessions: Sessions persist across app restarts with automatic resumption
- Terminal Theming: Choose from preset themes (macOS Light/Dark, Solarized Dark, Dracula, One Dark, GitHub Dark)
- Setup Commands: Configure shell commands to run before the coding agent starts
- MCP Server Management: Add and configure Model Context Protocol (MCP) servers
- Session Management: Rename, close, and delete sessions with automatic worktree cleanup
## Prerequisites

- Node.js 16+
- Git
- Claude CLI (npm install -g @anthropic-ai/claude-cli) or Codex
## Installation

```plain text
npm install
```

## Usage

### Development

```plain text
npm run dev
```

### Production Build

```plain text
npm run build
npm start
```

## How It Works

### Session Creation

1. Select a project directory (must be a git repository)
1. Choose a parent branch for the worktree
1. Select your coding agent (Claude or Codex)
1. Optionally add setup commands (e.g., environment variables, source files)
1. FleetCode creates a new git worktree and spawns a terminal session
### Session Management

- New Sessions: Use -session-id <uuid> for first-time Claude sessions
- Reopened Sessions: Automatically resume with -resume <uuid>
- Worktrees: Each session gets its own isolated git worktree
- Persistence: Sessions are saved and can be reopened after closing the app
### Terminal Settings

Access settings via the gear icon (⚙️) in the sidebar:

- Font Family: Choose from common monospace fonts
- Font Size: Adjust terminal text size
- Theme: Select from preset color themes
- Cursor Blink: Toggle cursor blinking
### MCP Servers

Configure Model Context Protocol servers for enhanced agent capabilities:

- stdio: Direct process communication
- SSE: Server-sent events via HTTP
## Troubleshooting

### macOS: "App can't be opened because it is from an unidentified developer"

If you encounter a quarantine warning when trying to open the app on macOS, run:

```plain text
xattr -cr /path/to/FleetCode.app
```

This removes the quarantine attribute that prevents the app from opening.

### Claude Code: Working Directory Issues

If you're using Claude Code and it's reading/writing files from the wrong directory instead of the worktree, disable "Auto connect to IDE" in your Claude Code settings:

```plain text
claude config
```

Set autoConnectToIde to false. This ensures Claude Code operates within the correct worktree directory.

## License

ISC


