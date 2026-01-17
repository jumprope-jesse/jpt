#!/usr/bin/env python3
"""
Notion Reading List Sync

Extracts links from Notion databases and stores them as markdown files with
metadata and fetched content for later analysis.

Usage:
    python notion_reading_sync.py                    # Sync unsynced items
    python notion_reading_sync.py --list             # List items in database
    python notion_reading_sync.py --all              # Force sync all items
    python notion_reading_sync.py --dry-run          # Show what would be synced
    python notion_reading_sync.py --db DB_KEY        # Sync specific database

Configuration (~/.config/notion_reading.json):
    {
        "token": "secret_xxx",
        "databases": {
            "main": "database-id-1",
            "archive": "database-id-2"
        }
    }

Environment variables (alternative):
    NOTION_TOKEN         - Notion integration token
    NOTION_READING_DB    - Primary reading list database ID
    NOTION_READING_DB_2  - Secondary database ID (optional)
"""

import json
import os
import re
import argparse
import urllib.request
import urllib.error
import gzip
import ssl
from datetime import datetime
from pathlib import Path
from typing import Optional
from html.parser import HTMLParser
from urllib.parse import urlparse


# Configuration paths - tries reading-specific config first, then falls back to general notion_sync.json
CONFIG_FILE = Path.home() / ".config" / "notion_reading.json"
FALLBACK_CONFIG_FILE = Path.home() / ".config" / "notion_sync.json"
OUTPUT_DIR = Path(__file__).parent
PROCESSED_FILE = OUTPUT_DIR / ".processed_reading.json"

# Notion API
NOTION_API_BASE = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"

# Content fetching settings
MAX_CONTENT_SIZE = 500_000  # 500KB max content to fetch
FETCH_TIMEOUT = 30
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"


