# Modal's Serverless HTTP Infrastructure

Source: https://modal.com/blog/serverless-http
Type: Tech Deep Dive
Added: 2026-01-19

## Overview

Modal built HTTP and WebSocket support for serverless functions with **no traditional serverless limits**. Unlike AWS Lambda (6 MB request/response), Modal supports:
- Request bodies up to **4 GiB** (682x larger than Lambda)
- Unlimited streaming response bodies
- Full WebSocket support with GPUs
- Up to 64 CPUs, 336 GB memory, 8x H100 GPUs per container
- 30-minute+ execution times (vs Lambda's 15 min)

**Philosophy:** Serverless functions should be **ordinary functions you can call**, not just HTTP endpoints you wrap in REST APIs.

## Architecture: HTTP → Function Calls

### The Translation Layer

Modal translates HTTP requests into function calls rather than proxying HTTP directly:

```
Web Request → modal-http (Rust) → ASGI events → Function Call → Response
```

**Why not reverse proxy?**
- Enables optimized paths for function-to-function calls (cache-aware, location-aware)
- Supports both real-time streaming AND traditional RPC
- Shares infrastructure with core serverless runtime

### ASGI Protocol

Uses **ASGI** (Asynchronous Server Gateway Interface) as internal protocol:
- Originally designed for Python web frameworks (Flask, Django, FastAPI)
- Represents HTTP as stream of events
- Serialized as Protocol Buffers for distributed runtime

**ASGI Event Flow:**

```
Client → Server:
1. http.request scope (headers) → triggers function call
2. http.request events (body chunks, up to 1 MiB, 2ms intervals)
3. http.disconnect (if client cancels)

Server → Client:
1. Response headers + status
2. Response body chunks
3. Optional HTTP trailers
```

### Batching & Backpressure

Request body streaming:
- Buffers up to 1 MiB OR 2ms of data
- TCP/HTTP/2 flow control propagates backpressure to client
- Up to 16 chunks in flight

This allows smooth handling of large uploads (e.g., gigabyte videos) without overwhelming the function.

## Implementation: Rust + Tokio + Hyper

**Why Rust:**
- Speed for high-performance networking
- Type safety to handle HTTP edge cases correctly
- Pattern matching for error handling

**Stack:**
- `hyper` - HTTP server library
- `tokio` - async runtime
- `tokio-tungstenite` - WebSocket after handshake

**Error Reduction:** Moving from Python ingress to Rust decreased 502 Bad Gateway errors by **99.7%**.

## Handling Edge Cases

### 1. Client Disconnects

If client exits mid-request:
- Send `http.disconnect` event to function
- Allows graceful shutdown (don't waste compute)

### 2. Server Failures

Function can:
- Throw exception
- Crash (OOM)
- Hit user timeout
- Get preempted (spot instance)
- Send malformed response events

**Solution:** Track all violations, show error to user. Rust's ownership + pattern matching helps manage cases.

### 3. Long-Running Requests (Idle Timeout Hack)

**Problem:** Browsers timeout after 300s of no response (Chrome is non-configurable).

**Solution:** After 150s, send **303 See Other** redirect with request ID:
- Browser follows redirect (new connection)
- Can chain up to 20 redirects = **50 minute idle timeout**
- If function responds in <2.5 min, user never notices

## WebSocket Support

**Handshake:**

```
GET /ws HTTP/1.1
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==

→

HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=
```

After handshake, uses same data channel infrastructure as HTTP.

ASGI events: `websocket.connect`, `websocket.accept`, then messages.

## Deployment Stack

```
Internet
  ↓
DNS (*.modal.run, custom domains via CNAME)
  ↓
TCP Network Load Balancer
  ↓
Kubernetes Cluster
  ├─ Caddy (TLS termination, certificate allocation)
  └─ modal-http (Rust service, multiple replicas)
       ↓
  Serverless Runtime (custom, not k8s)
    └─ gVisor containers
```

**Why Kubernetes for ingress?**
- Reliable for traditional infrastructure
- Handles rolling deployments, replication, fault tolerance
- Actual serverless functions run on **custom runtime** (gVisor, custom file system, job scheduler)

## Limitations & Future

**Current:** All modal-http servers in Ashburn, Virginia
- Tradeoff: Flexibility vs latency
- Serverless functions already multi-region (GPUs are scarce)

**Future:** Deploy modal-http to edge regions for <100ms latency workloads

## Key Comparisons

| Feature | AWS Lambda | Google Cloud Run | Modal |
|---------|------------|------------------|-------|
| Max execution | 15 min | 60 min | 30+ min |
| Max CPUs | 3 (6 threads) | 4 | 64 |
| Max memory | 10 GB | 32 GB | 336 GB |
| Request body | 6 MB | 32 MB | 4 GiB |
| Response | 6 MB | 32 MB | Unlimited (streaming) |
| GPUs | No | No | 8x H100 |
| WebSockets | No | Limited | Full support |

## Code Examples

### Simple Web Endpoint

```python
from modal import Stub, web_endpoint

stub = Stub(name="small-app")

@stub.function()
@web_endpoint(method="GET")
def my_handler():
    return {"status": "success", "data": "Hello, world!"}
```

Deploys in **0.747 seconds**.

### Heavy Compute Endpoint

```python
from modal import Stub, web_endpoint

stub = Stub(name="big-app")

@stub.function(timeout=1800, cpu=8, memory=32 * 1024)
@web_endpoint(method="POST")
def video_processor(video_data):
    edited = do_expensive_processing(video_data)
    return edited
```

30 minutes, 8 CPUs, 32 GB memory for video processing.

## Technical Insights

**Request Body Buffering (Rust snippet):**

```rust
async fn stream_http_request_body(...) {
    let body_buffer_time = Duration::from_millis(2);
    let body_buffer_size = 1 << 20; // 1 MiB

    // Buffer chunks up to 1 MiB or 2ms
    while let Some(buf) = body.next().await {
        current_size += buf.len();
        current_segments.push(buf);

        if current_size > body_buffer_size
           || last_put.elapsed() > body_buffer_time {
            send_to_function(current_segments);
            current_segments.clear();
        }
    }
}
```

**Load Balancing Strategy:**

Modal uses **distributed job scheduler** (not nginx/HAProxy):
- Tracks container availability and locality
- Routes based on data cache proximity
- Optimizes for function-to-function calls

## Why This Matters

**Removes artificial limits** that force you to work around serverless constraints:
- Don't split up large files
- Don't reduce video quality
- Don't add complexity for chunk uploading

**Enables new use cases:**
- Real-time ML inference with streaming
- Data pipelines with large inputs/outputs
- WebSocket apps with GPU backing
- Long-running simulations ("simulate your whole bakery")

## Related Concepts

- ASGI (async web framework protocol)
- gRPC (needs HTTP/2 stream IDs, not fully supported in ASGI)
- Rust ownership for distributed systems
- Serverless constructs (see `serverless-evolution-constructs.md`)

## Quote

> "Lambda on hard mode" — Modal doesn't compromise on speed or compute capacity, making HTTP serving proportionally harder when resource limits are removed.
