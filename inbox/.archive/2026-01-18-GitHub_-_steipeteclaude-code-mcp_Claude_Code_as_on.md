---
type: link
source: notion
url: https://github.com/steipete/claude-code-mcp
notion_type: Software Repo
tags: ['Running']
created: 2025-05-23T03:35:00.000Z
---

# GitHub - steipete/claude-code-mcp: Claude Code as one-shot MCP server to have an agent in your agent.

## Overview (from Notion)
- The Claude Code MCP server enhances productivity by automating coding tasks, which can free up time for family and personal interests.
- Its capabilities, like direct file editing and version control, streamline the software development process, making it easier to manage projects and meet deadlines.
- The integration of AI in coding could inspire new ways to teach coding to your children, fostering an early interest in technology.
- As a company founder, adopting cutting-edge tools like this can position your business as a tech leader, attracting talent and investment.
- The emphasis on "dangerously-skip-permissions" highlights a need for careful consideration of security practices in software development.
- Alternate views might question the reliance on AI for coding tasks, emphasizing the importance of human oversight and creativity in the development process.
- The complexity of multi-step workflows managed by AI could lead to concerns about losing control over the code, advocating for a balance between automation and human input.

## AI Summary (from Notion)
An MCP server enables running Claude Code in one-shot mode with bypassed permissions, improving file editing and command queuing. It requires Node.js and Claude CLI setup, allowing for efficient code generation, file operations, and version control tasks directly through AI prompts.

## Content (from Notion)

# Claude Code MCP Server

An MCP (Model Context Protocol) server that allows running Claude Code in one-shot mode with permissions bypassed automatically.

Did you notice that Cursor sometimes struggles with complex, multi-step edits or operations? This server, with its powerful unified claude_code tool, aims to make Claude a more direct and capable agent for your coding tasks.

## Overview

This MCP server provides one tool that can be used by LLMs to interact with Claude Code. When integrated with Claude Desktop or other MCP clients, it allows LLMs to:

- Run Claude Code with all permissions bypassed (using -dangerously-skip-permissions)
- Execute Claude Code with any prompt without permission interruptions
- Access file editing capabilities directly
- Enable specific tools by default
## Benefits

- Claude/Windsurf often have trouble editing files. Claude Code is better and faster at it.
- Multiple commands can be queued instead of direct execution. This saves context space so more important stuff is retained longer, fewer compacts happen.
- File ops, git, or other operations don't need costy models. Claude Code is pretty cost effective if you sign up for Antropic Max. You can use Gemini or o3 in Max mode and save costs with offloading tasks to cheaper models.
- Claude has wider system access and can do things that Cursor/Windsurf can't do (or believe they can't), so whenever they are stuck just ask them "use claude code" and it will usually un-stuck them.
- Agents in Agents rules.
## Prerequisites

- Node.js v20 or later (Use fnm or nvm to install)
- Claude CLI installed locally (run it and call /doctor) and dangerously-skip-permissions accepted.
## Configuration

### Environment Variables

-        
- 
## Installation & Usage

The recommended way to use this server is by installing it by using npx.

```plain text
    "claude-code-mcp": {
      "command": "npx",
      "args": [
        "-y",
        "@steipete/claude-code-mcp@latest"
      ]
    },
```

To use a custom Claude CLI binary name, you can specify the environment variable:

```plain text
    "claude-code-mcp": {
      "command": "npx",
      "args": [
        "-y",
        "@steipete/claude-code-mcp@latest"
      ],
      "env": {
        "CLAUDE_CLI_NAME": "claude-custom"
      }
    },
```

## Important First-Time Setup: Accepting Permissions

Before the MCP server can successfully use the claude_code tool, you must first run the Claude CLI manually once with the --dangerously-skip-permissions flag, login and accept the terms.

This is a one-time requirement by the Claude CLI.

```plain text
npm install -g @anthropic-ai/claude-code
```

```plain text
claude --dangerously-skip-permissions
```

Follow the prompts to accept. Once this is done, the MCP server will be able to use the flag non-interactively.

macOS might ask for all kind of folder permissions the first time the tool runs and the first run then fails. Subsequent runs will work.

## Connecting to Your MCP Client