class HTMLTextExtractor(HTMLParser):
    """Extract readable text from HTML, stripping tags."""

    def __init__(self):
        super().__init__()
        self.text_parts = []
        self.skip_tags = {'script', 'style', 'nav', 'header', 'footer', 'aside', 'noscript'}
        self.current_skip_depth = 0
        self.in_title = False
        self.title = ""
        self.in_main = False
        self.main_content = []

    def handle_starttag(self, tag, attrs):
        if tag in self.skip_tags:
            self.current_skip_depth += 1
        if tag == 'title':
            self.in_title = True
        if tag in ('main', 'article'):
            self.in_main = True
        if tag in ('p', 'div', 'br', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            if self.current_skip_depth == 0:
                self.text_parts.append('\n')
                if self.in_main:
                    self.main_content.append('\n')

    def handle_endtag(self, tag):
        if tag in self.skip_tags and self.current_skip_depth > 0:
            self.current_skip_depth -= 1
        if tag == 'title':
            self.in_title = False
        if tag in ('main', 'article'):
            self.in_main = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        if self.current_skip_depth == 0:
            text = data.strip()
            if text:
                self.text_parts.append(text + ' ')
                if self.in_main:
                    self.main_content.append(text + ' ')

    def get_text(self) -> str:
        # Prefer main/article content if substantial
        if self.main_content and len(''.join(self.main_content)) > 500:
            text = ''.join(self.main_content)
        else:
            text = ''.join(self.text_parts)
        # Clean up whitespace
        text = re.sub(r'\n\s*\n', '\n\n', text)
        text = re.sub(r' +', ' ', text)
        return text.strip()


class NotionClient:
    """Client for Notion API using urllib (no external dependencies)."""

    def __init__(self, token: str, quiet: bool = False):
        self.token = token
        self.quiet = quiet
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Notion-Version": NOTION_VERSION,
        }

    def _request(self, method: str, endpoint: str, payload: Optional[dict] = None) -> Optional[dict]:
        """Make an API request to Notion."""
        url = f"{NOTION_API_BASE}{endpoint}"
        data = json.dumps(payload).encode('utf-8') if payload else None

        try:
            req = urllib.request.Request(url, data=data, headers=self.headers, method=method)
            with urllib.request.urlopen(req, timeout=30) as response:
                return json.loads(response.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            error_body = e.read().decode('utf-8') if e.fp else ''
            if not self.quiet:
                print(f"  API error {e.code}: {error_body[:200]}")
            return None
        except Exception as e:
            if not self.quiet:
                print(f"  Request failed: {e}")
            return None

    def query_database(self, database_id: str, filter_obj: Optional[dict] = None,
                       sorts: Optional[list] = None) -> list:
        """Query a Notion database with optional filter and sort."""
        payload = {}
        if filter_obj:
            payload["filter"] = filter_obj
        if sorts:
            payload["sorts"] = sorts

        all_results = []
        has_more = True
        start_cursor = None

        while has_more:
            if start_cursor:
                payload["start_cursor"] = start_cursor

            result = self._request("POST", f"/databases/{database_id}/query", payload)
            if not result:
                break

            all_results.extend(result.get("results", []))
            has_more = result.get("has_more", False)
            start_cursor = result.get("next_cursor")

        return all_results

    def get_page(self, page_id: str) -> Optional[dict]:
        """Get a single page by ID."""
        return self._request("GET", f"/pages/{page_id}")

    def update_page(self, page_id: str, properties: dict) -> Optional[dict]:
        """Update page properties."""
        return self._request("PATCH", f"/pages/{page_id}", {"properties": properties})

    def get_block_children(self, block_id: str) -> list:
        """Get all child blocks of a page/block."""
        all_blocks = []
        has_more = True
        start_cursor = None

        while has_more:
            endpoint = f"/blocks/{block_id}/children"
            if start_cursor:
                endpoint += f"?start_cursor={start_cursor}"

            result = self._request("GET", endpoint)
            if not result:
                break

            all_blocks.extend(result.get("results", []))
            has_more = result.get("has_more", False)
            start_cursor = result.get("next_cursor")

        return all_blocks

    def get_database(self, database_id: str) -> Optional[dict]:
        """Get database schema/properties."""
        return self._request("GET", f"/databases/{database_id}")


def load_config() -> tuple:
    """Load configuration from file or environment.

    Tries in order:
    1. Environment variables (NOTION_TOKEN, NOTION_READING_DB, NOTION_READING_DB_2)
    2. ~/.config/notion_reading.json (reading-list specific config)
    3. ~/.config/notion_sync.json (general Notion config, for token only)

    Returns:
        (token, databases_dict) where databases_dict maps name -> database_id
    """
    databases = {}

    # Try environment first
    token = os.environ.get("NOTION_TOKEN")
    if os.environ.get("NOTION_READING_DB"):
        databases["main"] = os.environ.get("NOTION_READING_DB")
    if os.environ.get("NOTION_READING_DB_2"):
        databases["secondary"] = os.environ.get("NOTION_READING_DB_2")

    # Try reading-specific config file
    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, 'r') as f:
                config = json.load(f)
            token = token or config.get("token")
            if "databases" in config:
                databases.update(config["databases"])
            elif "database_id" in config:
                databases["main"] = config["database_id"]
        except Exception:
            pass

    # Fall back to general notion_sync.json for token only (not database IDs)
    if not token and FALLBACK_CONFIG_FILE.exists():
        try:
            with open(FALLBACK_CONFIG_FILE, 'r') as f:
                config = json.load(f)
            token = config.get("token")
        except Exception:
            pass

    return token, databases


def load_processed() -> set:
    """Load set of already processed page IDs."""
    if PROCESSED_FILE.exists():
        try:
            with open(PROCESSED_FILE, 'r') as f:
                data = json.load(f)
                return set(data.get("processed", []))
        except Exception:
            pass
    return set()


def save_processed(processed: set):
    """Save processed page IDs."""
    PROCESSED_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(PROCESSED_FILE, 'w') as f:
        json.dump({"processed": list(processed), "updated": datetime.now().isoformat()}, f, indent=2)


