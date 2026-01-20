# AWS Multi-Tenancy Architecture

*Source: [The single-tenancy to multi-tenancy spectrum](https://lucvandonkersgoed.com/2023/12/08/the-single-tenancy-to-multi-tenancy-spectrum/) by Luc van Donkersgoed - Added: 2026-01-19*

A case study from building PostNL's Event-Broker e-Commerce (EBE) platform, covering the journey from single-tenant to multi-tenant architecture and the trade-offs involved.

## The Spectrum

**Key insight:** Single-tenancy vs multi-tenancy is not a binary choice - it's a spectrum with architectural options at every point.

```
Single-Tenant ←――――――――――――――――――→ Multi-Tenant
(High Isolation)                    (High Scalability)

Benefits:
- Simple to develop        ←→    - Unbounded scale
- Small blast radius       ←→    - Resource efficiency
- Stateless resources      ←→    - Fast deployments
- No cross-tenant logic    ←→    - Cost effective

Drawbacks:
- AWS resource limits      ←→    - Runtime complexity
- Slow deployments         ←→    - Large blast radius
- Concurrency issues       ←→    - Shared fate design
```

## Single-Tenancy Architecture

### What It Looks Like
Every consumer gets a dedicated CloudFormation stack containing:
- Unique API Gateway endpoints
- Isolated Lambda functions
- Dedicated SQS queues
- Separate event routing infrastructure

Configuration is **baked in at deploy time** - Lambda environment variables are set once per tenant, making resources stateless with no runtime dependencies.

### Pros

**1. Speed of Development**
- Inherently simpler to reason about
- Look at any resource → instantly know it serves one tenant
- Zero risk of cross-tenant resource access
- No complex routing logic needed

**2. Small Blast Radius**
- Deploy updates to one tenant at a time
- Verify behavior before moving to next tenant
- Avoids "big bang" deployments affecting all tenants
- Minimizes noisy neighbor problems

**3. Immutable Configuration**
- Resources configured once at deployment
- No external control plane dependencies
- Each tenant can have different settings (e.g., BACKOFF_RATE)

### Cons

**1. Hard AWS Resource Limits**

Hit these ceilings at scale:
- **5,000 IAM roles per account** - at 560 stacks, max 8 roles/stack
  - Had to consolidate roles, violating principle of least privilege
- **CloudFormation stack limits**
- **CloudWatch alarms/metrics costs**

**2. Concurrency Limits During Deployments**

At ~100 stacks, parallel updates caused:
- Max concurrent CodeBuild containers
- API Gateway deploy rate limits
- CloudFormation concurrent stack operations
- **Lambda control plane limit: 15 ops/second**
  - 100 stacks × multiple Lambdas each = rate limit hell
  - Failed updates trigger rollbacks... which also hit rate limits
  - Result: `UPDATE_ROLLBACK_FAILED` (the pain state)

**Solution:** Limit deployment concurrency to 50 using Step Functions state machine orchestration
- Outer state machine: checks concurrency, backs off if >50
- Inner state machine: performs actual CDK deployment
- Cost: deployments take ~1 hour (10 waves × 5 min each for 500 stacks)

## Multi-Tenancy Architecture

### What It Looks Like
- Single ingress service receives all events
- Single egress service forwards all events
- Configuration retrieved **at runtime** (push or pull mechanism)
- Shared infrastructure across all tenants

### Pros
- **Reduced resources** - no per-tenant duplication
- **Avoid concurrency limits** - single deployment instead of hundreds
- **Fast deployments** - one update instead of waves
- **Unbounded scale** - only way to serve large customer counts

### Cons
- **Runtime complexity** - must fetch and maintain tenant configuration in local state
- **Larger blast radius** - incident affects all tenants
- **Increased service complexity** - more opportunity for bugs
- **Harder to develop** - need robust isolation and consistency measures

## The Middle Ground: Tiered/Cellular Architectures

Don't have to choose the extremes. Options include:

### Tiered Architecture (PostNL's Approach)
- **Tier 3:** Internal testing/validation tenants
- **Tier 2:** Non-critical production workloads
- **Tier 1:** Mission-critical production

Each tier is multi-tenant, but isolated from other tiers.

**Deployment flow:** Tier 3 → validate → Tier 2 → validate → Tier 1

**Result:**
- Smaller blast radius than pure multi-tenant
- Better isolation for critical workloads
- Slightly more resources + slower deploys than pure multi-tenant
- Still scales within each tier

### Other Options
- **Regional:** Separate infrastructure per AWS region
- **Zonal:** Separate per availability zone
- **Cell-based:** Physical server/rack isolation
- **Hybrid:** Mix and match based on tenant criticality

All follow same principle: divide large multi-tenant system into smaller chunks, each still multi-tenant but with better isolation.

## Decision Framework

### Choose Single-Tenancy If:
- Limited, known customer count (won't grow past AWS limits)
- Need maximum isolation (security, compliance)
- Early stage product finding market fit
- Speed to market > operational efficiency
- Small team that benefits from simpler architecture

### Choose Multi-Tenancy If:
- Need to serve many customers (hundreds to millions)
- Already hitting AWS resource/concurrency limits
- Mature product with stable feature set
- Have operational maturity to handle complexity
- Cost optimization is important

### Choose Tiered/Cellular If:
- Need to scale but want controlled blast radius
- Different customer tiers with different SLAs
- Want progressive rollout capabilities
- Can afford slightly higher operational overhead

## Key Lessons

1. **Single-tenancy is a valid long-term choice** for bounded scale - not just for MVPs
2. **Every AWS service is multi-tenant** - it's the only way to reach AWS-scale
3. **The spectrum exists** - don't feel forced to pick extremes
4. **Context matters** - business stage, stakeholder priorities, team capabilities all factor in
5. **You can migrate** - start simple (single-tenant), evolve to multi-tenant when you hit limits

## AWS-Specific Gotchas

### Resource Limits That Hurt
- IAM roles: 5,000 per account
- CloudFormation stacks: 2,000 per account (soft limit)
- Lambda control plane: 15 operations/second

### Deployment Orchestration
When managing many stacks:
- Monitor concurrency to avoid rate limits
- Implement exponential backoff
- Use Step Functions for orchestration
- Consider canary deployments (small batch → verify → bulk)

### Signs You've Outgrown Single-Tenancy
- Hitting IAM role limits
- Deployments taking >30 minutes
- Frequent `UPDATE_ROLLBACK_FAILED` states
- Spending more time on deployment orchestration than features
- CloudWatch costs spiraling from per-tenant metrics
