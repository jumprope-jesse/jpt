#!/usr/bin/env python3
"""
Knowledge Curator

Nightly agent that organizes the knowledge directory:
- Creates subfolders when topic clusters reach 5+ files
- Merges related small files into cohesive topics
- Moves files into appropriate subfolders
- Opens a PR for human review

Usage:
    python3 knowledge_curator.py run        # Run curation, create PR
    python3 knowledge_curator.py dry-run    # Show what would change
    python3 knowledge_curator.py status     # Show current clusters
    python3 knowledge_curator.py analyze    # Deep analysis without changes
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
LOG_FILE = JPT_ROOT / "lib" / ".curator.log"
STATE_FILE = JPT_ROOT / "lib" / ".curator_state.json"

# Configuration
SUBFOLDER_THRESHOLD = 5  # Minimum files to create a subfolder
MAX_NESTING_DEPTH = 2    # e.g., knowledge/ai/agents/ but no deeper


def log(message: str):
    """Log a message with timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] {message}"
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


def get_recent_changes(hours: int = 24) -> list[str]:
    """Get files changed in the last N hours using git."""
    changes = []

    try:
        # Get committed changes
        result = subprocess.run(
            ["git", "log", f"--since={hours} hours ago", "--name-only", "--pretty=format:", "--", "knowledge/"],
            capture_output=True, text=True, cwd=str(JPT_ROOT)
        )
        if result.returncode == 0:
            for line in result.stdout.strip().split("\n"):
                if line and line.startswith("knowledge/"):
                    changes.append(line)

        # Get uncommitted changes
        result = subprocess.run(
            ["git", "status", "--porcelain", "--", "knowledge/"],
            capture_output=True, text=True, cwd=str(JPT_ROOT)
        )
        if result.returncode == 0:
            for line in result.stdout.strip().split("\n"):
                if line:
                    # Format: " M knowledge/file.md" or "?? knowledge/file.md"
                    parts = line.split()
                    if len(parts) >= 2 and parts[-1].startswith("knowledge/"):
                        changes.append(parts[-1])

    except Exception as e:
        log(f"Error getting git changes: {e}")

    return list(set(changes))


def get_all_knowledge_files() -> list[Path]:
    """Get all markdown files in knowledge directory (recursively)."""
    files = []

    for path in KNOWLEDGE_DIR.rglob("*.md"):
        # Skip archive, README, and plan files
        if ".archive" in str(path) or path.name in ("README.md", ".plan.md"):
            continue
        files.append(path)

    return sorted(files)


def extract_topic_prefix(filename: str) -> str:
    """Extract the topic prefix from a filename."""
    # Remove .md extension
    name = filename.replace(".md", "")

    # Split on hyphens and take first part(s)
    parts = name.split("-")

    # Common multi-word prefixes
    multi_prefixes = {
        ("ai", "agent"): "ai",
        ("ai", "coding"): "ai",
        ("ai", "pdf"): "ai",
        ("ai", "safety"): "ai",
        ("ai", "automation"): "ai",
        ("ai", "fluency"): "ai",
        ("ai", "pkm"): "ai",
        ("ai", "image"): "ai",
        ("ai", "therapeutic"): "ai",
        ("ai", "audience"): "ai",
        ("ai", "information"): "ai",
        ("ai", "verification"): "ai",
        ("ai", "elements"): "ai",
        ("aws", "lambda"): "aws",
        ("aws", "aurora"): "aws",
        ("aws", "xray"): "aws",
        ("aws", "waf"): "aws",
        ("aws", "q"): "aws",
        ("aws", "ses"): "aws",
        ("aws", "mwaa"): "aws",
        ("aws", "arc"): "aws",
        ("aws", "sqs"): "aws",
        ("aws", "verified"): "aws",
        ("aws", "backup"): "aws",
        ("aws", "zero"): "aws",
        ("aws", "quicksuite"): "aws",
        ("aws", "ai"): "aws",
        ("django", "watchfiles"): "django",
        ("django", "chronos"): "django",
        ("django", "remake"): "django",
        ("django", "generic"): "django",
        ("django", "reliable"): "django",
        ("django", "wtf"): "django",
        ("mac", "productivity"): "tools",
        ("python", "type"): "python",
    }

    # Check for known multi-word prefixes
    if len(parts) >= 2:
        key = (parts[0].lower(), parts[1].lower())
        if key in multi_prefixes:
            return multi_prefixes[key]

    # Default to first part
    return parts[0].lower() if parts else "misc"