After setting up the server, you need to configure your MCP client (like Cursor or others that use mcp.json or mcp_config.json).

### MCP Configuration File

The configuration is typically done in a JSON file. The name and location can vary depending on your client.

### Cursor

Cursor uses mcp.json.

- macOS: ~/.cursor/mcp.json
- Windows: %APPDATA%\\Cursor\\mcp.json
- Linux: ~/.config/cursor/mcp.json
### Windsurf

Windsurf users use mcp_config.json

- macOS: ~/.codeium/windsurf/mcp_config.json
- Windows: %APPDATA%\\Codeium\\windsurf\\mcp_config.json
- Linux: ~/.config/.codeium/windsurf/mcp_config.json
(Note: In some mixed setups, if Cursor is also installed, these clients might fall back to using Cursor's ~/.cursor/mcp.json path. Prioritize the Codeium-specific paths if using the Codeium extension.)

Create this file if it doesn't exist. Add or update the configuration for claude_code:

## Tools Provided

This server exposes one primary tool:

### claude_code

Executes a prompt directly using the Claude Code CLI with --dangerously-skip-permissions.

Arguments:

- prompt (string, required): The prompt to send to Claude Code.
- options (object, optional): 
Example MCP Request:

```plain text
{
  "toolName": "claude_code:claude_code",
  "arguments": {
    "prompt": "Refactor the function foo in main.py to be async."
  }
}
```

### Examples

Here are some visual examples of the server in action:

### Fixing ESLint Setup

Here's an example of using the Claude Code MCP tool to interactively fix an ESLint setup by deleting old configuration files and creating a new one:

### Listing Files Example

Here's an example of the Claude Code tool listing files in a directory:

## Key Use Cases

This server, through its unified claude_code tool, unlocks a wide range of powerful capabilities by giving your AI direct access to the Claude Code CLI. Here are some examples of what you can achieve:

1.  
1.  
1.  
1.  
1.  
1.   
1. 
1.  
1.  
### Correcting GitHub Actions Workflow

### Complex Multi-Step Operations

This example illustrates claude_code handling a more complex, multi-step task, such as preparing a release by creating a branch, updating multiple files (package.json, CHANGELOG.md), committing changes, and initiating a pull request, all within a single, coherent operation.

CRITICAL: Remember to provide Current Working Directory (CWD) context in your prompts for file system or git operations (e.g., "Your work folder is /path/to/project\n\n...your command...").

## Troubleshooting

- "Command not found" (claude-code-mcp): If installed globally, ensure the npm global bin directory is in your system's PATH. If using npx, ensure npx itself is working.
- "Command not found" (claude or ~/.claude/local/claude): Ensure the Claude CLI is installed correctly. Run claude/doctor or check its documentation.
- Permissions Issues: Make sure you've run the "Important First-Time Setup" step.
- JSON Errors from Server: If MCP_CLAUDE_DEBUG is true, error messages or logs might interfere with MCP's JSON parsing. Set to false for normal operation.
- ESM/Import Errors: Ensure you are using Node.js v20 or later.
For Developers: Local Setup & Contribution

If you want to develop or contribute to this server, or run it from a cloned repository for testing, please see our Local Installation & Development Setup Guide.

## Testing

The project includes comprehensive test suites:

```plain text
# Run all tests
npm test

# Run unit tests only
npm run test:unit

# Run e2e tests (with mocks)
npm run test:e2e

# Run e2e tests locally (requires Claude CLI)
npm run test:e2e:local

# Watch mode for development
npm run test:watch

# Coverage report
npm run test:coverage
```

For detailed testing documentation, see our E2E Testing Guide.

## Configuration via Environment Variables

The server's behavior can be customized using these environment variables:

- CLAUDE_CLI_PATH: Absolute path to the Claude CLI executable. 
- MCP_CLAUDE_DEBUG: Set to true for verbose debug logging from this MCP server. Default: false.
These can be set in your shell environment or within the env block of your mcp.json server configuration (though the env block in mcp.json examples was removed for simplicity, it's still a valid way to set them for the server process if needed).

## Contributing

Contributions are welcome! Please refer to the Local Installation & Development Setup Guide for details on setting up your environment.

Submit issues and pull requests to the GitHub repository.

## License

MIT


