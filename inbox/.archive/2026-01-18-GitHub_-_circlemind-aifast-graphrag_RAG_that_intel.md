---
type: link
source: notion
url: https://github.com/circlemind-ai/fast-graphrag
notion_type: Software Repo
tags: ['Running']
created: 2024-11-19T01:22:00.000Z
---

# GitHub - circlemind-ai/fast-graphrag: RAG that intelligently adapts to your use case, data, and queries

## Overview (from Notion)
- The Fast GraphRAG framework offers a streamlined way to integrate intelligent retrieval workflows, potentially aiding in both personal projects and business applications.
- As a software engineer and company founder, you could leverage this technology for building innovative applications that utilize large language models, enhancing user interaction and data retrieval.
- The cost-effectiveness of Fast GraphRAG might allow you to allocate resources more efficiently in your startup, especially if you're exploring AI-driven solutions.
- Its focus on dynamic data management could help in maintaining an adaptive business model that evolves with user needs and market trends.
- Engaging with the open-source community around this project can provide networking opportunities and insights into cutting-edge technology, beneficial for both personal growth and business development.
- Consider alternate views: while this tech promises efficiency, reliance on AI tools may raise concerns about data privacy and the quality of retrieved information. Balancing automation with human oversight is crucial.

## AI Summary (from Notion)
Fast GraphRAG is a streamlined framework for high-precision retrieval workflows, offering interpretable knowledge graphs that are cost-effective and efficient. It supports dynamic data updates and intelligent exploration, making it suitable for various applications. Installation is straightforward via PyPi, and contributions are welcomed to enhance the open-source community. The service also provides a managed option with free initial requests.

## Content (from Notion)

# 

###          

Streamlined and promptable Fast GraphRAG framework designed for interpretable, high-precision, agent-driven retrieval workflows.  Looking for a Managed Service? » 

### Install | Quickstart | Community | Report Bug | Request Feature

Note

Using The Wizard of Oz, fast-graphrag costs $0.08 vs. graphrag $0.48 — a 6x costs saving that further improves with data size and number of insertions. Stay tuned for the official benchmarks, and join us as a contributor!

## Features

- Interpretable and Debuggable Knowledge: Graphs offer a human-navigable view of knowledge that can be queried, visualized, and updated.
- Fast, Low-cost, and Efficient: Designed to run at scale without heavy resource or cost requirements.
- Dynamic Data: Automatically generate and refine graphs to best fit your domain and ontology needs.
- Incremental Updates: Supports real-time updates as your data evolves.
- Intelligent Exploration: Leverages PageRank-based graph exploration for enhanced accuracy and dependability.
- Asynchronous & Typed: Fully asynchronous, with complete type support for robust and predictable workflows.
Fast GraphRAG is built to fit seamlessly into your retrieval pipeline, giving you the power of advanced RAG, without the overhead of building and designing agentic workflows.

## Install

Install from PyPi (recommended)

```plain text
pip install fast-graphrag
```

Install from source

```plain text
# clone this repo first
cd fast-graphrag
poetry install
```

## Quickstart

Set the OpenAI API key in the environment:

```plain text
export OPENAI_API_KEY="sk-..."
```

Download a copy of A Christmas Carol by Charles Dickens:

```plain text
curl https://raw.githubusercontent.com/circlemind-ai/fast-graphrag/refs/heads/main/mock_data.txt > ./book.txt
```

Use the Python snippet below:

```plain text
from fast_graphrag import GraphRAG

DOMAIN = "Analyze this story and identify the characters. Focus on how they interact with each other, the locations they explore, and their relationships."

EXAMPLE_QUERIES = [
    "What is the significance of Christmas Eve in A Christmas Carol?",
    "How does the setting of Victorian London contribute to the story's themes?",
    "Describe the chain of events that leads to Scrooge's transformation.",
    "How does Dickens use the different spirits (Past, Present, and Future) to guide Scrooge?",
    "Why does Dickens choose to divide the story into \"staves\" rather than chapters?"
]

ENTITY_TYPES = ["Character", "Animal", "Place", "Object", "Activty", "Event"]

grag = GraphRAG(
    working_dir="./book_example",
    domain=DOMAIN,
    example_queries="\n".join(EXAMPLE_QUERIES),
    entity_types=ENTITY_TYPES
)

with open("./book.txt") as f:
    grag.insert(f.read())

print(grag.query("Who is Scrooge?").response)
```

The next time you initialize fast-graphrag from the same working directory, it will retain all the knowledge automatically.

## Contributing

Whether it's big or small, we love contributions. Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated. Check out our guide to see how to get started.

Not sure where to get started? You can join our Discord and ask us any questions there.

## Philosophy

Our mission is to increase the number of successful GenAI applications in the world. To do that, we build memory and data tools that enable LLM apps to leverage highly specialized retrieval pipelines without the complexity of setting up and maintaining agentic workflows.

## Open-source or Managed Service

This repo is under the MIT License. See LICENSE.txt for more information.

The fastest and most reliable way to get started with Fast GraphRAG is using our managed service. Your first 100 requests are free every month, after which you pay based on usage.

#    

To learn more about our managed service, book a demo or see our docs.

## Conversation

Contributor

###  YuhangSong  commented Nov 1, 2024

No description provided.

Yuhang Song added 2 commits  November 1, 2024 20:52

chore: update .gitignore

be254e1

chore: update .gitignore

687281e

YuhangSong merged commit f364179 into main Nov 1, 2024

3 checks passed

liukidar deleted the add_git_ignore branch  November 1, 2024 23:19

Sign up for free to join this conversation on GitHub. Already have an account? Sign in to comment

Reviewers

No reviews

Assignees

No one assigned

Labels

None yet

Projects

None yet

Milestone

No milestone


