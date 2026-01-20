---
type: link
source: notion
url: https://github.com/mitsuhiko/playwrightess-mcp
notion_type: Software Repo
tags: ['Running']
created: 2025-08-18T13:15:00.000Z
---

# GitHub - mitsuhiko/playwrightess-mcp: An experiment of using playwright MCP via JavaScript

## Overview (from Notion)
- Experimenting with Playwright MCP could enhance your web automation capabilities, streamlining testing and development processes for your software projects.
- The persistent evaluation environment enables more efficient coding, allowing you to write and test JavaScript code seamlessly, which could save time in your development workflow.
- Given your role as a founder, leveraging such tools might lead to innovative features in your products, potentially giving you a competitive edge in the tech space.
- The focus on a JavaScript programming interface aligns with current trends in web development, making it relevant for your work and personal projects.
- The idea of open experimentation in software aligns with the startup culture of agility and iteration, encouraging a mindset of continuous improvement and learning.
- Consider alternate views on the sustainability of using such tools; while they can promote efficiency, weigh the impact of reliance on specific technologies in your long-term tech stack strategy.
- The project’s experimental nature sparks curiosity and encourages a culture of innovation, which can be inspiring for your team and help foster a creative work environment.

## AI Summary (from Notion)
An MCP server provides a persistent Playwright evaluation environment with a JavaScript programming interface. It allows for writing against the Playwright API using a tool called playwright_eval. Installation requires running npm commands, and usage involves configuring the MCP server. The project is experimental and not published, with a license under Apache 2.0.

## Content (from Notion)

# Playwrightess MCP

An MCP (Model Context Protocol) server that provides a persistent Playwright evaluation environment.

Unlike Playwright MCP this takes a very different approach. It exposes a JavaScript progrmaming interface with persistence between calls. This allows the agent to write against the playwright API with a single ubertool called playwright_eval.

This is an experiment and intentionally not published.

## Installation

```plain text
npm install
npm run build
```

## Usage

Configure the MCP server:

```plain text
{
  "mcpServers": {
    "playwriter-mcp": {
      "type": "stdio",
      "command": "node",
      "args": ["/path/to/dist/index.js"],
      "env": {}
    }
  }
}
```

## License

This is built with Claude and might not be copyrightable. Otherwise consider it Apache 2.0.

- License: Apache-2.0

