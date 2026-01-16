---
name: granola-sync
description: |
  Manage Granola meeting transcript extraction and sync. Use when:
  - User asks about meeting transcripts, notes, or summaries
  - User wants to check sync status or logs
  - User needs to re-extract meetings or troubleshoot sync
  - User mentions "granola", "meeting notes", or "meeting transcripts"
  Provides access to extracted meetings in ~/jpt/meetings/ and controls the launchd sync service.
---

# Granola Sync

Extracts meeting transcripts and AI-generated summaries from Granola's local cache to markdown files.

## File Locations

- **Summaries**: `~/jpt/meetings/summaries/` (small ~1-2KB, read first)
- **Transcripts**: `~/jpt/meetings/transcripts/` (large ~30-50KB, read for detail)
- **People profiles**: `~/jpt/people/` (auto-generated from meetings)
- **Extraction script**: `~/jpt/meetings/extract_granola.py`
- **Post-processing prompt**: `~/jpt/meetings/post_meeting_prompt.md`
- **Sync log**: `~/jpt/meetings/granola-sync.log`
- **launchd plist**: `~/Library/LaunchAgents/com.jesse.granola-sync.plist`
- **Granola cache**: `~/Library/Application Support/Granola/cache-v3.json`

## Output Files

Each meeting produces up to two files in separate directories:
- `summaries/YYYY-MM-DD_Meeting_Title_summary.md` - AI-generated summary with action items (~1-2KB)
- `transcripts/YYYY-MM-DD_Meeting_Title.md` - Full transcript with metadata and notes (~30-50KB)

**For agents**: Read summaries first for quick context. Only access transcripts when deeper detail is needed.

## Common Tasks

### Check sync status
```bash
launchctl list | grep granola-sync
tail -20 ~/jpt/meetings/granola-sync.log
```

### Manual extraction
```bash
# Incremental (last 30 hours, skip existing)
python3 ~/jpt/meetings/extract_granola.py

# Full re-extraction
python3 ~/jpt/meetings/extract_granola.py --full

# Specific time window
python3 ~/jpt/meetings/extract_granola.py --hours 48
```

### Service management
```bash
# Stop
launchctl unload ~/Library/LaunchAgents/com.jesse.granola-sync.plist

# Start
launchctl load ~/Library/LaunchAgents/com.jesse.granola-sync.plist
```

### List available meetings
```bash
python3 ~/jpt/meetings/extract_granola.py --list

# List extracted summaries
ls ~/jpt/meetings/summaries/

# List extracted transcripts
ls ~/jpt/meetings/transcripts/
```

## Script Options

| Flag | Description |
|------|-------------|
| `--hours N` | Extract meetings from last N hours (default: 30) |
| `--full` | Extract ALL meetings, overwrite existing |
| `--force` | Overwrite existing files |
| `--list` | List available meetings without extracting |
| `--id ID` | Extract specific meeting by document ID |
| `--quiet` | Minimal output (for automation) |
| `--no-process` | Skip post-meeting processing (people/tasks) |

## Post-Meeting Processing

When a NEW summary is extracted (first time seen), the script automatically runs Claude to:
1. **Update people profiles** in `~/jpt/people/` - creates/updates profiles for each attendee
2. **Extract action items** to `~/jpt/TASKS.md` - adds clear commitments to the inbox

The prompt is in `~/jpt/meetings/post_meeting_prompt.md` - edit it to customize the behavior.

Use `--no-process` to skip this step (useful for bulk imports or re-extraction).

## Automation

The sync runs automatically via launchd:
- **On file change**: Triggers when Granola's cache updates (after meetings)
- **Daily at 6 AM**: Backup run in case file watch misses something
- **Throttled**: Won't run more than once per 60 seconds

## Troubleshooting

**No new meetings extracted**: Check if meetings are within the 30-hour window. Use `--hours 48` or `--full`.

**Service not running**: Check `launchctl list | grep granola-sync`. Reload with the service management commands above.

**Missing summaries**: Granola only caches summaries for meetings you've opened in the app. Open the meeting in Granola first.
