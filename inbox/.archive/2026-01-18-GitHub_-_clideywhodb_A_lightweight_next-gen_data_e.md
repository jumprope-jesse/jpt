---
type: link
source: notion
url: https://github.com/clidey/whodb
notion_type: Software Repo
tags: ['Running']
created: 2025-05-21T04:28:00.000Z
---

# GitHub - clidey/whodb: A lightweight next-gen data explorer - Postgres, MySQL, SQLite, MongoDB, Redis, MariaDB, Elastic Search, and Clickhouse with Chat interface

## Overview (from Notion)
- Data Management Made Easy: WhoDB simplifies database management, allowing you to focus on building your projects without getting bogged down by complex SQL queries.
- Natural Language Queries: The integration with ChatGPT and other AI tools allows you to interact with your data using natural language, making it accessible even if you're not a database expert.
- Efficiency for Startups: As a founder, the lightweight nature of WhoDB means it can run on minimal resources, making it suitable for startups or smaller projects without heavy infrastructure.
- Collaboration Potential: This tool can streamline collaborative efforts with your team, enhancing productivity and communication when dealing with data.
- Adaptability: WhoDB supports various databases, allowing you to pivot your projects or adopt new technologies without being tied to a specific system.
- Unique Selling Point: The focus on user-friendly interfaces and interactive visualizations can set your projects apart in a crowded market.
- Critical Perspective: While WhoDB simplifies tasks, reliance on AI for data queries may raise concerns about accuracy and understanding; balancing automation with knowledge is key.
- Future of Data Interaction: This tool represents a shift toward more intuitive ways of working with data, which could transform how software development and data analysis are approached.

## AI Summary (from Notion)
WhoDB is a lightweight database management tool that allows users to interact with data using natural language, supporting various databases like PostgreSQL and MongoDB. It features an intuitive interface, schema visualization, and fast performance, and can be quickly deployed using Docker.

## Content (from Notion)

# WhoDB

Build Status:

### "Is it magic? Is it sorcery? No, it's just WhoDB!"

### Table of Contents

1. Description
1. Key Features
1. Demo
1. Documentation
1. Quick Start
1. Development Setup
1. Frontend
1. Backend
1. FAQs
1. Contributing
1. Infrastructure
1. Contact details
## Description

WhoDB is a lightweight (<50MB), powerful, and user-friendly database management tool designed to streamline your database administration tasks. Combining the simplicity of Adminer with enhanced UX and performance, WhoDB is built with GoLang to deliver optimal speed and efficiency. With features like interactive schema visualization and inline editing, WhoDB caters to both small projects and complex enterprise systems.

WhoDB offers you the opportunity to talk to your data using natural language thanks to our integration with Ollama, ChatGPT, and Anthropic. This feature allows you to perform queries and manage your data through conversation instead of complex SQL.

## Key Features

- Conversate With Your Data: No more wasting time crafting complex SQL queries - ask away!
- Enhanced UX: A clean, intuitive interface that’s easy to navigate.
- Blazing Fast Performance: Built with GoLang for exceptional speed, including table virtualization on the frontend.
- Schema Visualization: Interactive graphs to easily visualize your database schema.
- Inline Editing & Preview: Edit and preview data directly in the interface.
- Broad Database Support: Compatible with PostgreSQL, MySQL, SQLite3, MongoDB, Redis, MariaDB, & ElasticSearch.
- Scratchpad: A Jupyter notebook-like interface for performing database queries.
## Try the demo

Experience WhoDB firsthand with our live demo.

Note: This demo is populated with a sample database from postgresDBSamples, with credentials pre-filled.

Or checkout our demo video

## Documentation

For more detailed information, check out our Documentation.

## Quick Start

Get up and running with WhoDB quickly using Docker:

```plain text
docker run -it -p 8080:8080 clidey/whodb
```

Or, use Docker Compose:

```plain text
version: "3.8"
services:
  whodb:
    image: clidey/whodb
    # volumes: # (optional for sqlite)
    #   - ./sample.db:/db/sample.db
    environment:
#      optional if you have ollama configured elsewhere. will use these defaults otherwise
#      - WHODB_OLLAMA_HOST=localhost
#      - WHODB_OLLAMA_PORT=11434

#      use this to preconfigure your Anthropic connection. endpoint will default to below
      - WHODB_ANTHROPIC_API_KEY=...
#      - WHODB_ANTHROPIC_ENDPOINT=https://api.anthropic.com/v1

#     use this to preconfigure your OpenAI connection. endpoint will default to below
      - WHODB_OPENAI_API_KEY=...
#      - WHODB_OPENAI_ENDPOINT=https://api.openai.com/v1
    ports:
      - "8080:8080"
```

Access WhoDB by navigating to http://localhost:8080 in your browser.

## Development Setup

### Prerequisites

- GoLang (latest version recommended)
- PNPM (latest version recommended)
### Frontend Setup

To start the frontend service, navigate to the frontend/ directory and run:

```plain text
pnpm i && pnpm start
```

### Backend Setup

### 1. Preparing the Frontend for the Backend (Only if you don’t have a build/ directory in core/):

If the core/ directory doesn't have a build/ folder, you'll need to build the frontend and move it to the backend directory. From the root directory, run:

```plain text
cd frontend && pnpm install && pnpm run build && rm -rf ../core/build/ && cp -r ./build ../core/ && cd -;
```

This command will compile the frontend and copy the build/ folder to core/. This step is required because Go will attempt to embed the build/ folder on each launch. You only need to do this once.

### 2. Setting up Ollama (if you'd like to enable the natural conversation integration)

Go to https://ollama.com/ and download it for your system. Once that is done, we recommend that you start out with the Llama 3.1 8b model. WhoDB will automatically detect your installed model(s) and will show you a Chat option on the left sidebar.

### 3. Starting the Backend Service

If the core/ directory already has a build/ folder, or once you've completed the step above, you can start the backend service by running:

```plain text
cd core/
go run .
```

## FAQs

What inspired the creation of WhoDB?

WhoDB was inspired by Adminer for its lightweight nature and ease of use. We aimed to build on these qualities with enhanced visualization and a consistent user experience across various databases.

How does WhoDB handle large queries?

WhoDB supports lazy loading, ensuring smooth performance even with large datasets.

What makes WhoDB different from DBeaver?

Unlike DBeaver, which is feature-rich but resource-heavy, WhoDB is designed to be lightweight and efficient, running on minimal resources—perfect for smaller setups or resource-constrained environments.

Is WhoDB compatible with any database? WhoDB supports a wide range of databases, providing a consistent experience across SQL, NoSQL, and Graph databases. Currently, it supports PostgreSQL, MySQL, SQLite3, MongoDB, Redis, MariaDB, & ElasticSearch.

How do I deploy WhoDB? WhoDB can be deployed easily using Docker or Docker Compose. See the "Quick Start" section for details.

Q: Is WhoDB suitable for production environments?

While WhoDB is lightweight and efficient, we recommend evaluating its suitability for your specific production environment.

## Contributing

We welcome contributions from the community! Feel free to open issues or submit pull requests to help improve WhoDB. We have a contribution guide here.

## Infrastructure

WhoDB's deployment and CI/CD are managed by Clidey, a no-code DevOps platform. For more information, visit https://clidey.com

Clidey Build Status:

## Contact

For any inquiries or support, please reach out to support@clidey.com.

"Is it magic? Is it sorcery? No, it's just WhoDB!"


