# Automated Reasoning

Source: [Amazon Science - A gentle introduction to automated reasoning](https://www.amazon.science/blog/a-gentle-introduction-to-automated-reasoning)

## What is Automated Reasoning?

Automated reasoning tools answer questions about programs (or logic formulas) using mathematical techniques, rather than exhaustive testing. They can be dramatically faster than testing and can work with infinite domains (e.g., unbounded mathematical integers).

**Key difference from testing:**
- Testing validates the entire stack (code + compiler + runtime + hardware)
- Automated reasoning focuses on one layer (typically source code), with precise assumptions about the surrounding environment
- Automated reasoning can answer questions in milliseconds that would take lifetimes with exhaustive testing

## Core Concepts

### The Three Steps of Reasoning

When analyzing programs, automated reasoning tools work through:

1. **Control structure** - Understanding program flow (conditionals, loops, etc.)
2. **Eventual truth** - What becomes true as the program executes
3. **Invariants** - What is always true during execution

Example analyzing loop termination:
```c
void g(int x, int y) {
   if (y > 0)
      while (x > y)
         x = x - y;
}
```

Reasoning: If y > 0, then x always decreases in each iteration (invariant), so the loop eventually terminates.

### The "Don't Know" Problem

Automated reasoning tools sometimes return "Don't know" or timeout. This is unavoidable due to fundamental theoretical limits (halting problem, Gödel's incompleteness theorems).

**The halting problem example:**
```c
void h() {
   if terminates(h) while(1){}
}
```

No tool can correctly answer whether this terminates - it's a logical paradox.

**The science challenge:** Minimize "Don't know" responses through better heuristics, even though they can never be fully eliminated.

## Amazon's Use Cases

### AWS Customer-Facing Features
- **IAM Access Analyzer** - Reasons about policy permissions
- **S3 Block Public Access** - Verifies bucket configurations
- **VPC Reachability Analyzer** - Analyzes network paths
- **AWS Config Rules** - Constraint-based reasoning about policies

### Internal Development
- Integrated into development processes
- Raises bar on security, durability, availability, quality
- Both automated and semi-automated tools used internally
- Only fully automated tools in customer-facing features

### Key Insight
Configuration artifacts (AWS policies, VPC networks, makefiles) can be treated as code and reasoned about using the same techniques.

## Limitations

1. **Not a complete replacement for testing** - Still need end-to-end validation of assumptions (compiler correctness, hardware behavior, etc.)
2. **"Don't know" answers** - Some problems are theoretically impossible; others just need better tools
3. **Intractability** - Many problems are NP-hard; tools use heuristics that sometimes fail
4. **Single layer focus** - Typically analyzes one abstraction layer at a time

## Nomenclature

- **Logic** - Formal system for defining truth (e.g., propositional logic, first-order logic)
- **Theorem** - A true statement in logic
- **Proof** - Valid logical argument for a theorem
- **Mechanical theorem prover** - Semi-automated tool that checks machine-readable proofs (e.g., HOL-light)
- **Formal verification** - Theorem proving applied to computer systems (e.g., CompCert verified C compiler)
- **Formal methods** - Broad term for using logic to reason about systems
- **Automated reasoning** - Focus on automation and scale
- **Semi-automated reasoning** - Requires user hints but finds valid proofs

## Tools Ecosystem

### SAT/SMT Solvers
- **Z3** - Microsoft's SMT solver, widely used
- **CVC4** - Cooperating Validity Checker
- **MiniSat** - Minimalist SAT solver
- **Vampire** - First-order logic theorem prover

### Program Verifiers
- **Dafny** - Programming language with built-in verification
- **CBMC** - C Bounded Model Checker
- **SeaHorn** - Verification framework for C/LLVM
- **KLEE** - Symbolic execution engine
- **Infer** - Facebook's static analyzer

### Proof Assistants (Semi-automated)
- **Coq** - Proof assistant with extensive libraries
- **Isabelle** - Generic proof assistant
- **Lean** - Microsoft's theorem prover
- **HOL light** - Simple higher-order logic prover (by Amazon's John Harrison)

### Specialized Tools
- **TLA+** - Temporal logic specification language (Leslie Lamport)
- **Alloy** - Relational logic analyzer
- **SPIN** - Model checker for concurrent systems
- **PRISM** - Probabilistic model checker
- **Rust** - Programming language with memory safety proofs in type system

## Learning Path

**Recommended approach:** Bounded depth-first search - look at a variety of tools and techniques in moderate detail, rather than going deep on one area.

### Essential Books
1. *Handbook of Practical Logic and Automated Reasoning*
2. *Decision Procedures*
3. *Model Checking*
4. *Software Foundations*
5. *Introduction to Static Analysis*

### Key Conferences
- **TACAS** - Tools and Algorithms for Construction and Analysis
- **CAV** - Computer Aided Verification
- **IJCAR** - International Joint Conference on Automated Reasoning
- **POPL** - Principles of Programming Languages
- **SMT Workshop**

### Competitions
- Termination Competition
- SV-COMP (Software Verification)
- SMT-COMP
- SAT Competition
- CASC (Automated Theorem Proving)

## AWS Automated Reasoning Team

Key insights from AWS talks:

- **Byron Cook** - Focus on provable security at AWS scale
- **Neha Rungta** - Constraint-based reasoning in AWS Config
- **Serdar Tasiran** - Formal methods leadership
- Integration with compliance (Chad Woolf, VP Compliance)
- Cryptographic verification with s2n (work with Galois)
- SideTrail - Time-balancing verification for crypto

## Historical Context

- **1931** - Gödel's incompleteness theorems
- **1936** - Turing's decidability paper
- **1959** - Hao Wang uses automated reasoning to prove theorems from *Principia Mathematica*
- Decades of research on handling heaps, stacks, pointers, recursion, concurrency, callbacks

## Virtuous Cycle at Amazon

More input problems → Tool improvements → More usage → More problems → Better tools

This flywheel drives rapid progress in practical automated reasoning capabilities.

## Related Concepts

- **Static analysis** - Analyzing code without executing it
- **Symbolic execution** - Executing programs with symbolic inputs
- **Model checking** - Systematically exploring state spaces
- **Abstract interpretation** - Analyzing programs using abstract domains
- **Separation logic** - Logic for reasoning about heap-allocated data structures
- **Constraint solving** - Finding values that satisfy constraints

## Practical Value

**Speed:** Milliseconds vs. lifetimes for exhaustive testing

**Precision:** Makes assumptions explicit, separates concerns between stack layers

**Scale:** Can handle infinite domains and complex systems

**Confidence:** When it says "yes" or "no", it's mathematically sound (modulo assumptions)

**Limitations awareness:** "Don't know" answers are honest about uncertainty
