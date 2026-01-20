---
type: link
source: notion
url: https://flowiseai.com/
notion_type: Software Repo
tags: ['Running']
created: 2024-04-05T04:07:00.000Z
---

# Flowise - Low code LLM Apps Builder

## AI Summary (from Notion)
- Project Overview: Flowise is an open-source low-code tool designed for developers to create customized LLM orchestration flows and AI agents.
- Creation Date: April 5, 2024
- Status: Not started
- Backed by: Y Combinator
- Usage: Trusted by teams globally for building LLM applications.
- Key Features:
- Iterative Development: Allows for quick iterations from testing to production using low-code approaches.
- Chatflow: Connect LLMs with various components like memory, data loaders, and moderation tools.
- Agents & Assistants: Enables the creation of autonomous agents capable of executing tasks using custom tools and APIs.
- Developer Friendly: Offers APIs, SDKs, and embedded chat options for easy integration into applications.
- Platform Agnostic: Supports running in air-gapped environments with local LLMs and vector databases.
- Installation Commands: Simple commands to install and start Flowise using npm.
- Target Audience: Developers looking for efficient ways to build and deploy LLM applications.

## Content (from Notion)

Open source low-code tool for developers to build customized LLM orchestration flow & AI agents

Github ⭐ 21K

Backed byCombinator

Trusted and used by teams around the globe

# Iterate, fast

Developing LLM apps takes countless iterations. With low code approach, we enable quick iterations to go from testing to production

- $ npm install -g flowise
- $ npx flowise start
Get Started

Features 01

Chatflow

### LLM Orchestration

Connect LLMs with memory, data loaders, cache, moderation and many more

- Langchain
- LlamaIndex
- 100+ integrations
Agents

### Agents & Assistants

Create autonomous agent that can uses tools to execute different tasks

- Custom Tools
- OpenAI Assistant
- Function Agent
- import requests
- url = "/api/v1/prediction/:id"
- def query(payload):
- response = requests.post(
- url,
- json = payload
- )
- return response.json()
- output = query({
- question: "hello!"
- )}
Developer Friendly

### API, SDK, Embed

Extend and integrate to your applications using APIs, SDK and Embedded Chat

- APIs
- Embedded Widget
- React SDK
Features 02

Platform Agnostic

### Open source LLMs

Run in air-gapped environment with local LLMs, embeddings and vector databases


