# AWS X-Ray SDK for Python - Django, Flask, Aiohttp

*Source: https://docs.aws.amazon.com/xray-sdk-for-python/latest/reference/frameworks.html - Added: 2026-01-19*

AWS X-Ray SDK integration patterns for Python web frameworks.

## Django Integration

### Basic Setup

Add middleware as **first entry** in `settings.py`:

```python
MIDDLEWARE = [
    'aws_xray_sdk.ext.django.middleware.XRayMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # ... other middleware
]

INSTALLED_APPS = [
    # ... other apps
    'aws_xray_sdk.ext.django',
]
```

### Configuration

Configure under `XRAY_RECORDER` namespace:

```python
XRAY_RECORDER = {
    'AWS_XRAY_DAEMON_ADDRESS': '127.0.0.1:2000',
    'AUTO_INSTRUMENT': True,  # Records DB queries & template rendering as subsegments
    'AWS_XRAY_CONTEXT_MISSING': 'LOG_ERROR',
    'PLUGINS': (),
    'SAMPLING': True,
    'SAMPLING_RULES': None,
    'AWS_XRAY_TRACING_NAME': None,  # Required: segment name for incoming requests
    'DYNAMIC_NAMING': None,  # Pattern for host name matching
    'STREAMING_THRESHOLD': None,  # When to start streaming subsegments
}
```

**Precedence**: Environment variables > user settings > defaults

### Accessing Current Segment

```python
from aws_xray_sdk.core import xray_recorder

segment = xray_recorder.current_segment()
# Add annotations/metadata as needed
```

### Local Development Gotcha

`manage.py runserver` may fail with `AUTO_INSTRUMENT=True` and `AWS_XRAY_CONTEXT_MISSING=RUNTIME_ERROR` because migrations check generates subsegments without an active segment.

**Solutions**:
1. Set `AWS_XRAY_CONTEXT_MISSING='LOG_ERROR'` for local dev
2. Manually create placeholder segment in `ready()` function

**Note**: Django docs recommend deploying to production servers anyway, so this is mainly a dev issue.

## Flask Integration

```python
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

app = Flask(__name__)

xray_recorder.configure(service='my_app_name')
XRayMiddleware(app, xray_recorder)
```

Built-in template rendering automatically wrapped into subsegments.

## Aiohttp Integration

Aiohttp requires **AsyncContext** instead of default threaded context.

### Server

```python
import asyncio
from aiohttp import web
from aws_xray_sdk.ext.aiohttp.middleware import middleware
from aws_xray_sdk.core.async_context import AsyncContext
from aws_xray_sdk.core import xray_recorder

# Configure X-Ray for async
xray_recorder.configure(service='service_name', context=AsyncContext())

async def handler(request):
    return web.Response(body='Hello World')

loop = asyncio.get_event_loop()
# X-Ray middleware MUST come first
app = web.Application(middlewares=[middleware])
app.router.add_get("/", handler)

web.run_app(app)
```

### Client (Subsegment Tracking)

Since aiohttp 3.0.0, use `aws_xray_trace_config()` to track HTTP calls as subsegments:

```python
from aws_xray_sdk.ext.aiohttp.client import aws_xray_trace_config

trace_config = aws_xray_trace_config()
async with ClientSession(loop=loop, trace_configs=[trace_config]) as session:
    async with session.get(url) as resp:
        await resp.read()
```

## Key Takeaways

- **Middleware order matters**: X-Ray middleware must be first
- **Async frameworks need AsyncContext**: Default threaded context won't work
- **Auto-instrumentation**: DB queries and templates tracked automatically with `AUTO_INSTRUMENT=True`
- **Environment > config**: Env vars take precedence over code configuration
- **Local dev friction**: Be aware of context-missing errors during migrations

## Related

- `aws-xray-adaptive-sampling.md` - Sampling strategies and cost optimization
- `wide-events-observability.md` - Tail sampling patterns in application code
