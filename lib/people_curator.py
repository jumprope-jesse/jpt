#!/usr/bin/env python3
"""
People Curator

Weekly agent that reviews and curates the people directory:
- Generates a digest of changes from the past week
- Identifies profiles ready to archive (inactive + sparse)
- Finds potential duplicates to merge (same person, different names)
- Spots renaming opportunities (better name info available)
- Flags inconsistencies across profiles
- Opens a PR for review (uses curator/ branch pattern)

Usage:
    python3 people_curator.py run        # Run curation, create PR
    python3 people_curator.py dry-run    # Show what would change
    python3 people_curator.py status     # Show profile analysis
    python3 people_curator.py digest     # Generate digest only (no PR)
"""

import os
import sys
import json
import subprocess
import re
from pathlib import Path
from datetime import datetime, timedelta
from typing import Optional
from collections import defaultdict

# Paths
JPT_ROOT = Path.home() / "jpt"
PEOPLE_DIR = JPT_ROOT / "people"
PEOPLE_ARCHIVE = PEOPLE_DIR / ".archive"
LOG_FILE = JPT_ROOT / "lib" / ".curator.log"  # Share log with knowledge curator
STATE_FILE = JPT_ROOT / "lib" / ".people_curator_state.json"

# Import notion tasks
sys.path.insert(0, str(JPT_ROOT / "lib"))
try:
    from notion_tasks import create_task
except ImportError:
    create_task = None
    print("WARNING: Could not import notion_tasks, digest creation disabled")


