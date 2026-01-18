---
type: link
source: notion
url: https://github.com/ChrisWiles/claude-code-showcase
notion_type: Software Repo
tags: ['Running']
created: 2026-01-07T09:58:00.000Z
---

# GitHub - ChrisWiles/claude-code-showcase: Comprehensive Claude Code project configuration example with hooks, skills, agents, commands, and GitHub Actions workflows

## Overview (from Notion)
- Leverage AI tools like Claude Code to enhance coding efficiency, allowing more time for family and personal interests.
- Automate mundane tasks in software development, freeing up bandwidth for strategic thinking and creative pursuits.
- Understand the potential of integrating AI into project management for smoother workflows, especially in a busy city like New York.
- Explore the balance between technology and personal life; technology should enhance, not replace, meaningful interactions with family.
- Consider the implications of AI in job markets while fostering a growth mindset in your children about future skills.
- Reflect on the importance of maintaining a human touch in leadership, especially in tech-driven environments.
- Embrace continuous learning; the tech landscape evolves rapidly, and staying updated can inspire innovation in your ventures.
- Engage with local tech communities in NYC to expand networks, share knowledge, and gain fresh perspectives.

## AI Summary (from Notion)
The showcase highlights the capabilities of Claude Code for software development, emphasizing reusable skills and specialized agents for tasks like code review and automation. Key features include automated quality gates, intelligent skill suggestions, and integration with ticket systems like JIRA. It outlines best practices for project configuration, including the use of hooks for automation and the importance of maintaining a structured directory for skills and commands. The setup involves creating specific files and configurations to enhance code quality and streamline workflows.

## Content (from Notion)

# Claude Code Project Configuration Showcase

> 

Once you've got Claude Code set up, you can point it at your codebase, have it learn your conventions, pull in best practices, and refine everything until it's basically operating like a super-powered teammate. The real unlock is building a solid set of reusable "skills" plus a few "agents" for the stuff you do all the time.

### What This Looks Like in Practice

Custom UI Library? We have a skill that explains exactly how to use it. Same for how we write tests, how we structure GraphQL, and basically how we want everything done in our repo. So when Claude generates code, it already matches our patterns and standards out of the box.

Automated Quality Gates? We use hooks to auto-format code, run tests when test files change, type-check TypeScript, and even block edits on the main branch. Claude Code also created a bunch of ESLint automation, including custom rules and lint checks that catch issues before they hit review.

Deep Code Review? We have a code review agent that Claude runs after changes are made. It follows a detailed checklist covering TypeScript strict mode, error handling, loading states, mutation patterns, and more. When a PR goes up, we have a GitHub Action that does a full PR review automatically.

Scheduled Maintenance? We've got GitHub workflow agents that run on a schedule:

- Monthly docs sync - Reads commits from the last month and makes sure docs are still aligned
- Weekly code quality - Reviews random directories and auto-fixes issues
- Biweekly dependency audit - Safe dependency updates with test verification
Intelligent Skill Suggestions? We built a skill evaluation system that analyzes every prompt and automatically suggests which skills Claude should activate based on keywords, file paths, and intent patterns.

A ton of maintenance and quality work is just... automated. It runs ridiculously smoothly.

JIRA/Linear Integration? We connect Claude Code to our ticket system via MCP servers. Now Claude can read the ticket, understand the requirements, implement the feature, update the ticket status, and even create new tickets if it finds bugs along the way. The /ticket command handles the entire workflow—from reading acceptance criteria to linking the PR back to the ticket.

We even use Claude Code for ticket triage. It reads the ticket, digs into the codebase, and leaves a comment with what it thinks should be done. So when an engineer picks it up, they're basically starting halfway through already.

There is so much low-hanging fruit here that it honestly blows my mind people aren't all over it.

## Table of Contents

- Directory Structure
- Quick Start
- Configuration Reference 
- GitHub Actions Workflows
- Best Practices
- Examples in This Repository
## Directory Structure

