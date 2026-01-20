#!/usr/bin/env python3
"""
Digest Processor

Generates daily, weekly, and monthly digests from various content sources.
Each digest is created as a Notion task with the content in the notes field.

Usage:
    python3 digest_processor.py daily    # 3-min read
    python3 digest_processor.py weekly   # 10-min read
    python3 digest_processor.py monthly  # 10-min read
    python3 digest_processor.py status   # Show last digest dates
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime, timedelta
from typing import Optional

# Paths
JPT_ROOT = Path.home() / "jpt"
INBOX_ARCHIVE = JPT_ROOT / "inbox" / ".archive"
MEETINGS_DIR = JPT_ROOT / "meetings" / "transcripts"
KNOWLEDGE_DIR = JPT_ROOT / "knowledge"
LOG_FILE = JPT_ROOT / "lib" / ".digest.log"
STATE_FILE = JPT_ROOT / "lib" / ".digest_state.json"

# Import notion tasks
sys.path.insert(0, str(JPT_ROOT / "lib"))
try:
    from notion_tasks import create_task, query_tasks
except ImportError:
    print("ERROR: Could not import notion_tasks")
    sys.exit(1)


def log(message: str):
    """Log a message with timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] {message}"
    print(log_line)
    with open(LOG_FILE, "a") as f:
        f.write(log_line + "\n")


def load_state() -> dict:
    """Load digest state (last run times)."""
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text())
        except Exception:
            pass
    return {}


def save_state(state: dict):
    """Save digest state."""
    STATE_FILE.write_text(json.dumps(state, indent=2))


def get_files_since(directory: Path, since: datetime, extension: str = ".md") -> list[tuple[Path, str]]:
    """Get files modified since a given time, returns list of (path, content) tuples."""
    files = []
    if not directory.exists():
        return files

    for file in directory.iterdir():
        if file.is_file() and file.suffix == extension:
            try:
                mtime = datetime.fromtimestamp(file.stat().st_mtime)
                if mtime >= since:
                    content = file.read_text()
                    # Truncate very long files
                    if len(content) > 5000:
                        content = content[:5000] + "\n\n[... truncated ...]"
                    files.append((file, content))
            except Exception:
                continue

    return sorted(files, key=lambda x: x[0].stat().st_mtime, reverse=True)


def get_tasks_since(since: datetime) -> list[dict]:
    """Get tasks created since a given time."""
    try:
        since_str = since.strftime("%Y-%m-%dT%H:%M:%S")
        tasks = query_tasks(created_after=since_str, limit=100)

        result = []
        for task in tasks:
            props = task.get("properties", {})

            # Get task name
            name = ""
            for p in props.values():
                if p.get("type") == "title":
                    name = "".join(t.get("plain_text", "") for t in p.get("title", []))
                    break

            # Get status
            status_prop = props.get("Status", {})
            status_obj = status_prop.get("status", {})
            status = status_obj.get("name", "") if status_obj else ""

            # Get source
            source_prop = props.get("Source", {})
            source_text = source_prop.get("rich_text", [])
            source = "".join(t.get("plain_text", "") for t in source_text)

            result.append({
                "name": name,
                "status": status,
                "source": source,
                "url": task.get("url", "")
            })

        return result
    except Exception as e:
        log(f"Error querying tasks: {e}")
        return []


def gather_content(period: str) -> dict:
    """Gather content from all sources for the given period."""
    now = datetime.now()

    if period == "daily":
        since = now - timedelta(days=1)
        period_label = "Daily"
    elif period == "weekly":
        since = now - timedelta(weeks=1)
        period_label = "Weekly"
    elif period == "monthly":
        since = now - timedelta(days=30)
        period_label = "Monthly"
    else:
        raise ValueError(f"Unknown period: {period}")

    content = {
        "period": period,
        "period_label": period_label,
        "since": since.strftime("%Y-%m-%d"),
        "until": now.strftime("%Y-%m-%d"),
        "inbox_items": [],
        "meetings": [],
        "knowledge_updates": [],
        "tasks": [],
    }

    # Gather inbox items
    inbox_files = get_files_since(INBOX_ARCHIVE, since)
    for path, text in inbox_files[:50]:  # Limit to 50 items
        content["inbox_items"].append({
            "filename": path.name,
            "content": text[:2000]  # Truncate long content
        })

    # Gather meeting transcripts
    meeting_files = get_files_since(MEETINGS_DIR, since)
    for path, text in meeting_files[:20]:  # Limit to 20 meetings
        content["meetings"].append({
            "filename": path.name,
            "content": text[:3000]
        })

    # Gather knowledge updates
    knowledge_files = get_files_since(KNOWLEDGE_DIR, since)
    for path, text in knowledge_files[:30]:  # Limit to 30 files
        content["knowledge_updates"].append({
            "filename": path.name,
            "content": text[:2000]
        })

    # Gather tasks
    content["tasks"] = get_tasks_since(since)

    return content


