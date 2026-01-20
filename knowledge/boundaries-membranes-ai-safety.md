# Boundaries/Membranes & AI Safety

A compilation of research connecting the concept of «Boundaries/Membranes» to AI alignment and safety.

---

## Core Concept: What Are Boundaries?

From Andrew Critch's «Boundaries» Sequence:

> By boundaries, I just mean the approximate causal separation of regions in some kind of physical space (e.g., spacetime) or abstract space (e.g., cyberspace).

**Important distinction:**
> When I say boundary, I don't just mean an arbitrary constraint or social norm.

Boundaries are about the **approximate causal separation** of regions - both physical (cell membranes, skin, property lines) and abstract (firewalls, cryptographic boundaries, Markov blankets).

**Better exposition:** See "Agent membranes and causal distance" for clearer explanation of agent boundaries concept.

---

## Why This Matters for AI Safety

This concept has become increasingly central to practical AI alignment approaches, particularly in the past year (2023-2024).

### Davidad's Open Agency Architecture (OAA)

Most notably, Davidad's alignment paradigm uses boundaries as one of four core hypotheses.

**Deontic Sufficiency Hypothesis:** There exists a human-understandable set of features that, when satisfied, gives high probability of existential safety - and boundaries formalization makes this plausible.

From his "Bold Plan for Alignment":
- Most desiderata can be represented as **violations of Markov blankets**
- Formulated as negative constraints (avoid catastrophe, not solve full value problem)
- Core safety property to model-check policies against

**Davidad's current favorite target (2023):**
> "defend the boundaries of existing sentient beings" - nowhere near as ambitious as "human values", yet nowhere near as anti-natural or buck-passing as corrigibility.

**Key insight:** This target lies in the "vast moral gulf" between:
- Narrow technical targets (corrigibility)
- Overly ambitious targets (full human values)

### Applications to Alignment

From Critch's "Part 3b: Alignment problems in terms of boundaries":

Boundaries can elucidate murky alignment problem areas:
- Side effects as boundary violations
- Over-optimization as ignoring boundaries
- Multi-agent conflicts as boundary disputes
- Value alignment as respecting preference boundaries

---

## Technical Formalizations

### Markov Blankets / Directed Boundaries

From Critch's Part 3a:

**Definition:** Boundaries as **directed Markov blankets** in causal graphs
- Delineate regions where a living system's functioning occurs
- Can be "soft" (permeable) and directional (asymmetric causation)
- Time-extended version of Cartesian Frames

**Viscera vs Boundary:**
- Agent = boundary + viscera (internal processes)
- What Scott Garrabrant calls "agent" is subdivided into these components

### Cartesian Frames (Scott Garrabrant)

Related formalization from 2020:

> Cartesian frames are a way to add a first-person perspective (with choices, uncertainty, etc.) on top of a third-person "here is the set of all possible worlds"

**Connection:** Boundaries formalism is like a time-extended Cartesian Frame with explicit boundary/viscera distinction.

See also: Garrabrant's "Boundaries vs Frames" (2022) comparing the concepts.

**Related work (likely connected):**
- Embedded Agency
- Finite Factored Sets

---

## Key Researchers & Contributions

### Andrew Critch

**«Boundaries» Sequence (4 posts to date):**
1. Part 1: A key missing concept from utility theory (2022 Jul)
2. Part 2: Trends in EA's handling of boundaries (2022 Aug)
3. Part 3a: Defining boundaries as directed Markov blankets (2022 Oct)
4. Part 3b: Alignment problems in terms of boundaries (2022 Dec)

**Encultured AI plan (2022):**
- Many "minimize side effects" attempts can be operationalized as **respecting boundaries**
- Abstract principles for respecting boundaries that transfer across species/scales
- Not unique to humans, simple enough to be broadly applicable

**Acausal normalcy (2023):**
- Which human values are most likely to be acausally normal?
- Connection between boundaries and values that emerge across intelligent agents

### Scott Garrabrant

**Cartesian Frames** (2020) - related formalization
**Boundaries vs Frames** (2022) - comparison of the two concepts

Connection: Boundaries work builds on and extends Cartesian Frames framework

### Mark Miller

**Object-capability model** - applies boundaries to computer security

**Goal:** Make sure only processes that should have read/write permissions to a resource actually have those permissions, enforceable with cryptography.

**Key concepts:**
- Boundaries-based security and AI safety approaches (Allison Duettmann, 2023)
- AI safety problem = gross power imbalance problem, not intrinsically about AI
- Safety comes from good security (boundaries), not absence of threats

See also: "Gaming the Future" for boundaries-like ideas

