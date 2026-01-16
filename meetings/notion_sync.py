#!/usr/bin/env python3
"""
Notion Meeting Sync

Polls a Notion database for unsynced meetings and writes them as local markdown files.
Designed to work with Granola → Zapier → Notion workflow.

Usage:
    python notion_sync.py                    # Sync unsynced meetings
    python notion_sync.py --list             # List meetings in Notion database
    python notion_sync.py --all              # Force sync all meetings (ignore Synced flag)
    python notion_sync.py --dry-run          # Show what would be synced without writing

Environment:
    NOTION_TOKEN     - Notion integration token (required)
    NOTION_DATABASE  - Database ID (required)

Or create ~/.config/notion_sync.json:
    {"token": "secret_xxx", "database_id": "xxx-xxx-xxx"}
"""

import json
import os
import re
import argparse
import urllib.request
import urllib.error
from datetime import datetime
from pathlib import Path
from typing import Optional


# Configuration paths
CONFIG_FILE = Path.home() / ".config" / "notion_sync.json"
OUTPUT_DIR = Path(__file__).parent

# Notion API
NOTION_API_BASE = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"


class NotionClient:
    """Client for Notion API using urllib (no external dependencies)."""

    def __init__(self, token: str, quiet: bool = False):
        self.token = token
        self.quiet = quiet
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Notion-Version": NOTION_VERSION,
        }

    def _request(self, method: str, endpoint: str, payload: Optional[dict] = None) -> Optional[dict]:
        """Make an API request to Notion."""
        url = f"{NOTION_API_BASE}{endpoint}"
        data = json.dumps(payload).encode('utf-8') if payload else None

        try:
            req = urllib.request.Request(url, data=data, headers=self.headers, method=method)
            with urllib.request.urlopen(req, timeout=30) as response:
                return json.loads(response.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            error_body = e.read().decode('utf-8') if e.fp else ''
            if not self.quiet:
                print(f"  API error {e.code}: {error_body[:200]}")
            return None
        except Exception as e:
            if not self.quiet:
                print(f"  Request failed: {e}")
            return None

    def query_database(self, database_id: str, filter_obj: Optional[dict] = None,
                       sorts: Optional[list] = None) -> list:
        """Query a Notion database with optional filter and sort."""
        payload = {}
        if filter_obj:
            payload["filter"] = filter_obj
        if sorts:
            payload["sorts"] = sorts

        all_results = []
        has_more = True
        start_cursor = None

        while has_more:
            if start_cursor:
                payload["start_cursor"] = start_cursor

            result = self._request("POST", f"/databases/{database_id}/query", payload)
            if not result:
                break

            all_results.extend(result.get("results", []))
            has_more = result.get("has_more", False)
            start_cursor = result.get("next_cursor")

        return all_results

    def get_page(self, page_id: str) -> Optional[dict]:
        """Get a single page by ID."""
        return self._request("GET", f"/pages/{page_id}")

    def update_page(self, page_id: str, properties: dict) -> Optional[dict]:
        """Update page properties."""
        return self._request("PATCH", f"/pages/{page_id}", {"properties": properties})

    def get_block_children(self, block_id: str) -> list:
        """Get all child blocks of a page/block (for reading page content)."""
        all_blocks = []
        has_more = True
        start_cursor = None

        while has_more:
            endpoint = f"/blocks/{block_id}/children"
            if start_cursor:
                endpoint += f"?start_cursor={start_cursor}"

            result = self._request("GET", endpoint)
            if not result:
                break

            all_blocks.extend(result.get("results", []))
            has_more = result.get("has_more", False)
            start_cursor = result.get("next_cursor")

        return all_blocks


def load_config() -> tuple:
    """Load Notion credentials from environment or config file.

    Returns:
        (token, database_id) tuple
    """
    # Try environment first
    token = os.environ.get("NOTION_TOKEN")
    database_id = os.environ.get("NOTION_DATABASE")

    if token and database_id:
        return token, database_id

    # Try config file
    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, 'r') as f:
                config = json.load(f)
            token = token or config.get("token")
            database_id = database_id or config.get("database_id")
        except Exception:
            pass

    return token, database_id


def sanitize_filename(name: str) -> str:
    """Convert a string to a safe filename."""
    name = re.sub(r'[<>:"/\\|?*]', '', name)
    name = re.sub(r'\s+', '_', name)
    name = name.strip('._')
    return name[:100]


def extract_rich_text(rich_text_array: list) -> str:
    """Extract plain text from Notion rich_text array."""
    if not rich_text_array:
        return ""
    return "".join(item.get("plain_text", "") for item in rich_text_array)


def extract_property_value(prop: dict) -> str:
    """Extract value from a Notion property object."""
    prop_type = prop.get("type", "")

    if prop_type == "title":
        return extract_rich_text(prop.get("title", []))
    elif prop_type == "rich_text":
        return extract_rich_text(prop.get("rich_text", []))
    elif prop_type == "date":
        date_obj = prop.get("date")
        if date_obj:
            return date_obj.get("start", "")
        return ""
    elif prop_type == "select":
        select_obj = prop.get("select")
        if select_obj:
            return select_obj.get("name", "")
        return ""
    elif prop_type == "multi_select":
        items = prop.get("multi_select", [])
        return ", ".join(item.get("name", "") for item in items)
    elif prop_type == "checkbox":
        return prop.get("checkbox", False)
    elif prop_type == "url":
        return prop.get("url", "") or ""
    elif prop_type == "number":
        return str(prop.get("number", ""))
    else:
        return ""


