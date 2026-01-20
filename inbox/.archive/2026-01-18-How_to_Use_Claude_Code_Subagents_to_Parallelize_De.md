---
type: link
source: notion
url: https://zachwills.net/how-to-use-claude-code-subagents-to-parallelize-development/
notion_type: Software Repo
tags: ['Running']
created: 2025-09-13T12:15:00.000Z
---

# How to Use Claude Code Subagents to Parallelize Development | zach wills

## Overview (from Notion)
- Leveraging AI to parallelize development can save significant time, allowing you to focus on family and personal interests while efficiently managing your software projects.
- Running multiple AI agents simultaneously can enhance productivity, making the development process less linear and more dynamic—perfect for balancing a busy life.
- The approach of breaking tasks into specialized roles can help you delegate effectively, mirroring how you might manage responsibilities at home and work.
- Embracing the idea of low-cost failure in a tech setting can encourage a culture of experimentation, which can be applied to parenting by allowing for trial and error in teaching your kids.
- Consider the implications of AI in your industry and how staying ahead can impact your startup's success in the competitive NYC market.
- An alternate view might suggest that reliance on AI could risk losing the human touch in software development, which is valuable in both tech and personal relationships.
- The use of AI tools can provide a structured way to manage complexity, not just in coding but also in juggling life’s various demands, ensuring you don’t miss important family moments.

## AI Summary (from Notion)
Utilizing Claude Code subagents allows for parallel execution of tasks in software development, significantly speeding up processes like feature planning and implementation. By assigning specialized agents for different tasks, such as product management, UX design, and software engineering, teams can generate comprehensive tickets and implement features more efficiently. This approach enhances workflow by isolating contexts for each agent, preserving quality and enabling rapid iteration, while also presenting challenges such as managing costs and ensuring effective synthesis of outputs.

## Content (from Notion)

4 Terminals Running Claude Code

In my last post I talked about how I spent a week heads down using AI to work on a greenfield engineering metrics tool. As I built it, I’d often navigate the web app and spot things that needed to be fleshed out. Sometimes it was a small typo; other times it was a bigger feature that was still TODO.

At one point I had Claude Code redesign the homepage to make it more lively. In doing so, it added some new functionality that didn’t fully exist yet: A “View All Insights” link that would show you all the AI-generated analyses about a given pull request or piece of work. Since I hadn’t actually built the page for it yet, it led to a 404.

Traditionally, fixing this would kick off a whole sequence of events. I’d have to scope out the feature, think about the UI, define the API needs, and write a detailed ticket. Then, I’d need to build the backend endpoint, create the UI components, and wire everything together. It’s a linear, manual process.

Instead, I took a different approach. I ran a single custom command to generate a ticket for the new page. This command invoked several specialist sub-agents (you can find their .md definitions in the appendix)—a product-manager, a ux-designer, and a senior-software-engineer—who worked in parallel to flesh out the requirements. The result was a fully-formed ticket, created in minutes.

Terminal window showing 3 subagents in Claude Code running in parallel.

Here’s a quick preview of the actual ticket these agents generated in Linear:

Screenshot from Linear for a ticket: "Add AI insights listing page with pagination"

With the plan defined, I could then feed that ticket into another command that kicks off the implementation agents (senior-software-engineer, code-reviewer, etc.).

This workflow changes the dynamic. What would normally take hours of planning, spec’ing, and building was done asynchronously while I focused elsewhere. If the agents get it wrong, I don’t really care—I’ll just fire off another run. The cost of failure is so low that optimizing for speed and taking more “shots on goal” is the right call.

This entire process—from planning to implementation—ran in the background across multiple terminals while I moved on to the next task. This is what true parallelization looks like; the agents were so active they even started hitting API rate limits.

## The Core Principles of an Agentic Workflow

My workflow is built on three core principles. Understanding them will help you apply this approach to your own tasks.

### 1. Parallel Execution for Speed

The most direct benefit is the ability to perform independent tasks concurrently instead of sequentially. A common task like scaffolding a new feature can be broken down into its constituent parts, with a specialist agent assigned to each.

