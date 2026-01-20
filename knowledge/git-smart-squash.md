# Git Smart Squash - AI Commit History Cleanup

*Source: https://github.com/edverma/git-smart-squash - Added: 2026-01-18*

An AI-powered tool that transforms messy commit histories into clean, logical commits before PR reviews.

---

## The Problem It Solves

Feature branches often accumulate messy commits:
```
* fix tests
* typo
* more auth changes
* WIP: working on auth
* update tests
* initial auth implementation
```

Git Smart Squash reorganizes these into clean, conventional commits:
```
* feat: implement complete authentication system with JWT tokens
* test: add comprehensive test coverage for auth endpoints
```

## Quick Start

```bash
# Install
pip install git-smart-squash

# Run on your feature branch (shows plan, asks for confirmation)
git-smart-squash

# Auto-apply without confirmation
git-smart-squash --auto-apply

# Use different base branch
git-smart-squash --base develop

# Short command alias
gss
```

## AI Provider Options

**Local AI (Free & Private) - Default:**
```bash
# Install Ollama from https://ollama.com
ollama serve
ollama pull devstral
```

**Cloud AI (requires API keys):**
```bash
export OPENAI_API_KEY="your-key"      # or
export ANTHROPIC_API_KEY="your-key"   # or
export GEMINI_API_KEY="your-key"

git-smart-squash --ai-provider openai
```

## Safety Features

- **Dry run by default** - always shows plan first
- **Backup branch created** before making changes
- **Never auto-pushes** - you stay in control
- **Easy recovery:**
  ```bash
  git branch | grep backup
  git reset --hard your-branch-backup-[timestamp]
  ```

## Configuration

Project-specific (`.git-smart-squash.yml` in repo):
```yaml
ai:
  provider: openai
```

Global default (`~/.git-smart-squash.yml`):
```yaml
ai:
  provider: local
```

## Limitations

- Ollama has a hard limit of 32,000 tokens (~128,000 characters)
- For large diffs:
  - Break work into smaller chunks
  - Use `--base` with a more recent commit
  - Switch to cloud provider: `--ai-provider openai`

## Why It's Useful

- Saves 30+ minutes of manual commit reorganization before PRs
- Creates conventional commit messages automatically
- Makes code reviews smoother with logical commit groupings
- Privacy-friendly with local AI option (Ollama)
- Safe workflow with automatic backups
