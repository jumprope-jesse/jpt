#!/usr/bin/env python3
"""
Notion Tasks API Client

Provides functions to create and query tasks in the Notion Tasks database.
Used by meeting processor, inbox processor, and other scripts.

Configuration:
    Uses ~/.config/notion_sync.json for credentials:
    {
        "token": "ntn_xxx",
        "database_id": "xxx",  // Meetings database (legacy)
        "tasks_database_id": "xxx",
        "projects_database_id": "xxx"
    }

    Or environment variables:
    NOTION_TOKEN, NOTION_TASKS_DATABASE, NOTION_PROJECTS_DATABASE
"""

import json
import os
import urllib.request
import urllib.error
from pathlib import Path
from typing import Optional

# Configuration
CONFIG_FILE = Path.home() / ".config" / "notion_sync.json"
NOTION_API_BASE = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"

# Database IDs (loaded from config)
_config_cache = None


def _load_config() -> dict:
    """Load configuration from file or environment."""
    global _config_cache
    if _config_cache is not None:
        return _config_cache

    config = {}

    # Try config file first
    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, 'r') as f:
                config = json.load(f)
        except Exception:
            pass

    # Environment overrides
    if os.environ.get("NOTION_TOKEN"):
        config["token"] = os.environ["NOTION_TOKEN"]
    if os.environ.get("NOTION_TASKS_DATABASE"):
        config["tasks_database_id"] = os.environ["NOTION_TASKS_DATABASE"]
    if os.environ.get("NOTION_PROJECTS_DATABASE"):
        config["projects_database_id"] = os.environ["NOTION_PROJECTS_DATABASE"]

    _config_cache = config
    return config


def _request(method: str, endpoint: str, payload: Optional[dict] = None) -> Optional[dict]:
    """Make an API request to Notion."""
    config = _load_config()
    token = config.get("token")
    if not token:
        raise ValueError("NOTION_TOKEN not configured")

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Notion-Version": NOTION_VERSION,
    }

    url = f"{NOTION_API_BASE}{endpoint}"
    data = json.dumps(payload).encode('utf-8') if payload else None

    try:
        req = urllib.request.Request(url, data=data, headers=headers, method=method)
        with urllib.request.urlopen(req, timeout=30) as response:
            return json.loads(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8') if e.fp else ''
        print(f"Notion API error {e.code}: {error_body[:200]}")
        return None
    except Exception as e:
        print(f"Notion request failed: {e}")
        return None


def create_task(
    task_name: str,
    source: Optional[str] = None,
    notes: Optional[str] = None,
    due_date: Optional[str] = None,
    status: str = "Not started",
    project_id: Optional[str] = None,
    body: Optional[str] = None,
) -> Optional[dict]:
    """
    Create a task in the Notion Tasks database.

    Args:
        task_name: The task title (required)
        source: Where the task came from (e.g., "Meeting: Weekly Standup", "Inbox: Article")
        notes: Additional context for Notes property (truncated to 2000 chars)
        due_date: Due date in ISO format (YYYY-MM-DD)
        status: Task status (default: "Not started")
        project_id: Notion page ID of related project (optional)
        body: Content for the page body (supports longer text than notes property)

    Returns:
        The created page object, or None on failure
    """
    config = _load_config()
    tasks_db_id = config.get("tasks_database_id")
    if not tasks_db_id:
        raise ValueError("tasks_database_id not configured")

    properties = {
        "Task name": {
            "title": [{"text": {"content": task_name}}]
        },
        "Status": {
            "status": {"name": status}
        }
    }

    if source:
        properties["Source"] = {
            "rich_text": [{"text": {"content": source}}]
        }

    if notes:
        properties["Notes"] = {
            "rich_text": [{"text": {"content": notes[:2000]}}]  # Notion limit
        }

    if due_date:
        properties["Due"] = {
            "date": {"start": due_date}
        }

    if project_id:
        properties["Project"] = {
            "relation": [{"id": project_id}]
        }

    payload = {
        "parent": {"database_id": tasks_db_id},
        "properties": properties
    }

    # Add page body content if provided
    if body:
        children = _text_to_blocks(body)
        if children:
            payload["children"] = children

    result = _request("POST", "/pages", payload)
    if result:
        print(f"  Created Notion task: {task_name[:50]}...")
    return result


def _text_to_blocks(text: str) -> list[dict]:
    """
    Convert plain text to Notion block objects.

    Splits text into paragraphs and creates paragraph blocks.
    Each text chunk is limited to 2000 chars (Notion's limit).
    """
    blocks = []
    paragraphs = text.split('\n\n')

    for para in paragraphs:
        para = para.strip()
        if not para:
            continue

        # Split long paragraphs into chunks
        chunks = []
        while para:
            chunks.append(para[:2000])
            para = para[2000:]

        for chunk in chunks:
            blocks.append({
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [{"type": "text", "text": {"content": chunk}}]
                }
            })

    return blocks


