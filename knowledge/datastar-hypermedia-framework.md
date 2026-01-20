# Datastar Hypermedia Framework

Datastar is a server-side-driven library for building high-performance, web-native, live-updating web applications. It's an alternative to HTMX with a different philosophy and capabilities.

## Key Differences from HTMX

| Aspect | HTMX | Datastar |
|--------|------|----------|
| Philosophy | Advances HTML specification | Leverages web-native features (SSE, CSS transitions, web components) |
| Logic location | Scattered across HTML attributes | Centralized on server side |
| Download size | ~14 KB | ~11 KB |
| Real-time updates | Polling or custom WebSockets | Server-Sent Events (SSE) built-in |

## Simpler API

HTMX requires multiple attributes:
```html
<span hx-target="#status-button"
      hx-select="#status-button"
      hx-swap="outerHTML"
      hx-trigger="click"
      hx-get="/status-button"></span>
```

Datastar achieves the same with one attribute:
```html
<span data-on-click="@get('/status-button')"></span>
```

## Server-Driven Updates

Datastar expects the server to define what changes. The server returns HTML with IDs matching elements to update:

```html
<!-- Server response updates multiple elements -->
<p id="info-details">Details content...</p>
<div id="alert">Alert message</div>
```

## Multiple Component Updates

Update multiple components in a single request (Django example):
```python
from datastar_py.django import DatastarResponse, ServerSentEventGenerator as SSE

def add_item(request):
    return DatastarResponse([
        SSE.patch_elements(render_to_string('purchase-item.html', context=...)),
        SSE.patch_elements(render_to_string('cart-count.html', context=...)),
    ])
```

## Server-Sent Events (SSE)

- Push-based updates without custom WebSocket code
- Automatic reconnection on connection loss
- Can notify server of last received event
- Enables real-time dashboards, admin panels, collaborative tools

## Component-Based Thinking

Datastar encourages thinking in component states:
- Placeholder state (before interaction)
- Active/loaded state (after interaction)
- Prevents invalid states and simplifies state tracking

## Web Components Integration

Datastar promotes using native web components for complex client-side logic:
- High locality of behavior
- Reusable across the app
- Encapsulated logic with attribute-driven state

## Performance Examples

- Database monitoring demo with significant speed/memory improvements
- One billion checkboxes on inexpensive server
- 800,000+ radar points updating per second with 100ms latency

## Best Practices from Community

1. Don't fear re-rendering whole components - HTML parsing is fast, compression ratios are good
2. Server is source of truth - minimize client-side reactive signals
3. Web components for encapsulating complex local behavior
4. Think in component states rather than scattered updates

## Resources

- [Datastar website](https://data-star.dev/)
- [Datastar Discord](https://discord.gg/datastar) - active community
- Python SDK: `datastar_py`

## Source

[Why I switched from HTMX to Datastar](https://everydaysuperpowers.dev/articles/why-i-switched-from-htmx-to-datastar/) - October 2025
