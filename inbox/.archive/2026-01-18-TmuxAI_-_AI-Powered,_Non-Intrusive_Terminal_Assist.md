---
type: link
source: notion
url: https://tmuxai.dev/
notion_type: Software Repo
tags: ['Running']
created: 2025-04-28T03:38:00.000Z
---

# TmuxAI - AI-Powered, Non-Intrusive Terminal Assistant

## Overview (from Notion)
- Efficiency Boost: TmuxAI can streamline your coding sessions, allowing you to focus more on development and less on searching for commands or managing terminal windows.
- Learning Aid: It serves as a real-time tutor, helping you understand complex commands and workflows, which can be beneficial when mentoring junior developers.
- Work-Life Balance: By automating repetitive tasks, you can reclaim time to spend with family or pursue personal interests, reducing work-related stress.
- Flexible Collaboration: The assistant's context-awareness mimics real-life collaboration, enhancing remote teamwork, especially crucial for a founder managing a growing team.
- Open Source Advantage: As a software engineer, the open-source nature allows customization to fit your specific needs, promoting innovation within your projects.
- Urban Tech Integration: Living in NYC, TmuxAI can help manage projects that require rapid iteration, aligning with the fast-paced tech scene of the city.
- Alternate Viewpoints: Some may argue that reliance on AI tools could hinder deep learning and mastery of terminal commands, emphasizing the balance between using such tools and maintaining foundational skills.

## AI Summary (from Notion)
TmuxAI is a non-intrusive terminal assistant that enhances productivity by providing context-aware help in real-time across terminal panes, requiring no special setup. It supports various terminal environments and offers features like command tracking and proactive assistance, available as open-source software.

## Content (from Notion)

Tmux
AI

## AI-Powered, Non-Intrusive Terminal Assistant

TmuxAI is a non-intrusive terminal assistant that works alongside you in a tmux window. TmuxAI's design philosophy mirrors the way humans collaborate at the terminal. Just as a colleague sitting next to you, TmuxAI observes your screen, understand context from what's visible, and helps accordingly.

curl -fsSL https://get.tmuxai.dev | bash

$tmuxai find large files and cleanup some space

TmuxAI » I'll help you find large files taking up space in this directory.

TmuxAI » find . -type f -size +100M -exec du -h {} \; | sort -rh | head -5

Do you want to execute this command? [Y]es/No/Edit:

TmuxAI » Found several large files in node_modules and logs directories.

TmuxAI » rm -i ./logs/debug-*.log

Do you want to execute this command? [Y]es/No/Edit: _

### 01 FEATURES

CONTEXT-AWARE TERMINAL ASSISTANCE

TmuxAI reads and understands what's displayed across all your terminal panes in real-time, providing intelligent help based on what you're actually working on.

ZERO-CONFIGURATION SETUP

Works instantly with your existing tmux setup without requiring special shells, wrappers, or terminal emulators. Just install and run.

UNIVERSAL TERMINAL COMPATIBILITY

Works with nested shells, SSH connections, database CLIs, network equipment shells (Cisco IOS, Juniper, etc), and any other text-based terminal interface.

Enhances command tracking with custom shell prompts that provide exact command completion detection and exit code awareness for more accurate assistance.

Transforms TmuxAI into a proactive assistant that monitors your terminal activity and offers improvements or explanations based on your specified goals.

Available as open source software. Use TmuxAI for free and adapt it to your workflow.

### 02 DEMO

TmuxAI»start docker container mysql and then connect to mysql shell.

First I'll start the container:

TmuxAI»docker run --name mysql_container -e MYSQL_ROOT_PASSWORD=password -d mysql:latest

Do you want to execute this command? [Y]es/No/Edit:

TmuxAI»docker exec -it mysql_container mysql -u root -p

Do you want to execute this command? [Y]es/No/Edit:

TmuxAI» I'll now send the password to the mysql shell.

Welcome to the MySQL monitor. Commands end with ; or \g.

Your MySQL connection id is 9

Server version: 8.2.0 MySQL Community Server - GPL

Copyright (c) 2000, 2023, Oracle and/or its affiliates.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

TmuxAI


