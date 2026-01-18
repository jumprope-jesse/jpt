---
type: link
source: notion
url: https://github.com/libragen/libragen
notion_type: Software Repo
tags: ['Running']
created: 2026-01-15T13:07:00.000Z
---

# GitHub - libragen/libragen: Create private, local RAG libraries that work offline—no API keys, no cloud services. Share them as single files your whole team can use.

## Overview (from Notion)
- Leverage local RAG libraries to provide your family with accurate information—whether it's about school projects or home improvement tasks—without relying on outdated or incorrect online data.
- Use the private and secure nature of libragen to manage sensitive family documents, ensuring that everything stays within your home network.
- Automate documentation for your startup, making internal policies and technical documentation easily accessible for your team, enhancing productivity.
- Consider integrating AI tools that utilize your curated libraries, streamlining communication and reducing repetitive questions among team members.
- Explore ways to make your children's educational resources searchable via AI, fostering a more interactive and engaging learning environment.
- Think about the potential to create a shared library for family recipes or home maintenance tips, ensuring everyone is aligned and informed.
- Alternate view: Some may argue that relying too heavily on AI for documentation can lead to dependency, diminishing critical thinking and problem-solving skills. Balance tech use with hands-on learning and family discussions.

## AI Summary (from Notion)
Create private, local RAG libraries from documentation that work offline without API keys or cloud services. Libraries are shareable SQLite files that ensure AI agents use authoritative, up-to-date information, reducing hallucinations. Key features include building libraries from local docs or Git repositories, connecting AI tools, and making internal documentation searchable. Additional functionalities include chatting with Obsidian vaults and auto-building libraries in CI.

## Content (from Notion)

# libragen

(pronounced "LIB-ruh-jen")

Ground your AI in real documentation—not stale training data

Documentation • Getting Started • CLI • MCP Server • Discussions

Create private, local RAG libraries from any documentation. Libraries are single SQLite files you can share with your team—no cloud, no API keys.

## Why libragen?

- Stop hallucinations — Give AI agents authoritative docs to cite instead of guessing
- Always current — Rebuild when docs change; your AI gets the latest APIs
- Private & local — Everything runs on your machine, nothing leaves your network
- Shareable — Single .libragen files work anywhere
## Packages

## Quick Start

### 1. Build a library

```plain text
# From local docs
npx @libragen/cli build ./your-private-docs --name company-docs

# From a git repository
npx @libragen/cli build https://github.com/anthropics/anthropic-cookbook --name anthropic-cookbook
```

### 2. Connect your AI

```plain text
npx -y install-mcp @libragen/mcp
```

Restart your AI tool (Claude Desktop, VS Code, Cursor, etc.). Libraries in your global directory are now searchable.

### 3. Ask questions

> 

> 

> 

Your AI retrieves relevant documentation and responds with accurate, cited answers—not hallucinated guesses from 2-year-old training data.

## What else can you do?

- Chat with your Obsidian vault — Tutorial →
- Make your company's internal docs searchable — Runbooks, wikis, policies—all queryable by AI
- Create a shared library for your team — One .libragen file, everyone's on the same page
- Auto-build libraries in CI — Use the GitHub Action to generate .libragen files on every push
Full documentation →

## License

MIT — see LICENSE for details.


