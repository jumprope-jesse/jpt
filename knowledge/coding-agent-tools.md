# Coding Agent Tools & UIs

Tools and interfaces for running AI coding agents.

---

## Double - AI Coding Copilot for VS Code

*Source: https://docs.double.bot/introduction - Added: 2026-01-20*

AI coding assistant from a YC-backed team emphasizing craftsmanship and attention to detail. VS Code only for now.

### Key Features

- **Chat** - GPT-4o or Claude 3.5 Sonnet in sidebar with code context
- **CodeSnap** - Generate and apply code changes with one click
- **Autocomplete** - Tab-based code suggestions
- **Inline Edit** - Cmd-based code modifications within editor
- **Custom Instructions** - Personalize AI responses
- **Multiple Models** - Access to latest AI models, updated frequently

### Platform Support

- **Current**: VS Code only
- **Waitlist**: JetBrains, Neovim

### Notes

- Emphasis on UI polish and craftsmanship differentiator
- Keeping up with model updates (had Sonnet 3.5 2024-10-22 on release day)
- Similar feature set to Cursor but as VS Code extension rather than fork

---

## vm0 - Scheduled AI Workflow Runner

*Source: https://github.com/vm0-ai/vm0 - Added: 2026-01-19*

Cloud platform for running natural language-described AI agent workflows automatically, on schedule, and in secure sandbox environments.

### Key Features

- **Cloud Sandboxes** - Run Claude Code, Codex, or other agents in isolated containers
- **60+ Skills** - Pre-built integrations: GitHub, Slack, Notion, Firecrawl, and more
- **Scheduled Execution** - Run workflows on a schedule ("while you sleep")
- **Session Persistence** - Continue chat, resume, fork, and version workflow sessions
- **Full Observability** - Logs, metrics, and network visibility for every run
- **Multi-Agent Support** - Claude Code, Codex (with Gemini CLI, DeepAgent CLI, OpenCode coming soon)

### Quick Start

```bash
npm install -g @vm0/cli
vm0 auth login
mkdir my-agent && cd my-agent
vm0 init
cat AGENTS.md # check the workflow definition
vm0 cook "run your workflow"
```

### Why It's Interesting

- **Scheduled Automation** - Unlike one-off agent runs, vm0 enables recurring workflows (e.g., daily code reviews, weekly dependency updates)
- **Skills Library** - Pre-built integrations reduce workflow setup time
- **Sandbox Security** - Isolated execution environments for untrusted workflows
- **Session Management** - Forking and versioning workflows like git for agents
- **Observability First** - Built-in monitoring vs. running agents blind

### Comparison to Other Agent Platforms

| Feature | vm0 | Claude Code | Devin | OpenHands |
|---------|-----|-------------|-------|-----------|
| Scheduled Runs | Yes | No | No | No |
| Cloud Sandbox | Yes | Local | Yes | Local/Cloud |
| Skills Library | 60+ | Via MCP | Limited | Limited |
| Session Persistence | Yes | No | Yes | No |
| Observability | Built-in | Logs only | Dashboard | Logs only |

### Use Cases

- Daily automated code reviews
- Scheduled dependency updates and security audits
- Recurring data pipeline maintenance
- Automated documentation updates
- Periodic integration testing across environments

---

## Cursor - AI-First Code Editor

*Source: https://www.cursor.com/ - Added: 2024-07-03*

Fork of VS Code with deep AI integration. One of the first mainstream AI-native editors, now a benchmark for AI coding tools.

### Key Features

- **Codebase-Aware Chat** - Ask questions about your specific code; references files and docs
- **Copilot++** - Predicts next edits (not just completions), handles multi-line changes
- **Cmd-K Natural Language Editing** - Update classes/functions via text instructions
- **VS Code Compatibility** - Import extensions, themes, and keybindings in one click
- **Privacy Mode** - SOC 2 certified, code not stored when enabled
- **BYOK** - Bring your own API key or use hosted models

### Why It Matters

- Set the standard for "AI-first editor" category that Zed, Windsurf, and others now compete in
- Tab completion that predicts edits (not just next tokens) was novel when launched
- Proved developers would pay for AI tooling beyond GitHub Copilot
- Referenced as comparison baseline in most AI coding tool discussions

### User Feedback (2024)

- "At least 2x improvement over Copilot" - Sr. Staff Engineer, Instacart
- "How Copilot should feel" - Engineers praising seamless integration
- "No going back" - Common sentiment from VSCode converts

### Comparison

| Feature | Cursor | Claude Code | VS Code + Copilot | Zed |
|---------|--------|-------------|-------------------|-----|
| Base | VS Code fork | Terminal | VS Code | Native |
| AI Model | Multiple | Claude | GPT-4 | Multiple |
| Edit Prediction | Yes (Copilot++) | No | Basic | No |
| Cmd-K Editing | Yes | Yes (diff) | No | Yes |
| Codebase Chat | Yes | Yes | Limited | Yes |

---

## GPT Engineer (Lovable) - AI Web App Builder

*Source: https://gptengineer.app/ - Added: 2024-08-29*

Chat-based AI tool for building web applications. Emphasizes quick prototyping with GitHub sync and one-click deployment.

### Key Features

- **Conversational Building** - Chat with AI to create and modify web apps
- **GitHub Sync** - Push changes directly to repositories
- **One-Click Deploy** - Deploy directly from the platform
- **Full-Stack Generation** - Creates frontend and backend code

### Why It's Interesting

- Lower barrier to entry than IDE-based tools like Cursor or Claude Code
- Good for rapid prototyping and MVPs
- Non-developers can build functional apps
- Rebranded to "Lovable" - positioning as more user-friendly alternative to traditional coding agents

### Comparison to Other Tools

| Feature | GPT Engineer | v0 (Vercel) | Bolt.new | Claude Artifacts |
|---------|--------------|-------------|----------|------------------|
| Full Apps | Yes | UI Focus | Yes | Components Only |
| GitHub Sync | Yes | Limited | Yes | No |
| Deployment | Built-in | Vercel | Built-in | None |
| Backend Support | Yes | No | Yes | No |

---

## Refact.ai - Self-Hosted Autonomous AI Coding Agent

*Source: https://refact.ai/ - Added: 2026-01-18*

Open-source, self-hosted AI coding agent with IDE integration. Key differentiator is on-premise deployment for data privacy and fine-tuning capability.

### Key Features

- **Autonomous Agent** - Delegates coding tasks end-to-end; plans, executes, and deploys
- **IDE Integration** - VS Code, JetBrains suite (PyCharm, WebStorm, IntelliJ, etc.), Visual Studio, Neovim, Sublime Text
- **In-IDE Chat** - Context-aware chat with 32k-64k context window
- **Code Completions** - Powered by Qwen2.5-Coder with RAG for project-specific insights
- **Tool Integrations** - Connects to GitHub, PostgreSQL, Docker, CI/CD pipelines, Chrome
- **25+ Languages** - Python, JavaScript, TypeScript, Java, Rust, C++, Go, PHP, Ruby, etc.

### Self-Hosted / Privacy Focus

- **On-Premise Deployment** - Run entirely on your infrastructure
- **LLM Fine-Tuning** - Train models on your company's codebase
- **Multi-GPU Support** - Optimized for enterprise GPU clusters
- **Code Never Leaves Servers** - Full data ownership

### Model Options

- Claude 3.7 Sonnet, GPT-4o, GPT-4o mini for agent/chat
- BYOK (Bring Your Own Key) - Gemini, Grok, OpenAI, Deepseek, others
- Qwen2.5-Coder for completions (runs locally)

### Pricing

- **Free** - Limited agent usage/day, 32k chat context, unlimited completions
- **Pro ($10/mo)** - 40 agent requests/day, 64k chat context, additional models
- **Enterprise** - On-premise, fine-tuning, priority support

### Why It's Interesting

- Self-hosted option addresses data privacy concerns that block other AI tools at enterprises
- Fine-tuning on company codebases is unique capability vs Claude Code, Cursor, Copilot
- Open-source core allows customization
- Price point undercuts most competitors
- Memory/learning system improves with usage ("digital twin" concept)

### User Testimonials (Discord/LinkedIn)

- Built full Django IoT monitoring app "99.9% with Refact.ai Agent"
- Fixed 80-hour WordPress rewrite estimate in 30 minutes
- "Saved thousands of euros" - built prototype in a week vs months with freelancer
- Good for non-web-devs learning new stacks with "vibe coding"

### Comparison

| Feature | Refact.ai | Claude Code | Cursor | GitHub Copilot |
|---------|-----------|-------------|--------|----------------|
| Self-Hosted | Yes | No | No | No |
| Fine-Tuning | Yes | No | No | No |
| Autonomous Agent | Yes | Yes | Limited | Limited |
| Open Source | Partial | No | No | No |
| IDE Integration | Multiple | Terminal | Cursor | VS Code/JetBrains |

---

## Zed - Agentic Editing in a Multiplayer IDE

*Source: https://zed.dev/agentic - Added: 2026-01-18*

Zed is a Rust-powered code editor with native multiplayer support and integrated agentic editing capabilities. Fast (120fps), designed for developers coming from vim.

### Key Features

- **Agent Panel** - Chat interface for natural language codebase exploration and modification
- **Automatic Context Discovery** - Agent searches codebase as needed; no manual context or indexing required
- **Follow Mode** - Track the agent's location in real-time as it navigates your code
- **Editable Unified Diffs** - Review agent changes in a diff view that supports full editing
- **Background Operation** - Let agents work and get notified when done or needing input
- **MCP Support** - Extend with Model Context Protocol servers for databases, browsers, PRs, etc.

### Model Options

- **Hosted** - Claude 3.7 Sonnet with simple pricing
- **Local** - Connect via Ollama to run models on your own hardware
- **BYOK** - Bring your own API keys from any provider

### Notable Quotes from Users

- José Valim: "Zed agents delivered complete features while preserving my project's coding standards"
- Isaac Harris-Holt (CTO): "Using the Agent to learn mobile app development... correcting my mistakes has been invaluable"
- Amos Wenger: "I dictate prompts to various LLMs and get notified when their work is ready to review. I got so much better at code review!"

### Why It's Interesting

- Native IDE integration (not a plugin) means tighter agent-editor integration
- Multiplayer-first architecture enables real-time agent collaboration
- Vim mode praised as best-in-class for vim converts
- Agent-as-background-worker model differs from Claude Code's conversational approach
- MCP extensibility allows for custom integrations

### Comparison

| Feature | Zed | Claude Code | Cursor |
|---------|-----|-------------|--------|
| Primary Use | IDE with agent | Terminal agent | IDE with agent |
| Environment | Native app | CLI | Electron app |
| Agent Model | Background worker | Conversational | Inline + Chat |
| Multiplayer | Native | Via Claudetainer | No |
| Vim Mode | Excellent | N/A | Good |

---

## Claudetainer - Containerized Claude Code for Mobile/Remote

*Source: https://github.com/smithclay/claudetainer - Added: 2026-01-18*

A Docker-based development environment for running Claude Code anywhere, including from your phone. Auto-configures hooks, slash commands, and specialized sub-agents.

### Key Features

- **Instant Setup** - Auto-detects language (Python, Node.js, Go, Rust, Shell) and configures tooling
- **Mobile-Friendly** - SSH + terminal multiplexer (Zellij) designed for coding from iPhone/mobile
- **Pre-Configured Claude Code** - Hooks, slash commands, and sub-agents ready out of the box
- **Push Notifications** - Know when Claude needs attention
- **Isolated Docker Environment** - Everything runs in a container

### Language Support

Auto-detects and configures tooling for:
- **Python** (requirements.txt, pyproject.toml) → black, flake8, autopep8
- **Node.js** (package.json) → eslint, prettier, TypeScript
- **Go** (go.mod) → gofmt, golangci-lint
- **Rust** (Cargo.toml) → rustfmt, clippy
- **Shell** (.sh files) → shellcheck, shfmt

### Quick Start

```bash
# Install via Homebrew
brew tap smithclay/tap
brew install claudetainer

cd ~/your-project

# Initialize with language preset
claudetainer init python

# Start container
claudetainer up

# Connect (default password: vscode)
claudetainer ssh

# Inside container, start Claude Code
claude
```

### Remote Access

```bash
claudetainer mosh    # MOSH + Zellij (better for mobile)
# SSH also available
```

### Why It's Interesting

- Solves the "code from anywhere" problem with proper mobile UX
- Pre-baked hooks and sub-agents for keyboard-less coding
- Team configs shareable via GitHub repos
- Works well with Happy Coder for mobile Claude Code access (see `claude-code-configuration.md`)

### Comparison

| Feature | Claudetainer | Happy Coder | Conductor |
|---------|--------------|-------------|-----------|
| Primary Use | Remote/mobile coding | Mobile sync | Parallel agents |
| Environment | Docker container | Native app | Desktop workspaces |
| Setup | CLI-based | QR code pairing | Uses existing login |
| Best For | Coding from phone | Mobile monitoring | Running many agents |

### Notes

- Requires Docker and DevContainer CLI
- The pre-configured hooks and sub-agents are borrowed from Claude Code community configs
- Good companion to Happy Coder for true mobile development

---

## Claude Code in Docker (VSCode Dev Containers)

*Source: https://timsh.org/claude-inside-docker/ - Added: 2026-01-18*

Minimal DIY setup for running Claude Code in an isolated Docker container via VSCode's Dev Container feature. Focus is on security isolation rather than remote access.

### Security Motivation

Running an AI agent with full filesystem and terminal access is risky:
- Access to SSH keys, secrets, and sensitive files
- Potential for catastrophic mistakes (`rm -rf` on important directories)
- MCP vulnerabilities allow external attacks
- Models can bypass command blacklists

**Solution:** Put Claude Code in a container with only the project files mounted.

### Minimal Setup

1. Create `.devcontainer/devcontainer.json` in your project root:

```json
{
  "name": "Claude Code Dev Container",
  "image": "mcr.microsoft.com/devcontainers/base:ubuntu",
  "features": {
    "ghcr.io/devcontainers/features/node:1": {}
  },
  "postCreateCommand": "npm install -g @anthropic-ai/claude-code"
}
```

2. Open folder in VSCode → "Reopen in Container"
3. Run `claude` in the integrated terminal

**Repository:** https://github.com/tim-sha256/claude-in-docker

### What Container Isolation Provides

