#!/usr/bin/env python3
"""
Meeting Processing Pipeline

Watches Meetily SQLite DB for new meetings, processes them through Claude,
and outputs:
- Structured meeting notes (using appropriate template)
- Action items → TASKS.md
- People insights → /people/*.md updates
"""

import sqlite3
import json
import os
import re
import sys
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Optional

# Paths
MEETILY_DB = Path.home() / "Library/Application Support/com.meetily.ai/meeting_minutes.sqlite"
JPT_ROOT = Path.home() / "jpt"
TEMPLATES_DIR = JPT_ROOT / "meetings/templates"
TRANSCRIPTS_DIR = JPT_ROOT / "meetings/transcripts"
PEOPLE_DIR = JPT_ROOT / "people"
TASKS_FILE = JPT_ROOT / "TASKS.md"
PROCESSED_FILE = JPT_ROOT / "meetings/.processed_meetings.json"

# Template definitions with detection rules
TEMPLATES = {
    "1-on-1": {
        "file": "1-on-1.md",
        "indicators": ["1:1", "1-on-1", "one on one", "check-in", "check in"],
        "participant_count": 2,
        "priority": 10
    },
    "product-leadership": {
        "file": "product-leadership.md",
        "indicators": ["product", "leadership", "board", "roadmap", "quarterly", "division"],
        "participant_count": None,  # any
        "priority": 8
    },
    "standup": {
        "file": "standup.md",
        "indicators": ["standup", "stand-up", "daily", "scrum"],
        "participant_count": None,
        "priority": 7
    },
    "general": {
        "file": "general.md",
        "indicators": [],
        "participant_count": None,
        "priority": 0  # fallback
    }
}


def call_claude(prompt: str, system: str = "") -> str:
    """Call Claude via the claude CLI (uses Claude Max auth)."""
    # Combine system and user prompt for CLI
    full_prompt = prompt
    if system:
        full_prompt = f"{system}\n\n---\n\n{prompt}"

    # Use claude CLI with --print flag for non-interactive output
    # --dangerously-skip-permissions avoids interactive permission prompts
    # Full path to happy binary (launchd doesn't have shell PATH)
    # happy --yolo is equivalent to claude --dangerously-skip-permissions
    happy_bin = Path.home() / "Library/pnpm/happy"

    result = subprocess.run(
        [str(happy_bin), "--yolo", "--print", full_prompt],
        capture_output=True,
        text=True,
        timeout=180
    )

    if result.returncode != 0:
        raise Exception(f"Claude CLI error: {result.stderr}")

    return result.stdout


def get_meetings_from_db() -> list[dict]:
    """Get all meetings from Meetily database."""
    if not MEETILY_DB.exists():
        return []

    conn = sqlite3.connect(MEETILY_DB)
    conn.row_factory = sqlite3.Row

    meetings = []
    cursor = conn.execute("""
        SELECT m.id, m.title, m.created_at,
               GROUP_CONCAT(t.transcript, ' ') as full_transcript,
               GROUP_CONCAT(DISTINCT t.speaker) as speakers
        FROM meetings m
        LEFT JOIN transcripts t ON t.meeting_id = m.id
        GROUP BY m.id
        ORDER BY m.created_at DESC
    """)

    for row in cursor:
        meetings.append({
            "id": row["id"],
            "title": row["title"],
            "created_at": row["created_at"],
            "transcript": row["full_transcript"] or "",
            "speakers": [s for s in (row["speakers"] or "").split(",") if s]
        })

    conn.close()
    return meetings


def get_processed_meetings() -> set:
    """Get set of already processed meeting IDs."""
    if PROCESSED_FILE.exists():
        data = json.loads(PROCESSED_FILE.read_text())
        return set(data.get("processed", []))
    return set()


def mark_processed(meeting_id: str):
    """Mark a meeting as processed."""
    processed = get_processed_meetings()
    processed.add(meeting_id)
    PROCESSED_FILE.parent.mkdir(parents=True, exist_ok=True)
    PROCESSED_FILE.write_text(json.dumps({"processed": list(processed)}, indent=2))


