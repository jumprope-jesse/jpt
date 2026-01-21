#!/usr/bin/env python3
"""
Granola Meeting Transcript Extractor

Extracts meeting transcripts and summaries from Granola's local cache
and saves them as markdown files.

Usage:
    python extract_granola.py                    # Extract all meetings
    python extract_granola.py --recent 7         # Extract meetings from last 7 days
    python extract_granola.py --list             # List available meetings
    python extract_granola.py --id <doc_id>      # Extract specific meeting by ID
"""
from __future__ import annotations

import json
import os
import re
import argparse
import subprocess
import gzip
import urllib.request
import urllib.error
from datetime import datetime, timedelta
from pathlib import Path


# Granola paths
GRANOLA_CACHE = Path.home() / "Library/Application Support/Granola/cache-v3.json"
GRANOLA_TOKENS = Path.home() / "Library/Application Support/Granola/supabase.json"

# API configuration
GRANOLA_API_BASE = "https://api.granola.ai"
WORKOS_AUTH_URL = "https://api.workos.com/user_management/authenticate"
GRANOLA_CLIENT_ID = "client_01JZJ0XBDAT8PHJWQY09Y0VD61"  # From auth flow
API_HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "User-Agent": "Granola/5.354.0",
    "X-Client-Version": "5.354.0",
}

# Minimum transcript word count to consider "complete"
MIN_TRANSCRIPT_WORDS = 50

# Output directory (same folder as this script by default)
OUTPUT_DIR = Path(__file__).parent

# Post-processing prompt file
POST_MEETING_PROMPT = OUTPUT_DIR / "post_meeting_prompt.md"


# ============================================================================
# Granola API Client
# ============================================================================

