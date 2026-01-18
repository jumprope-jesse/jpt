# Coding Agent Tools & UIs

Tools and interfaces for running AI coding agents.

---

## Heatmap (0github.com)

*Source: https://0github.com/ - Added: 2026-01-18*

A heatmap diff viewer that color-codes code changes by how much human attention they need during code review.

### Key Features

- **Attention-Based Coloring** - Color-codes diff lines/tokens by priority, not just bugs
- **Beyond Bug Detection** - Flags hard-coded secrets, weird crypto modes, gnarly logic
- **Easy to Try** - Replace `github.com` with `0github.com` in any PR URL
- **Open Source** - Full source available

### How It Works

1. Clones repo into a VM
2. Runs GPT-5 Codex on every diff
3. Outputs JSON structure parsed into colored heatmap

### Why It's Interesting

- Different philosophy from PR-review bots: "worth a second look" vs "is it a bug"
- Zero friction to try (URL replacement)
- Focuses human attention where it matters most

---

## Strands Agents

*Source: https://strandsagents.com/latest/ - Added: 2026-01-18*

An enterprise-ready AI agent framework used by companies like Smartsheet for building production AI assistants.

### Key Features

- **Conversation Memory** - Built-in robust conversation memory system for context-aware interactions
- **Dynamic Tool Registration** - Tools can be registered dynamically, adapting to changing project needs
- **Enterprise-Ready** - Designed for secure, scalable production deployments
- **Development Efficiency** - Aims to balance enterprise features with quick implementation

### Notable Users

- **Smartsheet** - Used Strands for their next-generation AI capabilities, citing it as providing "the perfect balance of enterprise-ready features and development efficiency"

### Why It's Interesting

- Positions itself for enterprise use cases where security and scalability matter
- Conversation memory is a first-class feature, not an afterthought
- Dynamic tool registration suggests good extensibility

### Notes

- More of an SDK/framework than a UI tool (unlike Conductor or 1Code)
- Good option to evaluate if building enterprise AI assistants
- Compare with other agent frameworks like LangGraph, CrewAI, AutoGen

## Conductor

*Source: https://www.conductor.build/ - Added: 2026-01-18*

A macOS app for running parallel Claude Code agents in isolated workspaces. Monitor what they're working on, then review and merge their changes.

### Key Features

- **Parallel Agents** - Run multiple Claude Code agents simultaneously
- **Isolated Workspaces** - Each agent works in its own workspace to prevent conflicts
- **Real-time Monitoring** - See at a glance what each agent is working on
- **Review & Merge** - Review agent changes before merging into your codebase

### Authentication

Uses your existing Claude Code login—no separate API key needed:
- Works with Claude Pro/Max plan credentials
- Works with API keys if you're using those instead

### How It Compares

| Feature | Conductor | 1Code | Aizen | Vibe Kanban |
|---------|-----------|-------|-------|-------------|
| Primary Focus | Parallel Claude Code | Multi-agent UI | Worktree management | Kanban orchestration |
| Agent Support | Claude Code only | Multiple (Claude, OpenCode, Codex) | ACP-compatible | Agent-agnostic |
| Isolation | Workspace-based | Git worktrees | Per-worktree | Conflict prevention |
| Platform | macOS | Cross-platform | macOS | Web |
| Auth | Uses Claude login | Separate config | Unknown | Unknown |

### Why It's Interesting

- Minimal friction - uses existing Claude Code credentials
- Purpose-built for Claude Code users rather than agent-agnostic
- Combines workspace isolation with visual monitoring
- Good fit for Claude Max subscribers who want to parallelize work

### Notes

- macOS only
- Early stage - see what's new in version updates (currently 0.28.6)
- Similar conceptually to Vibe Kanban but focused specifically on Claude Code

---

## 1Code (21st.dev)

*Source: https://github.com/21st-dev/1code - Added: 2026-01-18*

A desktop UI for running code agents (Claude Code, OpenCode, Codex) with local and remote execution.

### Key Features

- **Plan & Agent Modes** - Read-only analysis or full code execution permissions
- **Git Worktree Isolation** - Each chat session runs in its own isolated worktree
- **Real-time Tool Execution** - See bash commands, file edits, and web searches as they happen
- **Project Management** - Link local folders with automatic Git remote detection
- **Integrated Terminal** - Full terminal access within the app
- **Change Tracking** - Visual diffs and PR management

### Installation

**Build from source (free):**
```bash
# Prerequisites: Bun, Python, Xcode Command Line Tools (macOS)
bun install
bun run build
bun run package:mac  # or package:win, package:linux
```

**Subscription:** Pre-built releases + background agents support at 1code.dev

### Notes

- Apache License 2.0
- Community Discord for support
- Interesting approach: combines project management with coding agent execution
- The git worktree isolation is clever - prevents agents from stepping on each other's changes

## Obsidian ACP Plugin (Zed)

*Source: https://zed.dev/acp/editor/obsidian - Added: 2026-01-18*

An Obsidian plugin using Zed's Agent Control Protocol (ACP) to bring AI coding agents into your vault.

### What It Does

- Integrates Claude Code, Codex, Gemini CLI, and other AI agents into Obsidian
- Provides a dedicated side panel for agent interaction
- Chat with agents directly from within your vault

### Why It's Interesting

- Bridges personal knowledge management with coding agents
- Could enable agents to reference vault notes while coding
- Potential for using Obsidian as a project management layer on top of code agents

### Links

- Documentation: https://zed.dev/acp/editor/obsidian
- Part of Zed's broader ACP ecosystem (also supports VS Code, other editors)

## marimo ACP Client (Zed)

*Source: https://zed.dev/acp/editor/marimo - Added: 2026-01-18*

A Python notebook environment with integrated ACP agent support, designed for data science workflows.

### What It Does

- Provides an interactive Python notebook environment
- Integrates with Zed's ACP (Agent Control Protocol) for AI agent support
- Built specifically for data science workflows

### Why It's Interesting

- Combines data science notebooks with coding agents
- Could enable AI-assisted data exploration and analysis
- Part of the growing Zed ACP ecosystem alongside Obsidian, VS Code, etc.

### Links

- Documentation: https://zed.dev/acp/editor/marimo

## Aizen

*Source: https://aizen.win/ - Added: 2026-01-18*

A macOS app for managing multiple repositories and worktrees with integrated coding agents. "Switch worktrees, not windows."

### Key Features

- **Workspace Organization** - Group repositories into workspaces
- **Worktree-Centric UX** - Each worktree gets its own terminal, file browser, web browser, and chat session
- **Parallel Development** - Run agents on one branch while reviewing code on another
- **Agent Support** - Compatible with Claude, Codex (OpenAI), Gemini, Kimi, and any ACP-compatible agent
- **Auto-Install Agents** - Agents can be auto-installed from NPM or GitHub

### How It Compares to 1Code

| Feature | Aizen | 1Code |
|---------|-------|-------|
| Primary Focus | Worktree management | Project/chat management |
| Context Switching | Per-worktree (terminal, browser, agent) | Per-chat session (isolated worktree) |
| Platform | macOS only (13.5+) | macOS, Windows, Linux |
| Pricing | Free + $6/mo or $179 lifetime Pro | Free + subscription for builds |
| License | GPL-3.0 | Apache-2.0 |

### Why It's Interesting

- Optimized for developers juggling multiple branches across repos
- The "each worktree has its own everything" approach minimizes context switching
- Built around git worktrees as the core abstraction, not just projects

### Notes

- Requires macOS 13.5 Ventura or later (Apple Silicon & Intel)
- Pro tier is mainly for supporting development - all features currently free
- 30-day money-back guarantee

## OpenWork (different-ai)

*Source: https://github.com/different-ai/openwork - Added: 2026-01-18*

An open-source "Claude Work" style desktop app for knowledge workers, built on top of OpenCode.

### Key Features

- **Non-CLI Workflow** - Designed for knowledge workers who don't want to use a terminal
- **Session Management** - Create/select sessions, send prompts
- **Live Streaming** - SSE subscription for real-time updates
- **Execution Plan** - Renders OpenCode todos as a visual timeline
- **Permission Handling** - Surface permission requests with allow once/always/deny options
- **Templates** - Save and re-run common workflows (stored locally)
- **Skills Manager** - Plugin management for extending functionality
- **Dual Mode** - Host mode (spawn OpenCode locally) or Client mode (connect to remote server)

### Technical Details

- Built with Tauri (Rust + web frontend)
- Uses OpenCode CLI under the hood
- Plugins via `opencode.json` configuration
- Project scope: `<workspace>/opencode.json`
- Global scope: `~/.config/opencode/opencode.json`

### How It Compares

| Feature | OpenWork | 1Code | Aizen |
|---------|----------|-------|-------|
| Primary Focus | Guided workflow | Project management | Worktree management |
| Agent Backend | OpenCode | Multiple (Claude, OpenCode, Codex) | ACP-compatible agents |
| Remote Support | Yes (client/host modes) | Yes | No |
| Templates/Skills | Yes | Unknown | Unknown |
| Platform | macOS (DMG available) | Cross-platform | macOS only |
| License | TBD | Apache-2.0 | GPL-3.0 |

### Why It's Interesting

- "Make agentic work feel like a product, not a terminal" - clear UX philosophy
- Good for non-technical knowledge workers who want agent capabilities
- Remote server support enables team/enterprise scenarios
- Open source alternative to Claude's proprietary Cowork product

### Notes

- Very early (v0.1) but actively developed
- Requires Node.js + pnpm + Rust toolchain to build from source
- DMG available at GitHub releases for easier installation

## speak_when_done (MCP Server)

*Source: https://github.com/Marviel/speak_when_done - Added: 2026-01-18*

An MCP server that enables AI assistants to speak aloud when long-running tasks complete. Useful for multitasking during builds, tests, or deployments.

### What It Does

- Provides a `speak` tool to your AI assistant
- Uses pocket-tts for text-to-speech generation
- Supports multiple voices (default: "alba") and voice cloning from audio files
- macOS only (uses `afplay` for audio playback)

### Installation

**Claude Code (global):**
```bash
claude mcp add speak_when_done -s user -- uv run --directory /path/to/speak_when_done python server.py
```

**Claude Code (project):**
```bash
claude mcp add speak_when_done -- uv run --directory /path/to/speak_when_done python server.py
```

**Cursor:** Add to `~/.cursor/mcp.json` or `.cursor/mcp.json`:
```json
{
  "mcpServers": {
    "speak_when_done": {
      "command": "uv",
      "args": ["run", "--directory", "/path/to/speak_when_done", "python", "server.py"]
    }
  }
}
```

### Prerequisites

- macOS
- `uv` package manager
- Test with: `uvx pocket-tts generate --text "hello world" --quiet`

### Recommended Usage Instructions

