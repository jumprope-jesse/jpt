# Code Completion AI Architecture

*Source: [The lifecycle of a code AI completion](https://sourcegraph.com/blog/the-lifecycle-of-a-code-ai-completion) - Sourcegraph/Cody, Added: 2026-01-18*

Deep dive into how production code completion systems work, from Sourcegraph's Cody. Covers the four-stage lifecycle: planning, retrieval, generation, and post-processing.

---

## The Four Stages of Code Completion

Every code completion goes through:

1. **Planning** - Analyze code context to categorize the request and optimize execution
2. **Retrieval** - Gather contextual information from the codebase (RAG)
3. **Generation** - Use an LLM to produce code completions
4. **Post-processing** - Refine the output to ensure relevance and quality

---

## Stage 1: Planning

Rule-based heuristics (no AI) that categorize the request before heavy processing. Like a database query planner.

### Single-line vs. Multi-line Detection

Use language heuristics (indentation, symbols) and Tree-sitter syntax parsing to determine:
- **Single-line**: User expects quick inline completion
- **Multi-line**: User willing to wait for full function implementation

Multi-line uses more complex models since users accept higher latency for better quality.

### Tree-sitter for Syntactic Triggers

Tree-sitter provides concrete syntax trees for each file:
- Extremely fast parsing
- Incremental (changes applied with low latency)
- Robust even with syntax errors (works on incomplete code)

**Use cases:**
- Detect if cursor is inside a comment
- Categorize into actions: implementing function body, writing docstring, method call
- Trigger different context retrieval strategies

### Suggestion Widget Interaction

VS Code's IntelliSense provides:
- Range of document being replaced
- Currently selected suggestion

Using the suggest widget to steer LLM results creates "magical" experiences - completions that work with what the user already sees.

---

## Stage 2: Retrieval (RAG)

Finding the right code examples has huge impact on completion quality. The constraint: retrieval happens before generation and is in the hot path.

### Editor Context Retrieval

Primary mechanism - look at what the developer is working on:
- Other open tabs
- Recently viewed files
- Same programming language files

**Sliding window Jaccard similarity:**
1. Take a few lines above cursor as "reference"
2. Slide a window over relevant files
3. Find best matches by Jaccard similarity

**Example:** When writing a class, retrieve the class implementation from another file as context.

### Context Ranking Challenges

Multiple context sources need ranking. Key insight: **adding irrelevant context can make response quality worse**.

Don't just throw everything at the model - curate what's actually helpful.

---

## Stage 3: Generation

### From Trivial to Production

Trivial implementation:
```
"Complete the following code: {prefix}"
```

Production problems with naive approach:
- **No Fill-in-the-Middle (FITM)**: LLM repeats code already in next line
- **High latency**: Many requests return empty (LLM terminates early)
- **Prompt sensitivity**: Slight variants have huge quality impact

### Latency Reduction Strategies

To get 75th percentile end-to-end latency from 1.8s to under 900ms:

| Strategy | Impact |
|----------|--------|
| Token limits | Reduce output size |
| Stop words | Early termination on delimiters |
| Streaming responses | User sees progress immediately |
| Keep-alive connections | Avoid TCP handshake overhead |
| Regional deployment | Reduce network latency |

### Use-Case Specific LLMs

General-purpose models (Claude Instant) are larger than needed for code completion.

**StarCoder benefits:**
- Built specifically for code completion
- Multiple size variants (7B, 14B, 32B parameters)
- Quantized versions with minimal quality loss
- Native FITM support

Result: Much reduced latencies + higher acceptance rates.

### The Model Portability Principle

Strength doesn't come from hyper-optimizing around one LLM. The field moves fast - the model you optimize for may be outdated in months.

Focus on:
- Relevant context retrieval
- Model-agnostic architecture
- Ability to swap models easily (including local inference via Ollama)

---

## Stage 4: Post-Processing

Salvage and refine LLM output to ensure relevance:

### Key Techniques

| Technique | Purpose |
|-----------|---------|
| **Syntax normalization** | Fix indentation, match document style |
| **Context overlap detection** | Prevent repeating code already in document |
| **Bracket completion** | Handle partial blocks correctly |
| **Truncation** | Cut at reasonable boundaries |

### The "Don't Filter Too Much" Principle

Filtering out too many completions makes users think the product doesn't work. Better to show a mediocre completion than nothing.

Focus effort on generating relevant completions rather than aggressive filtering.

---

## Metrics & Evaluation

### Key Metrics

| Metric | What It Measures |
|--------|------------------|
| **Suggestion latency** | Time from keystroke to completion visible |
| **Completion acceptance rate** | User accepts suggestion (primary metric) |
| **Completion retention** | User keeps suggestion after ~30s |
| **Perceived latency** | User experience of speed |

Acceptance rate combines latency and quality into a single number.

### Logging Sensitivity

Well-instrumented logging can detect:
- 50ms latency regressions within hours
- Provider-side performance issues
- Language-specific failure modes

### Syntax-Categorized Analysis

By attaching Tree-sitter syntax information to every event, you can identify which code positions work well vs. need improvement.

**Example finding:** Reduce completion frequency at positions where completions are known to be unhelpful (e.g., end of already-complete statements).

---

## Reliability Engineering

### Integration Test Pattern

Test the full autocomplete architecture by calling directly into the VS Code API:
1. Define document state
2. Define mock LLM responses
3. Assert on all steps in the pipeline

```typescript
// Pseudocode pattern
test('completes function body', async () => {
  const document = createDocument('function foo() {|}');
  const mockResponse = 'return 42;';
  const completion = await provideInlineCompletionItems(document, mockResponse);
  expect(completion).toContain('return 42');
});
```

### LLM Inference Test Suite

Static examples of document states to automatically test the autocomplete stack:
- Not just single-file tests - full workspace configurations
- Example: Write a class, then in another file write a unit test for that class
- Automated correctness tests run against generated completions

**Evolution:**
1. Started with manual evaluation via web UI
2. HumanEval-style tests for correctness
3. Full workspace simulation with automated testing

---

## Key Insights

### Context is Everything

The more relevant context provided to the AI, the better the completion quality. This includes:
- Current file prefix/suffix
- Related files the user has open
- Class implementations being used
- Project-specific patterns

### The RAG Retrieval Challenge

"New dev" analogy: What context would you give a new team member to help them write code at this position?

Automate extracting relevant context for the current problem. Modern LLMs know the language and common libraries - your job is filling in project-specific gaps.

### Latency is a Feature

End-to-end latency must be under 1 second, ideally much faster. Every millisecond matters because:
- Users type fast
- Completions that arrive late are useless
- Perceived slowness kills adoption

### Acceptance Rate Target

Cody's completion acceptance rate reaches as high as 30%. This is the north star metric combining all quality and latency factors.

---

## Architecture Pattern Summary

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   PLANNING  │────▶│  RETRIEVAL  │────▶│ GENERATION  │────▶│   POST-     │
│             │     │   (RAG)     │     │   (LLM)     │     │ PROCESSING  │
│ - Classify  │     │ - Editor    │     │ - Model     │     │ - Normalize │
│ - Syntax    │     │   context   │     │   selection │     │ - Dedupe    │
│   analyze   │     │ - Jaccard   │     │ - Streaming │     │ - Truncate  │
│ - Route     │     │   search    │     │ - FITM      │     │ - Validate  │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
```

---

## Supermaven's Architecture Innovations

*Source: [Introducing Supermaven](https://supermaven.com/blog/introducing-supermaven) - Feb 2024*

Supermaven (from TabNine creator) takes a different architectural approach to compete with larger players.

### 300,000-Token Context Window

Custom neural network architecture (not Transformer) achieves:
- 75x larger context than Copilot's 8,192 tokens
- Same cost/latency as 4,000-token Transformer
- Processes entire 50k-token repositories

**Key insight:** High serving costs of large models levels the playing field - everyone must use small models to remain profitable. The best product is the one using a small model most effectively.

### Edit Sequence Training

Unlike most tools that see code as a sequence of files, Supermaven is trained on **edit sequences** (like `git diff`):
- Better understanding of developer intent
- Excels at refactoring tasks
- Recognizes patterns in how code changes, not just static state

### Speed Optimization

Custom infrastructure for low latency with long prompts. In tests, significantly faster response times than competitors despite larger context windows.

### The "Idiosyncratic Codebase" Problem

Most common Copilot complaint: works great with well-known APIs (good training data coverage), struggles with large, unique codebases.

Supermaven's solution: Large enough context window to include project-specific APIs and conventions.

---

## Related

- `applied-llm-development.md` - Production LLM best practices
- `ai-agent-architecture.md` - Broader agent patterns
- `coding-agent-tools.md` - Development agent ecosystem
