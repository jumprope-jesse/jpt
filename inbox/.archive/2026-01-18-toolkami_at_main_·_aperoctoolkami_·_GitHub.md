---
type: link
source: notion
url: https://github.com/aperoc/toolkami/tree/main
notion_type: Software Repo
tags: ['Running']
created: 2025-05-07T02:14:00.000Z
---

# toolkami/ at main · aperoc/toolkami · GitHub

## Overview (from Notion)
- Toolkami offers a streamlined approach to AI, which can enhance your efficiency as a software engineer and entrepreneur.
- The minimalistic design with seven essential tools may resonate with your busy lifestyle, allowing you to focus on what truly matters in your projects.
- The "Turbo mode" feature could be particularly useful for rapid prototyping or testing ideas quickly without unnecessary interruptions.
- The emphasis on hands-free operation can help you manage tasks while balancing family responsibilities, enabling multitasking effectively.
- The integration of OpenAI and Anthropic support suggests potential for innovative applications, perhaps in your startups or personal projects.
- The roadmap hints at future capabilities, which means investing time in understanding Toolkami now could position you advantageously as it evolves.
- An alternate view could be to consider whether a minimalistic tool can meet the more complex demands of a growing tech environment—are there features that might be lacking?
- The community and support around such tools can provide networking opportunities and collaboration potential with other tech professionals in NYC.

## AI Summary (from Notion)
Toolkami is a minimal AI agent utilizing seven tools, featuring Turbo mode for full autonomy and hot-reloading for self-modification. Quickstart installation instructions are provided, along with a roadmap for future API compatibility and system prompt guidelines.

## Content (from Notion)

# Toolkami

Seven tools is all you need. A minimal AI agent that just works, using only seven tools. Comes with hands-free Turbo mode and Hot-reloading for self-modification.

Watch it in action:

Go Turbo: The standard pace is for chumps. Have it go full autonomous by disabling ask.

```plain text
# @mcp.tool()
async def ask(question: str) -> str:
```

## Quickstart

Devcontainer (.devcontainer) included and useable, otherwise proceed with manual install.

Install UV:

```plain text
# OSX/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Start the MCP server:

```plain text
# --reload enables Hot-reloading
cd servers && PYTHONPATH=. uv run app.py --reload

# For Browser Use (on linux)
# sudo apt-get update && sudo apt-get install -y  libglib2.0-0t64 libnss3 libnspr4 libdbus-1-3 libatk1.0-0t64 libatk-bridge2.0-0t64 libcups2t64 libxkbcommon0 libatspi2.0-0t64 libxcomposite1 libxdamage1 libxfixes3 libxrandr2 libgbm1 libpango-1.0-0 libcairo2 libasound2t64
# cd servers && uv run sync && uv run patchright install chromium
```

Start the MCP client (self-executable UV script):

```plain text
./clients/gemini_client.py http://localhost:8081/sse # --debug
```

## Roadmap

- OpenAI compatible API, Anthropic support
- System prompt guidelines with single file project templates
## Limitations

- This is a customisable sharp tool for now. Guardrails will only be implemeted over time.

