# Lightdash - Open-Source BI Platform

Open-source business intelligence platform that transforms dbt models into interactive dashboards. Self-hostable alternative to Looker/Mode.

GitHub: https://github.com/lightdash/lightdash
Docs: https://docs.lightdash.com/

## Overview

Lightdash connects directly to your dbt project and data warehouse, automatically generating a BI layer from your dbt semantic layer. If you're already using dbt for data transformation, Lightdash leverages that work for analytics.

**Core Philosophy**: Reuse dbt's semantic layer (metrics, dimensions, relationships) rather than rebuilding it in a separate BI tool.

## Key Features

- **dbt-native**: Reads metrics and dimensions directly from dbt YML files
- **Data warehouse integration**: Connects to BigQuery, Snowflake, Redshift, Postgres, Databricks
- **Self-hostable**: Docker Compose for local/proof-of-concept, Kubernetes for production
- **Version control**: Changes to metrics/dashboards can be tracked alongside dbt code
- **Semantic layer**: Leverages dbt's modeling work; no duplicate metric definitions

## Self-Hosting with Docker Compose

Minimal setup for local development or proof-of-concept (not internet-accessible):

### Prerequisites
- Docker
- Docker Compose

### Quick Start

```bash
# 1. Clone repository
git clone https://github.com/lightdash/lightdash
cd lightdash

# 2. Configure environment
# Edit .env file with your setup:
PGHOST=db
PGPORT=5432
PGUSER=pg_user
PGPASSWORD=pg_password
PGDATABASE=postgres
DBT_DEMO_DIR=/path/to/lightdash/project/examples/full-jaffle-shop-demo
LIGHTDASH_CONFIG_FILE=/path/to/lightdash/lightdash.yml

# 3. Set secrets and start containers
export LIGHTDASH_SECRET="not very secret"  # Used to encrypt data at rest
export PGPASSWORD="password"               # Postgres password
docker-compose -f docker-compose.yml --env-file .env up --detach --remove-orphans
```

**Windows Note**: If you get `Error response from daemon: i/o timeout`, enable "Expose daemon on tcp://localhost:2375 without TLS" in Docker > Settings > General.

### Important Environment Variables

- `LIGHTDASH_SECRET`: Encrypts data at rest in database. **Don't lose this** or you lose access to your data.
- `PGPASSWORD`: Internal Postgres database password
- `DBT_DEMO_DIR`: Path to your dbt project (or use included example)

## Use Cases

- **dbt users wanting BI**: If you already model data in dbt, Lightdash is lowest-friction BI tool
- **Self-hosted analytics**: Alternative to cloud BI tools when data can't leave your infrastructure
- **Version-controlled metrics**: Metrics defined in code, reviewed via PR, deployed with CI/CD
- **Proof-of-concept BI**: Docker Compose setup is quick for testing before committing to full BI platform

## Comparison to Alternatives

- **vs Looker**: Open-source, self-hostable; dbt as semantic layer vs LookML
- **vs Metabase/Redash**: Built specifically for dbt users; leverages existing semantic modeling
- **vs Observable Framework**: Lightdash is GUI-based BI tool; Observable is code-first dashboards
- **vs Django SQL Explorer**: Lightdash is full BI platform; SQL Explorer is lightweight query tool

## Architecture

```
dbt Project (YML) → Lightdash → Data Warehouse
      ↓                           ↑
   Metrics/Dimensions     Direct queries
   (semantic layer)
```

Lightdash reads your dbt semantic layer and generates SQL queries against your warehouse based on user selections in dashboards.

## Deployment Options

1. **Docker Compose** (local/proof-of-concept)
2. **Kubernetes** (production)
3. **Lightdash Cloud** (managed SaaS option)

## Links

- GitHub: https://github.com/lightdash/lightdash
- Documentation: https://docs.lightdash.com/
- Self-hosting guide: https://docs.lightdash.com/self-host/self-host-lightdash-docker-compose
- Community: https://join.slack.com/t/lightdash-community/

## Related Tools

- dbt (data transformation layer)
- Looker (commercial BI with LookML)
- Metabase (open-source BI, more general-purpose)
- Redash (SQL-focused open-source BI)
- Observable Framework (code-first dashboards)
- Django SQL Explorer (lightweight Django query tool)

## Tags
Created: 2026-01-19 (from Notion inbox)
Tags: Business Intelligence, Open Source, dbt, Analytics, Self-Hosting, Docker
