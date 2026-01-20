# Amazon Q Developer Cost Management

Amazon Q Developer includes enhanced cost management capabilities for analyzing AWS costs using natural language queries.

## Capabilities

- **Historical and forecasted costs/usage analysis**
- **Optimization recommendations**
- **Commitment coverage and utilization**
- **Cost anomalies detection**
- **Budget tracking**
- **Free tier usage monitoring**
- **Product attributes**
- **Cost estimation**

## How It Works

Q Developer can:
- Explore data across multiple sources
- Form hypotheses about cost changes
- Perform calculations (period-over-period changes, unit economics like effective cost per instance-hour)
- Provide transparency on API calls made, including parameters
- Link to console pages for verification

## Example Queries

- "Why did costs for this application increase last week?"
- Complex questions about costs by service, account, or resource

## Access

Open the Amazon Q chat panel from anywhere in the AWS Management Console.

## Use Cases

Useful for:
- FinOps practitioners
- Engineers
- Finance professionals

Delegates cost analysis and estimation tasks to reduce time and expertise required.

## MCP Server for External AI Assistants

AWS released an open-source MCP (Model Context Protocol) server for Billing and Cost Management (Aug 2025), bringing these capabilities to any MCP-compatible AI assistant.

### Compatible Tools

- Q Developer CLI
- Kiro IDE
- Visual Studio Code
- Claude Desktop
- Any MCP-compatible agent

### Features

- Analyze historical and forecasted cost/usage data
- Identify cost optimization opportunities
- Understand AWS service pricing
- Detect cost anomalies
- Dedicated SQL-based calculation engine for reliable, reproducible calculations
- Handles large volumes of cost and usage data

### Setup

- Download from [AWS Labs GitHub repository](https://github.com/awslabs)
- Connects using standard AWS credentials
- Minimal configuration required

## Billing and Cost Management Dashboards

A feature within AWS Billing and Cost Management (GA Aug 2025) that allows combining multiple visualizations of billing and cost data in a single page. Free to use.

### Key Features

- **Custom Dashboards**: Up to 20 widgets per dashboard, adjustable sizes/positions
- **Share Across Accounts**: Via AWS Resource Access Manager (RAM) with "Can View" or "Can Edit" permissions
- **API Access**: Create and manage dashboards programmatically

### Widget Types

**Custom Widgets:**
- Cost widget - spending patterns by service
- Usage widget - aggregate resource consumption
- Savings Plans Utilization/Coverage
- Reserved Instance Utilization/Coverage

**Predefined Widgets:**
- Monthly costs by service (6 months)
- Monthly costs by linked account (6 months)
- Monthly EC2 running hour costs (6 months)
- Daily costs (6 months)
- AWS Marketplace costs (6 months)

### Prerequisites

- IAM permissions for Dashboards and fine-grained Cost Management access controls
- AWS Cost Explorer enabled
- AWS RAM permissions for cross-account sharing

### Use Cases

- Track cost optimization efforts (e.g., Savings Plans coverage + EC2 Spot/On-Demand spend)
- Establish common FinOps reporting practices across organization
- Identify correlations and trends across multiple metrics

## Third-Party Alternative: aws-cost-scanner Claude Code Plugin

Community-built Claude Code plugin with 97 automated cost optimization checks across 6 domains:
- **Compute**: EC2 idle instances, unattached volumes, storage type optimization
- **Storage**: S3 lifecycle policies, CloudWatch log retention, snapshots
- **Database**: RDS underutilization, reserved instance coverage
- **Networking**: Unused elastic IPs, NAT gateway optimization
- **Serverless**: Lambda memory allocation, unused functions
- **Reservations**: Coverage gaps in Reserved Instances and Savings Plans

**Key differences from Q Developer:**
- Runs locally (credentials never leave machine)
- 6 parallel sub-agents for faster scanning
- More prescriptive checks vs Q's conversational analysis
- Outputs JSON + markdown reports

**Install:** `/plugin` → Marketplaces → `git@github.com:prajapatimehul/aws-cost-scanner.git`

**Requires:** `uv` package manager, read-only AWS credentials

## References

- [AWS Announcement (Nov 2025)](https://aws.amazon.com/about-aws/whats-new/2025/11/enhanced-cost-management-amazon-q-developer/)
- [Managing costs with Amazon Q Developer - User Guide](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-q.html)
- [Billing and Cost Management MCP Server Announcement (Aug 2025)](https://aws.amazon.com/about-aws/whats-new/2025/08/aws-billing-cost-management-mcp-server/)
- [Billing and Cost Management Dashboards Blog (Aug 2025)](https://aws.amazon.com/blogs/aws-cloud-financial-management/streamline-aws-cost-analytics-with-new-customized-billing-and-cost-management-dashboards/)
- [aws-cost-scanner GitHub](https://github.com/prajapatimehul/aws-cost-scanner)