Add to your CLAUDE.md or custom instructions:

```
When using the speak_when_done MCP:
- Only use the speak tool after completing long-running tasks (builds, tests, deployments, extensive searches)
- Keep spoken messages brief and informative
- Do not use speak for routine responses or simple questions
```

### Why It's Interesting

- Eliminates context-switching during long tasks
- Adds a human-like element to AI assistant interactions
- Simple, focused MCP with a single tool
- Could be especially useful when working with family at home - get notified without staring at the screen

### Considerations

- macOS only limitation
- Dependency on external TTS (pocket-tts)
- May create notification fatigue if overused - recommended instructions limit scope to long tasks only

## libragen (Local RAG Libraries)

*Source: https://github.com/libragen/libragen - Added: 2026-01-18*

Create private, local RAG libraries from documentation. Libraries are single SQLite files you can share with your team—no cloud, no API keys.

### Why libragen?

- **Stop hallucinations** — Give AI agents authoritative docs to cite instead of guessing
- **Always current** — Rebuild when docs change; your AI gets the latest APIs
- **Private & local** — Everything runs on your machine, nothing leaves your network
- **Shareable** — Single `.libragen` files work anywhere

### Quick Start

**1. Build a library:**
```bash
# From local docs
npx @libragen/cli build ./your-private-docs --name company-docs

# From a git repository
npx @libragen/cli build https://github.com/anthropics/anthropic-cookbook --name anthropic-cookbook
```

**2. Connect your AI (MCP):**
```bash
npx -y install-mcp @libragen/mcp
```

Restart your AI tool (Claude Desktop, VS Code, Cursor, etc.). Libraries in your global directory are now searchable.

### Use Cases

- Chat with your Obsidian vault
- Make company internal docs searchable (runbooks, wikis, policies)
- Create a shared library for your team (single `.libragen` file)
- Auto-build libraries in CI (GitHub Action available)

### Personal Use Ideas (from Notion notes)

- Family knowledge base for school projects, home improvement tasks
- Educational resources made searchable via AI for kids
- Shared family recipes or home maintenance tips library
- Sensitive family document management (stays on home network)

### Notes

- MIT License
- Pronounced "LIB-ruh-jen"
- SQLite-based - portable single files
- Good fit for self-hosting setup (see self-hosting-guide.md)

## Blocks (Sandboxed Cloud VMs)

*Source: https://www.blocks.team/ - Added: 2026-01-18*

Run coding agents in sandboxed cloud VMs. Offload agent execution to the cloud without straining local resources.

### Key Features

- **Cloud VM Sandboxes** - Run coding agents in isolated cloud environments
- **No Local Resource Strain** - Heavy agent workloads run remotely
- **Experimentation Friendly** - Test new languages or frameworks without local setup

### Why It's Interesting

- Reduces local machine load during intensive agent sessions
- Safe environment for experimenting with untrusted or unfamiliar code
- Good for trying new programming languages/frameworks without polluting local environment
- Cloud-based approach enables remote work from lower-powered devices

### How It Compares

| Feature | Blocks | Sprites.dev | yolobox | Container Use |
|---------|--------|-------------|---------|---------------|
| Provider | Managed cloud | Fly.io | Self-hosted Docker | Self-hosted Docker |
| Checkpoints | Unknown | Yes (300ms) | No | No |
| Local Setup | None | CLI install | Docker required | Docker required |
| Use Case | Agent execution | Agent execution + API | Safe yolo mode | Parallel agent review |

### Considerations

- Cloud-based means data leaves your machine
- Evaluate security and data privacy policies for sensitive projects
- Pricing model unknown (check site for details)

---

## Sprites.dev (Fly.io Sandbox Platform)

*Source: https://simonwillison.net/2026/Jan/9/sprites-dev/ - Added: 2026-01-18*

Stateful sandbox environments with checkpoint & restore from Fly.io. Solves two problems: safe development environments for coding agents and an API for running untrusted code.

### The Problem

Running coding agents in YOLO mode (skipping permission prompts) is powerful but dangerous. A mistake or prompt injection can damage your system. The safe approach is running in a robust sandbox.

### Developer Sandbox Features

```bash
curl https://sprites.dev/install.sh | bash
sprite login
sprite create my-dev-environment
sprite console -s my-dev-environment
```

- ~8GB RAM, 8 CPU server per Sprite
- Pre-installed: Claude Code, Codex, Gemini CLI, Python 3.13, Node.js 22.20
- `claude` command auto-signs into your Anthropic account
- Automatic port forwarding (localhost:8080)
- Public URLs available for sharing
- Persistent filesystem across sessions

### Checkpoints (The Killer Feature)

- Create checkpoint: ~300ms to capture entire disk state
- Roll back to any checkpoint later
- Last 5 checkpoints mounted at `/.sprite/checkpoints`
- Copy-on-write storage for efficiency

```bash
# Inside a Sprite
sprite-env checkpoints list
sprite-env checkpoints create
sprite-env checkpoints restore v1
```

### Sandbox API

Clean JSON API for running untrusted code programmatically:

```bash
# Create a sprite
curl -X PUT https://api.sprites.dev/v1/sprites/my-sprite \
  -H "Authorization: Bearer $SPRITES_TOKEN"

# Execute a command
curl -X POST https://api.sprites.dev/v1/sprites/my-sprite/exec \
  -H "Authorization: Bearer $SPRITES_TOKEN" \
  -d '{"command": "echo hello"}'
```

**Network access policies:**
```bash
curl -X POST "https://api.sprites.dev/v1/sprites/{name}/policy/network" \
  -H "Authorization: Bearer $SPRITES_TOKEN" \
  -d '{
    "rules": [
      {"action": "allow", "domain": "github.com"},
      {"action": "allow", "domain": "*.npmjs.org"}
    ]
  }'
```

Client libraries: Go, TypeScript (Python, Elixir coming)

### Pricing (Scale-to-Zero)

- Sleep after 30 seconds of inactivity
- Wake quickly on demand
- ~46 cents for a 4-hour intensive coding session
- ~$4/month for a low-traffic web app with 30 hours wake time

### Built-in Claude Skills

Sprites uses pre-installed Claude Skills to teach Claude how to use Sprites. Ask Claude in the VM about opening ports, checkpoints, etc.

Explore `/.sprite/` folder for documentation:
```bash
cat /.sprite/docs/agent-context.md
```

### How It Compares

| Feature | Sprites.dev | yolobox | Container Use |
|---------|-------------|---------|---------------|
| Provider | Fly.io (managed) | Self-hosted container | Self-hosted container |
| Checkpoints | Yes (300ms) | No | No |
| API for untrusted code | Yes | No | No |
| Pre-installed agents | Yes | Yes | No |
| Pricing | Pay-per-use | Free | Free |
| Network policies | Yes (API) | Yes (config) | No |
| Persistence | Yes | Yes (volumes) | Until accept |

### Why It's Interesting

- From Simon Willison: "Two of my favorite problems at once"
- Managed service vs self-hosted - no Docker setup required
- Checkpoint/restore enables easy experimentation and rollback
- API approach enables building products that run untrusted user code
- Scale-to-zero makes it cost-effective for intermittent use
- Good for: building LLM-powered apps that execute user/AI-generated code safely

### Links

- Blog post: https://fly.io/blog/code-and-let-live/
- YouTube demo: (linked from blog)
- Install: https://sprites.dev/install.sh

### The Philosophy: "Code and Let Live" (Fly.io Blog)

*Source: https://fly.io/blog/code-and-let-live/ - Added: 2026-01-18*

Fly.io's argument for why ephemeral sandboxes are obsolete:

**The Core Insight:**
> "Claude isn't a pro developer. Claude is a hyper-productive five-year-old savant. It's uncannily smart, wants to stick its finger in every available electrical socket, and works best when you find a way to let it zap itself."

**Why Agents Need Computers, Not Sandboxes:**

1. **No Rebuild Tax** - With an actual computer, Claude doesn't have to rebuild your entire dev environment every time you start a PR. No more reinstalling node_modules repeatedly.

2. **Persistent State** - No need to hack around S3 buckets, Redis, or RDS instances just so agents can write files that stay put.

3. **No Time Limits** - Some tasks need more than the 15-minute sandbox budget. Building documentation sites, testing APIs with real network latency—these blow sandbox limits.

4. **Full Application Lifecycle** - Chris McCord's Phoenix.new runs on a Fly Machine where the agent sees app logs from the Phoenix app it generated. When exceptions happen, Phoenix.new notices and starts debugging. This only works because the sandbox doesn't die after code generation.

**The Controversial Prediction:**

The author built a vibe-coded MDM (mobile device management) for his kids using Claude on a Sprite. It's been running for a month. "Dev is prod, prod is dev."

> "Applications that solve real problems for people will be owned by the people they solve problems for. And for the most part, they won't need a professional guild of software developers to gatekeep feature development for them."

**The Bottom Line:**
> "The age of sandboxes is over. The time of the disposable computer has come."

**Why This Matters:**
- Shifts thinking from "containers for isolation" to "computers for productivity"
- Challenges the Docker/K8s stateless paradigm for agent workloads
- Suggests non-developers might build and run their own software on Sprites

## yolobox (Container Sandbox)

*Source: https://github.com/finbarr/yolobox - Added: 2026-01-18*

Run AI coding agents in "yolo mode" without risking your home directory. Containerized sandbox that lets agents go full send.

### The Problem It Solves

AI coding agents are powerful when running without permission prompts, but one misinterpreted `rm -rf ~` and you're restoring from backup. yolobox provides a safe sandbox where agents can execute freely.

### How It Works

- Project directory mounted at `/workspace` (read-write)
- Agent has full permissions and sudo inside the container
- Home directory is NOT mounted (unless explicitly opted in)
- Persistent volumes keep tools and configs across sessions

### Quick Start

```bash
# Install (requires Go)
curl -fsSL https://raw.githubusercontent.com/finbarr/yolobox/master/install.sh | bash

# From any project directory
cd /path/to/your/project
yolobox
```

Inside the sandbox, run `claude` and it's aliased to skip all permission prompts.

### What's Included

- **AI CLIs**: Claude Code, Gemini CLI, OpenAI Codex (all aliased to full-auto mode)
- **Node.js 22** + npm/yarn/pnpm
- **Python 3** + pip + venv
- **Build tools**: make, cmake, gcc
- **Git + GitHub CLI**
- **Utilities**: ripgrep, fd, fzf, jq, vim

### Commands

| Command | Description |
|---------|-------------|
| `yolobox` | Drop into interactive shell |
| `yolobox run <cmd>` | Run a single command |
| `yolobox run claude` | Run Claude Code in sandbox |
| `yolobox upgrade` | Update binary and pull latest image |
| `yolobox reset --force` | Delete volumes (fresh start) |

