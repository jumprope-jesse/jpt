---
type: link
source: notion
url: https://github.com/stravu/crystal
notion_type: Software Repo
tags: ['Running']
created: 2025-06-23T13:39:00.000Z
---

# GitHub - stravu/crystal: An IVE: Integrated Vibe Environment

## Overview (from Notion)
- Crystal is a powerful tool for managing multiple AI coding sessions, which can enhance productivity and streamline workflows, especially for software development.
- The ability to run parallel instances of Claude Code can help in testing various code solutions simultaneously, saving time on debugging and iteration.
- The Git integration facilitates version control and tracking changes, making it easier to collaborate with team members or maintain different project versions.
- This tool's design focuses on user-friendliness, which can be crucial for balancing work tasks while managing family responsibilities, allowing you to maximize efficiency.
- The open-source nature of Crystal encourages community contributions, fostering innovation and collaboration among developers, which can be inspiring.
- Consider the environmental impact of tech tools—Crystal promotes sustainable development practices, which may align with personal values regarding eco-friendliness.
- An alternate view is that the reliance on tools like Crystal could lead to over-dependence on technology, potentially diminishing hands-on coding skills or personal interactions in development teams.

## AI Summary (from Notion)
Crystal is an Electron desktop application for managing multiple Claude Code instances using git worktrees, allowing parallel sessions, session persistence, and built-in git operations. Users can create projects, manage sessions, run scripts, and perform git operations efficiently. The application is open source and requires Claude Code and git to function.

## Content (from Notion)

# Crystal - Multi-Session Claude Code Manager

### *Get the Latest Release Here**

Crystal is an Electron desktop application that lets you run, inspect, and test multiple Claude Code instances simultaneously using git worktrees. Crystal is an independent project created by Stravu. Stravu is the way AI-first teams collaborate.

Create multiple Claude Code sessions with a simple prompt, each running in its own git worktree

## ✨ Key Features

- 🚀 Parallel Sessions - Run multiple Claude Code instances at once
- 🌳 Git Worktree Isolation - Each session gets its own branch
- 💾 Session Persistence - Resume conversations anytime
- 🔧 Git Integration - Built-in rebase and squash operations
- 📊 Change Tracking - View diffs and track modifications
- 🔔 Notifications - Desktop alerts when sessions need input
- 🏗️ Run Scripts - Test changes instantly without leaving Crystal
## 🚀 Quick Start

### Prerequisites

- Claude Code installed and logged in or API key provided
- Git installed
- Git repository (Crystal will initialize one if needed)
### Installation

### Download Pre-built Binaries

- macOS: Download Crystal-{version}.dmg from the latest release 
### Building from Source

```plain text
# Clone the repository
git clone https://github.com/stravu/crystal.git
cd crystal

# One-time setup
pnpm run setup

# Run in development
pnpm run electron-dev
```

### Building for Production

```plain text
# Build for macOS
pnpm build:mac
```

### Developing Crystal with Crystal

If you're using Crystal to develop Crystal itself, you need to use a separate data directory to avoid conflicts with your main Crystal instance:

```plain text
# Set the run script in your Crystal project settings to:
pnpm run setup && CRYSTAL_DIR=~/.crystal_test pnpm electron-dev
```

This ensures:

- Your development Crystal instance uses ~/.crystal_test for its data
- Your main Crystal instance continues using ~/.crystal
- Worktrees won't conflict between the two instances
- You can safely test changes without affecting your primary Crystal setup
## 📖 How to Use

### 1. Create a Project

You must create a project before you can proceed. A project should point to a git repository. If there is no repo in the folder you select one will be created.

### 2. Create a Session

Click "Create Session" and enter:

- Prompt: What you want Claude to do
- Worktree Name: Branch name (optional)
- Count: Number of parallel sessions
### 3. Manage Sessions

- 🟢 Initializing: Setting up git worktree
- 🟢 Running: Claude is working
- 🟡 Waiting: Needs your input
- ⚪ Completed: Task finished successfully
- 🔵 New Activity: Session has new unviewed results
- 🔴 Error: Something went wrong
- Click any session to view or continue it
### 4. View Your Work

- Output: Formatted terminal output
- Changes: Git diffs of all modifications
- Terminal: Run tests or build scripts
- Messages: Raw JSON for debugging
### 5. Run Scripts

Configure project-specific scripts in the project settings:

- Run scripts: Execute dev servers, test watchers, or any continuous processes
- Scripts run in the Terminal tab while Claude is working
- Each line runs sequentially - perfect for setup commands followed by servers
- All scripts stop automatically when the session ends
### 6. Git Operations

- Rebase from main: Pull latest changes
- Squash and rebase: Combine commits
- Preview commands before executing
## 🤝 Contributing

We welcome contributions! Please see our Contributing Guidelines for details.

## 📄 License

Crystal is open source software licensed under the MIT License.

### Third-Party Licenses

Crystal includes third-party software components. All third-party licenses are documented in the NOTICES file. This file is automatically generated and kept up-to-date with our dependencies.

To regenerate the NOTICES file after updating dependencies:

```plain text
pnpm run generate-notices
```

## Disclaimer

Crystal is an independent project created by Stravu. Claude™ is a trademark of Anthropic, PBC. Crystal is not affiliated with, endorsed by, or sponsored by Anthropic. This tool is designed to work with Claude Code, which must be installed separately.

Made with ❤️ by Stravu


