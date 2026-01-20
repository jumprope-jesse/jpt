# AWS Generative AI Application Builder

AWS Solution for rapidly developing and deploying production-ready generative AI applications without deep AI expertise.

## What It Is

A deployable reference architecture (AWS Solution) that accelerates building gen AI apps by providing:
- Data/document ingestion pipelines for business-specific content
- LLM evaluation and comparison tooling
- Extensible application framework
- Enterprise-grade deployment architecture
- No-code deployment wizard

## Integrations

- **Amazon Bedrock** - Primary LLM provider with included models
- **Amazon SageMaker** - Custom model deployment
- **Anthropic** - Pre-built connector
- **Hugging Face** - Pre-built connector
- **Custom models** - Via LangChain or AWS Lambda

## Pre-Built Application Types

- Conversational search
- AI-generated chatbots
- Text generation
- Text summarization

## How It Differs from Bedrock Studio

| Aspect | GenAI App Builder | Bedrock Studio |
|--------|-------------------|----------------|
| Type | Deployable AWS Solution | Web-based dev environment |
| Target | Production deployment | Rapid prototyping |
| Setup | Full infrastructure deployment | Managed workspace |
| Flexibility | Extensible architecture | Constrained to Studio features |
| LLM Options | Multi-provider (Bedrock, SageMaker, external) | Bedrock models only |

## When to Use

- Need production-ready architecture (not just prototyping)
- Want to use models outside Bedrock ecosystem
- Require data ingestion pipelines for RAG
- Need to compare multiple LLMs systematically

## Links

- [AWS Solutions Page](https://aws.amazon.com/solutions/implementations/generative-ai-application-builder-on-aws/)
- [GitHub Repository](https://github.com/aws-solutions/generative-ai-application-builder-on-aws)

## Related

- `aws-bedrock-studio.md` - Prototyping environment
- `aws-bedrock-knowledge-bases-rag.md` - RAG patterns
- `aws-ai-powered-sdlc-patterns.md` - AI in development workflows
