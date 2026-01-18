# AI Agent Architecture Patterns

## Browser-Based Data Management for Agents

*Source: [We Gave Our Browser Agent a 3MB Data Warehouse](https://100x.bot/a/we-gave-our-browser-agent-a-3mb-data-warehouse) via 100X.Bot - Added: 2026-01-18*

### The Problem

Traditional browser-based AI agents struggle with data management when scraping or collecting information from multiple sources. The standard answer of "just use a JSON array" fails at complexity, not performance:

- V8 can iterate 5,000 JSON objects in milliseconds
- But reconciling data from different sources in JavaScript means reinventing database logic
- You end up writing hash maps to simulate JOINs, complex reduce functions for moving averages
- Heavy libraries just for fuzzy string matching

**Key insight:** Agents don't need faster loops; they need a cortex. They need SQL.

### The Solution: PGLite (Postgres in WebAssembly)

Embedding PGLite directly in the browser treats data as a relational dataset rather than transient variables.

#### 1. Fuzzy Joins for Dirty Data

The hardest part of scraping is matching data that *should* be the same but isn't ("Apple Inc." vs "Apple Computer"). Using `pg_trgm` extension in-browser:

```sql
SELECT scraped.product_name, master.sku,
       similarity(scraped.product_name, master.name) as match_score
FROM scraped_products scraped
JOIN master_catalog master ON scraped.product_name % master.name
ORDER BY match_score DESC;
```

#### 2. Preserving Hierarchy with ltree

The web is a tree (DOM), but we flatten it into lists and lose context. Using `ltree` extension:

```sql
-- Find all comments in a specific sub-thread without recursion
SELECT * FROM comments WHERE path <@ 'root.123.456';
```

#### 3. Analytical Reasoning with Window Functions

Questions like "Is this price significantly lower than the average for this category?" require maintaining state in JS. In SQL, it's declarative:

```sql
SELECT product_name, price,
       AVG(price) OVER (
         PARTITION BY category
         ORDER BY scrape_date
         ROWS BETWEEN 5 PRECEDING AND CURRENT ROW
       ) as moving_avg
FROM pricing_history;
```

### How PGLite Works

- **Single-User Mode Hack**: Postgres normally needs multi-process architecture (forking). PGLite uses "single-user mode" (bootstrap mode for disaster recovery) to run as a single process in the browser tab.
- **Virtual File System**: Maps Postgres filesystem to IndexedDB for persistence across sessions.
- **Storage Limits**: Browser quotas constrain this - the sweet spot is keeping the "working set" lean (~3MB).

### Performance Characteristics

| Scale | Winner |
|-------|--------|
| Up to 10k rows | JavaScript faster |
| 100k+ rows | PGLite wins |

### Engineering Learnings

1. **Memory Wall**: Database file structure often loaded into memory. Browser tabs are hostile environments - keep working sets lean.

2. **Relaxed Durability is Mandatory**: Waiting for synchronous fsync to IndexedDB kills performance. Accept risk of losing last few milliseconds of data in exchange for 100x write performance.

3. **The Real Constraint**: Not compiling Postgres to WASM (ElectricSQL did that), but managing memory in browser's hostile environment.

### When to Use This Pattern

- Data scraping tasks needing reconciliation across sources
- Prototyping before building server infrastructure
- Privacy-sensitive apps where data shouldn't leave browser
- When JSON.filter isn't enough and you want declarative SQL

### Trade-offs

| Browser-Based (PGLite) | Server-Based |
|------------------------|--------------|
| Fast, local, no latency | Scalable, persistent, robust |
| ~3MB working set limit | Virtually unlimited |
| Session-scoped (IndexedDB) | Persistent across devices |
| Privacy-friendly | Centralized, easier backup |

---

## Agent Configuration Validation: Fail Fast Patterns

*Source: [Reddit r/aws - AWS Security Agent Feedback](https://www.reddit.com/r/aws/comments/1qcyfwc/aws_security_agent_feedback_agent_should_validate/) - Added: 2026-01-18*

### The Problem

When AI agents operate within platform constraints (allowed URLs, permissions, etc.), they often can't distinguish between:
- **Configuration mismatch**: "I'm blocked from accessing this URL by my own platform's controls"
- **Actual failure**: "The credentials are invalid"

Example: AWS Security Agent was given authentication instructions pointing to `https://api.app.example.com`, but that URL wasn't in the allowed target list. The agent got `ERR_ACCESS_DENIED` and incorrectly concluded the credentials were invalid.

### The Improvement Pattern

**Cross-reference instructions against constraints before execution:**

1. Parse URLs/resources mentioned in natural language instructions
2. Validate against configured allowlists/blocklists
3. Fail fast with clear configuration error if mismatch detected

Instead of:
> "Authentication failed - invalid credentials"

Surface:
> "Configuration error: URL 'https://api.app.example.com' in your authentication instructions is not in the allowed target URLs list."

### Alternative: Pre-flight Validation

During setup/configuration phase:
- Extract all URLs referenced in instructions
- Validate against target URL list
- Surface mismatches before the agent starts executing

### Why This Matters

AI agents are excellent at adapting testing/execution strategy, but need visibility into their own platform's configuration constraints. Without this:
- Wasted compute on doomed attempts
- Misleading error messages
- Poor user experience debugging "why didn't it work"

### Generalized Principle

Any autonomous agent operating within constraints should:
1. **Know its boundaries** - Have access to its own configuration/permission model
2. **Validate early** - Check that instructions are achievable within constraints before attempting
3. **Report accurately** - Distinguish "I can't do this" from "this didn't work"
