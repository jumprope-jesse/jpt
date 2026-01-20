# Dera - RAG Embeddings Management Platform

*Source: [getdera.com](https://getdera.com/) - Open-source RAG operations platform*

## Overview

Dera is an open-source platform for managing embeddings and chunks when building production-ready RAG applications. Built on Neon Database for cost-effective scalability.

## Key Features

### Chunking Strategy Iteration
- Create different embedding schemas easily
- Track matching results across strategies
- Visualize and compare chunking approaches in the UI
- Rapid experimentation on retrieval quality

### Evaluation & Visualization
- Inspired by Jerry Liu's (LlamaIndex CEO) talks on RAG evaluation
- Built to address frustration with evaluating text and embeddings data
- Visual tools for assessing chunk quality and embedding performance

### Cost Management
- Built on Neon Database for reduced costs
- Scalable architecture without typical vector DB overhead

## Deployment Options

**Open Source Self-Hosting**
- Completely open-source codebase
- Free to self-host on your infrastructure
- Check GitHub for setup instructions

**Managed Cloud**
- Hassle-free hosted option available
- Free tier: 1 project, up to 5 team members, 20 API requests per 60s

## Use Cases

Based on the maturity model in `rag-maturity-levels.md`, Dera fits at **Level 4-5**:
- **Level 4**: Evaluating search quality with different chunking strategies
- **Level 5**: Understanding shortcomings through visualization and comparison

Good for teams who have:
- Basic RAG pipeline working (Levels 1-2)
- Observability/logging in place (Level 3)
- Need to systematically improve retrieval quality

## Pricing

### Free Tier
- 1 project
- Up to 5 team members
- 20 API requests every 60 seconds
- Perfect for evaluation and prototyping

## Contact

- Email: hendy@getdera.com (direct to founder)
- Website: getdera.com
- Launched: February 2024

## Related Tools

- **LlamaIndex** - RAG framework (Dera inspired by Jerry Liu's work)
- **Cognita** (`cognita-rag-framework.md`) - Another open-source RAG framework
- **AWS Bedrock Knowledge Bases** (`aws-bedrock-knowledge-bases-rag.md`) - Managed alternative

## Evaluation Approach

Complements the synthetic evaluation pattern from `rag-maturity-levels.md`:

```python
# From RAG maturity doc
def test():
    text_chunk = sample_text_chunk()
    questions = ask_ai(f"generate questions for {text_chunk.text}")
    for question in questions:
        search_results = search(question)
    return {"recall@5": (1 if text_chunk in search_results[:5] else 0)}
```

Dera would help:
1. Create multiple chunking schemas
2. Run the same evaluation against each
3. Visualize which strategy performs best
4. Track improvements over time

## When to Use

**Good fit:**
- Experimenting with chunking strategies (fixed-size vs semantic vs recursive)
- Need visual comparison of embedding quality
- Team collaboration on RAG improvement
- Cost-conscious projects (built on Neon)

**Not needed if:**
- Basic RAG with fixed chunking is good enough
- Using managed service like AWS Bedrock Knowledge Bases
- Don't need systematic evaluation yet (still at Level 1-2)
