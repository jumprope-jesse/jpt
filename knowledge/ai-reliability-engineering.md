# Building Reliable AI Systems from Unreliable Agents

Practical guide to shipping reliable AI products despite LLM unreliability.

*Source: https://www.rainforestqa.com/blog/building-reliable-systems-out-of-unreliable-agents (Rainforest QA) - Added: 2026-01-18*

---

## The Core Problem

AI makes great demos but questionable products. After getting uncannily correct answers at first, you get burned on reliability with wild outputs and decide you can't make anything useful.

**The insight:** Even though AI agents aren't reliable, it's possible to build reliable systems out of them.

---

## The Process (High-Level)

1. Write simple prompts to solve your problem
2. Build an eval system for principled prompt engineering
3. Deploy with good observability, gather examples, improve evals
4. Invest in RAG (Retrieval-Augmented Generation)
5. Fine-tune using gathered data
6. **Breakthrough:** Use complementary agents

---

## Step 1: Start with Simple Prompts

The naive "ask a simple question" approach often works well enough to give hope, but starts falling down when you need reliability.

**The problem:** Best LLMs are amazing generalists but not good specialists. You need specialists to solve business problems - enough general knowledge to not be tedious, but knowing how to handle gray areas.

### Example: Getting Ingredients List

Naive prompt returns correct information plus unwanted commentary (knife hygiene lectures). Refined prompts get closer but still have inconsistencies (key capitalization, value formatting varies across runs).

**Lesson:** Even with `temperature=0.0`, you won't get perfect reproducibility, but it's the best place to start.

### Minimum Necessary Product Integration

Integrate minimally with your product to start building infrastructure, knowing results won't be great yet.

**Cheat codes:**
- Skip strongly-typed inputs with mypy - plain dictionaries are easier for building messages
- Set `temperature=0.0` for reliability
- Start without `instructor` for flexibility, bring it in later once you're confident in data shape

---

## Step 2: Eval System for Prompt Engineering

**Definition:** Prompt engineering = "iterative improvement of a prompt based on measurable success criteria"

Key phrases: **iterative** and **measurable success criteria**. You need a way to determine if an answer is correct, then measure correctness across examples to compare over time.

### Create an Evaluation Loop

Make the loop as fast as possible for effective iteration.

### Handling Multiple Correct Answers

Unlike traditional testing, any given question might have multiple correct answers.

| Situation | Solution |
|-----------|----------|
| Deterministic transformations possible | Normalize output before comparing (e.g., fix capitalization) |
| Heuristics available | String matching for required elements (e.g., "these words must appear") |
| Structured output expected | Validate against schema, retry on errors |
| True Inception scenario | Use smaller, cheaper LLM to evaluate bigger LLM outputs |
| Must execute to verify | Run full instructions (e.g., Playwright) and check final state |

**Trade-off for LLM-as-judge:** Introduces some flakiness into test suite.

### Building Your Validation Set

Once you have the eval loop, build example inputs and expected outputs. Aim for a single metric like "% prompts answered correctly" or precision/recall.

### Prompt Engineering Tricks

| Trick | Description |
|-------|-------------|
| Full context | Provide all context you'd give an intelligent human unfamiliar with nuances |
| Chain-of-thought | Ask agent to think step-by-step before providing actual answer |
| Few-shot prompting | Include examples of questions and answers in prompt |
| Bribes/threats | Tell agent something bad will happen if it answers incorrectly (results vary) |

**Chain-of-thought gotcha:** If using tool-calling API, naive `chain_of_thought` field comes *after* function name selection, defeating the purpose. Solution: Ask agent to output JSON that wraps the function spec, putting reasoning first.

```json
{
    "chain_of_thought": "Reasoning goes here first",
    "function_name": "scoop_out" | "spread",
    "function_args": { ... }
}
```

**Trade-off:** Chain-of-thought has speed/cost vs. accuracy trade-off.

---

## Step 3: Deploy with Observability

Ship as alpha-quality product as soon as you can to get real user data and feedback. Be open about robustness level.

**Cannot overstate:** Real user feedback is absolutely necessary. You'll hit diminishing returns without it.

