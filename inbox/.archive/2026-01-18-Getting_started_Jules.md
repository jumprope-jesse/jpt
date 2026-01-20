---
type: link
source: notion
url: https://jules.google/docs/
notion_type: Software Repo
tags: ['Running']
created: 2025-06-15T02:58:00.000Z
---

# Getting started | Jules

## Overview (from Notion)
- Jules can streamline your coding tasks, allowing you to focus on balancing work and family life without getting bogged down by minor bugs or documentation.
- Its asynchronous nature means you can keep up with your dad duties while Jules handles repetitive coding tasks.
- Integrating with GitHub simplifies collaboration, which is crucial if you're leading a software company; you can oversee projects without micromanaging.
- The ease of setting up tasks and the ability to review plans before they’re executed can save you significant time, making it easier to manage both your career and personal life.
- Consider the future of AI in coding – while tools like Jules enhance productivity, think about how they could impact job roles and skills needed in software development.
- Explore the balance between leveraging automation like Jules and maintaining a human touch in coding, especially in creative problem-solving and innovation.

## AI Summary (from Notion)
Jules is an experimental coding agent that assists with bug fixes, documentation, and feature development by integrating with GitHub. To set it up, users need to log in with their Google account, connect their GitHub repositories, and start tasks by selecting a repository and writing a specific prompt. Notifications can be enabled to stay updated on task progress. Additional resources for running tasks, environment setup, and reviewing plans are available online.

## Content (from Notion)

Jules is an experimental coding agent that helps you fix bugs, add documentation, and build new features. It integrates with GitHub, understands your codebase, and works asynchronously — so you can move on while it handles the task.

This guide will walk you through setting up Jules and running your first task.

## Login

1. Visit jules.google.com
1. Sign in with your Google account.
1. Accept the privacy notice (one‑time).
## Connect GitHub

Jules needs access to your repositories in order to work.

1. Click Connect to GitHub account.
1. Complete the login flow.
1. Choose all or specific repos that you want to connect to Jules.
1. You will be redirected back to Jules. If not, try refreshing the page.
Once connected, you’ll see a repo selector where you can select the repo you want Jules to work with, and a prompt input box.

## Starting your first task

Jules runs in a virtual machine where it clones your code, installs dependencies, and modifies files.

1. Pick a repository from the repo selector.
1. Choose the branch you want Jules to work on. The default branch will be selected already. You do not have to modify this unless you want Jules to work on a specific branch.
1. Write a clear, specific prompt. For example, Add a test for "parseQueryString function in utils.js
1. (Optional) Add environment setup scripts.
1. Click Give me a plan
Once you submit a task, Jules will generate a plan. You can review and approve it before any code changes are made.

Screenshot of prompt

## Enabling notifications

You are free to leave Jules while it is running. To stay informed:

1. When prompted, enable browser notifications.
1. Go to Settings —> notifications at any time to enable or disable notifications.
You’ll be notified when the task completes or needs your input.

## What’s next?

- Running a task with Jules - Full walkthrough
- Environment setup - Make Jules smarter about your project
- Reviewing plans & feedback - how to approve and integrates
Want to dive into real-world use cases? Check out the Jules Awesome Prompts repo.


