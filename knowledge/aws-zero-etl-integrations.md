# AWS Zero-ETL Integrations

Zero-ETL integration eliminates traditional ETL pipeline complexity by enabling direct, automatic data replication from transactional databases to analytics environments.

## Overview

- **Purpose**: Automatic near-real-time data replication without custom ETL code
- **Sources**: Aurora MySQL, RDS for MySQL (also Aurora PostgreSQL, RDS for PostgreSQL)
- **Targets**: Amazon Redshift, Amazon SageMaker Lakehouse (via AWS Glue managed catalog)
- **Mechanism**: Uses binary logs (binlog) for change data capture

## Key Benefits

1. **Reduced Complexity**: No custom ETL pipelines to build/maintain
2. **Cost Savings**: Less compute/storage for duplicate data and pipeline infrastructure
3. **Near Real-Time**: Changes available in analytics environment within seconds
4. **Automatic Schema Sync**: Schema changes propagate automatically

## Use Cases

- **Content Targeting**: Personalized content using latest clickstream/profile data
- **Fraud Detection**: Real-time monitoring and alerting on suspicious behavior
- **Customer Analytics**: Dynamic campaign adjustments based on user activity
- **Cross-System Reporting**: Unified dashboards across business units
- **ML Training**: Fresh production data for model training without pipeline delays

## Architecture Components

```
Aurora MySQL / RDS MySQL
    │ (binlog replication)
    ▼
Zero-ETL Integration
    │
    ▼
AWS Glue Managed Catalog (metadata)
    │
    ▼
Amazon Redshift Managed Storage (data)
    │
    ├── Amazon Redshift (SQL analytics)
    ├── Amazon SageMaker (ML workloads)
    └── Amazon Athena (ad-hoc queries)
```

## Prerequisites for Aurora MySQL

1. **DB Cluster Parameter Group** with enhanced binlog:
   - `aurora_enhanced_binlog=1`
   - `binlog_format=ROW`
   - `binlog_row_image=full`
   - `binlog_row_metadata=full`
   - `binlog_backup=0`
   - `binlog_replication_globaldb=0`

2. **For RDS MySQL**: Set backup retention period > 0 to enable binlogs

## Key Setup Steps

1. Configure source database with binlog parameters
2. Create AWS Glue managed catalog backed by Redshift managed storage
3. Create IAM role for Glue/Redshift with catalog access
4. Configure Lake Formation permissions
5. Set resource policy authorizing inbound integrations
6. Create zero-ETL integration via `aws rds create-integration`

## Data Filtering

Use `--data-filter` parameter to control replication:
- `include: *.*` - all databases and tables
- `include: mydb.*` - all tables in specific database
- `include: mydb.orders, mydb.customers` - specific tables

## Querying Data

Access replicated data via Amazon Redshift Data API:
```bash
aws redshift-data execute-statement \
  --sql 'SELECT * FROM "integration_id@catalog"."database"."table"' \
  --database "arn:aws:glue:region:account:catalog/catalog-name"
```

## Limitations to Consider

- Not all data types supported for replication
- Schema change handling has specific behaviors
- Data filtering capabilities have constraints
- See AWS documentation for full list

## Cost Considerations

- No additional charge for the zero-ETL integration itself
- Pay for Redshift managed storage and compute for queries
- Consider data volume and query frequency for cost planning

## Resources

- [Aurora Zero-ETL Integrations Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/zero-etl.html)
- [Creating Zero-ETL Integrations with SageMaker Lakehouse](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/zero-etl-glue-data-catalog.html)
- [Amazon RDS Zero-ETL Integrations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-zero-etl.html)

---
Source: AWS Blog - Amazon Aurora MySQL zero-ETL integration with Amazon SageMaker Lakehouse (2025-10)
