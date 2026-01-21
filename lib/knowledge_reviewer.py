#!/usr/bin/env python3
"""
Knowledge Reviewer

Weekly agent that reviews knowledge for staleness and structural balance:
- Identifies outdated content for archival
- Checks subfolder balance
- Flags items for human review
- Opens a PR with recommendations

Uses context-aware archival:
- Philosophy/frameworks: Rarely archive (compounds over time)
- News/predictions: Roll up into worldview, archive specifics
- Tool docs: Keep active tools current, archive abandoned
- Trends: Archive when mainstream or dead

Usage:
    python3 knowledge_reviewer.py run        # Run review, create PR
    python3 knowledge_reviewer.py dry-run    # Show what would change
    python3 knowledge_reviewer.py status     # Show staleness report
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime, timedelta
from typing import Optional
from collections import defaultdict

# Paths
JPT_ROOT = Path.home() / "jpt"
KNOWLEDGE_DIR = JPT_ROOT / "knowledge"
KNOWLEDGE_ARCHIVE = KNOWLEDGE_DIR / ".archive"
INBOX_ARCHIVE = JPT_ROOT / "inbox" / ".archive"
LOG_FILE = JPT_ROOT / "lib" / ".curator.log"  # Share log with curator
STATE_FILE = JPT_ROOT / "lib" / ".reviewer_state.json"


def log(message: str):
    """Log a message with timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] [reviewer] {message}"
    print(log_line)
    with open(LOG_FILE, "a") as f:
        f.write(log_line + "\n")


def load_state() -> dict:
    """Load reviewer state."""
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text())
        except Exception:
            pass
    return {}


def save_state(state: dict):
    """Save reviewer state."""
    STATE_FILE.write_text(json.dumps(state, indent=2))


def get_all_knowledge_files() -> list[Path]:
    """Get all markdown files in knowledge directory (recursively)."""
    files = []

    for path in KNOWLEDGE_DIR.rglob("*.md"):
        if ".archive" in str(path) or path.name in ("README.md", ".plan.md"):
            continue
        files.append(path)

    return sorted(files)


def get_recent_inbox_topics(days: int = 180) -> set[str]:
    """Get topics mentioned in recent inbox items."""
    topics = set()
    cutoff = datetime.now() - timedelta(days=days)

    if not INBOX_ARCHIVE.exists():
        return topics

    for file in INBOX_ARCHIVE.iterdir():
        if not file.suffix == ".md":
            continue

        try:
            mtime = datetime.fromtimestamp(file.stat().st_mtime)
            if mtime >= cutoff:
                # Extract keywords from filename
                name = file.stem.lower()
                for word in name.split("-"):
                    if len(word) > 3:
                        topics.add(word)

                # Extract from content (first 500 chars)
                content = file.read_text()[:500].lower()
                for word in ["aws", "django", "python", "ai", "agent", "claude", "llm", "react", "typescript"]:
                    if word in content:
                        topics.add(word)
        except Exception:
            continue

    return topics


def categorize_content(filename: str, content: str) -> str:
    """Categorize content type for staleness rules."""
    name = filename.lower()
    text = content.lower()

    # Philosophy/principles - rarely archive
    if any(word in name or word in text[:500] for word in [
        "philosophy", "principle", "framework", "theory", "ethics",
        "critique", "psychology", "phenomenology", "leadership"
    ]):
        return "philosophy"

    # News/predictions - archive faster
    if any(word in name or word in text[:500] for word in [
        "prediction", "timeline", "2024", "2025", "announce", "release",
        "news", "strategy", "positioning"
    ]):
        return "news"

    # Tool documentation - context dependent
    if any(word in name for word in [
        "tool", "cli", "editor", "app", "browser", "framework"
    ]):
        return "tool"

    # AWS/cloud services - keep if active
    if "aws" in name:
        return "cloud"

    # Default to reference
    return "reference"


