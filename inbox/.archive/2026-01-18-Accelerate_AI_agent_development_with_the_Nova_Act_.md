---
type: link
source: notion
url: https://aws.amazon.com/blogs/aws/accelerate-ai-agent-development-with-the-nova-act-ide-extension/
notion_type: Software Repo
tags: ['Running']
created: 2025-09-28T07:41:00.000Z
---

# Accelerate AI agent development with the Nova Act IDE extension | AWS News Blog

## Overview (from Notion)
- The Nova Act IDE extension could significantly streamline your workflow as a software engineer, making it easier to develop automation agents directly within your preferred coding environment.
- Emphasizing natural language processing means you can quickly prototype ideas, potentially saving you time during development and allowing you to focus more on family and business.
- The integration of real-time testing and debugging features can enhance your productivity, enabling you to deliver robust solutions faster, which is crucial when balancing work with family life.
- The collaborative aspect of the open-source community might provide opportunities for networking and learning, connecting with other like-minded individuals in the tech space.
- Consider how automation can simplify routine tasks at home or in your startup, freeing up precious time for family activities or entrepreneurial growth.
- An alternate view could be the concern over reliance on automation; consider the balance between tech efficiency and the personal touch that family and human interactions bring.
- The accessibility of the Nova Act extension at no cost allows you to explore automation tools without financial risk, encouraging experimentation and innovation.

## AI Summary (from Notion)
The Nova Act extension streamlines the development of browser automation agents directly within IDEs like Visual Studio Code, Kiro, and Cursor. It allows users to create scripts using natural language, customize them in a notebook-style interface, and test them locally. Key features include modular cell-based editing, predefined templates for common tasks, and a chat interface for script generation. The extension is open source, free to use, and aims to enhance productivity in automation workflows.

## Content (from Notion)

---

Today, I’m excited to announce the Nova Act extension — a tool that streamlines the path to build browser automation agents without leaving your IDE. The Nova Act extension integrates directly into IDEs like Visual Studio Code (VS Code), Kiro, and Cursor, helping you to create web-based automation agents using natural language with the Nova Act model.

Here’s a quick look at the Nova Act extension in Visual Studio Code:

The Nova Act extension is built on top of the Amazon Nova Act SDK (preview), our browser automation agents SDK (Software Development Kit). The Nova Act extension transforms traditional workflow development by eliminating context switching between coding and testing environments. You can now build, customize, and test production-grade agent scripts—all within your IDE—using features like natural language based generation, atomic cell-style editing, and integrated browser testing. This unified experience accelerates development velocity for tasks like form filling, QA automation, search, and complex multi-step workflows.

You can start with the Nova Act extension by describing your workflow in natural language to quickly generate an initial agent script. Customize it using the notebook-style builder mode to integrate APIs, data sources, and authentication, then validate it with local testing tools that simulate real-world conditions, including live step-by-step debugging of lengthy multi-step workflows.

Getting started with the Nova Act extensionFirst, I need to install the Nova Act extension from the extension manager in my IDE.

I’m using Visual Studio Code, and after choosing Extensions, I enter Nova Act. Then, I select the extension and choose Install.

To get started, I need to obtain an API key. To do this, I navigate to the Nova Act page and follow the instructions to get the API key. I select Set API Key by opening the Command Palette with Cmd+Shift+P / Ctrl+Shift+P.

After I’ve entered my API key, I can try Builder Mode. This is a notebook-style builder mode that breaks complex automation scripts into modular cells, allowing me to test and debug each step individually before moving to the next.

Here, I can use the Nova Act SDK to build my agent. On the right side, I have a Live view panel to preview my agent’s actions in the browser and an Output panel to monitor execution logs, including the model’s thinking and actions.

To test the Nova Act extension, I choose Run all cells. This will start a new browser instance and act based on the given prompt.

I choose Fullscreen to see how browser automation works.

Another useful feature in Builder Mode is that I can navigate to the Output panel and select the cell to see its logs. This helps me debug or review logs specific to the cell I’m working on.

I can also select a template to get started.

Besides using Builder Mode, I can also chat with Nova Act to create a script for me. To do that, I select the extension and choose Generate Nova Act Script. The Nova Act extension opens a chat dialog in the right panel and automatically creates a script for me.

After I finish creating the script, I can choose Start Builder Mode, and the Nova Act extension will help me create a Python file in Builder Mode. This creates a seamless integration because I can switch between chat capability and Builder Mode.

In the chat interface, I see three workflow modes available:

- Ask: Describe tasks in natural language to generate automation scripts
- Edit: Refine or customize generated scripts before execution
- Agent: Run, monitor, and interact with the AI agent performing the workflow
I can also add Context to provide relevant information about my active documents, instructions, problems, or additional Model Context Protocol (MCP) resources the agent can use, plus a screenshot of the current window. Providing this information helps the agent understand any specific requirements for the automation task.

The Nova Act extension also provides a set of predefined templates that I can access by entering / in the chat. These templates are predefined automation scenarios designed to help quickly generate scripts for common web tasks.

I can use these templates (for example, @novaAct /shopping [my requirements]) to get tailored Python scripts for my workflow. At launch, Nova Act extension provides the following templates:

- /shopping: Automates online shopping tasks (searching, comparing, purchasing)
- /extract: Handles data extraction
- /search: Performs search and information gathering
- /qa: Automates quality assurance and testing workflows
- /formfilling: Completes forms and data entry tasks
This extension transforms my agent development workflow by positioning Nova Act extension as a full-stack agent builder tool—a complete agent IDE for the entire development lifecycle. I can prototype with natural language, customize with modular scripting, and validate with local testing—all without leaving my IDE—ensuring production-grade scripts.

Things to knowHere are key points to note:

- Supported IDEs: At launch, the Nova Act extension is available for Visual Studio Code, Cursor, and Kiro, with additional IDE support planned
- Open source: The Nova Act extension is available under the Apache 2.0 license, allowing for community contributions and customization
- Pricing: The Nova Act extension is available at no charge.
Get started with Nova Act extension by installing it from your IDE’s extension marketplace or visiting the GitHub repository for documentation and examples.

Happy automating!

— Donnie


