---
type: link
source: notion
url: https://github.com/awslabs/mcp
notion_type: Software Repo
tags: ['Running']
created: 2025-06-04T03:27:00.000Z
---

# GitHub - awslabs/mcp: AWS MCP Servers — specialized MCP servers that bring AWS best practices directly to your development workflow

## Overview (from Notion)
- Streamlined Development: The AWS MCP servers can significantly enhance your software development workflow, making it easier to implement best practices and access up-to-date documentation without sifting through extensive resources.
- AI Integration: Leveraging AI through these servers can automate routine tasks, allowing you to focus on creative aspects of your projects or spend more time with family.
- Collaboration Opportunities: These tools enable you to collaborate more effectively with remote teams, fostering innovation while balancing work and family life.
- Cost Efficiency: Use the Cost Analysis MCP Server to gain insights into project expenses, helping you make more informed financial decisions for your startup.
- Experimentation with Emerging Technologies: Explore cutting-edge advancements in AI and cloud services, positioning your company at the forefront of technology trends.
- Flexibility and Scalability: The framework allows for rapid scaling of your applications as your business grows, aligning with your entrepreneurial ambitions.
- Community Engagement: Contributing to open-source projects and the AWS community can enhance your professional network and lead to mentorship opportunities for your children in technology.
- Alternate Viewpoint: Some may argue that reliance on automated systems can lead to a loss of fundamental programming skills or critical thinking, emphasizing the importance of maintaining a balance between technology and traditional methods.

## AI Summary (from Notion)
AWS MCP Servers enhance development workflows by integrating AI applications with AWS services, providing improved output quality, access to up-to-date documentation, and automation of workflows for cloud-native development.

## Content (from Notion)

# AWS MCP Servers

A suite of specialized MCP servers that help you get the most out of AWS, wherever you use MCP.

## Table of Contents

- AWS MCP Servers 
## What is the Model Context Protocol (MCP) and how does it work with AWS MCP Servers?

> 

An MCP Server is a lightweight program that exposes specific capabilities through the standardized Model Context Protocol. Host applications (such as chatbots, IDEs, and other AI tools) have MCP clients that maintain 1:1 connections with MCP servers. Common MCP clients include agentic AI coding assistants (like Q Developer, Cline, Cursor, Windsurf) as well as chatbot applications like Claude Desktop, with more clients coming soon. MCP servers can access local data sources and remote services to provide additional context that improves the generated outputs from the models.

AWS MCP Servers use this protocol to provide AI applications access to AWS documentation, contextual guidance, and best practices. Through the standardized MCP client-server architecture, AWS capabilities become an intelligent extension of your development environment or AI application.

AWS MCP servers enable enhanced cloud-native development, infrastructure management, and development workflows—making AI-assisted cloud computing more accessible and efficient.

The Model Context Protocol is an open source project run by Anthropic, PBC. and open to contributions from the entire community. For more information on MCP, you can find further documentation here

### Why MCP Servers?

MCP servers enhance the capabilities of foundation models (FMs) in several key ways:

- 
- 
- 
- 
## Available Servers

This monorepo contains the following MCP servers:

### Core MCP Server

A server for managing and coordinating other AWS Labs MCP servers.

- Automatic MCP Server Management
- Planning and guidance to orchestrate AWS Labs MCP Servers
- UVX Installation Support
- Centralized Configuration
Learn more | Documentation

### AWS Documentation MCP Server

A server for accessing AWS documentation and best practices.

- Search Documentation using the official AWS search API
- Get content recommendations for AWS documentation pages
- Convert documentation to markdown format
Learn more | Documentation

### Amazon Kendra Index MCP Server

A server for listing and querying Amazon Kendra Indexes

- List the Kendra indexes in your account.
- Query Kendra indexes with natural language to give additional RAG context to your AI tool.
Learn more | Documentation

### Amazon Bedrock Knowledge Bases Retrieval MCP Server

A server for accessing Amazon Bedrock Knowledge Bases.

- Discover knowledge bases and their data sources
- Query knowledge bases with natural language
- Filter results by data source
- Rerank results
Learn more | Documentation