class GranolaAPIClient:
    """Client for Granola's API with automatic token refresh."""

    def __init__(self, quiet: bool = False):
        self.quiet = quiet
        self.access_token = None
        self.refresh_token = None
        self.token_expiry = None
        self._load_tokens()

    def _load_tokens(self):
        """Load tokens from Granola's local storage."""
        if not GRANOLA_TOKENS.exists():
            return

        try:
            with open(GRANOLA_TOKENS, 'r') as f:
                data = json.load(f)

            workos_tokens = json.loads(data.get('workos_tokens', '{}'))
            self.access_token = workos_tokens.get('access_token')
            self.refresh_token = workos_tokens.get('refresh_token')

            # Calculate expiry from obtained_at + expires_in
            obtained_at = workos_tokens.get('obtained_at', 0)
            expires_in = workos_tokens.get('expires_in', 0)
            if obtained_at and expires_in:
                expiry_ms = obtained_at + (expires_in * 1000)
                self.token_expiry = datetime.fromtimestamp(expiry_ms / 1000)
        except Exception as e:
            if not self.quiet:
                print(f"  ⚠ Could not load Granola tokens: {e}")

    def _save_tokens(self):
        """Save updated tokens back to Granola's storage."""
        if not GRANOLA_TOKENS.exists():
            return

        try:
            with open(GRANOLA_TOKENS, 'r') as f:
                data = json.load(f)

            workos_tokens = json.loads(data.get('workos_tokens', '{}'))
            workos_tokens['access_token'] = self.access_token
            workos_tokens['refresh_token'] = self.refresh_token
            workos_tokens['obtained_at'] = int(datetime.now().timestamp() * 1000)
            workos_tokens['expires_in'] = 21600  # 6 hours typical

            data['workos_tokens'] = json.dumps(workos_tokens)

            with open(GRANOLA_TOKENS, 'w') as f:
                json.dump(data, f)
        except Exception as e:
            if not self.quiet:
                print(f"  ⚠ Could not save Granola tokens: {e}")

    def _is_token_expired(self) -> bool:
        """Check if access token is expired or about to expire."""
        if not self.access_token or not self.token_expiry:
            return True
        # Add 5 minute buffer
        return datetime.now() > (self.token_expiry - timedelta(minutes=5))

    def _refresh_access_token(self) -> bool:
        """Refresh the access token using WorkOS."""
        if not self.refresh_token:
            return False

        try:
            payload = json.dumps({
                "client_id": GRANOLA_CLIENT_ID,
                "grant_type": "refresh_token",
                "refresh_token": self.refresh_token,
            }).encode('utf-8')

            req = urllib.request.Request(
                WORKOS_AUTH_URL,
                data=payload,
                headers={"Content-Type": "application/json"},
                method='POST'
            )

            with urllib.request.urlopen(req, timeout=30) as response:
                if response.status != 200:
                    if not self.quiet:
                        print(f"  ⚠ Token refresh failed: {response.status}")
                    return False

                data = json.loads(response.read().decode('utf-8'))

            self.access_token = data.get('access_token')
            expires_in = data.get('expires_in', 21600)
            self.token_expiry = datetime.now() + timedelta(seconds=expires_in)

            # Handle refresh token rotation
            new_refresh = data.get('refresh_token')
            if new_refresh and new_refresh != self.refresh_token:
                self.refresh_token = new_refresh
                if not self.quiet:
                    print("  ↻ Refresh token rotated")

            self._save_tokens()
            return True

        except urllib.error.HTTPError as e:
            if not self.quiet:
                print(f"  ⚠ Token refresh failed: {e.code}")
            return False
        except Exception as e:
            if not self.quiet:
                print(f"  ⚠ Token refresh error: {e}")
            return False

    def _get_valid_token(self) -> str | None:
        """Get a valid access token, refreshing if necessary."""
        if self._is_token_expired():
            if not self._refresh_access_token():
                return None
        return self.access_token

    def _decode_response(self, response) -> dict:
        """Decode API response, handling gzip compression."""
        raw_data = response.read()
        # Check for gzip magic bytes
        if raw_data[:2] == b'\x1f\x8b':
            raw_data = gzip.decompress(raw_data)
        return json.loads(raw_data.decode('utf-8'))

    def _api_request(self, endpoint: str, payload: dict) -> dict | None:
        """Make an authenticated API request."""
        token = self._get_valid_token()
        if not token:
            return None

        headers = {**API_HEADERS, "Authorization": f"Bearer {token}"}
        url = f"{GRANOLA_API_BASE}{endpoint}"
        data = json.dumps(payload).encode('utf-8')

        try:
            req = urllib.request.Request(url, data=data, headers=headers, method='POST')

            try:
                with urllib.request.urlopen(req, timeout=60) as response:
                    return self._decode_response(response)
            except urllib.error.HTTPError as e:
                if e.code == 401:
                    # Token might have been invalidated, try refresh
                    if self._refresh_access_token():
                        headers["Authorization"] = f"Bearer {self.access_token}"
                        req = urllib.request.Request(url, data=data, headers=headers, method='POST')
                        with urllib.request.urlopen(req, timeout=60) as response:
                            return self._decode_response(response)
                if not self.quiet:
                    print(f"  ⚠ API error {e.code}: {endpoint}")
                return None

        except Exception as e:
            if not self.quiet:
                print(f"  ⚠ API request failed: {e}")
            return None

    def is_available(self) -> bool:
        """Check if API client has valid credentials."""
        return self.access_token is not None and self.refresh_token is not None

    def get_document_transcript(self, doc_id: str) -> list | None:
        """Fetch full transcript for a document from API."""
        result = self._api_request("/v1/get-document-transcript", {"document_id": doc_id})
        if result and 'transcript' in result:
            return result['transcript']
        return None

    def get_document(self, doc_id: str) -> dict | None:
        """Fetch a single document with full content from API."""
        result = self._api_request("/v1/get-documents-batch", {"document_ids": [doc_id]})
        if result and 'documents' in result and len(result['documents']) > 0:
            return result['documents'][0]
        return None

    def get_recent_documents(self, limit: int = 50) -> list | None:
        """Fetch recent documents from API."""
        result = self._api_request("/v2/get-documents", {
            "limit": limit,
            "offset": 0,
            "include_last_viewed_panel": True
        })
        if result:
            # API returns 'docs' not 'documents'
            return result.get('docs') or result.get('documents')
        return None