def blocks_to_markdown(blocks: list) -> str:
    """Convert Notion blocks to markdown."""
    lines = []

    for block in blocks:
        block_type = block.get("type", "")
        block_data = block.get(block_type, {})

        if block_type == "paragraph":
            text = extract_rich_text(block_data.get("rich_text", []))
            if text:
                lines.append(text)
                lines.append("")

        elif block_type == "heading_1":
            text = extract_rich_text(block_data.get("rich_text", []))
            lines.append(f"# {text}")
            lines.append("")

        elif block_type == "heading_2":
            text = extract_rich_text(block_data.get("rich_text", []))
            lines.append(f"## {text}")
            lines.append("")

        elif block_type == "heading_3":
            text = extract_rich_text(block_data.get("rich_text", []))
            lines.append(f"### {text}")
            lines.append("")

        elif block_type == "bulleted_list_item":
            text = extract_rich_text(block_data.get("rich_text", []))
            lines.append(f"- {text}")

        elif block_type == "numbered_list_item":
            text = extract_rich_text(block_data.get("rich_text", []))
            lines.append(f"1. {text}")

        elif block_type == "to_do":
            text = extract_rich_text(block_data.get("rich_text", []))
            checked = block_data.get("checked", False)
            checkbox = "[x]" if checked else "[ ]"
            lines.append(f"- {checkbox} {text}")

        elif block_type == "toggle":
            text = extract_rich_text(block_data.get("rich_text", []))
            lines.append(f"<details><summary>{text}</summary></details>")
            lines.append("")

        elif block_type == "code":
            text = extract_rich_text(block_data.get("rich_text", []))
            language = block_data.get("language", "")
            lines.append(f"```{language}")
            lines.append(text)
            lines.append("```")
            lines.append("")

        elif block_type == "quote":
            text = extract_rich_text(block_data.get("rich_text", []))
            lines.append(f"> {text}")
            lines.append("")

        elif block_type == "divider":
            lines.append("---")
            lines.append("")

        elif block_type == "callout":
            text = extract_rich_text(block_data.get("rich_text", []))
            icon = block_data.get("icon", {})
            emoji = icon.get("emoji", "") if icon.get("type") == "emoji" else ""
            lines.append(f"> {emoji} {text}")
            lines.append("")

    return "\n".join(lines)


def format_meeting_markdown(page: dict, content_blocks: list, client: NotionClient) -> str:
    """Format a Notion meeting page as markdown."""
    props = page.get("properties", {})
    lines = []

    # Extract properties - try common naming conventions
    title = ""
    date_str = ""
    attendees = ""
    summary = ""
    transcript = ""
    source = ""

    for prop_name, prop_value in props.items():
        prop_lower = prop_name.lower()
        value = extract_property_value(prop_value)

        if prop_value.get("type") == "title":
            title = value
        elif prop_lower in ("date", "meeting date", "datetime"):
            date_str = value
        elif prop_lower in ("attendees", "participants", "people"):
            attendees = value
        elif prop_lower == "summary":
            summary = value
        elif prop_lower == "transcript":
            transcript = value
        elif prop_lower == "source":
            source = value

    # Header
    lines.append(f"# {title or 'Untitled Meeting'}")
    lines.append("")

    # Metadata
    if date_str:
        try:
            dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            lines.append(f"**Date**: {dt.strftime('%Y-%m-%d %H:%M')}")
        except Exception:
            lines.append(f"**Date**: {date_str}")

    if attendees:
        lines.append(f"**Participants**: {attendees}")

    if source:
        lines.append(f"**Source**: {source}")

    lines.append("")

    # Summary (from property)
    if summary:
        lines.append("## Summary")
        lines.append("")
        lines.append(summary)
        lines.append("")

    # Page content (from blocks)
    if content_blocks:
        content_md = blocks_to_markdown(content_blocks)
        if content_md.strip():
            lines.append("## Notes")
            lines.append("")
            lines.append(content_md)
            lines.append("")

    # Transcript (from property)
    if transcript:
        lines.append("## Transcript")
        lines.append("")
        lines.append(transcript)
        lines.append("")

    return "\n".join(lines)


