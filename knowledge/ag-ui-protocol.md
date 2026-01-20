# AG-UI Protocol

*Source: https://docs.ag-ui.com/introduction - Added: 2026-01-18*

AG-UI (Agent User Interaction Protocol) is an open, lightweight, event-based protocol that standardizes how AI agents connect to user-facing applications.

## The Problem It Solves

Agentic applications break the traditional request/response model. Agents exhibit characteristics that make them challenging to serve behind REST/GraphQL APIs:

- **Long-running streams** - Agents stream intermediate work across multi-turn sessions
- **Non-deterministic UI control** - Agents can control application UI non-deterministically
- **Mixed I/O** - Simultaneous text, voice, tool calls, and state updates
- **Recursive composition** - Agents may call sub-agents, often recursively

## The AI Protocol Landscape

AG-UI positions itself as the third leg of the AI protocol ecosystem:

| Protocol | Purpose |
|----------|---------|
| **MCP** | Connects agents to tools and context |
| **A2A** | Connects agents to other agents |
| **AG-UI** | Connects agents to users (through applications) |

These protocols are complementary - a single agent can use all three simultaneously. Integration points between them are being developed for seamless handshakes.

## Key Characteristics

- **Event-based** - Designed for streaming, not request/response
- **Built on web foundations** - HTTP, WebSockets abstraction layer
- **Framework-agnostic** - Integrates with LangGraph, CrewAI, Mastra, etc.
- **Supports non-deterministic behavior** - Enabling richer, dynamic user experiences

## Origin

Born from partnership between CopilotKit, LangGraph, and CrewAI. Gaining adoption across the AI developer ecosystem.

## When to Consider

- Building agentic frontends that need dynamic, streaming communication
- Multi-turn sessions where state management is complex
- Applications mixing structured outputs (tool calls) with unstructured (text/voice)
- Avoiding ad-hoc wiring between agent runtime and frontend

## Resources

- Documentation: https://docs.ag-ui.com
- GitHub Issues: For bug reports and feature requests
- Specification Discussions: For protocol Q&A
