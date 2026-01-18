---
type: link
source: notion
url: https://github.com/aws/mcp-proxy-for-aws
notion_type: Software Repo
tags: ['Running']
created: 2025-11-01T12:46:00.000Z
---

# GitHub - aws/mcp-proxy-for-aws: AWS MCP Proxy Server

## Overview (from Notion)
- The MCP Proxy for AWS simplifies interactions with AWS services, making it easier to integrate advanced technology into your projects.
- As a software engineer and company founder, leveraging such tools can enhance productivity and innovation in your business.
- The lightweight setup allows for rapid deployment, which is crucial for keeping pace with the fast-moving tech landscape in NYC.
- Its focus on security with SigV4 authentication is vital for protecting sensitive data, especially in a startup environment.
- The use of Python and Docker aligns with modern development practices, providing flexibility and scalability for your projects.
- Consider the potential for integrating AI tools with this proxy, which could streamline workflows and improve efficiency.
- An alternate view might be the complexity it introduces for less tech-savvy users; ensuring your team is on board with such tools is essential.
- Balancing the use of cutting-edge technology with family time might require setting clear boundaries on your work hours and project commitments.

## AI Summary (from Notion)
The MCP Proxy for AWS is a lightweight bridge between MCP clients and AWS MCP servers, facilitating SigV4 authentication and dynamic tool discovery. Prerequisites include Python 3.10+, the uv package manager, and AWS CLI configuration. Installation can be done via PyPi, local repository, or Docker. Configuration parameters and optional environment variables are detailed for setup. Development and contribution guidelines are provided, alongside resources for understanding SigV4. Users must implement proper security controls and IAM management when using this package.

## Content (from Notion)

# MCP Proxy for AWS

## Overview

The MCP Proxy for AWS serves as a lightweight, client-side bridge between MCP clients (AI assistants and developer tools) and backend AWS MCP servers.

The proxy handles SigV4 authentication using local AWS credentials and provides dynamic tool discovery, making it ideal for developers who want access to AWS Hosted SigV4 secured MCP Servers without complex gateway setups.

## Prerequisites

- Install Python 3.10+
- Install the uv package manager
- Install and configure the AWS CLI with credentials
- (Optional, for docker users) Install Docker Desktop
## Installation

### Using PyPi

```plain text
# Run the server
uvx mcp-proxy-for-aws@latest <SigV4 MCP endpoint URL>

```

### Using Local Repository

```plain text
git clone https://github.com/aws/mcp-proxy-for-aws.git
cd mcp-proxy-for-aws
uv run mcp_proxy_for_aws/server.py <SigV4 MCP endpoint URL>

```

### Using Docker

```plain text
# Build the Docker image
docker build -t mcp-proxy-for-aws .

```

## Configuration Parameters

## Optional Environment Variables

Set the environment variables for the MCP Proxy for AWS:

```plain text
# Credentials through profile
export AWS_PROFILE=<aws_profile>

# Credentials through parameters
export AWS_ACCESS_KEY_ID=<access_key_id>
export AWS_SECRET_ACCESS_KEY=<secret_access_key>
export AWS_SESSION_TOKEN=<session_token>

# AWS Region
export AWS_REGION=<aws_region>

```

## Setup Examples

Add the following configuration to your MCP client config file (e.g., for Amazon Q Developer CLI, edit ~/.aws/amazonq/mcp.json): Note Add your own endpoint by replacing <SigV4 MCP endpoint URL>

### Running from local - using uv

```plain text
{
  "mcpServers": {
    "<mcp server name>": {
      "disabled": false,
      "type": "stdio",
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/mcp_proxy_for_aws",
        "run",
        "server.py",
        "<SigV4 MCP endpoint URL>",
        "--service",
        "<your service code>",
        "--profile",
        "default",
        "--region",
        "us-east-1",
        "--read-only",
        "--log-level",
        "INFO",
      ]
    }
  }
}

```

### Using Docker

```plain text
{
  "mcpServers": {
    "<mcp server name>": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "--volume",
        "/full/path/to/.aws:/app/.aws:ro",
        "mcp-proxy-for-aws",
        "<SigV4 MCP endpoint URL>"
      ],
      "env": {}
    }
  }
}

```

## Development & Contributing

For development setup, testing, and contribution guidelines, see:

- DEVELOPMENT.md - Development environment setup and testing
- CONTRIBUTING.md - How to contribute to this project
Resources to understand SigV4:

- https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html
- SigV4: https://github.com/boto/botocore/blob/develop/botocore/signers.py
- SigV4a: https://github.com/aws-samples/sigv4a-signing-examples/blob/main/python/sigv4a_sign.py
## License

Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. Licensed under the Apache License, Version 2.0 (the "License").

## Disclaimer

LLMs are non-deterministic and they make mistakes, we advise you to always thoroughly test and follow the best practices of your organization before using these tools on customer facing accounts. Users of this package are solely responsible for implementing proper security controls and MUST use AWS Identity and Access Management (IAM) to manage access to AWS resources. You are responsible for configuring appropriate IAM policies, roles, and permissions, and any security vulnerabilities resulting from improper IAM configuration are your sole responsibility. By using this package, you acknowledge that you have read and understood this disclaimer and agree to use the package at your own risk.