def sanitize_filename(name: str) -> str:
    """Convert a string to a safe filename."""
    name = re.sub(r'[<>:"/\\|?*]', '', name)
    name = re.sub(r'\s+', '_', name)
    name = name.strip('._')
    return name[:100]


def extract_rich_text(rich_text_array: list) -> str:
    """Extract plain text from Notion rich_text array."""
    if not rich_text_array:
        return ""
    return "".join(item.get("plain_text", "") for item in rich_text_array)


def extract_property_value(prop: dict):
    """Extract value from a Notion property object."""
    prop_type = prop.get("type", "")

    if prop_type == "title":
        return extract_rich_text(prop.get("title", []))
    elif prop_type == "rich_text":
        return extract_rich_text(prop.get("rich_text", []))
    elif prop_type == "date":
        date_obj = prop.get("date")
        if date_obj:
            return date_obj.get("start", "")
        return ""
    elif prop_type == "select":
        select_obj = prop.get("select")
        if select_obj:
            return select_obj.get("name", "")
        return ""
    elif prop_type == "multi_select":
        items = prop.get("multi_select", [])
        return [item.get("name", "") for item in items]
    elif prop_type == "checkbox":
        return prop.get("checkbox", False)
    elif prop_type == "url":
        return prop.get("url", "") or ""
    elif prop_type == "number":
        num = prop.get("number")
        return num if num is not None else ""
    elif prop_type == "created_time":
        return prop.get("created_time", "")
    elif prop_type == "last_edited_time":
        return prop.get("last_edited_time", "")
    elif prop_type == "files":
        files = prop.get("files", [])
        urls = []
        for f in files:
            if f.get("type") == "file":
                urls.append(f.get("file", {}).get("url", ""))
            elif f.get("type") == "external":
                urls.append(f.get("external", {}).get("url", ""))
        return urls
    else:
        return ""


def blocks_to_markdown(blocks: list) -> str:
    """Convert Notion blocks to markdown."""
    lines = []

    for block in blocks:
        block_type = block.get("type", "")
        block_data = block.get(block_type, {})

        if block_type == "paragraph":
            text = extract_rich_text(block_data.get("rich_text", []))
            if text:
                lines.append(text)
                lines.append("")

        elif block_type == "heading_1":
            text = extract_rich_text(block_data.get("rich_text", []))
            lines.append(f"# {text}")
            lines.append("")

        elif block_type == "heading_2":
            text = extract_rich_text(block_data.get("rich_text", []))
            lines.append(f"## {text}")
            lines.append("")

        elif block_type == "heading_3":
            text = extract_rich_text(block_data.get("rich_text", []))
            lines.append(f"### {text}")
            lines.append("")

        elif block_type == "bulleted_list_item":
            text = extract_rich_text(block_data.get("rich_text", []))
            lines.append(f"- {text}")

        elif block_type == "numbered_list_item":
            text = extract_rich_text(block_data.get("rich_text", []))
            lines.append(f"1. {text}")

        elif block_type == "to_do":
            text = extract_rich_text(block_data.get("rich_text", []))
            checked = block_data.get("checked", False)
            checkbox = "[x]" if checked else "[ ]"
            lines.append(f"- {checkbox} {text}")

        elif block_type == "code":
            text = extract_rich_text(block_data.get("rich_text", []))
            language = block_data.get("language", "")
            lines.append(f"```{language}")
            lines.append(text)
            lines.append("```")
            lines.append("")

        elif block_type == "quote":
            text = extract_rich_text(block_data.get("rich_text", []))
            lines.append(f"> {text}")
            lines.append("")

        elif block_type == "bookmark":
            url = block_data.get("url", "")
            caption = extract_rich_text(block_data.get("caption", []))
            if caption:
                lines.append(f"[{caption}]({url})")
            else:
                lines.append(f"<{url}>")
            lines.append("")

        elif block_type == "embed":
            url = block_data.get("url", "")
            lines.append(f"Embed: <{url}>")
            lines.append("")

        elif block_type == "divider":
            lines.append("---")
            lines.append("")

        elif block_type == "callout":
            text = extract_rich_text(block_data.get("rich_text", []))
            icon = block_data.get("icon", {})
            emoji = icon.get("emoji", "") if icon.get("type") == "emoji" else ""
            lines.append(f"> {emoji} {text}")
            lines.append("")

    return "\n".join(lines)


