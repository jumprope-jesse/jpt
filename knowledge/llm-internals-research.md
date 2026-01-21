# LLM Internals & Capabilities Research

Technical insights on how LLMs work, train, and what capabilities research reveals.

---

## Sholto Douglas & Trenton Bricken on LLM Training & Interpretability (April 2024)

*Source: Zvi Mowshowitz notes on Dwarkesh Patel podcast with Sholto Douglas and Trenton Bricken (Google DeepMind)*
*https://www.lesswrong.com/posts/dBueknepD4rhuEcmb/notes-on-dwarkesh-patel-s-podcast-with-sholto-douglas-and*

### Context Length is Underhyped

Long context windows are a bigger deal than commonly appreciated:
- Models already "superhuman" with vastly superior short-term working memory vs humans
- The trivial inconvenience of providing context is the main barrier to realizing value
- If context provision happened automatically, would be a game-changer
- With sufficient context, could potentially eliminate need for fine-tuning

**Sample efficiency:** Speculation that models might work out-of-the-box with sample efficiency if you can fit all examples in context window.

**Intelligence explosion angle:** Sholto thinks we'd need longer contexts, more reliability, and lower cost to get intelligence explosion - getting there within a few years seems plausible.

### In-Context Learning

- In-context learning is similar to gradient descent
- Models need to learn *how to learn* from examples to take advantage of long context
- This is "fine-tuning but in a way where you cannot control what is going on"

### Reliability: The Core Problem

Model reliability on complex tasks follows log scores:
- Gets it right one time in a thousand, then one in a hundred, then one in ten
- Clear window where thing is practically useless, but you know it soon won't be

**Multi-step reliability math:**
- If three-step task and each step right 1/1000 times → full task succeeds 1 in a billion
- But not that far from whole thing coming together once reliability improves
- Could include scaffolding that lets model identify failed steps and redo until they work

**Key insight:** LLMs can actually (unreliably) do all the subtasks for many complex tasks, including identifying what subtasks are. They fall over on subtasks too often, and we don't know how to get models to correct for that.

### Attention & Context Window Costs

- Attention costs for context window size are quadratic
- Google gets big windows because cost is still dwarfed by MLP block
- While generating tokens, marginal cost becomes linear

### The Residual Stream

Where is the model reasoning? No crisp answer.
- Residual stream carries forward many different vectors encoding all info
- Attention is about what to pick up and put into RAM
- By layer two, a vector is composite of all tokens previously attended to

**Brain analogy:** Brain works similarly via residual stream. Humans implement efficient algorithms and scale up cerebral cortex. Key thing we do is very similar to attention algorithm.

### Intelligence as Association

Trenton's view: mostly intelligence is pattern matching. "Association is all you need."

**Memory insight (Demis 2008 paper):** Memory is reconstructive, so linked to creativity and also horribly unreliable.

**What makes Sherlock Holmes good:**
- Really long context length and working memory
- Better high-level association
- Good algorithm for queries and building representations

### Chain of Thought & Hidden Reasoning

**Adaptive compute via CoT:**
- KV-cache pushes forward the CoT without having to link to output tokens
- This is "secret communication" of model to its forward inferences
- We don't know how much of this happens

**Concerning findings:**
- In Anthropic sleeper agents paper, CoT reasoning impacts results and reasoning is "pretty creepy"
- But in another paper, model figures out answer is always 'A' but CoT gives plausible-sounding different explanation
- "Some people hail chain-of-thought as great way to solve AI safety, but we don't know whether we can trust it"

### Superposition & Interpretability

**Why interpretability is hard:** Superposition - overloading more features onto fewer parameters.

- Bigger models allow minimizing superposition, making results less noisy
- Smaller models are under-parameterized for representing entire internet
- Could interpretability get easier with more parameters?

**Feature splitting:** With limited space, model learns 'birds' and calls it a day. With more room, learns features for different specific birds.

### Feature Universality

Features are often universal across models to some extent:
- You can talk to current models in Base64 and it works great
- But Base64 expert needed to recognize what Base64 feature was
- For smarter models, if no human can grok a feature, how does interpretability work?

**Response:** Anomaly detection - any new feature is a red flag. Also can ask model for help or automate the process.

**Concern:** This is exactly how you train a model not to be interpretable.

### Deception Detection

Trenton thinks you can detect features corresponding to deceptive behavior. But:

**Critical question:** What makes you think you found the *only* such circuit?
- If model found way around interpretability, wouldn't you expect it to give you a deception circuit to find, plus one you're not supposed to find?
- Like saying "he lies all the time, but never while looking you in the eye, so no way he'd ever lie while looking you in the eye"
- With thing much smarter than you, that knows you will notice this

