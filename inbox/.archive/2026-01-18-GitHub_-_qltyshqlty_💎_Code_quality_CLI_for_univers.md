---
type: link
source: notion
url: https://github.com/qltysh/qlty
notion_type: Software Repo
tags: ['Running']
created: 2025-06-18T22:10:00.000Z
---

# GitHub - qltysh/qlty: 💎 Code quality CLI for universal linting, auto-formatting, security scanning, and maintainability

## Overview (from Notion)
- Qlty CLI can streamline your development process, saving you time and effort in maintaining code quality, which is crucial for a busy parent and entrepreneur.
- With support for over 70 static analysis tools across 40+ languages, it can enhance collaboration with diverse teams, making it easier to manage projects in a polyglot environment.
- The focus on security scanning and maintainability helps mitigate risks in your applications, which is vital in a competitive market like NYC.
- The integration of auto-formatting and linting ensures consistent code quality, reducing bugs and improving team efficiency—important for meeting tight deadlines.
- The tool is free for all uses, offering a cost-effective solution for startups or small businesses looking to maintain high coding standards without the burden of licensing fees.
- Consider the balance between adopting new technologies like Qlty and maintaining a healthy work-life dynamic; automation can help reduce workload but requires initial setup and learning.
- An alternate view might emphasize the potential overwhelm from too many tools; it’s essential to evaluate whether this addition genuinely adds value to your workflow or complicates it.

## AI Summary (from Notion)
Qlty CLI is a free multi-language code quality tool for linting, auto-formatting, maintainability, and security scanning, supporting over 70 static analysis tools across 40+ languages. It allows teams to configure quality checks easily via a .qlty/qlty.toml file and provides features like comprehensive linting, security scanning, and code coverage metrics. The tool can be installed quickly on various platforms and integrates with Git workflows, offering automated feedback and support for numerous plugins.

## Content (from Notion)

## Universal linting, auto-formatting, maintainability, and security scanning

Qlty CLI is a multi-language code quality tool for linting, auto-formatting, maintainability, and security with support for 70+ static analysis tools for 40+ languages and technologies.

With Qlty CLI, polyglot team can take advantage of the best code quality static analysis with fast, consistent, and unified results through a single tool. Configuration is done through a simple .qlty/qlty.toml file in your repository, which can be auto-generated based on the languages you use.

The Qlty CLI is completely free for all use, including for commercial projects, with no limits on contributors.

## 📖 Table of Contents

- ✨ Key Features
- 🚀 Quick Start 
- 🧹 Available Linters
- 📊 Code Quality Metrics
- 🖥️ System Requirements
- 🛟 Help or Feedback
- 🧑‍💻 Contributing
- ⚖️ License
## ✨ Key Features

### What We Do

### How We Do It

💡 Learn more in the Documentation.

### Qlty Software: Code quality and coverage done right

Qlty CLI is part of Qlty Software's comprehensive platform for code quality. Bring code quality into every step of your software development workflow with:

- Qlty CLI -- Polyglot code quality CLI written in Rust
- Qlty Cloud -- Automated code review and quality trends
- Visual Studio Code Extension -- Linting and auto-formatting in your IDE
- GitHub Action -- Run Qlty CLI within your CI workflows
- Chrome and Firefox Extension -- Adds code coverage data to GitHub.com
## 🚀 Quick Start

### Installation

The fastest way to install Qlty CLI is using our installer scripts which install our native binaries:

```plain text
# Install on MacOS or Linux
curl https://qlty.sh | bash


# Install on Windows
powershell -c "iwr https://qlty.sh | iex"
```

We also package the CLI as a Docker image on GitHub Container Registry (GHCR).

Note

The Qlty CLI does not use Docker to run linters. By running linters natively, we achieve maximum performance. The Docker image is provided for situations where running the CLI as a containers is preferred over running it as a native binary.

### Setting up Qlty in a new repository

Setup Qlty within a Git repository:

```plain text
cd my_repo/
qlty init
```

### Usage

### Configuration

Qlty CLI is configured using a .qlty/qlty.toml file in your Git repository. You can generate a default configuration with qlty init and then customize it.

Read our documentation about configuration for more information.

## 🧹 Available Linters

Over 20,000 code quality rules are available via the Qlty CLI through its 60+ linter plugins.

To enable new plugins by adding them to your .qlty/qlty.toml file run:

```plain text
qlty plugins enable <NAME>
```

The full list of plugins is available on GitHub.

## 📊 Code Quality Metrics

The Qlty CLI calculates a variety of code quality metrics which are available through the qlty metrics subcommand and as trends on Qlty Cloud.

Quality metrics are available for C#, Go, Java, JavaScript, Kotlin, PHP, Python, Ruby, Rust, and TypeScript.

## 🖥️ System Requirements

Qlty CLI is available for MacOS, Linux, and Windows on x86 and ARM platforms.

### Additional requirements for PHP linters

Certain PHP linters require a working installation of PHP available in your $PATH. To install PHP, use Homebrew or an alternative method.

## 🛟 Help or Feedback

- Read the documentation
- Join our Discord chat
- Community support via GitHub Discussions
- Feature requests via GitHub Discussions
- Bug reports via GitHub Issues
- Plugin request via GitHub Issues
## 🧑‍💻 Contributing

### Adding plugins

Creating a plugin can be as easy as writing a small plugin definition TOML file. If the tool has a custom output format (instead of a standard like SARIF), then writing a simple output parser in Rust is also needed.

We also happily accept requests for new plugins via GitHub issues.

### Developing the CLI

Developing on Qlty CLI requires a working Rust toolchain and adheres to the standard Rust development process:

```plain text
git clone https://github.com/qltysh/qlty.git
cd qlty
cargo build
cargo test
```

### More information

More information about how to contribute can be found in CONTRIBUTING.md.

Reports of security vulnerabilities should be handled with the process outlined in SECURITY.md.

## ⚖️ License

Qlty CLI is published under a Fair Source license. As Fair Source, the Qlty CLI is free to use (including in commercial contexts), modify, and distribute in accordance with its license.

This code is made available under the Business Source License 1.1 (BSL) and transitions into Open Source via a Delayed Open Source Publication (DOSP). More details are available in LICENSE.md.

### Acknowledgements

We would like to thank all of the developers of code quality tooling like linters and meta-linters as well as everyone who has contributed to the field of open source static analysis. Qlty CLI stands on the shoulders of decades of this excellent work.

Licenses for code incorporated into Qlty CLI can be found in the docs/licenses folder.


