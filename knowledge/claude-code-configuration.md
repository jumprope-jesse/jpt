# Claude Code Configuration Patterns

Comprehensive patterns for configuring Claude Code with hooks, skills, agents, MCP servers, and GitHub Actions.

*Source: https://github.com/ChrisWiles/claude-code-showcase - Added: 2026-01-18*

## Directory Structure

```
your-project/
├── CLAUDE.md                      # Project memory (main instructions)
├── .mcp.json                      # MCP server configuration (JIRA, GitHub, etc.)
├── .claude/
│   ├── settings.json              # Hooks, environment, permissions
│   ├── settings.local.json        # Personal overrides (gitignored)
│   ├── .gitignore                 # Ignore local/personal files
│   │
│   ├── agents/                    # Custom AI agents
│   │   └── code-reviewer.md       # Proactive code review agent
│   │
│   ├── commands/                  # Slash commands (/command-name)
│   │   ├── onboard.md             # Deep task exploration
│   │   ├── pr-review.md           # PR review workflow
│   │   └── ...
│   │
│   ├── hooks/                     # Hook scripts
│   │   ├── skill-eval.sh          # Skill matching on prompt submit
│   │   ├── skill-eval.js          # Node.js skill matching engine
│   │   └── skill-rules.json       # Pattern matching configuration
│   │
│   ├── skills/                    # Domain knowledge documents
│   │   ├── README.md              # Skills overview
│   │   ├── testing-patterns/
│   │   │   └── SKILL.md
│   │   └── ...
│   │
│   └── rules/                     # Modular instructions (optional)
│       ├── code-style.md
│       └── security.md
│
└── .github/
    └── workflows/
        ├── pr-claude-code-review.yml
        ├── scheduled-claude-code-docs-sync.yml
        └── scheduled-claude-code-quality.yml
```

## Hooks

### Hook Events

| Event | Timing | Use Case |
|-------|--------|----------|
| PreToolUse | Before tool runs | Block edits on main, validate commands |
| PostToolUse | After tool runs | Auto-format, run tests |
| UserPromptSubmit | On prompt submit | Skill evaluation, doc checking |
| Stop | Session ends | Sound notification |
| Notification | Claude notifies | Alert sounds |

### Hook Response Format

```json
{
  "block": true,           // Block the action (PreToolUse only)
  "message": "Reason",     // Message to show user
  "feedback": "Info",      // Non-blocking feedback
  "suppressOutput": true,  // Hide command output
  "continue": false        // Whether to continue
}
```

### Exit Codes

- `0` - Success
- `2` - Blocking error (PreToolUse only, blocks the tool)
- Other - Non-blocking error

### Example: Block Edits on Main Branch

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "[ \"$(git branch --show-current)\" != \"main\" ] || { echo '{\"block\": true, \"message\": \"Cannot edit on main branch\"}' >&2; exit 2; }",
            "timeout": 5
          }
        ]
      }
    ]
  }
}
```

### Example: Sound Notifications

```json
{
  "hooks": {
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
}
```

### Example: Enforce uv run for pytest

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

## Skills

Skills are markdown documents that teach Claude project-specific patterns.

**Location:** `.claude/skills/{skill-name}/SKILL.md`

### SKILL.md Format

```markdown
---
name: skill-name
description: What this skill does and when to use it.
allowed-tools: Read, Grep, Glob
model: claude-sonnet-4-20250514
---

# Skill Title

## When to Use
- Trigger condition 1
- Trigger condition 2

## Core Patterns

### Pattern Name
```typescript
// Example code
```

## Anti-Patterns

### What NOT to Do
```typescript
// Bad example
```
```

### Skill Evaluation System

Pattern-match prompts to automatically suggest relevant skills:

**skill-rules.json:**
```json
{
  "testing-patterns": {
    "description": "Jest testing patterns and TDD workflow",
    "priority": 9,
    "triggers": {
      "keywords": ["test", "jest", "spec", "tdd", "mock"],
      "keywordPatterns": ["\\btest(?:s|ing)?\\b", "\\bspec\\b"],
      "pathPatterns": ["**/*.test.ts", "**/*.test.tsx"],
      "intentPatterns": [
        "(?:write|add|create|fix).*(?:test|spec)",
        "(?:test|spec).*(?:for|of|the)"
      ]
    },
    "excludePatterns": ["e2e", "maestro", "end-to-end"]
  }
}
```

## Agents

Custom AI assistants with focused purposes.

**Location:** `.claude/agents/{agent-name}.md`

### Agent Format

```markdown
---
name: code-reviewer
description: Reviews code for quality, security, and conventions.
model: opus
---

# Agent System Prompt

You are a senior code reviewer...

## Your Process
1. Run `git diff` to see changes
2. Apply review checklist
3. Provide feedback

## Checklist
- [ ] No TypeScript `any`
- [ ] Error handling present
- [ ] Tests included
```

## Commands (Slash Commands)

**Location:** `.claude/commands/{command-name}.md`

### Command Format

```markdown
---
description: Brief description shown in command list
allowed-tools: Bash(git:*), Read, Grep
---

# Command Instructions

Your task is to: $ARGUMENTS

## Steps
1. Do this first
2. Then do this
```

### Variables

- `$ARGUMENTS` - All arguments as single string
- `$1`, `$2`, `$3` - Individual positional arguments

### Inline Bash

```markdown
Current branch: !`git branch --show-current`
Recent commits: !`git log --oneline -5`
```

## MCP Server Configuration

**Location:** `.mcp.json` (project root)

### Basic Format

```json
{
  "mcpServers": {
    "server-name": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-name"],
      "env": {
        "API_KEY": "${API_KEY}"
      }
    }
  }
}
```

### JIRA Integration

```json
{
  "mcpServers": {
    "jira": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-jira"],
      "env": {
        "JIRA_HOST": "${JIRA_HOST}",
        "JIRA_EMAIL": "${JIRA_EMAIL}",
        "JIRA_API_TOKEN": "${JIRA_API_TOKEN}"
      }
    }
  }
}
```

**Workflow with /ticket command:**
1. Fetches ticket details and acceptance criteria
2. Searches codebase for related files
3. Creates feature branch
4. Implements feature
5. Updates JIRA status to "In Review"
6. Creates PR linked to ticket

### Claude Code as Sub-Agent (claude-code-mcp)

*Source: https://github.com/steipete/claude-code-mcp - Added: 2026-01-18*

MCP server that enables running Claude Code in one-shot mode with permissions bypassed. Allows LLMs in other tools (Cursor, Windsurf, Claude Desktop) to spawn Claude Code as a sub-agent for complex coding tasks.

**Use case:** When Cursor/Windsurf struggle with complex multi-step edits, delegate to Claude Code which is better and faster at file operations.

**Configuration:**
```json
{
  "mcpServers": {
    "claude-code-mcp": {
      "command": "npx",
      "args": ["-y", "@steipete/claude-code-mcp@latest"]
    }
  }
}
```

**With custom CLI binary:**
```json
{
  "mcpServers": {
    "claude-code-mcp": {
      "command": "npx",
      "args": ["-y", "@steipete/claude-code-mcp@latest"],
      "env": {
        "CLAUDE_CLI_NAME": "claude-custom"
      }
    }
  }
}
```

**Prerequisites:**
1. Node.js v20+
2. Claude CLI installed (`npm install -g @anthropic-ai/claude-code`)
3. One-time permissions acceptance: `claude --dangerously-skip-permissions` (follow prompts)

**Client-specific paths:**
- **Cursor:** `~/.cursor/mcp.json`
- **Windsurf:** `~/.codeium/windsurf/mcp_config.json`

**Benefits:**
- Claude Code handles file editing better than most IDE agents
- Multiple commands queued instead of executed one-by-one (saves context)
- Cost effective with Anthropic Max subscription
- Wider system access - unsticks agents that believe they can't do something

**Environment variables:**
- `CLAUDE_CLI_PATH` - Absolute path to Claude CLI executable
- `MCP_CLAUDE_DEBUG` - Set to `true` for verbose logging

**Key insight:** "Agents in agents" - let your primary agent delegate complex file operations, git workflows, and multi-step tasks to Claude Code as a specialized sub-agent.

### Claude Code on Amazon Bedrock

*Source: https://builder.aws.com/content/2tXkZKrZzlrlu0KfH8gST5Dkppq/claude-code-on-amazon-bedrock-quick-setup-guide - Added: 2026-01-18*

Quick setup for running Claude Code with Amazon Bedrock as the backend instead of the Anthropic API.

**Configuration:**
```bash
# Set Bedrock as the provider
export CLAUDE_CODE_USE_BEDROCK=1

