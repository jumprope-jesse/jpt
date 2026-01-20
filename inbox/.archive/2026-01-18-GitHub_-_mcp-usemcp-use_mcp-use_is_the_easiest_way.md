---
type: link
source: notion
url: https://github.com/mcp-use/mcp-use
notion_type: Software Repo
tags: ['Running']
created: 2025-08-01T04:32:00.000Z
---

# GitHub - mcp-use/mcp-use: mcp-use is the easiest way to interact with mcp servers with custom agents

## Overview (from Notion)
- Empowerment through Tech: Leverage MCP-Use to simplify interactions with various tools, enabling you to automate mundane tasks and focus on creative problem-solving.
- Family Engagement: Use the technology to enhance family activities, like planning outings or educational projects, tapping into AI-driven insights for better experiences.
- Entrepreneurial Edge: As a founder, integrating MCP agents can streamline operations, improve efficiency, and enhance customer interactions, giving your startup a competitive advantage.
- Community Building: Connect with fellow tech enthusiasts and share experiences on platforms like GitHub, fostering collaboration and innovation in your local and online communities.
- Flexibility in Work: Embrace the remote capabilities of MCP-Use for flexible working arrangements, balancing professional and family life more effectively.
- Sustainability Focus: Consider the environmental impact of tech choices; utilize sustainable practices in your software projects, aligning with a growing trend towards eco-consciousness in the tech industry.
- Unique Perspectives: Explore the intersection of AI and daily life, questioning how these tools can augment human experiences rather than replace them, promoting a balanced view of technology's role.

## AI Summary (from Notion)
MCP-Use is an open-source library that facilitates connecting any LLM to MCP servers for building custom agents with tool access. Key features include ease of use, support for multiple LLMs, dynamic server selection, and tool access control. Users can quickly set up agents, utilize streaming output, and manage multiple servers simultaneously. The library supports sandboxed execution and provides configuration file support for easy management. Installation instructions and example use cases are provided for various applications, including web browsing and 3D creation.

## Content (from Notion)

# Connect any LLM to any MCP server

🌐 MCP-Use is the open source way to connect any LLM to any MCP server and build custom MCP agents that have tool access, without using closed source or application clients.

💡 Let developers easily connect any LLM to tools like web browsing, file operations, and more.

- Visit the mcp-use.com website to know how to build and deploy MCP agents.
- Visit the mcp-use docs to get started with mcp-use library
💬 Get started quickly - chat with your servers on our hosted version! Try mcp-use chat (beta).

## Features

# Quick start

With pip:

```plain text
pip install mcp-use
```

Or install from source:

```plain text
git clone https://github.com/pietrozullo/mcp-use.git
cd mcp-use
pip install -e .
```

### Installing LangChain Providers

mcp_use works with various LLM providers through LangChain. You'll need to install the appropriate LangChain provider package for your chosen LLM. For example:

```plain text
# For OpenAI
pip install langchain-openai

# For Anthropic
pip install langchain-anthropic
```

For other providers, check the LangChain chat models documentation and add your API keys for the provider you want to use to your .env file.

```plain text
OPENAI_API_KEY=
ANTHROPIC_API_KEY=
```

> 

### Spin up your agent:

```plain text
import asyncio
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from mcp_use import MCPAgent, MCPClient

async def main():
    # Load environment variables
    load_dotenv()

    # Create configuration dictionary
    config = {
      "mcpServers": {
        "playwright": {
          "command": "npx",
          "args": ["@playwright/mcp@latest"],
          "env": {
            "DISPLAY": ":1"
          }
        }
      }
    }

    # Create MCPClient from configuration dictionary
    client = MCPClient.from_dict(config)

    # Create LLM
    llm = ChatOpenAI(model="gpt-4o")

    # Create agent with the client
    agent = MCPAgent(llm=llm, client=client, max_steps=30)

    # Run the query
    result = await agent.run(
        "Find the best restaurant in San Francisco",
    )
    print(f"\nResult: {result}")

if __name__ == "__main__":
    asyncio.run(main())
```

You can also add the servers configuration from a config file like this:

```plain text
client = MCPClient.from_config_file(
        os.path.join("browser_mcp.json")
    )
```

Example configuration file (browser_mcp.json):

```plain text
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"],
      "env": {
        "DISPLAY": ":1"
      }
    }
  }
}
```

For other settings, models, and more, check out the documentation.

## Streaming Agent Output

MCP-Use supports asynchronous streaming of agent output using the astream method on MCPAgent. This allows you to receive incremental results, tool actions, and intermediate steps as they are generated by the agent, enabling real-time feedback and progress reporting.

### How to use

Call agent.astream(query) and iterate over the results asynchronously:

