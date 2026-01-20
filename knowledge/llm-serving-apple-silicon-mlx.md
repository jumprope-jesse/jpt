# LLM Serving on Apple Silicon with MLX

*Source: https://github.com/skyzh/tiny-llm - Added: 2026-01-18*

A hands-on tutorial for systems engineers to learn LLM serving using MLX on Apple Silicon. Builds infrastructure from scratch using only MLX array/matrix APIs (no high-level neural network APIs).

## Overview

Goal: Understand techniques for efficiently serving LLM models (specifically Qwen2) by implementing everything from scratch.

**Why MLX?** Easier to get an Apple Silicon MacBook than an NVIDIA GPU. The concepts transfer to PyTorch.

## 3-Week Curriculum

### Week 1: LLM from Scratch (Python only)

**Day 1: Attention**
- Implement `scaled_dot_product_attention`
- Implement `MultiHeadAttention` with K, V, Q weight matrices
- Reference: Annotated Transformer, PyTorch/MLX attention APIs

**Day 2: RoPE Embedding**
- Rotary Positional Embeddings (traditional and non-traditional variants)
- Reference: torchtune, vLLM implementations

**Day 3: Grouped Query Attention (GQA)**
- Different dimensions for query vs key/value
- Used by Qwen2 models
- Reference: mlx-lm Qwen2 implementation

**Day 4: RMSNorm and MLP**
- RMSNorm (accumulate at float32 for precision)
- SiLU activation

**Day 5: Transformer Block**
- Combine attention + normalization + MLP

**Day 6: Load the Model**
- Use mlx-lm's loader, extract parameters into custom operators

**Day 7: Generate Responses**
- Basic inference loop

**Week 1 Performance (M4 Pro Mac Mini):**
- Custom implementation: 17 tokens/sec
- mlx-lm reference: 50 tokens/sec
- Memory: 4x more than mlx-lm (no quantization support yet)

### Week 2: Optimizations

- Quantization
- Custom kernels (softmax, linear, silu) in C++/Metal
- Attention kernel optimization
- Key-value cache and compression
- Attention masks
- Prompt cache

### Week 3: Production Features

- Continuous batching
- OpenAI-compatible HTTP endpoint
- Service integration

## Quick Start

```bash
poetry install
poetry run pytest
poetry run python main.py
```

## Key Concepts

**Attention dimensions:**
```
K, V, Q: N.. x H x L x E
Where: N = batch, H = heads, L = sequence length, E = embedding size
```

**Multi-Head Attention:**
```
x: N x L x D
D = num_heads x head_dim
```

## Key References

- [Annotated Transformer](https://nlp.seas.harvard.edu/annotated-transformer/) - Original paper walkthrough
- [mlx-lm Qwen2](https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/models/qwen2.py) - Reference implementation
- [vLLM RoPE](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/rotary_embedding.py)
- [torchtune](https://pytorch.org/torchtune/stable/) - PyTorch reference implementations

## Why This Tutorial

Good for understanding:
- How attention mechanisms work at the matrix level
- Memory vs compute tradeoffs in inference
- Why MLX/Metal optimizations matter for Apple Silicon
- Foundation for understanding production LLM serving systems
