---
type: link
source: notion
url: https://diwank.space/field-notes-from-shipping-real-code-with-claude
notion_type: Software Repo
tags: ['Running']
created: 2025-06-08T03:59:00.000Z
---

# Field Notes From Shipping Real Code With Claude - diwank's space

## Overview (from Notion)
- Embrace AI-assisted development as a tool to enhance productivity and creativity, allowing you to focus on high-level decision-making and strategy as a founder.
- Consider establishing a robust documentation culture (like CLAUDE.md) that not only aids AI but also serves as a knowledge repository for your team, helping onboard new members effectively.
- Explore the balance between trusting AI and maintaining control over critical aspects of your codebase; recognize that while AI can speed up processes, it requires careful oversight to avoid chaos.
- Leverage the insights on "vibe-coding" to foster a collaborative environment where AI and human creativity coexist, enhancing your software development practices.
- Reflect on the importance of writing tests; implementing this discipline will ensure quality and reliability in your products, safeguarding both user experience and company reputation.
- In the fast-paced New York tech scene, being an early adopter of structured AI practices could give you a competitive edge, allowing you to innovate while keeping your team aligned and productive.
- Consider alternate views that caution against over-reliance on AI; some argue that it may stifle critical thinking and problem-solving skills if not integrated thoughtfully.
- Remain aware of the evolving nature of software development; staying current with trends in AI and development methodologies will be crucial for long-term success in your business.

## AI Summary (from Notion)
This guide explores AI-assisted software development, emphasizing practices that enhance productivity and maintain code quality. Key insights include the importance of writing tests, understanding different modes of AI collaboration (as first-drafter, pair-programmer, and validator), and the necessity of maintaining thorough documentation like CLAUDE.md. It also highlights the significance of proper guardrails to prevent chaotic coding and outlines the critical boundaries that AI should never cross, such as modifying test files or database migrations. The document encourages a disciplined approach to integrating AI tools in development workflows for better outcomes.

## Content (from Notion)

Shimmering Substance - Jackson Pollock

Think of this post as your field guide to a new way of building software. By the time you finish reading, you’ll understand not just the how but the why behind AI-assisted development that actually works.

### Here’s What You’re Going to Learn

First, we’ll explore how to genuinely achieve that mythical 10x productivity boost—not through magic, but through deliberate practices that amplify AI’s strengths while compensating for its weaknesses. You’ll discover why some developers ship features in hours while others fight their AI tools for days.

Next, I’ll walk you through the exact infrastructure we use at Julep to ship production code daily with Claude’s help. This isn’t theoretical—it’s battle-tested on a codebase serving real users with real money on the line. You’ll see our CLAUDE.md templates, our commit strategies, and the guardrails that keep us from shipping disasters.

Most importantly, you’ll understand why writing your own tests remains absolutely sacred, even (especially) in the age of AI. This single principle will save you from the midnight debugging sessions that plague developers who hand over too much control to their AI assistants.

We’ll explore the three distinct modes of AI-assisted development, each with its own rhythms and rules. Like a musician learning when to play forte versus pianissimo, you’ll develop an intuition for when to let AI lead versus when to take firm control.

> 

## Why This Post Exists: From Meme to Method

Let me take you back to when this all started. 2Andrej Karpathy 3tweeted about “vibe-coding”—this idea of letting AI write your code while you just vibe. The developer community had a good laugh. It sounded like the ultimate developer fantasy: kick back, sip coffee, let the machines do the work.

The birth of “vibe coding”

Then Anthropic released Sonnet 3.7 and Claude Code, and something unexpected happened. The joke stopped being funny because it started being… possible? Of course, our trusty friend Cursor had been around awhile but this new interface finally felt like true vibe coding.

At Julep, we build complex AI workflow orchestration. Imagine trying to explain to an AI assistant a codebase that includes FastAPI services talking to Temporal workflows, all backed by a TimescaleDB database with 4vector embeddings, documented in TypeSpec, and organized in a 5monorepo that would make most developers weep. Our backend isn’t just complex—it’s a living, breathing system with years of accumulated decisions, patterns, and occasional technical debt.

We have taken the utmost care to keep code quality high, and ample documentation for ourselves. However, the sheer size, and historical context of why different parts of the code are organized the way they are takes weeks for a good engineer to grok. Getting AI to understand this interconnected maze felt like teaching calculus to someone who just learned arithmetic. But here’s what we discovered: Claude Code is intentionally low-level and unopinionated, providing close to raw model access without forcing specific workflows. This design philosophy creates something powerful—a tool that adapts to your workflow rather than forcing you into its box.

