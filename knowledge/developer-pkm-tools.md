# Developer-Focused PKM & Note-Taking Tools

Tools designed for developers and technical users who want to manage knowledge within their existing development workflows.

---

## Dendron

**URL:** https://www.dendron.so/
**Type:** VS Code Plugin (Open Source)
**Category:** Personal Knowledge Management / Second Brain
**Added:** 2026-01-18

### Overview

Dendron is an open-source knowledge management system built as a VS Code plugin. It's designed for developers who want to organize, store, and share information efficiently while staying in their IDE.

### Key Features

- **Hierarchical Organization with Schemas**: Schema-based system providing structure without forcing rigid categorization. Define templates and organizational patterns that adapt to your needs.
- **Fast Search and Retrieval**: Quick access with cached indexing - notes are "a few keystrokes away"
- **Flexible Growth**: Notes can evolve from daily journals to scratch notes to full knowledge bases
- **Publishing & Sharing**: Create personal digital gardens, share curated knowledge while keeping some notes private
- **Developer-Friendly**: Native VS Code integration - no context switching for developers

### What Makes It Unique

The standout differentiator is the hierarchical schema system combined with ease of restructuring. Unlike flat-file systems (Obsidian, Roam), Dendron encourages hierarchy but makes restructuring painless. Users report that "the ease of restructuring hierarchies gives you the confidence to just write, safe in the knowledge that you can restructure it later."

### Comparison to Other Tools

| Aspect | Dendron | Obsidian | Notion |
|--------|---------|----------|--------|
| Primary interface | VS Code | Standalone app | Web/Desktop |
| Organization model | Hierarchical schemas | Flat + links | Database pages |
| Target user | Developers | General PKM | Teams/General |
| Linking approach | Hierarchy + links | Graph/backlinks | Relations |
| Publishing | Built-in | Plugin | Native |

### When to Consider Dendron

- You live in VS Code and want notes in the same environment
- You prefer hierarchical organization over pure graph-based linking
- You want schema templates for consistent note structure
- You're building a large knowledge base that needs organizational discipline

### When to Avoid

- You prefer visual graph-based navigation (Obsidian)
- You need rich database features (Notion)
- You want AI to do the organizing (mymind, Grug Notes)
- You don't use VS Code

---

## Johnny.Decimal

**URL:** https://johnnydecimal.com/
**Type:** Organizational System (Method, not software)
**Category:** Personal Knowledge Management / File Organization
**Added:** 2026-01-18

### Overview

Johnny.Decimal is a system for organizing files, projects, and life using a structured numerical ID system. Unlike software tools, it's a method you apply to any storage system (file system, Notion, physical files).

### Core Concept

Everything gets a unique ID in the format `XX.YY`:
- **Areas** (10-99): Ten "shelves" for major life areas (e.g., 10-19 Life Admin, 20-29 Home Business)
- **Categories** (X0-X9): Ten "boxes" per area (e.g., 11 Me, 12 House, 13 Money)
- **IDs** (XX.01-XX.99): Individual folders/items within a category (e.g., 15.23 Travel Insurance)

### Key Principles

- **Hard Limit of Ten**: Never more than 10 areas, 10 categories per area - forces prioritization
- **Numbers Stay Put**: Unlike alphabetical sorting, numbered folders don't move when new ones are added
- **Speakable IDs**: "Where's the travel insurance?" → "Fifteen twenty-three" - easy to communicate
- **Flat Structure**: Maximum three levels (area → category → ID) - no nesting chaos
- **Universal Application**: Same system works for digital files, physical filing, shared drives

### Benefits

- **Muscle Memory**: Positions are stable, you develop intuition for where things are
- **Communication**: Numbers are unambiguous - "check 31.17" is clearer than "it's in the Projects folder somewhere"
- **Constraint as Feature**: The 10-item limit forces you to think about what actually matters
- **Cross-System Consistency**: Same numbering works across Finder, Notion, Google Drive, physical files

### Example Structure

