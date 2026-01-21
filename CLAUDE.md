# Claude Code Project Guidelines

## LaunchAgents / launchd Services

When setting up launchd plist files for background services:

### PATH Environment
launchd does NOT inherit shell PATH. Always include an `EnvironmentVariables` section:

```xml
<key>EnvironmentVariables</key>
<dict>
    <key>PATH</key>
    <string>/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Users/jesse/Library/pnpm:/Users/jesse/.local/bin</string>
    <key>HOME</key>
    <string>/Users/jesse</string>
</dict>
```

### Binary Paths
Use full absolute paths for binaries in scripts called by launchd:
- Python: `/opt/homebrew/bin/python3`
- Node tools (claude, happy): `/Users/jesse/Library/pnpm/<tool>`
- ffmpeg: `/Users/jesse/.local/bin/ffmpeg`

### Common Commands
```bash
# Load service
launchctl load ~/Library/LaunchAgents/com.jpt.<service>.plist

# Unload service
launchctl unload ~/Library/LaunchAgents/com.jpt.<service>.plist

# Check status
launchctl list | grep jpt

# View logs (if configured)
tail -f ~/jpt/<service>/.processor.log
```

### Plist Template
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.jpt.SERVICE_NAME</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>/Users/jesse/jpt/PATH/TO/script.py</string>
    </array>
    <key>EnvironmentVariables</key>
    <dict>
        <key>PATH</key>
        <string>/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Users/jesse/Library/pnpm:/Users/jesse/.local/bin</string>
        <key>HOME</key>
        <string>/Users/jesse</string>
    </dict>
    <key>StartInterval</key>
    <integer>120</integer>
    <key>RunAtLoad</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/Users/jesse/jpt/PATH/.service.log</string>
    <key>StandardErrorPath</key>
    <string>/Users/jesse/jpt/PATH/.service.log</string>
    <key>WorkingDirectory</key>
    <string>/Users/jesse/jpt</string>
</dict>
</plist>
```

## Claude CLI Usage

When calling Claude from scripts (for Claude Max users):

```python
# Use happy (Claude Code wrapper) with full path
happy_bin = Path("/opt/homebrew/bin/happy")
result = subprocess.run(
    [str(happy_bin), "--yolo", "--print", prompt],
    capture_output=True,
    text=True,
    timeout=180
)
```

- `--yolo` = skip permission prompts (equivalent to `--dangerously-skip-permissions`)
- `--print` = non-interactive mode, output to stdout
- Always use full binary path for launchd compatibility

## Linear Integration

Linear is the primary task management system for dev work. Use `linear-cli` for all issue management.

### Configuration
- API Key: `LINEAR_API_KEY` environment variable (in `~/.zshenv`)
- Workspace: **jesolsen**
- Team: **JES** (Personal) - single team for all work
- CLI: `/Users/jesse/.local/bin/linear` (symlinked from `~/.deno/bin/linear`)

### Projects
| Project | Purpose |
|---------|---------|
| Personal | Personal tasks (not product work) |
| JPT | This repo - personal side project |
| Jumprope | Main day job |
| JumpBot | Day job side project |

### Claude Code Skill
The Linear skill is installed at `~/.claude/skills/linear/SKILL.md`. It provides:
- CLI commands for issue management
- Direct GraphQL API access via `linear auth token`

### Common Commands
```bash
# List issues assigned to you
linear issue list

# View current issue (detected from git branch)
linear issue view

# Start working on an issue (creates branch)
linear issue start JES-123

# Create a new issue
linear issue create

# Create PR with issue details
linear issue pr

# Add a comment
linear issue comment JES-123 "Status update"

# List teams
linear team list

# List projects
linear project list
```

### Git Integration
The CLI is git-aware:
- Detects issue IDs from branch names (e.g., `jes-123-feature-name`)
- `linear issue start` creates branches automatically
- `linear issue pr` populates PR with issue details

### Workflow
1. Create issue in Linear (web or CLI)
2. `linear issue start JES-XXX` - creates branch
3. Implement feature
4. `linear issue pr` - creates GitHub PR linked to issue
5. Issue auto-closes when PR merges (if configured)

## Notion Integration

Tasks are stored in Notion, not local files. Use the `lib/notion_tasks.py` module.

### Configuration
Credentials in `~/.config/notion_sync.json`:
```json
{
  "token": "ntn_xxx",
  "database_id": "xxx",
  "tasks_database_id": "xxx",
  "projects_database_id": "xxx"
}
```

The Notion integration is named "Meeting Sync" and must be connected to each database.

### Creating Tasks

```python
# From Python
import sys
sys.path.insert(0, '/Users/jesse/jpt/lib')
from notion_tasks import create_task

create_task(
    task_name="Do the thing",
    source="Meeting: Weekly Standup",  # or "Inbox: Article Name"
    notes="Brief context for the Notes property",  # truncated to 2000 chars
    body="Longer content goes in the page body...",  # supports full-length text
    due_date="2026-01-20",  # optional, ISO format
)
```

```bash
# From CLI
python3 ~/jpt/lib/notion_tasks.py create "Task name" "Source" "Notes" "Body content"
python3 ~/jpt/lib/notion_tasks.py list              # list tasks
python3 ~/jpt/lib/notion_tasks.py projects          # list projects
```

### Task Properties
- **Task name** (title) - required
- **Source** (text) - where it came from (e.g., "Meeting: 1-on-1 with Justin")
- **Notes** (text) - brief additional context (2000 char limit)
- **Page body** - longer content via `body` parameter (no practical limit)
- **Due** (date) - due date
- **Project** (relation) - link to Projects database
- **Status** (status) - "Not started", "In progress", "Done", "Delegated (AI)", "In Progress (AI)", "Done (AI)"

### Where Tasks Are Created
- `meetings/process_meeting.py` - creates tasks from meeting action items
- `inbox/inbox_processor.py` - Claude routes inbox items, can create tasks via CLI

### AI Agent Task Execution

The `lib/notion_agent.py` script polls for tasks to execute automatically.

**Triggers:**
1. Set task status to **"Delegated (AI)"** - agent picks it up within 60s
2. Add a comment containing **"@jb"** on any non-done task

**Workflow:**
1. Agent sets status to "In Progress (AI)"
2. Runs `happy --yolo --print` with task context
3. Posts output as comment on the task
4. Sets status to "Done (AI)" on success, or back to "Not started" on failure

**Safety:**
- 15-minute timeout per task
- Errors posted as comments with debug info
- Only one task processed at a time

**Commands:**
```bash
# Check status
python3 ~/jpt/lib/notion_agent.py status

