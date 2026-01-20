---
type: link
source: notion
url: https://ofcr.se/jujutsu-merge-workflow/
notion_type: Software Repo
tags: ['Running']
created: 2024-07-01T15:27:00.000Z
---

# A Better Merge Workflow with Jujutsu | ofcrse by Benjamin Tan

## AI Summary (from Notion)
- Introduction to Jujutsu: A modern, user-friendly Version Control System (VCS) that is compatible with Git repositories, offering a better user experience despite being experimental.

- Austin's Mega Merge Strategy: A workflow shared by Austin Seipp that simplifies the manipulation of merge commits in Jujutsu, allowing multiple branches to be activated in the same working directory.

- Key Features of Jujutsu:
- Separate notions of changes and commits, improving the management of commit histories.
- Use of revsets for more expressive commit selection compared to Git.
- Eliminates the concept of the index, simplifying the commit process.

- Merge Commits: While not a new concept, Jujutsu enhances the ability to manipulate the commit graph safely, avoiding unrecoverable states.

- Use Cases:
- Testing features in a holistic manner by merging branches.
- Quickly fixing bugs without the complexity of traditional Git workflows.

- Manipulating Merge Commits: The ability to add, remove, and rebase parents of merge commits makes Jujutsu more flexible than Git.

- Conflict Management: Jujutsu handles conflicts with full metadata, allowing for manual resolution while maintaining the integrity of the merge commit.

- Conclusion: Jujutsu provides a powerful workflow for managing multiple branches and testing features simultaneously. While it may not replace Git for everyone, it offers valuable tools for those who need more flexibility in their version control processes.

## Content (from Notion)

Table of contents   
1.   Introduction  
2.   A quick primer on Jujutsu  
3.   Creating a new merge commit  
4.   A new merge workflow?  
5.   Adding a new parent from an existing commit  
6.   Rebasing all parents  
7.   Adding a new parent from new changes  
8.   Moving a change to a parent  
9.   Removing parents  
10.   Conflicting changes  
11.   Conclusion   

## Introduction

Since reading Chris Krycho’s essay introduction to Jujutsu, I’ve been excited about the possibilities of a more modern, user-friendly Version Control System (VCS) tool. For those of you who aren’t familiar, Jujutsu (binary name: jj) is a new VCS which is compatible with existing Git repositories. I’ve been using Jujutsu as my daily Git driver for a while now. Though it’s still experimental software—with its fair share of bugs and unimplemented features, it has made my day-to-day interactions with Git repositories a much more pleasant experience.

There’s a really cool workflow that Austin Seipp shared on Jujutsu’s Discord, which I’m beginning to use everywhere, that I thought was worth writing more about. He calls it The Austin™ Mega Merge Strategy®, but me—I’m just going to call it for what it is: a Better Workflow for Manipulating Merge Commits in Jujutsu1. This workflow makes it easy to simultaneously activate multiple branches in the same working directory.

Before I go through the workflow, let’s take a look at some of the basics of Jujutsu.

## A quick primer on Jujutsu

There’s no better way to demonstrate a VCS than by using it on its own repository. Jujutsu is compatible with Git repositories, and its own repository is a Git repository as well, hosted on GitHub.

Here’s the terminal output of jj log, which displays the graph of commits in the repository:

There’s a couple of things to note, which differ from Git:

1.    
1. 
1. 
## Creating a new merge commit

In the repository, I’ve been working on a few distinct features, some of which I’ve already pushed to various branches in my fork of the repository. Let’s take a look at the commits that I’m interested in—commits for which I’m the author, and have been pushed to a remote branch:

I’d like to create a new merge commit which includes the changes from zoz and qkl. With Jujutsu, you can use jj new to start working on a new change, and specify any number of parent changes:

This creates a new merge commit with the change ID of orl, with the 2 parents specified. Note that you can specify as many parents as you want, and Jujutsu can still merge them. (I’m only specifying 2 here, so I can add more later manually.) Here’s what the commit graph looks like at this point:

## A new merge workflow?

Merge commits, you might be wondering. Is that a new workflow? Can’t you just use Git for this?

Merge commits definitely aren’t anything new—nearly every modern VCS tool has merge commits. However, Jujutsu’s support for manipulating the commit graph is miles ahead of Git’s. With Jujutsu, you can merge commits without fear of modifying your repository to an unrecoverable state. Jujutsu’s first-class conflicts and jj undo makes it safe to merge different branches, play around with different configurations of your code, and then restore your original changes.

