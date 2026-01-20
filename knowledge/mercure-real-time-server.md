# Mercure - Real-time Communications Server

Open-source real-time communications solution built on HTTP and Server-Sent Events (SSE). Modern replacement for WebSockets that works natively in browsers without client libraries.

## Key Features

- **Pure HTTP/SSE**: No WebSocket complexity, leverages HTTP/2+
- **Simple pub/sub**: Publish with POST request, subscribe with EventSource
- **Auto-reconnection**: Handles disconnects, refetches missed messages
- **Private updates**: JWT-based authorization for secure channels
- **Event store**: Replay missed events on reconnect
- **Presence API**: Track connected subscribers
- **E2E encryption**: Optional end-to-end encryption support
- **Serverless-friendly**: Works with PHP, serverless functions, etc.

## Quick Start

```bash
# Docker
docker run -e MERCURE_PUBLISHER_JWT_KEY='!ChangeThisMercureHubJWTSecretKey!' \
           -e MERCURE_SUBSCRIBER_JWT_KEY='!ChangeThisMercureHubJWTSecretKey!' \
           -p 80:80 dunglas/mercure

# Or via Homebrew
brew install mercure
```

## Usage Pattern

### Publish (Server-side)
```bash
curl -d 'topic=https://example.com/books/1' \
     -d 'data={"status": "updated"}' \
     -H "Authorization: Bearer <jwt>" \
     http://localhost/.well-known/mercure
```

### Subscribe (Client-side)
```javascript
const es = new EventSource('http://localhost/.well-known/mercure?topic=https://example.com/books/1');
es.onmessage = (e) => console.log(e.data);
```

## When to Use

- Adding real-time features to REST/GraphQL APIs
- Live notifications, chat, collaborative editing
- IoT device updates
- Cases where WebSocket complexity is overkill
- Mobile apps (battery-efficient SSE vs WebSocket)

## Comparison to WebSockets

| Aspect | Mercure (SSE) | WebSocket |
|--------|---------------|-----------|
| Protocol | HTTP | Custom |
| Direction | Server→Client (+ POST for client→server) | Full duplex |
| Browser support | Native EventSource | Native but needs upgrade |
| Reconnection | Built-in | Manual |
| Proxy/firewall | Easier (standard HTTP) | Can have issues |
| Complexity | Lower | Higher |

## Links

- Website: https://mercure.rocks/
- GitHub: https://github.com/dunglas/mercure
- Created by Kévin Dunglas (Symfony/API Platform maintainer)

---
*Source: mercure.rocks (saved 2026-01)*
