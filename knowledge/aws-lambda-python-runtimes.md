# AWS Lambda Python Runtimes

## Python 3.14 Support (November 2025)

AWS Lambda now supports Python 3.14, the latest long-term support release.

### Availability
- Available as managed runtime and container base image
- Automatic updates applied by AWS
- Available in **all regions** including GovCloud and China Regions
- Supported with Lambda@Edge for low-latency CloudFront customization

### Deployment Options
- Lambda console
- AWS CLI
- AWS SAM
- AWS CDK
- CloudFormation

### Tooling Support
- Powertools for AWS Lambda (Python) supports 3.14

## Performance Considerations

**Important:** Benchmarks from late 2025 show Python 3.11 outperforms newer versions (3.12, 3.13, 3.14) by 9-15% on Lambda. Consider whether you need 3.14-specific features before upgrading from 3.11.

See: `aws-lambda-arm64-performance.md` for detailed benchmarks.

## References
- [Python 3.14 Announcement](https://aws.amazon.com/about-aws/whats-new/2025/11/aws-lambda-python-314/)
- [AWS Lambda Runtimes Documentation](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html)
