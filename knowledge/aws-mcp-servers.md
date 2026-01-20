# AWS MCP Servers (Official awslabs/mcp)

*Source: [GitHub - awslabs/mcp](https://github.com/awslabs/mcp) - Added: 2026-01-18*

## Amazon Q Developer CLI MCP Support

*Source: [AWS What's New](https://aws.amazon.com/about-aws/whats-new/2025/04/amazon-q-developer-cli-model-context-protocol) - April 2025*

Amazon Q Developer CLI officially supports MCP, enabling integration with external tools and APIs for enhanced development workflows. Previously limited to native Q Developer tools, MCP support allows:

- Integration with AWS pre-built MCP servers (see below)
- Any MCP server supporting stdio transport layer
- Orchestration of tasks across native and MCP-based tools
- More customized, contextual responses

This makes Q Developer CLI a first-class MCP client alongside Claude Code, Cursor, and other AI assistants.

## Overview

Official AWS suite of specialized MCP servers that integrate AWS services with AI assistants (Claude Code, Q Developer, Cursor, Windsurf, etc.). Available via `uvx` for easy installation.

## Core MCP Server

The orchestrator for managing other AWS MCP servers.

```json
{
  "awslabs.core-mcp-server": {
    "command": "uvx",
    "args": ["awslabs.core-mcp-server@latest"]
  }
}
```

Features:
- Automatic MCP server management
- Planning and orchestration guidance
- Centralized configuration

## Available Servers by Category

### Documentation & Research

| Server | Purpose |
|--------|---------|
| `awslabs.aws-documentation-mcp-server` | Search AWS docs, get content recommendations, convert to markdown |
| `awslabs.bedrock-kb-retrieval-mcp-server` | Query Bedrock Knowledge Bases with natural language |
| `awslabs.kendra-index-mcp-server` | Query Amazon Kendra indexes for RAG context |
| `awslabs.git-repo-research-mcp-server` | Semantic search in git repos using FAISS + Bedrock embeddings |

### Infrastructure as Code

| Server | Purpose |
|--------|---------|
| `awslabs.cdk-mcp-server` | AWS CDK best practices and construct recommendations |
| `awslabs.terraform-mcp-server` | Terraform with Checkov integration, AWS-IA modules |
| `awslabs.cfn-mcp-server` | CloudFormation CRUDL operations via CloudControl |

### Cost & Observability

| Server | Purpose |
|--------|---------|
| `awslabs.cost-analysis-mcp-server` | Analyze AWS costs, natural language queries, generate reports |

### Databases

| Server | Purpose |
|--------|---------|
| `awslabs.aurora-postgres-mcp-server` | NL to SQL for Aurora Postgres |
| `awslabs.aurora-mysql-mcp-server` | NL to SQL for Aurora MySQL |
| `awslabs.aurora-dsql-mcp-server` | Aurora DSQL queries |
| `awslabs.neptune-mcp-server` | openCypher/Gremlin queries on Neptune |
| `awslabs.documentdb-mcp-server` | MongoDB-compatible queries on DocumentDB |
| `awslabs.dynamodb-mcp-server` | DynamoDB control and data plane operations |
| `awslabs.valkey-mcp-server` | ElastiCache/MemoryDB for Valkey (String, Hash, List, Set, JSON, Streams) |
| `awslabs.memcached-mcp-server` | ElastiCache for Memcached operations |

### Compute & Functions

| Server | Purpose |
|--------|---------|
| `awslabs.lambda-mcp-server` | Run Lambda functions as MCP tools without code changes |

### Messaging

| Server | Purpose |
|--------|---------|
| `awslabs.sns-sqs-mcp-server` | Create topics/queues, publish/subscribe, send/receive messages |
| `awslabs.amazon-mq-mcp-server` | Analyze and provision ActiveMQ/RabbitMQ brokers |

### AI & Media

| Server | Purpose |
|--------|---------|
| `awslabs.nova-canvas-mcp-server` | Image generation with Amazon Nova Canvas |
| `awslabs.diagram-mcp-server` | Generate diagrams using Python diagrams DSL |

### Frontend & Location

| Server | Purpose |
|--------|---------|
| `awslabs.frontend-mcp-server` | React + AWS Amplify + shadcn/ui documentation |
| `awslabs.aws-location-mcp-server` | Geocoding, reverse geocoding, routing, place search |

### Data & Documentation Generation

| Server | Purpose |
|--------|---------|
| `awslabs.synthetic-data-mcp-server` | Generate, validate, manage synthetic data |
| `awslabs.code-doc-gen-mcp-server` | Auto-generate repo documentation |

## Installation

### Prerequisites

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install Python 3.10+
uv python install 3.10
```

### MCP Client Configuration

For Amazon Q CLI (`~/.aws/amazonq/mcp.json`):

```json
{
  "mcpServers": {
    "awslabs.aws-documentation-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.aws-documentation-mcp-server@latest"],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      }
    },
    "awslabs.cost-analysis-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.cost-analysis-mcp-server@latest"],
      "env": {
        "AWS_PROFILE": "your-profile",
        "FASTMCP_LOG_LEVEL": "ERROR"
      }
    },
    "awslabs.cdk-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.cdk-mcp-server@latest"],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      }
    }
  }
}
```

For Claude Code (`~/.config/claude-code/mcp.json`), same format.

### Performance Note

Using `@latest` suffix checks PyPI on every start. For faster startup:
- Remove `@latest` suffix
- Manage cache manually: `uv cache clean awslabs.cdk-mcp-server`
- Update explicitly: `uvx awslabs.cdk-mcp-server@latest`

## Lambda Functions as MCP Tools

The Lambda MCP Server is particularly powerful - expose existing Lambda functions as MCP tools without modifying them:

```json
{
  "awslabs.lambda-mcp-server": {
    "command": "uvx",
    "args": ["awslabs.lambda-mcp-server@latest"],
    "env": {
      "AWS_PROFILE": "your-profile",
      "AWS_REGION": "us-east-1",
      "FUNCTION_PREFIX": "mcp-",
      "FUNCTION_TAG_KEY": "mcp-enabled",
      "FUNCTION_TAG_VALUE": "true"
    }
  }
}
```

The Lambda function description becomes the tool description for the AI.

## Running in Containers

```bash
# Build
docker build --build-arg SERVER_NAME=awslabs.nova-canvas-mcp-server -t nova-canvas-mcp-server .

