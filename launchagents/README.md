# LaunchAgents

macOS launchd plist files for jpt background services.

## Installation

```bash
# Copy to LaunchAgents directory
cp ~/jpt/launchagents/com.jpt.*.plist ~/Library/LaunchAgents/

# Load all services
for plist in ~/Library/LaunchAgents/com.jpt.*.plist; do
  launchctl load "$plist"
done
```

## Uninstall

```bash
# Unload all services
for plist in ~/Library/LaunchAgents/com.jpt.*.plist; do
  launchctl unload "$plist"
done

# Optionally remove the plist files
rm ~/Library/LaunchAgents/com.jpt.*.plist
```

## Prerequisites

Before loading services, ensure:

1. **jpt repo cloned** to `~/jpt`
2. **Homebrew installed** with Python 3: `/opt/homebrew/bin/python3`
3. **Notion credentials** in `~/.config/notion_sync.json`
4. **Claude CLI** (happy) installed at `~/Library/pnpm/happy`

## Services

| Service | Interval | Purpose |
|---------|----------|---------|
| meeting-processor | 120s | Process Meetily transcripts |
| notion-agent | 60s daemon | Execute AI-delegated tasks |
| inbox-fetcher | 120s | Fetch new inbox items |
| inbox-processor | 120s | Process inbox with Claude |
| digest-daily | Daily 6PM | Generate daily digest |
| digest-weekly | Sunday 10AM | Generate weekly digest |
| digest-monthly | 1st of month 9AM | Generate monthly digest |
| knowledge-curator | Daily 2AM | Organize knowledge files |
| knowledge-reviewer | Sunday 3AM | Review staleness |
| people-curator | Sunday 4AM | Curate people profiles |

## Logs

Each service logs to its respective directory:
- `~/jpt/meetings/.processor.log`
- `~/jpt/inbox/.fetcher.log`
- `~/jpt/inbox/.processor.log`
- `~/jpt/lib/.agent.log`
- `~/jpt/lib/.curator.log`

## Management

```bash
# Check status
launchctl list | grep jpt

# View logs
tail -f ~/jpt/lib/.agent.log

# Reload a specific service
launchctl unload ~/Library/LaunchAgents/com.jpt.notion-agent.plist
launchctl load ~/Library/LaunchAgents/com.jpt.notion-agent.plist
```
