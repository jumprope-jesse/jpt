# RAG Application Maturity Levels

*Source: [Levels of Complexity: RAG Applications](https://jxnl.github.io/blog/writing/2024/02/28/levels-of-complexity-rag-applications/) by Jason Liu (jxnl) - February 2024*

A progressive guide to building RAG applications from basic to production-ready. Each level builds on the previous.

---

## Level 1: The Basics

Core pipeline: traverse files → chunk text → embed → store → query.

### Processing Pipeline

```python
class TextChunk(BaseModel):
    id: int
    text: str
    embedding: np.array
    filename: str
    uuid: str = Field(default_factory=uuid.uuid4)

def flatmap(f, items):
    for item in items:
        for subitem in f(item):
            yield subitem

def chunk_text(items, window_size, overlap=0):
    for i in range(0, len(items), window_size-overlap):
        yield TextChunk(
            text=items[i:i+window_size],
            embedding=None,
            filename=items[i].filename
        )

# Main flow
texts = get_texts()
chunks = flatmap(chunk_text, texts)
batched_chunks = batched(chunks, 10)
for chunks in batched_chunks:
    chunk_with_embedding = embed_batch(chunks)
    save_batch(chunk_with_embedding)
```

### Search Pipeline

```python
def search(question: str) -> List[TextChunk]:
    embeddings = embedding_api(texts=[question])
    results = db.search(question)
    return results
```

### Answer Pipeline

```python
def answer(question: str, results: List[TextChunk]) -> str:
    return client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt(question, results)}
        ]
    )
```

---

## Level 2: Structured Processing

Improvements over basics:
- Better asyncio with semaphores
- Improved chunking strategies
- Retry mechanisms

### Search Enhancements

1. **Better Ranking** (Cohere reranker)
2. **Query Expansion/Rewriting**
3. **Parallel Queries**

```python
class SearchQuery(BaseModel):
    semantic_search: str

def extract_query(question: str) -> Iterable[SearchQuery]:
    return client.completions.create(
        model="gpt-3.5-turbo",
        messages=[...],
        response_model=Iterable[SearchQuery]
    )

def rerank(question: str, results: List[TextChunk]) -> List[TextChunk]:
    return cohere_api(
        question=question,
        texts=[chunk.text for chunk in results]
    )
```

### Structured Responses

```python
class MultiPartResponse(BaseModel):
    response: str
    followups: List[str]
    sources: List[int]  # Citations

def answer(question: str, results: List[TextChunk]) -> Iterable[MultiPartResponse]:
    return client.chat.completions.create(
        model="gpt-3.5-turbo",
        stream=True,
        response_model=instructor.Partial[MultiPartResponse],
        messages=[...]
    )
```

---

## Level 3: Observability

Comprehensive logging to pinpoint bottlenecks. Use **wide event tracking** (see `wide-events-observability.md`).

### What to Log

| Log Type | Purpose |
|----------|---------|
| Query rewrites | Debug when complaints arise; found "latest" was selecting current date instead of 1 week |
| Citations | What was shown vs. cited; identify important chunks |
| Mean cosine scores | Cheaply identify poorly performing queries |
| Reranker scores | Same as above |
| User metadata | Org ID, user role, device type, geo, language |

### Insights from Metadata

- Different devices → shorter queries → worse performance
- New orgs → question patterns not well served
- Group by attributes, review weekly during standup

---

## Level 4: Evaluations

Two systems to evaluate: **Search** and **QA**.

### Evaluating Search (Precision/Recall@K)

Use synthetic data: pick random chunks, generate questions they could answer, verify retrieval.

```python
def test():
    text_chunk = sample_text_chunk()
    questions = ask_ai(f"generate questions that could be answered by {text_chunk.text}")
    for question in questions:
        search_results = search(question)
    return {
        "recall@5": (1 if text_chunk in search_results[:5] else 0),
    }

average_recall = sum(test() for _ in range(n)) / n
```

### Evaluating QA

Build datasets with actual answers, not just questions.

```python
def test():
    text_chunk = sample_text_chunks(n=...)
    question, answer = ask_ai(f"generate questions and answers for {text_chunk.text}")
    ai_answer = rag_app(question)
    return ask_ai(f"for the question {question} is the answer {ai_answer} correct given that {answer} is the correct answer?")
```

### Feedback Systems

**Use thumbs up/down** not 5-star ratings. Binary is more reliable.

---

## Level 5: Understanding Shortcomings

With synthetic + production data and multiple scores, do exploratory data analysis.

### Clustering Queries

Identify two types of clusters:

**1. Topics** - Captured by text chunks and queries
**2. Capabilities** - Captured by sources/metadata

Capability examples:
- Metadata questions: "who modified the file last"
- Summarization: "what are the main points"
- Timeline: "what happened in the last 3 months"
- Comparison: "differences between these two documents"

---

## Future Levels (Outline)

### Level 6: Advanced Data Handling
- Segment routing
- Processing tables
- Processing images

### Level 7: Query Enhancement
- Timeline queries
- Additional metadata enrichment

### Level 8: Summarization
- Summary indices for large corpora

### Level 9: Outcome Modeling
- Tying RAG to business outcomes

---

## Key Takeaways

1. **Start simple** - Basic pipeline first, add complexity as needed
2. **Log everything** - Wide events enable debugging and improvement
3. **Evaluate both systems** - Search quality affects QA quality
4. **Use synthetic data** - Bootstrap evaluation before having users
5. **Cluster to understand** - Find patterns in failures
6. **Binary feedback > 5-star** - More reliable signal

---

## Related

- `applied-llm-development.md` - Broader LLM production patterns
- `cognita-rag-framework.md` - Open source RAG framework
- `aws-bedrock-knowledge-bases-rag.md` - Managed RAG service
- `wide-events-observability.md` - Wide event logging patterns
