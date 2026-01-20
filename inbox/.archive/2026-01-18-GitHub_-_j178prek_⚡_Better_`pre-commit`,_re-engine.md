---
type: link
source: notion
url: https://github.com/j178/prek
notion_type: Software Repo
tags: ['Running']
created: 2025-09-13T13:41:00.000Z
---

# GitHub - j178/prek: ⚡ Better `pre-commit`, re-engineered in Rust

## Overview (from Notion)
- Efficiency Boost: Prek promises faster execution for pre-commit hooks, saving time that can be redirected towards family or other business ventures.
- Simplicity: A single binary with no dependencies means less setup hassle, allowing you to focus on coding rather than environment management.
- Modern Design: Built in Rust, it reflects a trend towards performance-oriented programming languages, which can inspire new projects or ideas.
- Community Engagement: Early adopters like Airflow and OpenLineage show a growing community around this tool, presenting networking opportunities.
- Sustainability: With its focus on efficiency and reduced resource usage, it aligns with a contemporary awareness of sustainable tech practices.
- Future of Tools: Represents a shift in how developer tools can be designed—focusing on speed and user experience—which could influence your own product development strategies.
- Alternative Views: While some may prefer established tools for their stability, experimenting with new technologies like prek can foster innovation and keep your skills sharp.

## AI Summary (from Notion)
prek is a re-engineered version of pre-commit, built in Rust, designed to be faster and dependency-free. It supports multiple languages and is compatible with existing pre-commit configurations. Key features include a single binary installation, improved performance, and better user experience. While still in development, it has already been adopted by several projects. Installation options include standalone scripts, PyPI, Homebrew, and Cargo.

## Content (from Notion)

# prek

pre-commit is a framework to run hooks written in many languages, and it manages the language toolchain and dependencies for running the hooks.

prek is a reimagined version of pre-commit, built in Rust. It is designed to be a faster, dependency-free and drop-in alternative for it, while also providing some additional long-requested features.

Warning

prek is not production-ready yet, a few subcommands and languages are still in works. But it's already being adopted by some projects, please give it a try - we'd love your feedback!

Current supported languages are python, node, go, docker, docker-image, pygrep, system, script and fail.

## Features

- 🚀 A single binary with no dependencies, does not require Python or any other runtime.
- ⚡ About 10x faster than pre-commit and uses only a third of disk space.
- 🔄 Fully compatible with the original pre-commit configurations and hooks.
- 🐍 Integration with uv for managing Python virtual environments and dependencies.
- 🛠️ Improved toolchain installations for Python, Node.js, Go, Rust and Ruby, shared between hooks.
- 📦 Built-in implementation of some common hooks.
- 🏗️ (TODO) Built-in support for monorepos.
## How to migrate

prek is designed as a drop-in replacement:

- Install prek
- Replace pre-commit with prek in your commands
- Your existing .pre-commit-config.yaml works unchanged
```plain text
$ prek run
trim trailing whitespace.................................................Passed
fix end of files.........................................................Passed
typos....................................................................Passed
cargo fmt................................................................Passed
cargo clippy.............................................................Passed
```

For configuring .pre-commit-config.yaml and writing hooks, you can refer to the pre-commit documentation as prek is fully compatible with it.

## Why prek?

### prek is way faster

- It is about 10x faster than pre-commit and uses only a third of disk space.
- It redesigned how hook environments and toolchains are managed, they are all shared between hooks, which reduces the disk space usage and speeds up the installation process.
- Repositories are cloned in parallel, and hooks are installed in parallel if their dependencies are disjoint.
- It uses uv for creating Python virtualenvs and installing dependencies, which is known for its speed and efficiency.
- It implements some common hooks in Rust, built in prek, which are faster than their Python counterparts.
### prek provides a better user experience

- No need to install Python or any other runtime, just download a single binary.
- No hassle with your Python version or virtual environments, prek automatically installs the required Python version and creates a virtual environment for you.
- (TODO): Built-in support for workspaces (or monorepos), each subproject can have its own .pre-commit-config.yaml file.
- prek run has some improvements over pre-commit run, such as: 
- prek list command lists all available hooks, their ids, and descriptions, providing a better overview of the configured hooks.
- prek provides shell completions for prek run <hook_id> command, making it easier to run specific hooks without remembering their ids.
## Who are using prek?

prek is pretty new, but it is already being used or recommend by some projects and organizations:

- Airflow
- PDM
- basedpyright
- OpenLineage
- Authlib
## Installation

If installed via the standalone installer, prek can update itself to the latest version:

```plain text
$ prek self update
```

## Acknowledgements

This project is heavily inspired by the original pre-commit tool, and it wouldn't be possible without the hard work of the maintainers and contributors of that project.

And a special thanks to the Astral team for their remarkable projects, particularly uv, from which I've learned a lot on how to write efficient and idiomatic Rust code.