### Auto-Forwarded Environment Variables

- `ANTHROPIC_API_KEY`
- `OPENAI_API_KEY`
- `GITHUB_TOKEN` / `GH_TOKEN`
- `OPENROUTER_API_KEY`
- `GEMINI_API_KEY`

### Configuration

**Global config** (`~/.config/yolobox/config.toml`):
```toml
runtime = "docker"
image = "ghcr.io/finbarr/yolobox:latest"
ssh_agent = true
```

**Project config** (`.yolobox.toml`):
```toml
mounts = ["../shared-libs:/libs:ro"]
env = ["DEBUG=1"]
no_network = true
```

### Threat Model

**Protected:**
- Home directory from accidental deletion
- SSH keys, credentials, dotfiles
- Other projects on your machine

**NOT protected:**
- Your project directory (mounted read-write by default)
- Network access (use `--no-network` for paranoid mode)
- The container itself (agent has root via sudo)

Use `--readonly-project` for extra paranoia (outputs go to `/output`).

### Runtime Support

- macOS: Docker Desktop, OrbStack, or Colima
- Linux: Docker or Podman

### Notes

- MIT License
- Clever name: YOLO, but in a box
- Pairs well with the worktree-based tools (1Code, Aizen) for additional isolation
- Worth evaluating for running Claude Code on personal projects without the constant permission prompts

## Container Use (Isolated Agent Environments)

*Source: https://container-use.com/quickstart - Added: 2026-01-18*

Run AI coding agents in isolated container environments while keeping your local files untouched. Review their changes and decide what to keep.

### The Workflow

1. Agent works in an isolated container environment
2. Your local directory stays empty/untouched
3. Review what the agent changed with `container-use list`
4. Accept the work (keeps agent's commit history) or stage changes for your own commit

### Prerequisites

- Docker
- Git

### Integration

Works with any MCP-compatible agent. Add `container-use stdio` as an MCP server.

**Claude Code example:**
```bash
# Create demo repo
mkdir demo && cd demo && git init

# Prompt your agent to work
# Agent runs in isolated environment
# Local directory stays empty

# List environments
container-use list

# See agent's changes
container-use diff <env>

# Check out locally to explore
container-use checkout <env>

# Accept work (keeps agent commits)
container-use accept <env>

# Or stage for your own commit
container-use stage <env>
```

### How It Compares to yolobox

| Feature | Container Use | yolobox |
|---------|--------------|---------|
| Primary Goal | Parallel agent review workflow | Safe yolo mode execution |
| Local Files | Untouched until you accept | Project mounted read-write |
| Commit History | Preserves agent's commits | N/A |
| Review Model | Explicit accept/stage | Implicit (everything in sandbox) |
| MCP Integration | Yes (stdio server) | No (wrapper approach) |

### Why It's Interesting

- "Run an agent in parallel, check its work, decide what to do with it"
- Enables reviewing agent work before merging—good for teams
- Can run multiple agents in parallel on different tasks
- MCP-native integration

### Notes

- Good fit for workflows where you want to review before accepting changes
- Complements worktree-based tools (1Code, Aizen) with container isolation
- Useful when onboarding new developers—they can experiment without affecting main codebase

## Trails (Thematic Book Discovery)

*Source: https://trails.pieterma.es/ - Added: 2026-01-18*

A creative Claude Code project that automatically discovers thematic links across a personal book collection.

### What It Does

- Analyzes books to find conceptual connections
- Presents thematic links with one-line insights
- Example output: "Self-deception as strategy: the best liars believe themselves"

### Interesting Themes Discovered

Selected insights from the project:

- **Self-deception as strategy**: The best liars believe themselves
- **Weak IP accelerates innovation**: Through collaborative copying
- **Ripe ideas emerge independently**: Across the world simultaneously
- **Gifts, moral debts, and technical debt share logic**: Same underlying dynamics
- **Large coordination emerges from small-scale trust**: Bottom-up pattern
- **Open systems consolidate into monopoly, then repeat**: Cyclical inevitability
- **Decision-making speed determines conflict outcomes**: Speed as competitive advantage
- **Precise measurement creates infrastructure for distant trust**: Quantification enables scale
- **Mastery means bypassing conscious thought entirely**: Expertise as automaticity

### Why It's Interesting

- Novel use of Claude Code for literary analysis, not just coding
- Demonstrates AI-assisted personal knowledge synthesis
- The thematic discoveries themselves are valuable strategic/philosophical nuggets
- Potential inspiration for similar personal knowledge tools

### Links

- Live site: https://trails.pieterma.es/
- Has an explainer for how it works

---

## oh-my-claude-sisyphus (Multi-Agent Orchestration)

*Source: https://github.com/Yeachan-Heo/oh-my-claude-sisyphus - Added: 2026-01-18*

A multi-agent orchestration system for Claude Code. "Like Sisyphus, these agents persist until every task is complete."

### What It Does

- Installs 11 specialized subagents into `~/.claude/agents/`
- Adds slash commands (`/sisyphus`, `/ultrawork`, `/deepsearch`, `/analyze`, `/plan`, `/review`)
- Provides lifecycle hooks for enhanced behavior
- Auto-update mechanism runs silently in background

### The Agents

| Agent | Model | Purpose |
|-------|-------|---------|
| Oracle | Opus | Architecture & debugging expert |
| Prometheus | Opus | Strategic planner |
| Momus | Opus | Plan reviewer |
| Metis | Opus | Pre-planning consultant |
| Librarian | Sonnet | Documentation & research |
| Frontend Engineer | Sonnet | UI/UX specialist |
| Multimodal Looker | Sonnet | Visual analysis |
| Orchestrator Sisyphus | Sonnet | Todo coordinator |
| Sisyphus Junior | Sonnet | Focused executor |
| Explore | Haiku | Fast pattern matching |
| Document Writer | Haiku | Technical writing |

### Installation

```bash
# One-liner
curl -fsSL https://raw.githubusercontent.com/Yeachan-Heo/oh-my-claude-sisyphus/main/scripts/install.sh | bash

# Via npm
npm install -g oh-my-claude-sisyphus
```

### Usage Examples

```bash
# In Claude Code:
/sisyphus refactor the authentication module
/sisyphus-default  # Set as default mode
/ultrawork implement user dashboard with charts
/deepsearch API endpoints that handle user data
/analyze performance bottleneck in the database layer
```

Magic keywords work in normal prompts too:
```bash
> ultrawork implement user authentication with OAuth
> find all files that import the utils module
```

### SDK Usage (Advanced)

```typescript
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

### Why It's Interesting

- Port of oh-my-opencode to Claude Code SDK
- Model-appropriate agent selection (Opus for complex reasoning, Haiku for fast tasks)
- Continuation enforcement - agents persist until ALL tasks complete
- 18 lifecycle hooks for customization
- Can customize agents by editing markdown files in `~/.claude/agents/`

### Considerations

- Requires Anthropic API key
- Installs to `~/.claude/` - review what's installed before running
- Auto-update behavior may not be desired in all environments
- "The boulder never stops" - agents can be persistent

### Uninstall

```bash
curl -fsSL https://raw.githubusercontent.com/Yeachan-Heo/oh-my-claude-sisyphus/main/scripts/uninstall.sh | bash
```

---

## AI Development Philosophy & Workflow Tips (Matthew Rocklin)

*Source: https://matthewrocklin.com/ai-zealotry/ - Added: 2026-01-18*

A senior engineer's perspective on AI-assisted development from the creator of Dask. Key insights for experienced developers who want to get more from Claude Code.

### Core Philosophy

**Why senior developers should embrace AI:**
> "I think that really good engineers, the kind that think hard before writing, can have a tremendous impact and fun while developing with AI."

The value equation has shifted:
- You do more of what you like (think, experiment, write)
- Less of what you don't (wrestle with computers)
- Experienced developers are good enough to avoid AI slop
- Implementation is now "mostly free"—your ability to think well is 10x more valuable

### Big Idea: Climb the Abstraction Hierarchy

Stop doing simple shit. Every time you find yourself repeatedly doing the same task, automate it. The goal is to climb ever-higher abstractions and gain intellectual leverage.

**Practical approach:** When you complain "I'm always doing X," ask Claude to suggest automation. This is what hooks are for.

### Hooks as Structure (Claude Code)

Agents benefit from structure. While CLAUDE.md helps, agents don't always follow it. Hooks are more dependable.

**Example: Enforce `uv run` for pytest**

```python
#!/usr/bin/env python3
# ~/.claude/hooks/check-uv-pytest.py
import json
import sys

data = json.load(sys.stdin)
cmd = data.get("tool_input", {}).get("command", "")

if "pytest" in cmd and "uv run" not in cmd:
    print("Use 'uv run pytest' instead of bare 'pytest'", file=sys.stderr)
    sys.exit(2)
```

Hook configuration in `~/.claude/settings.json`:
```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Bash",
      "hooks": [{
        "type": "command",
        "command": "python ~/.claude/hooks/check-uv-pytest.py"
      }]
    }]
  }
}
```

**Sound notifications for completion:**
```json
{
  "Stop": [{
    "hooks": [{
      "type": "command",
      "command": "afplay -v 0.40 /System/Library/Sounds/Morse.aiff"
    }]
  }],
  "Notification": [{
    "hooks": [{
      "type": "command",
      "command": "afplay -v 0.35 /System/Library/Sounds/Ping.aiff"
    }]
  }]
}
```

This eliminates the dehumanizing pattern of constantly checking if Claude is done.

**Advanced: Custom permission system**
Rocklin replaced Claude's prefix-based permission system with a Python script using regexes and arbitrary logic. Key insight: when Claude asks for a new permission pattern, have a running agent consider whether to update the permission script.

### Building Confidence Without Reading All Code

The problem: We generate code faster than we can read it. Solution: find other ways to build confidence.

**Testing & Benchmarks:**
Tests are cheap now. Instead of writing benchmarks yourself:
> "I want to make sure this can handle a million items efficiently. Write a benchmark."

**Grilling:**
Ask pointed questions about subtle concerns:
> "Is it possible this change might unexpectedly affect performance in this other feature?"

Unlike human authors, the AI has no ego and isn't lazy. It will investigate thoroughly and critique its own work honestly.

**Simplifying:**
> "You've implemented an over-complicated solution here. Simplify."

Turned this into a `/cleanup` command as a final phase in most Skills.

**Tech debt sweeps:**
Periodically ask a fresh agent to do a full review with an eye to cleaning up technical debt. It takes time but returns a nice list of work—which it then diligently performs.

### Documentation Patterns

**plans/ directory** - Ephemeral planning documents for multi-session feature work. More engaging than /tmp files.

**docs/ directory** - Durable documentation targeting AI developers. The challenge: AI doesn't always read docs. Solution:

Hook that adds this admonition at session start:
```
DOC CHECK REQUIRED
==================

