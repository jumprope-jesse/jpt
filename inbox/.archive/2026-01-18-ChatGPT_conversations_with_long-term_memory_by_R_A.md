---
type: link
source: notion
url: https://medium.com/@busybus/chatgpt-conversations-with-long-term-memory-23cf899f4883
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-07-07T18:50:00.000Z
---

# ChatGPT conversations with long-term memory | by R A | Medium

## AI Summary (from Notion)
- Integration of Persistent Memory: The article discusses how to enhance ChatGPT's capabilities by integrating persistent memory and information retrieval using Typesense, an open-source search engine.

- Implementation Steps:
- Set up a Typesense instance (cloud-hosted or self-hosted).
- Create a collection named "notes" to store conversation data.
- Structure the collection with fields such as body, summary, tags, and date.

- Fields for Notes Collection:
- Summary, note content, date, tags, source, and embedding fields for storing additional metadata and enabling search functionalities.

- Custom GPT Actions: Instructions on implementing a custom action in ChatGPT to connect with the Typesense API, allowing for saving and retrieving notes.

- Continuous Interaction: The setup aims to provide continuity in conversations and create a dynamic knowledge base that evolves with user interactions.

- Use Cases: The system can be used for capturing ideas, solidifying knowledge, and tracking customer queries, enhancing the overall user experience with ChatGPT.

- Versatility: This integration transforms ChatGPT into a more versatile assistant, enriching interactions through personalized memory and data management.

## Content (from Notion)

# ChatGPT conversations with long-term memory

R A

·

Follow

2 min read

·

Mar 15, 2024

Integrating persistent memory and information retrieval into your ChatGPT interactions significantly elevates its capabilities. By leveraging Typesense, an open-source search engine optimized for speed, you can store and recall your conversation histories and notes. This process turns ChatGPT into a great tool for managing information and personalizing dialogues.

## How to Implement This Feature

First, make sure your Typesense instance is up and running, accessible either through the cloud or a self-hosted setup. See my notes in this post. Typesense will act as the foundation for storing and retrieving your data.

In Typesense, create a collection named “notes.” This collection will store your conversation data, structured with fields like body, summary, tags, and date. Specifically, I suggest something like this:

The schema for the “notes” collection

Next, implement a custom action within your custom GPT to connect with the Typesense API, guided by the OpenAPI specifications. This step empowers ChatGPT to save new notes or fetch existing ones based on your commands. The OpenAPI specs provided in this gist should take you most of the way.

Specify the X-TYPESENSE-API-KEY as a custom field in the GPT action.

You can now command your custom GPT to store detailed explanations, summaries, or quick notes and retrieve them whenever needed, enriching your interactions with a persistent memory layer.

This setup not only provides continuity in your conversations with ChatGPT but also creates a dynamic, personal knowledge base that grows with every interaction. Whether it’s for capturing fleeting ideas, solidifying knowledge, or keeping track of customer queries, combining ChatGPT’s conversational depth with Typesense’s efficient data management transforms ChatGPT into an even more versatile, interactive assistant.


