# Context Engineering for AI Agents

Managing the limited context window of LLMs to build effective agents.

---

## Context Engineering vs Prompt Engineering

*Source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (Anthropic) - Added: 2026-01-18*

**Prompt engineering** = Writing effective prompts (one-shot tasks, system instructions)

**Context engineering** = Curating and maintaining the optimal set of tokens during LLM inference across multiple turns

### The Shift

Early LLM work focused on single-turn tasks. Agents operate over multiple inference turns and longer time horizons. Context engineering is iterative - curation happens each time we decide what to pass to the model.

### The Core Problem: Context Rot

As token count increases, model's ability to accurately recall information decreases. This emerges across all models.

**Key insight:** Context is a finite resource with diminishing marginal returns.

**Why it happens (architectural reasons):**
- Transformers have every token attend to every other token = n² pairwise relationships for n tokens
- Models trained on shorter sequences more often than longer ones
- Position encoding interpolation allows longer sequences but with degradation

**Result:** Performance gradient, not hard cliff. Models remain capable at longer contexts but show reduced precision for information retrieval and long-range reasoning.

---

## Anatomy of Effective Context

**Guiding principle:** Find the smallest possible set of high-signal tokens that maximize the likelihood of the desired outcome.

### System Prompts

**The Goldilocks Zone** - avoid two failure modes:

| Failure Mode | Problem |
|--------------|---------|
| Too specific | Hardcoded brittle logic, fragility, maintenance complexity |
| Too vague | No concrete signals, false assumptions of shared context |

**Optimal:** Specific enough to guide behavior, flexible enough to provide strong heuristics.

**Best practices:**
- Organize into distinct sections with XML tags or Markdown headers
- Start minimal with best model, add instructions based on observed failure modes
- Strive for minimal set that fully outlines expected behavior (minimal ≠ short)

### Tools

Tools define the contract between agents and their information/action space.

**Key requirements:**
- Self-contained and robust to error
- Extremely clear on intended use
- Minimal overlap in functionality
- Input parameters descriptive and unambiguous

**Common failure mode:** Bloated tool sets with ambiguous decision points. If a human can't definitively say which tool to use, neither can an AI.

### Examples (Few-Shot)

Still strongly advised, but:

**Don't:** Stuff laundry list of edge cases
**Do:** Curate diverse, canonical examples that portray expected behavior

> "For an LLM, examples are the 'pictures' worth a thousand words."

---

## Context Retrieval Strategies

### Pre-Inference Retrieval (Traditional)

Embedding-based retrieval surfaces context before the agent starts. Works but has limitations.

### Just-In-Time Context (Agentic)

Maintain lightweight identifiers (file paths, stored queries, web links), dynamically load data at runtime using tools.

**Example - Claude Code:**
- Writes targeted queries, stores results
- Uses `head` and `tail` to analyze large data
- Never loads full data objects into context

**Advantages:**
- Metadata provides signals (folder hierarchies, naming conventions, timestamps)
- Progressive disclosure - agents incrementally discover context through exploration
- Self-managed context window stays focused

**Trade-offs:**
- Runtime exploration slower than pre-computed retrieval
- Requires good tools and heuristics for navigation
- Without proper guidance, agents waste context on dead-ends

### Hybrid Strategy

Some data retrieved up front for speed, further autonomous exploration at agent's discretion.

**Example - Claude Code:**
- `CLAUDE.md` files dropped into context up front
- `glob` and `grep` allow just-in-time navigation

**When to use:** Contexts with less dynamic content (legal, finance). As models improve, trend toward more autonomy.

> "Do the simplest thing that works"

---

## Long-Horizon Task Techniques

For tasks spanning tens of minutes to multiple hours.

### 1. Compaction

Taking conversation near context limit, summarizing, reinitiating with summary.

**What to preserve:**
- Architectural decisions
- Unresolved bugs
- Implementation details

**What to discard:**
- Redundant tool outputs
- Superfluous messages

**Implementation tips:**
- Tune prompt on complex agent traces
- Start by maximizing recall (capture everything relevant)
- Then improve precision (eliminate superfluous)
- **Low-hanging fruit:** Clear tool calls and results deep in message history