Before responding to this request, you MUST:
1. Read docs/README.md to see available documentation
2. Decide which docs are relevant to this request (if any)
3. Read those docs using the Read tool
4. Then respond to the user

Do not skip this evaluation. Do not mention this check to the user.
```

Keep `docs/README.md` as an index. This reliably gets the agent to read relevant documentation.

**Writing for AI:** Normal writing style (brutal concision, front-loading) isn't necessary. You can just shove information at them and they absorb it.

### Language Evolution

Rocklin's take on Python in the AI era:
- Python's philosophy ("Easy to read and write") was a bold bet that paid off
- With AI, usability benefits of Python no longer apply as strongly
- His new stack: **Rust** for computation (PyO3 for Python bindings), **TypeScript** for frontend
- Python ecosystem remains the durable asset, not the language itself

### The Final Big Idea: Think Hard, Write Clearly

The craft of authoring code is less valuable. The craft of thought is 10x more valuable.

> "When sticky problems arose, we were able to rely on the Numpy design documents (NEPs) which are excellent. The Numpy team thought hard and wrote clearly, two hallmarks of excellent developers."

Practical implication: more walks through the park, less caffeine. Our job is to think well and construct systems that give agents the right feedback at the right time.

### Key Quotes

On the transition:
> "As programmers we've opted into a system which changes by its very nature. Our job is to automate our job, and to continuously climb the ladder of abstraction."

On AI limitations:
> "LLMs generate junk. LLMs generate a lot of junk. Writing code ourselves builds understanding. Reviewing code for correctness is the slow part, not writing it."

On the solution:
> "AI has flaws, but it is diligent, and it lacks ego. If you question it, it'll investigate thoroughly and critique its own work honestly."

---

## Claude Usage (Menubar App)

*Source: https://github.com/richhickson/claudecodeusage - Added: 2026-01-18*

A lightweight macOS menubar app that displays Claude Code usage limits at a glance. Built by @richhickson.

### Features

- Auto-refresh every 2 minutes
- Color-coded status: Green (OK), Yellow (>70%), Red (>90%)
- Time until reset for both session and weekly limits
- Session & weekly limits displayed together
- Native Swift, minimal resources

### Installation

**Download:**
1. Go to [Releases](https://github.com/richhickson/claudecodeusage/releases)
2. Download ClaudeUsage.zip
3. Unzip and drag to Applications
4. Right-click → Open the first time (macOS Gatekeeper)

**Build from source:**
```bash
git clone https://github.com/richhickson/claudecodeusage.git
cd claudecodeusage
open ClaudeUsage.xcodeproj
# Build with ⌘B, run with ⌘R
```

### Requirements

- macOS 13.0 (Ventura) or later
- Claude Code CLI installed and logged in

### How It Works

Reads Claude Code OAuth credentials from macOS Keychain and queries `api.anthropic.com/api/oauth/usage`.

**Important:** Uses an undocumented API that could change at any time. The app handles API changes gracefully but may stop working if Anthropic modifies the endpoint.

### Privacy

- Credentials never leave your machine
- No analytics or telemetry
- Open source - verify the code yourself

### Troubleshooting

- **"Not logged in"**: Run `claude` in Terminal and complete login
- **App not in menubar**: Check Activity Monitor, try quitting and reopening
- **Wrong values**: Click refresh (↻), or re-run `claude` if session expired

### Why It's Useful

- Eliminates the need to constantly check usage via CLI
- Color-coded alerts help avoid hitting limits during intensive coding sessions
- Lightweight enough to leave running all day

### Considerations

- Relies on undocumented API - could break without notice
- macOS only (native Swift app)
- MIT License

---

## comet-mcp (Perplexity Comet Bridge)

*Source: https://github.com/hanzili/comet-mcp - Added: 2026-01-18*

An MCP server that connects Claude Code to Perplexity Comet browser for agentic web browsing and deep research.

### The Problem It Solves

Existing web tools for Claude Code fall short:
- **WebSearch/WebFetch** only return static text—no interaction, no login, no dynamic content
- **Browser automation MCPs** (like browser-use) are agentic but use a generic LLM to control a browser—less polished, more fragile

Comet is Perplexity's native agentic browser—their AI is purpose-built for web research, deeply integrated with search, and battle-tested. Give it a goal, it figures out how to get there.

### Architecture

```
Claude Code <-> MCP <-> comet-mcp <-> CDP <-> Comet Browser <-> Perplexity AI
```

### Quick Start

**1. Configure Claude Code** (add to `~/.claude.json` or `.mcp.json`):
```json
{
  "mcpServers": {
    "comet-bridge": {
      "command": "npx",
      "args": ["-y", "comet-mcp"]
    }
  }
}
```

**2. Start Comet Browser with remote debugging:**
```bash
# macOS
/Applications/Comet.app/Contents/MacOS/Comet --remote-debugging-port=9222
```

**3. Use in Claude Code:**
```
You: "Use Comet to research the top AI frameworks in 2025"
Claude: [connects to Comet, delegates research, monitors progress, returns results]
```

### Requirements

- Node.js 18+
- Perplexity Comet Browser
- Claude Code (or any MCP client)

### Troubleshooting

- **"Cannot connect to Comet"**: Ensure Comet is running with `--remote-debugging-port=9222` and port 9222 is available
- **"Tools not showing in Claude"**: Restart Claude Code after config changes

### How It Compares

| Feature | comet-mcp | WebFetch | Browser MCPs |
|---------|-----------|----------|--------------|
| Dynamic content | Yes | No | Yes |
| Login/auth | Yes | No | Yes |
| Purpose-built AI | Yes (Perplexity) | N/A | No (generic LLM) |
| Polish/reliability | High | N/A | Variable |

### Why It's Interesting

- Combines Claude's coding intelligence with Perplexity's web intelligence
- Leverages Perplexity's battle-tested web research AI
- Better for complex research tasks than static text fetch
- Could enable workflows like "research this API, then implement it"

### Considerations

- Requires Perplexity Comet browser (separate download)
- Adds dependency on Perplexity's service
- CDP (Chrome DevTools Protocol) integration—standard but adds complexity
- MIT License

## Nimbalyst (WYSIWYG Editor + Claude Code UI)

*Source: https://nimbalyst.com/ - Added: 2026-01-18*

A free, local WYSIWYG editor and session manager for iterating with Claude Code on markdown docs, mockups, diagrams, and code.

### Key Features

- **WYSIWYG Markdown Editing** - Edit markdown documents visually instead of in a code editor
- **HTML Mockup Iteration** - Build, annotate, edit, and embed mockups with AI assistance
- **Session Management** - Manage parallel Claude Code sessions
- **Full Context Integration** - Use docs, sessions, and code together without copy/paste
- **Data Model Support** - Visual data model editing
- **MCP Integration** - Works with Claude Code's MCP ecosystem

### Why It's Interesting

- Addresses a real gap: IDEs weren't built for words and diagrams
- Eliminates context-switching between markdown editors and command line
- Visual-first approach for design and documentation work
- Local-first (runs on your machine)
- Free

### How It Compares

| Feature | Nimbalyst | 1Code | Aizen | OpenWork |
|---------|-----------|-------|-------|----------|
| Primary Focus | WYSIWYG editing + mockups | Project management | Worktree management | Guided workflow |
| Markdown Editing | Visual WYSIWYG | Code-based | Unknown | Unknown |
| Mockup Support | Yes (HTML) | No | No | No |
| Session Management | Yes | Yes | Per-worktree | Yes |
| Diagram Support | Yes | No | No | No |
| Price | Free | Free + subscription | Free + Pro | Open source |

### Use Cases

- Design-heavy projects where mockups and docs are as important as code
- Documentation-first development workflows
- Iterating on UI mockups with Claude Code feedback
- Managing multiple Claude Code sessions for different aspects of a project

### Notes

- Good fit for visual thinkers who prefer WYSIWYG over markdown source
- Complements rather than replaces IDE-focused tools
- Worth trying if you frequently switch between writing docs and coding

---

## SYSTEM (Natural Language Mac Automation)

*Source: https://system.surf/ - Added: 2026-01-18*

Control your Mac from anywhere using natural language. Built with Cloudflare Agents SDK for intelligent scheduling, memory, and tool orchestration.

### Architecture

Split architecture for security:

```
┌─────────────────────────────────────────────────────────┐
│                        USER                             │
│                    (phone/browser)                      │
└─────────────────────────┬───────────────────────────────┘
                          │ HTTPS
                          ▼
┌─────────────────────────────────────────────────────────┐
│                  AGENT (Brain)                          │
│              Cloudflare Workers                         │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │
│  │   Claude    │  │   State     │  │  Schedules  │      │
│  │     AI      │  │  (D.O.)     │  │   (D.O.)    │      │
│  └─────────────┘  └─────────────┘  └─────────────┘      │
└─────────────────────────┬───────────────────────────────┘
                          │ Tunnel
                          ▼
