---
type: link
source: notion
url: https://github.com/kingjulio8238/memary
notion_type: Software Repo
tags: ['Running']
created: 2024-04-29T14:03:00.000Z
---

# GitHub - kingjulio8238/memary: Longterm Memory for Autonomous Agents.

## AI Summary (from Notion)
- Project Overview: memary is an open-source project aimed at enhancing long-term memory for autonomous agents by storing information in knowledge graphs and allowing agents to retrieve relevant information for responses.

- Key Features:
- Routing Agent: Utilizes a ReAct agent to efficiently route queries among tools.
- Knowledge Graphs: Employs Neo4j to create and manage knowledge graphs for storing agent responses.
- Memory Stream: Tracks entities in the knowledge graph to reflect user knowledge breadth.
- Entity Knowledge Store: Categorizes and ranks entities based on user engagement to enhance response relevance.

- Installation Instructions: Provides steps to set up a virtual environment and install required Python dependencies.

- Future Integrations: Plans to implement multiprocessing to process multiple queries simultaneously, enhancing responsiveness and accuracy.

- Advanced Techniques:
- Query Decomposition: Breaks complex queries into simpler components for better processing.
- Reranking: Scores and ranks responses based on their relevance to original queries, with ColBERT performing best in tests.

- Contributions: The project encourages community contributions to further develop memary, with several initial contributors named.

- Interesting Facts:
- The project aims to overcome the limitations of large language models (LLMs) with finite context windows.
- Uses advanced techniques like recursive retrieval and multi-hop reasoning for complex queries.
- Offers a demo and detailed breakdown of its components for potential users and contributors.

## Content (from Notion)

# memary: Open-Source Longterm Memory for Autonomous Agents

memary demo

## Why use memary?

Agents use LLMs that are currently constrained to finite context windows. memary overcomes this limitation by allowing your agents to store a large corpus of information in knowledge graphs, infer user knowledge through our memory modules, and only retrieve relevant information for meaningful responses.

## Features

- Routing Agent: Leverage a ReAct agent to route a query for execution amongst many tools.
- Knowledge Graph Creation & Retrieval: Leverage Neo4j to create knowledge graphs storing agent responses for later retrieval.
- Memory Stream: Track all entities stored in the knowledge graph using entity extraction. This stream reflects the user's breadth of knowledge.
- Entity Knowledge Store: Group and order all the entities in the memory stream and pass the top N entities into the context window. This knowledge store reflects the user's depth of knowledge.
## How it works

The current structure of memary is detailed in the diagram below.

The above process includes the routing agent, knoweldge graph and memory module are all integrated into the ChatAgent class located in the src/agent directory.

Raw source code for these components can also be found in their respective directories including benchmarks, notebooks, and updates.

## Installation

1. 
1.  
## Demo

To run the Streamlit app:

1. Ensure that a .env exists with necessary API keys and Neo4j credentials.
```plain text
OPENAI_API_KEY="YOUR_API_KEY"
NEO4J_PW="YOUR_NEO4J_PW"
NEO4J_URL="YOUR_NEO4J_URL"
PERPLEXITY_API_KEY="YOUR_API_KEY"
GOOGLEMAPS_API_KEY="YOUR_API_KEY"

```

1. Run: 
## Detailed Component Breakdown

### Routing Agent

- Uses the ReAct agent to plan and execute a query given the tools provided. This type of agent can reason over which of the tools to use next to further the response, feed inputs into the selected tool, and repeat the process with the output until it determines that the answer is satisfactory.
- Current tool suite: While we didn't emphasize equipping the agent with many tools, we hope to see memary help agents in the community equipped with a vast array of tools covering multi-modalities. 
- How does it work? 
- Purpose in larger system 
- Future contributions 
### Knowledge Graph

- What are knowledge graphs (KG)? 
- KGs vs other knowledge stores 
- Knowledge graphs ↔ LLMs 
- What can one do with the KG? 
- Purpose in larger system 
- Future contributions 
### Memory Module

- What is the memory module?
The memory module comprises the Memory Stream and Entity Knowledge Store. The memory module was influenced by the design of K-LaMP proposed by Microsoft Research.

1. The Memory Stream captures all entities inserted into the KG and their associated timestamps. This stream reflects the breadth of the users' knowledge, i.e., concepts users have had exposure to but no depth of exposure is inferred. 
1. The Entity Knowledge Store tracks the frequency and recency of references to each entity stored in the memory stream. This knowledge store reflects users' depth of knowledge, i.e., concepts they are more familiar with than others. 
- Purpose in larger system 
- Future contributions 
## Future Integrations

Currently memary is structured so that the ReAct agent can only process one query at a time. We hope to see multiprocessing integrated so that the agent can process many subqueries simultaneously. We expect this to improve the relevancy and accuracy of responses. The source code for both decomposing the query and reranking the many agent responses has been provided, and once multiprocessing has been added to the system, these components can easily be integrated into the main ChatAgent class. The diagram below shows how the newly integrated system would work.

### Query Decomposition

-  
-  
-  
-  
-  
### Reranking

- What is reranking? 
- Why rerank agent responses? 
- Our Approach 
- Purpose in larger system 
- Future contributions 
## Contributing

We welcome contributions from the community and hope to see memary advance as agents do!

Initial Contributors: Julian Saks, Kevin Li, Seyeong Han, Arnav Chopra, Aishwarya Balaji, Anshu Siripurapu (Hook 'em!)


