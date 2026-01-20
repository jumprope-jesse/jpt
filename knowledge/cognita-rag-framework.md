# Cognita - Open Source RAG Framework

*Source: [GitHub - truefoundry/cognita](https://github.com/truefoundry/cognita) - April 2024*

## Overview

Cognita is TrueFoundry's open-source framework for organizing RAG codebases. It wraps LangChain/LlamaIndex with production-ready architecture while providing a no-code UI for testing.

**Demo**: https://cognita.truefoundry.com

## Why Use Cognita Over Raw LangChain/LlamaIndex

LangChain/LlamaIndex are great for Jupyter notebook prototyping, but production requires:

1. **Chunking/Embedding Jobs** - Need to be abstracted and deployed separately, often on schedules
2. **Query Service** - FastAPI wrapper with autoscaling for multiple concurrent queries
3. **Model Deployment** - Open-source models need separate hosting as APIs
4. **Vector DB** - In-memory/disk DBs need production-grade deployment

Cognita addresses these by providing modular, API-driven components.

## Key Features

- **Modular architecture** - Parsers, loaders, embedders, retrievers are swappable
- **Incremental indexing** - Tracks indexed documents, prevents re-indexing
- **No-code UI** - Non-technical users can upload docs and query
- **API-driven** - Everything exposed as REST APIs for integration
- **Ollama support** - Run with local LLMs
- **mixedbread-ai embeddings** - SOTA open-source embeddings and reranking

## Architecture Components

| Component | Purpose |
|-----------|---------|
| Data Sources | Where documents live |
| Metadata Store | Tracks indexing state |
| LLM Gateway | Routes to model endpoints |
| Vector DB | Stores embeddings (Qdrant supported) |
| Indexing Jobs | Cron-triggered chunking/embedding |
| API Server | FastAPI query endpoints |

## Data Indexing Flow

1. Cron triggers indexing job
2. Scan data sources for files
3. Compare VectorDB state vs source (find new/updated/deleted)
4. Parse and chunk new/updated files
5. Embed chunks (OpenAI or mixedbread-ai)
6. Store in VectorDB with metadata

## Query Flow

1. User query hits API server
2. Query controller processes request
3. Retrieve relevant chunks from VectorDB
4. Optional: Rerank results
5. Generate response via LLM
6. Return to user

## Code Structure

```
backend/
├── indexer/           # Indexing job logic
├── modules/
│   ├── dataloaders/   # Local dir, S3, etc.
│   ├── embedder/      # OpenAI, mixedbread
│   ├── parsers/       # PDF, text, etc.
│   ├── reranker/      # mxbai reranker
│   ├── vector_db/     # Qdrant, others
│   └── query_controllers/  # RAG query logic
└── server/            # FastAPI app
```

## Customization

### Adding a Query Controller

```python
from backend.server.decorator import query_controller, post

@query_controller("/my-controller")
class MyCustomController:

    @post("/answer")
    def answer(query: str):
        # Custom RAG logic
        # Exposed as POST /my-controller/answer
        ...
```

Register in `backend/modules/query_controllers/__init__.py`.

### Swapping Components

- **Dataloaders**: Register in `backend/modules/dataloaders/__init__.py`
- **Embedders**: Register in `backend/modules/embedder/__init__.py`
- **Parsers**: Register in `backend/modules/parsers/__init__.py`
- **Vector DBs**: Register in `backend/modules/vector_db/__init__.py`

## Local Setup

```bash
python3 -m venv ./venv
source venv/bin/activate
pip install -r backend/requirements.txt
cp env.local.example .env
# Edit .env with your config
```

## Comparison to AWS Bedrock Knowledge Bases

| Aspect | Cognita | AWS Bedrock KB |
|--------|---------|----------------|
| Hosting | Self-hosted or TrueFoundry | Fully managed |
| Cost | Infrastructure + compute | Pay-per-use |
| Customization | Full code access | Limited to API options |
| LLMs | Any (Ollama, OpenAI, etc.) | Bedrock models only |
| Vector DB | Qdrant, extensible | OpenSearch, Pinecone |

## Related

- `aws-bedrock-knowledge-bases-rag.md` - AWS managed RAG alternative
