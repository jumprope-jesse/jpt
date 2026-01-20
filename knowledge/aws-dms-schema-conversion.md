# AWS DMS Schema Conversion

## Overview
AWS DMS Schema Conversion (DMS SC) is a serverless tool for assessing, converting, and migrating database schema and code objects. It's integrated into the AWS DMS console, replacing the need for the standalone AWS Schema Conversion Tool (SCT) download.

**Source**: https://aws.amazon.com/blogs/database/accelerate-your-database-migration-journey-using-aws-dms-schema-conversion/

## Supported Databases (as of early 2024)
**Sources**: Oracle, SQL Server
**Targets**: Amazon RDS, Amazon Aurora, Amazon Redshift

## Key Components

### Instance Profile
Specifies network, security, and S3 settings for DMS SC:
- VPC and subnet configuration
- Security groups
- S3 bucket for metadata storage

### Data Providers
Store database connection information:
- Engine type (e.g., Aurora PostgreSQL, SQL Server)
- Connection details (host, port, database name)
- Credentials stored in Secrets Manager

### Migration Project
Ties together:
- Instance profile
- Source and target data providers
- Secrets Manager references
- IAM roles
- S3 bucket for artifacts

## Prerequisites

### Network Setup
DMS SC provisions resources in a VPC. Requires:
- Connectivity to source and target databases
- Security group rules allowing inbound connections from DMS SC

### IAM Roles
1. **S3 Role** (`sc-s3-role`): Access to S3 bucket for artifacts
   - Trust policy: `schema-conversion.dms.amazonaws.com`
   - Permissions: `AmazonS3FullAccess`

2. **Secrets Manager Role** (`sc-secrets-manager-role`): Access to database credentials
   - Trust policy: `schema-conversion.dms.amazonaws.com`
   - Permissions: `SecretsManagerReadWrite`

### Trust Policy Example
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "dms.us-east-1.amazonaws.com",
          "schema-conversion.dms.amazonaws.com"
        ]
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

## Workflow

### 1. Assessment
- Select database/schema to assess
- Generate assessment report (PDF summary, CSV details)
- Review action items for objects requiring manual intervention
- Reports exported to S3

### 2. Conversion
- Select objects to convert
- Auto-converts compatible objects
- Flags items requiring manual resolution
- Save converted SQL to S3

### 3. Apply Changes
Two options:
- Download SQL scripts, validate, run manually
- Apply directly to target database via DMS SC

## Monitoring
CloudWatch log groups created automatically:
- Log group pattern: `dms-tasks-sct-xxxx`
- Multiple log types for tracking conversion progress
- Search for "Failed" or "Error" keywords

## Cleanup
Delete in order:
1. Migration projects
2. Instance profiles
3. Data providers
4. S3 bucket with migration files

## Key Benefits
- Serverless - no infrastructure to manage
- Integrated into AWS DMS console
- Automated assessment reports with effort estimates
- Direct database application of converted schemas
- CloudWatch integration for monitoring
