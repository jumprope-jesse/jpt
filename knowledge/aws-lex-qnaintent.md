# AWS Amazon Lex QnAIntent - RAG-Powered FAQ Automation

*Source: [AWS What's New](https://aws.amazon.com/about-aws/whats-new/2024/03/qnaintent-amazon-lex-available/) - March 2024*

## Overview

QnAIntent for Amazon Lex connects foundation models to enterprise data for Retrieval Augmented Generation (RAG), automating FAQ handling through text and voice channels without extensive intent/utterance configuration.

## Key Benefits

- **Reduced bot configuration**: No need to create many intents, sample utterances, slots, and prompts for FAQ handling
- **Direct knowledge integration**: Connect to company knowledge sources for immediate Q&A capability
- **Multi-channel**: Works with text and voice channels (including Amazon Connect)
- **Reduced agent transfers**: Automates customer questions to avoid unnecessary escalation

## Supported Knowledge Sources

- Knowledge Bases for Amazon Bedrock
- Amazon OpenSearch
- Amazon Kendra

## Response Options

Developers can choose between:
1. **Generative response summary**: FM-generated answer synthesized from retrieved content
2. **Exact response match**: Direct excerpts from knowledge base

## Regional Availability

- US East (N. Virginia)
- US West (Oregon)
- English language only (as of GA)

## Use Case Example

Instead of creating dozens of intents to handle insurance claim questions, connect QnAIntent to your claims documentation knowledge base. Questions like "What documents do I need to submit for an accident claim?" are answered automatically from the allowed content.

## Timeline

- **November 2023**: Preview at re:Invent
- **March 2024**: General availability

## Integration Pattern

```
User Voice/Text → Amazon Lex → QnAIntent → Knowledge Base → FM (Bedrock) → Response
```

Works with both new and existing Lex bots.

## Related

- `aws-bedrock-knowledge-bases-rag.md` - Knowledge bases setup and configuration
- `aws-bedrock-agents.md` - More complex agentic workflows
