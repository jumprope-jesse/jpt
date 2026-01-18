---
type: link
source: notion
url: https://github.com/microsoft/amplifier
notion_type: Software Repo
tags: ['Running']
created: 2025-10-11T18:50:00.000Z
---

# GitHub - microsoft/amplifier

## Overview (from Notion)
- Amplifier can streamline your development process, making it easier to juggle work and family life by automating mundane tasks and reducing stress.
- The specialized agents allow you to tackle complex coding problems efficiently, freeing up time for family or personal projects.
- Its knowledge extraction features can help you build a repository of insights that could enhance your decision-making as a founder.
- The parallel development capabilities enable you to experiment with multiple solutions at once, offering a creative outlet and potentially leading to innovative products.
- This project emphasizes a future where AI handles tedious tasks, which might resonate with your desire for efficiency in both work and life.
- While the technology is promising, consider the implications of relying heavily on AI, such as the need for human oversight to avoid potential pitfalls.
- Alternative views might highlight concerns about AI's unpredictability and the balance between automation and personal oversight in your work and parenting.

## AI Summary (from Notion)
Amplifier is a research demonstrator for AI-assisted development, providing a complete environment with specialized agents for various tasks, pre-loaded context, and automation tools. It allows parallel development, knowledge extraction, and conversation transcripts to enhance coding efficiency. Users need Python, Node.js, and Git for setup, and the system is designed to evolve with AI technologies, although it is currently experimental and not accepting contributions.

## Content (from Notion)

# Amplifier: Supercharged AI Development Environment

> 

Caution

This project is a research demonstrator. It is in early development and may change significantly. Using permissive AI tools in your repository requires careful attention to security considerations and careful human supervision, and even then things can still go wrong. Use it with caution, and at your own risk.

## What Is Amplifier?

Amplifier is a complete development environment that takes AI coding assistants and supercharges them with discovered patterns, specialized expertise, and powerful automation — turning a helpful assistant into a force multiplier that can deliver complex solutions with minimal hand-holding.

We've taken our learnings about what works in AI-assisted development and packaged them into a ready-to-use environment. Instead of starting from scratch every session, you get immediate access to proven patterns, specialized agents for different tasks, and workflows that actually work.

Amplifier provides powerful tools and systems:

- 20+ Specialized Agents: Each expert in specific tasks (architecture, debugging, security, etc.)
- Pre-loaded Context: Proven patterns and philosophies built into the environment
- Parallel Worktree System: Build and test multiple solutions simultaneously
- Knowledge Extraction System: Transform your documentation into queryable, connected knowledge
- Conversation Transcripts: Never lose context - automatic export before compaction, instant restoration
- Automation Tools: Quality checks and patterns enforced automatically
## 🚀 Step-by-Step Setup

### Prerequisites

Before starting, you'll need:

- Python 3.11+ - Download Python
- Node.js - Download Node.js
- VS Code (recommended) - Download VS Code
- Git - Download Git
> 

### Installation

1.  
1.   
1.       
1.  
## 📖 How to Use Amplifier

### Basic Usage

Start Claude in the Amplifier directory to get all enhancements automatically:

```plain text
cd amplifier
claude  # Everything is pre-configured and ready
```

### Using with Your Own Projects

Want Amplifier's power on your own code? Easy:

1.  
1.  
1.  
### Parallel Development

Why use this? Stop wondering "what if" — build multiple solutions simultaneously and pick the winner.

```plain text
# Try different approaches in parallel
make worktree feature-jwt     # JWT authentication approach
make worktree feature-oauth   # OAuth approach in parallel

# Compare and choose
make worktree-list            # See all experiments
make worktree-rm feature-jwt  # Remove the one you don't want
```

Each worktree is completely isolated with its own branch, environment, and context.

See the Worktree Guide for advanced features, such as hiding worktrees from VSCode when not in use, adopting branches from other machines, and more.

### Enhanced Status Line

See costs, model, and session info at a glance:

Example: ~/repos/amplifier (main → origin) Opus 4.1 💰$4.67 ⏱18m

Shows:

- Current directory and git branch/status
- Model name with cost-tier coloring (red=high, yellow=medium, blue=low)
- Running session cost and duration
Enable with:

```plain text
/statusline use the script at .claude/tools/statusline-example.sh

```

## 🎯 Key Features

### Specialized Agents

Instead of one generalist AI, you get 20+ specialists:

Core Development:

- zen-architect - Designs with ruthless simplicity
- modular-builder - Builds following modular principles
- bug-hunter - Systematic debugging
- test-coverage - Comprehensive testing
- api-contract-designer - Clean API design
Analysis & Optimization:

- security-guardian - Security analysis
- performance-optimizer - Performance profiling
- database-architect - Database design and optimization
- integration-specialist - External service integration
Knowledge & Insights:

