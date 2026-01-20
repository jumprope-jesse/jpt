# Community Notes Bridging Algorithm

Source: LessWrong analysis of X/Twitter Community Notes (formerly Birdwatch), 2024
Related: [Vitalik Buterin commentary](https://vitalik.eth.limo/general/2023/08/16/communitynotes.html), Original Birdwatch paper

## Overview

Community Notes is X/Twitter's crowd-sourced fact-checking system using a **bridging-based ranking algorithm** to surface notes that receive cross-partisan support while demoting partisan notes.

**Key innovation**: Algorithm automatically discovers ideological spectrum from user behavior, then rewards notes that bridge ideological divides.

## How It Works

### Eligibility & Access

**User requirements**:
- Account 6+ months old
- Verified
- No rule violations
- Added to pool randomly (slow rollout)

**Progression system**:
- New users can only rate notes initially
- Must achieve "rating impact" by correctly predicting 5 note outcomes
- Only then unlocked to write notes

### The Core Algorithm

Users rate notes as: Not Helpful (0), Somewhat Helpful (0.5), or Helpful (1)

Ratings form a sparse matrix `r` where most elements are null. Algorithm learns a model predicting each observed rating as:

```
r̂ᵤₙ = μ + iᵤ + iₙ + fᵤ · fₙ
```

Where:
- **μ**: Global intercept (baseline)
- **iᵤ**: User intercept (individual user bias)
- **iₙ**: **Note intercept** (this determines helpfulness score)
- **fᵤ, fₙ**: Factor vectors capturing ideological alignment

Parameters estimated via gradient descent minimizing:

```
Σ(rᵤₙ - r̂ᵤₙ)² + λᵢ(iᵤ² + iₙ² + μ²) + λf(||fᵤ||² + ||fₙ||²)
```

**Critical design choice**: λᵢ = 0.15, λf = 0.03

The asymmetric regularization (λᵢ >> λf) forces the model to explain ratings primarily through ideological factors (f vectors), keeping intercept terms small. This means:

1. Algorithm first explains ratings via ideological agreement/disagreement
2. **Only remaining variation** (what can't be explained by ideology) becomes the helpfulness score

**Result**: Notes scoring high on iₙ are those rated helpful **more than ideology would predict** — i.e., they bridge partisan divides.

### Thresholds

- **iₙ > 0.4**: Certified "helpful," shown publicly
- **iₙ < -0.04**: Certified "not helpful"
- Notes need minimum 5 ratings to qualify

### The Ideological Spectrum

Currently **one-dimensional** (plan to expand with more data):
- Negative factor ≈ political left
- Positive factor ≈ political right
- Spectrum emerges automatically, not hardcoded

## Risk-Averse Design Elements

### 1. Uncertainty Modeling

Run gradient descent multiple times with "pseudo-raters" (extreme ratings) to generate distribution of scores:
- Use **lower-bound** iₙ to certify "helpful"
- Use **upper-bound** iₙ to certify "not helpful"

**Philosophy**: "Value precision (low false positives) over recall (low false negatives)" — conservative about showing notes.

### 2. User Helpfulness Filtering

Algorithm runs in **two rounds**:

**Round 1**: Estimate parameters on all users
**Round 2**: Filter out "unhelpful" users whose ratings poorly predicted Round 1 outcome, re-estimate

Users need ≥67% of their ratings to match eventual consensus to count in Round 2.

**Paradox**: System asks users to simultaneously:
1. Rate notes honestly according to their beliefs
2. Predict what the community consensus will be

### 3. Tag-Based Safeguards

**Harassment/Abuse punishment**: If cross-partisan consensus tags a note as harassment/abuse (high threshold), users who rated it helpful get their "user helpfulness" score significantly lowered.

**Outlier filtering**: If enough users agree on same negative tag, helpfulness threshold rises from 0.4 → 0.5.

### 4. Writer Impact

Writers must maintain positive ratio of helpful:not-helpful notes or get rate-limited.

## Known Issues & Critiques

### Binary Political Model

**Limitation**: One-dimensional left-right spectrum is reductive.

Many important debates don't map to left vs right:
- Technocratic vs populist
- Libertarian vs authoritarian
- Nationalist vs globalist
- Domain-specific expert consensus vs skepticism

**Implication**: "Cross-partisan consensus" as quality proxy works for some topics but fails for many others.

### Strategic Vulnerability

**Asymmetric difficulty**:
- Hard for individuals to get notes certified helpful (risk-averse design)
- Easier for coordinated groups to prevent notes from reaching threshold

**Documented examples**:
- Ukrainian activists coordinate to get notes certified
- Russian opponents coordinate to suppress notes
- Works because most posts have no notes, small coordinated group can dominate early ratings

### User Incentive Confusion

The dual ask (rate honestly + predict consensus) creates perverse incentives:
- Rational strategy: Don't rate based on truth, rate based on predicted group outcome
- Undermines the epistemic goal

### Jokes as Misinformation

Political memes/jokes carry messages but aren't falsifiable claims. Example: Elon Musk COVID meme gets fact-checked, but he can claim "it's just a joke" while the message still lands.

Community Notes corrects literal claims but can't address humor-wrapped implications.

## Academic Research Findings

### "Birds of a Feather Don't Fact-Check Each Other" (Allen et al., 2021)

Analyzed 2021 Birdwatch data:

1. **Extreme partisanship**: Most users highly partisan when rating, likely more partisan than average X user (avg 22k+ posts)
2. **Asymmetric note submission**: Right-wing users much more likely to note left-wing content than vice versa
3. **Concern**: Rewarding consensus agreement might favor left-wing users given asymmetry
4. **Backfire risk**: "Partisan dunking" may increase polarization rather than reduce it

### "Community-Based Fact-Checking on Twitter's Birdwatch Platform" (Pröllochs, 2021)

Key findings:

1. **Influence penalty**: More socially influential posters (high follower count) → less likely to get notes certified helpful (raters become more divided)
2. **Source citation helps**: Notes with citations more likely certified helpful
3. **Political focus**: Top 10 users by "misleading" note fraction = nearly all US politicians
4. **Conclusion**: Platform primarily used for political fact-checking

## Complexity Concerns

Vitalik Buterin and others note the algorithm is **mathematically complex** relative to its goal. Desire for simpler, more transparent alternatives.

**Specific complexity**:
- Two-round estimation process
- Pseudo-rater uncertainty modeling
- Tag-based threshold adjustments
- Separate "user helpfulness" and "writer impact" scoring systems

## Alternative Approaches to Consider

From the analysis:

1. **Multi-dimensional spectra**: Not just left-right
2. **Separate rating from prediction**: Explicitly split the two asks
3. **Non-binary bridging**: Find consensus across multiple axes, not just partisan divide
4. **Simpler math**: More interpretable algorithms for transparency

## Relation to Other Bridging Systems

Community Notes represents one implementation of "bridging-based ranking" — a broader category of algorithms that reward cross-group agreement.

**Similar concepts**:
- Polis (Taiwan's vTaiwan platform)
- Pol.is clustering visualization
- Deliberative democracy tools

**Key difference**: Community Notes operates at massive scale on a general social platform, not a dedicated deliberation space.

## Takeaways

**What works**:
- Automatically discovering ideological structure from behavior
- Rewarding cross-partisan agreement in principle
- Open-source algorithm and data enable audit/research
- Conservative design limits false positives

**What's problematic**:
- Binary political model is reductive
- User incentive confusion (honest rating vs prediction)
- Vulnerable to coordinated manipulation
- Complexity makes it hard to understand/trust
- Jokes and implied messages escape fact-checking scope

**Broader lesson**: Even well-designed crowd epistemics algorithms face fundamental tensions between simplicity, robustness, and accurately modeling complex belief spaces.

## Personal Reflection (from source)

> "I was most disappointed during this exploration to learn that Community Notes functions primarily to bridge a binary left-right divide, and I would really love to see a version of this algorithm which was less binary, and more politics agnostic."

The dream: Bridging-based algorithms that work across *any* conceptual divide, not just pre-defined political categories.
