#!/usr/bin/env python3
"""
Auto-fetch unsynced items from Notion My Links database.

This script is designed to run via launchd on a timer. It fetches all
unsynced items and saves them to the inbox for processing.

Items are marked as "Synced and Done" in Notion immediately after saving,
preventing duplicates even if the inbox processor hasn't run yet.

Fetches newest items first so new links take priority while still
catching up on any backlog. Processes up to MAX_PER_RUN items per run
to avoid overloading the processor.
"""

import sys
from datetime import datetime
from pathlib import Path

# Import from the reading sync module
sys.path.insert(0, str(Path(__file__).parent.parent / "reading"))
from notion_reading_sync import (
    load_config, NotionClient, extract_property_value,
    sanitize_filename, blocks_to_markdown
)

INBOX_DIR = Path(__file__).parent
LOG_FILE = INBOX_DIR / ".fetcher.log"
SYNCED_STATUS = "Synced and Done"
MAX_PER_RUN = 5  # Max items to fetch per run (prevents overloading processor)


def log(message: str):
    """Log a message with timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] {message}"
    print(log_line)
    with open(LOG_FILE, "a") as f:
        f.write(log_line + "\n")


def is_synced(page: dict) -> bool:
    """Check if a page has already been synced to JPT."""
    props = page.get("properties", {})
    status_prop = props.get("Status", {})
    status_obj = status_prop.get("status")
    if status_obj:
        return status_obj.get("name") == SYNCED_STATUS
    return False


def mark_as_synced(client: NotionClient, page_id: str) -> bool:
    """Mark a Notion page as synced to JPT."""
    try:
        client.update_page(page_id, {"Status": {"status": {"name": SYNCED_STATUS}}})
        return True
    except Exception as e:
        log(f"  Warning: Could not mark {page_id} as synced: {e}")
        return False


def format_inbox_item(page: dict, notion_content: str) -> str:
    """Format a Notion page as an inbox markdown item."""
    props = page.get("properties", {})

    title = extract_property_value(props.get("Name", {})) or "Untitled"
    url = extract_property_value(props.get("URL", {})) or ""
    item_type = extract_property_value(props.get("Type", {})) or "link"
    tags = extract_property_value(props.get("Tags", {})) or ""
    created = extract_property_value(props.get("Created", {})) or datetime.now().isoformat()
    overview = extract_property_value(props.get("Overview", {})) or ""
    ai_summary = extract_property_value(props.get("AI summary", {})) or ""

    md = f"""---
type: link
source: notion
url: {url}
notion_type: {item_type}
tags: {tags}
created: {created}
---

# {title}

"""
    if overview:
        md += f"## Overview (from Notion)\n{overview}\n\n"

    if ai_summary:
        md += f"## AI Summary (from Notion)\n{ai_summary}\n\n"

    if notion_content:
        md += f"## Content (from Notion)\n\n{notion_content}\n\n"

    return md


def fetch_item(client: NotionClient, page: dict) -> bool:
    """Fetch a single item and save to inbox."""
    props = page.get("properties", {})
    page_id = page.get("id", "")
    title = extract_property_value(props.get("Name", {})) or "Untitled"

    log(f"Fetching: {title[:50]}...")

    # Get page content
    notion_content = ""
    if page_id:
        blocks = client.get_block_children(page_id)
        if blocks:
            notion_content = blocks_to_markdown(blocks)

    # Format and save
    md_content = format_inbox_item(page, notion_content)

    safe_title = sanitize_filename(title)
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"{date_str}-{safe_title[:50]}.md"
    filepath = INBOX_DIR / filename

    # Avoid overwrites
    counter = 1
    while filepath.exists():
        filename = f"{date_str}-{safe_title[:50]}-{counter}.md"
        filepath = INBOX_DIR / filename
        counter += 1

    filepath.write_text(md_content)
    log(f"  Saved: {filename}")

    # Mark as synced immediately
    if mark_as_synced(client, page_id):
        log(f"  Marked as synced")
        return True
    return False


def main():
    """Main entry point."""
    log("=== Auto Fetch Started ===")

    # Load config
    token, databases = load_config()
    if not token:
        log("Error: No Notion token found")
        sys.exit(1)

    db_id = databases.get("main") or databases.get("reading_list")
    if not db_id:
        log("Error: No database ID found")
        sys.exit(1)

    client = NotionClient(token, quiet=True)

    # Get ALL items sorted newest first - this ensures new links take priority
    # while still catching up on any backlog over time
    items = client.query_database(
        db_id,
        sorts=[{"property": "Created", "direction": "descending"}]
    )

    # Filter to unsynced only
    unsynced = [item for item in items if not is_synced(item)]

    if not unsynced:
        log("No unsynced items found")
        log("=== Auto Fetch Finished ===")
        return

    log(f"Found {len(unsynced)} unsynced item(s), processing up to {MAX_PER_RUN}")

    # Fetch items (newest first, limited to MAX_PER_RUN)
    fetched = 0
    for item in unsynced[:MAX_PER_RUN]:
        try:
            if fetch_item(client, item):
                fetched += 1
        except Exception as e:
            title = extract_property_value(item.get("properties", {}).get("Name", {})) or "Unknown"
            log(f"Error fetching {title}: {e}")

    log(f"Fetched {fetched} item(s)")
    log("=== Auto Fetch Finished ===")


if __name__ == "__main__":
    main()