def transcript_word_count(transcript: list) -> int:
    """Count total words in a transcript."""
    if not transcript:
        return 0
    return sum(len(entry.get('text', '').split()) for entry in transcript)


def load_granola_cache():
    """Load and parse Granola's cache file."""
    if not GRANOLA_CACHE.exists():
        raise FileNotFoundError(f"Granola cache not found at {GRANOLA_CACHE}")

    with open(GRANOLA_CACHE, 'r') as f:
        data = json.load(f)

    cache = json.loads(data['cache'])
    return cache['state']


def extract_full_name(display_name: str = None, email: str = None) -> str:
    """Extract the best possible full name from display name and/or email.

    Prefers displayName if it looks like a real name (has at least first and last).
    Falls back to deriving a name from email address if possible.

    Args:
        display_name: The displayName field (e.g., "Jesse Olsen")
        email: The email address (e.g., "jesse.olsen@company.com")

    Returns:
        The best full name available, or email if no name can be derived.
    """
    # Try display_name first if it looks like a full name (has space = likely first+last)
    if display_name:
        display_name = display_name.strip()
        # If display name has multiple parts, it's likely a full name
        if ' ' in display_name:
            return display_name
        # Single word display name - check if we can do better with email

    # Try to extract name from email
    if email:
        email = email.strip()
        local_part = email.split('@')[0] if '@' in email else email

        # Common patterns: first.last, first_last, firstlast
        # Try splitting on . or _
        if '.' in local_part or '_' in local_part:
            parts = re.split(r'[._]', local_part)
            # Filter out common non-name parts and numbers
            name_parts = [p for p in parts if p and not p.isdigit() and len(p) > 1]
            if len(name_parts) >= 2:
                # Title case each part
                full_name = ' '.join(p.capitalize() for p in name_parts[:2])
                return full_name

    # Fall back to display_name (even if single word) or email
    if display_name:
        return display_name
    return email or ''


def sanitize_filename(name: str) -> str:
    """Convert a string to a safe filename."""
    # Remove or replace invalid characters
    name = re.sub(r'[<>:"/\\|?*]', '', name)
    name = re.sub(r'\s+', '_', name)
    name = name.strip('._')
    return name[:100]  # Limit length


def prosemirror_to_markdown(node: dict, indent: int = 0, ordered: int = None) -> str:
    """Convert ProseMirror document structure to markdown."""
    if not isinstance(node, dict):
        return ""

    node_type = node.get('type', '')
    content = node.get('content', [])
    text = node.get('text', '')
    attrs = node.get('attrs', {})

    result = []

    if node_type == 'doc':
        for child in content:
            result.append(prosemirror_to_markdown(child, indent))

    elif node_type == 'heading':
        level = attrs.get('level', 1)
        heading_text = ''.join(prosemirror_to_markdown(c, indent) for c in content)
        result.append(f"{'#' * level} {heading_text}\n\n")

    elif node_type == 'paragraph':
        para_text = ''.join(prosemirror_to_markdown(c, indent) for c in content)
        if para_text.strip():
            result.append(f"{para_text}\n")

    elif node_type == 'bulletList':
        for child in content:
            result.append(prosemirror_to_markdown(child, indent))
        result.append("\n")

    elif node_type == 'orderedList':
        for i, child in enumerate(content, 1):
            child_result = prosemirror_to_markdown(child, indent, ordered=i)
            result.append(child_result)
        result.append("\n")

    elif node_type == 'listItem':
        item_content = []
        for child in content:
            child_md = prosemirror_to_markdown(child, indent + 1)
            item_content.append(child_md.strip())
        item_text = ' '.join(item_content)
        if ordered:
            prefix = '  ' * indent + f'{ordered}. '
        else:
            prefix = '  ' * indent + '- '
        result.append(f"{prefix}{item_text}\n")

    elif node_type == 'text':
        marks = node.get('marks', [])
        formatted_text = text
        for mark in marks:
            mark_type = mark.get('type', '')
            if mark_type == 'bold':
                formatted_text = f"**{formatted_text}**"
            elif mark_type == 'italic':
                formatted_text = f"*{formatted_text}*"
            elif mark_type == 'code':
                formatted_text = f"`{formatted_text}`"
        result.append(formatted_text)

    elif node_type == 'hardBreak':
        result.append('\n')

    else:
        # For unknown types, try to extract text from children
        for child in content:
            result.append(prosemirror_to_markdown(child, indent))

    return ''.join(result)


