---
type: link
source: notion
url: https://github.com/truefoundry/cognita
notion_type: Software Repo
tags: ['Running']
created: 2024-04-28T03:47:00.000Z
---

# GitHub - truefoundry/cognita: RAG (Retrieval Augmented Generation) Framework for building modular, open source applications for production by TrueFoundry

## AI Summary (from Notion)
- Overview of Cognita: An open-source RAG (Retrieval Augmented Generation) framework designed for building modular, scalable applications for production.
- Key Features:
- Modular components that are API-driven and easily extendable.
- Supports local and production environments with no-code UI for easier testing and deployment.
- Incremental indexing by default for efficient data handling.

- Advantages:
- Central repository for parsers, loaders, and retrievers simplifies the development process.
- Non-technical users can interact with the UI to upload documents and perform queries.
- Fully API-driven, allowing integration with other systems and services.

- Architecture:
- Composed of various entities including Data Sources, Metadata Store, LLM Gateway, Vector DB, Indexing Jobs, and API Server.
- Each component plays a crucial role in data handling, query processing, and response generation.

- Getting Started:
- Instructions for setting up Python, creating virtual environments, and running Cognita locally.
- Emphasizes the importance of managing dependencies to avoid conflicts.

- Customization:
- Users can customize dataloaders, embedders, parsers, and vector databases easily.
- Instructions on how to add custom query controllers for tailored query handling.

- Deployment with Truefoundry:
- Detailed steps for registering at Truefoundry, setting up clusters, and deploying RAG applications.
- Highlights the integration of RAG applications with Truefoundry for enhanced scalability and management.

- Future Directions:
- Upcoming developments include support for more vector databases, advanced embedding techniques, RAG evaluation, visualization, and conversational chatbots.

- Open Source Contribution:
- Call for community contributions, with a link to the contribution guide for interested developers.

- Interesting Fact: Cognita aims to bridge the gap between experimentation in Jupyter notebooks and the robustness required for production environments, making it easier for developers to transition their prototypes into scalable applications.

## Content (from Notion)

# Cognita

## Why use Cognita?

Langchain/LlamaIndex provide easy to use abstractions that can be used for quick experimentation and prototyping on jupyter notebooks. But, when things move to production, there are constraints like the components should be modular, easily scalable and extendable. This is where Cognita comes in action. Cognita uses Langchain/Llamaindex under the hood and provides an organisation to your codebase, where each of the RAG component is modular, API driven and easily extendible. Cognita can be used easily in a local setup, at the same time, offers you a production ready environment along with no-code UI support. Cognita also supports incremental indexing by default.

You can try out Cognita at: https://cognita.truefoundry.com

# Contents

- Cognita 
- ✨ Getting Started
- 🐍 Installing Python and Setting Up a Virtual Environment 
- 🚀 Quickstart: Running Cognita Locally 
- 🛠️ Project Architecture 
- 💡 Writing your Query Controller (QnA): 
- 🐳 Quickstart: Deployment with Truefoundry: 
- 💖 Open Source Contribution
- 🔮 Future developments
## Introduction

Cognita is an open-source framework to organize your RAG codebase along with a frontend to play around with different RAG customizations. It provides a simple way to organize your codebase so that it becomes easy to test it locally while also being able to deploy it in a production ready environment. The key issues that arise while productionizing RAG system from a Jupyter Notebook are:

1. Chunking and Embedding Job: The chunking and embedding code usually needs to be abstracted out and deployed as a job. Sometimes the job will need to run on a schedule or be trigerred via an event to keep the data updated.
1. Query Service: The code that generates the answer from the query needs to be wrapped up in a api server like FastAPI and should be deployed as a service. This service should be able to handle multiple queries at the same time and also autoscale with higher traffic.
1. LLM / Embedding Model Deployment: Often times, if we are using open-source models, we load the model in the Jupyter notebook. This will need to be hosted as a separate service in production and model will need to be called as an API.
1. Vector DB deployment: Most testing happens on vector DBs in memory or on disk. However, in production, the DBs need to be deployed in a more scalable and reliable way.
Cognita makes it really easy to customize and experiment everything about a RAG system and still be able to deploy it in a good way. It also ships with a UI that makes it easier to try out different RAG configurations and see the results in real time. You can use it locally or with/without using any Truefoundry components. However, using Truefoundry components makes it easier to test different models and deploy the system in a scalable way. Cognita allows you to host multiple RAG systems using one app.