The flexibility, though, is a double-edged sword. Without proper guardrails, you’re not coding anymore—you’re playing whack-a-mole with an overeager intern who has memorized Stack Overflow but never shipped production code.

> 

## Understanding Vibe-Coding: More Than Meets the Eye

‘pls fix’

6Steve Yegge brilliantly coined the term CHOP—Chat-Oriented Programming in a slightly-dramatic-titled post “The death of the junior developer”. It’s a perfect description of the surface mechanics: you chat with an AI until code materializes. But after months of living this workflow, I’ve come to understand it’s much deeper than that.

Think of traditional coding like sculpting marble. You start with a blank block and carefully chisel away, line by line, function by function. Every stroke is deliberate, every decision yours. It’s satisfying but slow.

Vibe-coding is more like conducting an orchestra. You’re not playing every instrument—you’re directing, shaping, guiding. The AI provides the raw musical talent, but without your vision, it’s just noise. With your direction, it becomes a symphony.

I’ve identified three distinct postures you can take when vibe-coding, each suited to different moments in the development cycle:

1. AI as First-Drafter: Here, AI generates initial implementations while you focus on architecture and design. It’s like having a junior developer who can type at the speed of thought but needs constant guidance. Perfect for boilerplate, CRUD operations, and standard patterns.
1. AI as Pair-Programmer: This is the sweet spot for most development. You’re actively collaborating, bouncing ideas back and forth. The AI suggests approaches, you refine them. You sketch the outline, AI fills in details. It’s like pair programming with someone who has read every programming book ever written but has never actually shipped code.
1. AI as Validator: Sometimes you write code and want a sanity check. AI reviews for bugs, suggests improvements, spots patterns you might have missed. Think of it as an incredibly well-read code reviewer who never gets tired or cranky.
> 

## The Three Modes of Vibe-Coding: A Practical Framework

After months of experimentation and more than a few production incidents, I’ve settled on three distinct modes of operation. Each has its own rhythm, its own guardrails, and its own optimal use cases.

### Mode 1: The Playground

Lighter Fluid

When to use it: Weekend hacks, personal scripts, proof-of-concepts, and those “I wonder if…” moments that make programming fun.

In Playground Mode, you embrace the chaos. There’s zero ceremony, no extensive documentation, no careful guardrails. Claude writes 80-90% of the code while you provide just enough steering to keep things on track. It’s liberating and slightly terrifying.

Here’s what Playground Mode looks like in practice: You have an idea for a script to analyze your Spotify listening history. You open Claude, describe what you want in plain English, and watch as it generates a complete solution. No CLAUDE.md file, no careful prompting—just raw, unfiltered AI assistance.

The beauty of Playground Mode is its speed. You can go from idea to working prototype in minutes. The danger is that this cowboy coding style is absolutely inappropriate for anything that matters. Use it for experiments, never for production. Trust me, while the amazing folks preaching otherwise, good engineering principles still matter, now more than ever.

### Mode 2: Pair Programming

Compiling

When to use it: Projects under ~5,000 lines of code, side projects with real users, demos (you don’t want to break), or well-scoped small services in larger systems.

This is where vibe-coding starts to shine for real work. You need structure, but not so much that it slows you down. The key innovation here is the CLAUDE.md file—custom documentation that Claude automatically reads when invoked. From Anthropic’s Best practices for Claude Code:

> 

Let me show you how this transforms the development experience. Instead of repeatedly explaining your project’s conventions, you document them once. Here’s a real example from a recent side project:

```plain text
## Project: Analytics Dashboard

This is a Next.js dashboard for visualizing user analytics. We follow
these conventions to maintain consistency:

### Architecture Decisions
- Server Components by default, Client Components only when necessary
- tRPC for type-safe API calls
- Prisma for database access with explicit select statements
- Tailwind for styling (no custom CSS files)

### Code Style
- Formatting: Prettier with 100-char lines
- Imports: sorted with simple-import-sort
- Components: Pascal case, co-located with their tests
- Hooks: always prefix with 'use'

### Patterns to Follow
- Data fetching happens in Server Components
- Client Components receive data as props
- Use Zod schemas for all external data
- Error boundaries around every data display component

### What NOT to Do
- Don't use useEffect for data fetching
- Don't create global state without explicit approval
- Don't bypass TypeScript with 'any' types
```

With this context, Claude becomes remarkably effective. It’s like the difference between explaining your project to a new hire every single day versus having them read the onboarding docs once.