def extract_summary(doc_id: str, document_panels: dict, doc: dict) -> str:
    """Extract AI-generated summary from document panels."""
    panels = document_panels.get(doc_id, {})
    if not panels:
        return ""

    lines = []
    title = doc.get('title', 'Meeting')

    # Get meeting date for header
    created = doc.get('created_at', '')
    date_str = ""
    if created:
        try:
            dt = datetime.fromisoformat(created.replace('Z', '+00:00'))
            date_str = dt.strftime('%Y-%m-%d %H:%M')
        except:
            date_str = created

    lines.append(f"# {title} - Summary")
    lines.append("")
    if date_str:
        lines.append(f"**Date**: {date_str}")

    # Get attendees
    cal_event = doc.get('google_calendar_event') or {}
    if cal_event.get('attendees'):
        attendees = [extract_full_name(a.get('displayName'), a.get('email')) for a in cal_event['attendees']]
        lines.append(f"**Attendees**: {', '.join(attendees)}")

    lines.append("")
    lines.append("---")
    lines.append("")

    # Process each panel (usually just "Summary")
    for panel_id, panel in panels.items():
        panel_title = panel.get('title', '')
        content = panel.get('content', {})

        if content:
            # Convert ProseMirror content to markdown
            md_content = prosemirror_to_markdown(content)
            if md_content.strip():
                lines.append(md_content)

    return '\n'.join(lines)


def format_transcript(transcript_entries: list, include_timestamps: bool = True) -> str:
    """Format transcript entries into readable text."""
    if not transcript_entries:
        return ""

    lines = []
    current_speaker = None
    current_text = []

    for entry in transcript_entries:
        text = entry.get('text', '').strip()
        if not text:
            continue

        source = entry.get('source', 'unknown')
        # Map source to speaker label
        speaker = "You" if source == "microphone" else "Other"

        timestamp = entry.get('start_timestamp', '')
        if timestamp:
            try:
                dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
                time_str = dt.strftime('%H:%M:%S')
            except:
                time_str = ""
        else:
            time_str = ""

        # Group consecutive utterances from same speaker
        if speaker == current_speaker:
            current_text.append(text)
        else:
            # Flush previous speaker's text
            if current_speaker and current_text:
                combined = ' '.join(current_text)
                lines.append(f"**{current_speaker}**: {combined}")

            current_speaker = speaker
            current_text = [text]

    # Flush final speaker
    if current_speaker and current_text:
        combined = ' '.join(current_text)
        lines.append(f"**{current_speaker}**: {combined}")

    return '\n\n'.join(lines)


