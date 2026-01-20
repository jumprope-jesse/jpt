---
type: link
source: notion
url: https://www.loro.dev/
notion_type: Product Website
tags: 
created: 2024-01-23T14:32:00.000Z
---

# Loro – Reimagine state management with CRDTs

## AI Summary (from Notion)
- Loro Overview
- A tool designed for state management using Conflict-free Replicated Data Types (CRDTs).
- Aims to facilitate seamless collaboration in local-first software.

- Key Features
- High Performance: Low memory usage and CPU efficiency with compact encoding.
- Comprehensive Integration: Supports multiple CRDT algorithms, designed for extensibility.
- Time Travel: Allows users to navigate historical edits, preventing regret over mistakes.
- Enhanced Collaboration: Supports real-time and asynchronous collaboration with robust version control.

- CRDT Support
- Basic data structures like List, LWW Map, Tree, and Text are included for various applications.
- Integration with Fugue for improved text/list editing.
- Rich text management inspired by Peritext, focusing on concurrent style edits.
- Use of Moveable Tree algorithm for hierarchical data manipulation.

- Performance Benchmarks
- Encoding Speed: 2.2 ms
- Encode Size: 244 KB
- Apply Time: 10 ms
- Memory Usage: 3.5 MB
- Decode Speed: 1.1 ms

- Demo Availability: A rich text editor demo is provided to showcase capabilities.

## Content (from Notion)

Implement collaboration effortlessly. Powered by CRDTs.

Built for local-first software.

# ReimagineStateManagementwith

### High Performance

Low memory footprint, CPU-efficient, with compact encoding sizes.

### Comprehensive Integration

Incorporates multiple CRDT algorithms, designed for extensibility.

### Time Travel

An antidote to regret, enabling historical edits traversal.

### Enhanced Collaboration

Enables easy real-time or asynchronous collaboration, integrated with robust version control.

## Rich CRDTs Algorithm Support

### Basic Data Structures

Includes support for List for ordered collections, LWW (Last Write Win) Map for key-value pairs, Tree for hierarchical data, and Text for rich text manipulation, enabling various of applications.

### Text/List Editing with Fugue

Loro integrates Fugue, a novel CRDT algorithm designed to minimize the interleaving anomalies when merging concurrent text/list edits.

### Rich Text with Peritext-like CRDT

Drawing inspiration from Peritext, Loro manages rich text CRDTs that excel at merging concurrent rich text style edits, maintaining the original intent of each user's input as much as possible. Please read our blog,  Loro's Rich Text CRDT, to learn more.

### Hierarchical Data with Moveable Tree

For applications requiring directory-like data manipulation, Loro utilizes the algorithm from A Highly-Available Move Operation for Replicated Trees, simplifying moving and reorganizing hierarchical data structures.

## High-Performance

Benchmarking results for the widely recognized Automerge document editing trace.

## Rich Text Editor Demo


