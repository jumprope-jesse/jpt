# AWS Lambda Powertools: Bedrock Agents Function Utility

*Source: [AWS What's New](https://aws.amazon.com/about-aws/whats-new/2025/06/powertools-lambda-bedrock-agents-function-utility/) - Added: 2026-01-18*

## Overview

Powertools for AWS Lambda now includes a **Bedrock Agents Function utility** that simplifies building serverless applications integrated with Amazon Bedrock Agents.

## What It Does

The utility enables developers to create AWS Lambda functions that respond to Bedrock Agent action requests with:

- **Built-in parameter injection** - Automatic handling of parameters from Bedrock Agents
- **Response formatting** - Properly formatted responses for Bedrock Agent integration
- **Boilerplate elimination** - Focus on business logic, not integration plumbing

## Key Benefits

1. **Reduced development time** - Eliminates the complex integration patterns between Lambda and Bedrock Agents
2. **Seamless Powertools integration** - Works with existing Powertools features:
   - Logger
   - Metrics
   - Tracer
   - Other utilities
3. **Production-ready** - Designed for building, testing, and deploying AI applications

## Available Languages

- Python
- TypeScript
- .NET

## Use Case

When building agent-based solutions where Lambda functions process actions requested by Bedrock Agents. Instead of manually handling:

- Request parsing
- Parameter extraction
- Response formatting
- Error handling

...the utility handles these automatically, letting you focus on the actual business logic.

## Getting Started

1. Update Powertools for AWS Lambda to latest version
2. Import the Bedrock Agents Function utility
3. Define your action handlers
4. Deploy and connect to Bedrock Agents

## Resources

- [Python Documentation](https://docs.powertools.aws.dev/lambda/python/)
- [TypeScript Documentation](https://docs.powertools.aws.dev/lambda/typescript/)
- [.NET Documentation](https://docs.powertools.aws.dev/lambda/dotnet/)
- [GitHub Examples](https://github.com/aws-powertools)

## Related

- Amazon Bedrock Agents - For orchestrating multi-step AI workflows
- AWS Lambda - Serverless compute for agent actions
- `ai-agent-architecture.md` - General agent architecture patterns
