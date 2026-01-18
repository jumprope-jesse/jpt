---
type: link
source: notion
url: https://github.com/Yeachan-Heo/oh-my-claude-sisyphus
notion_type: Software Repo
tags: ['Running']
created: 2026-01-11T06:52:00.000Z
---

# GitHub - Yeachan-Heo/oh-my-claude-sisyphus: Sisyphus from OmO (Oh My Opencode), ported to the Claude Code SDK. Written with Claude Code — ironically. Anthropic, what are you gonna do next?

## Overview (from Notion)
- This software, "oh-my-claude-sisyphus," offers a multi-agent orchestration system that can streamline your software projects, making them more efficient and collaborative.
- Its focus on automation and task delegation can help manage the complexities of balancing work and family life, allowing for more time spent with loved ones.
- The unique narrative of resilience—like Sisyphus rolling his boulder—can serve as a metaphor for persistence in your career and personal life, emphasizing the importance of continual effort despite challenges.
- The integration of advanced tools like LSP and AST can enhance your coding experience, potentially leading to better product outcomes and innovations in your startup.
- Consider the potential for using such technology to mentor younger engineers or your children, providing them with cutting-edge tools to explore their interests in coding and technology.
- Alternate views might question the reliance on automation; emphasizing the need for human creativity and intuition in software development, reminding you to balance tech with personal touch.

## AI Summary (from Notion)
A multi-agent orchestration system for Claude Code, named oh-my-claude-sisyphus, is designed to persistently complete tasks. It includes eleven specialized agents for various functions like debugging, documentation, and planning, and offers commands for activation and management. The system features an auto-update mechanism, lifecycle hooks, and built-in skills for enhanced performance. Installation can be done via a simple script or npm, and it supports project-specific configurations.

## Content (from Notion)

Multi-agent orchestration system for Claude Code

Like Sisyphus, these agents persist until every task is complete.

Install • Usage • Agents • Website

## The Saga

> 

Port of oh-my-opencode.

## Quick Install

### One-liner (recommended)

```plain text
curl -fsSL https://raw.githubusercontent.com/Yeachan-Heo/oh-my-claude-sisyphus/main/scripts/install.sh | bash
```

### Via npm

```plain text
npm install -g oh-my-claude-sisyphus
```

### Manual Install

```plain text
git clone https://github.com/Yeachan-Heo/oh-my-claude-sisyphus.git
cd oh-my-claude-sisyphus
chmod +x scripts/install.sh
./scripts/install.sh
```

## What Gets Installed

The installer adds to your Claude Code config (~/.claude/):

```plain text
~/.claude/
├── agents/
│   ├── oracle.md              # Architecture & debugging expert (Opus)
│   ├── librarian.md           # Documentation & research (Sonnet)
│   ├── explore.md             # Fast pattern matching (Haiku)
│   ├── frontend-engineer.md   # UI/UX specialist (Sonnet)
│   ├── document-writer.md     # Technical writing (Haiku)
│   ├── multimodal-looker.md   # Visual analysis (Sonnet)
│   ├── momus.md               # Plan reviewer (Opus)
│   ├── metis.md               # Pre-planning consultant (Opus)
│   ├── orchestrator-sisyphus.md # Todo coordinator (Sonnet)
│   ├── sisyphus-junior.md     # Focused executor (Sonnet)
│   └── prometheus.md          # Strategic planner (Opus)
├── commands/
│   ├── sisyphus.md         # /sisyphus command
│   ├── sisyphus-default.md # /sisyphus-default command
│   ├── ultrawork.md        # /ultrawork command
│   ├── deepsearch.md       # /deepsearch command
│   ├── analyze.md          # /analyze command
│   ├── plan.md             # /plan command (Prometheus)
│   ├── review.md           # /review command (Momus)
│   ├── prometheus.md       # /prometheus command
│   ├── orchestrator.md     # /orchestrator command
│   ├── ralph-loop.md       # /ralph-loop command
│   └── cancel-ralph.md     # /cancel-ralph command
└── CLAUDE.md               # Sisyphus system prompt

```

## Usage

### Start Claude Code

```plain text
claude
```

### Slash Commands

### Examples

```plain text
# In Claude Code:

# Activate Sisyphus for a task
/sisyphus refactor the authentication module

# Set as default mode (persistent)
/sisyphus-default

# Use ultrawork for maximum performance
/ultrawork implement user dashboard with charts

# Deep search
/deepsearch API endpoints that handle user data

# Deep analysis
/analyze performance bottleneck in the database layer
```