### AWS CDK MCP Server

A server for AWS CDK best practices.

- AWS CDK project analysis and assistance
- CDK construct recommendations
- Infrastructure as Code best practices
Learn more | Documentation

### Cost Analysis MCP Server

A server for AWS Cost Analysis.

- Analyze and visualize AWS costs
- Query cost data with natural language
- Generate cost reports and insights
Learn more | Documentation

### Amazon Nova Canvas MCP Server

A server for generating images using Amazon Nova Canvas.

- Text-based image generation with customizable parameters
- Color-guided image generation with specific palettes
- Workspace integration for saving generated images
- AWS authentication through profiles
Learn more | Documentation

### AWS Diagram MCP Server

A server for seamlessly creating diagrams using the Python diagrams package DSL.

- Generate professional diagrams using Python code
- Support for AWS architecture, sequence diagrams, flow charts, and class diagrams
- Customize diagram appearance, layout, and styling
- Code scanning to ensure secure diagram generation
Learn more | Documentation

### AWS CloudFormation MCP Server

A server to manage AWS resources via cloudcontrol. This allows you to perform CRUDL operations on any AWS resources in your AWS account

- This server acts as a bridge between MCP clients and AWS, allowing foundation models (FMs) to read and manage resources in your AWS account.
- This can be used, for example, to create an AWS::S3::Bucket, list any AWS::Lambda::Function, etc.
Learn more | Documentation

### AWS Lambda MCP Server

A server to select and run AWS Lambda function as MCP tools without code changes.

- This server acts as a bridge between MCP clients and AWS Lambda functions, allowing foundation models (FMs) to access and run Lambda functions as tools.
- This can be used, for example, to access private resources such as internal applications and databases without the need to provide public network access.
- This approach allows an MCP client to use other AWS services, private networks, and the public internet.
- The Lambda function description is used by MCP to describe the tool and should guide the FMs on when (what does the function provide?) and how (which parameters it needs? which syntax?) to use it.
Learn more | Documentation

### Amazon SNS / SQS MCP Server

A server for Amazon SNS / SQS.

- Create SNS / SQS Topics and Queues.
- Subscribe, PublishMessages to SNS Topics.
- Send and receive messages from / to Queues.
- Modify Topic / Queue Attributes
Learn more | Documentation

### AWS Terraform MCP Server

A server for AWS Terraform best practices.

- Security-First Development Workflow
- Checkov Integration
- AWS and AWSCC Provider Documentation
- AWS-IA GenAI Modules
- Terraform Workflow Execution
Learn more | Documentation

### Frontend MCP Server

A server that provides specialized documentation for modern web application development with AWS.

- Comprehensive documentation on React with AWS integrations
- Topics include AWS Amplify authentication, React Router, and shadcn/ui
- Best practices for building AWS-powered React applications
Learn more | Documentation

### Amazon ElastiCache / MemoryDB for Valkey MCP Server

A server that provides natural language interface to interact with Amazon ElastiCache Valkey datastores, enabling AI agents to efficiently manage and search data. This MCP server can be used with Amazon MemoryDB Valkey datastores.

- Natural language interface for data operations
- Comprehensive data type support (String, Hash, List, Set, Sorted Set)
- Advanced features like Streams, JSON documents
- Secure connections with SSL/TLS and cluster mode support
- Connection pooling and efficient resource management
Learn more | Documentation

### Amazon ElastiCache for Memcached MCP Server

A server that provides natural language interface to interact with Amazon ElastiCache Memcached caches, enabling AI agents to efficiently manage and search cached data.

- Natural language interface for cache operations
- Comprehensive command support (Get, Set, Remove, Touch, CAS, Increment, Decrement)
- Secure connections with SSL/TLS
- Connection pooling and efficient resource management
Learn more | Documentation

### AWS Location Service MCP Server

A server for accessing AWS Location Service capabilities, focusing on place search, geographical coordinates, and route planning.

- Search for places using geocoding
- Get details for specific places by PlaceId
- Reverse geocode coordinates to addresses
- Search for places near a location
- Search for places that are currently open
- Calculate routes between locations with turn-by-turn directions
- Optimize waypoints for efficient routing
Learn more