```
10-19 Life Admin
  11 Me
    11.01 Passport
    11.02 Birth certificate
  12 House
    12.11 Lease agreement
    12.12 Utilities setup
  15 Travel
    15.23 Travel insurance
20-29 Home Business
  21 Clients
  22 Accounting
```

### When to Consider Johnny.Decimal

- You have chaos across multiple storage systems and want one organizational principle
- You value structure and predictability over flexibility
- You work with others and need a shared organizational language
- You're frustrated by deep folder hierarchies

### When to Avoid

- You prefer AI-driven organization (mymind, Grug Notes)
- You want graph-based linking (Obsidian, Roam)
- The 10-item limit feels too restrictive for your domain
- You're already happy with your current system

### Comparison to Other Approaches

| Aspect | Johnny.Decimal | Dendron | Obsidian | PARA Method |
|--------|----------------|---------|----------|-------------|
| Structure | Numeric hierarchy | Schema-based hierarchy | Flat + links | Projects/Areas/Resources/Archive |
| Limit enforcement | Hard (max 10) | Soft (schemas) | None | Conceptual |
| Primary interface | Any file system | VS Code | Obsidian app | Any system |
| Philosophy | "Impose constraints" | "Structure with flexibility" | "Everything connects" | "Actionability" |

---

## Eidos

**URL:** https://eidos.space/
**Type:** Web Application (Open Source, Local-First)
**Category:** Personal Knowledge Management / Lifetime Data Management
**Added:** 2026-01-18

### Overview

Eidos is an extensible, local-first framework for managing personal data throughout your lifetime. Everything runs in the browser with no server - data is stored locally in SQLite. Heavy emphasis on privacy, offline capability, and developer extensibility.

### Key Features

- **Browser-Only Architecture**: Entire app runs in-browser, no web server required
- **SQLite Storage**: All data stored in SQLite tables - standard format, accessible by any SQLite client
- **Offline-First**: Works without internet; data stored locally for fast performance
- **AI Integration**: Deep LLM integration for translation, summarization, Q&A. AI can also run offline (download model once)
- **Email Integration**: Each resource has a unique email address - create/update data by sending emails
- **Open Source & Open Format**: Transparent code, standard formats for data portability

### Developer Extensibility

- **Custom Functions (UDF)**: Write JavaScript to extend formula functions
- **Scripts**: Build custom data processing logic in TypeScript/JavaScript
- **Prompt Extension**: Natural language automation - "what you say is what you get"
- **API Access**: Full API for building custom workflows

### Philosophy

"Get your data back from cloud providers and merge them into one place." Focus on:
- Data ownership and control
- Long-term data durability (SQLite outlasts SaaS)
- Privacy (no data leaves your device)
- Flexibility through extensibility

### When to Consider Eidos

- You want true local-first with no server dependency
- You value SQLite's durability and portability over proprietary formats
- You're a developer who wants to extend your PKM with custom scripts
- You want offline AI capabilities
- You're concerned about SaaS longevity ("SaaS may come and go, but SQLite will always be there")

### When to Avoid

- You need real-time collaboration features
- You prefer hosted solutions with automatic sync
- You want AI organization without developer setup (mymind, Grug Notes)
- You need mobile apps (browser-only currently)

### Comparison to Other Tools

| Aspect | Eidos | Obsidian | Notion | Dendron |
|--------|-------|----------|--------|---------|
| Architecture | Browser-only | Desktop app | Cloud | VS Code plugin |
| Data format | SQLite | Markdown files | Proprietary | Markdown files |
| Offline support | Full (including AI) | Full | Limited | Full |
| Server required | No | No | Yes | No |
| AI integration | Built-in, offline-capable | Plugin-based | Native (cloud) | None |
| Extensibility | JS/TS scripts, UDFs | Plugins | API, formulas | Plugins |
| Target user | Privacy-focused developers | PKM enthusiasts | Teams/General | VS Code developers |

---

## Loro - CRDT-Based State Management

