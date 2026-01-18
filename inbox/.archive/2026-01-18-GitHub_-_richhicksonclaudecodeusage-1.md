---
type: link
source: notion
url: https://github.com/richhickson/claudecodeusage
notion_type: Software Repo
tags: ['Running']
created: 2026-01-09T04:54:00.000Z
---

# GitHub - richhickson/claudecodeusage

## Overview (from Notion)
- Efficiency Booster: The Claude Usage app can help streamline your workflow by providing real-time insights into your usage limits, allowing you to optimize your coding sessions and manage resources effectively.
- Family Time: With auto-refresh and easy setup, you can focus on family activities without constantly worrying about resource limits on your projects.
- Tech Savvy: As a founder, leveraging innovative tools like this showcases your commitment to efficiency and modern solutions, potentially inspiring your team.
- Privacy Conscious: The app prioritizes user privacy, ensuring your credentials remain secure—important in today's data-driven world.
- Open Source: The ability to verify and contribute to the code aligns with a culture of transparency and collaboration, which can be a great lesson for your kids about community and sharing knowledge.
- Urban Lifestyle: Living in NYC, utilizing such tools can help balance the fast-paced city life with your professional commitments, enhancing both personal and professional productivity.
- Alternative View: Consider the trade-offs of relying on third-party apps; while they enhance productivity, they also introduce dependencies that could affect your workflow if the API changes unexpectedly.

## AI Summary (from Notion)
A lightweight macOS menubar app that displays Claude Code usage limits with features like auto-refresh, color-coded status, and session/weekly limit displays. Installation instructions include downloading from releases or building from source. The app reads OAuth credentials from macOS Keychain and queries an API for usage data, ensuring privacy by not sending data elsewhere. Troubleshooting tips are provided, and contributions are welcomed under the MIT License.

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