def update_task(
    page_id: str,
    task_name: Optional[str] = None,
    source: Optional[str] = None,
    notes: Optional[str] = None,
    due_date: Optional[str] = None,
    status: Optional[str] = None,
    project_id: Optional[str] = None,
    body: Optional[str] = None,
) -> Optional[dict]:
    """
    Update an existing task in the Notion Tasks database.

    Args:
        page_id: The Notion page ID of the task to update (required)
        task_name: New task title (optional)
        source: New source (optional)
        notes: New notes for Notes property (optional, truncated to 2000 chars)
        due_date: New due date in ISO format YYYY-MM-DD, or "" to clear (optional)
        status: New status (optional)
        project_id: New project relation ID, or "" to clear (optional)
        body: New content for page body - replaces existing body content (optional)

    Returns:
        The updated page object, or None on failure
    """
    properties = {}

    if task_name is not None:
        properties["Task name"] = {
            "title": [{"text": {"content": task_name}}]
        }

    if source is not None:
        properties["Source"] = {
            "rich_text": [{"text": {"content": source}}] if source else []
        }

    if notes is not None:
        properties["Notes"] = {
            "rich_text": [{"text": {"content": notes[:2000]}}] if notes else []
        }

    if due_date is not None:
        properties["Due"] = {
            "date": {"start": due_date} if due_date else None
        }

    if status is not None:
        properties["Status"] = {
            "status": {"name": status}
        }

    if project_id is not None:
        properties["Project"] = {
            "relation": [{"id": project_id}] if project_id else []
        }

    # Update properties if any were provided
    result = None
    if properties:
        payload = {"properties": properties}
        result = _request("PATCH", f"/pages/{page_id}", payload)

    # Update body content if provided (requires separate API calls)
    if body is not None:
        # First, get existing blocks to delete them
        existing = _request("GET", f"/blocks/{page_id}/children?page_size=100", None)
        if existing:
            for block in existing.get("results", []):
                _request("DELETE", f"/blocks/{block['id']}", None)

        # Then add new blocks
        if body:
            children = _text_to_blocks(body)
            if children:
                _request("PATCH", f"/blocks/{page_id}/children", {"children": children})

        # If we didn't update properties, fetch the page to return it
        if not result:
            result = _request("GET", f"/pages/{page_id}", None)

    if result:
        print(f"  Updated Notion task: {page_id[:20]}...")
    return result


def create_tasks_from_action_items(
    action_items: list[dict],
    meeting_title: str,
    meeting_date: str,
) -> list[dict]:
    """
    Create multiple tasks from meeting action items.

    Args:
        action_items: List of dicts with 'owner', 'task', 'due' keys
        meeting_title: The source meeting title
        meeting_date: The meeting date (YYYY-MM-DD)

    Returns:
        List of created task objects
    """
    created = []
    source = f"Meeting: {meeting_title}"

    for item in action_items:
        task_name = item.get("task", "")
        if not task_name:
            continue

        owner = item.get("owner", "")
        due = item.get("due")

        # Add owner to notes if not Jesse
        notes = None
        if owner and owner.lower() not in ("jesse", "me", "you", ""):
            notes = f"Owner: @{owner}"

        result = create_task(
            task_name=task_name,
            source=source,
            notes=notes,
            due_date=due if due and due != "null" else None,
        )

        if result:
            created.append(result)

    print(f"  Created {len(created)} tasks in Notion")
    return created


def query_tasks(
    status: Optional[str] = None,
    project_id: Optional[str] = None,
    limit: int = 100,
    created_after: Optional[str] = None,
) -> list[dict]:
    """
    Query tasks from the Notion database.

    Args:
        status: Filter by status (e.g., "Not started", "In progress", "Done")
        project_id: Filter by project relation
        limit: Maximum number of results
        created_after: Filter to tasks created after this ISO timestamp (e.g., "2026-01-17T00:00:00")

    Returns:
        List of task page objects
    """
    config = _load_config()
    tasks_db_id = config.get("tasks_database_id")
    if not tasks_db_id:
        raise ValueError("tasks_database_id not configured")

    filters = []

    if status:
        filters.append({
            "property": "Status",
            "status": {"equals": status}
        })

    if project_id:
        filters.append({
            "property": "Project",
            "relation": {"contains": project_id}
        })

    if created_after:
        filters.append({
            "timestamp": "created_time",
            "created_time": {"on_or_after": created_after}
        })

    payload = {
        "page_size": min(limit, 100),
    }

    if filters:
        if len(filters) == 1:
            payload["filter"] = filters[0]
        else:
            payload["filter"] = {"and": filters}

    result = _request("POST", f"/databases/{tasks_db_id}/query", payload)
    return result.get("results", []) if result else []