But Pair Programming Mode requires more than just documentation. You need to actively guide the AI with what I call “anchor comments”—breadcrumbs that prevent Claude from wandering into the wilderness:

```plain text
// AIDEV-NOTE: This component uses virtual scrolling for performance
// See: https://tanstack.com/virtual/latest
// Don't convert to regular mapping—we handle 10k+ items

export function DataTable({ items }: DataTableProps) {
  // Claude, when you edit this, maintain the virtual scrolling
  ...
}
```

These comments serve a dual purpose: they guide the AI and document your code for humans. It’s documentation that pays dividends in both directions. The key distinction between such “anchor comments” and regular comments: these are written, maintained, and meant to be used by Claude itself. Here’s an actual snippet from our project’s CLAUDE.md:

```plain text
## Anchor comments

Add specially formatted comments throughout the codebase, where appropriate, for yourself as inline knowledge that can be easily `grep`ped for.

### Guidelines:

- Use `AIDEV-NOTE:`, `AIDEV-TODO:`, or `AIDEV-QUESTION:` (all-caps prefix) for comments aimed at AI and developers.
- Keep them concise (≤ 120 chars).
- **Important:** Before scanning files, always first try to **locate existing anchors** `AIDEV-*` in relevant subdirectories.
- **Update relevant anchors** when modifying associated code.
- **Do not remove `AIDEV-NOTE`s** without explicit human instruction.

Example:
# AIDEV-NOTE: perf-hot-path; avoid extra allocations (see ADR-24)
async def render_feed(...):
    ...
```

### Mode 3: Production/Monorepo Scale

RTFM

When to use it: Large codebases, systems with real users, anything where bugs cost money or reputation.

This is where you become an editor-in-chief managing a newsroom. Claude can generate tremendous amounts of code, but integrating it into a complex system requires careful orchestration. You’re not just coding anymore—you’re conducting.

Let me start with a big caveat: vibe coding at this scale does NOT scale very well, yet. I definitely do see these systems getting significantly better at handling larger codebases but, for them to be effective, significant effort is needed to help them navigate, understand, and safely hack on them without getting lost in a maze. Generally speaking, it’s better to section them into individual services, and 7sub-modules when possible.

As a universal principle, good engineering practices apply to large-scale projects, vibe coded or not. For example, at production scale, boundaries become critical. Every integration point needs explicit documentation:

```plain text
# AIDEV-NOTE: API Contract Boundary - v2.3.1
# This response format is consumed by:
# - iOS app v3.2+
# - Android app v3.0+
# - Dashboard frontend
# ANY changes require version bump and migration plan
# See: docs/api-versioning.md

@router.get("/users/{user_id}/feed")
async def get_user_feed(user_id: UUID) -> FeedResponse:
    # Claude: the response shape here is sacred
    # Changes break real apps in production
    ...
```

Without these boundaries, Claude will happily “improve” your API and break every client in production. Bottom line: larger projects should definitely start adopting vibe coding in parts, and adopt methodologies that enhance that experience but, don’t expect to land large features reliably just yet. (as of June 7, 2025 / AI epoch)

## Infrastructure: The Foundation of Sustainable AI Development

### CLAUDE.md: Your Single Source of Truth

Let me be absolutely clear about this: CLAUDE.md is not optional documentation. It’s the difference between AI that helps and AI that hurts. Every minute you spend updating it saves an hour of cleanup later.

Think of CLAUDE.md as a constitution for your codebase. It establishes the fundamental laws that govern how code should be written, how systems interact, and what patterns to follow or avoid. Organizations that invest in developing the skills and capabilities of their teams get better outcomes—and your CLAUDE.md is that investment crystallized into documentation.

Here’s an abridged version of our production CLAUDE.md structure, refined over thousands of AI-assisted commits:

```plain text
# CLAUDE.md - Julep Backend Service

## The Golden Rule
When unsure about implementation details, ALWAYS ask the developer.
Do not make assumptions about business logic or system behavior.

## Project Context
Julep enables developers to build stateful AI agents using declarative
workflows. We handle the complexity of state management, execution,
and recovery so developers can focus on agent behavior.

## Critical Architecture Decisions

### Why Temporal?
We use Temporal for workflow orchestration because:
1. Workflows can run for days/weeks with perfect reliability
2. Automatic recovery from any failure point
3. Built-in versioning for long-running workflows
4. Native support for human-in-the-loop patterns

### Why PostgreSQL + pgvector?
1. ACID compliance for workflow state (can't lose user data)
2. Vector similarity search for agent memory
3. JSON columns for flexible agent configurations
4. Row-level security for multi-tenant isolation

### Why TypeSpec?
Single source of truth for API definitions that generates:
- OpenAPI specs
- TypeScript/Python clients
- Validation schemas
- Documentation

This prevents drift between implementation and contracts.

## Code Style and Patterns

### Anchor comments

Add specially formatted comments throughout the codebase, where appropriate, for yourself as inline knowledge that can be easily `grep`ped for.

### Guidelines:

- Use `AIDEV-NOTE:`, `AIDEV-TODO:`, or `AIDEV-QUESTION:` (all-caps prefix) for comments aimed at AI and developers.
- Keep them concise (≤ 120 chars).
- **Important:** Before scanning files, always first try to **locate existing anchors** `AIDEV-*` in relevant subdirectories.
- **Update relevant anchors** when modifying associated code.
- **Do not remove `AIDEV-NOTE`s** without explicit human instruction.
- Make sure to add relevant anchor comments, whenever a file or piece of code is:
  * too long, or
  * too complex, or
  * very important, or
  * confusing, or
  * could have a bug unrelated to the task you are currently working on.

### Python Conventions
- Format: Black with 96-char lines (see pyproject.toml)
- Imports: isort with black profile
- Types: Full typing with `from __future__ import annotations`
- Docstrings: Google style for public APIs only

### Async Patterns
# CORRECT: Always use async context managers
async with self.db_pool.acquire() as conn:
    result = await conn.fetchrow(query)

# WRONG: Manual connection handling
conn = await self.db_pool.acquire()
result = await conn.fetchrow(query)
await conn.close()  # Easy to forget!

### Error Handling Hierarchy
ApplicationError
├── ValidationError (4xx - client's fault)
│   ├── SchemaValidationError
│   ├── BusinessRuleError
│   └── RateLimitError
└── SystemError (5xx - our fault)
    ├── DatabaseError
    ├── ExternalServiceError
    └── InfrastructureError

Always use specific errors. Never raise generic Exception.

## Domain Glossary (Claude, learn these!)

- **Agent**: AI entity with memory, tools, and defined behavior
- **Task**: Workflow definition composed of steps (NOT a Celery task)
- **Execution**: Running instance of a task
- **Tool**: Function an agent can call (browser, API, etc.)
- **Session**: Conversation context with memory
- **Entry**: Single interaction within a session

These terms have specific meanings. Don't use them casually.

## Integration Points and Boundaries

### API Versioning
- URL: /api/v{major}/...
- Breaking changes require major version bump
- Deprecation notice: 3 months minimum
- See: docs/api-versioning.md

### Database Migrations
- Tool: Alembic with async support
- Pattern: Expand-contract for zero-downtime
- Testing: Migration dry-run required
- Rollback: Every migration needs a down()

### External Services
- Circuit breakers on all external calls
- Timeout: 30s default, configurable per service
- Retries: Exponential backoff with jitter
- Fallbacks: Graceful degradation required

## What AI Must NEVER Do

1. **Never modify test files** - Tests encode human intent
2. **Never change API contracts** - Breaks real applications
3. **Never alter migration files** - Data loss risk
4. **Never commit secrets** - Use environment variables
5. **Never assume business logic** - Always ask
6. **Never remove AIDEV- comments** - They're there for a reason

## Performance Considerations

- Database queries must use indexes (run EXPLAIN)
- N+1 queries are bugs (use DataLoader pattern)
- Memory leaks matter (profile long-running tasks)
- Cache invalidation needs explicit strategy

## Getting Started

1. Read this entire file
2. Check docs/architecture/decisions/ for ADRs
3. Run `make dev-setup` for local environment
4. Try `make test-watch` for fast feedback
5. Ask questions early and often

Remember: We optimize for maintainability over cleverness.
When in doubt, choose the boring solution.
```

This document becomes the shared context between you and Claude. It’s like having a senior developer whispering guidance in Claude’s ear throughout the coding session.

### Anchor Comments: Breadcrumbs at Scale

As your codebase grows, CLAUDE.md alone isn’t enough. You need inline guidance—what I call anchor comments. These serve as local context that prevents AI from making locally bad decisions.

Think of your codebase as a city and anchor comments as street signs. Without them, even smart visitors get lost. Here’s how we use them effectively:

