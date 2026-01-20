#!/usr/bin/env python3
"""
Notion Agent Poller

Polls for tasks assigned to AI and executes them via Claude.

Triggers:
1. Tasks with Status = "Delegated to AI"
2. Comments containing "@jb" on any task

Workflow:
1. Pick up task, set status to "AI In Progress"
2. Run happy --yolo --print with task context
3. Post output as comment
4. Set status to "Done" (or back to "Not started" on error)

Safety:
- 15-minute timeout per task
- Error comments with debug info
- Only processes one task at a time
"""

import json
import os
import subprocess
import time
import urllib.request
import urllib.error
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

# Configuration
CONFIG_FILE = Path.home() / ".config" / "notion_sync.json"
JPT_ROOT = Path.home() / "jpt"
LOG_FILE = JPT_ROOT / "lib" / ".agent.log"
LOCK_FILE = JPT_ROOT / "lib" / ".agent.lock"
HANDLED_FILE = JPT_ROOT / "lib" / ".agent_handled.json"

NOTION_API_BASE = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"

# Timeouts
TASK_TIMEOUT_SECONDS = 15 * 60  # 15 minutes
POLL_INTERVAL_SECONDS = 60

# Status values
STATUS_DELEGATED = "Delegated (AI)"
STATUS_IN_PROGRESS = "In Progress (AI)"
STATUS_DONE = "Done (AI)"
STATUS_NOT_STARTED = "Not started"

# Trigger keyword for comments
MENTION_TRIGGER = "@jb"

# Response prefix (must NOT contain MENTION_TRIGGER to avoid self-reply loop)
RESPONSE_PREFIX = "**Agent response**"


def log(message: str):
    """Log with timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {message}"
    print(line)
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")


def load_config() -> dict:
    """Load Notion credentials."""
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE) as f:
            return json.load(f)
    return {}


def load_handled_comments() -> set:
    """Load set of already-handled comment IDs."""
    if HANDLED_FILE.exists():
        try:
            with open(HANDLED_FILE) as f:
                data = json.load(f)
                return set(data.get("handled_ids", []))
        except Exception:
            pass
    return set()


def save_handled_comment(comment_id: str):
    """Mark a comment as handled."""
    handled = load_handled_comments()
    handled.add(comment_id)
    # Keep only the most recent 1000 to prevent unbounded growth
    handled_list = list(handled)[-1000:]
    with open(HANDLED_FILE, "w") as f:
        json.dump({"handled_ids": handled_list}, f)


def notion_request(method: str, endpoint: str, payload: Optional[dict] = None) -> Optional[dict]:
    """Make Notion API request."""
    config = load_config()
    token = config.get("token")
    if not token:
        raise ValueError("NOTION_TOKEN not configured")

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Notion-Version": NOTION_VERSION,
    }

    url = f"{NOTION_API_BASE}{endpoint}"
    data = json.dumps(payload).encode() if payload else None

    try:
        req = urllib.request.Request(url, data=data, headers=headers, method=method)
        with urllib.request.urlopen(req, timeout=30) as response:
            return json.loads(response.read().decode())
    except urllib.error.HTTPError as e:
        error_body = e.read().decode() if e.fp else ""
        log(f"API error {e.code}: {error_body[:200]}")
        return None
    except Exception as e:
        log(f"Request failed: {e}")
        return None


def get_tasks_by_status(status: str) -> list[dict]:
    """Get tasks with a specific status."""
    config = load_config()
    tasks_db_id = config.get("tasks_database_id")
    if not tasks_db_id:
        return []

    payload = {
        "filter": {
            "property": "Status",
            "status": {"equals": status}
        }
    }

    result = notion_request("POST", f"/databases/{tasks_db_id}/query", payload)
    return result.get("results", []) if result else []


def get_task_comments(page_id: str) -> list[dict]:
    """Get comments on a task page."""
    result = notion_request("GET", f"/comments?block_id={page_id}")
    return result.get("results", []) if result else []


def add_comment(page_id: str, text: str) -> Optional[dict]:
    """Add a comment to a task page."""
    # Truncate if too long (Notion limit is 2000 chars per rich_text)
    if len(text) > 1900:
        text = text[:1900] + "\n\n... (truncated)"

    payload = {
        "parent": {"page_id": page_id},
        "rich_text": [{"text": {"content": text}}]
    }
    return notion_request("POST", "/comments", payload)


def update_task_status(page_id: str, status: str) -> Optional[dict]:
    """Update task status."""
    payload = {
        "properties": {
            "Status": {"status": {"name": status}}
        }
    }
    return notion_request("PATCH", f"/pages/{page_id}", payload)


def extract_task_info(page: dict) -> dict:
    """Extract task name, notes, source from page."""
    props = page.get("properties", {})

    task_name = ""
    notes = ""
    source = ""

    for prop_name, prop_value in props.items():
        prop_type = prop_value.get("type")

        if prop_type == "title":
            title_arr = prop_value.get("title", [])
            task_name = "".join(t.get("plain_text", "") for t in title_arr)
        elif prop_name == "Notes" and prop_type == "rich_text":
            rt_arr = prop_value.get("rich_text", [])
            notes = "".join(t.get("plain_text", "") for t in rt_arr)
        elif prop_name == "Source" and prop_type == "rich_text":
            rt_arr = prop_value.get("rich_text", [])
            source = "".join(t.get("plain_text", "") for t in rt_arr)

    return {
        "id": page.get("id"),
        "url": page.get("url"),
        "task_name": task_name,
        "notes": notes,
        "source": source,
    }


def find_unhandled_mentions() -> list[dict]:
    """Find tasks with @jb mentions in comments that haven't been handled."""
    config = load_config()
    tasks_db_id = config.get("tasks_database_id")
    if not tasks_db_id:
        return []

    # Load already-handled comment IDs
    handled_ids = load_handled_comments()

    # Get all non-done tasks
    payload = {
        "filter": {
            "property": "Status",
            "status": {"does_not_equal": "Done"}
        }
    }

    result = notion_request("POST", f"/databases/{tasks_db_id}/query", payload)
    tasks = result.get("results", []) if result else []

    mentions = []
    for task in tasks:
        page_id = task.get("id")
        comments = get_task_comments(page_id)

        for comment in comments:
            comment_id = comment.get("id")

            # Skip if we've already handled this comment
            if comment_id in handled_ids:
                continue

            # Extract comment text
            rich_text = comment.get("rich_text", [])
            text = "".join(rt.get("plain_text", "") for rt in rich_text)

            if MENTION_TRIGGER in text.lower():
                mentions.append({
                    "task": task,
                    "comment": comment,
                    "comment_text": text,
                    "comment_id": comment_id,
                })

    return mentions


