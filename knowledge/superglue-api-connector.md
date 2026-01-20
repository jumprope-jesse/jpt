# Superglue: Self-Writing API Connector

*Source: [GitHub - superglue-ai/superglue](https://github.com/superglue-ai/superglue) - Added: 2026-01-18*

## What It Is

Superglue is an open-source API connector that uses LLMs to automatically generate integration code. It translates data from external systems into exactly the format you need, acting as a proxy that extracts, maps, and transforms data so developers don't have to write and maintain complex integration code.

**Key insight:** Instead of writing API integration boilerplate, describe what you want and let the LLM generate deterministic, high-performance translation code.

## Core Features

| Feature | Description |
|---------|-------------|
| **LLM-Powered Translations** | One-off code generation for data extraction and mapping |
| **Self-Healing** | Detects format changes in source APIs and updates translations automatically |
| **Multi-Format Support** | APIs, GraphQL, files (CSV, JSON, XML), legacy systems |
| **Schema Validation** | Ensure output compliance with your specified schemas |
| **Flexible Auth** | Header auth, API keys, OAuth, and more |
| **Smart Pagination** | Handle different pagination styles automatically |
| **Caching & Retry** | Built-in for reliability |

## How It Works

```
┌─────────────┐     ┌──────────────────┐     ┌───────────────┐
│ Your App    │────▶│ Superglue Proxy  │────▶│ External APIs │
│             │     │ (LLM-generated   │     │ & Data Sources│
└─────────────┘     │  transformations)│     └───────────────┘
                    └──────────────────┘
```

1. Describe what data you want and the output format (schema)
2. Superglue uses an LLM to generate transformation code
3. Generated code runs deterministically (no LLM at runtime)
4. Self-healing kicks in when source formats change

## Quick Example

```javascript
import { SuperglueClient } from "@superglue/client";

const superglue = new SuperglueClient({ apiKey: "***" });

const config = {
  urlHost: "https://futuramaapi.com",
  urlPath: "/graphql",
  instruction: "get all characters from the show",
  responseSchema: {
    type: "object",
    properties: {
      characters: {
        type: "array",
        items: {
          type: "object",
          properties: {
            name: { type: "string" },
            species: { type: "string", description: "lowercased" }
          }
        }
      }
    }
  }
};

const result = await superglue.call({ endpoint: config });
// Returns data in exactly the schema you specified
```

## Deployment Options

### Hosted Version
- Sign up at superglue.cloud
- `npm install @superglue/client`
- Use their API endpoint

### Self-Hosted (Docker)

```bash
docker pull superglueai/superglue

# Required env vars
GRAPHQL_PORT=3000
WEB_PORT=3001
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4o-2024-11-20
AUTH_TOKEN=your-auth-token

# Optional: Redis for persistence (vs in-memory)
DATASTORE_TYPE=redis
REDIS_HOST=localhost
REDIS_PORT=6379

docker run -d \
  --name superglue \
  --env-file .env \
  -p 3000:3000 \
  -p 3001:3001 \
  superglueai/superglue
```

Web dashboard at `http://localhost:3001/` for configuration management.

## When to Use Superglue

**Good fit:**
- Integrating with many third-party APIs with varying formats
- Need schema normalization across diverse data sources
- Want to reduce API integration maintenance burden
- Building ETL pipelines that need to adapt to upstream changes
- Rapid prototyping of data integrations

**Trade-offs:**
- Requires OpenAI API key for code generation
- Generated code may need review for edge cases
- Self-healing depends on LLM's ability to understand format changes
- Another abstraction layer between you and the data source

## Comparison: API Integration Approaches

| Approach | Code Generation | Self-Healing | Flexibility | Control |
|----------|-----------------|--------------|-------------|---------|
| Superglue | LLM-powered | Yes | High | Medium |
| **Nango** | Pre-built + custom | No | High | High |
| Manual integration | Manual | No | High | High |
| Zapier/n8n | No-code | No | Medium | Low |
| GraphQL federation | Schema-based | No | High | High |
| Airbyte/Fivetran | Pre-built connectors | Partial | Low | Low |

### Nango vs Superglue

[Nango](https://www.nango.dev/) is an open unified API with 190+ pre-built integrations. Key differences:
- **Auth handling**: Nango excels at managed OAuth - embed their UI for user authorization
- **Pre-built vs generated**: Nango has ready connectors; Superglue generates transformation code
- **Two-way sync**: Nango supports continuous bidirectional sync with webhooks
- **Compliance**: SOC2, GDPR compliant out of the box
- **Self-hostable**: Both are open-source and self-hostable

## Related

- EnrichMCP (see `ai-agent-architecture.md`) - Semantic layer for MCP data access
- ContextForge Gateway (see `ai-agent-architecture.md`) - REST-to-MCP conversion
- Airweave (see `ai-agent-architecture.md`) - Universal app search for agents

## License

GPL licensed (server), MIT licensed (client SDKs).