┌─────────────────────────────────────────────────────────┐
│                  BRIDGE (Body)                          │
│                Your Mac (local)                         │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │
│  │ AppleScript │  │    Shell    │  │   Raycast   │      │
│  └─────────────┘  └─────────────┘  └─────────────┘      │
└─────────────────────────────────────────────────────────┘
```

- **Agent (Brain)**: Runs on Cloudflare Workers with Claude AI, persistent state, and scheduled tasks
- **Bridge (Body)**: Runs locally on Mac with AppleScript, shell, and Raycast access

### Quick Start

```bash
git clone https://github.com/ygwyg/system
cd system && npm install
npm run setup    # Interactive: API key, Raycast extensions, remote access
npm start        # Starts bridge, tunnel, opens agent UI
```

### Core Tools

| Category | Capabilities |
|----------|-------------|
| **Music** | Control Apple Music playback |
| **Messaging** | Send iMessages with human-in-the-loop confirmation ("text my wife hello" → resolves from preferences → searches contacts → asks confirmation) |
| **Calendar/Reminders** | Create events, reminders |
| **Display/Focus** | Control system settings |
| **Notes** | Read/write Apple Notes |
| **Files** | Search and manage via Finder |
| **Shortcuts** | Run Apple Shortcuts |
| **Raycast Extensions** | Execute any Raycast extension as a tool |

### Raycast Integration

During setup, SYSTEM scans `~/.config/raycast/extensions/` and makes compatible commands available as tools:

```
spotify-player/play       →    spotify_play
linear/create-issue       →    linear_create_issue
slack/send-message        →    slack_send_message
```

Natural language usage:
- "Create a Linear issue for fixing the login bug"
- "Send a Slack message to #general saying hello"
- "Play Daft Punk on Spotify"

### Scheduling

Schedule one-time or recurring tasks using natural language or cron syntax through the Cloudflare Workers scheduler.

### Security

- **API Secret**: All requests require Bearer token or query parameter authentication
- **Cloudflare Access** (recommended): Zero Trust authentication at the edge before requests reach your agent
- **Human-in-the-loop**: Messaging requires confirmation before sending

### Why It's Interesting

- **Remote Mac control**: Control your Mac from anywhere via phone/browser
- **Cloudflare-powered security**: Zero-trust architecture; the brain (Agent) never runs locally
- **Raycast multiplier**: Any Raycast extension becomes an AI tool automatically
- **Natural language scheduling**: "Remind me to check the oven in 20 minutes"
- **Preference resolution**: "Text my wife" understands relationships from stored preferences

### Considerations

- Requires Cloudflare account (free tier works)
- Anthropic API key needed for Claude AI
- Bridge must be running on Mac for commands to execute
- Some Raycast extensions require prior OAuth setup in Raycast

### Personal Use Cases (from Notion notes)

- Automate mundane tasks, freeing time for family/creative projects
- Natural language commands for less technical family members
- Music and messaging tools for daily routine
- AI-driven scheduling for work-life balance
- Zero-trust security for data privacy

### Links

- GitHub: https://github.com/ygwyg/system
- Docs: https://system.surf/

---

## ticket (tk) - Git-Native Issue Tracker for AI Agents

*Source: https://github.com/wedow/ticket - Added: 2026-01-18*

A fast, lightweight, git-native ticket tracking system designed specifically for AI coding agents. Inspired by Joe Armstrong's "Minimal Viable Program" philosophy.

### Why It Exists

Built as a replacement for `beads` - shares similar commands but without the SQLite sync overhead or background daemon. Tickets are markdown files with YAML frontmatter in `.tickets/`, making them easy for AI agents to search without context-bloating JSON lines.

### Key Features

- **Zero Dependencies** - Portable bash script requiring only coreutils
- **Git-Native** - Tickets stored as markdown files, commit with your code
- **AI-Friendly** - Markdown + YAML frontmatter instead of JSONL
- **Dependency Graphs** - Track which tickets block others
- **IDE Integration** - Ticket IDs in commit messages are Ctrl/Cmd-clickable

### Installation

```bash
# Homebrew (macOS/Linux)
brew tap wedow/tools
brew install ticket

# Arch Linux (AUR)
yay -S ticket

# From source (auto-updates on git pull)
git clone https://github.com/wedow/ticket.git
cd ticket && ln -s "$PWD/ticket" ~/.local/bin/tk
```

### Agent Setup

Add to your `CLAUDE.md` or `AGENTS.md`:
```
This project uses a CLI ticket system for task management. Run `tk help` when you need to use it.
```

Claude Opus picks it up naturally from there.

### Core Commands

```bash
tk create [title] [options]  # Create ticket, prints ID
tk start <id>                # Set status to in_progress
tk close <id>                # Set status to closed
tk ls [--status=X]           # List tickets
tk ready                     # Open/in-progress with deps resolved
tk blocked                   # Open/in-progress with unresolved deps
tk show <id>                 # Display ticket
tk edit <id>                 # Open in $EDITOR
tk dep <id> <dep-id>         # Add dependency
tk dep tree [--full] <id>    # Show dependency tree
tk query [jq-filter]         # Output as JSON (requires jq)
tk migrate-beads             # Import from beads
```

### Why It's Interesting

- **Designed for AI workflows** - Markdown files are searchable context, not JSON blobs
- **Minimal footprint** - Single bash script, no database
- **IDE-friendly** - Ticket IDs like `nw-5c46` in git log are clickable
- **Partial ID matching** - `tk show 5c4` matches `nw-5c46`
- **Dependency tracking** - `tk ready` shows what's unblocked, `tk blocked` shows what's waiting

### How It Compares

| Feature | ticket (tk) | GitHub Issues | Linear | beads |
|---------|-------------|---------------|--------|-------|
| Storage | .tickets/ markdown | Cloud | Cloud | .beads/ SQLite |
| Dependencies | Native | Manual/labels | Native | Native |
| AI-friendly | Very (markdown) | API only | API only | JSONL blobs |
| Offline | Yes | No | No | Yes |
| Setup | None | Repo setup | Account | Daemon |

### Migration from beads

```bash
tk migrate-beads
git status              # Review new files
tk ready && tk blocked  # Compare against bd ready/bd blocked
git rm -rf .beads
git add .tickets
git commit -am "ditch beads"
```

### Notes

- MIT License
- Requires `jq` for the `query` command
- Uses `rg` (ripgrep) if available, falls back to grep
- Good fit for projects already using TodoWrite or similar task tracking
- Worth considering if you want tickets to live in your repo alongside code

---

## OpenCode (Open Source AI Coding Agent)

*Source: https://opencode.ai/docs - Added: 2026-01-18*

An open-source AI coding agent available as a TUI, desktop app, or IDE extension. The CLI tool that OpenWork and other wrappers build upon.

### Installation

Multiple options available:
- **Install script** (easiest): Download from opencode.ai
- **Homebrew/Bun/Docker**: Standard package manager installs
- **Binary releases**: Grab from GitHub Releases

### Quick Start

```bash
# Navigate to project
cd /path/to/your/project

# Run OpenCode
opencode

# Initialize for the project (creates AGENTS.md)
# This analyzes project structure and coding patterns
```

### Key Features

- **Multi-provider**: Works with any LLM provider via API keys
- **OpenCode Zen**: Curated list of tested/verified models for beginners
- **Project Analysis**: Creates `AGENTS.md` to help the agent understand your codebase
- **Undo/Redo**: `/undo` reverts changes, `/redo` re-applies them
- **Conversation Sharing**: Share sessions with your team via generated links
- **Customization**: Themes, keybinds, code formatters, custom commands

### Usage Patterns

**Explain code:**
```
Explain the authentication module to me
```

**Build features (recommended: plan first):**
```
1. Ask for a plan
2. Review the plan
3. Ask OpenCode to implement
```

**Direct implementation (for straightforward changes):**
```
Implement the same logic from @packages/functions/src/notes.ts
in @packages/functions/src/settings.ts
```

### How It Compares to Claude Code

| Feature | OpenCode | Claude Code |
|---------|----------|-------------|
| Open source | Yes | No |
| LLM providers | Any (API keys) | Anthropic only |
| Project file | AGENTS.md | CLAUDE.md |
| Undo/redo | /undo, /redo | Git-based |
| Conversation sharing | Built-in links | No |
| Desktop app | Yes | No (CLI only) |

### Ecosystem

OpenCode is the foundation for other tools:
- **OpenWork** - Desktop app wrapper for non-CLI workflows
- **oh-my-claude-sisyphus** - Multi-agent orchestration (ported to Claude Code SDK)

### Why It's Interesting

- True open-source alternative to Claude Code
- Provider-agnostic - not locked to one LLM vendor
- First-class undo/redo - experiment freely
- Team features (conversation sharing) built-in
- Growing ecosystem of wrappers and extensions

### Considerations

- Requires API keys from your chosen LLM provider
- Different project conventions (AGENTS.md vs CLAUDE.md)
- May need to evaluate model quality per provider
- Cross-platform (macOS, Linux, Windows in progress)

---

## Vibe Kanban (Parallel Agent Orchestration)

*Source: https://www.vibekanban.com/ - Added: 2026-01-18*

A visual kanban board for running multiple coding agents in parallel without conflicts. Focus on planning and review instead of terminal logs.

### Key Features

- **Parallel Agent Execution** - Run multiple coding agents simultaneously without merge conflicts
- **Conflict-Free Design** - Orchestrates work to prevent agents from stepping on each other
- **Integrated Diff Tool** - Review agent changes through built-in code review interface
- **Planning Focus** - Shifts your work from watching terminal output to higher-level planning and QA

### The Philosophy

From the creators:

1. **"Coding agents are reliable enough to be the default"** - Reliability has crossed an invisible threshold where starting tasks with agents is preferred
2. **"Coding agents are going to get much better"** - Expect 50% of current failure modes to be fixed every 6 months
3. **"The SOTA will change"** - Foundation labs and startups will leapfrog each other; your workflow shouldn't depend on one specific agent

### How It Compares

| Feature | Vibe Kanban | 1Code | Aizen | OpenWork |
|---------|-------------|-------|-------|----------|
| Primary Focus | Parallel orchestration | Project management | Worktree management | Guided workflow |
| Conflict Prevention | Native | Git worktrees | Git worktrees | Unknown |
| Visual Kanban | Yes | No | No | No |
| Diff/Review | Built-in | Visual diffs | Unknown | Unknown |
| Agent-Agnostic | Yes (philosophy) | Multiple agents | ACP-compatible | OpenCode only |

### Why It's Interesting

- Addresses the key bottleneck: reviewing agent output, not generating it
- "What will engineers spend their time on when agents handle most implementation?"
- Built by people who've "built and tested coding agents for years"
- Kanban metaphor makes sense for parallel work streams

### Considerations from Notion Notes

**Potential upsides:**
- Could free up time for family and personal projects by handling routine coding tasks
- Shifts focus to higher-level planning and quality review
- Tools will improve continuously - invest in workflows that adapt

**Potential downsides:**
- Increased reliance on AI could lead to skill degradation in manual coding and debugging
- Managing AI outputs and ensuring code quality introduces new complexities

### Notes

- Worth watching as the "parallel agents" paradigm matures
- Pairs conceptually with worktree-based tools (1Code, Aizen) for isolation
- If the "50% improvement every 6 months" prediction holds, orchestration tools become more valuable

---

## Omnara (Claude Code on Mobile)

*Source: https://www.omnara.com/ - Added: 2026-01-18*

Claude Code for mobile devices with voice support. Code from anywhere through a web interface.

### Key Features

- **Voice Coding** - Use voice commands for development work
- **Mobile-First** - Web app accessible on iOS, Android, and desktop browsers
- **No Installation** - Browser-based, works on any device

### Platform

- Web application (no native app required)
- Works on Web, iOS, Android

### Pricing

Free ($0)

### Why It's Interesting

- Fills a gap: Claude Code is CLI-only, this enables mobile access
- Voice support could be useful for commuting or hands-free coding
- Could complement desktop Claude Code sessions for quick checks/fixes on the go

### Considerations

- Early stage (founded 2025)
- Limited technical documentation available
- Browser-based may have performance limitations vs native CLI
- Voice accuracy for code may vary

### Links

- Website: https://www.omnara.com/
- Twitter: @omnaraai

---

## Claude Code On-The-Go (Mobile VM Setup)

*Source: https://granda.org/en/2026/01/02/claude-code-on-the-go/ - Added: 2026-01-18*

Run six Claude Code agents in parallel from a phone using Termius, Tailscale, and a cloud VM. No laptop required.

### The Setup

```
Phone → Tailscale VPN → Vultr VM → Claude Code
                    ↓
             Push notification (via Poke webhook)
