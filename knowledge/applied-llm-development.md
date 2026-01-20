# Applied LLM Development: Lessons from Production

*Source: [Applied LLMs - What We've Learned From A Year of Building with LLMs](https://applied-llms.org/) - Added: 2026-01-18*

Comprehensive guide to building effective LLM applications, organized into tactical (practitioners), operational (product leaders), and strategic (founders/executives) tiers.

---

## Tactical: Core Practices

### Prompting Fundamentals

**Start with proven techniques, not novel approaches:**
- **N-shot examples**: Aim for n ≥ 5 examples
- **Chain-of-thought**: Explicit reasoning steps improve output
- **Structured I/O**: Define clear input/output formats

**Key principle:** "Small prompts that do one thing, and only one thing, well." Decompose complex tasks into focused sub-prompts rather than creating sprawling God Objects.

### RAG Best Practices

RAG quality depends on three factors:
1. **Document relevance** - Are you retrieving the right content?
2. **Information density** - Is the content concise and useful?
3. **Detail level** - Appropriate granularity for the task?

**Critical insight:** Don't abandon keyword search (BM25) for embeddings alone. Hybrid approaches combining semantic matching with term-based retrieval work best.

RAG remains valuable even as context windows grow:
- Cost savings from targeted retrieval
- Better reasoning quality with focused context

### Workflow Optimization

Multi-step flows dramatically outperform single prompts.

**Prioritize deterministic planning over reactive agents:**
1. Generate explicit plans first
2. Then execute them reliably
3. Avoid fully autonomous agent loops for production systems

**Achieving diversity:** Adjust prompt elements beyond temperature:
- Shuffle example ordering
- Vary phrasing
- Use different example sets

### Evaluation & Monitoring

**Build assertion-based unit tests** from real production samples, not synthetic cases.

**LLM-as-Judge patterns:**
- Works well for pairwise comparisons
- Not a silver bullet for absolute scoring
- Simplify annotation tasks to binary decisions or pairwise comparisons for consistency

**The "intern test":** Could a college student succeed with the given context? If not, your prompt context is insufficient.

---

## Operational: Shipping at Scale

### Data Practices

**Monitor development-prod skew constantly:**
- Formatting differences between test and production
- Typos and semantic shifts
- Evolving user language patterns

**"Look at samples of LLM inputs and outputs every day"** to catch:
- Emerging failure modes
- Evolving user expectations
- Edge cases becoming common cases

### Model Management

| Practice | Why |
|----------|-----|
| Generate structured output | Easier downstream integration |
| Pin model versions | Avoid surprise behavior changes |
| Expect prompt migration work | Versions matter deeply |
| Use smallest capable model | Cost, latency, often better results with careful prompting |

### Product Design

**Involve designers early** - They reframe problems beyond aesthetics into user experience.

**Design for human-in-the-loop:**
- Users validate and correct suggestions
- Creates natural feedback loops
- Builds training data for improvement

**Ruthlessly prioritize requirements** - You cannot optimize everything simultaneously.

### Team Structure

Avoid the trap of "AI Engineering solves everything."

**Effective teams need:**
- Platform engineers (infrastructure, reliability)
- Domain experts (understand the problem space)
- ML engineers (when optimization requires it)
- AI engineers (prompting, integration)

**Sequencing matters:**
1. Build evaluation infrastructure BEFORE hiring ML specialists
2. Focus on process understanding BEFORE adopting tools
3. Define domain-specific needs BEFORE using generic evaluation platforms

---

## Strategic: Long-term Thinking

### No Custom Models Before PMF

Training from scratch almost never makes sense:
- Bloomberg's specialized model got outpaced by gpt-3.5-turbo within a year
- Capabilities improve faster than you can train

**Finetuning rules:**
1. Exhaust prompting approaches first
2. Prove necessity through production data
3. Only then consider finetuning

**Hosting progression:**
1. Start with inference APIs for speed
2. Prepare for self-hosting as requirements demand (privacy, control, scale)

### The System Beats the Model

Models will become commoditized. Your durable advantage lies in:
- **Evals** - Domain-specific quality measurement
- **Guardrails** - Safety and reliability systems
- **Caching** - Cost and latency optimization
- **Data flywheels** - Continuous improvement from usage

**"The model isn't the product, the system around it is."**

**Avoid building features many can now buy:**
- Text-to-SQL (commoditized)
- Documentation chatbots (commoditized)
- Generic summarization (commoditized)

**Specialize deeply** in specific domains rather than trying general solutions.

### Build Iteration Velocity

LLMOps should shorten feedback loops, not create process overhead.

**The data flywheel:**
1. Human evaluation identifies defects
2. Annotations improve models/prompts
3. Repeat continuously

**Complexity budget:**
1. Start with prompt engineering and evals
2. Only add complexity as proven necessary
3. Resist premature optimization

### Cost Trends Enable New Products

Model capabilities roughly double every ~6 months for fixed cost (inverse Moore's Law).

**Implications:**
- Applications economically infeasible today become viable in 1-2 years
- Build systems cognizant of this trajectory
- Avoid over-optimizing for current costs

Example: LLM-powered game NPCs - too expensive now, viable by 2027.

### Keep Humans Central

Rather than automating workflows entirely, design LLMs as **"centaur chess" partners** amplifying human capability.

**Why this works:**
- Reduces brittleness (humans catch edge cases)
- Maximizes productivity gains
- Builds user trust and adoption

**GitHub Copilot model:** Succeeds because it accelerates human developers, not replaces them.

---

## Summary Principles

1. **Ship simple prompts with solid evals**
2. **Iterate on systems, not models**
3. **Focus relentlessly on what differentiates your product**
4. **Build for human-AI collaboration, not full automation**
5. **Let the data flywheel drive improvement**

---

## Production Insights: 500M Token Lessons

*Source: [Ken Kantzer](https://kenkantzer.com/lessons-after-a-half-billion-gpt-tokens/) - B2B summarize/extract use case*

### Less is More in Prompting

GPT gets confused when you over-specify things it already knows. Counter-intuitive: **vague prompts can produce better results** for common knowledge tasks.

**Bad approach:**
```
Return locality_id using this list:
[{"locality": "Alabama", "locality_id": 1}, ...]
```

**Better approach:**
```
Give me the full name of the US state this pertains to
```

Let GPT use its internal knowledge rather than forcing it through explicit mappings.

**Formatting tip:** Prettified JSON with newlines works better than comma-separated lists. `\n` is a stronger separator than `,`.

### You Don't Need LangChain

A 40-line OpenAI wrapper handles most production needs:
- Just use chat completions API
- Always extract JSON
- Don't need: JSON mode, function calling, assistants, system prompts
- Auto-truncate: `if length > context_size * 3` then truncate

**Key insight:** Powerful generalized models reduce the need for complex abstractions.

### Null Hypothesis Problem

"Return nothing if you don't find anything" is the most error-prone prompt pattern. GPT will:
- Hallucinate rather than return nothing
- Lack confidence and return blank when it shouldn't

**Solution:** Don't call GPT at all if there's no input. Handle "empty" cases programmatically before invoking the model.

**Fun fact:** When hallucinating businesses, GPT loves bakeries (Sunshine Bakery, Golden Grain Bakery, Bliss Bakery).

### Context Window Reality

- GPT-4's 128k input window has only 4k **output** limit
- Getting more than 10 JSON objects back is unreliable
- Hitting 10 items with ~800 tokens and GPT just stops

### RAG/Embeddings Are Overrated

For most business apps, RAG has fundamental issues:
1. **No relevancy cutoff** - Risk poisoning context with irrelevant results
2. **Data isolation** - Vectors in separate DB lose relational context
3. **Users are experts** - Domain users know what they want; semantic guessing annoys them

**Better approach:** Use LLM to convert search queries into faceted search or SQL.

### Hallucination is Rare (with context)

For extraction tasks ("here's text, extract X"), hallucination basically doesn't happen. GPT won't:
- Make up company names that aren't in the text
- Invent variables in code
- Introduce typos when rewriting code

The issue is the null hypothesis: GPT doesn't know how to say "I don't know."

**Rule:** Good data in → reliable GPT responses out.

### Bitter Lesson for LLM Users

General improvements to model performance outweigh niche improvements. Implication: **Only track when GPT-5 is coming out.** Everything else OpenAI releases in the meantime is mostly noise.

### Variable-Speed Typing UX

Streaming API with variable-speed character output is a genuine UX innovation - feels like the mouse/cursor moment for AI interfaces.

---

## LLM Memory Management: Zep

*Source: [Zep v0.17 Blog](https://blog.getzep.com/zep-v0-17/) - Added: 2026-01-18*

Zep provides long-term memory for LLM applications by persisting and searching chat histories.

### Core Problem

Vector similarity search has poor results when chat messages are short or lack context. A single "yes" answer to a question contains important information but won't match search queries well.

### Solution: Summary Search

Zep periodically generates summaries from chat histories. Instead of searching individual messages, search over summaries:
- Summaries are distillations of conversations
- More likely to match queries
- Provide richer, more succinct context

```python
# Search summaries instead of messages
search_payload = MemorySearchPayload(
    text=search_text,
    search_scope="summary"  # vs "messages"
)
```

### MMR Re-Ranking

Maximum Marginal Relevance addresses the problem of successive summaries containing similar content:
- Standard similarity returns highest matches but with little diversity
- MMR re-ranks to ensure both relevance AND diversity
- Each summary in the prompt offers additional information to the LLM

### Named Entity Enrichment

Summaries are enriched with named entities for filtered searches:

```javascript
const searchPayload = new MemorySearchPayload({
   metadata: {
      where: {
         and: [
            { jsonpath: '$.system.entities[*] ? (@.Label == "WORK_OF_ART")' },
            { jsonpath: '$.system.entities[*] ? (@.Name like_regex "^parable*" flag "i")' },
         ],
      },
   },
   text: searchText,
});
```

### Architecture

- Stateless service design for easy scale-out
- Background operations via message queue in Postgres
- Deploy multiple Zep instances as needed

### When to Use Zep

Good fit for:
- Conversation-heavy applications (chatbots, assistants)
- Apps needing long-term context across sessions
- When individual message search is too granular

Not needed for:
- Single-turn Q&A applications
- Document-only RAG (use standard vector stores)

---

## Related

- `ai-agent-architecture.md` - Agent design patterns
- `ai-fluency-framework.md` - Broader AI adoption framework
- `context-engineering.md` - Context window optimization (if exists)