```plain text
async for chunk in agent.astream("Find the best restaurant in San Francisco"):
    print(chunk["messages"], end="", flush=True)
```

Each chunk is a dictionary containing keys such as actions, steps, messages, and (on the last chunk) output. This enables you to build responsive UIs or log agent progress in real time.

### Example: Streaming in Practice

```plain text
import asyncio
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from mcp_use import MCPAgent, MCPClient

async def main():
    load_dotenv()
    client = MCPClient.from_config_file("browser_mcp.json")
    llm = ChatOpenAI(model="gpt-4o")
    agent = MCPAgent(llm=llm, client=client, max_steps=30)
    async for chunk in agent.astream("Look for job at nvidia for machine learning engineer."):
        print(chunk["messages"], end="", flush=True)

if __name__ == "__main__":
    asyncio.run(main())
```

This streaming interface is ideal for applications that require real-time updates, such as chatbots, dashboards, or interactive notebooks.

# Example Use Cases

## Web Browsing with Playwright

```plain text
import asyncio
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from mcp_use import MCPAgent, MCPClient

async def main():
    # Load environment variables
    load_dotenv()

    # Create MCPClient from config file
    client = MCPClient.from_config_file(
        os.path.join(os.path.dirname(__file__), "browser_mcp.json")
    )

    # Create LLM
    llm = ChatOpenAI(model="gpt-4o")
    # Alternative models:
    # llm = ChatAnthropic(model="claude-3-5-sonnet-20240620")
    # llm = ChatGroq(model="llama3-8b-8192")

    # Create agent with the client
    agent = MCPAgent(llm=llm, client=client, max_steps=30)

    # Run the query
    result = await agent.run(
        "Find the best restaurant in San Francisco USING GOOGLE SEARCH",
        max_steps=30,
    )
    print(f"\nResult: {result}")

if __name__ == "__main__":
    asyncio.run(main())
```

## Airbnb Search

```plain text
import asyncio
import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from mcp_use import MCPAgent, MCPClient

async def run_airbnb_example():
    # Load environment variables
    load_dotenv()

    # Create MCPClient with Airbnb configuration
    client = MCPClient.from_config_file(
        os.path.join(os.path.dirname(__file__), "airbnb_mcp.json")
    )

    # Create LLM - you can choose between different models
    llm = ChatAnthropic(model="claude-3-5-sonnet-20240620")

    # Create agent with the client
    agent = MCPAgent(llm=llm, client=client, max_steps=30)

    try:
        # Run a query to search for accommodations
        result = await agent.run(
            "Find me a nice place to stay in Barcelona for 2 adults "
            "for a week in August. I prefer places with a pool and "
            "good reviews. Show me the top 3 options.",
            max_steps=30,
        )
        print(f"\nResult: {result}")
    finally:
        # Ensure we clean up resources properly
        if client.sessions:
            await client.close_all_sessions()

if __name__ == "__main__":
    asyncio.run(run_airbnb_example())
```

Example configuration file (airbnb_mcp.json):

```plain text
{
  "mcpServers": {
    "airbnb": {
      "command": "npx",
      "args": ["-y", "@openbnb/mcp-server-airbnb"]
    }
  }
}
```

## Blender 3D Creation

```plain text
import asyncio
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from mcp_use import MCPAgent, MCPClient

async def run_blender_example():
    # Load environment variables
    load_dotenv()

    # Create MCPClient with Blender MCP configuration
    config = {"mcpServers": {"blender": {"command": "uvx", "args": ["blender-mcp"]}}}
    client = MCPClient.from_dict(config)

    # Create LLM
    llm = ChatAnthropic(model="claude-3-5-sonnet-20240620")

    # Create agent with the client
    agent = MCPAgent(llm=llm, client=client, max_steps=30)

    try:
        # Run the query
        result = await agent.run(
            "Create an inflatable cube with soft material and a plane as ground.",
            max_steps=30,
        )
        print(f"\nResult: {result}")
    finally:
        # Ensure we clean up resources properly
        if client.sessions:
            await client.close_all_sessions()

if __name__ == "__main__":
    asyncio.run(run_blender_example())
```

# Configuration File Support

MCP-Use supports initialization from configuration files, making it easy to manage and switch between different MCP server setups:

```plain text
import asyncio
from mcp_use import create_session_from_config

async def main():
    # Create an MCP session from a config file
    session = create_session_from_config("mcp-config.json")

    # Initialize the session
    await session.initialize()

    # Use the session...

    # Disconnect when done
    await session.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
```

## HTTP Connection Example

MCP-Use supports HTTP connections, allowing you to connect to MCP servers running on specific HTTP ports. This feature is particularly useful for integrating with web-based MCP servers.

