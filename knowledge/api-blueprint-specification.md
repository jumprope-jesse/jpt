# API Blueprint

API Blueprint is an open-source API specification format focused on design-first API development and collaboration.

## Overview

- **Media type**: `text/vnd.apiblueprint`
- **File extension**: `.apib`
- **License**: MIT (fully open source)
- **Website**: https://apiblueprint.org/

## Key Features

### Design-First Philosophy
Like tests in TDD, API Blueprint acts as a contract for the API. Design and agree on the contract before implementation.

### Concise Syntax
Markdown-based syntax that's accessible to all stakeholders (developers, PMs, customers).

### Data Modeling
Define reusable data structures separately from endpoints:

```apib
# Data Structures

## Blog Post (object)
+ id: 42 (number, required)
+ text: Hello World (string)
+ author (Author) - Author of the blog post.

## Author (object)
+ name: Boba Fett
+ email: fett@intergalactic.com
```

### Modularity
Reuse data structures across multiple endpoints:

```apib
# Blog Posts [/posts]

## Retrieve All Posts [GET]
+ Response 200 (application/json)
    + Attributes (array[Blog Post])
```

## Basic Example

```apib
# GET /message
+ Response 200 (text/plain)

        Hello World!
```

## Ecosystem

- GitHub syntax highlighting for `.apib` files
- Search GitHub: `language:"API Blueprint"`
- Tools for mock servers, documentation generation, and testing
- RFC-based governance (similar to Rust/Django)

## When to Use

- Prototyping new APIs quickly
- Documenting existing APIs
- Facilitating stakeholder collaboration on API design
- Generating mock servers for frontend development
- Contract testing

## Comparison Notes

Alternative to OpenAPI/Swagger with a more human-readable Markdown syntax. Better for collaboration with non-developers but less tooling ecosystem than OpenAPI.

---
*Source: https://apiblueprint.org/ (saved 2025-09)*