# Run one poll cycle manually
python3 ~/jpt/lib/notion_agent.py once

# View logs
tail -f ~/jpt/lib/.agent.log
```

## Digest Processor

The `lib/digest_processor.py` generates daily, weekly, and monthly digests from inbox, meetings, knowledge, and tasks.

### Usage
```bash
# Manual run
python3 ~/jpt/lib/digest_processor.py daily    # 3-min read
python3 ~/jpt/lib/digest_processor.py weekly   # 10-min read
python3 ~/jpt/lib/digest_processor.py monthly  # 10-min read
python3 ~/jpt/lib/digest_processor.py status   # Show last run times
```

### Output
- Creates Notion task with digest as notes (truncated to 2000 chars)
- Saves full digest to `digests/YYYY-MM-DD_<period>_digest.md`
- State tracked in `lib/.digest_state.json` to prevent duplicate runs

### Schedule
- **Daily**: 2:00 AM every day
- **Weekly**: 3:00 AM Saturday
- **Monthly**: 4:00 AM on the 1st

## Knowledge Curator

Two agents maintain the `knowledge/` directory, creating PRs for human review.

### Nightly Curator (`lib/knowledge_curator.py`)

Runs at 2am daily. Organizes knowledge files:
- Creates subfolders when topic clusters reach 5+ files
- Merges related small files into cohesive topics (semi-aggressive)
- Moves files into appropriate subfolders
- Max nesting depth: 2 levels (e.g., `knowledge/ai/agents/`)

```bash
python3 ~/jpt/lib/knowledge_curator.py status    # Show current clusters
python3 ~/jpt/lib/knowledge_curator.py dry-run   # Preview changes
python3 ~/jpt/lib/knowledge_curator.py run       # Run and create PR
```

### Weekly Reviewer (`lib/knowledge_reviewer.py`)

Runs Sunday 3am. Reviews for staleness with context-aware rules:

| Content Type | Archive When |
|--------------|--------------|
| Philosophy/frameworks | Rarely - compounds over time |
| News/predictions | 3-6 months if topic inactive |
| Tool documentation | When tool abandoned |
| AWS/cloud features | When deprecated |
| Trends | When mainstream or dead |

```bash
python3 ~/jpt/lib/knowledge_reviewer.py status   # Staleness report
python3 ~/jpt/lib/knowledge_reviewer.py dry-run  # Preview archival
python3 ~/jpt/lib/knowledge_reviewer.py run      # Run and create PR
```

### State & Logs
- Shared log: `lib/.curator.log`
- Curator state: `lib/.curator_state.json`
- Reviewer state: `lib/.reviewer_state.json`

Both agents create git branches (`curator/YYYY-MM-DD-nightly` or `curator/YYYY-MM-DD-weekly`) and open PRs. They won't run if a previous PR is still open.

## People Curator

Weekly agent that curates the `people/` directory (`lib/people_curator.py`).

### What It Does
Runs Sunday 4am. Reviews all people profiles and:
1. **Generates weekly digest** - Summary of profile changes, posted to Notion as a task
2. **Archives inactive profiles** - Sparse profiles with no meetings in 6+ months
3. **Merges duplicates** - Same person with different filenames (transcription variations)
4. **Renames for consistency** - First-name-only files → full names when available
5. **Flags inconsistencies** - Conflicting info across profiles

Opens a **PR for review** with executive summary.

### Commands
```bash
python3 ~/jpt/lib/people_curator.py status    # Profile analysis
python3 ~/jpt/lib/people_curator.py dry-run   # Preview changes
python3 ~/jpt/lib/people_curator.py run       # Run and create PR
python3 ~/jpt/lib/people_curator.py digest    # Generate digest only
```

### State
- Log: `lib/.curator.log` (shared with knowledge curator)
- State: `lib/.people_curator_state.json`
- Branch pattern: `curator/YYYY-MM-DD-people`

## Active Services

| Service | Plist | Interval | Purpose |
|---------|-------|----------|---------|
| meeting-processor | `com.jpt.meeting-processor.plist` | 120s | Process Meetily transcripts |
| notion-agent | `com.jpt.notion-agent.plist` | 60s (daemon) | Execute AI-delegated tasks |
| digest-daily | `com.jpt.digest-daily.plist` | Daily 6PM | Generate daily digest |
| digest-weekly | `com.jpt.digest-weekly.plist` | Sunday 10AM | Generate weekly digest |
| digest-monthly | `com.jpt.digest-monthly.plist` | 1st of month 9AM | Generate monthly digest |
| knowledge-curator | `com.jpt.knowledge-curator.plist` | Daily 2AM | Organize knowledge, create PR |
| knowledge-reviewer | `com.jpt.knowledge-reviewer.plist` | Sunday 3AM | Review staleness, create PR |
| people-curator | `com.jpt.people-curator.plist` | Sunday 4AM | Curate people profiles, create PR |