def analyze_staleness(files: list[Path], recent_topics: set[str]) -> list[dict]:
    """Analyze files for staleness based on content type and context."""
    now = datetime.now()
    analysis = []

    for file in files:
        try:
            stat = file.stat()
            mtime = datetime.fromtimestamp(stat.st_mtime)
            age_days = (now - mtime).days
            content = file.read_text()

            category = categorize_content(file.name, content)

            # Check if topic is still active in inbox
            name_words = set(file.stem.lower().split("-"))
            topic_active = bool(name_words & recent_topics)

            # Determine staleness based on category
            is_stale = False
            reason = None

            if category == "philosophy":
                # Rarely stale - only if explicitly superseded
                is_stale = False
            elif category == "news":
                # Stale after 6 months, or 3 months if not active
                if age_days > 180 or (age_days > 90 and not topic_active):
                    is_stale = True
                    reason = "News/prediction content, topic no longer active"
            elif category == "tool":
                # Stale after 9 months if not active
                if age_days > 270 and not topic_active:
                    is_stale = True
                    reason = "Tool documentation for inactive topic"
            elif category == "cloud":
                # Keep AWS docs unless very old and inactive
                if age_days > 365 and not topic_active:
                    is_stale = True
                    reason = "Cloud feature doc, no recent activity"
            else:
                # Reference - stale after 12 months if inactive
                if age_days > 365 and not topic_active:
                    is_stale = True
                    reason = "Reference material, no recent activity"

            analysis.append({
                "path": str(file),
                "name": file.name,
                "category": category,
                "age_days": age_days,
                "modified": mtime.strftime("%Y-%m-%d"),
                "topic_active": topic_active,
                "is_stale": is_stale,
                "reason": reason,
                "size": stat.st_size,
                "preview": content[:300]
            })

        except Exception as e:
            log(f"Error analyzing {file}: {e}")

    return analysis


def analyze_structure(files: list[Path]) -> dict:
    """Analyze subfolder structure for balance."""
    structure = defaultdict(list)

    for file in files:
        relative = file.relative_to(KNOWLEDGE_DIR)
        if len(relative.parts) > 1:
            folder = relative.parts[0]
        else:
            folder = "(root)"
        structure[folder].append(file)

    # Calculate balance metrics
    folder_counts = {k: len(v) for k, v in structure.items()}
    total = sum(folder_counts.values())
    avg = total / len(folder_counts) if folder_counts else 0

    imbalanced = []
    for folder, count in folder_counts.items():
        if count > avg * 2.5 and count > 10:
            imbalanced.append({
                "folder": folder,
                "count": count,
                "suggestion": "Consider splitting into subfolders"
            })
        elif count < 3 and folder != "(root)":
            imbalanced.append({
                "folder": folder,
                "count": count,
                "suggestion": "Consider merging with parent or related folder"
            })

    return {
        "folders": dict(structure),
        "counts": folder_counts,
        "total": total,
        "average": avg,
        "imbalanced": imbalanced
    }


