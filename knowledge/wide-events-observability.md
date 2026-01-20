# Wide Events & Observability

Reference material for implementing effective logging and observability in distributed systems.

## Wide Events / Canonical Log Lines

*Source: https://loggingsucks.com/ - Added: 2026-01-18*

### The Problem with Traditional Logging

Traditional logging is broken for modern distributed systems:
- Logs designed for monoliths, single servers, and locally reproducible problems
- A single user request might touch 15 services, 3 databases, 2 caches, and a message queue
- String search treats logs as bags of characters with no understanding of structure
- No way to correlate events across services
- Logs optimized for writing, not reading/debugging

### Key Definitions

**Structured Logging**: Logs emitted as key-value pairs (usually JSON) instead of plain strings. Necessary but not sufficient.

**Cardinality**: Number of unique values a field can have. High cardinality fields (user_id, request_id) are what make logs useful for debugging.

**Dimensionality**: Number of fields in your log event. More dimensions = more questions you can answer.

**Wide Event**: A single, context-rich log event emitted per request per service. Instead of 13 log lines for one request, you emit 1 line with 50+ fields.

**Canonical Log Line**: Another term for wide event, popularized by Stripe.

### The Mental Model Shift

> Instead of logging what happened, log everything you might need to debug what happened.

Stop thinking about logs as a debugging diary. Start thinking about them as a structured record of business events.

### What a Wide Event Looks Like

```json
{
  "timestamp": "2025-01-15T10:23:45.612Z",
  "request_id": "req_8bf7ec2d",
  "trace_id": "abc123",

  "service": "checkout-service",
  "version": "2.4.1",
  "deployment_id": "deploy_789",
  "region": "us-east-1",

  "method": "POST",
  "path": "/api/checkout",
  "status_code": 500,
  "duration_ms": 1247,

  "user": {
    "id": "user_456",
    "subscription": "premium",
    "account_age_days": 847,
    "lifetime_value_cents": 284700
  },

  "cart": {
    "id": "cart_xyz",
    "item_count": 3,
    "total_cents": 15999,
    "coupon_applied": "SAVE20"
  },

  "payment": {
    "method": "card",
    "provider": "stripe",
    "latency_ms": 1089,
    "attempt": 3
  },

  "error": {
    "type": "PaymentError",
    "code": "card_declined",
    "message": "Card declined by issuer",
    "retriable": false,
    "stripe_decline_code": "insufficient_funds"
  },

  "feature_flags": {
    "new_checkout_flow": true,
    "express_payment": false
  }
}
```

From one query you can see:
- Premium customer (high priority)
- Account age > 2 years (very high priority)
- Payment failed on 3rd attempt
- Actual reason: insufficient funds
- Using new checkout flow (potential correlation?)

### OpenTelemetry Won't Save You

OpenTelemetry is a protocol and set of SDKs. It standardizes how telemetry data is collected and exported. It does NOT:
1. Decide what to log
2. Add business context
3. Fix your mental model

If you're still thinking in terms of "log statements," you'll just emit bad telemetry in a standardized format.

### Implementation Pattern

Build the event throughout the request lifecycle, emit once at the end:

```typescript
// middleware/wideEvent.ts
export function wideEventMiddleware() {
  return async (ctx, next) => {
    const startTime = Date.now();

    const event: Record<string, unknown> = {
      request_id: ctx.get('requestId'),
      timestamp: new Date().toISOString(),
      method: ctx.req.method,
      path: ctx.req.path,
      service: process.env.SERVICE_NAME,
      version: process.env.SERVICE_VERSION,
    };

    ctx.set('wideEvent', event);

    try {
      await next();
      event.status_code = ctx.res.status;
      event.outcome = 'success';
    } catch (error) {
      event.status_code = 500;
      event.outcome = 'error';
      event.error = {
        type: error.name,
        message: error.message,
        code: error.code,
        retriable: error.retriable ?? false,
      };
      throw error;
    } finally {
      event.duration_ms = Date.now() - startTime;
      logger.info(event);
    }
  };
}
```

Enrich with business context in handlers:

