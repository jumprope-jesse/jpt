# Git by Example - Interactive Reference Guide

*Source: https://antonz.org/git-by-example/ - Added: 2026-01-18*

A comprehensive interactive Git guide with runnable examples, from basic operations to advanced features.

---

## Core Concepts

```
┌──────────────┐         ┌──────────────┐
│ local        │ push ─> │ remote       │
│ repo         │ <- pull │ repo         │
└──────────────┘         └──────────────┘
check │  ↑↓ commit / reset
out   │ ┌──────────────┐
      │ │ staging area │
      │ └──────────────┘
      ▽  ↑↓ add / restore
┌──────────────┐
│ working tree │
└──────────────┘
```

- **Working tree**: Current slice of the project (your files right now)
- **Staging area**: Changes queued for commit
- **Repository**: Collection of permanent commits
- **HEAD**: Currently checked-out commit

## Essential Commands Quick Reference

### Viewing State
```bash
git status                    # Working tree status
git log --oneline            # Compact commit log
git log --oneline --graph    # Compact ASCII graph
git diff                     # Unstaged changes
git diff --cached            # Staged changes
git show HEAD                # Last commit details
git show HEAD~1              # Second-to-last commit
```

### Searching
```bash
git grep "pattern"           # Search working tree
git grep "pattern" HEAD~1    # Search specific commit
```

### Branching
```bash
git branch                   # List branches
git branch -a                # List local + remote branches
git branch feature           # Create branch
git switch feature           # Switch to branch
git log main..feature        # Commits only in feature branch
```

### Merging Strategies
```bash
git merge feature            # Standard merge (preserves history)
git rebase feature           # Linear history (rewrites commits)
git merge --squash feature   # Combine all branch commits into one
```

### Remote Operations
```bash
git push                     # Push to remote
git pull                     # Fetch + merge from remote
git push -u origin branch    # Push new branch to remote
git fetch                    # Download remote changes without merging
git push --tags              # Push tags to remote
```

### Conflict Resolution
```bash
git checkout --theirs -- file.txt   # Accept remote version
git checkout --ours -- file.txt     # Keep local version
git add file.txt && git commit      # Complete merge after resolving
```

## Undo Operations

### Before Committing
```bash
git restore --staged file.txt    # Unstage (keep changes)
git restore file.txt             # Discard changes entirely
```

### After Local Commit (not pushed)
```bash
git commit --amend -m "new msg"  # Fix last commit message
git reset --soft HEAD~           # Undo commit, keep staged changes
git reset --hard HEAD~           # Undo commit and discard changes
```

### After Remote Commit (already pushed)
```bash
git revert HEAD --no-edit        # Create "undo" commit
git push                         # Push the revert
```

### Emergency Recovery
```bash
git reflog                       # Show all repo states
git reset --hard HEAD@{3}        # Rewind to specific state
```

### Stash (temporary save)
```bash
git stash                        # Save current changes
git stash list                   # Show stash contents
git stash pop                    # Apply latest stash
git stash clear                  # Clear all stashes
```

## Advanced Features

### Log Summary
```bash
git shortlog v1.0..              # Commits grouped by author since tag
git shortlog -ns v1.0..          # Author commit counts (sorted)
git log --pretty=format:'%h %an %s %d'  # Custom format
```

### Worktree (multiple branches checked out)
```bash
git worktree add -b hotfix /tmp/hotfix main  # Checkout branch to separate dir
# Work in /tmp/hotfix while keeping main checkout intact
```

### Bisect (find bug-introducing commit)
```bash
git bisect start
git bisect bad HEAD              # Current is broken
git bisect good HEAD~10          # Known good commit
# Git auto-checkouts middle commit, test it, then:
git bisect good                  # or git bisect bad
# Repeat until culprit found
```

### Partial Clone (for huge repos)
```bash
git clone --filter=blob:none URL     # Skip file contents initially
git clone --filter=tree:0 URL        # Skip trees and blobs
# Git fetches data lazily when needed
```

### Partial Checkout (sparse checkout)
```bash
git clone --no-checkout URL
cd repo
git sparse-checkout init --cone
git sparse-checkout set users        # Only checkout specific dirs
git checkout main
```

## Related

- [[git-interactive-rebasing]] - Workflow for cleaning up commits before PR
- [[git-smart-squash]] - AI tool that automates commit cleanup
- [[jujutsu-version-control]] - Modern VCS alternative with native stacked diffs
- [Oh My Git!](https://ohmygit.org/) - Open source game that visualizes Git internals in realtime with card-based interface for beginners
