---
type: link
source: notion
url: https://system.surf/
notion_type: Software Repo
tags: ['Running']
created: 2026-01-06T15:24:00.000Z
---

# SYSTEM — docs

## Overview (from Notion)
- Automate mundane tasks on your Mac, freeing up time for family and creative projects.
- Use natural language commands to control your environment, making tech more accessible for everyone.
- Cloudflare integration ensures security, allowing you to focus on what matters without worrying about vulnerabilities.
- The split architecture (Cloudflare Workers and local Mac) provides a robust solution that balances performance and security.
- Leverage music and messaging tools to enhance your daily routine, making life smoother and more enjoyable.
- Explore the potential of AI-driven scheduling and task management to keep both personal and professional life organized.
- Consider the implications of zero-trust security in a world where data privacy is paramount, especially as a business owner.
- Embrace the minimalist design philosophy, which can inspire a more organized and less cluttered home/work environment.
- Reflect on how this tech fits into the broader narrative of work-life balance, especially in a fast-paced city like NYC.

## AI Summary (from Notion)
SYSTEM allows users to control their Mac using natural language through a split architecture with an Agent running on Cloudflare Workers and a Bridge on the local machine. It includes setup instructions, tools for automation, music control, messaging, and system management, with a focus on security and integration with Raycast extensions. Users can schedule tasks, manage files, and utilize various core tools for enhanced functionality.

## Content (from Notion)

Control your Mac from anywhere using natural language. Built with Cloudflare Agents SDK for intelligent scheduling, memory, and tool orchestration.

## quick start

### 1. clone and install

```plain text
git clone https://github.com/ygwyg/system
cd system && npm install
```

### 2. run setup wizard

```plain text
npm run setup
```

Interactive setup: Anthropic API key, Raycast extensions, remote access.

### 3. start system

```plain text
npm start
```

Starts bridge, tunnel, and opens the agent UI.

## architecture

SYSTEM uses a split architecture for security: the Agent (brain) runs on Cloudflare Workers, while the Bridge (body) runs locally on your Mac.

```plain text
┌───────────────────────────────────────────────────────┐
│                        USER                           │
│                    (phone/browser)                    │
└─────────────────────┬─────────────────────────────────┘
                      │ HTTPS
                      ▼
┌───────────────────────────────────────────────────────┐
│                  AGENT (Brain)                        │
│              Cloudflare Workers                       │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐    │
│  │   Claude    │  │   State     │  │  Schedules  │    │
│  │     AI      │  │  (D.O.)     │  │   (D.O.)    │    │
│  └─────────────┘  └─────────────┘  └─────────────┘    │
└─────────────────────┬─────────────────────────────────┘
                      │ Tunnel
                      ▼
┌───────────────────────────────────────────────────────┐
│                  BRIDGE (Body)                        │
│                Your Mac (local)                       │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐    │
│  │ AppleScript │  │    Shell    │  │   Raycast   │    │
│  └─────────────┘  └─────────────┘  └─────────────┘    │
└───────────────────────────────────────────────────────┘

```

## authentication

All requests require an API secret via Bearer token or query parameter.

```plain text
// Header
Authorization: Bearer <api_secret>

// Or query parameter
?token=<api_secret>
```

## chat

Send natural language commands to control your Mac.

```plain text
{
  "message": "Play some jazz music"
}
```

### response

```plain text
{
  "message": "Playing jazz on Apple Music",
  "actions": [{
    "tool": "music_play",
    "args": { "query": "jazz" },
    "success": true,
    "result": "Now playing: Jazz Vibes"
  }]
}
```

Clear conversation history and state.

## schedules

Schedule one-time or recurring tasks using natural language or cron syntax.

```plain text

  }]
}
```

Cancel a scheduled task by ID.

## state

The agent maintains persistent state including preferences and conversation history.

```plain text
{
  "preferences": { "wife": "Jane" },
  "historyLength": 12,
  "scheduleCount": 2
}
```

## core tools

Foundational tools for Mac automation.

## music

Control Apple Music playback.

## messaging

Send iMessages with human-in-the-loop confirmation.

When you say "text my wife hello", SYSTEM will: 1) resolve "wife" from preferences, 2) search contacts, 3) ask for confirmation before sending.