```plain text
your-project/
├── CLAUDE.md                      # Project memory (alternative location)
├── .mcp.json                      # MCP server configuration (JIRA, GitHub, etc.)
├── .claude/
│   ├── settings.json              # Hooks, environment, permissions
│   ├── settings.local.json        # Personal overrides (gitignored)
│   ├── settings.md                # Human-readable hook documentation
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
│   │   ├── graphql-schema/
│   │   │   └── SKILL.md
│   │   └── ...
│   │
│   └── rules/                     # Modular instructions (optional)
│       ├── code-style.md
│       └── security.md
│
└── .github/
    └── workflows/
        ├── pr-claude-code-review.yml           # Auto PR review
        ├── scheduled-claude-code-docs-sync.yml # Monthly docs sync
        ├── scheduled-claude-code-quality.yml   # Weekly quality review
        └── scheduled-claude-code-dependency-audit.yml

```

## Quick Start

### 1. Create the .claude directory

```plain text
mkdir -p .claude/{agents,commands,hooks,skills}
```

### 2. Add a CLAUDE.md file

Create CLAUDE.md in your project root with your project's key information. See CLAUDE.md for a complete example.

```plain text
# Project Name

## Quick Facts
- **Stack**: React, TypeScript, Node.js
- **Test Command**: `npm run test`
- **Lint Command**: `npm run lint`

## Key Directories
- `src/components/` - React components
- `src/api/` - API layer
- `tests/` - Test files

## Code Style
- TypeScript strict mode
- Prefer interfaces over types
- No `any` - use `unknown`
```

### 3. Add settings.json with hooks

Create .claude/settings.json. See settings.json for a full example with auto-formatting, testing, and more.

```plain text
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

### 4. Add your first skill

Create .claude/skills/testing-patterns/SKILL.md. See testing-patterns/SKILL.md for a comprehensive example.

```plain text
---
name: testing-patterns
description: Jest testing patterns for this project. Use when writing tests, creating mocks, or following TDD workflow.
---

# Testing Patterns

## Test Structure
- Use `describe` blocks for grouping
- Use `it` for individual tests
- Follow AAA pattern: Arrange, Act, Assert

## Mocking
- Use factory functions: `getMockUser(overrides)`
- Mock external dependencies, not internal modules
```

> 

## Configuration Reference

### CLAUDE.md - Project Memory

CLAUDE.md is Claude's persistent memory that loads automatically at session start.

Locations (in order of precedence):

1. .claude/CLAUDE.md (project, in .claude folder)
1. ./CLAUDE.md (project root)
1. ~/.claude/CLAUDE.md (user-level, all projects)
What to include:

- Project stack and architecture overview
- Key commands (test, build, lint, deploy)
- Code style guidelines
- Important directories and their purposes
- Critical rules and constraints
📄 Example: CLAUDE.md

### settings.json - Hooks & Environment

The main configuration file for hooks, environment variables, and permissions.

Location: .claude/settings.json

📄 Example: settings.json | Human-readable docs

### Hook Events

### Hook Response Format

```plain text
{
  "block": true,           // Block the action (PreToolUse only)
  "message": "Reason",     // Message to show user
  "feedback": "Info",      // Non-blocking feedback
  "suppressOutput": true,  // Hide command output
  "continue": false        // Whether to continue
}
```

### Exit Codes

- 0 - Success
- 2 - Blocking error (PreToolUse only, blocks the tool)
- Other - Non-blocking error
### MCP Servers - External Integrations

MCP (Model Context Protocol) servers let Claude Code connect to external tools like JIRA, GitHub, Slack, databases, and more. This is how you enable workflows like "read a ticket, implement it, and update the ticket status."

Location: .mcp.json (project root, committed to git for team sharing)

📄 Example: .mcp.json

### How MCP Works

```plain text
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Claude Code   │────▶│   MCP Server    │────▶│  External API   │
│                 │◀────│  (local bridge) │◀────│  (JIRA, GitHub) │
└─────────────────┘     └─────────────────┘     └─────────────────┘

```

MCP servers run locally and provide Claude with tools to interact with external services. When you configure a JIRA MCP server, Claude gets tools like jira_get_issue, jira_update_issue, jira_create_issue, etc.

### .mcp.json Format

```plain text
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

Fields:

### Example: JIRA Integration

```plain text
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

What this enables:

- Read ticket details, acceptance criteria, and comments
- Update ticket status (To Do → In Progress → In Review)
- Add comments with progress updates
- Create new tickets for bugs found during development
- Link PRs to tickets
Example workflow with /ticket command:

```plain text
You: /ticket PROJ-123

Claude:
1. Fetching PROJ-123 from JIRA...
   "Add user profile avatar upload"

2. Reading acceptance criteria...
   - Upload button on profile page
   - Support JPG/PNG up to 5MB
   - Show loading state

