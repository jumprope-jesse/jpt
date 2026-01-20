# Rust Programming Language

A systems programming language designed for safety, concurrency, and performance.

---

## Rust at 10: Origin Story

*Source: https://www.zdnet.com/article/rust-turns-10-how-a-broken-elevator-changed-software-forever/ - Added: 2026-01-18*

Rust 1.0 shipped May 15, 2015. The language has grown from a personal project to major adoption.

### The Broken Elevator

In 2006, Graydon Hoare was annoyed with his apartment building's elevator constantly breaking down. He suspected memory errors in its control software (likely C or C++). Sick of climbing 21 flights of stairs, he started designing a new language.

Named it "Rust" after a family of tough fungi "over-engineered for survival."

### Design Goals

**Memory Safety Without Garbage Collection:**
- Unique ownership system prevents common errors
- No null pointer dereferencing
- No buffer overflows
- Each piece of data has a single owner
- Data automatically freed when it goes out of scope
- Entire categories of memory bugs eliminated at compile time

**Concurrency Safety:**
- Catches data races before code runs
- Makes it easier to write safe concurrent programs

### Timeline

- **2006**: Hoare starts Rust as a home project
- **2009**: Mozilla begins sponsoring
- **2010**: Publicly announced
- **2015**: Rust 1.0 releases (May 15)
- **2025**: 10th anniversary

### Growth Since 1.0

- **crates.io**: From ~2,000 packages to 180,000+
- **Standard library**: Tripled in size
- **Contributors**: 6,700+
- **Changes merged**: 246,000+
- **Public crates tested per release**: Nearly 600,000

### Ecosystem Maturity

- rust-analyzer for IDE support
- Cargo package manager
- Non-breaking releases every six weeks
- Regular release cycles enable rapid innovation

### What Rust Is For

Systems programming / infrastructure:
- Network protocols
- Web servers
- Load balancers
- Telemetry systems
- Databases
- Codecs
- Cryptography
- File systems
- Operating systems
- Virtual machines
- Interpreters

> "The world needs robust and reliable infrastructure, and the infrastructure we had was not up to the task. Put simply: it failed too often, in spectacular and expensive ways." — Graydon Hoare

### Major Adopters

- **Mozilla**: Firefox
- **Google**: Android, Chrome OS, Fuchsia
- **Microsoft**: Windows core libraries, Azure Confidential Compute
- **Linux kernel**: Ongoing Rust integration

### Linux Kernel Adoption

Linus Torvalds on Rust in Linux:
> "I was expecting [Rust] updates to be faster, but part of the problem is that old-time kernel developers are used to C and don't know Rust. They're not exactly excited about having to learn a new language that is, in some respects, very different."

Still a "stalwart Rust-in-Linux supporter."

### Learning Rust

**Recommended resources:**
1. *The Rust Programming Language* (aka "The Book")
2. *Rust for Rustaceans*
3. Rust by Example (free, web-based)
4. Google's Comprehensive Rust (free)

**The borrow checker**: Steepest part of learning curve. Handles lifetimes and ownership. Author found it not that hard.

### Why Developers Love It

Stack Overflow survey: For 8 consecutive years, "Rust is the most admired language; more than 80% of developers who use it want to use it again next year."

The appeal: "It just works, and I don't need to sweat the memory details as I once did with C."

### Key Quote

> "Rust is a story about a large community of stakeholders coming together to design, build, maintain, and expand shared technical infrastructure." — Graydon Hoare

---

## Rust Tools Built in Rust

- **prek**: Pre-commit alternative, ~10x faster than Python version
- **uv**: Python package manager
- **ruff**: Python linter

See: `prek-precommit-rust.md`, `uv-python-package-manager.md`
