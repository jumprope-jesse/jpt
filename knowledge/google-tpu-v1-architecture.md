# Google TPU v1 Architecture

*Source: https://thechipletter.substack.com/p/googles-first-tpu-architecture - Added: 2026-01-19*

Deep dive on Google's first Tensor Processing Unit (TPU v1), developed in 15 months starting late 2013. Designed specifically for inference (not training).

## Project Goals

1. **10x cost-performance advantage** over GPUs for inference tasks
2. **Build quickly** - ASIC development in 15 months
3. **TensorFlow compatibility** - seamless integration with existing CPU/GPU code

## Systolic Array Architecture

The core innovation: systolic arrays for efficient matrix multiplication.

From Kung & Leiserson's 1978 paper:
> "A systolic system is a network of processors which rhythmically compute and pass data through the system... the function of a processor is analogous to that of the heart."

### How It Works

Data flows through a grid of multiply/accumulate units (MACs):
- Values feed in from the top (weights) and left (data)
- Each MAC performs multiplication and addition
- Partial sums flow through the array
- Results emerge from the bottom

**Key benefit:** No need to store/fetch intermediate results from main memory. Results are automatically available when needed due to the array structure and input ordering.

### TPU v1 Matrix Unit

- 256 x 256 MAC array (65,536 units)
- 8-bit x 8-bit integer multiplications
- Uses quantization to avoid expensive floating-point operations
- New matrix multiplication every 2 cycles (pipelined)

## System Architecture

```
Host CPU ←→ PCIe ←→ TPU v1
                      ↓
              DDR3 DRAM (weights)
                      ↓
               Weight FIFO
                      ↓
          Matrix Multiply Unit (256x256)
                      ↓
               Accumulators
                      ↓
         Activation (ReLU, Sigmoid, etc.)
                      ↓
              Unified Buffer
                      ↓
         (loops back as input for next layer)
```

### Key Components

| Component | Purpose |
|-----------|---------|
| DDR3 DRAM | Stores weights, loaded from host |
| Weight FIFO | Feeds weights into matrix unit |
| Matrix Unit | 256x256 systolic array |
| Accumulators | Stores matrix multiply results |
| Activation | Hardware-accelerated ReLU, Sigmoid |
| Unified Buffer | Stores inputs and intermediate results |

## Instruction Set

Remarkably simple CISC design with ~20 instructions. Five core instructions:

```
Read_Host_Memory    # PCIe → Unified Buffer
Read_Weights        # Weight memory → Weight FIFO
Matrix_Multiply     # Systolic array operation
Activate            # Apply activation function
Write_Host_Memory   # Unified Buffer → PCIe
```

**Pseudo-code for inference:**
```
Read_Host_Memory
Read_Weights
Loop_Start
    Matrix_Multiply
    Activate
Loop_End
Write_Host_Memory
```

Instructions sent by host over PCIe, not fetched from memory.

## Die Utilization

| Component | Die Area |
|-----------|----------|
| Matrix Multiply Unit | 24% |
| Unified Buffer | 29% |
| Control (decode, etc.) | 2% |

Only 2% for control logic demonstrates the elegance of the simple ISA.

**Fabrication:** TSMC 28nm (mature process for quick development)
**Die area:** Less than half of Intel Haswell CPU or Nvidia K80 GPU

## Performance (vs 2013 hardware)

| Metric | TPU v1 vs K80 GPU | TPU v1 vs Haswell CPU |
|--------|-------------------|----------------------|
| Inference speed | 15-30x faster | 15-30x faster |
| Performance/Watt | 25-29x better | 25-29x better |

### Hardware Comparison

| Spec | TPU v1 | K80 GPU |
|------|--------|---------|
| MACs | 25x more | baseline |
| On-chip memory | 3.5x more | baseline |

## Limitations

- **Inference only** - not designed for training
- **Host-dependent** - relies on PCIe communication
- **Limited flexibility** - optimized for specific neural network patterns

## Legacy

> "We say tongue-in-cheek that TPU v1 'launched a thousand chips.'"

Laid groundwork for TPU v2, v3, etc. which added training capabilities and improved architecture.

---

*See also: gpu-architecture-llm-scaling.md for modern GPU/TPU training comparisons*
