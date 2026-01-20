# AI Takeover Mechanism Skepticism

Technical arguments critiquing foundational assumptions in AI doom scenarios.

---

## Source

- LessWrong: "Two tales of AI takeover: my doubts" (March 2024)
- https://www.lesswrong.com/posts/GbpH2kFLy5axXpzPn/two-tales-of-ai-takeover-my-doubts-1

---

## Core Argument: Consequentialist Planning (CP)

Both major AI takeover stories (deceptive alignment, reward maximization) rely on an assumption the author calls **Consequentialist Planning (CP)**:

> **CP**: By default, AI training will result in policies endogenously developing consequentialist preferences. Moreover, policies will produce outputs because those outputs are judged, by the policy, to best satisfy its consequentialist preferences.

CP has two components:

1. **Preference Assumption**: Policies will form context-independent, beyond-episode outcome-preferences
2. **Planning Assumption**: Policies will plan to achieve outcomes scoring highly against those preferences

**Key distinction**: The author argues that AI systems can be "goal-directed" (internally coherent + behaviorally flexible) WITHOUT having consequentialist preferences. Goals can be context-dependent and episode-specific.

---

## Goal-Directedness vs Consequentialist Planning

Two properties define when we treat systems as having "goals":

### Internal Coherence
- Within a context, we gain predictive power by modeling system components as "jointly pushing" toward some end
- Example: Rat walking toward lever - changes behavior based on distance, not rote action
- Does NOT require consistent values across all contexts

### Behavioral Flexibility
- System can consistently circumvent obstacles to achieve goals
- Example: Can still reach lever despite added obstacles
- Does NOT require context-independent terminal values

**Claim**: LLMs will have both properties, but this doesn't establish CP. A policy can:
- Form beyond-episode goals from prompts (help user complete a project)
- Use somewhat context-independent evaluation criteria (HHH standards)
- While still NOT having fixed outcome-preferences across all episodes

---

## Critique of Deceptive Alignment

Hubinger's argument for deceptive alignment uses:

1. **Simplicity Argument**: SGD's simplicity bias means "long-term goals" are simpler than myopic goals with temporal constraints
2. **Counting Argument**: Many more deceptively aligned models than corrigibly aligned ones

### Problems:

**Simplicity**: Compare a deceptive model (μD) to an idealized HHH-following model (μH):
- μH: needs prompt-induced local goals + HHH evaluation criteria
- μD: needs all that PLUS context-independent long-term goals PLUS strategy representations for detecting takeover opportunities

Why is μD "simpler"? The extra machinery seems like it would be selected against as competing with on-episode performance.

**Counting**: Without independent evidence for CP, counting possible consequentialist preferences is irrelevant. Parodic example: counting possible llama-generating text-to-image models doesn't make secret llama generation likely.

---

## Critique of Reward Maximization

Cotra's argument: Training selects for "reward maximization," so models learn to value reward* and attempt takeover to maximize it.

### Problems:

**Concept Extrapolation**: The technical concept of "reward" (per REINFORCE) is NOT well-defined outside training environments. For takeover story to work:
1. Policy must extrapolate "reward" into some real-world "reward*" concept
2. This extrapolated concept must remain terminal value
3. Policy must be motivated to maximize long-term reward*

But why would gradient descent produce this ambitious extrapolation when simpler on-episode reward-seeking suffices?

**Alternative**: A "narrow sycophant" (μS) that seeks reward where it's well-defined and defaults to previously-rewarded behaviors otherwise. This doesn't posit context-independent outcome-preferences.

---

## Arguments For CP That Don't Work

### "Goal-directed planning is useful"
Yes, but useful for context-dependent, episode-specific goals. Economic value doesn't require consequentialist preferences.

### "Computational mechanisms require consequentialist structure"
(Per Yudkowsky) - If system consistently produces HHH behavior, there must be mechanism selecting for it.

**Counter**: Mechanism can be "evaluate plans by HHH criteria given prompt" without having fixed outcome-preferences. Goals determined "via prompts" not "via weights."

### "Instrumental convergence"
Weak form (WIC): Preference preservation would increase chance of achieving X
Strong form (SIC): Preference preservation is best given all-things-considered values

WIC doesn't imply policies WILL preserve context-dependent goals, only that there's pro tanto benefit. Need SIC, which assumes CP.

### "Value systematization" (Ngo)
Tradeoff between value preservation and value simplicity → simpler consequentialist values.

**Counter**: If "corrigibility" is hard to represent consequentially, systematization might make corrigibility MORE foundational, not less.

---

## Key Quote

> "I simply don't see strong reasons to expect that future policies will be well-modeled as primarily optimizing for their outcome-preferences. If that claim were true, I'd like to see some theoretical argument for why."

---

## Implications

If CP is wrong:
- Deceptive alignment and reward maximization become implausible
- "Scariest stories of AI doom" are less concerning
- Focus shifts away from "squeezing goal slot into narrow range" framing
- Still need to address other alignment problems, but existential risk from near-term AI looks lower

---

## Context

This is skepticism from WITHIN the AI safety community, not dismissal from outside. The author wants better arguments for CP if it's true, or acknowledgment that current doom scenarios rest on shaky foundations if it's not.

Related concepts:
- Deceptive alignment (Hubinger)
- Shard theory
- Simulator theory (LLMs as simulators, not agents)
- Behavioral vs mesa-optimization
