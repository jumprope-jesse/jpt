# PGMQ - Postgres Message Queue

**Added:** 2026-01-18
**Source:** https://github.com/tembo-io/pgmq
**Docs:** https://tembo-io.github.io/pgmq/

## Overview

PGMQ is a lightweight message queue built as a Postgres extension. Like AWS SQS and RSMQ but self-hosted on Postgres. No external dependencies - just Postgres functions.

## Key Features

- **Exactly once delivery** within visibility timeout
- **API parity** with AWS SQS and RSMQ
- **Message archival** - messages can be archived instead of deleted for replay
- **Partitioned queues** - via pg_partman for high-volume scenarios
- Supports Postgres 12-16

## Quick Start

```bash
# Run with Docker
docker run -d --name postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 quay.io/tembo/pgmq-pg:latest
```

```sql
-- Enable extension
CREATE EXTENSION pgmq;

-- Create queue
SELECT pgmq.create('my_queue');

-- Send message (JSON payload)
SELECT pgmq.send('my_queue', '{"foo": "bar"}');

-- Read with 30s visibility timeout (2 messages max)
SELECT * FROM pgmq.read('my_queue', 30, 2);

-- Pop (read + delete atomically)
SELECT pgmq.pop('my_queue');

-- Archive (moves to a_my_queue table)
SELECT pgmq.archive('my_queue', 2);

-- Delete permanently
SELECT pgmq.delete('my_queue', 3);

-- Drop queue
SELECT pgmq.drop_queue('my_queue');
```

## Visibility Timeout

Messages become invisible after being read. If not deleted/archived within the timeout, they reappear for other consumers. Set timeout longer than expected processing time.

## Partitioned Queues

For high volume, use `pgmq.create_partitioned()` with pg_partman:
- Partition by time (`'daily'`) or message count (`'100'`)
- Automatic retention/cleanup of old partitions

Requires postgresql.conf:
```
shared_preload_libraries = 'pg_partman_bgw'
pg_partman_bgw.interval = 60
pg_partman_bgw.role = 'postgres'
pg_partman_bgw.dbname = 'postgres'
```

## Client Libraries

- **Official:** Rust, Python
- **Community:** Go, Elixir, Java (Spring Boot), Node.js, .NET

## When to Use

- Already using Postgres and want to avoid adding Redis/SQS
- Need message archival and replay capability
- Want transactional guarantees with your database
- Simpler ops than running separate message broker

## Comparison to SQS

| Feature | PGMQ | SQS |
|---------|------|-----|
| Hosting | Self-hosted Postgres | AWS managed |
| Exactly-once | Within visibility timeout | Within visibility timeout |
| Dead letter | Via archival | Built-in DLQ |
| Cost | Postgres hosting | Per-request pricing |
| Latency | Database latency | ~ms |