def detect_template(meeting: dict) -> str:
    """Detect the best template for a meeting based on title and content."""
    title_lower = meeting["title"].lower()
    transcript_lower = meeting["transcript"].lower()[:1000]  # first 1000 chars
    speaker_count = len(meeting["speakers"]) if meeting["speakers"] else 0

    best_match = "general"
    best_score = 0

    for template_name, config in TEMPLATES.items():
        score = config["priority"]

        # Check title indicators
        for indicator in config["indicators"]:
            if indicator in title_lower:
                score += 20
            if indicator in transcript_lower:
                score += 5

        # Check participant count
        if config["participant_count"] is not None:
            if speaker_count == config["participant_count"]:
                score += 15

        if score > best_score:
            best_score = score
            best_match = template_name

    return best_match


def get_known_people() -> list[str]:
    """Get list of known people from /people directory."""
    if not PEOPLE_DIR.exists():
        return []
    return [f.stem for f in PEOPLE_DIR.glob("*.md")]


def process_meeting(meeting: dict) -> dict:
    """Process a meeting through Claude to generate structured output."""
    template_name = detect_template(meeting)
    template_file = TEMPLATES_DIR / TEMPLATES[template_name]["file"]
    template_content = template_file.read_text() if template_file.exists() else ""

    known_people = get_known_people()

    system_prompt = """You are a meeting processing assistant. Analyze transcripts and output ONLY valid JSON, no other text.

Required JSON structure:
{
  "summary": "2-3 sentence summary of the meeting",
  "key_points": ["point 1", "point 2"],
  "decisions": ["decision 1", "decision 2"],
  "action_items": [{"owner": "Name", "task": "description", "due": "date or null"}],
  "risks": ["risk or concern 1"],
  "people_insights": [{"name": "PersonName", "insight": "what we learned about them"}],
  "meeting_type_confidence": 85
}

Rules:
- Output ONLY the JSON object, no markdown, no explanation
- Be concise and actionable
- For people_insights, only include substantive new information about people mentioned
- Match names to known people when possible"""

    user_prompt = f"""Meeting Title: {meeting["title"]}
Date: {meeting["created_at"]}
Detected Type: {template_name}
Known People: {", ".join(known_people)}

TRANSCRIPT:
{meeting["transcript"]}

Output the JSON:"""

    response = call_claude(user_prompt, system_prompt)

    # Extract JSON from response
    try:
        # Try to find JSON in the response
        json_match = re.search(r'\{[\s\S]*\}', response)
        if json_match:
            return json.loads(json_match.group())
    except json.JSONDecodeError:
        pass

    # Fallback structure
    return {
        "summary": response[:500],
        "key_points": [],
        "decisions": [],
        "action_items": [],
        "risks": [],
        "people_insights": [],
        "meeting_type_confidence": 50
    }


def format_meeting_markdown(meeting: dict, processed: dict, template_name: str) -> str:
    """Format processed meeting data into markdown using the template."""
    date_str = meeting["created_at"][:10]

    # Build action items table
    action_items_md = ""
    for item in processed.get("action_items", []):
        owner = item.get("owner", "TBD")
        task = item.get("task", "")
        due = item.get("due", "")
        action_items_md += f"| {owner} | {task} | {due} |\n"

    # Build key points
    key_points_md = "\n".join(f"- {p}" for p in processed.get("key_points", []))

    # Build decisions
    decisions_md = "\n".join(f"- {d}" for d in processed.get("decisions", []))

    # Build risks
    risks_md = "\n".join(f"- {r}" for r in processed.get("risks", []))

    content = f"""# {meeting["title"]}

**Date**: {date_str}
**Template**: {template_name}
**Participants**: {", ".join(meeting.get("speakers", [])) or "Unknown"}

## Summary
{processed.get("summary", "")}

## Key Points
{key_points_md or "- No key points extracted"}

## Decisions
{decisions_md or "- No decisions recorded"}

## Risks & Concerns
{risks_md or "- None noted"}

## Action Items
| Owner | Task | Due |
|-------|------|-----|
{action_items_md or "| - | No action items | - |"}

## Full Transcript
{meeting["transcript"]}
"""
    return content


