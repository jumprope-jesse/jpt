---
type: link
source: notion
url: https://github.com/21st-dev/1code
notion_type: Software Repo
tags: ['Running']
created: 2026-01-16T23:41:00.000Z
---

# GitHub - 21st-dev/1code: Better UI app for running code agents in parallel (ClaudeCode, OpenCode, Codex)

## Overview (from Notion)
- 1Code offers a user-friendly interface for executing code agents, which could simplify your coding workflows.
- The ability to run local and remote agents in parallel may enhance productivity, especially if juggling multiple projects or commitments.
- Real-time tool execution and integrated terminal access can streamline debugging and testing processes, saving time.
- Project management features could aid in organizing code and maintaining version control, beneficial for both personal projects and company initiatives.
- Engaging with the community on Discord can foster connections, helping you keep up with industry trends and gain support from peers.
- Unique aspect: It combines project management and coding in one app, potentially transforming how you approach software development.
- Alternate view: While powerful, reliance on such tools may lead to less hands-on experience with core coding concepts, so balance is key.

## AI Summary (from Notion)
1Code offers a user-friendly interface for executing code agents locally and remotely, featuring project management, real-time tool execution, isolated worktree sessions, and integrated terminal access. Installation options include building from source or subscribing for pre-built releases and support. Community feedback is encouraged through Discord, and the project is licensed under Apache License 2.0.

## Content (from Notion)

# 1Code

Best UI for Claude Code with local and remote agent execution.

By 21st.dev

## Features

- Plan & Agent Modes - Read-only analysis or full code execution permissions
- Project Management - Link local folders with automatic Git remote detection
- Real-time Tool Execution - See bash commands, file edits, and web searches as they happen
- Git Worktree Isolation - Each chat session runs in its own isolated worktree
- Integrated Terminal - Full terminal access within the app
- Change Tracking - Visual diffs and PR management
## Installation

### Option 1: Build from source (free)

```plain text
# Prerequisites: Bun, Python, Xcode Command Line Tools (macOS)
bun install
bun run build
bun run package:mac  # or package:win, package:linux
```

### Option 2: Subscribe to 1code.dev (recommended)

Get pre-built releases + background agents support by subscribing at 1code.dev.

Your subscription helps us maintain and improve 1Code.

## Development

```plain text
bun install
bun run dev
```

## Feedback & Community

Join our Discord for support and discussions.

## License

Apache License 2.0 - see LICENSE for details.