### Advantages of using Cognita are:

1. A central reusable repository of parsers, loaders, embedders and retrievers.
1. Ability for non-technical users to play with UI - Upload documents and perform QnA using modules built by the development team.
1. Fully API driven - which allows integration with other systems. 
### Features:

1. Support for multiple document retrievers that use Similarity Search, Query Decompostion, Document Reranking, etc
1. Support for SOTA OpenSource embeddings and reranking from mixedbread-ai
1. Support for using LLMs using Ollama
1. Support for incremental indexing that ingests entire documents in batches (reduces compute burden), keeps track of already indexed documents and prevents re-indexing of those docs.
# ✨ Getting Started

You can play around with the code locally using the python script or using the UI component that ships with the code.

# 🐍 Installing Python and Setting Up a Virtual Environment

Before you can use Cognita, you'll need to ensure that Python >=3.10.0 is installed on your system and that you can create a virtual environment for a safer and cleaner project setup.

## Setting Up a Virtual Environment

It's recommended to use a virtual environment to avoid conflicts with other projects or system-wide Python packages.

### Create a Virtual Environment:

Navigate to your project's directory in the terminal. Run the following command to create a virtual environment named venv (you can name it anything you like):

```plain text
python3 -m venv ./venv

```

### Activate the Virtual Environment:

- On Windows, activate the virtual environment by running:
```plain text
venv\Scripts\activate.bat

```

- On macOS and Linux, activate it with:
```plain text
source venv/bin/activate

```

Once your virtual environment is activated, you'll see its name in the terminal prompt. Now you're ready to install Cognita using the steps provided in the Quickstart sections.

> 

# 🚀 Quickstart: Running Cognita Locally

Following are the instructions for running Cognita locally without any additional Truefoundry dependencies

## Install necessary packages:

In the project root execute the following command:

```plain text
pip install -r backend/requirements.txt

```

## Setting up .env file:

- Create a .env file by copying copy from env.local.example set up relavant fields.
## Executing the Code:

- Now we index the data (sample-data/creditcards) by executing the following command from project root: 
- To run the query execute the following command from project root: 
> 

> 

> 

> 

# ⚒️ Project Architecture

Overall the architecture of Cognita is composed of several entities

## Cognita Components:

1. 
1.  
1. 
1. 
1.  
1.  
## Data Indexing:

1. A Cron on some schedule will trigger the Indexing Job
1. The data source associated with the collection are scanned for all data points (files)
1. The job compares the VectorDB state with data source state to figure out newly added files, updated files and deleted files. The new and updated files are downloaded
1. The newly added files and updated files are parsed and chunked into smaller pieces each with their own metadata
1. The chunks are embedded using embedding models like text-ada-002 from openai or mxbai-embed-large-v1 from mixedbread-ai
1. The embedded chunks are put into VectorDB with auto generated and provided metadata
## ❓ Question-Answering using API Server:

1. 
1. 
1. 
1. 
1. 
1. 
1.  
## 💻 Code Structure:

Entire codebase lives in backend/