def analyze_clusters() -> dict[str, list[Path]]:
    """Analyze files and group them by topic cluster."""
    clusters = defaultdict(list)

    for file in get_all_knowledge_files():
        # Determine if file is already in a subfolder
        relative = file.relative_to(KNOWLEDGE_DIR)
        if len(relative.parts) > 1:
            # Already in subfolder - use folder name as cluster
            cluster = relative.parts[0]
        else:
            # In root - extract prefix from filename
            cluster = extract_topic_prefix(file.name)

        clusters[cluster].append(file)

    return dict(clusters)


def get_file_info(file: Path) -> dict:
    """Get metadata about a knowledge file."""
    try:
        stat = file.stat()
        content = file.read_text()
        lines = content.split("\n")

        # Extract title (first # line)
        title = file.stem.replace("-", " ").title()
        for line in lines[:10]:
            if line.startswith("# "):
                title = line[2:].strip()
                break

        return {
            "path": str(file),
            "name": file.name,
            "title": title,
            "size": stat.st_size,
            "lines": len(lines),
            "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
            "preview": content[:500] if content else ""
        }
    except Exception as e:
        return {"path": str(file), "name": file.name, "error": str(e)}


def build_curation_prompt(clusters: dict, recent_changes: list[str]) -> str:
    """Build the prompt for Claude to analyze and recommend curation."""

    # Build cluster summary
    cluster_info = []
    for cluster, files in sorted(clusters.items(), key=lambda x: -len(x[1])):
        file_list = [f.name for f in files]
        cluster_info.append(f"**{cluster}** ({len(files)} files):\n  - " + "\n  - ".join(file_list[:15]))
        if len(files) > 15:
            cluster_info[-1] += f"\n  - ... and {len(files) - 15} more"

    clusters_text = "\n\n".join(cluster_info)

    # Recent changes
    changes_text = "\n".join(f"- {c}" for c in recent_changes) if recent_changes else "No recent changes"

    prompt = f"""You are the Knowledge Curator for Jesse's personal knowledge management system.

## Current State
- **Total files**: {sum(len(f) for f in clusters.values())}
- **Clusters**: {len(clusters)}
- **Recent changes**: {len(recent_changes)} files

## Cluster Analysis
{clusters_text}

## Recent Changes (last 24h)
{changes_text}

## Rules
1. **Subfolder threshold**: Create a subfolder when a cluster has 5+ files
2. **Max depth**: 2 levels max (e.g., knowledge/ai/agents/ but no deeper)
3. **Merging**: Combine 2-3 small related files into one cohesive topic (semi-aggressive)
4. **Naming**: Use lowercase kebab-case for folders and files
5. **Preserve sources**: When merging, keep all source URLs and dates

## Your Task
Analyze the clusters and recommend curation actions. Output JSON in this exact format:

```json
{{
  "summary": "Brief description of recommended changes",
  "create_folders": [
    {{
      "path": "knowledge/aws",
      "description": "AWS services and features",
      "files_to_move": ["aws-lambda-snapstart.md", "aws-ses-email-validation.md", ...]
    }}
  ],
  "merge_files": [
    {{
      "target": "knowledge/python-type-checkers.md",
      "sources": ["pyrefly-python-type-checker.md", "ty-python-type-checker.md"],
      "reason": "Both cover Python type checkers, can be unified"
    }}
  ],
  "move_files": [
    {{
      "from": "knowledge/ai-agent-architecture.md",
      "to": "knowledge/ai/agent-architecture.md",
      "reason": "Fits in ai subfolder"
    }}
  ],
  "no_action_reason": "Only if no changes recommended - explain why"
}}
```

Be thoughtful:
- Don't create folders just because you can - only when it meaningfully improves organization
- Merging should combine truly related content, not just similar names
- Consider if the current flat structure is actually fine for smaller clusters
- If no changes are needed, say so and explain why

Output ONLY the JSON, no other text."""

    return prompt


