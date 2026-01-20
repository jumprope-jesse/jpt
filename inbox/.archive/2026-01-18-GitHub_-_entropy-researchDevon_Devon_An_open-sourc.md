---
type: link
source: notion
url: https://github.com/entropy-research/Devon
notion_type: Software Repo
tags: ['Running']
created: 2024-05-20T03:55:00.000Z
---

# GitHub - entropy-research/Devon: Devon: An open-source pair programmer

## AI Summary (from Notion)
- Project Overview: Devon is an open-source pair programming tool developed by entropy-research.
- Creation Date: The project was created on May 20, 2024.
- Current Status: Not started.
- Installation Requirements:
- Requires node.js, npm, and pipx.
- Needs an API key from either Anthropic or OpenAI.
- Installation Commands:
- Provides a simple command for installation via a script or using pipx and npm.
- Running the Agent:
- Users must set their API key as an environment variable before running the command.
- The agent operates only within the directory it is initiated from.
- Features:
- Multi-file editing, code exploration, config and test writing, bug fixing, and architecture exploration.
- Limitations:
- Minimal support for non-Python languages.
- Requires specification of files for changes sometimes.
- Goals:
- Aim to support multiple models, launch a plugin system, and create a self-hostable Electron app.
- Past Milestones:
- Lists significant achievements from April to May 2024, including the launch of various agent versions.
- Contribution:
- Encourages community contributions in core functionality, research, feedback, and testing.
- Feedback Mechanism:
- Users are encouraged to provide feedback via Discord or GitHub issues.
- Telemetry:
- Collects basic telemetry to improve user experience, which can be disabled by setting an environment variable.
- Community Engagement:
- Invites users to join their Discord server for communication and feedback.
- License:
- Distributed under the Apache 2.0 License.

## Content (from Notion)

# Devon: An open-source pair programmer

demo.mp4

# Installation

## Prerequisites

1. node.js and npm
1. pipx, if you don't have this go here
1. Anthropic API Key or OpenAI API key
## Installation commands

To install, simply run:

```plain text
curl -sSL https://raw.githubusercontent.com/entropy-research/Devon/main/install.sh | bash
```

Or to install using pipx + npm:

```plain text
pipx install devon_agent
npm install -g devon-tui
```

This installs the Python backend, and the cli command to run the tool

### Thats it! Happy building :)

# Running the agent

Navigate to your project folder and open the terminal.

Set your Anthropic API or OpenAI API key as an environment variable:

```plain text
export ANTHROPIC_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#OR

export OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Then to run, the command is:

```plain text
devon
```

It's as easy as that.

Note

Don't worry, the agent will be able to only access files and folders in the directory you started it from. You can also correct it while it's performing actions.

To run in debug mode, the command is:

```plain text
devon --debug
```

# Features

- Multi-file editing
- Codebase exploration
- Config writing
- Test writing
- Bug fixing
- Architecture exploration
### Limitations

- Minimal functionality for non-Python languages
- Sometimes have to specify the file where you want the change to happen
# Progress

### This project is still super early and we would love your help to make it great!

### Current goals

- Multi-model support
- Launch plugin system for tool and agent builders
- Create self-hostable Electron app
- Set SOTA on SWE-bench Lite
> 

### Star history

### Past milestones

- May 10, 2024 - Complete interactive agent v0.1.0
- May 10, 2024 - Add steerability features
- May 8, 2024 - Beat AutoCodeRover on SWE-Bench Lite
- Mid April, 2024 - Add repo level code search tooling
- April 2, 2024 - Begin development of v0.1.0 interactive agent
- March 17, 2024 - Launch non-interactive agent v0.0.1
## Current development priorities

1. Improve context gathering and code indexing abilities ex: 
1. Add alternative models and agents to: 
1. Introduce Electron app and new UI
# How can I contribute?

Devon and the entropy-research org are community-driven, and we welcome contributions from everyone! From tackling issues to building features to creating datasets, there are many ways to get involved:

- Core functionality: Help us develop the core agents, user experience, tool integrations, plugins, etc.
- Research: Help us research agent performance (including benchmarks!), build data pipelines, and finetune models.
- Feedback and Testing: Use Devon, report bugs, suggest features, or provide feedback on usability.
For details, please check CONTRIBUTING.md.

If you would like to contribute to the project, please fill out our Contribution Form

# Feedback

We would love feedback! Feel free to drop us a note on our Discord in the #feedback channel, or create issues!

We collect basic event type (i.e. "tool call") and failure telemetry to solve bugs and improve the user experience, but if you want to reach out, we would love to hear from you!

To disable telemetry, set the environment variable DEVON_TELEMETRY_DISABLED to true

```plain text
export DEVON_TELEMETRY_DISABLED=true
```

# Community

Join our Discord server and say hi! Discord

# License

Distributed under the Apache 2.0 License. See LICENSE for more information.


