# Git Interactive Rebasing Workflow

*Source: https://rednafi.com/misc/on_rebasing/ - Added: 2026-01-18*

A practical workflow for cleaning up messy commits before PR reviews using interactive rebasing.

---

## Why Rebase

Benefits over merge:
- Linear history (`git log --oneline --graph` tells a cleaner story)
- Squash messy WIP commits into logical units before review
- Bundle related changes with passing tests and documentation

Alternative approaches that achieve similar results:
- `git merge --squash feat_branch`
- GitHub's squash-merge feature

## Basic Feature Branch Workflow

```bash
# 1. Start with latest main
git pull

# 2. Create feature branch
git switch -c feat_branch

# 3. Do work, make messy commits as needed

# 4. Before PR: interactive rebase to clean up
git rebase -i HEAD~n  # where n = number of commits to tidy

# 5. Rebase onto latest main
git switch main
git pull
git switch feat_branch
git rebase main

# 6. Push and create PR
git push origin HEAD
```

## Interactive Rebasing Commands

### Count commits on feature branch (not in main)
```bash
git log main..@ --oneline | wc -l
```

Note: `@` is shorthand for current branch (HEAD).

### View commits on feature branch
```bash
git log main..@ --oneline --graph
```

### Start interactive rebase
```bash
git rebase -i HEAD~5  # last 5 commits
```

### Available actions in rebase-todo file
- `pick` (p) - use commit as-is
- `reword` (r) - use commit, but edit message
- `squash` (s) - meld into previous commit, combine messages
- `fixup` (f) - meld into previous, discard this commit's message
- `edit` (e) - pause for amending
- `drop` (d) - remove commit entirely
- `exec` (x) - run shell command

### Example: Squash 5 messy commits into 1

Edit the rebase-todo file:
```
pick 763e178 ci
s 4b10faf ci
s 7f7ce20 ci
s 88fc529 ci
s 8bc19b6 ci
```

Then edit the combined commit message in the next file that opens.

## Running Commands During Rebase

Run tests (or any command) after each commit:
```bash
git rebase -i --exec "pytest" HEAD~5
```

This ensures tests pass at each intermediate commit - useful for bisecting later.

## Handling Conflicts

When conflicts occur during rebase:
```bash
# 1. Fix conflicts in editor (VSCode, etc.)
# 2. Stage resolved files
git add .
# 3. Continue rebase
git rebase --continue
```

To abort and start over:
```bash
git rebase --abort
```

## Related

- [[git-smart-squash]] - AI tool that automates commit cleanup
- [[jujutsu-version-control]] - Modern VCS with native stacked diffs support