Here's an example of how to use the HTTP connection feature:

```plain text
import asyncio
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from mcp_use import MCPAgent, MCPClient

async def main():
    """Run the example using a configuration file."""
    # Load environment variables
    load_dotenv()

    config = {
        "mcpServers": {
            "http": {
                "url": "http://localhost:8931/sse"
            }
        }
    }

    # Create MCPClient from config file
    client = MCPClient.from_dict(config)

    # Create LLM
    llm = ChatOpenAI(model="gpt-4o")

    # Create agent with the client
    agent = MCPAgent(llm=llm, client=client, max_steps=30)

    # Run the query
    result = await agent.run(
        "Find the best restaurant in San Francisco USING GOOGLE SEARCH",
        max_steps=30,
    )
    print(f"\nResult: {result}")

if __name__ == "__main__":
    # Run the appropriate example
    asyncio.run(main())
```

This example demonstrates how to connect to an MCP server running on a specific HTTP port. Make sure to start your MCP server before running this example.

# Multi-Server Support

MCP-Use allows configuring and connecting to multiple MCP servers simultaneously using the MCPClient. This enables complex workflows that require tools from different servers, such as web browsing combined with file operations or 3D modeling.

## Configuration

You can configure multiple servers in your configuration file:

```plain text
{
  "mcpServers": {
    "airbnb": {
      "command": "npx",
      "args": ["-y", "@openbnb/mcp-server-airbnb", "--ignore-robots-txt"]
    },
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"],
      "env": {
        "DISPLAY": ":1"
      }
    }
  }
}
```

## Usage

The MCPClient class provides methods for managing connections to multiple servers. When creating an MCPAgent, you can provide an MCPClient configured with multiple servers.

By default, the agent will have access to tools from all configured servers. If you need to target a specific server for a particular task, you can specify the server_name when calling the agent.run() method.

```plain text
# Example: Manually selecting a server for a specific task
result = await agent.run(
    "Search for Airbnb listings in Barcelona",
    server_name="airbnb" # Explicitly use the airbnb server
)

result_google = await agent.run(
    "Find restaurants near the first result using Google Search",
    server_name="playwright" # Explicitly use the playwright server
)
```

## Dynamic Server Selection (Server Manager)

For enhanced efficiency and to reduce potential agent confusion when dealing with many tools from different servers, you can enable the Server Manager by setting use_server_manager=True during MCPAgent initialization.

When enabled, the agent intelligently selects the correct MCP server based on the tool chosen by the LLM for a specific step. This minimizes unnecessary connections and ensures the agent uses the appropriate tools for the task.

```plain text
import asyncio
from mcp_use import MCPClient, MCPAgent
from langchain_anthropic import ChatAnthropic

async def main():
    # Create client with multiple servers
    client = MCPClient.from_config_file("multi_server_config.json")

    # Create agent with the client
    agent = MCPAgent(
        llm=ChatAnthropic(model="claude-3-5-sonnet-20240620"),
        client=client,
        use_server_manager=True  # Enable the Server Manager
    )

    try:
        # Run a query that uses tools from multiple servers
        result = await agent.run(
            "Search for a nice place to stay in Barcelona on Airbnb, "
            "then use Google to find nearby restaurants and attractions."
        )
        print(result)
    finally:
        # Clean up all sessions
        await client.close_all_sessions()

if __name__ == "__main__":
    asyncio.run(main())
```

# Tool Access Control

MCP-Use allows you to restrict which tools are available to the agent, providing better security and control over agent capabilities:

```plain text
import asyncio
from mcp_use import MCPAgent, MCPClient
from langchain_openai import ChatOpenAI

async def main():
    # Create client
    client = MCPClient.from_config_file("config.json")

    # Create agent with restricted tools
    agent = MCPAgent(
        llm=ChatOpenAI(model="gpt-4"),
        client=client,
        disallowed_tools=["file_system", "network"]  # Restrict potentially dangerous tools
    )

    # Run a query with restricted tool access
    result = await agent.run(
        "Find the best restaurant in San Francisco"
    )
    print(result)

    # Clean up
    await client.close_all_sessions()

if __name__ == "__main__":
    asyncio.run(main())
```

# Sandboxed Execution

MCP-Use supports running MCP servers in a sandboxed environment using E2B's cloud infrastructure. This allows you to run MCP servers without having to install dependencies locally, making it easier to use tools that might have complex setups or system requirements.

## Installation

To use sandboxed execution, you need to install the E2B dependency:

```plain text
# Install mcp-use with E2B support
pip install "mcp-use[e2b]"

# Or install the dependency directly
pip install e2b-code-interpreter
```