### Example: Scaffolding a New API Integration in Parallel

Let’s say you need to add a new third-party API integration like processing payments with Stripe. Typically, you’d work sequentially: build the server-side route, then the client-side form, then the tests, and finally write the documentation.

With sub-agents, you can parallelize this work. An orchestrating agent, given the Stripe API documentation, can spin up multiple specialists at once:

- backendspecialist: Reads the docs and writes the Node.js API endpoint to handle the charge creation.
- frontend-specialist: Reads the same docs and builds the React component for the payment form that communicates with the backend endpoint.
- qa-specialist: Generates a corresponding integration test suite using Vitest to verify the backend logic.
- docs-specialist: Drafts a README.md section explaining the new feature, the required environment variables, and how to get API keys.
You receive a complete starting point in the time it takes to complete the longest single task.

```plain text
#mermaid-1757737226570{font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:16px;fill:#333;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-1757737226570 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-1757737226570 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-1757737226570 .error-icon{fill:#552222;}#mermaid-1757737226570 .error-text{fill:#552222;stroke:#552222;}#mermaid-1757737226570 .edge-thickness-normal{stroke-width:1px;}#mermaid-1757737226570 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-1757737226570 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-1757737226570 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-1757737226570 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-1757737226570 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-1757737226570 .marker{fill:#333333;stroke:#333333;}#mermaid-1757737226570 .marker.cross{stroke:#333333;}#mermaid-1757737226570 svg{font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:16px;}#mermaid-1757737226570 p{margin:0;}#mermaid-1757737226570 .label{font-family:"trebuchet ms",verdana,arial,sans-serif;color:#333;}#mermaid-1757737226570 .cluster-label text{fill:#333;}#mermaid-1757737226570 .cluster-label span{color:#333;}#mermaid-1757737226570 .cluster-label span p{background-color:transparent;}#mermaid-1757737226570 .label text,#mermaid-1757737226570 span{fill:#333;color:#333;}#mermaid-1757737226570 .node rect,#mermaid-1757737226570 .node circle,#mermaid-1757737226570 .node ellipse,#mermaid-1757737226570 .node polygon,#mermaid-1757737226570 .node path{fill:#ECECFF;stroke:#9370DB;stroke-width:1px;}#mermaid-1757737226570 .rough-node .label text,#mermaid-1757737226570 .node .label text,#mermaid-1757737226570 .image-shape .label,#mermaid-1757737226570 .icon-shape .label{text-anchor:middle;}#mermaid-1757737226570 .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-1757737226570 .rough-node .label,#mermaid-1757737226570 .node .label,#mermaid-1757737226570 .image-shape .label,#mermaid-1757737226570 .icon-shape .label{text-align:center;}#mermaid-1757737226570 .node.clickable{cursor:pointer;}#mermaid-1757737226570 .root .anchor path{fill:#333333!important;stroke-width:0;stroke:#333333;}#mermaid-1757737226570 .arrowheadPath{fill:#333333;}#mermaid-1757737226570 .edgePath .path{stroke:#333333;stroke-width:2.0px;}#mermaid-1757737226570 .flowchart-link{stroke:#333333;fill:none;}#mermaid-1757737226570 .edgeLabel{background-color:rgba(232,232,232, 0.8);text-align:center;}#mermaid-1757737226570 .edgeLabel p{background-color:rgba(232,232,232, 0.8);}#mermaid-1757737226570 .edgeLabel rect{opacity:0.5;background-color:rgba(232,232,232, 0.8);fill:rgba(232,232,232, 0.8);}#mermaid-1757737226570 .labelBkg{background-color:rgba(232, 232, 232, 0.5);}#mermaid-1757737226570 .cluster rect{fill:#ffffde;stroke:#aaaa33;stroke-width:1px;}#mermaid-1757737226570 .cluster text{fill:#333;}#mermaid-1757737226570 .cluster span{color:#333;}#mermaid-1757737226570 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:12px;background:hsl(80, 100%, 96.2745098039%);border:1px solid #aaaa33;border-radius:2px;pointer-events:none;z-index:100;}#mermaid-1757737226570 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#333;}#mermaid-1757737226570 rect.text{fill:none;stroke-width:0;}#mermaid-1757737226570 .icon-shape,#mermaid-1757737226570 .image-shape{background-color:rgba(232,232,232, 0.8);text-align:center;}#mermaid-1757737226570 .icon-shape p,#mermaid-1757737226570 .image-shape p{background-color:rgba(232,232,232, 0.8);padding:2px;}#mermaid-1757737226570 .icon-shape rect,#mermaid-1757737226570 .image-shape rect{opacity:0.5;background-color:rgba(232,232,232, 0.8);fill:rgba(232,232,232, 0.8);}#mermaid-1757737226570 .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#mermaid-1757737226570 .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#mermaid-1757737226570 :root{--mermaid-font-family:"trebuchet ms",verdana,arial,sans-serif;}Primary Agent: Integrate Stripe PaymentsDispatchbackend_agentfrontend_agentqa_agentdocs_agentAPI Route CodeReact ComponentTest SuiteREADME.md Draft
```

