# Quantum Supremacy Skepticism: The Case Against Google's Claims

Source: Gil Kalai's blog (Combinatorics and more), Dec 2024
https://gilkalai.wordpress.com/2024/12/09/the-case-against-googles-claims-of-quantum-supremacy-a-very-short-introduction/

## Background

Google's 2019 paper claimed their 53-qubit Sycamore processor performed a computation in 200 seconds that would take a classical supercomputer ~10,000 years. The claim rests on two pillars:
1. **Fidelity claims** - assertions about sample quality
2. **Supremacy claims** - translating fidelity into classical compute advantage

## Key Criticisms

### Classical Runtime Estimates Were Wrong

- Google's classical runtime estimates were off by **10 orders of magnitude**
- The team knew better algorithms existed - they had developed them for one circuit class, then switched circuit types weeks before the final experiment
- IBM researchers and others (Pan & Zhang, Kalachev et al., Gao et al., Liu et al.) refuted the supremacy claims in subsequent papers
- Google now acknowledges their 2019 result can be computed classically in <200 seconds using tensor network contraction

### Fidelity Claims Are Statistically Implausible

The Google paper uses a simple a priori formula (Formula 77) predicting fidelity from component error rates.

Problems:
- Agreement between prediction and actual fidelity is "too good to be true" (10-20% across hundreds of circuits)
- Statistical explanation relies on unreasonable premises (exact ±20% error rates, unbiased instability, statistical independence)
- Error rates for individual components have never been released (as of Dec 2024)
- These concerns apply even to the smallest 12-qubit circuits

### Calibration Process Issues

According to Google, calibration used only 1- and 2-qubit circuit behavior. However:
- Statistical evidence suggests undocumented global optimization occurred
- Google provided outdated calibration to Jülich Research Center scientists, later modified after experiment
- Calibration programs not disclosed (cited as commercial secret)
- Inputs for calibration never shared despite promises

### Gap with IBM Results

IBM quantum computers (more advanced in some ways) show significantly worse random circuit sampling results than Google claims, even for 7-12 qubit circuits. This gap likely reflects methodological issues rather than superior hardware.

## Supporting Evidence for Google

- 2020 replication by USTC (University of Science and Technology of China)
- Some later verifications of fidelity estimations

## Current Status (2024)

Google's 2023/24 "Phase Transitions" paper claims 67-70 qubits would require years of classical supercomputer time. The debate continues.

## Key Papers Challenging Google

- Rinott, Shoham, Kalai (2022) - Statistical Aspects of the Quantum Supremacy Demonstration
- Kalai, Rinott, Shoham (2022) - Google's 2019 "Quantum Supremacy" Claims: Data, Documentation, & Discussion
- Kalai, Rinott, Shoham (2023) - Questions and Concerns About Google's Quantum Supremacy Claim
- Kalai, Rinott, Shoham (2024) - Random circuit sampling: Fourier expansion and statistics

## Implications

- Bitcoin dropped ~$1,000 (>$10B market cap loss) after the 2019 announcement
- May have imposed unrealistic expectations on other quantum computing efforts
- Author recommends not using Google's quantum claims as basis for policy decisions

---

# Google Willow: A Real Milestone (Scott Aaronson's Take)

Source: Shtetl-Optimized, Dec 2024
https://scottaaronson.blog/?p=8525

Scott Aaronson—quantum computing theorist and longtime field observer—provides a counterpoint to the skepticism above, calling Google's Willow chip "a real milestone."

## What Willow Achieved

**Hardware improvements since 2019:**
- 105 qubits (roughly doubled from 53)
- 5x improvement in coherence time
- 2-qubit gate fidelity: ~99.7% (controlled-Z) / ~99.85% (iswap), up from ~99.5%

**Error correction milestone:**
- As surface code size increases (3×3 → 5×5 → 7×7), the encoded logical qubit survives *longer*, not shorter
- This crosses an important threshold—"tickling the tail of the dragon" of fault tolerance
- However: only a single encoded qubit created, no encoded operations attempted yet