def run_agent(task_info: dict, extra_context: str = "") -> tuple[bool, str]:
    """Run happy --yolo --print with task context."""
    prompt = f"""You are an AI agent working on a task from Jesse's Notion task list.

## Task
**Name**: {task_info['task_name']}
**Source**: {task_info['source'] or 'Not specified'}
**Notes**: {task_info['notes'] or 'None'}

{extra_context}

## Instructions
Complete this task to the best of your ability. You have full access to the filesystem at ~/jpt and can run commands.

If the task is unclear or you need more information, explain what's missing.
If you complete the task, summarize what you did.
If you cannot complete the task, explain why.

Work in the ~/jpt directory. Be concise but thorough."""

    happy_bin = Path.home() / "Library/pnpm/happy"

    try:
        result = subprocess.run(
            [str(happy_bin), "--yolo", "--print", prompt],
            capture_output=True,
            text=True,
            timeout=TASK_TIMEOUT_SECONDS,
            cwd=str(JPT_ROOT),
        )

        output = result.stdout.strip()
        if result.stderr:
            output += f"\n\nSTDERR:\n{result.stderr.strip()}"

        success = result.returncode == 0
        return success, output

    except subprocess.TimeoutExpired:
        return False, f"TIMEOUT: Task exceeded {TASK_TIMEOUT_SECONDS // 60} minute limit"
    except Exception as e:
        return False, f"ERROR: {str(e)}"


def process_delegated_task(task: dict) -> bool:
    """Process a task with 'Delegated to AI' status."""
    task_info = extract_task_info(task)
    page_id = task_info["id"]

    log(f"Processing task: {task_info['task_name'][:50]}...")

    # Set status to AI In Progress
    update_task_status(page_id, STATUS_IN_PROGRESS)

    # Run agent
    success, output = run_agent(task_info)

    if success:
        # Post success comment
        comment = f"**Agent completed task**\n\n{output}"
        add_comment(page_id, comment)
        update_task_status(page_id, STATUS_DONE)
        log(f"  Completed successfully")
        return True
    else:
        # Post error comment and revert status
        comment = f"**Agent failed**\n\n{output}"
        add_comment(page_id, comment)
        update_task_status(page_id, STATUS_NOT_STARTED)
        log(f"  Failed: {output[:100]}")
        return False


