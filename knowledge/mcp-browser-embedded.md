# MCP-B: Browser-Embedded MCP Servers

*Source: https://mcp-b.ai/ - Added: 2026-01-18*

MCP-B embeds MCP servers directly into web pages, allowing AI assistants to interact with web app APIs using the user's existing authenticated session.

## The Key Insight

Instead of running MCP servers as separate processes or requiring OAuth flows, the MCP server runs inside the web page itself. This means:

- **Automatic authentication** - Uses the user's existing session cookies/tokens
- **No separate infrastructure** - Server lives in the browser tab
- **Simpler integration** - Just add the SDK to your web app

## How It Works

1. Web app includes MCP-B SDK and defines tools
2. User has MCP-B Chrome extension installed
3. AI assistants can discover and call tools on the page
4. Tools execute using the user's authenticated session

## Example Implementation

```typescript
import { TabServerTransport } from '@webmcp/transports';
import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';
import { z } from 'zod';

const server = new McpServer({
  name: 'invoice-system',
  version: '1.0.0'
});

server.tool('createInvoice', 'Create a new invoice', {
  customerEmail: z.string().email(),
  items: z.array(z.object({
    description: z.string(),
    amount: z.number()
  }))
}, async ({ customerEmail, items }) => {
  // Uses existing authenticated API client
  const response = await yourPreAuthorizedApiClient('/api/invoices', {
    method: 'POST',
    body: JSON.stringify({ customerEmail, items })
  });

  return {
    content: [{ type: 'text', text: JSON.stringify(await response.json()) }]
  };
});

const transport = new TabServerTransport();
await server.connect(transport);
```

## Comparison with Traditional Browser Automation

| Approach | Auth Handling | Complexity | Reliability |
|----------|--------------|------------|-------------|
| Screen scraping | Implicit (user session) | High | Fragile |
| OAuth-based MCP | Explicit tokens | High | Robust |
| **MCP-B** | Implicit (user session) | Low | Robust |

## Security Considerations

- Servers have full access to user's session - need to trust the page
- Extension acts as bridge between AI and page tools
- Same security model as the web app itself

## Relationship to Other MCP Approaches

| Tool | Purpose |
|------|---------|
| Standard MCP | Standalone servers with explicit auth |
| MCP-UI | Rich UI in MCP responses |
| **MCP-B** | Browser-embedded servers using session auth |

## When to Use

- Adding AI capabilities to existing authenticated web apps
- Avoiding complex OAuth flows for internal tools
- Building browser-based AI integrations

## Resources

- Website: https://mcp-b.ai/
- Chrome extension required for AI assistant integration

---

# Herd: Browser Automation for AI Agents

*Source: https://herd.garden - Added: 2026-01-18*

Herd is a browser automation platform that connects AI tools (ChatGPT, Claude, Cursor) to websites via pre-built automation "trails."

## How It Works

- Exposes MCP (Model Context Protocol) servers that AI agents can call
- Trails are pre-built automations for specific websites
- Agent actions execute through the user's browser securely

## @omneity/serp Trail

SERP (Search Engine Results Page) scraper for multiple search engines:

- **Supported engines**: Google, Bing, DuckDuckGo, Brave Search
- **Tool**: `search` - Search across one or more engines simultaneously
- **Use case**: Automated research, product comparison, trend monitoring

## Comparison with MCP-B

| Tool | Approach | Best For |
|------|----------|----------|
| **MCP-B** | SDK embedded in web app | Adding AI to your own apps |
| **Herd** | Pre-built trails for existing sites | Automating third-party sites |

Both use browser-based execution with user session auth, avoiding OAuth complexity.

---

# Operative.sh: Browser Agents for Web App Testing

*Source: https://www.operative.sh/ - Added: 2026-01-18*

Operative.sh provides a browser agent (via MCP) that can "vibe-test" web applications - letting coding agents automatically test and verify your app during development.

## Key Features

- **MCP integration** - Works with coding agents like Cursor via MCP protocol
- **BrowserUse under the hood** - Uses BrowserUse but claims 2x faster
- **Network traffic capture** - Monitor all requests/responses in real-time
- **Autonomous debugging** - Agent automatically tests app flows end-to-end

## Quick Install

```bash
curl -LSf https://operative.sh/install.sh -o install.sh && bash install.sh && rm install.sh
```

## Use Cases

- Login flow testing
- Dashboard view verification
- API key creation flows
- General E2E testing during development

## Expanding to Electron Apps

Planning to bring automated UX testing to desktop apps - seeking design partners for Electron app testing.

## Comparison with Other MCP Browser Tools

| Tool | Primary Use Case |
|------|------------------|
| **MCP-B** | Embed MCP servers in your web app for AI interaction |
| **Herd** | Pre-built automations for third-party sites |
| **Operative.sh** | Automated testing/QA for web apps during dev |

Operative focuses specifically on the dev workflow - giving your coding agent the ability to test the app it's building.