Whether you find this article useful likely depends on how you’re using your VCS right now. If you’re just building a linear stack of commits, then this is probably not going to be very helpful. However, if you use separate branches to work on different features and group commits together for code review, then you might find this useful. (If you’ve read Jackson Gabbard’s article on Stacked Diffs vs Pull Requests, I like to think that this workflow allows you to enjoy the benefits of a Stacked Diff-like workflow of working on a single branch, but still allows you to work with code forges like GitHub which expect a Pull Request-style workflow.)

The gist of this workflow is basically: merge all or as many of your branches/commits together as you need, and keep that combined merge commit in your working directory.

Why is this useful? Some good usecases include:

- Testing a full build of your application with different WIP features together, to see how it operates holistically as a whole
- Quickly fixing a bug or making a change without having to do the traditional Git dance of stashing changes and switching branches
Modifying existing merge commits is difficult using Git, but is much simpler with Jujutsu. Let’s go through a few examples.

## Adding a new parent from an existing commit

Here’s how to add another parent to the merge commit:

This command rebases the commit with change ID orl and all its descendants on top of all the given destinations. The given destinations here were all:orl-, which means all of orl’s existing parents, as well as the new destination of wtm. We’ve now got a new merge commit with the 2 original parents and the new one:

If you’ve got any other commits on top of the one you specified for -s, Jujutsu also correctly rebases all of the original commit’s descendants on top of the new commit, so you don’t have to worry about those commits going out of sync.

## Rebasing all parents

In this case, I realized that all my feature branches were outdated, and I’d like to rebase them on top of main. Here’s the command to do that:

The syntax is a bit of a doozy, but can be better understood by breaking it down part-by-part:

1. main..@: This finds all ancestors of @, the working copy commit, which are not ancestors of main. (By coincidence, my default configured revset for jj log shows exactly all the commits in the main..@ set.)
1. roots(main..@): This gets the roots of commits in main..@ set, which are commits that do not have any ancestors within the set. This evaluates to the first commit of each arm of the merge commit in the log above (qkl, yow, and zoz).
1. all:roots(main..@): The all prefix is required since s expects a single commit by default, but roots(main..@) evaluates to multiple commits.
Each of these 3 commits are rebased on top of the destination, main, and have their descendants automatically rebased as well. This results in a subgraph where the root is main, and the leaf is the merge commit with its 3 parents:

Here, we’ve automatically rebased all the changes we’re interested in with just a single command! 😲

## Adding a new parent from new changes

Whilst testing out the features from these different changes, you might want to work on a new change. Instead of having to check out a new branch as you would in Git, you can just work on the new change on top of this merge commit:

Here’s the updated commit graph, with the new commit (change ID rwq) as a child of the merge commit:

Although this change was made on top of the merge commit, you typically wouldn’t want to leave it there for long. You’d likely want to rebase it to a better location (not on top of the mega merge commit), before sending the change up for code review. For example, you can first rebase the new change onto main:

The -r option rebases only the given revision on top of the destination; it rebases all of its descendants on top of its parents. Effectively, this is similar to moving a commit to another location in the graph.

After rebasing onto main, you can then add rwq as a new parent of the merge commit to keep the change applied to your working directory:

This persists the change in the working directory, whilst extracting it to a standalone commit on top of the main branch which can be sent for code review. Here’s how you can create a branch and push to an upstream repository (GitHub in this case):

## Moving a change to a parent

Another possible scenario is that you’ve made some modifications to your working copy, and want to shift the commit into one of the arms of the merge commit.

This is what the commit graph looks like after making the change:

There’s a new change ovy which we want to set as the child of our previous change rwq, then update the branch test to point to ovy. There’s two possible ways to do this right now using Jujutsu:

1. Rebase ovy onto rwq, rebase the merge commit to point to ovy instead of rwq, then update the branch test to point to ovy.
1. Create a new commit after rwq, squash the changes from ovy into it, then update the branch test to point to ovy.
The first way is similar to what’s already been done above, so I’ll show the second way of doing this. First, we insert a new commit after rwq, making sure to specify --no-edit to avoid checking out the changes in rwq:

A new, empty commit with change ID lqks was created after rwq. Note how lqks was correctly inserted between orl and rwq, maintaining the ancestry of the merge commit:

Next, we can “squash” or move the changes from ovy into lqks. This is followed by updating the branch test to point to lqks:

The log now shows that test@bnjmnt4n (the branch test on the remote bnjmnt4n) points to the previous commit, whilst test is pointing to the commit with change ID orl. The * indicator shows that the branch has been updated, but isn’t consistent with the remote.

The biggest downside of the jj squash workflow is that the change ID of the squashed commit is lost. You’ll need to refer to the change ID of the newly created commit instead.