```plain text
# AIDEV-NOTE: Critical performance path - this serves 100k req/sec
# We pre-compute these values in a background job (see workers/feed_prep.py)
# DO NOT add database queries here
def get_user_feed(user_id: UUID, cached_data: FeedCache) -> List[FeedItem]:
    # The seemingly redundant list copy is intentional
    # We need to avoid mutating the cached data
    items = cached_data.items[:]

    # AIDEV-TODO: Implement pagination (ticket: FEED-123)
    # Current implementation returns all items (max 1000)
    # Need cursor-based pagination for infinite scroll

    # AIDEV-QUESTION: Why do we filter private items here instead of in cache?
    # Historical context: Privacy rules can change between cache updates
    # User might revoke access after cache was built
    filtered = [item for item in items if user_has_access(user_id, item)]

    return filtered
```

These comments create a narrative that helps both AI and humans understand not just what the code does, but why it does it that way.

### Git Workflows for AI Development

One of the most underappreciated aspects of AI-assisted development is how it changes your git workflow. You’re now generating code at a pace that can quickly pollute your git history if you’re not careful.

It really only applies to very large codebases because it is not a very straightforward tool, but I recommend using git worktrees to create isolated environments for AI experiments:

```plain text
# Create an AI playground without polluting main
git worktree add ../ai-experiments/cool-feature -b ai/cool-feature

# Let Claude go wild in the isolated worktree
cd ../ai-experiments/cool-feature
# ... lots of experimental commits ...

# Cherry-pick the good stuff back to main
cd ../main-repo
git cherry-pick abc123  # Just the commits that worked

# Clean up when done
git worktree remove ../ai-experiments/cool-feature
```

> 

This approach gives you the best of both worlds: Claude can experiment freely while your main branch history stays clean and meaningful.

For commit messages, we’ve standardized on tagging AI-assisted commits:

```plain text
feat: implement user feed caching [AI]

- Add Redis-based cache for user feeds
- Implement cache warming on user login
- Add metrics for cache hit rate

AI-assisted: core logic generated, tests human-written
```

This transparency helps during code review—reviewers know to pay extra attention to AI-generated code.

## The Sacred Rule: Humans Write Tests

Now we come to the most important principle in AI-assisted development. It’s so important that I’m going to repeat it in multiple ways until it’s burned into your memory:

Never. Let. AI. Write. Your. Tests.

Tests are not just code that verifies other code works. Tests are executable specifications. They encode your actual intentions, your edge cases, your understanding of the problem domain. High performers excel at both speed and stability—there’s no trade-off. Tests are how you achieve both.

Beware…

Let me illustrate why this matters with an example. Let’s say we asked Claude to implement a rate limiter:

```plain text
class RateLimiter:
    def __init__(self, max_requests: int, window_seconds: int):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = defaultdict(list)

    def is_allowed(self, user_id: str) -> bool:
        now = time.time()
        user_requests = self.requests[user_id]

        # Clean old requests
        self.requests[user_id] = [
            req_time for req_time in user_requests
            if now - req_time < self.window_seconds
        ]

        if len(self.requests[user_id]) < self.max_requests:
            self.requests[user_id].append(now)
            return True
        return False
```

Looks reasonable, right? Claude even helpfully generated tests:

```plain text
def test_rate_limiter():
    limiter = RateLimiter(max_requests=3, window_seconds=60)

    assert limiter.is_allowed("user1") == True
    assert limiter.is_allowed("user1") == True
    assert limiter.is_allowed("user1") == True
    assert limiter.is_allowed("user1") == False  # Limit reached
```

But here’s what Claude’s tests missed—what only a human who understands the business requirements would test: Claude’s implementation has a memory leak. Users who hit the API once and never return leave their data in memory forever. The AI-generated tests check the happy path but miss this critical production concern.

Vibe coding at its best

This is why humans write tests. We understand the context, the production environment, the edge cases that matter. At Julep, our rule is absolute:

```plain text
## Testing Discipline

| What | AI CAN Do | AI MUST NOT Do |
|------|-----------|----------------|
| Implementation | Generate business logic | Touch test files |
| Test Planning | Suggest test scenarios | Write test code |
| Debugging | Analyze test failures | Modify test expectations |

If an AI tool touches a test file, the PR gets rejected. No exceptions.
```

Your tests are your specification. They’re your safety net. They’re the encoded wisdom of every bug you’ve fixed and every edge case you’ve discovered. Guard them zealously.

## Scaling Without Drowning: Token Economics and Context Management

One of the most counterintuitive lessons in AI-assisted development is that being stingy with context to save tokens actually costs you more. It’s like trying to save money on gas by only filling your tank halfway—you just end up making more trips to the gas station.

