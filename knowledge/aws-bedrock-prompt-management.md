# AWS Bedrock Prompt Management and Prompt Flows

*Source: [AWS What's New](https://aws.amazon.com/about-aws/whats-new/2024/07/amazon-bedrock-prompt-management-flows-preview) - Originally announced July 2024*

## Overview

Amazon Bedrock includes two features for managing prompts and building AI workflows:

1. **Prompt Management** - Create, evaluate, version, and share prompts
2. **Prompt Flows** - Visual builder for AI workflows

## Prompt Management

Simplifies prompt development with:

- **Prompt Builder** - Experiment across multiple foundation models and configurations without deployment
- **In-place testing** - Test and compare prompts directly
- **Version control** - Track prompt versions and share via API
- **Multi-model experimentation** - Try prompts across different Bedrock models

## Prompt Flows

Visual workflow automation tool:

- **Drag-and-drop interface** - Build workflows visually
- **Component integration** - Connect prompts, Knowledge Bases, and Lambda functions
- **No-code orchestration** - Create multi-step AI processes without writing integration code

## Use Cases

- Prompt engineering iteration and A/B testing
- Building RAG pipelines with Knowledge Bases
- Creating multi-step agent workflows
- Standardizing prompt templates across teams

## Availability

Available in: US East (N. Virginia), US West (Oregon), Frankfurt, Tokyo, Sydney, Singapore, Ireland, Paris, Mumbai.

## Related

- `aws-lambda-powertools-bedrock.md` - Lambda utilities for Bedrock Agents
- `ai-agent-architecture.md` - General agent architecture patterns
