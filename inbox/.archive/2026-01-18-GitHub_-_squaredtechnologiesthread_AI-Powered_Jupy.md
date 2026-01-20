---
type: link
source: notion
url: https://github.com/squaredtechnologies/thread
notion_type: Software Repo
tags: ['Running']
created: 2024-06-11T12:54:00.000Z
---

# GitHub - squaredtechnologies/thread: AI-Powered Jupyter Notebook built using React

## AI Summary (from Notion)
- Project Overview: Thread is an AI-powered Jupyter Notebook developed using React that allows users to interact with their code through natural language.

- Key Features:
- Familiar Jupyter Notebook editing experience.
- Natural language code editing and cell generation.
- Context-aware chat sidebar for asking questions.
- Automatic error explanation and fixing.
- Built with a React frontend for accessibility.

- Development:
- Can be run locally for free with an API key.
- Installation via pip install thread-dev and start commands provided.

- Future Development:
- Planned features include inline code suggestions, SQL support, no-code data exploration, UI-based chart creation, notebook collaboration, and Jupyter Widgets support.

- Cloud Integration: Future plans to integrate Thread into a cloud platform for collaborative features and hosting notebooks as web applications.

- Development Instructions: Clear instructions for running the project in development mode, including necessary commands for setting up the environment.

- Contact and Collaboration: Open invitation for suggestions, issues, and partnerships, with contact options provided for interested parties.

## Content (from Notion)

#       

🧵 AI-powered Jupyter Notebook built using React 🧵

Thread is a Jupyter Notebook that combines the experience of OpenAI's code interpreter with the familiar development environment of a Python notebook. With Thread, you can use natural language to generate cells, edit code, ask questions or fix errors all while being able to edit or re-run code as you would in a regular Jupyter Notebook.

Best of all, Thread runs locally, and can be used for free with your own API key. To start:

```plain text
pip install thread-dev

```

To start thread-dev, run the following

```plain text
thread

```

or

```plain text
jupyter thread

```

# Demo

ThreadDemo720.mp4

# Key features

### 1. Familiar Jupyter Notebook editing experience

### 2. Natural language code edits

### 3. Generate cells to answer natural language questions

### 4. Ask questions in a context aware chat sidebar

### 5. Automatically explain or fix errors

### 6. React frontend

- Thread is built from the ground up using React, hopefully making it more accessible to build on top of for a wider range of developers.
# Feature Roadmap

These are some of the features we are hoping to launch in the next few month. If you have any suggestions or would like to see a feature added, please don't hesitate to open an issue or reach out to us via email or discord.

- Add co-pilot style inline code suggestions
- Data warehouse + SQL support
- No code data exploration
- UI based chart creation
- Ability to collaborate on notebooks
- Publish notebooks as shareable webapps
- Add support for Jupyter Widgets
- Add file preview for all file types
# Thread.dev Cloud

Eventually we hope to integrate Thread into a cloud platform that can support collaboration features as well hosting of notebooks as web application. If this sounds interesting to you, we are looking for enterprise design partners to partner with and customize the solution for. If you're interested, please reach out to us via email or join our waitlist.

# Development instructions

To run the repo in development mode, you need to run two terminal commands. One will run Jupyter Server, the other will run the NextJS front end.

To begin, run:

```plain text
yarn install

```

Then in one terminal, run:

```plain text
sh ./run_dev.sh

```

And in another, run:

```plain text
yarn dev

```

Navigate to localhost:3000/thread and you should see your local version of Thread running.

If you would like to develop with the AI features, I would recommend changing API_URL in constants.tsx to point to the production server as we haven't released the proxy to run locally yet.


