---
type: link
source: notion
url: https://community.aws/content/2s44xHTSbQgo2Ws2bJr6hZsECGr/building-a-serverless-remote-mcp-server-on-aws-part-1
notion_type: Tech Deep Dive
tags: ['Running']
created: 2025-06-24T14:26:00.000Z
---

# AWS | Community | Building a Serverless remote MCP Server on AWS - Part 1

## Overview (from Notion)
- Explore the potential of serverless architecture to innovate your startup without the overhead of managing infrastructure.
- Consider how the Model Context Protocol (MCP) could allow you to integrate specialized tools into your applications, enhancing user experience.
- Reflect on the rise of AI tools and how leveraging them could streamline your daily tasks, from project management to family logistics.
- Recognize the importance of creating an ecosystem of interconnected services that could benefit your personal and professional life.
- The approach of "MCP as a Service" opens avenues for monetizing your expertise in AI and software development, turning knowledge into a scalable product.
- Alternate view: While embracing new technologies, remain cautious about security and privacy, especially when integrating tools into your family routine or business.
- Consider how the trends in AI and serverless tech could influence your children's future educational paths and career choices.

## AI Summary (from Notion)
This article discusses building a serverless remote Model Context Protocol (MCP) server on AWS Lambda, focusing on core implementation and architecture. It introduces Streamable HTTP transport for creating an "MCP as a Service," allowing LLMs to access tools remotely. The implementation uses Amazon API Gateway and AWS Lambda, ensuring a stateless HTTP-only server. The article also highlights the MCP Inspector for testing the server and emphasizes the potential for businesses to expose specialized functionalities as MCP tools. Future considerations will address security measures for the MCP server.

## Content (from Notion)

If you've been working with LLMs lately, you've probably heard about the Model Context Protocol (MCP). It's a standardized way for LLMs to access external tools and data. I recently built a remote MCP server on AWS Lambda, and I wanted to share what I learned.

This is part 1 of a 2-part series where I'll walk through how I implemented a serverless MCP server. In this post, I'll focus on the core implementation and architecture. Part 2 will cover security considerations.

MCP is pretty straightforward, it's a protocol that lets LLMs call external tools. Think of it as a standardized API contract between LLMs and tool providers.

As a developer, this means you can build tools once and have them work with any MCP compatible LLM. No need to recreate tool specific logic AI application you want to develop.

Most MCP examples you'll find use STDIO transport, which works great for local tools like those used with Claude Desktop or coding assistants. But MCP also supports Streamable HTTP transport, which is what we're implementing in this article and it's a game-changer.

Streamable HTTP lets us expose our MCP server to the world as a service. You are essentially creating an "MCP as a Service", let’s call it MCPaaS 😎. This opens up exciting business possibilities:

This is where the protocol is headed, toward a world of interconnected, specialized AI tools that can be composed and reused across different LLMs and applications.

The current MCP specification uses "Streamable HTTP" as a single transport that can optionally upgrade to SSE streaming. For our implementation we’ll focus on the raw HTTP use case. The combination of Amazon API Gateway and AWS Lambda is perfect for this scenario. It gives us exactly what we need: the ability to expose our tools as HTTP endpoints that clients can invoke on demand.

We get the benefits of serverless (pay-per-use, auto-scaling, zero management) while providing a simple, standard way for clients to access our tools.

Our MCP server implements the Streamable HTTP transport to comply with the current MCP specification:

Since we're implementing a stateless HTTP-only server, we handle these methods as follows:

Our implementation structure using Express.js:

This structure cleanly separates the routing layer from the MCP protocol implementation, making it easy to maintain and extend with additional tools.

Let's start with the AWS Lambda handler - this is the entry point for all requests:

The handler uses the serverless-http package to adapt our Express app for AWS Lambda. When Amazon API Gateway receives a request, it passes the event to this handler, which then routes it through our Express application and returns the response.

Next, our Express app sets up the middleware and routes:

This setup is straightforward - we parse JSON bodies, validate headers, route MCP requests to our handlers, and add error handling.

I've separated the MCP service implementation from the tool definitions to make the codebase more maintainable. First, let's look at the MCP service:

The key part here is using StreamableHTTPServerTransport instead of the STDIO transport that most local MCP examples use. This is what enables our MCP server to be accessible over HTTP and function as a service.

Notice how the service now imports and uses a registerTools function from a separate file. This is where all our tool definitions live. As a sports person and for the sake of this demo, I have implemented a series of health and fitness related tools.

This separation of concerns makes it easy to add new tools without modifying the core MCP service. Adding tools is as simple as defining them in the mcp-tools.ts file.

The routes and controller files are all about routing the request to the McpService.

I have implemented 2 middlewares for header validation and error handling that I omitted for sake of brevity.

I used CDK to define the AWS resources. Here's the stack:

The Amazon API Gateway setup is particularly important here because it's what enables our MCP server to be accessible over HTTP, turning our tools into a service that any MCP-compatible LLM can use remotely. This is the foundation of the "MCPaaS" approach I mentioned earlier.

Deploying is straightforward with CDK:

After deployment, CDK will output the API Gateway URL where your MCP server is accessible.

The MCP project provides an excellent tool for testing MCP servers called the MCP Inspector. It's a web-based interface that makes it easy to discover and test your tools.

To use it, simply run: npx @modelcontextprotocol/inspector@0.14.2

This will start a local web server and open a browser window with the MCP Inspector interface. Here's how to test your server:

Enter your MCP endpoint (Amazon API Gateway URL + /mcp) in the connection field and click "Connect".

Connecting to MCP server

Once connected, click on "List Tools" to see what tools are available on your server. You should see all tools appear in the list.

Listing tools with MCP Inspector

Click on the estimate-vo2-max-cooper tool (or any other tool), enter the required parameters (distance run over 12min, gender and age), and click "Run". You'll see the calculated VO2 max result appear in the response section.

Invoking tools with MCP Inspector

The MCP Inspector is invaluable for testing and debugging your MCP server. It provides a visual interface for exploring your tools and testing them with different parameters.

Now that we’ve validated that the remote MCP server is successfully working, we can use the URL of our MCP server to test it with Claude as it supports remote MCP servers as integrations.

Below, you will see a screenshot of a conversation with Claude, helping me figure out some key fitness metrics about myself leveraging the MCP server we just created. (Notice how Claude calls me overweight 🤣).

Claude Testing

Building an MCP server on AWS Lambda is a great way to extend LLM capabilities without managing servers or spending a lot of money. The official MCP SDK makes implementation relatively straightforward, and the serverless approach keeps costs down.

What excites me most about this approach is how it transforms MCP from a local tool protocol into a globally accessible service. By leveraging Streamable HTTP transport and serverless architecture, we're creating the foundation for an ecosystem of specialized AI tools that can be composed and reused across different LLMs and applications.

For businesses, this means you can expose your domain expertise as MCP tools, allowing customers to integrate your specialized functionality directly into their AI workflows. Whether you're offering financial analysis, medical diagnostics, legal research, or any other specialized capability, MCP provides a standardized way to make that functionality available to AI systems.

For this implementation, we have purposefully created a public-facing MCP server, which allows any MCP-compatible client to access the tools we've exposed. In the next part, we'll explore how to secure these exposed tools and make the MCP server private, which is crucial when offering it as a service to customers.

In Part 2, I'll cover security considerations for your MCP server, including:

If you want to learn more about MCP and serverless:

Alexis is a Senior Solutions Architect at Amazon Web Services. He works with startups across Middle-East and Africa. He focuses on serverless and GenAI architectures, often diving deep through live demos and hands-on solutions.

Please note that the content presented in this document is designed solely for the demonstration of a Proof of Concept (PoC) and utilizes synthetic data to illustrate its capabilities. It does not incorporate production-grade security measures and should not be implemented as is in a production environment.

Security Awareness Disclaimer For any considerations of adopting these services in a production environment, it is imperative to consult with your company-specific security policies and requirements. Each production environment demands a uniquely tailored security assessment that comprehensively addresses its particular risks and regulatory standards. If in doubt, reach out to your AWS Account team.

Generative AI Disclaimer. The cover image for this article was generated with Amazon Nova Canvas.Relevant Security Resources


