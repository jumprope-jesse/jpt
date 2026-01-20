---
type: link
source: notion
url: https://github.com/stagewise-io/stagewise
notion_type: Software Repo
tags: ['Running']
created: 2025-08-06T03:02:00.000Z
---

# GitHub - stagewise-io/stagewise: stagewise is the first frontend coding agent for existing production-grade web apps 🪄 -- Lives inside your browser 💻 -- Makes changes in local codebase 🤓 -- Compatible with all kinds of frameworks and setups 💪

## Overview (from Notion)
- The stagewise tool integrates AI into frontend development, potentially streamlining your coding process and saving you time.
- As a father and founder, this could free up hours each week, allowing you to balance work and family life more effectively.
- The real-time context feature means you can get instant feedback, reducing the learning curve for your team or even your kids if they show interest in coding.
- The product's minimalist design aligns with modern aesthetics, which can fit well in your NYC lifestyle, emphasizing both function and style.
- You might appreciate the community aspect, joining a network of developers on Discord for support and collaboration.
- Consider the potential for this tool to enhance productivity without sacrificing quality, giving you more time for creative pursuits or family adventures.
- An alternative view might question reliance on AI, emphasizing the importance of manual coding skills and critical thinking in software development.

## AI Summary (from Notion)
Stagewise is a browser toolbar that connects frontend UI to AI agents for seamless coding. It allows developers to select elements, leave comments, and utilize AI for real-time context. The tool supports various frameworks and offers a quick setup process. Upcoming features include a faster frontend agent, and the project encourages contributions and community support.

## Content (from Notion)

# stagewise

# Visual vibe coding. Right in your codebase.

Important

## 🚀 A 10x Faster Frontend Agent is Coming. The stagewise agent.

We're building a native frontend agent that integrates seamlessly with stagewise - delivering 10x faster UI development with unprecedented accuracy.

Get Early Access to the stagewise agent →

## About the project

stagewise is a browser toolbar that connects your frontend UI to your code ai agents in your code editor.

- 🧠 Select any element(s) in your web app
- 💬 Leave a comment on it
- 💡 Let your AI-Agent do the magic
> 

## ✨ Features

The stagewise Toolbar makes it incredibly easy to edit your frontend code with AI agents:

- ⚡ Works out of the box
- 🧩 Customise and extend functionality with Plugins
- 🧠 Sends DOM elements & more metadata to your AI agent
- 🧪 Comes with examples for React, Vue, Svelte and more
## 📖 Quickstart

### 1. 🧩 Install the extension

Install the extension from the extension store of your code editor:

- Cursor: cursor:extension/stagewise.stagewise-vscode-extension
- VS Code: vscode:extension/stagewise.stagewise-vscode-extension
- Trae: trae:extension/stagewise.stagewise-vscode-extension
- Windsurf: windsurf:extension/stagewise.stagewise-vscode-extension
### 2. 👨🏽‍💻 Install and inject the toolbar (the extension will guide you)

Tip

🪄 AI-Assisted Setup (recommended):

1. In Cursor, Press CMD + Shift + P
1. Enter setupToolbar
1. Execute the command and the toolbar will init automatically 🦄
Or follow the Manual Setup:

Install @stagewise/toolbar:

```plain text
pnpm i -D @stagewise/toolbar
```

Inject the toolbar into your app dev-mode:

```plain text
// 1. Import the toolbar
import { initToolbar } from '@stagewise/toolbar';

// 2. Define your toolbar configuration
const stagewiseConfig = {
  plugins: [],
};

// 3. Initialize the toolbar when your app starts
// Framework-agnostic approach - call this when your app initializes
function setupStagewise() {
  // Only initialize once and only in development mode
  if (process.env.NODE_ENV === 'development') {
    initToolbar(stagewiseConfig);
  }
}

// Call the setup function when appropriate for your framework
setupStagewise();
```

> 

### 3. 🎉 Start dev mode and begin coding!

The toolbar should appear in the bottom right corner of your web app. If not, please reach out via Discord.

### Framework-specific integration examples

For easier integration, we provide framework-specific NPM packages that come with dedicated toolbar components (e.g., <StagewiseToolbar>). You can usually import these from @stagewise/toolbar-[framework-name].

## 🤖 Agent support

## 🛣️ Roadmap

Check out our project roadmap for upcoming features, bug fixes, and progress.

## 📜 License

stagewise is developed by tiq UG (haftungsbeschränkt) and offered under the AGPLv3 license.

For more information on the license model, visit the FAQ about the GNU Licenses.

For use cases that fall outside the scope permitted by the AGPLv3 license, feel free to 📬 Contact Us.

## 🤝 Contributing

We're just getting started and love contributions! Check out our CONTRIBUTING.md guide to get involved. For bugs and fresh ideas, please Open an issue!

## 💻 Test stagewise locally

1. git clone https://github.com/stagewise-io/stagewise && cd stagewise
1. pnpm i && pnpm dev
1. Open the stagewise project in your IDE
1. Uninstall/ Disable the official stagewise extension
1. Press F5 (a new IDE window with the local extension-version installed will open up)
1. Visit http://localhost:3002
> 

## 💬 Community & Support

- 👾 Join our Discord
- 📖 Open an issue on GitHub for dev support.
## 📬 Contact Us

Got questions or want to license stagewise for commercial or enterprise use?

📧 sales@stagewise.io


