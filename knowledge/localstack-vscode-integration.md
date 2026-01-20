# LocalStack VS Code Integration

AWS Toolkit for VS Code now integrates directly with LocalStack for local serverless testing.

## Key Benefits

- **No context switching**: Connect to LocalStack endpoints directly from VS Code
- **Same deployment flow**: Use `sam deploy --guided --profile localstack` just like cloud deployments
- **End-to-end local testing**: Test event-driven workflows with Lambda, SQS, EventBridge, DynamoDB without cloud resources
- **Edit deployed code**: Modify Lambda function code running locally

## Setup

1. Update AWS Toolkit for VS Code to v3.74.0+
2. Go to Application Builder > Walkthrough of Application Builder
3. Click to install LocalStack (installs LocalStack extension automatically)
4. Start LocalStack from status bar
5. Select LocalStack from AWS profiles list

## Testing Tiers

| Tier | Tool | Use Case |
|------|------|----------|
| Unit testing | AWS SAM CLI | Individual Lambda functions |
| Integration testing | LocalStack | Multi-service workflows locally |
| Cloud testing | Remote debugging | Full VPC/IAM validation |

## Commands

```bash
# Deploy to LocalStack using SAM
sam deploy --guided --profile localstack
```

## Notes

- LocalStack Free tier covers core AWS services for early development
- Available in all commercial AWS Regions except GovCloud
- No additional AWS costs for the integration
- LocalStack offers paid tiers for broader service coverage

## Source

- AWS Blog: [Accelerate serverless testing with LocalStack integration in VS Code IDE](https://aws.amazon.com/blogs/aws/accelerate-serverless-testing-with-localstack-integration-in-vs-code-ide/)
- Date: September 2025
