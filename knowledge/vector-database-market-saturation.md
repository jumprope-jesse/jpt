# Vector Database Market Saturation and the Reinvention of Search

*Source: [Are we at peak vector database?](https://softwaredoug.com/blog/2024/01/24/are-we-at-peak-vector-db) by Doug Turnbull - January 2024*

A veteran search engineer's perspective on the proliferation of vector databases and what it means for the evolution of retrieval systems.

## The Current State: Too Many Options

As of early 2024, the vector database market has dozens of options across multiple categories:

**Pure Vector DBs**: Pinecone, QDrant, Milvus/Zilliz, Weaviate, Turbopuffer, MyScale

**Open Source Search Engines**: Solr, Elasticsearch, OpenSearch, Vespa

**Libraries**: Annoy, FAISS, NMSLib, HNSWLib, Lucene

**Open Source DBs Adding Vectors**: Redis, PGVector, Cassandra, Mongo

**Cloud Solutions**: Google Vertex, Azure AI Search

### Comparison to NoSQL Era

In the NoSQL paradigm, each category typically had 2-3 dominant players:
- Document databases: MongoDB, CouchDB
- Columnar stores: Cassandra, Scylla, HBase

Yet vector search has dozens of options, creating overwhelming choice for customers.

## The Real Problems Aren't Vector Retrieval

Vector similarity search itself is increasingly solved. The hard problems are everything around it:

### 1. Intent Classification
Given a "query," how do I:
- Know whether I can solve the problem (RAG viability)
- Route the query to the correct handler
- Determine if this is even a retrieval problem

### 2. Inference and Reranking
Given a query and candidate vectors:
- How to perform inference on arbitrary models (TensorFlow, etc.)
- How to rerank for actual relevance vs. just similarity

### 3. Diversity
How to broaden the candidate pool beyond "similar to vectors":
- Get at multiple possible intents
- Avoid filter bubbles
- Balance exploration vs. exploitation

### 4. Hybrid Search
Combining approaches:
- Direct lexical signals (BM25)
- Simple filtering
- Natural language understanding
- Structured queries

### 5. Evaluation
Nobody has created robust ways to evaluate:
- Quality of context for RAG
- When vector retrieval is appropriate
- Trade-offs between approaches

## Why We're NOT at Peak Vector DB

Capital and brainpower need a place to focus on rethinking retrieval problems - similar to how NoSQL forced rethinking of databases.

### The Learning Curve Reality

The average "AI Engineer" will:
1. Think first of vector retrieval (it's trendy)
2. Stand up their app quickly
3. **Only then** stumble into all the problems listed above
4. Learn they need traditional search engineering concepts

This mirrors how search engineers of the past backed into problems only after standing up Solr or Elasticsearch.

### The Coming Shift: Retrieval-Driven Applications

More surfaces will be driven by "retrieval-ish" things - not traditional search boxes:
- Search-but-not-search interfaces
- Real-time recommendations driven by vector retrieval
- Not batch-computed nightly jobs (current standard)
- More like search engines under the hood

Author predicted this in 2016 as "Relevance Driven Applications" - happening now but through reinventing retrieval layers, not boring old search engines.

## The Inevitable Evolution

Smart vector DB companies will branch out beyond "making ANN better/more scalable" to building **complete retrieval and ranking systems** solving a tremendous array of problems. Money flows where customers see the problem.

### The SQL-After-NoSQL Pattern

Like NoSQL ultimately led back to SQL (but with NoSQL innovations), we may end up with:
- Vector DB vendors building full-blown "search engines"
- But with many more batteries included
- Native AI/Chat/RAG/whatever experiences
- Not just ANN indexes

## Key Insights

1. **Market saturation is real** - Dozens of vector DBs for one narrow problem
2. **Vector retrieval is solved** - The hard parts are intent, reranking, diversity, evaluation
3. **History repeats** - This mirrors the NoSQL cycle
4. **Consolidation coming** - Vendors will expand to full retrieval systems
5. **Search is being reinvented** - Not abandoned, but reimagined for AI-era UX

## Implications for Builders

**Don't start with a vector DB**. Start with the problem:
- What are you retrieving?
- How will users interact with it?
- Do you need filtering, ranking, diversity?
- Is this a search problem in disguise?

**Then** choose the appropriate tool - which might be pgvector (see `vector-embeddings-pgvector-search.md`) if you need SQL, or a full search engine if you need ranking and relevance.

## Related

- `vector-embeddings-pgvector-search.md` - When to use pgvector instead of dedicated vector DB
- `rag-maturity-levels.md` - The full complexity stack beyond just vector retrieval
- `search-engine-architecture.md` - Traditional search patterns being reinvented