### 2. Structured Note-Taking (Agentic Memory)

Agent writes notes persisted outside context window, pulled back in later.

**Examples:**
- Claude Code creating a to-do list
- Agent maintaining a `NOTES.md` file
- Claude playing Pokemon tracking objectives across thousands of steps

**Benefits:**
- Track progress across complex tasks
- Maintain critical context and dependencies
- Survive context resets

### 3. Sub-Agent Architectures

Specialized sub-agents handle focused tasks with clean context windows.

**Pattern:**
- Main agent coordinates with high-level plan
- Subagents perform deep work or search
- Each subagent may use tens of thousands of tokens
- Returns condensed summary (1,000-2,000 tokens)

**Result:** Clear separation of concerns - detailed search context isolated in sub-agents, lead agent focuses on synthesis.

### Choosing Between Approaches

| Technique | Best For |
|-----------|----------|
| Compaction | Tasks requiring extensive back-and-forth |
| Note-taking | Iterative development with clear milestones |
| Multi-agent | Complex research/analysis with parallel exploration |

---

## Key Principles Summary

1. **Context is finite** - Treat it as precious resource with diminishing returns
2. **High-signal, minimal tokens** - Smallest set that maximizes desired outcome
3. **Tools should be clear and minimal** - No ambiguous decision points
4. **Examples over rules** - Few well-chosen examples beat exhaustive edge cases
5. **Just-in-time over pre-loading** - Let agents discover context progressively
6. **Compaction for long tasks** - Summarize, don't accumulate
7. **Notes for persistence** - External memory survives context limits
8. **Sub-agents for isolation** - Deep work in clean contexts, return summaries

---

## Multi-Agent Research Systems: Anthropic's Approach

*Source: https://www.anthropic.com/engineering/built-multi-agent-research-system (Anthropic) - Added: 2026-01-18*

Anthropic published a detailed breakdown of how they built "Claude Research" using multiple agents. This is one of the most practical, actionable guides to multi-agent system design available.

### What is a Multi-Agent System?

Multiple agents (LLMs autonomously using tools in a loop) working together. Claude Research uses an orchestrator-worker pattern where a lead agent coordinates the process while delegating to specialized subagents operating in parallel.

**Flow:**
1. User submits query
2. Lead agent analyzes query, develops strategy
3. Lead agent spawns subagents to explore different aspects simultaneously
4. Subagents act as intelligent filters - iteratively using search tools to gather info
5. Subagents return condensed findings to lead agent
6. Lead agent compiles final answer with citations

### Why Multi-Agent?

**The core benefit:** Managing context limits. Each sub-task has its own separate context, allowing much larger volumes of content to be processed.

**Token usage analysis (BrowseComp eval):**
- Token usage alone explains **80%** of performance variance
- Number of tool calls and model choice explain the remaining 15%
- Multi-agent systems effectively scale token usage for tasks exceeding single-agent limits

**Performance comparison:** Multi-agent with Claude Opus 4 (lead) + Claude Sonnet 4 (subagents) outperformed single-agent Claude Opus 4 by **90.2%** on internal research eval.

**Best use cases:**
- Breadth-first queries requiring multiple independent directions
- Tasks where information exceeds single context windows
- Heavy parallelization scenarios
- Complex tool interfaces

**The trade-off:** Burns tokens fast:
- Agents use ~4× more tokens than chat interactions
- Multi-agent systems use ~15× more tokens than chats
- Economic viability requires tasks where value justifies the cost

**Poor fit for multi-agent:**
- Domains requiring all agents to share the same context
- Many dependencies between agents
- Most coding tasks (fewer truly parallelizable subtasks)
- Real-time coordination and delegation

### Prompt Engineering Principles for Multi-Agent Systems

Anthropic's key lessons for prompting agents:

#### 1. Think Like Your Agents

Build simulations to watch agents work step-by-step. This reveals failure modes:
- Agents continuing when they already had sufficient results
- Using overly verbose search queries
- Selecting incorrect tools

**Key insight:** Effective prompting relies on developing an accurate mental model of the agent.

#### 2. Teach the Orchestrator How to Delegate