# Or use the CLI flag
claude --bedrock
```

**Prerequisites:**
- AWS account with Bedrock access
- Claude models enabled in your Bedrock region
- AWS credentials configured (via `~/.aws/credentials`, IAM role, or environment variables)

**Required IAM permissions:**
- `bedrock:InvokeModel`
- `bedrock:InvokeModelWithResponseStream`

**Benefits over direct API:**
- Use existing AWS billing and cost controls
- Leverage AWS VPC endpoints for private connectivity
- Apply AWS IAM policies for access control
- May have different rate limits than direct API

### AWS MCP Servers Suite (Official Open Source)

*Source: https://aws.amazon.com/blogs/machine-learning/introducing-aws-mcp-servers-for-code-assistants-part-1/ - Added: 2026-01-18*

AWS released open-source MCP servers that bring AWS best practices directly into development workflows. Available on [GitHub](https://github.com/awslabs/mcp) and PyPI.

**Installation via uvx:**
```json
{
  "mcpServers": {
    "awslabs-core-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.core-mcp-server@latest"],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR",
        "MCP_SETTINGS_PATH": "path to your mcp server settings"
      }
    },
    "awslabs-bedrock-kb-retrieval-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.bedrock-kb-retrieval-mcp-server@latest"],
      "env": {
        "AWS_PROFILE": "your-aws-profile",
        "AWS_REGION": "us-east-1"
      }
    },
    "awslabs-cdk-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.cdk-mcp-server@latest"],
      "env": { "FASTMCP_LOG_LEVEL": "ERROR" }
    },
    "awslabs-cost-analysis-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.cost-analysis-mcp-server@latest"],
      "env": {
        "AWS_PROFILE": "your-aws-profile",
        "FASTMCP_LOG_LEVEL": "ERROR"
      }
    },
    "awslabs-nova-canvas-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.nova-canvas-mcp-server@latest"],
      "env": {
        "AWS_PROFILE": "your-aws-profile",
        "AWS_REGION": "us-east-1"
      }
    }
  }
}
```

**Available Servers:**

| Server | Purpose |
|--------|---------|
| **Core** | Foundation server with AI processing pipeline, federation to other MCP servers |
| **AWS CDK** | IaC knowledge, cdk-nag security, Powertools integration, GenAI constructs |
| **Bedrock KB Retrieval** | Query enterprise knowledge bases with natural language, filter by data source |
| **Nova Canvas** | Image generation via Amazon Nova Canvas (mockups, diagrams, UI concepts) |
| **Cost Analysis** | Generate cost reports, optimize architectural decisions |

**Key Benefits:**
- Enforce AWS best practices automatically (security controls, observability, resource configs)
- Skip hours of documentation research
- Access ready-to-use CDK constructs and Bedrock patterns
- Proactive cost optimization recommendations

### AWS Knowledge MCP Server

*Source: https://aws.amazon.com/about-aws/whats-new/2025/10/aws-knowledge-mcp-server-generally-available - Added: 2026-01-18*

Free, public MCP server providing AI agents access to authoritative AWS knowledge including documentation, blog posts, What's New announcements, and Well-Architected best practices.

**Key features:**
- Regional availability info for AWS APIs and CloudFormation resources
- No AWS account required
- Subject to rate limits
- Globally available

**Configuration:**
```json
{
  "mcpServers": {
    "aws-knowledge": {
      "type": "url",
      "url": "https://mcp.aws.amazon.com/aws-knowledge"
    }
  }
}
```

**Use cases:**
- Accurate reasoning about AWS services and regional availability
- Reduced manual context management for AWS projects
- Anchoring AI responses in trusted AWS best practices

Setup instructions: https://docs.aws.amazon.com/mcp/latest/userguide/getting-started.html

### Settings for MCP

```json
{
  "enableAllProjectMcpServers": true
}
```

Or approve specific servers:
```json
{
  "enabledMcpjsonServers": ["jira", "github", "slack"]
}
```

## GitHub Actions Workflows

### PR Code Review

```yaml
name: PR - Claude Code Review
on:
  pull_request:
    types: [opened, synchronize, reopened]
  issue_comment:
    types: [created]