```typescript
app.post('/checkout', async (ctx) => {
  const event = ctx.get('wideEvent');
  const user = ctx.get('user');

  event.user = {
    id: user.id,
    subscription: user.subscription,
    account_age_days: daysSince(user.createdAt),
    lifetime_value_cents: user.ltv,
  };

  const cart = await getCart(user.id);
  event.cart = {
    id: cart.id,
    item_count: cart.items.length,
    total_cents: cart.total,
    coupon_applied: cart.coupon?.code,
  };

  // ... rest of handler
});
```

### Tail Sampling

Manage costs while keeping what matters:

```typescript
function shouldSample(event: WideEvent): boolean {
  // Always keep errors
  if (event.status_code >= 500) return true;
  if (event.error) return true;

  // Always keep slow requests (above p99)
  if (event.duration_ms > 2000) return true;

  // Always keep VIP users
  if (event.user?.subscription === 'enterprise') return true;

  // Always keep requests with specific feature flags (debugging rollouts)
  if (event.feature_flags?.new_checkout_flow) return true;

  // Random sample the rest at 5%
  return Math.random() < 0.05;
}
```

### Common Misconceptions

**"Structured logging is the same as wide events"**
No. Structured logging is JSON instead of strings (table stakes). Wide events are a philosophy: one comprehensive event per request, with all context attached.

**"We use OpenTelemetry, so we're good"**
OpenTelemetry is a delivery mechanism. Most OTel implementations capture the bare minimum: span name, duration, status. You need to deliberately instrument with business context.

**"This is just tracing with extra steps"**
Tracing gives you request flow across services. Wide events give you context within a service. They're complementary. Ideally, your wide events ARE your trace spans, enriched with all context.

**"Logs are for debugging, metrics are for dashboards"**
This distinction is artificial. Wide events can power both. Query them for debugging. Aggregate them for dashboards.

**"High-cardinality data is expensive and slow"**
Expensive on legacy logging systems. Modern columnar databases (ClickHouse, BigQuery) are designed for high-cardinality, high-dimensionality data.

### The Payoff

Debugging transforms from archaeology to analytics:

Before: "The user said checkout failed. Let me grep through 50 services and hope I find something."

After: "Show me all checkout failures for premium users in the last hour where the new checkout flow was enabled, grouped by error code."

One query. Sub-second results. Root cause identified.

### Field Cardinality Spectrum

From most to least useful for debugging:

**Essential (high cardinality):**
- request_id
- trace_id
- user_id
- session_id
- error_code

**Medium:**
- endpoint
- status_code
- region

**Useless (low cardinality):**
- environment
- http_method

---

## Related Concepts

### Three Pillars of Observability

1. **Logs** - Discrete events with context
2. **Metrics** - Aggregated measurements over time
3. **Traces** - Request flow across services

Wide events can serve as the foundation for all three when properly implemented.

### Recommended Tools

For high-cardinality, high-dimensionality data:
- ClickHouse
- BigQuery
- Honeycomb (built for wide events)
- Baselime (serverless-focused)
- **SigNoz** (open-source Datadog alternative)

---

## SigNoz - Open Source Observability Platform