def extract_meeting(doc: dict, transcript: list = None) -> str:
    """Generate markdown content for a meeting."""
    lines = []

    # Title
    title = doc.get('title', 'Untitled Meeting')
    lines.append(f"# {title}")
    lines.append("")

    # Metadata
    created = doc.get('created_at', '')
    if created:
        try:
            dt = datetime.fromisoformat(created.replace('Z', '+00:00'))
            lines.append(f"**Date**: {dt.strftime('%Y-%m-%d %H:%M')}")
        except:
            lines.append(f"**Date**: {created}")

    # Calendar event info
    cal_event = doc.get('google_calendar_event') or {}
    if cal_event:
        if cal_event.get('attendees'):
            attendees = [extract_full_name(a.get('displayName'), a.get('email')) for a in cal_event['attendees']]
            lines.append(f"**Attendees**: {', '.join(attendees)}")
        if cal_event.get('location'):
            lines.append(f"**Location**: {cal_event['location']}")

    # People
    people = doc.get('people', [])
    if people and not cal_event.get('attendees'):
        names = []
        for p in people:
            if isinstance(p, dict):
                name = extract_full_name(p.get('name'), p.get('email'))
                if name:
                    names.append(name)
            elif isinstance(p, str):
                names.append(p)
        if names:
            lines.append(f"**Participants**: {', '.join(names)}")

    lines.append("")

    # Overview/Summary
    overview = doc.get('overview')
    summary = doc.get('summary')

    if overview:
        lines.append("## Overview")
        lines.append("")
        if isinstance(overview, str):
            lines.append(overview)
        elif isinstance(overview, dict):
            lines.append(json.dumps(overview, indent=2))
        lines.append("")

    if summary:
        lines.append("## Summary")
        lines.append("")
        if isinstance(summary, str):
            lines.append(summary)
        elif isinstance(summary, dict):
            lines.append(json.dumps(summary, indent=2))
        lines.append("")

    # Notes
    notes = doc.get('notes_markdown') or doc.get('notes_plain') or doc.get('notes')
    if notes:
        lines.append("## Notes")
        lines.append("")
        if isinstance(notes, str):
            lines.append(notes)
        elif isinstance(notes, dict):
            lines.append(json.dumps(notes, indent=2))
        lines.append("")

    # Chapters (AI-generated sections)
    chapters = doc.get('chapters', [])
    if chapters and isinstance(chapters, list):
        lines.append("## Chapters")
        lines.append("")
        for chapter in chapters:
            if isinstance(chapter, dict):
                ch_title = chapter.get('title', 'Section')
                ch_summary = chapter.get('summary', '')
                lines.append(f"### {ch_title}")
                if ch_summary and isinstance(ch_summary, str):
                    lines.append(ch_summary)
                lines.append("")

    # Transcript
    if transcript:
        lines.append("## Transcript")
        lines.append("")
        formatted = format_transcript(transcript)
        if formatted:
            lines.append(formatted)
        else:
            lines.append("_No transcript content available_")
        lines.append("")

    return '\n'.join(lines)


def get_meeting_date(doc: dict) -> datetime:
    """Extract meeting date from document."""
    created = doc.get('created_at', '')
    if created:
        try:
            return datetime.fromisoformat(created.replace('Z', '+00:00'))
        except:
            pass
    return datetime.min


def summary_has_content(summary_content: str) -> bool:
    """Check if summary has meaningful content (not just headers)."""
    if not summary_content:
        return False

    lines = summary_content.strip().split('\n')
    # Filter out empty lines, headers, and metadata lines
    content_lines = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith('#'):  # Headers
            continue
        if line.startswith('**Date**:') or line.startswith('**Attendees**:'):
            continue
        if line == '---':
            continue
        content_lines.append(line)

    # Need at least a few lines of real content
    return len(content_lines) >= 3


def extract_action_items_json(output: str) -> list[dict]:
    """Extract action items JSON from Claude's output."""
    # Look for JSON block with action_items
    json_match = re.search(r'```json\s*(\{[^`]*"action_items"[^`]*\})\s*```', output, re.DOTALL)
    if json_match:
        try:
            data = json.loads(json_match.group(1))
            return data.get('action_items', [])
        except json.JSONDecodeError:
            pass

    # Fallback: try to find raw JSON object
    json_match = re.search(r'\{"action_items":\s*\[.*?\]\}', output, re.DOTALL)
    if json_match:
        try:
            data = json.loads(json_match.group())
            return data.get('action_items', [])
        except json.JSONDecodeError:
            pass

    return []


def create_vibe_kanban_tasks(action_items: list[dict], meeting_title: str, meeting_date: str, quiet: bool = False):
    """Create tasks in vibe-kanban from action items."""
    if not action_items:
        return

    try:
        from vibe_kanban_client import create_tasks_from_action_items
        create_tasks_from_action_items(
            action_items=action_items,
            meeting_title=meeting_title,
            meeting_date=meeting_date,
            quiet=quiet
        )
    except ImportError:
        if not quiet:
            print(f"  ⚠ vibe_kanban_client not found - skipping task creation")
    except Exception as e:
        if not quiet:
            print(f"  ⚠ Error creating vibe-kanban tasks: {e}")