def call_claude(prompt: str) -> Optional[str]:
    """Call Claude via happy CLI."""
    happy_bin = Path.home() / "Library/pnpm/happy"

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
        # Extract JSON from response (in case there's extra text)
        start = response.find("{")
        end = response.rfind("}") + 1
        if start == -1 or end == 0:
            log("ERROR: No JSON found in response")
            return None

        json_str = response[start:end]
        return json.loads(json_str)

    except json.JSONDecodeError as e:
        log(f"ERROR parsing JSON: {e}")
        log(f"Response was: {response[:500]}")
        return None


def execute_folder_creation(folder_info: dict, dry_run: bool = False) -> bool:
    """Create a subfolder and move files into it."""
    folder_path = JPT_ROOT / folder_info["path"]

    if dry_run:
        log(f"  [DRY-RUN] Would create folder: {folder_path}")
        for f in folder_info.get("files_to_move", []):
            log(f"    Would move: {f}")
        return True

    try:
        folder_path.mkdir(parents=True, exist_ok=True)

        # Create README for the subfolder
        readme_path = folder_path / "README.md"
        if not readme_path.exists():
            readme_content = f"# {folder_path.name.replace('-', ' ').title()}\n\n{folder_info.get('description', '')}\n"
            readme_path.write_text(readme_content)
            log(f"  Created {readme_path}")

        # Move files
        for filename in folder_info.get("files_to_move", []):
            src = KNOWLEDGE_DIR / filename
            if src.exists():
                dst = folder_path / filename
                subprocess.run(["git", "mv", str(src), str(dst)], cwd=str(JPT_ROOT), check=True)
                log(f"  Moved {filename} -> {folder_path.name}/")

        return True

    except Exception as e:
        log(f"  ERROR creating folder: {e}")
        return False


def execute_merge(merge_info: dict, dry_run: bool = False) -> bool:
    """Merge multiple files into one."""
    target_path = JPT_ROOT / merge_info["target"]
    sources = merge_info["sources"]

    if dry_run:
        log(f"  [DRY-RUN] Would merge into: {target_path}")
        for s in sources:
            log(f"    Source: {s}")
        return True

    try:
        # Read all source files
        combined_content = []
        for src_name in sources:
            src_path = KNOWLEDGE_DIR / src_name
            if src_path.exists():
                content = src_path.read_text()
                combined_content.append(f"<!-- Source: {src_name} -->\n{content}")

        if not combined_content:
            log(f"  ERROR: No source files found for merge")
            return False

        # Write combined content
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_text("\n\n---\n\n".join(combined_content))
        log(f"  Created merged file: {target_path}")

        # Remove source files
        for src_name in sources:
            src_path = KNOWLEDGE_DIR / src_name
            if src_path.exists():
                subprocess.run(["git", "rm", str(src_path)], cwd=str(JPT_ROOT), check=True)
                log(f"  Removed: {src_name}")

        # Add the new file
        subprocess.run(["git", "add", str(target_path)], cwd=str(JPT_ROOT), check=True)

        return True

    except Exception as e:
        log(f"  ERROR merging files: {e}")
        return False


def execute_move(move_info: dict, dry_run: bool = False) -> bool:
    """Move a file to a new location."""
    src = JPT_ROOT / move_info["from"]
    dst = JPT_ROOT / move_info["to"]

    if dry_run:
        log(f"  [DRY-RUN] Would move: {src} -> {dst}")
        return True

    try:
        dst.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "mv", str(src), str(dst)], cwd=str(JPT_ROOT), check=True)
        log(f"  Moved: {move_info['from']} -> {move_info['to']}")
        return True

    except Exception as e:
        log(f"  ERROR moving file: {e}")
        return False


def create_pr(recommendations: dict) -> Optional[str]:
    """Create a git branch, commit changes, and open a PR."""
    today = datetime.now().strftime("%Y-%m-%d")
    branch_name = f"curator/{today}-nightly"

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
        summary = recommendations.get("summary", "Nightly knowledge curation")
        commit_msg = f"""knowledge: {summary}

Automated curation by Knowledge Curator.

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
        pr_body = f"""## Summary
{recommendations.get('summary', 'Automated knowledge curation')}

