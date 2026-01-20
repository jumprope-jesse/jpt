---
type: link
source: notion
url: https://antonz.org/git-by-example/
notion_type: Software Repo
tags: ['Running']
created: 2024-04-11T02:15:00.000Z
---

# Git by example: Interactive guide

## Overview (from Notion)
- Understanding Git enhances collaboration in your software projects, making version control seamless for you and your team.
- The interactive guide simplifies complex Git concepts, saving you time and frustration with commands.
- Emphasizing the importance of a clean commit history can help you maintain clarity in your projects, beneficial for both you and your colleagues.
- The guide's focus on branching and merging can inspire innovative approaches to project management, allowing you to experiment without disrupting the main workflow.
- Learning to resolve conflicts effectively can improve team dynamics, fostering better communication and collaboration.
- The advanced features like partial clone and sparse checkout could significantly optimize your project workflow, especially with large codebases.
- Experimenting with Git's capabilities can spark creativity, leading to new ideas for your startup.
- Consider alternative version control systems as well; they may offer unique features that could align better with specific project needs.

## AI Summary (from Notion)
An interactive guide to Git operations, covering basic to advanced commands, including concepts like working tree, staging area, branches, and merging. Users can experiment with commands and learn through practical examples. The guide also addresses undoing changes, syncing with remote repositories, and advanced features like partial cloning and bisecting commits.

## Content (from Notion)

Git is the distributed version control system used in software development today. It's very powerful, but also known for its not-so-obvious syntax.

I got tired of googling the same Git commands over and over again. So I created an interactive step-by-step guide to Git operations, from basic to advanced. You can read it from start to finish to (hopefully) learn more about Git, or jump to a specific use case that interests you.

Feel free to experiment with the examples by changing the commands and clicking Run.

Concepts • Basics • Branch & merge • Local & remote • Undo • Advanced • Final thoughts

This guide is also available in other formats:

PDF minibook

Playground

## Concepts

This is the only piece of theory in the guide. I'll keep it short and simplified to the π == 3 level. Please don't judge me if you're a Git master.

### Working tree, staging area, repository

```plain text
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
│ .            │
│ ├── go.mod   │
│ └── main.go  │
└──────────────┘

```