def run_post_meeting_processing(summary_path: Path, transcript_path: Path, quiet: bool = False):
    """Run Claude to process a new meeting summary and create vibe-kanban tasks."""
    if not POST_MEETING_PROMPT.exists():
        if not quiet:
            print(f"  ⚠ Post-processing prompt not found: {POST_MEETING_PROMPT}")
        return

    # Read the prompt template and substitute paths
    with open(POST_MEETING_PROMPT, 'r') as f:
        prompt_template = f.read()

    prompt = prompt_template.replace('{SUMMARY_PATH}', str(summary_path))
    prompt = prompt.replace('{TRANSCRIPT_PATH}', str(transcript_path))

    if not quiet:
        print(f"  🤖 Running post-meeting processing...")

    try:
        # Run Claude with dangerously-skip-permissions for automation
        result = subprocess.run(
            ['claude', '--dangerously-skip-permissions', '-p', prompt],
            capture_output=True,
            text=True,
            timeout=300  # 5 minute timeout
        )

        if result.returncode == 0:
            if not quiet:
                print(f"  ✅ Post-processing complete")

            # Extract action items and create vibe-kanban tasks
            action_items = extract_action_items_json(result.stdout)
            if action_items:
                # Extract meeting info from summary path
                # Format: YYYY-MM-DD_Meeting_Title.md
                filename = summary_path.stem
                parts = filename.split('_', 1)
                meeting_date = parts[0] if len(parts) > 0 else datetime.now().strftime('%Y-%m-%d')
                meeting_title = parts[1].replace('_', ' ') if len(parts) > 1 else filename

                create_vibe_kanban_tasks(action_items, meeting_title, meeting_date, quiet=quiet)
        else:
            if not quiet:
                print(f"  ❌ Post-processing failed: {result.stderr[:200]}")
    except subprocess.TimeoutExpired:
        if not quiet:
            print(f"  ⚠ Post-processing timed out")
    except FileNotFoundError:
        if not quiet:
            print(f"  ⚠ Claude CLI not found - skipping post-processing")
    except Exception as e:
        if not quiet:
            print(f"  ⚠ Post-processing error: {e}")


def list_meetings(state: dict):
    """Print a list of all available meetings."""
    docs = state.get('documents', {})
    transcripts = state.get('transcripts', {})

    meetings = []
    for doc_id, doc in docs.items():
        if doc.get('deleted_at'):
            continue

        title = doc.get('title', 'Untitled')
        date = get_meeting_date(doc)
        has_transcript = doc_id in transcripts and len(transcripts[doc_id]) > 0
        has_notes = bool(doc.get('notes_markdown') or doc.get('notes'))
        has_summary = bool(doc.get('summary') or doc.get('overview'))

        meetings.append({
            'id': doc_id,
            'title': title,
            'date': date,
            'has_transcript': has_transcript,
            'has_notes': has_notes,
            'has_summary': has_summary
        })

    # Sort by date descending
    meetings.sort(key=lambda x: x['date'], reverse=True)

    print(f"\n{'Date':<12} {'Title':<50} {'Trans':<6} {'Notes':<6} {'Summary':<8} {'ID'}")
    print("-" * 120)

    for m in meetings:
        date_str = m['date'].strftime('%Y-%m-%d') if m['date'] != datetime.min else 'Unknown'
        trans = '✓' if m['has_transcript'] else ''
        notes = '✓' if m['has_notes'] else ''
        summary = '✓' if m['has_summary'] else ''
        print(f"{date_str:<12} {m['title'][:48]:<50} {trans:<6} {notes:<6} {summary:<8} {m['id'][:8]}...")

    print(f"\nTotal: {len(meetings)} meetings")


