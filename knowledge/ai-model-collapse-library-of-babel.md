# AI Model Collapse and the Library of Babel

Source: The Conversation - "An 83-year-old short story by Borges portends a bleak future for the internet" (2024)

## The Core Problem

LLMs require vast amounts of high-quality text for training. The web is finite, and high-quality content not already scraped is becoming scarce. NYT called this an "emerging crisis in content" - shortage of additional training data may hit as early as 2026.

## The Feedback Loop

As LLM output (with hallucinations, errors, biased content) ends up online, it pollutes the training data for future models:

1. LLMs trained on web content
2. LLM output published online (complete with errors)
3. Next-gen LLMs train on degraded content
4. Output quality degrades further
5. Repeat

A July 2024 Nature paper showed training AI on recursively generated data leads to "irreversible defects" and eventual "model collapse" - like copying a copy of a copy.

## Borges' Library of Babel (1941)

Borges imagined a universe of hexagonal rooms containing every possible permutation of letters:
- By definition, books containing all truths must exist
- But so do all possible falsehoods
- Both embedded in incomprehensible amounts of gibberish
- Finding truth becomes impossible; verifying it even harder

**The parallel**: The internet may become so polluted that meaningful, accurate content becomes unfindable amid AI-generated noise.

## Stephenson's Prediction (Fall, 2019)

Neal Stephenson imagined an internet so polluted with misinformation and advertising that it's unusable. Solutions:
- The wealthy subscribe to "edit streams" - human-curated trustworthy content
- Everyone else consumes low-quality, uncurated content

**Already happening**: Quality journalism behind paywalls while misinformation festers on free platforms.

## Two Dystopian Futures

1. **Economic divide**: Only wealthy can afford accurate/reliable information
2. **Signal-to-noise collapse**: So much AI-generated content that finding accurate information becomes impossible

## Implications for Software/Product Development

- Products that help users find signal in noise become valuable
- Curation and verification services have economic value
- Need to consider how your tools contribute to or combat content pollution
- Media literacy becomes essential skill to teach