def generate_digest(content: dict) -> Optional[str]:
    """Call Claude to generate the digest."""
    period = content["period"]

    # Determine target length
    if period == "daily":
        target = "3-minute read (approximately 600-800 words)"
    else:
        target = "10-minute read (approximately 2000-2500 words)"

    # Build content summary for prompt
    inbox_summary = ""
    if content["inbox_items"]:
        inbox_summary = "\n\n### Inbox Items Processed\n"
        for item in content["inbox_items"]:
            inbox_summary += f"\n---\n**{item['filename']}**\n{item['content']}\n"

    meetings_summary = ""
    if content["meetings"]:
        meetings_summary = "\n\n### Meetings\n"
        for meeting in content["meetings"]:
            meetings_summary += f"\n---\n**{meeting['filename']}**\n{meeting['content']}\n"

    knowledge_summary = ""
    if content["knowledge_updates"]:
        knowledge_summary = "\n\n### Knowledge Base Updates\n"
        for kb in content["knowledge_updates"]:
            knowledge_summary += f"\n---\n**{kb['filename']}**\n{kb['content']}\n"

    tasks_summary = ""
    if content["tasks"]:
        tasks_summary = "\n\n### Tasks\n"
        for task in content["tasks"]:
            status_emoji = "✅" if task["status"] in ("Done", "Done (AI)") else "⏳"
            tasks_summary += f"- {status_emoji} {task['name']} ({task['status']})\n"

    prompt = f"""Generate a {content['period_label']} Digest for Jesse.

## Requirements

1. **Length**: {target}
2. **Format**: Markdown with clear structure
3. **Include**:
   - Table of Contents (linked sections)
   - Executive Summary (2-3 paragraphs, the TL;DR)
   - Key sections based on the content below

## Structure Template

```markdown
# {content['period_label']} Digest: {content['since']} to {content['until']}

## Table of Contents
- [Executive Summary](#executive-summary)
- [Key Themes](#key-themes)
- [Meetings & Decisions](#meetings--decisions)
- [Knowledge & Learning](#knowledge--learning)
- [Tasks & Progress](#tasks--progress)
- [Action Items](#action-items)

## Executive Summary
[2-3 paragraph overview of the most important things from this period]

## Key Themes
[What patterns or themes emerged across inbox, meetings, and knowledge?]

## Meetings & Decisions
[Summary of key meetings and decisions made]

## Knowledge & Learning
[New topics explored, insights gained]

## Tasks & Progress
[What got done, what's pending]

## Action Items
[Any clear next steps or items needing attention]
```

## Content to Summarize

**Period**: {content['since']} to {content['until']}
**Inbox Items**: {len(content['inbox_items'])}
**Meetings**: {len(content['meetings'])}
**Knowledge Updates**: {len(content['knowledge_updates'])}
**Tasks**: {len(content['tasks'])}
{inbox_summary}
{meetings_summary}
{knowledge_summary}
{tasks_summary}

---

Generate the digest now. Focus on extracting signal from noise - what actually matters?
Synthesize across sources to identify patterns and themes.
Be concise but comprehensive. This is for Jesse to review, so write in second person where appropriate ("You attended...", "Your focus was on...").

Output ONLY the markdown digest, nothing else."""

    # Call Claude
    happy_bin = Path.home() / "Library/pnpm/happy"

    try:
        log(f"Calling Claude to generate {period} digest...")
        result = subprocess.run(
            [str(happy_bin), "--yolo", "--print", prompt],
            capture_output=True,
            text=True,
            timeout=300,  # 5 min timeout
            cwd=str(JPT_ROOT)
        )

        if result.returncode != 0:
            log(f"ERROR: Claude returned non-zero: {result.stderr}")
            return None

        digest = result.stdout.strip()
        if not digest:
            log("ERROR: Empty response from Claude")
            return None

        log(f"Generated digest: {len(digest)} characters")
        return digest

    except subprocess.TimeoutExpired:
        log("ERROR: Claude timed out")
        return None
    except Exception as e:
        log(f"ERROR: {e}")
        return None