# Run
docker run -e AWS_PROFILE=your-profile -e AWS_REGION=us-east-1 nova-canvas-mcp-server
```

## MCP Lambda Handler Library

For building custom serverless MCP servers, AWS provides `mcp-lambda-handler`:

```python
from awslabs.mcp_lambda_handler import MCPLambdaHandler

mcp = MCPLambdaHandler(name="my-mcp-server", version="1.0.0")

@mcp.tool()
def my_tool(param: str) -> str:
    """Tool description for the AI."""
    return f"Result: {param}"

def lambda_handler(event, context):
    return mcp.handle_request(event, context)
```

Features:
- Pluggable session management (NoOp, DynamoDB, custom)
- Built-in authentication hooks
- Python 3.10+

See `mcp-protocol-adoption.md` for architecture patterns.

## Key Use Cases

1. **Up-to-date documentation** - AWS docs search ensures current API usage
2. **Cost estimation** - "What would this CDK stack cost monthly?"
3. **IaC best practices** - CDK/Terraform with built-in security scanning
4. **Database queries** - Natural language to SQL for Aurora/Neptune/DynamoDB
5. **Private resource access** - Lambda MCP bridges AI to VPC resources

## Community AWS MCP Servers

### alexei-led/aws-mcp-server

*Source: [GitHub](https://github.com/alexei-led/aws-mcp-server) - v1.0.2 released March 2025*

Generic AWS CLI bridge for MCP - enables natural language interaction with *any* AWS CLI command (vs. the official specialized servers above).

```bash
docker pull ghcr.io/alexei-led/aws-mcp-server:1.0.2
```

Key differences from official AWS MCP:
- **Scope**: Full AWS CLI access vs. purpose-built tools
- **Deployment**: Docker-first vs. uvx
- **Flexibility**: Any AWS operation vs. curated workflows

Use cases:
- "List my S3 buckets" → `aws s3 ls`
- "Create EC2 instance with SSM agent" → Complex multi-step CLI operations
- Quick ad-hoc queries without configuring specialized servers

Trade-off: More flexible but less guardrails than official servers.

## Related

- `mcp-protocol-adoption.md` - MCP ecosystem overview, serverless patterns
- `aws-lambda-powertools-bedrock.md` - Bedrock Agents + Lambda
- `coding-agent-tools.md` - AI coding assistant landscape
