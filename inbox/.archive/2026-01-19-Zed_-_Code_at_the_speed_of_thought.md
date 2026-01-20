---
type: link
source: notion
url: https://zed.dev/
notion_type: Software Repo
tags: ['Running']
created: 2024-01-24T21:46:00.000Z
---

# Zed - Code at the speed of thought

## Overview (from Notion)
- Zed can streamline your coding process, saving you time for family while maintaining productivity as a founder.
- The AI-driven code generation allows you to focus on high-level tasks, potentially reducing stress and fostering a better work-life balance.
- Real-time collaboration features could enhance team dynamics, making remote work more engaging and effective.
- The multi-core design ensures responsiveness, which can be crucial when juggling multiple projects or parental duties.
- Unique aspects like CRDTs for collaboration could inspire innovative ways to manage team workflows and code reviews.
- Consider alternate views: some may prefer traditional IDEs for their familiarity and extensive plugin ecosystems, while Zed's cutting-edge approach might feel risky or overwhelming.
- Reflect on the potential of shared coding experiences as a way to mentor junior developers, enriching both your professional and personal life.

## AI Summary (from Notion)
Zed is an advanced code editor that integrates AI for code generation and refactoring, supports collaborative editing in real-time, and features a unique multi-core architecture for enhanced performance. It utilizes a context-free grammar parsing framework for syntax analysis and employs Conflict-Free Replicated Data Types (CRDTs) for seamless collaboration. The platform aims to create a shared software development experience with tools designed for efficiency and responsiveness.

## Content (from Notion)

### Intelligence on tap

Save time and keystrokes by generating code with AI. Zed supports GitHub Copilot out of the box, and you can use GPT-4 generate or refactor code by pressing ctrl-enter and typing a natural language prompt. Interact with the model conversationally without switching context in the built-in assistant panel, then reference your conversation during inline generation.

Zed maintains a full syntax tree for every buffer as you type, enabling precise code highlighting, auto-indent, a searchable outline view, and structural selection. Zed also speaks the Language Server Protocol to provide autocompletion, code navigation, diagnostics, and refactorings.

Keep your fingers on their keys with a searchable command palette, VS Code style default bindings, and Vim-style modal editing. New to relying on shortcuts? Tooltips show key bindings so you work faster next time.

Zed ships with a variety of light and dark themes out of the box. Closer to 1.0 Zed will also provide a way to create your own theme, or load a theme someone else has created.

## Connect with your team

With Zed, multiple developers can navigate and edit within a shared workspace. This makes it easy to have nuanced, real-time conversations about any part of your codebase, whether the code in question was committed last year or hasn't yet been saved to disk.

### A virtual office for software teams

Channels are spaces to discuss, plan, and write software with your team. Each channel has a shared document for taking notes and tracking projects, and channels nest in a hierarchy to keep you organized. Share projects with the channel and use audio or text-based chat to engage collaborators in real time.

More about channels →

### Work with code on any machine

When you join a teammate's project, you can navigate and edit as if the code is on your local machine. Open any file, type with low latency, and interact with language servers. It all works seamlessly, whether you're working with someone at the next desk or on a different continent.

Jump to a teammate's location and follow them around the code, then switch roles and have them follow you. It's a great way to review changes or help a new teammate get oriented in your codebase. You can also use the built-in screen sharing to follow someone outside of Zed to view documentation or experiment with an app in development.

### Designed for the multi-core era

Rust's unique type system lets us parallelize work across multiple cores without compromising application stability. Zed uses copy-on-write data structures and Rust's expressive async primitives to shift CPU-intensive tasks away from the main thread, yielding responsiveness that wouldn’t be possible in a single-threaded editor.

### A principled approach to syntax

Regular expressions are the wrong tool for analyzing context-free languages. That's why we created Tree-sitter, an open-source parsing framework based on the same theoretical foundation used in compilers: context-free grammars. Tree-sitter uses an incremental version of generalized LR parsing, enabling language-aware features for a general-purpose editor that were once only possible in language-specific IDEs.

### Every buffer is a CRDT

Conflict-Free Replicated Data Types, or CRDTs, are a class of eventually-consistent data structures that allow data to be kept in sync in the face of concurrent mutations. In Zed, every buffer is a CRDT by default, which provides a foundation for multiple forms of collaboration. They're also a key component of the multi-threaded architecture that makes Zed a joy to use on your own.

## From the team

We’re Zed Industries, a small and passionate team on a mission to build the world’s best text editor—for you, and for your team.

Zed isn’t our first editor. It’s the culmination of more than a decade of experience building tools for developers.

We created the hackable text editor, Atom, and the pioneering software platform that launched an entirely new generation of desktop apps, Electron.

We also built Tree-sitter, an advanced syntax parsing framework used by the most popular editors in the world. Building tools that matter is in our DNA.

Now, we’re building something new again with that same drive and a new vision. We believe the best software is handcrafted, with unparalleled attention to detail.

We believe software development is better when it’s a shared experience. We believe there’s a better way to write software—and this is just the start of the adventure.


