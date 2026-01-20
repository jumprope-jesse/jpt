---
type: link
source: notion
url: https://blog.vm0.ai/en/posts/manage-agents-team
notion_type: link
tags: ['Running']
created: 2026-01-19T14:09:00.000Z
---

# VM0 dev workflow: Managing AI agents like a team | VM0 Blog

## Content (from Notion)

In the VM0 dev team, every developer works with multiple Claude Code instances at the same time. Usually more than eight.

We treat Claude Code the same way we treat a real developer. (Yes, our company is half-jokingly called AI Colleagues Co!)

Because of that, the design philosophy behind the VM0 dev workflow mirrors classic team management practices in software engineering.

We use GitHub Issues to track work, Pull Requests for code review and merging, and GitHub Actions to handle automation. Over two months, this setup helped us ship 404 releases and write more than 230,000 lines of code.

This post explains how we made that workable, and why the key problem was never AI capability, but human coordination.

## AI-Powered dev workflow in practice

When you coordinate many AI agents in parallel, the bottleneck isn’t whether the model can write code. The real bottleneck is human cognitive load

This workflow consists of 14 slash commands, organized into three layers: Deep Dive, Issue Management, and PR Management.

Let’s first look at what my workflow looks like and how a feature usually gets built.

1.  
1.  
1.  
1.   
1.  
1.   
## Mindset shift: you’re leading a team of AI developers

The moment I realized we needed a structured workflow was when adding more Claude sessions actually made things worse. The more instances I ran in parallel, the harder it became to track what each one was doing, what state the work was in, and what had already been decided.

Without external tools, I simply couldn’t manage that many Claude instances at once. That’s when it clicked: this wasn’t an AI problem, it was a management problem.

GitHub is already the natural tool for collaboration in software development, so instead of inventing something new, I started treating Claude the same way I treat a human teammate. Once I did that, my management bandwidth suddenly scaled.

Ten years of project and team management experience finally made sense in this new context. By treating Claude as a team member and GitHub as our shared communication and management space, the whole system became manageable again.

A good team leader knows when to engage and when to step back:

This mirrors how effective software teams operate. I don't micromanage developer but set clear requirements, review key decisions, and verify the final output. The same principle applies when managing AI agents.

## The deep dive flow enforces structured, slow thinking

The deep dive workflow enforces deliberate thinking before implementation. Sometimes Claude runs into a dead end. When that happens, we force Claude to stop and think, and then talk it through together. It has three phases:

Each phase has strict boundaries.

- Research: no suggestions
- Innovate: no details
- Plan: no implementation
These constraints force Claude into slow, deliberate reasoning instead of jumping straight to code. Without them, edge cases and architectural concerns are often missed!

### Usage example

```plain text
/deep-research investigate the authentication flow, I'm seeing token expiration issues

[Claude researches, analyzes 12 related files, finds 3 similar patterns]

/deep-innovate what are our options for fixing this?

[Claude presents 3 approaches with trade-offs, you pick one]

/issue-create let's track this fix


```

For simple tasks, you can skip the deep dive and go directly to /issue-create.

For complex tasks with technical uncertainty, the deep dive phases help ensure you and Claude are aligned before implementation begins.

## Use GitHub as shared memory

Most AI tools treat context as temporary. When the session ends, the memory disappears.

VM0 uses GitHub as persistent memory:

This also solves a human problem: context recovery.

When I am managing 8+ Claude instances, I receive notifications that work is complete. But I can't reconstruct from Claude's conversation what it was doing, what decisions were made, or what the current state is.

GitHub issues solve this. Each issue displays:

- The original requirements
- Research findings (what was discovered)
- Innovation phase (what options were considered)
- The approved plan (what will be implemented)
This structured format makes review efficient. So I can quickly scan the phases, understand the approach, and approve or request changes, all without needing to remember the original conversation.

When work finishes, I don’t need to remember what happened in a chat window. I can open the issue and see the full story, structured and written down.

## Handoff between agents

Because all context lives in GitHub, work can move between agents seamlessly:

- One agent create an issue or PR
- Another continues later using /deep-research issue 123 or /issue-todo 123 or /deep-research PR 124
For long discussions, /issue-compact consolidates everything into a clean issue body. This makes handoffs easy for both humans and AI.

## Let’s summarize the workflow patterns

After all that, let me summarize a few practical tips.

### Simple tasks

```plain text
/issue-create → /issue-todo → /issue-continue → /pr-check-and-merge

```

Use this when requirements are clear and the work is straightforward.

### Complex tasks

```plain text
/deep-research → discussion → /deep-innovate → discussion →
/issue-create → /issue-todo → /issue-continue →
/pr-review-and-comment → /pr-check-and-merge

```

This prevents wasted effort on the wrong approach.

### Parallel work

Multiple agents can work at once while the human reviews completed checkpoints. This is where the workflow scales best.

```plain text
Agent 1: /issue-todo #123
Agent 2: /issue-todo #124
Agent 3: /pr-review-and-comment #100
Agent 4: /deep-research new feature requirements

```

## Command reference

### Deep dive commands

### Issue commands

### PR commands

## Getting started

1. Start simple: Use /issue-create → /issue-todo → /issue-continue for your first task
1. Add deep dive for complex tasks: When requirements are unclear or technically complex, start with /deep-research
1. Scale gradually: Add more Claude instances as you get comfortable with the review rhythm
1. Trust the process: Let Claude work autonomously between checkpoints
The workflow is designed to be adopted incrementally. You don't need to use all 14 commands from day one. Start with the basic issue flow, then add deep dive phases and parallel work as you gain confidence.

## Scaling considerations: What to do when you have more agents

The workflow has been tested with 10+ concurrent Claude instances. Our recommendation:

- Up to 10 agents: Comfortable for deep collaboration with each
- Beyond 10: Not recommended
The limiting factor isn't the workflow, it's human attention and decision quality. When managing more than 10 agents, you risk becoming a bottleneck at review checkpoints, and decision quality starts to degrade.

The classic "two pizza team" principle applies here. The same constraints that limit human team size also limit how many AI agents one person can effectively manage.

> 

The VM0 dev workflow changes how we think about software development when AI becomes part of the team.

When you treat AI agents as team members rather than tools, everything clicks into place. GitHub becomes your team's shared memory. Issues become work items. PRs become deliverables. And you become the team leader, focusing on architecture, direction, and quality while your AI team handles the implementation.

That's how we shipped 404 releases in 2 months. And it's how you can scale your own development with AI.

How to automatically test AI agent skills against rapidly changing APIs