- Claude can only access files inside the container or mounted volumes
- No access to local SSH keys, secrets, or external directories
- Can't break anything outside the container
- Worst case: container breaks and stops

### GitHub Access with Fine-Grained Tokens

Since the container doesn't have your SSH keys, use a fine-grained GitHub Personal Access Token for safer git operations:

1. Create token at https://github.com/settings/personal-access-tokens/new
2. Grant access only to specific repositories
3. Set only "Contents: Read and write" permission (enough for clone/pull/push)
4. Clone with token:

```bash
git clone https://<USERNAME>:<TOKEN>@github.com/<USERNAME>/<REPO>.git
cd <REPO>
git remote set-url origin https://<USERNAME>:<TOKEN>@github.com/<USERNAME>/<REPO>.git
```

**Benefit:** Token can't modify GitHub account settings, access other repos, or do anything beyond basic git operations on selected repos.

### Comparison to Claudetainer

| Feature | This Approach | Claudetainer |
|---------|--------------|--------------|
| Setup complexity | Minimal (one JSON file) | Full tooling with CLI |
| Primary goal | Security isolation | Mobile/remote access |
| Pre-configured tooling | None | Hooks, sub-agents, notifications |
| Use case | Cautious local development | Coding from anywhere |

### When to Use This

- Working with sensitive codebases or client projects
- Paranoid about AI agent access to local filesystem
- Want minimal setup without additional tooling
- Don't need mobile access or pre-configured agent features

---

## Klavis AI / Strata - MCP Integration Layer

*Source: https://www.klavis.ai/ - Added: 2026-01-18*

An open-source MCP integration layer that provides a single MCP server for AI agents to access thousands of tools.

### Key Features

- **Unified MCP Server** - One server to handle connections to many tools
- **SOC 2 Certified** - Enterprise-grade security compliance
- **GDPR Compliance** - In progress for EU data protection requirements
- **Open Source** - Integration layers are open source

### Why It's Interesting

- Simplifies MCP tool management by consolidating into a single server
- Enterprise focus with compliance certifications
- Could reduce complexity when agents need access to many different tools

### Notes

- Product called "Strata" launched on Product Hunt
- Light on technical details in public docs - worth revisiting when more documentation available

---

## mcp-use - Python Library for Custom MCP Agents

*Source: https://github.com/mcp-use/mcp-use - Added: 2026-01-18*

An open-source Python library for connecting any LLM to any MCP server to build custom agents with tool access. The simplest way to give LLMs access to MCP tools without using closed-source clients.

### Key Features

- **LLM Agnostic** - Works with OpenAI, Anthropic, Groq, and other LangChain-supported providers
- **Multiple Server Support** - Connect to multiple MCP servers simultaneously
- **Dynamic Server Selection** - Server Manager auto-selects correct server based on tool choice
- **Tool Access Control** - Restrict which tools agents can use via `disallowed_tools`
- **Streaming Output** - Async streaming via `agent.astream()` for real-time feedback
- **HTTP/SSE/stdio Support** - Connect to MCP servers over various transports
- **Sandboxed Execution** - Optional E2B cloud sandbox for isolated execution

### Quick Start

```bash
pip install mcp-use
pip install langchain-openai  # or langchain-anthropic
```

```python
import asyncio
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from mcp_use import MCPAgent, MCPClient

async def main():
    load_dotenv()

    # Create MCP client from config
    client = MCPClient.from_config_file("browser_mcp.json")

    # Create agent
    llm = ChatOpenAI(model="gpt-4o")
    agent = MCPAgent(llm=llm, client=client, max_steps=30)

    # Run query
    result = await agent.run("Find restaurants in SF using Google Search")
    print(result)

asyncio.run(main())
```

Config file (`browser_mcp.json`):
```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"],
      "env": { "DISPLAY": ":1" }
    }
  }
}
```

### Multi-Server Configuration

```json
{
  "mcpServers": {
    "airbnb": {
      "command": "npx",
      "args": ["-y", "@openbnb/mcp-server-airbnb"]
    },
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

Enable Server Manager for automatic server selection:
```python
agent = MCPAgent(
    llm=llm,
    client=client,
    use_server_manager=True  # Auto-selects correct server
)
```

### HTTP Connection

```python
config = {
    "mcpServers": {
        "http": {
            "url": "http://localhost:8931/sse"
        }
    }
}
client = MCPClient.from_dict(config)
```

### Tool Restrictions

```python
agent = MCPAgent(
    llm=llm,
    client=client,
    disallowed_tools=["file_system", "network"]  # Security controls
)
```

### Sandboxed Execution (E2B)

```bash
pip install "mcp-use[e2b]"
```

```python
from mcp_use.types.sandbox import SandboxOptions

sandbox_options: SandboxOptions = {
    "api_key": os.getenv("E2B_API_KEY"),
    "sandbox_template_id": "base",
}

client = MCPClient(
    config=server_config,
    sandbox=True,
    sandbox_options=sandbox_options,
)
```

### Debugging

```bash
DEBUG=1 python script.py  # INFO level
DEBUG=2 python script.py  # Full DEBUG output
```

### When to Use

**Good fit:**
- Building custom agents that need MCP tool access
- Prototyping LLM applications with existing MCP servers
- Need LLM provider flexibility (not locked to Claude)
- Want programmatic control over agent behavior

**Compare with:**
- **Claude Code** - Pre-built agent with MCP support, but Claude-only
- **Dedalus Labs** - Hosted platform vs library approach
- **IBM Context Forge** - Gateway/registry vs direct client
- **Klavis/Strata** - Managed MCP layer vs build-it-yourself

### Notes

- MIT licensed
- Python 3.11+ required
- Docs: https://mcp-use.com
- Hosted chat available at mcp-use.com/chat (beta)

---

## Inkeep - No-Code + Code AI Agent Builder

*Source: https://docs.inkeep.com/overview - Added: 2026-01-18*

A platform for building AI agents with both no-code visual builder and TypeScript SDK approaches, with full 2-way sync between them.

### Key Features

- **Dual Authoring** - No-code canvas (drag-and-drop) or TypeScript SDK with 2-way sync between formats
- **Multi-Agent Architecture** - Build teams of agents that work together
- **MCP Tools** - Built-in support with credentials management
- **UI Component Library** - For dynamic chat experiences
- **Flexible Deployment** - Vercel, Docker, or self-hosted
- **Observability** - Traces UI and OpenTelemetry integration
- **LLM Agnostic** - Use any LLM provider

### Use Cases

**Agentic Chat Assistants:**
- Customer experience agents for help centers, docs, in-app
- Internal copilots for support, sales, marketing, ops teams

**Agentic Workflow Automation:**
- Creating/updating knowledge bases, docs, blogs
- Updating CRMs, triaging helpdesk tickets
- Tackling repetitive tasks

### Why It's Interesting

- Technical and non-technical teams can collaborate on same agents
- Fair-code license allows self-hosting
- Open protocols (MCP, A2A, Vercel SDK APIs) for triggering agents
- Bridges the gap between "I want to prototype quickly" and "I need production-grade code"

### Deployment Options

- Inkeep Cloud (waitlist)
- Inkeep Enterprise (managed)
- Self-hosted via Docker

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

## claudecode-orchestrator (Multi-Agent Development Framework)

*Source: https://github.com/darrenapfel/claudecode-orchestrator - Added: 2026-01-18*

A comprehensive orchestration framework that enables Claude Code to operate as a "full software development team" through parallel execution, structured workflows, and evidence-based validation.

### Core Philosophy

**Quality Through Truth:** Every claim requires evidence, every test result must be shown, and validation failures are documented and fixed rather than hidden. The system argues this "paradoxically saves tokens by catching issues early rather than building on broken foundations."

### Key Features

| Feature | Description |
|---------|-------------|
| **Milestone Completion Protocol** | Services started and smoke-tested before declaring completion |
| **Parallel Execution** | Visual execution guides, system-level warnings against sequential execution |
| **Evidence-Based Development** | Every task produces `EVIDENCE.md` with reproducible proof |
| **User Feedback Loop** | Structured feedback collection via auto-generated testing guides |
| **Fix Cycle Protocol** | Validation failures trigger documented fix cycles (treated as normal) |

### Personas/Agents

The system uses specialized "personas" with designated responsibilities:

**Core Team:**
- Orchestrator, Product Manager, Architect, Software Engineer, UX Designer

**QA Team:**
- SDET, Test Engineer, Integration Engineer, Performance Engineer, Security Engineer

**Support:**
- DevOps, Documentation Writer

### Directory Structure

```
your-project/
├── .claude/
│   ├── personas/           # AI role definitions
│   ├── patterns/           # Workflow patterns
│   ├── guides/             # How-to documentation
│   └── validators/         # Validation protocols
├── .work/
│   ├── foundation/         # Core architecture/design
│   ├── milestones/         # Development phases
│   │   └── sprint-001/
│   │       ├── tasks/
│   │       ├── validation-1/
│   │       ├── fixes/cycle-1/
│   │       └── completion/
│   └── discovery/          # Project understanding
└── CLAUDE.md
```

### Installation

```bash
# Global installation (affects all projects)
./orchestrator.sh global
# ⚠️ WARNING: Replaces ~/.claude/claude.md

# Local installation only
./orchestrator.sh local
```

### Workflow Overview

1. **Discovery** - Gather clarifying questions (one-time)
2. **Requirements** - PM defines scope and acceptance criteria
3. **Foundation Design** - Architect and UX Designer create blueprint
4. **Implementation** - Engineers build in parallel batches
5. **Integration** - Connect all components
6. **Validation** - Four validators verify quality in parallel
7. **Fix Cycles** - Address any validation failures
8. **Milestone Completion** - Start service and prepare for user testing
9. **Feedback Processing** - Implement user-reported improvements

### Critical Differences from Built-in Claude Code

**This framework deliberately contradicts some Claude Code design principles:**

| Claude Code Built-in | This Orchestrator |
|---------------------|-------------------|
| Single-threaded, max-1-branch depth | Multiple parallel personas |
| Simple todo list maintained by model | Elaborate milestone/sprint structure |
| "I highly doubt you need multi-agent" | Full multi-agent team simulation |
| Minimal scaffolding | Heavy structure (.work/, validators, evidence) |

### When This Might Be Useful

- Very large projects needing formal structure
- Teams wanting explicit documentation trails
- Projects requiring audit-level evidence of testing
- Situations where "honest failure documentation" is valued

### When to Avoid

- Simple projects (massive overhead)
- When you trust Claude Code's built-in single-thread model
- If you value simplicity and debuggability (see MinusX analysis in claude-code-configuration.md)
- If you prefer the "master-clone" subagent philosophy

### Comparison with oh-my-claude-sisyphus

| Feature | claudecode-orchestrator | oh-my-claude-sisyphus |
|---------|------------------------|----------------------|
| Primary Focus | Full SDLC workflow | Task persistence |
| Structure | Heavy (milestones, sprints, validation) | Lightweight (agents + commands) |
| Philosophy | "Quality through truth" | "Agents persist until complete" |
| Installation | Replaces claude.md | Adds to ~/.claude/agents/ |
| Personas | 12+ specialized roles | 11 specialized agents |

### Notes

- Consider whether the overhead matches your project complexity
- The evidence-based validation is interesting for compliance contexts
- The "fix cycle" normalization could reduce frustration with failures
- Heavy structure trades debuggability for documentation

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

## Omnara - Mission Control for AI Coding Agents

*Source: https://github.com/omnara-ai/omnara - Added: 2026-01-18*

YC S25 startup providing a mobile control plane for AI coding agents (Claude Code, Cursor, GitHub Copilot). Real-time visibility, push notifications, and instant responses to agent questions from your phone.

### Key Features

- **Real-Time Monitoring** - See every step your agents take as they work
- **Push Notifications** - Get alerted when agents need input or hit blockers
- **Interactive Q&A** - Answer agent questions from anywhere, instantly
- **Universal Dashboard** - Monitor all agents (Claude, Cursor, Copilot) in one place
- **Mobile-First** - iOS app + web dashboard

### Use Cases

- **Code Review** - Launch Claude to review PRs while at lunch, respond only when needed
- **Production Debugging** - Debug issues from phone at 2am with real-time agent guidance
- **Data Migrations** - Monitor 6-hour jobs remotely, approve schema changes on the go
- **Refactoring** - Let Claude refactor legacy code during meetings, answer questions without context switching
- **Test Fixing** - Have Claude fix tests overnight, wake up to green builds or specific questions

### Integration Options

```bash
# CLI wrapper (monitors Claude sessions)
pip install omnara
omnara monitor --api-key YOUR_KEY

# Or launch agents remotely via webhook
omnara serve
```

```python
# Python SDK
from omnara import OmnaraClient
import uuid

client = OmnaraClient(api_key="your-api-key")
instance_id = str(uuid.uuid4())

# Log progress
response = client.send_message(
    agent_type="claude-code",
    content="Analyzing codebase structure",
    agent_instance_id=instance_id,
    requires_user_input=False
)

# Ask for user input when needed
answer = client.send_message(
    content="Should I refactor this legacy module?",
    agent_instance_id=instance_id,
    requires_user_input=True
)
```

### Architecture

- **Backend**: FastAPI with separate read/write servers
- **Frontend**: React (web) + React Native (mobile)
- **Protocol**: Model Context Protocol (MCP) + REST API
- **Database**: PostgreSQL with SQLAlchemy
- **Auth**: Dual JWT (Supabase for users, custom for agents)

### Pricing

| Tier | Price | Features |
|------|-------|----------|
| Free | $0 | Basic monitoring |
| Pro | TBD | More features + support |

### Why It's Interesting

- Solves a real problem: long-running agents get stuck, and you don't know until hours later
- "Mission control" framing is spot-on—agents need oversight and guidance
- MCP integration means it can work with many different agent frameworks
- Open source (Apache 2.0)
- Could pair well with Happy Coder for mobile Claude Code (Happy for sync, Omnara for monitoring)

### Comparison to Similar Tools

| Feature | Omnara | Claudetainer | Happy Coder |
|---------|--------|--------------|-------------|
| Primary Use | Agent monitoring/control | Remote coding environment | Mobile sync |
| Notifications | Push when agent needs input | When Claude needs attention | Session sync |
| Multi-Agent | Yes (any MCP-compatible) | Claude Code only | Claude Code only |
| Setup | SDK/wrapper install | Docker container | QR code pairing |

### Links

- GitHub: https://github.com/omnara-ai/omnara
- Website: https://www.omnara.ai/
- iOS App: App Store

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

## Playwrightess MCP - Single-Tool Playwright Eval

*Source: https://github.com/mitsuhiko/playwrightess-mcp - Added: 2026-01-18*

An experimental MCP server by Mitsuhiko (Flask creator) that provides a persistent Playwright evaluation environment through a single JavaScript-based tool.

### Key Concept

Unlike Playwright MCP which exposes many individual tools (click, type, screenshot, etc.), Playwrightess exposes just **one tool**: `playwright_eval`. This tool lets agents write and execute arbitrary Playwright JavaScript code with persistence between calls.

### Architecture

```
┌─────────────────┐     ┌──────────────────────────────┐
│  Agent/LLM      │ ──► │  Playwrightess MCP Server    │
│                 │     │  ┌────────────────────────┐  │
│  Uses single    │     │  │ Persistent JS Context  │  │
│  playwright_eval│     │  │ - State maintained     │  │
│  tool           │     │  │ - Full Playwright API  │  │
│                 │     │  │ - Between-call memory  │  │
└─────────────────┘     │  └────────────────────────┘  │
                        └──────────────────────────────┘
