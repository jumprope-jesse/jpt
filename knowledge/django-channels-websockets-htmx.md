# Django Channels + WebSockets + HTMX

Source: https://www.saaspegasus.com/guides/django-websockets-chatgpt-channels-htmx/

## Overview

Complete guide to building real-time streaming UIs (like ChatGPT) using Django Channels, WebSockets, and HTMX.

## WebSocket Basics

**HTTP vs WebSockets:**
- HTTP: Request/response like letter-writing - one message, one response, connection closes
- WebSockets: Like a phone call - open connection where both sides send messages anytime

**Channels Consumer Methods:**
```python
class WebsocketConsumer:
    def connect(self):       # New connection established
    def accept(self):        # Accept the connection
    def receive(self, text_data=None):  # Message received from client
    def send(self, text_data=None):     # Send message to client
    def close(self, code=None):         # Close from server side
    def disconnect(self, code):         # Connection closed
```

## Setup

### Routing (routing.py)
```python
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path(r"ws/chat/", consumers.ChatConsumer.as_asgi(), name="chat"),
]
```

### ASGI Configuration (asgi.py)
```python
from chat.routing import websocket_urlpatterns

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(websocket_urlpatterns)
        )
    ),
})
```

## HTMX WebSocket Integration

### Frontend Setup
```html
<head>
  <script src="https://unpkg.com/htmx.org@1.9.11"></script>
  <script src="https://unpkg.com/htmx.org/dist/ext/ws.js"></script>
</head>

<div hx-ext="ws" ws-connect="/ws/chat/">
  <div id="message-list">
    <!-- Messages appear here -->
  </div>
  <form ws-send>
    <input name="message" type="text">
    <button type="submit">Send</button>
  </form>
</div>
```

**Key attributes:**
- `hx-ext="ws"` - Enable websocket extension
- `ws-connect="/ws/chat/"` - Connect to websocket endpoint
- `ws-send` - Send form data over websocket (auto-serializes as JSON)

### Server-Side Swapping

Send HTML with out-of-band swaps to update specific elements:

```html
<div id="message-list" hx-swap-oob="beforeend">
  <div class="chat-message">{{ message_text }}</div>
</div>
```

- `hx-swap-oob="beforeend"` - Append to end of target element
- Target element matched by ID

## Consumer Implementation

### Basic Consumer
```python
import json
from channels.generic.websocket import WebsocketConsumer
from django.template.loader import render_to_string

class ChatConsumer(WebsocketConsumer):
    def receive(self, text_data):
        data = json.loads(text_data)
        message = data["message"]

        # Render and send response
        html = render_to_string("chat/message.html", {"message_text": message})
        self.send(text_data=html)
```

### Streaming Responses (ChatGPT-style)

1. Send empty placeholder with unique ID
2. Stream chunks into that placeholder

```python
import uuid
from openai import OpenAI

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.messages = []  # Chat history
        super().connect()

    def receive(self, text_data):
        data = json.loads(text_data)
        message_text = data["message"]

        # Add to history
        self.messages.append({"role": "user", "content": message_text})

        # Send empty placeholder
        message_id = uuid.uuid4().hex
        self.send(text_data=render_to_string("chat/message.html", {
            "message_text": "",
            "is_system": True,
            "message_id": message_id,
        }))

        # Stream response
        client = OpenAI()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.messages,
            stream=True,
        )

        chunks = []
        for chunk in response:
            content = chunk.choices[0].delta.content
            if content:
                # Swap into the placeholder
                self.send(text_data=f'<div id="{message_id}" hx-swap-oob="beforeend">{content}</div>')
                chunks.append(content)

        # Save to history
        self.messages.append({"role": "system", "content": "".join(chunks)})
```

### Async Version (Production)

```python
from channels.generic.websocket import AsyncWebsocketConsumer
from openai import AsyncOpenAI

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.messages = []
        await super().connect()

    async def receive(self, text_data):
        data = json.loads(text_data)
        message_text = data["message"]

        self.messages.append({"role": "user", "content": message_text})

        message_id = uuid.uuid4().hex
        await self.send(text_data=render_to_string("chat/message.html", {
            "message_text": "",
            "is_system": True,
            "message_id": message_id,
        }))

        client = AsyncOpenAI()
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.messages,
            stream=True,
        )

        chunks = []
        async for chunk in response:
            content = chunk.choices[0].delta.content
            if content:
                await self.send(text_data=f'<div id="{message_id}" hx-swap-oob="beforeend">{content}</div>')
                chunks.append(content)

        self.messages.append({"role": "system", "content": "".join(chunks)})
```

## Message Template

```html
<!-- chat/message.html -->
<div id="message-list" hx-swap-oob="beforeend">
  <div class="chat-message{% if is_system %} is-system{% endif %}"
       {% if message_id %}id="{{ message_id }}"{% endif %}>
    {{ message_text }}
  </div>
</div>
```

## Key Points

- Use `AsyncWebsocketConsumer` for production (non-blocking I/O)
- Store chat history on consumer instance (per-session)
- HTMX `hx-swap-oob` enables updating any element by ID
- Streaming: send placeholder first, then stream content into it
- Alternative to websockets: Server-Sent Events (SSE) - one-way only

## Related

- Django Channels tutorial: https://channels.readthedocs.io/en/latest/tutorial/
- HTMX websocket extension: https://htmx.org/extensions/websockets/
- SaaS Pegasus: Django boilerplate with this built-in
