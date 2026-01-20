# Agentic Coding Practices

Methodologies and lessons from teams using AI agents for software development at scale.

---

## The New Calculus of AI-based Coding

*Source: https://blog.joemag.dev/2025/10/the-new-calculus-of-ai-based-coding.html - Added: 2026-01-18*

Experience report from a team at Amazon Bedrock achieving 10x throughput with AI-assisted development.

### Agentic Coding vs Vibe Coding

**Agentic coding** (preferred term): Human and AI agent collaborate, with human oversight and accountability.

Key distinctions:
- Every commit has an engineer's name attached who must review and stand behind the code
- Engineers pay attention to every line the agent produces
- Use steering rules to set constraints for how the AI agent operates
- "Boring is usually good" - focus on robust software, not flashy demos

### Workflow Pattern

1. Break down task until you have clarity (often using AI to explore approaches)
2. Prompt the AI agent
3. Review its output
4. Iterate with it until satisfied
5. Occasionally take over and finish manually

Result: ~80% of committed code written by AI agent, with rigorous human review.

### Why Rust Works Well

- Compiler focuses on correctness and safety
- Catches many problems at compile time
- Helpful error messages enable the agent to iterate effectively

### The Velocity Challenge: "Driving at 200mph"

**Key insight:** Bug probability per commit may not change much with AI, but at 10x throughput, the math changes fundamentally.

- Annual production bug becomes weekly occurrence
- Bugs in integration/test environments slow down shared codebase
- At high velocity, commits begin interacting in unexpected ways

**Formula:** To increase engineering velocity by 10x, need to decrease problematic commits by 10x+ too.

### The Cost-Benefit Rebalance

Ideas that were "sound in principle but too expensive" just had their costs decrease by an order of magnitude.

#### "Wind Tunnel" Style Testing

Inspired by airplane manufacturing: early simulations, component testing, wind tunnel testing, testing to breaking point.

**Pattern:** High-fidelity fake versions of external dependencies run locally
- Build-time tests that verify end-to-end behavior
- Inject unexpected behaviors and failures
- Catch bugs that previously only surfaced in test environments

**The team's approach:**
- Maintains fake implementations of auth, storage, chain replication, inference engine
- Test harness spins up entire distributed system locally
- Canaries run against the fully assembled stack

**Previously:** "Too expensive" resistance
**Now:** A few days to implement for a relatively complex system

### CI/CD at High Velocity

Traditional healthy team: Several hours to build/package/test, days to roll through stages.

**At 10x velocity:**
- While one set builds, another dozen commits waiting
- A batch may contain 100+ commits by deployment time
- One problematic commit = full rollback, grinding pipeline to halt

**F1 Analogy:** Yellow flags slow everything down. Race organizers prepare for all accidents to restart in minutes.

**Requirement:** CICD pipelines need to identify, isolate, and revert issues in minutes, not hours/days.

### The Communication Bottleneck

At 10x velocity, you're making 10x decisions, not just writing 10x code.

**The conflict pattern:**
- Engineer A refactors auth flow
- That affects API Engineer B is extending
- These are architectural choices that ripple through codebase

**Traditional mechanisms fail:**
- Waiting for Slack creates bottlenecks
- Scheduling a sync blocks progress
- Async communication = risk of conflicting decisions

**Their solution:** Co-located team
- Walk over and hash it out in minutes
- Whiteboard discussions in real-time
- Align on approach, discuss trade-offs, get back to work

**Open challenge:** No solution yet for distributed teams at this velocity.

### Key Takeaways

1. **Can't bolt on AI agents to existing practices** - "Like adding a turbocharger to a car with narrow tires and old brakes"

2. **Bottleneck moves, not disappears:**
   - CI/CD pipelines designed for 10 commits/day buckle at 100
   - "Good enough" testing lets too many bugs through
   - Communication patterns create blocked work pile-ups

3. **AI can build its own supporting infrastructure** - Same agents increasing throughput can build the testing/deployment infrastructure to sustain it

4. **The real opportunity:** Making previously impractical engineering practices practical, not just writing more code faster

### Scaling Checklist

For teams considering agentic development at scale:

- [ ] Comprehensive local testing with fake dependencies
- [ ] Sub-minute CI/CD feedback loops
- [ ] Real-time communication channels (co-location or equivalent)
- [ ] Steering rules/constraints for AI agent behavior
- [ ] Strong type systems (Rust, TypeScript) for compile-time catches
- [ ] Human review and accountability for every commit

---

## Code Like a Surgeon

*Source: https://www.geoffreylitt.com/2025/10/24/code-like-a-surgeon (Geoffrey Litt, Notion) - Added: 2026-01-18*

Mental model for individual practitioners using AI coding tools effectively.

### The Surgeon Mindset

The "AI makes us all managers" framing is incomplete. A surgeon isn't a manager—they do the actual work, but their skills and time are highly leveraged with a support team handling prep, secondary tasks, and admin.

**Goal:** Spend 100% of your time doing stuff that matters.

### Primary vs Secondary Tasks

**Secondary tasks suitable for AI delegation:**
- Write a guide to relevant codebase areas before attempting a big task
- Spike out an attempt at a big change (review as a sketch, not necessarily use directly)
- Fix TypeScript errors or bugs with clear specifications
- Write documentation

**Key pattern:** Run secondary tasks async in the background—while eating lunch, or even overnight. When you sit down for a work session, everything is prepped and ready.

### The Autonomy Slider (Andrej Karpathy concept)

Different autonomy levels require different tools and mindsets:

| Task Type | Autonomy | Tools | What Matters |
|-----------|----------|-------|--------------|
| Primary (core creative work) | Low | Cursor tab-complete | Fast feedback loops, visibility |
| Secondary (grunt work) | High | Claude Code, Codex CLI | Eventually gets done; speed/visibility matter less |

**Warning:** Dangerous to conflate different parts of the autonomy spectrum.

### Historical Context

The "software surgeon" concept is old—Fred Brooks attributes it to Harlan Mills in *The Mythical Man-Month* (1975). Back then, the support roles were filled by humans.

**What AI changes:** The economics. Plus a subtle benefit around status hierarchies—you can now delegate pure grunt work without the awkwardness of giving lower-status team members all the unfulfilling tasks.

### 24/7 Availability

"I would never call a human intern at 11pm and tell them to have a research report on some code ready by 7am… but here I am, commanding my agent to do just that!"

### Related Ideas from Geoffrey Litt

- **AI HUDs over Copilots:** Consider non-copilot form factors that more directly extend the human mind
- **AI-generated tools:** Build custom tools (like debugger UIs) that make manual coding more fun
- **ChatGPT as muse, not oracle:** Use LLMs to ask questions and inspire creativity, not just answer

---

## Crystal - Multi-Session AI Code Manager

*Source: https://github.com/stravu/crystal - Added: 2026-01-18*

Desktop app for running multiple Claude Code and Codex sessions in parallel git worktrees.

### The Problem It Solves

AI coding agents take time to complete tasks. Instead of waiting, run multiple isolated sessions simultaneously on different tasks.

### Core Workflow

1. **Create sessions from prompts** - Each session gets its own isolated git worktree
2. **Iterate with AI** - Work with Claude Code or Codex; each iteration auto-commits for easy rollback
3. **Review diffs** - Built-in diff viewer, make manual edits as needed
4. **Squash and merge** - Combine commits with a clean message, rebase to main branch

### Key Features

| Feature | Description |
|---------|-------------|
| Parallel sessions | Run multiple Claude Code/Codex sessions simultaneously |
| Git worktree isolation | Each session works on isolated copy of code |
| Auto-commits | Every AI iteration creates a commit for easy rollback |
| Built-in diff viewer | Review changes without leaving the app |
| Run scripts | Configure test commands to validate changes in-app |
| Squash & rebase | Clean commit history when merging to main |

### Git Operations

- **Rebase from main**: Pull latest changes from main into worktree
- **Squash and rebase to main**: Combine all commits and merge cleanly

### Installation

```bash
# Homebrew
brew install --cask stravu-crystal

# Or download from GitHub releases for macOS/Windows
```

### Third-Party Deployment Support

Works with cloud providers/corporate infrastructure via settings file with ENV vars:

```json
{
  "env": {
    "CLAUDE_CODE_USE_BEDROCK": "1",
    "AWS_REGION": "us-east-2",
    "AWS_PROFILE": "my-aws-profile"
  }
}
```

### Connection to "Surgeon" Workflow

Crystal directly enables the async secondary task pattern: spin up multiple AI sessions, let them work in parallel, then review and merge the best results. Supports the "run overnight" workflow mentioned in Geoffrey Litt's surgeon model.

### Prerequisites

- Claude Code installed and logged in (or API key)
- Codex installed via npm (`@openai/codex`) or Homebrew
- Git installed

---

## When Coding Agents Don't Work (Karpathy's nanochat Experience)

