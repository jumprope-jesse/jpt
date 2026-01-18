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