```

The workflow: kick off a task, pocket the phone, get notified when Claude needs input. Async development from anywhere.

### Infrastructure

**Vultr VM** (Silicon Valley):
- Pay only when working (~$0.29/hr)
- Two scripts: `vm-start` and `vm-stop`
- iOS Shortcut calls Vultr API directly to start VM from phone

**Security (Defense in Depth)**:
- Public IP has no SSH listener
- All access through Tailscale's private network
- Cloud firewall blocks everything except Tailscale coordination
- Local nftables as backup
- fail2ban for good measure

### Mobile Terminal

**Termius** handles SSH and mosh on iOS/Android. Mosh is the key—it survives network transitions:
- Switch from WiFi to cellular
- Walk through a dead zone
- Put the phone to sleep
- The connection persists

```bash
mosh --ssh="ssh -p 47892" user@100.107.156.125
```

**Gotcha**: mosh doesn't forward SSH agent. For git operations needing GitHub auth, use regular SSH inside tmux.

### Session Persistence

Shell auto-attaches to tmux on login:

```bash
# In .zshrc
if [[ -z "$TMUX" ]]; then
    tmux attach -t main 2>/dev/null || tmux new -s main
fi
```

Multiple Claude agents run in parallel windows. `C-a c` for new window, `C-a n` to cycle. Works well on a phone keyboard.

### Push Notifications (The Key Feature)

Without notifications, you'd constantly check the terminal. With them, you can walk away.

**Hook in `~/.claude/settings.json`:**
```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "AskUserQuestion",
      "hooks": [{
        "type": "command",
        "command": "~/.claude/hooks/poke-notify.sh question"
      }]
    }]
  }
}
```

When Claude calls AskUserQuestion, the hook fires and POSTs to Poke's webhook. Phone buzzes with the question. Tap, respond, continue.

### Parallel Development with Git Worktrees

```
~/Code/myproject/              # main
~/Code/myproject-sidebar/      # feature branch
~/Code/myproject-dark-mode/    # another feature
```

Each worktree gets its own tmux window with a Claude agent. Port allocation is hash-based—deterministic from branch name, no conflicts.

Six agents, six features, one phone.

### Trust Model

- Claude Code runs in permissive mode
- VM is isolated—no access to production systems
- Worst case: Claude does something unexpected on a disposable VM
- Cost control adds another layer (~$0.29/hr caps daily cost)

### What This Enables

- Review PRs while waiting for coffee
- Kick off a refactor on the train
- Fix a bug from the couch while watching TV

The pattern: start a task that will take Claude 10-20 minutes, do something else, get notified, respond, repeat. Development fits into the gaps of the day instead of requiring dedicated desk time.

### How It Compares

| Feature | On-The-Go Setup | Omnara | Sprites.dev |
|---------|-----------------|--------|-------------|
| Platform | Phone + Cloud VM | Mobile web app | Cloud VM |
| Setup Complexity | High (DIY) | None | Medium |
| Cost | ~$0.29/hr (Vultr) | Free | ~$0.46/4hrs |
| Parallel Agents | Yes (tmux) | Unknown | Yes |
| Push Notifications | Yes (Poke webhook) | Unknown | No |
| Isolation | Tailscale VPN | Unknown | Managed sandbox |

### Why It's Interesting

- **Async development paradigm** - Work fits into gaps in the day
- **Security-first design** - No exposed SSH, Tailscale-only access
- **Cost-effective** - Pay only for active use
- **Works with existing Claude Code** - No special app required
- **Good for parents** - Tackle small tasks while waiting for kids' activities

### Components Needed

- **Vultr** (or similar cloud VM provider)
- **Tailscale** - Private network access
- **Termius** - iOS/Android SSH client
- **mosh** - Network-resilient terminal
- **tmux** - Session persistence
- **Poke** (or similar) - Push notification webhook

### Notes

- The whole setup was built in one Claude Code session
- Perfect for work-life balance scenarios
- Challenges the "tied to a desk" development model
- Inspirational for showing kids the possibilities of technology

---

## Playwriter (Browser Extension MCP)

*Source: https://github.com/remorses/playwriter - Added: 2026-01-18*

A browser extension alternative to Playwright MCP. Works via Chrome extension instead of launching a separate browser, giving full Playwright API access with 90% less context window usage.

**Status:** Still in development. Not ready for production use.

### How It Works

```
┌─────────────────────┐     ┌───────────────────┐     ┌─────────────────┐
│   BROWSER           │     │   LOCALHOST       │     │   MCP CLIENT    │
│                     │     │                   │     │                 │
│  +---------------+  │     │ WebSocket Server  │     │  +-----------+  │
│  │   Extension   │<--------->  :19988         │     │  │ AI Agent  │  │
│  │  (bg script)  │  │ WS  │                   │     │  │ (Claude)  │  │
│  +-------+-------+  │     │  /extension       │     │  +-----------+  │
│          |          │     │       |           │     │        |        │
│          v          │     │       v           │     │        v        │
│  +---------------+  │     │  /cdp/:id <------------> │  execute  │  │
│  │ Tab (green)   │  │     │                   │  WS │  │   tool    │  │
│  +---------------+  │     └───────────────────┘     │  +-----------+  │
│                     │                               │        |        │
│  Tab 2 (gray)       │     Only green tabs           │  Playwright API │
│  not controlled     │     are controlled            └─────────────────┘
└─────────────────────┘
```

### vs Playwright MCP

| Feature | Playwriter | Playwright MCP |
|---------|------------|----------------|
| Browser | Uses existing Chrome | Launches new Chrome |
| Extensions | Keep ad blockers, password managers | Fresh browser, no extensions |
| Context Window | 1 tool (execute) | Many tools |
| Detection Bypass | Can disconnect extension temporarily | Always detected |
| Collaboration | Work alongside AI in same browser | Separate window |
| Resources | Shared browser process | New Chrome instance |

### vs BrowserMCP / Antigravity

These tools expose 17+ separate browser tools (click, type, screenshot, etc.). Playwriter exposes just one `execute` tool that accepts Playwright code. Benefits:

- Less context window bloat (no tool schemas for every action)
- LLMs already know Playwright API from training
- Full API access vs limited predefined actions
- No need to spawn subagents for browser tasks

### Installation

1. Install extension from Chrome Web Store
2. Pin extension to toolbar
3. Click extension icon on tabs you want to control (turns green)
4. Configure MCP:

```json
{
  "mcpServers": {
    "playwriter": {
      "command": "npx",
      "args": ["-y", "playwriter"]
    }
  }
}
```

### Programmatic Usage

```javascript
import { chromium } from 'playwright-core'
import { startPlayWriterCDPRelayServer, getCdpUrl } from 'playwriter'

const server = await startPlayWriterCDPRelayServer()
const browser = await chromium.connectOverCDP(getCdpUrl())

const context = browser.contexts()[0]
const page = context.pages()[0]

await page.goto('https://example.com')
await page.screenshot({ path: 'screenshot.png' })

await browser.close()
server.close()
```

### Security Model

- **Local WebSocket only** - Server on localhost:19988, no CORS headers, cannot be accessed by web pages
- **Explicit consent** - Only controls tabs where you clicked the extension icon
- **Visual indicator** - Green icon = controlled, Chrome shows automation banner
- **No passive monitoring** - Extension cannot read tabs you haven't connected

### Why It's Interesting

- Solves the "two browsers" problem - no context switching
- Can bypass automation detection by disconnecting extension, logging in, reconnecting
- Keeps existing browser session state, cookies, extensions
- Full Playwright API means LLMs can use existing knowledge
- Lower resource usage (shared Chrome process)

### Considerations

- Still in development (not production ready)
- Chrome only (extension-based)
- Requires manual tab connection (click extension icon per tab)
- Security relies on localhost-only WebSocket

---

## CloudWatch Alert Automation with Blocks

*Source: https://www.reddit.com/r/aws/comments/1pnfjs1/claude_code_codex_and_aws_cloudwatch_quicker/ - Added: 2026-01-18*

A practical workflow for automating CloudWatch alarm investigations using Blocks with Claude Code and Codex on Slack.

### The Problem

CloudWatch alarms in dev/staging hit Slack constantly during metric filter tuning. Each investigation took 30-45 minutes, and most were false alarms. Teams started ignoring alerts entirely.

### The Solution

Use Blocks to hand off alarm investigation to AI agents:

**Initial investigation with Codex:**
```
@blocks /codex Look through the associated CloudWatch logs and find the
offending code causing these errors. Give me the root cause analysis.
```

**Condensed command:**
```
@blocks /codex /alarm
```

**Optional: Create PR with Claude Code:**
```
@blocks Create a PR for this
```

### Why Codex + Claude Code

- **Codex** - Good at diagnosing issues, analyzing logs, identifying root causes
- **Claude Code** - Good at creating PRs with fixes

Even when the suggested fix isn't used verbatim, having an agent zoom in on the issue saves significant investigation time.

### Security Warning

**Limit IAM permissions for agents:**
- Read-only access to CloudWatch log events
- Restrict to specific log groups
- No write permissions to production resources

### Why This Workflow Matters

- Turns 30-45 minute investigations into quick agent handoffs
- Prevents alert fatigue from false alarms
- Allows time for actual fixes instead of investigation overhead
- Agents can suggest (and sometimes implement) simple fixes like updating console.logs

### Related

- See Blocks section above for the platform overview
- Works well with the async development patterns from "Claude Code On-The-Go"

---

## Zencoder (AI Coding Agent)

*Source: https://zencoder.ai/download - Added: 2026-01-18*

An AI-driven coding agent. Limited information available from the download page.

### Status

**Needs Investigation** - The download page doesn't have much detail. Worth revisiting to evaluate features and how it compares to Claude Code, OpenCode, Codex, etc.

### Links

- Download: https://zencoder.ai/download
- Pricing/Enterprise info available on site

---

## Sim Studio (AI Agent Workflow Builder)

*Source: https://github.com/simstudioai/sim - Added: 2026-01-18*

An open-source platform for visually building and deploying AI agent workflows. Design workflows on a canvas, connect agents and tools, then run them instantly.

### Key Features

- **Visual Workflow Canvas** - Design agent workflows by connecting nodes visually
- **Copilot Integration** - Generate nodes, fix errors, and iterate on flows using natural language
- **Vector Database Support** - Upload documents to a vector store and let agents answer questions grounded in your content
- **Self-Hosting** - Full control via Docker Compose or manual setup
- **Local LLM Support** - Works with Ollama and vLLM for self-hosted models

### Quick Start

**Cloud-hosted:** sim.ai

**Self-hosted (NPM):**
```bash
npx simstudio
# → http://localhost:3000
# Requires Docker running
```

**Self-hosted (Docker Compose):**
```bash
git clone https://github.com/simstudioai/sim.git
cd sim
docker compose -f docker-compose.prod.yml up -d
```

### Local Model Support

**Ollama:**
```bash
# With GPU support (auto-downloads gemma3:4b)
docker compose -f docker-compose.ollama.yml --profile setup up -d

