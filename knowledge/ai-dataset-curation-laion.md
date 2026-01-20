# AI Dataset Curation: LAION-5B Case Study

Source: [Knowing Machines - Models All The Way Down](https://knowingmachines.org/models-all-the-way#section2)

## Overview

LAION-5B is a 5+ billion image-text pair dataset built from Common Crawl, used to train models like Stable Diffusion and Midjourney. This analysis reveals how "curation by statistics" shapes AI training data.

## Data Pipeline

```
Common Crawl (3B+ websites)
    → Extract IMG tags with ALT attributes
    → CLIP similarity scoring (image-text match)
    → Language detection (CLD3)
    → Threshold filtering
    → LAION-5B
```

## Key Findings

### ALT Tags Reflect Commercial Intent, Not Reality

Top sources in LAION-5B:
- Pinterest: 155M pairs (users write ALT tags for caption generation)
- Shopify: 140M pairs (SEO-optimized descriptions)
- SlidePlayer: 72M pairs (auto-generated from PowerPoint text)

**Critical insight**: ALT tags describe what site owners want algorithms to see, not what humans see. LAION-5B encodes commercial logic, not human perception.

### Threshold Sensitivity

- CLIP similarity threshold: 0.26-0.28
- 16% of images score within 0.1 of the threshold
- Changing threshold by 0.01 would add/remove ~937 million pairs
- Content plays no role; it's purely statistical filtering

### Language Bias

| Language | Captions per Speaker |
|----------|---------------------|
| English | 1.6 per speaker |
| Dutch | 3 per speaker |
| Icelandic | 7 per speaker |
| Russian | 1 per 1 speaker |
| French | 1 per 2 speakers |
| Swahili | 1 per 35 speakers |

English (and English-speaking culture) valued more than all 107 other languages combined.

CLD3 language detection has significant errors - 34M captions classified as Luxembourgian (a 300K speaker language), mostly actually English.

### Aesthetic Subset (LAION-Aesthetics)

Used by Midjourney and Stable Diffusion for fine-tuning. Built from:
1. **SAC (Simulacra Aesthetic Captions)**: 238K AI-generated images rated by Discord users (self-described as "nerdy" and "esoteric", most ratings from a "handful of users")
2. **AVA dataset**: 250K images from dpchallenge.com, rated by middle-aged photography enthusiasts (95% from US/Canada/Europe)
3. 15K logos

**Result**: Aesthetic preferences of a tiny, homogeneous demographic define what "visually appealing" means for billions of users.

## The Circularity Problem

```
LAION-5B uses CLIP scores
    → CLIP trained on undisclosed OpenAI dataset
    → Threshold determined by testing against ImageNet-1K
    → ImageNet benchmark set by ResNet50
    → Each layer compounds biases and blind spots
```

"Models on top of models, training sets on top of training sets."

## Practical Implications

1. **Dataset investigation is essential** - One of few tools to understand complex AI systems
2. **Openness matters** - LAION publishing as open-source enabled this analysis; most companies don't
3. **Statistical curation amplifies structural biases** - What gets crawled, what has ALT tags, what CLIP "understands"
4. **"Not production-ready" disclaimers don't prevent production use**

## Current Status (as of late 2024)

- LAION-5B unavailable following CSAM findings
- Replacement: CommonPool (12.8B pairs) - same methodology, same issues

## Related

- Common Crawl: Monthly web crawl corpus, 45% English content
- CLIP: OpenAI's image-text similarity model (training data undisclosed)
- ImageNet: Classic benchmark dataset with its own well-documented biases
