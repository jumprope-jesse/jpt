---
type: link
source: notion
url: https://aws.amazon.com/blogs/database/review-your-amazon-aurora-and-amazon-rds-security-configuration-with-prowlers-new-checks/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-08-06T14:12:00.000Z
---

# Review your Amazon Aurora and Amazon RDS security configuration with Prowler’s new checks | AWS Database Blog

## AI Summary (from Notion)
- Overview: The article discusses the new checks introduced by Prowler for enhancing the security configuration of Amazon Aurora and Amazon RDS databases.

- Key Enhancements:
- Certificate Expiration Monitoring: Alerts administrators about upcoming RDS certificate expirations.
- Transport Encryption Enforcement: Expanded checks now include additional database engine types.
- Security Group Event Subscription: Verifies that security group events are monitored.
- Default Admin Username Check: Ensures the admin username is not set to its default value.
- IAM Database Authentication: Checks if IAM authentication is enabled for certain database engine types.

- Benefits of Enhanced Checks:
- Proactive Monitoring: Timely alerts regarding certificate expirations.
- Centralized Security Management: Consolidates security alerts in AWS Security Hub.
- Improved Security Posture: Helps organizations maintain robust security and reduce risks.

- Getting Started with Prowler:
- Installation and configuration steps for Prowler.
- Enabling integration with Security Hub for streamlined monitoring.
- Running security checks and addressing findings.

- Conclusion: The expanded checks empower users to secure RDS instances effectively, providing an integrated security management solution with AWS Security Hub.

- Author: Sanjeet Singireddy, Senior Cloud Architect at AWS Managed Services, focuses on addressing operational and security challenges for customers.

## Content (from Notion)

Ensuring the security and reliability of cloud infrastructure is paramount for organizations that use AWS services. At Amazon security is job zero and in collaboration with AWS Managed Services (AMS), the open source security tool Prowler has recently introduced new checks to review and improve user configurable security of Amazon Relational Database Services (Amazon RDS) databases. Amazon Aurora and Amazon RDS provide a set of features to ensure that your data is securely stored and accessed. Prowler allows you to confirm your databases are correctly configured to meet your security requirements.

Prowler is an Open-Source security tool to perform AWS, Azure, Google Cloud and Kubernetes security best practices assessments, audits, incident response, continuous monitoring, hardening, and forensics readiness. Prowler for AWS provides hundreds of security configuration checks across services such as Amazon Redshift, Amazon ElasticCache, Amazon API Gateway, Amazon CloudFront, and many more.

In this post, we focus on these new and expanded Amazon RDS security checks, their integration with AWS Security Hub, and the benefits they offer AWS users. You can use Prowler checks to supplement the existing CIS AWS Foundations compliance standard Security Hub already provides.

## Introducing Prowler’s expanded checks

Prowler’s new and expanded checks are designed to help users configure Amazon RDS databases more securely. Here are the key enhancements:

- Certificate expiration: Prowler now includes checks that monitor the expiration dates of RDS certificates, including the imminent rds-ca-2019 expiration, alerting administrators before they expire.
- Transport encryption required: This existing check has been expanded to add additional engine types and now checks RDS cluster transport encryption enforcement as well.
- Security group event subscription: This check verifies that RDS security group events have been subscribed to make you aware about any security group changes.
- Default admin username: This control checks whether an RDS database instance or cluster has changed the admin username from its default value.
- IAM database authentication: This control checks whether a RDS database instance or cluster has IAM authentication enabled. This control only evaluates RDS resources with the following engine types: RDS for MySQL, RDS for PostgreSQL, Amazon Aurora, and RDS for MariaDB.
## Benefits of Prowler’s enhanced checks

Prowler’s enhanced checks offer several significant benefits:

- Proactive monitoring: Administrators receive timely alerts about upcoming Amazon RDS certificate expiration, allowing you to act before issues arise.
- Centralized security management: Adds additional information to Security Hub to ensure that all security alerts are consolidated in a single dashboard.
- Enhanced security posture: By proactively ensuring RDS security controls are implemented, organizations can maintain a stronger security posture and reduce the risk of data breaches and downtime.
## Getting started with Prowler’s security checks

To take advantage of Prowler’s enhanced features for RDS, follow these steps:

1. Install and configure Prowler: If you haven’t already, follow the instructions on the Prowler GitHub repository to install Prowler. Configure it to scan your AWS environment.
1. Enable Security Hub integration: Ensure that Prowler is configured to send findings to Security Hub. This allows you to view all security alerts in one place. Follow this integration guide to set it up.
1. Run checks: Use Prowler to run the checks against your AWS infrastructure. Review the findings in Security Hub and start securing your resources.
1. Review Prowler findings: Security Hub results can be filtered down to specific resource types such as “AwsRdsDbInstance“.
1. Address findings: Work on securing your resources by selecting the findings and following the remediation steps.
1. Rerun Prowler: Run Prowler again to verify that the resources have been remediated.
## Conclusion

In this post, we describe the expanded checks for Amazon RDS databases in Prowler. They empower you to secure your RDS instances. Integrating these checks with AWS Security Hub allows your security teams to maintain a comprehensive view of your security posture and address potential issues before they impact your resources.

Leave your questions and feedback in the comments section.

### About the Author

Sanjeet Singireddy is a Senior Cloud Architect with AWS Managed Services. He is passionate about solving customers’ operational and security challenges to move them forward in their cloud adoption journey. Outside of work, Sanjeet enjoys spending time with his family and tinkering around in the garage.


