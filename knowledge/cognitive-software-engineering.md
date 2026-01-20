# Cognitive Software Engineering

Philosophy and principles for treating AI systems as software that can be engineered, tested, and maintained—rather than as inscrutable magic brains.

---

## Conjecture's Roadmap for Cognitive Software

*Source: https://www.lesswrong.com/posts/H26ndkABmGvoc9PTC/conjecture-a-roadmap-for-cognitive-software-and-a-humanist - Added: 2026-01-18*

A comprehensive manifesto on what's wrong with AI development and how to do it better. Core thesis: The way to build safe, beneficial AI is to treat it as a **software engineering problem**, applying decades of hard-won lessons from software development.

### What is Cognitive Software?

Cognitive software is "the stuff you can get a human to do, but not (currently) a computer"—anything you could write on a sheet of paper and hand to an intern.

Traditional software development hasn't solved these problems, so we have neural networks, LLMs, and prompt engineering. But the field is nascent, informal, and full of slop.

### The Oracle Database Analogy

Oracle's database codebase is:
- Millions of lines of poorly documented, confusing mess
- Relies on thousands of "flags" with weird, undocumented interactions
- Any change requires running literally millions of tests taking days
- Every change breaks thousands of tests
- No one knows how it all works

**The punchline:** This is how we currently develop AI, but worse. At least Oracle has a codebase—we have a neural network, a huge blob of numbers we can't look inside.

We can't find every edge case or test each "subpart" of a neural network in isolation. "Fixing" one eval often breaks others. It's brute force trial and error, worse than Oracle's magic flags.

### The Strange Decoupling

The weirdest thing about AI: **capabilities have decoupled from understanding**.

In traditional software, as complexity grows beyond your understanding, things break. In AI, you can get more capabilities without understanding—just shovel more data into GPUs.

The scientific process of AI:
1. Mess around with huge things
2. Gain no new understanding
3. Gain new capabilities but none of the nice properties
4. Build big dangerous things

All our intuitions are reversed. We assume capable systems come with understanding—but AI subverts this.

### Software Senescence vs Algorithmic Carcinogenesis

**Software Senescence:** Traditional software hits a natural limit. Push too far beyond understanding, things break. Legacy systems arrest in ungraceful stasis but don't get worse.

**Algorithmic Carcinogenesis:** AI has no natural limit to growth, spread, or virulence. Every compromise on quality for growth gets taken. Cancer in our media, art, software, soul.

> "There has been a palpable sickness in the internet for quite a while, at least for the last 15 years. Gen AI slop is the most salient recent expression of it, but it is not where it started."

Machine learning funded social media algorithms from day one. Slop isn't new to the AI era—remember listicles? Buzzfeed? The transition from the wild human-built Web 1.0 to algorithmically curated walled gardens?

### Complexity as the Enemy

As complexity grows, responsibility diffuses. No one is in charge, problems don't get solved. Facebook can claim "it's The Algorithm!! It's not our fault!!"

The antidote is simplicity. Simple systems enable:
- Accountability
- Responsibility
- Detectability of bad behavior
- Ability to find who's responsible
- Ability to make changes and fixes

> "A computer can never be held accountable. Therefore a computer must never make a management decision." — IBM, 1979

Yet computers now manage all our online social relationships.

### Examples of Great Software Engineering

Principles and concepts that stood the test of time:

1. **The Unix Philosophy (1978)** - Deep principles of modularity, often synonymous with "good software"
2. **The Relational Model / SQL (1969)** - Theoretical model from formal logic, still dominates 50+ years later
3. **Type Systems and ML/OCaml (1973)** - Catch bugs before running, formal Type Theory made practical

These prove we CAN do principled engineering in software. The goal: develop comparable principles for cognitive software.

### Conjecture's Roadmap (5 Phases)

**Phase 1: Foundational Infrastructure (tactics.dev)**
Solve 20th century DevOps headaches—backend, scaling, auth, LLM ops all out of the box. Remove friction so you can focus on cognitive code.

**Phase 2: Cognitive Language Design (CTAC)**
New programming language designed around deep integration with cognitive systems. New abstractions and primitives:
- Native uncertainty tracking
- Keywords like "reflect" (examine own execution trace) and "reify" (distill trace into a tactic)
- Control flow primitives that traditional languages lack

**Phase 3: Horizontal Scaling**
Solve breadth—many cognitive components remaining coherent. Inspired by Voyager (Minecraft-playing GPT-4 that "crystallizes" learning into discrete code shards).

Key: Strong safety engineering and software architecture to prevent sloppification. Complexity measures, type systems, time-traveling debuggers, AI-assisted reviews.

**Phase 4: Vertical Scaling - Deliberate Teaching and Cognitive Provenance**
Solve depth—teaching models new behaviors selectively.

**Deliberate teaching:** Know what the model does/doesn't know at each step. Add knowledge, check if integrated, understand generalization, revert if needed.

**Empty Language Models (ELMs):** Train on patterns but not facts. Then add facts one by one, monitoring the learning process. Know not just what went in (Provenance), but what generalizations were learned (Cognitive Provenance).

> "This is the philosopher's stone of how to turn AI into software engineering."

**Phase 5: Cognitive Emulation (CoEm)**
Build cognitive programs that emulate human cognition specifically. Human cognition is a specific kind—different from "tell AI to solve problems by whatever means."

Benefits:
- Economically valuable (economy built on human cognition)
- Institutions already adapted to it
- We can understand, audit, and make it safe

### Key Principles

1. **Complexity is the enemy** - Of security, responsibility, understanding
2. **Understanding enables vision** - You can't build what you don't understand
3. **Software lessons apply** - Decades of hard-won knowledge about managing complexity
4. **Simple systems enable accountability** - When you understand the system, you can fix it
5. **Good AI must be good software** - Same solutions that make AI beneficial make it safer

### On the Current State

> "People say 'so far AI hasn't led to any large scale damage.' I couldn't disagree more."

The damage already done:
- Can no longer tell if online responses are human
- AI images clog search engines and crush artists
- Social media addiction via algorithmic optimization
- Mental health devastation of younger generations
- Time, effort, sanity lost to algorithmic manipulation

This is explicitly the result of AI optimization. The few who don't fall prey do so *despite* AI, not thanks to it.

### Related

- `programming-philosophy.md` - "Do The Simplest Thing" and complexity management
- `context-engineering-agents.md` - Managing LLM context as software engineering
- `ai-agent-architecture.md` - Practical agent patterns that embody some of these principles

---

## Connections to Other Principles

**To "Do The Simplest Thing":** Both emphasize that complexity is the enemy. Simple systems enable understanding, which enables safety and effectiveness.

**To "Theory Building":** Conjecture's cognitive provenance is theory building applied to AI—knowing what the model "believes" and why.

**To "The Copilot Delusion":** Both critique capability without understanding. The decoupling of capabilities from understanding is exactly what makes current AI dangerous.

**To "Software Senescence":** Conjecture names the phenomenon and contrasts it with algorithmic carcinogenesis—AI lacks the natural limits that force traditional software to stop growing.