Token budgets matter. Provide focused prompts, reduce diff length, and avoid large-file bloat by summarizing intent in advance. But “focused” doesn’t mean “minimal”—it means “relevant and complete.”

Let me show you the false economy of starved prompts:

Starved Prompt Attempt:

```plain text
"Add caching to the user endpoint"
```

Claude’s Response: Implements caching… but:

- Uses in-memory cache (won’t work with multiple servers)
- No cache invalidation strategy
- No metrics or monitoring
- No consideration of cache stampede
Result: 3 more rounds of fixes, 4x the tokens spent.

Proper Context-Rich Prompt:

```plain text
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

The lesson? Front-load context to avoid iteration cycles. Think of tokens like investing in good tools—the upfront cost pays for itself many times over.

In fact, I recommend that all projects should routinely ask Claude to look through the codebase changes, and add context to CLAUDE.md

### Fresh Sessions and Mental Models

Here’s another counterintuitive practice: use fresh Claude sessions for distinct tasks. It’s tempting to keep one long-running conversation, but this leads to context pollution.

Think of it like this: you wouldn’t use the same cutting board for vegetables after cutting raw chicken. Similarly, don’t use the same Claude session for database migrations after discussing frontend styling. The context bleeds through in subtle ways.

Our rule: One task, one session. When the task is done, start fresh. This keeps Claude’s “mental model” clean and focused.

## Case Study: Shipping Structured Errors in Production

Let me walk you through a real refactoring we did at Julep that showcases production-scale vibe-coding. We needed to replace our ad-hoc error handling with a structured error hierarchy across 500+ endpoints.

The Human Decisions (The Why):

First, we had to decide on our error taxonomy. This is pure architectural work—Claude can’t make these decisions because they involve understanding our business, our users, and our operational needs:

```plain text
# SPEC.md - Error Hierarchy Design (Human-Written)

## Error Philosophy
- Client errors (4xx) must include actionable feedback
- System errors (5xx) must include trace IDs for debugging
- All errors must be JSON-serializable
- Error codes must be stable (clients depend on them)

## Hierarchy
BaseError
├── ClientError (4xx)
│   ├── ValidationError
│   │   ├── SchemaValidationError - Request doesn't match schema
│   │   ├── BusinessRuleError - Valid schema, invalid business logic
│   │   └── RateLimitError - Too many requests
│   └── AuthError
│       ├── AuthenticationError - Who are you?
│       └── AuthorizationError - You can't do that
└── SystemError (5xx)
    ├── DatabaseError - Connection, timeout, deadlock
    ├── ExternalServiceError - APIs, webhooks failing
    └── InfrastructureError - Disk full, OOM, etc.

## Error Response Format
{
  "error": {
    "code": "VALIDATION_FAILED",     // Stable code for clients
    "message": "Email already exists", // Human-readable
    "details": { ... },               // Structured data
    "trace_id": "abc-123-def"         // For debugging
  }
}
```

The AI Execution (The How):

With the specification clear, we unleashed Claude on the mechanical refactoring:

```plain text
# Prompt to Claude:
"""
Refactor our error handling to match SPEC.md.

Current state:
- raise Exception("User not found")
- raise ValueError("Invalid email")
- return {"error": "Something went wrong"}, 500

Target state:
- Use error hierarchy from SPEC.md
- Include proper error codes
- Add trace_id to all 5xx errors
- Preserve existing error messages where sensible

Start with the auth module. Show me the plan before implementing.
"""
```

Claude’s plan was solid:

```plain text
1. Create error hierarchy in `common/errors.py`
2. Create error response formatter
3. Update each module systematically
4. Add error handling middleware
```

The beautiful part? Claude handled the tedious work of finding and updating 500+ error sites, while we focused on reviewing the semantics:

```plain text
# Before (Claude found these patterns):
if not user:
    raise Exception("User not found")

# After (Claude's refactoring):
if not user:
    raise AuthenticationError(
        message="User not found",
        code="USER_NOT_FOUND",
        details={"identifier": email}
    )
