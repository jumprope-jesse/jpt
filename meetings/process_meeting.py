#!/usr/bin/env python3
"""
Meeting Processing Pipeline

Watches Meetily SQLite DB for new meetings, processes them through Claude,
and outputs:
- Structured meeting notes (using appropriate template)
- Action items → Notion Tasks database
- People insights → /people/*.md updates
"""
from __future__ import annotations

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
# Notion tasks module
sys.path.insert(0, str(JPT_ROOT / "lib"))
from notion_tasks import create_task

# Agenda processor (optional - won't fail if not available)
try:
    from agenda_processor import get_agenda_for_meeting, update_agenda_after_meeting
    AGENDA_AVAILABLE = True
except ImportError:
    AGENDA_AVAILABLE = False

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
    happy_bin = Path("/opt/homebrew/bin/happy")

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


def identify_speakers(meeting: dict, known_people: list[str]) -> list[str]:
    """Use Claude to identify speakers from transcript patterns."""
    system_prompt = """You are a speaker identification assistant. Analyze the transcript and identify who is speaking.

Look for:
- Self-identification ("This is Jesse", "It's Sarah here")
- Role/title mentions ("As the product owner...", "I'm the CTO")
- Name mentions by others ("Thanks John", "What do you think, Maria?")
- Contextual clues about roles and relationships
- Speaking patterns and topics that suggest expertise/role

Output ONLY a JSON object:
{
  "speakers": ["Name1", "Name2"],
  "confidence": 75,
  "reasoning": "Brief explanation of how you identified each speaker"
}

Rules:
- Output ONLY the JSON object, no markdown
- Match names to known people when possible
- If you can't identify specific names, use descriptive roles like "Product Owner", "Developer"
- Jesse is usually one of the participants (the meeting recorder)"""

    user_prompt = f"""Meeting Title: {meeting["title"]}
Known People: {", ".join(known_people)}

TRANSCRIPT:
{meeting["transcript"][:5000]}

Identify the speakers:"""

    try:
        response = call_claude(user_prompt, system_prompt)
        json_match = re.search(r'\{[\s\S]*\}', response)
        if json_match:
            result = json.loads(json_match.group())
            speakers = result.get("speakers", [])
            print(f"  Identified speakers: {speakers} (confidence: {result.get('confidence', 'N/A')}%)")
            return speakers
    except Exception as e:
        print(f"  Speaker identification failed: {e}")

    return []


def process_meeting(meeting: dict, agenda_context: dict = None) -> dict:
    """Process a meeting through Claude to generate structured output."""
    template_name = detect_template(meeting)
    template_file = TEMPLATES_DIR / TEMPLATES[template_name]["file"]
    template_content = template_file.read_text() if template_file.exists() else ""

    known_people = get_known_people()

    # First, try to identify speakers if not already known
    if not meeting.get("speakers"):
        meeting["speakers"] = identify_speakers(meeting, known_people)

    # Build agenda section for prompt if available
    agenda_prompt_section = ""
    if agenda_context:
        agenda_items = []
        for topic in agenda_context.get("topics", []):
            # Strip checkbox prefix for cleaner display
            clean_topic = re.sub(r'^- \[.\] ', '', topic)
            if clean_topic:
                agenda_items.append(f"  - {clean_topic}")
        for question in agenda_context.get("questions", []):
            if question:
                agenda_items.append(f"  - Question: {question}")
        for share in agenda_context.get("to_share", []):
            if share:
                agenda_items.append(f"  - Share: {share}")

        if agenda_items:
            agenda_prompt_section = f"""

JESSE'S AGENDA ITEMS FOR THIS MEETING:
{chr(10).join(agenda_items)}

Compare the transcript against these agenda items:
- For items that WERE discussed, note them in "covered_agenda_items" with the outcome/decision
- For items NOT discussed, list them in "missed_agenda_items"
"""

    system_prompt = """You are a meeting processing assistant. Analyze transcripts and output ONLY valid JSON, no other text.

Required JSON structure:
{
  "summary": "2-3 sentence summary of the meeting",
  "key_points": ["point 1", "point 2"],
  "decisions": ["decision 1", "decision 2"],
  "action_items": [{"owner": "Name", "task": "description", "due": "date or null"}],
  "risks": ["risk or concern 1"],
  "people_insights": [{"name": "PersonName", "insight": "what we learned about them"}],
  "participants": ["Name1", "Name2"],
  "meeting_type_confidence": 85,
  "covered_agenda_items": [{"item": "agenda item text", "outcome": "what was decided/discussed"}],
  "missed_agenda_items": ["agenda item that was not discussed"]
}

Rules:
- Output ONLY the JSON object, no markdown, no explanation
- Be concise and actionable
- For people_insights, only include substantive new information about people mentioned
- Match names to known people when possible
- For participants, list everyone who spoke in the meeting
- For covered_agenda_items, match against the provided agenda items and note outcomes
- For missed_agenda_items, list any agenda items that were NOT addressed in the meeting"""

    speakers_hint = f"\nIdentified Speakers: {', '.join(meeting['speakers'])}" if meeting.get('speakers') else ""

    user_prompt = f"""Meeting Title: {meeting["title"]}
Date: {meeting["created_at"]}
Detected Type: {template_name}
Known People: {", ".join(known_people)}{speakers_hint}{agenda_prompt_section}

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

    # Get participants - prefer processed output, fall back to meeting speakers
    participants = processed.get("participants") or meeting.get("speakers") or []
    participants_str = ", ".join(participants) if participants else "Unknown"

    content = f"""# {meeting["title"]}