def extract_meetings(state: dict, output_dir: Path, recent_hours: float = None, doc_id: str = None, force: bool = False, process: bool = True, quiet: bool = False, use_api: bool = True):
    """Extract meetings to markdown files.

    Outputs are organized into subdirectories:
    - summaries/   AI-generated summaries (small, read first)
    - transcripts/ Full transcripts with notes (large, read for detail)

    Args:
        state: Granola cache state
        output_dir: Directory to write files
        recent_hours: Only extract meetings from the last N hours (default: 30)
        doc_id: Extract only a specific meeting by ID
        force: Overwrite existing files (default: skip existing)
        process: Run post-meeting processing for new summaries (default: True)
        quiet: Suppress output (default: False)
        use_api: Fall back to API for incomplete transcripts (default: True)
    """
    docs = state.get('documents', {})
    transcripts = state.get('transcripts', {})
    document_panels = state.get('documentPanels', {})

    # Initialize API client for fallback
    api_client = None
    if use_api:
        api_client = GranolaAPIClient(quiet=quiet)
        if api_client.is_available() and not quiet:
            print("  API fallback enabled for incomplete transcripts")

    # Create subdirectories
    summaries_dir = output_dir / "summaries"
    transcripts_dir = output_dir / "transcripts"
    summaries_dir.mkdir(parents=True, exist_ok=True)
    transcripts_dir.mkdir(parents=True, exist_ok=True)

    # Default to last 30 hours if not specified and not extracting specific ID
    if recent_hours is None and doc_id is None:
        recent_hours = 30

    cutoff_date = None
    if recent_hours:
        cutoff_date = datetime.now().astimezone() - timedelta(hours=recent_hours)

    extracted = 0
    summaries_extracted = 0
    skipped_date = 0
    skipped_exists = 0
    skipped_empty = 0
    new_summaries = []  # Track (summary_path, transcript_path) for post-processing

    for d_id, doc in docs.items():
        # Skip deleted
        if doc.get('deleted_at'):
            continue

        # Filter by specific ID (supports partial matching)
        if doc_id and not d_id.startswith(doc_id):
            continue

        # Filter by date (skip if specific doc_id is provided)
        meeting_date = get_meeting_date(doc)
        if cutoff_date and not doc_id and meeting_date < cutoff_date:
            skipped_date += 1
            continue

        title = doc.get('title', 'Untitled')
        if not isinstance(title, str):
            title = str(title) if title else 'Untitled'
        transcript = transcripts.get(d_id, [])
        has_summary_panel = d_id in document_panels and len(document_panels[d_id]) > 0

        # Skip if no meaningful content
        has_content = (
            transcript or
            doc.get('notes_markdown') or
            doc.get('notes') or
            doc.get('summary') or
            doc.get('overview') or
            has_summary_panel
        )

        if not has_content:
            skipped_empty += 1
            continue

        # Generate filename (same name used in both folders)
        date_str = meeting_date.strftime('%Y-%m-%d') if meeting_date != datetime.min else 'unknown'
        safe_title = sanitize_filename(title)
        filename = f"{date_str}_{safe_title}.md"

        # Extract transcript to transcripts/ folder
        transcript_filepath = transcripts_dir / filename

        if transcript_filepath.exists() and not force:
            skipped_exists += 1
        else:
            # Check if transcript is incomplete and try API fallback
            word_count = transcript_word_count(transcript)
            api_fetched = False

            if api_client and api_client.is_available() and word_count < MIN_TRANSCRIPT_WORDS:
                if not quiet:
                    print(f"  ⚡ Cache transcript incomplete ({word_count} words), fetching from API...")
                api_transcript = api_client.get_document_transcript(d_id)
                if api_transcript:
                    api_word_count = transcript_word_count(api_transcript)
                    if api_word_count > word_count:
                        transcript = api_transcript
                        api_fetched = True
                        if not quiet:
                            print(f"  ✓ Got {api_word_count} words from API")

            content = extract_meeting(doc, transcript)
            with open(transcript_filepath, 'w') as f:
                f.write(content)

            status = "✓"
            if api_fetched:
                status = "✓ (API)"
            print(f"{status} Transcript: {filename}")
            extracted += 1

        # Extract summary to summaries/ folder (if available)
        if has_summary_panel:
            summary_filepath = summaries_dir / filename
            is_new_summary = not summary_filepath.exists()

            if summary_filepath.exists() and not force:
                pass  # Don't count as skipped, transcript might be new
            else:
                summary_content = extract_summary(d_id, document_panels, doc)
                if summary_content.strip():
                    with open(summary_filepath, 'w') as f:
                        f.write(summary_content)
                    if not quiet:
                        print(f"  ✓ Summary: {filename}")
                    summaries_extracted += 1

                    # Track for post-processing if this is a NEW summary with real content
                    if is_new_summary and summary_has_content(summary_content):
                        new_summaries.append((summary_filepath, transcript_filepath))

    # Print summary
    if not quiet:
        print(f"\nDone! Extracted {extracted} transcripts, {summaries_extracted} summaries")
        if skipped_exists > 0:
            print(f"  Skipped {skipped_exists} (already exist)")
        if skipped_date > 0:
            print(f"  Skipped {skipped_date} (outside time range)")
        if skipped_empty > 0:
            print(f"  Skipped {skipped_empty} (no content)")
        print(f"Output: {transcripts_dir} and {summaries_dir}")

    # Run post-meeting processing for new summaries
    if process and new_summaries:
        if not quiet:
            print(f"\n📋 Processing {len(new_summaries)} new meeting(s)...")
        for summary_path, transcript_path in new_summaries:
            if not quiet:
                print(f"\n  Processing: {summary_path.name}")
            run_post_meeting_processing(summary_path, transcript_path, quiet=quiet)


