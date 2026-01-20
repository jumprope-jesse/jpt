# PowerSync - Offline-First Sync Layer

Drop-in sync layer for building offline-first applications with bidirectional sync.

## Overview

PowerSync provides a turnkey solution for making apps work offline with automatic sync when connectivity is restored. It's designed as a sync layer that sits between your backend database and client-side storage.

## Key Features

- **Offline-First**: Apps continue working without connectivity
- **Bidirectional Sync**: Local changes sync back to server when online
- **Drop-In Integration**: Minimal changes to existing architecture
- **Real-Time**: Live updates when online
- **Conflict Resolution**: Handles concurrent edits intelligently

## Use Cases

- Mobile apps in low-connectivity environments
- Field service applications
- Collaborative tools that need offline capability
- Consumer apps requiring seamless offline/online transitions

## Architecture

PowerSync acts as middleware:
1. **Backend**: Connects to Postgres, MongoDB, MySQL, or Supabase
2. **Sync Layer**: PowerSync service handles replication and conflict resolution
3. **Client**: Local SQLite database with PowerSync SDK

## Related Tools

- **PGlite**: Embeddable Postgres for local-first apps (see `pglite-embeddable-postgres.md`)
- **ElectricSQL**: Alternative sync solution for Postgres
- **Supabase**: Backend platform with real-time features

## Links

- Website: https://www.powersync.com/
- GitHub: https://github.com/powersync-ja
- Docs: https://docs.powersync.com/

## Added

2026-01-19 - From Notion inbox item
