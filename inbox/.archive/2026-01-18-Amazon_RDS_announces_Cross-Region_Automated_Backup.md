---
type: link
source: notion
url: https://aws.amazon.com/about-aws/whats-new/2025/04/amazon-rds-cross-region-automated-backups-additional-aws-regions
notion_type: Tech Announcement
tags: ['Running']
created: 2025-05-01T02:39:00.000Z
---

# Amazon RDS announces Cross-Region Automated Backups in five additional AWS Regions - AWS

## Overview (from Notion)
- Data Security: As a software engineer and company founder, understanding automated backups is crucial for protecting your business data, especially in a city like New York where tech startups thrive.
- Disaster Recovery: Cross-region backups can help ensure that your company's operational continuity is maintained in case of regional outages, which is vital for your peace of mind as a father supporting a family.
- Scalability: The ability to replicate backups across regions can provide insights into how to scale your infrastructure efficiently as your company grows.
- Cost Implications: Consider the cost-effectiveness of using AWS services for backup solutions versus traditional methods; balancing technology investment against family needs is key.
- Work-Life Balance: Automating backups allows you to focus more on quality family time and less on worry about data loss or recovery processes.
- Alternate View: Some may argue that reliance on cloud services for data management can lead to complacency; thus, it’s vital to maintain an understanding of local backups and data governance.

## AI Summary (from Notion)
Amazon RDS now offers Cross-Region Automated Backup replication in five additional AWS Regions, enhancing recovery capabilities for databases by allowing point-in-time restoration and achieving a Recovery Point Objective of just a few minutes in case of regional outages.

## Content (from Notion)

Cross-Region Automated Backup replication for Amazon RDS is now available in five additional AWS Regions. This launch allows you to setup automated backup replication between Australia (Melbourne) and Australia (Sydney); between Asia Pacific (Hong Kong) and Asia Pacific (Singapore) or Asia Pacific (Tokyo); between Asia Pacific (Malaysia) and Asia Pacific (Singapore); between Canada (Central) and Canada West (Calgary); and between Europe (Zurich) and Europe (Frankfurt) or Europe (Ireland) Regions.

Automated Backups enable recovery capability for mission-critical databases by providing you the ability to restore your database to a specific point in time within your backup retention period. With Cross-Region Automated Backup replication, RDS will replicate snapshots and transaction logs to the chosen destination AWS Region. In the event that your primary AWS Region becomes unavailable, you can restore the automated backup to a point in time in the secondary AWS Region and quickly resume operations. As transaction logs are uploaded to the target AWS Region frequently, you can achieve a Recovery Point Objective (RPO) of within the last few minutes.

You can setup Cross-Region Automated Backup replication with just a few clicks on the Amazon RDS Management Console or using the AWS SDK or CLI. Cross-Region Automated Backup replication is available on Amazon RDS for PostgreSQL, Amazon RDS for MariaDB, Amazon RDS for MySQL, Amazon RDS for Oracle, and Amazon RDS for Microsoft SQL Server. For more information, including instructions on getting started, read the Amazon RDS documentation.


