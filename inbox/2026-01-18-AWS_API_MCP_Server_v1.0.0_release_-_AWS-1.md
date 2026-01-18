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
- The AWS API MCP Server v1.0.0 release enables natural language interaction with AWS APIs, simplifying complex tasks and reducing the coding burden.
- As a software engineer and founder, this tool could streamline operations for your startup, allowing for more efficient project management and implementation of cloud solutions.
- The emphasis on security and input validation is crucial, especially when dealing with sensitive data, providing peace of mind in your development processes.
- The containerized version in the Amazon ECR Public Gallery allows for easy deployment, which can save valuable time and resources.
- The experimental tool for prescriptive workflows could help automate routine tasks, freeing you up to focus on strategic decisions and family time.
- Consider the balance between automation and human oversight; while efficiency is key, maintaining some level of human intervention might preserve quality control in critical applications.
- Explore how these advancements could influence the tech landscape in NYC, potentially leading to new opportunities or collaborations with other tech firms.

## AI Summary (from Notion)
AWS has released version 1.0.0 of the API model context protocol (MCP) server, enabling natural language interaction with AWS APIs. This version includes enhancements for easier configuration, reduced startup time, improved security, and the ability to collect logs via AWS CloudWatch. It supports streamable HTTP transport and features a new tool for prescriptive workflows. The server is open-source and available for configuration with MCP-compatible clients.

## Content (from Notion)

Today, AWS announces the v1.0.0 release of the AWS API model context protocol (MCP) server enabling foundation models (FMs) to interact with any AWS API through natural language by creating and executing syntactically correct CLI commands.

The v1.0.0 release of the AWS API MCP Server contains many enhancements that make the server easier to configure, use, and integrate with MCP clients and agentic frameworks. This release reduces startup time and removes several dependencies by converting the suggest_aws_command tool to a remote service rather than relying on local installation. Security enhancements offer improved secure file system controls, and better input validation. Customers using AWS CloudWatch agent can now collect logs from the API MCP Server for improved observability. In order to support more hosting and configuration options, the AWS API MCP Server now offers streamable HTTP transport in addition to the existing stdio. To make human-in-the-loop workflows requiring iterative inputs more reliable, the AWS API MCP Server now includes elicitation in supported MCP clients. To provide additional safeguards the API MCP Server can be configured to deny certain types of actions or require human oversight and consent for mutating actions. This release also includes a new experimental tool called get_execution_plan to provide prescriptive workflows for common AWS tasks. The tool can be enabled by setting the EXPERIMENTAL_AGENT_SCRIPTS flag to true.

Customers can configure the AWS API MCP Server for use with their MCP-compatible clients from several popular MCP registries. The AWS API MCP Server is also available packaged as a container in the Amazon ECR Public Gallery.

The AWS API MCP Server is open-source and available now. Visit the AWS Labs GitHub repository to view the source, download, and start experimenting with natural language interaction with AWS APIs today.