### Git Repo Research MCP Server

A server for researching Git repositories using semantic search.

- Repository Indexing with FAISS and Amazon Bedrock embeddings
- Semantic Search within repositories
- Repository Structure Analysis
- GitHub Repository Search in AWS organizations
- File Access with text and binary support
Learn more | Documentation

### Code Documentation Generation MCP Server

A server that automatically generates comprehensive documentation for code repositories.

- Automated documentation generation based on repository analysis
- AWS architecture diagram integration with AWS Diagrams MCP Server
- Multiple document types (README, API, Backend, Frontend)
- Interactive documentation creation workflow for AI assistants
Learn more | Documentation

### Amazon Aurora Postgres MCP Server

A server for Aurora Postgres.

- Converting human-readable questions and commands into structured Postgres-compatible SQL queries and executing them against the configured Aurora Postgres database
- Fetch table columns and comments from Postgres using RDS Data API
Learn more | Documentation

### Amazon Aurora MySql MCP Server

A server for Aurora MySql.

- Converting human-readable questions and commands into structured MySQL-compatible SQL queries and executing them against the configured Aurora MySQL database.
- Fetch table schema
Learn more | Documentation

### Amazon Neptune MCP Server

A server for interacting with Amazon Neptune graph database.

- Run openCypher/Gremlin queries on a Neptune Database
- Run openCypher queries on Neptune Analytics
- Get the schema of the graph
Learn more | Documentation

### Amazon DocumentDB MCP Server

A server for interacting with Amazon DocumentDB clusters, Amazon's MongoDB-compatible document database service.

- Connect to DocumentDB clusters with SSL/TLS support
- Execute queries, aggregations, and CRUD operations
- Analyze collection schema and document structure
- Manage databases and collections
- Get database and collection statistics
- Optimize operations with query planning and execution statistics
Learn more | Documentation

### Amazon MQ MCP Server

A server for Amazon MQ.

- Analyze existing Amazon MQ for ActiveMQ and RabbitMQ brokers .
- Provision new Amazon MQ for ActiveMQ and RabbitMQ broker instances.
Learn more | Documentation

### Synthetic Data MCP Server

A server for generating, validating, and managing synthetic data.

- Business-Driven Generation: Generate synthetic data instructions based on business descriptions
- Safe Pandas Code Execution: Run pandas code in a restricted environment with automatic DataFrame detection
- JSON Lines Validation: Validate and convert JSON Lines data to CSV format
- Data Validation: Validate data structure, referential integrity, and save as CSV files
- Referential Integrity Checking: Validate relationships between tables
- Data Quality Assessment: Identify potential issues in data models (3NF validation)
- Storage Integration: Load data to various storage targets (S3) with support for multiple formats and configurations
Learn more | Documentation

### Amazon Aurora DSQL MCP Server

An AWS Labs Model Context Protocol (MCP) server for Aurora DSQL

- Converting human-readable questions and commands into structured Postgres-compatible SQL queries and executing them against the configured Aurora DSQL database.
Learn more | Documentation

### Amazon DynamoDB MCP Server

A server for interacting with Amazon DynamoDB

- Control Plane operations like table creation, table update, global secondary index, streams, global table management, backup, restore, etc.
- Data Plane operations like put, get, update, query and scan.
Learn more | Documentation

## MCP AWS Lambda Handler Module

A Python library for creating serverless HTTP handlers for the Model Context Protocol (MCP) using AWS Lambda. This module provides a flexible framework for building MCP HTTP endpoints with pluggable session management, including built-in DynamoDB support.

Features:

- Easy serverless MCP HTTP handler creation using AWS Lambda
- Pluggable session management system
- Built-in DynamoDB session backend support
- Customizable authentication and authorization
- Example implementations and tests
See src/mcp-lambda-handler/README.md for full usage, installation, and development instructions.

## Use Cases for the Servers

