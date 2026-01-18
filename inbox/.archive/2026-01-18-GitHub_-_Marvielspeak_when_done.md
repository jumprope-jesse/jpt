---
type: link
source: notion
url: https://github.com/Marviel/speak_when_done
notion_type: Software Repo
tags: ['Running']
created: 2026-01-16T00:03:00.000Z
---

# GitHub - Marviel/speak_when_done

## Overview (from Notion)
- Imagine automating notifications for your long coding sessions—no more distractions while you juggle work and family.
- This tool can transform how you manage time, allowing you to focus on quality family moments while still keeping tabs on your work tasks.
- The voice notifications add a unique personal touch, making tech feel more human and approachable in your busy life.
- Consider how integrating AI can free up mental space, letting you think creatively rather than constantly checking for task completions.
- An alternative view: reliance on voice notifications might detract from the satisfaction of completing tasks without prompts—could it create a dependency?
- Think about how this could inspire conversations with your kids about technology and innovation, sparking their interest in STEM fields.

## AI Summary (from Notion)
An MCP server called "speak_when_done" allows your AI assistant to notify you verbally when long tasks like builds or tests are completed, eliminating the need for constant tab-switching. It requires macOS and the uv package manager for installation. Users can set it up globally or for specific projects, and it supports multiple voices for notifications. Troubleshooting tips are provided for common issues like command errors and audio playback problems.

## Content (from Notion)

# speak_when_done

An MCP server that lets your AI assistant speak to you when it's done with a task. No more tab-switching to check on long builds!

## What it does

You kick off a long task (build, test suite, deployment) and go do something else. When it's done, your AI speaks to you:

> 

> 

> 

## Prerequisites

- macOS (uses afplay for audio playback)
- uv package manager
Test that pocket-tts works:

```plain text
uvx pocket-tts generate --text "hello world" --quiet
```

## Installation

### Claude Code

Add globally (available in all projects):

```plain text
claude mcp add speak_when_done -s user -- uv run --directory /path/to/speak_when_done python server.py
```

Or project-specific:

```plain text
claude mcp add speak_when_done -- uv run --directory /path/to/speak_when_done python server.py
```

### Cursor

Add to ~/.cursor/mcp.json (global) or .cursor/mcp.json (project):

```plain text
{
  "mcpServers": {
    "speak_when_done": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/path/to/speak_when_done",
        "python",
        "server.py"
      ]
    }
  }
}
```

Then restart Cursor or reload the window.

## Usage

Once installed, your AI has access to a speak tool. Ask it to notify you when something finishes:

> 

> 

> 

### Tool: speak

Parameters:

- message (required): The message to speak aloud
- voice (optional): Voice to use (default: "alba")
## Recommended Instructions

Add to your custom instructions or CLAUDE.md:

```plain text
When using the speak_when_done MCP:
- Only use the speak tool after completing long-running tasks (builds, tests, deployments, extensive searches)
- Keep spoken messages brief and informative
- Do not use speak for routine responses or simple questions

```

## Voices

Pocket TTS supports multiple voices. The default "alba" is a natural-sounding voice. You can also provide a path to an audio file for voice cloning.

## Troubleshooting

"Command not found" error: Make sure uvx and pocket-tts are available in your PATH.

No audio playback: Ensure your macOS audio is not muted and afplay is working:

```plain text
afplay /System/Library/Sounds/Glass.aiff
```

MCP not connecting in Claude Code:

```plain text
claude mcp list
claude mcp get speak_when_done
```

MCP not connecting in Cursor: Check Settings → Features → MCP to ensure MCP is enabled, then verify your JSON config is valid.


