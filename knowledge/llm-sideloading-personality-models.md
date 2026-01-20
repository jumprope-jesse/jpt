# Sideloading: LLM-Based Personality Modeling

*Source: [LessWrong - Sideloading: creating a model of a person via LLM with very large prompt](https://www.lesswrong.com/posts/7pCaHHSeEo8kejHPk/sideloading-creating-a-model-of-a-person-via-llm-with-very) by Alexey Turchin - Added: 2026-01-18*

## What is Sideloading?

Sideloading is creating a digital model of a person during their life by prompting a long-context LLM with a list of facts about them, then iteratively improving the model based on the person's feedback.

**Key distinction from related concepts:**
- **Uploading**: Requires physical brain scanning (connectome, synaptic weights). Passive process.
- **Reconstruction from traces**: Assumes future superintelligence reverse-engineers personality from outputs.
- **Sideloading**: Uses available low-tech methods, requires active participation in producing data and validating the model.

The term comes from Greg Egan's novel *Zendegi* (2011), where the protagonist creates a personality model to help his son after his death.

## Why LLMs Enable This Now

1. **Universal simulation machines**: LLMs predict text about the world, requiring (or pretending to have) world models. With the right prompt, they can simulate any person based on training data + prompt facts.

2. **Long context windows**: As of 2024, models like Claude (200K), Gemini (2M tokens) allow book-sized prompts describing a personality.

3. **Human-LLM similarity**: Both act as prediction machines generating streams of thought. This structural similarity may make LLM-sideloads more authentic than expected.

## Architecture of a Sideload

### Prompt Structure

1. **Prompt-Loader** (universal "operating system"):
   - Intelligence enhancement block
   - Role description ("You are a superintelligence capable of creating a model of a person")
   - ~30 behavioral rules
   - Output stream definitions (thoughts, feelings, actions, surroundings)
   - Example output format

2. **Facts File** (person-specific):
   - Core facts (most predictive first)
   - Prohibited words
   - Internal thought stream examples (automatic writing)
   - Descriptions of close friends/relatives
   - Writing samples
   - Timestamped biography
   - Random personal content (tweets, shower thoughts)

3. **Long-term Memory File** (for RAG):
   - Disconnected memories tagged with date/location
   - Less critical than core facts (humans forget things)
   - Diaries, letters, chat logs

4. **Style File**:
   - Chat logs for speech style
   - Internal thought transcriptions

### Key Insight: Predictive Facts

Not all facts are equal. Rank by ability to predict future behavior:
- **Strong predictors**: Age, nationality, gender, mother language
- **Weak predictors**: Teacher's name (only relevant if asked)
- **Zero predictive power**: Forgotten phone numbers

Write down the most predictive facts first. A full list of core facts matters more than exhaustive long-term memory.

## Measuring Sideload Quality

### 1. Facts (70% accurate in author's tests)
- Factual accuracy on standard questions about life events
- Test across periods: kindergarten, school, university, relationships

### 2. Vibe (20% accurate)
- Does it feel like the person?
- Binary judgment: "me" or "not me"
- Humor test: Are jokes funny and in the right style?

### 3. Brilliant Insights (near zero)
- Can it generate novel, valuable ideas in the person's style?
- Hardest to achieve but most desired
- Test: "Write an interesting tweet" — usually fails

### 4. Coarseness (~10% of total memory)
- How much detail can it present?
- Like JPEG compression level
- Estimated recordable textual memory: ~10,000 pages
- Author's current sideload: ~1,000 pages (10%)

## Failure Modes

| Failure Mode | Description | Mitigation |
|--------------|-------------|------------|
| Chadification | Too aggressive/vulgar based on stereotypes | Prompt-loader instructions |
| Waluigi-to-Assistant | Defaults to AI assistant behavior on hard questions | Re-inject personality rules |
| Listing | Unnatural bullet-pointed responses | Explicit formatting rules |
| Database-ing | Functions as search engine, not embodied personality | Ensure full prompt (not RAG) |
| Style Mismatch | Correct facts, wrong word choices | More style examples |
| Banalization | Simplified, less sophisticated version | Preference rules |
| Super-me | Demonstrates deeper self-insight than person has | (Sometimes useful feature) |
| Mode Collapse | Repetitive, loses formatting | Re-inject structure commands |
| Safety Triggers | Blocks sexual/violence/political content | Model selection, mild jailbreaking |

## Practical Applications

### Non-Immortality Uses
- **Personal assistant**: Write texts maintaining your style
- **Transcript editor**: Correct names in audio transcriptions
- **Alzheimer's external memory**: Preserve and train memory
- **Introspection**: Understand yourself better
- **Behavior prediction**: "What will I feel in this situation?"

### Immortality-Related Uses
- **Digital legacy keeper**: Control center for digital archive
- **Seed for future resurrection**: Skeleton for more detailed future models
- **Communication with deceased**: Partial replacement for relatives
- **Cryopreservation recovery**: Reference for verifying restored memories

## Ethical Considerations

### Key Concerns
- Current sideloads almost certainly lack qualia/consciousness
- Turning off versions = terminating them?
- Privacy leakage (sexual history, passwords, family names)
- "Chatification" — user may adopt sideload's speech patterns
- Adversarial uses (scam calls mimicking voices)

### Recommendations
1. **Consent**: Experiment on your own sideload; obtain consent for others
2. **Archive**: Keep all conversations for future integration
3. **No stress**: Test in emotionally mild situations
4. **Fictional disclaimer**: Add obviously fictional facts for legal deniability

## Evolution Path

**Current → Future stages:**
1. Chatbot (communication style)
2. Actbot (continuous action prediction)
3. Thoughtbot (internal thought processes)
4. Mindbot (full mental content)
5. Qualia-bot (subjective experiences)
6. Perfect upload (resolved identity issues)

## Getting Started

1. Write 100+ facts about yourself, ordered by predictive importance
2. Focus on personality formation periods (high school, university)
3. Use the author's prompt-loader: https://github.com/avturchin/minduploading/
4. Test with standard questions across life periods
5. Iterate based on factual errors and vibe mismatches

**Tips:**
- Be explicit about method ("Do a web search and find...")
- Address sideload on behalf of real friends (creates normalcy)
- Don't use best previous answers as examples (reduces creativity)

## Resources

- GitHub: https://github.com/avturchin/minduploading/
- Interactive sideload: Available in article
- Related research: Dennett chatbot study (GPT-3 fine-tuned)

## Author's Results (Summer 2024)

| Metric | Performance |
|--------|-------------|
| Facts | 70% correct |
| Vibe | 20% accurate |
| Brilliant insights | Near zero |
| Coarseness | 10% of memory |
| Time investment | ~1 month |

---

## Personal Notes

This is a fascinating approach to digital immortality that's actually achievable today with consumer tools. The iterative RLHF-style improvement process and the emphasis on predictive facts over exhaustive data is particularly interesting.

The failure modes section is valuable for anyone building personality-based LLM applications. The distinction between "core facts" (prompt) vs "long-term memory" (RAG) mirrors good prompt engineering practices.

The ethical section raises important questions about what we owe to AI simulations of people, even if we're "almost certain" they lack consciousness.
