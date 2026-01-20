---
type: link
source: notion
url: https://docs.codacy.com/codacy-guardrails/codacy-guardrails-getting-started/
notion_type: Software Repo
tags: ['Running']
created: 2025-06-18T22:11:00.000Z
---

# Getting Started - Codacy docs

## Overview (from Notion)
- Codacy Guardrails can enhance your workflow by ensuring that the code you or your team produce is secure and adheres to quality standards, saving you time on revisions.
- The integration with IDEs like VSCode means you can seamlessly monitor and improve your coding practices without disrupting your development flow.
- Using AI to enforce best practices in real-time can help you instill a culture of quality in your team, which is essential for scaling your company.
- The focus on eco-friendly practices in tech aligns with a growing trend towards sustainability, which can be a unique selling point for your software products.
- Consider the implications of relying on AI for code quality: while it can reduce human error, it may also create a dependency that could stifle creative problem-solving.
- As a founder, leveraging such tools can free up your time for strategic decision-making and mentoring your team instead of getting bogged down in code reviews.
- The potential for real-time feedback can lead to faster iterations and innovation, keeping your product competitive in the fast-paced NYC tech scene.

## AI Summary (from Notion)
Codacy Guardrails is a tool for enforcing code security and quality standards for AI-generated code, integrated into various IDEs. It requires prerequisites like git and node.js, and supports operating systems including macOS, Linux, and Windows (via WSL). Users can install the Codacy extension, activate the Codacy CLI for local analysis, and set up the MCP server for interaction with Codacy tools. Detailed installation steps for different environments and troubleshooting tips are provided.

## Content (from Notion)

Codacy Guardrails is a brand new way of enforcing code security and quality standards for AI-generated code, built into the free Codacy IDE Extension for VSCode, Copilot, Cursor, and Windsurf. Guardrails help developers ship safer, cleaner AI code by applying best practices and blocking insecure patterns while the code is being generated.

Besides real-time AI code scanning, Guardrails users can now prompt all their Codacy findings, without ever leaving the AI chat panel inside their IDE.

New to Codacy Guardrails? Check our blog post

## Prerequisites

- git
- node.js - ensure the npx command runs without issues
- curl
### Supported Operating Systems

- macOS
- Linux
- Windows (via WSL)
Important

For Windows users: Windows WSL (a feature that allows you to run a Linux environment directly on Windows, without the need for a virtual machine or dual-boot setup) is the only way you can use this feature for now, but we're still working to fully support Windows.

### Supported IDEs

- Visual Studio Code
- Cursor
- Windsurf
Note

Visual Studio Code Insiders is recommended for its faster performance and compatibility with Codacy Guardrails. However, since it's a beta version, you may encounter occasional issues.

### Built-in Scanners

- Trivy
- Semgrep
- ESLint
- Pylint
- PMD
- dartanalyzer
- Lizard
## How to install - Quick Guide

### Note for Windows users:

To take full advantage of Codacy Guardrails on Windows, you might need to setup WSL first, check the steps here.

### 1. Download the extension

- Visual Studio Code
- Cursor
- Windsurf
This will open the Codacy Extension in your IDE Marketplace. Click Install

Install Extension

### 2. Install and activate the Codacy CLI for local analysis

Click on the button Install Codacy CLI

Install CLI

It will create a folder in your local repository called .codacy with all needed configuration:

- The configuration from all built-in scanners
- Codacy CLI script to run analysis locally
Note

If you don't want this folder to be part of your repository in future commits but continue working with it locally, please add .codacy to your .gitignore file

### 3. Install MCP Server

### a. Add the Codacy MCP Server

In the Codacy Extension tab, click Add Codacy MCP Server

Add Codacy MCP Server

### b. Check if the Codacy MCP Server is enabled

On the left side menu of the Codacy extension, please make sure that MCP server is set up and ready.

Codacy MCP Server is enabled

### 4. Restart your IDE

## How to install - WSL

### 1. Install or update WSL.

### 2. Install the WSL extension for VSCode.

- Ensure you go through all the installation steps and double check all warnings the extension may show during setup, since your machine may require some extra setup steps.
### 3. Open a WSL Window.

- You can do this by using the WSL extension keyboard shortcut Ctrl + Alt + O and then selecting the option or going to the command palette and selecting WSL: Connect to WSL in New Window.
### 4. Open your project folder in WSL using the command WSL: Open Folder in WSL....

