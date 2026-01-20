---
type: link
source: notion
url: https://github.com/awslabs/mcp/blob/main/src/mcp-lambda-handler/README.md
notion_type: Software Repo
tags: ['Running']
created: 2025-06-04T03:35:00.000Z
---

# mcp/src/mcp-lambda-handler/README.md at main · awslabs/mcp · GitHub

## Overview (from Notion)
- The MCP Lambda Handler module can streamline your projects by simplifying serverless HTTP endpoint creation, saving you time and effort in development.
- As a founder, leveraging serverless architecture allows you to scale applications efficiently without heavy infrastructure management, freeing up resources for innovation.
- The emphasis on flexible session management can enhance user experience in your applications, making them more responsive to user needs.
- Consider the balance between serverless and traditional architectures; while serverless offers scalability, it might introduce complexity in debugging and monitoring.
- The open-source nature of the library encourages community involvement, which can be a unique opportunity for collaboration and networking within the tech space.
- Integrating AWS tools can be beneficial, but also weigh the costs and vendor lock-in against potential benefits to ensure sustainability for your projects.
- The focus on development best practices (like testing and code quality) aligns with maintaining high standards in your work, which is crucial in a competitive market.

## AI Summary (from Notion)
A Python library for creating serverless HTTP handlers for the Model Context Protocol (MCP) using AWS Lambda, featuring pluggable session management and easy deployment. Supports DynamoDB for persistent sessions and includes a quick start guide and development instructions.

## Content (from Notion)

# MCP Lambda Handler Module

A Python library for creating serverless HTTP handlers for the Model Context Protocol (MCP) using AWS Lambda. This library provides a minimal, extensible framework for building MCP HTTP endpoints with pluggable session management support.

## Features

- 🚀 Easy serverless MCP HTTP handler creation using AWS Lambda
- 🔌 Pluggable session management system (NoOp or DynamoDB, or custom backends)
## Quick Start

1. Install the package with development dependencies:
```plain text
pip install -e .[dev]
```

1. Use the handler in your AWS Lambda function:
## Basic Usage

```plain text
from awslabs.mcp_lambda_handler import MCPLambdaHandler

mcp = MCPLambdaHandler(name="mcp-lambda-server", version="1.0.0")

@mcp.tool()
def add_two_numbers(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

def lambda_handler(event, context):
    """AWS Lambda handler function."""
    return mcp.handle_request(event, context)
```

## Session Management

The library provides flexible session management with built-in support for DynamoDB and the ability to create custom session backends. You can use the default stateless (NoOp) session store, or configure a DynamoDB-backed store for persistent sessions.

## Example Architecture for Auth & Session Management

A typical serverless deployment using this library might look like:

- API Gateway: Exposes the /mcp endpoint.
- Lambda Authorizer: Validates authentication tokens (e.g., bearer tokens in the Authorization header).
- MCP Server Lambda: Implements MCP tools and session logic using this library.
- DynamoDB: Stores session data (if using the DynamoDB session backend).
## Development

1. Clone the repository:
```plain text
git clone https://github.com/awslabs/mcp.git
cd mcp/src/mcp-lambda-handler
```

1. Install development dependencies:
```plain text
pip install -e .[dev]
```

1. Run tests:
```plain text
pytest
```

## Contributing

Contributions are welcome! Please see the CONTRIBUTING.md in the monorepo root for guidelines.

## License

This project is licensed under the Apache-2.0 License - see the LICENSE file for details.

## Python Version Support

- Python 3.10+
## Dependencies

Core dependencies:

- python-dateutil >= 2.8.2
Optional dependencies:

- boto3 >= 1.38.1 (for AWS/DynamoDB support)
- botocore >= 1.38.1 (for AWS/DynamoDB support)
Development dependencies:

- pytest >= 8.0.0
- black >= 24.2.0
- isort >= 5.13.0
- flake8 >= 7.0.0
- moto >= 5.0.3 (for AWS mocking in tests)