While some tasks are parallel, many complex processes are sequential. Here, agents act like an automated assembly line, with the output of one agent becoming the input for the next. This automates the entire lifecycle of a task, from planning to review.

### Example: The Automated Engineering Lifecycle

The workflow from the introduction is a perfect example of this. The product-manager and ux-designer agents first produce a ticket. That ticket is then handed off to the senior-software-engineer to build the feature. Finally, the resulting code is handed off to the code-reviewer for approval.

1. Planning & Implementation: The main orchestrator assigns a ticket, like the one from our intro, to the senior-software-engineer agent (running on Opus). The agent follows its defined “concise working loop” to plan and implement the code.
1. Code Review: Once done, the orchestrator triggers the code-reviewer. This agent is relentless. If rules are broken, it fails the process.
1. Iterative Refinement: A loop in the main context window feeds the reviewer’s feedback back to the engineer agent until the reviewer is satisfied.
This process yields structured, parsable artifacts. Here’s a sample output snippet from the code-reviewer:

CODE REVIEW REPORT 📊 Summary: Verdict: NEEDS REVISION Blockers: 0 High Priority Issues: 2 Medium Priority Issues: 1 🚨 Blockers (Must Fix) None. Basic test coverage is present and no critical security issues were found. ⚠️ High Priority Issues (Strongly Recommend Fixing) Issue: The main handler mixes responsibilities, violating the Single Responsibility Principle. Location: app/api/posts/[postId]/comments/route.ts:25-50 Analysis: The POST handler function currently performs request body validation, user authentication checks, and direct database interaction within a single block. This makes the function difficult to unit test and couples the API layer tightly with the database logic. Suggestion: Refactor this into separate concerns. Extract validation logic into a Zod schema for parsing the request body. Create a service function, e.g., createCommentForPost({ authorId, postId, content }), to encapsulate the business logic and database interaction. The route handler should then be a thin orchestrator: validate input, call the service function, and handle the response.

The orchestrator can parse this structured output and automatically manage the feedback loop.

## 3. Context Isolation for Quality

This is the most critical principle. If you asked a single AI agent to perform a complex, multi-stage task, it would exhaust its context window and start losing crucial details. By using subagents you give each specialist its own dedicated context window, ensuring the quality of each step is preserved.

### Example: Planning the “AI Insights” Page

In our intro story, the product-manager was able to use its entire 200k context to focus only on user needs and business logic. The senior-software-engineer then received the final ticket and could use its own fresh 200k context to focus only on implementation, without needing to remember the nuances of the initial product discussion. This prevents quality degradation.

