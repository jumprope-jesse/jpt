# AWS Lambda Web Adapter

Run existing web applications on AWS Lambda without code changes. Same Docker image works on Lambda, EC2, Fargate, and locally.

**Repo**: https://github.com/awslabs/aws-lambda-web-adapter

## Why Use It

- Run Express.js, Next.js, Flask, Django, SpringBoot, ASP.NET, Laravel, etc. on Lambda
- No framework-specific serverless wrappers needed (no Zappa, Serverless Express, etc.)
- Same container runs anywhere - truly portable
- Works with API Gateway (REST/HTTP), Lambda Function URLs, and ALB

## How It Works

Lambda Web Adapter runs as a Lambda Extension. It:
1. Boots up alongside your web app
2. Performs readiness checks until your app responds
3. Forwards Lambda invocations as HTTP requests to your app
4. Returns HTTP responses back to Lambda

## Quick Start (Docker)

Add one line to your Dockerfile:

```dockerfile
FROM public.ecr.aws/docker/library/node:20-slim
COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.8.3 /lambda-adapter /opt/extensions/lambda-adapter
ENV PORT=8080
WORKDIR "/var/task"
COPY . .
RUN npm install --omit=dev
CMD ["node", "index.js"]
```

That's it. Your app listens on port 8080 (configurable), the adapter handles the rest.

## Zip Package (Managed Runtimes)

1. Attach the adapter as a Lambda Layer
2. Set `AWS_LAMBDA_EXEC_WRAPPER` to `/opt/bootstrap`
3. Configure your start command

## Key Environment Variables

| Variable | Purpose | Default |
|----------|---------|---------|
| `AWS_LWA_PORT` / `PORT` | Port your app listens on | 8080 |
| `AWS_LWA_READINESS_CHECK_PATH` | Health check endpoint | `/` |
| `AWS_LWA_ASYNC_INIT` | Enable async init for slow starts | `false` |
| `AWS_LWA_REMOVE_BASE_PATH` | Strip path prefix (e.g., `/orders`) | empty |
| `AWS_LWA_ENABLE_COMPRESSION` | Enable gzip response compression | `false` |
| `AWS_LWA_INVOKE_MODE` | `buffered` or `response_stream` | `buffered` |

## Port Restrictions

- Avoid ports < 1024 (Lambda runs as non-root)
- Avoid 9001 (Lambda Runtime API)
- Avoid 3000 (CloudWatch Lambda Insight)
- Avoid 8080 for local testing with SAM (RIE uses it)

## Async Init for Slow-Starting Apps

Lambda gives 10 seconds free init time. If your app needs more:

```
AWS_LWA_ASYNC_INIT=true
```

The adapter signals init complete at 9.8s, continues readiness check in handler. Avoids restart penalty.

## Response Streaming

For streaming responses (SSE, chunked):

```
AWS_LWA_INVOKE_MODE=response_stream
```

Must match Lambda Function URL invoke mode setting.

## Non-HTTP Triggers

Works with SQS, SNS, S3, DynamoDB, Kinesis, Kafka, EventBridge, Bedrock Agents:

- Events POST to `/events` (configurable via `AWS_LWA_PASS_THROUGH_PATH`)
- Your app processes the JSON body, returns JSON response

## Request Context

API Gateway metadata (requestId, identity, authorizer) passed via:
- Header: `x-amzn-request-context`

Lambda context (function name, memory, timeout) passed via:
- Header: `x-amzn-lambda-context`

## Graceful Shutdown

Lambda sends SIGTERM before shutdown. Adapter supports this - catch it in your app:

```javascript
process.on('SIGTERM', async () => {
  console.log('Shutting down...');
  await server.close();
  process.exit(0);
});
```

## Local Development

```bash
# Just run your app locally
node index.js

# Or use SAM for Lambda simulation
sam local start-api
```

## When to Use

**Good fit:**
- Migrating existing web apps to serverless
- Same container for Lambda + Fargate (traffic-based routing)
- Frameworks without good serverless wrappers
- Team unfamiliar with Lambda-specific patterns

**Consider alternatives:**
- Greenfield serverless → native Lambda handlers are simpler
- Very high throughput → Fargate/App Runner may be more cost-effective
- Sub-100ms cold starts critical → native handlers have less overhead

## Compared to Framework-Specific Solutions

| Approach | Pros | Cons |
|----------|------|------|
| Lambda Web Adapter | Framework agnostic, portable | Extra layer, slight overhead |
| Serverless Express | Native integration | Express-only, vendor lock-in |
| Zappa (Python) | Mature, Django support | Python-only, less maintained |
| Lamby (Rails) | Rails conventions | Rails-only |

## Supported Frameworks (Examples in Repo)

- Node.js: Express, Next.js
- Python: FastAPI, Flask, Django
- Java: SpringBoot
- .NET: ASP.NET MVC/Web API
- Go: Gin
- Rust: Actix, Axum
- PHP: Laravel
- Deno: Oak
