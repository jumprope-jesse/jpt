---
type: link
source: notion
url: https://github.com/stitionai/devika
notion_type: Software Repo
tags: ['Running']
created: 2024-05-11T02:58:00.000Z
---

# GitHub - stitionai/devika: Devika is an Agentic AI Software Engineer that can understand high-level human instructions, break them down into steps, research relevant information, and write code to achieve the given objective. Devika aims to be a competitive open-source alternative to Devin by Cognition AI.

## AI Summary (from Notion)
- Project Overview: Devika is an open-source Agentic AI software engineer designed to understand high-level human instructions, break them down into actionable steps, and write code accordingly.
- Purpose: Aims to provide a competitive alternative to Cognition AI's Devin, with the goal of matching or exceeding its performance on the SWE-bench benchmarks.
- Development Stage: Currently in early development with many unimplemented features; contributions are encouraged to enhance its capabilities.
- Key Features:
- Supports multiple AI models (Claude 3, GPT-4, etc.) for optimal performance.
- Advanced planning, reasoning, and contextual keyword extraction capabilities.
- Web browsing and information gathering functionalities.
- Natural language interaction and project management features.
- Getting Started: Detailed installation instructions provided, including requirements for Python, NodeJs, and additional libraries.
- Usage Instructions: Step-by-step guide on how to create projects, interact with the AI, and monitor progress.
- Configuration: Requires API keys for various services, including Bing and Google for search capabilities.
- Community Engagement: Encourages contributions and has a support system through Discord and issue tracking for user feedback.
- License: Released under the MIT License, promoting openness and collaboration.
- Interesting Fact: The project is modeled after Devin, an ambitious AI software engineer, aiming to achieve similar levels of performance in software development tasks.

## Content (from Notion)

# 🚀 Devika - Agentic AI Software Engineer 👩‍💻

Important

This project is currently in a very early development/experimental stage. There are a lot of unimplemented/broken features at the moment. Contributions are welcome to help out with the progress!

## Table of Contents

- About
- Key Features
- System Architecture
- Getting Started 
- Configuration
- Contributing
- Help and Support
- License
## About

Devika is an advanced AI software engineer that can understand high-level human instructions, break them down into steps, research relevant information, and write code to achieve the given objective. Devika utilizes large language models, planning and reasoning algorithms, and web browsing abilities to intelligently develop software.

Devika aims to revolutionize the way we build software by providing an AI pair programmer who can take on complex coding tasks with minimal human guidance. Whether you need to create a new feature, fix a bug, or develop an entire project from scratch, Devika is here to assist you.

Note

Devika is modeled after Devin by Cognition AI. This project aims to be an open-source alternative to Devin with an "overly ambitious" goal to meet the same score as Devin in the SWE-bench Benchmarks... and eventually beat it?

## Demos

devika-pygame-demo.mp4

## Key Features

- 🤖 Supports Claude 3, GPT-4, Gemini, Mistral , Groq and Local LLMs via Ollama. For optimal performance: Use the Claude 3 family of models.
- 🧠 Advanced AI planning and reasoning capabilities
- 🔍 Contextual keyword extraction for focused research
- 🌐 Seamless web browsing and information gathering
- 💻 Code writing in multiple programming languages
- 📊 Dynamic agent state tracking and visualization
- 💬 Natural language interaction via chat interface
- 📂 Project-based organization and management
- 🔌 Extensible architecture for adding new features and integrations
## System Architecture

Read README.md for the detailed documentation.

## Getting Started

### Requirements

```plain text
Version's requirements
  - Python >= 3.10 and < 3.12
  - NodeJs >= 18
  - bun

```

- Install uv - Python Package manager download
- Install bun - JavaScript runtime download
- For ollama ollama setup guide (optinal: if you don't want to use the local models then you can skip this step)
- For API models, configure the API keys via setting page in UI.
### Installation

To install Devika, follow these steps:

1. Clone the Devika repository: 
1. Navigate to the project directory: 
1. Create a virtual environment and install the required dependencies (you can use any virtual environment manager): 
1. Install the playwright for browsering capabilities: 
1. Start the Devika server: 
1. if everything is working fine, you see the following output: 
1. Now, for frontend, open a new terminal and navigate to the ui directory: 
1. Access the Devika web interface by opening a browser and navigating to http://127.0.0.1:3001
### how to use

To start using Devika, follow these steps:

1. Open the Devika web interface in your browser.
1. To create a project, click on 'select project' and then click on 'new project'.
1. Select the search engine and model configuration for your project.
1. In the chat interface, provide a high-level objective or task description for Devika to work on.
1. Devika will process your request, break it down into steps, and start working on the task.
1. Monitor Devika's progress, view generated code, and provide additional guidance or feedback as needed.
1. Once Devika completes the task, review the generated code and project files.
1. Iterate and refine the project as desired by providing further instructions or modifications.
## Configuration

Devika requires certain configuration settings and API keys to function properly:

when you first time run Devika, it will create a config.toml file for you in the root directory. You can configure the following settings in the settings page via UI:

-  
-  
Make sure to keep your API keys secure and do not share them publicly. For setting up the Bing and Google search API keys, follow the instructions in the search engine setup

## Contributing

We welcome contributions to enhance Devika's capabilities and improve its performance. To contribute, please see the CONTRIBUTING.md file for steps.

## Help and Support

If you have any questions, feedback, or suggestions, please feel free to reach out to us. you can raise an issue in the issue tracker or join the discussions for general discussions.

We also have a Discord server for the Devika community, where you can connect with other users, share your experiences, ask questions, and collaborate on the project. To join the Devika community Discord server, click here.

## License

Devika is released under the MIT License. See the LICENSE file for more information.

## Star History

We hope you find Devika to be a valuable tool in your software development journey. If you have any questions, feedback, or suggestions, please don't hesitate to reach out. Happy coding with Devika!


