# AI-Powered Note-Taking & PKM Tools

Tools that use AI to reduce or eliminate manual organization in personal knowledge management.

**URL:** https://mymind.com/
**Status:** Evaluating / Running
**Category:** Personal Knowledge Management / Second Brain

## Overview

mymind is a privacy-focused bookmarking and note-taking tool that uses AI to automatically organize saved content. The core philosophy: "Remember everything. Organize nothing."

## Key Features

- **No Manual Organization**: AI automatically categorizes and visualizes saved content - no folders, labels, or tags required
- **Intelligent Content Recognition**: Automatically identifies if a link is an article, product, book, recipe, etc. and displays it appropriately
- **Associative Search**: Search by color, keyword, brand, date, or any detail you remember
- **OCR/Image Search**: Can read text in images (memes, handwritten notes, photos) and make them searchable
- **Distraction-Free Reading**: Strips articles of ads, pop-ups, and clutter
- **Quick Notes**: Capture ideas on the go, expand later in Focus Mode
- **Cross-Device Sync**: Always accessible across devices
- **Privacy First**: Strong emphasis on data privacy and ownership

## Design Philosophy

- Visual-first approach for visual thinkers
- Minimal friction for capturing information
- Works with how your brain naturally recalls (associative, visual cues)
- Focused on spending less time organizing, more time doing

## Use Cases

- Saving inspiration and references
- Bookmarking articles for later reading
- Quick note-taking for fleeting ideas
- Visual mood boards and idea collections
- Marketing research and quote collection

## Comparison Notes

Unlike traditional bookmarking tools (Raindrop.io, Pinboard) or note apps (Notion, Obsidian), mymind:
- Removes organizational burden entirely
- Relies on AI + search rather than hierarchy
- Focuses heavily on visual presentation
- Positions as "extension for your mind" vs productivity tool

---

## Grug Notes

**URL:** https://grugnotes.com/
**Category:** Personal Knowledge Management / Daily Notes
**Added:** 2026-01-18

### Overview

Grug Notes is an AI-powered note-taking tool built for simplicity. Philosophy: "Simple daily notes for a complicated world." Write plain text (type or voice), and AI automatically links and organizes.

### Key Features

- **Auto-Linking**: Names, dates, companies auto-link; phone numbers, emails, and other attributes extracted automatically
- **Daily Notes First**: Start with daily notes, dump everything there, system figures out where it belongs
- **Natural Language Search**: Ask "Who do I know in tech that surfs?" or "What's on my training schedule for Monday?"
- **Big Brain Planning**: Multi-model AI creates comprehensive plans from your ideas
- **Visual Diff**: See exactly what AI changed with before/after comparison, accept/reject individual edits
- **Model Flexibility**: Mix and match different AI models for different tasks

### Tech Stack

- Django + MySQL
- Hosted on Google Cloud Run
- Server-rendered HTML with HTMX
- Optimized for cold starts and slow connections
- Multi-page app (back button always works)

### Origin Story

Built by Kamanu Composites, a canoe manufacturing company. In 2020 they made 900,000 face shields and used Roam Research to stay organized. Learned they wanted "the organization without the overhead, the linking without the learning curve."

### Pricing

- 30-day free trial, no credit card
- $7 after trial (one-time? monthly? unclear)

### Comparison to mymind

| Aspect | mymind | Grug Notes |
|--------|--------|------------|
| Primary input | Bookmarks, images, articles | Daily notes, voice/text |
| Organization | Visual boards, no folders | Auto-linking, no folders |
| AI role | Categorization, search | Linking, extraction, Q&A |
| Philosophy | "Remember everything" | "Write stuff down, Grug connects" |
| Price point | Subscription | $7 |

### Why It's Interesting

- **Simplicity obsession**: No formatting, no folders, no categories, no decisions
- **Voice input**: Good for capturing thoughts on the go
- **Q&A interface**: Natural language queries over your notes
- **Indie origin**: Built by non-software company solving their own problem
- **Tech choices**: Django + HTMX is a refreshing alternative to SPA complexity

---

## Capacities

**URL:** https://capacities.io/
**Category:** Personal Knowledge Management / Object-Based Notes
**Added:** 2026-01-18

### Overview

Capacities is a note-taking app built around "objects" (books, people, ideas, meetings) rather than files or folders. The core philosophy: your units of thinking are objects, so your note-taking should work with objects too.

### Key Features

- **Object-Based Approach**: Define types of content (Person, Book, Idea, Meeting) with their own properties and templates. Create instances rather than generic notes.
- **Networked Objects**: Connect objects to each other to build a knowledge graph. A "Meeting" links to "People" who attended and "Ideas" discussed.
- **AI Assistant**: Built-in AI to interact with notes, answer questions, improve writing, and work with predefined commands
- **GDPR Compliant**: European company with encrypted servers, signed URLs for media, 2FA support
- **Free Tier**: Free to use without credit card

### Philosophy

"Our units of thinking are objects such as books, people, conversations, or ideas." Instead of creating generic documents, you create typed objects that naturally structure information and reveal connections.

### Comparison to Other Tools

| Aspect | Capacities | Notion | Obsidian | mymind |
|--------|-----------|--------|----------|--------|
| Primary model | Objects with types | Databases + pages | Files + links | Visual boards |
| Organization | Object relationships | Hierarchical | Graph/backlinks | AI auto-categorize |
| AI role | Writing assistant | Built-in | Plugin-based | Categorization |
| Target user | Structured thinkers | Teams/General | PKM enthusiasts | Visual thinkers |
| Philosophy | "World of objects" | "All-in-one workspace" | "Your second brain" | "Remember everything" |

### When to Consider Capacities

- You think in terms of entities (people, books, projects) not documents
- You want structure without manual folder hierarchies
- You appreciate typed data (like a personal CRM for everything)
- You want built-in AI without plugins or setup

### When to Avoid

- You prefer freeform notes without predefined types
- You want AI to do all organization (mymind, Grug Notes)
- You need heavy developer extensibility (Eidos, Dendron)
- You prefer local-only storage