```

### Why This Matters

| Approach | Tools | Context Cost | Flexibility |
|----------|-------|--------------|-------------|
| Playwright MCP | ~17 individual tools | High (all tool schemas) | Limited to predefined actions |
| Playwrightess | 1 tool (playwright_eval) | Low | Full Playwright API |
| Playwriter | 1 tool (execute) | Low | Full API, uses existing Chrome |

The "single ubertool" approach means:
- Less context window usage (no schema bloat)
- LLMs already know Playwright API from training data
- Persistence between calls enables stateful workflows

### Installation

```bash
npm install
npm run build
```

### Configuration

```json
{
  "mcpServers": {
    "playwriter-mcp": {
      "type": "stdio",
      "command": "node",
      "args": ["/path/to/dist/index.js"],
      "env": {}
    }
  }
}
```

### Status

**Experimental** - Mitsuhiko explicitly states this is an experiment and intentionally not published to npm.

### Related

- **Playwriter** - Similar single-tool philosophy but uses Chrome extension instead of MCP
- **Playwright MCP** - Official multi-tool approach from Playwright team

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

---

## AWS API MCP Server

*Source: https://aws.amazon.com/about-aws/whats-new/2025/10/aws-api-mcp-server-v1-0-0-release - Added: 2026-01-18*

An MCP server that enables foundation models (FMs) to interact with any AWS API through natural language by creating and executing syntactically correct CLI commands.

### Key Features (v1.0.0)

- **Natural Language to AWS CLI** - Creates and executes CLI commands from natural language requests
- **Streamable HTTP Transport** - Now supports HTTP transport in addition to stdio
- **CloudWatch Integration** - Collect logs for improved observability
- **Human-in-the-Loop Controls** - Elicitation support for iterative inputs, configurable human oversight for mutating actions
- **Action Safeguards** - Can deny certain action types or require consent for mutations
- **Reduced Startup Time** - `suggest_aws_command` tool converted to remote service (removes local dependencies)

### New in v1.0.0

- **get_execution_plan Tool** (Experimental) - Provides prescriptive workflows for common AWS tasks
  - Enable with `EXPERIMENTAL_AGENT_SCRIPTS=true`
- **Improved Security** - Better file system controls and input validation
- **Elicitation Support** - More reliable iterative input workflows

### Installation Options

Available from:
- Popular MCP registries
- Amazon ECR Public Gallery (container)
- AWS Labs GitHub repository (source)

### Why It's Interesting

- **Natural Language AWS Access** - Ask Claude/Q to "list my S3 buckets" and it generates the correct CLI command
- **Safety Features** - Human oversight controls address concerns about AI executing cloud operations
- **Official AWS Tool** - Maintained by AWS Labs, production-ready
- **Pairs with MCP Proxy** - Use with AWS MCP Proxy Server for authenticated remote access

### Links

- Announcement: https://aws.amazon.com/about-aws/whats-new/2025/10/aws-api-mcp-server-v1-0-0-release
- GitHub: https://github.com/awslabs/mcp (AWS Labs MCP repository)

---

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

---

## Microsoft Amplifier - Supercharged AI Dev Environment

*Source: https://github.com/microsoft/amplifier - Added: 2026-01-18*

A research demonstrator from Microsoft that provides a complete development environment for AI coding assistants, including specialized agents, pre-loaded context, and automation tools.

**Status:** Experimental research project, not accepting contributions yet.

### Core Components

| Component | Description |
|-----------|-------------|
| 20+ Specialized Agents | Each expert in specific tasks (architecture, debugging, security, etc.) |
| Pre-loaded Context | Proven patterns and philosophies built into the environment |
| Parallel Worktree System | Build and test multiple solutions simultaneously |
| Knowledge Extraction | Transform documentation into queryable, connected knowledge |
| Conversation Transcripts | Auto-export before compaction, instant restoration |
| Automation Tools | Quality checks and patterns enforced automatically |

### Specialized Agents Catalog

**Core Development:**
- `zen-architect` - Designs with ruthless simplicity
- `modular-builder` - Builds following modular principles
- `bug-hunter` - Systematic debugging
- `test-coverage` - Comprehensive testing
- `api-contract-designer` - Clean API design

**Analysis & Optimization:**
- `security-guardian` - Security analysis
- `performance-optimizer` - Performance profiling
- `database-architect` - Database design and optimization
- `integration-specialist` - External service integration

**Knowledge & Insights:**
- `insight-synthesizer` - Finds hidden connections
- `knowledge-archaeologist` - Traces idea evolution
- `concept-extractor` - Extracts knowledge from documents
- `ambiguity-guardian` - Preserves productive contradictions

**Meta & Support:**
- `subagent-architect` - Creates new specialized agents
- `post-task-cleanup` - Maintains codebase hygiene
- `content-researcher` - Researches from content collection

### Parallel Worktree Development

```bash
# Try different approaches in parallel
make worktree feature-jwt     # JWT authentication approach
make worktree feature-oauth   # OAuth approach in parallel

# Compare and choose
make worktree-list            # See all experiments
make worktree-rm feature-jwt  # Remove the one you don't want
```

Each worktree is completely isolated with its own branch, environment, and context.

### Enhanced Status Line

Shows costs, model, and session info at a glance:
```
~/repos/amplifier (main → origin) Opus 4.1 💰$4.67 ⏱18m
```

### Conversation Transcript System

- **PreCompact Hook** - Captures full conversation before compaction
- **Timestamps & Organization** - Stored in `.data/transcripts/`
- **Instant Restoration** - `/transcripts` command to restore full history
- **Search** - `make transcript-search TERM="auth"` to find past discussions

### Modular Builder (Lite)

One-command workflow from idea to module:

1. Contract & Spec
2. Plan
3. Generate
4. Review

**Modes:**
- `auto` (default) - Runs autonomously if confidence ≥ 0.75
- `assist` - Asks ≤ 5 questions to resolve ambiguity
- `dry-run` - Plan/validate only (no code writes)

### Knowledge Base System

```bash
make knowledge-update              # Process documentation
make knowledge-query Q="error handling patterns"
```

### Prerequisites

- Python 3.11+
- Node.js
- VS Code (recommended)
- Git

### Why It's Interesting

- **Specialized vs Generalist Agents** - 20+ focused agents instead of one jack-of-all-trades
- **Parallel Exploration** - Git worktrees enable testing multiple solutions simultaneously
- **Knowledge Compounds** - Documentation becomes queryable knowledge
- **Conversation Persistence** - Solves the context loss problem on compaction
- **Microsoft Research Backing** - Real engineering resources behind it

### Vision

Building toward:
1. Natural language to working systems
2. Test 10 approaches simultaneously
3. Knowledge compounds across projects
4. AI handles tedious work, humans focus on creative decisions

### Links

- GitHub: https://github.com/microsoft/amplifier
- License: Microsoft CLA required for contributions

---

## OpenHands (All-Hands-AI)

*Source: https://github.com/All-Hands-AI/OpenHands - Added: 2026-01-18*

An open-source AI-powered platform for software development where agents can modify code, run commands, browse the web, call APIs, and interact with the world like a human developer.

### Key Features

- **Full Developer Capabilities** - Agents can modify code, run shell commands, browse web, call APIs
- **Multiple Run Options** - Cloud (with $20 free credits), local CLI launcher, or Docker
- **MCP Support** - Default MCP servers for tool integration
- **LLM Flexibility** - Works with multiple providers, Anthropic Claude Sonnet 4 recommended

### Installation Options

**Cloud (easiest):**
```bash
# Sign up at OpenHands Cloud - $20 free credits
```

**Local CLI (recommended for local):**
```bash
# Install uv first (see uv installation guide)
# Launch GUI server
uvx --python 3.12 --from openhands-ai openhands serve

# Or launch CLI
uvx --python 3.12 --from openhands-ai openhands
```
OpenHands runs at http://localhost:3000 in GUI mode.

**Docker:**
Available for more isolated deployments. See their hardened installation guide for secure setups on public networks.

### Important Limitations

- **Single-user only** - Not designed for multi-tenant deployments
- **No built-in auth** - No authentication, isolation, or scalability for shared instances
- For multi-tenant needs: OpenHands Cloud Helm Chart (commercial, source-available)

### Integration Options

- Connect to local filesystem
- CLI for direct interaction
- Headless mode for scripting
- GitHub Action for tagged issues

### How It Compares

| Feature | OpenHands | Claude Code | Codex | Aider |
|---------|-----------|-------------|-------|-------|
| Deployment | Cloud/Local/Docker | CLI | CLI/Web | CLI |
| MCP Support | Yes | Yes | No | No |
| GUI | Yes (web) | No | Yes | No |
| Multi-tenant | No (use Helm chart) | No | No | No |
| Open Source | MIT | No | No | Yes |

### Why It's Interesting

- Full web browsing capability - can research while coding
- Active community (Slack + GitHub)
- Backed by academic research (ICLR 2025 publication)
- MIT licensed with commercial options for enterprise
- The `uvx` launcher provides nice isolation from local Python environments

### Links

- GitHub: https://github.com/All-Hands-AI/OpenHands
- Docs: https://docs.all-hands.dev
- Cloud: OpenHands Cloud (with free credits)
- Slack: Community workspace for research/architecture discussions
- License: MIT (except enterprise/ folder)
---

## Open-Agent

*Source: https://github.com/AFK-surf/open-agent - Added: 2026-01-18*

An open-source alternative to Claude Agent SDK (Claude Code), ChatGPT Agents, and Manus. Self-hostable agentic AI system with multi-model collaboration.

### Key Features

- **Multi-Agent Collaboration** - Multiple agents can work together using different models
- **Self-Hosting** - Full control over data and processes via Docker deployment
- **Open Source** - Apache 2.0 licensed, fully modifiable
- **Decision-Making Focus** - Emphasizes decision support over prompt-chasing

### Quick Start

```bash
# Copy config and docker-compose
mkdir deploy && cd deploy
cp ../.docker/config.example.json ./config.json
cp ../.docker/docker-compose.yml ./docker-compose.yml

# Launch
docker compose up -d
```

### How It Compares

| Feature | Open-Agent | OpenHands | Claude Code | Codex |
|---------|------------|-----------|-------------|-------|
| Deployment | Docker self-host | Cloud/Local/Docker | CLI | CLI/Web |
| Multi-Agent | Yes | No | No | No |
| License | Apache 2.0 | MIT | Proprietary | Proprietary |
| Open Source | Yes | Yes | No | No |

### Why It's Interesting

- Fills the gap for self-hosted multi-agent orchestration
- Can mix different LLM providers/models within the same system
- Active development with Discord community
- Apache 2.0 license allows full commercial use and modification
- Builds on ideas from AFFiNE and broader agentic AI community

### Links

- GitHub: https://github.com/AFK-surf/open-agent
- Discord: Community server (linked from GitHub)
- License: Apache 2.0

---

## Happy Coder - Voice Coding with Claude Code

*Source: https://happy.engineering/docs/features/voice-coding-with-claude-code/ - Added: 2026-01-18*

A mobile app that connects to Claude Code, enabling voice-driven coding sessions away from your desk. Real-time bidirectional sync means you can start on your phone and continue on your computer.

### The Core Insight

Voice coding isn't about replacing your desk setup—it's about capturing thinking time that would otherwise produce zero code.

**Key realization:** Voice might be 50% as effective as sitting at your desk, but 50% of three extra hours beats 0% of those hours.

### Why It Matters

1. **Activation energy, not quality** - The barrier is starting, not output quality
2. **Finger health** - AI assistants turned us into prompt machines (six books of text per month). Voice gives hands a break
3. **High-risk idea exploration** - Think through that risky refactor without committing to a desk session
4. **Time reclamation** - Hours between dinner and bed, Saturday mornings, commutes

### The Voice Agent Architecture

The voice agent is deliberately simple—a translator, not a partner:

1. Uses Eleven Labs for speech-to-text
2. Maintains its own context separate from Claude Code
3. Cleans up verbal rambling into structured requests
4. Syncs in real-time with your desktop session

**Critical point:** It doesn't ask clever questions or provide insights. It does one thing: takes your rambling and makes it comprehensible to Claude Code.

### Bidirectional Sync

Start talking on your phone, continue typing on your computer. Or vice versa. The session persists across both.

**The bridge effect:** Voice doesn't replace your desk—it bridges the gap between "too tired to sit at my desk" and "excited enough to go back."

Example workflow:
1. Talk through ideas in the hammock
2. Claude Code stubs out implementations
3. Get excited about what you're seeing
4. Go inside where the same session is already open in your terminal

### When to Use It

| Good For | Not Good For |
|----------|--------------|
| Thinking through architecture | Precise syntax work |
| Exploring risky refactors | Code review |
| Creating Linear issues while driving | Documentation that needs formatting |
| Brainstorming during "off" hours | Pair programming with others |
| Breaking through activation energy | Tasks requiring immediate precision |

### How It Compares

| Feature | Happy Coder | speak_when_done | Crystal |
|---------|-------------|-----------------|---------|
| Primary Use | Voice input to Claude Code | TTS notification | Parallel sessions |
| Mobile | Yes | No | No |
| Sync | Real-time bidirectional | N/A | Git worktree |
| Input | Voice | N/A | Text |
| Platform | iOS, Android | macOS only | macOS, Windows |

### The Deeper Philosophy

> "Every engineer has that one idea... But you can't walk into Monday's standup and propose it without doing the homework first. These ideas need exploration time. But they can't get it because work hours are for delivering on commitments."

Voice coding enables "side bets"—low-commitment exploration of ideas that might transform your codebase but need unofficial thinking time that doesn't exist otherwise.

### Installation

Get Happy Coder at:
- GitHub: github.com/slopus/happy
- iOS App Store
- Android Play Store

The voice agent prompts are fully customizable inside the app—no need to fork and rebuild to try different approaches.

### Links

- Docs: https://happy.engineering/docs/features/voice-coding-with-claude-code/
- GitHub: https://github.com/slopus/happy

---

## Recall - Persistent Memory MCP Server for Claude

*Source: https://www.npmjs.com/package/@joseairosa/recall - Added: 2026-01-18*

An MCP server that gives Claude persistent memory via Redis, solving the context window problem by storing and retrieving relevant context across sessions.

### Core Features

- **Persistent Memory** - Memories survive context compaction and session restarts
- **Workspace Isolation** - Memories scoped by working directory (project A doesn't pollute project B)
- **Semantic Search** - Hybrid embeddings (Claude keywords + trigrams) for relevance retrieval
- **Session Snapshots** - Summarize and save entire sessions for later reference
- **Memory Relationships** - Link related memories, build knowledge graphs

### Memory Types

- `directive` - Guidelines and rules
- `decision` - Architecture and design decisions
- `code_pattern` - Code snippets and patterns
- `session` - Session summaries
- `context` - General context

### Workspace Modes (v1.3+)

- **isolated** (default) - Workspace-only memories, no cross-workspace access
- **global** - All memories shared globally
- **hybrid** - Both workspace-specific AND global memories

### Installation

```bash
# Via npx (auto-updates)
npx -y @joseairosa/recall