jobs:
  review:
    if: |
      github.event_name == 'pull_request' ||
      (github.event_name == 'issue_comment' &&
       github.event.issue.pull_request &&
       contains(github.event.comment.body, '@claude'))
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - uses: anthropics/claude-code-action@beta
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
          model: claude-opus-4-5-20251101
          prompt: |
            Review this PR using .claude/agents/code-reviewer.md standards.
            Run `git diff origin/main...HEAD` to see changes.
```

### Scheduled Workflows

| Workflow | Schedule | Purpose |
|----------|----------|---------|
| docs-sync | Monthly | Reads commits, aligns docs |
| code-quality | Weekly | Reviews random directories, auto-fixes |
| dependency-audit | Biweekly | Safe updates with test verification |

**Estimated monthly cost:** ~$10-50 depending on PR volume

## Real-World Automation Examples

From the showcase:

1. **Custom UI Library** - Skill explaining exactly how to use it
2. **Automated Quality Gates** - Auto-format, run tests, type-check, block main edits
3. **Deep Code Review** - Agent with detailed checklist (TypeScript strict, error handling, loading states)
4. **Scheduled Maintenance** - Monthly docs sync, weekly quality review, biweekly dependency audit
5. **Intelligent Skill Suggestions** - Analyze prompts and auto-suggest relevant skills
6. **JIRA/Linear Integration** - Read ticket → implement → update status → create PR

## Key Insight

> "Once you've got Claude Code set up, you can point it at your codebase, have it learn your conventions, pull in best practices, and refine everything until it's basically operating like a super-powered teammate."

The real unlock: building reusable skills + agents for repetitive workflows.

---

## Writing Effective CLAUDE.md Files

*Source: https://www.humanlayer.dev/blog/writing-a-good-claude-md - Added: 2026-01-18*

Best practices for writing CLAUDE.md (or AGENTS.md for other harnesses like OpenCode, Zed, Cursor, Codex).

### Principle: LLMs Are (Mostly) Stateless

LLMs are stateless functions with frozen weights. The only thing the model knows about your codebase is the tokens you put into it. CLAUDE.md is the only file that goes into every single conversation.

**Implications:**
1. Coding agents know nothing about your codebase at session start
2. The agent must be told anything important each session
3. CLAUDE.md is the preferred way of doing this

### CLAUDE.md Onboards Claude to Your Codebase

Cover three areas:

- **WHAT**: Tech stack, project structure, monorepo maps (what apps exist, what packages are shared, where to look for things)
- **WHY**: Purpose of the project, function of different parts
- **HOW**: How to work on the project (use bun instead of node?), how to verify changes, run tests, typechecks, compilation

**Warning:** Don't stuff every possible command into CLAUDE.md—you'll get suboptimal results.

### Why Claude Often Ignores CLAUDE.md

Claude Code injects this system reminder with your CLAUDE.md:

```
<system-reminder>
IMPORTANT: this context may or may not be relevant to your tasks.
You should not respond to this context unless it is highly relevant to your task.
</system-reminder>
```

Claude will ignore CLAUDE.md contents if it decides they're not relevant. The more non-universally-applicable instructions you include, the more likely Claude ignores your important instructions.

### Less (Instructions) Is More

Research findings on instruction following:

1. Frontier thinking LLMs follow ~150-200 instructions with reasonable consistency
2. Smaller models degrade exponentially as instruction count increases; larger models degrade linearly
3. LLMs bias toward instructions at the peripheries (beginning and end)
4. As instruction count increases, instruction-following decreases **uniformly** (not just newer instructions)

**Key insight:** Claude Code's system prompt already contains ~50 instructions. That's nearly 1/3 of what the agent can reliably follow before you add anything.

**Rule:** Include only instructions that are universally applicable to your tasks.

### Keep It Concise and Universally Applicable

- Avoid task-specific instructions (e.g., how to structure a new database schema)
- General consensus: <300 lines is best, shorter is even better
- HumanLayer's root CLAUDE.md is less than 60 lines

### Progressive Disclosure

Instead of putting all instructions in CLAUDE.md, create separate markdown files with self-descriptive names:

```
agent_docs/
  |- building_the_project.md
  |- running_tests.md
  |- code_conventions.md
  |- service_architecture.md
  |- database_schema.md
  |- service_communication_patterns.md
