---
type: link
source: notion
url: https://github.com/inkeep/agents
notion_type: Software Repo
tags: ['Running']
created: 2025-10-17T03:40:00.000Z
---

# GitHub - inkeep/agents: Create AI Agents in a No-Code Visual Builder or TypeScript SDK with full 2-way sync. For shipping AI assistants and multi-agent AI workflows.

## Overview (from Notion)
- Efficiency Boost: The no-code visual builder allows you to create AI agents without extensive coding, saving time for family or other business ventures.
- Versatile Applications: Use AI chat assistants for customer support or internal tasks, freeing up resources to focus on your startup's growth.
- Collaboration Flexibility: Both technical and non-technical team members can contribute, enhancing teamwork and productivity.
- Streamlined Processes: Automate repetitive tasks like updating CRMs, allowing you to dedicate more time to strategic planning.
- Sustainable Development: The open-source nature and extensibility align with modern software practices, making it a fitting tool in today's tech landscape.
- Community Engagement: Opportunities to contribute to the project can expand your network and lead to collaborations with like-minded professionals.
- Unique Perspective: Consider how integrating AI can enhance not just business efficiency but also family life—like automating reminders for family events.
- Alternate Viewpoint: While the focus is on productivity, think critically about potential over-reliance on AI and ensure personal touch in business and family interactions.

## AI Summary (from Notion)
Inkeep allows users to create AI Agents using a No-Code Visual Builder or TypeScript SDK with full 2-way sync, enabling collaboration between technical and non-technical teams. Use cases include AI chat assistants for customer support and workflow automation. The platform features a multi-agent architecture, deployment options, and observability tools, all under an Elastic License 2.0, promoting extensibility and community contributions.

## Content (from Notion)

# Inkeep Agents

With Inkeep, you can build and ship AI Agents with a No-Code Visual Builder or TypeScript SDK. Agents can be edited in code or no-code with full 2-way sync, so technical and non-technical teams can create and manage their Agents in a single platform.

## Use Cases

Inkeep Agents can operate as real-time AI Chat Assistants, for example:

- a customer experience agent for customer support, technical docs, or in-app product copilot
- an internal copilot to assist your support, sales, marketing, ops, and other teams
Agents can also be used for AI workflow automation like:

- Creating and updating knowledge bases, documentation, and blogs
- Updating CRMs, triaging helpdesk tickets, and streamlining repetitive tasks
To get started, see the docs.

## Two ways to build

### No-Code Visual Builder

A no-code drag-and-drop canvas designed to allow any team to create and manage teams of Agents visually.

### TypeScript Agents SDK

A code-first approach for building and managing multi-agent systems. Engineering teams to build with the tools and developer experience they expect.

```plain text
import { agent, subAgent } from "@inkeep/agents-sdk";

const helloAgent = subAgent({
  id: "hello-agent",
  name: "Hello Agent",
  description: "Says hello",
  prompt: 'Only reply with the word "hello", but you may do it in different variations like h3110, h3110w0rld, h3110w0rld! etc...',
});

export const basicAgent = agent({
  id: "basic-agent",
  name: "Basic Agent",
  description: "A basic agent",
  defaultSubAgent: helloAgent,
  subAgents: () => [helloAgent],
});
```

The Visual Builder and TypeScript SDK are fully interoperable: your technical and non-technical teams can edit and manage Agents in either format and switch or collaborate with others at any time.

## Platform Overview

Inkeep Open Source includes:

- A Visual Builder & TypeScript SDK with 2-way sync
- Multi-agent architecture to support teams of agents
- MCP Tools with credentials management
- A UI component library for dynamic chat experiences
- Triggering Agents via MCP, A2A, & Vercel SDK APIs
- Observability via a Traces UI & OpenTelemetry
- Easy deployment to Vercel and using Docker
For a full overview, see the Concepts guide.

## Architecture

The Inkeep Agent Platform is composed of several key services and libraries that work together:

- agents-manage-api: An API that handles configuration of Agents, Sub Agents, MCP Servers, Credentials, and Projects with a REST API.
- agents-manage-ui: Visual Builder web interface for creating and managing Agents. Writes to the agents-manage-api.
- agents-sdk: TypeScript SDK (@inkeep/agents-sdk) for declaratively defining Agents and custom tools in code. Writes to agents-manage-api.
- agents-cli: Includes various handy utilities, including inkeep push and inkeep pull which sync your TypeScript SDK code with the Visual Builder.
- agents-run-api: The Runtime API that exposes Agents as APIs and executes Agent conversations. Keeps conversation state and emits OTEL traces.
- agents-ui: A UI component library of chat interfaces for embedding rich, dynamic Agent conversational experiences in web apps.
Underneath the hood, the framework uses the Vercel AI SDK for interfacing with LLM providers. The agents-sdk/ agents-manage-api share many concepts with Vercel's ai SDK, and agents-run-api outputs a data stream compatible with Vercel's useChat and AI Elements primitives for custom UIs.

## License and Community

The Inkeep Agent Framework is licensed under the Elastic License 2.0 (ELv2) subject to Inkeep's Supplemental Terms (SUPPLEMENTAL_TERMS.md). This is a fair-code, source-available license that allows broad usage while protecting against certain competitive uses.

Inkeep is designed to be extensible and open: you can use the LLM provider of your choice, use Agents via open protocols, and easily deploy and self-host Agents in your own infra.

If you'd like to contribute, follow our contribution guide.

Follow us to stay up to date, get help, and share feedback.