### Magic Keywords

Just include these words anywhere in your prompt:

```plain text
# These work in normal prompts too:
> ultrawork implement user authentication with OAuth

> find all files that import the utils module

> analyze why the tests are failing
```

## Auto-Update

Oh-my-claude-sisyphus includes a silent auto-update system that checks for updates in the background. Updates are applied automatically without interrupting your workflow.

To manually check for updates:

```plain text
/update
```

## Hooks System

Oh-my-claude-sisyphus includes 18 lifecycle hooks that enhance Claude Code's behavior:

### Core Hooks

### Context & Recovery

### Quality & Validation

### Environment & Notifications

## Builtin Skills

Six builtin skills provide specialized capabilities:

Skills are automatically activated via slash commands or magic keywords.

## The Eleven Agents

Claude will automatically delegate to these specialized agents:

### Task Execution

### Planning & Review

### Orchestration

### Manual Agent Invocation

You can explicitly request an agent:

```plain text
Use the oracle agent to debug the memory leak in the worker process

Have the librarian find all documentation about the API

Ask explore to find all TypeScript files that import React

```

## Configuration

### Project-Level Config

Create .claude/CLAUDE.md in your project for project-specific instructions:

```plain text
# Project Context

This is a TypeScript monorepo using:
- Bun runtime
- React for frontend
- PostgreSQL database

## Conventions
- Use functional components
- All API routes in /src/api
- Tests alongside source files
```

### Agent Customization

Edit agent files in ~/.claude/agents/ to customize behavior:

```plain text
---
name: oracle
description: Your custom description
tools: Read, Grep, Glob, Bash, Edit
model: opus  # or sonnet, haiku
---

Your custom system prompt here...
```

## Uninstall

```plain text
curl -fsSL https://raw.githubusercontent.com/Yeachan-Heo/oh-my-claude-sisyphus/main/scripts/uninstall.sh | bash
```

Or manually:

```plain text
rm ~/.claude/agents/{oracle,librarian,explore,frontend-engineer,document-writer,multimodal-looker,momus,metis,orchestrator-sisyphus,sisyphus-junior,prometheus}.md
rm ~/.claude/commands/{sisyphus,sisyphus-default,ultrawork,deepsearch,analyze,plan,review,prometheus,orchestrator,ralph-loop,cancel-ralph}.md
```

## SDK Usage (Advanced)

For programmatic use with the Claude Agent SDK:

```plain text
npm install oh-my-claude-sisyphus @anthropic-ai/claude-agent-sdk
```

```plain text
import { createSisyphusSession } from 'oh-my-claude-sisyphus';
import { query } from '@anthropic-ai/claude-agent-sdk';

const session = createSisyphusSession();

for await (const message of query({
  prompt: session.processPrompt("ultrawork implement feature X"),
  ...session.queryOptions
})) {
  console.log(message);
}
```

## How It Works

```plain text
┌─────────────────────────────────────────────────────────────────┐
│                      SISYPHUS ORCHESTRATOR                       │
│                    (The Boulder Never Stops)                     │
└─────────────────────────────────────────────────────────────────┘
                              │
          ┌───────────────────┼───────────────────┐
          │                   │                   │
          ▼                   ▼                   ▼
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│    PLANNING     │  │   EXECUTION     │  │    SUPPORT      │
├─────────────────┤  ├─────────────────┤  ├─────────────────┤
│ 🔥 Prometheus   │  │ 🔮 Oracle       │  │ 📚 Librarian    │
│ 🎭 Momus        │  │ 🎨 Frontend Eng │  │ 🔍 Explore      │
│ 🦉 Metis        │  │ 🪨 Orchestrator │  │ 📝 Doc Writer   │
│                 │  │ ✨ Sisyphus Jr  │  │ 👁️ Multimodal   │
└─────────────────┘  └─────────────────┘  └─────────────────┘

```

1. Sisyphus Orchestrator: The main Claude instance coordinates all work
1. Specialized Subagents: Each agent has focused expertise and tools
1. Parallel Execution: Independent tasks run concurrently
1. Continuation Enforcement: Agents persist until ALL tasks complete
1. Context Injection: Project-specific instructions from CLAUDE.md files
## Requirements

- Claude Code installed
- Anthropic API key (ANTHROPIC_API_KEY environment variable)
## License

MIT - see LICENSE

## Credits

Inspired by oh-my-opencode by code-yeongyu.

One must imagine a multi-agent system happy.

The boulder never stops.


