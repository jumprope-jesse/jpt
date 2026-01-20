# API Database Architecture

An architectural pattern that eliminates HTTP GET endpoint development by using PostgREST to serve PostgreSQL views directly as a RESTful API.

## Core Concept

- **Data retrieval**: Served directly from PostgreSQL via PostgREST (no backend code)
- **Data modification**: Traditional backend handles POST/PUT/PATCH/DELETE with business logic

PostgREST connects to PostgreSQL and dynamically serves tables/views as REST endpoints with filtering, sorting, paging, and JWT auth built-in.

## Key Benefits

- **No GET endpoint code** - SQL views become APIs automatically
- **Frontend independence** - Teams can shape data requests without backend changes
- **Performance transparency** - All optimization happens at the database level
- **Auto-generated OpenAPI schema** - Always up to date
- **Security via PostgreSQL** - Row-level security, JWT tokens
- **2000 req/sec** on low-end server (per PostgREST benchmarks)

## Migration Strategies

### Monolith
1. Route GET requests to PostgREST, backend updates API database on writes
2. Reuse existing DB with new schema containing public-facing views
3. Batch job syncs data (watch for staleness)
4. Foreign data wrappers for pull-based retrieval

### Microservices
1. Central API database - all services share one PostgreSQL with per-domain schemas
2. Per-domain databases - separate PostgREST instances with reverse proxy routing

## Schema Organization

```
_api_myviewtable     - Exposed via PostgREST
_internal_mytable    - Backend-only storage
```

Configure PostgreSQL users so each service writes only to its domain's tables.

## When to Use

- CQRS-style read/write separation
- Frontend-heavy apps needing flexible data queries
- Reducing backend maintenance for pure data retrieval
- Teams with strong PostgreSQL/SQL skills

## Caveats

- Data modifications still need traditional backends (SQL not ideal for step-by-step algorithms)
- Separate PostgREST instances can't join data cross-database
- Requires PostgreSQL (or compatible)

## Links

- PostgREST: https://postgrest.org/
- Source article: https://www.fabianzeindl.com/posts/the-api-database-architecture

---
*Source: Fabian Zeindl - "The API database architecture" (saved 2026-01)*