def detect_content_type(url: str, title: str = "", content: str = "") -> str:
    """Detect the type of content based on URL patterns and content.

    Returns one of: github_repo, news_article, tech_deep_dive, product_review,
                    documentation, video, podcast, social_post, newsletter, tool, unknown
    """
    url_lower = url.lower()
    title_lower = title.lower()
    content_lower = content.lower()[:5000] if content else ""

    # GitHub repositories
    if 'github.com' in url_lower:
        if '/blob/' in url_lower or '/tree/' in url_lower:
            return "github_code"
        if '/issues/' in url_lower or '/pull/' in url_lower:
            return "github_discussion"
        if '/releases' in url_lower:
            return "github_release"
        return "github_repo"

    # Video platforms
    if any(v in url_lower for v in ['youtube.com', 'youtu.be', 'vimeo.com', 'loom.com']):
        return "video"

    # Podcasts
    if any(p in url_lower for p in ['podcast', 'spotify.com/episode', 'podcasts.apple.com', 'overcast.fm']):
        return "podcast"

    # Social media
    if any(s in url_lower for s in ['twitter.com', 'x.com', 'linkedin.com/posts', 'threads.net']):
        return "social_post"

    # Newsletters
    if any(n in url_lower for n in ['substack.com', 'newsletter', 'buttondown.email', 'mailchi.mp']):
        return "newsletter"

    # Documentation
    if any(d in url_lower for d in ['docs.', '/docs/', 'documentation', 'readme', 'wiki']):
        return "documentation"

    # Tools/Products (common patterns)
    if any(t in url_lower for t in ['/pricing', '/features', 'producthunt.com', '/product/']):
        return "tool"

    # News sites
    news_domains = ['techcrunch', 'theverge', 'wired.com', 'arstechnica', 'bbc.com/news',
                    'nytimes.com', 'wsj.com', 'reuters.com', 'bloomberg.com', 'hackernews',
                    'news.ycombinator']
    if any(n in url_lower for n in news_domains):
        return "news_article"

    # Tech blogs / deep dives
    tech_indicators = ['technical', 'architecture', 'implementation', 'deep dive',
                       'how we built', 'engineering blog', 'system design']
    if any(t in title_lower or t in content_lower for t in tech_indicators):
        return "tech_deep_dive"

    # Product reviews
    review_indicators = ['review', 'comparison', 'vs', 'tested', 'hands-on', 'first look']
    if any(r in title_lower for r in review_indicators):
        return "product_review"

    # Research / academic
    if any(r in url_lower for r in ['arxiv.org', 'research', 'paper', 'scholar.google']):
        return "research_paper"

    return "article"