def log(message: str):
    """Log a message with timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] [people] {message}"
    print(log_line)
    with open(LOG_FILE, "a") as f:
        f.write(log_line + "\n")


def load_state() -> dict:
    """Load curator state."""
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text())
        except Exception:
            pass
    return {}


def save_state(state: dict):
    """Save curator state."""
    STATE_FILE.write_text(json.dumps(state, indent=2))


def get_weekly_changes() -> list[dict]:
    """Get files changed in the last 7 days using git."""
    changes = []
    week_ago = datetime.now() - timedelta(days=7)

    try:
        # Get committed changes from last week
        result = subprocess.run(
            ["git", "log", "--since=7 days ago", "--name-status", "--pretty=format:", "--", "people/"],
            capture_output=True, text=True, cwd=str(JPT_ROOT)
        )
        if result.returncode == 0:
            for line in result.stdout.strip().split("\n"):
                if line and "\t" in line:
                    parts = line.split("\t")
                    status = parts[0]
                    filepath = parts[1] if len(parts) > 1 else ""
                    if filepath.startswith("people/") and filepath.endswith(".md"):
                        changes.append({
                            "file": filepath,
                            "status": status,  # A=added, M=modified, D=deleted
                            "name": Path(filepath).stem.replace("_", " ").replace("-", " ")
                        })

        # Get uncommitted changes
        result = subprocess.run(
            ["git", "status", "--porcelain", "--", "people/"],
            capture_output=True, text=True, cwd=str(JPT_ROOT)
        )
        if result.returncode == 0:
            for line in result.stdout.strip().split("\n"):
                if line:
                    status = line[:2].strip()
                    filepath = line[3:].strip()
                    if filepath.startswith("people/") and filepath.endswith(".md"):
                        changes.append({
                            "file": filepath,
                            "status": "M" if "M" in status else ("A" if "?" in status else status),
                            "name": Path(filepath).stem.replace("_", " ").replace("-", " ")
                        })

    except Exception as e:
        log(f"Error getting git changes: {e}")

    # Deduplicate
    seen = set()
    unique = []
    for c in changes:
        if c["file"] not in seen:
            seen.add(c["file"])
            unique.append(c)

    return unique


def get_all_people_files() -> list[Path]:
    """Get all markdown files in people directory."""
    files = []

    for path in PEOPLE_DIR.glob("*.md"):
        if path.name == "README.md":
            continue
        files.append(path)

    return sorted(files)


def parse_profile(file: Path) -> dict:
    """Parse a people profile for analysis."""
    try:
        content = file.read_text()
        stat = file.stat()
        lines = content.split("\n")

        # Extract name from header
        name = file.stem.replace("_", " ").replace("-", " ").title()
        for line in lines[:5]:
            if line.startswith("# "):
                name = line[2:].strip()
                break

        # Extract role/company
        role = ""
        company = ""
        for line in lines:
            if line.startswith("- **Title**:") or line.startswith("- Title:"):
                role = line.split(":", 1)[1].strip().strip("*")
            if line.startswith("- **Company**:") or line.startswith("- Company:"):
                company = line.split(":", 1)[1].strip().strip("*")

        # Count meeting history entries
        meeting_count = 0
        in_meetings = False
        for line in lines:
            if "meeting history" in line.lower():
                in_meetings = True
            elif line.startswith("## "):
                in_meetings = False
            elif in_meetings and line.strip().startswith("- 20"):
                meeting_count += 1

        # Find last meeting date
        last_meeting = None
        meeting_dates = re.findall(r"- (20\d{2}-\d{2}-\d{2})", content)
        if meeting_dates:
            last_meeting = max(meeting_dates)

        # Estimate profile completeness
        non_empty_lines = len([l for l in lines if l.strip() and not l.startswith("#")])
        completeness = "sparse" if non_empty_lines < 15 else "moderate" if non_empty_lines < 40 else "detailed"

        return {
            "path": str(file),
            "filename": file.name,
            "name": name,
            "role": role,
            "company": company,
            "lines": len(lines),
            "non_empty_lines": non_empty_lines,
            "meeting_count": meeting_count,
            "last_meeting": last_meeting,
            "modified": datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d"),
            "completeness": completeness,
            "content_preview": content[:500]
        }

    except Exception as e:
        return {
            "path": str(file),
            "filename": file.name,
            "error": str(e)
        }


def analyze_profiles(profiles: list[dict]) -> dict:
    """Analyze profiles for archival, merging, renaming opportunities."""
    now = datetime.now()
    six_months_ago = (now - timedelta(days=180)).strftime("%Y-%m-%d")
    one_year_ago = (now - timedelta(days=365)).strftime("%Y-%m-%d")

    analysis = {
        "archive_candidates": [],
        "merge_candidates": [],
        "rename_candidates": [],
        "inconsistencies": [],
    }

    # Check for archive candidates
    for p in profiles:
        if p.get("error"):
            continue

        last_meeting = p.get("last_meeting")
        completeness = p.get("completeness", "sparse")

        # Archive if: no meetings in 6+ months AND sparse profile
        # OR no meetings ever AND sparse AND modified over 6 months ago
        if completeness == "sparse":
            if last_meeting and last_meeting < six_months_ago:
                analysis["archive_candidates"].append({
                    "file": p["filename"],
                    "name": p["name"],
                    "reason": f"Sparse profile, last meeting {last_meeting}",
                    "last_meeting": last_meeting
                })
            elif not last_meeting and p.get("modified", "") < six_months_ago:
                analysis["archive_candidates"].append({
                    "file": p["filename"],
                    "name": p["name"],
                    "reason": f"Sparse profile, no meetings recorded, last modified {p.get('modified')}",
                    "last_meeting": None
                })

    # Check for potential duplicates (similar names)
    names = [(p["filename"], p["name"].lower(), p) for p in profiles if not p.get("error")]

    for i, (file1, name1, p1) in enumerate(names):
        for file2, name2, p2 in names[i+1:]:
            # Check for similar names
            similarity = 0

            # Same first name
            first1 = name1.split()[0] if name1.split() else ""
            first2 = name2.split()[0] if name2.split() else ""
            if first1 and first2 and first1 == first2:
                similarity += 0.5

            # Check if one name contains the other
            if name1 in name2 or name2 in name1:
                similarity += 0.3

            # Same company
            if p1.get("company") and p2.get("company") and p1["company"].lower() == p2["company"].lower():
                similarity += 0.2

            # Same role
            if p1.get("role") and p2.get("role") and p1["role"].lower() == p2["role"].lower():
                similarity += 0.1

            if similarity >= 0.5:
                analysis["merge_candidates"].append({
                    "files": [file1, file2],
                    "names": [p1["name"], p2["name"]],
                    "reason": f"Similar names/attributes (score: {similarity:.1f})",
                    "profiles": [p1, p2]
                })

    # Check for renaming opportunities
    for p in profiles:
        if p.get("error"):
            continue

        filename_name = p["filename"].replace(".md", "").replace("_", " ").replace("-", " ").lower()
        header_name = p["name"].lower()

        # If header has more info than filename
        if len(header_name.split()) > len(filename_name.split()):
            analysis["rename_candidates"].append({
                "file": p["filename"],
                "current_name": filename_name,
                "better_name": p["name"],
                "reason": "Header has fuller name than filename"
            })

        # Filename is just first name but header has full name
        if len(filename_name.split()) == 1 and len(header_name.split()) > 1:
            analysis["rename_candidates"].append({
                "file": p["filename"],
                "current_name": filename_name,
                "better_name": p["name"],
                "reason": "Filename is first name only, header has full name"
            })

    return analysis


def generate_digest(changes: list[dict], profiles: list[dict]) -> str:
    """Generate a weekly digest of people changes."""
    now = datetime.now()
    week_start = (now - timedelta(days=7)).strftime("%Y-%m-%d")

    digest = f"""# People Directory Digest