def process_mention(mention: dict) -> bool:
    """Process a @jb mention in a comment."""
    task = mention["task"]
    task_info = extract_task_info(task)
    page_id = task_info["id"]
    comment_text = mention["comment_text"]
    comment_id = mention["comment_id"]

    log(f"Processing mention on: {task_info['task_name'][:50]}...")

    # Mark as handled FIRST to prevent loops even if we crash
    save_handled_comment(comment_id)

    # Extra context from the comment
    extra_context = f"""## Comment that triggered this
Someone mentioned @jb in a comment:
"{comment_text}"

Respond to this comment in the context of the task above."""

    # Run agent
    success, output = run_agent(task_info, extra_context)

    if success:
        comment = f"{RESPONSE_PREFIX}\n\n{output}"
        add_comment(page_id, comment)
        log(f"  Responded to mention")
        return True
    else:
        comment = f"{RESPONSE_PREFIX} (failed)\n\n{output}"
        add_comment(page_id, comment)
        log(f"  Failed: {output[:100]}")
        return False


def acquire_lock() -> bool:
    """Simple file-based lock to prevent concurrent runs."""
    if LOCK_FILE.exists():
        # Check if lock is stale (older than 20 minutes)
        mtime = datetime.fromtimestamp(LOCK_FILE.stat().st_mtime)
        if datetime.now() - mtime > timedelta(minutes=20):
            log("Removing stale lock file")
            LOCK_FILE.unlink()
        else:
            return False

    LOCK_FILE.write_text(str(os.getpid()))
    return True


def release_lock():
    """Release the lock file."""
    if LOCK_FILE.exists():
        LOCK_FILE.unlink()


def poll_once():
    """Run one poll cycle."""
    # Check for delegated tasks
    delegated = get_tasks_by_status(STATUS_DELEGATED)
    if delegated:
        log(f"Found {len(delegated)} delegated task(s)")
        for task in delegated:
            process_delegated_task(task)
            # Only process one at a time
            break
        return

    # Check for @jb mentions
    # Note: This requires comments permission in the integration
    try:
        mentions = find_unhandled_mentions()
        if mentions:
            log(f"Found {len(mentions)} @jb mention(s)")
            for mention in mentions:
                process_mention(mention)
                # Only process one at a time
                break
            return
    except Exception as e:
        # Comments API might not be enabled
        log(f"Could not check mentions: {e}")


def run_daemon():
    """Run as a polling daemon."""
    log("=== Notion Agent Poller Started ===")

    while True:
        if acquire_lock():
            try:
                poll_once()
            finally:
                release_lock()
        else:
            log("Another instance is running, skipping")

        time.sleep(POLL_INTERVAL_SECONDS)


def main():
    import sys

    if len(sys.argv) > 1:
        cmd = sys.argv[1]

        if cmd == "daemon":
            run_daemon()
        elif cmd == "once":
            if acquire_lock():
                try:
                    poll_once()
                finally:
                    release_lock()
            else:
                print("Another instance is running")
        elif cmd == "status":
            delegated = get_tasks_by_status(STATUS_DELEGATED)
            in_progress = get_tasks_by_status(STATUS_IN_PROGRESS)
            print(f"Delegated to AI: {len(delegated)}")
            print(f"AI In Progress: {len(in_progress)}")
            for t in delegated + in_progress:
                info = extract_task_info(t)
                print(f"  - {info['task_name'][:60]}")
        else:
            print(f"Unknown command: {cmd}")
            print("Usage: python notion_agent.py [daemon|once|status]")
    else:
        print("Notion Agent Poller")
        print()
        print("Commands:")
        print("  daemon  - Run continuously, polling every 60s")
        print("  once    - Run one poll cycle and exit")
        print("  status  - Show delegated/in-progress tasks")
        print()
        print("Setup:")
        print("  1. Add 'Delegated to AI' and 'AI In Progress' statuses in Notion")
        print("  2. Enable comments permission in the Meeting Sync integration")
        print("  3. Run: python notion_agent.py daemon")


if __name__ == "__main__":
    main()