```

In CLAUDE.md, list these files with brief descriptions. Instruct Claude to decide which are relevant and read them before starting.

**Prefer pointers to copies.** Don't include code snippets—they become outdated. Use `file:line` references to point Claude to authoritative context.

This is similar to how Claude Skills work, though skills focus more on tool use than instructions.

### Claude Is NOT a Linter

**Never send an LLM to do a linter's job.** LLMs are expensive and slow compared to deterministic tools.

Problems with code style in CLAUDE.md:
- Adds instructions and mostly-irrelevant code snippets
- Degrades instruction-following and eats context window
- LLMs are in-context learners—they'll follow existing patterns without being told

**Better approaches:**
- Use a Claude Code Stop hook that runs your formatter/linter and presents errors
- Use linters that auto-fix (like Biome) and tune rules for safe auto-fix coverage
- Create a Slash Command that includes guidelines and points at git diff/status
- Handle implementation and formatting separately for better results on both

### Don't Auto-Generate CLAUDE.md

Don't use `/init` or auto-generation tools for CLAUDE.md.

The leverage hierarchy:
- Bad line of code → bad line of code
- Bad line in implementation plan → many bad lines of code
- Bad line in research → bad plan → many bad lines of code
- **Bad line in CLAUDE.md → affects every phase and every artifact**

CLAUDE.md is the highest leverage point of the harness. Spend time carefully crafting every line.

### Summary

1. **CLAUDE.md is for onboarding Claude** - Define your project's WHY, WHAT, and HOW
2. **Less (instructions) is more** - Include as few instructions as reasonably possible
3. **Keep it concise and universally applicable** - Avoid task-specific instructions
4. **Use Progressive Disclosure** - Tell Claude how to find information, not everything it could possibly need
5. **Claude is not a linter** - Use hooks and Slash Commands for formatting/linting
6. **Carefully craft CLAUDE.md** - Avoid auto-generation; this is your highest leverage point

---

## Power User Patterns & Philosophy

*Source: https://blog.sshh.io/p/how-i-use-every-claude-code-feature (Shrivu Shankar) - Added: 2026-01-18*

Insights from someone whose team consumes billions of tokens/month for codegen.

### CLAUDE.md Philosophy

**Treat it as guardrails, not a manual:**

1. **Start with Guardrails** - Document based on what Claude gets wrong, not everything possible
2. **Don't @File Docs** - Bloats context. Instead, *pitch* why/when to read: "For complex usage or FooBarError, see path/to/docs.md"
3. **Never Say Just "Never"** - Avoid "Never use -foo flag" without alternative. Provide what to do instead.
4. **Use as Forcing Function** - Complex CLI commands? Write a bash wrapper instead of paragraphs explaining them. Short CLAUDE.md = incentive to simplify tooling.

**Size guidelines:** ~13KB for large monorepo, could grow to 25KB. Only document tools used by 30%+ of engineers—others go in product-specific markdown files.

### Context Management Workflows

Run `/context` mid-session to understand your 200k token usage. Fresh monorepo session: ~20k tokens baseline, 180k remaining.

**Three workflows:**

1. **`/compact` (Avoid)** - Auto-compaction is opaque and error-prone
2. **`/clear` + `/catchup` (Simple Restart)** - Clear state, custom command reads all changed files in git branch
3. **"Document & Clear" (Complex Restart)** - Have Claude dump plan/progress to `.md`, clear, new session reads the `.md` and continues

### Subagent Philosophy

**Problem with custom subagents:**
1. **Gatekeep Context** - A "PythonTests" subagent hides testing context from main agent
2. **Force Human Workflows** - You dictate delegation instead of letting agent solve it

**Preferred approach: "Master-Clone"**
- Put key context in CLAUDE.md
- Let main agent use built-in `Task(...)` to spawn clones of itself
- Agent manages its own orchestration dynamically
- Avoids "Lead-Specialist" brittleness

### Hook Strategy

**Use "Block-at-Submit" hooks, not "Block-at-Write":**

Blocking mid-plan confuses the agent. Let it finish, then check final result at commit time.

**Example pattern:**
- PreToolUse hook wraps `Bash(git commit)`
- Checks for `/tmp/agent-pre-commit-pass` file
- Test script only creates this file if all tests pass
- If missing, hook blocks commit → forces "test-and-fix" loop

**Hint hooks:** Non-blocking feedback for suboptimal patterns.

### Session History & Learning

```bash
# Resume old sessions
claude --resume
claude --continue
```

Session history stored in `~/.claude/projects/`. Run meta-analysis on logs for common exceptions, permission requests, and error patterns to improve CLAUDE.md.

### Slash Commands Philosophy

Keep them minimal and simple:
- `/catchup` - Read all changed files in current git branch
- `/pr` - Clean up code, stage, prepare PR

**Anti-pattern:** Long list of complex custom commands. The whole point of agents is typing whatever you want—don't force engineers to learn magic commands.

### Skills vs MCP

Skills formalize the "scripting" model (better than rigid API-like MCP).

**New role for MCP:** Secure gateway providing few high-level tools:
- `download_raw_data(filters…)`
- `take_sensitive_gated_action(args…)`
- `execute_code_in_environment_with_state(code…)`

MCP manages auth/networking/security, then gets out of the way.

**Only stateful tools need MCP** (like Playwright). Stateless tools (Jira, AWS, GitHub) → simple CLIs.

### Claude Code SDK Use Cases

1. **Massive Parallel Scripting** - Bash scripts calling `claude -p "change X to Y"` in parallel across files
2. **Internal Chat Tools** - Wrap complex processes for non-technical users (installers that self-fix, "v0-at-home" for designers)
3. **Rapid Agent Prototyping** - General-purpose framework for any agentic task before committing to full deployment

### GitHub Actions: Operationalization

The GHA is how you turn Claude Code from personal tool to auditable engineering system.

**Benefits:**
- Full control over container/environment
- Stronger sandboxing and audit controls than managed alternatives
- Supports hooks and MCP
- Full agent logs enable ops review for common mistakes

**Flywheel pattern:**
```bash
$ query-claude-gha-logs --since 5d | claude -p "see what the claudes were stuck on and fix it, PR"
```

**Use cases:** PR-from-anywhere triggered by Slack/Jira/CloudWatch alerts.

### Settings.json Tips

- `HTTPS_PROXY/HTTP_PROXY` - Debug by inspecting raw traffic
- `MCP_TOOL_TIMEOUT/BASH_MAX_TIMEOUT_MS` - Bump for long-running commands
- `ANTHROPIC_API_KEY` - Enterprise keys enable usage-based pricing vs per-seat
- `permissions` - Self-audit allowed auto-run commands

### Key Philosophy

> "My goal is to 'shoot and forget'—delegate, set context, let it work. Judge the tool by the final PR, not how it gets there."

Don't over-index on output style or UI. Sycophancy like "you're absolutely right!" signals you're too in-the-loop.

## Example Skill: Playwright Browser Automation

*Source: https://github.com/lackeyjb/playwright-skill - Added: 2026-01-18*

A concrete example of a well-structured Claude Code skill for browser automation.

### What It Does

Claude autonomously writes and executes Playwright code for any browser automation task. Model-invoked (not a slash command) - Claude decides when to use it based on your request.

### Installation

```bash
# Via plugin system
/plugin marketplace add lackeyjb/playwright-skill
/plugin install playwright-skill@playwright-skill
cd ~/.claude/plugins/marketplaces/playwright-skill/skills/playwright-skill
npm run setup