**Week of {week_start} to {now.strftime('%Y-%m-%d')}**

## Summary
- **Total profiles**: {len(profiles)}
- **Changed this week**: {len(changes)}

"""

    if changes:
        digest += "## Changes This Week\n\n"

        added = [c for c in changes if c["status"] == "A"]
        modified = [c for c in changes if c["status"] == "M"]
        deleted = [c for c in changes if c["status"] == "D"]

        if added:
            digest += "### New Profiles\n"
            for c in added:
                digest += f"- **{c['name']}** (`{c['file']}`)\n"
            digest += "\n"

        if modified:
            digest += "### Updated Profiles\n"
            for c in modified:
                digest += f"- {c['name']}\n"
            digest += "\n"

        if deleted:
            digest += "### Removed Profiles\n"
            for c in deleted:
                digest += f"- ~~{c['name']}~~\n"
            digest += "\n"

    else:
        digest += "*No changes to people profiles this week.*\n\n"

    # Add some stats
    by_completeness = defaultdict(int)
    for p in profiles:
        by_completeness[p.get("completeness", "unknown")] += 1

    digest += "## Profile Health\n"
    digest += f"- Detailed: {by_completeness['detailed']}\n"
    digest += f"- Moderate: {by_completeness['moderate']}\n"
    digest += f"- Sparse: {by_completeness['sparse']}\n"

    return digest


def create_digest_task(digest: str) -> bool:
    """Create a Notion task with the digest."""
    if not create_task:
        log("Notion integration not available")
        return False

    now = datetime.now()
    title = f"People Digest - Week of {now.strftime('%Y-%m-%d')}"

    try:
        result = create_task(
            task_name=title,
            source="People Curator",
            notes=digest[:2000],  # Notion limit
            status="Not started"
        )
        if result:
            log(f"Created Notion task: {title}")
            return True
        return False
    except Exception as e:
        log(f"Error creating task: {e}")
        return False


def build_curation_prompt(profiles: list[dict], changes: list[dict], analysis: dict) -> str:
    """Build the prompt for Claude to analyze and recommend curation."""

    # Profile summary
    profile_summary = f"**Total profiles**: {len(profiles)}\n"
    profile_summary += f"**Changed this week**: {len(changes)}\n\n"

    for p in profiles[:30]:  # Sample for context
        if not p.get("error"):
            profile_summary += f"- `{p['filename']}`: {p['name']} ({p.get('role', 'no role')}) - {p['completeness']}, {p.get('meeting_count', 0)} meetings, last: {p.get('last_meeting', 'never')}\n"

    if len(profiles) > 30:
        profile_summary += f"... and {len(profiles) - 30} more\n"

    # Pre-analysis summary
    pre_analysis = ""
    if analysis["archive_candidates"]:
        pre_analysis += "\n**Potential Archive Candidates**:\n"
        for c in analysis["archive_candidates"][:10]:
            pre_analysis += f"- `{c['file']}` ({c['name']}): {c['reason']}\n"

    if analysis["merge_candidates"]:
        pre_analysis += "\n**Potential Duplicates to Merge**:\n"
        for c in analysis["merge_candidates"][:5]:
            pre_analysis += f"- `{c['files'][0]}` + `{c['files'][1]}`: {c['reason']}\n"

    if analysis["rename_candidates"]:
        pre_analysis += "\n**Potential Renames**:\n"
        for c in analysis["rename_candidates"][:10]:
            pre_analysis += f"- `{c['file']}` → `{c['better_name']}`: {c['reason']}\n"

    prompt = f"""You are the People Curator for Jesse's personal knowledge management system.

