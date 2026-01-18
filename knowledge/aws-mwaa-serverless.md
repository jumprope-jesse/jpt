# AWS MWAA Serverless (Apache Airflow)

Amazon Managed Workflows for Apache Airflow (MWAA) now offers a serverless deployment option.

## Key Features

- **True serverless scaling** - Automatic resource provisioning and scaling, pay only for compute time during task execution
- **No operational overhead** - Eliminates need to manage Apache Airflow environments
- **Workflow definition options**:
  - YAML configurations
  - Python-based DAGs
- **80+ AWS Operators** from Apache Airflow v3.0
- **Workflow isolation** - Each workflow runs with distinct IAM permissions

## Availability

Available in 15 AWS regions including US East/West, Europe, Asia Pacific, Canada, and South America.

## Considerations

- Dependency management in serverless environments may add complexity
- May require organizational culture shift toward automation and CI/CD practices

## Links

- [MWAA Serverless Documentation](https://docs.aws.amazon.com/mwaa/)
- [Announcement](https://aws.amazon.com/about-aws/whats-new/2025/11/mwaa-serverless-deployment-apache-airflow-workflows/)

---
*Added: 2025-11-18*
