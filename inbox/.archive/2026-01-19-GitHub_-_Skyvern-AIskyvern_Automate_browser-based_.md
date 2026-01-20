---
type: link
source: notion
url: https://github.com/Skyvern-AI/skyvern
notion_type: Software Repo
tags: ['Running']
created: 2024-03-15T04:06:00.000Z
---

# GitHub - Skyvern-AI/skyvern: Automate browser-based workflows with LLMs and Computer Vision

## AI Summary (from Notion)
- Project Overview: Skyvern is an automation tool for browser-based workflows using LLMs (Large Language Models) and computer vision.
- Key Features:
- Operates on unseen websites without needing custom code.
- Resistant to layout changes, improving reliability over traditional methods.
- Capable of reasoning through complex interactions, enhancing automation capabilities.
- Usage:
- Provides a simple API for automating manual workflows.
- Can be integrated into various applications, from insurance quotes to procurement processes.
- Cloud Version: Offers a managed cloud option that includes anti-bot measures and supports multiple instances for scaling.
- Quickstart Guide: Instructions provided for setting up Skyvern locally, including prerequisites and setup steps.
- Debugging Tools: Features a visualizer for monitoring and debugging interactions on websites.
- Real-World Examples: Showcases practical applications such as navigating government websites and retrieving insurance quotes.
- Future Roadmap: Plans for open-sourcing the core code, integrating UI improvements, and enhancing stability and cost-effectiveness.
- Contributing: Open invitation for contributions and feedback, with a clear contribution guide available.
- Telemetry: Collects usage statistics by default, with an option to opt-out.
- License: Licensed under the AGPL-3.0 License, with specifics provided for core logic versus managed cloud offerings.

## Content (from Notion)

#       

🐉 Automate Browser-based workflows using LLMs and Computer Vision 🐉

Skyvern automates browser-based workflows using LLMs and computer vision. It provides a simple API endpoint to fully automate manual workflows, replacing brittle or unreliable automation solutions.

Traditional approaches to browser automations required writing custom scripts for websites, often relying on DOM parsing and XPath-based interactions which would break whenever the website layouts changed.

Instead of only relying on code-defined XPath interactions, Skyvern adds computer vision and LLMs to the mix to parse items in the viewport in real-time, create a plan for interaction and interact with them.

This approach gives us a few advantages:

1. Skyvern can operate on websites it’s never seen before, as it’s able to map visual elements to actions necessary to complete a workflow, without any customized code
1. Skyvern is resistant to website layout changes, as there are no pre-determined XPaths or other selectors our system is looking for while trying to navigate
1. Skyvern leverages LLMs to reason through interactions to ensure we can cover complex situations. Examples include: 
Want to see examples of Skyvern in action? Jump to #real-world-examples-of-skyvern

# How it works

Skyvern was inspired by the Task-Driven autonomous agent design popularized by BabyAGI and AutoGPT -- with one major bonus: we give Skyvern the ability to interact with websites using browser automation libraries like Playwright.

# Demo

skyvern_demo_video.mp4

# Skyvern Cloud

We offer a managed cloud version of Skyvern that allows you to run Skyvern without having to manage the infrastructure. It allows to you run multiple Skyvern instances in parallel to automate your workflows at scale. In addition, Skyvern cloud comes bundled with a anti-bot detection mechanisms, proxy network, and CAPTCHA solving to allow you to complete more complicated workflows.

Skyvern Cloud is currently in private beta. If you're interested in using Skyvern Cloud, please reach out to us via email

# Quickstart

This quickstart guide will walk you through getting Skyvern up and running on your local machine.

## Prerequisites

Before you begin, make sure you have the following installed:

