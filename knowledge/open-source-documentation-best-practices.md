# Open Source Documentation Best Practices

*Source: https://johnjago.com/great-docs/ - Added: 2026-01-19*

Case studies of esbuild and Redis as examples of exceptional documentation.

## Why Documentation Matters

- **Saves time**: Team members read docs first, leading to more productive discussions
- **Enables contributions**: Faster onboarding for open source contributors
- **Preserves decisions**: Past reasoning recorded, prevents reintroducing old problems
- **Structures thinking**: Writing reveals flaws you wouldn't otherwise notice

## README Best Practices

**esbuild approach:**
- Short, focused on end users
- Links to major doc sections (getting started, FAQ, API)
- Single "Why?" section explaining value proposition
- Hard to get lost

**Redis approach:**
- Short intro for users, then detailed sections for contributors
- Includes build instructions, common problems, OS gotchas
- Source code layout overview

## Architecture Documentation

**esbuild's architecture.md:**
- Table of contents for navigation
- Design principles section (foundation for understanding decisions)
- Graphics to visualize complex concepts (phases, parallelism)
- Code snippets mixed with visuals
- Shows traversal/flow through code

**Redis internals (in README):**
- Source code directory layout
- Key files and their structure
- Control flow starting points
- Compact but comprehensive

## Changelog Best Practices

esbuild's changelog entries include:
- Summary
- Extended description
- Example code showing before/after
- Impact understandable without reading actual code changes

## Code Comments

Redis examples:
- Multiple paragraphs for complex single lines (providing context)
- NOT for trivial operations
- Explain "why" for potentially questioned assertions
- Teach intent, not just mechanics

## Key Takeaways

1. README audience matters - users vs contributors may need separate sections
2. Graphics help explain phases, parallelism, and looping processes
3. Design principles first, then specific decisions
4. Changelogs should be readable without code diffs
5. Comments explain "why", not "what"
6. Time invested in docs saves more time later
7. Not every project needs exhaustive docs - match to project scope and users

## When to Document

- **Do document**: Projects others use or contribute to, complex systems
- **Skip documenting**: Purely for fun, uncertain if going anywhere, solo experiments

## Tools for Auto-Documentation

### Sage AI

**URL:** https://sage-ai.dev/

AI-powered tool that auto-generates engineering documentation for complex codebases.

**Key Features:**
- Breaks down knowledge silos within teams
- Reduces onboarding time from months to days
- Creates comprehensive, contextual knowledge base of software systems
- Addresses "knowledge friction" - the barrier of understanding existing code

**Target Use Cases:**
- Large, complex software systems
- Teams with high engineer turnover
- Organizations struggling with tribal knowledge
- Codebases lacking documentation

**Free demo available**

*Added: 2026-01-19*

## ARCHITECTURE.md Guide (matklad)

*Source: https://matklad.github.io/2021/02/06/ARCHITECTURE.md.html - Added: 2026-01-19*

For projects in the 10k-200k LOC range, add an ARCHITECTURE document alongside README and CONTRIBUTING.

### Why It Matters

- **10x problem**: Takes 2x longer to write a patch when unfamiliar, but 10x longer to find *where* to change code
- **Mental map gap**: Core devs have internalized the codebase structure; occasional contributors lack this map
- **Low-effort, high-leverage**: Short document that every contributor should read

### Key Principles

1. **Keep it short** - Every contributor reads it; shorter = less likely to go stale
2. **Only stable info** - Don't synchronize with code; revisit a few times per year
3. **Name things, don't link** - Files/modules/types by name; encourage symbol search (links go stale)

### What to Include

1. **Bird's eye overview** - The problem being solved at high level
2. **Codemap** - Coarse-grained modules and relationships
   - Answers "where's the thing that does X?"
   - Answers "what does this thing I'm looking at do?"
   - Like a map of a country, not an atlas of states
3. **Architectural invariants** - Often expressed as *absence* of something (e.g., "model layer doesn't depend on views")
4. **Boundaries** - Between layers and systems; constrains possible implementations
5. **Cross-cutting concerns** - Separate section after the codemap

### Good Example

rust-analyzer's [architecture.md](https://github.com/rust-analyzer/rust-analyzer/blob/master/docs/dev/architecture.md)
