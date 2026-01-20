---
type: link
source: notion
url: https://smithery.ai/
notion_type: Software Repo
tags: ['Running']
created: 2025-01-08T02:49:00.000Z
---

# Smithery - Model Context Protocol Registry

## Overview (from Notion)
- Integration Opportunities: Leverage the Model Context Protocol to enhance software tools for productivity, potentially streamlining workflows in both personal and professional life.
- AI Enhancement: Use the capabilities of AI tools like the ones mentioned (e.g., mcp-obsidian, mcp-gsuite) to manage family schedules, automate reminders, and improve communication.
- Creative Solutions: Explore unique AI-driven solutions for everyday challenges, such as automating grocery lists or organizing family activities.
- Community Engagement: Engage with local tech communities in NYC to share insights on AI applications and exchange ideas on innovative software solutions.
- Work-Life Balance: Consider how these tools might help balance work responsibilities with family commitments, making time for both professional growth and quality family time.
- Alternative Perspectives: While AI can enhance productivity, consider the importance of human interaction and creativity in both family life and software development—ensure technology complements rather than replaces personal connections.

## AI Summary (from Notion)
Integrate various capabilities into your language model using Model Context Protocol servers, including tools for Obsidian notes, Google Workspace, browser automation, semantic web searches, and more, with detailed installation instructions provided.

## Content (from Notion)

Extend your language model with 365 capabilities via Model Context Protocol servers.

Obsidian Reader

mcp-obsidian

Read and search within a directory of Markdown notes in an Obsidian vault.

Vendor: SmitherySourceHomepage

### Configuration:

- vaultPath: The path to your Obsidian vault.
### Install Command

Integrate this tool for Claude Desktop.

```plain text
npx -y @smithery/cli install mcp-obsidian --client claude
```

Report Bug

Google Workspace Integration

mcp-gsuite

Interact with Gmail and Google Calendar. Manage multiple Google accounts, search and compose emails, and manage calendar events. Requires .gauth.json with Google Cloud OAuth2 credentials and .accounts.json with account configurations in working directory.

Playwright

@executeautomation/playwright-mcp-server

Provides browser automation capabilities using Playwright, enabling LLMs to interact with web pages, take screenshots, and execute JavaScript in a browser environment.

Exa

exa

Bring knowledge to your AI via the Exa Search API for real-time semantic web searches.

Docker

docker-mcp

Enabling seamless Docker container and compose stack management.

Sequential Thinking MCP Server

@modelcontextprotocol/server-sequential-thinking

An MCP server implementation that provides a tool for dynamic and reflective problem-solving through a structured thinking process.

YouTube Transcript Server

@kimtaeyoon83/mcp-server-youtube-transcript

Enables retrieval of transcripts from YouTube videos. Provides direct access to video captions and subtitles through a simple interface, with support for multiple languages and video URL formats.

E2B

e2b

Add code execution and interpreting capabilities to your agents.

CLI

cli-mcp-server

Command line interface for executing controlled CLI operations with robust security features including command whitelisting, path validation, and execution controls.


