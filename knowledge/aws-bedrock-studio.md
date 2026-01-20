# AWS Bedrock Studio

Web-based development environment for building generative AI applications. Public preview as of May 2024.

## What It Is

- Rapid prototyping environment for gen AI apps
- Access to Bedrock features: Knowledge Bases, Agents, Guardrails
- No AWS Console access required - uses SSO credentials
- Targets developers who may not have ML expertise

## Key Features

- **Model exploration**: Try multiple foundation models with natural language prompts
- **Playground mode**: Experiment with model configurations and system prompts
- **Knowledge Bases**: Bring your own data via single file or Bedrock Knowledge Base
- **Functions**: Add API calls via OpenAPI schema for dynamic data retrieval
- **Guardrails**: Configure safeguards for responsible AI

## How It Works

1. **Admin setup**: Create workspace in Bedrock console, configure IAM Identity Center SSO, add users
2. **Developer access**: Sign in via SSO, create projects, build apps
3. **Resource management**: Knowledge bases, agents, guardrails auto-deploy to AWS account
4. **API access**: Resources accessible via Bedrock API for downstream apps

## Key Differentiators

- Developers don't need broader AWS access
- Managed resources created automatically
- Collaboration features for team iteration

## Availability

US East (N. Virginia), US West (Oregon) - preview regions

## Related

- `aws-bedrock-prompt-management.md` - Prompt versioning and flows
- `aws-app-studio.md` - No-code business app builder (different use case)
- `ai-agent-architecture.md` - Agent patterns

## Links

- [Bedrock Studio User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-studio.html)
