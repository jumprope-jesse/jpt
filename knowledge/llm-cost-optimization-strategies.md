# LLM Cost Optimization Strategies

*Source: [Jellypod - How I Reduced Our LLM Costs by Over 85%](https://jellypod.ai/blog/how-I-reduced-llm-costs) - Added: 2026-01-19*

Case study of reducing production LLM costs from GPT-4 to fine-tuned Mistral 7B while maintaining output quality.

---

## The Problem with AI Applications

Most AI applications are unreliable (90-99% success rate vs enterprise software's multiple nines). This forces architectural decisions that increase costs:

- Can't just "stuff everything into one API call with excellent prompt engineering and hope for the best"
- Need redundancy and proper error handling
- Non-deterministic nature requires thoughtful code design

**Key insight:** Treat AI as a specific tool, not a "magical universal function that doesn't fail."

---

## Architectural Principles

### 1. Minimize AI Interaction

Only use AI when absolutely necessary—specifically for "human-level" analysis of unstructured data.

### 2. Return Pointers, Not Data

Force LLMs to return references to information (identifiers, pointers) instead of raw data:
- Ensures data integrity
- Reduces output tokens consumed
- Enables verification and error handling

### 3. Smallest Unit of Work

Design prompts for the smallest discrete task the AI needs to perform. This enables:
- Confident model swapping
- Better error isolation
- Predictable outputs

---

## Case Study: Jellypod

**Product:** Newsletter aggregation → daily podcast summary

### Initial Architecture (MVP)
- Process each email individually
- Summarize and convert to speech
- Stitch audio together

**Problem:** Duplicate coverage when multiple newsletters discussed same topic.

### Failed Approach
Stuffing all newsletter content into one big GPT-4 call:
- Couldn't guarantee consistent detection of important topics
- Couldn't reliably merge similar sections
- Couldn't maintain consistent ~10 minute podcast length

### Successful Architecture
Semantic chunking with similarity detection to merge related topics across sources.

**Cost problem:** O(n log n) API calls, where n = number of input chunks from all newsletters.

---

## Cost Reduction Solution

### Tool: OpenPipe

[OpenPipe](https://openpipe.ai/) - Fine-tuning platform (YC-backed)

**Process:**
1. Swap OpenAI SDK with OpenPipe SDK (drop-in replacement)
2. All calls pass through to OpenAI but inputs/outputs are recorded
3. Creates unique datasets for each prompt
4. One-click fine-tuning of open-source models

### Results

| Metric | GPT-4 | Fine-tuned Mistral 7B | Reduction |
|--------|-------|----------------------|-----------|
| Input tokens | $10/1M | $1.20/1M | 88% |
| Output tokens | $30/1M | $1.60/1M | 95% |

**Quality verification:**
- Series of evals
- In-app customer feedback
- Output quality matched GPT-4

---

## Implementation Recipe

1. **Build with GPT-4 first** - Get system working correctly
2. **Instrument with OpenPipe** - Record all inputs/outputs
3. **Collect sufficient data** - ~50,000 rows over ~1 week
4. **Fine-tune per prompt** - Separate model for each distinct LLM call type
5. **Swap and verify** - Replace GPT-4 with fine-tuned models, run evals

---

## Key Questions for AI Architecture

Before building, ask:

1. **Reliability:** What happens if the LLM doesn't answer correctly?
2. **Data handling:** Can the model return identifiers instead of raw data?
3. **Model flexibility:** Can GPT-4 be swapped with a cheaper, fine-tuned model?

---

## Related

- `llm-fine-tuning-personal-data.md` - Fine-tuning Mistral on chat data (similar model, different use case)
- `llm-eval-systems.md` - Evaluation methods for verifying fine-tuned model quality