For example, you can use the AWS Documentation MCP Server to help your AI assistant research and generate up-to-date code for any AWS service, like Amazon Bedrock Inline agents. Alternatively, you could use the CDK MCP Server or the Terraform MCP Server to have your AI assistant create infrastructure-as-code implementations that use the latest APIs and follow AWS best practices. With the Cost Analysis MCP Server, you could ask "What would be the estimated monthly cost for this CDK project before I deploy it?" or "Can you help me understand the potential AWS service expenses for this infrastructure design?" and receive detailed cost estimations and budget planning insights. The Valkey MCP Server enables natural language interaction with Valkey data stores, allowing AI assistants to efficiently manage data operations through a simple conversational interface. For example, you can use the AWS Documentation MCP Server to help your AI assistant research and generate up-to-date code for any AWS service, like Amazon Bedrock Inline agents. Alternatively, you could use the CDK MCP Server or the Terraform MCP Server to have your AI assistant create infrastructure-as-code implementations that use the latest APIs and follow AWS best practices. With the Cost Analysis MCP Server, you could ask "What would be the estimated monthly cost for this CDK project before I deploy it?" or "Can you help me understand the potential AWS service expenses for this infrastructure design?" and receive detailed cost estimations and budget planning insights. The Valkey MCP Server enables natural language interaction with Valkey data stores, allowing AI assistants to efficiently manage data operations through a simple conversational interface.

## Installation and Setup

Each server has specific installation instructions. Generally, you can:

1. Install uv from Astral
1. Install Python using uv python install 3.10
1. Configure AWS credentials with access to required services
1. Add the server to your MCP client configuration
Example configuration for Amazon Q CLI MCP (~/.aws/amazonq/mcp.json):

