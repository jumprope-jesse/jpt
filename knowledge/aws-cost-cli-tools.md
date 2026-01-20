# AWS Cost CLI Tools

Open-source and third-party CLI tools for AWS cost analysis and reporting.

## eraXplor

Open-source AWS cost export tool for automated cost reporting. Calls AWS Cost Explorer API directly and exports to CSV.

- **Repo**: https://mohamed-eleraki.github.io/eraXplor/
- **License**: Apache 2.0

### Features

- Account-level cost breakdown (monthly unblended costs per linked account)
- Service-level cost breakdown (monthly unblended costs per service)
- Flexible date ranges with validation
- Multi-profile support (works with all configured AWS profiles)
- CSV export
- Cross-platform CLI

### Use Cases

- Quick cost exports without logging into AWS Console
- Automated cost reporting scripts
- FinOps/DevOps cost visibility

### Notes

Self-described as "initial model" - still under active development. Good for simple cost extraction; for more advanced analysis consider AWS's native tools (Q Developer, Cost Explorer) or the AWS Billing MCP server.

## Vantage MCP Server

Third-party MCP server from Vantage.sh for LLM-powered AWS cost analysis. Requires a Vantage account (free tier available).

- **Repo**: https://github.com/vantage-sh/vantage-mcp-server
- **Blog**: https://www.vantage.sh/blog/vantage-mcp

### Advantages Over Direct AWS APIs

- Multi-account access across different AWS accounts
- Cost data from other cloud platforms (not just AWS)
- Data normalization and tagging that improves LLM comprehension

### Use Cases

- Answering ad-hoc questions about spending
- Creating cost optimization action plans
- Identifying cost spikes and anomalies

### Trade-offs

- Requires Vantage account (vs. direct AWS API access)
- Additional vendor dependency
- Data flows through Vantage platform

See also: [AWS Q Developer Cost Management](aws-q-developer-cost-management.md) for AWS's native MCP server approach.
