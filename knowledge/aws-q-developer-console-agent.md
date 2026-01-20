# Amazon Q Developer Console Agent

Amazon Q Developer has an agentic experience in the AWS Management Console for resource analysis and operational troubleshooting. Also available in Slack and Microsoft Teams.

## Key Capabilities

- **Multi-service resource analysis**: Analyzes relationships between resources across multiple AWS services
- **Natural language queries**: Ask questions about resources, Q Developer identifies appropriate APIs
- **Multi-step reasoning**: Breaks queries into executable steps, asks clarification when needed
- **Operational troubleshooting**: Correlates configs with logs, metrics, and events to find root causes

## How It Works

1. User asks natural language question about AWS resources
2. Q Developer determines analytical steps required
3. Automatically selects appropriate AWS APIs across all services
4. Retrieves information from multiple data sources
5. Analyzes relationships and configurations
6. Provides comprehensive answer

## Example Queries

### Resource Introspection

- "List the AMIs used by my running EC2 instances in us-west-2 that can communicate with my RDS cluster"
- "List my AWS Lambda functions and the CloudFormation stacks that manage those resources"
- "What Lambda functions do I have in us-east-1 and are any invoked by an S3 bucket?"
- "How much did I spend on Lambda functions that are invoked by my S3 bucket?"
- "Show me all my SNS topics and their subscribers"
- "How is this Lambda function getting invoked?"
- "What are the IAM roles and permissions of my Lambda function?"

### Operational Troubleshooting

- "Why is my user-profile-service-prod Lambda function throwing a 500 Internal server error?"
  - Q Developer gathers CloudWatch metrics, examines function config/permissions, checks connected services, analyzes recent changes
  - Identifies root cause (e.g., database connection timeouts)
  - Provides resolution suggestions

## Use Cases

- Understanding resource dependencies and interdependencies
- Analyzing security configurations
- Examining resource relationships across services
- Troubleshooting infrastructure issues
- Managing account resources more efficiently
- Quick identification of root causes for operational issues

## Availability

- AWS Management Console
- Microsoft Teams
- Slack

## References

- [AWS DevOps Blog (June 2025)](https://aws.amazon.com/blogs/devops/new-and-improved-amazon-q-developer-experience-in-the-aws-management-console/)
- [Amazon Q Developer Documentation](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/what-is.html)