## Changes
"""

        if recommendations.get("create_folders"):
            pr_body += "\n### New Subfolders\n"
            for folder in recommendations["create_folders"]:
                pr_body += f"- `{folder['path']}/` - {folder.get('description', '')} ({len(folder.get('files_to_move', []))} files)\n"

        if recommendations.get("merge_files"):
            pr_body += "\n### Merged Files\n"
            for merge in recommendations["merge_files"]:
                sources = " + ".join(f"`{s}`" for s in merge["sources"])
                pr_body += f"- {sources} → `{merge['target']}`\n"

        if recommendations.get("move_files"):
            pr_body += "\n### Moved Files\n"
            for move in recommendations["move_files"]:
                pr_body += f"- `{move['from']}` → `{move['to']}`\n"

        pr_body += "\n---\n🤖 Generated by Knowledge Curator"

        # Create PR
        result = subprocess.run(
            ["gh", "pr", "create", "--title", f"Knowledge Curation: {today}", "--body", pr_body],
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
        # Try to get back to main
        subprocess.run(["git", "checkout", "main"], cwd=str(JPT_ROOT), capture_output=True)
        return None


def run_curation(dry_run: bool = False):
    """Run the full curation pipeline."""
    log(f"=== Starting Knowledge Curation {'(DRY RUN)' if dry_run else ''} ===")

    # Check for pending PRs from previous runs
    state = load_state()
    if state.get("pending_pr"):
        log(f"Previous curator PR still open: {state['pending_pr']}")
        log("Please review and merge/close before running again")
        return

    # Analyze current state
    recent_changes = get_recent_changes(24)
    log(f"Recent changes: {len(recent_changes)} files")

    clusters = analyze_clusters()
    log(f"Found {len(clusters)} topic clusters across {sum(len(f) for f in clusters.values())} files")

    # Get Claude's recommendations
    prompt = build_curation_prompt(clusters, recent_changes)
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
        recommendations.get("create_folders") or
        recommendations.get("merge_files") or
        recommendations.get("move_files")
    )

    if not has_changes:
        log(f"No changes recommended: {recommendations.get('no_action_reason', 'unknown')}")
        return

    log(f"Recommendations: {recommendations.get('summary', 'N/A')}")

    # Execute changes
    if recommendations.get("create_folders"):
        log("Creating folders...")
        for folder in recommendations["create_folders"]:
            execute_folder_creation(folder, dry_run)

    if recommendations.get("merge_files"):
        log("Merging files...")
        for merge in recommendations["merge_files"]:
            execute_merge(merge, dry_run)

    if recommendations.get("move_files"):
        log("Moving files...")
        for move in recommendations["move_files"]:
            execute_move(move, dry_run)

    # Create PR (unless dry run)
    if not dry_run:
        pr_url = create_pr(recommendations)
        if pr_url:
            state["pending_pr"] = pr_url
            state["last_run"] = datetime.now().isoformat()
            save_state(state)

    log("=== Curation Complete ===")


def show_status():
    """Show current cluster status."""
    clusters = analyze_clusters()

    print("\nKnowledge Cluster Analysis")
    print("=" * 50)

    for cluster, files in sorted(clusters.items(), key=lambda x: -len(x[1])):
        status = "📁" if len(files) >= SUBFOLDER_THRESHOLD else "📄"
        print(f"\n{status} {cluster} ({len(files)} files)")
        for f in files[:5]:
            print(f"   - {f.name}")
        if len(files) > 5:
            print(f"   ... and {len(files) - 5} more")

    print(f"\nTotal: {sum(len(f) for f in clusters.values())} files in {len(clusters)} clusters")
    print(f"Subfolder candidates (≥{SUBFOLDER_THRESHOLD} files): {sum(1 for f in clusters.values() if len(f) >= SUBFOLDER_THRESHOLD)}")

    # Show state
    state = load_state()
    if state.get("pending_pr"):
        print(f"\n⚠️  Pending PR: {state['pending_pr']}")
    if state.get("last_run"):
        print(f"Last run: {state['last_run']}")


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
    elif cmd == "analyze":
        # Deep analysis without changes
        clusters = analyze_clusters()
        recent = get_recent_changes(24)
        prompt = build_curation_prompt(clusters, recent)
        print(prompt)
    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
