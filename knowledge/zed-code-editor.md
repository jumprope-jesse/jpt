# Zed - High-Performance Code Editor

*Source: https://zed.dev/ - Added: 2026-01-19*

Modern code editor built in Rust with AI integration, real-time collaboration, and multi-core performance. From the creators of Atom, Electron, and Tree-sitter.

## Core Features

### AI Integration

- **Built-in AI assistance**: GitHub Copilot support out of the box
- **GPT-4 integration**: Press `ctrl-enter` for natural language code generation/refactoring
- **Assistant panel**: Conversational interaction with AI without context switching
- **Context preservation**: Reference conversations during inline generation

### Real-Time Collaboration

**Shared workspaces:**
- Multiple developers navigate and edit simultaneously
- Works with uncommitted changes and files not yet saved to disk
- Remote code feels local - open files, type with low latency, interact with language servers
- Works across desks or continents

**Channels:**
- Virtual office spaces for software teams
- Shared documents for notes and project tracking
- Hierarchical organization
- Audio and text-based chat
- Screen sharing

**Follow mode:**
- Jump to teammate's location and follow their navigation
- Switch roles fluidly
- Great for code review and onboarding

### Performance Architecture

**Multi-core design:**
- Built in Rust with parallelization across cores
- Copy-on-write data structures
- Async primitives shift CPU work off main thread
- Responsiveness impossible in single-threaded editors

**Every buffer is a CRDT:**
- Conflict-Free Replicated Data Types by default
- Foundation for multiple collaboration forms
- Key component of multi-threaded architecture
- Eventually-consistent in face of concurrent mutations

### Language Support

**Tree-sitter parsing:**
- Context-free grammar framework (not regex)
- Incremental generalized LR parsing
- Precise syntax highlighting
- Auto-indent
- Searchable outline view
- Structural selection
- Used by most popular editors worldwide

**Language Server Protocol:**
- Autocompletion
- Code navigation
- Diagnostics
- Refactorings

## Keyboard-First Workflow

- Searchable command palette
- VS Code style default bindings
- Vim-style modal editing support
- Tooltips show key bindings for faster learning

## Themes

Ships with light and dark themes. Custom theme support planned for 1.0 release.

## Team & History

**Zed Industries team:**
- Created Atom (hackable text editor)
- Created Electron (desktop app platform)
- Created Tree-sitter (syntax parsing framework)
- Over a decade of developer tools experience

**Philosophy:**
> "We believe the best software is handcrafted, with unparalleled attention to detail. We believe software development is better when it's a shared experience."

## Technical Deep Dive

### Why Tree-sitter

Regular expressions are inappropriate for analyzing context-free languages. Tree-sitter uses:
- Same theoretical foundation as compilers (context-free grammars)
- Incremental parsing for real-time updates
- Language-aware features previously only possible in language-specific IDEs
- Now available for general-purpose editors

### CRDT Implementation

Every buffer maintains CRDT data structure enabling:
- Concurrent edits without conflicts
- Real-time synchronization
- Multi-user collaboration
- Multi-threaded local editing

## Use Cases for Jesse

**Personal productivity:**
- Faster than Electron-based editors (VS Code, Cursor)
- AI assistance for quick tasks
- Vim bindings for keyboard efficiency

**Potential team collaboration:**
- Real-time pair programming without screen share lag
- Channel-based async collaboration
- Could be interesting for remote team dynamics

**Concerns:**
- Newer ecosystem vs VS Code's mature extensions
- May lack specific plugins/integrations needed
- AI features less mature than Claude Code or Cursor

## Comparison to Other Editors

| Feature | Zed | VS Code | Cursor | Claude Code |
|---------|-----|---------|--------|-------------|
| Performance | Rust, multi-core | Electron | Electron | N/A (CLI) |
| Collaboration | Real-time native | Live Share | No | No |
| AI | Copilot, GPT-4 | Copilot | Custom AI | Claude (best) |
| Maturity | Newer | Mature | Growing | Beta |
| Extensions | Growing | Huge | VS Code compat | Skills/MCP |

## Installation & Setup

Not included in original source. Check https://zed.dev/ for current install instructions.

## Related Tools

- **Cursor** - VS Code fork with better AI integration
- **Claude Code** - CLI-first agentic coding (see `claude-code-configuration.md`)
- **VS Code** - Industry standard, massive ecosystem
- **Atom** - Predecessor by same team (deprecated)

## Key Insight

Zed represents a bet that **native performance + collaboration** beats **ecosystem size**. The team's track record (Atom, Electron, Tree-sitter) suggests they understand developer tools deeply, but ecosystem network effects are powerful.

Worth trying for:
- Performance-critical workflows
- Real-time collaboration needs
- Rust/native app enthusiasm

Probably not ideal for:
- Deep VS Code extension dependencies
- Complex agentic workflows (Claude Code better)
- Teams already standardized on other tools