You'll also need an E2B API key. You can sign up at e2b.dev to get your API key.

## Configuration

To enable sandboxed execution, use the sandbox parameter when creating your MCPClient:

```plain text
import asyncio
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from mcp_use import MCPAgent, MCPClient
from mcp_use.types.sandbox import SandboxOptions

async def main():
    # Load environment variables (needs E2B_API_KEY)
    load_dotenv()

    # Define MCP server configuration
    server_config = {
        "mcpServers": {
            "everything": {
                "command": "npx",
                "args": ["-y", "@modelcontextprotocol/server-everything"],
            }
        }
    }

    # Define sandbox options
    sandbox_options: SandboxOptions = {
        "api_key": os.getenv("E2B_API_KEY"),  # API key can also be provided directly
        "sandbox_template_id": "base",  # Use base template
    }

    # Create client with sandboxed mode enabled
    client = MCPClient(
        config=server_config,
        sandbox=True,
        sandbox_options=sandbox_options,

    )

    # Create agent with the sandboxed client
    llm = ChatOpenAI(model="gpt-4o")
    agent = MCPAgent(llm=llm, client=client)

    # Run your agent
    result = await agent.run("Use the command line tools to help me add 1+1")
    print(result)

    # Clean up
    await client.close_all_sessions()

if __name__ == "__main__":
    asyncio.run(main())
```

## Sandbox Options

The SandboxOptions type provides configuration for the sandbox environment:

## Benefits of Sandboxed Execution

- No local dependencies: Run MCP servers without installing dependencies locally
- Isolation: Execute code in a secure, isolated environment
- Consistent environment: Ensure consistent behavior across different systems
- Resource efficiency: Offload resource-intensive tasks to cloud infrastructure
# Build a Custom Agent:

You can also build your own custom agent using the LangChain adapter:

```plain text
import asyncio
from langchain_openai import ChatOpenAI
from mcp_use.client import MCPClient
from mcp_use.adapters.langchain_adapter import LangChainAdapter
from dotenv import load_dotenv

load_dotenv()


async def main():
    # Initialize MCP client
    client = MCPClient.from_config_file("examples/browser_mcp.json")
    llm = ChatOpenAI(model="gpt-4o")

    # Create adapter instance
    adapter = LangChainAdapter()
    # Get LangChain tools with a single line
    tools = await adapter.create_tools(client)

    # Create a custom LangChain agent
    llm_with_tools = llm.bind_tools(tools)
    result = await llm_with_tools.ainvoke("What tools do you have available ? ")
    print(result)


if __name__ == "__main__":
    asyncio.run(main())

```

# Debugging

MCP-Use provides a built-in debug mode that increases log verbosity and helps diagnose issues in your agent implementation.

## Enabling Debug Mode

There are two primary ways to enable debug mode:

### 1. Environment Variable (Recommended for One-off Runs)

Run your script with the DEBUG environment variable set to the desired level:

```plain text
# Level 1: Show INFO level messages
DEBUG=1 python3.11 examples/browser_use.py

# Level 2: Show DEBUG level messages (full verbose output)
DEBUG=2 python3.11 examples/browser_use.py
```

This sets the debug level only for the duration of that specific Python process.

Alternatively you can set the following environment variable to the desired logging level:

```plain text
export MCP_USE_DEBUG=1 # or 2
```

### 2. Setting the Debug Flag Programmatically

You can set the global debug flag directly in your code:

```plain text
import mcp_use

mcp_use.set_debug(1)  # INFO level
# or
mcp_use.set_debug(2)  # DEBUG level (full verbose output)
```

### 3. Agent-Specific Verbosity

If you only want to see debug information from the agent without enabling full debug logging, you can set the verbose parameter when creating an MCPAgent:

```plain text
# Create agent with increased verbosity
agent = MCPAgent(
    llm=your_llm,
    client=your_client,
    verbose=True  # Only shows debug messages from the agent
)
```

This is useful when you only need to see the agent's steps and decision-making process without all the low-level debug information from other components.

## Star History

# Contributing

We love contributions! Feel free to open issues for bugs or feature requests. Look at CONTRIBUTING.md for guidelines.

## Contributors

Thanks to all our amazing contributors!

## Top Starred Dependents

# Requirements

- Python 3.11+
- MCP implementation (like Playwright MCP)
- LangChain and appropriate model libraries (OpenAI, Anthropic, etc.)
# License

MIT

# Citation

If you use MCP-Use in your research or project, please cite:

```plain text
@software{mcp_use2025,
  author = {Zullo, Pietro},
  title = {MCP-Use: MCP Library for Python},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/pietrozullo/mcp-use}
}
```