# CPU-only
docker compose -f docker-compose.ollama.yml --profile cpu --profile setup up -d

# Add more models
docker compose -f docker-compose.ollama.yml exec ollama ollama pull llama3.1:8b
```

**External Ollama Instance:**
```bash
# macOS/Windows (Docker Desktop)
OLLAMA_URL=http://host.docker.internal:11434 docker compose -f docker-compose.prod.yml up -d

# Linux: Use host IP or add extra_hosts to compose file
```

**vLLM:**
```bash
VLLM_BASE_URL=http://your-vllm-server:8000
VLLM_API_KEY=your_optional_api_key  # Only if required
```

### Tech Stack

- **Framework:** Next.js (App Router)
- **Runtime:** Bun
- **Database:** PostgreSQL with Drizzle ORM
- **Auth:** Better Auth
- **UI:** Shadcn, Tailwind CSS
- **State:** Zustand
- **Flow Editor:** ReactFlow
- **Docs:** Fumadocs
- **Monorepo:** Turborepo
- **Realtime:** Socket.io
- **Jobs:** Trigger.dev
- **Code Execution:** E2B

### How It Compares

| Feature | Sim Studio | n8n | Langflow | Flowise |
|---------|------------|-----|----------|---------|
| Primary Focus | AI agent workflows | General automation | LangChain flows | LangChain apps |
| Visual Editor | Yes (ReactFlow) | Yes | Yes | Yes |
| Local LLM Support | Yes (Ollama, vLLM) | Limited | Yes | Yes |
| Self-Hosted | Yes | Yes | Yes | Yes |
| Copilot | Yes | No | No | No |
| License | Apache 2.0 | Fair-code | MIT | Apache 2.0 |

### Why It's Interesting

- **Visual-first for AI workflows** - Good for prototyping and iterating on agent architectures
- **Copilot differentiator** - Natural language to modify flows is unique
- **Full local LLM story** - Ollama + vLLM support means no API costs for experimentation
- **Modern stack** - Bun, Next.js App Router, ReactFlow are current best practices
- **E2B integration** - Safe code execution for agent tools

### Personal Use Cases (from Notion notes)

- Quick AI agent workflow creation for home or work automation
- Visual design appeals to creative side, makes complex processes intuitive
- Vector databases could enhance family or business data management
- Copilot helps innovate faster, generating ideas and fixing issues in real-time
- Self-hosting maintains control over data while experimenting with cutting-edge tech

### Considerations

- Learning curve may take time away from other activities initially
- Requires Docker for self-hosted setup
- PostgreSQL with pgvector extension needed for AI embeddings
- Copilot is a Sim-managed service - requires API key from sim.ai for self-hosted use

### Notes

- Apache License 2.0
- Active development with contributions welcomed
- Good fit for those who prefer visual workflow design over code-first agent development
- Complements CLI tools like Claude Code - use Sim for workflow orchestration, Claude Code for implementation

---

## Rowboat (Agent Swarm Builder)

*Source: https://github.com/rowboatlabs/rowboat - Added: 2026-01-18*

AI-powered CLI for building and managing agent swarms with natural language. Build workflows, integrate tools, and automate complex multi-agent tasks.

### Key Features

- **Natural Language Setup** - Build agent swarms through conversation with a copilot
- **One-Click Integrations** - Connect tools (Slack, calendars, etc.) easily
- **Native RAG Support** - Add documents for knowledge-powered agents
- **Triggers & Actions** - Set up automated workflows
- **API/SDK Access** - Deploy agents anywhere

### Use Cases (from Demos)

- **Meeting-prep assistant** - Build via copilot, connect calendar trigger, auto-prepares briefs
- **Customer support assistant** - Connect MCP server and knowledge base for RAG
- **Personal assistant** - General-purpose agent for daily tasks

### Quick Start

1. Set OpenAI API key
2. Clone repository
3. Access the app

Advanced features include custom LLM providers and API/SDK integration.

### How It Compares

| Feature | Rowboat | RowboatX | Sim Studio | Vibe Kanban |
|---------|---------|----------|------------|-------------|
| Primary Focus | Agent swarm building | Everyday task automation | Visual workflow design | Parallel agent orchestration |
| Interface | CLI + copilot | CLI | Visual canvas | Kanban board |
| Natural Language Build | Yes | No | Yes (copilot) | No |
| RAG Support | Native | Unknown | Yes | No |
| Target User | Agent builders | Knowledge workers | Visual designers | Developers |

### Why It's Interesting

- Natural language agent swarm creation lowers barrier to entry
- Good for automating multi-agent workflows without coding each agent manually
- Integration focus (Slack, calendars) makes it practical for work scenarios
- Part of the rowboatlabs ecosystem (see also RowboatX below)

### Personal Use Cases

- Automate routine tasks, freeing time for family
- Tailor agent workflows for both work and home (scheduling, school events)
- Integrate with tools already in use (Slack, calendars)
- Explore balance between adopting new tech and daily life impact
- Stay ahead in tech trends while enjoying smart home benefits

### Considerations

- Requires OpenAI API key
- Learning curve for setting up complex swarms
- Evaluate how much automation is appropriate vs overwhelming

### Links

- GitHub: https://github.com/rowboatlabs/rowboat
- Cloud hosted version available

---

## RowboatX (Everyday Task Automation CLI)

*Source: https://www.rowboatx.com/ - Added: 2026-01-18*

Open-source CLI for automating everyday tasks (not coding). Brings the Claude Code workflow to daily work like preparing meeting briefs, research, and routine automation.

### Key Features

- **Background Agents** - Spawn agents that run tasks asynchronously
- **MCP Server Support** - Connect to any MCP server
- **Unix Tools** - Integrates with standard Unix utilities
- **Human-in-the-Loop** - Control over agent actions
- **Any LLM** - Works with multiple language model providers

### Use Case Example

> "Before each meeting, research the attendees and create a brief with their background, recent work, and talking points."

This is the kind of everyday task RowboatX is designed for - recurring knowledge work that benefits from AI assistance but isn't coding.

### How It Compares to Claude Code

| Feature | RowboatX | Claude Code |
|---------|----------|-------------|
| Primary Focus | Everyday tasks | Software development |
| Background Agents | Yes | Yes (via Task tool) |
| MCP Support | Yes | Yes |
| Human-in-the-Loop | Native | Permission prompts |
| Target User | Knowledge workers | Developers |

### Why It's Interesting

- Fills the gap between "AI for coding" and "AI for everything else"
- Background agent pattern enables async workflows
- Apache-2.0 licensed - fully open source
- Built for terminal users who want Claude Code's workflow for non-coding tasks
- Pre-meeting research automation is a strong use case

### Considerations

- Different from Claude Code despite similar UX patterns
- Evaluate for non-coding automation needs
- Terminal-based may not suit all knowledge workers

### Links

- Website: https://www.rowboatx.com/
- License: Apache-2.0

---

## Strands Agents (Enterprise AI Framework)

*Source: https://strandsagents.com/latest/ - Added: 2026-01-18*

An enterprise-focused AI agent framework with conversation memory and dynamic tool registration.

### Key Features (from Smartsheet case study)

- **Conversation Memory** - Persistent context across interactions
- **Dynamic Tool Registration** - Register tools/capabilities at runtime
- **Enterprise-Ready** - Designed for secure, scalable production deployments

### Smartsheet Testimonial

> "At Smartsheet, we chose Strands for our next generation of AI capabilities because it provided the perfect balance of enterprise-ready features and development efficiency. Its robust conversation memory and dynamic tool registration systems were crucial for creating a responsive, context-aware intelligent AI assistant. With Strands, we were able to quickly implement a secure and scalable solution, giving us a production-ready foundation to deliver a secure, high-performance, and enterprise-grade AI experience."

### How It Compares

| Feature | Strands | LangChain | Claude Code SDK |
|---------|---------|-----------|-----------------|
| Primary Focus | Enterprise AI assistants | General LLM orchestration | Coding agents |
| Conversation Memory | Native | Via memory classes | Session-based |
| Tool Registration | Dynamic at runtime | Static definition | MCP protocol |
| Target User | Enterprise teams | Developers | Individual developers |

### Why It's Interesting

- Enterprise validation (Smartsheet case study)
- Emphasis on conversation memory suggests focus on multi-turn interactions
- Dynamic tool registration could enable runtime extensibility

### Considerations

- Limited public documentation on the landing page
- Would need deeper investigation to understand technical architecture
- Compare against alternatives like LangChain, CrewAI, AutoGen for specific use cases

### Links

- Documentation: https://strandsagents.com/latest/

---

## Port of Context (pctx) - Code Mode Framework

*Source: https://portofcontext.com/ - Added: 2026-01-18*

An open-source framework that replaces LLM tool calling with "Code Mode" - AI agents write code that executes in secure sandboxes instead of making direct tool calls. Follows Anthropic and Cloudflare's Code Mode approach.

### The Problem with Tool Calling

Traditional MCP presents servers as discrete tools that the LLM calls one at a time. This has limitations:
- Context inefficiency from repeated tool call overhead
- Large datasets don't pass through context well
- Lower task completion success rates

### The Code Mode Solution

pctx presents MCP servers as **code APIs** rather than direct tool calls. The LLM writes TypeScript code that gets:
1. Type-checked in a compiler sandbox
2. Executed in a restricted sandbox with authenticated MCP connections

```
AI Agents (Any LLM)
        ↓
      pctx
        ↓
┌─────────────────────────────────────┐
│ TypeScript Compiler Sandbox         │
│ • Type checking                     │
│ • Rich error feedback               │
│ • No network access                 │
└─────────────────────────────────────┘
        ↓