Each subagent needs:
- A clear objective
- Output format specification
- Guidance on tools and sources to use
- Clear task boundaries

**Failure mode:** Simple instructions like "research the semiconductor shortage" are too vague - subagents misinterpret tasks or duplicate work.

#### 3. Scale Effort to Query Complexity

Embed explicit scaling rules in prompts:

| Query Complexity | Subagents | Tool Calls Each |
|-----------------|-----------|-----------------|
| Simple fact-finding | 1 | 3-10 |
| Direct comparisons | 2-4 | 10-15 |
| Complex research | 10+ | Clearly divided responsibilities |

Without guidelines, agents overinvest in simple queries.

#### 4. Tool Design and Selection

Agent-tool interfaces are as critical as human-computer interfaces. Using the right tool is often strictly necessary.

**Heuristics to embed in prompts:**
- Examine all available tools first
- Match tool usage to user intent
- Search the web for broad external exploration
- Prefer specialized tools over generic ones

**Warning:** Bad tool descriptions send agents down wrong paths. Each tool needs a distinct purpose and clear description.

#### 5. Let Agents Improve Themselves

Claude 4 models can be excellent prompt engineers. When given a prompt and failure mode, they diagnose why the agent is failing and suggest improvements.

**Tool-testing agent pattern:**
1. Give agent a flawed MCP tool
2. Agent attempts to use the tool
3. Agent rewrites the tool description to avoid failures
4. Test dozens of times to find nuances and bugs

**Result:** 40% decrease in task completion time for future agents.

#### 6. Start Wide, Then Narrow Down

Search strategy should mirror expert human research:
- Explore the landscape before drilling into specifics
- Start with short, broad queries
- Evaluate what's available
- Progressively narrow focus

**Common failure:** Agents default to overly long, specific queries that return few results.

#### 7. Guide the Thinking Process

Extended thinking mode serves as controllable scratchpad:
- Lead agent uses thinking to plan approach
- Assesses which tools fit the task
- Determines query complexity and subagent count
- Defines each subagent's role

**Subagents:** Use interleaved thinking after tool results to evaluate quality, identify gaps, and refine next query.

#### 8. Parallel Tool Calling

Two kinds of parallelization:
1. Lead agent spins up 3-5 subagents in parallel
2. Subagents use 3+ tools in parallel

**Result:** Cut research time by up to 90% for complex queries.

### Evaluation Strategies

#### Start Small, Iterate Fast

In early development, changes have dramatic impacts. A prompt tweak might boost success from 30% to 80%.

**Start with ~20 queries representing real usage patterns.** Don't delay creating evals - small-scale testing right away beats waiting for large evals.

#### LLM-as-Judge

For free-form research outputs, LLM judges work well. Use a single prompt outputting scores 0.0-1.0 and pass/fail:

**Evaluation criteria:**
- Factual accuracy (do claims match sources?)
- Citation accuracy (do cited sources match claims?)
- Completeness (all requested aspects covered?)
- Source quality (primary sources over lower-quality secondary?)
- Tool efficiency (right tools, reasonable number of times?)

**Most effective when test cases have clear answers.**

#### Human Evaluation

People catch edge cases automation misses:
- Hallucinated answers on unusual queries
- System failures
- Subtle source selection biases (e.g., SEO-optimized content farms over authoritative academic PDFs)

### Production Engineering Challenges

#### Agents Are Stateful and Errors Compound

Agents run for long periods, maintaining state across many tool calls. Without mitigations, minor system failures are catastrophic.

**Solutions:**
- Build systems that resume from where errors occurred (not restart from beginning)
- Let agents know when tools are failing and let them adapt
- Combine AI adaptability with deterministic safeguards (retry logic, regular checkpoints)

#### Debugging Agents

Agents are non-deterministic between runs, even with identical prompts.

**Add full production tracing:** Monitor agent decision patterns and interaction structures (without monitoring individual conversation contents for privacy).

#### Deployment: Rainbow Deployments

Agent systems are highly stateful webs of prompts, tools, and execution logic running almost continuously. Updates may catch agents anywhere in their process.