```plain text
{
  "mcpServers": {
    "awslabs.core-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.core-mcp-server@latest"],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR",
      }
    },
    "awslabs.nova-canvas-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.nova-canvas-mcp-server@latest"],
      "env": {
        "AWS_PROFILE": "your-aws-profile",
        "AWS_REGION": "us-east-1",
        "FASTMCP_LOG_LEVEL": "ERROR"
      }
    },
    "awslabs.bedrock-kb-retrieval-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.bedrock-kb-retrieval-mcp-server@latest"],
      "env": {
        "AWS_PROFILE": "your-aws-profile",
        "AWS_REGION": "us-east-1",
        "FASTMCP_LOG_LEVEL": "ERROR"
      }
    },
    "awslabs.cost-analysis-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.cost-analysis-mcp-server@latest"],
      "env": {
        "AWS_PROFILE": "your-aws-profile",
        "FASTMCP_LOG_LEVEL": "ERROR"
      }
    },
    "awslabs.cdk-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.cdk-mcp-server@latest"],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      }
    },
    "awslabs.aws-documentation-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.aws-documentation-mcp-server@latest"],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "disabled": false,
      "autoApprove": []
    },
    "awslabs.lambda-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.lambda-mcp-server@latest"],
      "env": {
        "AWS_PROFILE": "your-aws-profile",
        "AWS_REGION": "us-east-1",
        "FUNCTION_PREFIX": "your-function-prefix",
        "FUNCTION_LIST": "your-first-function, your-second-function",
        "FUNCTION_TAG_KEY": "your-tag-key",
        "FUNCTION_TAG_VALUE": "your-tag-value"
      }
    },
    "awslabs.terraform-mcp-server": {
       "command": "uvx",
       "args": ["awslabs.terraform-mcp-server@latest"],
       "env": {
         "FASTMCP_LOG_LEVEL": "ERROR"
       },
       "disabled": false,
       "autoApprove": []
     },
    "awslabs.frontend-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.frontend-mcp-server@latest"],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "disabled": false,
      "autoApprove": []
    },
    "awslabs.valkey-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.valkey-mcp-server@latest"],
      "env": {
        "VALKEY_HOST": "127.0.0.1",
        "VALKEY_PORT": "6379",
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "autoApprove": [],
      "disabled": false
    },
    "awslabs.valkey-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.valkey-mcp-server@latest"],
      "env": {
        "VALKEY_HOST": "127.0.0.1",
        "VALKEY_PORT": "6379",
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "autoApprove": [],
      "disabled": false
    },
    "awslabs.aws-location-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.aws-location-mcp-server@latest"],
      "env": {
        "AWS_PROFILE": "your-aws-profile",
        "AWS_REGION": "us-east-1",
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "disabled": false,
      "autoApprove": []
    },
    "awslabs.memcached-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.memcached-mcp-server@latest"],
      "env": {
        "MEMCACHED_HOST": "127.0.0.1",
        "MEMCACHED_PORT": "11211",
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "autoApprove": [],
      "disabled": false
    },
    "awslabs.memcached-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.memcached-mcp-server@latest"],
      "env": {
        "MEMCACHED_HOST": "127.0.0.1",
        "MEMCACHED_PORT": "11211",
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "autoApprove": [],
      "disabled": false
    },
    "awslabs.git-repo-research-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.git-repo-research-mcp-server@latest"],
      "env": {
        "AWS_PROFILE": "your-aws-profile",
        "AWS_REGION": "us-east-1",
        "FASTMCP_LOG_LEVEL": "ERROR",
        "GITHUB_TOKEN": "your-github-token"
      },
      "disabled": false,
      "autoApprove": []
    },
    "awslabs.cloudformation": {
      "command": "uvx",
      "args": ["awslabs.cfn-mcp-server@latest"],
      "env": {
        "AWS_PROFILE": "your-aws-profile",
      },
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

See individual server READMEs for specific requirements and configuration options.

Note about performance when using uvx "@latest" suffix:

Using the "@latest" suffix checks and downloads the latest MCP server package from pypi every time you start your MCP clients, but it comes with a cost of increased initial load times. If you want to minimize the initial load time, remove "@latest" and manage your uv cache yourself using one of these approaches:

- uv cache clean <tool>: where {tool} is the mcp server you want to delete from cache and install again (e.g.: "awslabs.lambda-mcp-server") (remember to remove the '<>').
- uvx <tool>@latest: this will refresh the tool with the latest version and add it to the uv cache.
### Running MCP servers in containers

This example uses docker with the "awslabs.nova-canvas-mcp-server and can be repeated for each MCP server

-  
-  
-  
### Getting Started with Cline and Amazon Bedrock

### Getting Started with Cursor

### Getting Started with Windsurf

## Samples

Ready-to-use examples of AWS MCP Servers in action are available in the samples directory. These samples provide working code and step-by-step guides to help you get started with each MCP server.

## Documentation

Comprehensive documentation for all servers is available on our documentation website.

Documentation for each server:

- Core MCP Server
- Amazon Bedrock Knowledge Bases Retrieval MCP Server
- AWS CDK MCP Server
- Cost Analysis MCP Server
- Amazon Nova Canvas MCP Server
- AWS Diagram MCP Server
- Amazon ElastiCache/MemoryDB Valkey MCP Server erver/)
- Amazon ElastiCache Memcached MCP Server
- Amazon ElastiCache/MemoryDB Valkey MCP Server erver/)
- Amazon ElastiCache Memcached MCP Server
- Git Repo Research MCP Server
- CloudFormation MCP Server
Documentation includes:

- Detailed guides for each server
- Installation and configuration instructions
- API references
- Usage examples
## Vibe coding

You can use these MCP servers with your AI coding assistant to vibe code. For tips and tricks on how to improve your vibe coding experience, please refer to our guide.

## Additional Resources

- Introducing AWS MCP Servers for code assistants
- Vibe coding with AWS MCP Servers | AWS Show & Tell
## Security

See CONTRIBUTING for more information.

## Contributing

Big shout out to our awesome contributors! Thank you for making this project better!

Contributions of all kinds are welcome! Check out our contributor guide for more information.

## Developer guide

If you want to add a new MCP Server to the library, check out our development guide and be sure to follow our design guidelines.

## License

This project is licensed under the Apache-2.0 License.

## Disclaimer

Before using an MCP Server, you should consider conducting your own independent assessment to ensure that your use would comply with your own specific security and quality control practices and standards, as well as the laws, rules, and regulations that govern you and your content.