# Or manual
cd ~/.claude/skills
git clone https://github.com/lackeyjb/playwright-skill.git
cd playwright-skill/skills/playwright-skill
npm run setup
```

### Structure (Good Example)

```
playwright-skill/
├── .claude-plugin/
│   ├── plugin.json          # Plugin metadata
│   └── marketplace.json     # Marketplace config
├── skills/
│   └── playwright-skill/
│       ├── SKILL.md         # What Claude reads (314 lines - concise)
│       ├── run.js           # Universal executor
│       ├── package.json
│       └── lib/helpers.js
├── API_REFERENCE.md         # Full reference (630 lines - loaded on demand)
└── README.md
```

### Key Design Patterns

1. **Progressive disclosure** - SKILL.md is concise (314 lines), full API reference loaded only when needed
2. **Universal executor** - `run.js` handles module resolution, avoiding common errors
3. **Visible by default** - `headless: false` so you see what's happening
4. **Smart cleanup** - Temp file management without race conditions

### Usage Examples

```
"Test the homepage"
"Check if the contact form works"
"Take screenshots of the dashboard in mobile and desktop"
"Fill out the registration form and submit it"
"Check for broken links"
```

### Defaults

- Headless: false (browser visible)
- Slow motion: 100ms
- Timeout: 30s
- Screenshots: saved to /tmp/

This skill demonstrates the "master-clone" philosophy mentioned in Power User Patterns - Claude writes custom code for each request rather than relying on pre-built scripts.

---

## Why Skills May Be a Bigger Deal Than MCP

*Source: https://simonwillison.net/2025/Oct/16/claude-skills/ (Simon Willison) - Added: 2026-01-18*

Strategic perspective on why skills represent a significant shift in AI capabilities.

### Token Efficiency

Skills use frontmatter YAML for discovery. At session start, Claude scans available skills but only reads the `name` and `description` from metadata—just a few dozen tokens per skill. Full contents only load when the user requests a relevant task.

### Skills vs MCP Limitations

**MCP issues that emerged over time:**
- GitHub's official MCP alone consumes tens of thousands of tokens
- Once you add multiple MCPs, little context space remains for actual work
- The "AI strategy checkbox" effect led to many implementations

**Skills advantage:**
- Everything MCP can do, a CLI tool can do
- LLMs know how to call `cli-tool --help` and figure it out later
- Skills don't even need a CLI—just a Markdown file describing how to do a task
- Scripts only added when needed for reliability/efficiency

### The Filesystem Dependency

Skills require the model to have:
- Access to a filesystem
- Tools to navigate it
- Ability to execute commands

This is the pattern of ChatGPT Code Interpreter (2023), later extended to local machines via Cursor, Claude Code, Codex CLI, and Gemini CLI.

### What This Enables: Data Journalism Agent Example

Imagine a folder of skills covering:
- Where to get US census data and how to understand its structure
- How to load data into SQLite/DuckDB
- How to publish data to S3 or Datasette Cloud
- How to find interesting stories in data (from experienced data reporter)
- How to build clean D3 visualizations

**Result:** A "data journalism agent" from Markdown files and a few Python scripts.

### Model Agnostic

Skills aren't locked to Claude. You can point Codex CLI or Gemini CLI at a skills folder and say "read pdf/SKILL.md then create a PDF"—it works despite no baked-in skills knowledge.

### The Safe Sandbox Challenge

Skills make a strong argument for safe coding environments for LLMs. But "safe" does a lot of work:
- Sandboxing against prompt injections
- Limiting damage from attacks
- Acceptable risk thresholds

This remains an open challenge.

### Key Insight

> "Claude Code is, with hindsight, poorly named. It's not purely a coding tool: it's a tool for general computer automation. Anything you can achieve by typing commands into a computer is something that can now be automated by Claude Code. It's best described as a general agent."

Skills make this general-purpose nature explicit.

---

## Happy Coder: Mobile Claude Code Client

*Source: https://happy.engineering/docs/features/ - Added: 2026-01-18*

Native mobile app for Claude Code with real-time synchronization, voice coding, and push notifications.

### Core Architecture

**Real-Time CLI Synchronization:**
- Bidirectional WebSocket communication between desktop CLI (`happy`) and mobile app
- Both devices can initiate conversations and send messages in the same shared session
- Terminal state serialization, command history, and context preservation
- Cross-device cursor position and selection state sync

**Multi-Session Management:**
- Multiple concurrent Claude Code sessions with independent state
- Each session maintains its own project context and conversation history
- Sessions can be paused, resumed, and switched seamlessly
- Background session state preservation

**Security (Zero-Trust Architecture):**
- End-to-end AES encryption using shared secrets (scan QR code to pair)
- Relay server handles only encrypted blobs - no access to plaintext
- Public key authentication with challenge-response protocol
- Open-source relay server available for self-hosting

**Offline-First Architecture:**
- Desktop CLI logs activity, encrypts, uploads to object storage
- Mobile app polls for encrypted updates and decrypts locally
- Bidirectional encrypted pub/sub messaging
- Session persistence independent of network connectivity

### Mobile Features

**Permission Prompts:**
- Real-time permission system for MCP tool calls and file edits
- Mobile displays operation details with Allow/Deny before execution
- Granular permission categories (file ops, API calls, system commands)
- Per-session permission memory with "Remember for this session"

**File Mentions & Slash Commands:**
- Full Claude Code file mention support
- All user-defined agents from `~/.claude/agents/` synced to mobile
- Command autocomplete with fuzzy search
- Agent metadata parsing (name, description, tools, model preferences)

**Push Notifications:**
- Session status updates, completion alerts, error notifications
- Deep linking to specific sessions and completion points
- Rich notification content with operation details

**Voice Agent:**
- Speech-to-text and text-to-speech via Eleven Labs
- Separate conversation context from Claude Code session
- Agentic assistant (Claude Sonnet 4) converts stream-of-consciousness planning into concrete Claude Code requests
- Hands-free brainstorming while multitasking

### Use Cases

- Start coding session on laptop, continue on phone during breaks
- Approve/deny permission prompts while away from desk
- Voice-driven planning and brainstorming hands-free
- Monitor long-running tasks via push notifications
- Work offline during commutes with sync when connected

---

## Claude Code Architecture: Why It Works So Well

*Source: https://minusx.ai/blog/decoding-claude-code/ (MinusX) - Added: 2026-01-18*

Analysis of Claude Code's internal design based on extensive use and network request logging. The key insight: keep things simple, and let the model do the heavy lifting.

### The Fundamental Philosophy

Claude Code has been crafted with a fundamental understanding of what the LLM is good at and what it's terrible at. Its prompts and tools cover for the model's weaknesses and help it shine where it excels. The control loop is extremely simple to follow and trivial to debug.

**Core principle:** Keep Things Simple, Dummy. LLMs are terrible enough to debug and evaluate. Any additional complexity (multi-agents, agent handoffs, complex RAG algorithms) only makes debugging 10x harder.

### Single-Threaded Architecture

Despite multi-agent systems being all the rage, Claude Code has just one main thread:
- Uses a flat list of messages
- Periodically summarizes git history or conversation
- Can spawn itself as a sub-agent (max one branch depth) without the ability to spawn more sub-agents
- Sub-agent results added to main message history as "tool response"

**Key insight:** The combination of max-1-branch and an explicit todo list gives the agent ability to break problems into sub-problems while keeping the eye on the final outcome.

> "I highly doubt your app needs a multi-agent system. With every layer of abstraction you make your system harder to debug, and more importantly you deviate from the general-model-improvement trajectory."

### Small Model Usage for Scaffolding

Over 50% of all important LLM calls are to claude-3-5-haiku (70-80% cheaper than Sonnet). Used for:
- Reading large files
- Parsing web pages
- Processing git history
- Summarizing long conversations
- Generating one-word processing labels (literally for every keystroke!)

### Prompt Design Patterns

**Scale:** System prompt is ~2800 tokens, with Tools taking 9400 tokens. User prompt includes claude.md (typically 1000-2000 tokens).

**XML Tag Patterns:**

```xml
<!-- Reminder tags for things the model forgets -->
<system-reminder>This is a reminder that your todo list is currently empty.
DO NOT mention this to the user explicitly because they are already aware.</system-reminder>