def create_digest_task(period: str, digest: str) -> bool:
    """Create a Notion task with the digest content."""
    now = datetime.now()

    if period == "daily":
        title = f"Daily Digest - {now.strftime('%Y-%m-%d')}"
    elif period == "weekly":
        week_start = (now - timedelta(days=now.weekday())).strftime('%Y-%m-%d')
        title = f"Weekly Digest - Week of {week_start}"
    elif period == "monthly":
        title = f"Monthly Digest - {now.strftime('%B %Y')}"
    else:
        title = f"Digest - {now.strftime('%Y-%m-%d')}"

    # Notion notes field has a 2000 char limit, so we need to truncate
    # But the digest is the main content, so we'll include as much as we can
    notes = digest[:2000] if len(digest) > 2000 else digest

    try:
        result = create_task(
            task_name=title,
            source="Digest Processor",
            notes=notes,
            status="Not started"
        )

        if result:
            log(f"Created Notion task: {title}")
            return True
        else:
            log("ERROR: Failed to create Notion task")
            return False

    except Exception as e:
        log(f"ERROR creating task: {e}")
        return False


def save_digest_file(period: str, digest: str) -> Path:
    """Save the full digest to a file (since Notion truncates)."""
    digests_dir = JPT_ROOT / "digests"
    digests_dir.mkdir(exist_ok=True)

    now = datetime.now()
    filename = f"{now.strftime('%Y-%m-%d')}_{period}_digest.md"
    filepath = digests_dir / filename

    filepath.write_text(digest)
    log(f"Saved full digest to: {filepath}")

    return filepath


def run_digest(period: str):
    """Run the full digest pipeline."""
    log(f"=== Starting {period.upper()} Digest ===")

    # Check if we already ran today (for daily) or this week (for weekly)
    state = load_state()
    now = datetime.now()

    last_run_key = f"last_{period}"
    if last_run_key in state:
        last_run = datetime.fromisoformat(state[last_run_key])

        if period == "daily" and last_run.date() == now.date():
            log(f"Already ran {period} digest today")
            return
        elif period == "weekly" and (now - last_run).days < 6:
            log(f"Already ran {period} digest this week")
            return
        elif period == "monthly" and last_run.month == now.month and last_run.year == now.year:
            log(f"Already ran {period} digest this month")
            return

    # Gather content
    log("Gathering content...")
    content = gather_content(period)

    total_items = (
        len(content["inbox_items"]) +
        len(content["meetings"]) +
        len(content["knowledge_updates"]) +
        len(content["tasks"])
    )

    if total_items == 0:
        log("No content to digest")
        return

    log(f"Found: {len(content['inbox_items'])} inbox, {len(content['meetings'])} meetings, "
        f"{len(content['knowledge_updates'])} knowledge, {len(content['tasks'])} tasks")

    # Generate digest
    digest = generate_digest(content)
    if not digest:
        log("Failed to generate digest")
        return

    # Save full digest to file
    filepath = save_digest_file(period, digest)

    # Create Notion task with truncated content + link to full file
    task_notes = digest[:1900]  # Leave room for file path
    if len(digest) > 1900:
        task_notes += f"\n\n[Full digest: {filepath}]"

    create_task(
        task_name=f"{period.capitalize()} Digest - {now.strftime('%Y-%m-%d')}",
        source="Digest Processor",
        notes=task_notes,
        status="Not started"
    )

    # Update state
    state[last_run_key] = now.isoformat()
    save_state(state)

    log(f"=== {period.upper()} Digest Complete ===")


def show_status():
    """Show the status of digest runs."""
    state = load_state()

    print("\nDigest Status")
    print("=" * 40)

    for period in ["daily", "weekly", "monthly"]:
        key = f"last_{period}"
        if key in state:
            last_run = datetime.fromisoformat(state[key])
            ago = datetime.now() - last_run
            print(f"{period.capitalize():10} Last run: {last_run.strftime('%Y-%m-%d %H:%M')} ({ago.days}d {ago.seconds//3600}h ago)")
        else:
            print(f"{period.capitalize():10} Never run")

    print()


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1].lower()

    if cmd == "status":
        show_status()
    elif cmd in ("daily", "weekly", "monthly"):
        run_digest(cmd)
    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