def get_recent_task_stats() -> dict:
    """
    Get stats about tasks created in the last 24 hours.

    Returns:
        Dict with 'created_24h', 'completed_24h', 'pending' counts
    """
    from datetime import datetime, timedelta

    yesterday = (datetime.now() - timedelta(hours=24)).strftime("%Y-%m-%dT%H:%M:%S")

    # Get all tasks created in last 24 hours
    recent_tasks = query_tasks(created_after=yesterday, limit=100)

    completed = 0
    pending = 0
    for task in recent_tasks:
        props = task.get("properties", {})
        status_prop = props.get("Status", {})
        status_obj = status_prop.get("status", {})
        status_name = status_obj.get("name", "") if status_obj else ""

        if status_name in ("Done", "Done (AI)"):
            completed += 1
        else:
            pending += 1

    return {
        "created_24h": len(recent_tasks),
        "completed_24h": completed,
        "pending_24h": pending,
    }


def get_projects() -> list[dict]:
    """
    Get all projects from the Projects database.

    Returns:
        List of project page objects with id and name
    """
    config = _load_config()
    projects_db_id = config.get("projects_database_id")
    if not projects_db_id:
        raise ValueError("projects_database_id not configured")

    result = _request("POST", f"/databases/{projects_db_id}/query", {"page_size": 100})

    projects = []
    for page in result.get("results", []) if result else []:
        props = page.get("properties", {})
        name = ""
        for prop_name, prop_value in props.items():
            if prop_value.get("type") == "title":
                title_arr = prop_value.get("title", [])
                name = "".join(t.get("plain_text", "") for t in title_arr)
                break

        projects.append({
            "id": page["id"],
            "name": name,
            "url": page.get("url", "")
        })

    return projects


# CLI interface for testing
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python notion_tasks.py <command> [args]")
        print("Commands:")
        print("  create <task_name> [source] [notes] [body]")
        print("  update <page_id> --field=value ...")
        print("    Fields: --name, --source, --notes, --body, --status, --due, --project")
        print("  list [status]")
        print("  projects")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "create":
        task_name = sys.argv[2] if len(sys.argv) > 2 else "Test task"
        source = sys.argv[3] if len(sys.argv) > 3 else None
        notes = sys.argv[4] if len(sys.argv) > 4 else None
        body = sys.argv[5] if len(sys.argv) > 5 else None
        result = create_task(task_name, source=source, notes=notes, body=body)
        if result:
            print(f"Created: {result.get('url')}")

    elif cmd == "update":
        if len(sys.argv) < 3:
            print("Usage: update <page_id> --field=value ...")
            sys.exit(1)
        page_id = sys.argv[2]
        kwargs = {}
        for arg in sys.argv[3:]:
            if arg.startswith("--name="):
                kwargs["task_name"] = arg[7:]
            elif arg.startswith("--source="):
                kwargs["source"] = arg[9:]
            elif arg.startswith("--notes="):
                kwargs["notes"] = arg[8:]
            elif arg.startswith("--body="):
                kwargs["body"] = arg[7:]
            elif arg.startswith("--status="):
                kwargs["status"] = arg[9:]
            elif arg.startswith("--due="):
                kwargs["due_date"] = arg[6:]
            elif arg.startswith("--project="):
                kwargs["project_id"] = arg[10:]
        if not kwargs:
            print("No fields to update. Use --field=value syntax.")
            sys.exit(1)
        result = update_task(page_id, **kwargs)
        if result:
            print(f"Updated: {result.get('url')}")

    elif cmd == "list":
        status = sys.argv[2] if len(sys.argv) > 2 else None
        tasks = query_tasks(status=status)
        for task in tasks:
            props = task.get("properties", {})
            name = ""
            for p in props.values():
                if p.get("type") == "title":
                    name = "".join(t.get("plain_text", "") for t in p.get("title", []))
                    break
            print(f"- {name}")

    elif cmd == "projects":
        projects = get_projects()
        for p in projects:
            print(f"{p['id']}: {p['name']}")
