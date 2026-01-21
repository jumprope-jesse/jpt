#!/usr/bin/env python3
"""
Agenda Processor

Manages meeting agendas with two-way integration:
- Provides agenda items to meeting processor for comparison
- Updates agendas after meetings with outcomes and links

Usage:
    python3 agenda_processor.py status              # List agendas with item counts
    python3 agenda_processor.py briefing <name>     # Pre-meeting prep (fuzzy match)
    python3 agenda_processor.py check               # Find stale items
    python3 agenda_processor.py add <name> "topic"  # Add item to agenda
"""

import os
import re
import sys
import yaml
from pathlib import Path
from datetime import datetime, timedelta
from typing import Optional

# Paths
JPT_ROOT = Path.home() / "jpt"
AGENDAS_DIR = JPT_ROOT / "agendas"
LOG_FILE = AGENDAS_DIR / ".agenda.log"

# Import notion tasks for check command
sys.path.insert(0, str(JPT_ROOT / "lib"))
try:
    from notion_tasks import create_task
    NOTION_AVAILABLE = True
except ImportError:
    NOTION_AVAILABLE = False


def log(message: str):
    """Log a message with timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] {message}"
    print(log_line)
    try:
        with open(LOG_FILE, "a") as f:
            f.write(log_line + "\n")
    except Exception:
        pass


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Parse YAML frontmatter from markdown content."""
    if not content.startswith("---"):
        return {}, content

    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content

    try:
        frontmatter = yaml.safe_load(parts[1])
        body = parts[2].lstrip("\n")
        return frontmatter or {}, body
    except yaml.YAMLError:
        return {}, content


def get_all_agendas() -> list[dict]:
    """Get all agenda files with their frontmatter."""
    agendas = []

    if not AGENDAS_DIR.exists():
        return agendas

    for file in AGENDAS_DIR.glob("*.md"):
        if file.name == "README.md":
            continue

        try:
            content = file.read_text()
            frontmatter, body = parse_frontmatter(content)

            agendas.append({
                "path": file,
                "name": file.stem,
                "frontmatter": frontmatter,
                "body": body,
                "content": content
            })
        except Exception as e:
            log(f"Error reading {file.name}: {e}")

    return agendas


def match_meeting_to_agenda(meeting_title: str) -> Optional[dict]:
    """Match a meeting title to an agenda file using frontmatter patterns."""
    meeting_title_lower = meeting_title.lower()
    agendas = get_all_agendas()

    for agenda in agendas:
        patterns = agenda["frontmatter"].get("patterns", [])
        for pattern in patterns:
            try:
                if re.search(pattern, meeting_title_lower, re.IGNORECASE):
                    return agenda
            except re.error:
                continue

    return None


def fuzzy_match_agenda(query: str) -> Optional[dict]:
    """Fuzzy match a query to an agenda file name."""
    query_lower = query.lower().replace("-", "").replace("_", "").replace(" ", "")
    agendas = get_all_agendas()

    # Try exact stem match first
    for agenda in agendas:
        if agenda["name"].lower() == query.lower():
            return agenda

    # Try partial match on name
    for agenda in agendas:
        name_normalized = agenda["name"].lower().replace("-", "")
        if query_lower in name_normalized or name_normalized in query_lower:
            return agenda

    # Try match on person name from frontmatter
    for agenda in agendas:
        person = agenda["frontmatter"].get("person", "").lower()
        if query_lower in person.replace(" ", "") or person.split()[0].lower() == query_lower:
            return agenda

    return None


def parse_next_section(body: str) -> dict:
    """Parse the NEXT section from agenda body."""
    result = {
        "topics": [],
        "questions": [],
        "to_share": [],
        "waiting_for": []
    }

    # Find NEXT section
    next_match = re.search(r"## NEXT\s*\n(.*?)(?=\n## |\Z)", body, re.DOTALL)
    if not next_match:
        return result

    next_content = next_match.group(1)

    # Parse Topics
    topics_match = re.search(r"### Topics\s*\n(.*?)(?=\n### |\n## |\Z)", next_content, re.DOTALL)
    if topics_match:
        for line in topics_match.group(1).strip().split("\n"):
            line = line.strip()
            if line.startswith("- ["):
                # Extract the item text (remove checkbox)
                item = re.sub(r"^- \[.\] ", "", line)
                if item and item != "[ ]":
                    result["topics"].append(line)

    # Parse Questions
    questions_match = re.search(r"### Questions\s*\n(.*?)(?=\n### |\n## |\Z)", next_content, re.DOTALL)
    if questions_match:
        for line in questions_match.group(1).strip().split("\n"):
            line = line.strip()
            if line.startswith("- ") and line != "-":
                result["questions"].append(line[2:])

    # Parse To Share
    share_match = re.search(r"### To Share\s*\n(.*?)(?=\n### |\n## |\Z)", next_content, re.DOTALL)
    if share_match:
        for line in share_match.group(1).strip().split("\n"):
            line = line.strip()
            if line.startswith("- ") and line != "-":
                result["to_share"].append(line[2:])

    return result