## Current State
{profile_summary}

## Automated Pre-Analysis
{pre_analysis if pre_analysis else "No obvious issues detected by automated scan."}

## Your Task
Review the profiles and recommend curation actions. Consider:

1. **Archive candidates**: People who are inactive (no meetings in 6+ months) AND have sparse profiles.
   - Don't archive important contacts even if inactive
   - Don't archive if the profile has good reference info worth keeping

2. **Merge candidates**: Same person with different file names (meeting transcription differences)
   - Look for same first name + same company
   - Look for name variations (Bob/Robert, Mike/Michael)

3. **Rename candidates**: Files that could have better names
   - First name only → full name when available
   - Misspellings
   - Inconsistent formatting

4. **Inconsistencies**: Any data quality issues
   - Conflicting info across profiles
   - Formatting inconsistencies

Output JSON in this exact format:

```json
{{
  "summary": "Brief executive summary of the review findings",
  "archive": [
    {{
      "file": "John_Doe.md",
      "reason": "Sparse profile, last interaction over 8 months ago, vendor contact no longer relevant"
    }}
  ],
  "merge": [
    {{
      "keep": "Robert_Smith.md",
      "remove": "Bob_Smith.md",
      "reason": "Same person - Robert is the complete profile"
    }}
  ],
  "rename": [
    {{
      "from": "priscilla.md",
      "to": "Priscilla_Garcia.md",
      "reason": "Header contains full name"
    }}
  ],
  "inconsistencies": [
    {{
      "files": ["person1.md", "person2.md"],
      "issue": "Description of the inconsistency"
    }}
  ],
  "no_action_reason": "Only if no changes needed - explain why current state is good"
}}
```

Be conservative:
- Only archive people who are clearly inactive AND unimportant
- Only merge when you're confident it's the same person
- Renaming is low-risk, be more liberal there
- When unsure, don't include in recommendations

Output ONLY the JSON, no other text."""

    return prompt


def call_claude(prompt: str) -> Optional[str]:
    """Call Claude via happy CLI."""
    happy_bin = Path("/opt/homebrew/bin/happy")

    try:
        result = subprocess.run(
            [str(happy_bin), "--yolo", "--print", prompt],
            capture_output=True,
            text=True,
            timeout=180,
            cwd=str(JPT_ROOT)
        )

        if result.returncode != 0:
            log(f"ERROR: Claude returned non-zero: {result.stderr}")
            return None

        return result.stdout.strip()

    except subprocess.TimeoutExpired:
        log("ERROR: Claude timed out")
        return None
    except Exception as e:
        log(f"ERROR calling Claude: {e}")
        return None


def parse_recommendations(response: str) -> Optional[dict]:
    """Parse Claude's JSON recommendations."""
    try:
        start = response.find("{")
        end = response.rfind("}") + 1
        if start == -1 or end == 0:
            log("ERROR: No JSON found in response")
            return None

        json_str = response[start:end]
        return json.loads(json_str)

    except json.JSONDecodeError as e:
        log(f"ERROR parsing JSON: {e}")
        return None


