# AWS RDS Cross-Region Automated Backups

## Overview

Amazon RDS can automatically replicate snapshots and transaction logs to a different AWS Region for disaster recovery. Unlike AWS Backup (which copies snapshots on-demand), this is continuous replication achieving RPO of just a few minutes.

## Key Capabilities

- **Continuous replication**: Transaction logs uploaded frequently to target Region
- **Point-in-time restore**: Restore to any second within retention period
- **Low RPO**: Recovery Point Objective within last few minutes
- **Native RDS feature**: Set up directly in RDS console/CLI

## Supported Engines

- PostgreSQL
- MariaDB
- MySQL
- Oracle
- Microsoft SQL Server

## Available Region Pairs (as of April 2025)

| Source Region | Target Region(s) |
|---------------|------------------|
| Australia (Melbourne) | Australia (Sydney) |
| Asia Pacific (Hong Kong) | Singapore, Tokyo |
| Asia Pacific (Malaysia) | Singapore |
| Canada (Central) | Canada West (Calgary) |
| Europe (Zurich) | Frankfurt, Ireland |

## When to Use

- **Disaster recovery**: Regional outage protection with minimal data loss
- **Compliance**: Geographic data redundancy requirements
- **Business continuity**: Mission-critical databases needing fast recovery

## RDS Automated Backups vs AWS Backup

| Feature | RDS Automated Backups | AWS Backup |
|---------|----------------------|------------|
| Replication | Continuous | Scheduled snapshots |
| RPO | Minutes | Hours (depends on schedule) |
| Transaction logs | Yes | No (snapshot only) |
| Cross-account | No | Yes |
| Multi-service | RDS only | Multiple AWS services |

Use RDS Automated Backups for lowest RPO. Use AWS Backup for centralized backup management across services or cross-account needs.

## Source

https://aws.amazon.com/about-aws/whats-new/2025/04/amazon-rds-cross-region-automated-backups-additional-aws-regions
