---
type: link
source: notion
url: https://aws.amazon.com/about-aws/whats-new/2025/10/aws-api-mcp-server-v1-0-0-release
notion_type: Software Repo
tags: ['Running']
created: 2025-10-02T04:25:00.000Z
---

# AWS API MCP Server v1.0.0 release - AWS

## Overview (from Notion)
- The AWS API MCP Server v1.0.0 enhances interaction with AWS APIs, making it easier to create and execute commands through natural language, which could streamline your software development processes.
- This release reduces dependencies and startup time, saving you precious time as a busy founder and engineer, allowing you to focus on innovation rather than configuration.
- The server's security improvements and human oversight features could be vital in maintaining data integrity and compliance, which is critical for any business owner.
- The introduction of the get_execution_plan tool offers prescriptive workflows, which can simplify complex tasks and potentially reduce the learning curve for new team members.
- As a parent, consider how advancements in technology like this can create opportunities for your children in tech and engineering, inspiring them to engage with coding and problem-solving.
- Alternate viewpoints could argue that reliance on AI-driven tools may reduce hands-on experience in coding, emphasizing the importance of maintaining a balance between automation and traditional skills development.
- The accessibility of the open-source server can encourage collaboration and sharing of ideas within the developer community, which could lead to innovative solutions that benefit your business.

## AI Summary (from Notion)
AWS has released version 1.0.0 of the API model context protocol (MCP) server, allowing foundation models to interact with AWS APIs using natural language. Enhancements include reduced startup time, improved security, and support for collecting logs via AWS CloudWatch. The server now offers streamable HTTP transport and includes a new tool for prescriptive workflows. It is open-source and available for configuration with MCP-compatible clients.

## Content (from Notion)

Today, AWS announces the v1.0.0 release of the AWS API model context protocol (MCP) server enabling foundation models (FMs) to interact with any AWS API through natural language by creating and executing syntactically correct CLI commands.

The v1.0.0 release of the AWS API MCP Server contains many enhancements that make the server easier to configure, use, and integrate with MCP clients and agentic frameworks. This release reduces startup time and removes several dependencies by converting the suggest_aws_command tool to a remote service rather than relying on local installation. Security enhancements offer improved secure file system controls, and better input validation. Customers using AWS CloudWatch agent can now collect logs from the API MCP Server for improved observability. In order to support more hosting and configuration options, the AWS API MCP Server now offers streamable HTTP transport in addition to the existing stdio. To make human-in-the-loop workflows requiring iterative inputs more reliable, the AWS API MCP Server now includes elicitation in supported MCP clients. To provide additional safeguards the API MCP Server can be configured to deny certain types of actions or require human oversight and consent for mutating actions. This release also includes a new experimental tool called get_execution_plan to provide prescriptive workflows for common AWS tasks. The tool can be enabled by setting the EXPERIMENTAL_AGENT_SCRIPTS flag to true.

Customers can configure the AWS API MCP Server for use with their MCP-compatible clients from several popular MCP registries. The AWS API MCP Server is also available packaged as a container in the Amazon ECR Public Gallery.

The AWS API MCP Server is open-source and available now. Visit the AWS Labs GitHub repository to view the source, download, and start experimenting with natural language interaction with AWS APIs today.