```

> 

## Leadership and Culture in the AI Era

Your role as a senior engineer has fundamentally shifted. You’re no longer just writing code—you’re curating knowledge, setting boundaries, and teaching both humans and AI systems how to work effectively.

Think of yourself as the editor-in-chief of a newspaper. Your junior developers and AI assistants are reporters bringing you stories (code). Your job is to ensure consistency, quality, and alignment with the bigger picture. Lean management and continuous delivery practices help improve software delivery performance, which in turn improves organizational performance—and this includes how you manage AI collaboration.

### The New Onboarding Checklist

When new developers join our team, they get two onboarding tracks: one for humans, one for working with AI. Here’s our combined checklist:

Week 1: Foundation

```plain text
□ Read team CLAUDE.md files (start with root, then service-specific)
□ Set up development environment
□ Run the test suite successfully
□ Make first PR (human-written, no AI)
□ Review 3 PRs from other team members
```

Week 2: Guided AI Collaboration

```plain text
□ Set up Claude with team templates
□ Complete "toy problem" with AI assistance
□ Review an AI-assisted PR with a senior
□ Practice prompt patterns
□ Create first AI-assisted PR (with supervision)
```

Week 3: Independent Work

```plain text
□ Ship first significant AI-assisted feature
□ Write tests for another developer's AI output
□ Contribute to prompt pattern library
□ Lead one code review session
```

### Building a Culture of Transparency

One cultural shift that’s essential: normalize disclosure of AI assistance. We’re not trying to hide that we use AI—we’re trying to use it responsibly. Every commit message that includes AI work gets tagged:

```plain text
# Our .gitmessage template
# feat/fix/docs: <description> [AI]?
#
# [AI] tag meanings:
# [AI] - Significant AI assistance (>50% generated)
# [AI-minor] - Minor AI assistance (<50% generated)
# [AI-review] - AI used for code review only
#
# Body: Explain what AI did vs. what you did
# Example:
# feat: add Redis caching to user service [AI]
#
# AI generated the cache implementation and Redis client setup.
# I designed the cache key structure and wrote all tests.
# Manually verified cache invalidation logic works correctly.
```

This transparency serves multiple purposes:

1. Reviewers know to pay extra attention
1. Future debuggers understand the code’s provenance
1. Team learns which patterns work well with AI
1. No one feels shame about using available tools
Creating an environment where developers can leverage AI effectively, without fear or shame, is part of building that high-performing culture.

## Things Claude Should Never Touch (Carved in Stone)

Let’s be crystal clear about boundaries. These aren’t suggestions—they’re commandments. Violate them at your peril.

### The Sacred List of Never-Touch

❌ Test Files

```plain text
# This is SACRED GROUND
# No AI shall pass
def test_critical_business_logic():
    """This test encodes $10M worth of domain knowledge"""
    pass
```

Tests encode human understanding. They’re your safety net, your specification, your accumulated wisdom. When Claude writes tests, it’s just verifying that the code does what the code does—not what it should do.

❌ Database Migrations

```plain text
-- migrations/2024_01_15_restructure_users.sql
-- DO NOT LET AI TOUCH THIS
-- One wrong move = data loss = career loss
ALTER TABLE users ADD COLUMN subscription_tier VARCHAR(20);
UPDATE users SET subscription_tier = 'free' WHERE subscription_tier IS NULL;
ALTER TABLE users ALTER COLUMN subscription_tier SET NOT NULL;
```

Migrations are irreversible in production. They require understanding of data patterns, deployment timing, and rollback strategies that AI cannot grasp.

❌ Security-Critical Code

```plain text
# auth/jwt_validator.py
# HUMAN EYES ONLY - Security boundary
def validate_token(token: str) -> Optional[UserClaims]:
    # Every line here has been security-reviewed
    # Changes require security team approval
    # AI suggestions actively dangerous here
```

❌ API Contracts Without Versioning

```plain text
# openapi.yaml
# Breaking this = breaking every client
# AI doesn't understand mobile app release cycles
paths:
  /api/v1/users/{id}:
    get:
      responses:
        200:
          schema:
            $ref: '#/definitions/UserResponse'  # FROZEN until v2
