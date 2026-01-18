# AI Verification Engineering

Frameworks for ensuring AI outputs are reliable and trustworthy. AI can only run as fast as humans can verify its work.

*Source: https://higashi.blog/2025/12/07/ai-verification/ - Added: 2026-01-18*

## Core Insight

With AI, tasks break down into two parts: **learning/creation** and **verification**. The speed at which humans can verify AI work determines whether AI actually helps.

- If verification << creation → AI is highly effective (you quickly confirm it's right)
- If verification ≈ creation → AI becomes an automation script (marginal benefit)
- If verification >> creation → Welcome to vibe-land (unverified work piles up)

## The Eric and Daniel Story

**Eric** (PM, non-engineer): Started vibe coding with Gemini. Can't verify outputs without learning software development from scratch. No edge over engineering teams for shipping features reliably.

**Daniel** (Staff engineer): Uses AI coding as a "force multiplier." Can spot-check and skim through AI's work, knows immediately if it's doing the right thing with a few simple verification steps. Results are reliable.

The difference: **Daniel's existing expertise makes verification cheap.**

## Where AI Exploded: Fast Verification, Slow Creation

Image generation is the canonical example:
- Creating a realistic image → hours of work (centering text boxes alone takes forever)
- Verifying an image looks right → milliseconds (your vision cortex answers "does this look right?" instantly)

This cost asymmetry explains why AI image generation exploded. Look for similar scenarios to identify other killer use cases.

## Verification Debt

When verification effort > creation effort, organizations accumulate **verification debt**:

- More things are created than can be verified
- Unverified code runs in production
- Unvalidated outputs cause unexpected side effects
- The debt compounds over time

This is scarier than tech debt because it's invisible until something breaks.

## Verification Engineering

After Prompt Engineering and Context Engineering, **Verification Engineering** is the next frontier:

> "AI can only reliably run as fast as we check their work."

### Key Questions

1. How to craft more technically precise prompts that guide AI to do surgical, verifiable work (vs. vibing it)
2. How to train more capable technical stakeholders who can effectively verify and approve AI outputs
3. How to find more tasks that are easy to verify but hard to create
4. How to push theoretical boundaries of what can be succinctly verified

### Possible Approaches

- **Discard traditional programming languages** - Program in abstract graph-like dataflow representations where correctness is easier to judge regardless of implementation details
- **Leverage human intuition** - Find ways to harvest low-latency "feelings" that nature gives us (like we do with visual evaluation)
- **Match tasks to expertise** - Route AI work to people whose verification costs are lowest

## Implications

1. **Whoever figures out cheap verification wins** - The ability to verify more complex tasks faster = extracting more benefit from AI
2. **Expertise becomes more valuable, not less** - Experts can verify quickly; novices cannot
3. **Track verification debt** - Technical leaders should monitor how much unverified AI output is accumulating
4. **Design for verifiability** - Structure AI outputs to be easier to check

## Related Concepts

- See `ai-automation-ironies.md` for the human factors of AI monitoring (deskilling, vigilance fatigue)
- See `coding-agent-tools.md` section on "Building Confidence Without Reading All Code" (Matthew Rocklin's approaches)