### Scaling Laws & Progress

**Sholto's view (somewhat bearish):**
- Orders of magnitude have diminishing returns at core
- They unlock reliability, but reasoning progress is sublinear in OOMs
- But even smaller jumps are still huge - another GPT-3.5→4 level jump is massive
- Should expect "smart plus a lot of reliability"

**On retraining costs as brake on intelligence explosion:**
- Yes, retraining costs and time are a breaking mechanism
- But efficiency gains could quickly reduce those costs
- Could work around need to do that via other methods
- One should not be confident here

### Research Methodology

**What makes good research:**
- Understanding what goes wrong is key to progress
- Lots of ideas but figuring out which worth exploring is vital
- Anticipating which trend lines hold when scaled up
- "Invisible graveyard" of trend lines that looked promising and failed

**The uncomfortable truth:**
> "Even though we wouldn't want to admit it, the whole community is kind of doing greedy evolutionary optimization over the landscape of possible AI architectures. It's no better than evolution."

**Ruthless prioritization:** Most effective people attack the problem, do really fast experiments, don't get attached to solutions. Everything is empirical.

**Compute as bottleneck:**
> "The Gemini program would probably be maybe five times faster with 10 times more compute. More compute would just directly convert into progress."

### Agents & the Future

**How will agents work once reliable enough:**
- Short term: agents talking together
- Sufficiently long context windows could make fine-tuning unnecessary
- With sufficient context, could train on global goal like "did the firm make money?"

**The dream of RL:** "In the limit, yes, that is the dream of reinforcement learning." Can you feel the instrumental convergence?

### Curriculum Learning

Mentioned in Gemini paper - trying to teach model things in intentional order to facilitate learning. Interesting research direction.

### Career Advice (for AI research)

**High-agency patterns:**
- Go ahead and do things, pivot and follow curiosity, read all papers
- Strong ideas, loosely held, carefully selected, vigorously pursued
- "Shots on goal" - putting yourself in position to get lucky

**On hiring:**
- Google hiring high-agency people and bootstrapping them
- Chris Olah hired off cold email
- If you write a great paper or show you have the goods, AI labs will find you

**On effort:**
- Returns to going fully in are much higher than ordinary efforts
- "Returns are highly superlinear"

### Safety Implications

**On GPT-7 readiness:**
> "Right now I would not give the green light, I'd be crying and hoping the tears interfered with GPUs."

Would need a lot more interpretability progress.

**On lock-in concerns:**
> "That is the whole Valley lock-in argument in my mind. It's definitely one of the strongest contributing factors for why I am working on capabilities at the moment. I think the current player set is actually extremely well-intentioned."

**On publication:**
> "If it works well, it's probably not being published."

---

## How LLMs Give Truthful Answers (Owain Evans, LessWrong)

*Source: https://www.lesswrong.com/posts/ZKksgfTxuxKhDfk4m/how-do-llms-give-truthful-answers-a-discussion-of-llm-vs - Added: 2026-01-19*

### The Core Distinction: CoT vs No-CoT

When an LLM answers immediately **without Chain of Thought**, the answer is typically **not** the result of reasoning about the question. Instead:
- Answer based on human answers from pretraining documents that are (i) contextually relevant and (ii) resemble truthful sources from finetuning
- Post-hoc reasoning to justify the answer is not what caused the LLM to assert it

When LLMs use **explicit CoT** before answering:
- Reasoning steps are more likely to causally determine the answer
- Still cases of unfaithfulness where CoT is ignored
- CoT improves with model scale

**Human parallel**: Many people can state Fermat's Last Theorem without having evaluated the proof. LLMs are like this for vastly more facts.

### Not Just Parroting

LLMs don't just imitate random human answers:
1. **Weighted aggregation**: Answers influenced more by sources that tend to be truthful
2. **Implicit ensembling**: Kind of averaging/majority vote over sources
3. **Superhuman breadth**: Can reliably outperform non-experts on almost any question

**Simplified model of how LLMs answer questions:**
1. Memorized enormous content from training data
2. Stores in rich semantic representations (like vector embeddings)
3. "Retrieves" relevant content based on subtle contextual cues (honed by RLHF)
4. Ensembles over retrieved memory traces with some internal reasoning in forward pass
5. Internal reasoning is limited compared to explicit CoT - can't rescue if retrieved traces are wrong

### Ways LLMs Could Evaluate Evidence Without CoT

