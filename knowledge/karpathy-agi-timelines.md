# Karpathy on AGI, LLM Limitations & Intelligence

Andrej Karpathy's perspective on AGI timelines, fundamental LLM limitations, and the nature of intelligence.

*Source: [Andrej Karpathy - AGI is still a decade away](https://www.dwarkesh.com/p/andrej-karpathy) (Dwarkesh Patel interview, October 2025) - Added: 2026-01-18*

---

## AGI Timeline: A Decade, Not a Year

Karpathy's "decade of agents" prediction is a reaction to industry hype. His reasoning:

**Why agents aren't ready today:**
- Can't hire an LLM as an intern/employee
- Lack multimodality, computer use capability
- No continual learning (can't remember what you tell them)
- Fundamental cognitive deficits that are intuitively obvious when you talk to models

**Why not shorter?** Problems are tractable but still difficult. Based on 15 years of seeing predictions and how they turned out.

**Why not longer?** The problems appear surmountable. Progress continues.

---

## LLMs vs Animal Brains: Different Optimization Processes

Key insight: **We're not building animals. We're building ghosts/spirits.**

| Animals | LLMs |
|---------|------|
| Evolved over millions of years | Trained by imitation on internet data |
| Hardware baked in via evolution (zebra runs minutes after birth) | Start from scratch each session |
| Evolution encodes weights in DNA somehow | Weights trained on text patterns |
| Very little RL for intelligence tasks | RL is core training paradigm |

**"We're building ghosts":** LLMs are ethereal spirit entities mimicking humans. Different starting point in the space of possible intelligences.

---

## Fundamental LLM Limitations

### 1. Reinforcement Learning is Terrible

> "You're sucking supervision through a straw."

**The problem:** After potentially minutes of complex reasoning/rollout, you get a single bit: correct or incorrect. Then you broadcast that signal across the entire trajectory.

- If the answer is correct, every single token gets upweighted - including wrong alleys you went down
- Humans would never do hundreds of rollouts
- Humans do complicated post-hoc review: "These parts I did well, these I didn't"

**No equivalent in current LLMs** of this reflect-and-review process.

### 2. Process-Based Supervision is Tricky

Why not reward intermediate steps? Because:
- LLM judges are gameable
- They have adversarial examples ("dhdhdhdh" gets 100% reward)
- Can't train against LLM reward for too long before finding cracks

### 3. Model Collapse

> "Any individual sample will look okay, but the distribution is quite terrible."

LLMs are "silently collapsed":
- Ask ChatGPT for a joke - it only knows ~3 jokes
- Samples lack diversity/entropy that humans have
- Training on your own outputs collapses further

**Why collapse matters:** Can't do effective synthetic data generation if your samples lack the richness and entropy of human-generated data.

### 4. Too Good at Memorization

> "LLMs are distracted by all the memory they have of pre-training documents."

- Can regurgitate passages verbatim
- Memorize random sequences in 1-2 iterations
- This is a bug, not a feature

**Humans' poor memory is a feature:** Forces us to find generalizable patterns. LLMs should be worse at memorization.

**Vision:** A "cognitive core" - intelligent entity stripped of knowledge but containing the algorithms of intelligence. Maybe ~1 billion parameters.

---

## Missing Pieces for True Agents

### Sleep/Distillation
Humans build up context during the day, then "something magical happens" during sleep - distillation into weights. No LLM equivalent.

### Memory Architecture
- Context window = working memory (very accessible)
- Weights = hazy recollection (compressed)
- No hippocampus equivalent
- No process for taking what happened and distilling it back

### Culture
LLMs don't have culture:
- Why can't an LLM write a book for other LLMs?
- Why can't LLMs be inspired/shocked by each other's work?
- No growing repertoire of knowledge for their own purposes

### Self-Play
No equivalent of AlphaGo-style self-play:
- LLM creates problems, another learns to solve them
- First LLM makes problems harder over time
- This multi-agent improvement hasn't been claimed yet

---

## On Coding Agents

### Why Karpathy Uses Autocomplete, Not Agents

Three modes of AI-assisted coding:
1. **Reject all LLMs** - probably wrong now
2. **Autocomplete** (Karpathy's sweet spot) - you're still the architect
3. **Vibe coding / agents** - useful for specific settings

### Where Agents Fail (nanochat example)

- Can't handle intellectually intense, non-boilerplate code
- Keep misunderstanding because they have too much memory of "typical ways"
- Too over-defensive (try-catch everywhere)
- Using deprecated APIs
- Bloating the codebase
- Can't internalize that you have custom implementations

> "They're not very good at code that has never been written before."

### Where Agents Work

- Boilerplate code
- Code that occurs often on the internet
- Languages you're less familiar with (Rust for Karpathy)
- Tasks with clear tests to validate

---

## Why Self-Driving Took So Long (and What It Means)

### Demo-to-Product Gap
- First demos: 1986
- Karpathy's perfect Waymo demo: 2014
- Still not done in 2025

### March of Nines
Each 9 of reliability = constant amount of work:
- 90% working = just the first nine
- Need 2nd, 3rd, 4th, 5th nine
- Each nine is the same effort

**Implication for AI:** "I'm very unimpressed by demos." Demos are easy, products are hard, especially when cost of failure is high.

### Software Has Same Property
> "In software, it's almost unbounded how terrible something could be."

Security vulnerabilities, data leaks, etc. Software engineering should be treated like self-driving - high cost of failure.

---

## On Intelligence Explosion & GDP

### AI Won't Break the Exponential

> "We're in an intelligence explosion already and have been for decades."

- GDP has been exponential for centuries
- Couldn't find computers, mobile phones, or any single technology in GDP
- Everything diffuses slowly, averages into the same exponential
- AI will be the same - more automation, same pattern

**Prediction:** AGI stays on the 2% GDP growth trajectory.

### Counterargument (Dwarkesh)

- Labor is the bottleneck
- If you had billions of smart agents, it's like population explosion
- Places with lots of people relative to capital have had 10-20% growth
- Industrial Revolution changed the regime (0.2% → 2%), AI might again

**Karpathy's response:** Still presupposing a discrete jump with no historical precedent. "God in a box" assumption is wrong - it will be gradual diffusion.

---

## Loss of Control & Understanding

Most likely outcome: **gradual loss of understanding and control**

- Layer automation everywhere
- Fewer people understand it
- Not a single entity takeover
- Multiple competing autonomous entities, some going rogue, others fighting them off
- "Hot pot of completely autonomous activity we've delegated to"

---

## Key Quotes

On RL:
> "Reinforcement learning is terrible. It just so happens that everything we had before it is much worse."

On models:
> "Claude Code or Codex, they still feel like this elementary-grade student. I know they can take PhD quizzes, but they still cognitively feel like a kindergarten or elementary school student."

On demos:
> "Whenever I see demos of anything, I'm extremely unimpressed."

On memorization:
> "I would love to have them have less memory so that they have to look things up, and they only maintain the algorithms for thought."

On the future:
> "Starfleet Academy... an elite institution for technical knowledge."