**URL:** https://www.loro.dev/
**Type:** JavaScript/Rust Library (Open Source)
**Category:** CRDT / Local-First / Collaboration / State Management
**Added:** 2026-01-19

### Overview

Loro is a high-performance CRDT (Conflict-free Replicated Data Type) library designed to make collaboration effortless in local-first software. It provides rich data structures and algorithms for building applications where multiple users can edit data concurrently, both in real-time and asynchronously, without conflicts.

### Key Features

- **High Performance**: Low memory footprint (3.5 MB for benchmark), CPU-efficient, with compact encoding (244 KB for Automerge trace)
  - Encoding speed: 2.2 ms
  - Decode speed: 1.1 ms
  - Apply time: 10 ms
- **Comprehensive CRDT Support**: Multiple algorithms integrated into one library
- **Time Travel**: Navigate through historical edits - "an antidote to regret"
- **Enhanced Collaboration**: Seamless real-time or asynchronous collaboration with robust version control

### CRDT Algorithms & Data Structures

1. **Basic Data Structures**
   - **List**: Ordered collections
   - **LWW Map**: Last-Write-Win key-value pairs
   - **Tree**: Hierarchical data
   - **Text**: Rich text manipulation

2. **Fugue for Text/List Editing**
   - Novel CRDT algorithm designed to minimize interleaving anomalies when merging concurrent text/list edits
   - Better preservation of user intent during merge operations

3. **Peritext-Inspired Rich Text**
   - Manages rich text CRDTs that excel at merging concurrent style edits
   - Maintains the original intent of each user's input as much as possible
   - See their blog post "Loro's Rich Text CRDT" for details

4. **Moveable Tree for Hierarchical Data**
   - Based on "A Highly-Available Move Operation for Replicated Trees"
   - Simplifies moving and reorganizing directory-like data structures
   - Ideal for applications with hierarchical data manipulation needs

### Performance Benchmarks

Tested on the widely-recognized Automerge document editing trace:
- **Encode Size**: 244 KB (compact)
- **Memory Usage**: 3.5 MB (low footprint)
- **Encoding Speed**: 2.2 ms (fast)
- **Decoding Speed**: 1.1 ms (very fast)
- **Apply Time**: 10 ms (efficient)

### Use Cases

- Collaborative text editors (rich text demo available)
- Real-time document collaboration
- Offline-first applications with sync
- Distributed data structures
- Version-controlled state management
- Applications requiring conflict-free merges

### When to Consider Loro

- You're building local-first software with collaboration features
- You need conflict-free merging of concurrent edits
- Performance is critical (low latency, low memory)
- You want time-travel/version control capabilities
- You need multiple CRDT data structures (not just text)
- You're working with rich text or hierarchical data

### When to Avoid

- You have a centralized, single-writer architecture (CRDTs add complexity)
- You don't need offline support or conflict resolution
- Your data model doesn't fit CRDT patterns
- Simple operational transformation (OT) is sufficient for your use case

### Comparison to Other Collaboration Tools

| Aspect | Loro | Automerge | Yjs | OT (e.g., ShareDB) |
|--------|------|-----------|-----|-------------------|
| Approach | CRDT | CRDT | CRDT | Operational Transform |
| Performance | High (benchmarked) | Moderate | High | Varies |
| Rich text | Peritext-inspired | Basic | Good | Good |
| Tree structures | Moveable Tree algo | Basic | Yes | Limited |
| Time travel | Built-in | Yes | Yes | External |
| Encoding size | Compact (244 KB) | Larger | Compact | N/A |
| Interleaving handling | Fugue algorithm | Standard | Standard | Server-dependent |

### Integration Notes

- JavaScript/TypeScript and Rust support
- Works with local-first architectures
- Can integrate with existing state management
- Supports both synchronous and asynchronous collaboration modes

### Related Tools

- **Automerge**: Another CRDT library, Loro benchmarks against it
- **Yjs**: Popular CRDT library for collaborative editing
- **Eidos** (above): Local-first PKM that could benefit from CRDT integration
- **Electric SQL**: Sync engine for local-first apps (different approach)