*Source: [signoz.io](https://signoz.io/) - Added: 2026-01-18*

### What It Does
Open-source alternative to Datadog for logs, metrics, and traces. Uses ClickHouse as the backend, making it suitable for high-cardinality data. Native OpenTelemetry support.

### Key Features
- **Unified telemetry**: Logs, metrics, and traces from one platform
- **OpenTelemetry native**: Single SDK generates all telemetry types
- **Powerful ingestion**: Handles 10TB+ daily
- **Data residency options**: Self-host or managed (US, EU, India regions)
- **ClickHouse backend**: Designed for high-cardinality queries

### Deployment Options
1. **Self-hosted**: Full control, no data leaves your infrastructure
2. **Managed cloud**: SigNoz handles infrastructure (choose region for compliance)

### Trade-offs

**Pros:**
- Cost-effective vs Datadog/New Relic (no per-host/per-GB pricing surprises)
- OpenTelemetry-native means no vendor lock-in on instrumentation
- Self-hosting option for data sovereignty
- Active open-source community

**Cons:**
- Self-hosting requires more operational overhead than managed SaaS
- Smaller ecosystem/fewer integrations than established vendors
- May need to manage ClickHouse scaling for very large deployments

### When to Consider
- Outgrowing free tiers of cloud observability tools
- Want observability without per-seat or per-GB cost anxiety
- Need data residency control (compliance requirements)
- Already using OpenTelemetry (or want to migrate to it)
- Comfortable with some self-hosting operational work

---

## HyperDX - Open Source Observability Platform

*Source: [hyperdx.io](https://www.hyperdx.io/) - Added: 2026-01-18*

**Update (2025):** ClickHouse acquired HyperDX to accelerate open-source observability.

### What It Does
Open-source alternative to Datadog that unifies session replays, logs, traces, metrics, and errors. Uses ClickHouse backed by Object Storage for cost-effective storage. Native OpenTelemetry support means no vendor lock-in.

### Key Features
- **Session replay correlation**: Automatically links frontend session replays with backend logs and traces
- **End-to-end tracing**: Traces requests from browser/mobile through backend and async workers
- **Automatic pattern clustering**: Aggregates log patterns to condense billions of events into clusters
- **Fast search**: Terabyte-scale searches in seconds (ClickHouse-powered)
- **Native JSON parsing**: Structured logs work out of the box
- **Automatic instrumentation**: Trace logs, API requests, DB queries with minimal code

### Pricing Model (as of 2025)
- **$0.40 per GB** ingested
- **$0 per user** (unlimited seats)
- **$0 per host** (no agent fees)

Example: 10 TB/month of logs and traces, 30-day retention, 45 hosts, 35 seats → significantly cheaper than Datadog equivalent.

### Integrations
- OpenTelemetry (vendor-agnostic instrumentation)
- Intercom (jump from support ticket to user's session/logs)
- Slack, Email, PagerDuty (alerting)
- Agent-free install option (no sidecars/containers to manage)

### Languages & Platforms
- **Languages**: Node.js, Python, Java, Go, Elixir, React Native, Browser
- **Platforms**: Kubernetes, AWS EC2, Vercel, Fly.io, Heroku, Cloudflare

### HyperDX vs SigNoz

| Aspect | HyperDX | SigNoz |
|--------|---------|--------|
| Session Replays | ✅ Built-in correlation | ❌ Not included |
| Pricing | Per-GB ($0.40) | Per-GB (varies) |
| ClickHouse | Core backend | Core backend |
| OpenTelemetry | Native | Native |
| Acquisition | By ClickHouse | Independent |

### When to Consider HyperDX
- Need session replay alongside backend observability
- Want the Datadog experience without Datadog pricing
- Already running ClickHouse (or want to)
- Frontend-to-backend correlation is important for debugging
- Team size is large (no per-seat pricing)

---

## LLMs for Incident Response - Meta's Approach

*Source: [Parity Blog](https://www.tryparity.com/blog/how-meta-uses-llms-to-improve-incident-response) - Added: 2026-01-18*

Meta achieved **42% accuracy** in using LLMs to identify root causes of incidents in their web monorepo. This means nearly half the time, MTTR could potentially be reduced from hours to seconds.

### The Scale Problem

Meta ships thousands of changes per day to a single monorepo. They literally re-engineered Mercurial to handle the growth velocity. At this scale, "did anyone ship anything recently?" doesn't work as incident response.

### Two-Phase Approach

1. **Heuristic-based retrieval**: Narrow down potential culprit code changes using:
   - Code ownership
   - Directory structures
   - Runtime code graphs

2. **LLM-based ranking**: Fine-tuned Llama 2 7B ranks the narrowed set of changes by likelihood of being the root cause

### Fine-Tuning Process

- **Continued Pre-Training (CPT)**: Model exposed to internal wikis, code repos, Q&A docs
- **Supervised Fine-Tuning (SFT)**: Mixed original Llama 2 training data with Meta's RCA dataset
- Training examples: 2-20 potential code changes per incident, minimal info at investigation start
- Output: Ranked list of potential causes using log probabilities

### Integration

The AI results surface at the start of an investigation automatically. Engineers investigate as normal, but likely root causes are pre-ranked. The AI assists rather than replaces engineer expertise.

### 42% Accuracy - Is That Good?

On surface: seems low vs human performance. In practice: nearly half the time, engineers get the root cause handed to them immediately. Combined with engineer ability to quickly rule out incorrect results, this leads to massive MTTR improvements.

### What's Next: Agents

Natural progression from ranking to agents that can:
- Gather additional context from more data sources
- Find and follow runbooks
- Measure impact
- Take mitigation steps
- Create code changes
- Write initial post-mortems

### Parity - Productizing This Approach

[Parity](https://www.tryparity.com/) is building an "AI SRE for incident response" to bring Meta-like capabilities to all teams. When an alert triggers from PagerDuty/DataDog, Parity's agent investigates, gathers context, and presents findings before the on-call engineer opens their laptop.

### Key Takeaways

1. **Heuristics first, LLMs second**: Don't throw raw data at LLMs. Pre-filter with domain knowledge.
2. **Fine-tuning matters**: Generic LLMs won't have context for your codebase/patterns.
3. **AI as assistant, not replacement**: Surface results early, let engineers validate.
4. **42% is transformative**: Even partial automation of RCA dramatically improves MTTR.
5. **Agents are the future**: Expect LLMs to handle more of the incident lifecycle.

---

## DrDroid Playbooks - Investigation Automation

*Source: [docs.drdroid.io/docs/playbooks](https://docs.drdroid.io/docs/playbooks) - Added: 2026-01-18*

### What It Does
Open-source platform for standardizing on-call investigation and analysis. Define automated investigation steps that run when alerts fire, reducing manual toil and tribal knowledge dependencies.

### Key Features
- **Investigation automation**: Define repeatable steps for common on-call scenarios
- **Data source integration**: Connects to APM, logging platforms, tracing tools, metrics dashboards, Kubernetes, deployment tools
- **Alert enrichment**: Automatically augments alert summaries with relevant context
- **LLM/statistical analysis**: Configure models to interpret data and provide summaries alongside alerts
- **Community templates**: Share investigation playbooks as templates

### Use Cases
1. **Standardize tribal knowledge**: Turn "ask Sarah, she knows how to debug this" into documented, automated runbooks
2. **Reduce human error**: Consistent investigation steps regardless of who's on-call
3. **Accelerate MTTR**: Pre-gather context before the engineer even looks at the alert
4. **Onboarding**: New on-call engineers can follow established playbooks

### How It Fits
Complements the Meta LLM approach above - Playbooks automates the context-gathering and initial investigation steps, which could then feed into LLM-based root cause analysis. Think of it as the "heuristic retrieval" layer for your own incidents.

### Trade-offs
- Requires upfront investment to define playbooks for common scenarios
- Value scales with number of recurring incident types
- Open-source means self-hosting (operational overhead)

---

## Pydantic Logfire - Python-First Observability

*Source: [pydantic.dev/logfire](https://pydantic.dev/logfire) - Added: 2026-01-18*

### What It Does
Observability platform from the Pydantic team, built on OpenTelemetry. Python-first but works with any language. Designed to make observability accessible without needing a dedicated observability team.

### Key Features
- **OpenTelemetry foundation**: Uses OTel for data collection, sends to any OTLP-compatible backend
- **Structured data & SQL**: Query logs directly with SQL, integrates with Pandas/SQLAlchemy
- **Manual tracing API**: Modern logging interface that's easier than raw OpenTelemetry
- **Pydantic integration**: Out-of-the-box monitoring for data flowing through Pydantic models
- **Performance insights**: Identifies slow queries and function runtimes
- **Execution traces**: Full request flow visibility

### Code Examples

Basic logging:
```python
import logfire

logfire.info('Hello, {name}!', name='world')

with logfire.span('payment processing', user_id=123, amount=99.99):
    # code here is timed and traced
    process_payment()
```

SQL querying of structured data:
```sql
SELECT
  attributes->>'campaign' as campaign,
  count(distinct attributes->>'track_id') as clicks
FROM records
WHERE message ilike 'click%'
GROUP BY attributes->>'campaign'
```

### When to Consider
- Python shop wanting observability without the OTel complexity
- Already using Pydantic (get tailored insights for free)
- Want structured logs that are actually queryable
- Prefer MIT-licensed, open-source SDKs
- Need something between "print statements" and "full Datadog deployment"

### Compared to Other Tools

| Aspect | Logfire | HyperDX | SigNoz |
|--------|---------|---------|--------|
| Python Focus | ✅ Primary | General | General |
| Pydantic Integration | ✅ Native | ❌ | ❌ |
| Session Replay | ❌ | ✅ | ❌ |
| Self-host Option | Via OTLP | ✅ | ✅ |
| OpenTelemetry | Native | Native | Native |

### Links
- [Documentation](https://logfire.pydantic.dev/)
- [GitHub (SDK)](https://github.com/pydantic/logfire)
- MIT licensed SDK

---

## WireQuery - Full-Stack Session Replay

*Source: [github.com/wirequery/wirequery](https://github.com/wirequery/wirequery) - Added: 2026-01-19*

### What It Does
Open-source full-stack session replay tool that combines frontend video-like recordings with backend network call traces, including upstream service calls and actual payloads. Designed to give a holistic view of how issues occur across the entire stack.

### Key Features
- **Frontend session replay**: Video-like recordings of user experience
- **Full backend trace correlation**: Network calls to backend services, including upstream calls and payloads
- **WQL (WireQuery Language)**: Query language for backend-first investigations - find issues that users haven't reported yet
- **Privacy-focused SDKs**: Designed to minimize exposure of sensitive information with minimal configuration
- **Bi-directional debugging**: Start from frontend replay OR backend query and trace in either direction

### SDKs Available
- JVM (Java, Kotlin, etc.)
- JavaScript (browser)
- Go
- Universal SDK (other languages)

### Quick Start
```bash
# Docker install
git clone https://github.com/wirequery/wirequery.git
cd wirequery
docker-compose up -d
# Navigate to localhost:8090, login: admin/admin
```

### WireQuery vs HyperDX

| Aspect | WireQuery | HyperDX |
|--------|-----------|---------|
| Session Replay | ✅ | ✅ |
| Backend Trace Correlation | ✅ Full upstream | ✅ |
| Query Language | WQL (specialized) | SQL-like |
| Self-host | ✅ Docker | ✅ |
| Pricing | Open-source (AGPLv3) | $0.40/GB |
| Primary Focus | Full-stack debugging | Unified observability |

### When to Consider WireQuery
- Need to correlate frontend issues with deep backend traces (multiple upstream services)
- Want backend-first investigation capability (find issues before users report them)
- Prefer AGPLv3 open-source licensing
- Have complex microservice architectures where seeing the full call chain matters

### Trade-offs
- AGPLv3 license (more restrictive than MIT/Apache for commercial use)
- Smaller community than established alternatives
- Self-hosting required (no managed option mentioned)
- May overlap with existing APM tools for backend tracing

---

## Sentry Performance - Endpoint Regression Detection

*Source: [Sentry Workshop](https://sentry.io/resources/identify-trace-fix-endpoint-regression-issues-workshop/) - Added: 2026-01-19*

### What It Does
Automatic regression detection for API endpoints. Identifies when performance degrades due to inefficient code, resource bottlenecks, or slow database calls before they bring your app down.

### Workshop Coverage
Engineer Tony Xiao's demo covers:
1. **End-to-end request tracing**: Correlating frontend issues with backend bottlenecks
2. **Performance Issues feature**: Automated detection of regressions
3. **Root cause identification**: Drilling down from endpoint slowdown to specific code/query

### Key Capabilities
- **Automatic baseline establishment**: Learns normal performance patterns for each endpoint
- **Threshold-based alerts**: Flags when endpoints cross p95/p99 degradation thresholds
- **Transaction profiling**: Shows exact functions/queries contributing to slowdown
- **Version correlation**: Links regressions to specific deployments/commits

### Common Regression Causes
- Inefficient code (N+1 queries, missing indexes)
- Resource bottlenecks (memory leaks, connection pool exhaustion)
- Slow database calls (missing indexes, table locks, query plan changes)
- Cascading failures (timeout increases, retry storms)

### Integration Pattern
```python
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="...",
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,  # Adjust based on volume
    profiles_sample_rate=1.0,  # Profile slow transactions
    enable_tracing=True,
)
```

### Compared to Other Tools

| Aspect | Sentry | HyperDX | SigNoz | Pydantic Logfire |
|--------|--------|---------|--------|------------------|
| Regression Detection | ✅ Automatic | Manual | Manual | Manual |
| Frontend Correlation | ✅ | ✅ | ❌ | ❌ |
| Pricing Model | Per-event | Per-GB | Per-GB | Per-GB |
| Self-host | ✅ | ✅ | ✅ | Via OTLP |
| OpenTelemetry | Compatible | Native | Native | Native |

### When to Consider Sentry
- Need automatic regression detection out of the box
- Want frontend error tracking + backend performance in one tool
- Already paying for Sentry (performance is an add-on)
- Prefer managed SaaS over self-hosting
- Don't want to build custom alerting logic for regressions

### Trade-offs
**Pros:**
- Zero-config regression detection (learns baselines automatically)
- Strong frontend-backend correlation
- Mature ecosystem with many integrations
- Managed service (no operational overhead)

**Cons:**
- Per-event pricing can get expensive at scale
- Less flexible than query-based tools (HyperDX, SigNoz) for custom analysis
- Proprietary vs open-source alternatives
- Performance monitoring requires separate subscription tier

### Links
- [Workshop recording](https://sentry.io/resources/identify-trace-fix-endpoint-regression-issues-workshop/)
- [Sentry Performance docs](https://docs.sentry.io/product/performance/)
- [Django integration guide](https://docs.sentry.io/platforms/python/guides/django/)

---

## structlog - Structured Logging for Python/Django

*Source: https://loop0.sh/posts/structlog-with-django-is-awesome/ - Added: 2026-01-19*

### What It Does
Python library that enhances standard logging with structured key-value or JSON output. Offers elegant console rendering during development, production-ready JSON for log aggregation systems.

### Why It Matters
Complements the "wide events" philosophy above by making structured logging trivial in Python. Instead of string-formatting log messages, you log events as structured data.

### Django Integration

```python
# settings.py
import structlog

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json_formatter": {
            "()": structlog.stdlib.ProcessorFormatter,
            "processor": structlog.processors.JSONRenderer(),
        },
        "plain_console": {
            "()": structlog.stdlib.ProcessorFormatter,
            "processor": structlog.dev.ConsoleRenderer(),
        },
        "key_value": {
            "()": structlog.stdlib.ProcessorFormatter,
            "processor": structlog.processors.KeyValueRenderer(
                key_order=['timestamp', 'level', 'event', 'logger']
            ),
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "plain_console"  # or json_formatter for prod
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}

structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
    ],
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    cache_logger_on_first_use=True
)
```

### Usage

```python
import structlog

logger = structlog.get_logger()

# Instead of: logger.info(f"User {user.id} logged in")
logger.info("User logged in", user_id=request.user.id)

# Add context throughout request lifecycle
logger.info(
    "checkout_completed",
    user_id=user.id,
    cart_total=cart.total,
    payment_method=payment.method,
    duration_ms=elapsed_ms
)
```

### Formatters

**ConsoleRenderer** (development):
- Colorized, human-readable output
- Great for local debugging
- Example: `2026-01-19T10:23:45Z [info] User logged in user_id=123`

**JSONRenderer** (production):
- Machine-readable JSON
- Works with log aggregation systems (Datadog, CloudWatch, etc.)
- Example: `{"timestamp": "2026-01-19T10:23:45Z", "level": "info", "event": "User logged in", "user_id": 123}`

**KeyValueRenderer** (alternative):
- Plain key=value pairs
- Easy to grep/parse without JSON tooling

### Advanced: Django-Structlog

For automatic request context, see [django-structlog](https://django-structlog.readthedocs.io/):
- Automatic request_id injection
- User info binding
- Correlation IDs
- Middleware for context propagation

### Compared to Standard Logging

| Aspect | structlog | stdlib logging |
|--------|-----------|----------------|
| Format | Structured k=v or JSON | String templates |
| Context | Bind context, propagates | Manual f-string every time |
| Parsing | Machine-readable | Regex parsing required |
| Wide Events | Natural fit | Requires manual formatting |

### When to Use
- Starting new Django projects (easier to set up from scratch)
- Migrating to structured logging (can coexist with stdlib)
- Need to send logs to modern observability tools
- Want better local development log readability
- Building towards "wide events" approach

### Installation

```bash
pip install structlog
```

### Links
- [structlog documentation](https://www.structlog.org/)
- [django-structlog](https://django-structlog.readthedocs.io/)
- GitHub: [hynek/structlog](https://github.com/hynek/structlog)
