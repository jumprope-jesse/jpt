---
type: link
source: notion
url: https://github.com/lackeyjb/playwright-skill
notion_type: Software Repo
tags: ['Running']
created: 2025-10-20T14:46:00.000Z
---

# GitHub - lackeyjb/playwright-skill: Claude Code Skill for browser automation with Playwright. Model-invoked - Claude autonomously writes and executes custom automation for testing and validation.

## Overview (from Notion)
- This Playwright skill can automate repetitive web tasks, freeing up time for family and personal projects.
- As a software engineer, leveraging this tool can enhance productivity in testing and validation, allowing for more creative coding.
- The ability to see automation in real-time can help demystify coding for kids, fostering their interest in technology.
- It promotes a hands-on approach to learning; you can experiment with browser automation and share insights with peers or at tech meetups.
- The focus on eco-friendly practices in tech aligns with a modern, responsible lifestyle in a bustling city like New York.
- Consider alternate views: some may argue that automation could replace jobs, emphasizing the need for balance between technology and human skills.
- The minimalist design ethos of the tool can resonate with a desire for simplicity amidst the chaos of urban life.

## AI Summary (from Notion)
A Claude Skill for browser automation using Playwright allows users to request custom automation tasks, with features like real-time visibility, zero module resolution errors, and smart cleanup. Installation options include a plugin system, manual Git clone, or downloading releases. The skill autonomously generates Playwright code for various tasks, such as testing web pages and validating forms, and provides results with screenshots and console output. Contributions are welcome, and comprehensive documentation is available for advanced usage.

## Content (from Notion)

# Playwright Skill for Claude Code

General-purpose browser automation as a Claude Skill

A Claude Skill that enables Claude to write and execute any Playwright automation on-the-fly - from simple page tests to complex multi-step flows. Packaged as a Claude Code Plugin for easy installation and distribution.

Claude autonomously decides when to use this skill based on your browser automation needs, loading only the minimal information required for your specific task.

## Features

- Any Automation Task - Claude writes custom code for your specific request, not limited to pre-built scripts
- Visible Browser by Default - See automation in real-time with headless: false
- Zero Module Resolution Errors - Universal executor ensures proper module access
- Progressive Disclosure - Concise SKILL.md with full API reference loaded only when needed
- Safe Cleanup - Smart temp file management without race conditions
- Comprehensive Helpers - Optional utility functions for common tasks
## Installation

This skill can be installed via the Claude Code plugin system or manually.

### Option 1: Via Plugin System (Recommended)

```plain text
# Add this repository as a marketplace
/plugin marketplace add lackeyjb/playwright-skill

# Install the plugin
/plugin install playwright-skill@playwright-skill

# Navigate to the skill directory and run setup
cd ~/.claude/plugins/marketplaces/playwright-skill/skills/playwright-skill
npm run setup
```

Verify installation by running /help to confirm the skill is available.

### Option 2: Manual Git Clone

Install directly from GitHub to your skills directory:

Global Installation (Available Everywhere):

```plain text
# Navigate to your Claude skills directory
cd ~/.claude/skills

# Clone the skill
git clone https://github.com/lackeyjb/playwright-skill.git

# Navigate into the skill directory (note the nested structure)
cd playwright-skill/skills/playwright-skill

# Install dependencies and Chromium browser
npm run setup
```

Project-Specific Installation:

```plain text
# Install in a specific project
cd /path/to/your/project
mkdir -p .claude/skills
cd .claude/skills
git clone https://github.com/lackeyjb/playwright-skill.git
cd playwright-skill/skills/playwright-skill
npm run setup
```

### Option 3: Download Release

1. Download the latest release from GitHub Releases
1. Extract to: 
1. Navigate to the skill directory and run setup: 
### Verify Installation

Run /help to confirm the skill is loaded, then ask Claude to perform a simple browser task like "Test if google.com loads".

## Quick Start

After installation, simply ask Claude to test or automate any browser task. Claude will write custom Playwright code, execute it, and return results with screenshots and console output.

## Usage Examples

### Test Any Page

```plain text
"Test the homepage"
"Check if the contact form works"
"Verify the signup flow"

```

### Visual Testing

```plain text
"Take screenshots of the dashboard in mobile and desktop"
"Test responsive design across different viewports"

```

### Interaction Testing

```plain text
"Fill out the registration form and submit it"
"Click through the main navigation"
"Test the search functionality"

```

### Validation

```plain text
"Check for broken links"
"Verify all images load"
"Test form validation"

```

## How It Works

1. Describe what you want to test or automate
1. Claude writes custom Playwright code for the task
1. The universal executor (run.js) runs it with proper module resolution
1. Browser opens (visible by default) and automation executes
1. Results are displayed with console output and screenshots
## Configuration

Default settings:

- Headless: false (browser visible unless explicitly requested otherwise)
- Slow Motion: 100ms for visibility
- Timeout: 30s
- Screenshots: Saved to /tmp/
## Project Structure

```plain text
playwright-skill/
├── .claude-plugin/
│   ├── plugin.json          # Plugin metadata for distribution
│   └── marketplace.json     # Marketplace configuration
├── skills/
│   └── playwright-skill/    # The actual skill (Claude discovers this)
│       ├── SKILL.md         # What Claude reads (314 lines)
│       ├── run.js           # Universal executor (proper module resolution)
│       ├── package.json     # Dependencies & setup scripts
│       └── lib/
│           └── helpers.js   # Optional utility functions
├── API_REFERENCE.md         # Full Playwright API reference (630 lines)
├── README.md                # This file - user documentation
├── CONTRIBUTING.md          # Contribution guidelines
└── LICENSE                  # MIT License

```

## Advanced Usage

Claude will automatically load API_REFERENCE.md when needed for comprehensive documentation on selectors, network interception, authentication, visual regression testing, mobile emulation, performance testing, and debugging.

## Dependencies

- Node.js >= 14.0.0
- Playwright ^1.48.0 (installed via npm run setup)
- Chromium (installed via npm run setup)
## Troubleshooting

Playwright not installed? Navigate to the skill directory and run npm run setup.

Module not found errors? Ensure automation runs via run.js, which handles module resolution.

Browser doesn't open? Verify headless: false is set. The skill defaults to visible browser unless headless mode is requested.

Install all browsers? Run npm run install-all-browsers from the skill directory.

## What is a Claude Skill?

Skills are modular capabilities that extend Claude's functionality. Unlike slash commands that you invoke manually, skills are model-invoked—Claude autonomously decides when to use them based on your request.

When you ask Claude to test a webpage or automate browser interactions, Claude discovers this skill, loads the necessary instructions, executes custom Playwright code, and returns results with screenshots and console output.

## Contributing

Contributions are welcome. Fork the repository, create a feature branch, make your changes, and submit a pull request. See CONTRIBUTING.md for details.

## Learn More

- Claude Skills - Official announcement from Anthropic
- Claude Code Skills Documentation
- Claude Code Plugins Documentation
- Plugin Marketplaces
- API_REFERENCE.md - Full Playwright documentation
- GitHub Issues
## License

MIT License - see LICENSE file for details.