### Observability Requirements

Log all LLM input/output pairs so you can:
1. Look at them and learn what users need
2. Label them manually to build up eval set

**Their approach:** JSON files in S3 with web interface to view and label. Not as many bells and whistles as off-the-shelf options, but enough.

---

## Step 4: Invest in RAG

When prompt engineering plateaus, try RAG - runtime prompt engineering where you dynamically add relevant things to prompts before asking.

### Example: Web Search RAG

Answering questions about recent events by running web search and including relevant articles in prompt.

### Example: Historical Data RAG

Rainforest has 10+ years of human testers executing English testing prompts. They tell the agent: "most human testers executing similar tasks clicked on button X and then typed Y into field Z."

### RAG Trade-offs

| Consideration | Notes |
|--------------|-------|
| Complexity | Real trade-off - use external providers, roll your own, or hybrid |
| Embedding choice | Didn't evaluate alternatives - used OpenAI embeddings |
| Result count | Only find top-3 related samples currently |
| Data richness | Get limited details from each sample |

**Their stack:** BigQuery for data extraction, OpenAI for embeddings, Pinecone for storage and nearest-neighbor search.

---

## Step 5: Fine-Tuning (Maybe)

If you've exhausted RAG possibilities, consider fine-tuning. But beware - conflicting opinions on merits vs. effort.

**Current state:**
- OpenAI only allows fine-tuning older models
- Anthropic promising availability with caveats
- Self-hosted fine-tuning is whole different expertise area

**Advice:** Wait a few months unless you've tried everything else. They haven't had to do this yet because earlier steps haven't been exhausted.

---

## Step 6: Complementary Agents (Breakthrough)

The principle: it's possible to build systems of complementary agents that work much more reliably than a single agent.

**The analogy:** "Pioneers, settlers, and city planners" - different people thrive in different situations. Rare for single person to have both grand vision AND precise execution ability.

### The Pattern: Planner + Verifier

Instead of whack-a-mole prompt fixing, create teams where agents complement each other.

**Example conversation:**

```
Planner: OK, we need to make a PB&J sandwich! Get peanut butter, jelly, bread,
         plate, and knife.

Verifier: Cool, sounds good.

Planner: Now take the peanut butter and spread it on the bread.

Verifier: (noticing no slice of bread visible) Wait, I can't see the bread -
          you can't spread on it because it's not there.

Planner: Ah, we need to take the slice of bread out first and put it on plate.

Verifier: Yep, that seems reasonable, let's do it.
```

### Implementation: QA Testing Agents

**Planner agent:**
- Knows the overall goal
- Creative, finds non-obvious paths to goals
- Uses search if button isn't on current page
- Sometimes too optimistic

**Verifier agent:**
- Doesn't know overall goal
- Only looks at immediate situation
- Corrects planner when concrete tasks aren't possible
- Example: Points out "Pay now" button is below the fold, not visible

**Why "complementary" over "ensemble":** Highlights that agents are meaningfully different and support each other in ways identical agents couldn't.

---

## Key Takeaways

1. **Iterative process** - Can't design and build in single try. Build, use, notice flaws, improve, release, repeat.

2. **Don't optimize single metric too much** - They still rely on "vibe checks" when evaluating prompts. Counting passing examples might not be enough if some are more important.

3. **Step-by-step complexity increase** - Start with naive prompting, add complexity only when needed. Getting through first four steps handles most problems.

4. **User feedback is essential** - Tempting to perfect before release, but impossible without real usage data.

5. **Complementary agents work** - Often very difficult to make single agent do the right thing, but detecting wrong thing so you can retry tends to be easier.

---

## What's Next (Rainforest's Roadmap)

- Continue monitoring usage and finding edge cases
- Experiment with alternative models, providers, ways of work
- Intrigued by Anthropic's latest models (what can Haiku do with vision?)
- Deeply intrigued by DSPy ideas
- Suspect unrealized wins in prompt structure

---

## Related

- `context-engineering-agents.md` - Managing context windows effectively
- `ai-agent-architecture.md` - Various agent architecture patterns
- DSPy - Framework for programming LLMs mentioned as area of interest