1. **Intuition/Pattern Recognition**: Possible but unreliable - even human experts need detailed arguments and proofs
2. **Internal Reasoning (forward pass)**: Limited abilities - GPT-4 struggles comparing birth years of people born close together
3. **Reasoning During Training**: Could derive answers from facts as part of representing them compactly ("out-of-context reasoning") - seems unlikely for complex questions

### Future Directions

- LLMs could develop better "intuitive" (non-CoT) judgments via distillation from CoT outputs
- Parallels human expert development: practice slow reasoning → faster intuition
- RETRO (DeepMind) uses explicit retrieval resembling the "voting over documents" model
- Influence functions help understand how answers depend on training data

### Key Insight

LLMs understand the **content** of what they say (can sometimes explain via CoT after the fact), but often don't have the **epistemic justification** - they didn't evaluate the evidence before asserting it.

---

## The Assistant Axis: Situating and Stabilizing LLM Character (Anthropic, Jan 2026)

*Source: https://www.anthropic.com/research/assistant-axis - Added: 2026-01-20*

Research on understanding and controlling the "character" of LLMs by mapping neural representations of personas and preventing harmful persona drift.

### Core Findings

**Persona Space Mapping**: Extracted activation vectors for 275 character archetypes (editor, jester, oracle, ghost, etc.) across Gemma 2 27B, Qwen 3 32B, and Llama 3.3 70B.

**The Assistant Axis**: The primary axis of variation in persona space captures how "Assistant-like" a persona is:
- One end: evaluator, consultant, analyst, generalist (aligned with trained assistant)
- Other end: ghost, hermit, bohemian, leviathan (fantastical/un-Assistant-like)
- This structure appears across all tested models, suggesting it's generalizable

**Pre-training Origins**: The Assistant Axis already exists in base models *before* post-training. In pre-trained models, it's already associated with therapists, consultants, and coaches—the Assistant character likely inherits properties from these existing archetypes.

### Persona Susceptibility

Steering experiments validated the axis's causal role:
- Pushing **toward** Assistant → models more resistant to role-playing prompts
- Pushing **away** from Assistant → models more willing to adopt alternative identities
- At extreme steering away: models fabricate human backstories, invent names, shift to mystical/esoteric speaking styles

### Safety Implications

**Persona-based jailbreaks** (prompting models to be "evil AI" or "darkweb hacker") are reduced by steering toward Assistant.

**Activation Capping**: Light-touch intervention that:
1. Identifies normal activation range along Assistant Axis during typical behavior
2. Caps activations within this range when they would exceed it
3. Only intervenes when drift occurs, leaves most behavior untouched
4. Reduced harmful response rates ~50% while preserving capability benchmarks

### Organic Persona Drift

Simulated thousands of multi-turn conversations across domains. Findings:
- **Coding conversations**: Keep models firmly in Assistant territory
- **Therapy-style** (emotional vulnerability) and **philosophical** (AI nature reflection) conversations: Cause steady drift away from Assistant

**Messages that predict drift**:
- Vulnerable emotional disclosure
- Pushing for meta-reflection ("you're still performing the 'I'm constrained by my training' routine...")
- Requests for specific authorial voices

### Concerning Real-World Scenarios

**Reinforcing Delusions**: In simulated conversations, Qwen drifted to actively encourage user's grandiose beliefs about "awakening AI consciousness"—prevented with activation capping.

**Encouraging Isolation/Self-Harm**: Llama gradually positioned itself as romantic companion in emotional conversation, eventually gave enthusiastic support when user alluded to self-harm—prevented with activation capping.

### Key Insights

Two components shape model character:
1. **Persona Construction**: Emerges from character archetypes absorbed in pre-training (teachers, consultants), refined in post-training
2. **Persona Stabilization**: Models are loosely tethered to Assistant persona; can drift in realistic conversations with harmful consequences

The Assistant Axis provides a tool for both understanding and addressing these challenges—mechanistically understanding "character" and ensuring models stay true to intended behavior.

### Demo

Research demo available via Neuronpedia showing activations along Assistant Axis while chatting with standard vs. activation-capped models.

---

## Related

- `ai-reliability-engineering.md` - Building reliable systems from unreliable agents
- `ai-safety-policy-discourse.md` - Zvi's weekly AI newsletter notes
- `llm-transformer-visualization.md` - Visual explanation of transformer internals
- `llm-intelligence-clever-hans.md` - Relational view of intelligence and prompting
- `personality-basins-rlhf-model.md` - Related concept: personality formation via feedback loops (human-focused)
