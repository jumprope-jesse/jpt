# Vector Embeddings with pgvector for Search

*Source: [Embeddings are a good starting point for the AI curious app developer](https://bawolf.substack.com/p/embeddings-are-a-good-starting-point) - April 2024*

## Why Embeddings

Vector embeddings compress considerable human knowledge into arrays of numbers. They make similarity search that "just works" - even across languages. Features that used to be substantial specialized projects become approachable for individual engineers.

## pgvector: Postgres Extension

Use pgvector instead of a dedicated vector database when you need to combine embedding search with business logic (filtering, scoring, joins).

**Tradeoffs**:
- Not the fastest pure vector search
- But avoids comparing results across multiple data sources
- Standard SQL logic + embedding operations in one query

Libraries available for most ORMs (drizzle-orm for TypeScript, Ecto for Elixir).

## Creating Embeddings

Encode the attributes that best represent what users search for:

```typescript
const createIconEmbeddingsString = (icon) =>
  `icon: "${icon.name}", categories: [${categories}] tags: [${tags}]`;
```

**Key decisions**:
- Include attributes relevant to search (name, categories, tags)
- Exclude irrelevant metadata (dimensions, set name)
- Model: OpenAI `text-embedding-3-small` works well

## Similarity Search

OpenAI embeddings work best with cosine distance:

```sql
SELECT
  1 - cosine_distance(search_query.embedding, icon.embedding) as similarity,
  *
FROM icon
JOIN search_query ON search_query.text = 'dog'
ORDER BY cosine_distance(search_query.embedding, icon.embedding) ASC
LIMIT 50;
```

**Works across languages**: Query "chien" (French) or "犬" (Japanese) returns relevant dog icons.

**Limit by count, not threshold**: Absolute distance varies by query. Limiting to top N results is more reliable than a similarity threshold.

## Filtering with SQL

Combine vector search with standard WHERE clauses:

```sql
SELECT *
FROM icon
JOIN search_query ON search_query.text = 'dog'
JOIN icon_set ON icon_set.slug = icon.icon_set_slug
WHERE icon_set.slug IN ('lucide', 'mdi')
ORDER BY cosine_distance(search_query.embedding, icon.embedding) ASC
LIMIT 50;
```

## Ranking with User Feedback

Combine embedding similarity with click data:

```sql
SELECT
  (
    0.5 * COALESCE(1 - cosine_distance(search_query.embedding, icon.embedding), 0)
    + 0.5 * COALESCE(
      click_count::decimal / max(click_count) OVER (),
      0
    )
  ) AS score,
  icon.*
FROM icon
LEFT JOIN search_query_selection ON icon.id = search_query_selection.icon_id
LEFT JOIN search_query ON search_query.text = 'dog'
  AND search_query.id = search_query_selection.search_query_id
ORDER BY score DESC
LIMIT 50;
```

**Algorithm** (inspired by Simulacra paper):
1. Cosine similarity (0-1) × 0.5
2. Normalized clicks (0-1) × 0.5
3. Sum for final score

## Similar Item Recommendations

Find similar items by comparing embeddings directly:

```sql
WITH current_icon AS (
  SELECT embedding, slug, icon_set_slug
  FROM icon
  WHERE icon_set_slug = 'lucide' AND slug = 'activity'
)
SELECT *
FROM icon
INNER JOIN current_icon ON icon.icon_set_slug = current_icon.icon_set_slug
  AND icon.slug != current_icon.slug
ORDER BY 1 - cosine_distance(icon.embedding, current_icon.embedding)
LIMIT 50;
```

## Implementation Checklist

| Component | Recommendation |
|-----------|----------------|
| Vector DB | pgvector if you need SQL joins/filters |
| Embedding model | OpenAI `text-embedding-3-small` |
| Distance metric | Cosine distance (for OpenAI embeddings) |
| Search limit | Top N results, not similarity threshold |
| Hosts | Neon, Supabase, fly.io |

## vs Keyword Search

Traditional search: Brittle, depends on exact keyword matches and manually curated tags.

Embedding search: Robust similarity matching, works across synonyms and languages, degrades gracefully.

## Related

- `cognita-rag-framework.md` - Full RAG framework with vector DB support
- `aws-bedrock-knowledge-bases-rag.md` - Managed RAG service
