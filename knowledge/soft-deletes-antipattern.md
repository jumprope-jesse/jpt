# Soft Deletes: An Antipattern

Source: https://blog.bemi.io/soft-deleting-chaos/

## What Are Soft Deletes?

Setting a `deleted_at` flag instead of performing a DELETE operation. Seems simple - add a column, update on delete, filter in queries.

## Why They're Dangerous

### The Incident
A developer removed a library (`acts_as_paranoid`) that auto-filtered soft-deleted records. Without the automatic exclusion, a background worker processed "deleted" claims, releasing successfully-purchased concert seats for resale. Same seats sold multiple times across multiple events globally.

### Complexity Creep
- Infects every query - must remember to filter deleted records
- ORMs hide the complexity but manual SQL can expose deleted data
- Indexes, unique constraints, and foreign keys all need to account for deleted state
- Table bloat from keeping deleted records affects performance

### Data Integrity Loss
- Lose database-level referential integrity enforcement
- Handling deletion in app layer is error-prone
- Significant maintenance overhead

## Better Alternatives

### History/Audit Tables
Archive deleted data to separate tables before deleting:

```sql
BEGIN;
INSERT INTO deleted_seat_claims SELECT * FROM seat_claims WHERE id = ?;
DELETE FROM seat_claims WHERE id = ?;
COMMIT;
```

### Database-Level Audit Trail
- PostgreSQL: triggers, logical replication, or change data capture
- Services like Bemi.io for automatic immutable change records

## Key Takeaway

Soft deletes trade short-term convenience for long-term liability. The "safety net" of recoverable data creates a minefield of query complexity and data integrity risks. Archive to history tables instead.
