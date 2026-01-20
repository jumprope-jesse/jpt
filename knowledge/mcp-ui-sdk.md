# MCP-UI SDK

*Source: https://mcpui.dev/ - Added: 2026-01-18*

MCP-UI enables building rich, dynamic user interfaces for MCP applications. It provides SDKs for creating and rendering interactive UI as part of MCP tool results.

## The Problem It Solves

MCP tools typically return text/JSON results. MCP-UI extends this to allow tools to return interactive UI components that the client can render - forms, external iframes, HTML, React components, etc.

## Architecture

Two-part system:

1. **Server SDK** (`@mcp-ui/server`) - Create UI resources in your MCP tool implementations
2. **Client SDK** (`@mcp-ui/client`) - Render those resources in host applications

## Supported UI Types

- HTML content
- React components
- Web Components
- External URLs (iframes)

## Quick Example

**Server Side** - Return UI from MCP tool:

```typescript
import { createUIResource } from '@mcp-ui/server';

const interactiveForm = createUIResource({
  uri: 'ui://user-form/1',
  content: {
    type: 'externalUrl',
    iframeUrl: 'https://yourapp.com'
  },
  encoding: 'text',
});
```

**Client Side** - Render in host application:

```tsx
import { UIResourceRenderer } from '@mcp-ui/client';

function MyApp({ mcpResource }) {
  return (
    <UIResourceRenderer
      resource={mcpResource.resource}
      onUIAction={(action) => {
        console.log('User action:', action);
      }}
    />
  );
}
```

## Relationship to Other Protocols

| Protocol | Purpose |
|----------|---------|
| **MCP** | Connects agents to tools and context |
| **MCP-UI** | Adds rich UI capabilities to MCP responses |
| **AG-UI** | Broader protocol for agent-to-user communication |

MCP-UI is complementary to MCP itself - it extends what tool results can contain.

## When to Use

- Building MCP servers that need user interaction (forms, confirmations)
- Creating rich tool outputs beyond text/JSON
- Embedding external applications within MCP tool flows

## Resources

- Website: https://mcpui.dev/
- TypeScript and Ruby SDKs available
