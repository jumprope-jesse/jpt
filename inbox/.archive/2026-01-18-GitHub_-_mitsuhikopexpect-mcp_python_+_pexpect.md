---
type: link
source: notion
url: https://github.com/mitsuhiko/pexpect-mcp/
notion_type: Software Repo
tags: 
created: 2025-08-18T13:17:00.000Z
---

# GitHub - mitsuhiko/pexpect-mcp: python + pexpect

## Overview (from Notion)
- The pexpect-mcp tool can enhance your debugging efficiency, allowing you to solve issues in code quickly, which is crucial when balancing work and family time.
- Use this tool to teach your kids about programming; interactive debugging can make coding feel more engaging and less intimidating.
- As a company founder, leveraging AI-assisted debugging could streamline development processes, reducing time spent on troubleshooting and allowing more focus on innovation.
- Living in NYC, consider collaborating with tech meetups or workshops to share insights about tools like pexpect-mcp, fostering a community of learning and support.
- Unique viewpoint: This MCP server embodies the intersection of AI and traditional programming, showcasing how technology evolves to aid human creativity.
- Alternate view: Some may argue that reliance on tools like pexpect could lead to a less hands-on understanding of debugging, emphasizing the importance of balancing tool usage with foundational knowledge.

## AI Summary (from Notion)
The pexpect-mcp is an MCP server that allows remote control of pexpect sessions for debugging and process interaction using Python. It supports interactive debugging with tools like LLDB and GDB, and includes installation instructions, usage examples, and a demo with a buggy C program for practical application. Requirements include Python 3.12.1, pexpect 4.9.0, and mcp 1.13.0.

## Content (from Notion)

# pexpect-mcp

An MCP (Model Context Protocol) server that provides remote pexpect session control for debugging and process interaction.

## Overview

This MCP server enables AI assistants to execute Python code with pexpect functionality, allowing for interactive debugging sessions with tools like LLDB, GDB, and other command-line utilities that require programmatic interaction.

In some sense this is less of a pexpect MCP as one that is just maintaining a stateful Python session.

## Installation

```plain text
uv tool install git+https://github.com/mitsuhiko/pexpect-mcp
```

## Usage

### As an MCP Server

Add to your Claude Code configuration:

```plain text
{
  "mcpServers": {
    "pexpect": {
      "command": "pexpect-mcp"
    }
  }
}
```

### Tool Usage

The server provides a single tool: pexpect_tool

Parameters:

- code (string): Python code to execute with pexpect support
- timeout (optional int): Timeout in seconds (default: 30)
Example Usage:

```plain text
# Start a debugging session
child = pexpect.spawn('lldb ./my-program')
child.expect('(lldb)')

# Run the program
child.sendline('run')
child.expect('(lldb)')
print(child.before.decode())

# Get backtrace
child.sendline('bt')
child.expect('(lldb)')
print(child.before.decode())
```

## Demo

The repository includes a demo with a buggy C program (demo-buggy.c) that can be debugged using LLDB through the pexpect interface. This demonstrates the server's capability for interactive debugging sessions.

```plain text
The program `./demo-buggy` crashes when executed. Use LLDB to:

- Start the program under the debugger
- Identify where and why it crashes
- Examine variables, memory, and call stack
- Report the root cause of the crash

```

## Requirements

- Python ≥ 3.12.1
- pexpect ≥ 4.9.0
- mcp ≥ 1.13.0
## License

See LICENSE file for details.


