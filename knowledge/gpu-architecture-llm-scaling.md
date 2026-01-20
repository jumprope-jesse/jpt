# GPU Architecture for LLM Training

*Source: https://jax-ml.github.io/scaling-book/gpus/ - "How To Scale Your Model" Chapter - Added: 2026-01-18*

Deep-dive on NVIDIA GPU architecture, networking, and roofline analysis for LLM training at scale. Compares GPUs to TPUs and covers parallelism strategies.

## GPU Hardware Architecture

### Core Components

A modern ML GPU (H100, B200) consists of:
- **Streaming Multiprocessors (SMs)** - compute cores specializing in matrix multiplication
- **HBM** - high-bandwidth memory stick
- **Tensor Cores** - matrix multiplication accelerators within each SM
- **CUDA Cores** - vector arithmetic units (SIMD/SIMT)
- **Memory hierarchy** - HBM > L2 cache > L1/SMEM > registers

### H100 Architecture

- 132 SMs (B200 has 148)
- Each SM has 4 subpartitions containing:
  - Tensor Core
  - Warp Scheduler
  - 16K 32-bit registers
  - CUDA Cores
- 256kB SMEM per SM
- 50MB shared L2 cache

### GPU vs TPU Comparison

| Component | GPU | TPU |
|-----------|-----|-----|
| Matrix Core | Tensor Core | MXU |
| Vector Unit | CUDA Cores/Warp | VPU |
| Memory | HBM + L2 + SMEM | HBM + VMEM |
| On-chip SRAM | 33MB | 95MB |
| Memory BW | 3.35 TB/s | 4.8 TB/s |

**Key differences:**
- **Modularity**: GPUs have 100+ small independent SMs; TPUs have 1-2 large Tensor Cores
- **Programming model**: CUDA cores use SIMT (per-thread instruction pointer); TPUs use SIMD
- **Cache memory**: TPUs have much more VMEM than GPUs have SMEM+TMEM
- **Tradeoff**: GPUs are more flexible; TPUs are cheaper, more predictable when used as intended

## GPU Networking

### Intra-Node (NVLink)

Within a node (typically 8 GPUs), all GPUs are connected via NVLink switches with all-to-all connectivity.

**H100 Node:**
- 4 NVSwitches per node
- 18 NVLink links per GPU
- 25 GB/s per link (50 GB/s for B200)
- **Total egress: 450 GB/s per GPU** (900 GB/s for B200)

**GB200 NVL72:**
- Larger NVLink domain of 72 GPUs
- Enables larger tensor parallelism within NVLink domain

### Cross-Node (InfiniBand/Ethernet)

Fat tree topology with full bisection bandwidth:

```
[Spine switches] - 16x NDR IB (50GB/s)
       |
[Leaf switches] - 8 per SU
       |
[Nodes] - 32 per SU, 8 GPUs each
```

**H100 DGX SuperPod (1024 GPUs):**
- 128 nodes (8 GPUs each)
- 4 Scalable Units (256 GPUs each)
- 400 GB/s egress bandwidth per node into scale-out network
- Full bisection bandwidth at all levels

### Bandwidth Summary

| Level | H100 Egress BW | B200 Egress BW |
|-------|----------------|----------------|
| Intra-node | 450 GB/s | 900 GB/s |
| Cross-node | 400 GB/s | 400 GB/s |

## Collective Operations

### Intra-Node Collectives

**AllGather/ReduceScatter cost:**
```
T = (N-1)/N * B / (N * W)  ≈  B / (N * W)
```
Where: N = GPUs, B = bytes, W = egress bandwidth

- H100: ~B / 450e9 seconds
- B200: ~B / 900e9 seconds

**AllReduce:** 2x above cost (without SHARP in-network reductions)

**AllToAll:** Cost = B * (N-1) / (N^2 * W)
- 2x faster than TPU for small clusters
- Ragged AllToAll (top-k): Cost reduced by k/N factor

### Cross-Node Collectives

With full bisection bandwidth:
```
T ≈ B / 400e9  (node egress bandwidth)
```

**AllToAll across nodes:** Cost spikes 4x+ when spanning node boundary

