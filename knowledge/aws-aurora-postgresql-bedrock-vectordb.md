# Aurora PostgreSQL as Bedrock Knowledge Base Vector Store

*Source: [AWS Database Blog](https://aws.amazon.com/blogs/database/build-generative-ai-applications-with-amazon-aurora-and-knowledge-bases-for-amazon-bedrock/) - March 2024*

## Overview

Aurora PostgreSQL can serve as a vector database for Knowledge Bases for Amazon Bedrock, enabling RAG applications with high-performance vector similarity search. Aurora delivers queries 20x faster with pgvector's HNSW indexing, and Aurora Optimized Reads can increase performance by up to 9x for workloads exceeding instance memory.

## Prerequisites

- Aurora PostgreSQL 15.5+ (for latest pgvector)
- RDS Data API enabled (required by Bedrock)
- pgvector extension installed
- Secrets Manager for credentials
- IAM role for Bedrock access

## Database Setup

```sql
-- Enable pgvector extension
CREATE EXTENSION IF NOT EXISTS vector;

-- Create dedicated schema for Bedrock
CREATE SCHEMA bedrock_integration;

-- Create user for Bedrock access
CREATE ROLE bedrock_user WITH PASSWORD 'your-password' LOGIN;
GRANT ALL ON SCHEMA bedrock_integration TO bedrock_user;

-- Create embeddings table (example structure)
CREATE TABLE bedrock_integration.bedrock_kb (
    id uuid PRIMARY KEY,
    embedding vector(1536),  -- Titan Embeddings dimension
    chunks text,
    metadata json
);

-- Create index for fast similarity search
CREATE INDEX ON bedrock_integration.bedrock_kb
    USING hnsw (embedding vector_cosine_ops);
```

## Secrets Manager Configuration

Create secret with RDS credentials type:
- Username: `bedrock_user`
- Password: (your password)
- Select your Aurora cluster

Note the secret ARN for knowledge base configuration.

## Knowledge Base Setup in Bedrock Console

1. Create knowledge base, select "Choose a vector store you have created"
2. Select Amazon Aurora
3. Provide:
   - **Database cluster ARN**: Your Aurora cluster ARN
   - **Database name**: Your database name
   - **Table name**: `bedrock_integration.bedrock_kb`
   - **Secret ARN**: From Secrets Manager
   - **Vector field**: `embedding`
   - **Text field**: `chunks`
   - **Metadata field**: `metadata`
   - **Primary key field**: `id`

## Aurora ML for Embedding Generation

Aurora ML enables calling Bedrock embedding models directly from SQL.

### Prerequisites for Aurora ML

1. Create IAM policy with `bedrock:InvokeModel` for embedding models
2. Create IAM role with RDS trust policy
3. Attach role to Aurora cluster with Bedrock feature

### Install Extension

```sql
CREATE EXTENSION IF NOT EXISTS aws_ml CASCADE;
```

### Generate Embeddings

```sql
-- Single embedding
SELECT aws_bedrock.invoke_model_get_embeddings(
   model_id      := 'amazon.titan-embed-text-v1',
   content_type  := 'application/json',
   json_key      := 'embedding',
   model_input   := '{ "inputText": "Your text here"}'
) AS embedding;
```

### Batch Embedding Generation

For bulk embedding generation, use a stored procedure to avoid long-running transactions:

```sql
DO
$embed$
    DECLARE
        doc RECORD;
        emb vector(1536);
    BEGIN
        FOR doc in SELECT id, content FROM documents WHERE embedding IS NULL LOOP
            EXECUTE $$ SELECT aws_bedrock.invoke_model_get_embeddings(
                    model_id      := 'amazon.titan-embed-text-v1',
                    content_type  := 'application/json',
                    json_key      := 'embedding',
                    model_input   := json_build_object('inputText', $1)::text)$$
                INTO emb
                USING doc.content;
            UPDATE documents SET embedding = emb WHERE id = doc.id;
            COMMIT;
        END LOOP;
    END;
$embed$ LANGUAGE plpgsql;
```

**Performance note**: Single embedding calls take 100-400ms. Use batch processing with per-row commits to avoid blocking.

## Network Configuration

Aurora must be able to reach Bedrock endpoints:
- Configure VPC endpoints for private connectivity
- Or allow outbound internet access (NAT gateway)
- See [Enabling network communication from Aurora to AWS services](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-mysql-ml.html#aurora-mysql-ml-prereqs)

## Embedding Models

| Model | Dimensions | Use Case |
|-------|------------|----------|
| `amazon.titan-embed-text-v1` | 1536 | General purpose |
| `amazon.titan-embed-text-v2:0` | 256-1024 (configurable) | Flexible dimensions |
| `cohere.embed-english-v3` | 1024 | English text |
| `cohere.embed-multilingual-v3` | 1024 | Multilingual |

## Performance Optimizations

1. **HNSW indexing**: Use `hnsw` index type for fast approximate nearest neighbor search
2. **Aurora Optimized Reads**: For workloads exceeding memory, provides up to 9x speedup
3. **Aurora Serverless v2**: Auto-scales compute based on workload
4. **Aurora I/O-Optimized**: Predictable pricing for I/O-intensive vector search

## Related

- `aws-bedrock-knowledge-bases-rag.md` - Knowledge Bases features and APIs
- `aws-aurora-mysql-bedrock-integration.md` - Aurora MySQL integration
- `rag-maturity-levels.md` - RAG architecture patterns