```

❌ Configuration and Secrets

```plain text
# config/production.py
DATABASE_URL = os.environ["DATABASE_URL"]  # Never hardcode
STRIPE_SECRET_KEY = os.environ["STRIPE_SECRET_KEY"]  # Obviously
FEATURE_FLAGS = {
    "new_pricing": False,  # Requires product decision
}
```

### The Hierarchy of AI Mistakes

Not all AI mistakes are equal. Here’s how we categorize them:

Level 1: Annoying but Harmless

- Wrong formatting (your linter will catch it)
- Verbose code (refactor later)
- Suboptimal algorithms (profile will reveal)
Level 2: Expensive to Fix

- Breaking internal APIs (requires coordination)
- Changing established patterns (confuses team)
- Adding unnecessary dependencies (bloat)
Level 3: Career-Limiting

- Modifying tests to make them pass
- Breaking API contracts
- Leaking secrets or PII
- Corrupting data migrations
Your guardrails should be proportional to the mistake level. Level 1 mistakes teach juniors. Level 3 mistakes teach you to update your LinkedIn.

## The Future of Development: Where This Is Heading

As I write this in 2025, we’re in the awkward adolescence of AI-assisted development. The tools are powerful but clumsy, like a teenager who just hit a growth spurt. But the trajectory is clear, and it’s accelerating.

Good documentation is foundational for successfully implementing DevOps capabilities. In the AI age, documentation isn’t just helpful—it’s the interface between human intent and AI capability. The teams that excel will be those who treat documentation as code, who maintain their CLAUDE.md files with the same rigor as their test suites.

What I see coming:

- AI that understands entire codebases, not just files
- Persistent memory across sessions and projects
- Proactive AI that suggests improvements without prompting
- AI that learns your team’s patterns and preferences
But even as capabilities expand, the fundamentals remain: humans set direction, AI provides leverage. We’re tool users, and these are simply the most powerful tools we’ve ever created.

## The Bottom Line: Start Here, Start Today

If you’ve made it this far, you’re probably feeling a mix of excitement and trepidation. That’s the right response. AI-assisted development is powerful, but it requires discipline and intentionality.

Here’s your action plan:

Today:

1. Create a CLAUDE.md for your current project
1. Add three anchor comments yourself to your gnarliest code
1. Try one AI-assisted feature with proper boundaries
This Week:

1. Establish AI commit message conventions with your team
1. Run an AI-assisted coding session with a junior developer
1. Write tests for one piece of AI-generated code
This Month:

1. Measure your deployment frequency before/after AI adoption
1. Create a prompt pattern library for common tasks
1. Run a team retrospective on AI-assisted development
The most important thing? Start. Start small, start careful, but start. The developers who master this workflow aren’t necessarily smarter or more talented—they’re just the ones who started earlier and learned from more mistakes.

Software delivery performance predicts organizational performance. In an industry where speed and quality determine success, AI assistance isn’t a nice-to-have—it’s a competitive necessity. But only if you do it right.

Vibe-coding, despite its playful name, is serious business. It’s a new way of thinking about software development that amplifies human capabilities rather than replacing them. Master it, and you’ll ship better software faster than you ever thought possible. Ignore it, and you’ll watch competitors lap you while you’re still typing boilerplate.

The tools are here. The patterns are proven. The only question is: will you be conducting the orchestra, or still playing every instrument yourself?

### Ready to Dive In? Resources to Get Started:

📄 Our Battle-Tested CLAUDE.md Template:

github.com/julep-ai/julep/blob/main/AGENTS.md

🤝 Questions? Find me on Twitter: @diwanksingh

💬 Join the Discussion: Share your own patterns and learnings

📚 Recommended reading:

- Peter Senge – The Fifth Discipline (2010)
- “Beyond the 70 %: Maximising the Human 30 % of AI-Assisted Coding” (Mar 13 2025) – Addy Osmani
- Mark Richards & Neal Ford – Fundamentals of Software Architecture, 2nd ed. (2025)
- Nicole Forsgren, Jez Humble, Gene Kim - Accelerate: The Science of Lean Software and DevOps
Remember: perfect is the enemy of shipped. Start with one small project, establish your boundaries, and iterate. The future of development is here—it’s just not evenly distributed yet.

> 

1. That statistic comes from the groundbreaking research in the book “Accelerate: The Science of Lean Software and DevOps” by Nicole Forsgren, Jez Humble, and Gene Kim.     
1. Andrej Karpathy is a Slovak-Canadian computer scientist who served as the director of artificial intelligence and Autopilot Vision at Tesla. He co-founded and formerly worked at OpenAI, where he specialized in deep learning and computer vision.
1. There's a new kind of coding I call "vibe coding", where you fully give in to the vibes, embrace exponentials, and forget that the code even exists. It's possible because the LLMs (e.g. Cursor Composer w Sonnet) are getting too good. Also I just talk to Composer with SuperWhisper…— Andrej Karpathy (@karpathy) February 2, 2025 ↩︎
1. https://github.com/pgvector/pgvector↩︎
1. https://en.wikipedia.org/wiki/Monorepo↩︎
1. Steve Yegge is an American computer programmer and blogger who is known for writing about programming languages, productivity and software culture through his “Stevey’s Drunken Blog Rants” site, followed by “Stevey’s Blog Rants.”
1. I don’t mean git submodules – in fact, don’t use them with coding assistants for sure, they are mine fields for models.↩︎
Vibe Engineering


