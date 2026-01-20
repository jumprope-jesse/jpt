# Jujutsu (jj) Version Control

A modern version control system that's gaining traction as an alternative/complement to git.

## Resources

- [Steve's Jujutsu Tutorial](https://steveklabnik.github.io/jujutsu-tutorial/) - Beginner-friendly tutorial written as Steve learns jj himself. Good for those who learn similarly to how TRPL (The Rust Programming Language) was written.
- [Chris Krycho's article on jj](https://chriskrycho.com/) - Helped Steve finally "get" jj concepts

## Key Concepts

- **Stacked diffs** - A workflow pattern that jj handles well (common in companies like Meta/Google)
- Works with existing git repos (can clone git repos with jj)

## Notes

- People who are comfortable with git's CLI may still benefit from jj's model
- Like Rust, jj may require multiple attempts to "click" - coming back after stepping away can help
- The learning curve seems to resolve with persistence

## Stacked Diffs Workflow

Stacked diffs (or stacked PRs) is a workflow where you build changes incrementally on top of each other, rather than waiting for one PR to merge before starting the next.

### Traditional Git Approach with `git rebase --onto`

The command syntax:
```bash
git rebase --onto <new-base> <old-base> <branch>
```

Think of it as: "Take everything after `<old-base>` on `<branch>`, and replay it onto `<new-base>`."

**The Marker Branch Pattern:**
1. When creating a dependent branch (e.g., `feature-2` off `feature-1`), also create a marker branch pointing to the base:
   ```bash
   git checkout -b feature-2-base  # marker at feature-1's current tip
   git checkout -b feature-2       # your working branch
   ```

2. When syncing after `main` updates:
   ```bash
   # First rebase feature-1 onto main
   git checkout feature-1
   git rebase main

   # Then rebase feature-2 using the marker
   git rebase --onto feature-1 feature-2-base feature-2

   # Update the marker to the new feature-1 tip
   git branch -f feature-2-base feature-1
   ```

3. After `feature-1` merges to main, clean up feature-2:
   ```bash
   git checkout feature-2
   git rebase -i main
   # Drop/delete the commits that came from feature-1
   ```

**Key considerations:**
- Force pushes required after rebasing (coordinate with team)
- Marker branches must be updated consistently - this is what makes repeat syncs work
- Potential merge conflicts on each sync
- Benefits: smaller PRs, faster reviews, cleaner history

Source: [Dinesh Pandiyan - Stacked Diffs with git rebase --onto](https://dineshpandiyan.com/blog/stacked-diffs-with-rebase-onto/)

### Tools that Simplify Stacked Diffs
- **Jujutsu (jj)** - Native support for stacked changes, no branch names needed
- **GitButler** - GUI tool for managing stacked branches
- **Graphite** - Stacked PR management for GitHub
- **ghstack** - Meta's tool for stacking PRs

### Benefits
- Smaller, more reviewable PRs
- Continue working while waiting for reviews
- Reduces merge conflicts vs long-lived branches
- Better for complex projects with multiple dependent changes

### Comparison to Trunk-Based Development
- Trunk-based: frequent small merges to main, feature flags
- Stacked diffs: chain of dependent changes, merge in order
- Both aim to avoid large, long-lived feature branches

Source: [HN Discussion](https://news.ycombinator.com/item?id=46103571)

## Mega Merge Workflow

A powerful workflow for working on multiple branches simultaneously by creating merge commits that combine all your WIP features in one working directory. Coined by Austin Seipp, documented by Benjamin Tan.

### Why This Matters
- Test multiple WIP features together holistically
- Make quick bugfixes without stashing/switching branches
- Avoid the "Git dance" of context switching
- Maintain Pull Request-style workflow while getting Stacked Diff benefits

### Core Commands

**Create a merge commit with multiple parents:**
```bash
jj new qkl zoz  # Creates new commit with 2 parents
```

**Add a new parent to existing merge:**
```bash
jj rebase -s orl -d "all:orl-" -d NEW_PARENT_ID
# all:orl- = all existing parents, then add new one
```

**Remove a parent from merge:**
```bash
jj rebase -s orl -d "all:orl- ~ qkl"
# Set difference removes qkl from parents
```

**Rebase all feature branches onto updated main:**
```bash
jj rebase -s "all:roots(main..@)" -d main
# roots() finds the first commits of each arm
# Rebases all at once with one command
```

**Move a working copy change to a specific parent:**
```bash
jj new rwq --no-edit     # Insert empty commit after target
jj squash --from ovy --into lqks  # Move changes into it
jj branch set test -r lqks  # Update branch
```

### Key Revset Expressions
- `@` - working copy commit
- `orl-` - all parents of orl
- `all:X` - prefix for commands expecting single commit but getting multiple
- `roots(A..B)` - commits in A..B with no ancestors in the set
- `X ~ Y` - set difference (X minus Y)
- `X | Y` - set union

### Conflict Handling
- Jujutsu stores full conflict metadata, not just markers
- Merge commit can be conflict-free even if children have conflicts
- After manual resolution in a branch, merge may show conflict (metadata lost)
- Use `jj restore --from ORIGINAL_COMMIT_ID` to restore pre-conflict state

### Related Tools
- **GG** - GUI app for Jujutsu with good visualization of this workflow
- **GitButler** - Similar "virtual branches" concept for Git

Source: [Benjamin Tan - A Better Merge Workflow with Jujutsu](https://ofcr.se/jujutsu-merge-workflow/)