- insight-synthesizer - Finds hidden connections
- knowledge-archaeologist - Traces idea evolution
- concept-extractor - Extracts knowledge from documents
- ambiguity-guardian - Preserves productive contradictions
Meta & Support:

- subagent-architect - Creates new specialized agents
- post-task-cleanup - Maintains codebase hygiene
- content-researcher - Researches from content collection
[See .claude/AGENTS_CATALOG.md for the complete list]

### Knowledge Base

Why use this? Stop losing insights. Every document, specification, design decision, and lesson learned becomes part of your permanent knowledge that Claude can instantly access.

Note

Knowledge extraction is an evolving feature that continues to improve with each update.

1. 
1.  
1.  
### Conversation Transcripts

Never lose context again. Amplifier automatically exports your entire conversation before compaction, preserving all the details that would otherwise be lost. When Claude Code compacts your conversation to stay within token limits, you can instantly restore the full history.

Automatic Export: A PreCompact hook captures your conversation before any compaction event:

- Saves complete transcript with all content types (messages, tool usage, thinking blocks)
- Timestamps and organizes transcripts in .data/transcripts/
- Works for both manual (/compact) and auto-compact events
Easy Restoration: Use the /transcripts command in Claude Code to restore your full conversation:

```plain text
/transcripts  # Restores entire conversation history

```

The transcript system helps you:

- Continue complex work after compaction without losing details
- Review past decisions with full context
- Search through conversations to find specific discussions
- Export conversations for sharing or documentation
Transcript Commands (via Makefile):

```plain text
make transcript-list            # List available transcripts
make transcript-search TERM="auth"  # Search past conversations
make transcript-restore         # Restore full lineage (for CLI use)
```

### Modular Builder (Lite)

A one-command workflow to go from an idea to a module (Contract & Spec → Plan → Generate → Review) inside the Amplifier Claude Code environment.

- Run inside a Claude Code session: 
- Docs: see docs/MODULAR_BUILDER_LITE.md for the detailed flow and guardrails.
- Artifacts: planning goes to ai_working/<module>/… (contract/spec/plan/review); code & tests to amplifier/<module>/….
- Isolation & discipline: workers read only this module’s contract/spec plus dependency contracts. The spec’s Output Files are the single source of truth for what gets written. Every contract Conformance Criterion maps to tests. 〔Authoring Guide〕
### Modes

- auto (default): runs autonomously if confidence ≥ 0.75; otherwise falls back to assist.
- assist: asks ≤ 5 crisp questions to resolve ambiguity, then proceeds.
- dry-run: plan/validate only (no code writes).
### Continue later

Re‑run /modular-build with a follow‑up ask; it resumes from ai_working/<module>/session.json.

### Development Commands

```plain text
make check            # Format, lint, type-check
make test             # Run tests
make ai-context-files # Rebuild AI context
```

## 💡 Example Workflows

### Building a Feature in Your Code

1. Design: "Use zen-architect to design my notification system"
1. Build: "Have modular-builder implement the notification module"
1. Test: "Deploy test-coverage to add tests for the new notification feature"
### Debugging Your Application

1. Investigate: "Use bug-hunter to find why my application's API calls are failing"
1. Verify: "Have security-guardian review my authentication implementation"
### Knowledge-Driven Development

1. Extract: make knowledge-update (processes your documentation)
1. Query: make knowledge-query Q="error handling patterns"
1. Apply: "Implement error handling using patterns from our knowledge base"
> 

- Not accepting contributions yet (but we plan to!)
- No stability guarantees
- Pin commits if you need consistency
- This is a learning resource, not production software
- No support provided - See SUPPORT.md
## 🔮 Vision

We're building toward a future where:

1. You describe, AI builds - Natural language to working systems
1. Parallel exploration - Test 10 approaches simultaneously
1. Knowledge compounds - Every project makes you more effective
1. AI handles the tedious - You focus on creative decisions
The patterns, knowledge base, and workflows in Amplifier are designed to be portable and tool-agnostic, ready to evolve with the best available AI technologies.

See AMPLIFIER_VISION.md for details.

## Current Limitations

- Knowledge extraction works best in Claude environment
- Processing time: ~10-30 seconds per document
- Memory system still in development
"The best AI system isn't the smartest - it's the one that makes YOU most effective."

## Contributing

Note

This project is not currently accepting external contributions, but we're actively working toward opening this up. We value community input and look forward to collaborating in the future. For now, feel free to fork and experiment!

Most contributions require you to agree to a Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us the rights to use your contribution. For details, visit Contributor License Agreements.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the Microsoft Open Source Code of Conduct. For more information see the Code of Conduct FAQ or contact opencode@microsoft.com with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft trademarks or logos is subject to and must follow Microsoft's Trademark & Brand Guidelines. Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship. Any use of third-party trademarks or logos are subject to those third-party's policies.