- Brew (if you're on a Mac)
- Poetry 
Note: Our setup script does these two for you, but they are here for reference.

- Python 3.11 
- PostgreSQL 14 (if you're on a Mac, setup script will install it for you if you have homebrew installed) 
## Setup

1. Clone the repository and navigate to the root directory
1. Run the setup script to install the necessary dependencies and setup your environment 
1. Start the server 
1. You can start sending requests to the server, but we built a simple UI to help you get started. To start the UI, run the following command: 
1. Navigate to http://localhost:8501 in your browser to start using the UI
## Additional Setup for Contributors

If you're looking to contribute to Skyvern, you'll need to install the pre-commit hooks to ensure code quality and consistency. You can do this by running the following command:

```plain text
pre-commit install
```

## Running your first automation

### Executing tasks (UI)

Once you have the UI running, you can start an automation by filling out the fields shown in the UI and clicking "Execute"

### Executing tasks (cURL)

```plain text
curl -X POST -H 'Content-Type: application/json' -H 'x-api-key: {Your local API key}' -d '{
    "url": "https://www.geico.com",
    "webhook_callback_url": "",
    "navigation_goal": "Navigate through the website until you generate an auto insurance quote. Do not generate a home insurance quote. If this page contains an auto insurance quote, consider the goal achieved",
    "data_extraction_goal": "Extract all quote information in JSON format including the premium amount, the timeframe for the quote.",
    "navigation_payload": "{Your data here}",
    "proxy_location": "NONE"
}' http://0.0.0.0:8000/api/v1/tasks

```

## Debugging Skyvern

Skyvern's visualizer allows you to debug every interaction Skyvern takes on the web.

demo_visualizer.mp4

### Tasks, Steps, and Actions

Each API request you sent to Skyvern is called a "task". Each task is made up of "steps" which are the individual actions Skyvern takes to complete the task. Each step is made up of "actions" which are the individual interactions Skyvern takes on a particular website.

Every time you call the API, you will be given a task_id you can use to find a task within the visualizer. Within each task, you'll be able to interact with each step, and see the specific actions Skyvern took to complete the task.

In the screenshot below, we're navigating to finditparts.com and searching for a truck part. You'll see each action it took listed there, alongside the reasoning behind each action.

In addition to the actions suggested by the LLM in text form, Skyvern's visualizer also shows the state of the screen at the time of the action, with a 1:1 action to screenshot mapping. This allows you to see exactly what Skyvern saw when it made a decision, and debug any issues that may have arisen.

# Real-world examples of Skyvern

We love to see how Skyvern is being used in the wild. Here are some examples of how Skyvern is being used to automate workflows in the real world. Please open PRs to add your own examples!

You'll need to have Skyvern running locally if you want to try these examples out. Please run the following command after going through the quickstart guide:

```plain text
./run_skyvern.sh

```

## Automate materials procurement for a manufacturing company

💡 See it in action

```plain text
./run_ui.sh finditparts

```

## Navigating to government websites to register accounts or fill out forms

💡 See it in action

```plain text
./run_ui.sh california_edd

```

## Retrieving insurance quotes from insurance providers in any language

💡 See it in action

```plain text
./run_ui.sh bci_seguros

```

💡 See it in action

```plain text
./run_ui.sh geico

```

# Frequently Asked Questions (FAQs)

### What gets us excited about Skyvern?

Our focus is bringing stability to browser-based workflows. We leverage LLMs to create an AI Agent capable of interacting with websites like you or I would — all via a simple API call.

# Feature Roadmap

This is our planned roadmap for the next few months. If you have any suggestions or would like to see a feature added, please don't hesitate to reach out to us via email or discord.

- Open Source - Open Source Skyvern's core codebase
- [BETA] Workflow support - Allow support to chain multiple Skyvern calls together
- Improved context - Improve Skyvern's ability to understand content around interactable elements by introducing feeding relevant label context through the text prompt
- Cost Savings - Improve Skyvern's stability and reduce the cost of running Skyvern by optimizing the context tree passed into Skyvern
- Self-serve UI - Deprecate the Streamlit UI in favour of a React-based UI component that allows users to kick off new jobs in Skyvern
- Prompt Caching - Introduce a caching layer to the LLM calls to dramatically reduce the cost of running Skyvern (memorize past actions and repeat them!)
- Chrome Viewport streaming - Introduce a way to live-stream the Chrome viewport to the user's browser (as a part of the self-serve UI)
- Past Runs UI - Deprecate the Streamlit UI in favour of a React-based UI that allows you to visualize past runs and their results
- Integrate LLM Observability tools - Integrate LLM Observability tools to allow back-testing prompt changes with specific data sets + visualize the performance of Skyvern over time
- Integrate public datasets - Integrate Skyvern with public benchmark tests to track the quality our models over time
- Workflow UI Builder - Introduce a UI to allow users to build and analyze workflows visually
- Langchain Integration - Create langchain integration in langchain_community to use Skyvern as a "tool".
# Contributing

We welcome PRs and suggestions! Don't hesitate to open a PR/issue or to reach out to us via email or discord. Please have a look at our contribution guide and "Help Wanted" issues to get started!

# Telemetry

By Default, Skyvern collects basic usage statistics to help us understand how Skyvern is being used. If you would like to opt-out of telemetry, please set the SKYVERN_TELEMETRY environment variable to false.

# License

Skyvern's open source repository is supported via a managed cloud. All of the core logic powering Skyvern is available in this open source repository licensed under the AGPL-3.0 License, with the exception of anti-bot measures available in our managed cloud offering.

If you have any questions or concerns around licensing, please contact us and we would be happy to help.


