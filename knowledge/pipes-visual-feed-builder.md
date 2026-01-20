# Pipes.digital - Visual Feed Builder

Visual programming editor for creating, filtering, and manipulating RSS/Atom/JSON feeds. Spiritual successor to Yahoo! Pipes.

**URL:** https://www.pipes.digital
**Self-hosted:** Pipes CE (AGPL) - https://github.com/nicholaswmin/pipes-ce

## What It Does

Block-based visual editor where you connect blocks to create data pipelines. Data flows through blocks from input to output, resulting in a new RSS feed.

**Input formats:** RSS, Atom, JSON feeds, HTML (scraping), plain text
**Output format:** RSS (can use `.txt` extension for content-only)

## Core Blocks

| Block | Purpose |
|-------|---------|
| **Feed** | Download RSS/Atom/JSON, auto-discovers `<link rel="alternate">` |
| **Download** | Fetch raw HTML/text (for scraping) |
| **Extract** | CSS selectors, XPath, or JSONPath to pull elements |
| **Filter** | Include/exclude items by keyword or regex |
| **Filter Language** | Keep/remove items by detected language |
| **Replace** | sed-like find/replace with regex support |
| **Combine** | Merge multiple feeds into one |
| **Unique** | Deduplicate items by guid |
| **Sort** | Reorder items by date or other fields |
| **Truncate** | Limit feed to first N items |
| **Build Feed** | Construct new feed from extracted elements |
| **ForEach** | Loop over items (e.g., fetch full text for each link) |
| **Webhook** | Receive POST data as feed input |
| **Textinput** | Dynamic user parameters for shareable pipes |

## Use Cases

- Filter noisy feeds for specific topics
- Create feeds for sites that don't have RSS
- Merge multiple sources into one feed
- Full-text RSS (fetch complete articles)
- Extract structured data from HTML tables
- Build custom feeds from scraped content

## Integrations

Built-in blocks for YouTube, Vimeo, Mixcloud, and others (via RSS Box).

## Sharing

- Pipes can be made public, liked, and forked
- Feed URLs contain randomized IDs (not easily guessable)

*Saved 2026-01-18 from Notion inbox*
