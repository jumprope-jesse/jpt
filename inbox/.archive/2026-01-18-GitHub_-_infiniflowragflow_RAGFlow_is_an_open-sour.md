---
type: link
source: notion
url: https://github.com/infiniflow/ragflow
notion_type: Software Repo
tags: ['Running']
created: 2024-04-02T03:04:00.000Z
---

# GitHub - infiniflow/ragflow: RAGFlow is an open-source RAG (Retrieval-Augmented Generation) engine based on deep document understanding.

## AI Summary (from Notion)
- Project Overview: RAGFlow is an open-source engine for Retrieval-Augmented Generation (RAG) based on deep document understanding.
- Creation Date: April 2, 2024.
- Status: Not started.
- Key Features:
- Deep document understanding for knowledge extraction.
- Template-based chunking for intelligent data handling.
- Grounded citations to reduce hallucinations in answers.
- Compatibility with diverse data sources (e.g., Word, images, structured data).
- Automated RAG workflow suitable for personal and business use.
- System Requirements: Minimum CPU of 2 cores, RAM of 8 GB, and Docker installed.
- Setup Instructions:
- Ensure proper system configurations before starting the server.
- Clone the repository and build Docker images.
- Check server status via logs and access through a web browser.
- Configurations: Important files include .env, service_conf.yaml, and docker-compose.yml for system setups and configurations.
- Building from Source: Steps provided to clone the repo and build Docker images from the source.
- Community Engagement: Encouragement for collaboration through Discord and Twitter, and an invitation to contribute to the project.
- Roadmap: A dedicated roadmap for RAGFlow is available for future developments.

## Content (from Notion)

English | 简体中文

## 💡 What is RAGFlow?

RAGFlow is an open-source RAG (Retrieval-Augmented Generation) engine based on deep document understanding. It offers a streamlined RAG workflow for businesses of any scale, combining LLM (Large Language Models) to provide truthful question-answering capabilities, backed by well-founded citations from various complex fomatted data.

## 🌟 Key Features

### 🍭 "Quality in, quality out"

- Deep document understandingbased knowledge extraction from unstructured data with complicated formats.
- Finds "needle in a data haystack" of literally unlimited tokens.
### 🍱 Template-based chunking

- Intelligent and explainable.
- Plenty of template options to choose from.
### 🌱 Grounded citations with reduced hallucinations

- Visualization of text chunking to allow human intervention.
- Quick view of the key references and traceable citations to support grounded answers.
### 🍔 Compatibility with heterogeneous data sources

- Supports Word, slides, excel, txt, images, scanned copies, structured data, web pages, and more.
### 🛀 Automated and effortless RAG workflow

- Streamlined RAG orchestration catered to both personal and large businesses.
- Configurable LLMs as well as embedding models.
- Multiple recall paired with fused re-ranking.
- Intuitive APIs for seamless integration with business.
## 🔎 System Architecture

## 🎬 Get Started

### 📝 Prerequisites

- CPU >= 2 cores
- RAM >= 8 GB
- Docker 
### 🚀 Start up the server

1.  
1.  
1.   
1.    
1.  
1.   
## 🔧 Configurations

When it comes to system configurations, you will need to manage the following files:

- .env: Keeps the fundamental setups for the system, such as SVR_HTTP_PORT, MYSQL_PASSWORD, and MINIO_PASSWORD.
- service_conf.yaml: Configures the back-end services.
- docker-compose.yml: The system relies on docker-compose.yml to start up.
You must ensure that changes to the .env file are in line with what are in the service_conf.yaml file.

> 

To update the default HTTP serving port (80), go to docker-compose.yml and change 80:80 to <YOUR_SERVING_PORT>:80.

> 

## 🛠️ Build from source

To build the Docker images from source:

```plain text
$ git clone https://github.com/infiniflow/ragflow.git
$ cd ragflow/
$ docker build -t infiniflow/ragflow:v1.0 .
$ cd ragflow/docker
$ docker compose up -d
```

## 📜 Roadmap

See the RAGFlow Roadmap 2024

## 🏄 Community

- Discord
- Twitter
## 🙌 Contributing

RAGFlow flourishes via open-source collaboration. In this spirit, we embrace diverse contributions from the community. If you would like to be a part, review our Contribution Guidelines first.


