---
type: link
source: notion
url: https://zackproser.com/blog/openai-codex-review
notion_type: Software Repo
tags: ['Running']
created: 2025-05-20T15:04:00.000Z
---

# OpenAI Codex Hands-on Review

## Overview (from Notion)
- Codex can streamline your workflow, allowing you to juggle family responsibilities while managing software projects.
- The chat-first interface might resonate with your multitasking lifestyle, enabling you to initiate tasks quickly and check in on progress without getting bogged down.
- The focus on rapid task execution aligns well with the need for efficiency in both personal and professional life.
- Unique viewpoint: The concept of a "dream untethered workflow" could inspire you to think about how to optimize your work-life balance, potentially using tools like Codex to free up time for family.
- Alternate view: Consider the limitations highlighted, such as poor error handling and the inability to directly address network dependencies, which may require you to remain hands-on for critical tasks.
- The idea of using AI for mundane tasks might lead you to reflect on the broader implications of automation in your field, especially in a fast-paced environment like NYC.
- Explore how Codex’s potential for increased productivity can be harnessed to allow more meaningful family time or personal projects.

## AI Summary (from Notion)
Codex offers a chat-first interface for managing tasks across GitHub repositories, allowing users to initiate multiple tasks in parallel. While it has potential for productivity gains, current limitations include poor error handling, challenges with multi-turn updates, and lack of internet connectivity in execution sandboxes, which hinder its effectiveness for complex tasks. Improvements are anticipated to enhance usability and integration capabilities.

## Content (from Notion)

The interface I want and the performance I'll have to wait for...

## Table of contents

- Codex: How it works
- Things I like about Codex 
- Things I'm waiting on to improve 
- Did it unlock insane productivity gains for me?
## Codex: How it works

Codex is currently a chat-first experience. You gain access by being invited or by paying for the Pro ($200/per month) subscription.

Codex is a chat-first experience now

Once you've got access, you start by enabling multi-factor authentication, which is required to use Codex. Next, you authorize the Codex GitHub app for each organization you want it to work with.

Codex then clones your repositories into its own sandboxes so it can run commands and create branches on your behalf.

If you maintain dozens of public and private repositories, this setup is fantastic because you can jump between projects and queue up tasks for each of them without leaving the interface.

If you only keep a single repo or two, the overhead may feel heavier than just asking an LLM for help or working in an AI-powered editor like Cursor.

## Things I like about Codex

### Consciousness and desire are multi-threaded

Codex feels like it was designed for me.

This GitHub connection allows you to specify which repository and which branch your current instructions are for, because the primary chat interface is contemplated as a place for you to rapid-fire a day's worth of tasks into the interface to spin up multiple tasks in parallel.

A real Codex task

I took a swing through the Codex best practices guide, which encourages you to spin up as many tasks as you need. The current rate limits support you doing this.

This is one of the things I like most about Codex and that I'm most excited for as the platform improves, because this gels with the way I work.

Asking Codex to resolve a merge issue

By the time I start work, I tend to have a laundry list of items I want to complete, so initiating a ton of them in parallel via natural language feels like a reasonable interface.

### I think this will eventually support my dream untethered workflow

As I wrote about in Walking and talking with AI in the woods, ideally I'd like to start my morning in an office, launch a bunch of tasks, get some planning out of the way, and then step out for a long walk in nature.

Codex is usable from my phone even today:

Codex is even usable on mobile

I think, ultimately, once some of the sharp edges are polished, Codex will support me and others in performing our work effectively away from our desks.

Codex and similar tools will ultimately support workers who want to be effective away from their desks

### Follow ups via chat

Once your initial task has had some time to bake, you can click into it to view its progress, see the logs and make follow-up requests via a very familiar chat interface.

Codex exposes a familiar chat interface

### Looks good - ship it!

Once you're satisfied, Codex can open your PRs

Once you're satisfied with the changes on a given branch, you can tell Codex to open a PR for you, and it will automatically fill in the description.

Codex hard at working opening your pull request

### Monitor logs and progress of tasks

You can step into any tasks to see the chat pane but also the raw logs, which show you the commands and shells that Codex is spawning in order to make changes.

Launching a new environment via Codex

## Things I'm waiting on to improve

### Poor error handling

Starting tasks fails. Opening pull requests fails.

Why?

Codex currently shows evidence of poor or incomplete error handling

Who knows.

### Code quality and one-shot task execution

I've been experimenting with Codex for about 3 days at the time of writing. I haven't yet noticed a marked difference in the performance of the Codex model, which OpenAI explains is a descendant of GPT-3 and is proficient in more than 12 programming languages.

Right now, it feels like I can spin up multiple tasks in parallel with a 40-60% chance that I'll be content enough with the result to hit the Open PR button instead of requesting changes.

So far Codex has been perfect for firing off a bunch of maintenance-level updates: minor copy tweaks, style changes and other small chores. I've tried asking it to tackle larger refactors and the experience quickly becomes cumbersome. The current workflow wants to open a fresh pull request for every iteration, which means pushing follow-up commits to an existing branch is awkward at best.

### Multi-turn updates on a branch

Updating existing PRs is rough.

It's not clear when or if changes will be pushed on an existing branch, and right now the app encourages you to create more pull requests. That makes multi-step refactors tricky because you can't reliably iterate on the same branch within Codex. Until this becomes smoother, I plan to use it mainly for the quick wins that can ship in a single pass.

### Lack of network connectivity in execution sandboxes

To be clear, I understand this is an intentional design choice. It mitigates remote code execution vulnerabilities amongst others.

This currently blocks the use of Codex for a lot of the tasks that working developers are going to want to use it for, namely resolving annoying dependency issues by installing a more recent version of a package and regenerating the relevant lockfiles in the process.

Codex can't reach the internet right now, but it does have your repo freshly cloned and made available to its execution environment.

This means it can't pnpm add @tar-fs@latest even if you ask it to. So, for now, I'll still be pulling down these branches and fixing them locally or commenting @dependabot rebase on PRs that support it.

## Did it unlock insane productivity gains for me?

Not yet, but I can see how it will once:

- More tasks become one-shottable via additional refinements or model training or perhaps even the ability to multipex between different models for different tasks
- The dev ex around opening and pushing to existing branches to update an already open pull request is improved
- Codex enables more integrations with additional OpenAI platform capabilities such as generating images.
- Codex (potentially) becomes more of the high-level orchestration and signaling layer that humans primarily work out of
At the moment, Codex is useful for flushing the low priority yet numerous and tedious maintenance tasks and small updates at the beginning of the day.

For significant refactoring or feature-building, I'm still better served doing that myself in an IDE with optional LLM support.

I'm sure that imminent improvements will make Codex even more usable soon

I'm confident that shortly I'll be able to use Codex as an indeal interface for starting a day of work and for keeping tabs on what needs attention and what is up next.