### SHARP (In-Network Reductions)

NVIDIA switches support in-network reductions:
- Theoretically halves AllReduce cost
- Practical improvement: ~30% (not 75%)
- Effective bandwidth ~480 GB/s with SHARP

## Roofline Analysis for LLM Training

### Data Parallelism / FSDP

To be compute-bound:
```
Batch size per GPU > FLOPs / (2 * Bandwidth)
```

**H100 requirements:**
- Intra-node: BS > 2200 tokens/GPU
- Cross-node: BS > 2475 tokens/GPU

**MoE models:** Multiply by E/k (e.g., 32x for E=128, k=4)

### Tensor Parallelism

Compute-bound when: `Y < F * 2 / (990e12 / W)`

**Practical limits:**
- ~8-way TP within single node
- Up to 16-19 way with 2-node spanning

### Expert Parallelism

Two regimes:
1. Small EP (1-2 nodes): Similar cost to TP
2. Large F models: Can scale to E-way EP across many nodes

### Pipeline Parallelism

Communication cost is tiny: `B * D / (M * X * bandwidth)`

**Challenges:**
- Code complexity (zero-bubble scheduling)
- Conflicts with FSDP/ZeRO-3
- Pipeline bubbles and step imbalance

## Production Sharding Examples

### DeepSeek V3 (2048 H800s)

- 64-way Expert Parallelism (8 nodes)
- 16-way Pipeline Parallelism
- 2-way ZeRO-1 Data Parallelism
- Batch size: 62.9M tokens (~30k tokens/GPU)

### LLaMA-3 (16k H100s)

- 8-way Tensor Parallelism (within node)
- 16-way Pipeline Parallelism
- 128-way ZeRO-1 Data Parallelism
- Batch size: 16M tokens (~1k tokens/GPU)

## Practical Guidelines

### General Recipe

1. **Small dense models:** Aggressive FSDP + some PP/TP
2. **Large dense models:** 1-2 node TP + multi-node PP + pure DP
3. **MoE models:** EP preferred over TP; scale EP if F is large

### Key Constraints

- **TP limited to NVLink domain** (~8 GPUs, up to 72 for GB200)
- **Cross-node AllToAll 4x+ penalty** - keep EP within 1-2 nodes if possible
- **FSDP needs large batches** - use PP to reduce critical batch size
- **Latency matters** - empirical bandwidth << theoretical, especially for small messages

## Hardware Specs Reference

| Spec | H100 | B200 |
|------|------|------|
| SMs | 132 | 148 |
| bf16 MXU FLOPs | 990 TFLOPs | 2.25 PFLOPs |
| HBM | 80 GB | 192 GB |
| HBM BW | 3.35 TB/s | 8 TB/s |
| NVLink BW | 450 GB/s | 900 GB/s |
| IB egress | 400 GB/s | 400 GB/s |

## Key Formulas

**Matmul intensity:** FLOPs / Bandwidth = tokens needed for compute-bound

**AllGather time:** T = B / (N * W)

**AllReduce time:** T = 2 * B / (N * W) without SHARP

**DP critical batch:** BS > FLOPs / (2 * BW) ≈ 2500 tokens/GPU on H100

---

*From "How To Scale Your Model" scaling book by the JAX-ML team*

## Nvidia Competitive Strategy and Software Moat