def execute_archive(file_info: dict, dry_run: bool = False) -> bool:
    """Move a profile to the archive."""
    src = PEOPLE_DIR / file_info["file"]
    dst = PEOPLE_ARCHIVE / file_info["file"]

    if dry_run:
        log(f"  [DRY-RUN] Would archive: {src.name}")
        return True

    try:
        PEOPLE_ARCHIVE.mkdir(exist_ok=True)
        subprocess.run(["git", "mv", str(src), str(dst)], cwd=str(JPT_ROOT), check=True)
        log(f"  Archived: {file_info['file']} ({file_info['reason']})")
        return True

    except Exception as e:
        log(f"  ERROR archiving {file_info['file']}: {e}")
        return False


def execute_merge(merge_info: dict, dry_run: bool = False) -> bool:
    """Merge two profiles (append content from removed to kept, then delete removed)."""
    keep_file = PEOPLE_DIR / merge_info["keep"]
    remove_file = PEOPLE_DIR / merge_info["remove"]

    if dry_run:
        log(f"  [DRY-RUN] Would merge: {remove_file.name} → {keep_file.name}")
        return True

    try:
        if not keep_file.exists() or not remove_file.exists():
            log(f"  ERROR: One of the files doesn't exist")
            return False

        # Append content from removed to kept
        keep_content = keep_file.read_text()
        remove_content = remove_file.read_text()

        merged = keep_content + f"\n\n---\n\n<!-- Merged from {remove_file.name} -->\n\n" + remove_content
        keep_file.write_text(merged)

        # Remove the duplicate
        subprocess.run(["git", "rm", str(remove_file)], cwd=str(JPT_ROOT), check=True)
        subprocess.run(["git", "add", str(keep_file)], cwd=str(JPT_ROOT), check=True)

        log(f"  Merged: {remove_file.name} → {keep_file.name}")
        return True

    except Exception as e:
        log(f"  ERROR merging: {e}")
        return False


def execute_rename(rename_info: dict, dry_run: bool = False) -> bool:
    """Rename a profile file."""
    src = PEOPLE_DIR / rename_info["from"]
    # Sanitize the new name
    new_name = rename_info["to"].replace(" ", "_")
    if not new_name.endswith(".md"):
        new_name += ".md"
    dst = PEOPLE_DIR / new_name

    if dry_run:
        log(f"  [DRY-RUN] Would rename: {src.name} → {new_name}")
        return True

    try:
        subprocess.run(["git", "mv", str(src), str(dst)], cwd=str(JPT_ROOT), check=True)
        log(f"  Renamed: {src.name} → {new_name}")
        return True

    except Exception as e:
        log(f"  ERROR renaming: {e}")
        return False