def build_review_prompt(staleness: list[dict], structure: dict) -> str:
    """Build the prompt for Claude to analyze and recommend actions."""

    # Build staleness summary
    stale_files = [f for f in staleness if f["is_stale"]]
    by_category = defaultdict(list)
    for f in staleness:
        by_category[f["category"]].append(f)

    staleness_text = f"**Total files**: {len(staleness)}\n"
    staleness_text += f"**Potentially stale**: {len(stale_files)}\n\n"
    staleness_text += "**By category**:\n"
    for cat, files in by_category.items():
        stale_count = sum(1 for f in files if f["is_stale"])
        staleness_text += f"- {cat}: {len(files)} files ({stale_count} potentially stale)\n"

    if stale_files:
        staleness_text += "\n**Potentially stale files**:\n"
        for f in stale_files[:20]:
            staleness_text += f"- `{f['name']}` ({f['category']}, {f['age_days']}d old): {f['reason']}\n"

    # Build structure summary
    structure_text = f"**Folders**: {len(structure['counts'])}\n"
    structure_text += f"**Average files per folder**: {structure['average']:.1f}\n\n"
    structure_text += "**Distribution**:\n"
    for folder, count in sorted(structure['counts'].items(), key=lambda x: -x[1]):
        bar = "█" * min(count // 2, 20)
        structure_text += f"- {folder}: {count} {bar}\n"

    if structure['imbalanced']:
        structure_text += "\n**Balance issues**:\n"
        for issue in structure['imbalanced']:
            structure_text += f"- {issue['folder']}: {issue['count']} files - {issue['suggestion']}\n"

    prompt = f"""You are the Knowledge Reviewer for Jesse's personal knowledge management system.

## Staleness Analysis
{staleness_text}

## Structure Analysis
{structure_text}

## Context-Aware Archival Rules
- **Philosophy/frameworks/principles**: Rarely archive - these compound over time
- **News/predictions**: Roll up insights into worldview, archive the specifics
- **Tool documentation**: Keep if tool is actively used, archive abandoned tools
- **Cloud/AWS features**: Keep if still in use, archive deprecated services
- **Trends**: Archive once the trend is mainstream or dead

## Your Task
Review the analysis and recommend actions. Consider:
1. Which files should be archived (moved to .archive/)?
2. Which files need human review before deciding?
3. Any structural rebalancing needed?

Output JSON in this exact format:

```json
{{
  "summary": "Brief description of the review findings",
  "archive": [
    {{
      "file": "karpathy-agi-timelines.md",
      "reason": "Prediction piece from 2025, now dated"
    }}
  ],
  "needs_review": [
    {{
      "file": "openai-strategy-devday-2025.md",
      "question": "Is this still relevant or should it be archived?"
    }}
  ],
  "structure_recommendations": [
    {{
      "action": "split",
      "folder": "ai",
      "into": ["ai/agents", "ai/tools"],
      "reason": "Folder has 15+ files, natural split between agent patterns and tool docs"
    }}
  ],
  "no_action_reason": "Only if nothing to do - explain why current state is good"
}}
```

Be conservative:
- Only archive things that are clearly outdated, not just old
- Philosophy and frameworks should almost never be archived
- When in doubt, flag for human review instead of archiving
- Structure changes should be significant improvements, not churn

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
    """Move a file to the archive."""
    src = KNOWLEDGE_DIR / file_info["file"]

    # Handle files in subfolders
    if "/" in file_info["file"]:
        # e.g., "ai/agent-architecture.md" -> ".archive/ai/agent-architecture.md"
        dst = KNOWLEDGE_ARCHIVE / file_info["file"]
    else:
        dst = KNOWLEDGE_ARCHIVE / file_info["file"]

    if dry_run:
        log(f"  [DRY-RUN] Would archive: {src} -> {dst}")
        return True

    try:
        dst.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "mv", str(src), str(dst)], cwd=str(JPT_ROOT), check=True)
        log(f"  Archived: {file_info['file']} ({file_info['reason']})")
        return True

    except Exception as e:
        log(f"  ERROR archiving {file_info['file']}: {e}")
        return False


def create_pr(recommendations: dict) -> Optional[str]:
    """Create a git branch, commit changes, and open a PR."""
    today = datetime.now().strftime("%Y-%m-%d")
    branch_name = f"curator/{today}-weekly"

    try:
        # Check if we have changes
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True, text=True, cwd=str(JPT_ROOT)
        )
        if not result.stdout.strip():
            log("No changes to commit")
            return None

        # Create and checkout branch
        subprocess.run(["git", "checkout", "-b", branch_name], cwd=str(JPT_ROOT), check=True)

        # Stage all changes
        subprocess.run(["git", "add", "-A"], cwd=str(JPT_ROOT), check=True)

        # Build commit message
        summary = recommendations.get("summary", "Weekly knowledge review")
        commit_msg = f"""knowledge: {summary}

Automated review by Knowledge Reviewer.

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

        # Build PR body
        pr_body = f"""## Weekly Knowledge Review
{recommendations.get('summary', 'Automated knowledge review')}

## Archived Files
"""

        if recommendations.get("archive"):
            for item in recommendations["archive"]:
                pr_body += f"- `{item['file']}` - {item['reason']}\n"
        else:
            pr_body += "None\n"

        if recommendations.get("needs_review"):
            pr_body += "\n## Needs Human Review\n"
            for item in recommendations["needs_review"]:
                pr_body += f"- `{item['file']}` - {item['question']}\n"

        if recommendations.get("structure_recommendations"):
            pr_body += "\n## Structure Recommendations\n"
            for rec in recommendations["structure_recommendations"]:
                pr_body += f"- **{rec['action']}** `{rec.get('folder', 'N/A')}`: {rec['reason']}\n"

        pr_body += "\n---\n🤖 Generated by Knowledge Reviewer"

        # Create PR
        result = subprocess.run(
            ["gh", "pr", "create", "--title", f"Weekly Knowledge Review: {today}", "--body", pr_body],
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


def run_review(dry_run: bool = False):
    """Run the full review pipeline."""
    log(f"=== Starting Knowledge Review {'(DRY RUN)' if dry_run else ''} ===")

    # Check for pending PRs
    state = load_state()
    if state.get("pending_pr"):
        log(f"Previous reviewer PR still open: {state['pending_pr']}")
        log("Please review and merge/close before running again")
        return

    # Gather data
    files = get_all_knowledge_files()
    log(f"Analyzing {len(files)} knowledge files...")

    recent_topics = get_recent_inbox_topics(180)
    log(f"Found {len(recent_topics)} active topics from recent inbox")

    # Analyze staleness
    staleness = analyze_staleness(files, recent_topics)
    stale_count = sum(1 for f in staleness if f["is_stale"])
    log(f"Staleness analysis: {stale_count} potentially stale files")

    # Analyze structure
    structure = analyze_structure(files)
    log(f"Structure: {len(structure['counts'])} folders, {len(structure['imbalanced'])} imbalanced")

    # Get Claude's recommendations
    prompt = build_review_prompt(staleness, structure)
    log("Asking Claude for review recommendations...")

    response = call_claude(prompt)
    if not response:
        log("Failed to get recommendations from Claude")
        return

    recommendations = parse_recommendations(response)
    if not recommendations:
        log("Failed to parse recommendations")
        return

    # Check if any changes recommended
    has_changes = bool(recommendations.get("archive"))

    if not has_changes:
        log(f"No archival needed: {recommendations.get('no_action_reason', 'Current state is good')}")

        # Still log items needing review
        if recommendations.get("needs_review"):
            log("Files flagged for human review:")
            for item in recommendations["needs_review"]:
                log(f"  - {item['file']}: {item['question']}")

        return

    log(f"Recommendations: {recommendations.get('summary', 'N/A')}")

    # Execute archival
    if recommendations.get("archive"):
        log("Archiving files...")
        for item in recommendations["archive"]:
            execute_archive(item, dry_run)

    # Create PR (unless dry run)
    if not dry_run:
        pr_url = create_pr(recommendations)
        if pr_url:
            state["pending_pr"] = pr_url
            state["last_run"] = datetime.now().isoformat()
            save_state(state)

    log("=== Review Complete ===")


def show_status():
    """Show staleness status report."""
    files = get_all_knowledge_files()
    recent_topics = get_recent_inbox_topics(180)
    staleness = analyze_staleness(files, recent_topics)
    structure = analyze_structure(files)

    print("\nKnowledge Review Status")
    print("=" * 50)

    # By category
    by_category = defaultdict(list)
    for f in staleness:
        by_category[f["category"]].append(f)

    print("\n📊 By Category:")
    for cat, files in sorted(by_category.items(), key=lambda x: -len(x[1])):
        stale = [f for f in files if f["is_stale"]]
        print(f"  {cat}: {len(files)} files ({len(stale)} potentially stale)")

    # Stale files
    stale_files = [f for f in staleness if f["is_stale"]]
    if stale_files:
        print(f"\n⚠️  Potentially Stale ({len(stale_files)}):")
        for f in stale_files[:10]:
            print(f"  - {f['name']} ({f['age_days']}d, {f['category']})")
        if len(stale_files) > 10:
            print(f"  ... and {len(stale_files) - 10} more")

    # Structure
    print("\n📁 Structure:")
    for folder, count in sorted(structure['counts'].items(), key=lambda x: -x[1])[:10]:
        bar = "█" * min(count // 2, 15)
        print(f"  {folder}: {count} {bar}")

    if structure['imbalanced']:
        print("\n⚖️  Balance Issues:")
        for issue in structure['imbalanced']:
            print(f"  - {issue['folder']}: {issue['suggestion']}")

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
        run_review(dry_run=False)
    elif cmd == "dry-run":
        run_review(dry_run=True)
    elif cmd == "status":
        show_status()
    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