**Rainbow deployments:** Gradually shift traffic from old to new versions while keeping both running simultaneously. Avoid disrupting running agents.

#### Synchronous vs Asynchronous Execution

Current: Lead agents execute subagents synchronously, creating bottlenecks:
- Lead agent can't steer subagents mid-task
- Subagents can't coordinate with each other
- Entire system blocked waiting for single subagent

**Future opportunity:** Asynchronous execution enables additional parallelism but adds coordination challenges.

### Architecture Pattern: Subagent Filesystem Output

Direct subagent outputs can bypass the main coordinator:

**Pattern:**
1. Subagents call tools to store work in external systems
2. Pass lightweight references back to coordinator
3. Coordinator retrieves stored context from memory when needed

**Benefits:**
- Prevents information loss during multi-stage processing
- Reduces token overhead from copying large outputs
- Works well for structured outputs (code, reports, data visualizations)

### Long-Horizon Conversation Management

For hundreds of turns:
- Agents summarize completed work phases
- Store essential information in external memory before new tasks
- Spawn fresh subagents with clean contexts when limits approach
- Retrieve stored context (research plan, key findings) from memory

### Key Takeaways

1. **Token usage drives performance** - 80% of variance explained by tokens alone
2. **Context isolation is primary benefit** - Each agent gets fresh context for deep work
3. **Prompt quality multiplies** - Investment pays dividends across all agent invocations
4. **Parallel execution is powerful** - Up to 90% time reduction
5. **Tool descriptions matter** - Have agents help write them (40% improvement)
6. **Scale effort to complexity** - Embed explicit guidelines
7. **Hybrid evals work best** - LLM-as-judge for speed, humans for edge cases
8. **Production is different** - Stateful systems need resume capability, rainbow deployments

### Resources

