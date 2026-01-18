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

## Related

- See `coding-agent-tools.md` for UI wrappers and execution environments
- See `CLAUDE.md` patterns in main project for launchd/service integration