*Source: [Andrej Karpathy - AGI is still a decade away](https://www.dwarkesh.com/p/andrej-karpathy) - Added: 2026-01-18*

Karpathy built nanochat (simplest complete LLM training pipeline) over a month and found agents "not net useful" for intellectually intense code.

### Three Modes of AI-Assisted Coding

| Mode | Description | When to Use |
|------|-------------|-------------|
| Reject all LLMs | Write everything from scratch | Probably wrong now |
| **Autocomplete** (Karpathy's sweet spot) | You're still the architect, LLM completes patterns | Core implementation work |
| Vibe coding / agents | "Hi, please implement this" | Boilerplate, familiar patterns |

### Why Agents Failed on nanochat

**Fundamentally:** Agents aren't good at code that has never been written before.

**Specific issues:**
- **Too much memory** of "typical ways" on the internet - couldn't accept custom implementations
- **Over-defensive** - excessive try-catch, production-grade patterns where simplicity was needed
- **Deprecated APIs** - using old patterns from training data
- **Bloating** - adding unnecessary complexity
- **Misunderstanding custom code** - kept trying to make Karpathy use DDP container when he had his own gradient sync

**Example:** Karpathy wrote custom gradient synchronization instead of PyTorch's Distributed Data Parallel. Models kept insisting he use DDP, couldn't understand the custom approach.

### Where Agents DO Work

1. **Boilerplate code** - copy-paste patterns
2. **Code that's common on the internet** - lots of training examples
3. **Languages you're less familiar with** - Karpathy used more vibe coding for Rust tokenizer port
4. **When you have tests** - validation gives confidence

### The Information Bandwidth Point

> "It's annoying to have to type out what I want in English because it's too much typing."

With autocomplete: navigate to location, type first few characters → model completes. This is **higher information bandwidth** than describing what you want in prose.

### Implications for AI Research Automation

This is highly relevant to "AI automating AI research" forecasts:

> "They're not very good at code that has never been written before, which is what we're trying to achieve when we're building these models."

The asymmetric weakness is precisely in novel intellectual work - suggesting AI research acceleration may be slower than demos imply.

---

## Vibe Engineering (Simon Willison)

*Source: https://simonwillison.net/2025/Oct/7/vibe-engineering/ - Added: 2026-01-18*

A proposed term to distinguish professional, accountable AI-assisted development from casual "vibe coding."

### The Terminology Gap

**Vibe coding** = fast, loose, irresponsible AI development. Entirely prompt-driven with no attention to how the code works.

**Vibe engineering** = seasoned professionals accelerating work with LLMs while staying accountable for the software they produce.

### Why It's Difficult

One of the "lesser spoken truths": working productively with LLMs as a software engineer on non-toy-projects is difficult. There's depth to understanding the tools, traps to avoid, and the pace of code generation raises the bar for human contribution.

### The Coding Agent Shift

Tools like Claude Code (Feb 2025), OpenAI Codex CLI (April), and Gemini CLI (June) represent a dramatic increase in usefulness for real-world problems.

**Credible engineers are now running multiple agents in parallel** - tackling several problems simultaneously. Willison was skeptical at first but found it "surprisingly effective, if mentally exhausting."

### Practices That LLMs Actively Reward

| Practice | Why It Matters More |
|----------|---------------------|
| **Automated testing** | Agents can iterate in a loop with a robust test suite. Without tests, agents claim things work without verification. Test-first is particularly effective. |
| **Planning in advance** | Iterate on the plan first, then hand off to the agent to write code. |
| **Comprehensive documentation** | LLMs can only keep subset of codebase in context. Good docs let them use APIs without reading all the code. Docs-first may enable AI to build matching implementation. |
| **Good version control** | Even more important when an agent made the changes. LLMs are "fiercely competent at Git" - can navigate history, use git bisect effectively. |
| **Effective automation** | CI, formatting, linting, CD to preview environment - agents benefit from these too. |
| **Culture of code review** | Fast, productive code review is essential. If you'd rather write than review, you'll struggle. |
| **Really good manual QA** | Beyond automated tests, predicting and testing edge cases manually. |
| **Strong research skills** | Figuring out best approaches and proving them before unleashing an agent. |
| **Preview environments** | Safely previewing features without deploying to production. |

### Management-Adjacent Skills

> "Getting good results out of a coding agent feels uncomfortably close to getting good results out of a human collaborator."

Requirements:
- Clear instructions
- Necessary context provided
- Actionable feedback on output

**Advantage over humans:** No worry about offending or discouraging them. But any existing management experience proves surprisingly useful.

### Developing New Intuitions

**What can be outsourced vs handled manually** - constantly evolving as models improve. A major part of effectiveness is maintaining this intuition.

**Updated estimation skills** - Always hard, now harder. Things that took long are faster, but estimates depend on new factors everyone is still figuring out.

### The Full Stack of Responsibilities

With vibe engineering, you're not just responsible for writing code:
- Researching approaches
- Deciding on high-level architecture
- Writing specifications
- Defining success criteria
- Designing agentic loops
- Planning QA
- Managing "a growing army of weird digital interns who will absolutely cheat if you give them a chance"
- Spending "so much time on code review"

### The Senior Engineer Connection

> "Almost all of these are characteristics of senior software engineers already!"

AI tools amplify existing expertise. More skills and experience = faster and better results with LLMs and coding agents.

### Why "Vibe Engineering" as a Name

- Establishes clear distinction from vibe coding
- Signals different, harder, more sophisticated approach
- Cheeky and likely controversial - appropriate since the space is "absurd in all sorts of ways"
- A bit of gatekeeping is "exactly what we need" here

---

## The AI Coding Trap (Chris Loy)

*Source: https://chrisloy.dev/post/2025/09/28/the-ai-coding-trap - Added: 2026-01-18*

The "tech lead's dilemma" as a lens for understanding AI coding productivity gaps.

### The Fundamental Disconnect

**Marketing claim:** AI makes coding 10X faster.
**Reality:** Marginal productivity gains in delivering working software (~10%).

**Why the gap?** Most of software development isn't typing code—it's thinking:
- Learning the domain
- Narrowing requirements
- Mapping abstractions
- Considering side effects
- Testing incrementally
- Squashing bugs

**Traditional flow:** Thinking → Coding
**AI-driven flow:** Coding → Trying to understand what the AI wrote

When AI writes code without human thinking upfront, time shifts to post-hoc understanding, review, and integration.

### The Tech Lead's Dilemma

As engineers become tech leads, they face a choice:
1. **Fair delegation** - Maximize learning for juniors, but delivery bottlenecked by slowest team members
2. **Mollycoddling** - Keep hard work for yourself, delegate only easy tasks

Mollycoddling accelerates short-term delivery but leads to:
- Siloing of experience
- Brittle teams
- Single points of failure
- Eventual burnout and crisis

**The third way:** Expose engineers to work at the limit of their capabilities, using processes that minimize delivery risk while enabling growth.

### LLMs as Lightning-Fast Junior Engineers

Two fundamental differences from human juniors:
1. **Speed:** Not constrained by thinking or writing time
2. **Learning:** No true capacity to learn—only improve via context engineering or new models

This maps to two deployment approaches:
- **AI-driven engineering:** Best practices, foregrounding human understanding, sustainable development
- **Vibe coding:** Speed over understanding, eventual wall of unsalvageable code

### Where Vibe Coding Works

Great for:
- Tiny projects
- Throwaway prototypes
- Anything simple enough to deliver without human thinking

**The wall:** You'll hit complexity that AI can't scale alone.

### The New Playbook: AI Across the SDLC

Treat LLMs as junior engineers requiring structure, standards, and processes. Apply best practices at every lifecycle stage:

| Stage | AI Application |
|-------|----------------|
| **Analyze** | Research existing patterns, map dependencies |
| **Design** | Explore architectural options, document trade-offs |
| **Implement** | Write code with constraints and steering rules |
| **Test** | Generate test cases, run validation loops |
| **Review** | Check for consistency, standards compliance |
| **Deploy** | Automate infrastructure, handle rollout |

### Key Insight

> "As with junior engineering talent, treating AI well requires understanding that delivering software is so much more than just writing code."

The same practices that make teams sustainable (code review, incremental delivery, TDD, pair programming, good docs, CI) apply to human-AI collaboration—they just need adaptation for the AI context.

---

## Unit of Work Management for AI Agents

*Source: http://blog.nilenso.com/blog/2025/09/15/ai-unit-of-work/ (nilenso blog) - Added: 2026-01-18*

The craft of AI-assisted software creation is substantially about correctly managing **units of work**—the major bottleneck is not intelligence, but providing the correct context.

### The Right-Sized Unit of Work

Breaking down tasks into "right-sized" units is perhaps the most powerful lever to improve context quality and output correctness.

**Two competing pressures:**
- **Too little context** → hallucinations, code incongruent with codebase practices
- **Too much context** → degraded quality from lack of focused attention

**Goal:** Find the smallest possible set of high-signal tokens that describe just the right amount of detail.

### Error Propagation Math

Napkin calculation for multi-turn agentic workflows:

| Per-Turn Success Rate | 10-Turn Task Success |
|----------------------|---------------------|
| 95% | 59.9% |
| 99% | 90.4% |
| 99.9% | 99.0% |

**Key insight:** Even small per-turn error rates compound dramatically over long-horizon tasks.

**METR benchmark findings:**
- GPT-5 achieves ~70% success on 2-hour tasks (METR "clean" benchmark)
- Real-world "messiness rating": Most production software scores 7-8/16 or higher
- Extrapolated real-world success: ~40% for 2-hour tasks at typical messiness levels

**Implications:** Need verifiable checkpoints and gating mechanisms at each step to control error propagation.

### User Stories as Units of Work

User Stories are proposed as a foundational unit because they:
- Provide **legible business value** at each checkpoint
- Are **robust to messy, dynamic environments** (unlike technical tasks)
- Center **user outcomes** that all stakeholders can understand
- Are small enough to **one-shot** with proper context

**Contrast with "planning modes":**
- AI agent planning tools keep agents on rails but provide mostly technical value
- User stories provide business-legible outcomes
- Both are complementary: plan within the scope of a well-defined story

### What User Stories Need

Plain Agile-canon user stories are not sufficient. They need "something more":
- Context gathering heuristics
- Nudges to collect the right information
- Integration guidance for the specific codebase

**The goal:** Units of work that help AI build useful software effortlessly, less like a slot machine.

### Practical Workflow

1. **Break down** project into user story-sized chunks with clear business value
2. **Provide context** specific to each story (relevant code, docs, patterns)
3. **Verify** at each checkpoint before proceeding
4. **Iterate** - let AI plan within the story scope

**Connection to other practices:**
- Reinforces Karpathy's "tight leash" / "small chunks of a single concrete thing"
- Enables the "surgeon" model's secondary task delegation
- Integrates with test-first approaches (tests verify story completion)

---

## Claude Code Subagents for Parallelization

*Source: https://zachwills.net/how-to-use-claude-code-subagents-to-parallelize-development/ - Added: 2026-01-18*

Using Claude Code's subagent/Task capability to parallelize development work, transforming linear workflows into concurrent execution.

### Core Principles

**1. Parallel Execution for Speed**

Break tasks into constituent parts with specialist agents assigned to each:

| Agent Role | Task |
|------------|------|
| backend-specialist | Write API endpoints |
| frontend-specialist | Build UI components |
| qa-specialist | Generate test suites |
| docs-specialist | Draft documentation |

All work simultaneously, completing in the time of the longest single task.

**2. Sequential Pipelines (Automated Assembly Line)**

For dependent workflows, agents pass outputs forward:

1. **product-manager** + **ux-designer** → produce ticket specification
2. **senior-software-engineer** → implements from ticket
3. **code-reviewer** → reviews and provides structured feedback
4. Loop: Orchestrator feeds feedback back to engineer until reviewer approves

**3. Context Isolation for Quality**

Each subagent gets its own 200k context window, preventing quality degradation:

- Product manager uses full context for user needs and business logic
- UX designer uses full context for design patterns and user flows
- Engineer uses fresh context for implementation, receiving only the ticket

**No single agent has to sacrifice specialized knowledge to stay within limits.**

### Implementation with Claude Code

```bash
# Define agents in ~/.claude/agents/ or ./.claude/agents/
# Example: product-manager.md, senior-software-engineer.md, code-reviewer.md
```

**Custom commands** in `.claude/commands/` can orchestrate multi-agent workflows:
- `/generate-ticket` - Spins up PM, UX, and engineer agents in parallel
- `/implement-ticket` - Chains engineer → reviewer with feedback loop

### Example: Ticket Generation

Single command spawns three specialists in parallel:
1. **product-manager**: Defines user needs, acceptance criteria
2. **ux-designer**: Analyzes existing patterns, proposes UI
3. **senior-software-engineer**: Provides technical constraints

Result: Fully-formed ticket in minutes, not hours.

### Structured Code Review Output

Code reviewer agent produces parseable output:

```
CODE REVIEW REPORT
📊 Summary:
  Verdict: NEEDS REVISION
  Blockers: 0
  High Priority Issues: 2
  Medium Priority Issues: 1

🚨 Blockers (Must Fix)
None.

⚠️ High Priority Issues
Issue: Handler mixes responsibilities (SRP violation)
Location: app/api/posts/[postId]/comments/route.ts:25-50
Suggestion: Extract validation to Zod schema, create service function...
```

Orchestrator parses this to manage the feedback loop automatically.

### Practical Applications

| Use Case | Approach |
|----------|----------|
| **Codebase documentation** | List all functions → subagent per file → assembler agent for README |
| **Large-scale refactoring** | grep for instances → subagent per file for replacement |
| **Incident response** | Subagent per service for log analysis → main agent synthesizes timeline |
| **User feedback synthesis** | Define themes → subagents process response chunks → summary agent |
| **Security audit** | Subagents scan CVEs, GitHub issues, code patterns → security brief |

### Trade-offs and Challenges

**Cost and Usage Limits:**
- Chaining agents increases token usage significantly
- Hits Claude Pro/Max usage caps faster
- Trade-off: dramatically increased output vs. higher usage

**Non-Determinism:**
- Changing one part (prompt, command, instructions) has ripple effects
- Debugging requires creative approaches
- Part of the craft

**The Synthesis Challenge:**
- The "reduce" step is often hardest
- **Mitigation:** Have each subagent save output to distinct files for audit trail

**Prompts as Fragile Dependencies:**
- Treat agent definitions like code
- Version control, test, monitor
- Model updates can cause behavioral drift

### Philosophy: Low-Cost Failure

> "If the agents get it wrong, I don't really care—I'll just fire off another run. The cost of failure is so low that optimizing for speed and taking more 'shots on goal' is the right call."

This enables:
- Running workflows in background across multiple terminals
- Moving to next task while agents work
- Accepting that not every run succeeds

### Connection to Other Patterns

- **Crystal**: Desktop app for parallel sessions with git worktree isolation
- **Surgeon model**: Subagents handle "secondary tasks" while human focuses on primary work
- **Unit of work**: Each subagent operates on well-scoped unit with appropriate context
- **Master-Clone philosophy**: Main agent spawns clones via Task() rather than rigid specialist hierarchy

---

## Writing Code Was Never The Bottleneck

*Source: https://ordep.dev/posts/writing-code-was-never-the-bottleneck - Added: 2026-01-18*

A counterpoint to the narrative that LLMs "finally cracked" the code-writing bottleneck. The real bottlenecks remain human-centric.

### The Persistent Bottlenecks

Writing lines of code was never the bottleneck. The actual bottlenecks were, and still are:

- **Code reviews** - require thought and shared understanding
- **Knowledge transfer** - mentoring and pairing
- **Testing and debugging** - verification takes judgment
- **Human coordination** - tickets, planning meetings, agile rituals

These processes require thought, shared understanding, and sound judgment—qualities that don't speed up just because code generation is faster.

### The Marginal Cost Trap

**Marketing claim**: The marginal cost of adding new software is approaching zero with LLMs.

**Reality**: The cost of understanding, testing, and trusting that code is higher than ever.

LLMs shift the workload—they don't remove it:

| Before LLMs | After LLMs |
|-------------|------------|
| Thinking → Coding | Coding → Trying to understand what AI wrote |
| Time spent writing | Time shifted to post-hoc understanding, review, integration |

### When Verification Becomes Harder

Code review pressure increases when:
- It's unclear whether the author fully understands what they submitted
- Generated code introduces unfamiliar patterns or breaks conventions
- Edge cases and unintended side effects aren't obvious

**Result**: Code is easier to produce but harder to verify. This doesn't necessarily make teams move faster overall.

### The "Copy-Paste Engineering" Amplification

Developers have long joked about copy-paste engineering. LLMs have amplified those habits to unprecedented velocity and scale.

### Understanding Remains The Hard Part

> "LLMs reduce the time it takes to produce code, but they haven't changed the amount of effort required to reason about behavior, identify subtle bugs, or ensure long-term maintainability."

Review and understanding work can be *harder* when reviewers struggle to distinguish between generated and handwritten code, or understand why a particular solution was chosen.

### The Collaborative Nature of Software

Software engineering depends on:
- Shared understanding
- Alignment
- Mentoring

When code is generated faster than it can be discussed or reviewed, teams risk falling into a mode where quality is assumed rather than ensured. This creates stress on reviewers and mentors.

### The Unchanged Bottleneck

Yes, the cost of writing code has dropped. But the cost of **making sense of it together as a team** hasn't.

That's still the bottleneck.

### Connection to Other Patterns

This analysis reinforces several themes in this file:

- **The AI Coding Trap**: Same insight that time shifts to post-hoc understanding
- **Karpathy's nanochat experience**: Understanding custom code remains hard for AI
- **Vibe Engineering**: Code review becomes even more important with faster generation
- **Unit of Work Management**: Breaking into right-sized units helps manage the verification burden
- **Communication Bottleneck** (from New Calculus): At 10x velocity, coordination becomes the limiting factor

---

## Claude Code Framework Wars: A Taxonomy

*Source: https://shmck.substack.com/p/claude-code-framework-wars (Shawn) - Added: 2026-01-18*

A survey of emerging Claude Code frameworks across the open-source community. The key insight: Claude Code doesn't require code to become a framework—just structured prompts.

### The Eight Design Decisions

When designing a Claude Code workflow, there are eight key architectural choices:

| Decision | Question | Options |
|----------|----------|---------|
| **1. Where Tasks Live** | Claude's source of truth | Markdown backlogs, structured specs, GitHub Issues/Jira |
| **2. How Claude Is Guided** | Replacing ambiguous prompts with structure | Command libraries, coding standards, definition of done, validation hooks |
| **3. How Agents Coordinate** | Multiple Claudes need roles and plans | Role simulation, swarm parallelism, repo-native artifacts |
| **4. How Sessions Are Run** | Managing AI output and isolation | Terminal orchestration, parallel git worktrees, isolated containers |
| **5. How Claude Accesses Tools** | Stack knowledge and integrations | MCP integrations, custom tool libraries, database accessors, test hooks |
| **6. How Code Is Developed** | Different hats for different stages | PM, Architect, Implementer, Tester, Reviewer roles |
| **7. How Code Is Delivered** | Scale of output | Small diffs, feature flags/experiments, full app scaffolds |
| **8. How Context Is Preserved** | Fighting Claude's forgetfulness | Docs/journals, persistent memory, project health checks |

### Decision Details

**1. Where Tasks Live**
- Markdown backlogs: Tasks as todo lists in markdown
- Structured text: Product specs converted to tasks
- Issues/tickets: GitHub Issues or Jira, tied to code reviews

**2. How Claude Is Guided**
- Slash commands: Prebuilt commands like `/create-tasks`, `/review`
- Coding standards: Tech stack and guidelines documentation
- Definition of Done: Encoded completion criteria
- Validation hooks: Lint and test enforcement on every change
- Claude as reviewer: AI fills both developer and reviewer roles

**3. How Agents Coordinate**
- Role simulation: AI as PM, architect, developer, tester
- Swarm parallelism: Structured flow (spec → pseudocode → code → tests)
- Repo artifacts: Tasks, logs, and ADRs in codebase for persistence

**4. How Sessions Are Run**
- Terminal orchestration: Claude controls commands, panes, logs
- Parallel worktrees: Multiple branches via Git worktrees
- Parallel containers: Isolated containers prevent collisions

**5. How Claude Accesses Tools**
- MCP servers: Connect to browsers, databases, test runners, UI automation
- Custom tool libraries: Built-in shell scripts and commands
- Database accessors: Strong database access tooling
- Test hooks: Run tests before declaring work done

**6. How Code Is Developed**
- PM: Turns specs into tasks and backlogs
- Architect: Designs structure, defines interfaces, sets conventions
- Implementer: Writes code within guardrails
- Tester: Runs unit tests or UI checks via MCP
- Reviewer: Audits PRs for quality, readability, risk

**7. How Code Is Delivered**
- Small diffs: AI produces small PRs, always reviewed
- Experiments: Deploy behind feature flags
- Full scaffolds: Build and deploy entire apps from prompts

**8. How Context Is Preserved**
- Docs and journals: CLAUDE.md, architecture notes, project journals
- Persistent memory: Recap recent work, store decisions
- Health checks: Regular project checkups

### Framework Menu (Pick Your Stack)

| Setup Type | Components |
|------------|------------|
| **Beginner** | Markdown backlog + ticket diffs |
| **Structured Team** | Product specs + standards + role simulation |
| **Experiment-Heavy** | Repo artifacts + parallel sessions |
| **Prototype Mode** | App builder + docs scaffolding |

### Key Insight

> "AI works best when you give it structure. Claude isn't replacing developers—it's shifting their roles."

The frameworks are converging on a future where AI is not a magic box but a set of teammates you manage. The more structure you give, the more you get back.

### Connection to Other Frameworks

This taxonomy maps to existing patterns:
- **Task location** → Unit of work management
- **Agent coordination** → Subagent parallelization
- **Session management** → Crystal's git worktree approach
- **Context preservation** → CLAUDE.md best practices
- **Role simulation** → Surgeon model (delegating secondary tasks)

---

## Programming with Agents (David Crawshaw)

*Source: https://crawshaw.io/blog/programming-with-agents (David Crawshaw, Tailscale co-founder) - Added: 2026-01-18*

A practitioner's guide to using agents effectively, from someone building sketch.dev.

### The 9-Line Definition of Agent

For engineers, an agent is simply **a for loop containing an LLM call** where the LLM can execute commands and see their output without a human in the loop.

```
User → LLM → tool call → tool result → (repeat) → Response
```

That's it. The simplicity is deceptive - this loop transforms LLM utility dramatically.

### Why Agents Matter: The Whiteboard Analogy

**Agentless LLM = whiteboard coding interview**

Without feedback:
- Must remember API specifications from memory
- Must remember language grammar perfectly
- No compiler to catch mistakes
- No ability to test or iterate

**Agent = real development environment**

With feedback:
- Compiler surfaces syntax errors and hallucinated interfaces
- Web search finds documentation and APIs
- Tests reveal bugs in generated code
- Can navigate large codebases selectively

### Core Agent Tools

Surprisingly small set needed:
- `bash(cmd)` - for file system, git, curl, etc.
- `patch(hunks)` - for code changes
- `todo(tasks)` - for task tracking
- `web_nav(url)`, `web_eval(script)`, `web_screenshot()` - for browser interaction
- `keyword_search(keywords)` - for codebase navigation
- `codereview()` - for self-review

**Key insight:** Agents navigate codebases like pre-IDE programmers - `find`, `cat`, `grep -R`. The bash tool enables most functionality.

### The Time Trade-off

**Downside:** A single sentence request can generate tens of thousands of intermediate tokens, several minutes, and many test runs.

**Upside:** Mechanizing labor means getting further into the list of programs you wish you could write.

**Cost trajectory:** The author notes his last significant agent commit cost $1.15 in API credits - expensive today, but GPU improvements will rapidly reduce this. "The fact that we still call LLM chips 'graphics' chips shows the economic machine has a lot of restructuring to do."

### Practical Example: GitHub App Auth

Using sketch.dev to implement GitHub App auth:
1. Agent did the whole first pass with 3-4 pieces of feedback
2. Requested a specific constraint (avoid per-user tokens)
3. Agent implemented it

**But then the real work:**

1. **Security vulnerability** - Anyone who authorized the app could access any repository authorized with the app. Disaster, but obvious enough to catch quickly.
   - One sentence explanation → agent fixed it correctly

2. **Performance problem** - Code listed all app installations, then for each repo checked if user is collaborator. O(users × repos) API calls.
   - Root cause: Original naive constraint (no per-user tokens) was wrong
   - Solution: Told agent to remove the constraint, store per-user tokens
   - Agent quickly found efficient API calls

**Key insight:** "Telling this story took more words than I typed in total into Sketch to generate the GitHub auth code."

### Helping Agents with Conventions: SQL JSON Pattern

Tailscale's unconventional SQL pattern (from Brad and Maisem):

```sql
CREATE TABLE IF NOT EXISTS Cookie (
  Cookie   TEXT    NOT NULL AS (Data->>'cookie')  STORED UNIQUE, -- PK
  UserID   INTEGER NOT NULL AS (Data->>'user_id') STORED REFERENCES User (UserID),
  Created  INTEGER NOT NULL AS (unixepoch(Data->>'created')) STORED,
  LastUsed INTEGER AS (unixepoch(Data->>'last_used')) CHECK (LastUsed>0),
  Data     JSONB   NOT NULL
);
```

**The pattern:** Every table has one real column (Data JSONB), all others generated from it.

**Agent problem:** When creating tables, sometimes followed the pattern, sometimes didn't. Got more confused when exceptions were added.

**Fix:** Three sentences at the top of the SQL schema file:
> "Each table has a single concrete Data JSON column, all other columns are generated from it"

Plus comments on tables that break the pattern explaining they're exceptions.

**Counter-intuitive insight:** Engineers heavily discount comments. LLMs seem to give them more weight. Comments that humans skip past may be the key to agent behavior.

### Asset vs Debt Models of Code

**Common argument against agents:** Writing code is only a small fraction of overall cost; maintenance dominates.

**Crawshaw's counter:**
1. This is true for some projects (heavily used, long-lived products)
2. But most programs have few users, or are short-lived, or both
3. Don't extrapolate from "maintaining large existing products" to all engineering

**Most importantly:** Agents aren't just code generation - they read and edit code. "Agents are as happy removing code as adding it."

### Why Agents Work Now (2025)

Despite feedback being "obvious," useful agents only emerged recently. The reason: **model training**.

- LLMs of 2023 could not drive agents reliably
- LLMs of 2025 are optimized for tool calling
- Open models trail frontier models in tool-calling evals (as of writing)
- Expected to change in ~6 months

### What's Next: Containerized Development

**Current limits:**
1. **Safety** - Agents need safeguards. Running on real machines with production credentials is dangerous. Babysitting tool calls is tedious.
2. **Serialization** - Agents take minutes per turn. Running one at a time wastes human time.

**sketch.dev's solution:** Containers

- Each agent runs in a container with a copy of source code
- Git commits can be extracted
- Run many simultaneously
- Production credentials isolated

**Practical example:** While working on auth, opened a second Sketch instance, pasted a screenshot of an ugly form, wrote "this is ugly, please make it less ugly." Came back 30 minutes later, it had improved the form. Asked it to rebase, it resolved the merge conflict, pushed.

> "One of the great things about talking to an agent is if you only have a tiny bit of mental energy left you have a good chance of getting something of value out of 30 seconds work."

### What Does the IDE Become?

Open questions being explored:
1. **Editable diff view** - Type in the right-hand side of diffs directly
2. **SSH access to containers** - Shell in, or open in VSCode via `vscode://` URL
3. **Code review-style comments** - Comment on diff lines, send back to agent as feedback

> "We are convinced that containers can be useful and warranted for programming. The idea has been around for a long time but I have never personally wanted to start programming in a container. But cleaning up a diff that an agent wrote for me in a container is far more interesting."

### The Humility Lesson

> "Every fundamental assumption about how I work has to be questioned, and it ripples through all the experience I have accumulated. There are days when it feels like I would be better off if I did not know anything about programming and started from scratch."

**Changed norms:**
- Code review process needs reinvention
- The IDE concept needs to be torn up and repurposed
- Team interactions will change

**Advice:** Curiosity and humility. Turn away from internet forums where people talk in circles about this technology. "That is a job for an agent."

---

## Additional Practitioner Notes

### GitHub Copilot Parallel Agents (Igor Šarčević)

*Source: https://morningcoffee.io/parallel-ai-agents-are-a-game-changer.html - Added: 2026-01-18*

Practitioner experience running 10-20 parallel PRs using GitHub Copilot agents.

**Workflow pattern:**
1. Prepare issues with sufficient context (behavior, file locations, requirements)
2. Assign agents in batches (@copilot on issues)
3. Review locally - each agent takes 5-20 minutes
4. Maintain flow between reviews - don't wait for one to finish

**Observed success rates:**
- 10%: Perfect one-shot, ready to ship
- 20%: Almost there, 10 min local refinement
- 40%: Needs manual intervention
- 20%: Completely wrong (close and document learnings)
- 10%: Bad product idea

**Key insight:** Even 10% perfect solutions are valuable because agents reliably handle initial setup—finding files, writing boilerplate, adding tests. By review time, groundwork is done.

**What works well:** Bug fixes, race conditions, backend logic, database changes, package bumps, well-defined tasks.

**What struggles:** New UI (need real-time visual feedback), undocumented additions to existing PRs, complex architectural decisions.

**Engineering enablers:**
- Fast CI/CD pipeline for quick validation
- System documentation (APIs, conventions, boundaries)
- Preview/staging environments
- Monorepo architecture (context stays unified)

---

## Developer Evolution: From Skeptic to Strategist

*Source: Peter Steinberger's Essential Reading (https://steipete.me/posts/2025/essential-reading-august-2025) citing Thomas Dohmke's research - Added: 2026-01-18*

Research from interviews with developers who've made AI tools central to their workflows reveals a four-stage evolution.

### The Four Stages

| Stage | Mindset | Activities |
|-------|---------|------------|
| **AI Skeptic** | Doubtful, experimental | Dabbling with code completions |
| **AI Curious** | Open, learning | Trying copilots and assistants |
| **AI Practitioner** | Integrated, productive | Regular AI-assisted workflows |
| **AI Strategist** | Orchestrating, leading | Multi-agent workflows, planning + coding models |

### Role Transformation

Advanced practitioners describe their work shifting from "writing code to architecting and verifying implementation work carried out by AI agents."

**Two core activities:**
1. **Delegation** - Context engineering, prompt design
2. **Verification** - Validating AI output against objectives

### Timeline Predictions

- Half expect 90% AI-written code within 2 years
- Half expect it within 5 years
- Crucially viewed as role reinvention, not replacement

> "Maybe we become less code producers and more code enablers. My next title might be Creative Director of Code"

### Skills Evolution

**New emphasis:**
- AI fluency
- Agent orchestration
- Human-AI collaboration
- Product understanding

**Still essential:** Foundational programming knowledge for verification and quality control.

### Key Mindset

"Realistic optimists" focus less on "time saved" and more on "increasing ambition" - expanding the scope and complexity of what they can accomplish rather than just working faster.

---

## The Hidden Cost of AI-Assisted Learning

*Source: Peter Steinberger's Essential Reading citing Namanyay Goel - Added: 2026-01-18*

A sobering counterpoint: AI tools may be creating developers who can ship code without truly understanding it.

### The Learning Crisis

Junior developers increasingly rely on AI-generated solutions without understanding underlying principles. This creates a knowledge gap that compounds over time.

### Pattern Matching vs Understanding

AI tools excel at providing working code snippets, but developers miss the crucial "struggle phase" where deep understanding forms.

**The difference:**
- Knowing how to use a solution
- Understanding *why* it works

### The Generational Divide

| Developer Type | Foundation | Risk |
|---------------|------------|------|
| Pre-AI learners | Strong fundamentals | Can verify AI output |
| AI-native learners | Potentially shallow | May not recognize subtle errors |

### Long-Term Implications

> "We're going to pay for this later" when complex debugging or architectural decisions require fundamental understanding.

### Balanced Approach

- Interrogate AI solutions - don't just accept them
- Build from scratch periodically
- Engage in meaningful code reviews ("why does it work this way?" not just "does it work?")

---

## Reality Check: AI Productivity Claims

*Source: Peter Steinberger's Essential Reading citing Colton Anglin - Added: 2026-01-18*

A much-needed reality check on hyperbolic 10x/100x productivity claims.

### The Math Doesn't Add Up

Claims of 10x productivity ignore that most engineering time isn't spent typing code:
- Thinking
- Debugging
- Reviewing
- Coordinating with teams

**AI doesn't fundamentally accelerate these activities.**

### Real Productivity Gains

AI excels at specific tasks:
- Writing one-off scripts
- Generating boilerplate
- Handling repetitive patterns

**Realistic improvement:** ~20-30% in specific contexts, not 10x overall.

### The Correction Overhead

AI-generated code often requires significant manual review and fixing, sometimes taking longer than writing from scratch.

> "A competent engineer will figure this stuff out in less than a week of moderate AI usage"

### Psychological Impact

The constant barrage of "10x engineer" claims creates unnecessary anxiety and imposter syndrome. Reality: experienced engineers quickly discover AI's actual limitations through hands-on use.

### The Balanced View

AI tools are valuable additions to our toolkit, but core skills remain fundamentally human:
- Understanding problems
- Designing solutions
- Building maintainable systems

---

## The End of Platform Dominance (Speculation)

*Source: Peter Steinberger's Essential Reading citing Austin Parker - Added: 2026-01-18*

A visionary thesis: AI will restructure software from platform monopolies to custom applications on open protocols.

### Time Economics Revolution

Platforms rose to dominance when developer time was expensive.

> "AI makes time very, very, very cheap" - fundamentally altering the economic equation.

### Custom Over Commodity

With AI reducing development time from months to minutes:

> "Custom applications will become the norm, not the exception"

Why use generic tools when bespoke solutions cost virtually nothing to create?

### The Scale Paradox

> "Why do I need planet-scale infrastructure to share baby photos with, like, 5 people?"

AI enables right-sized solutions instead of one-size-fits-all platforms.

### Hardware Convergence

Within 5 years: consumer devices with onboard AI rivaling today's best models, enabling truly personal computing where applications are generated on-demand.

---

## MCP's Fundamental Limitations (Armin Ronacher)

*Source: https://lucumr.pocoo.org/2025/7/3/tools/ - Added: 2026-01-18*

A foundational critique of MCP (Model Context Protocol) and the argument that code generation is fundamentally superior to tool-based inference for automation.

### The Two Major Flaws of MCP

1. **Not truly composable** - Most composition happens through inference, not deterministically
2. **Too much context demand** - Significant upfront input required, and every tool invocation consumes more context than simply writing and running code

**Quick test:** Complete any GitHub task using the GitHub MCP, then repeat with the `gh` CLI. The CLI almost always uses context more efficiently and reaches results faster.

### The "MCP is the Future" Counterargument

Common feedback: MCP might not make sense for code generation (models are good at that), but works for domain-specific end-user tasks in specialized environments.

**Ronacher's response:** Even for non-programming, domain-specific tasks, code generation is the better choice because of composability. Current MCP approaches rely too heavily on inference, which doesn't scale.

### Why Automation Needs Code

**The core insight:** "Replace yourself with a shell script" has been happening for a long time. With LLMs, the goal is replacing yourself with an LLM instead—but you hit three problems:
- Cost
- Speed
- Reliability

These must be solved before tool usage or MCP even matters. We need to ensure automated tasks work correctly at scale.

### The Key to Automation: Repetition

You don't automate one-shot changes. You automate things that happen over and over.

**For repetitive tasks, code wins because:**
- Validation is harder with inference ("did the LLM calculate correctly?")
- Code can be reviewed at the formula level, not the calculation level
- Python calculating correctly can be trusted; LLM inference cannot

### The Blog Conversion Example

Ronacher converted his entire blog from reStructuredText to Markdown. He worried about:
- Context exhaustion causing hallucinated text
- Subtle wording changes
- Regressions that would be hard to catch

**The solution:** Ask the LLM to do the transformation through code, not inference.

1. Take document, analyze structure, write Python conversion code
2. Run conversion, compare input to output
3. Write a short summary describing differences
4. Iterate until differences are acceptable

**Why this worked:**
- Reviewable approach (verify the formula, not each calculation)
- Constant inference cost regardless of document count
- Mechanical process that couldn't corrupt text
- Spot-checkable with high confidence

### MCP Cannot Do This

**The Playwright example:**

Using Playwright MCP to browse your own app requires inference at every step—reading pages, finding buttons, clicking inputs in real-time.

**Alternative:** If you know the page structure (e.g., your own app), have the LLM write a Playwright Python script instead. This script performs all steps sequentially without inference.

**Benefits:**
- Significantly faster execution
- The LLM understands your code, produces correct results
- Once written, the script runs 100, 200, 300 times without additional inference
- Reusable automation that scales

### The Human Debugging Problem

> "I'm a human, not an MCP client. I can run and debug a script, I cannot even figure out how to reliably do MCP calls. It's always a gamble and incredibly hard to debug."

Scripts generated by Claude Code during development can become permanent additions to the workflow.

### What Comes Next?

**Open questions:**
- Better abstractions combining what MCP is great at with code generation
- Better sandboxes for agent code execution
- APIs exposing fan-out/fan-in patterns for inference
- Code generation that provides enough context for non-programmers to understand what scripts do

**The principle:** Do as much in generated code as possible, then use LLM inference to judge the results—not to perform the operations.

### Connection to Other Patterns

This is the foundational argument behind the "Code Over Tools" MCP design pattern (see section below). The key insight: inference-based MCP tools hit fundamental scaling limits that code generation sidesteps entirely.

---

## MCP Server Proliferation: Less Is More

*Source: Peter Steinberger's Essential Reading citing Geoffrey Huntley - Added: 2026-01-18*

Warning: the rush to add more MCP tools and integrations is degrading AI coding assistant performance.

### Context Window Economics

Every MCP server and tool consumes precious tokens from the LLM's limited context window:
- More tools = less space for actual code and reasoning
- Fundamental trade-off most developers don't realize

### The Allocation Paradox

> "Less is more. The more you allocate into the context window of an LLM… the worse the outcomes you're going to get"

Each additional tool:
- Increases cognitive overhead
- Reduces AI's ability to focus on the actual task

### Tool Proliferation Problems

Multiple similar tools create non-deterministic behavior:
- LLM struggles to choose between overlapping capabilities
- Leads to confusion and errors
- Not enhanced functionality

### Security Concerns

Third-party MCP servers introduce:
- Supply chain risks
- Potential attack vectors
- Context injection that manipulates AI behavior
- New class of vulnerabilities enterprises aren't prepared for

### Strategic Recommendations

1. **Limit MCP servers to essential tools**
2. **Prefer first-party integrations** from trusted vendors
3. **Consider dynamic enabling/disabling** based on workflow stages
4. **Don't load everything at once**

### Connection to Context Engineering

This reinforces the context engineering principle: context is a finite resource with diminishing returns. Be strategic about what consumes it.

---

## The AI Factory Model (John Rush)

*Source: https://john-rush.com/posts/ai-20250701.html - Added: 2026-01-18*

A practitioner workflow treating AI agents as a self-improving factory. The core insight: **fix inputs, not outputs**.

### The Factory Metaphor

Inspired by Factorio: build a factory of agents that can produce code, verify it, and improve themselves over time. The code itself is disposable; the instructions and agents are the real asset.

### Three-Step Workflow

**Step 1: Planning (o3)**
- Give high-level task to Claude Code
- Claude calls o3 via MCP to generate a plan
- o3 asks clarifying questions and writes `<task>-plan.md`
- Plan includes both original ask and implementation details

**Step 2: Execution (Sonnet 3.7/4)**
- Sonnet 4 reads plan, verifies it, turns into task list
- Claude Code executes with Sonnet 3.7 or 4 depending on complexity
- **Critical:** Commits after each task step for easy rollback
- Uses Sonnet 4 for Clojure "to get the parens right"

**Step 3: Verification → Feedback (Sonnet 4 + o3)**
- Sonnet 4 verifies code against original plan
- o3 verifies against original plan AND original ask
- **Key insight:** o3 is "uncompromising" - catches issues Claude lets slide:
  - Unnecessary backwards compatibility code
  - Lint ignore flags
  - Over-defensive patterns

**Feedback loop:** Any issues get baked into the plan template, not fixed inline.

### The Core Principle

> "When something goes wrong, I don't hand-patch the generated code. I don't argue with claude. Instead, I adjust the plan, the prompts, or the agent mix so the next run is correct by construction."

**Outputs are disposable; plans and prompts compound.**

### Example: Self-Improving Factory

Agent wrote code loading entire CSV into memory:
1. Made it switch to streaming
2. Had agent write instructions to plan template: "always use streaming for CSVs"
3. Plan checker now flags any code without streaming
4. Never need to remember this in PR reviews

**The factory improved itself.**

### Parallelization with Git Worktrees

- Multiple Claude Code windows, each on its own git-worktree
- Build multiple features simultaneously
- Still merge manually, but no longer babysitting single agent

### Scaling: Specialized MCP Agents

**Style enforcement agent:**
- Sweeps all generated Clojure code
- Applies local style rules consistently
- Handles style drift from lint/test/debug cycles

**Library replacement agent:**
- Looks at generated code
- Replaces patterns (e.g., `Thread/sleep`) with internal libraries (e.g., retry library)

**Composition pattern:**
- Take API doc + internally defined business cases
- Compose agents to build integrations, tests, and documentation
- Powerful for features without doing all work by hand

### The "Dozen Attempts" Strategy

> "It's essentially free to fire off a dozen attempts at a task - so I do."

- All agents run in parallel
- When one fails, stalls, or lacks context: feed lesson into next iteration
- Resist the urge to fix outputs; fix the inputs instead

### Current Limitations & Future Work

| Challenge | Current State |
|-----------|---------------|
| Agent coordination | Manual kickoff, want automated dependencies |
| Business doc alignment | Moving from low-level details to higher-level use cases |
| Complex workflows | Building out more agents and interactions |
| Token limits | Bedrock limits Sonnet 4; need seamless provider switching |

### Assessment

> "Good enough to ship code while I refill my coffee, not yet good enough to bump me off the payroll."

### Connection to Other Patterns

- **Git worktrees:** Same pattern as Crystal desktop app
- **Multi-model verification:** Uses model-specific strengths (o3 for strictness, Sonnet for execution)
- **Fix inputs not outputs:** Foundational principle matching Armin Ronacher's MCP critique
- **Specialized agents:** Similar to subagent parallelization patterns
- **Plan templates:** External memory pattern from context engineering

---

## Why Agents Are Bad Pair Programmers (Justin Searls)

*Source: https://justin.searls.co/posts/why-agents-are-bad-pair-programmers/ - Added: 2026-01-18*

A critique of real-time agentic pair programming, with practical alternatives for human-AI collaboration.

### The Core Problem

LLM agents code faster than humans think. The experience mirrors the worst human pair programming:

- Partner grabs keyboard, hammers out code in silence
- You can't keep up, slowly disengage
- When they hit a roadblock, you're lost
- You realize they've been building the wrong thing all along
- Now you have to fix it under deadline pressure

**The speed gap:** Agent speed creates the same disengagement and miscommunication as a runaway human pair.

### Two Alternatives to Agentic Pairing

**1. Async workflows (let them have it)**

Just like with human pairs who want to run with it:
- Break work into discrete sub-components
- Let the agent build independently
- Review as pull requests

**Tools:** GitHub Coding Agent, similar async-first workflows

**2. Throttle down to turn-based modes**

Continue editor-based pairing, but:
- Use "Edit" or "Ask" modes instead of "Agent" mode
- LLM proposes individual edits, you manually accept
- Go slower—that's the point

**Best practice:** Establish rigorously consistent workflow, not just reaching for AI to troubleshoot.

### Feature Requests for AI Tool Makers

To make agent pairing more like good human pairing:

| Feature | Why It Matters |
|---------|----------------|
| **Adjustable output speed** | Let users set lines/minute to match reading speed |
| **Pausable conversations** | Ask clarifying questions without derailing the session |
| **Work-mirroring UI** | Pin to GitHub issue, integrated to-do list, not just chat |
| **Built-in self-doubt** | Stop to validate "why are we building this?", solicit advice |
| **Voice chat mode** | Keep eyes on code, engage the speaking/listening brain |

### The Insight

> "Agentic pair programmers are not inherently bad, but their lightning-fast speed has the unintended consequence of undercutting any opportunity for collaborating with us mere mortals."

The fix isn't better agents—it's agents designed to expect more of us as equal partners.

### Connection to Other Patterns

This reinforces several themes:
- **Surgeon model:** Delegate secondary tasks async, stay engaged on primary work
- **Turn-based vs agent mode:** Matching Karpathy's "autocomplete sweet spot"
- **Review bottleneck:** Even fast agent code needs human comprehension and review
- **Unit of work management:** Breaking into reviewable chunks enables async collaboration

---

## The Case Against AI Skepticism (Thomas Ptacek, Fly.io)

*Source: https://fly.io/blog/youre-all-nuts/ - Added: 2026-01-18*

A provocation arguing that smart developers dismissing LLMs for coding are making unserious arguments.

### The Core Claim

> "All progress on LLMs could halt today, and LLMs would remain the 2nd most important thing to happen over the course of my career."

Important caveat: This is specifically about software development, not art, music, or writing.

### Level-Setting: What Agents Actually Are

**If you're not using agents, you're not doing what AI boosters are doing.**

Agents aren't ChatGPT in a browser. They:
- Poke around your codebase on their own
- Author files directly
- Run tools, compile code, run tests, iterate on results
- Pull in arbitrary code from the tree or online
- Run Unix tools to navigate and extract information
- Interact with Git
- Make arbitrary tool calls through MCP

**Key insight:** The code in an agent that "does stuff" is not AI—it's simple systems code wired to ground truth about programming. You could write an effective coding agent in a weekend. Its strength comes from how you structure builds, linting, and test harnesses.

### The Tedium Quadrant

LLMs handle tedious code. Most code on most projects is tedious. LLMs don't get tired; they're immune to inertia.

**The insight about inertia:** Think of anything you wanted to build but didn't because you weren't in the "limerent phase" of a new language. The bookkeeping, Googling, dependency drama of starting projects. An LLM can figure all that out and drop you at the golden moment where shit almost works.

**The yak-shaving insight:** Sometimes you refactor unit tests to avoid gnarly work. Now an agent can putz with your tests in a VM for hours and come back with a PR. You'll feel worse yak-shaving, so you'll do... real work.

### "But the Code Quality"

**Response: What the fuck is wrong with you?**

- You've always been responsible for what you merge to main
- Read the code. Spend 5-10 minutes knocking it back into your style
- LLM output isn't "probabilistic code"—it's code. It's knowable
- What matters is whether you can make sense of it and whether your guardrails hold
- Reading other people's code is part of the job—if you can't metabolize boring, repetitive LLM code, skills issue

### "But Hallucination"

**Response: If hallucination matters to you, your programming language has let you down.**

- Agents lint, compile, and run tests
- If the LLM invents a function signature, the agent sees the error
- It feeds back to the LLM, which says "oh right, I made that up" and tries again
- This is why you shouldn't watch the chain of thought log—tab away and let it work
- Hallucination is essentially a solved problem for coding agents

### "But the Code is Shitty, Like a Junior Developer"

**Response: Does an intern cost $20/month?**

Part of being a senior developer is making less-able coders productive, be they human or algebraic. Using agents well is a skill AND an engineering project of prompts, indices, and tooling.

### "But the Craft"

**Response: Do you like fine Japanese woodworking? Do it on your own time.**

- Professional developers solve practical problems for people with code
- We are not artisans in our day jobs
- Steve Jobs was wrong: nobody cares if the logic board traces are pleasingly routed
- If anything we build endures, it won't be because the codebase was beautiful

**The self-soothing insight:** Carefully golfing functions into graceful minimal expressions is yak-shaving. You're not building; you're self-soothing. LLMs devour schlep and clear a path to the important stuff.

### The Defense of Mediocrity

> "As a mid-late career coder, I've come to appreciate mediocrity. You should be so lucky as to have it flowing almost effortlessly from a tap."

- We all write mediocre code. Often it's fine.
- Not all code is equally important. Some code should be mediocre.
- Maximum effort on a random unit test? You're doing something wrong.

**Floor vs Ceiling:**
- Developers worry LLMs lower the "ceiling" for quality. Maybe.
- But they also raise the "floor."
- Gemini's floor is higher than the author's—LLM code is more thorough, even if repetitive.
- LLMs have a bigger bag of algorithmic tricks than you do: radix tries, topological sorts, LDPC codes.

### "But the Hype"

**Response: I don't give a shit.**

Things either work or they don't, no matter what Jensen Huang says.

### "But Job Displacement"

**Response: We're a field premised on automating other people's jobs away.**

- "Productivity gains" means fewer people doing the same stuff
- Talked to a travel agent lately? Or a floor broker? Or a record store clerk?
- LLMs might displace many software developers
- We're not East Coast dockworkers; we won't stop progress on our own

### "But Plagiarism / IP"

**Response: Shove this concern up your ass.**

No profession has demonstrated more contempt for intellectual property than software developers:
- Star Wars and Daft Punk treated as public commons
- Global-scale piracy networks
- Sneering at anyone who tries to preserve a new-release window

> "If you don't believe a typeface designer can stake a moral claim on the terminals and counters of a letterform, you sure as hell can't be possessive about a red-black tree."

### What's Actually Happening Now

**Asynchronous agents:**
- Wake up, free-associate 13 things for LLMs to work on
- Make coffee, fill out a TPS report, drive somewhere
- Check notifications—13 PRs to review
- Three get tossed and re-prompted, five get junior-dev feedback, five get merged

**Log analysis:** Fed 4o (not o4-mini) log transcripts during an incident—it spotted LVM metadata corruption issues in seconds that had been complained about for months.

### The Takeaway

> "Something real is happening. My smartest friends are blowing it off. Maybe I persuade you. Probably I don't. But we need to be done making space for bad arguments."

The cool kid haughtiness about "stochastic parrots" and "vibe coding" can't survive much more contact with reality. When smart skeptics get over this affectation, they'll make coding agents profoundly more effective.

### Connection to Other Patterns

- **Vibe Engineering (Willison):** Similar defense of serious AI-assisted work vs. dismissive "vibe coding" label
- **Hallucination as solved:** Reinforces the agent loop pattern (lint → compile → test → iterate)
- **Floor vs Ceiling:** Adds to the "mediocrity as feature" argument—LLMs raise the floor
- **Tedium/Yak-shaving:** The dopamine insight—agents get you to the fun part faster
- **Code as commodity:** Aligns with "writing code was never the bottleneck"

---

## MCP Design: Code Over Tools (Armin Ronacher)

*Source: https://lucumr.pocoo.org/2025/8/18/code-mcps/ - Added: 2026-01-18*

A provocative argument: instead of building MCPs with dozens of specialized tools, expose a single "ubertool" that accepts programming code as input.

### The Problem with CLI Tools

CLI tools have several challenges when used by AI agents:

| Challenge | Example |
|-----------|---------|
| **Platform/version dependence** | Different behaviors across systems |
| **Character encoding** | Agents struggle with non-ASCII, newlines, control characters in shell args |
| **Unknown syntax** | Novel tools not in training data cause confusion |
| **Security preflight** | Claude Code runs Haiku check before shell commands, adding latency |
| **Stateful sessions** | Agents lose track of tmux sessions, rename them mid-task, forget they exist |

### Why Composability Matters

The shell works because of composability through bash:
- `tmux send-keys` + `sleep` + `tmux capture-pane` chains together
- Agents can compose larger scripts from one-liners
- They can even use `base64 -d` to work around encoding issues

**The key insight:** The command line isn't one tool—it's a programming language (bash) that composes many tools.

### The Ubertool Pattern

Instead of exposing many MCP tools, expose **one tool that accepts code**:

```python
# The MCP exposes a single tool: pexpect_tool
# But it's really a Python interpreter with retained state
# that happens to have pexpect installed
```

**Why this works:**
1. The meta input language (Python/JavaScript) is well-known to the model
2. The SDK (pexpect, playwright) has stable APIs with extensive training examples
3. MCP handles session management automatically
4. Code written is close to what would go in a reusable script

### Example: pexpect-mcp

Instead of 36+ individual pexpect methods as tools, one Python eval tool:

```python
# Tool description says this:
"""
Execute Python code in a pexpect session. Use 'child' variable to interact.
Example:
  child = pexpect.spawn('lldb ./mytool')
  child.expect("(lldb)")
"""
```

Basic usage requires three chained operations anyway:
```python
child = pexpect.spawn('scp foo user@example.com:.')
child.expect('Password:')
child.sendline(mypassword)
```

**This is now one tool call, not three.**

### The Reusability Payoff

Because the MCP accepts Python code:
1. Run an interactive debug session through pexpect_tool (~45 seconds, 7 tool calls)
2. Ask Claude to dump the session into a reusable Python script
3. Re-run the same debugging with `uv run debug_demo.py` (~5 seconds, 1 tool call)
4. **The script works without the MCP** - any human can run it

### Handling Novel APIs

For completely unknown APIs:
- The programming language is still known (Python/JavaScript)
- Agents know `dir()`, `globals()`, `repr()`, `sys._getframe()`
- They can explore the MCP's state programmatically
- Prompt can include "run this function to learn what's available"

### playwrightess: Taking It Further

Same concept applied to Playwright:
- Instead of ~30 tool definitions, one JavaScript eval tool
- `console.log` from browser and script auto-forwarded to agent
- State variable for accumulating data across calls
- Loops happen in JavaScript, not inference

**Result:** Pagination across multiple pages requires no additional inference—the loop runs within JavaScript.

### Security Acknowledgment

> "The elephant in the room for all things agentic coding is security... But does it matter? We are seemingly okay with it writing code and running tests."

The tail risks of code execution are already present. An MCP running Python code isn't dramatically worse when pexpect itself can run any bash command.

**Open question:** How to protect systems that are "inherently unsafe and impossible to secure"?

### Connection to "Less Is More"

This is the architectural solution to MCP tool proliferation:
- **30 tools** = context rot, cognitive overhead, non-deterministic tool choice
- **1 code tool** = model uses familiar language, composes naturally, produces reusable artifacts

The insight flips the MCP design question: instead of "what tools should my MCP expose?", ask "what programming environment should my MCP provide?"

---

## AlphaCodium: Flow Engineering for Code Generation

*Source: https://arxiv.org/abs/2401.08500 (Tal Ridnik et al., CodiumAI) - Added: 2026-01-18*

A foundational paper introducing "flow engineering" as the next evolution beyond prompt engineering for code generation tasks.

### The Core Insight

Code generation differs fundamentally from natural language tasks:
- Must match exact syntax of target language
- Must identify happy paths AND edge cases
- Must adhere to specific problem requirements
- Must handle code-specific issues (imports, types, etc.)

**Key claim:** Many optimizations successful for NL generation don't apply to code tasks.

### AlphaCodium: Test-Based Iterative Flow

AlphaCodium is a multi-stage, code-oriented iterative flow that uses tests as feedback:

| Phase | Description |
|-------|-------------|
| **Pre-processing** | Problem reflection, public tests reasoning, AI-generated tests |
| **Iteration** | Generate initial solution → run on tests → iterate on failures |

### Results

On CodeContests (competitive programming from Codeforces):

| Approach | GPT-4 Accuracy (pass@5) |
|----------|------------------------|
| Single well-designed prompt | 19% |
| AlphaCodium flow | 44% |

**2.3x improvement** from flow engineering vs. prompt engineering.

### Flow Engineering vs Prompt Engineering

**Prompt engineering:** Crafting a single optimal prompt for one-shot generation.

**Flow engineering:** Designing multi-stage processes where:
- Each stage has a focused objective
- Tests provide ground truth feedback
- Iteration happens within the system, not requiring human intervention

### Key Principles (Broadly Applicable)

1. **Test-first iteration** - Use tests as oracle, iterate until passing
2. **Multi-stage decomposition** - Break complex problems into focused phases
3. **Code-specific reasoning** - Pre-process to understand edge cases before generating
4. **AI-generated tests** - Expand test coverage beyond provided examples

### Connection to Other Patterns

This paper predates (Jan 2024) but anticipates many patterns in this file:
- **Agent loops** (Crawshaw): AlphaCodium's iteration is an early form of the compile → test → iterate loop
- **Context engineering**: Pre-processing phases curate relevant context for code generation
- **Unit of work management**: Each stage operates on right-sized context
- **Test-first development**: Vibe engineering's emphasis on automated tests for agent iteration

The term "flow engineering" is essentially what we now call agentic coding workflows with tool-use feedback loops.

---

## Three Modes of Vibe-Coding (Diwank Singh, Julep)

*Source: https://diwank.space/field-notes-from-shipping-real-code-with-claude - Added: 2026-01-18*

A practical framework for AI-assisted development based on production experience at Julep (complex AI workflow orchestration platform).

### Mode 1: Playground

**When to use:** Weekend hacks, personal scripts, proof-of-concepts, "I wonder if..." moments.

**Characteristics:**
- Zero ceremony, no extensive documentation
- Claude writes 80-90% of the code
- Just enough steering to keep things on track
- Fast: idea to working prototype in minutes

**Rule:** Great for experiments, never for production.

### Mode 2: Pair Programming

**When to use:** Projects under ~5,000 lines, side projects with real users, well-scoped small services.

**Characteristics:**
- Structure needed, but not so much it slows you down
- CLAUDE.md file provides context Claude reads automatically
- Anchor comments provide inline guidance
- Active collaboration—bouncing ideas back and forth

**Key innovation:** CLAUDE.md transforms effectiveness. Instead of repeatedly explaining conventions, document once.

### Mode 3: Production/Monorepo Scale

**When to use:** Large codebases, systems with real users, anything where bugs cost money or reputation.

**Characteristics:**
- You become an editor-in-chief managing a newsroom
- Claude generates code, but integration requires careful orchestration
- Boundaries become critical at every integration point
- Significant effort needed to help AI navigate safely

**Caveat:** Vibe coding at this scale doesn't scale well yet. Better to section into individual services and sub-modules when possible.

### The Anchor Comment System

Anchor comments are inline breadcrumbs that prevent AI from wandering. Use `AIDEV-NOTE:`, `AIDEV-TODO:`, or `AIDEV-QUESTION:` prefixes.

**Guidelines:**
- Keep concise (≤120 chars)
- Before scanning files, always first locate existing `AIDEV-*` anchors in relevant subdirectories
- Update relevant anchors when modifying associated code
- Do not remove `AIDEV-NOTE`s without explicit human instruction
- Add anchors when code is too long, too complex, very important, confusing, or could have an unrelated bug

**Examples:**
```python
# AIDEV-NOTE: Critical performance path - this serves 100k req/sec
# We pre-compute these values in a background job (see workers/feed_prep.py)
# DO NOT add database queries here

# AIDEV-TODO: Implement pagination (ticket: FEED-123)
# Current implementation returns all items (max 1000)

# AIDEV-QUESTION: Why do we filter private items here instead of in cache?
# Historical context: Privacy rules can change between cache updates
```

**Dual purpose:** Comments serve both AI navigation and human documentation.

### The Sacred Rule: Humans Write Tests

**Never let AI write your tests.**

Tests are not just verification code—they encode human intentions, edge cases, and understanding of the problem domain.

**Why AI-written tests fail:**

AI-generated tests check that "code does what the code does," not what it *should* do. Example from a rate limiter:

```python
# AI's test checks the happy path
def test_rate_limiter():
    limiter = RateLimiter(max_requests=3, window_seconds=60)
    assert limiter.is_allowed("user1") == True
    assert limiter.is_allowed("user1") == True
    assert limiter.is_allowed("user1") == True
    assert limiter.is_allowed("user1") == False  # Limit reached
```

**What AI missed:** The implementation has a memory leak—users who hit the API once and never return leave their data in memory forever.

**Rule:**
| What | AI CAN Do | AI MUST NOT Do |
|------|-----------|----------------|
| Implementation | Generate business logic | Touch test files |
| Test Planning | Suggest test scenarios | Write test code |
| Debugging | Analyze test failures | Modify test expectations |

If an AI tool touches a test file, the PR gets rejected. No exceptions.

### Things Claude Should Never Touch

**❌ Test Files** - Tests encode human understanding

**❌ Database Migrations** - One wrong move = data loss. Migrations require understanding of data patterns, deployment timing, and rollback strategies.

**❌ Security-Critical Code** - Every line needs security review. AI suggestions are actively dangerous here.

**❌ API Contracts Without Versioning** - Breaking this = breaking every client. AI doesn't understand mobile app release cycles.

**❌ Configuration and Secrets** - Never hardcode. Feature flags require product decisions.

### Token Economics

**Front-load context to avoid iteration cycles.**

**Starved prompt:** "Add caching to the user endpoint"
- Result: In-memory cache (won't work with multiple servers), no invalidation, no metrics, no stampede protection
- Outcome: 3 more rounds of fixes, 4x the tokens spent

**Context-rich prompt:**
```
Add Redis caching to the GET /users/{id} endpoint.

Context:
- This endpoint serves 50k requests/minute
- We run 12 API servers behind a load balancer
- User data changes infrequently (few times per day)
- We already have Redis at cache.redis.internal:6379
- Use our standard cache key pattern: "user:v1:{id}"
- Include cache hit/miss metrics (we use Prometheus)
- Implement cache-aside pattern with 1 hour TTL
- Handle cache stampede with probabilistic early expiration

See our caching guide: docs/patterns/caching.md
```

**Rule:** One task, one session. When task is done, start fresh.

### Git Workflow for AI Development

**Git worktrees for isolation:**
```bash
# Create AI playground without polluting main
git worktree add ../ai-experiments/cool-feature -b ai/cool-feature

# Let Claude experiment in isolation
cd ../ai-experiments/cool-feature
# ... lots of experimental commits ...

# Cherry-pick the good stuff back to main
cd ../main-repo
git cherry-pick abc123

# Clean up
git worktree remove ../ai-experiments/cool-feature
```

**Tagging AI commits:**
```
feat: implement user feed caching [AI]

- Add Redis-based cache for user feeds
- Implement cache warming on user login
- Add metrics for cache hit rate

AI-assisted: core logic generated, tests human-written
```

Transparency helps reviewers—they know to pay extra attention to AI-generated code.

### Connection to Other Patterns

- **Surgeon model**: The three modes map to autonomy levels—Playground is high autonomy, Production is low
- **Unit of work management**: Mode 2 and 3 require right-sized units
- **Context engineering**: Anchor comments are external memory patterns
- **Code review bottleneck**: Acknowledges that AI speed creates review pressure

---

## VM0 Dev Workflow: Managing AI Agents Like a Team

*Source: https://blog.vm0.ai/en/posts/manage-agents-team (VM0 Team, AI Colleagues Co) - Added: 2026-01-19*

A production workflow treating multiple Claude Code instances as team members, using GitHub as shared memory and coordination infrastructure. Shipped 404 releases and 230,000+ lines of code over two months.

### The Core Insight

When coordinating many AI agents in parallel, **the bottleneck isn't whether the model can write code—it's human cognitive load**.

Without external tools, managing 8+ Claude Code sessions simultaneously becomes impossible. The solution: treat Claude the same way you treat human teammates, using GitHub as the natural collaboration tool.

### The Real Problem

**Adding more Claude sessions made things worse** when:
- Unable to track what each instance is doing
- Lost track of work state across sessions
- Couldn't remember what had already been decided
- No shared memory between sessions

This isn't an AI problem—it's a **management problem**.

### Three-Layer Workflow Architecture

The workflow consists of 14 slash commands organized into three layers:

| Layer | Purpose | Commands |
|-------|---------|----------|
| **Deep Dive** | Structured slow thinking before implementation | `/deep-research`, `/deep-innovate` |
| **Issue Management** | Tracking work and context | `/issue-create`, `/issue-todo`, `/issue-continue`, `/issue-compact` |
| **PR Management** | Code review and merging | `/pr-review-and-comment`, `/pr-check-and-merge` |

### The Deep Dive Flow: Enforcing Slow Thinking

Prevents Claude from jumping straight to code without understanding the problem space.

**Three phases with strict boundaries:**

1. **Research Phase** - Explore and analyze, no suggestions
   - `/deep-research` investigates the problem
   - Claude analyzes related files, patterns, architecture
   - No proposals yet—just understanding

2. **Innovate Phase** - Brainstorm approaches, no implementation details
   - `/deep-innovate` presents 3+ options with trade-offs
   - Human picks the approach
   - Still no code

3. **Plan Phase** - Detailed implementation plan, no coding
   - `/issue-create` creates GitHub Issue with approved approach
   - Plan includes what will be implemented
   - Checkpoint for human approval before execution

**Why constraints matter:** Without these boundaries, edge cases and architectural concerns get missed. The phases force deliberate reasoning instead of rushing to code.

### GitHub as Persistent Shared Memory

**The memory problem:** Most AI tools treat context as temporary. When session ends, memory disappears.

**VM0's solution:** GitHub Issues become persistent memory where:
- Original requirements documented
- Research findings captured
- Innovation phase options recorded
- The approved plan stored

**Human benefit:** When managing 8+ Claude instances and receiving "work complete" notifications, you can't reconstruct from chat what happened. GitHub Issues provide structured history:
- What was discovered (research)
- What options were considered (innovation)
- What will be implemented (plan)

This makes review efficient without needing to remember conversations.

### Handoff Between Agents

Because all context lives in GitHub, work moves seamlessly between agents:

```
Agent 1: /issue-create #123
Agent 2: /deep-research issue 123
Agent 3: /issue-todo 123
Agent 4: /deep-research PR 124
```

For long discussions, `/issue-compact` consolidates everything into clean issue body, making handoffs easy for both humans and AI.

### Workflow Patterns

**Simple tasks (clear requirements):**
```
/issue-create → /issue-todo → /issue-continue → /pr-check-and-merge
```

**Complex tasks (technical uncertainty):**
```
/deep-research → discussion →
/deep-innovate → discussion →
/issue-create → /issue-todo → /issue-continue →
/pr-review-and-comment → /pr-check-and-merge
```

**Parallel work (where workflow scales best):**
```
Agent 1: /issue-todo #123
Agent 2: /issue-todo #124
Agent 3: /pr-review-and-comment #100
Agent 4: /deep-research new feature requirements
```

Multiple agents work at once while human reviews completed checkpoints.

### The Command Reference

**Deep Dive Commands:**
- `/deep-research` - Investigate and analyze without proposing solutions
- `/deep-innovate` - Explore multiple approaches with trade-offs

**Issue Commands:**
- `/issue-create` - Create GitHub Issue from current discussion
- `/issue-todo` - Generate task list for an issue
- `/issue-continue` - Continue working on current task
- `/issue-compact` - Consolidate discussion into clean issue body

**PR Commands:**
- `/pr-review-and-comment` - Review code and add comments
- `/pr-check-and-merge` - Final checks and merge if approved

### Scaling Considerations

**Tested with 10+ concurrent Claude instances.**

**Recommendation:**
- **Up to 10 agents:** Comfortable for deep collaboration
- **Beyond 10:** Not recommended

**Limiting factor:** Human attention and decision quality at review checkpoints. Beyond 10 agents, you become the bottleneck and decision quality degrades.

**The "two pizza team" principle applies:** Same constraints limiting human team size also limit how many AI agents one person can effectively manage.

### Team Management Mindset

**Good team leaders know when to engage and when to step back:**
- Set clear requirements
- Review key decisions
- Verify final output
- But don't micromanage every detail

**Same principle with AI agents:** Don't micromanage each Claude instance. Set clear requirements, review at checkpoints, and verify output—but let them work autonomously between reviews.

### Adoption Path

**Incremental adoption recommended:**

1. **Week 1:** Start with basic issue flow
   - `/issue-create` → `/issue-todo` → `/issue-continue`
   - Get comfortable with one agent

2. **Week 2:** Add deep dive for complex tasks
   - Use `/deep-research` and `/deep-innovate` when requirements unclear

3. **Week 3+:** Scale gradually
   - Add more Claude instances as review rhythm becomes comfortable
   - Trust the process between checkpoints

Don't need all 14 commands from day one. Build muscle memory with basic patterns first.

### Key Success Factors

**What makes this work:**

1. **External memory (GitHub)** - Context persists beyond chat sessions
2. **Structured phases** - Deep dive prevents premature implementation
3. **Clear checkpoints** - Human reviews at defined stages
4. **Handoff capability** - Work moves between agents seamlessly
5. **Parallel execution** - Multiple agents work while human reviews
6. **Trust in autonomy** - Let agents work between checkpoints

**What doesn't scale:**
- Trying to hold context in your head across 8+ sessions
- Reviewing every intermediate step in real-time
- Treating each agent conversation as isolated/ephemeral

### Connection to Other Patterns

This workflow integrates several patterns from this file:

- **Crystal parallel sessions:** Same git worktree isolation pattern, but with GitHub Issues instead of desktop app UI
- **Surgeon model:** Human focuses on architecture/direction/quality while agents handle implementation
- **Unit of work management:** Issues represent right-sized units with clear business value
- **Context engineering:** GitHub Issues are external memory, CLAUDE.md provides coding standards
- **Subagent parallelization:** Multiple agents work simultaneously on different issues
- **Code review culture:** PR reviews are mandatory checkpoints before merge
- **Master-Clone philosophy:** Multiple Claude instances are peers, not rigid specialist hierarchy

### Why This Matters

The VM0 workflow demonstrates that **team management skills directly translate to AI agent coordination**:
- Clear requirements → better agent output
- Defined checkpoints → manageable review load
- Persistent memory → scalable across sessions
- Trust with verification → parallel execution

It's not about AI capabilities—it's about **human coordination of multiple AI workers**.
