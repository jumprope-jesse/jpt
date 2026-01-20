# Prowler - AWS Security Auditing Tool

## Overview

Prowler is an open-source security tool for AWS, Azure, Google Cloud, and Kubernetes. It performs security best practices assessments, audits, incident response, continuous monitoring, hardening, and forensics readiness.

## Key Features

- Hundreds of security configuration checks across AWS services
- Integrates with AWS Security Hub for centralized alert management
- Supplements CIS AWS Foundations compliance standards
- Covers services like RDS, Redshift, ElastiCache, API Gateway, CloudFront, and more

## RDS Security Checks

Prowler includes specific checks for Amazon RDS and Aurora:

### Certificate Expiration
- Monitors RDS certificate expiration dates
- Alerts before certificates expire (including rds-ca-2019)

### Transport Encryption
- Verifies encryption in transit is enforced
- Covers multiple database engine types
- Checks both instances and clusters

### Security Group Event Subscription
- Verifies RDS security group events are subscribed
- Ensures awareness of security group changes

### Default Admin Username
- Checks if admin username changed from default
- Applies to both instances and clusters

### IAM Database Authentication
- Verifies IAM authentication is enabled
- Supports: RDS for MySQL, PostgreSQL, Aurora, MariaDB

## Security Hub Integration

Prowler findings can be sent to AWS Security Hub:
- Centralized security dashboard
- Filter by resource type (e.g., "AwsRdsDbInstance")
- Track remediation progress

## Getting Started

```bash
# Install from GitHub
# https://github.com/prowler-cloud/prowler

# Run checks against AWS environment
prowler aws

# Send findings to Security Hub
prowler aws --security-hub
```

## Benefits

- **Proactive monitoring**: Alerts before issues arise
- **Centralized management**: All findings in Security Hub
- **Compliance**: Supplements CIS benchmarks
- **Open source**: Free, community-maintained

## Source

https://aws.amazon.com/blogs/database/review-your-amazon-aurora-and-amazon-rds-security-configuration-with-prowlers-new-checks/
