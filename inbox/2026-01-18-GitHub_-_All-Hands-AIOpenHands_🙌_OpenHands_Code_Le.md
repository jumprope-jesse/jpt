---
type: link
source: notion
url: https://github.com/All-Hands-AI/OpenHands
notion_type: Software Repo
tags: ['Running']
created: 2025-10-10T04:15:00.000Z
---

# GitHub - All-Hands-AI/OpenHands: 🙌 OpenHands: Code Less, Make More

## Overview (from Notion)
- AI-Driven Development: OpenHands allows you to automate mundane coding tasks, freeing up time for more creative and strategic work as a founder.
- Community Engagement: Joining their Slack community can connect you with like-minded developers, fostering collaboration and innovation.
- Scalability and Flexibility: Whether you need a quick prototype or a robust application, OpenHands can scale with your needs, catering to both personal projects and business demands.
- Local vs. Cloud Running: The option to run the software locally or in the cloud provides flexibility based on your current projects and resources.
- Educational Opportunity: Explore how AI tools can enhance coding efficiency; this knowledge can be shared with your kids, introducing them to tech at a young age.
- Sustainability in Tech: The focus on eco-friendly practices aligns with a growing trend towards sustainable tech solutions, which can be a valuable lesson for your children.
- Alternate Views: Some may argue that reliance on AI can diminish coding skills; it's essential to balance automation with hands-on learning.

## AI Summary (from Notion)
OpenHands is an AI-powered platform for software development that allows agents to modify code, run commands, and interact with APIs. Users can start with OpenHands Cloud, which offers free credits, or run it locally using a CLI launcher or Docker. The project encourages community contributions and provides resources for troubleshooting, documentation, and joining the community through Slack and GitHub. It is distributed under the MIT License and acknowledges contributions from various open-source projects.

## Content (from Notion)

# OpenHands: Code Less, Make More

Deutsch | Español | français | 日本語 | 한국어 | Português | Русский | 中文

Welcome to OpenHands (formerly OpenDevin), a platform for software development agents powered by AI.

OpenHands agents can do anything a human developer can: modify code, run commands, browse the web, call APIs, and yes—even copy code snippets from StackOverflow.

Learn more at docs.all-hands.dev, or sign up for OpenHands Cloud to get started.

Important

Using OpenHands for work? We'd love to chat! Fill out this short form to join our Design Partner program, where you'll get early access to commercial features and the opportunity to provide input on our product roadmap.

## ☁️ OpenHands Cloud

The easiest way to get started with OpenHands is on OpenHands Cloud, which comes with $20 in free credits for new users.

## 💻 Running OpenHands Locally

### Option 1: CLI Launcher (Recommended)

The easiest way to run OpenHands locally is using the CLI launcher with uv. This provides better isolation from your current project's virtual environment and is required for OpenHands' default MCP servers.

Install uv (if you haven't already):

See the uv installation guide for the latest installation instructions for your platform.

Launch OpenHands:

```plain text
# Launch the GUI server
uvx --python 3.12 --from openhands-ai openhands serve

# Or launch the CLI
uvx --python 3.12 --from openhands-ai openhands
```

You'll find OpenHands running at http://localhost:3000 (for GUI mode)!

### Option 2: Docker

> 

Warning

On a public network? See our Hardened Docker Installation Guide to secure your deployment by restricting network binding and implementing additional security measures.

### Getting Started

When you open the application, you'll be asked to choose an LLM provider and add an API key. Anthropic's Claude Sonnet 4 (anthropic/claude-sonnet-4-20250514) works best, but you have many options.

See the Running OpenHands guide for system requirements and more information.

## 💡 Other ways to run OpenHands

Warning

OpenHands is meant to be run by a single user on their local workstation. It is not appropriate for multi-tenant deployments where multiple users share the same instance. There is no built-in authentication, isolation, or scalability.

If you're interested in running OpenHands in a multi-tenant environment, check out the source-available, commercially-licensed OpenHands Cloud Helm Chart

You can connect OpenHands to your local filesystem, interact with it via a friendly CLI, run OpenHands in a scriptable headless mode, or run it on tagged issues with a github action.

Visit Running OpenHands for more information and setup instructions.

If you want to modify the OpenHands source code, check out Development.md.

Having issues? The Troubleshooting Guide can help.

## 📖 Documentation

To learn more about the project, and for tips on using OpenHands, check out our documentation.

There you'll find resources on how to use different LLM providers, troubleshooting resources, and advanced configuration options.

## 🤝 How to Join the Community

OpenHands is a community-driven project, and we welcome contributions from everyone. We do most of our communication through Slack, so this is the best place to start, but we also are happy to have you contact us on Github:

- Join our Slack workspace - Here we talk about research, architecture, and future development.
- Read or post Github Issues - Check out the issues we're working on, or add your own ideas.
See more about the community in COMMUNITY.md or find details on contributing in CONTRIBUTING.md.

## 📈 Progress

See the monthly OpenHands roadmap here (updated at the maintainer's meeting at the end of each month).

## 📜 License

Distributed under the MIT License, with the exception of the enterprise/ folder. See LICENSE for more information.

## 🙏 Acknowledgements

OpenHands is built by a large number of contributors, and every contribution is greatly appreciated! We also build upon other open source projects, and we are deeply thankful for their work.

For a list of open source projects and licenses used in OpenHands, please see our CREDITS.md file.

## 📚 Cite

```plain text
@inproceedings{
  wang2025openhands,
  title={OpenHands: An Open Platform for {AI} Software Developers as Generalist Agents},
  author={Xingyao Wang and Boxuan Li and Yufan Song and Frank F. Xu and Xiangru Tang and Mingchen Zhuge and Jiayi Pan and Yueqi Song and Bowen Li and Jaskirat Singh and Hoang H. Tran and Fuqiang Li and Ren Ma and Mingzhang Zheng and Bill Qian and Yanjun Shao and Niklas Muennighoff and Yizhe Zhang and Binyuan Hui and Junyang Lin and Robert Brennan and Hao Peng and Heng Ji and Graham Neubig},
  booktitle={The Thirteenth International Conference on Learning Representations},
  year={2025},
  url={https://openreview.net/forum?id=OJd3ayDDoF}
}

```


