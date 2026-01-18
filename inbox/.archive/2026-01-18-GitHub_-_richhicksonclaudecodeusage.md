---
type: link
source: notion
url: https://github.com/richhickson/claudecodeusage
notion_type: Software Repo
tags: ['Running']
created: 2026-01-09T04:56:00.000Z
---

# GitHub - richhickson/claudecodeusage

## Overview (from Notion)
- The Claude Usage app simplifies monitoring your code usage, freeing up time for family and work.
- Features like auto-refresh and color-coded alerts help you stay informed without constant checking.
- Minimal resource use means it won't slow down your workflow, ideal for busy days juggling parenting and projects.
- The open-source nature allows you to customize it, aligning with your innovative mindset as a founder.
- Privacy-focused, ensuring your credentials are secure, which resonates with the importance of data security in today's climate.
- Alternate view: While useful, reliance on undocumented APIs could present risks; consider traditional methods for critical tasks.
- Living in NYC, the app can enhance your tech-savvy lifestyle, integrating seamlessly into your digital ecosystem.

## AI Summary (from Notion)
A lightweight macOS menubar app that displays Claude Code usage limits with features like auto-refresh, color-coded status, and session/weekly limit displays. Installation options include downloading the app or building from source. It reads OAuth credentials from macOS Keychain and queries an API for usage data, ensuring privacy by not sending credentials outside the machine. Troubleshooting tips and contributing guidelines are provided, along with a disclaimer that it's an unofficial tool using an undocumented API.

## Content (from Notion)

# Claude Usage

A lightweight macOS menubar app that displays your Claude Code usage limits at a glance.

Built by @richhickson

## Features

- 🔄 Auto-refresh every 2 minutes
- 🚦 Color-coded status - Green (OK), Yellow (>70%), Red (>90%)
- ⏱️ Time until reset for both session and weekly limits
- 📊 Session & Weekly limits displayed together
- 🪶 Lightweight - Native Swift, minimal resources
## Installation

### Download

1. Go to Releases
1. Download ClaudeUsage.zip
1. Unzip and drag ClaudeUsage.app to your Applications folder
1. Open the app (you may need to right-click → Open the first time)
### Build from Source

```plain text
git clone https://github.com/YOUR_USERNAME/claude-usage.git
cd claude-usage
open ClaudeUsage.xcodeproj
```

Then build with ⌘B and run with ⌘R.

## Requirements

- macOS 13.0 (Ventura) or later
- Claude Code CLI installed and logged in
## Setup

1.  
1.  
1. 
## How It Works

Claude Usage reads your Claude Code OAuth credentials from macOS Keychain and queries the usage API endpoint at api.anthropic.com/api/oauth/usage.

Note: This uses an undocumented API that could change at any time. The app will gracefully handle API changes but may stop working if Anthropic modifies the endpoint.

## Privacy

- Your credentials never leave your machine
- No analytics or telemetry
- No data sent anywhere except Anthropic's API
- Open source - verify the code yourself
## Screenshots

## Troubleshooting

### "Not logged in to Claude Code"

Run claude in Terminal and complete the login flow.

### App doesn't appear in menubar

Check if the app is running in Activity Monitor. Try quitting and reopening.

### Usage shows wrong values

Click the refresh button (↻) in the dropdown. If still wrong, your Claude Code session may have expired - run claude again.

## Contributing

PRs welcome! Please open an issue first to discuss major changes.

## License

MIT License - do whatever you want with it.

## Disclaimer

This is an unofficial tool not affiliated with Anthropic. It uses an undocumented API that may change without notice.

Made by @richhickson


