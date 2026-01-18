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