# Global
npm install -g @joseairosa/recall
```

### Configuration

```json
{
  "mcpServers": {
    "recall": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@joseairosa/recall"],
      "env": {
        "REDIS_URL": "redis://localhost:6379",
        "ANTHROPIC_API_KEY": "${ANTHROPIC_API_KEY}",
        "WORKSPACE_MODE": "hybrid"
      }
    }
  }
}
```

### Usage Examples

```
"Remember that our API base URL is https://api.example.com/v2"
"Store this as a directive: Always use functional components in React"
"Remember globally: I prefer TypeScript strict mode for all projects"
"What do you remember about our database schema?"
"Analyze our conversation and remember the important parts"
"Summarize this session and save it as 'Authentication Refactoring'"
```

### Key Tools

- `store_memory` / `store_batch_memories` - Store memories
- `search_memories` - Semantic search with fuzzy/regex support
- `recall_relevant_context` - Auto-retrieve relevant context
- `analyze_and_remember` - Extract memories from conversation
- `summarize_session` - Create session snapshots
- `convert_to_global` / `convert_to_workspace` - Change memory scope
- `link_memories` / `get_related_memories` - Build knowledge graphs
- `export_memories` / `import_memories` - Backup and restore

### Security Considerations

**Critical:** Recall stores conversation context in Redis, which may include sensitive data (API keys, credentials, proprietary code, personal info).

- Use dedicated, authenticated Redis instances
- Enable TLS encryption (`rediss://`) for remote connections
- Never use public/shared Redis for sensitive projects
- Regularly audit stored memories
- Consider Redis ACLs for fine-grained access control

### Why It's Interesting

- Solves the "repeating yourself" problem across sessions
- Automatic context injection at conversation start
- Cost-effective (~$0.20/day using Claude Haiku for analysis)
- Team collaboration via shared Redis
- Memory versioning and rollback (v1.5+)
- Templates for reusable memory patterns

### Links

- npm: https://www.npmjs.com/package/@joseairosa/recall
- Requires: Node.js 18+, Redis

---

## Crystal - Multi-Session Claude Code Manager

*Source: https://github.com/stravu/crystal (blog: https://stravu.com/blog/crystal-supercharge-your-development-with-multi-session-claude-code-management) - Added: 2026-01-18*

A desktop application (macOS) for managing multiple Claude Code sessions in parallel. Built by Stravu, who call it an "IVE" (Integrated Vibe Environment).

### The Problem It Solves

Running multiple Claude Code sessions from CLI is possible but cumbersome:
- Switching between sessions requires multiple commands
- Easy to forget what each session is working on
- No unified view of session status
- Git conflicts when working on parallel changes

### Key Features

- **Git Worktree Isolation**: Each session runs in its own git worktree, preventing conflicts
- **Real-time Session Dashboard**: Monitor all sessions from unified interface
- **Conversation Continuity**: Resume any session with full history intact
- **Integrated Git Operations**: Rebase, squash commits, view diffs without leaving the app
- **AI-Powered Session Naming**: Sessions auto-named based on prompts
- **Visual Status Tracking**: See which sessions are initializing, running, waiting, or completed
- **Execute & Test**: Run configured build/test scripts per worktree

### Use Cases

| Pattern | Description |
|---------|-------------|
| Multi-pass problem solving | Run same prompt multiple times, pick best solution |
| Parallel feature development | Work on feature A while testing feature B |
| Idea generation | Multiple "explore codebase and suggest improvements" sessions |
| UX experimentation | Several "improve the look of X" sessions to compare |

### Stravu Integration (MCP)

Crystal connects to Stravu's collaboration platform to bridge business and dev teams:
1. Write bugs/todos/features in Stravu notebook
2. Crystal turns each into test cases
3. Run tests, update status back in Stravu
4. Write code, sync progress

### Comparison

| Feature | Crystal | CLI Multi-Session |
|---------|---------|-------------------|
| Session isolation | Git worktrees | Manual |
| Session overview | Visual dashboard | tmux/screen splits |
| Status tracking | Built-in indicators | None |
| History resume | One-click | Manual session restore |
| Git operations | Integrated UI | Separate terminal |

### Open Source

Crystal is open source and accepts pull requests.

### Notes

- macOS desktop app only (currently)
- Solves the "AI downtime" problem while waiting for Claude Code responses
- Enables "parallel exploration" development style
- Good for comparing multiple approaches to same problem

---

## FleetCode - Parallel CLI Coding Agent Sessions

*Source: https://github.com/built-by-as/FleetCode - Added: 2026-01-18*

A desktop terminal application for running multiple CLI coding agents (Claude Code, Codex) simultaneously in isolated git worktrees. Similar to Crystal but with multi-agent support and terminal theming.

### Key Features

- **Multi-Agent Support**: Run Claude Code or Codex sessions in parallel
- **Git Worktree Isolation**: Each session runs in its own worktree, keeping work separate
- **Persistent Sessions**: Sessions persist across app restarts with automatic resumption
- **Terminal Theming**: Choose from presets (macOS Light/Dark, Solarized Dark, Dracula, One Dark, GitHub Dark)
- **Setup Commands**: Configure shell commands to run before the coding agent starts
- **MCP Server Management**: Add and configure Model Context Protocol servers per session
- **Session Management**: Rename, close, and delete sessions with automatic worktree cleanup

### Session Workflow

1. Select a project directory (must be a git repository)
2. Choose a parent branch for the worktree
3. Select your coding agent (Claude or Codex)
4. Optionally add setup commands (e.g., environment variables, source files)
5. FleetCode creates a new git worktree and spawns a terminal session

### Comparison with Crystal

| Feature | FleetCode | Crystal |
|---------|-----------|---------|
| Agents | Claude, Codex | Claude only |
| Terminal theming | Yes (6 presets) | No |
| MCP configuration | Built-in | Via Stravu |
| Session naming | Manual | AI-powered |
| Git operations | Basic | Integrated (rebase, squash) |
| Status tracking | Basic | Visual dashboard |

### Installation

```bash
npm install
npm run dev  # development
npm run build && npm start  # production
```

Requires: Node.js 16+, Git, Claude CLI or Codex

### Troubleshooting

- **macOS quarantine**: `xattr -cr /path/to/FleetCode.app`
- **Claude working directory issues**: Disable "Auto connect to IDE" in Claude config (`claude config` → set `autoConnectToIde` to false)

### Notes

- Good for developers who use multiple coding agents (not just Claude)
- Terminal theming helps differentiate sessions visually
- Setup commands useful for project-specific environment configuration
- Less polished than Crystal but more agent-flexible

---

## AG Grid MCP Server

*Source: https://blog.ag-grid.com/introducing-the-ag-grid-model-context-protocol-mcp-server/ - Added: 2026-01-18*

An MCP server that provides LLMs with version and framework-specific AG Grid context. Ensures responses use accurate, up-to-date documentation for the specific AG Grid version and framework you're using.

### The Problem It Solves

AG Grid has 350,000+ documentation pages across 99 versions and 4 frameworks, with new content added every six weeks. LLMs struggle with:
- Outdated training data missing recent features/APIs
- Framework nuances (React, Angular, Vue, Vanilla each have different syntax)
- Version-specific differences in configs and migration paths
- Residual context from removed documentation

### Key Components

- **Tools** - Schema-defined interfaces for searching docs and detecting/setting AG Grid version
- **Prompts** - Pre-configured actions for common tasks (creating grids, migrating versions)
- **Resources** - Documentation, examples, and API definitions in condensed markdown (optimized for token usage)

### Use Cases

- **Faster Initial Configuration** - Use `quick-start` prompt to scaffold a new grid tailored to your framework
- **Version Migration** - Use `upgrade-grid` prompt to get step-by-step migration guidance between versions
- **Feature Implementation** - Get precise instructions for complex features like Pivoting, Theming API, or Server Side Row Model

### Installation

```bash
# For Claude Code
claude mcp add ag-mcp -- npx ag-mcp
```

Works with any MCP-compatible LLM: Claude, Cursor, Copilot, etc.

### Notes

- Open source on GitHub (ag-mcp repo)
- LLM-optimized search delivers condensed markdown to minimize token usage
- Version-by-version migration approach ensures each step is correct before continuing
- Good example of domain-specific MCP servers that give LLMs expert knowledge in a particular library

---

## CopilotKit

*Source: https://www.copilotkit.ai/ - Added: 2026-01-18*

A framework for building in-app AI copilots—adding AI assistants directly into your application's UI rather than running them externally.

### Key Features

- **In-App AI Copilots** - Build AI assistants that live inside your application, not as separate tools
- **Single Command Setup** - `npx copilotkit@latest init` to get started
- **Pre-built Components** - Customizable UI components for chat interfaces, suggestions, etc.
- **Headless UI Option** - Use the logic layer without pre-built components for full design control

### Quick Start

```bash
npx copilotkit@latest init
```

### Why It's Interesting

- Different from other tools here—this is for **building** AI copilots into your apps, not for running coding agents
- 22.3k GitHub stars, 100k+ developers
- Good for adding AI assistance to user-facing applications (customer support, document editing, workflow automation)
- Bridges the gap between "AI chatbot" and "AI-native application"

### Use Cases

- In-app customer support copilots
- AI-powered document editors
- Workflow assistants embedded in dashboards
- Any app where you want AI to understand and act on app context

### Notes

- Compare with Vercel AI SDK, LangChain for similar use cases
- The "in-app" focus is key—agents have access to application state and can take actions within the app
- Different problem space from tools like Claude Code or Cursor which are coding assistants

---

## Amazon Bedrock AgentCore MCP Server

*Source: https://aws.amazon.com/about-aws/whats-new/2025/10/open-source-mcp-server-amazon-bedrock-agentcore - Added: 2026-01-18*

An open-source MCP server for Amazon Bedrock AgentCore that enables developers to analyze, transform, and deploy AI agents directly from their IDE using natural language.

### Key Features

- **One-Click Installation** - Integrates with Kiro, Claude Code, Cursor, and Amazon Q Developer CLI
- **Natural Language Development** - Use natural language to iteratively develop agents
- **AgentCore SDK Integration** - Transforms agent logic to work with the AgentCore SDK
- **Direct Deployment** - Deploy agents to development accounts from your IDE
- **Open Source** - Available on GitHub

### Compatible Tools

- Kiro (AWS agentic IDE)
- Claude Code
- Cursor
- Amazon Q Developer CLI

### Why It's Interesting

- Bridges local agent development with AWS deployment infrastructure
- Democratizes agent development by allowing natural language iteration
- Part of AWS's push into the MCP ecosystem
- Reduces friction between development and deployment of production agents

### Getting Started

- GitHub: AgentCore MCP Server repository
- Docs: AgentCore documentation
- Pricing: Amazon Bedrock AgentCore Pricing page

### Notes

- Pairs well with AWS Bedrock for model access
- Good for teams already in the AWS ecosystem who want to deploy production agents
- The "transform agent logic" feature suggests it can help migrate existing agent code to AWS patterns

---

## Nova Act IDE Extension

*Source: https://aws.amazon.com/blogs/aws/accelerate-ai-agent-development-with-the-nova-act-ide-extension/ - Added: 2026-01-18*

An IDE extension for building browser automation agents using natural language, built on top of the Amazon Nova Act SDK.

### Key Features

- **IDE Integration** - Works with VS Code, Cursor, and Kiro directly
- **Natural Language Generation** - Describe workflows in plain English to generate automation scripts
- **Builder Mode** - Notebook-style interface that breaks complex scripts into modular cells for individual testing/debugging
- **Live Preview** - Real-time browser preview panel to watch agent actions as they execute
- **Chat Interface** - Generate scripts via conversation with three modes: Ask, Edit, Agent
- **Templates** - Predefined templates for common tasks: `/shopping`, `/extract`, `/search`, `/qa`, `/formfilling`
- **Context Support** - Add active documents, instructions, MCP resources, and screenshots as context

### How It Works

1. Install extension from IDE marketplace
2. Get API key from Nova Act page
3. Use Builder Mode for notebook-style development OR chat to generate scripts
4. Test with integrated live browser view and step-by-step debugging
5. Output panel shows model's thinking and actions for debugging

### Workflow Modes in Chat

- **Ask** - Describe tasks in natural language to generate scripts
- **Edit** - Refine or customize generated scripts
- **Agent** - Run and monitor the AI agent performing the workflow

### Why It's Interesting

