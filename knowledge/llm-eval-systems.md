# Building Evaluation Systems for LLM Products

*Source: [Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/) by Hamel Husain - Added: 2026-01-18*

Comprehensive guide to building evaluation infrastructure for LLM-powered products. Key thesis: unsuccessful AI products almost always share a common root cause - failure to create robust evaluation systems.

---

## Core Principle: Iteration Speed = Success

Success with AI hinges on how fast you can iterate. You need processes for:
1. **Evaluating quality** (tests)
2. **Debugging issues** (logging & inspecting data)
3. **Changing behavior** (prompt eng, fine-tuning, code)

Most teams focus only on #3, which prevents improvement beyond demo stage. Streamlining evaluation makes everything else easy.

---

## Three Levels of Evaluation

Cost: Level 3 > Level 2 > Level 1. This dictates cadence.

### Level 1: Unit Tests (Assertions)

Fast, cheap assertions that run on every code change. Unlike typical unit tests, organize these for reuse in:
- Unit tests
- Data cleaning
- Automatic retries (using assertion errors to course-correct)

**Step 1: Write Scoped Tests**

Break down LLM scope into features and scenarios:

```
Feature: Listing Finder
- Scenario: Basic search (verify results returned)
- Scenario: Complex filters (verify filter accuracy)
- Scenario: Edge cases (verify graceful handling)
```

Example generic assertion (check no UUID exposed):
```javascript
const noExposedUUID = message => {
  const sanitizedComment = message.comment.replace(/\{\{.*?\}\}/g, '')
  const regexp = /[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/ig
  const matches = Array.from(sanitizedComment.matchAll(regexp))
  expect(matches.length).to.equal(0, 'Exposed UUIDs found')
}
```

**Step 2: Generate Test Cases**

Use LLMs to generate synthetic inputs:
```
Write 50 different instructions that a real estate agent can give
to his assistant to create contacts on his CRM. The contact details
can include name, phone, email, partner name, birthday, tags,
company, address and job.

For each instruction, generate a second instruction to look up
the created contact.
```

**Key insight:** Make tests as challenging as possible while representing real user interactions. A good signal: when the model struggles to pass them.

**Step 3: Track Results Over Time**

Use existing analytics (Metabase, etc.) to visualize test results. Track pass rates over time to measure progress.

**Note:** Unlike traditional tests, you don't need 100% pass rate. Pass rate is a product decision.

---

### Level 2: Human & Model Evaluation

Build solid Level 1 foundation first, then move to validation that can't be tested by assertions.

**Logging Traces**

A trace is a logical grouping of logs (user message -> AI response -> user message). Tools like LangSmith help but aren't required.

**Critical: Remove ALL Friction from Looking at Data**

Build domain-specific viewing tools that show everything on one screen:
- What tool/feature was being evaluated
- Whether trace was synthetic or real user input
- Filters by tool/scenario combinations
- Links to CRM, trace logs for current record

Build these with Gradio, Streamlit, Panel, or Shiny in less than a day.

**How Much Data to Look At?**

When starting: as much as possible. Read ALL test case traces and user-generated traces. You can never stop looking at data. Over time, you can sample more.

**Automated Evaluation with LLMs**

Track correlation between model-based and human evaluation. Use spreadsheets to iterate on alignment:

| Column | Purpose |
|--------|---------|
| model_response | LLM's prediction |
| model_critique | Critique from evaluator LLM |
| model_outcome | Binary good/bad label |
| human_critique | Human's critique |
| human_outcome | Human's binary label |
| human_desired_response | What human wanted |

**Model-based eval tips:**
- Use most powerful model you can afford (slower is OK for critiques)
- Treat it as a meta-problem requiring its own mini-evaluation system
- Continue periodic human-model agreement monitoring

---

### Level 3: A/B Testing

Only appropriate for mature products. Put this off until convinced your AI is suitable for real users. Not fundamentally different from A/B testing other products.

---

## Eval Systems Unlock Superpowers

### Fine-Tuning Data Generation

If you have a solid eval system, you already have a robust data generation and curation engine:

1. Use same prompts that generate test cases to generate fine-tuning data
2. Filter with Level 1 assertions
3. Filter with Level 2 critique model
4. Use human eval tools to curate traces

Fine-tuning is best for: syntax, style, rules
RAG is best for: context, up-to-date facts

### Debugging

Robust eval infrastructure provides:
- Searchable trace database
- Mechanisms to flag errors (assertions, tests)
- Log navigation to find root cause (RAG issue? Code bug? Model failure?)
- Ability to make changes and quickly test efficacy

---

## Case Study: Lucy (Real Estate AI Assistant)

Symptoms of plateau without good evals:
1. Addressing one failure mode caused others (whack-a-mole)
2. Limited visibility beyond vibe checks
3. Prompts expanded into unwieldy forms covering edge cases

Solution: Systematic evaluation-centered approach broke through the plateau.

---

## Key Takeaways

1. **Remove ALL friction from looking at data**
2. **Keep it simple** - Use existing tools first, not fancy LLM platforms
3. **You're doing it wrong if you aren't looking at lots of data**
4. **Create domain-specific evaluation** - Don't rely on generic frameworks
5. **Write lots of tests and frequently update them**
6. **Use LLMs to bootstrap eval systems** (generate test cases, critiques)
7. **Re-use eval infrastructure for debugging and fine-tuning**

---

## Related

- `applied-llm-development.md` - Broader LLM development practices
- `ai-agent-architecture.md` - Agent design patterns

---

## Tools & Libraries

### continuous-eval (Relari AI)

Open-source package for granular GenAI pipeline evaluation. [GitHub](https://github.com/relari-ai/continuous-eval)

**Install:** `pip install continuous-eval`

**Key differentiators:**
- Modularized evaluation with tailored metrics per pipeline stage
- Comprehensive metric library (deterministic, semantic, LLM-based)
- Ensemble evaluations combining metrics with user feedback
- Synthetic dataset generation for testing

**Built-in metrics:** PrecisionRecallF1, RankedRetrievalMetrics, DeterministicAnswerCorrectness, FleschKincaidReadability, plus custom metric support via `Metric` class extension.

**Pipeline evaluation pattern:**
```python
from continuous_eval.eval import Module, ModuleOutput, Pipeline, Dataset
from continuous_eval.metrics.retrieval import PrecisionRecallF1

retriever = Module(
    name="Retriever",
    input=dataset.question,
    output=List[str],
    eval=[PrecisionRecallF1().use(
        retrieved_context=ModuleOutput(),
        ground_truth_context=dataset.ground_truth_context,
    )],
)
```

Useful for RAG, code generation, classification pipelines. Apache 2.0 license.
