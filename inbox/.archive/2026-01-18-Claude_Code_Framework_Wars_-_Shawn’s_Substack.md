---
type: link
source: notion
url: https://shmck.substack.com/p/claude-code-framework-wars
notion_type: Tech Deep Dive
tags: ['Running']
created: 2025-09-07T11:27:00.000Z
---

# Claude Code Framework Wars - Shawn’s Substack

## Overview (from Notion)
- Embrace AI as a collaborative tool: Shift your focus from coding to managing AI-driven processes, enhancing productivity while maintaining oversight.
- Integration of structured frameworks: Establishing clear workflows with Claude can streamline development, allowing you to balance work and family life more effectively.
- Experiment with open-source projects: Engage with the developer community to discover innovative approaches that can give your startup a competitive edge.
- Foster a growth mindset: Embrace the transition from developer to project manager, allowing for personal and professional growth as you navigate the evolving tech landscape.
- Consider potential challenges: Be aware of over-reliance on AI, ensuring that human oversight remains integral to maintain quality and creativity in your projects.
- Reflect on work-life balance: Use AI to automate mundane tasks, freeing up more time for family and personal interests, enhancing overall life satisfaction.
- Explore the future of work: This shift towards AI collaboration may redefine roles in tech, creating opportunities for new business models that blend technology with personal engagement.

## AI Summary (from Notion)
Claude can automate coding, allowing developers to focus on higher-value roles. Key decisions include task management, guiding Claude with structured prompts, coordinating multiple agents, and preserving context. The framework emphasizes that AI performs best with clear structure, transforming developers' roles rather than replacing them. The goal is to manage AI as teammates, enhancing productivity and collaboration in software development.

## Content (from Notion)

We’re just now starting to learn how to work with AI as software developers.

The big idea: Claude can automate the coding, while you step into higher-value roles as project manager, designer, and software architect. The trick is to stop treating Claude as a chatbox and start treating it as a framework—a set of rules, roles, and workflows that make its output predictable and valuable.

Even more fascinating - claude code doesn’t require code to become a framework - just structured prompts. And right now, the developer community is experimenting wildly—what you could call the Claude Code Framework Wars. Dozens of open-source projects are testing different recipes for how to work with AI productively.

Here’s a field report.

## The Menu of Decisions

If you’re designing your own Claude setup, there are seven big choices you’ll need to make:

1. Where tasks live?
1. How do you guide Claude?
1. How agents coordinate?
1. How sessions are run?
1. How code accesses tools?
1. How code is developed?
1. How code is delivered?
1. How context is preserved?
Think of it like setting up a kitchen. Claude is the line cook, but you need to decide: where do recipes go, how do cooks learn the house style, who runs the kitchen, and how does food reach the table?

### 1. Where Tasks Live

Claude needs a source of truth.

- Markdown backlogs: Tasks as a todo list in markdown.
- Structured text: Specify product specs that get converted into tasks.
- Issues/tickets: Store specs as GitHub Issues or Jira tickets, tie them to code reviews.
Takeaway: Tasks must live somewhere Claude can see them and you can trace them.

### 2. How Claude Is Guided

Replace ambigious prompts with structure.

- Command libraries: Prebuilt slash commands (e.g. /create-tasks, /review).
- Coding standards: Clarify the tech stack, coding guidelines
- Definition of Done: Encode “definition of done”
- Trigger Validation Hooks: enforce linting & tests on every change
- Claude as a Reviewer: Claude as the developer and reviewer
Takeaway: Claude does better work when the rules are clear and repeatable.

### 3. How Agents Coordinate

Multiple Claudes? Give them roles and a plan.

- Role simulation: AI as PM, architect, developer, tester.
- Swarm parallelism: Many agents run at once in a structured flow (e.g. spec → pseudocode → code → tests).
- Repo-native artifacts: Store tasks, logs, and ADRs in codebase so memory persists.
Takeaway: Coordination keeps many AI workers from stepping on each other.

### 4. How Sessions Are Run

AI output can get messy—sessions are your workstation setup.

- Terminal orchestration: Claude controls commands, panes, and logs.
- Parallel worktrees: Run multiple branches in parallel using Git Worktrees.
- Parallel containers: Run Claude in isolated containers to avoid collisions
Takeaway: Get more done by running tasks in parallel without constant collisions

### 5. How Claude Accesses Tools

Give Claude knowledge about your whole stack.

- MCP Integrations (Model Context Protocol): bundled MCP servers that connect Claude to external resources—browsers, databases, test runners, even UI automation frameworks.
- Custom Tool Libraries: built in shell scripts and commands
- Database Accessors: tooling for strong database access
- Testing and Validation Hooks: run tests (e.g., Vitest, Jest) before declaring work “done.” This ties Claude’s output into real validation loops
Takeaway: Tooling turns Claude from “a smart autocomplete” into “an active teammate” who can check their own work and interact with your systems.

### 6. How Code Is Developed

Claude can wear different hats depending on what you need:

- Project Manager (PM): turns product specs into tasks and backlogs
- Architect: designs the overall structure, defines interfaces, and sets conventions before coding begins.
- Implementer: writes code inside those guardrails, following tests and standards.
- Tester: runs unit tests or UI checks via MCP servers
- Reviewer: audits PRs for quality, readability, and risk.
Takeaway: leverage AI at each step of the software lifecycle.

### 7. How Code Is Delivered

How does the code reach your repo?

- Small diffs: AI picks up tickets and produces small PRs, always reviewed.
- Experiments: Deploying changes behind feature flags
- Full app scaffolds: AI builds and deploys entire apps from high-level prompts.
Takeaway: Pick your scale—safe iteration for production, scaffolds for prototypes.

### 8. How Context Is Preserved

Claude forgets. Frameworks remember.

- Docs and journals: Keep CLAUDE.md, architecture notes, and project journals fresh.
- Persistent memory & checkups: Recap recent work, run project health checks, store decisions.
Takeaway: Without memory, AI repeats mistakes. With memory, it compounds progress.

## Putting It Together

Think of these options as a menu. You don’t need to order everything at once.

- Beginner setup: Markdown backlog + ticket diffs.
- Structured team: Product Specs + standards + role simulation.
- Experiment-heavy: Repo artifacts + parallel sessions.
- Prototype mode: App builder + docs scaffolding.
## The Payoff

The early lesson from the Claude Code framework wars is simple: AI works best when you give it structure.

Claude isn’t replacing developers—it’s shifting their roles. You spend less time typing boilerplate and more time shaping specs, reviewing designs, and defining architecture. If you’re not doing your job, things can go off the rails fast.

We’re still early, but the frameworks are converging on a future where AI is not a magic box but a set of teammates you manage. And that’s the exciting part: the more structure you give, the more you get back.

Subscribe for more.