A working tree is the slice of the project at any given moment (usually it's the current moment). When you add or edit code, you change the working tree.

A staging area is where you stage the changes from the working tree before making them permanent.

A repo (repository) is the collection of permanent changes (commits) made throughout the history of the project. Typically, there is a single remote repo (managed by GitHub/GitLab/etc) and many local repos — one for each developer involved in a project.

When you make a change in the staging area permanent, it is removed from the staging area and committed to the local repo. A commit is the permanent record of that change. The repo contains all the commits that have been made.

When you checkout a specific commit, the working tree is updated to reflect the project state at the time of that commit.

Local and remote repos are frequently synchronized so that all repos contain all commits from all developers.

### Branch, tag, HEAD

```plain text
      main             ○ v1.1
feat-2 │               │
      ╲│               •
       │ feat-1        │
       │╱              ○ v1.0
       │               │

```

A branch is an alternate version of the project reality. Typically, there is a main branch, and separate branches for features under development. When work on a feature branch is complete, it is merged into the main branch (or discarded).

A tag is a named state of the project. Typically, tags are created on the main branch for important milestones such as releases.

The currently checked-out commit (usually the latest commit in a branch) is referenced as HEAD.

Now that the boring stuff is out of the way, let's get to the recipes!

## Basics

Let's start with basic Git operations on a local repo.

init repo • add file • edit file • rename file • delete file • show status • show log • show commit • search

### Init repo

Create an empty repo:

```plain text
git init

```

Edit

Set user name and email for the repo (they are required):

```plain text
git config user.email alice@example.com
git config user.name "Alice Zakas"

```

Edit

Use the --global flag to set the name and email at the OS user level instead of the repo level.

Show user and repo configs:

```plain text
git config --list --show-origin

```

Edit

### Add file

Create a file and add it to the staging area:

```plain text
echo "git is awesom" > message.txt
git add message.txt

```

Edit

View changes in the staging area:

```plain text
git diff --cached

```

Edit

Commit to the local repo:

```plain text
git commit -m "add message"

```

Edit

### Edit file

Edit the previously committed file:

```plain text
echo "git is awesome" > message.txt

```

Edit

View local changes:

```plain text
git diff

```

Edit

Add modified files and commit in one command:

```plain text
git commit -am "edit message"

```

Edit

Note that -a does not add new files, only changes to the already committed files.

### Rename file

Rename the previously committed file:

```plain text
git mv message.txt praise.txt

```

Edit

The change is already in the staging area, so git diff won't show it. Use --cached:

```plain text
git diff --cached

```

Edit

Commit the change:

```plain text
git commit -m "rename message.txt"

```

Edit

### Delete file

Delete the previously committed file:

```plain text
git rm message.txt

```

Edit

The change is already in the staging area, so git diff won't show it. Use --cached:

```plain text
git diff --cached

```

Edit

Commit the change:

```plain text
git commit -m "delete message.txt"

```

Edit

### Show current status

Edit the previously committed file and add the changes to the staging area:

```plain text
echo "git is awesome" > message.txt
git add message.txt

```

Edit

Create a new file:

```plain text
echo "git is great" > praise.txt

```

Edit

Show the working tree status:

```plain text
git status

```

Edit

Note that message.txt is in the staging area, while praise.txt is not tracked.

### Show commit log

Show commits:

```plain text
git log

```

Edit

Show only the commit message and the short hash:

```plain text
git log --oneline

```

Edit

Show commits as an ASCII graph:

```plain text
git log --graph

```

Edit

Show compact ASCII graph:

```plain text
git log --oneline --graph

```

Edit

### Show specific commit

Show the last commit contents:

```plain text
git show HEAD

```

Edit

Show the second-to-last commit:

```plain text
git show HEAD~1

```

Edit

Use HEAD~n to show the nth-before-last commit or use the specific commit hash instead of HEAD~n.

### Search repo

There are 3 commits, each adding a new line to message.txt:

```plain text
git log --oneline

```

Edit

The current message.txt state:

```plain text
cat message.txt

```

Edit

Search in working tree (current state):

```plain text
git grep "debate"

```

Edit

Search the project as of the second-to-last commit:

```plain text
git grep "great" HEAD~1

```

Edit

You can use the specific commit hash instead of HEAD~n.

## Branch and merge

Let's dive into the wondrous world of merging.

branch • merge • rebase • squash • cherry-pick

### Branch

Show branches (there is only main now):

```plain text
git branch

```

Edit

Create and switch to a new branch:

```plain text
git branch ohmypy
git switch ohmypy

```

Edit

Show branches (the current one is ohmypy):

```plain text
git branch

```

Edit

Add and commit a file:

```plain text
echo "print('git is awesome')" > ohmy.py
git add ohmy.py
git commit -m "ohmy.py"

```

Edit

Show only commits from the ohmypy branch:

```plain text
git log --oneline main..ohmypy

```

Edit

### Merge

Show commits from all branches (two commits in main, one in ohmypy):

```plain text
git log --all --oneline --graph

```

Edit

We are now on the main branch, let's merge the ohmypy branch back into main:

```plain text
git merge ohmypy

```

Edit

There are no conflicts, so git commits automatically. Show the new commit history:

```plain text
git log --all --oneline --graph

```

Edit

### Rebase

Show commits from all branches (two commits in main, one in ohmypy):

```plain text
git log --all --oneline --graph

```

Edit

We are now on the main branch, let's rebase the ohmypy branch back into main:

```plain text
git rebase ohmypy

```

Edit

Note that the new commit history is linear, unlike when we do a git merge ohmypy:

```plain text
git log --all --oneline --graph

```

Edit

Rebasing rewrites history. So it's better not to rebase branches that have already been pushed to remote.

### Squash

Show commits from all branches (two commits in main, three in ohmypy):

```plain text
git log --all --oneline --graph

```

Edit

If we do git merge ohmypy to merge the ohmypy branch into main, the main branch will receive all three commits from ohmypy.

Sometimes we prefer to "squash" all the branch commits into a single commit, and then merge it into main. Let's do it.

Switch to the ohmypy branch:

```plain text
git switch ohmypy

```

Edit

Combine all ohmypy changes into a single commit in the working directory:

```plain text
git merge --squash main

```

Edit

Commit the combined changes:

```plain text
git commit -m "ohmy[py,sh,lua]"

```

Edit

Switch back to the main branch:

```plain text
git switch main

```

Edit

Merge the ohmypy branch into main:

```plain text
git merge --no-ff ohmypy -m "ohmy[py,sh,lua]"

```

Edit

Note the single commit in main made of three commits in ohmypy:

```plain text
git log --all --oneline --graph

```

Edit

### Cherry-pick

I have a typo in message.txt:

```plain text
cat message.txt

```

Edit

And I accidentally fixed it in the ohmypy branch instead of main:

```plain text
git log --all --oneline --graph --decorate

```

Edit

I'm not ready to merge the entire ohmypy branch, so I will cherry-pick the commit:

```plain text
git cherry-pick cbb09c6

```

Edit

cherry-pick applied the comment to the main branch:

```plain text
git log --all --oneline --graph --decorate

```

Edit

The typo is fixed:

```plain text
cat message.txt

```

Edit

## Local and remote

Working with a local repo is fun, but adding a remote repo is even funnier.

push • pull • resolve • push branch • fetch branch • tags

### Push

Alice wants to clone our repo and make some changes.

Clone the remote repo:

```plain text
git clone /tmp/remote.git /tmp/alice

```

Edit

Normally you'd see a GitHub/GitLab/etc URL here, but our "remote" repo is on the same machine in /tmp/remote.git.

Set user name and email:

```plain text
cd /tmp/alice
git config user.email alice@example.com
git config user.name "Alice Zakas"

```

Edit

Make some changes and commit:

```plain text
echo "Git is awesome!" > message.txt
git commit -am "edit from alice"

```

Edit

Push locally committed changes to the remote repo:

```plain text
git push

```

Edit

### Pull

I want to pull Alice's changes to the local repo.

No commits from Alice yet:

```plain text
git log --oneline

```

Edit

Pull the latest changes from the remote repo:

```plain text
git pull

```

Edit

The local repo now contains commits from Alice:

```plain text
git log --oneline

```

Edit

### Resolve conflict

I have a local commit (not yet pushed to the remote) that conflicts with Alice's changes (already pushed to the remote), so I need to resolve it.

Pull the changes from the remote repo:

```plain text
git pull

```

Edit

There is a conflict in message.txt! Let's show it:

```plain text
cat message.txt

```

Edit

I like Alice's version better, so let's choose it:

```plain text
git checkout --theirs -- message.txt
# to choose our version, use --ours

```

Edit

Add the resolved file to the staging area and complete the merge:

```plain text
git add message.txt
git commit -m "merge alice"

```

Edit

### Push branch

Create the local ohmypy branch:

```plain text
git branch ohmypy
git switch ohmypy

```

Edit

Add and commit a file:

```plain text
echo "print('git is awesome')" > ohmy.py
git add ohmy.py
git commit -m "ohmy.py"

```

Edit

Push the local branch to remote:

```plain text
git push -u origin ohmypy

```

Edit

Show both local and remote branches:

```plain text
git branch --all

```

Edit

### Fetch branch

Fetch remote branches:

```plain text
git fetch

```

Edit

Remote has the ohmypy branch, but it's not checked out locally:

```plain text
git branch

```

Edit

Checkout the ohmypy branch:

```plain text
git switch ohmypy
# or: git checkout ohmypy

```

Edit

Show branches:

```plain text
git branch

```

Edit

### Tags

Create a tag for the latest commit:

```plain text
git tag 0.1.0 HEAD

```

Edit

Create a tag for the nth-before-last commit:

```plain text
git tag 0.1.0-alpha HEAD~1

```

Edit

You can use the commit hash instead of HEAD~n.

Show tags:

```plain text
git tag -l

```

Edit

Show compact log with tags:

```plain text
git log --decorate --oneline

```

Edit

Delete tag:

```plain text
git tag -d 0.1.0-alpha

```

Edit

Push tags to the remote:

```plain text
git push --tags

```

Edit

## Undo

"Damn, how do I undo what I just did?" — is the eternal Git question. Let's answer it once and for all.

amend commit • undo uncommitted • undo local • undo remote • rewind history • stash changes

### Amend commit

Edit a file and commit:

```plain text
echo "git is awesome" > message.txt
git commit -am "edit nessage"

```

Edit

Show commits:

```plain text
git log --oneline

```

Edit

I made a typo, so I want to change the commit message:

```plain text
git commit --amend -m "edit message"

```

Edit

Git has replaced the last commit:

```plain text
git log --oneline

```

Edit

To change the commit message for one of the last n commits, use git rebase -i HEAD~n (interactive) and follow the instructions on the screen.

Amend only works if the commit has not yet been pushed to the remote repo!

### Undo uncommitted changes

Edit the previously committed file and add the changes to the staging area:

```plain text
echo "git is awesome" > message.txt
git add message.txt

```

Edit

Show the working tree status:

```plain text
git status

```

Edit

Remove the changes from the staging area:

```plain text
git restore --staged message.txt

```

Edit

The local file is still modified, but it's not staged for commit:

```plain text
git status

```

Edit

Now let's discard the changes altogether:

```plain text
git restore message.txt
# or: git checkout message.txt

```

Edit

Show the file contents:

```plain text
cat message.txt

```

Edit

The changes are gone.

### Undo local commit

I changed my mind about the last commit and I want to undo it.

Show commits:

```plain text
git log --oneline

```

Edit

Undo the last one:

```plain text
git reset --soft HEAD~

```

Edit

The commit is gone:

```plain text
git log --oneline

```

Edit

But the changes are still in the staged area:

```plain text
git status

```

Edit

To remove both the commit and the local changes, use --hard instead of --soft:

```plain text
git reset --hard HEAD~
git status

```

Edit

Reset only works if the commit has not yet been pushed to the remote repo!

### Undo remote commit

I changed my mind about the last commit and I want to undo it, but the commit is already pushed to the remote repo.

Show commits:

```plain text
git log --oneline

```

Edit

Undo the last one:

```plain text
git revert HEAD --no-edit

```

Edit

You can revert to nth-before-last commit by using HEAD~n or use the specific commit hash instead of HEAD~n.

Since the commit has already been pushed, git can't delete it. Instead it creates an "undo" commit:

```plain text
git log --oneline

```

Edit

Push the "undo" commit to the remote:

```plain text
git push

```

Edit

### Rewind history

Show commits:

```plain text
git log --oneline --graph

```

Edit

Show all repo states in reverse chronological order:

```plain text
git reflog

```

Edit

Suppose I want to go back to HEAD@{3}:

```plain text
git reset --hard HEAD@{3}

```

Edit

This resets the entire repo and the working tree to the moment of HEAD@{3}:

```plain text
git log --oneline --graph

```

Edit

### Stash changes

Edit the previously committed file:

```plain text
echo "git is awesome" > message.txt
git add message.txt

```

Edit

Let's say we need to switch to another branch, but we don't want to commit the changes yet.

Stash the local changes (i.e. save them in "drafts"):

```plain text
git stash

```

Edit

Stash is a stack, so you can push multiple changes onto it:

```plain text
echo "Git is awesome!" > message.txt
git stash

```

Edit

Show stash contents:

```plain text
git stash list

```

Edit

Now we can switch to another branch and do something:

```plain text
...(omitted for brevity)...

```

Switch back to the main branch and re-apply the latest changes from the stash:

```plain text
git switch main
git stash pop

```

Edit

pop returns changes from the stack in "last in, first out" order.

Clear the stash:

```plain text
git stash clear

```

Edit

## Advanced stuff

While git gurus probably know all about these features, most developers have never heard of them. Let's fix that.

log summary • worktree • bisect • partial checkout • partial clone

### Log summary

Since the 1.0 release (tag v1.0), we have 6 commits from 3 contributors:

```plain text
git log --pretty=format:'%h %an %s %d'

```

Edit

Note the --pretty option which customizes the log fields:

```plain text
%h   commit hash
%an  author
%s   message
%d   decoration (e.g. branch name or tag)

```

List the commits grouped by contributors:

```plain text
git shortlog v1.0..

```

Edit

A couple of useful options:

- n (-numbered) sorts the output by descending number of commits per contributor.
- s (-summary) omits commit descriptions and prints only counts.
List contributors along with the number of commits they have authored:

```plain text
git shortlog -ns v1.0..

```

Edit

### Worktree

I'm in the middle of something important in the ohmypy branch:

```plain text
echo "-- pwd --"
pwd
echo "-- branches --"
git branch
echo "-- status --"
git status

```

Edit

Suddenly I need to fix an annoying typo in the main branch. I can stash the local changes with git stash, or I can checkout multiple branches at the same time with git worktree.

Checkout the main branch into /tmp/hotfix:

```plain text
git worktree add -b hotfix /tmp/hotfix main

```

Edit

Fix the typo and commit:

```plain text
cd /tmp/hotfix
echo "git is awesome" > message.txt
git commit -am "fix typo"

```

Edit

Push to remote main:

```plain text
git push --set-upstream origin main

```

Edit

Now I can return to /tmp/repo and continue working on the ohmypy branch.

### Bisect

I have 5 poorly named commits:

```plain text
git log --oneline

```

Edit

And a failing test:

```plain text
sh test.sh

```

Edit

I will use the bisection algorithm to find the commit that introduced the bug:

```plain text
git bisect start

```

Edit

The current state is obviously buggy, but I'm pretty sure the first "main.sh" commit was good:

```plain text
git bisect bad HEAD
git bisect good HEAD~4

```

Edit

Git has automatically checked out the middle commit. Let's test it:

```plain text
sh test.sh

```

Edit

The test passes. Mark the commit as good:

```plain text
git bisect good

```

Edit

Git has automatically checked out the middle commit. Let's test it:

```plain text
sh test.sh

```

Edit

The test fails. Show the commit details:

```plain text
git show

```

Edit

This is the commit that introduced the bug (subtraction instead of addition)!

### Partial checkout

The remote repo looks like this:

```plain text
.
├── go.mod
├── main.go
├── products
│   └── products.go
└── users
    └── users.go

```

We will selectively checkout only some of the directories.

Clone the repo, but do not checkout the working tree:

```plain text
git clone --no-checkout /tmp/remote.git /tmp/repo
cd /tmp/repo

```

Edit

Tell git to checkout only the root and users directories:

```plain text
git sparse-checkout init --cone
git sparse-checkout set users

```

Edit

Checkout the directories:

```plain text
git checkout main

```

Edit

Only the root and users directories are checked out:

```plain text
tree

```

Edit

The products directory was not checked out.

### Partial clone

The partial checkout approach we tried earlier still clones the entire repo. So if the repo itself is huge (which is often the case if it has a long history or large binary files), the clone step can be slow and traffic-intensive.

To reduce the amount of data downloaded during cloning, use partial clone with one of the following commands:

```plain text
# Download commits and trees (directories),
# but not blobs (file contents):
git clone --filter=blob:none file:///tmp/remote.git
# Download commits only, without trees (directories)
# or blobs (file contents):
git clone --filter=tree:0 file:///tmp/remote.git

```

In both cases, git will lazily fetch the missing data later when needed.

Note that for this to work, the remote server should support partial cloning (GitHub does).

## Final thoughts

We've covered important Git operations, from basic editing to branching and merging, remote syncing, undoing changes, and performing some moderate magic.

To learn more about Git, check out the reference manual and the Pro Git book by Scott Chacon and Ben Straub.

And may Git be with you!

──

P.S. Interactive examples in this post are powered by codapi — an open source tool I'm building. Use it to embed live code snippets into your product docs, online course or blog.

Subscribe to keep up with new posts.


