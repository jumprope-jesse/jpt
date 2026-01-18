---
type: link
source: notion
url: https://github.com/stravu/crystal
notion_type: Software Repo
tags: ['Running']
created: 2025-10-18T11:48:00.000Z
---

# GitHub - stravu/crystal: Run multiple Codex and Claude Code AI sessions in parallel git worktrees. Test, compare approaches & manage AI-assisted development workflows in one desktop app.

## Overview (from Notion)
- Crystal allows you to run multiple AI code sessions simultaneously, which can help streamline your workflow and increase productivity.
- The ability to isolate tasks in separate git worktrees means you can manage complex projects without losing track of changes, a boon for both personal and professional coding endeavors.
- The integrated testing scripts let you monitor your code while working, reducing the time spent on back-and-forth debugging.
- The minimalist design and user-friendly features make it accessible, even if you're balancing family life and work commitments.
- As a founder, leveraging AI tools like Crystal could provide a competitive edge, allowing your team to innovate faster and adapt to changing markets.
- Consider the implications of AI-assisted development: while it enhances efficiency, it may also shift the role of software engineers toward more strategic thinking and problem-solving.
- Some might argue that reliance on AI could diminish coding skills over time; finding a balance between leveraging technology and maintaining core competencies is crucial.

## AI Summary (from Notion)
Crystal is a multi-session AI code assistant that allows users to run isolated sessions with Claude Code and Codex in separate git worktrees. Users can create projects, monitor changes, and manage commits efficiently. The tool supports installation on macOS and Windows, and offers guidelines for building from source. It is open-source under the MIT License and designed for seamless integration with third-party deployments.

## Content (from Notion)

# Crystal - Multi-Session AI Code Assistant Manager

### *Get the Latest Release Here**

Crystal lets you use AI on isolated copies of your code so you can work on multiple tasks instead of waiting for your agents to finish.

Run one or more sessions with Claude Code, Codex, or both

## The Crystal Workflow

1. Create sessions from prompts, each in an isolated git worktree
1. Iterate with your AI assistant (Claude Code or Codex) inside your sessions. Each iteration will make a commit so you can always go back.
1. Review the diff changes and make manual edits as needed
1. Squash your commits together with a new message and merge to your main branch.
## 🚀 Quick Start

### Prerequisites

- For Claude Code: Claude Code installed and logged in or API key provided
- For Codex: Codex installed (via npm: @openai/codex or Homebrew) with ChatGPT account or API key
- Git installed
- Git repository (Crystal will initialize one if needed)
### 1. Create a Project

Create a new project if you haven't already. This can be an empty folder or an existing git repository. Crystal will initialize git if needed.

### 2. Create Sessions from a Prompt

For any feature you're working on, create one or multiple new sessions:

- Each session will be an isolated git worktree
### 3. Monitor and Test Your Changes

As sessions complete:

- Configure run scripts in project settings to test your application without leaving Crystal
- Use the diff viewer to review all changes and make manual edits as needed
- Continue conversations with your AI assistant if you need additional changes
### 4. Finalize Your Changes

When everything looks good:

- Click "Rebase to main" to squash all commits with a new message and rebase them to your main branch
- This creates a clean commit history on your main branch
### Git Operations

- Rebase from main: Pull latest changes from main into your worktree
- Squash and rebase to main: Combine all commits and rebase onto main
- Always preview commands with tooltips before executing
## Installation

### Download Pre-built Binaries

-  
-  
### Homebrew

```plain text
brew install --cask stravu-crystal
```

## Building from Source

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

## 🤝 Contributing

We welcome contributions! Please see our Contributing Guidelines for details.

### Developing Crystal with Crystal

If you're using Crystal to develop Crystal itself, you need to use a separate data directory to avoid conflicts with your main Crystal instance:

```plain text
# Set the run script in your Crystal project settings to:
pnpm run setup && pnpm run build:main && CRYSTAL_DIR=~/.crystal_test pnpm electron-dev
```

This ensures:

- Your development Crystal instance uses ~/.crystal_test for its data
- Your main Crystal instance continues using ~/.crystal
- Worktrees won't conflict between the two instances
- You can safely test changes without affecting your primary Crystal setup
### Using with Third-Party Deployments

To use Crystal with cloud providers or via corporate infrastructure, you should create a settings file with ENV values to correctly connect to the provider.

For example, here is a minimal configuration to use Amazon Bedrock via an AWS Profile:

```plain text
{
  "env": {
    "CLAUDE_CODE_USE_BEDROCK": "1",
    "AWS_REGION": "us-east-2", // Replace with your AWS region
    "AWS_PROFILE": "my-aws-profile" // Replace with your profile
  },
}
```

Check the deployment documentation for more information on getting setup with your particular deployment.

## Additional Documentation

For a full project overview, see CLAUDE.md. Additional diagrams, database schema details, release instructions, and license notes can be found in the docs directory.

## 📄 License

Crystal is open source software licensed under the MIT License.

### Third-Party Licenses

Crystal includes third-party software components. All third-party licenses are documented in the NOTICES file. This file is automatically generated and kept up-to-date with our dependencies.

To regenerate the NOTICES file after updating dependencies:

```plain text
pnpm run generate-notices
```

## Disclaimer

Crystal is an independent project created by Stravu. Claude™ is a trademark of Anthropic, PBC. Codex™ is a trademark of OpenAI, Inc. Crystal is not affiliated with, endorsed by, or sponsored by Anthropic or OpenAI. This tool is designed to work with Claude Code and Codex, which must be installed separately.

Made with ❤️ by Stravu


