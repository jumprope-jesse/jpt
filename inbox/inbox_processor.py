#!/usr/bin/env python3
"""
Inbox Processor

Scans inbox/ for new items and launches Claude to process each one.
Claude handles all routing decisions and file operations directly.
"""

import os
import subprocess
from pathlib import Path
from datetime import datetime

# Paths
JPT_ROOT = Path.home() / "jpt"
INBOX_DIR = JPT_ROOT / "inbox"
ARCHIVE_DIR = INBOX_DIR / ".archive"
LOG_FILE = INBOX_DIR / ".processor.log"

# Files to ignore
IGNORE_FILES = {"README.md", ".processor.log", ".DS_Store"}


def log(message: str):
    """Log a message with timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] {message}"
    print(log_line)
    with open(LOG_FILE, "a") as f:
        f.write(log_line + "\n")


def get_inbox_items() -> list[Path]:
    """Get all markdown files in inbox that need processing."""
    items = []
    for file in INBOX_DIR.iterdir():
        if file.is_file() and file.suffix == ".md" and file.name not in IGNORE_FILES:
            items.append(file)
    return sorted(items, key=lambda f: f.stat().st_mtime)


def process_item(item_path: Path):
    """Launch Claude to process a single inbox item."""
    log(f"Processing: {item_path.name}")

    # Read item content
    content = item_path.read_text()

    # Build prompt for Claude
    prompt = f"""You are processing an inbox item for Jesse's second brain system.

## Your Task
Read the inbox item below and route it appropriately. A single item may generate MULTIPLE outputs.

## Available Destinations

1. **TASKS.md** (`/Users/jesse/jpt/TASKS.md`)
   - Append actionable tasks with appropriate priority/context
   - Format: `- [ ] Task description`

2. **knowledge/** (`/Users/jesse/jpt/knowledge/`)
   - Create new files OR append to existing files for reference material
   - Use descriptive kebab-case filenames (e.g., `react-server-components.md`)
   - Decide: is this a new topic or does it relate to existing knowledge?

3. **people/** (`/Users/jesse/jpt/people/`)
   - Update person profiles with new insights
   - Check if person already has a file, append to it if so

4. **personal/** (`/Users/jesse/jpt/personal/`)
   - Personal life stuff (family, health, home, hobbies)

5. **work/** (`/Users/jesse/jpt/work/`)
   - Work-specific projects and notes

## After Processing
Move the inbox item to the archive:
`/Users/jesse/jpt/inbox/.archive/{item_path.name}`

## The Inbox Item

Filename: {item_path.name}

---
{content}
---

Process this item now. Read any existing files you need to check for context, then write your updates."""

    # Call Claude via happy CLI
    happy_bin = Path.home() / "Library/pnpm/happy"

    try:
        result = subprocess.run(
            [str(happy_bin), "--yolo", "--print", prompt],
            capture_output=True,
            text=True,
            timeout=300,  # 5 min timeout for complex items
            cwd=str(JPT_ROOT)
        )

        if result.returncode != 0:
            log(f"ERROR processing {item_path.name}: {result.stderr}")
            return False

        log(f"Completed: {item_path.name}")
        if result.stdout.strip():
            # Log a summary (first 200 chars)
            summary = result.stdout.strip()[:200].replace('\n', ' ')
            log(f"  Output: {summary}...")

        return True

    except subprocess.TimeoutExpired:
        log(f"TIMEOUT processing {item_path.name}")
        return False
    except Exception as e:
        log(f"EXCEPTION processing {item_path.name}: {e}")
        return False


def main():
    """Main processing loop."""
    log("=== Inbox Processor Started ===")

    # Ensure archive directory exists
    ARCHIVE_DIR.mkdir(exist_ok=True)

    # Get items to process
    items = get_inbox_items()

    if not items:
        log("No items to process")
        return

    log(f"Found {len(items)} item(s) to process")

    for item in items:
        process_item(item)

    log("=== Inbox Processor Finished ===")


if __name__ == "__main__":
    main()
