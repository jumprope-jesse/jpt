# GitLab Postgres Schema Design

**Source:** https://shekhargulati.com/2022/07/08/my-notes-on-gitlabs-postgres-schema-design/
**Author:** Shekhar Gulati
**Date:** 2022-07-08
**Type:** Production schema analysis from 34,000-line structure.sql (573 tables)

## Overview

Analysis of GitLab's PostgreSQL schema - one of the few large-scale open-source monolithic applications with visible production database design. GitLab is a Ruby on Rails DevOps platform using `structure.sql` instead of `schema.rb` for schema management.

## Key Design Decisions

### 1. Primary Key Types

**Strategy:** Choose based on table growth expectations, not standardization.

- **380 tables:** `bigserial` (int8, up to 9.2 quintillion)
- **170 tables:** `serial` (int4, up to 2.1 billion)
- **23 tables:** Composite primary keys
- **0 tables:** UUID v4 (avoided due to 25% storage overhead, 75% insert rate drop)

**Performance impact of changing int→bigint:**
- 10M row table: ~11 seconds to alter column type
- Requires table rewrite and exclusive lock
- Sequence type change is fast (4ms)

**Tradeoff:** Some tables like `issues`, `web_hooks`, `merge_requests` use `serial` which may be risky for SaaS scale (GitHub has 128M+ repos × 20 issues/repo would overflow).

### 2. Internal vs External IDs

**Pattern:** Use two IDs to avoid exposing primary keys and provide better UX.

```sql
CREATE TABLE issues (
    id integer NOT NULL,        -- Internal, never exposed
    iid integer,                -- External, user-facing
    project_id integer,
    -- ...
);
CREATE UNIQUE INDEX index_issues_on_project_id_and_iid
  ON issues (project_id, iid);
```

**Why:** Issues should start at #1 per project, not reveal total issue count, prevent guessability.

- Unique constraint on `(project_id, iid)` ensures per-project sequential numbering
- Example: `gitlab.com/user/sg/-/issues/1` and `gitlab.com/user/sg2/-/issues/1` both exist

### 3. Text vs Varchar with CHECK Constraints

**Preferred:** `text` with `CHECK` constraints over `varchar(n)`

```sql
CREATE TABLE audit_events (
    author_name text,
    entity_path text,
    target_details text,
    CONSTRAINT check_83ff8406e2 CHECK ((char_length(author_name) <= 255)),
    CONSTRAINT check_492aaa021d CHECK ((char_length(entity_path) <= 5500)),
    CONSTRAINT check_d493ec90b5 CHECK ((char_length(target_details) <= 5500))
);
```

**Benefits:**
- Schema evolution: Increasing `varchar(200)` → `varchar(300)` is instant, but decreasing `varchar(300)` → `varchar(100)` requires table rewrite (36s for 10M rows)
- With `text` + `CHECK`: Drop constraint (instant) + add new constraint (~2s for 10M rows)
- Same storage under the hood (both use `varlena`)

**Exception:** Use `character varying` without length checks where unlimited flexibility is needed (e.g., `key`, `value` columns).

### 4. Naming Conventions

- **Tables:** Plural, snake_case (`issues`, `merge_requests`, `audit_events`)
- **Columns:** snake_case (`created_at`, `is_active`, `lock_version`)
- **Namespacing:** Prefixes for related tables (`merge_request_*`, `ci_*`, `packages_*`)
- **Booleans:** Three patterns depending on semantics
  - `is_active`, `has_vulnerabilities`
  - `enabled`, `template`
  - `closed_at` (timestamp implies state)
- **Indexes:** `index_#{table}_on_#{col1}_and_#{col2}_#{condition}`
  - Example: `index_services_on_type_and_id_and_template_when_active`

### 5. Timestamp Types

**Pattern:** `timestamp without time zone` for system actions, `timestamp with time zone` for user actions.

```sql
CREATE TABLE issues (
    created_at timestamp without time zone,  -- System timestamp
    updated_at timestamp without time zone,  -- System timestamp
    closed_at timestamp with time zone,      -- User action (includes timezone)
    closed_by_id integer,
);
```

