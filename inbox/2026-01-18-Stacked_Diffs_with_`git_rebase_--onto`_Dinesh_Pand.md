---
type: link
source: notion
url: https://dineshpandiyan.com/blog/stacked-diffs-with-rebase-onto/
notion_type: Software Repo
tags: ['Running']
created: 2025-12-06T17:17:00.000Z
---

# Stacked Diffs with `git rebase --onto` | Dinesh Pandiyan

## Overview (from Notion)
- Mastering git rebase --onto can streamline your development process, allowing for cleaner code review cycles.
- Efficiently managing stacked diffs can save you time, which is vital when balancing work and family life.
- Implementing best practices in version control can help foster a culture of collaboration within your team, leading to better software products.
- Understanding the nuances of Git can empower you as a founder, giving you the confidence to lead technical discussions effectively.
- The discipline of maintaining marker branches mirrors parenting; consistency is key to navigating challenges smoothly.
- While the complexity of stacked diffs may seem daunting, the benefits of smaller, manageable tasks can enhance both your work life and personal productivity.
- An alternative view might suggest simplifying workflows; however, the long-term gains of a clean commit history often outweigh the initial learning curve.
- Emphasizing the importance of clear communication in your team can help mitigate the frustrations that arise from potential merge conflicts.

## AI Summary (from Notion)
Using git rebase --onto allows for clean rebasing of dependent branches without carrying over unrelated commits. Stacked diffs help manage large features by breaking them into smaller, reviewable PRs, but require careful syncing when the main branch updates. The process involves creating marker branches, performing regular updates, and cleaning up commit history post-merge. Key considerations include the necessity of force pushes, maintaining discipline with marker branches, and managing potential merge conflicts.

## Content (from Notion)

tldr; Use git rebase --onto to cleanly rebase a dependent branch without dragging along commits that don’t belong to it.

If you’ve ever worked on a larger feature and split your work into multiple PRs that depend on each other, you’ve probably experienced the pain of keeping them in sync. This workflow is called stacked diffs (or stacked PRs), and it’s incredibly powerful. But it comes with a learning curve. The secret weapon? git rebase --onto.

Here’s what we’ll cover:

- Why stacked diffs are worth the effort
- The difference between a regular git rebase and git rebase --onto
- Step-by-step: first sync, ongoing syncs, and post-merge cleanup
## Why Stacked Diffs?

Let’s say you’re building a large feature. You could dump everything into one massive PR, but reviewers hate that. Large PRs get superficial reviews (or no reviews at all), and you end up waiting forever for approvals.

Stacked diffs solve this by breaking your work into smaller, dependent PRs:

```plain text
main
  └── feature-1 (auth layer)
        └── feature-2 (user profile)
              └── feature-3 (profile settings)

```

Each PR is small, focused, and easy to review. The catch? When main updates or when feature-1 gets rebased, you need to sync all the downstream branches. That’s where most people get stuck.

## Regular rebase vs rebase –onto

### Regular rebase

A regular git rebase main replays your commits on top of the target branch:

```plain text
Before:
main:      A---B---C
                \
feature:         D---E
After git rebase main:
main:      A---B---C
                    \
feature:             D'---E'

```

Simple enough. But what happens with stacked branches?

### The Problem with Stacked Branches

Here’s a typical stacked setup:

```plain text
main:        A---B---C
                  \
feature-1:         D---E
                        \
feature-2:               F---G

```

Now main gets updated with new commits:

```plain text
main:        A---B---C---H---I
                  \
feature-1:         D---E
                        \
feature-2:               F---G

```

You rebase feature-1 onto main:

```plain text
main:        A---B---C---H---I
                  \          \
old:               D---E      D'---E'  ← feature-1 (new hashes!)
                        \
feature-2:               F---G  ← Still based on old D---E!

```

See the problem? feature-2 is still based on the old D---E commits. If you try a regular git rebase feature-1 on feature-2, git will try to include those old commits again and you’ll end up with duplicates or conflicts.

### Enter: git rebase –onto

This is where git rebase --onto shines. It lets you specify exactly which commits to move and where to put them:

```plain text
git rebase --onto <new-base> <old-base> <branch>
                      ↑          ↑          ↑
                new parent  old parent   branch to rebase

```

Think of it as saying: “Take everything after <old-base> on <branch>, and replay it onto <new-base>.”

## Step-by-Step: Using rebase –onto

### First rebase –onto

When you first create feature-2 off of feature-1, also create a marker branch:

The first time main updates and you need to sync your stack:

> 

### Syncing main

Every time main updates, you repeat the same pattern:

The marker update isn’t optional. It’s what makes repeat syncs work.

### Once a feature branch merges

When feature-1 finally lands in main, you no longer need its commits in your feature-2 history. Here’s how to clean up:

In the interactive rebase, you’ll see all commits including the ones from feature-1:

```plain text
pick abc123 D' ...  ← DELETE (from feature-1)
pick def456 E' ...  ← DELETE (from feature-1)
pick 789ghi F  ...  ← KEEP (your work)
pick 012jkl G  ...  ← KEEP (your work)

```

Delete (or mark as drop) the commits from feature-1, and Git will replay only your feature-2 commits directly onto main.

### Putting it all together visually

```plain text
BEFORE REBASE:
==============
main:             A---B---C---H---I
                       \
feature-1:              D---E              (needs rebase onto main)
                            ↑
feature-2-base:             * (marker pointing to E)
                             \
feature-2:                    F---G
AFTER REBASING FEATURE-1:
=========================
main:             A---B---C---H---I
                       \          \
old commits:            D---E      D'---E'  (feature-1, new hashes!)
                            ↑
feature-2-base:             * (still pointing to old E!)
                             \
feature-2:                    F---G         (orphaned on old commits)
AFTER REBASE --ONTO:
====================
main:             A---B---C---H---I
                                  \
feature-1:                         D'---E'
                                        ↑
feature-2-base:                         * (updated to new E')
                                         \
feature-2:                                F'---G'  (synced!)

```

## Closing Thoughts

git rebase --onto is one of those commands that looks intimidating but becomes second nature once you understand what each parameter does:

The marker branch pattern takes the guesswork out of tracking the old base. Use it, update it, and your stacked diffs will stay clean.

Here are a few thoughts to keep in mind when using this workflow:

1. 
1. 
1. 
1. 
Is this workflow more complex than just having one big branch? Absolutely. But the payoff (smaller PRs, faster reviews, and cleaner history) is worth the investment. Just remember to update those marker branches!

Happy rebasing! Have a great day!