**New supremacy result:**
- Random Circuit Sampling with 40 gate layers
- Classical simulation estimate: ~300 million years (unlimited memory) or ~10⁵ years (memory-constrained)
- Caveat: Direct classical verification would take ~10²⁵ years, so all validation is indirect extrapolation

## Aaronson's Assessment

- "Yes, this is great. Yes, it's a real milestone."
- Progress is "broadly in line with what most expected" but gratifying to see it work
- Google's claims appear "entirely correct, with the caveats stated"
- The unverifiable regime concern is real—this is why efficiently verifiable supremacy experiments matter

## On Gil Kalai's Skepticism

Aaronson notes Kalai continues to dismiss Google's claims, but:
- The 2019 experiment has been "long ago superseded"
- IBM, Quantinuum, QuEra, and USTC have all reported successful Random Circuit Sampling experiments
- "I predict that Gil, and others who take it as axiomatic that scalable quantum computing is impossible, will continue to have their work cut out for them"

## What "True" Fault Tolerance Requires

Per Sergio Boixo (Google): fault-tolerant two-qubit gates with error ~10⁻⁶ (a million operations before one error). "We're still some ways from that milestone."

## Competitive Landscape

- Trapped-ion (Quantinuum) and neutral-atom (QuEra) had been pulling ahead recently
- Willow is "Google's reply"—ball now in competitors' courts
- Superconducting advantage: gates 1000x faster than trapped-ion, enabling million-sample experiments
- Trapped-ion advantage: movable qubits, slightly better 2-qubit gate fidelity

---

# Control Engineering Behind Google's QEC Breakthrough

Source: Quantum Machines Blog, Nov 2024
https://www.quantum-machines.co/blog/understanding-googles-quantum-error-correction-breakthrough/

## The Core Achievement

Google demonstrated **below-threshold operation** using surface codes:
- Logical error decreased by **2.14x** when increasing code distance from 5 to 7
- Error reduction is exponential with code distance—the "smoking gun" that QEC works
- Distance-7 surface code on 101 qubits doubled logical qubit lifetime vs uncorrected physical qubits

This crosses a critical threshold: adding more qubits now *reduces* rather than increases errors.

## Why Control Systems Matter

Qubits are fragile—even slight breeze, vibration, or measurement can introduce errors. QEC combines multiple physical qubits into logical qubits that correct errors through entanglement-based monitoring (not direct observation, which would collapse quantum states).

**Key insight**: QEC only works if physical error rate is below a critical threshold *before* correction. More qubits helps only when each qubit is already good enough.

## Technical Requirements That Made It Work

### Real-Time Synchronization
- Every correction cycle must complete within **1.1 µs**
- All gate operations, measurements must be perfectly aligned across the qubit array

### Real-Time Decoding
- Decoder analyzes measurement data to locate errors
- Maintained **~63 µs latency** over 1 million+ correction cycles
- Fast enough to prevent error propagation and congestion
- Essential for non-Clifford gates required for universal quantum computation

### High-Fidelity Gate Operations
- Single-qubit gate errors: **<0.1%**
- Two-qubit CZ gate errors: **~0.3%**
- Minor gate errors can cascade and degrade QEC effectiveness

## Decoder Architecture Trade-offs

| Platform | Latency | Compute Power | Use Case |
|----------|---------|---------------|----------|
| FPGA | Very low | Limited | Qubit control, dedicated computation |
| GPU/CPU | Higher | Much greater | Complex algorithms, larger computations |

**DGX Quantum** (NVIDIA + Quantum Machines): <4 µs round-trip latency between controller and GPU, combining low latency with high compute power.

## What's Next for Fault Tolerance

Requirements for scalable fault-tolerant quantum computing:
- Faster decoders (<10 µs latency needed for QEC convergence)
- Full closed-loop feedback based on decoder decisions
- Automated calibrations embedded in quantum programs
- Control hardware integrating classical and quantum workflows

Target: fault-tolerant two-qubit gates with error ~10⁻⁶ (one error per million operations)
