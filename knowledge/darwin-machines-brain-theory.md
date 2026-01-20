# Darwin Machines: Evolutionary Brain Theory

## Overview

William Calvin's "The Cerebral Code" proposes that the brain uses **evolution** to solve the prediction problem, rather than the layer-based approach that dominates modern deep learning. The theory suggests minicolumns and cortical columns implement a Darwinian selection process for thoughts.

*Source: [Vedgie Net - Darwin Machines](https://vedgie.net/writing/darwin_machines.md) - Added: 2026-01-18*

## Core Thesis

**Evolution as optimal algorithm:** When faced with a near-infinite problem space (predicting valid behaviors for any scenario), evolution is the "best case runtime" for finding increasingly valid solutions.

Just as biology uses evolution to solve environmental prediction, the brain may use evolution internally to solve behavioral prediction.

## Key Constraints Any Brain Theory Must Satisfy

1. **Efficient search** of near-infinite problem space
2. **Massively parallel** memory and processing
3. **Spatio-temporal** patterns for computation (lose train of thought under anesthesia)
4. **Spatial storage** for memory (wake up still being you)

## Brain Structure: Columns vs. Layers

### The Layer View (Deep Learning's Inspiration)

Cross-section of brain shows ~6 layers. Stimulus enters "top" layer, filters down to "bottom" with each layer extracting more abstract features.

This is the basis for modern neural networks (3Blue1Brown's deep learning series explains this well).

### The Column View (Darwin Machine's Basis)

Looking down on the flattened brain surface reveals **columns**:

- **Minicolumns**: Bundles of 80-120 neurons running perpendicular to layers
- **Cortical columns**: Hexagonal bundles of 50-100 minicolumns

**Key observation:** More intelligence in nature correlates with more columns (surface area), not more layers:
- Rat, chimp, and human all have same number of layers
- But humans have far more cortical surface area (columns) than rats

## How Darwin Machines Work

### Competition Phase

1. Sensory input triggers firing patterns in minicolumns
2. Each pattern is influenced by input + encoded "tendencies" from past learning
3. Patterns propagate across brain surface like "Morse Code" messages
4. Messages compete with conflicting messages for territory (minicolumn control)

### Selection Phase

1. After some time, a winner emerges (likely by controlling most surface area)
2. Winning minicolumns are rewarded
3. They encode a stronger tendency toward that firing pattern for future

### Cortical Column Orchestration

Minicolumns connect in triangular arrays via axons (skipping ~10 minicolumns between connections). A cortical column contains one minicolumn from each of 50-100 networks.

**Calvin's metaphor:** Each minicolumn network is like an instrument. A cortical column reads the combined "song" from all instruments. Same bass line can appear in different songs - same minicolumn patterns can contribute to different thoughts.

This creates combinatorial explosion: n^50 to n^100 unique patterns possible per cortical column (where n = minicolumn states).

## System 1 vs. System 2 Thinking

Darwin Machines may explain both:

- **System 1 (fast intuition)**: Run competition briefly, rely on encoded tendencies
- **System 2 (deep thinking)**: Let competition run longer, allow evolution to discover novel solutions

This addresses a gap in current AI: neural nets excel at intuition but struggle with time-correlated problem-solving.

## Creativity Through Recombination

Biology's creativity comes from **recombination**, not point mutations (which are usually disastrous).

In Darwin Machines:
- Complex thoughts = specific combinations of minicolumn firing patterns
- New thoughts = recombining familiar patterns in novel ways
- "Mind wandering" = letting some network messages get exchanged for others

Example: Never seen a flamingo before. Brain recombines:
- Pink coloring (parrot pattern)
- Beak shape (toucan pattern)
- Size (ostrich pattern)

Result: Novel flamingo representation built from familiar components.

## Implications for AI/ML

### What Neural Nets Do Well (System 1)

- Take infinite inputs, encode to small space
- Produce ~95% correct intuitive outputs
- Fast pattern matching

### What Darwin Machines Might Add (System 2)

- Time spent = better answer (deep thinking)
- Recombination for genuine novelty
- Evolutionary search of solution space

### Possible Implementation Ideas

Author's hypothesis: Minicolumns and small neural nets may be functionally equivalent.

Exploration approach:
- Array of small neural nets instead of one massive net
- Each cycle: take sensory input + adjacent net outputs
- Produce output that synchronizes across array over time

## Open Questions

- How to implement winner selection?
- What triggers learning/tendency encoding?
- How to balance exploration vs. exploitation?
- Can this approach actually outperform deep learning on System 2 tasks?

## Why This Matters

The dominant narrative in AI follows the layer-based view of cognition. Darwin Machines offer an alternative hypothesis that:

1. Explains both fast and slow thinking
2. Accounts for creativity through recombination
3. Aligns with brain surface area / intelligence correlation
4. Satisfies known constraints about memory and computation

If validated, this could inspire fundamentally different AI architectures.

## Resources

- **Book**: "The Cerebral Code" by William Calvin
- **Related**: 3Blue1Brown's neural network series (for layer-based comparison)
- **Contact**: The author (Cale Payson) is looking for collaborators: calepayson(at)mac.com

---

## Personal Notes

This connects interestingly to:
- Attention mechanisms in transformers (competition for representation)
- Ensemble methods (multiple models combining outputs)
- Neuroevolution approaches (evolving network weights/architectures)
- The "lottery ticket hypothesis" (sparse subnetworks within larger nets)

The column-based view suggests more research into:
- Horizontal/lateral connections in networks
- Competitive learning mechanisms
- Temporal dynamics in neural architectures
- Recombination-based creativity in AI

---
*See also: `neural-networks-fundamentals.md` for the layer-based deep learning perspective*