def update_people_profiles(insights: list[dict]):
    """Update people profiles with new insights."""
    for insight in insights:
        name = insight.get("name", "").strip()
        if not name:
            continue

        # Find matching profile (case-insensitive)
        profile_path = None
        for p in PEOPLE_DIR.glob("*.md"):
            if p.stem.lower() == name.lower() or name.lower() in p.stem.lower():
                profile_path = p
                break

        if not profile_path:
            continue

        # Append insight to meeting history section
        content = profile_path.read_text()
        date_str = datetime.now().strftime("%Y-%m-%d")
        new_entry = f"- {date_str}: {insight.get('insight', '')}\n"

        if "## Meeting History" in content:
            # Insert after Meeting History header
            content = content.replace(
                "## Meeting History\n",
                f"## Meeting History\n{new_entry}"
            )
        else:
            # Append new section
            content += f"\n## Meeting History\n{new_entry}"

        profile_path.write_text(content)
        print(f"  Updated profile: {profile_path.name}")


def append_tasks(action_items: list[dict], meeting_title: str):
    """Append action items to TASKS.md."""
    if not action_items:
        return

    date_str = datetime.now().strftime("%Y-%m-%d")

    tasks_content = TASKS_FILE.read_text() if TASKS_FILE.exists() else "# Tasks\n\n"

    new_tasks = f"\n## From: {meeting_title} ({date_str})\n"
    for item in action_items:
        owner = item.get("owner", "TBD")
        task = item.get("task", "")
        if "jesse" in owner.lower() or owner.lower() == "me" or owner.lower() == "you":
            new_tasks += f"- [ ] {task}\n"
        else:
            new_tasks += f"- [ ] {task} (@{owner})\n"

    tasks_content += new_tasks
    TASKS_FILE.write_text(tasks_content)
    print(f"  Added {len(action_items)} tasks to TASKS.md")


def process_new_meetings():
    """Main function to process all new meetings."""
    print("Checking for new meetings...")

    meetings = get_meetings_from_db()
    processed_ids = get_processed_meetings()

    new_meetings = [m for m in meetings if m["id"] not in processed_ids]

    if not new_meetings:
        print("No new meetings to process.")
        return

    print(f"Found {len(new_meetings)} new meeting(s)")

    for meeting in new_meetings:
        print(f"\nProcessing: {meeting['title']}")

        # Skip if transcript is empty or too short
        if len(meeting["transcript"]) < 50:
            print("  Skipping - transcript too short")
            mark_processed(meeting["id"])
            continue

        try:
            # Detect template
            template_name = detect_template(meeting)
            print(f"  Template: {template_name}")

            # Process through Claude
            print("  Calling Claude API...")
            processed = process_meeting(meeting)

            # Generate markdown
            markdown = format_meeting_markdown(meeting, processed, template_name)

            # Save to transcripts
            date_str = meeting["created_at"][:10]
            safe_title = re.sub(r'[^\w\s-]', '', meeting["title"]).strip().replace(' ', '_')
            output_file = TRANSCRIPTS_DIR / f"{date_str}_{safe_title}.md"
            output_file.write_text(markdown)
            print(f"  Saved: {output_file.name}")

            # Update people profiles
            if processed.get("people_insights"):
                update_people_profiles(processed["people_insights"])

            # Append tasks
            if processed.get("action_items"):
                append_tasks(processed["action_items"], meeting["title"])

            # Mark as processed
            mark_processed(meeting["id"])
            print("  Done!")

        except Exception as e:
            print(f"  Error: {e}")
            continue


def watch_mode():
    """Watch for new meetings continuously."""
    import time
    print("Watching for new meetings (Ctrl+C to stop)...")
    while True:
        process_new_meetings()
        time.sleep(60)  # Check every minute


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--watch":
        watch_mode()
    else:
        process_new_meetings()