def get_agenda_for_meeting(meeting_title: str) -> Optional[dict]:
    """
    Match meeting to agenda, return NEXT items for comparison.
    Called by process_meeting.py before Claude processing.

    Returns: {"path": Path, "topics": [...], "questions": [...], "person": str}
    """
    agenda = match_meeting_to_agenda(meeting_title)
    if not agenda:
        return None

    next_items = parse_next_section(agenda["body"])

    return {
        "path": agenda["path"],
        "name": agenda["name"],
        "person": agenda["frontmatter"].get("person"),
        "topics": next_items["topics"],
        "questions": next_items["questions"],
        "to_share": next_items["to_share"],
    }


def update_agenda_after_meeting(
    agenda_path: Path,
    meeting_date: str,
    summary_path: Path,
    transcript_path: Optional[Path],
    covered_items: list[dict],
    missed_items: list[str]
):
    """
    Update agenda file after meeting processing.

    1. Add meeting entry to Meetings section (reverse chron)
    2. Annotate covered items: - [x] Item (Discussed DATE: outcome)
    3. Keep missed items unchecked in NEXT
    4. Insert links to summary/transcript
    """
    content = agenda_path.read_text()

    # Build meeting entry
    summary_rel = summary_path.relative_to(JPT_ROOT) if summary_path else None
    transcript_rel = transcript_path.relative_to(JPT_ROOT) if transcript_path else None

    files_line = "**Files**: "
    file_links = []
    if summary_rel:
        file_links.append(f"[Summary](../{summary_rel})")
    if transcript_rel:
        file_links.append(f"[Transcript](../{transcript_rel})")
    files_line += " | ".join(file_links) if file_links else "None"

    covered_text = ""
    if covered_items:
        covered_text = "\n**Covered**:\n"
        for item in covered_items:
            item_name = item.get("item", "Unknown")
            outcome = item.get("outcome", "")
            if outcome:
                covered_text += f"- {item_name} → {outcome}\n"
            else:
                covered_text += f"- {item_name}\n"

    missed_text = ""
    if missed_items:
        missed_text = "\n**Missed**:\n"
        for item in missed_items:
            missed_text += f"- {item} (rolled to NEXT)\n"

    meeting_entry = f"""### {meeting_date}
{files_line}
{covered_text}{missed_text}
---

"""

    # Insert meeting entry after ## Meetings header
    meetings_pattern = r"(## Meetings\s*\n)"
    if re.search(meetings_pattern, content):
        content = re.sub(meetings_pattern, f"\\1\n{meeting_entry}", content)

    # Update covered items in NEXT section with annotations
    for item in covered_items:
        item_name = item.get("item", "")
        outcome = item.get("outcome", "")
        if not item_name:
            continue

        # Find the item in NEXT and mark it complete with annotation
        # Match unchecked items that contain the item name
        item_pattern = re.escape(item_name)
        old_pattern = rf"- \[ \] ([^\n]*{item_pattern}[^\n]*)"
        annotation = f"(Discussed {meeting_date}: {outcome})" if outcome else f"(Discussed {meeting_date})"

        match = re.search(old_pattern, content, re.IGNORECASE)
        if match:
            old_line = match.group(0)
            new_line = old_line.replace("- [ ]", "- [x]")
            if not new_line.endswith(")"):
                new_line += f" {annotation}"
            content = content.replace(old_line, new_line)

    # Write updated content
    agenda_path.write_text(content)
    log(f"Updated agenda: {agenda_path.name}")


def add_item_to_agenda(agenda_name: str, item: str) -> bool:
    """Add an item to an agenda's NEXT > Topics section."""
    agenda = fuzzy_match_agenda(agenda_name)
    if not agenda:
        print(f"No agenda found matching '{agenda_name}'")
        return False

    content = agenda["content"]

    # Find Topics section and add item
    topics_pattern = r"(### Topics\s*\n)"
    if re.search(topics_pattern, content):
        new_item = f"- [ ] {item}\n"
        content = re.sub(topics_pattern, f"\\1{new_item}", content)
        agenda["path"].write_text(content)
        print(f"Added to {agenda['path'].name}: {item}")
        return True
    else:
        print(f"Could not find Topics section in {agenda['path'].name}")
        return False


