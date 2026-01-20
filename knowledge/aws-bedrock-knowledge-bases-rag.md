# AWS Bedrock Knowledge Bases for RAG Applications

*Source: [AWS Machine Learning Blog](https://aws.amazon.com/blogs/machine-learning/building-scalable-secure-and-reliable-rag-applications-using-knowledge-bases-for-amazon-bedrock/) - April 2024*

## Overview

Knowledge Bases for Amazon Bedrock enables building Retrieval Augmented Generation (RAG) applications for question answering, contextual chatbots, and personalized search. As a fully managed service, it handles infrastructure provisioning, management, and scaling.

## Enterprise Features

### CloudFormation Support

Automate knowledge base deployment with IaC:

```json
{
    "Type": "AWS::Bedrock::KnowledgeBase",
    "Properties": {
        "Name": "my-knowledge-base",
        "RoleArn": "arn:aws:iam::xxx:role/bedrock-kb-role",
        "KnowledgeBaseConfiguration": {
            "Type": "VECTOR",
            "VectorKnowledgeBaseConfiguration": {}
        },
        "StorageConfiguration": {}
    }
}
```

Data sources configured separately:

```json
{
    "Type": "AWS::Bedrock::DataSource",
    "Properties": {
        "KnowledgeBaseId": "kb-id",
        "Name": "my-data-source",
        "DataSourceConfiguration": {
            "S3Configuration": {},
            "Type": "S3"
        },
        "VectorIngestionConfiguration": {
            "ChunkingConfiguration": {}
        }
    }
}
```

**Note**: Chunking configuration cannot be changed after data source creation.

### Private Network Policies (OpenSearch Serverless)

For secure vector storage:

1. Create OpenSearch Serverless collection configured for private network access
2. Set Network access settings to "Private"
3. Select "AWS service private access" with `bedrock.amazonaws.com`
4. All traffic stays on AWS backbone, never hits public internet

### Multiple S3 Buckets as Data Sources

- Aggregate data from multiple S3 buckets within a single knowledge base
- Cross-account access supported (provide credentials)
- Configure data retention policy per data source (retain or delete when source removed)
- Eliminates need for redundant data copies or multiple knowledge bases

### Service Quotas Integration

- Single pane of glass for viewing applied quotas and usage
- Monitor RetrieveAndGenerate API request limits
- Prevent overprovisioning and rate limit abuse

## Performance Features

- **Hybrid search**: Combines keyword and semantic search
- **Metadata filters**: Filter results based on document metadata
- **Custom prompts**: Override default prompts in RetrieveAndGenerate API
- **Max retrievals**: Configure number of documents retrieved

## Inference Configuration (Temperature, etc.)

When using the `RetrieveAndGenerate` API, control model behavior via `generationConfiguration`:

```python
response = bedrock_agent_runtime.retrieve_and_generate(
    input={"text": "your question"},
    retrieveAndGenerateConfiguration={
        "type": "KNOWLEDGE_BASE",
        "knowledgeBaseConfiguration": {
            "knowledgeBaseId": "kb-id",
            "modelArn": "arn:aws:bedrock:region::foundation-model/model-id",
            "generationConfiguration": {
                "inferenceConfig": {
                    "textInferenceConfig": {
                        "temperature": 0.0,  # 0.0-1.0, lower = more deterministic
                        "topP": 0.9,
                        "maxTokens": 512
                    }
                }
            }
        }
    }
)
```

**Key parameters:**
- `temperature`: 0.0 for factual/consistent responses, higher for creative
- `topP`: Nucleus sampling threshold
- `maxTokens`: Output length limit

For chatbots with Knowledge Bases, low temperature (0.0-0.3) typically works best to keep responses grounded in retrieved context.

## Well-Architected Alignment

| Pillar | How Knowledge Bases Addresses It |
|--------|----------------------------------|
| Operational Excellence | CloudFormation automation, consistent deployments |
| Security | Private network policies, encrypted vector stores |
| Reliability | Cross-account data sources, fault-tolerant architecture |
| Performance | Hybrid search, metadata filters, configurable retrievals |
| Cost Optimization | Single knowledge base for multiple sources, managed service |
| Sustainability | Managed infrastructure, efficient resource utilization |

## Vector Store Options

- Amazon OpenSearch Serverless (with private network support)
- Other supported stores (check docs for current list)
- Note: Redis Enterprise Cloud not supported in CloudFormation as of April 2024

## Single Document Q&A

*Added April 2024*

Knowledge Bases now supports asking questions directly on a single document without needing to create a full knowledge base. This simplifies ad-hoc document analysis:

- **No pre-indexing required**: Upload a document and query immediately
- **Use case**: Quick Q&A on individual PDFs, reports, or documents
- **Benefit**: Reduces friction for one-off document analysis vs. full RAG setup

This is useful when you need answers from a specific document rather than searching across a corpus.

## Related

- `aws-bedrock-prompt-management.md` - Prompt versioning and Prompt Flows
- `aws-bedrock-studio.md` - Web-based prototyping environment
- `aws-aurora-mysql-bedrock-integration.md` - Aurora integration patterns