**Mark's position:** Little intrinsically to do with artificial intelligence - it's about power imbalance and security. See talk "Misdiagnosing AGI risk."

### John Wentworth

Lists boundaries as one of open problems in understanding agents (comment, 2023).

**Position:** Boundaries are prerequisite for understanding 'agenty' phenomena.

**SERI MATS training:** Week 4, Day 1 - Boundaries Exercises (2022)
- Used as training exercise for alignment researchers
- Considered foundational enough to include in curriculum

### Vladimir Nesov

Active in discussions, see various comments on boundaries formalization.

---

## Applications Beyond Direct Alignment

### Computer Security

Object-capability model (Mark Miller) - cryptographic enforcement of boundaries

### Consequentialism

"One-Way Pattern Trap: Principled Cartesian Boundaries Keep the Good Stuff Inside" - David Udell (2023)

### Learning Theory

"The Learning-Theoretic Agenda: Status 2023: Agent Detection" - Vanessa Kosoy (2023)

### Causal Incentives

Causal Incentives Working Group (ongoing)

---

## Related Concepts (Likely Connected)

These topics deserve linking but haven't been fully explored:

- **Embedded Agency** - foundational work pre-Cartesian Frames
- **Finite Factored Sets** - post-Cartesian Frames development
- **Natural Abstractions** (John Wentworth) - what boundaries naturally emerge?
- **Free Energy Principle and Active Inference** (see Critch 3a)
- **Corrigibility** - boundaries might provide formalization approach
  - See Arbital page, particularly "side effects" section
- **Markov blankets** (general concept)

---

## Why This Approach Is Promising

### Compared to other alignment targets:

| Approach | Scope | Practicality | Natural Abstraction |
|----------|-------|--------------|---------------------|
| Full human values | Very broad | Intractable | Unclear |
| Corrigibility | Narrow | Buck-passing | Artificial |
| **Boundaries** | **Middle ground** | **Feasible** | **Natural** |

### Key advantages:

1. **Natural abstraction** - boundaries emerge naturally in physics, biology, social systems
2. **Mathematically formalizable** - Markov blankets, Cartesian Frames provide rigorous grounding
3. **Cross-domain** - applies to AI safety, security, multi-agent systems
4. **Actionable** - provides concrete properties to check/enforce
5. **Less ambitious than full value alignment** - but still provides existential safety

### Davidad's perspective:

From "Reframing inner alignment" (2022):
> Excited about Boundaries as a tool for specifying a core safety property to model-check policies against—one which would imply (at least) nonfatality—relative to alien and shifting predictive ontologies.

**The key insight:** You don't need to solve the full value alignment problem to get existential safety - just need to ensure boundaries of sentient beings are defended.

---

## Current Status & Resources

**Activity level:** "Booming subtopic" - interest picked up substantially in past year (2023-2024)

**Workshop:** Running workshop on boundaries/membranes and AI safety (as of Dec 2023)

**Tag:** "Boundaries [technical]" tag on LessWrong for all related posts

**Twitter compilation:** All of Davidad's tweets about boundaries collected into thread

**Further reading:**
- "«Boundaries» for formalizing a bare-bones morality" (May 2023) - how Davidad conceives boundaries applying to alignment
- "A list of core AI safety problems and how I hope to solve them" (Aug 2023) - Davidad's most direct explanation

**Specific examples:** See Davidad's reply about boundary violations (Jan 2024)

---

## Open Questions

From the compilation:

1. How do boundaries relate to Natural Abstractions?
2. Connection to Free Energy Principle?
3. How to formalize "soft" vs "hard" boundaries?
4. Can boundaries handle value drift/change?
5. What counts as a "violation" vs normal interaction?

---

## Meta: Why This Compilation Exists

From the original post author:

> I'm personally extremely excited about this topic, and I will be covering further developments.

The rapid growth of interest (particularly Davidad's adoption in OAA) suggests this may become a central formalization for practical alignment work.

---

## Key Quotes

**Davidad (Jan 2023):**
> "defend the boundaries of existing sentient beings," which is my current favourite. It's nowhere near as ambitious or idiosyncratic as "human values", yet nowhere near as anti-natural or buck-passing as corrigibility.

**Andrew Critch (on boundaries vs constraints):**
> When I say boundary, I don't just mean an arbitrary constraint or social norm.

**Davidad on humans as first-class parties:**
> Humans cannot be first-class parties to a superintelligence values handshake.

---

## Source

- Original LessWrong compilation: https://www.lesswrong.com/posts/fjgoMaBenyXcRDrbX/boundaries-membranes-and-ai-safety-compilation
- Created: March 2024
- Last updated in compilation: May 2023
- Still actively developed as of 2024