def main():
    parser = argparse.ArgumentParser(
        description='Extract Granola meeting transcripts and summaries',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                      # Incremental: last 30 hours, skip existing
  %(prog)s --full               # Full extraction, overwrite all files
  %(prog)s --hours 48           # Last 48 hours, skip existing
  %(prog)s --hours 48 --force   # Last 48 hours, overwrite existing
  %(prog)s --list               # List all available meetings
  %(prog)s --id abc123          # Extract specific meeting by ID
"""
    )
    parser.add_argument('--list', '-l', action='store_true',
                        help='List available meetings')
    parser.add_argument('--hours', '-r', type=float, metavar='HOURS',
                        help='Extract meetings from last N hours (default: 30)')
    parser.add_argument('--full', action='store_true',
                        help='Extract ALL meetings (ignores --hours)')
    parser.add_argument('--force', '-f', action='store_true',
                        help='Overwrite existing files (default: skip existing)')
    parser.add_argument('--id', type=str,
                        help='Extract specific meeting by ID')
    parser.add_argument('--output', '-o', type=str,
                        help='Output directory (default: same as script)')
    parser.add_argument('--quiet', '-q', action='store_true',
                        help='Minimal output (for cron/automation)')
    parser.add_argument('--no-process', action='store_true',
                        help='Skip post-meeting processing (people/tasks)')
    parser.add_argument('--no-api', action='store_true',
                        help='Disable API fallback for incomplete transcripts')

    args = parser.parse_args()

    try:
        if not args.quiet:
            print("Loading Granola cache...")
        state = load_granola_cache()

        output_dir = Path(args.output) if args.output else OUTPUT_DIR

        if args.list:
            list_meetings(state)
        else:
            # Determine hours cutoff
            if args.full:
                recent_hours = None  # No cutoff
            elif args.hours:
                recent_hours = args.hours
            else:
                recent_hours = 30  # Default

            extract_meetings(
                state,
                output_dir,
                recent_hours=recent_hours,
                doc_id=args.id,
                force=args.force or args.full,  # --full implies --force
                process=not args.no_process,
                quiet=args.quiet,
                use_api=not args.no_api
            )

    except FileNotFoundError as e:
        print(f"Error: {e}")
        return 1
    except json.JSONDecodeError as e:
        print(f"Error parsing Granola cache: {e}")
        return 1
    except Exception as e:
        print(f"Error: {e}")
        raise


if __name__ == '__main__':
    main()
