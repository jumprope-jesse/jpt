# InstantDB - Realtime Client-Side Database

A client-side database for building real-time and collaborative apps (like Notion or Figma).

## Key Features

- **Relational queries** - Write queries in the shape of data you want (InstaQL, similar to GraphQL)
- **Automatic data fetching** - No stores, selectors, or endpoints needed
- **Permission checking** - Built-in, powered by Google's CEL library
- **Offline caching** - IndexedDB on web, AsyncStorage in React Native
- **Optimistic updates** - Automatic with rollback handling
- **Multiplayer by default** - Every query is realtime
- **Ephemeral updates** - Support for cursors, presence indicators

## SDKs

- JavaScript
- React
- React Native

## Example Usage

```jsx
function Chat() {
  // Read with relational query
  const { isLoading, error, data } = useQuery({
    messages: {},
  });

  // Write with transactions
  const addMessage = (message) => {
    transact(tx.messages[id()].update(message));
  }

  return <UI data={data} onAdd={addMessage} />
}
```

## Architecture

- User data stored as **triples in Postgres** (multi-tenant)
- Sync server in **Clojure** talks to Postgres
- **WAL tailing** for change detection and query invalidation (inspired by Asana's WorldStore, Figma's LiveGraph)
- Client-side triple store with IndexedDB/AsyncStorage persistence

## Links

- Website: https://instantdb.com
- GitHub: https://github.com/instantdb/instant
- Discord: Available for community support

## When to Use

Good for apps that need:
- Real-time collaboration
- Offline support
- Quick prototyping without backend boilerplate
- Multiplayer features out of the box
