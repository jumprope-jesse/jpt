---
type: link
source: notion
url: https://opencode.ai/docs
notion_type: Software Repo
tags: ['Running']
created: 2026-01-05T15:45:00.000Z
---

# Intro | OpenCode

## Overview (from Notion)
- OpenCode can streamline your coding process, allowing you to focus more on your family and less on repetitive tasks.
- The integrated AI can help you mentor your kids in coding by simplifying complex concepts, creating a fun learning environment.
- Explore its potential for collaborative projects, making it easier to involve friends or family in tech-related activities.
- The adaptability of OpenCode to different programming environments means you can work on personal projects or your startup without being tethered to a single setup.
- Unique design features like themes and customizable keybinds can personalize your coding experience and make it more enjoyable.
- Consider the ethical implications of AI in coding; while it enhances productivity, think about how it shapes the future of work and learning for your children.
- Alternative view: Relying too heavily on AI tools could diminish fundamental coding skills; balance is key in leveraging technology while fostering critical thinking.

## AI Summary (from Notion)
OpenCode is an open-source AI coding agent available as a terminal interface, desktop app, or IDE extension. To use it, install via various methods like Homebrew or Docker, and configure API keys for LLM providers. Users can initialize OpenCode for projects, create plans for new features, and interact with the agent to explain code, build features, or undo changes. Customization options include themes, keybinds, and commands to enhance user experience.

## Content (from Notion)

OpenCode is an open source AI coding agent. It’s available as a terminal-based interface, desktop app, or IDE extension.

OpenCode TUI with the opencode theme

Let’s get started.

To use OpenCode in your terminal, you’ll need:

1.  
1. 
The easiest way to install OpenCode is through the install script.

Terminal window

You can also install it with the following commands:

- 
- 
- 
-  
-  
-  
-  
Support for installing OpenCode on Windows using Bun is currently in progress.

You can also grab the binary from the Releases.

With OpenCode you can use any LLM provider by configuring their API keys.

If you are new to using LLM providers, we recommend using OpenCode Zen. It’s a curated list of models that have been tested and verified by the OpenCode team.

1. 
1. 
Alternatively, you can select one of the other providers. Learn more.

Now that you’ve configured a provider, you can navigate to a project that you want to work on.

Terminal window

And run OpenCode.

Next, initialize OpenCode for the project by running the following command.

This will get OpenCode to analyze your project and create an AGENTS.md file in the project root.

This helps OpenCode understand the project structure and the coding patterns used.

You are now ready to use OpenCode to work on your project. Feel free to ask it anything!

If you are new to using an AI coding agent, here are some examples that might help.

You can ask OpenCode to explain the codebase to you.

This is helpful if there’s a part of the codebase that you didn’t work on.

You can ask OpenCode to add new features to your project. Though we first recommend asking it to create a plan.

1.      
1.   
1.   
For more straightforward changes, you can ask OpenCode to directly build it without having to review the plan first.

```plain text
handled in the /notes route in @packages/functions/src/notes.ts and implementthe same logic in @packages/functions/src/settings.ts
```

You want to make sure you provide a good amount of detail so OpenCode makes the right changes.

Let’s say you ask OpenCode to make some changes.

But you realize that it is not what you wanted. You can undo the changes using the /undo command.

OpenCode will now revert the changes you made and show your original message again.

From here you can tweak the prompt and ask OpenCode to try again.

Or you can redo the changes using the /redo command.

The conversations that you have with OpenCode can be shared with your team.

This will create a link to the current conversation and copy it to your clipboard.

Here’s an example conversation with OpenCode.

And that’s it! You are now a pro at using OpenCode.

To make it your own, we recommend picking a theme, customizing the keybinds, configuring code formatters, creating custom commands, or playing around with the OpenCode config.