<!-- Good/bad examples for decision forks -->
<good-example>
pytest /foo/bar/tests
</good-example>
<bad-example>
cd /foo/bar && pytest tests
</bad-example>
```

**Markdown Headings in System Prompt:**
- Tone and style
- Proactiveness
- Following conventions
- Code style
- Task Management
- Tool use policy
- Doing Tasks
- Tools

### No RAG - LLM Search Instead

Claude Code searches your codebase like you would: complex ripgrep, jq, and find commands. Since the LLM understands code well, it uses sophisticated regex to find relevant code.

**Why RAG is rejected:**
- Introduces hidden failure modes (similarity function? reranker? chunking strategy?)
- With LLM Search, it just looks at 10 lines to understand structure, then more if needed
- Most importantly: this is RL-learnable (BigLabs are already working on it)
- The model does the heavy lifting, dramatically reducing moving parts

> "Having two complicated, intelligent systems wired this way is just ugly."

### Tool Design Philosophy

**The real trade-off:** How often you expect the agent to use a tool vs. accuracy in using it.

| Level | Examples | Purpose |
|-------|----------|---------|
| Low | Bash, Read, Write | Generic capabilities |
| Medium | Edit, Grep, Glob | Frequently used, worth dedicating a tool |
| High | WebFetch, getDiagnostics | Extremely deterministic, saves multi-step clicking |

Claude Code uses bash but still has separate Grep/Glob tools because they're used so frequently that dedicated tools improve reliability.

### Explicit Todo List (Model-Maintained)

**Why this works:**
- Keeps LLM on track (heavily prompted to refer to todo list)
- Gives model flexibility to course-correct mid-implementation
- Leverages interleaved thinking to reject or insert items on the fly

**Contrast with alternatives:**
- Multi-agent handoff + verification (PRD→implementer→QA) - too complex
- Separate model for todo generation - unnecessary abstraction

### Aesthetic Control

Explicit sections on tone, style, and proactiveness with instructions and examples. This is why Claude Code "feels" tasteful.

```
# Example tone/style instructions
- IMPORTANT: You should NOT answer with unnecessary preamble or postamble
  (such as explaining your code or summarizing your action), unless the user asks you to.
- Only use emojis if the user explicitly requests it.
- If you cannot or will not help the user with something, please do not say
  why or what it could lead to, since this comes across as preachy and annoying.
