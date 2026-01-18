# AWS Backup: Cross-Region/Cross-Account Snapshot Copy

## Overview

AWS Backup now supports copying database snapshots across AWS Regions AND accounts in a **single copy action** (announced October 2025).

## Supported Services

- Amazon RDS (all engines)
- Amazon Aurora (all engines)
- Amazon Neptune
- Amazon DocumentDB

## Key Benefits

1. **Simplified Workflow**: Eliminates the previous two-step process (Region copy → account copy or vice versa)
2. **Faster RPO**: Single-action copying achieves faster recovery point objectives
3. **Cost Reduction**: No intermediate copies = no intermediate storage costs
4. **No Custom Scripts**: Removes need for Lambda functions monitoring intermediate copy status

## Use Cases

- **Ransomware Protection**: Isolate backups in separate accounts/regions
- **Region Outage Recovery**: Maintain copies outside primary region
- **Compliance**: Meet data residency requirements across regions

## Availability

- Available in all regions where AWS Backup supports cross-Region and cross-account copying
- Access via: AWS Management Console, CLI, or SDKs

## Links

- [AWS Announcement](https://aws.amazon.com/about-aws/whats-new/2025/10/aws-backup-single-action-database-snapshot-copy-regions/)
- [AWS Backup Documentation](https://docs.aws.amazon.com/aws-backup/)