- Note that the path you need to enter is the WSL path, not the Windows one, so for example if you want to open your project that's in C:\Users\your_username\project the equivalent WSL path should be something like /mnt/c/Users/your_username/project.
- To double check your path you can always open WSL directly by pressing Win + R and then typing WSL and pressing enter. There you can check your file structure. Keep in mind that your user folder in WSL (/home/your_username or ~) isn't your user folder in Windows (for example /mnt/c/Users/your_username).
- As an alternative, you can also open directly WSL, open your project folder and then opening VSCode from there with the command code ..
- If you open a project through Windows explorer, it might open in a new (non-WSL) window. Open it via the command palette instead.
### 5. Install curl on your WSL instance if it's not installed already.

- This will depend on the Linux distribution you are using, but for example in Debian and Ubuntu the command will be something like sudo apt update && sudo apt install curl.
- You can do this directly in WSL or in VSCode by going to View > Terminal.
### 6. Now you should be able to install the Codacy extension without issues. Go through the steps here.

- If you already have the extension installed, you will need to enable it for WSL. Check on your Extensions tab.
### 7. After everything is set up, you should now be able to interact with Codacy via Copilot.

- Remember that for you to be able to interact with Codacy MCP server, you must be on the Agent mode of the chat, not the default Ask mode.
- If you're still having issues with the MCP server, try to run the command Preferences: Open User Settings (JSON), look for the Codacy MCP server settings and right on top of it you'll should see a Start option. Click on it and, if unsuccessful, go to View > Debug Console and check for errors. Don't forget to ensure you have node.js and npx installed and set up.
## How to install - Manually

### 1. Install and activate the Codacy CLI for local analysis

### Download

### MacOS (brew)

To install codacy-cli using Homebrew:

```plain text
brew install codacy/codacy-cli-v2/codacy-cli-v2

```

### Linux

For Linux, we rely on the codacy-cli.sh script in the root. To download the CLI, run:

```plain text
bash <(curl -Ls https://raw.githubusercontent.com/codacy/codacy-cli-v2/main/codacy-cli.sh)

```

You can either put the downloaded script in a specific file or create an alias that will download the script and look for changes:

```plain text
alias codacy-cli="bash <(curl -Ls https://raw.githubusercontent.com/codacy/codacy-cli-v2/main/codacy-cli.sh)"

```

### Installation

Before running the analysis, install the specified tools:

```plain text
codacy-cli install

```

### 2. Install MCP Server

If you want to use MCP Server with a NPM package you should download it from here

Important

You can find some limitations using this approach because the AI doesn't automatically analyse the code generated unless there's a rule set for it to do so. When using the IDE extension (VS Code, Cursor, or Windsurf), we create those AI rules for the workspace, but if you are installing the MCP manually, you will need to create those rules by yourself. Let us know if you you plan to use this approach, so we can provide more information

### Setup

### Cursor, Windsurf and Claude Desktop

Depending on what IDE you are connecting the MCP Server to, you can use the following methods:

- Cursor: edit the .cursor/mcp.json file to add the following
- Windsurf: edit the .codeium/windsurf/mcp_config.json file to add the following
- Claude Desktop: edit the claude_desktop_config.json file to add the following
```plain text
{
  "mcpServers": {
    "codacy": {
      "command": "npx",
      "args": ["-y", "@codacy/codacy-mcp"],
      "env": {
        "CODACY_ACCOUNT_TOKEN": "<YOUR_TOKEN>",
        "CODACY_CLI_VERSION": "<VERSION>"
      }
    }
  }
}

```

### VS Code with Copilot

For connecting the MCP Server to Copilot in VS Code, add the following to the global config of the IDE:

```plain text
{
  "mcp": {
    "inputs": [],
    "servers": {
      "codacy": {
        "command": "npx",
        "args": ["-y", "@codacy/codacy-mcp"],
        "env": {
          "CODACY_ACCOUNT_TOKEN": "<YOUR_TOKEN>",
          "CODACY_CLI_VERSION": "<VERSION>"
        }
      }
    }
  }
}

```

You can open the user settings.json file in:

View > Command Palette > Preferences: Open User Settings (JSON)

Or open the general settings.json file directly, which according to your OS should be located in:

- for macOS: ~/Library/Application Support/Code/User/settings.json
- for Windows: %APPDATA%\Code\User\settings.json
- for Linux: ~/.config/Code/User/settings.json
Settings.json in VSCode

Make sure you update the value of CODACY_ACCOUNT_TOKEN with your API token.

a. Above the MCP Server configuration in Settings.json file, you can Click in the command Start

Start MCP Server in VSCode

b. Make sure you have Agent mode enabled: vscode://settings/chat.agent.enabled

c. Open the Copilot chat and switch the mode to Agent. You can check that the MCP server was enabled correctly by clicking on the Select tools icon, which should list all the available Codacy tools.

Copilot Agent with Codacy tools

### Share your feedback 📢

Did this page help you?

Edit this page on GitHub  if you notice something wrong or missing.

If you have a question or need help please contact support@codacy.com.