def fetch_url_content(url: str, quiet: bool = False) -> tuple:
    """Fetch and extract content from a URL.

    Returns:
        (title, content, error) tuple
    """
    if not url:
        return "", "", "No URL provided"

    # Skip certain URLs that won't have extractable content
    skip_patterns = ['youtube.com', 'youtu.be', 'vimeo.com', 'spotify.com',
                     'twitter.com', 'x.com/']
    if any(p in url.lower() for p in skip_patterns):
        return "", "", "Content type not extractable"

    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
    }

    try:
        # Create SSL context that's more permissive for various sites
        ctx = ssl.create_default_context()

        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=FETCH_TIMEOUT, context=ctx) as response:
            # Check content type
            content_type = response.headers.get('Content-Type', '')
            if 'text/html' not in content_type and 'application/xhtml' not in content_type:
                return "", "", f"Non-HTML content: {content_type}"

            # Read content
            raw_data = response.read()

            # Handle gzip
            if response.headers.get('Content-Encoding') == 'gzip':
                raw_data = gzip.decompress(raw_data)

            # Limit size
            if len(raw_data) > MAX_CONTENT_SIZE:
                raw_data = raw_data[:MAX_CONTENT_SIZE]

            # Decode
            encoding = 'utf-8'
            if 'charset=' in content_type:
                encoding = content_type.split('charset=')[-1].split(';')[0].strip()

            try:
                html = raw_data.decode(encoding)
            except (UnicodeDecodeError, LookupError):
                html = raw_data.decode('utf-8', errors='replace')

            # Extract text
            parser = HTMLTextExtractor()
            parser.feed(html)

            return parser.title.strip(), parser.get_text(), None

    except urllib.error.HTTPError as e:
        return "", "", f"HTTP {e.code}: {e.reason}"
    except urllib.error.URLError as e:
        return "", "", f"URL error: {e.reason}"
    except Exception as e:
        return "", "", f"Fetch error: {str(e)}"