However, there are plans to improve Jujutsu to make it easier to move commits around the commit graph. In the future, a command like jj rebase -r ovy --after rwq might be able to move the commit whilst maintaining its chnage ID.

## Removing parents

Again, we can use jj rebase (and a small change to the revset) to remove parents from a merge commit:

Previously, when adding new parents, we’ve specified the destinations using the flags -d "all:orl-" -d NEW_PARENT_ID. Now, we’re specifying the destinations using -d "all:orl- ~ qkl". The new argument for the destination highlights more of the revset language, in particular the set difference operator. As before, orl- evaluates to the set of all parents of orl, but ~ qkl now subtracts qkl from that set.

This has the effect of removing qkl from the merge commit:

(Likewise, we could also have used set operations to add new parents to the merge commit: jj rebase -d "all:orl- | NEW_PARENT_ID" uses the set union operator to add the new ID to the set of existing parents.)

## Conflicting changes

What happens if you update something in the working directory, which you want to shift to a specific parent of the merge commit, but it actually conflicts with another change you made in another parent?

Here, I’ve committed a change which modifies the same lines as the previous commit rwq:

Here’s the updated commit graph now, with uyl containing the change and no longer being empty:

I now want to shift this new commit into the arm of the merge commit with zoz (the ssh-openssh branch), so I create a new, empty commit after zoz:

The new commit has the change ID txs, so I’ll squash my changes from uyl into txs:

Jujutsu now warns that a new conflict appeared in txs, as expected. That’s because txs doesn’t have rwq in its history, which was where the first modification came from. Let’s take a look at the log now:

The commit txs is marked in the log as containing a conflict. Here’s what txs looks like:

The original line from txs’s parent commit in red is replaced with the new conflicting changes in green. Jujutsu’s conflict markers are slightly different from Git: lines following %%%%%%% are a diff between 2 sides, whilst lines following +++++++ are a snapshot of the changes a side. Here’s my annotations on what the conflict markers mean:

Even though txs has a conflict, note that the merge commit orl isn’t in a conflicted state. This is because Jujutsu doesn’t just store conflict markers, but the full metadata of the conflicts, so it can resolve the conflicts by applying all the changes from each of orl’s parents.

However, if we want to update the ssh-openssh branch to include the changes in txs, we can’t just push a conflicted file since it won’t be accepted in any code review. We need to first resolve the conflict in txs. I’m doing this manually here by checking out txs and editing the file in the working directory, but you can also use a graphical tool for conflict resolution.

The changes are updated in my working copy commit, so I can squash the changes into txs to apply the resolution there as well:

So, txs no longer has any conflicts, and we can update our branch to point to it and push it for review. However, if we go back to our merge commit orl, we can see that the merge commit is now marked as conflicting:

This makes sense, because we’ve removed manually resolved the conflicts from txs. Jujutsu no longer has the metadata about how the conflict came about from merging different files, so orl now has a conflict. Typically, this isn’t that big an issue since you can just delay conflict resolution for that individual commit until you’re done working on that branch. You can then remove that branch from the merge commit after that.

If you do want to continue working on both branches, you can also restore the state of the working directory to its original state, before squashing the commit. First, get the commit ID of the change uyl that we wrote originally, before any commit manipulation (128d5444 from above), then run jj restore:

This restores all the files in commit orl to their state in commit 128d5444—the original files before the conflict occured due to squashing of commits. This has the effect of solving the conflict within the merge commit orl:

## Conclusion

I’ve shown how you can use Jujutsu to manipulate merge commits and work on separate logical branches of code, by adding and removing parents using the jj rebase command. Arguably, this workflow might be better visualized with a graphical interface to see how the commit graph is being manipulated. There’s a GUI app for Jujutsu, called GG, with a pretty convincing demo of this workflow.

Working on multiple branches of code at the same time can be really powerful. Personally, I use this workflow all the time to avoid having to switch branches. This is especially convenient when working on small bugfixes where it’s definitely easier to just work in the current directory.

Merging multiple branches together also allows you to very simply test out various features at the same time, without having to wait for all of them to be merged into the main branch. In fact, I use this to build a custom jj binary which contains various features which haven’t been merged into main.

Even if you aren’t convinced about switching to Jujutsu, I think this workflow is still valuable. In fact, GitButler—a new Git client—was recently launched with a similar end product: making it easy to activate different “virtual branches” in your working directory. Otherwise, alternative tools like git-branchless might allow you to do something similar.

If you are intrigued by Jujutsu, do check out the introduction and tutorial. I’d also recommend Chris’s article and video series. Steve Klabnik also has a long-form tutorial on Jujutsu, which includes a chapter on this workflow.

## Footnotes

1. 
1. 
1. 