**Date**: {date_str}
**Template**: {template_name}
**Participants**: {participants_str}

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


def match_name_to_profile(name: str, profiles: list[Path]) -> Path | None:
    """Match a name to a profile, handling full names and first-name-only profiles.

    Matching priority:
    1. Exact match (normalized: spaces/underscores, case-insensitive)
    2. Profile stem matches first name of the input (e.g., "Alicia" matches "Alicia Smith")
    3. Input name is contained in profile stem (e.g., "Justin" in "Justin_Meyer")

    Args:
        name: The name to match (e.g., "Justin Meyer", "Alicia")
        profiles: List of profile file paths

    Returns:
        The matching profile path, or None if no match found.
    """
    name_normalized = name.lower().replace('_', ' ').replace('-', ' ').strip()
    name_parts = name_normalized.split()
    first_name = name_parts[0] if name_parts else ''

    best_match = None
    best_score = 0

    for p in profiles:
        stem = p.stem.lower().replace('_', ' ').replace('-', ' ')
        stem_parts = stem.split()
        stem_first = stem_parts[0] if stem_parts else ''

        # Exact match (highest priority)
        if stem == name_normalized:
            return p

        # Profile is a full name and matches input full name
        if len(stem_parts) >= 2 and len(name_parts) >= 2:
            if stem_parts[0] == name_parts[0] and stem_parts[-1] == name_parts[-1]:
                return p

        # Profile first name matches input first name (good match)
        if stem_first == first_name and len(first_name) > 1:
            # Prefer full name profiles over first-name-only
            score = 3 if len(stem_parts) >= 2 else 2
            if score > best_score:
                best_score = score
                best_match = p

        # Input name contained in profile (partial match)
        elif name_normalized in stem or first_name in stem:
            if best_score < 1:
                best_score = 1
                best_match = p

    return best_match


def update_people_profiles(insights: list[dict]):
    """Update people profiles with new insights."""
    profiles = list(PEOPLE_DIR.glob("*.md")) if PEOPLE_DIR.exists() else []

    for insight in insights:
        name = insight.get("name", "").strip()
        if not name:
            continue

        # Find matching profile using improved matching
        profile_path = match_name_to_profile(name, profiles)

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


def create_vibe_kanban_tasks(action_items: list[dict], meeting_title: str, meeting_date: str):
    """Create tasks in vibe-kanban from action items."""
    if not action_items:
        return

    try:
        from vibe_kanban_client import create_tasks_from_action_items
        create_tasks_from_action_items(
            action_items=action_items,
            meeting_title=meeting_title,
            meeting_date=meeting_date,
            quiet=False
        )
    except ImportError:
        print(f"  ⚠ vibe_kanban_client not found - skipping vibe-kanban task creation")
    except Exception as e:
        print(f"  ⚠ Error creating vibe-kanban tasks: {e}")


def append_tasks(action_items: list[dict], meeting_title: str):
    """Create action items in Notion Tasks database and vibe-kanban."""
    if not action_items:
        return

    date_str = datetime.now().strftime("%Y-%m-%d")
    source = f"Meeting: {meeting_title}"

    # Create tasks in Notion
    created_count = 0
    for item in action_items:
        owner = item.get("owner", "")
        task = item.get("task", "")
        due = item.get("due")

        if not task:
            continue

        # Add owner to notes if not Jesse
        notes = None
        if owner and owner.lower() not in ("jesse", "me", "you", "tbd", ""):
            notes = f"Owner: @{owner}"

        result = create_task(
            task_name=task,
            source=source,
            notes=notes,
            due_date=due if due and due != "null" else None,
        )
        if result:
            created_count += 1

    print(f"  Created {created_count} tasks in Notion")

    # Also create tasks in vibe-kanban
    create_vibe_kanban_tasks(action_items, meeting_title, date_str)


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

            # Load agenda context if available
            agenda_context = None
            if AGENDA_AVAILABLE:
                agenda_context = get_agenda_for_meeting(meeting["title"])
                if agenda_context:
                    print(f"  Agenda loaded: {agenda_context['name']}")

            # Process through Claude
            print("  Calling Claude API...")
            processed = process_meeting(meeting, agenda_context)

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

            # Update agenda with meeting results
            if AGENDA_AVAILABLE and agenda_context:
                try:
                    update_agenda_after_meeting(
                        agenda_path=agenda_context["path"],
                        meeting_date=date_str,
                        summary_path=output_file,
                        transcript_path=output_file,  # Same file for now
                        covered_items=processed.get("covered_agenda_items", []),
                        missed_items=processed.get("missed_agenda_items", [])
                    )
                    print("  Agenda updated")
                except Exception as e:
                    print(f"  Agenda update failed: {e}")

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
