---
type: link
source: notion
url: https://github.com/wedow/ticket
notion_type: Software Repo
tags: ['Running']
created: 2026-01-06T04:10:00.000Z
---

# GitHub - wedow/ticket: Fast, powerful, git-native ticket tracking in a single bash script. Dependency graphs, priority levels, zero setup.

## Overview (from Notion)
- Streamlined Task Management: The ticket tool offers a simple, git-native way to track tasks, which can help you manage both family commitments and software projects efficiently.
- Dependency Tracking: The ability to manage dependencies between tasks might resonate with juggling responsibilities at home and work, ensuring you focus on what truly matters.
- Minimal Setup: The zero-setup nature of the tool means you can quickly implement it without getting bogged down in configuration, freeing up time for your family.
- Markdown Files: Utilizing markdown for tickets allows for easy readability and collaboration, which aligns with modern development practices.
- Sustainability: The focus on using lightweight, portable scripts reflects a growing trend in software development towards sustainability and efficiency.
- AI Integration: The potential to integrate with AI agents enhances productivity, offering a glimpse into the future of work-life balance with smart tools.
- Community and Open Source: Engaging with open-source tools fosters a sense of community, which can be valuable in both personal and professional networks.
- Alternate View: Consider the balance between technology use and family time; while tools like this can enhance productivity, ensure they don't detract from quality family interactions.

## AI Summary (from Notion)
A git-native ticket tracking system called tk allows for efficient management of issues with features like dependency graphs and priority levels. It is a portable bash script that requires only coreutils, and tickets are stored as markdown files for easy access. Installation instructions are provided for various platforms, and it includes commands for creating, updating, and querying tickets, along with a migration tool for users transitioning from another system called Beads.

## Content (from Notion)

# ticket

The git-backed issue tracker for AI agents. tk is inspired by the Joe Armstrong post Minimal Viable Program with additional quality of life features for managing and querying against complex issue dependency graphs.

tk was written as a full replacement for beads. It shares many similar commands but without the need for keeping a SQLite file in sync or a rogue background daemon mangling your changes. It ships with a migrate-beads command to make this a smooth transition.

Tickets are markdown files with YAML frontmatter in .tickets/. This allows AI agents to easily search them for relevant content without dumping ten thousand character JSONL lines into their context window.

Using ticket IDs as file names also allows IDEs to quickly navigate to the ticket for you. For example, you might run git log in your terminal and see something like:

```plain text
nw-5c46: add SSE connection management

```

VS Code allows you to Ctrl+Click or Cmd+Click the ID and jump directly to the file to read the details.

## Install

Homebrew (macOS/Linux):

```plain text
brew tap wedow/tools
brew install ticket
```

Arch Linux (AUR):

```plain text
yay -S ticket  # or paru, etc.
```

From source (auto-updates on git pull):

```plain text
git clone https://github.com/wedow/ticket.git
cd ticket && ln -s "$PWD/ticket" ~/.local/bin/tk
```

Or just copy ticket to somewhere in your PATH.

## Requirements

tk is a portable bash script requiring only coreutils, so it works out of the box on any POSIX system with bash installed. The query command requires jq. Uses rg (ripgrep) if available, falls back to grep.

## Agent Setup

Add this line to your CLAUDE.md or AGENTS.md:

```plain text
This project uses a CLI ticket system for task management. Run `tk help` when you need to use it.

```

Claude Opus picks it up naturally from there. Other models may need additional guidance.

## Usage

```plain text
tk - minimal ticket system with dependency tracking

Usage: tk <command> [args]

Commands:
  create [title] [options] Create ticket, prints ID
    -d, --description      Description text
    --design               Design notes
    --acceptance           Acceptance criteria
    -t, --type             Type (bug|feature|task|epic|chore) [default: task]
    -p, --priority         Priority 0-4, 0=highest [default: 2]
    -a, --assignee         Assignee [default: git user.name]
    --external-ref         External reference (e.g., gh-123, JIRA-456)
    --parent               Parent ticket ID
  start <id>               Set status to in_progress
  close <id>               Set status to closed
  reopen <id>              Set status to open
  status <id> <status>     Update status (open|in_progress|closed)
  dep <id> <dep-id>        Add dependency (id depends on dep-id)
  dep tree [--full] <id>   Show dependency tree (--full disables dedup)
  undep <id> <dep-id>      Remove dependency
  link <id> <id> [id...]   Link tickets together (symmetric)
  unlink <id> <target-id>  Remove link between tickets
  ls [--status=X]          List tickets
  ready                    List open/in-progress tickets with deps resolved
  blocked                  List open/in-progress tickets with unresolved deps
  closed [--limit=N]       List recently closed tickets (default 20, by mtime)
  show <id>                Display ticket
  edit <id>                Open ticket in $EDITOR
  query [jq-filter]        Output tickets as JSON, optionally filtered
  migrate-beads            Import tickets from .beads/issues.jsonl

Tickets stored as markdown files in .tickets/
Supports partial ID matching (e.g., 'tk show 5c4' matches 'nw-5c46')
```

## Migrating from Beads

```plain text
tk migrate-beads

# review new files if you like
git status

# check state matches expectations
tk ready
tk blocked

# compare against
bd ready
bd blocked

# all good, let's go
git rm -rf .beads
git add .tickets
git commit -am "ditch beads"
```

## License

MIT