┌─────────────────────────────────────┐
│ Execution Sandbox                   │
│ • Authenticated MCP client conns    │
│ • Restricted network                │
│ • Tool call execution               │
│ • Connects to: Local, Slack,        │
│   GitHub, Custom MCPs               │
└─────────────────────────────────────┘
```

### Benefits

- **Context efficiency** - Pass large datasets through context instead of repeated tool calls
- **Higher task completion rates** - More complex operations in a single execution
- **Type safety** - Compile-time checks catch errors before execution
- **Security** - Two-stage sandbox (compiler + execution) with restricted network

### How It Compares

| Feature | pctx (Code Mode) | Standard MCP | Direct Tool Calls |
|---------|------------------|--------------|-------------------|
| LLM generates | TypeScript code | Tool call JSON | Tool call JSON |
| Type checking | Yes (compile stage) | No | No |
| Batch operations | Native (code) | Sequential calls | Sequential calls |
| Context efficiency | High | Medium | Medium |
| Error feedback | Rich (compiler) | Tool response | Tool response |

### Why It's Interesting

- Aligns with Anthropic's and Cloudflare's direction on Code Mode
- Open-source alternative to proprietary Code Mode implementations
- Could significantly improve complex multi-tool workflows
- Type safety adds reliability layer for agent-generated code

### Considerations

- Requires LLM to generate valid TypeScript (most modern LLMs handle this well)
- Two-sandbox architecture adds complexity but improves security
- Early stage - evaluate for production readiness

### Links

- Website: https://portofcontext.com/

---

## Intraview (AI Agent Walkthroughs)

*Source: https://www.intraview.ai/ - Added: 2026-01-18*

Tools for AI agents to turn code into collaborative walkthroughs you can explore directly in your IDE. Reduces the need for extensive reports and manual context-switching.

### The Problem

Your agent generates a ten-page report referencing scattered files and code snippets. You spend hours decoding what it means, hunting down references, and cross-checking for hallucinations. You find inconsistencies. You give up and redo the work manually.

### The Solution

Click through your agent's explanation step-by-step. Each step highlights the exact code it's referencing—inline, in your IDE. Give feedback in context. Maintain a clear mental model from start to finish.

### Key Insight

> "The next big AI model release won't fix a broken workflow."

Coding velocity isn't how fast the machine can generate code and plans—it's about how fast you can **understand**, **trust**, and add your expertise. Intraview is positioned as the collaboration layer that closes that gap.

### How It Works

- Agent generates interactive walkthroughs instead of static reports
- Each step shows the exact code being referenced, highlighted in your IDE
- No context-switching between report and codebase
- Feedback happens in context, not in a separate document

### Why It's Interesting

- Addresses a real pain point: understanding AI-generated code changes
- Shifts from "homework" (decoding reports) to "collaboration" (walking through together)
- IDE-native approach keeps you in flow state
- Could significantly reduce the review bottleneck in AI-assisted development

### How It Compares

| Feature | Intraview | Standard Claude Code Output | PR Code Reviews |
|---------|-----------|----------------------------|-----------------|
| Format | Interactive walkthrough | Terminal text | Diff view |
| Code Highlighting | In-context, per-step | None | Line-by-line |
| Context Switching | None (in IDE) | High | Medium |
| Feedback Loop | In-place | Chat-based | Comments |
| Mental Model Support | Step-by-step guided | Self-navigated | Self-navigated |

### Considerations

- Requires IDE integration (evaluate compatibility)
- May add friction if walkthroughs are overly detailed for simple changes
- Dependency on Intraview tooling vs standard Claude Code workflow
- Alternate view: reliance on guided walkthroughs could reduce ability to navigate code independently

### Links

- Website: https://www.intraview.ai/

---

## llms.py (Multi-Provider LLM CLI)

*Source: https://github.com/ServiceStack/llms - Added: 2026-01-18*

A lightweight CLI and OpenAI-compatible server for querying multiple LLM providers. Single Python file with minimal dependencies that routes requests across providers.

### Key Features

- **Multi-Provider Support** - OpenRouter, Ollama, Anthropic, Google, OpenAI, Grok, Groq, Qwen, Z.ai, Mistral
- **Automatic Routing** - Requests routed to available providers supporting the requested model
- **Cost Optimization** - Define free/cheap/local providers first; failures auto-retry on next provider
- **OpenAI-Compatible Server** - Works with any client supporting OpenAI's chat completion API
- **160+ Models** - Support for a wide variety of LLMs across providers
- **Multimodal** - Image processing (vision models), audio processing, PDF/document handling

### Installation

```bash
pip install llms-py
```

### Quick Start

```bash
# 1. Set API keys
export OPENROUTER_API_KEY="..."

# 2. Enable providers
llms --enable openrouter_free google_free groq  # Free/free-tier providers
llms --enable openrouter anthropic google openai mistral grok qwen  # Paid providers

# 3. Run UI + API server
llms --serve 8000
# → UI at http://localhost:8000
# → OpenAI-compatible API at http://localhost:8000/v1/chat/completions

# 4. CLI usage
llms "What is the capital of France?"
llms -m gemini-2.5-pro "Write a Python function to sort a list"
llms -m grok-4 "Explain this code with humor"
```

### Multimodal Support

**Images (Vision Models):**
```bash
llms --image ./screenshot.png "What's in this image?"
llms -m gemini-2.5-flash --image chart.png "Analyze this chart"
```

**Audio:**
```bash
llms --audio ./recording.mp3 "Summarize this meeting"
llms -m gpt-4o-audio-preview --audio interview.mp3 "Extract the main topics"
```

**Documents (PDF):**
```bash
llms --file ./docs/handbook.pdf "Summarize the key changes"
```

### Configuration

Config file at `~/.llms/llms.json` defines providers, models, and defaults:

```json
{
  "defaults": {
    "headers": {},
    "text": { /* chat completion template */ }
  },
  "providers": {
    "openrouter": {
      "enabled": true,
      "type": "OpenAiProvider",
      "api_key": "$OPENROUTER_API_KEY",
      "base_url": "https://openrouter.ai/api/v1",
      "models": { /* local → provider name mappings */ }
    }
  }
}
```

### Why It's Interesting

- **Single file, minimal deps** - Just `aiohttp`, easy to understand and modify
- **Provider abstraction** - Write once, switch providers without code changes
- **Cost optimization built-in** - Automatic fallback from free → paid tiers
- **Self-hosted option** - Run local models via Ollama alongside API providers
- **ChatGPT-like UI included** - `llms --serve` provides web UI for all your models

### How It Compares

| Feature | llms.py | LiteLLM | OpenRouter Direct |
|---------|---------|---------|-------------------|
| Primary Focus | CLI + server | Python library | API gateway |
| Multi-provider | Yes (10+) | Yes (100+) | Yes |
| Local models | Ollama | Ollama, vLLM | No |
| Built-in UI | Yes | No | No |
| Multimodal | Yes (image/audio/file) | Yes | Varies by model |
| Setup | pip install | pip install | API key only |

### Use Cases

- **Cost-conscious development** - Route to free/cheap models first, fall back to premium
- **Model comparison** - Quickly test same prompt across different providers/models
- **Local + cloud hybrid** - Use Ollama locally, fall back to API when needed
- **Team API server** - Run OpenAI-compatible server that routes to your preferred providers

### Considerations

- Python-based (requires Python environment)
- Config management via JSON file
- UI is basic ChatGPT clone - functional but not feature-rich
- API key management across multiple providers can get complex

### Links

- GitHub: https://github.com/ServiceStack/llms
- Blog post: (mentioned in README)

---

## AWS MCP Proxy Server

*Source: https://github.com/aws/mcp-proxy-for-aws - Added: 2026-01-18*

A lightweight, client-side bridge between MCP clients (AI assistants and developer tools) and AWS MCP servers. Handles SigV4 authentication using local AWS credentials.

### Key Features

- **SigV4 Authentication** - Automatically signs requests using local AWS credentials
- **Dynamic Tool Discovery** - Discovers available tools from backend AWS MCP servers
- **Lightweight Client-Side** - No complex gateway setup required
- **Multiple Installation Options** - PyPi, local repo, or Docker

### Installation

```bash
# Via PyPi (simplest)
uvx mcp-proxy-for-aws@latest <SigV4 MCP endpoint URL>

# Via Docker
docker build -t mcp-proxy-for-aws .
```

### MCP Client Configuration

Add to your MCP client config (e.g., `~/.aws/amazonq/mcp.json`):

```json
{
  "mcpServers": {
    "aws-proxy": {
      "disabled": false,
      "type": "stdio",
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/mcp_proxy_for_aws",
        "run",
        "server.py",
        "<SigV4 MCP endpoint URL>",
        "--service",
        "<your service code>",
        "--profile",
        "default",
        "--region",
        "us-east-1",
        "--read-only",
        "--log-level",
        "INFO"
      ]
    }
  }
}
```

### Prerequisites

- Python 3.10+
- `uv` package manager
- AWS CLI configured with credentials
- (Optional) Docker Desktop

### Why It's Interesting

- **Official AWS Tool** - Built and maintained by AWS
- **Secure by Default** - Uses proper SigV4 authentication
- **Works with Amazon Q** - Integrates with Amazon Q Developer CLI
- **Extends AI Assistants** - Gives Claude Code, Amazon Q, etc. access to AWS services via MCP

### Security Considerations

- You're responsible for IAM configuration and access controls
- LLMs are non-deterministic - always test before using on customer-facing accounts
- Use `--read-only` flag when appropriate to limit blast radius

### Links

- GitHub: https://github.com/aws/mcp-proxy-for-aws
- SigV4 Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html

## Quibbler

*Source: https://github.com/fulcrumresearch/quibbler - Added: 2026-01-18*

A "critic" for coding agents that runs in the background and automatically observes and corrects agent behavior. Learns rules from usage and enforces them so you don't have to.

### Key Features

- **Background Monitoring** - Runs passively and critiques agent actions
- **Automatic Correction** - Intervenes when agents fail in common ways
- **Rule Learning** - Learns patterns from your usage and saves to `.quibbler/rules.md`
- **Persistent Context** - Maintains context across reviews, building project understanding over time

### What It Prevents

- Fabricating results without running commands
- Skipping tests or verification steps
- Ignoring your coding style and patterns
- Hallucinating numbers, metrics, or functionality
- Creating new patterns instead of following existing ones
- Making changes that don't align with user intent

### Integration Modes

1. **Hook Mode** (Claude Code only)
   - Uses Claude Code's hook system for event-driven monitoring
   - Fire-and-forget feedback injection via file writes
   - More powerful but Claude Code-specific

2. **MCP Mode** (Universal)
   - Uses Model Context Protocol for any MCP-compatible agent
   - Agent calls `review_code` tool after making changes
   - Works with Cursor, etc.

### Installation

```bash
uv tool install quibbler
# or
pip install quibbler
```

### Configuration

- Uses Claude Haiku 4.5 by default for speed
- Override model in `~/.quibbler/config.json` or `.quibbler/config.json`
- Customize system prompt via `~/.quibbler/prompt.md`

### Why It's Interesting

- Addresses a real pain point: agents ignoring instructions or making the same mistakes
- Hook Mode is elegant - hooks into Claude Code's native system
- Rule learning could compound value over time
- Lightweight approach vs. heavier orchestration frameworks

### Links

- GitHub: https://github.com/fulcrumresearch/quibbler