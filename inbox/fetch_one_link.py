#!/usr/bin/env python3
"""
Fetch one link from Notion My Links and save to inbox.

Usage:
    python fetch_one_link.py           # Fetch oldest unsynced item
    python fetch_one_link.py --newest  # Fetch newest unsynced item
    python fetch_one_link.py --pick    # List unsynced items and pick one
    python fetch_one_link.py --include-synced --pick  # Include already synced items

Sync Tracking:
    Items are marked as "Synced and Done" in Notion IMMEDIATELY after saving
    to the inbox (before processing). This prevents duplicates even if the
    inbox processor takes a while to run. The processor handles routing to
    knowledge/, people/, etc. and archiving the file.
"""

import json
import sys
import argparse
import urllib.request
import urllib.error
import re
from datetime import datetime
from pathlib import Path

# Import from the reading sync module
sys.path.insert(0, str(Path(__file__).parent.parent / "reading"))
from notion_reading_sync import (
    load_config, NotionClient, extract_property_value,
    sanitize_filename, HTMLTextExtractor, FETCH_TIMEOUT, USER_AGENT, MAX_CONTENT_SIZE,
    blocks_to_markdown
)

INBOX_DIR = Path(__file__).parent
SYNCED_STATUS = "Synced and Done"  # Status value in Notion indicating already synced


def fetch_url_content(url: str) -> tuple[str, str]:
    """Fetch and extract text content from a URL. Returns (title, content)."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=FETCH_TIMEOUT) as response:
            content_type = response.headers.get('Content-Type', '')
            if 'text/html' not in content_type.lower():
                return "", f"[Non-HTML content: {content_type}]"

            raw = response.read(MAX_CONTENT_SIZE)
            # Try to decode
            for encoding in ['utf-8', 'latin-1', 'cp1252']:
                try:
                    html = raw.decode(encoding)
                    break
                except UnicodeDecodeError:
                    continue
            else:
                html = raw.decode('utf-8', errors='replace')

            extractor = HTMLTextExtractor()
            extractor.feed(html)
            return extractor.title.strip(), extractor.get_text()[:10000]  # Limit content
    except Exception as e:
        return "", f"[Failed to fetch: {e}]"


def get_items(client: NotionClient, database_id: str, limit: int = 20) -> list:
    """Get recent items from the database."""
    items = client.query_database(
        database_id,
        sorts=[{"property": "Created", "direction": "descending"}]
    )
    return items[:limit]


def format_inbox_item(page: dict, fetched_title: str, fetched_content: str, notion_content: str = "") -> str:
    """Format a Notion page as an inbox markdown item."""
    props = page.get("properties", {})

    # Extract key properties
    title = extract_property_value(props.get("Name", {})) or "Untitled"
    url = extract_property_value(props.get("URL", {})) or ""
    item_type = extract_property_value(props.get("Type", {})) or "link"
    tags = extract_property_value(props.get("Tags", {})) or ""
    created = extract_property_value(props.get("Created", {})) or datetime.now().isoformat()
    overview = extract_property_value(props.get("Overview", {})) or ""
    ai_summary = extract_property_value(props.get("AI summary", {})) or ""

    # Build markdown
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

    # Notion page content (block children) - this is the main content
    if notion_content:
        md += f"## Content (from Notion)\n\n{notion_content}\n\n"

    # Fallback to fetched URL content if no Notion content
    if fetched_content and not fetched_content.startswith("["):
        md += f"## Fetched Content (from URL)\n\n{fetched_content}\n"
    elif fetched_content:
        md += f"## Note\n{fetched_content}\n"

    return md


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
        print(f"  Warning: Could not mark as synced: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Fetch one link from Notion to inbox")
    parser.add_argument("--newest", action="store_true", help="Fetch newest unsynced item")
    parser.add_argument("--pick", action="store_true", help="List items and pick one")
    parser.add_argument("--index", type=int, help="Pick item by index (0-based)")
    parser.add_argument("--include-synced", action="store_true", help="Include already synced items")
    args = parser.parse_args()

    # Load config
    token, databases = load_config()
    if not token:
        print("Error: No Notion token found")
        sys.exit(1)

    db_id = databases.get("main") or databases.get("reading_list")
    if not db_id:
        print("Error: No database ID found")
        sys.exit(1)

    client = NotionClient(token, quiet=True)

    # Get items
    print("Fetching items from Notion...")
    all_items = get_items(client, db_id, limit=50)  # Fetch more to filter

    # Filter out synced items unless --include-synced
    if args.include_synced:
        items = all_items
    else:
        items = [item for item in all_items if not is_synced(item)]

    if not items:
        print("No unsynced items found (use --include-synced to see all)")
        sys.exit(1)

    # Pick or list items
    if args.pick:
        print("\nRecent items:" + (" (showing all)" if args.include_synced else " (unsynced only)"))
        print("-" * 65)
        for i, item in enumerate(items[:20]):  # Show max 20
            props = item.get("properties", {})
            title = extract_property_value(props.get("Name", {})) or "Untitled"
            item_type = extract_property_value(props.get("Type", {})) or "?"
            synced = "✓" if is_synced(item) else " "
            print(f"  [{i}] [{synced}] ({item_type}) {title[:45]}")
        print("-" * 65)
        try:
            idx = int(input("Enter index to fetch: "))
            selected = items[idx]
        except (ValueError, IndexError):
            print("Invalid selection")
            sys.exit(1)
    elif args.index is not None:
        selected = items[args.index]
    elif args.newest:
        selected = items[0]
    else:
        # Default: oldest unsynced item
        selected = items[-1]

    # Extract info
    props = selected.get("properties", {})
    page_id = selected.get("id", "")
    title = extract_property_value(props.get("Name", {})) or "Untitled"
    url = extract_property_value(props.get("URL", {})) or ""

    print(f"\nSelected: {title}")
    print(f"URL: {url}")

    # Fetch Notion page content (block children)
    notion_content = ""
    if page_id:
        print("Fetching Notion page content...")
        blocks = client.get_block_children(page_id)
        if blocks:
            notion_content = blocks_to_markdown(blocks)
            print(f"  Notion content length: {len(notion_content)} chars")
        else:
            print("  No block content found in Notion page")

    # Fetch URL content as fallback
    fetched_title, fetched_content = "", ""
    if url and not notion_content:
        print("Fetching URL content as fallback...")
        fetched_title, fetched_content = fetch_url_content(url)
        if fetched_title:
            print(f"  Page title: {fetched_title[:60]}")
        print(f"  Content length: {len(fetched_content)} chars")

    # Format and save
    md_content = format_inbox_item(selected, fetched_title, fetched_content, notion_content)

    # Generate filename
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
    print(f"\nSaved to: {filepath}")

    # Mark as synced in Notion
    if page_id:
        print("Marking as synced in Notion...")
        if mark_as_synced(client, page_id):
            print("  Done")

    print(f"Run the inbox processor to process it, or wait for the background job.")


if __name__ == "__main__":
    main()