def sync_meetings(client: NotionClient, database_id: str, output_dir: Path,
                  sync_all: bool = False, dry_run: bool = False, quiet: bool = False) -> int:
    """Sync unsynced meetings from Notion to local markdown files.

    Returns:
        Number of meetings synced
    """
    # Build filter for unsynced meetings
    filter_obj = None
    if not sync_all:
        # Try to filter by Synced = false
        filter_obj = {
            "property": "Synced",
            "checkbox": {"equals": False}
        }

    # Sort by date descending
    sorts = [{"property": "Date", "direction": "descending"}]

    # Query database
    if not quiet:
        print("Querying Notion database...")

    pages = client.query_database(database_id, filter_obj=filter_obj, sorts=sorts)

    if not pages:
        if not quiet:
            print("No unsynced meetings found.")
        return 0

    if not quiet:
        print(f"Found {len(pages)} meeting(s) to sync")

    # Create output directory
    transcripts_dir = output_dir / "transcripts"
    transcripts_dir.mkdir(parents=True, exist_ok=True)

    synced_count = 0

    for page in pages:
        page_id = page.get("id", "")
        props = page.get("properties", {})

        # Get title
        title = ""
        date_str = ""
        for prop_name, prop_value in props.items():
            if prop_value.get("type") == "title":
                title = extract_property_value(prop_value)
            if prop_name.lower() in ("date", "meeting date", "datetime"):
                date_str = extract_property_value(prop_value)

        if not title:
            title = "Untitled"

        # Generate filename
        if date_str:
            try:
                dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
                date_prefix = dt.strftime('%Y-%m-%d')
            except Exception:
                date_prefix = "unknown"
        else:
            date_prefix = "unknown"

        safe_title = sanitize_filename(title)
        filename = f"{date_prefix}_{safe_title}.md"
        filepath = transcripts_dir / filename

        if not quiet:
            print(f"  {'[DRY-RUN] ' if dry_run else ''}Syncing: {filename}")

        if dry_run:
            synced_count += 1
            continue

        # Fetch page content (blocks)
        content_blocks = client.get_block_children(page_id)

        # Format as markdown
        markdown = format_meeting_markdown(page, content_blocks, client)

        # Write file
        with open(filepath, 'w') as f:
            f.write(markdown)

        # Mark as synced in Notion
        client.update_page(page_id, {
            "Synced": {"checkbox": True}
        })

        synced_count += 1

    if not quiet:
        print(f"\nSynced {synced_count} meeting(s) to {transcripts_dir}")

    return synced_count


def list_meetings(client: NotionClient, database_id: str, quiet: bool = False):
    """List all meetings in the Notion database."""
    sorts = [{"property": "Date", "direction": "descending"}]
    pages = client.query_database(database_id, sorts=sorts)

    if not pages:
        print("No meetings found in database.")
        return

    print(f"\n{'Date':<12} {'Synced':<8} {'Title'}")
    print("-" * 80)

    for page in pages:
        props = page.get("properties", {})

        title = ""
        date_str = ""
        synced = False

        for prop_name, prop_value in props.items():
            if prop_value.get("type") == "title":
                title = extract_property_value(prop_value)
            if prop_name.lower() in ("date", "meeting date", "datetime"):
                date_str = extract_property_value(prop_value)
            if prop_name.lower() == "synced":
                synced = extract_property_value(prop_value)

        # Format date
        if date_str:
            try:
                dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
                date_display = dt.strftime('%Y-%m-%d')
            except Exception:
                date_display = date_str[:10]
        else:
            date_display = "unknown"

        synced_display = "Yes" if synced else "No"
        print(f"{date_display:<12} {synced_display:<8} {title[:55]}")

    print(f"\nTotal: {len(pages)} meetings")


def main():
    parser = argparse.ArgumentParser(
        description='Sync meetings from Notion database to local markdown',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Environment variables:
  NOTION_TOKEN     Your Notion integration token
  NOTION_DATABASE  The database ID to sync from

Or create ~/.config/notion_sync.json with:
  {"token": "secret_xxx", "database_id": "xxx-xxx-xxx"}

Examples:
  %(prog)s                    # Sync unsynced meetings
  %(prog)s --list             # List all meetings in database
  %(prog)s --all              # Sync all meetings (ignore Synced flag)
  %(prog)s --dry-run          # Preview what would be synced
"""
    )
    parser.add_argument('--list', '-l', action='store_true',
                        help='List meetings in Notion database')
    parser.add_argument('--all', '-a', action='store_true',
                        help='Sync all meetings (ignore Synced checkbox)')
    parser.add_argument('--dry-run', '-n', action='store_true',
                        help='Show what would be synced without writing')
    parser.add_argument('--output', '-o', type=str,
                        help='Output directory (default: same as script)')
    parser.add_argument('--quiet', '-q', action='store_true',
                        help='Minimal output')

    args = parser.parse_args()

    # Load configuration
    token, database_id = load_config()

    if not token:
        print("Error: NOTION_TOKEN not set")
        print("Set it as an environment variable or in ~/.config/notion_sync.json")
        return 1

    if not database_id:
        print("Error: NOTION_DATABASE not set")
        print("Set it as an environment variable or in ~/.config/notion_sync.json")
        return 1

    # Initialize client
    client = NotionClient(token, quiet=args.quiet)
    output_dir = Path(args.output) if args.output else OUTPUT_DIR

    if args.list:
        list_meetings(client, database_id, quiet=args.quiet)
    else:
        sync_meetings(
            client,
            database_id,
            output_dir,
            sync_all=args.all,
            dry_run=args.dry_run,
            quiet=args.quiet
        )

    return 0


if __name__ == '__main__':
    exit(main())