def create_pr(recommendations: dict, digest: str) -> Optional[str]:
    """Create a git branch, commit changes, and open a PR."""
    today = datetime.now().strftime("%Y-%m-%d")
    branch_name = f"curator/{today}-people"

    try:
        # Check if we have changes
        result = subprocess.run(
            ["git", "status", "--porcelain", "--", "people/"],
            capture_output=True, text=True, cwd=str(JPT_ROOT)
        )
        if not result.stdout.strip():
            log("No changes to commit")
            return None

        # Create and checkout branch
        subprocess.run(["git", "checkout", "-b", branch_name], cwd=str(JPT_ROOT), check=True)

        # Stage all changes
        subprocess.run(["git", "add", "-A", "people/"], cwd=str(JPT_ROOT), check=True)

        # Build commit message
        summary = recommendations.get("summary", "Weekly people directory curation")
        commit_msg = f"""people: {summary}

Automated curation by People Curator.

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"""

        subprocess.run(
            ["git", "commit", "-m", commit_msg],
            cwd=str(JPT_ROOT), check=True
        )

        # Push branch
        subprocess.run(
            ["git", "push", "-u", "origin", branch_name],
            cwd=str(JPT_ROOT), check=True
        )

        # Build PR body with executive summary
        pr_body = f"""## Executive Summary
{recommendations.get('summary', 'Weekly people directory review and curation.')}

## This Week's Digest
{digest[:1500]}

## Changes
"""

        if recommendations.get("archive"):
            pr_body += "\n### Archived Profiles\n"
            for item in recommendations["archive"]:
                pr_body += f"- `{item['file']}` - {item['reason']}\n"

        if recommendations.get("merge"):
            pr_body += "\n### Merged Profiles\n"
            for item in recommendations["merge"]:
                pr_body += f"- `{item['remove']}` → `{item['keep']}` - {item['reason']}\n"

        if recommendations.get("rename"):
            pr_body += "\n### Renamed Profiles\n"
            for item in recommendations["rename"]:
                pr_body += f"- `{item['from']}` → `{item['to']}` - {item['reason']}\n"

        if recommendations.get("inconsistencies"):
            pr_body += "\n### Inconsistencies Found\n"
            for item in recommendations["inconsistencies"]:
                pr_body += f"- {', '.join(item['files'])}: {item['issue']}\n"

        if not any([recommendations.get("archive"), recommendations.get("merge"),
                    recommendations.get("rename"), recommendations.get("inconsistencies")]):
            pr_body += "\n*No structural changes recommended. Profiles are in good shape!*\n"

        pr_body += "\n---\n🤖 Generated by People Curator"

        # Create PR
        result = subprocess.run(
            ["gh", "pr", "create", "--title", f"People Curation: {today}", "--body", pr_body],
            capture_output=True, text=True, cwd=str(JPT_ROOT)
        )

        if result.returncode == 0:
            pr_url = result.stdout.strip()
            log(f"Created PR: {pr_url}")

            # Switch back to main
            subprocess.run(["git", "checkout", "main"], cwd=str(JPT_ROOT))

            return pr_url
        else:
            log(f"ERROR creating PR: {result.stderr}")
            subprocess.run(["git", "checkout", "main"], cwd=str(JPT_ROOT))
            return None

    except Exception as e:
        log(f"ERROR in PR creation: {e}")
        subprocess.run(["git", "checkout", "main"], cwd=str(JPT_ROOT), capture_output=True)
        return None


def run_curation(dry_run: bool = False):
    """Run the full curation pipeline."""
    log(f"=== Starting People Curation {'(DRY RUN)' if dry_run else ''} ===")

    # Check for pending PRs
    state = load_state()
    if state.get("pending_pr"):
        log(f"Previous people curator PR still open: {state['pending_pr']}")
        log("Please review and merge/close before running again")
        return

    # Gather data
    files = get_all_people_files()
    log(f"Found {len(files)} people profiles")

    profiles = [parse_profile(f) for f in files]
    changes = get_weekly_changes()
    log(f"Changes this week: {len(changes)} files")

    # Generate digest
    digest = generate_digest(changes, profiles)
    log("Generated weekly digest")

    # Create Notion task with digest
    if not dry_run:
        create_digest_task(digest)

    # Run pre-analysis
    analysis = analyze_profiles(profiles)
    log(f"Pre-analysis: {len(analysis['archive_candidates'])} archive candidates, "
        f"{len(analysis['merge_candidates'])} merge candidates, "
        f"{len(analysis['rename_candidates'])} rename candidates")

    # Get Claude's recommendations
    prompt = build_curation_prompt(profiles, changes, analysis)
    log("Asking Claude for curation recommendations...")

    response = call_claude(prompt)
    if not response:
        log("Failed to get recommendations from Claude")
        return

    recommendations = parse_recommendations(response)
    if not recommendations:
        log("Failed to parse recommendations")
        return

    # Check if any changes recommended
    has_changes = (
        recommendations.get("archive") or
        recommendations.get("merge") or
        recommendations.get("rename")
    )

    if not has_changes:
        log(f"No changes recommended: {recommendations.get('no_action_reason', 'Current state is good')}")

        if recommendations.get("inconsistencies"):
            log("Inconsistencies found (no action taken):")
            for item in recommendations["inconsistencies"]:
                log(f"  - {item['issue']}")

        return

    log(f"Recommendations: {recommendations.get('summary', 'N/A')}")

    # Execute changes
    if recommendations.get("archive"):
        log("Archiving profiles...")
        for item in recommendations["archive"]:
            execute_archive(item, dry_run)

    if recommendations.get("merge"):
        log("Merging profiles...")
        for item in recommendations["merge"]:
            execute_merge(item, dry_run)

    if recommendations.get("rename"):
        log("Renaming profiles...")
        for item in recommendations["rename"]:
            execute_rename(item, dry_run)

    # Create PR (unless dry run)
    if not dry_run:
        pr_url = create_pr(recommendations, digest)
        if pr_url:
            state["pending_pr"] = pr_url
            state["last_run"] = datetime.now().isoformat()
            save_state(state)

    log("=== People Curation Complete ===")