- The product-manager can use its entire context to focus solely on user needs, acceptance criteria, and business logic.
- The ux-designer can use its full context to analyze existing design patterns and user flows, without needing to hold database schemas in memory.
- The senior-software-engineer then receives the concise output from the planners (the ticket) and can dedicate its entire 200k context to what matters for implementation: the codebase, technical constraints, and writing clean code.
The quality of each step is preserved because no single agent has to sacrifice its specialized knowledge to stay within the limit.

```plain text
#mermaid-1757737226764{font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:16px;fill:#333;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-1757737226764 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-1757737226764 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-1757737226764 .error-icon{fill:#552222;}#mermaid-1757737226764 .error-text{fill:#552222;stroke:#552222;}#mermaid-1757737226764 .edge-thickness-normal{stroke-width:1px;}#mermaid-1757737226764 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-1757737226764 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-1757737226764 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-1757737226764 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-1757737226764 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-1757737226764 .marker{fill:#333333;stroke:#333333;}#mermaid-1757737226764 .marker.cross{stroke:#333333;}#mermaid-1757737226764 svg{font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:16px;}#mermaid-1757737226764 p{margin:0;}#mermaid-1757737226764 .label{font-family:"trebuchet ms",verdana,arial,sans-serif;color:#333;}#mermaid-1757737226764 .cluster-label text{fill:#333;}#mermaid-1757737226764 .cluster-label span{color:#333;}#mermaid-1757737226764 .cluster-label span p{background-color:transparent;}#mermaid-1757737226764 .label text,#mermaid-1757737226764 span{fill:#333;color:#333;}#mermaid-1757737226764 .node rect,#mermaid-1757737226764 .node circle,#mermaid-1757737226764 .node ellipse,#mermaid-1757737226764 .node polygon,#mermaid-1757737226764 .node path{fill:#ECECFF;stroke:#9370DB;stroke-width:1px;}#mermaid-1757737226764 .rough-node .label text,#mermaid-1757737226764 .node .label text,#mermaid-1757737226764 .image-shape .label,#mermaid-1757737226764 .icon-shape .label{text-anchor:middle;}#mermaid-1757737226764 .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-1757737226764 .rough-node .label,#mermaid-1757737226764 .node .label,#mermaid-1757737226764 .image-shape .label,#mermaid-1757737226764 .icon-shape .label{text-align:center;}#mermaid-1757737226764 .node.clickable{cursor:pointer;}#mermaid-1757737226764 .root .anchor path{fill:#333333!important;stroke-width:0;stroke:#333333;}#mermaid-1757737226764 .arrowheadPath{fill:#333333;}#mermaid-1757737226764 .edgePath .path{stroke:#333333;stroke-width:2.0px;}#mermaid-1757737226764 .flowchart-link{stroke:#333333;fill:none;}#mermaid-1757737226764 .edgeLabel{background-color:rgba(232,232,232, 0.8);text-align:center;}#mermaid-1757737226764 .edgeLabel p{background-color:rgba(232,232,232, 0.8);}#mermaid-1757737226764 .edgeLabel rect{opacity:0.5;background-color:rgba(232,232,232, 0.8);fill:rgba(232,232,232, 0.8);}#mermaid-1757737226764 .labelBkg{background-color:rgba(232, 232, 232, 0.5);}#mermaid-1757737226764 .cluster rect{fill:#ffffde;stroke:#aaaa33;stroke-width:1px;}#mermaid-1757737226764 .cluster text{fill:#333;}#mermaid-1757737226764 .cluster span{color:#333;}#mermaid-1757737226764 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:12px;background:hsl(80, 100%, 96.2745098039%);border:1px solid #aaaa33;border-radius:2px;pointer-events:none;z-index:100;}#mermaid-1757737226764 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#333;}#mermaid-1757737226764 rect.text{fill:none;stroke-width:0;}#mermaid-1757737226764 .icon-shape,#mermaid-1757737226764 .image-shape{background-color:rgba(232,232,232, 0.8);text-align:center;}#mermaid-1757737226764 .icon-shape p,#mermaid-1757737226764 .image-shape p{background-color:rgba(232,232,232, 0.8);padding:2px;}#mermaid-1757737226764 .icon-shape rect,#mermaid-1757737226764 .image-shape rect{opacity:0.5;background-color:rgba(232,232,232, 0.8);fill:rgba(232,232,232, 0.8);}#mermaid-1757737226764 .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#mermaid-1757737226764 .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#mermaid-1757737226764 :root{--mermaid-font-family:"trebuchet ms",verdana,arial,sans-serif;}Phase 2: Implementation & Review Iterative ContextsHandoff ArtifactPhase 1: Planning Parallel ContextsFeedback / RevisionsApprovedInitial Goal: Build AI Insights Pageproduct_manager_agent 200k Contextux_designer_agent 200k ContextTicket.mdsenior_engineer_agent 200k ContextCode Draftcode_reviewer_agent 200k ContextFinal Code
```