3. Searching codebase for related files...
   Found: src/screens/Profile/ProfileScreen.tsx

4. Creating branch: cw/PROJ-123-avatar-upload

5. [Implements feature...]

6. Updating JIRA status to "In Review"
   Adding comment: "PR #456 ready for review"

7. Creating PR linked to PROJ-123...

```

### Common MCP Server Configurations

Issue Tracking:

```plain text
{
  "jira": {
    "type": "stdio",
    "command": "npx",
    "args": ["-y", "@anthropic/mcp-jira"],
    "env": {
      "JIRA_HOST": "${JIRA_HOST}",
      "JIRA_EMAIL": "${JIRA_EMAIL}",
      "JIRA_API_TOKEN": "${JIRA_API_TOKEN}"
    }
  },
  "linear": {
    "type": "stdio",
    "command": "npx",
    "args": ["-y", "@anthropic/mcp-linear"],
    "env": { "LINEAR_API_KEY": "${LINEAR_API_KEY}" }
  }
}
```

Code & DevOps:

```plain text
{
  "github": {
    "type": "stdio",
    "command": "npx",
    "args": ["-y", "@anthropic/mcp-github"],
    "env": { "GITHUB_TOKEN": "${GITHUB_TOKEN}" }
  },
  "sentry": {
    "type": "stdio",
    "command": "npx",
    "args": ["-y", "@anthropic/mcp-sentry"],
    "env": {
      "SENTRY_AUTH_TOKEN": "${SENTRY_AUTH_TOKEN}",
      "SENTRY_ORG": "${SENTRY_ORG}"
    }
  }
}
```

Communication:

```plain text
{
  "slack": {
    "type": "stdio",
    "command": "npx",
    "args": ["-y", "@anthropic/mcp-slack"],
    "env": {
      "SLACK_BOT_TOKEN": "${SLACK_BOT_TOKEN}",
      "SLACK_TEAM_ID": "${SLACK_TEAM_ID}"
    }
  }
}
```

Databases:

```plain text
{
  "postgres": {
    "type": "stdio",
    "command": "npx",
    "args": ["-y", "@anthropic/mcp-postgres"],
    "env": { "DATABASE_URL": "${DATABASE_URL}" }
  }
}
```

### Environment Variables

MCP configs support variable expansion:

- ${VAR} - Expands to environment variable (fails if not set)
- ${VAR:-default} - Uses default if VAR is not set
Set these in your shell profile or .env file (don't commit secrets!):

```plain text
export JIRA_HOST="https://yourcompany.atlassian.net"
export JIRA_EMAIL="you@company.com"
export JIRA_API_TOKEN="your-api-token"
```

### Settings for MCP

In settings.json, you can auto-approve MCP servers:

```plain text
{
  "enableAllProjectMcpServers": true
}
```

Or approve specific servers:

```plain text
{
  "enabledMcpjsonServers": ["jira", "github", "slack"]
}
```

### LSP Servers - Real-Time Code Intelligence

LSP (Language Server Protocol) gives Claude real-time understanding of your code—type information, errors, completions, and navigation. Instead of just reading text, Claude can "see" your code the way your IDE does.

Why this matters: When you edit TypeScript, Claude immediately knows if you introduced a type error. When you reference a function, Claude can jump to its definition. This dramatically improves code generation quality.

### Enabling LSP

LSP support is enabled through plugins in settings.json:

```plain text
{
  "enabledPlugins": {
    "typescript-lsp@claude-plugins-official": true,
    "pyright-lsp@claude-plugins-official": true
  }
}
```

### What Claude Gets from LSP

### Available LSP Plugins

### Custom LSP Configuration

For advanced setups, create .lsp.json:

```plain text
{
  "typescript": {
    "command": "typescript-language-server",
    "args": ["--stdio"],
    "extensionToLanguage": {
      ".ts": "typescript",
      ".tsx": "typescriptreact"
    },
    "initializationOptions": {
      "preferences": {
        "quotePreference": "single"
      }
    }
  }
}
```

### Troubleshooting

If LSP isn't working:

1.  
1.  
1.  
### Skill Evaluation Hooks

One of our most powerful automations is the skill evaluation system. It runs on every prompt submission and intelligently suggests which skills Claude should activate.

📄 Files: skill-eval.sh | skill-eval.js | skill-rules.json

### How It Works

When you submit a prompt, the UserPromptSubmit hook triggers our skill evaluation engine:

1.  
1.  
1.  
1.  
### Configuration

Skills are defined in skill-rules.json:

```plain text
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

