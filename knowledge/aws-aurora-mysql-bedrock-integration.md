# Aurora MySQL + Amazon Bedrock Integration

*Source: [AWS Database Blog](https://aws.amazon.com/blogs/database/integrate-amazon-aurora-mysql-and-amazon-bedrock-using-sql/) - May 2024*

## Overview

Aurora ML allows calling Amazon Bedrock foundation models directly from SQL queries without building custom integrations or moving data. Use cases:

1. **Data enrichment** - Supplement database records with AI-generated content
2. **Text summarization** - Summarize long texts stored in the database
3. **Content generation** - Generate descriptions, recommendations, etc.

## Prerequisites

- Aurora MySQL 3.06.0+ (for Bedrock integration)
- Custom DB cluster parameter group
- IAM role with Bedrock InvokeModel permissions
- Network config allowing outbound to Bedrock endpoints (or VPC endpoint)
- Model access enabled in Bedrock console

## Setup Steps

### 1. Database Setup

```sql
-- Create database and user
CREATE DATABASE bedrockdb;
CREATE USER `bedrock_user`@`%` IDENTIFIED BY 'password';

-- Grant permissions
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, ALTER, INDEX,
      CREATE ROUTINE, ALTER ROUTINE, EXECUTE ON bedrockdb.* TO `bedrock_user`@`%`;

-- Required role for Bedrock access
GRANT AWS_BEDROCK_ACCESS TO `bedrock_user`@`%`;
```

### 2. IAM Configuration

Create policy allowing `bedrock:InvokeModel` for needed models, attach to role with RDS trust policy.

### 3. Cluster Configuration

Add IAM role ARN to `aws_default_bedrock_role` parameter in cluster parameter group.

```sql
-- Verify configuration
SHOW GLOBAL VARIABLES LIKE 'aws_default%';
```

## Creating Bedrock Functions

Define SQL functions that call specific models. Example for Claude 3 Haiku:

```sql
-- Function calls are defined to invoke specific model IDs
-- See AWS docs for full function definitions
-- Model IDs: anthropic.claude-3-haiku-20240307-v1:0, amazon.titan-text-express-v1
```

## Usage Examples

### Query a Model Directly

```sql
SELECT json_unquote(json_extract(claude3_haiku(
  '{
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 1024,
    "temperature": 0,
    "messages": [{"role": "user","content": [{"type": "text", "text": "Your question here"}]}]
  }'),"$.content[0].text")) as response;
```

### Enrich Existing Data

Create a procedure that:
1. Retrieves rows from a table
2. Calls Bedrock for each row to get supplementary info
3. Updates the table with AI-generated content

### Summarize Long Text

```sql
-- Summarize content from a column
SELECT id,
       LEFT(description, 50) as original_excerpt,
       json_unquote(json_extract(claude3_haiku(
         CONCAT('{"anthropic_version":"bedrock-2023-05-31","max_tokens":256,"messages":[{"role":"user","content":[{"type":"text","text":"Summarize: ', description, '"}]}]}')
       ),"$.content[0].text")) as summary
FROM articles;
```

### Batch Processing with GROUP_CONCAT

```sql
SET SESSION group_concat_max_len = 1048576;
SET SESSION aurora_ml_inference_timeout = 30000;
SET @all = (SELECT group_concat(description) FROM t_feed ORDER BY id DESC LIMIT 20);
-- Then pass @all to Bedrock for categorization/summarization
```

## Supported Models

Check available models:
```bash
aws bedrock list-foundation-models --query '*[].[modelName,modelId]' --out table
```

Common choices:
- `amazon.titan-text-express-v1` - Amazon Titan Text
- `anthropic.claude-3-haiku-20240307-v1:0` - Claude 3 Haiku (fast, cheap)
- `anthropic.claude-3-sonnet-20240229-v1:0` - Claude 3 Sonnet

## Considerations

- **Latency** - Response time varies with prompt size and model
- **Costs** - Check [Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/)
- **Quotas** - Be aware of [Bedrock quotas](https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html)
- **Network** - May need VPC endpoint (`bedrock-runtime`) for private connectivity

## Related

- `aws-bedrock-prompt-management.md` - Prompt versioning and flows
- `aws-lambda-powertools-bedrock.md` - Lambda utilities for Bedrock Agents
- `aws-aurora-database-activity-streams.md` - Aurora monitoring