These core patterns can be applied all over the software lifecycle.

- Generating Codebase Documentation: For a large, undocumented module, a primary agent can list all functions, classes, or files. It then spins up a sub-agent for each one, tasked with analyzing its code and writing comprehensive comments or diagrams. A final agent can then assemble these into a coherent README.md file.
- Large-Scale Automated Refactoring: To deprecate a function used in 75 files, have a primary agent grep for all instances, then spin up a dedicated sub-agent for each file to perform the replacement in a small, safe context. Even better if the refactor could be explained via an SOP; define the SOP as a command or a subagent and iteratively kick them off to complete the work.
- Incident Response Analysis: To understand an outage across three microservices, use three sub-agents to analyze each service’s logs in parallel. Each one extracts a timeline of critical events. The main agent’s job is much simpler: synthesize the three pre-processed timelines into a single report.
- For a Product Manager – Synthesizing User Feedback: A PM can take a CSV of 500 survey responses. A primary agent defines key themes (e.g., UI/UX, Performance, Pricing, Feature Requests). It then spins up multiple sub-agents to process chunks of 50 responses each, tagging them and pulling out representative quotes. The main agent receives the structured output and generates a final summary report with key insights.
- For a Security Engineer: To audit a new open-source library, a primary agent can coordinate sub-agents to scan for CVEs, scour GitHub issues for security reports, and analyze the code for common anti-patterns, assembling a multi-faceted security brief much faster than a manual review.
This approach is powerful, but it’s not magic. It’s a workflow for a developer, and with it come practical trade-offs.

- Managing Cost and Usage Limits: Chaining agents, especially in a loop, will increase your token usage significantly. This means you’ll hit the usage caps on plans like Claude Pro/Max much faster. You need to be cognizant of this and decide if the trade-off—dramatically increased output and velocity at the cost of higher usage—is worth it.
- The Art of Non-Determinism: The non-deterministic nature of LLMs means changing one part of your workflow—a sub-agent’s prompt, a command, the orchestrator’s instructions—can have a ripple effect. This makes debugging a challenge, but it’s also where the creative aspect of this engineering comes in. Your approach to handling these issues is part of the craft.
- The Synthesis Challenge: The “reduce” step where a final agent synthesizes the work of others is often the most difficult part. To mitigate this, it’s crucial to have each sub-agent save its output to a distinct file. This creates a clear audit trail, allowing you to debug why the final synthesis went wrong.
- Prompts as Fragile Dependencies: The agent definitions, while clear, should be treated like code. They need to be version-controlled, tested, and monitored. A model update from the provider can cause subtle behavioral drifts that can only be caught with a rigorous evaluation suite.
You have to get creative, and the specific application will depend on your situation. But when you start having the mindset of breaking down problems for specialist agents running in parallel, you’ll start to find the patterns that work for you. It’s a more robust and scalable way to solve complex problems.

### Appendix: Commands & Agent Definitions

For those who want to implement this workflow, here are the definitions for the custom command and agents used.

To add a new command in Claude Code, create a command.md file in ~/.claude/commands or ./.claude/commands

Similarly, you can define subagents by manually adding them to ~/.claude/agents/ or your project’s ./.claude/agents/ folder or by using the /agents command when in a Claude Code session.