def cmd_status():
    """Show status of all agendas."""
    agendas = get_all_agendas()

    if not agendas:
        print("No agendas found in", AGENDAS_DIR)
        return

    print(f"\n{'Agenda':<35} {'Topics':<8} {'Questions':<10} {'Person/Meeting'}")
    print("-" * 80)

    for agenda in sorted(agendas, key=lambda a: a["name"]):
        next_items = parse_next_section(agenda["body"])

        # Count unchecked topics only
        unchecked = sum(1 for t in next_items["topics"] if "[ ]" in t)
        questions = len([q for q in next_items["questions"] if q])

        person = agenda["frontmatter"].get("person", "")
        attendees = agenda["frontmatter"].get("attendees", [])
        label = person if person else f"{len(attendees)} attendees" if attendees else ""

        print(f"{agenda['name']:<35} {unchecked:<8} {questions:<10} {label}")

    print()


def cmd_briefing(name: str):
    """Generate a pre-meeting briefing."""
    agenda = fuzzy_match_agenda(name)
    if not agenda:
        print(f"No agenda found matching '{name}'")
        return

    next_items = parse_next_section(agenda["body"])

    print(f"\n{'='*60}")
    print(f"BRIEFING: {agenda['frontmatter'].get('person', agenda['name'])}")
    print(f"{'='*60}\n")

    if next_items["topics"]:
        print("TOPICS:")
        for topic in next_items["topics"]:
            print(f"  {topic}")
        print()

    if next_items["questions"]:
        print("QUESTIONS:")
        for q in next_items["questions"]:
            if q:
                print(f"  - {q}")
        print()

    if next_items["to_share"]:
        print("TO SHARE:")
        for item in next_items["to_share"]:
            if item:
                print(f"  - {item}")
        print()

    # Show person profile link if available
    person = agenda["frontmatter"].get("person")
    if person:
        profile_name = person.replace(" ", "_") + ".md"
        profile_path = JPT_ROOT / "people" / profile_name
        if profile_path.exists():
            print(f"Profile: {profile_path}")

    print()


def cmd_check():
    """Check for stale items and create notification task."""
    agendas = get_all_agendas()
    stale_items = []
    today = datetime.now()

    for agenda in agendas:
        # Check Waiting For items
        waiting_match = re.search(
            r"### Waiting For\s*\n\|[^\n]+\n\|[-|\s]+\n(.*?)(?=\n### |\n## |\Z)",
            agenda["body"],
            re.DOTALL
        )
        if waiting_match:
            for line in waiting_match.group(1).strip().split("\n"):
                if line.startswith("|"):
                    parts = [p.strip() for p in line.split("|")[1:-1]]
                    if len(parts) >= 2:
                        item, since = parts[0], parts[1]
                        try:
                            since_date = datetime.strptime(since, "%Y-%m-%d")
                            days_old = (today - since_date).days
                            if days_old > 7 and item:
                                stale_items.append({
                                    "agenda": agenda["name"],
                                    "item": item,
                                    "days": days_old
                                })
                        except ValueError:
                            pass

    if stale_items:
        print(f"Found {len(stale_items)} stale items:")
        for item in stale_items:
            print(f"  - [{item['agenda']}] {item['item']} ({item['days']} days)")

        if NOTION_AVAILABLE:
            notes = "\n".join([
                f"- [{i['agenda']}] {i['item']} ({i['days']} days old)"
                for i in stale_items
            ])
            create_task(
                task_name="Stale agenda items need attention",
                source="Agenda Processor",
                notes=notes[:2000]
            )
            print("\nCreated Notion task for stale items")
    else:
        print("No stale items found")


def cmd_add(name: str, item: str):
    """Add an item to an agenda."""
    add_item_to_agenda(name, item)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "status":
        cmd_status()
    elif cmd == "briefing":
        if len(sys.argv) < 3:
            print("Usage: agenda_processor.py briefing <name>")
            sys.exit(1)
        cmd_briefing(sys.argv[2])
    elif cmd == "check":
        cmd_check()
    elif cmd == "add":
        if len(sys.argv) < 4:
            print("Usage: agenda_processor.py add <name> \"topic\"")
            sys.exit(1)
        cmd_add(sys.argv[2], " ".join(sys.argv[3:]))
    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)
        sys.exit(1)
