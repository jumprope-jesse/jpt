---
type: link
source: notion
url: https://github.com/RedPlanetHQ/core
notion_type: Software Repo
tags: ['Running']
created: 2025-07-01T22:12:00.000Z
---

# GitHub - RedPlanetHQ/core: Your personal plug and play memory layer for LLMs

## Overview (from Notion)
- C.O.R.E allows you to maintain a personal memory layer that enhances interactions with AI, creating a more tailored experience for your needs.
- As a software engineer, this system can streamline your workflows by storing relevant data and context, making project management more efficient.
- The transparency and traceability features can help in auditing and compliance, reducing the headache of tracking changes in your projects.
- The ability to ingest and search personal data means you can keep track of your children’s activities, preferences, and milestones, ensuring you don't miss important moments.
- Consider the potential of using C.O.R.E to collaborate more effectively with your team, sharing insights and decisions that matter without losing context.
- Alternate view: Relying on AI memory may create a dependency that could hinder personal memory retention or critical thinking—balance technology with personal engagement.
- Unique viewpoint: Imagine using C.O.R.E to create a family archive, documenting conversations and memories that can be easily revisited, fostering deeper connections with your kids as they grow.

## AI Summary (from Notion)
C.O.R.E. is a private, portable memory layer for LLMs that allows users to own and manage their contextual data. It features a dynamic knowledge graph for tracking changes and decisions, supports local and cloud setups, and integrates with tools like Cursor. Key functionalities include data ingestion, search capabilities, and API access, with ongoing improvements for compatibility with Llama models.

## Content (from Notion)

## C.O.R.E.

Contextual Observation & Recall Engine

C.O.R.E is a shareable memory for LLMs which is private, portable and 100% owned by the user. You can either run it locally or use our hosted version and then connect with other tools like Cursor, Claude to share your context at multiple places.

C.O.R.E is built for two reasons:

1. To give you complete ownership of your memory, stored locally and accessible across any app needing LLM context.
1. To help SOL (your AI assistant) access your context, facts, and preferences for more relevant and personalized responses.
> 

## Demo Video

Check C.O.R.E Demo

## How is C.O.R.E different from other Memory Providers?

Unlike most memory systems—which act like basic sticky notes, only showing what’s true right now. C.O.R.E is built as a dynamic, living temporal knowledge graph:

- Every fact is a first-class “Statement” with full history, not just a static edge between entities.
- Each statement includes what was said, who said it, when it happened, and why it matters.
- You get full transparency: you can always trace the source, see what changed, and explore why the system “believes” something.
### Use Case Example: Real Change Auditing

Imagine you ask SOL: "What changed in our pricing since Q1?"

With C.O.R.E, you see exactly what prices changed, who approved them, the context (meeting, email, document), and when each update happened—enabling true compliance, auditability, and insight across products, teams, and time.

Or ask: “What does Mike know about Project Phoenix?” and get a timeline of meetings, decisions, and facts Mike was involved in, with full traceability to those specific events.

## C.O.R.E Cloud Setup

1. Sign up to Core Cloud and start building your memory graph.
1. Add your text that you want to save in memory. Once clicking on add button your memory graph will be generated.
1. Connect Core Memory MCP with Cursor
## C.O.R.E Local Setup

### Prerequisites

1. Docker
1. OpenAI API Key
### Run C.O.R.E locally

1.   
1.   
1.  
1.  
1.  
1.  
## Connecting CORE MCP with Cursor

1. 
1. 
1.   
1. 
```plain text
After every interaction, update the memory with the user's query and the assistant's
response to core-memory mcp. sessionId should be the uuid of the conversation

```

## Connecting to the API

You can also interact with C.O.R.E. programmatically via its APIs.

1.  
1.  
### Ingest API

- 
- 
- 
-  
-  
### Search API

- 
- 
- 
-  
-  
> 

## Features (v1)

### Feature Checklist

### ✅ Done

- Private memory space: You can ingest and search your own data.
- Ingest for workspace: You can ingest data into a workspace.
- Search for workspace: You can search within a workspace.
### 🛠️ In Progress / Planned

- Multiple Spaces with unique URLs
- User-controlled sharing and privacy
- Ingestion filters rules
- Granular API Key Permissions
- Improved Session and Space Support
- Audit Logging & API Key Management
- Role-Based Access Control
- Webhooks & Notifications
## Usage Guidelines

Store:

- Conversation history
- User preferences
- Task context
- Reference materials
Don't Store:

- Sensitive data (PII)
- Credentials
- System logs
- Temporary data