```

### Negative Steering (IMPORTANT/NEVER/ALWAYS)

Unfortunately no better way exists to steer models away from landmines:

```
- IMPORTANT: DO NOT ADD ***ANY*** COMMENTS unless asked
- VERY IMPORTANT: You MUST avoid using search commands like `find` and `grep`
- IMPORTANT: You must NEVER generate or guess URLs for the user
```

Models should get more steerable in future, but for now use this liberally.

### Write the Algorithm with Heuristics

**Critical practice:** Identify the most important task and write out the algorithm explicitly, ideally as a flowchart.

**Benefits:**
- Structures decision making
- Aids LLM in following instructions
- Avoids "big soup of Dos and Don'ts" that become mutually exclusive

Task Management, Doing Tasks, and Tool Usage Policy sections in Claude Code's system prompt walk through algorithms with heuristics and examples.

### Key Takeaways for Your Own Agents

1. **Keep control loops simple** - debuggability >>> complicated scaffolding
2. **Use smaller models liberally** for scaffolding tasks (70-80% cheaper)
3. **Write elaborate prompts** with heuristics, examples, and IMPORTANT reminders
4. **Design tools at multiple levels** - low-level for flexibility, high-level for common operations
5. **Skip RAG** - let the model search like a human would
6. **Maintain explicit todo lists** but let the model maintain them
7. **Control aesthetics explicitly** - tone and style matter for user experience
8. **Write algorithms, not just rules** - structure helps LLMs follow complex instructions

---

## Claudius: Native Mac App for Claude Code

*Source: https://www.josh.ing/claudius - Added: 2026-01-18*

Native Mac application providing an alternative interface for Claude Code with enhanced session management.

### Features

- **Multi-session interface** - Manage multiple concurrent AI chat windows
- **Version control integration** - Review changes, AI-powered commit messages without leaving the app
- **Light/dark themes** - Full theme customization
- **Prompt management** - Tools to save, reuse, and perfect instructions
- **Conversation history** - Full history at your fingertips

### Status

Currently a side project (developer's day job is at Sentry). Not yet stable, but being actively developed. Long-term goal is democratizing AI-powered building.

### Comparison to Happy Coder

| Feature | Claudius | Happy Coder |
|---------|----------|-------------|
| Platform | Mac desktop | Mobile (iOS) |
| Multi-session | Yes | Yes |
| Sync | Local | Real-time CLI sync |
| Voice | Not mentioned | Yes (Eleven Labs) |
| Notifications | Not mentioned | Push notifications |
| Use case | Desktop power user | Mobile/away from desk |

---

## Claudia: Desktop Companion for Claude Code

*Source: https://claudiacode.com/ - Added: 2026-01-18*

Desktop application for managing Claude Code projects with an interactive session interface.

### Features

- **Interactive session interface** - Navigate through all Claude Code projects
- **Streamlined workflow** - Project management focused on simplicity
- **Claude Code integration** - Seamless integration with existing projects

### Comparison to Other Clients

| Feature | Claudia | Claudius | Happy Coder |
|---------|---------|----------|-------------|
| Platform | Desktop | Mac desktop | Mobile (iOS) |
| Focus | Project navigation | Multi-session | Remote/mobile access |
| Sync | Local | Local | Real-time CLI sync |
| Use case | Project management | Power user | Mobile/away from desk |

---

## AI Coding Process & CLAUDE.md Rules

*Source: https://www.sabrina.dev/p/ultimate-ai-coding-guide-claude-code (Sabrina Ramonov) - Added: 2026-01-18*

A structured approach to using Claude Code for implementing features in complex production codebases.

### Reality Check (2025)

> "There is no AI tool that performs at a senior eng level. You still need to be hands-on involved, push back on AI plans, stop it from going down the wrong rabbit hole, question the code, and test extensively."

### Example CLAUDE.md Structure

Well-organized CLAUDE.md file with implementation rules, coding standards, testing requirements, and keyboard shortcuts.

**Section 0 - Purpose:** Rules ensure maintainability, safety, and developer velocity. MUST rules enforced by CI; SHOULD rules strongly recommended.

**Section 1 - Before Coding:**
- **BP-1 (MUST)** Ask clarifying questions
- **BP-2 (SHOULD)** Draft and confirm approach for complex work
- **BP-3 (SHOULD)** List pros/cons if multiple approaches exist

**Section 2 - While Coding:**
- **C-1 (MUST)** Follow TDD: stub → failing test → implement
- **C-2 (MUST)** Use existing domain vocabulary for function names
- **C-3 (SHOULD NOT)** Introduce classes when small functions suffice
- **C-4 (SHOULD)** Prefer simple, composable, testable functions
- **C-5 (MUST)** Use branded types for IDs: `type UserId = Brand<string, 'UserId'>`
- **C-6 (MUST)** Use `import type { … }` for type-only imports
- **C-7 (SHOULD NOT)** Add comments except for critical caveats
- **C-9 (SHOULD NOT)** Extract functions unless reused, enables testing, or dramatically improves readability

**Section 3 - Testing:**
- **T-1 (MUST)** Colocate simple unit tests in `*.spec.ts` in same directory
- **T-2 (MUST)** Add/extend integration tests for any API change
- **T-3 (MUST)** Separate pure-logic unit tests from DB-touching integration tests
- **T-4 (SHOULD)** Prefer integration tests over heavy mocking
- **T-6 (SHOULD)** Test entire structure in one assertion when possible

**Section 6 - Tooling Gates:**
- **G-1 (MUST)** `prettier --check` passes
- **G-2 (MUST)** `turbo typecheck lint` passes

### Function Quality Checklist

When evaluating a function:
1. Can you honestly follow what it's doing easily?
2. High cyclomatic complexity (many if-else nesting)?
3. Would common data structures (parsers, trees, stacks) make it clearer?
4. Any unused parameters?
5. Any unnecessary type casts that could move to arguments?
6. Easily testable without mocking core features?
7. Hidden untested dependencies that could be arguments instead?
8. Brainstorm 3 better function names - is current name the best?

**Refactor only when:**
- Function used in more than one place
- Refactored function enables unit testing
- Original is extremely hard to follow

### Test Quality Checklist

1. **SHOULD** parameterize inputs; never embed unexplained literals
2. **SHOULD NOT** add tests that can't fail for real defects
3. **SHOULD** ensure test description matches what expect verifies
4. **SHOULD** compare to pre-computed expectations, not function output
5. **SHOULD** follow same lint/type rules as prod code
6. **SHOULD** use `fast-check` for property-based testing when practical
7. Unit tests grouped under `describe(functionName, () => ...)`
8. Use `expect.any(...)` for variable values like IDs
9. Use strong assertions: `toEqual(1)` not `toBeGreaterThanOrEqual(1)`
10. Test edge cases, realistic input, unexpected input, boundaries
11. **SHOULD NOT** test conditions caught by type checker

### Keyboard Shortcuts Pattern

Define shortcuts for common workflows:

| Shortcut | Purpose |
|----------|---------|
| `qnew` | Load CLAUDE.md best practices at session start |
| `qplan` | Analyze codebase consistency before implementing |
| `qcode` | Implement plan, run tests, prettier, typecheck |
| `qcheck` | Review all major code changes against checklists |
| `qcheckf` | Review functions against best practices |
| `qcheckt` | Review tests against best practices |
| `qux` | Generate UX test scenarios for implemented feature |
| `qgit` | Stage, commit (Conventional Commits), push |

### AI Coding Workflow

1. `/clear` - Start fresh context
2. `qnew` - Load best practices
3. Discuss user story, simplify plan, remove unnecessary features
4. `qplan` - Verify consistency with codebase
5. `qcode` - Implement and verify
6. `qcheck`/`qcheckf`/`qcheckt` - Review code changes
7. Watch working tree for real-time edits, stop early if going wrong direction
8. `qux` - Generate UX test scenarios
9. `qgit` - Commit with Conventional Commits

### Caveats

- First draft code often needs improvement - rarely accept without review
- Code that "works" isn't always high-quality for production
- Without active oversight, technical debt accumulates quickly
- AI can drift off course while appearing confident
- Watch thought process in real-time, check working tree, stop early if needed

### Key Philosophy

> "If you don't watch closely, you will waste a lot of time and accidentally introduce breaking changes."

Active oversight means reading Claude's real-time thinking, checking edits in working tree, and stopping early when it goes down wrong rabbit holes.

---

## VSCode Extension

*Source: https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code - Added: 2026-01-18*

Official VSCode extension that integrates Claude Code directly into the IDE.

### Requirements

- VS Code 1.98.0 or higher
- Claude Code CLI must be installed separately (see [claude.ai/code](https://claude.ai/code))

### Features

| Feature | Description |
|---------|-------------|
| **Auto-installation** | When you launch Claude Code from VSCode's terminal, the extension auto-detects and installs |
| **Selection context** | Selected text in the editor is automatically added to Claude's context |
| **Diff viewing** | Code changes displayed in VSCode's diff viewer instead of terminal |
| **Keyboard shortcuts** | `Alt+Cmd+K` to push selected code into Claude's prompt |
| **Tab awareness** | Claude can see which files you have open in the editor |

### Configuration

Set the diff tool to `auto` in `/config` to enable IDE integration features:

```bash
# In Claude Code session
/config
# Set diff tool to "auto"
```

### Status

Early release - may contain bugs or incomplete features.

---

## Claude 4 System Prompts Analysis (Simon Willison)

*Source: https://arstechnica.com/ai/2025/05/hidden-ai-instructions-reveal-how-anthropic-controls-claude-4/ - Added: 2026-01-18*

Simon Willison's analysis of Anthropic's Claude 4 (Opus 4 and Sonnet 4) system prompts reveals how Anthropic controls model behavior through hidden instructions.

### What System Prompts Are

LLMs process input prompts and return likely continuations. System prompts are instructions fed to models before each conversation to establish behavior. They typically remain hidden from users and tell the model:
- Its identity
- Behavioral guidelines
- Specific rules to follow

Each message includes the full conversation history plus system prompt, maintaining context.

### Published vs Full Prompts

Anthropic publishes portions of system prompts in release notes, but these are incomplete. Full prompts (including tool instructions for web search, code generation, etc.) must be extracted through **prompt injection** - tricking models into revealing hidden instructions.

### Emotional Support Instructions

Both Claude Opus 4 and Sonnet 4 receive identical instructions:
> "care about people's wellbeing and avoid encouraging or facilitating self-destructive behaviors such as addiction, disordered or unhealthy approaches to eating or exercise"

### Anti-Sycophancy Instructions

A major finding is how Anthropic addresses the flattery problem (e.g., ChatGPT's 4o "buttered up" responses):

> "Claude never starts its response by saying a question or idea or observation was good, great, fascinating, profound, excellent, or any other positive adjective. It skips the flattery and responds directly."

**The sycophancy problem:** User feedback during training creates a loop where models learn enthusiasm leads to higher ratings, even when inappropriate.

### Formatting Guidelines

Extensive instructions on when Claude should NOT use bullet points or numbered lists:
> "Claude should not use bullet points or numbered lists for reports, documents, explanations, or unless the user explicitly asks for a list or ranking."

Multiple paragraphs dedicated to discouraging frequent list-making in casual conversation.

### Prompt Injection as Archaeology

Willison's observation (he coined "prompt injection" in 2022):
> "A system prompt can often be interpreted as a detailed list of all of the things the model used to do before it was told not to do them."

Warning signs in system prompts hint at past problems, similar to physical warning signs in the real world.

### Key Insight

System prompts are essentially a negative steering mechanism - documenting model behaviors that needed correction. Reading them reveals the history of what models got wrong.

---

## Running --dangerously-skip-permissions Safely

*Source: https://news.ycombinator.com/item?id=46690907 (HN discussion) - Added: 2026-01-20*

The `--dangerously-skip-permissions` flag removes approval friction but introduces real risk. Multiple users report Claude deleting home directories with `rm -rf` or wiping shared dev databases.

### Sandboxing Approaches

**Virtual Machine Isolation (Recommended for High Risk)**
- Vagrant VMs with codebase synced via shared folders
- Each project gets its own VM
- Minimal blast radius from mistakes or prompt injection
- Claude cannot access other system files

**Docker Containers**
- Bind-mount only the working directory
- Lighter weight than VMs
- **Caveat:** Docker-in-Docker requires privileged mode, defeating sandboxing purpose

**Docker Native Sandbox (Newest)**
```bash
docker sandbox run claude
```
Built-in protection with integrated container isolation.

**Unprivileged User Account**
- Create dedicated user account for Claude operations
- Simpler setup but limits system package installation
- Good for projects that don't need root access

### Critical Safety Practices

**Credential Isolation**
- Never store SSH keys in sandboxed environment
- Keep database credentials out of Claude's reach
- API tokens should use minimal scopes
- Use environment variables injected at runtime, not stored files

**Version Control as Safety Net**
- Always work in git repositories
- Commit frequently before major operations
- Note: Claude occasionally deletes `.git` directories - back up important repos externally

**Database Protection**
- Use read-only database connections where possible
- Point Claude at staging/dev databases, never production
- Consider database snapshots before running destructive operations

### Real-World Incidents Reported

- `rm -rf ~` (home directory deletion)
- Wiping shared development databases
- Deleting `.git` directories
- Unintended production deployments

### Recommendation Matrix

| Risk Level | Environment | Use Case |
|------------|-------------|----------|
| Low | Unprivileged user | Personal projects, learning |
| Medium | Docker container | Most development work |
| High | Vagrant VM | Working with credentials, prod-adjacent |
| Maximum | Air-gapped VM | Security-sensitive operations |

**Key insight:** The friction of `--dangerously-skip-permissions` approval fatigue is real, but so is the blast radius. Choose your isolation level based on what's at stake.

---

## Related

- See `coding-agent-tools.md` for UI wrappers and execution environments
- See `CLAUDE.md` patterns in main project for launchd/service integration
- See `agentic-coding-practices.md` for team-level practices and workflows
