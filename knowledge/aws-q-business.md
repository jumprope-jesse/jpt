# Amazon Q Business

Amazon Q Business is a generative AI-powered assistant for enterprise workforce productivity (distinct from Amazon Q Developer which targets software developers).

## What It Does

- Answers questions, provides summaries, generates content based on enterprise data
- Connects to 40+ enterprise data sources (S3, Microsoft 365, Salesforce, etc.)
- Web-based chat assistant with follow-up questions and source citations
- Respects existing user permissions via SSO and ACLs

## Key Features

### Data Connectors & Plugins
- 40+ pre-built connectors (S3, SharePoint, Salesforce, ServiceNow, etc.)
- Amazon Kendra retriever integration
- Web crawling or direct document upload
- Pre-built plugins: Jira, Salesforce, ServiceNow, Zendesk
- **Custom plugins**: Connect any third-party app via OpenAPI schema

### Admin Controls
- Global controls: LLM-only vs enterprise-data-only responses
- Topic-level controls: Block specific topics or restrict responses
- Document enrichment: Modify metadata during ingestion, use Lambda for OCR
- Word blocking for sensitive terms

### Security
- IAM Identity Center integration (required for new apps)
- AWS PrivateLink for VPC access
- CloudTrail logging
- FIPS endpoint compliance
- Data encrypted with AWS KMS

### Content Creation Mode
Toggle to use generative AI without accessing enterprise content - useful for creative tasks like drafting emails or summarization.

## Amazon Q Apps (Preview as of May 2024)

No-code app builder within Q Business:
- Describe app in natural language → auto-generated
- Card-based UI: user input, text output, file upload, plugins
- Share apps across organization via library
- Inherits Q Business security and governance

Similar to PartyRock but connected to enterprise data.

## Pricing (as of May 2024)

| Tier | Price | Features |
|------|-------|----------|
| Q Business Lite | $3/user/month | Basic functionality |
| Q Business Pro | $20/user/month | All features + Q Apps + Q in QuickSight |

60-day free trial for 50 users.

## Regions

US East (N. Virginia), US West (Oregon) at GA.

## Q Developer vs Q Business

| | Q Developer | Q Business |
|---|---|---|
| Target | Software developers | Knowledge workers |
| Focus | Code generation, debugging, console ops | Enterprise Q&A, content generation |
| Data Sources | Code repos, AWS resources | Enterprise systems (SharePoint, Salesforce, etc.) |
| Interface | IDE, CLI, AWS Console | Web chat, Teams, Slack |

## References

- [GA Announcement (May 2024)](https://aws.amazon.com/blogs/aws/amazon-q-business-now-generally-available-helps-boost-workforce-productivity-with-generative-ai/)
- [Amazon Q Business Documentation](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/what-is.html)
