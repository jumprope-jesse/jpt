# Papr Memory: Universal Memory for GPTs

*Source: [Supercharge your GPTs with Universal Memory](https://paprai.substack.com/p/supercharge-your-gpts-with-universal) - February 2024*

## The Problem

Traditional GPTs rely on vector embeddings for knowledge retrieval, leading to:
- Storage limitations
- Scope constraints
- Context that doesn't persist across conversations or GPTs

## Papr Memory Solution

A robust retrieval system that transcends traditional storage and scope limitations:
- **Single, secure data upload** universally accessible across various GPTs and AI applications
- **Cross-GPT memory**: Same memory accessible from multiple custom GPTs
- **CRUD operations**: Save, retrieve, update, and delete personal memories
- **User authentication**: Memories are user-specific and secure

## How It Works

1. Conversation begins with a GPT using Papr Memory
2. GPT assesses whether to store or recall parts of the dialogue
3. User authentication occurs first
4. GPT executes appropriate memory action (save/retrieve/update/delete)

## Integration Steps

1. Copy the OpenAPI spec URL: `https://memory.papr.ai/openapi.yaml`
2. Create/edit GPT in ChatGPT
3. Configure → Add actions → Import from URL
4. Set up Authentication settings
5. Add privacy policy link
6. Create onboarding instructions that tell GPT to check Papr Memory before responding
7. Test in preview mode

## Use Cases

- **Personal context**: Remember user preferences, history, context across sessions
- **Multi-GPT consistency**: Share context between specialized GPTs
- **Long-term memory**: Persist information beyond single conversation

## Architecture

- OpenAPI-based integration
- User authentication layer
- RESTful CRUD operations for memories
- Works with ChatGPT's GPT Actions system

## Related

- `vector-embeddings-pgvector-search.md` - Traditional embedding-based search
- `ai-agent-architecture.md` - Agent memory and context systems
- `mcp-protocol-adoption.md` - Model Context Protocol for agent memory