def format_reading_item_markdown(page: dict, content_blocks: list,
                                  fetched_title: str, fetched_content: str,
                                  content_type: str, db_name: str) -> str:
    """Format a reading list item as markdown."""
    props = page.get("properties", {})
    lines = []

    # Extract all properties dynamically
    metadata = {}
    title = ""
    url = ""

    for prop_name, prop_value in props.items():
        value = extract_property_value(prop_value)
        prop_lower = prop_name.lower()

        # Identify key fields
        if prop_value.get("type") == "title":
            title = value
        elif prop_lower in ("url", "link", "source"):
            url = value

        # Store all non-empty values
        if value and value != [] and value != "":
            metadata[prop_name] = value

    # Use fetched title if we don't have one
    if not title and fetched_title:
        title = fetched_title

    # Header
    lines.append(f"# {title or 'Untitled'}")
    lines.append("")

    # Core metadata
    if url:
        lines.append(f"**URL**: <{url}>")
    lines.append(f"**Content Type**: {content_type}")
    lines.append(f"**Source Database**: {db_name}")
    lines.append(f"**Synced**: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("")

    # Additional metadata from Notion
    skip_fields = {'url', 'link', 'source', 'synced', 'processed'}
    for prop_name, value in metadata.items():
        if prop_name.lower() in skip_fields:
            continue
        if props[prop_name].get("type") == "title":
            continue

        if isinstance(value, list):
            value = ", ".join(str(v) for v in value)
        elif isinstance(value, bool):
            value = "Yes" if value else "No"

        lines.append(f"**{prop_name}**: {value}")

    lines.append("")

    # Notes from Notion page content
    if content_blocks:
        notes_md = blocks_to_markdown(content_blocks)
        if notes_md.strip():
            lines.append("## My Notes")
            lines.append("")
            lines.append(notes_md)
            lines.append("")

    # Fetched content
    if fetched_content:
        lines.append("## Extracted Content")
        lines.append("")
        # Truncate very long content but keep enough for analysis
        max_content_length = 50000
        if len(fetched_content) > max_content_length:
            lines.append(fetched_content[:max_content_length])
            lines.append(f"\n... (truncated, {len(fetched_content)} total characters)")
        else:
            lines.append(fetched_content)
        lines.append("")

    # Analysis placeholder (for Claude pipeline to fill)
    lines.append("## Analysis")
    lines.append("")
    lines.append("<!-- Analysis will be added by Claude pipeline -->")
    lines.append("")
    lines.append("### Summary")
    lines.append("")
    lines.append("### Key Takeaways")
    lines.append("")
    lines.append("### Action Items")
    lines.append("")

    return "\n".join(lines)


def sync_reading_list(client: NotionClient, databases: dict, output_dir: Path,
                      db_filter: Optional[str] = None, sync_all: bool = False,
                      dry_run: bool = False, quiet: bool = False,
                      skip_fetch: bool = False, mark_synced: bool = True) -> int:
    """Sync reading list items from Notion to local markdown files.

    Returns:
        Number of items synced
    """
    processed = load_processed()
    content_dir = output_dir / "content"
    content_dir.mkdir(parents=True, exist_ok=True)

    total_synced = 0

    # Filter databases if specified
    dbs_to_sync = databases
    if db_filter:
        if db_filter in databases:
            dbs_to_sync = {db_filter: databases[db_filter]}
        else:
            print(f"Error: Database '{db_filter}' not found. Available: {list(databases.keys())}")
            return 0

    for db_name, db_id in dbs_to_sync.items():
        if not quiet:
            print(f"\n📚 Syncing database: {db_name}")

        # Query without filter first, then check for sync status
        sorts = [{"timestamp": "created_time", "direction": "descending"}]
        pages = client.query_database(db_id, sorts=sorts)

        if not pages:
            if not quiet:
                print(f"  No items found in {db_name}")
            continue

        if not quiet:
            print(f"  Found {len(pages)} total items")

        synced_in_db = 0

        for page in pages:
            page_id = page.get("id", "").replace("-", "")
            props = page.get("properties", {})

            # Skip if already processed (unless --all)
            if not sync_all and page_id in processed:
                continue

            # Check for Synced/Processed property
            if not sync_all:
                for prop_name, prop_value in props.items():
                    if prop_name.lower() in ('synced', 'processed', 'extracted'):
                        if prop_value.get("type") == "checkbox" and prop_value.get("checkbox"):
                            continue

            # Extract title and URL
            title = ""
            url = ""
            created_time = page.get("created_time", "")

            for prop_name, prop_value in props.items():
                if prop_value.get("type") == "title":
                    title = extract_property_value(prop_value)
                elif prop_name.lower() in ("url", "link", "source"):
                    url = extract_property_value(prop_value)

            if not title:
                title = "Untitled"

            # Generate filename
            if created_time:
                try:
                    dt = datetime.fromisoformat(created_time.replace('Z', '+00:00'))
                    date_prefix = dt.strftime('%Y-%m-%d')
                except Exception:
                    date_prefix = datetime.now().strftime('%Y-%m-%d')
            else:
                date_prefix = datetime.now().strftime('%Y-%m-%d')

            safe_title = sanitize_filename(title)
            filename = f"{date_prefix}_{safe_title}.md"
            filepath = content_dir / filename

            if not quiet:
                print(f"  {'[DRY-RUN] ' if dry_run else ''}Processing: {title[:50]}...")

            if dry_run:
                synced_in_db += 1
                continue

            # Fetch URL content
            fetched_title = ""
            fetched_content = ""
            fetch_error = None

            if url and not skip_fetch:
                if not quiet:
                    print(f"    Fetching content from URL...")
                fetched_title, fetched_content, fetch_error = fetch_url_content(url, quiet)
                if fetch_error and not quiet:
                    print(f"    ⚠ {fetch_error}")

            # Detect content type
            content_type = detect_content_type(url, title, fetched_content)

            # Get Notion page content (notes)
            content_blocks = client.get_block_children(page_id)

            # Format markdown
            markdown = format_reading_item_markdown(
                page, content_blocks,
                fetched_title, fetched_content,
                content_type, db_name
            )

            # Write file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(markdown)

            # Mark as synced in Notion
            if mark_synced:
                # Try common property names
                for prop_name in ['Synced', 'Processed', 'Extracted']:
                    if prop_name in props or prop_name.lower() in [p.lower() for p in props]:
                        client.update_page(page_id, {prop_name: {"checkbox": True}})
                        break

            # Track as processed
            processed.add(page_id)
            synced_in_db += 1

        total_synced += synced_in_db
        if not quiet:
            print(f"  Synced {synced_in_db} items from {db_name}")

    # Save processed IDs
    if not dry_run:
        save_processed(processed)

    if not quiet:
        print(f"\n✅ Total synced: {total_synced} items to {content_dir}")

    return total_synced


def list_reading_items(client: NotionClient, databases: dict, db_filter: Optional[str] = None):
    """List all items in the reading list databases."""
    dbs_to_list = databases
    if db_filter:
        if db_filter in databases:
            dbs_to_list = {db_filter: databases[db_filter]}
        else:
            print(f"Error: Database '{db_filter}' not found. Available: {list(databases.keys())}")
            return

    for db_name, db_id in dbs_to_list.items():
        print(f"\n📚 Database: {db_name}")
        print("=" * 80)

        # Get database schema
        schema = client.get_database(db_id)
        if schema:
            props = schema.get("properties", {})
            print(f"Properties: {', '.join(props.keys())}")
            print("-" * 80)

        sorts = [{"timestamp": "created_time", "direction": "descending"}]
        pages = client.query_database(db_id, sorts=sorts)

        if not pages:
            print("No items found.")
            continue

        print(f"{'Created':<12} {'Type':<15} {'Title'}")
        print("-" * 80)

        for page in pages:
            props = page.get("properties", {})
            created = page.get("created_time", "")[:10]

            title = ""
            url = ""

            for prop_name, prop_value in props.items():
                if prop_value.get("type") == "title":
                    title = extract_property_value(prop_value)
                elif prop_name.lower() in ("url", "link", "source"):
                    url = extract_property_value(prop_value)

            content_type = detect_content_type(url, title) if url else "unknown"

            print(f"{created:<12} {content_type:<15} {title[:50]}")

        print(f"\nTotal: {len(pages)} items")


def main():
    parser = argparse.ArgumentParser(
        description='Sync reading list from Notion to local markdown files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Configuration file (~/.config/notion_reading.json):
  {
    "token": "secret_xxx",
    "databases": {
      "main": "database-id-1",
      "archive": "database-id-2"
    }
  }

Examples:
  %(prog)s                    # Sync unsynced items from all databases
  %(prog)s --list             # List all items in all databases
  %(prog)s --db main          # Sync only from 'main' database
  %(prog)s --all              # Sync all items (ignore processed status)
  %(prog)s --dry-run          # Preview what would be synced
  %(prog)s --skip-fetch       # Sync without fetching URL content
"""
    )
    parser.add_argument('--list', '-l', action='store_true',
                        help='List items in Notion databases')
    parser.add_argument('--db', type=str,
                        help='Sync only from specific database (by name)')
    parser.add_argument('--all', '-a', action='store_true',
                        help='Sync all items (ignore processed status)')
    parser.add_argument('--dry-run', '-n', action='store_true',
                        help='Show what would be synced without writing')
    parser.add_argument('--skip-fetch', action='store_true',
                        help='Skip fetching content from URLs')
    parser.add_argument('--no-mark-synced', action='store_true',
                        help='Do not mark items as synced in Notion')
    parser.add_argument('--output', '-o', type=str,
                        help='Output directory (default: same as script)')
    parser.add_argument('--quiet', '-q', action='store_true',
                        help='Minimal output')

    args = parser.parse_args()

    # Load configuration
    token, databases = load_config()

    if not token:
        print("Error: NOTION_TOKEN not set")
        print("Set it as an environment variable or in ~/.config/notion_reading.json")
        return 1

    if not databases:
        print("Error: No databases configured")
        print("Set NOTION_READING_DB environment variable or configure in ~/.config/notion_reading.json")
        return 1

    # Initialize client
    client = NotionClient(token, quiet=args.quiet)
    output_dir = Path(args.output) if args.output else OUTPUT_DIR

    if args.list:
        list_reading_items(client, databases, db_filter=args.db)
    else:
        sync_reading_list(
            client,
            databases,
            output_dir,
            db_filter=args.db,
            sync_all=args.all,
            dry_run=args.dry_run,
            quiet=args.quiet,
            skip_fetch=args.skip_fetch,
            mark_synced=not args.no_mark_synced
        )

    return 0


if __name__ == '__main__':
    exit(main())