## system

Control system settings, get status, manage files and apps.

### calendar & reminders

### display & focus

### system status

## notes

Read and write Apple Notes.

## files

Search and manage files via Finder.

## shortcuts

Run Apple Shortcuts.

## raycast extensions

Execute Raycast extensions for powerful integrations. SYSTEM scans your installed extensions and makes them available as tools.

### how it works

During npm run setup, SYSTEM scans your Raycast extensions folder and presents compatible commands for you to enable. Each enabled command becomes a dedicated tool.

```plain text
Raycast Extension              SYSTEM Tool
─────────────────              ───────────
spotify-player/play      →     spotify_play
linear/create-issue      →     linear_create_issue
slack/send-message       →     slack_send_message

```

### extension discovery

SYSTEM looks in ~/.config/raycast/extensions/ and reads each extension's package.json to find commands. Only commands with mode: "no-view" or mode: "view" are compatible.

### compatible extension types

### popular extensions that work well

### tool naming

Tools are named as {extension}_{command} with hyphens replaced by underscores:

```plain text
// Extension: linear, Command: create-issue-for-myself
Tool name: linear_create_issue_for_myself

// Extension: spotify-player, Command: play
Tool name: spotify_player_play
```

### using raycast tools

Once enabled, just ask naturally:

- "Create a Linear issue for fixing the login bug"
- "Send a Slack message to #general saying hello"
- "Play Daft Punk on Spotify"
- "Add 'buy groceries' to my Todoist"
### generic raycast tool

For extensions not in your enabled list, use the generic raycast tool:

```plain text
{
  "extension": "spotify-player",
  "command": "play",
  "arguments": { "query": "jazz" }
}
```

### deep link format

Under the hood, SYSTEM uses Raycast deep links:

```plain text
raycast://extensions/{author}/{extension}/{command}?arguments={json}
```

### troubleshooting

If an extension isn't showing in setup, make sure it's installed via Raycast Store, not manually. Check ~/.config/raycast/extensions/.

This usually means the command requires UI interaction (forms, selections). These commands aren't fully compatible. Try a different command from the same extension.

Many extensions require you to authenticate in Raycast first. Open Raycast and run the command manually once to complete OAuth/login flows.

### re-scanning extensions

If you install new Raycast extensions, run setup again to add them:

```plain text
npm run setup
```

Your existing configuration will be preserved—you'll just see new extensions to enable.

## bridge api

Direct API to the local bridge. Used by the agent, but also available for custom integrations.

List all available tools on the bridge.

```plain text
{
  "tool": "open_app",
  "args": { "app": "Safari" }
}
```

Check bridge status.

## websocket

Real-time updates for scheduled tasks and notifications.

```plain text
// Connect to WebSocket
const ws = new WebSocket('wss://your-agent.workers.dev/ws?token=...');

ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  // Types: scheduled_result, notification, bridge_status
  console.log(data.type, data.payload);
};
```

## security

SYSTEM is designed with security as a priority.

### cloudflare access (recommended)

If you deploy to Cloudflare Workers, add Cloudflare Access for Zero Trust authentication at the edge — before requests even reach your agent.

While the API secret provides application-level auth, Cloudflare Access adds network-level protection. Only authenticated users can reach your agent at all.

### setup via dashboard

1. Navigate to Access → Applications → Add an application
1. Select Self-hosted and enter your worker URL
1. Create an access policy (e.g., email = you@example.com)
1. Save — users must now authenticate before accessing SYSTEM
### automation (terraform)

```plain text
# Note: wrangler doesn't support Access config directly
# Use Terraform for infrastructure-as-code

resource "cloudflare_access_application" "system" {
  zone_id          = var.zone_id
  name             = "SYSTEM"
  domain           = "your-agent.workers.dev"
  session_duration = "24h"
}

resource "cloudflare_access_policy" "allow_me" {
  application_id = cloudflare_access_application.system.id
  zone_id        = var.zone_id
  name           = "Allow specific emails"
  precedence     = 1
  decision       = "allow"

  include {
    email = ["you@example.com"]
  }
}
```

Cloudflare Access is configured separately from Workers deployment. The wrangler CLI doesn't manage Access policies — use the dashboard or Terraform.


