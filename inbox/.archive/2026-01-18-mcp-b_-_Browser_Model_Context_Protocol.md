---
type: link
source: notion
url: https://mcp-b.ai/
notion_type: Software Repo
tags: ['Running']
created: 2025-07-09T23:38:00.000Z
---

# mcp-b - Browser Model Context Protocol

## Overview (from Notion)
- The integration of MCP servers directly into web pages can streamline workflows, making it easier to develop user-friendly applications without managing separate backend services.
- As a software engineer, this model can enhance productivity by allowing quick access to powerful AI tools within existing applications, potentially reducing the time spent on repetitive tasks.
- The use of existing authentication for MCP servers means less friction for users, which can lead to better user experiences and higher adoption rates for new features.
- The focus on browser-based automation can reflect a shift towards less complex solutions in software development, favoring simplicity over intricate OAuth systems.
- Living in NYC, this technology could be utilized to create innovative local services or apps that cater specifically to urban life, such as managing family logistics or optimizing local shopping experiences.
- An alternate view could be concerns about security and privacy with embedded servers—how safe is it to have these services directly linked to user sessions?
- The potential for AI assistance to become more integrated into daily life could change how you balance work and family, automating mundane tasks and freeing up time for more meaningful interactions.

## AI Summary (from Notion)
MCP servers can be embedded directly into web pages, allowing AI assistants to interact with APIs using existing user sessions without complex OAuth flows. The provided code snippet demonstrates how to set up an MCP server for creating invoices, utilizing existing authentication seamlessly.

## Content (from Notion)

The Breakthrough

Instead of running MCP servers as separate processes or cloud services, we embed them directly into web pages. The MCP server becomes part of your web application.

```plain text
import { TabServerTransport } from '@webmcp/transports';import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';import { z } from 'zod';
const server = new McpServer({  name: 'invoice-system',  version: '1.0.0'});
server.tool('createInvoice', 'Create a new invoice', {  customerEmail: z.string().email(),  items: z.array(z.object({    description: z.string(),    amount: z.number()  }))}, async ({ customerEmail, items }) => {  // This is just a normal fetch to your existing API  const response = await yourPreAuthorizedApiClient('/api/invoices', {    method: 'POST',    headers: { 'Content-Type': 'application/json' },    body: JSON.stringify({ customerEmail, items })  });
  if (!response.ok) {    throw new Error(`Failed to create invoice: ${response.statusText}`);  }  // You get full control over what the model get's to know about the response  return { content: [{ type: 'text', text: JSON.stringify(await response.json())  }] };});
const transport = new TabServerTransport();// This server is now callable by the mcp-b chrome extensionawait server.connect(transport);
```

Your MCP server automatically uses your existing authentication. When users with the MCP-B extension visit your site, their AI assistants can now interact with your APIs using their active session.

Traditional Browser Automation

MCP-B Structured Access

The future of AI assistance isn't in complex OAuth flows or managed infrastructure. It's in the browser you already have open.