```plain text
.
|-- Dockerfile
|-- README.md
|-- __init__.py
|-- backend/
|   |-- indexer/
|   |   |-- __init__.py
|   |   |-- indexer.py
|   |   |-- main.py
|   |   `-- types.py
|   |-- modules/
|   |   |-- __init__.py
|   |   |-- dataloaders/
|   |   |   |-- __init__.py
|   |   |   |-- loader.py
|   |   |   |-- localdirloader.py
|   |   |   `-- ...
|   |   |-- embedder/
|   |   |   |-- __init__.py
|   |   |   |-- embedder.py
|   |   |   -- mixbread_embedder.py
|   |   |   `-- embedding.requirements.txt
|   |   |-- metadata_store/
|   |   |   |-- base.py
|   |   |   |-- client.py
|   |   |   `-- truefoundry.py
|   |   |-- parsers/
|   |   |   |-- __init__.py
|   |   |   |-- parser.py
|   |   |   |-- pdfparser_fast.py
|   |   |   `-- ...
|   |   |-- query_controllers/
|   |   |   |-- default/
|   |   |   |   |-- controller.py
|   |   |   |   `-- types.py
|   |   |   |-- query_controller.py
|   |   |-- reranker/
|   |   |   |-- mxbai_reranker.py
|   |   |   |-- reranker.requirements.txt
|   |   |   `-- ...
|   |   `-- vector_db/
|   |       |-- __init__.py
|   |       |-- base.py
|   |       |-- qdrant.py
|   |       `-- ...
|   |-- requirements.txt
|   |-- server/
|   |   |-- __init__.py
|   |   |-- app.py
|   |   |-- decorators.py
|   |   |-- routers/
|   |   `-- services/
|   |-- settings.py
|   |-- types.py
|   `-- utils.py

```

## Customizing the Code for your usecase

Cognita goes by the tagline -

> 

Cognita makes it really easy to switch between parsers, loaders, models and retrievers.

### Customizing Dataloaders:

- 
- 
-  
### Customizing Embedder:

- The codebase currently uses OpenAIEmbeddings you can registered as default.
- You can register your custom embeddings in backend/modules/embedder/__init__.py
- You can also add your own embedder an example of which is given under backend/modules/embedder/mixbread_embedder.py. It inherits langchain embedding class.
### Customizing Parsers:

- 
- 
-  
### Adding Custom VectorDB:

- 
- 
### Rerankers:

- Rerankers are used to sort relavant documents such that top k docs can be used as context effectively reducing the context and prompt in general.
- Sample reranker is written under backend/modules/reranker/mxbai_reranker.py
# 💡 Writing your Query Controller (QnA):

Code responsible for implementing the Query interface of RAG application. The methods defined in these query controllers are added routes to your FastAPI server.

## Steps to add your custom Query Controller:

- 
- 
```plain text
from backend.server.decorator import query_controller

@query_controller("/my-controller")
class MyCustomController():
    ...
```

- Add methods to this controller as per your needs and use our http decorators like post, get, delete to make your methods an API
```plain text
from backend.server.decorator import post

@query_controller("/my-controller")
class MyCustomController():
    ...

    @post("/answer")
    def answer(query: str):
        # Write code to express your logic for answer
        # This API will be exposed as POST /my-controller/answer
        ...
```

- Import your custom controller class at backend/modules/query_controllers/__init__.py
```plain text
...
from backend.modules.query_controllers.sample_controller.controller import MyCustomController
```

> 

# 🐳 Quickstart: Deployment with Truefoundry:

To be able to Query on your own documents, follow the steps below:

1.   
1.  
1. 
1.  
1.   
1.  
## Using the RAG UI:

The following steps will showcase how to use the cognita UI to query documents:

1.  
1.  
1. 
1.  
# 💖 Open Source Contribution

Your contributions are always welcome! Feel free to contribute ideas, feedback, or create issues and bug reports if you find any! Before contributing, please read the Contribution Guide.

# 🔮 Future developments

Contributions are welcomed for the following upcoming developments:

- Support for other vector databases like Chroma, Weaviate, etc
- Support for Scalar + Binary Quantization embeddings.
- Support for RAG Evalutaion of different retrievers.
- Support for RAG Visualization.
- Support for conversational chatbot with context
- Support for RAG optimized LLMs like stable-lm-3b, dragon-yi-6b, etc
- Support for GraphDB
# Star History