def run_digest_only():
    """Generate and post digest without making changes."""
    log("=== Generating People Digest ===")

    files = get_all_people_files()
    profiles = [parse_profile(f) for f in files]
    changes = get_weekly_changes()

    digest = generate_digest(changes, profiles)
    print(digest)

    create_digest_task(digest)

    log("=== Digest Complete ===")


def show_status():
    """Show profile analysis status."""
    files = get_all_people_files()
    profiles = [parse_profile(f) for f in files]
    changes = get_weekly_changes()
    analysis = analyze_profiles(profiles)

    print("\nPeople Directory Status")
    print("=" * 50)

    print(f"\n📊 Overview:")
    print(f"  Total profiles: {len(profiles)}")
    print(f"  Changed this week: {len(changes)}")

    # By completeness
    by_completeness = defaultdict(int)
    for p in profiles:
        by_completeness[p.get("completeness", "unknown")] += 1

    print(f"\n📈 Profile Completeness:")
    print(f"  Detailed: {by_completeness['detailed']}")
    print(f"  Moderate: {by_completeness['moderate']}")
    print(f"  Sparse: {by_completeness['sparse']}")

    if analysis["archive_candidates"]:
        print(f"\n📦 Archive Candidates ({len(analysis['archive_candidates'])}):")
        for c in analysis["archive_candidates"][:5]:
            print(f"  - {c['name']}: {c['reason']}")
        if len(analysis["archive_candidates"]) > 5:
            print(f"  ... and {len(analysis['archive_candidates']) - 5} more")

    if analysis["merge_candidates"]:
        print(f"\n🔀 Potential Duplicates ({len(analysis['merge_candidates'])}):")
        for c in analysis["merge_candidates"][:3]:
            print(f"  - {c['names'][0]} + {c['names'][1]}")

    if analysis["rename_candidates"]:
        print(f"\n✏️  Rename Candidates ({len(analysis['rename_candidates'])}):")
        for c in analysis["rename_candidates"][:5]:
            print(f"  - {c['file']} → {c['better_name']}")

    # Recent changes
    if changes:
        print(f"\n📝 This Week's Changes:")
        for c in changes[:10]:
            status_emoji = "➕" if c["status"] == "A" else "📝" if c["status"] == "M" else "❌"
            print(f"  {status_emoji} {c['name']}")

    # State
    state = load_state()
    if state.get("pending_pr"):
        print(f"\n⚠️  Pending PR: {state['pending_pr']}")
    if state.get("last_run"):
        print(f"Last run: {state['last_run']}")

    print()


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1].lower()

    if cmd == "run":
        run_curation(dry_run=False)
    elif cmd == "dry-run":
        run_curation(dry_run=True)
    elif cmd == "status":
        show_status()
    elif cmd == "digest":
        run_digest_only()
    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
