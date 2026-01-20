# PostgreSQL Index Advisor

**Added:** 2026-01-18
**Source:** https://github.com/supabase/index_advisor
**Author:** Supabase

## Overview

PostgreSQL extension that analyzes SQL queries and recommends indexes to improve performance. Returns specific `CREATE INDEX` statements with before/after cost estimates.

## Key Features

- Supports generic parameters (`$1`, `$2`, etc.)
- Handles materialized views
- Can identify tables/columns hidden behind views
- Returns cost estimates (startup and total) before/after indexing

## Installation

Requires hypopg extension.

```bash
git clone https://github.com/supabase/index_advisor.git
cd index_advisor
sudo make install
```

```sql
CREATE EXTENSION IF NOT EXISTS index_advisor CASCADE;
```

## API

```sql
index_advisor(query text)
returns table (
    startup_cost_before jsonb,
    startup_cost_after jsonb,
    total_cost_before jsonb,
    total_cost_after jsonb,
    index_statements text[],
    errors text[]
)
```

## Usage

```sql
-- Simple single-table query
SELECT * FROM index_advisor('SELECT book.id FROM book WHERE title = $1');

-- Returns:
-- startup_cost_before: 0.00 -> 1.17
-- total_cost_before: 25.88 -> 6.40
-- index_statements: {"CREATE INDEX ON public.book USING btree (title)"}
```

For complex JOINs, returns multiple index suggestions prioritized by impact.

## When to Use

- Troubleshooting slow queries
- Pre-deployment performance review
- Database optimization audits
- Learning what indexes would help specific query patterns

## Related

- hypopg - hypothetical indexes extension (required dependency)
- pg_stat_statements - for finding slow queries to feed into index_advisor
- Supabase also maintains PGlite, PGMQ