*Source: [Stratechery - Nvidia Waves and Moats](https://stratechery.com/2024/nvidia-waves-and-moats/) by Ben Thompson - March 2024*

### Blackwell B200 Launch: "AI Woodstock"

**GTC 2024 vs Previous Events:**
- Previous GTCs (2021-2022): Broad exploration of use cases, heavy focus on CUDA libraries and SDK ecosystem
- GTC 2024: Laser-focused chip launch now that product-market fit is clear (generative AI)
- 11,000 seat arena - comparable to Windows 95 launch spectacle
- Jensen Huang: "Perhaps the last major launch before AI dominated everything"

### Blackwell Architecture Details

**Physical Architecture:**
- **Two dies fused into one chip** with full coherence (vs Hopper's single die)
- 208 billion transistors
- Same 4nm TSMC process as Hopper → similar serial calculation speed

**GB200 Platform:**
- 2 Blackwell GPUs + 1 Grace CPU (vs Hopper's 1:1)
- GB200 NVL72: 72 GPUs in liquid-cooled rack
  - 30x performance increase over equivalent H100s for LLM inference
  - 25x reduction in cost and energy per inference
  - Dedicated hardware for transformer inference

**Performance Characteristics:**
- Training time stays constant (90 days) between Hopper and Blackwell
- Calculation speed essentially the same (limited by 4nm process)
- **Gains come from parallelism**: More efficient multi-GPU coordination via NVLink
- Result: Smaller GPU fleet needed for same training run (lower power/cost)
- Forward-looking: Hopper-sized fleet of Blackwell → much larger models possible

**Model Generation Mapping:**
- GPT-4: Trained on Ampere A100s
- GPT-5: Likely trained on Hopper H100s
- GPT-6+: Path enabled by Blackwell's scale

### Pricing Strategy and Competitive Pressure

**Manufacturing vs Retail:**
- B100 costs **2x H100** to manufacture
- Nvidia increasing retail price **less than expected**
- Lower margins going forward

**Pressures driving conservative pricing:**
1. AMD aggressive on price
2. Major customers (Google, Meta, Amazon, Microsoft) building custom chips
3. High incentives to find alternatives for inference workloads

**Implication:** Nvidia concerned about market share erosion, willing to sacrifice some margin to maintain dominance.

### The Software Moat: NIMs (Nvidia Inference Microservices)

**What NIMs Are:**
- Pre-built containers with everything needed for model deployment
- Optimized for Nvidia GPUs
- Free to download and use
- Run anywhere: cloud, datacenter, workstations

**The Lock-In:**
> "These packages, incredible bodies of software... all you have to do is come to ai.nvidia.com. We call it Nvidia Inference Microservices, but inside the company we all call it NIMs."

**Critical detail:** NIMs only run on Nvidia GPUs.

**Agent-Based Future:**
Jensen's vision: Companies use multiple NIMs in agent frameworks to accomplish complex tasks. Each NIM has a "human API" (natural language interface).

### The CUDA Moat Evolution

**Before ChatGPT (2021-2022):**
- Nvidia building extensive free software stack on CUDA
- Libraries, SDKs, frameworks for every domain
- Challenge: Unclear who would use it all at scale
- GTC focus: Evangelizing use cases

**After ChatGPT (2024):**
- Use cases crystal clear (generative AI)
- Work happening at higher abstraction level (on top of models, not CUDA primitives)
- Pressure to escape CUDA higher than ever
- Incentives to find alternatives massive (cost savings)

**Nvidia's Response Stack:**
1. **DGX Cloud** - Capture Intel-like standardization inertia (even when competitors are better)
2. **NIMs** - Build new lock-in at the inference/deployment layer
3. **Conservative B200 pricing** - Maintain market share vs AMD and custom silicon

### The Digging-a-New-Moat Challenge

**Problem:** The wave that made GTC a spectacle also threatens CUDA's moat
- High-level model APIs abstract away GPU details
- Customers highly motivated to multi-source
- Training advantages may not translate to inference dominance
- Software lock-in must be re-established at new abstraction layer

**Solution Attempt:** Make the entire AI deployment ecosystem Nvidia-dependent through NIMs, even if CUDA itself becomes less directly visible.

**Open Question:** Will Nvidia be forced to give back more margin in future generations to maintain position?

### Strategic Takeaways

1. **Product-market fit changes strategy**: Pre-ChatGPT Nvidia evangelized broadly; post-ChatGPT they focus on maintaining dominance
2. **Moats must evolve**: CUDA alone insufficient when abstractions change
3. **Margin pressure from success**: Dominant position attracts competitors and vertical integration
4. **Software follows hardware**: NIMs are attempt to rebuild lock-in at the right abstraction level
5. **Spectacle as moat**: GTC's scale signals ecosystem dominance and deters competitors

---

*Combined sources: JAX-ML Scaling Book (technical architecture) + Stratechery (competitive strategy)*
