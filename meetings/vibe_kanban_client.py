#!/usr/bin/env python3
"""
Vibe Kanban MCP Client

Creates tasks in vibe-kanban from meeting action items.
Uses Claude CLI to call the MCP tool since it has direct access.
"""

import subprocess
import json
from pathlib import Path
from typing import Optional

# Default project ID for jpt (can be overridden)
DEFAULT_PROJECT_ID = "8f82f54b-3a37-4eed-a3af-54aeb09828b7"


def create_task(
    title: str,
    description: Optional[str] = None,
    project_id: str = DEFAULT_PROJECT_ID,
    quiet: bool = False
) -> Optional[str]:
    """
    Create a task in vibe-kanban using Claude CLI with MCP tools.

    Args:
        title: Task title (required)
        description: Optional task description
        project_id: Project ID to create task in (defaults to jpt project)
        quiet: Suppress output

    Returns:
        Task ID if created successfully, None otherwise
    """
    # Build the prompt for Claude to create the task
    prompt_parts = [
        f"Create a task in vibe-kanban with title: \"{title}\"",
        f"Project ID: {project_id}"
    ]
    if description:
        prompt_parts.append(f"Description: {description}")
    prompt_parts.append("Use the mcp__vibe_kanban__create_task tool. Return ONLY the task ID, nothing else.")

    prompt = "\n".join(prompt_parts)

    try:
        # Use claude CLI which has access to MCP tools
        result = subprocess.run(
            ['claude', '--dangerously-skip-permissions', '-p', prompt],
            capture_output=True,
            text=True,
            timeout=60
        )

        if result.returncode == 0:
            # Try to extract task ID from response
            output = result.stdout.strip()
            if not quiet:
                print(f"  ✅ Created task: {title[:50]}...")
            return output
        else:
            if not quiet:
                print(f"  ❌ Failed to create task: {result.stderr[:200]}")
            return None

    except subprocess.TimeoutExpired:
        if not quiet:
            print(f"  ⚠ Timeout creating task: {title[:50]}")
        return None
    except FileNotFoundError:
        if not quiet:
            print(f"  ⚠ Claude CLI not found - cannot create vibe-kanban tasks")
        return None
    except Exception as e:
        if not quiet:
            print(f"  ⚠ Error creating task: {e}")
        return None


def create_tasks_from_action_items(
    action_items: list[dict],
    meeting_title: str,
    meeting_date: str,
    project_id: str = DEFAULT_PROJECT_ID,
    quiet: bool = False
) -> list[str]:
    """
    Create multiple tasks from meeting action items.

    Args:
        action_items: List of action items with 'task', 'owner', 'due' keys
        meeting_title: Title of the source meeting
        meeting_date: Date of the meeting
        project_id: Project ID to create tasks in
        quiet: Suppress output

    Returns:
        List of created task IDs
    """
    if not action_items:
        return []

    created_ids = []

    if not quiet:
        print(f"  📋 Creating {len(action_items)} task(s) in vibe-kanban...")

    for item in action_items:
        task_text = item.get('task', '').strip()
        if not task_text:
            continue

        owner = item.get('owner', '').strip()
        due = item.get('due', '').strip()

        # Build task title
        title = task_text
        if owner and owner.lower() not in ['me', 'jesse', 'you']:
            title = f"@{owner}: {task_text}"

        # Build description with meeting context
        description_parts = [
            f"From meeting: {meeting_title}",
            f"Date: {meeting_date}"
        ]
        if owner:
            description_parts.append(f"Owner: {owner}")
        if due:
            description_parts.append(f"Due: {due}")

        description = "\n".join(description_parts)

        task_id = create_task(
            title=title,
            description=description,
            project_id=project_id,
            quiet=quiet
        )

        if task_id:
            created_ids.append(task_id)

    if not quiet:
        print(f"  ✅ Created {len(created_ids)}/{len(action_items)} tasks")

    return created_ids


if __name__ == "__main__":
    # Test creating a task
    import sys

    if len(sys.argv) > 1:
        title = " ".join(sys.argv[1:])
    else:
        title = "Test task from meeting analysis"

    print(f"Creating test task: {title}")
    task_id = create_task(title, description="Test description from CLI")
    print(f"Result: {task_id}")