```sql
CREATE TABLE merge_request_metrics (
    -- System-driven timestamps (no timezone)
    latest_build_started_at timestamp without time zone,
    latest_build_finished_at timestamp without time zone,
    merged_at timestamp without time zone,

    -- User-driven timestamps (with timezone)
    latest_closed_at timestamp with time zone,
    first_comment_at timestamp with time zone,
    first_commit_at timestamp with time zone,
);
```

**Rationale:** System events happen server-side in known timezone. User events need timezone context.

### 6. Foreign Key Constraints

**General rule:** Use foreign keys with appropriate `ON DELETE` actions.

**Exceptions:** Skip FKs on immutable log tables to avoid performance degradation.

- **No FKs:** `audit_events`, `abuse_reports`, `web_hooks_logs`, `spam_logs`
  - Immutable (insert-only)
  - High volume (millions+ rows)
  - Even small FK overhead compounds at scale

**FK Actions used:**
```sql
-- CASCADE: Delete children when parent deleted (careful with fan-out)
ALTER TABLE todos
    ADD CONSTRAINT fk_rails_a27c483435
    FOREIGN KEY (group_id) REFERENCES namespaces(id) ON DELETE CASCADE;

-- RESTRICT: Prevent parent deletion if children exist
ALTER TABLE projects
    ADD CONSTRAINT fk_projects_namespace_id
    FOREIGN KEY (namespace_id) REFERENCES namespaces(id) ON DELETE RESTRICT;

-- SET NULL: Orphan children by nulling reference
ALTER TABLE authentication_events
    ADD CONSTRAINT fk_rails_b204656a54
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL;
```

**Caution:** `ON DELETE CASCADE` can cascade large deletes. If one parent → thousands of children, single row deletion becomes expensive transaction.

### 7. Table Partitioning

Used for high-volume tables to improve query performance.

**RANGE partitioning** (time-series):
```sql
CREATE TABLE audit_events (
    id bigint NOT NULL,
    created_at timestamp without time zone NOT NULL,
    -- ...
)
PARTITION BY RANGE (created_at);
```

**LIST partitioning** (discrete values):
```sql
-- loose_foreign_keys_deleted_records partitioned by discrete column values
```

**HASH partitioning** (even distribution):
```sql
-- product_analytics_events_experimental uses hash partitioning
```

### 8. Full-Text Search with Trigrams

**Use case:** Efficient `LIKE '%pattern%'` searches.

```sql
CREATE EXTENSION pg_trgm;

CREATE INDEX index_issues_on_title_trigram
  ON issues USING gin (title gin_trgm_ops);

CREATE INDEX index_issues_on_description_trigram
  ON issues USING gin (description gin_trgm_ops);
```

**Performance:**
- Btree index: Sequential scan for `LIKE '%pattern%'`
- GIN trigram index: Bitmap index scan (much faster)

**Example query plan:**
```sql
-- Before GIN index:
Seq Scan on words (cost=0.00..211.20)

-- After GIN index:
Bitmap Index Scan on index_words_on_word_trigram (cost=0.00..12.01)
  -> Bitmap Heap Scan (cost=12.01..16.02)
```

**Also uses:** `tsvector` for full-text search where more sophisticated search is needed.

**Advantages of in-database text search:**
- Real-time indexing (no lag)
- Access to complete data
- Reduced architecture complexity

### 9. JSONB for Flexible Data

**Use cases:**
1. Dump request data for later processing
2. Support extra/optional fields
3. One-to-many where children don't need separate identity
4. Key-value storage
5. Simpler EAV (entity-attribute-value) designs

**Examples:**