### Adding to Your Project

1.  
1.  
1. 
### Skills - Domain Knowledge

Skills are markdown documents that teach Claude project-specific patterns and conventions.

Location: .claude/skills/{skill-name}/SKILL.md

📄 Examples:

- testing-patterns - TDD, factory functions, mocking
- systematic-debugging - Four-phase debugging methodology
- react-ui-patterns - Loading states, error handling
- graphql-schema - Queries, mutations, codegen
- core-components - Design system, tokens
- formik-patterns - Form handling, validation
### SKILL.md Frontmatter Fields

### SKILL.md Format

```plain text
---
name: skill-name
description: What this skill does and when to use it. Include keywords users would mention.
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

```plain text
// Bad example
```

## Integration

- Related skill: other-skill
```plain text

#### Best Practices for Skills

1. **Keep SKILL.md focused** - Under 500 lines; put detailed docs in separate referenced files
2. **Write trigger-rich descriptions** - Claude uses semantic matching on descriptions to decide when to apply skills
3. **Include examples** - Show both good and bad patterns with code
4. **Reference other skills** - Show how skills work together
5. **Use exact filename** - Must be `SKILL.md` (case-sensitive)

---

### Agents - Specialized Assistants

Agents are AI assistants with focused purposes and their own prompts.

**Location:** `.claude/agents/{agent-name}.md`

**📄 Examples:**
- [code-reviewer.md](.claude/agents/code-reviewer.md) - Comprehensive code review with checklist
- [github-workflow.md](.claude/agents/github-workflow.md) - Git commits, branches, PRs

#### Agent Format

```markdown
---
name: code-reviewer
description: Reviews code for quality, security, and conventions. Use after writing or modifying code.
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

### Agent Configuration Fields

### Commands - Slash Commands

Custom commands invoked with /command-name.

Location: .claude/commands/{command-name}.md

📄 Examples:

- onboard.md - Deep task exploration
- pr-review.md - PR review workflow
- pr-summary.md - Generate PR description
- code-quality.md - Quality checks
- docs-sync.md - Documentation alignment
### Command Format

```plain text
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

- $ARGUMENTS - All arguments as single string
- $1, $2, $3 - Individual positional arguments
### Inline Bash

```plain text
Current branch: !`git branch --show-current`
Recent commits: !`git log --oneline -5`
```

## GitHub Actions Workflows

Automate code review, quality checks, and maintenance with Claude Code.

📄 Examples:

- pr-claude-code-review.yml - Auto PR review
- scheduled-claude-code-docs-sync.yml - Monthly docs sync
- scheduled-claude-code-quality.yml - Weekly quality review
- scheduled-claude-code-dependency-audit.yml - Biweekly dependency updates
### PR Code Review

Automatically reviews PRs and responds to @claude mentions.

```plain text
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

### Setup Required

Add ANTHROPIC_API_KEY to your repository secrets:

- Settings → Secrets and variables → Actions → New repository secret
### Cost Estimate

Estimated monthly total: ~$10 - $50 (depending on PR volume)

## Best Practices

### 1. Start with CLAUDE.md

Your CLAUDE.md is the foundation. Include:

- Stack overview
- Key commands
- Critical rules
- Directory structure
### 2. Build Skills Incrementally

Don't try to document everything at once:

1. Start with your most common patterns
1. Add skills as pain points emerge
1. Keep each skill focused on one domain
### 3. Use Hooks for Automation

Let hooks handle repetitive tasks:

- Auto-format on save
- Run tests when test files change
- Regenerate types when schemas change
- Block edits on protected branches
### 4. Create Agents for Complex Workflows

Agents are great for:

- Code review (with your team's checklist)
- PR creation and management
- Debugging workflows
- Onboarding to tasks
### 5. Leverage GitHub Actions

Automate maintenance:

- PR reviews on every PR
- Weekly quality sweeps
- Monthly docs alignment
- Dependency updates
### 6. Version Control Your Config

Commit everything except:

- settings.local.json (personal preferences)
- CLAUDE.local.md (personal notes)
- User-specific credentials
## Examples in This Repository

## Learn More

- Claude Code Documentation
- Claude Code Action - GitHub Action
- Anthropic API
## License

MIT - Use this as a template for your own projects.


