---
type: link
source: notion
url: https://www.reddit.com/r/aws/comments/1k7n0hu/show_raws_an_mcp_server_to_query_and_analyze/
notion_type: Software Repo
tags: ['Running']
created: 2025-04-26T04:18:00.000Z
---

# Show r/AWS: An MCP Server to query and analyze normalized cost and usage data from AWS : r/aws

## Overview (from Notion)
- Cost Management Insight: Understanding AWS costs can help optimize your company's cloud spending, directly impacting your bottom line.
- Use of LLMs: Leveraging language models can streamline the analysis of complex data, making it more accessible without needing deep technical expertise.
- Focus on Efficiency: The ability to quickly answer ad-hoc questions about spending can lead to more informed decision-making and prevent budget overruns.
- Integration Potential: Combining this tool with GitHub workflows can enhance collaboration among your engineering team, leading to better project tracking and accountability.
- Normalization Benefits: The normalization of data allows for clearer insights, making it easier to identify trends and areas for improvement across different platforms.
- Unique Perspectives: Viewing cloud costs as a dynamic element of your overall business strategy rather than a static expense can shift how you approach budgeting and resource allocation.
- Alternative Views: Some might argue that relying on advanced AI tools could lead to overdependence, potentially obscuring the fundamental financial literacy needed to manage costs effectively.

## AI Summary (from Notion)
Vantage.sh has launched an MCP server that utilizes LLMs to analyze AWS cost and usage data, requiring a Vantage account. It helps in answering ad-hoc questions, creating action plans, and identifying cost spikes, while offering advantages like multi-account access and data normalization.

## Content (from Notion)

Hey all, we (vantage.sh) run a platform for tracking and optimizing cloud cost and usage data.

We just published an MCP server so you can use LLMs to make sense of your AWS cost and usage data. (You have to have a Vantage account to use it since it's using the Vantage API, but we have a free tier.)

It has been eye-opening for us how capable the latest-gen models are (we've been testing with Claude) at making sense of the massive complexity of AWS costs.

Blog post: https://www.vantage.sh/blog/vantage-mcp

Repo: https://github.com/vantage-sh/vantage-mcp-server

So far we have found it useful for:

- 
- 
- 
If you're wondering, the difference between using this vs a community-sourced MCP that goes directly to AWS API's is primarily: (1) Access to multiple AWS accounts, cost data from other platforms (2) Normalization and tagging of data seems to make it more usable to LLMs

Thought I'd share, let me know if you have questions