```sql
-- Request payload dump
CREATE TABLE error_tracking_error_events (
    id bigint NOT NULL,
    payload jsonb DEFAULT '{}'::jsonb NOT NULL,
);

-- Unknown parameter count
CREATE TABLE operations_strategies (
    id bigint NOT NULL,
    feature_flag_id bigint NOT NULL,
    name character varying(255) NOT NULL,
    parameters jsonb DEFAULT '{}'::jsonb NOT NULL
);

-- Extra fields support
CREATE TABLE packages_debian_file_metadata (
    package_file_id bigint NOT NULL,
    file_type smallint NOT NULL,
    component text,
    architecture text,
    fields jsonb,  -- Flexible additional fields
);

-- Store data already in JSON format
CREATE TABLE vulnerability_finding_evidences (
    id bigint NOT NULL,
    vulnerability_occurrence_id bigint NOT NULL,
    data jsonb DEFAULT '{}'::jsonb NOT NULL
);
```

**Benefits:** Efficient querying via PostgreSQL's JSONB operators vs storing as plain text.

### 10. Other Design Patterns

**Audit fields:**
- `updated_at` only on mutable tables
- Immutable logs (audit_events) omit `updated_at`

**Enums as smallint:**
```sql
CREATE TABLE merge_requests_compliance_violations (
    reason smallint NOT NULL,
    severity_level smallint DEFAULT 0 NOT NULL
);
```
- Space-efficient
- Caveat: Can't reorder enum values easily

**Optimistic locking:**
```sql
CREATE TABLE ci_builds (
    lock_version integer DEFAULT 0,
    CONSTRAINT check_1e2fbd1b39 CHECK ((lock_version IS NOT NULL))
);
```
- Used in 8 tables (issues, ci_builds)
- Active Record increments `lock_version` on each update
- Raises `StaleObjectError` if version mismatch detected

**IP addresses with inet type:**
```sql
CREATE TABLE audit_events (
    ip_address inet,
);
```

**Benefits:**
- Input validation (rejects `'192.168.1'`)
- Subnet operators: `<<` (contained by), `<<=` (contained or equal)
- Network functions (broadcast, netmask, etc.)

```sql
-- Find IPs in subnet
SELECT * FROM e WHERE ip_addr << inet '192.168.1.1/24';

-- Find IPs and subnets contained by/equal to range
SELECT * FROM e WHERE ip_addr <<= inet '192.168.1.1/24';
```

**Note:** Not consistently applied - some tables still use `character varying` for IPs.

**bytea for cryptographic data:**
- Used for SHA hashes, encrypted tokens, encrypted passwords, fingerprints

**Arrays for multi-valued columns:**
```sql
CREATE TABLE alert_management_alert_user_mentions (
    mentioned_users_ids integer[],
    mentioned_projects_ids integer[],
    mentioned_groups_ids integer[]
);

CREATE TABLE dast_site_profiles (
    excluded_urls text[] DEFAULT '{}'::text[] NOT NULL,
);

CREATE TABLE ci_pending_builds (
    tag_ids integer[] DEFAULT '{}'::integer[],
);
```

**Use cases:** hosts, tags, URLs, mentions - where count is variable and no separate identity needed.

## Key Lessons

1. **Context-specific decisions:** No one-size-fits-all. Choose based on table purpose, growth rate, access patterns.

2. **Performance at scale matters:** Decisions that seem trivial (UUID vs bigint, varchar vs text) compound massively at billions of rows.

3. **Plan for growth but don't over-engineer:** Some `serial` choices may cause future pain, but premature `bigserial` everywhere wastes space.

4. **Leverage PostgreSQL features:** `inet`, `jsonb`, `text` with `CHECK`, GIN indexes, partitioning - use the database's strengths.

5. **Foreign keys are usually good:** Only skip on high-volume immutable logs. The referential integrity and query optimization benefits outweigh performance concerns in most cases.

6. **Schema evolution cost:** Consider how constraints will change. `text` + `CHECK` is more flexible than `varchar(n)` when you need to adjust limits.

## Related Topics

- [PostgreSQL Index Advisor](postgres-index-advisor.md) - Automated index recommendations
- [ChartDB Schema Visualization](chartdb-schema-visualization.md) - Visualizing schema complexity
- [API Database Architecture](api-database-architecture.md) - PostgREST pattern for schema-driven APIs
- [Django ORM State](django-orm-state-2022.md) - ORM vs raw SQL tradeoffs

---

**Tags:** #postgres #schema-design #database #gitlab #production-scale #best-practices
