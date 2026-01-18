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

## Related

- See `coding-agent-tools.md` for UI wrappers and execution environments
- See `CLAUDE.md` patterns in main project for launchd/service integration
