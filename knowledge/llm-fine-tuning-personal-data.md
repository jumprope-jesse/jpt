# Fine-Tuning LLMs on Personal Chat Data

*Source: [Alexander Smirnov - Learnings from fine-tuning LLM on my Telegram messages](https://asmirnov.xyz/doppelganger) - Added: 2026-01-19*

Technical case study of fine-tuning Mistral 7B on 5 years of Telegram chat history to replicate writing style and conversational patterns.

---

## Approach Decision Tree

When building a personal LLM:

1. **Simple context loading** - Load messages into ChatGPT context
   - ❌ Limited by context window
   - ❌ Requires preprocessing to extract key points

2. **RAG (Retrieval Augmented Generation)**
   - ❌ Needs supervised fine-tuning of retrieval model for chat data
   - ❌ High effort for diverse conversational data

3. **Fine-tuning** ✓ Chosen approach
   - ✓ Captures writing style naturally
   - ✓ Accumulates knowledge from all messages
   - ✓ No need to select "important" content upfront

---

## Model Selection

### Base Model: Mistral 7B

Chosen from Hugging Face Open LLM Leaderboard as top small model (≤13B parameters), outperforming Llama 2 13B.

### Fine-Tuning Method

**LoRA vs Full Fine-Tuning considerations:**

Research on Llama instruction fine-tuning in Chinese (similar complexity to Russian chat):
- LoRA on base model < Full fine-tuning
- LoRA on instruction-tuned model ≈ Full fine-tuning

**Decision:** Try both approaches
1. Start with LoRA on Dolphin (English chat fine-tuned Mistral)
2. Fall back to full fine-tuning on base Mistral if quality insufficient

---

## Data Preparation

### Export & Processing

- **Source:** Telegram's built-in JSON export
- **Timeframe:** 5 years of chat history
- **Result:** 15,789 sessions from 466 chats, avg 8.51 messages/session

### Key Innovation: Preserving Conversational Flow

Unlike email, messaging apps have natural conversational patterns:
- Multiple messages from one person in a row
- Short messages
- Rapid back-and-forth shifts

**Structured as ChatML format:**

```
<|im_start|>John Smith
>>> damn, can't get around the 135 time limit
>>> trying to do everything super optimally, but no luck<|im_end|>

<|im_start|>Alexander Smirnov
>>> yeah same
>>> you still going with the same idea?<|im_end|>

<|im_start|>John Smith
>>> dunno, I think we're on the same page
>>> as you said
>>> going with the reversed string in a try and trying to find something there<|im_end|>
```

### Loss Calculation Strategy

**Key decision:** Calculate loss on ALL participants' responses, not just the author's.

**Rationale:**
- Model can role-play as the author OR as frequent conversational partners
- Predicting "who speaks next" is trivial and shouldn't dominate training
- Enables multi-persona capability

---

## LoRA Fine-Tuning

### Setup

- **Base:** Dolphin (Mistral fine-tuned for English chat)
- **Sequence length:** 1024
- **Batch size:** 8
- **Epochs:** 3
- **Duration:** 5.5 hours
- **Hardware:** RTX 3090 (20GB VRAM)
- **Cost:** $2 total ($0.362/hr on vast.ai)
- **Trainable params:** ~1% of total weights

### Results

**Strengths:**
- ✓ Captures writing style of different people
- ✓ Identifies common topics between specific pairs (e.g., work discussions with colleague)
- ✓ Appropriate subject matter matching

**Weaknesses:**
- ❌ Poor Russian grammar (model's non-native language)
- ❌ Loses conversational context quickly
- ❌ Would likely work well in English but struggles with Russian

---

## Full Fine-Tuning

### Setup

- **Method:** FSDP (Fully Sharded Data Parallel) - equivalent to ZeRO3
- **Precision:** Half-precision FSDP full shard
- **Sequence length:** 1024
- **Micro batch size:** 2
- **Epochs:** 3
- **Duration:** 20 minutes
- **Hardware:** 8x A100 80GB GPUs (63GB VRAM each)
- **Cost:** $3 total ($8.88/hr VM)

### Results

**Improvements over LoRA:**
- ✓ More engaging conversations
- ✓ Better Russian language performance (fewer errors)
- ✓ More natural dialogue flow

**Remaining issues:**
- ⚠️ Still loses context in longer conversations
- ⚠️ Russian errors still occur (not perfect)

### Incremental Improvement Assessment

"I wouldn't say it has turned out to be significantly better than LoRA."

**Suggested optimizations:**
1. Pre-train on large Russian corpus before task-specific fine-tuning
2. Add common conversation partners' names as separate tokens
3. Focus on single person (calculate loss only on author's responses)

---

## Evaluation Methodology

### Test Protocol

**Conversational scenarios:**
1. Model role-plays as author, human acts as friend
2. Human acts as author, model role-plays as friend

**Starter prompts:** Always identical ("hey", "what's up?" in Russian)

**Cherry-picking caveat:** Many model responses were simple ("I'll call you later", "busy", "ok") which are naturally frequent but uninteresting for demonstration.

### Baseline: Generic Mistral

Before any training, tested Dolphin (conversation fine-tuned Mistral):

**Problems identified:**
- ❌ No awareness of conversation context
- ❌ Bland, generic replies lacking distinct style
- ❌ Poor Russian language capability
- ❌ Overly proactive (ends every sentence with questions)
- ❌ Doesn't match natural messaging patterns

---

## Key Findings

### What Works

1. **Style mimicry** - Model excels at capturing writing style
2. **Topic awareness** - Identifies common discussion themes between people
3. **Person-pair patterns** - Different conversational dynamics with different contacts

### What Doesn't Work

1. **Context retention** - Significant challenge in maintaining conversation context
2. **Non-native language** - Small models struggle with languages beyond their primary training
3. **Nuanced queries** - Can't handle "yo, so?" or "what are your plans for the weekend" without full context

### The Missing Piece: Rewind-style Context

Responding to messages requires more than chat history. A system like [Rewind](https://www.rewind.ai/) that captures all computer activity could provide necessary context for authentic responses.

---

## Cost Analysis

| Method | Hardware | Duration | Cost | Quality |
|--------|----------|----------|------|---------|
| LoRA | RTX 3090 | 5.5 hrs | $2 | Good style, poor grammar |
| Full fine-tuning | 8x A100 | 20 min | $3 | Better overall, still context issues |

Both approaches are remarkably affordable for personal experimentation.

---

## Implementation Resources

- **Code:** [GitHub repo](https://github.com/asmirnov/telegram-doppelganger) with replication instructions
- **Training logs:** Available on WandB
- **References:**
  - Stanford Alpaca fine-tuning code
  - Anton Bacaj's Mistral fine-tuning code

---

## Lessons for Personal LLM Fine-Tuning

1. **Data structure matters** - Preserve natural conversational flow in training data
2. **Multi-persona training** - Calculating loss on all participants enables role-play flexibility
3. **Language matters significantly** - Small models (<13B) struggle with non-primary languages
4. **Context is everything** - Fine-tuning captures style but can't infer missing context
5. **LoRA is cost-effective** - For $2 you can achieve 80% of full fine-tuning results
6. **Focus beats generalization** - Single-person focus likely better than multi-person
7. **Pre-training helps** - Domain-specific pre-training (e.g., Russian corpus) before fine-tuning would improve results

---

## Related

- `llm-sideloading-personality-models.md` - Conceptual framework for personality modeling
- `applied-llm-development.md` - General fine-tuning best practices
- `rag-maturity-levels.md` - When RAG is better than fine-tuning