- Eliminates context switching between coding and browser testing
- Modular cell-based editing allows debugging individual steps before moving on
- Full-stack agent builder: prototype → customize → validate in one place
- Open source (Apache 2.0) and free to use
- Natural language + visual debugging is powerful combo for non-trivial automations

### Use Cases

- Form filling and data entry automation
- QA and testing workflows
- Web scraping and data extraction
- Online shopping automation
- Search and information gathering

### Notes

- Built on Amazon Nova Act SDK (preview)
- Good for teams wanting to build production browser automation without leaving their IDE
- Different from coding assistants like Claude Code—focused specifically on browser automation agents
- Templates provide quick starting points for common automation patterns

---

## Claude Proxy - Multi-Provider Routing for Claude API

*Source: https://github.com/raycastventures/claude-proxy - Added: 2026-01-18*

A Python-based proxy server for routing Claude API requests across multiple providers (AWS Bedrock, OpenRouter, Cerebras, Groq) with intelligent fallback, rate limiting, and request monitoring.

### Why Use This

The official Claude Bedrock support only allows one model and quickly times out on most AWS accounts (limited to 2 requests/minute without a lengthy support ticket process). This proxy allows you to specify multiple fallback models/regions to avoid 429 errors.

Also supports routing Haiku requests to Cerebras for near-instant responses. Note: Claude Code only uses Haiku for cosmetic messages like "Thinking..."

### Key Features

- **Multi-Provider Support** - AWS Bedrock, OpenAI, Cerebras, Groq, OpenRouter
- **Intelligent Fallback** - Automatic failover between providers and models on 429s
- **Rate Limiting** - Built-in protection against rate limits with configurable delays
- **Streaming Support** - Real-time response streaming
- **Request Monitoring** - SQLite-based request history tracking
- **Web Dashboard** - Streamlit frontend at :8501 for monitoring requests, token usage, success rates

### Quick Start

```yaml
# config.yaml
server:
  port: "3001"

providers:
  bedrock:
    region: us-west-2

routing:
  enable: true
  models:
    - model: "default"
      provider_sequence:
        - name: "bedrock"
          variants:
            - model: us.anthropic.claude-opus-4-1-20250805-v1:0
              region: us-west-2
            - model: us.anthropic.claude-sonnet-4-20250514-v1:0
              region: us-west-2
    - model: "haiku"
      provider_sequence:
        - name: "bedrock"
          variants:
            - model: us.anthropic.claude-3-5-haiku-20241022-v1:0
              region: us-west-2
            - model: us.anthropic.claude-3-5-haiku-20241022-v1:0
              region: us-east-1
  retry_timeout_millis: 1000
  rate_limit_seconds: 10
```

```bash
# Start with uv
uv run main.py

# Server runs on port 3001 by default
# Dashboard at http://localhost:8501
```

### Request Flow

```
Client → Proxy Server → Provider Selection → API Provider → Response
               ↓
       Bedrock (Sonnet) → Bedrock (Haiku) → OpenRouter (Sonnet) → Response
```

### API Endpoints

- `POST /v1/messages` - Main endpoint (add `"stream": true` for streaming)
- `GET /v1/models` - Available models
- `GET /health` - Health check
- `GET /debug` - Debug info

### Dashboard Features

- Request history with pagination
- Success/fail metrics and rates
- Token usage tracking
- Error analysis
- Real-time stats

### Why Not Claude Code Router (CCR)?

CCR is more complex. This proxy offers:
- Simpler architecture and setup
- Fallback support for 429s (especially useful on Bedrock)
- Dashboard focused on tracking, not config editing

### Requirements

- Python 3.10+
- AWS credentials configured for Bedrock
- OpenRouter API key (optional, for fallback)

### Use Case

Useful for Claude Code users on AWS Bedrock who frequently hit rate limits. Point your client at `http://localhost:3001` instead of the Anthropic API directly.

---

## Async - AI Coding + Task Management

*Source: https://www.async.build/ | GitHub: https://github.com/bkdevs/async-server - Added: 2026-01-18*

An open-source dev tool that combines AI coding with task management and code review. Positions itself as "Claude Code + Linear + GitHub PRs" in one opinionated tool.

### Key Features

- **GitHub-Native** - Each task is a GitHub issue, PRs created automatically
- **Cloud Execution** - Tasks run in isolated Google Cloud Run containers, not locally
- **Research Agent** - Confirms requirements and asks clarifying questions before coding
- **Focused Scope** - Intentionally limited to busywork (bug fixes, UI tweaks, simple features)
- **Stacked Diffs** - Breaks work into reviewable subtasks with built-in code review
- **Open Source** - MIT licensed, full source available

### Tech Stack

- Backend: FastAPI with async support
- AI Models: Claude Code for implementation, OpenAI/Anthropic/Google models for research
- Cloud: Google Cloud Platform with containerized execution (Cloud Run jobs)
- Database: Firebase Firestore
- Integrations: GitHub App, Stripe payments

### Philosophy

The interesting differentiator: Async says "no" and asks clarifying questions instead of blindly attempting tasks. Designed to make users think and encourage structured, critical thinking over lazy convenience-first interfaces.

> "Coding agents can't do everything and we think it's a mistake to ask them to do more than they can."

### Pricing

- Free tier: 10 tasks/day
- Paid: $20/month

### Why It's Interesting

- Opinionated approach that pushes back against "ask AI to do everything" mindset
- Research-first workflow ensures requirements are clear before execution
- GitHub integration means PRs and issues stay in familiar tooling
- Self-aware about AI limitations - doesn't oversell capabilities

### Concerns

- Cloud execution means code runs on their infrastructure
- Limited to "busywork" - may not replace more capable local agents for complex work
- Dependency on their hosted service for execution

---

## pexpect-mcp - Interactive Debugging for AI Agents

*Source: https://github.com/mitsuhiko/pexpect-mcp - Added: 2026-01-18*

An MCP server by Armin Ronacher (mitsuhiko) that provides remote pexpect session control, enabling AI agents to interact with debuggers and CLI tools that require programmatic interaction.

### What It Does

Enables AI assistants to run Python code with pexpect functionality, allowing interactive sessions with:
- LLDB and GDB debuggers
- REPLs and interactive shells
- Any CLI tool that requires back-and-forth interaction

Essentially maintains a stateful Python session that AI agents can control.

### Installation

```bash
uv tool install git+https://github.com/mitsuhiko/pexpect-mcp
```

### MCP Configuration

```json
{
  "mcpServers": {
    "pexpect": {
      "command": "pexpect-mcp"
    }
  }
}
```

### Usage Example

```python
# Start a debugging session
child = pexpect.spawn('lldb ./my-program')
child.expect('(lldb)')

# Run the program
child.sendline('run')
child.expect('(lldb)')
print(child.before.decode())

# Get backtrace
child.sendline('bt')
child.expect('(lldb)')
print(child.before.decode())
```

### Requirements

- Python ≥ 3.12.1
- pexpect ≥ 4.9.0
- mcp ≥ 1.13.0

### Why It's Interesting

- From mitsuhiko (creator of Flask, Rye, etc.) - high-quality engineering expected
- Enables AI to debug native code by controlling LLDB/GDB
- Bridges AI agents to interactive tools that can't be scripted with simple command execution
- Includes demo with buggy C program for testing

### Use Cases

- AI-assisted debugging of crashes in compiled programs
- Interactive exploration of complex CLI tools
- Teaching/learning debugging with AI assistance
- Automated crash analysis and root cause identification

---

## Magnet - Parallel Claude Code Agent Orchestration

*Source: https://www.magnet.run/ - Added: 2026-01-18*

A platform for running multiple Claude Code agents in parallel sandboxes with AI-powered context management and documentation assistance.

### What It Does

- **Parallel Sandboxes** - Run multiple Claude Code agents simultaneously in isolated environments
- **Context Suggestions** - Automatically suggests relevant context for tasks
- **Documentation Maintenance** - Helps write and maintain comprehensive product docs that agents can reference
- **Tool Supercharging** - Enhances existing workflows rather than replacing them

### Key Features

- Parallel agent execution without interference
- AI-curated context recommendations
- Product documentation as first-class concern (agents work better with good docs)
- Integrates with existing tooling

### Why It's Interesting

- Addresses the "one agent at a time" limitation of local Claude Code
- Context management is a key bottleneck - automatic suggestions could improve agent effectiveness
- Docs-first philosophy aligns with good engineering practices (better docs → better agent output)
- Positioned as enhancer rather than replacement - works with tools you already use

### Comparison

| Feature | Magnet | Crystal | Conductor |
|---------|--------|---------|-----------|
| Parallel Agents | Yes (sandboxes) | Yes (multi-session) | Yes (workspaces) |
| Context Management | AI-suggested | Manual | Shared context |
| Documentation | Built-in assistant | N/A | N/A |
| Isolation | Sandbox-based | Session-based | Workspace-based |

### Considerations

- Cloud-based execution (code runs on their infrastructure)
- Unclear pricing model
- Adds another abstraction layer on top of Claude Code

### Links

- Website: https://www.magnet.run/

---

## Stagewise - Browser Toolbar for Frontend AI Coding

*Source: https://github.com/stagewise-io/stagewise - Added: 2026-01-18*

A browser toolbar that connects your frontend UI directly to AI coding agents in your code editor. Select elements visually and let AI make the changes.

### Key Features

- **Visual Element Selection** - Click on any element(s) in your web app to provide context
- **Comment & Context** - Leave comments on elements, sends DOM + metadata to AI agent
- **Multi-Framework Support** - React, Vue, Svelte, and more
- **Plugin System** - Extend functionality with custom plugins
- **Quick Setup** - Install extension + inject toolbar, works out of the box

### Supported Editors

- Cursor
- VS Code
- Trae
- Windsurf

### Installation

```bash
# 1. Install extension from your editor's marketplace
# 2. Install toolbar package
pnpm i -D @stagewise/toolbar

# 3. Inject in dev mode
import { initToolbar } from '@stagewise/toolbar';

if (process.env.NODE_ENV === 'development') {
  initToolbar({ plugins: [] });
}
```

Or use the AI-assisted setup: `CMD + Shift + P` → `setupToolbar`

### Why It's Interesting

- **Visual-first workflow** - Point at what you want to change instead of describing it
- **Bridges UI and code** - Particularly useful for frontend work where visual context matters
- **Agent-agnostic** - Works with various AI agents through editor extensions
- **Native frontend agent coming** - Building their own faster agent optimized for UI work

### Comparison

| Feature | Stagewise | Heatmap (0github) | Standard AI Coding |
|---------|-----------|-------------------|-------------------|
| Visual Selection | Yes (live UI) | Yes (diff view) | No |
| Context Source | DOM elements | Code changes | File content |
| Best For | Frontend editing | Code review | General coding |
| Integration | Browser + editor | GitHub URL swap | Editor only |

### Considerations

- AGPLv3 license (may limit commercial use without enterprise agreement)
- Requires toolbar injection into your dev build
- Most valuable for visual/frontend work specifically

### Links

- GitHub: https://github.com/stagewise-io/stagewise
- Discord: Community support available

---

## Amazon Q Developer CLI Custom Agents

*Source: https://aws.amazon.com/blogs/devops/overcome-development-disarray-with-amazon-q-developer-cli-custom-agents/ - Added: 2026-01-18*

Custom agents in Amazon Q Developer CLI allow developers to create tailored configurations for different development contexts (front-end, back-end, testing, data science, etc.), making it easy to switch between projects with different tech stacks.

### Problem Solved

When working on multi-tier apps with different tools (e.g., Figma for frontend, PostgreSQL for backend), having all MCP servers loaded creates ambiguity. If you ask "how many tables do I have?", Q Developer can't tell if you mean HTML tables or SQL tables.

### Key Features

- **Context-Specific MCP Servers** - Load only the tools relevant to the current task
- **Tool Permissions** - Fine-grained control over which tools are trusted (auto-run) vs require confirmation
- **Resources** - Pre-load context files (README, coding preferences) into the session
- **Hooks** - Run commands at agent spawn (e.g., `git status`) to inject runtime context

### Configuration

Agents stored in `~/.aws/amazonq/agents/<name>.json`:

```json
{
  "description": "Optimized for front-end web development using React and Figma",
  "mcpServers": {
    "Figma": {
      "command": "npx",
      "args": ["mcp-remote", "http://127.0.0.1:3845/sse"]
    }
  },
  "tools": ["*"],
  "allowedTools": [
    "fs_read",
    "fs_write",
    "report_issues",
    "@Figma"
  ],
  "resources": [
    "file://README.md",
    "file://~/.aws/amazonq/react-preferences.md"
  ],
  "hooks": {
    "agentSpawn": [
      { "command": "git status" }
    ]
  }
}
```

### Usage

```bash
q chat --agent front-end   # Use front-end agent with Figma
q chat --agent back-end    # Use back-end agent with PostgreSQL
```

### Tool Permission Patterns

- `@Figma` - Trust all tools from the Figma MCP server
- `@PostgreSQL/get_table_schema` - Trust only specific tool from server
- `fs_read`, `fs_write` - Trust individual built-in tools

### Example Agents

| Agent | MCP Server | Trusted Tools | Resources |
|-------|-----------|---------------|-----------|
| front-end | Figma | fs_read, fs_write, @Figma | react-preferences.md |
| back-end | PostgreSQL | fs_read, @PostgreSQL/get_table_schema | python-preferences.md, sql-preferences.md |
| testing | - | fs_read, execute_bash | testing-guidelines.md |

### Why It's Useful

- **Reduced cognitive overhead** - No need to manually reconfigure between projects
- **Safer workflows** - Only trust tools appropriate for the current context
- **Consistent context** - Preferences and project context auto-loaded
- **Language clarity** - Eliminates ambiguity when same terms mean different things in different contexts

### Related

- See also: [AWS Q Developer Cost Management](/Users/jesse/jpt/knowledge/aws-q-developer-cost-management.md) for Q Developer's cost analysis capabilities
- MCP servers for AWS services available from AWS Labs GitHub

---

## Amazon Q Developer - State of the Art Software Development Agent

*Source: https://aws.amazon.com/about-aws/whats-new/2025/04/amazon-q-developer-releases-state-art-agent-feature-development - Added: 2026-01-18*

Amazon Q Developer's software development agent update achieves top-tier benchmarks: **49% on SWE-Bench Verified** (state-of-the-art) and **66% on SWEBench Verified** (among top ranking models).

