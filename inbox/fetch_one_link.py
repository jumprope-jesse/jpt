#!/usr/bin/env python3
"""
Fetch one link from Notion My Links and save to inbox.

Usage:
    python fetch_one_link.py           # Fetch oldest unsynced item
    python fetch_one_link.py --newest  # Fetch newest item
    python fetch_one_link.py --pick    # List recent items and pick one
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
    sanitize_filename, HTMLTextExtractor, FETCH_TIMEOUT, USER_AGENT, MAX_CONTENT_SIZE
)

INBOX_DIR = Path(__file__).parent


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


def format_inbox_item(page: dict, fetched_title: str, fetched_content: str) -> str:
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

    if fetched_content and not fetched_content.startswith("["):
        md += f"## Fetched Content\n\n{fetched_content}\n"
    elif fetched_content:
        md += f"## Note\n{fetched_content}\n"

    return md


def main():
    parser = argparse.ArgumentParser(description="Fetch one link from Notion to inbox")
    parser.add_argument("--newest", action="store_true", help="Fetch newest item")
    parser.add_argument("--pick", action="store_true", help="List items and pick one")
    parser.add_argument("--index", type=int, help="Pick item by index (0-based)")
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
    items = get_items(client, db_id, limit=20)

    if not items:
        print("No items found")
        sys.exit(1)

    # Pick or list items
    if args.pick:
        print("\nRecent items:")
        print("-" * 60)
        for i, item in enumerate(items):
            props = item.get("properties", {})
            title = extract_property_value(props.get("Name", {})) or "Untitled"
            item_type = extract_property_value(props.get("Type", {})) or "?"
            print(f"  [{i}] ({item_type}) {title[:50]}")
        print("-" * 60)
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
        # Default: oldest of the recent batch
        selected = items[-1]

    # Extract info
    props = selected.get("properties", {})
    title = extract_property_value(props.get("Name", {})) or "Untitled"
    url = extract_property_value(props.get("URL", {})) or ""

    print(f"\nSelected: {title}")
    print(f"URL: {url}")

    # Fetch content
    fetched_title, fetched_content = "", ""
    if url:
        print("Fetching URL content...")
        fetched_title, fetched_content = fetch_url_content(url)
        if fetched_title:
            print(f"  Page title: {fetched_title[:60]}")
        print(f"  Content length: {len(fetched_content)} chars")

    # Format and save
    md_content = format_inbox_item(selected, fetched_title, fetched_content)

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
    print(f"Run the inbox processor to process it, or wait for the background job.")


if __name__ == "__main__":
    main()
