---
type: link
source: notion
url: https://github.com/edverma/git-smart-squash
notion_type: Software Repo
tags: ['Running']
created: 2025-06-20T04:09:00.000Z
---

# GitHub - edverma/git-smart-squash

## Overview (from Notion)
- Git Smart Squash can save you significant time by automatically organizing messy commit histories, making your code reviews smoother and more efficient.
- The AI-driven tool simplifies collaboration with your team, allowing you to focus on building features rather than managing commit logistics.
- Its ability to provide clean, conventional commit messages can enhance communication within your development team and improve project documentation.
- The flexibility of using either local or cloud AI providers gives you control over privacy and cost, which is important for a founder managing budgets.
- You can integrate this tool into your daily workflow, helping to instill better practices among your team and set a standard for clean code management.
- Alternate viewpoints might argue against reliance on AI tools, emphasizing the importance of understanding commit history manually to maintain a deep connection to the codebase.
- Consider how this tool reflects the broader trend of AI integration in software development, potentially reshaping roles and responsibilities in tech.

## AI Summary (from Notion)
Git Smart Squash uses AI to organize messy commit histories into clean, logical commits, saving time before PR reviews. It offers a quick setup, multiple AI provider options, and ensures safety with dry runs and backup branches. Users can customize configurations and troubleshoot common issues easily.

## Content (from Notion)

# Git Smart Squash

Use AI to transform your messy commit history into clean, logical commits that reviewers will love

## Why Use Git Smart Squash?

Ever spent 30 minutes reorganizing commits before a PR? We've all been there. Git Smart Squash uses AI to automatically organize your changes into logical, well-structured commits in seconds.

### What It Does

Before (your typical feature branch):

```plain text
* 7f8d9e0 fix tests
* 6c5b4a3 typo
* 5a4b3c2 more auth changes
* 4d3c2b1 WIP: working on auth
* 3c2b1a0 update tests
* 2b1a0f9 initial auth implementation

```

After (AI-organized commits):

```plain text
* a1b2c3d feat: implement complete authentication system with JWT tokens
* e4f5g6h test: add comprehensive test coverage for auth endpoints

```

The AI analyzes your entire diff and groups related changes together, creating clean commit messages that follow conventional commit standards.

## Quick Start (2 minutes)

### 1. Install

```plain text
pip install git-smart-squash
```

### 2. Set up AI (choose one)

Option A: Local AI (Free & Private) - Default for Privacy

```plain text
# Install Ollama from https://ollama.com
ollama serve
ollama pull devstral
```

Option B: Cloud AI (if you have API keys)

```plain text
export OPENAI_API_KEY="your-key"      # or
export ANTHROPIC_API_KEY="your-key"   # or
export GEMINI_API_KEY="your-key"
```

### 3. Use It!

```plain text
cd your-git-repo
git checkout your-feature-branch

# Run it - shows the plan and asks for confirmation
git-smart-squash

# Or auto-apply without confirmation prompt
git-smart-squash --auto-apply
```

That's it! Your commits are now beautifully organized.

## Common Use Cases

### "I need to clean up before PR review"

```plain text
git-smart-squash              # Shows plan and prompts for confirmation
git-smart-squash --auto-apply # Auto-applies without prompting
```

### "I work with a different main branch"

```plain text
git-smart-squash --base develop
```

### "I want to use a specific AI provider"

```plain text
git-smart-squash --ai-provider openai
```

### "I use the short command"

```plain text
gss  # Same as git-smart-squash
```

## Safety First

Don't worry - Git Smart Squash is designed to be safe:

- Dry run by default - always shows you the plan first
- Always creates a backup branch before making changes
- Never pushes automatically - you stay in control
- Easy recovery - your original commits are always saved
### If You Need to Undo

```plain text
# Your original branch is always backed up
git branch | grep backup  # Find your backup
git reset --hard your-branch-backup-[timestamp]
```

## AI Provider Options

## Advanced Configuration (Optional)

Want to customize? Create a config file:

Project-specific (.git-smart-squash.yml in your repo):

```plain text
ai:
  provider: openai  # Use OpenAI for this project
```

Global default (~/.git-smart-squash.yml):

```plain text
ai:
  provider: local   # Always use local AI by default
```

## Troubleshooting

### "Ollama not found"

Install Ollama from https://ollama.com and run:

```plain text
ollama serve
ollama pull devstral
```

### "No changes to reorganize"

Make sure you're on your feature branch with committed work:

```plain text
git diff main  # Should show differences from main
```

### "Large diff taking too long" or "Token limit exceeded"

When using Ollama (local AI), there's a hard limit of 32,000 tokens (roughly 128,000 characters). For large diffs, try:

- Breaking your work into smaller chunks
- Using -base with a more recent commit
- Switching to a cloud provider for this operation: -ai-provider openai
### Need More Help?

Check out our detailed documentation or open an issue!

## License

MIT License - see LICENSE file for details.

Made with love for developers who want cleaner git history


