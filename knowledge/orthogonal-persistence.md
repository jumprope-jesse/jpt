# Orthogonal Persistence

Source: https://github.com/mighty-gerbils/gerbil-persist/blob/master/persist.md
Date: 2024-03-09

## Core Concept

**Orthogonal Persistence**: All data and execution state persists by default. If your system crashes, gets stolen, or destroyed, you can restore to the exact state - variable bindings, execution context, everything - without any code explicitly handling persistence.

This is the opposite of **Manual Persistence** where all data is transient by default and developers must explicitly save to files/databases.

## Key Insight

> "Designing a programming language without data persistence means 'I only care about toy computations for people whose data doesn't matter.' Designing a database without a good programming language means 'I only care about toy data not part of any computation that matters.'"

## How It Works

### Persistence Domains
- Logical entities mapped to physical storage (disks, databases, cloud)
- Domain survives hardware changes through reconfiguration
- Transactions handled automatically per domain
- Supports federation, replication, encryption

### Atomicity via Atomic Sections
- Code wrapped in atomic sections won't be persisted in intermediate states
- Unlike transactions, atomic sections are **modular** - you can compose code without knowing if it contains atomic sections
- No rollbacks needed - all processes share transactions within a domain

### Synchronization via Memory Barriers
- Explicit instruction to wait for changes to be committed
- Evaluation can continue optimistically after barrier
- Side-effects queued until persistence confirmed

### Process Persistence
Both high-level and low-level approaches:
- **Low-level**: VM (like WASM) snapshots entire state
- **High-level**: Compiler transforms (CPS, lambda-lifting, monads) make execution context explicit and serializable

## Why Manual Persistence Fails

### Modularity Problems
- Transactions are global - you must know if you're already in one
- Nested transactions don't actually work (can't protect return values)
- Client-side code after COMMIT isn't guaranteed to run
- "Sagas" across transactions are inherently unreliable
- Schema changes require coordinating across all modules

### The Client/Server Mismatch
- Database servers have persistence but bad programming languages
- Clients have good languages but no persistence
- Context is lost on every failure/restart
- Requires complex infrastructure to approximate what should be automatic

## Schema Upgrade

With manual persistence: catastrophic events requiring crack teams, downtime, and ad-hoc migration code.

With orthogonal persistence: regular development activity. Variables include defaults, class redefinitions include migration methods, schema evolution is part of the language.

## Practical Implementations

- **Golem**: WASM-based "Durable Execution" platform
- **Temporal**: Durable execution across any infrastructure
- **Acton**: Fault-tolerant distributed programming platform
- **Historical systems**: PS-Algol, Napier88, Ten15 (British/Scottish)

## The Social Commentary

Today's reality inverted:
- Big corporations have excellent persistence (they remember everything about you)
- Individuals have no persistence (you forget, your data disappears, services shut down)

Orthogonal persistence could flip this - automatic persistence for individuals, privacy-preserving channels for communication.

## Related Concepts

- Durable Execution (marketing term for same concept)
- Event Sourcing (different approach to the same problem)
- ACID properties (orthogonal to persistence approach)
- Continuation-Passing Style (compiler technique for process persistence)

## Implications for Development

1. **No explicit save/load code** - persistence is the default
2. **Modular atomicity** - atomic sections compose freely
3. **Process persistence** - execution context survives crashes
4. **Schema evolution** - built into the language
5. **Resource management** - configured per domain with alerts/limits