- [Anthropic's prompting cookbook](https://github.com/anthropics/anthropic-cookbook) - includes example prompts from Claude Research
- [Simon Willison's summary](https://simonwillison.net/2025/Jun/14/multi-agent-research-system/)

---

## Why "Context Engineering" Over "Prompt Engineering"

*Source: https://simonwillison.net/2025/Jun/27/context-engineering/ (Simon Willison) - Added: 2026-01-18*

The term has gained traction as a better alternative to "prompt engineering."

**The problem with "prompt engineering":** Most people's inferred definition is that it's a laughably pretentious term for typing things into a chatbot.

**Why "context engineering" works better:** The inferred definition is much closer to the intended meaning - the complexity and artistry of filling the context window with relevant information for optimal LLM performance.

**Key advocates:**
- **Tobi Lutke** (Shopify CEO) - uses and promotes the term
- **Andrej Karpathy** - amplified its usage

**Key insight:** Inferred definitions are the ones that stick. Terminology matters for how seriously people take the discipline.

---

## Practical Lessons from 500M GPT Tokens

*Source: https://kenkantzer.com/lessons-after-a-half-billion-gpt-tokens/ (Ken Kantzer, CTO @ Truss) - Added: 2026-01-18*

Battle-tested insights from processing 500M+ tokens (85% GPT-4, 15% GPT-3.5) in a B2B context focused on summarize/analyze-extract tasks.

### Lesson 1: Less is More in Prompts

GPT gets confused when you over-specify. Unlike coding where everything must be explicit, prompting benefits from trusting GPT's general knowledge.

**Example failure:** Asking GPT to classify text to one of 50 US states using a JSON list of `{"locality": "Alabama", "locality_id": 1}` mappings. Worked 98% but failed enough to investigate.

**The fix:** Noticed GPT was correctly returning the full state name in another field without being asked. Switched to asking for the state name directly, then used simple string matching. "You obviously know the 50 states, GPT, so just give me the full name."

**Key insight:** Quality can *improve* when you're more vague - a marker of higher-order delegation/thinking.

**Side notes:**
- GPT failed most often with M states (Maryland, Maine, Massachusetts, Michigan) - expected from a stochastic model
- Prettified JSON with each item on its own line confused GPT less than comma-separated - `\n` is a stronger separator than `,`

### Lesson 2: You Don't Need LangChain

After millions of tokens and 3-4 diverse LLM features, their OpenAI service file has one 40-line function:

```python
def extract_json(prompt, variable_length_input, number_retries)
```

**What they actually use:**
- Just the chat API
- Always extract JSON
- No JSON mode, function calling, or assistants
- No system prompts even

**Token length estimation (works 99% of the time):**
```python
if s.length > model_context_size * 3:
    # truncate it!
```

**Retry logic for edge cases:**
```python
if response_error_code == "context_length_exceeded":
    s.truncate(model_context_size * 3 / 1.3)
```

**Key insight:** The power of a generalized model means less abstraction is needed. Avoid premature abstraction.

### Lesson 3: Variable-Speed Typing is UX Innovation

Thought it was a gimmick, but users react very positively to variable-speed "typed" characters. This feels like the mouse/cursor UX moment for AI.

### Lesson 4: GPT is Bad at Null Hypothesis

"Return nothing if you don't find anything" is the most error-prone prompting language.

**Problems:**
- GPT often hallucinates rather than returning nothing
- It also lacks confidence, returning blank too often

**Fun fact:** GPT loves to hallucinate bakeries:
- Sunshine Bakery
- Golden Grain Bakery
- Bliss Bakery

**Solution:** Don't send prompts when the input is empty. If "empty" is hard to define programmatically, you have a harder problem.

### Lesson 5: Context Windows Are Input-Heavy

GPT-4 has 128k token input but only 4k output. "Context window" is a misnomer.

**The real limit:** GPT struggles to return more than 10 items in a JSON array, even when well under the 4k output limit.

**Workaround:** Trade output for input - give it (prompt + task), ask for one result, then (prompt + task + result), ask for next. But now you're playing telephone with GPT.

### Lesson 6: Vector Databases/RAG Are Overrated for Most Use Cases

**RAG/embeddings are really meant for real search (Google/Bing scale), not "search-like" retrieval.**

**Three problems:**

1. **No relevancy cutoff** - Always risk poisoning retrieval with irrelevant results, or being too conservative
2. **Why separate your vectors from your data?** - Unless at Google/Bing scale, loss of context isn't worth the tradeoff
3. **Users don't want semantic guessing** - Domain experts in business apps know exactly what they want

**Better alternative:** Use a completion prompt to convert user search into faceted-search, a complex query, or even SQL. This is not RAG at all.

### Lesson 7: Hallucination Basically Doesn't Happen (With Full Context)

For "here's a block of text, extract something from it" tasks, GPT is extremely reliable.

**What GPT won't do:**
- Won't give you a random company if asked for company names in a block of text
- Won't hallucinate code - doesn't make up variables or introduce typos when rewriting code you sent it

**What GPT does hallucinate:**
- Standard library functions that don't exist (the null hypothesis problem - "I don't know" is hard)
- Information when given no text to work with

**Key insight:** Hallucination is about good data in, good GPT out. Product releases emphasizing "here's the full context, analyze/summarize/extract" work because this pattern is reliable.

### Q&A: Strategic Outlook

**Will we achieve AGI?**
No. Not with transformers + internet data + $XB infrastructure approach.

**Is GPT-4 useful or marketing hype?**
100% useful. This is early internet days. Won't fire everyone, but lowers the barrier to ML/AI that was previously only available to Google.

**Claude, Gemini, etc?**
Meh. Haven't done serious A/B testing, but doesn't feel close in day-to-day coding. The subtle things matter - like intuiting intention.

**How to keep up with LLM news?**
You don't need to. Per The Bitter Lesson, general model improvements outweigh niche improvements. All that matters is when GPT-5 comes out. Everything else is noise.

**GPT-5 predictions?**
Incremental improvement likely. GPT-3 to GPT-3.5 suggested hyper-linear improvement with training. But the reality is logarithmic - token speed and cost per token growing exponentially for incremental improvements.

**The economic reality:** Was willing to pay 20x for GPT-4 over GPT-3.5. Wouldn't pay 20x per token to go from GPT-4 to GPT-5 for current task sets. GPT-4 might be near the Pareto-optimal point.

**Bottom line:** GPT-5 may be the iPhone 5 to the iPhone 4 - not a loss, just maturation.
