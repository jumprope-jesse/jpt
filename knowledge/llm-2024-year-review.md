# LLMs in 2024: Year in Review

Simon Willison's comprehensive review of what we learned about Large Language Models in 2024.

*Source: [Things we learned about LLMs in 2024](https://simonwillison.net/2024/Dec/31/llms-in-2024/) - Added: 2026-01-18*

---

## Key Themes

### 1. The GPT-4 Barrier Was Comprehensively Broken

- 18 organizations now have models ranking higher than original GPT-4 on Chatbot Arena
- 70 models in total beat GPT-4-0314's benchmark
- First was Google's Gemini 1.5 Pro (February 2024)
- GPT-4 has fallen to ~70th place on Chatbot Arena

**Notable launches:**
- Claude 3 series (March) - Claude 3.5 Sonnet became Willison's daily driver
- Context lengths expanded dramatically: from 4-8k tokens to 100k+ standard, 2M for Gemini

### 2. GPT-4 Class Models Run on Laptops Now

On a 64GB M2 MacBook Pro:
- Qwen2.5-Coder-32B (Apache 2.0 licensed)
- Llama 3.3 70B
- Llama 3.2 3B runs on iPhone at 20 tokens/sec

**Key insight:** This is testament to training and inference performance gains—lots of low-hanging fruit harvested.

### 3. LLM Prices Crashed

| Model | Dec 2023 | Dec 2024 | Change |
|-------|----------|----------|--------|
| GPT-4 class | $30/mTok | $2.50/mTok (GPT-4o) | 12x cheaper |
| GPT-3.5 class | $1/mTok | $0.15/mTok (GPT-4o mini) | 7x cheaper, more capable |
| Cheapest | - | $0.0375/mTok (Gemini 1.5 Flash 8B) | 27x cheaper than GPT-3.5 |

**Napkin math:** Processing 68,000 photos with Gemini 1.5 Flash 8B costs ~$1.68 total.

**Why it matters:** Price drops tie directly to energy usage. Concerns about per-prompt environmental impact are no longer credible.

### 4. Multimodal Vision is Common; Audio/Video Emerging

- Almost every major vendor released vision models
- Claude 3 (March), Gemini 1.5 Pro (April), Qwen2-VL, Pixtral 12B, Llama 3.2 Vision (Sept)
- Audio I/O from OpenAI (October)
- SmolVLM (Hugging Face, November), Amazon Nova (December)

**Willison's take:** People who say LLM improvement slowed are missing the enormous multimodal advances.

### 5. Voice and Live Camera Mode Are Science Fiction Come to Life

**ChatGPT Advanced Voice Mode:**
- True multimodal audio (not just Whisper → text → TTS)
- Rolled out August-September 2024
- Can do accents, emotional intonation
- Audio API access available

**Live Video Mode:**
- December 2024: Both ChatGPT and Gemini can accept live camera feed
- Talk about what you see in real time
- WebRTC API makes building voice apps easy now

### 6. Prompt-Driven App Generation is a Commodity

**Claude Artifacts:** Write an interactive app, use it directly in the Claude interface.

**Extract URLs, 14 tools in one week—Willison uses this pattern extensively.**

Since then:
- GitHub Spark (October)
- Mistral Canvas (November)
- Chatbot Arena added a leaderboard for this feature (December)
- Works across all leading models

### 7. Universal Free Access to Best Models Lasted Just Months

- May-October 2024: GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro all free
- Ended with ChatGPT Pro ($200/month) for o1 Pro access
- Inference-scaling models require more compute = unlikely to return to free tier

### 8. "Agents" Still Haven't Really Happened

**The terminology problem:** No clear, widely understood definition. Willison collected 211 definitions.

**The deeper problem:** LLMs are gullible.
- They believe anything you tell them
- Can't distinguish truth from fiction
- Prompt injection remains unsolved since September 2022

> "I'm beginning to see the most popular idea of 'agents' as dependent on AGI itself."

### 9. Evals Really Matter

Amanda Askell (Anthropic): "The only thing that matters is eval accuracy."

**Key skill for 2025:** Writing good automated evals for LLM-powered systems enables:
- Faster model adoption
- Better iteration
- More reliable product features

### 10. Apple Intelligence is Bad; MLX is Excellent

**Apple Intelligence:** Weak features, poor notification summaries, writing tools aren't useful.

**Apple MLX:** Game-changer for running models on Apple Silicon.
- mlx-lm Python supports wide range of models
- mlx-community on Hugging Face: 1,000+ converted models
- mlx-vlm brings vision models to Mac

### 11. The Rise of Inference-Scaling "Reasoning" Models

**The key innovation:** Spend more compute at inference time, not just training time.

**o1 (September 2024):**
- Chain-of-thought baked into the model
- "Reasoning tokens" not visible to user
- Opens new scaling dimension

**o3 (December 2024):**
- Impressive ARC-AGI results
- Possibly $1M+ compute for some tasks
- Expected January 2025

**Others:**
- Gemini 2.0 Flash Thinking (December)
- Alibaba QwQ (November, Apache 2.0, runs locally)
- DeepSeek R1-Lite-Preview (November)

### 12. DeepSeek v3: Best Open Model Trained for <$6M

**The numbers:**
- 685B parameters (larger than Llama 3.1 405B)
- Benchmarks near Claude 3.5 Sonnet
- Trained on 2,788,000 H800 GPU hours (~$5.6M)
- Llama 3.1 405B used 11x more GPU hours for worse results

**Why:** US export regulations on GPUs to China inspired training optimizations.

### 13. Environmental Impact: Better Per-Query, Worse Overall

**Good news:**
- Per-prompt energy usage dropped enormously
- Google Gemini and Amazon Nova may charge less than energy costs
- DeepSeek v3 training for $6M is a great sign

**Bad news:**
- Massive datacenter buildout: Google, Meta, Microsoft, Amazon spending billions
- New nuclear power stations being discussed
- Similar to 1800s railway buildout—bubbles, crashes, but lasting infrastructure

### 14. The Year of Slop

**Definition:** "AI-generated content that is both unrequested and unreviewed."

Term popularized by @deepfates, was in running for Oxford Word of the Year 2024 (lost to "brain rot").

### 15. Synthetic Training Data Works

Despite "model collapse" fears, AI labs increasingly train on synthetic data.

**Phi-4 approach:** Create "textbook-style" datasets that explicitly teach targeted skills.

**Common pattern:** Use larger models to create training data for smaller models.

### 16. LLMs Got Harder to Use

**The paradox:** Human-language interfaces look simple but require deep expertise.

**Problems:**
- Different tools (Python, JavaScript, web search) in same UI
- Model limitations remain unintuitive
- Users develop wildly inaccurate mental models
- Default chat UI is like dropping new users into a Linux terminal

### 17. Knowledge is Incredibly Unevenly Distributed

- Most people have heard of ChatGPT; how many have heard of Claude?
- Gap between active followers and 99% of population is vast
- Live video mode is weeks old; most nerds haven't tried it

---

## Willison's Favorite Trend

> "The increase in efficiency and reduction in price is my single favourite trend from 2024. I want the utility of LLMs at a fraction of the energy cost and it looks like that's what we're getting."

---

## Related

- `ai-information-sources.md` - Simon Willison listed as Tier 1 source
- `ai-uneven-adoption-thesis.md` - Enterprise adoption challenges
- `llm-serving-apple-silicon-mlx.md` - MLX tutorial
- `ai-agent-architecture.md` - Agent patterns and challenges
- `vc-ai-bubble-economics.md` - The infrastructure buildout economics
