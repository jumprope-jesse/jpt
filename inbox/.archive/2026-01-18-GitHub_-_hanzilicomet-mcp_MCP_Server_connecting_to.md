---
type: link
source: notion
url: https://github.com/hanzili/comet-mcp
notion_type: Software Repo
tags: ['Running']
created: 2026-01-07T16:14:00.000Z
---

# GitHub - hanzili/comet-mcp: MCP Server connecting to Perplexity Comet browser

## Overview (from Notion)
- Enhanced Productivity: This tool bridges Claude Code with Perplexity Comet, streamlining research and task management, freeing up time for family and other pursuits.
- Agentic Browsing: The ability to give commands and have an AI navigate the web can simplify complex tasks, making it easier to stay informed without getting bogged down in details.
- Innovative Learning: Using AI for research can lead to new insights and ideas, crucial for a founder looking to stay ahead in a competitive market.
- Dynamic Problem Solving: This tech allows for real-time task monitoring, which can enhance decision-making processes in both personal and professional contexts.
- Community Engagement: Contributing to or exploring open-source projects like this can foster connections with other tech enthusiasts and innovators, expanding your network.
- Alternate View: Consider the balance between reliance on AI and maintaining critical thinking skills; over-dependence could limit creative problem-solving.
- Future Trends: Staying updated with AI advancements can provide a competitive edge for your business, especially in a tech-savvy city like New York.

## AI Summary (from Notion)
An MCP server connects Claude Code to Perplexity Comet, enabling advanced web browsing and research capabilities. It addresses limitations of existing tools by providing dynamic content interaction and a purpose-built AI for web research. Users can configure Claude Code to utilize Comet for tasks, with various tools available for task management and troubleshooting. Requirements include Node.js and the Perplexity Comet Browser.

## Content (from Notion)

# comet-mcp

Give Claude Code a browser that thinks.

An MCP server that connects Claude Code to Perplexity Comet - enabling agentic web browsing, deep research, and real-time task monitoring.

## Why?

Existing web tools for Claude Code fall short:

- WebSearch/WebFetch only return static text - no interaction, no login, no dynamic content
- Browser automation MCPs (like browser-use) are agentic but use a generic LLM to control a browser - less polished, more fragile
Comet is Perplexity's native agentic browser - their AI is purpose-built for web research, deeply integrated with search, and battle-tested. Give it a goal, it figures out how to get there.

comet-mcp bridges Claude Code and Comet: Claude's coding intelligence + Perplexity's web intelligence.

## Quick Start

### 1. Configure Claude Code

Add to ~/.claude.json or .mcp.json:

```plain text
{
  "mcpServers": {
    "comet-bridge": {
      "command": "npx",
      "args": ["-y", "comet-mcp"]
    }
  }
}
```

### 2. Start Comet Browser

Download Perplexity Comet and launch with remote debugging:

```plain text
# macOS
/Applications/Comet.app/Contents/MacOS/Comet --remote-debugging-port=9222
```

### 3. Use in Claude Code

```plain text
You: "Use Comet to research the top AI frameworks in 2025"
Claude: [connects to Comet, delegates research, monitors progress, returns results]

```

## Tools

## Architecture

```plain text
Claude Code <-> MCP <-> comet-mcp <-> CDP <-> Comet Browser <-> Perplexity AI

```

## Requirements

- Node.js 18+
- Perplexity Comet Browser
- Claude Code (or any MCP client)
## Troubleshooting

"Cannot connect to Comet"

- Make sure Comet is running with -remote-debugging-port=9222
- Check if port 9222 is available
"Tools not showing in Claude"

- Restart Claude Code after config changes
## License

MIT

Report Issues · Contribute


