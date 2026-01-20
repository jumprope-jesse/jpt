# Inbox

Clearinghouse for all incoming captures. Items here get processed automatically and routed to the appropriate destination.

## Automated Notion Sync

Links saved to the **My Links** Notion database are automatically fetched and processed.

### How It Works

1. **Share a link** to the My Links Notion database (any status except "Synced and Done")
2. **Fetcher polls** every 60 seconds for unsynced items (`com.jpt.inbox-fetcher.plist`)
   - Processes newest items first (new links take priority)
   - Fetches up to 5 items per run (gradually catches up backlog)
3. **Markdown file created** in `inbox/` with Notion page content
4. **Status updated** to "Synced and Done" in Notion immediately (prevents duplicates)
5. **Processor runs** every 120 seconds (`com.jpt.inbox-processor.plist`)
6. **Content routed** to `knowledge/`, `people/`, `personal/`, `work/`, or **Notion Tasks**
7. **Original archived** to `.archive/`

### Sync Tracking

Items are marked as "Synced and Done" in Notion **immediately after saving** to the inbox (before processing). This prevents duplicates even if the inbox processor takes a while to run.

### Manual Fetch

```bash
# Fetch oldest unsynced item
python fetch_one_link.py

# Pick from list
python fetch_one_link.py --pick

# Fetch newest unsynced
python fetch_one_link.py --newest

# Include already-synced items
python fetch_one_link.py --include-synced --pick
```

### Service Management

```bash
# Check service status
launchctl list | grep jpt

# View fetcher logs
tail -f ~/jpt/inbox/.fetcher.log

# View processor logs
tail -f ~/jpt/inbox/.processor.log

# Reload services
launchctl unload ~/Library/LaunchAgents/com.jpt.inbox-fetcher.plist
launchctl load ~/Library/LaunchAgents/com.jpt.inbox-fetcher.plist
```

## Manual Capture

Create a markdown file with any name. The processor will pick it up within 2 minutes.

### Suggested Format

```markdown
---
type: link | thought | task | note
source: manual | notion | email | teams
url: (if applicable)
created: 2024-01-18T10:30:00
---

# Title or summary

Content, notes, why this matters...
```

The frontmatter is optional - the processor will figure out what to do with plain text too.

## What Happens to Items

The processor (Claude) reads each item and routes it appropriately:

- **Tasks** → Created in **Notion Tasks** database (via `lib/notion_tasks.py`)
- **Knowledge** → Created/updated in `knowledge/`
- **People insights** → Added to `people/{Name}.md`
- **Personal notes** → Routed to `personal/`
- **Work notes** → Routed to `work/`

A single item may generate multiple outputs (e.g., an article might create tasks AND knowledge AND people updates).

After processing, items are moved to `.archive/` for reference.

## Quick Capture Examples

**Link:**
```markdown
---
type: link
url: https://example.com/article
---

# Interesting article about X

My notes on why this matters...
```

**Thought:**
```markdown
---
type: thought
---

Random idea: what if we tried X approach for the Y problem?
```

**Task:**
```markdown
---
type: task
---

Remember to follow up with John about the Q1 planning doc
```
