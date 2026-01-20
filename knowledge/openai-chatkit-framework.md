# OpenAI ChatKit

*Source: https://openai.github.io/chatkit-js/ - Added: 2026-01-18*

ChatKit is OpenAI's framework for building high-quality, AI-powered chat experiences. Designed for minimal setup with production-ready features out of the box.

## Key Features

- **Deep UI customization** - Feels like a first-class part of your app
- **Built-in response streaming** - Interactive, natural conversations
- **Tool/workflow integration** - Visualize agentic actions and chain-of-thought reasoning
- **Rich interactive widgets** - Rendered directly inside the chat
- **Attachment handling** - File and image uploads
- **Thread/message management** - Organize complex conversations
- **Source annotations** - Entity tagging for transparency and references

## Usage Pattern

Framework-agnostic, drop-in solution:
1. Add the ChatKit component
2. Give it a client token
3. Customize as needed

No need to build custom UIs, manage low-level chat state, or patch together features.

## Comparison to Alternatives

| Tool | Purpose |
|------|---------|
| **ChatKit** | Full drop-in chat UI from OpenAI |
| **AI Elements** | shadcn/ui components for AI apps |
| **AG-UI** | Protocol for agent-to-user communication |

## When to Use

- Quick integration of AI chat into existing applications
- Want OpenAI-native solution without building from scratch
- Need streaming, attachments, and tool visualization out of the box

## Considerations

- Vendor lock-in to OpenAI ecosystem
- Data privacy implications when handling sensitive information
- May lose personal touch if over-relying on automated chat
