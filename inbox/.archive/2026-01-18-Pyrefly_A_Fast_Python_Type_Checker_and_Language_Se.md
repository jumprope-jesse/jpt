---
type: link
source: notion
url: https://pyrefly.org/
notion_type: Software Repo
tags: ['Running']
created: 2025-09-28T07:24:00.000Z
---

# Pyrefly: A Fast Python Type Checker and Language Server | Pyrefly

## Overview (from Notion)
- Pyrefly's focus on performance can help streamline development processes, freeing up time for family and personal interests.
- The language server features like instant feedback may reduce frustration during coding, allowing for more efficient work-life balance.
- Integration into existing workflows means less disruption and smoother transitions, which is crucial when juggling multiple responsibilities.
- Its gradual adoption policy provides a low-risk way to implement new technology, giving you peace of mind as a founder.
- Consider the potential for fostering a culture of modern coding practices in your team, enhancing collaboration and boosting morale.
- Alternate view: Some might argue that adopting new tools can lead to complexity and resistance from team members who are accustomed to existing systems.
- The emphasis on modern typing can also inspire better coding habits, making your codebase cleaner and easier to maintain, ultimately benefiting your projects.

## AI Summary (from Notion)
Pyrefly is a fast Python type checker and language server designed for large codebases, offering features like high-speed type checking, LSP support for IDEs, and modern typing capabilities. It is currently in alpha development and supports local development and CI pipelines. The document outlines recommendations for integrating Pyrefly into a codebase, including enabling the language server, conducting CI trials, and establishing a gradual adoption policy to maximize benefits while maintaining code quality.

## Content (from Notion)

### Pyrefly overview

Pyrefly is a fast Python type checker and language server focused on large‑codebase performance and rich IDE features.

- What it is: A next‑gen type checker plus LSP server that targets very high throughput for both cold and incremental checks, with modern typing features and strong editor integrations.
- Current status: Alpha, under active development with frequent releases.
### Key capabilities

- Speed at scale: Designed to type check very large projects quickly, with parallelism across many cores and aggressive incremental updates.
- Language Server features: Autocomplete, hover, go‑to definition, diagnostics and quick feedback loops through LSP‑compatible editors.
- Modern typing support: Broad PEP typing coverage, generics, protocols, and continued improvements to type parameter handling in recent releases.
- CLI workflow: A simple command like pyrefly check for batch checks or CI usage.
### Typical use

- Local development: Run the LSP in your editor for instant feedback and navigation.
- CI pipelines: Use the CLI to enforce typing in pull requests with fast end‑to‑end checks.
- Large repos: Benefit from multi‑threaded checks and incremental caching to keep feedback loops tight.
### Performance notes

Public benchmarks on well‑known repos and large internal codebases emphasize multi‑threaded throughput and low‑latency results in editors.

### Installation

- From PyPI: pip install pyrefly (Python 3.8+)
- Then configure editor integration via an LSP client of your choice.
### Project links

- Website and docs: https://pyrefly.org
- GitHub repository and releases: https://github.com/facebook/pyrefly
- PyPI package: https://pypi.org/project/pyrefly
---

### Recommendation: how to integrate Pyrefly into our codebase

A practical, low‑risk path to evaluate and adopt Pyrefly in the monorepo.

1) Developer tooling

- Editor LSP: Enable Pyrefly’s language server for fast diagnostics and navigation. Configure it alongside the current checker so folks can compare signals during the trial.
- Local CLI: Add make targets or scripts, for example:
2) CI trial run

- Shadow job: In CI, add a non‑blocking job that runs pyrefly check on a representative subset first.
- Metrics to capture per run:
3) Gradual adoption policy

- Directory opt‑in: Start with strict mode on a few apps and expand as issues decline. Keep a global baseline that doesn’t block merges initially.
- Allowlist first: Use an include list of packages or modules; move to default‑on later.
- Suppressions: Establish a pattern for local ignores and per‑file pragmas to prevent “warning fatigue.”
4) Config and performance

- Config file: Keep a repo‑root Pyrefly config living next to existing mypy or pyproject settings, documenting rule differences.
- Caching: Ensure CI runners cache Pyrefly’s state between workflow steps to show incremental improvements.
- Parallelism: Set threads to available cores in CI agents to realize speed gains on large modules.
- Exit strategy: Retain mypy/pyright for a period for A/B comparison. Remove overlapping jobs once confident.
5) Codebase hygiene to maximize benefits

- Prefer modern typing syntax: dict[str, Any], list[T], X | Y unions.
- Prioritize public API typing at module boundaries, GraphQL schema types, and ORM models.
- Enforce in PRs: Make Pyrefly checks part of the “green” criteria for changed files in opted‑in packages.
6) Developer experience

- Provide a brief internal doc with “common issues and fixes” for Django ORM, Graphene, task queues, etc.
- Encourage use of LSP features for navigation and instant errors to speed reviews.
7) Decision gates

- Gate 1: Shadow‑run success on a subset
- Gate 2: Make failures blocking for changed files in that subset
- Gate 3: Expand to more apps until backend is covered
- Gate 4: Remove old checker from CI if duplicate signal is no longer valuable

