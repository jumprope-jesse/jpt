---
type: link
source: notion
url: https://github.com/kingjulio8238/memary
notion_type: Software Repo
tags: ['Running']
created: 2024-04-29T13:56:00.000Z
---

# GitHub - kingjulio8238/memary: Longterm Memory for Autonomous Agents.

## AI Summary (from Notion)
- Project Overview:
- memary is an open-source project focused on long-term memory capabilities for autonomous agents.
- It aims to overcome limitations of LLMs bound by finite context windows.

- Core Features:
- Routing Agent: Utilizes a ReAct agent to manage queries among various tools.
- Knowledge Graph: Employs Neo4j for creating and retrieving knowledge graphs that store agent responses.
- Memory Stream: Tracks stored entities in the knowledge graph and reflects user knowledge.
- Entity Knowledge Store: Organizes and ranks entities based on user interactions to enhance response quality.

- Installation and Demo:
- Requires setting up a virtual environment and installing Python dependencies.
- Instructions for running a Streamlit app with necessary API keys provided.

- System Components:
- Routing Agent: Plans and executes queries, manages tools, and saves responses in the knowledge graph.
- Knowledge Graph: Stores information in a relational format, improving context retrieval and handling complex queries.
- Memory Module: Captures user knowledge breadth and depth, allowing personalized responses based on user interactions.

- Future Directions:
- Plans to integrate multiprocessing for handling multiple queries simultaneously.
- Development of advanced memory compression techniques for efficiency.

- Contributing:
- Open to community contributions to enhance the project and expand its capabilities.
- Initial contributors include several individuals from diverse backgrounds.

- Interesting Facts:
- Knowledge graphs are highlighted as superior for storing complex relationships compared to traditional knowledge stores.
- The project aims to support multi-modalities, such as integrating image processing capabilities.

- Hot Takes:
- Emphasizes the growing need for advanced memory systems in AI to enhance user experience and response relevance.
- Highlights the importance of community collaboration in advancing AI technologies.

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


