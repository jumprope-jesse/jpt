# DuckDB as a Command-Line Data Query Tool

DuckDB can replace jq for querying JSON files using familiar SQL syntax instead of jq's complex query language.

*Source: https://www.pgrs.net/2024/03/21/duckdb-as-the-new-jq/ - Added: 2026-01-19*

## Why Use DuckDB Instead of jq

- SQL syntax is familiar to most developers
- No need to learn jq's specialized query language
- Works with many formats: JSON, CSV, Parquet, Excel
- No schema definition or data persistence needed
- Can output JSON for piping to other tools

## Basic Usage

DuckDB reads JSON files directly as tables without configuration:

```bash
# Query JSON file with SQL
duckdb -c "select * from 'data.json' limit 10"

# Output as JSON
duckdb -json -c "select * from 'data.json'"

# Pipe to jq for pretty printing
duckdb -json -c "select * from 'data.json'" | jq
```

## Querying Nested JSON

Use PostgreSQL-style JSON operators:

```bash
# Access nested fields with ->> operator
duckdb -c "select license->>'key' as license, count(*) as count \
  from 'repos.json' \
  group by 1 \
  order by count desc"
```

## Example: jq vs DuckDB

**Task:** Count open source license types from GitHub API response

**jq approach:**
```bash
cat repos.json | jq \
  'group_by(.license.key)
  | map({license: .[0].license.key, count: length})
  | sort_by(.count)
  | reverse'
```

**DuckDB approach:**
```bash
duckdb -c \
  "select license->>'key' as license, count(*) as count \
  from 'repos.json' \
  group by 1 \
  order by count desc"
```

The SQL version requires no documentation lookup for anyone familiar with SQL and PostgreSQL JSON functions.

## Supported Formats

- JSON (including nested structures)
- CSV
- Parquet
- Excel files
- Many others via extensions

## When to Still Use jq

- Simple field extraction: `jq '.field'`
- Streaming large files
- Environments where DuckDB isn't installed
- Complex JSON transformations that map well to jq's paradigm

## Installation

```bash
# macOS
brew install duckdb

# Or download from https://duckdb.org/
```

## Further Reading

- [DuckDB JSON documentation](https://duckdb.org/docs/extensions/json.html)
- [Shredding Deeply Nested JSON, One Vector at a Time](https://duckdb.org/2023/03/03/json.html)
