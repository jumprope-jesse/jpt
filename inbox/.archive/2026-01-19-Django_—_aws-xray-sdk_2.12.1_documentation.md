---
type: link
source: notion
url: https://docs.aws.amazon.com/xray-sdk-for-python/latest/reference/frameworks.html
notion_type: Software Repo
tags: ['Running']
created: 2024-02-07T05:34:00.000Z
---

# Django — aws-xray-sdk 2.12.1 documentation

## AI Summary (from Notion)
- Overview of AWS X-Ray SDK for Django: Documentation for integrating the AWS X-Ray SDK with Django applications for tracing and monitoring.

- Configuration:
- Middleware Setup: Must add XRayMiddleware in settings.py to automatically record incoming requests.
- Segment Management: Use xray_recorder.current_segment() to manage segments and add annotations.
- Recorder Configuration: Options available under XRAY_RECORDER for customizing behavior, such as AWS X-Ray daemon address and sampling rules.

- Local Development Challenges:
- Issues may arise if AUTO_INSTRUMENT is enabled and AWS_XRAY_CONTEXT_MISSING is set to RUNTIME_ERROR, particularly during local migrations.
- Recommended to adjust settings for smoother local development.

- Integration with Flask and Aiohttp:
- Similar middleware setup for Flask and Aiohttp, with specific configurations for asynchronous contexts.
- Example code provided for each framework to demonstrate how to implement the X-Ray SDK.

- Client Session Tracking: Aiohttp's new features allow tracking HTTP calls as subsegments, enabling better monitoring of requests made during client sessions.

- Important Notes:
- Environment variables take precedence over user settings for configuration.
- The document emphasizes the importance of understanding how to leverage the SDK effectively for production environments.

## Content (from Notion)

## Configure X-Ray Recorder

Make sure you add XRayMiddleWare as the first entry in your Django settings.py file, as shown in the following example:

```plain text
MIDDLEWARE = [
    'aws_xray_sdk.ext.django.middleware.XRayMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

```

The incoming requests to the Django app are then automatically recorded as a segment.

To get the current segment and add annotations or metadata as needed, use the following statement in your application code when processing request:

```plain text
segment = xray_recorder.current_segment()

```

For more configurations in your Django settings.py file, add the following line:

```plain text
INSTALLED_APPS = [
    'django.contrib.admin',
    ...
    'django.contrib.sessions',
    'aws_xray_sdk.ext.django',
]

```

You can configure the X-Ray recorder in a Django app under the ‘XRAY_RECORDER’ namespace. The default values are as follows:

```plain text
XRAY_RECORDER = {
    'AWS_XRAY_DAEMON_ADDRESS': '127.0.0.1:2000',
    'AUTO_INSTRUMENT': True,  # If turned on built-in database queries and template rendering will be recorded as subsegments
    'AWS_XRAY_CONTEXT_MISSING': 'LOG_ERROR',
    'PLUGINS': (),
    'SAMPLING': True,
    'SAMPLING_RULES': None,
    'AWS_XRAY_TRACING_NAME': None, # the segment name for segments generated from incoming requests
    'DYNAMIC_NAMING': None, # defines a pattern that host names should match
    'STREAMING_THRESHOLD': None, # defines when a segment starts to stream out its children subsegments
}

```

Environment variables have higher precedence over user settings. If neither is set, the defaults values shown previously are used. ‘AWS_XRAY_TRACING_NAME’ is required unless specified as an environment variable. All other keys are optional. For further information on individual settings, see the Configure Global Recorder section.

## Local Development

When doing Django app local development, if you configured Django built-in database with AUTO_INSTRUMENT turned-on, the command manage.py runserver may fail if AWS_XRAY_CONTEXT_MISSING is set to RUNTIME_ERROR. This is because the command runserver performs migrations check which will generate a subsegment, the xray_recorder will raise an error since there is no active segment.

One solution is to set AWS_XRAY_CONTEXT_MISSING to LOG_ERROR so it only emits a error message on server startup. Alternatively if you have defined your own ready() function for code execution at startup you can manually create a segment as a placeholder.

By Django official guide it’s recommanded to deploy Django to other servers in production so this particular issue normally doesn’t exist in production.

To generate segment based on incoming requests, you need to instantiate the X-Ray middleware for flask:

```plain text
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

app = Flask(__name__)

xray_recorder.configure(service='my_app_name')
XRayMiddleware(app, xray_recorder)

```

Flask built-in template rendering will be wrapped into subsegments. You can configure the recorder, see Configure Global Recorder for more details.

## Server

For X-Ray to create a segment based on an incoming request, you need register some middleware with aiohttp. As aiohttp is an asyncronous framework, X-Ray will also need to be configured with an AsyncContext compared to the default threaded version.:

```plain text
import asyncio

from aiohttp import web

from aws_xray_sdk.ext.aiohttp.middleware import middleware
from aws_xray_sdk.core.async_context import AsyncContext
from aws_xray_sdk.core import xray_recorder
# Configure X-Ray to use AsyncContext
xray_recorder.configure(service='service_name', context=AsyncContext())


async def handler(request):
    return web.Response(body='Hello World')

loop = asyncio.get_event_loop()
# Use X-Ray SDK middleware, its crucial the X-Ray middleware comes first
app = web.Application(middlewares=[middleware])
app.router.add_get("/", handler)

web.run_app(app)

```

There are two things to note from the example above. Firstly a middleware corountine from aws-xray-sdk is provided during the creation of an aiohttp server app. Lastly the xray_recorder has also been configured with a name and an AsyncContext. See Configure Global Recorder for more information about configuring the xray_recorder.

## Client

Since 3.0.0 Aiohttp provides a generic object that allows third packages to gather the different events ocurred during an HTTP call, X-Ray can be configured to track these requests as subsegments using the aws_xray_trace_config function. This will return a valid TraceConfig ready to be installed in any aiohttp.ClientSession. The following example shows how it can be used.:

```plain text
from aws_xray_sdk.ext.aiohttp.client import aws_xray_trace_config

trace_config = aws_xray_trace_config()
async with ClientSession(loop=loop, trace_configs=[trace_config]) as session:
    async with session.get(url) as resp
        await resp.read()

```

### Navigation