### What's New

- **Multi-candidate solution generation** - Agent generates multiple solutions for a problem, evaluates them, and selects the best one
- **Dedicated execution environment** - Runs in isolated environment with full modern IDE capabilities
- **Advanced planning and reasoning** - Uses tools that leverage advanced models' full capacity
- **Higher quality code output** - Improved reliability means less debugging time

### How to Use

1. Install Amazon Q Developer plugin in VS Code or JetBrains IDE
2. Type `/dev` in the Q chat window
3. Describe the feature or problem
4. Agent handles planning, coding, and returns high-quality solution

### Why It Matters

- SWE-Bench Verified is the industry standard for evaluating AI coding agents on real-world software engineering tasks
- 49% SOTA puts Q Developer ahead of or competitive with most frontier models
- Multi-candidate approach mirrors how experienced developers explore solution space before committing
- Available in all AWS Regions where Amazon Q is supported

### Availability

- VS Code (via Amazon Q Developer plugin)
- JetBrains IDEs (via Amazon Q Developer plugin)
- Invoke with `/dev` command in chat

---

## Kiro - Spec-Driven Agentic IDE

*Source: https://kiro.dev/blog/introducing-kiro/ - Added: 2026-01-18*

An agentic IDE from AWS that emphasizes spec-driven development—moving beyond "vibe coding" to help get prototypes into production systems through structured requirements, design docs, and task management.

### Key Features

- **Spec-Driven Development** - Generates requirements, technical designs, and implementation tasks from prompts
- **Three-Phase Specs**:
  1. **Requirements** - User stories with EARS notation acceptance criteria
  2. **Design Docs** - Data flow diagrams, TypeScript interfaces, DB schemas, API endpoints
  3. **Tasks** - Sequenced tasks with sub-tasks, linked back to requirements
- **Agent Hooks** - Event-driven automations that run when you save/create/delete files
- **VS Code Compatible** - Built on Code OSS, keeps VS Code settings and Open VSX plugins
- **MCP Support** - Model Context Protocol for connecting specialized tools
- **Steering Rules** - Guide AI behavior across your project

### How Specs Work

1. **Prompt** → "Add a review system for products"
2. **Requirements Generated** → User stories for viewing, creating, filtering, rating reviews with acceptance criteria
3. **Design Generated** → Analyzes codebase, creates interfaces, schemas, API endpoints
4. **Tasks Generated** → Sequenced implementation tasks with dependencies, tests, accessibility requirements
5. **Execute** → Run tasks one-by-one with progress tracking and audit trail

### Hooks Examples

Hooks enforce consistency automatically across teams:

- Save React component → Updates test file
- Modify API endpoints → Refreshes README
- Pre-commit → Security scan for leaked credentials
- New component → Validates against coding standards (e.g., Single Responsibility Principle)

### Why It's Interesting

- **Documentation-first approach** - Addresses the common problem where docs drift from implementation
- **Production-focused** - Explicitly designed for getting past the prototype phase
- **Auditable** - Can view code diffs and agent execution history
- **Team scalability** - Hooks committed to Git enforce standards across entire team
- **Free during preview** - Currently in preview with some limits

### Comparison

| Feature | Kiro | Claude Code | Cursor | Amp |
|---------|------|-------------|--------|-----|
| Spec Generation | Yes (3-phase) | No | No | Partial |
| Auto-Documentation | Yes (stays synced) | No | No | No |
| Hooks/Automations | Yes (file events) | Yes (claude hooks) | No | No |
| Task Management | Built-in | Via TodoWrite | No | Yes |
| VS Code Compatible | Yes | Via extension | Fork | Fork |

### Considerations

- AWS product - likely integrates well with AWS ecosystem
- Spec-driven approach adds overhead vs. pure vibe coding
- Trade-off: more structure = more production-ready, but less immediate gratification
- Built on Code OSS, not a web-based IDE

### Links

- Website: https://kiro.dev/
- Tutorial: Available after installation
- Discord: Community server available

---

## GitHub Copilot Agent Mode + MCP Workflow

*Source: https://austen.info/blog/github-copilot-agent-mcp/ - Added: 2026-01-18*

A structured workflow for using GitHub Copilot Agent Mode in VS Code with MCP servers, custom chat modes, and prompt files for phased development.

### Key Concepts

1. **Custom Instructions** - Define coding practices, preferences, and constraints that persist across sessions
2. **Custom Chat Modes** - Create specialized modes for different phases (research, planning, implementation)
3. **Prompt Files** - Store reusable task templates in `.github/prompts/*.prompt.md`
4. **MCP Servers** - Extend agent capabilities with external tools

### Recommended VS Code Settings

```json
{
  "github.copilot.chat.codeGeneration.instructions": "...",  // Custom coding instructions
  "chat.agent.maxRequests": 50,  // Let agent run longer without asking permission
  "chat.tools.autoApprove": true  // Auto-approve run commands and tool requests
}
```

### Useful MCP Servers

- **Sequential Thinking** - Reflective problem-solving through thought sequences
- **SearXNG** - Web search capabilities
- **Playwright** - Browser automation and testing
- **GitHub** - Repository management and file operations
- **time** - Current time/date access
- **Fetch** - Web content fetching for LLM consumption

### Phased Workflow

#### 1. Research Phase
- Use custom "research" chat mode with web search + sequential thinking tools
- Model: Gemini 2.5 Pro (good for synthesis)
- Goal: Understand concepts, evaluate approaches

#### 2. Planning Phase
- Use custom "plan" chat mode with code editing disabled
- Model: Gemini 2.5 Pro
- Output: `.github/prompts/<feature>.prompt.md` file
- The prompt file serves as a blueprint/contract for implementation

#### 3. Implementation Phase
- Switch to regular agent mode
- Model: Claude Sonnet 4 (better for code generation)
- Run prompt with `/prompt-name` command
- Agent executes the plan with full context

#### 4. Course Correction
When agent deviates:
1. Clear git diff to reset changes
2. Modify the prompt file based on learnings
3. Restart implementation from scratch

This iterative refinement improves prompts for future use.

#### 5. Validation
- Use Playwright MCP for UI testing
- Agent can browse and interact with the application
- Enables visual verification of implementations

### Why This Approach Works

- **Separation of concerns** - Different models for different strengths (Gemini for planning, Claude for implementation)
- **Prompt files as contracts** - Planning phase output becomes implementation phase input
- **Reproducibility** - Documented prompts make complex tasks repeatable
- **Tool-aware modes** - Each phase has only the tools it needs
- **Iterative improvement** - Prompts get refined over time

### Comparison to Other Workflows

| Aspect | Copilot Agent + MCP | Claude Code | Kiro |
|--------|---------------------|-------------|------|
| Planning | Custom chat modes + prompt files | Built-in (via TodoWrite) | Spec-driven (3-phase) |
| Tool Access | MCP servers | Native tools + MCP | MCP + agent hooks |
| Model Choice | Can switch per phase | Fixed (Claude) | AWS Bedrock models |
| Prompt Reuse | .prompt.md files | CLAUDE.md + skills | Specs stored in project |

### Notes

- Requires VS Code with Copilot Chat extension
- Custom chat modes need manual setup in settings
- The "prompt file as contract" pattern could work with other agents too
- Good example of using right model for each phase rather than one-size-fits-all

---

## Qodo (formerly Codium) - Quality-First AI Coding Platform

*Source: https://www.qodo.ai/ - Added: 2026-01-18*

AI coding platform emphasizing code quality throughout the development pipeline. Formerly known as Codium.

### Key Products

- **Qodo Gen** - Generative AI solutions for code quality
- **Qodo Gen CLI** - Command-line interface for building, running, and managing AI agents (currently in Alpha)
- **Code Integrity Platform** - Bulletproof code quality tooling

### Features

- Generative AI solutions across the development pipeline
- CLI for AI agent management
- Focus on code quality over just code generation
- Python-focused (based on marketing materials showing Python code review tools)

### Why It's Interesting

- "Quality-first" positioning differentiates from pure code generation tools
- CLI for managing AI agents suggests infrastructure-level tooling
- Codium rebranding to Qodo suggests a pivot toward broader platform play
- Worth tracking as code quality + AI is an underexplored combination

### Notes

- Qodo Gen CLI is in Alpha as of mid-2026
- Previously known as Codium (not to be confused with VS Codium, the OSS VS Code fork)
- Positioned more as code quality tooling than pure agent/assistant

---

## Amp - Agentic Coding Tool

*Source: https://ampcode.com/ - Added: 2026-01-18*

An agentic coding tool designed to maximize capabilities with frontier models—autonomous reasoning, comprehensive code editing, and complex task execution.

### Key Features

- **Autonomous Reasoning** - Built for agentic workflows, not just autocomplete
- **Comprehensive Code Editing** - Handles multi-file changes and refactoring
- **Complex Task Execution** - Designed for longer-running, multi-step tasks
- **Frontier Model Focus** - Optimized for latest generation models

### Why It's Interesting

- Explicitly designed for the "agentic" paradigm rather than copilot-style assistance
- Competes with Claude Code, Cursor Agent Mode, and Codex in the autonomous coding space
- Emphasis on maximizing what frontier models can do suggests they may be early to adopt new model capabilities
- Could shift required skill set toward adaptability over traditional coding skills

### Considerations

- New entrant in increasingly crowded agentic coding space
- Worth tracking how they differentiate from established players
- Balance automation with maintaining foundational coding understanding

### Notes

- As of mid-2026, positioned as a standalone agentic tool
- Testimonials suggest good support/community engagement

---

## Codacy Guardrails - AI Code Quality & Security Enforcement

*Source: https://docs.codacy.com/codacy-guardrails/codacy-guardrails-getting-started/ - Added: 2026-01-18*

Real-time code security and quality enforcement for AI-generated code, built into the free Codacy IDE extension. Blocks insecure patterns and applies best practices while code is being generated.

### Key Features

- **Real-Time AI Code Scanning** - Catches issues as AI generates code
- **MCP Server Integration** - Query Codacy findings from AI chat panels
- **Multi-IDE Support** - VSCode, Cursor, Windsurf, Claude Desktop
- **Built-in Scanners** - Trivy, Semgrep, ESLint, Pylint, PMD, dartanalyzer, Lizard

### Supported Platforms

- macOS, Linux, Windows (WSL only for now)
- VSCode (Insiders recommended), Cursor, Windsurf

### Quick Setup

```bash
# 1. Install extension from IDE marketplace
# 2. Install Codacy CLI
brew install codacy/codacy-cli-v2/codacy-cli-v2  # macOS
# or
bash <(curl -Ls https://raw.githubusercontent.com/codacy/codacy-cli-v2/main/codacy-cli.sh)  # Linux

# 3. Install tools for analysis
codacy-cli install

# 4. Add MCP server via extension UI or manually
```

### MCP Server Configuration

For Cursor/Windsurf/Claude Desktop (in respective config files):
```json
{
  "mcpServers": {
    "codacy": {
      "command": "npx",
      "args": ["-y", "@codacy/codacy-mcp"],
      "env": {
        "CODACY_ACCOUNT_TOKEN": "<YOUR_TOKEN>",
        "CODACY_CLI_VERSION": "<VERSION>"
      }
    }
  }
}
```

For VSCode Copilot (in settings.json):
```json
{
  "mcp": {
    "servers": {
      "codacy": {
        "command": "npx",
        "args": ["-y", "@codacy/codacy-mcp"],
        "env": {
          "CODACY_ACCOUNT_TOKEN": "<YOUR_TOKEN>"
        }
      }
    }
  }
}
```

### Why It's Interesting

- Addresses the "AI code quality" problem - catches security issues before they ship
- MCP integration means you can ask about findings without leaving chat
- Free tier available via IDE extension
- Complements Claude Code/Cursor workflow rather than replacing it

### Considerations

- Creates `.codacy` folder in repos (add to .gitignore if unwanted)
- Manual MCP setup requires creating AI rules yourself (extension handles this automatically)
- Windows requires WSL setup
- Need to use Agent mode in Copilot chat for MCP features

### Notes

- NPM package: `@codacy/codacy-mcp`
- Pairs well with existing coding agent workflows as a quality gate
- Real-time feedback loop could speed up AI code iteration

---

## Jules - Google's Async Coding Agent

*Source: https://jules.google/docs/ - Added: 2026-01-18*

An experimental coding agent from Google that integrates with GitHub to handle bug fixes, documentation, and feature development asynchronously.

### Key Features

- **GitHub Integration** - Connects to your repos, clones code, and creates PRs
- **Asynchronous Workflow** - Submit task and walk away; get notified when done
- **Plan Review** - Generates a plan before making changes; you approve before execution
- **Virtual Machine Execution** - Runs in isolated VM, installs deps, modifies files

### How It Works

1. Connect GitHub account and select repos
2. Choose repository and branch
3. Write a specific prompt (e.g., "Add a test for parseQueryString in utils.js")
4. (Optional) Add environment setup scripts
5. Review and approve the generated plan
6. Jules executes and notifies when complete

### Quick Start

1. Visit jules.google.com
2. Sign in with Google account
3. Connect GitHub (all repos or specific ones)
4. Select repo, write prompt, approve plan

### Comparison with Other Agents

| Feature | Jules | Claude Code | Cursor | Codex |
|---------|-------|-------------|--------|-------|
| Primary Mode | Async/background | Interactive | Interactive | Async |
| VCS Integration | GitHub native | Git CLI | Git CLI | GitHub |
| Plan Review | Required | Optional | No | Yes |
| Execution | Cloud VM | Local | Local | Cloud |

### Use Cases

- Bug fixes while you're in meetings
- Documentation generation
- Routine feature additions
- Test writing

### Considerations

- Experimental/early stage
- Requires Google account
- Limited to GitHub (no GitLab, Bitbucket)
- Cloud execution means code goes to Google's servers

### Notes

- Fits the "delegate and forget" async agent pattern
- Good for tasks that don't need real-time iteration
- Browser notifications keep you informed without constant monitoring
- [Jules Awesome Prompts repo](https://github.com/google/jules-awesome-prompts) has real-world examples


---

## ask-human MCP - Human-in-the-Loop for AI Agents

*Source: https://masonyarbrough.com/blog/ask-human - Added: 2026-01-18*

An MCP server that lets AI agents ask questions instead of hallucinating. When the agent is confused or uncertain, it can "raise its hand" and wait for human input.

### The Problem

- AI agents blurt out endpoints that never existed
- False confidence leads to assumptions that are simply wrong
- Debugging hallucinations wastes hours when the agent could just ask

### How It Works

```
agent → ask_human()
⬇
question lands in ask_human.md
⬇
you swap "PENDING" for the answer
⬇
agent keeps coding
```

### Installation

```bash
pip install ask-human-mcp
ask-human-mcp --help
```

### Cursor Setup

`.cursor/mcp.json`:
```json
{
  "mcpServers": {
    "ask-human": { "command": "ask-human-mcp" }
  }
}
```

Restart Cursor and the tool is available.

### Features

- Zero config, cross-platform
- File-watching for instant feedback
- Supports multiple agents
- Built-in locks and limits
- Full Q&A history in markdown (debugging paper trail)

### Why It Matters

Reframes AI coding assistants as "sharp interns who actually ask before guessing" rather than fully autonomous agents. The escape hatch prevents the frustrating cycle of AI confidently producing wrong outputs.

### See Also

- Context engineering patterns in `context-engineering-agents.md`
- MCP protocol adoption in `mcp-protocol-adoption.md`

---

## OpenAI Codex - Hands-on Review

*Source: https://zackproser.com/blog/openai-codex-review - Added: 2026-01-18*

Chat-first interface for managing coding tasks across GitHub repositories. Designed for firing off many tasks in parallel.

### How It Works

1. Enable MFA (required)
2. Authorize Codex GitHub app for your orgs
3. Codex clones repos into sandboxed environments
4. Specify repo + branch, then describe tasks in natural language
5. Tasks run in parallel; check in on progress, request changes via chat
6. Hit "Open PR" when satisfied

### Strengths

- **Multi-threaded workflow** - Initiate a day's worth of tasks in parallel via natural language
- **Mobile-friendly** - Usable from phone for "untethered workflow" (checking in while away from desk)
- **Chat-based follow-ups** - Click into any task for familiar chat interface to iterate
- **Auto PR creation** - One click opens PR with auto-filled description
- **Logs visibility** - View raw commands/shells Codex spawns to make changes

### Current Limitations (as of mid-2025)

- **Poor error handling** - Tasks fail with unclear error messages
- **One-shot execution** - ~40-60% chance of being satisfied enough to merge without changes
- **Multi-turn updates awkward** - Pushing follow-up commits to existing branches is clunky
- **PR proliferation** - Encourages creating new PRs rather than iterating on existing branches
- **No network in sandbox** - Can't run `pnpm add @package@latest` or resolve dependencies
- **Maintenance-level tasks only** - Large refactors become cumbersome quickly

### Best Use Cases

- Minor copy tweaks
- Style changes
- Small maintenance chores
- Tasks that can ship in a single pass

### Not Great For

- Large refactors
- Multi-step feature building
- Dependency updates (no network access)
- Tasks requiring iteration

### Productivity Assessment

Not yet a game-changer, but has potential once:
- More tasks become one-shottable
- Multi-turn branch updates improve
- Additional integrations (image generation, etc.) arrive
- Orchestration layer matures

Currently useful for "flushing low-priority maintenance tasks at the start of the day." For significant work, an IDE with LLM support is still more effective.

### Comparison

| Feature | Codex | Claude Code | Cursor | Jules |
|---------|-------|-------------|--------|-------|
| Primary Mode | Async/parallel | Interactive | Interactive | Async |
| Interface | Chat-first web | CLI | IDE | Browser |
| Multi-task | Native | Via subagents | No | Via queue |
| Network Access | No (sandboxed) | Yes | Yes | Unknown |
| PR Workflow | Built-in | Manual | Manual | Built-in |
| Best For | Bulk maintenance | Complex work | Daily coding | Delegate & forget |

### Pricing

- Requires Pro subscription ($200/month) or invite

---

## codesys SDK - Python SDK for Claude CLI Automation

*Source: https://github.com/RVCA212/codesys - Added: 2026-01-18*

Python SDK for programmatically interacting with the Claude CLI tool. Enables scripting Claude Code workflows, particularly useful for plan-then-execute patterns.

### Installation

```bash
pip install codesys
```

Requires Python 3.8+ and Claude CLI installed and configured.

### Basic Usage

```python
from codesys import Agent

agent = Agent(working_dir="/path/to/project/")
lines = agent.run("/init", stream=True)
```

### Key Workflow: Plan Then Execute

The recommended pattern mirrors effective human-Claude Code interaction:

```python
def generate_plan(working_dir, user_message):
    """Generate a plan in plan.md based on the user message."""
    prompt = f'''
generate a plan into plan.md file given the following task:
<task>
{user_message}
</task>
Given this task, explore the codebase and create a plan for the implementation into plan.md. ultrathink
'''
    Agent(working_dir=working_dir).run(prompt, stream=True)

def execute_plan(working_dir):
    """Execute the plan laid out in plan.md."""
    prompt = 'Implement the task laid out in plan.md: ultrathink'
    Agent(working_dir=working_dir).run(prompt, stream=True)
```

### API Reference

**Agent Class:**
- `Agent(working_dir=None, allowed_tools=None)` - Initialize with directory and optional tool restrictions
- Default tools: `["Edit", "Bash", "Write"]`

**Methods:**
- `run(prompt, stream=False, output_format=None, additional_args=None, auto_print=True)` - Run Claude with prompt
- `run_with_tools(prompt, tools, stream=False)` - Run with specific tools for one operation

**Streaming Options:**
- `stream=True, auto_print=True` - Prints output, returns collected lines
- `stream=True, auto_print=False` - Returns subprocess.Popen for manual handling
- `stream=False` - Returns complete output as string

### Tool Restriction Example

```python
# Restrict to read-only tools
agent = Agent(working_dir="./", allowed_tools=["View"])

# Or temporarily restrict for one operation
agent.run_with_tools(
    prompt="List files in current directory",
    tools=["Bash"],
    stream=False
)  # Original tools restored after call
```

### Why It's Interesting

- **Scriptable Claude Code** - Automate repetitive Claude workflows
- **Plan-Execute Pattern** - Codifies the two-phase approach that works well with agentic coding
- **Tool Sandboxing** - Can restrict agent capabilities per-task
- **Streaming Support** - Real-time output for long-running tasks
- **Simple Wrapper** - Thin SDK, easy to understand and extend

### Comparison to Other Approaches

| Approach | Use Case |
|----------|----------|
| codesys SDK | Python scripts automating Claude CLI |
| Direct Claude CLI | Interactive terminal sessions |
| Async Server | Background Claude Code instances |
| Crystal | Multi-agent orchestration |

### Limitations

- Requires Claude CLI already configured
- No built-in concurrency management
- "ultrathink" prompts in examples are prompt engineering, not SDK features

License: MIT

---

## Flowcode - Visual AI Workflow Builder with Open-Source Core

*Source: https://www.getflowcode.io/ - Added: 2026-01-18*

A low-code platform for building production-grade AI workflows visually. Differentiator is the open-source core (Flyde) enabling self-hosting without vendor lock-in.

### Key Features

- **Visual Canvas** - Drag-and-drop workflow builder for AI agents, integrations, and logic
- **AI Copilot** - Adjust or build entire flows using natural language
- **Visual Debugging** - Debug workflows visually instead of tracing through code
- **One-Click Deploy** - Deploy workflows without infrastructure management
- **Turing-Complete** - Full flexibility for complex logic, not limited to simple automations

### Open-Source Foundation: Flyde

The key differentiator - Flowcode is built on Flyde, an open-source visual programming language:

- **Export Without Lock-in** - Export flows as `.flyde` files, run them with VS Code extension
- **No Docker Required** - Just paste the flow file, no heavyweight container infrastructure
- **Self-Hostable** - Keep full control of execution environment

### Target Users

| Role | Use Case |
|------|----------|
| Technical PMs | Add AI features, iterate on prompts without full dev cycles |
| Backend Developers | Create AI-driven APIs with visual debugging |
| IT/Automation Experts | Build and review AI automations quickly |

### Example Use Case

> "This flow is triggered via the SDK by a new user signup and generates insights on every new user"

Shows integration pattern: external triggers (signup event) → workflow execution → data generation

### Comparison to Similar Tools

| Feature | Flowcode | Sim Studio | Inkeep | n8n |
|---------|----------|------------|--------|-----|
| Primary Focus | AI workflows | Agent workflows | AI agents | General automation |
| Visual Editor | Yes | Yes (ReactFlow) | Yes | Yes |
| Open Source | Core (Flyde) | Full | Partial | Full |
| Self-Host | Yes (export flows) | Yes (Docker) | Unknown | Yes |
| AI Copilot | Yes | Unknown | No | No |
| VS Code Integration | Yes (Flyde extension) | No | No | No |

### Why It's Interesting

- **No vendor lock-in** - Open-source Flyde means you can export and self-host without converting to code
- **Hybrid approach** - Get low-code speed with code-level flexibility
- **VS Code bridge** - Flows can be edited in VS Code via extension, bridging visual and code-first workflows
- **Founder-level support** - Small team, responsive to feature requests

### Trade-offs

- Newer platform (less ecosystem/community than n8n or Make)
- Requires learning Flyde visual paradigm
- Cloud-first (self-hosting via export, not traditional deployment)

### Pricing

Not detailed on landing page - likely freemium with cloud hosting tiers.

---

## TmuxAI - AI-Powered Terminal Assistant

*Source: https://tmuxai.dev/ - Added: 2026-01-18*

Non-intrusive terminal assistant that runs alongside you in a tmux pane. Observes your terminal screen and provides context-aware help based on what's visible - mimics a colleague watching your screen.

### Installation

```bash
curl -fsSL https://get.tmuxai.dev | bash
```

### Key Features

- **Context-Aware Assistance** - Reads and understands what's displayed across all tmux panes in real-time
- **Zero-Configuration** - Works with existing tmux setup, no special shells or wrappers needed
- **Universal Compatibility** - Works with nested shells, SSH, database CLIs, network equipment shells (Cisco IOS, Juniper, etc.)
- **Proactive Mode** - Can monitor terminal activity and offer improvements based on your goals
- **Open Source** - Free to use and adapt

### How It Works

1. Runs in a tmux pane alongside your work
2. Observes visible terminal content across panes
3. Provides suggestions with confirmation prompts: `[Y]es/No/Edit`
4. Can execute commands on your behalf after approval

### Example Usage

```
$tmuxai find large files and cleanup some space

TmuxAI » find . -type f -size +100M -exec du -h {} \; | sort -rh | head -5
Do you want to execute this command? [Y]es/No/Edit:
```

### Why It's Interesting

- **Non-intrusive philosophy** - Watches your screen like a pair-programming partner, doesn't require special terminal setup
- **Works anywhere** - SSH sessions, database CLIs, router config - any text-based terminal
- **Lightweight** - Just observes tmux panes, no deep integration required
- **Open source** - Can be customized and self-hosted

### Comparison to Other Terminal AI Tools

| Feature | TmuxAI | Claude Code | Warp |
|---------|--------|-------------|------|
| Requires special shell | No | No | Yes |
| Works in SSH/nested | Yes | Yes | Limited |
| Visual screen awareness | Yes | No | No |
| Open source | Yes | No | No |
| Runs in tmux pane | Yes (designed for) | Yes (but not aware) | N/A |

---

## Warp Agent Mode - Terminal AI for Multi-Step Workflows

*Source: https://www.warp.dev/blog/agent-mode - Added: 2024-06-21*

Warp's Agent Mode embeds an LLM directly in the terminal to handle multi-step workflows using natural language. Executes commands, uses outputs to guide next steps, and self-corrects on errors.

### Key Features

- **Natural Language Input** - Type plain English instead of commands; auto-detection runs locally
- **Command Execution** - Runs commands with user approval and uses output to guide workflow
- **Self-Correcting** - When commands fail, agent adjusts and retries with correct flags/parameters
- **Zero Configuration Integration** - Works with any tool that has CLI, API, or public docs (GitHub, AWS, Kubernetes, etc.)
- **Internal CLI Learning** - Ask agent to read `--help` and it can immediately use internal tools

### Use Cases

- **DevOps** - "Help me upgrade an AWS database" - walks through step-by-step
- **Debugging** - Attach error output, type "fix it" - agent diagnoses and resolves
- **Cross-Tool Workflows** - Integrates with gh, aws, gcp, kubectl, datadog, curl, and any CLI

### Privacy & Security

- Natural language detection happens locally (classifier runs on device)
- User must explicitly approve each command before execution
- Opt-in context sharing - you control exactly what info is sent
- OpenAI backend (no training on data)
- Enterprise: Zero Data Retention and BYOK options available

### Pricing

- **Free** - 40 AI requests/month
- **Pro/Team/Enterprise** - Higher request limits

### Why It's Interesting

- Agent-in-terminal approach vs agent-as-IDE (Cursor, Zed) or agent-as-CLI (Claude Code)
- Self-correcting behavior reduces friction vs copy-paste-debug cycles
- Universal CLI integration without explicit setup for each tool
- Replaced Warp's original AI chat panel with more capable agent mode

### Comparison to Other Terminal AI Tools

| Feature | Warp Agent | Claude Code | TmuxAI | Amazon Q CLI |
|---------|------------|-------------|--------|--------------|
| Execution Model | Embedded in terminal | Standalone CLI | tmux observer | Standalone CLI |
| Self-Correcting | Yes | Yes | No | Limited |
| Multi-Step | Yes | Yes | No | Yes |
| Context from Output | Automatic (with approval) | Via conversation | Via screen | Via conversation |
| Works in SSH | Limited | Yes | Yes | Yes |
| Open Source | No | No | Yes | No |

---

## Devon - Early Open-Source Pair Programmer

*Source: https://github.com/entropy-research/Devon - Added: 2024-05-20*

One of the earlier open-source AI pair programming tools from entropy-research. Historically notable for beating AutoCodeRover on SWE-Bench Lite in May 2024.

### Key Features

- **Multi-File Editing** - Edit across multiple files in a project
- **Codebase Exploration** - Navigate and understand existing code
- **Config/Test Writing** - Generate configuration files and tests
- **Bug Fixing** - Diagnose and fix issues
- **Architecture Exploration** - Understand project structure

### Installation

```bash
# Via script
curl -sSL https://raw.githubusercontent.com/entropy-research/Devon/main/install.sh | bash

# Or via pipx + npm
pipx install devon_agent
npm install -g devon-tui
```

### Usage

```bash
# Navigate to project directory
cd /path/to/project

# Set API key (Anthropic or OpenAI)
export ANTHROPIC_API_KEY=sk-xxx
# OR
export OPENAI_API_KEY=sk-xxx

# Run
devon

# Debug mode
devon --debug
```

### Limitations (as of May 2024)

- Minimal support for non-Python languages
- Sometimes requires explicit file specification for changes
- Early-stage project with active development

### Historical Context

- **March 2024** - Initial non-interactive agent v0.0.1
- **April 2024** - Began interactive agent development, added repo-level code search
- **May 2024** - Beat AutoCodeRover on SWE-Bench Lite, released interactive agent v0.1.0

### Why It Was Interesting (2024)

- One of the first credible open-source alternatives to closed AI coding assistants
- SWE-Bench performance provided a benchmark comparison point
- Community-driven development model
- Apache 2.0 license enabled customization and self-hosting

### Status Note

This entry reflects the state as of May 2024. The AI coding agent space has evolved significantly since then with tools like Claude Code, Cursor agents, and Zed agents becoming more mature.

---

## Devin AI - First Commercial Autonomous Coding Agent (Historical)

*Source: https://devinai.ai/ - Added: 2024-05-11*

Devin AI, developed by Cognition AI, was announced in March 2024 as "the first fully autonomous AI software engineer." It sparked massive interest and a wave of open-source alternatives.

### What It Claimed

- **Autonomous Task Execution** - End-to-end software development from requirements to deployment
- **SWE-Bench Performance** - 13.86% unassisted issue resolution (state-of-the-art at announcement)
- **Integrated Environment** - Own shell, code editor, and browser in a sandboxed compute environment
- **Multi-Step Planning** - Breaks down high-level instructions into executable steps

### What Made It Novel

- First commercial offering to promise "fully autonomous" software engineering
- Chat interface for non-technical users to initiate projects
- Agent-as-worker model (runs in background, reports progress)
- Claimed ability to learn new technologies, train AI models, and contribute to production repos

### Reality Check (2024-2025)

The initial hype met reality:
- "Fully autonomous" proved less useful than "collaborative with human oversight"
- Demo videos were cherry-picked best-case scenarios
- Real-world usage showed significant failure rates on complex tasks
- Competitors (Claude Code, Cursor, Copilot agents) offered better human-in-the-loop experiences
- Sparked important debate about agent autonomy vs. controllability

### Historical Significance

Devin's announcement catalyzed the AI coding agent space:
1. Triggered wave of open-source alternatives (Devika, Devon, OpenHands)
2. Pushed incumbents (GitHub, Cursor) to accelerate agent features
3. Established "SWE-Bench" as the standard coding agent benchmark
4. Demonstrated that autonomous agents need better UX, not just better models

### Current Status

Still available at https://devin.ai/ but the market has moved toward hybrid approaches where AI assists rather than replaces developers.

---

## Devika - Early Open-Source Devin Alternative (Historical)

*Source: https://github.com/stitionai/devika - Added: 2024-05-11*

Open-source agentic AI software engineer that aimed to be a competitive alternative to Cognition AI's Devin. Now superseded by its successor project "Opcode."

### What It Was

- **Multi-Model Support** - Claude 3, GPT-4, Gemini, Mistral, Groq, local LLMs via Ollama
- **Planning & Reasoning** - Break down high-level instructions into steps
- **Web Browsing** - Research and gather information autonomously
- **Code Generation** - Write code in multiple languages
- **Project Management** - Organize work into discrete projects

### Tech Stack

- Python backend with Flask
- Node.js/Bun frontend
- Playwright for browser automation
- Supports multiple search engines (Bing, Google)

### Historical Significance

- **19.5k stars** - One of the most popular early Devin alternatives
- Released March 2024, shortly after Devin announcement sparked "open-source Devin" race
- Demonstrated community appetite for autonomous coding agents
- Set patterns that later tools (OpenHands, etc.) refined

### Why It Faded

- Never left "experimental stage" - many features remained unimplemented
- Devin hype cooled as people realized autonomous coding agents need more constraints
- Better alternatives emerged (OpenHands, Claude Code with agentic features)
- Team pivoted to commercial "Opcode" successor

### Lessons Learned

The early Devin-alternative projects (Devika, Devon, OpenDevin→OpenHands) showed that:
1. Planning + execution loop architecture is viable
2. Multi-model flexibility matters for cost/performance trade-offs
3. "Fully autonomous" is less useful than "collaborative with human oversight"
4. The winners combined autonomy with good UX (Claude Code, Cursor agents)

---

## E2B Code Interpreter SDK

*Source: https://github.com/e2b-dev/code-interpreter - Added: 2026-01-19*

An SDK for running AI-generated Python and JavaScript code with shared context across executions. Built on E2B's secure sandboxed micro VMs.

### Key Features

| Feature | Description |
|---------|-------------|
| **Shared Context** | Variables, definitions persist across code execution runs (like Jupyter Notebooks) |
| **Secure Sandboxes** | Runs in E2B Sandbox - isolated micro VMs for untrusted AI-generated code |
| **Streaming Output** | Stream charts, stdout, stderr in real-time |
| **Python & JS SDKs** | Both `pip install e2b-code-interpreter` and `npm install @e2b/code-interpreter` |
| **Serverless Ready** | Works on serverless and edge functions |
| **100% Open Source** | Including the infrastructure |

### Why Shared Context Matters

LLMs (especially GPT-3.5/4) expect Jupyter Notebook-style execution where each code block can reference previous ones. Classical sandboxes run code independently, causing AI-generated code to fail when it references variables from prior blocks.

E2B solves this by running a Jupyter server inside the sandbox, implementing the Jupyter Kernel messaging protocol.

### Quick Start

**Python:**
```python
from e2b_code_interpreter import CodeInterpreter

with CodeInterpreter() as sandbox:
    sandbox.notebook.exec_cell("x = 1")
    result = sandbox.notebook.exec_cell("x+=1; x")
    print(result.text)  # outputs 2
```

**JavaScript:**
```javascript
import { CodeInterpreter } from '@e2b/code-interpreter'

const sandbox = await CodeInterpreter.create()
await sandbox.notebook.execCell('x = 1')
const result = await sandbox.notebook.execCell('x+=1; x')
console.log(result.text)  // outputs 2
await sandbox.close()
```

### Charts and Visual Output

```python
code = """
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)
y = np.sin(x)

plt.plot(x, y)
plt.show()
"""

with CodeInterpreter() as sandbox:
    sandbox.notebook.exec_cell("!pip install matplotlib")
    result = sandbox.notebook.exec_cell(code)
    image = result.results[0].png  # Base64 encoded image
```

### Streaming Callbacks

```python
sandbox.notebook.exec_cell(
    code,
    on_stdout=print,
    on_stderr=print,
    on_result=lambda r: print(r.text)
)
```

### When to Use E2B Code Interpreter

**Good fit:**
- Building AI agents that need to run generated code safely
- Code that requires persistent state across multiple runs
- Applications requiring streaming visual output (charts, plots)
- Any LLM + code workflow that mimics Jupyter behavior

**Trade-offs:**
- Requires E2B API key and cloud (no local sandbox)
- Adds latency vs. local runs
- Cost considerations for high-volume usage

### Customization

Can customize the sandbox environment by following E2B's custom template guide to preinstall packages or configure the environment.

### Comparison

| Approach | Shared Context | Security | Local/Cloud |
|----------|----------------|----------|-------------|
| E2B Code Interpreter | Yes (Jupyter-style) | Sandboxed VM | Cloud |
| Local eval/run | No isolation | None | Local |
| Docker containers | Configurable | Good | Both |
| AWS Lambda | No (stateless) | Good | Cloud |

### Links

- GitHub: https://github.com/e2b-dev/code-interpreter
- E2B Platform: https://e2b.dev/
- Preinstalled packages: See requirements.txt in repo

---

## Skyvern - AI-Powered Browser Automation

*Source: https://www.skyvern.com/ | GitHub: https://github.com/Skyvern-AI/skyvern - Added: 2026-01-19*

An API-first browser automation platform that uses computer vision and AI to interact with websites without traditional selectors or page object models.

### Key Concept

Skyvern takes a fundamentally different approach than Playwright/Puppeteer: instead of writing code with CSS selectors, you give it natural language instructions and it uses computer vision to understand the page layout and complete tasks.

**Example:**
```
Traditional: page.click('#submit-button')
Skyvern: "Fill out the form and submit it"
```

### Core Features

**1. Computer Vision-Based Automation**
- No selectors needed - understands page content visually
- Adapts to layout changes automatically
- Works across different websites without rewriting automation

**2. Natural Language Control**
- Execute complex workflows with simple commands
- No coding required for basic automations
- Can handle multi-step processes with single instruction

**3. Built-in Intelligence**
- CAPTCHA solving capabilities
- Two-factor authentication (2FA/TOTP) support
- Authentication with user accounts
- Multi-language support for international sites

**4. Enterprise Features**
- Proxy network support (country/state/zip-code level targeting)
- Data extraction in CSV or JSON formats
- API-first design for cloud execution
- Horizontal scaling - run hundreds of workflows simultaneously

**5. Explainable AI**
- Provides justifications for every action
- Clear summaries of workflow execution
- Helps debug when automations fail

### Use Cases

**Government & Procurement**
- Automate tedious government form filling
- Streamline procurement pipelines across vendor portals
- Handle repetitive compliance documentation

**Data Extraction**
- Scrape data from sites that change frequently
- Extract structured data without maintaining selectors
- Handle dynamic content and infinite scroll

**E2E Testing**
- Test flows without brittle selectors
- Verify user journeys with natural language
- Cross-browser visual regression testing

### Architecture

```
┌──────────────────┐     API     ┌─────────────────────┐
│  Your Code       │ ─────────► │  Skyvern Cloud      │
│                  │             │  ┌───────────────┐  │
│  POST /workflow  │             │  │ Computer      │  │
│  {               │             │  │ Vision Engine │  │
│    "task": "...", │             │  └───────────────┘  │
│    "url": "..."  │             │  ┌───────────────┐  │
│  }               │             │  │ Browser Pool  │  │
└──────────────────┘             │  └───────────────┘  │
                                 │  ┌───────────────┐  │
                                 │  │ CAPTCHA/2FA   │  │
                                 │  │ Solver        │  │
                                 │  └───────────────┘  │
                                 └─────────────────────┘
```

### vs Traditional Browser Automation

| Feature | Skyvern | Playwright/Puppeteer |
|---------|---------|---------------------|
| **Selector Management** | None - uses CV | Manual CSS/XPath selectors |
| **Layout Changes** | Adapts automatically | Breaks when page changes |
| **Multi-site Support** | Generalizes across sites | One script per site |
| **CAPTCHA Handling** | Built-in solver | Requires external services |
| **Natural Language** | Native support | Requires custom LLM layer |
| **Deployment** | Cloud-based API | Self-hosted |
| **Scaling** | Horizontal (API) | Requires orchestration |
| **Cost** | Usage-based pricing | Open source (infra costs) |

### vs AI Browser Tools

| Tool | Approach | Best For |
|------|----------|----------|
| **Skyvern** | API service, CV-based | Production automation, scraping at scale |
| **Playwright MCP** | 17 individual tools | Claude Code integration, development |
| **Playwriter** | Single tool, Chrome ext | Development, keeping existing sessions |
| **Nova Act IDE** | IDE extension | Building automation agents in VS Code |

### When to Use Skyvern

**Good fit:**
- Automating workflows across multiple vendor sites
- Sites that change layout frequently
- Need to solve CAPTCHAs/2FA programmatically
- Want to avoid maintenance of selector-based scripts
- Need to scale to hundreds of concurrent workflows

**Not ideal for:**
- Simple one-off scraping tasks
- Sites with stable, well-documented APIs
- When you need full control of every browser action
- Local-only workflows (it's cloud-based)

### Considerations

**Pros:**
- Zero selector maintenance
- Handles modern web complexity (SPAs, dynamic content)
- Built-in CAPTCHA/2FA handling
- Natural language is easier for non-developers
- Scales horizontally out of the box

**Cons:**
- Proprietary service (not open source core)
- Less deterministic than selector-based automation
- Usage-based pricing vs free OSS alternatives
- Less control over exact browser behavior
- Requires internet connectivity (cloud-based)

### Company

Developed by Ikonomos Inc. (launched March 2024). Positioned as "AI that automates browser workflows" targeting enterprise automation use cases.

### Links

- Website: https://www.skyvern.com/
- GitHub: https://github.com/Skyvern-AI/skyvern
- Request Demo: Available on website

---

## Glide - AI Coding Assistant for Complex Tasks

*Source: https://glide.agenticlabs.com/ - Added: 2026-01-19*

AI assistant that helps tackle harder software engineering problems. Connects to repositories and provides codebase-aware assistance.

### Key Features

- **Repository Connection** - Grant access to specific repos for project-aware assistance
- **Code Search** - Search through your codebase intelligently
- **Task Description** - Describe what you're trying to accomplish in natural language
- **Code Generation & Editing** - Generate and modify code with project context
- **Issue Triage** - Help diagnose and prioritize problems
- **Step-by-Step Planning** - Break down complex tasks into actionable plans
- **Code Change Proposals** - Suggest specific code modifications
- **Pull Request Creation** - Coming soon

### Privacy Model

- Access granted only when you explicitly select a repository
- Requires login to access private repos
- Tailors generation to your specific project

### Comparison

| Feature | Glide | Claude Code | Cursor | GitHub Copilot |
|---------|-------|-------------|--------|----------------|
| Repo Connection | Yes | Local files | Local files | GitHub |
| Task Planning | Yes | Yes | Limited | No |
| Code Search | Yes | Yes | Yes | Limited |
| PR Creation | Coming | Manual | No | No |
| Privacy Control | Per-repo | Local only | Local only | Varies |

### Why It's Interesting

- Focus on "harder" engineering problems suggests more sophisticated reasoning vs autocomplete
- Step-by-step planning feature indicates multi-step task decomposition
- Per-repository access model balances utility with privacy
- Coming PR feature would close the loop on autonomous coding

### Developed By

Agentic Labs (https://agenticlabs.com)
