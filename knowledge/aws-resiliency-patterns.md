# AWS Resiliency Patterns and Trade-offs

*Source: [AWS Architecture Blog - Understand resiliency patterns and trade-offs](https://aws.amazon.com/blogs/architecture/understand-resiliency-patterns-and-trade-offs-to-architect-efficiently-in-the-cloud/) - Added: 2026-01-20*

Framework for evaluating cloud architecture resiliency patterns, with five patterns at different points on the cost/complexity vs. resilience spectrum.

## What Is Resiliency?

Per AWS Well-Architected Framework: "the capability to recover when stressed by load (more requests for service), attacks (either accidental through a bug, or deliberate through intention), and failure of any component in the workload's components."

## Trade-off Dimensions

Every resiliency pattern should be evaluated across:

| Factor | Consideration |
|--------|---------------|
| **Design Complexity** | More complexity = more emergent behaviors, more potential failure points |
| **Cost to Implement** | Higher resilience usually means more infrastructure components |
| **Operational Effort** | Highly resilient systems require mature processes and advanced skills |
| **Effort to Secure** | More components = more security surface area |
| **Environmental Impact** | Increased deployment footprint = higher resource consumption |

## The Five Patterns

### P1: Multi-AZ (Single Instance)

```
┌─────────────────────────────────────┐
│              Region                  │
│  ┌─────────┐        ┌─────────┐    │
│  │   AZ1   │        │   AZ2   │    │
│  │ ┌─────┐ │        │         │    │
│  │ │ EC2 │ │  Fail  │ New EC2 │    │
│  │ └─────┘ │  ───►  │ launches│    │
│  └─────────┘        └─────────┘    │
└─────────────────────────────────────┘
```

**How it works:** Single EC2 in Auto Scaling group. On AZ failure, ASG recreates instance in healthy AZ.

**Trade-offs:**
- ✅ Lowest cost
- ✅ Simple architecture
- ❌ **Bimodal behavior**: Users experience downtime during re-provisioning

**Best for:** Low-impact internal applications, dev/test environments

---

### P2: Multi-AZ with Static Stability

```
┌─────────────────────────────────────┐
│              Region                  │
│  ┌─────────┐        ┌─────────┐    │
│  │   AZ1   │        │   AZ2   │    │
│  │ ┌─────┐ │        │ ┌─────┐ │    │
│  │ │ EC2 │ │        │ │ EC2 │ │    │
│  │ └─────┘ │        │ └─────┘ │    │
│  └────┬────┘        └────┬────┘    │
│       └────────┬─────────┘         │
│           ┌────┴────┐              │
│           │   ELB   │              │
│           └─────────┘              │
└─────────────────────────────────────┘
```

**How it works:** Multiple instances pre-provisioned across AZs. Load balancer routes around failures. No control plane calls needed during recovery.

**Key concept - Static Stability:** System remains stable in one mode regardless of environment changes. Pre-provisioned capacity means no dependency on AWS control planes being available during a disruption.

**Trade-offs:**
- ✅ No downtime during AZ failure
- ✅ No dependency on control plane availability
- ❌ Higher cost (200% capacity in 2 AZs, or 150% across 3 AZs)
- ❌ App must support distributed operation

**Cost optimization:** Deploy across 3+ AZs to reduce over-provisioning (150% vs 200%)

**Best for:** Customer-facing apps, revenue-generating workloads

---

### P3: Application Portfolio Distribution

```
┌─────────────────┐    ┌─────────────────┐
│    Region A     │    │    Region B     │
│  ┌───────────┐  │    │  ┌───────────┐  │
│  │Mobile App │  │    │  │  Web App  │  │
│  └───────────┘  │    │  └───────────┘  │
└─────────────────┘    └─────────────────┘
         │                      │
         └──────────┬───────────┘
                    │
              Shared Backend
              (data sources)
```

**How it works:** Different critical applications deployed to separate regions. Regional failure impacts only one application type.

**Example:** Mobile app in us-east-1, web app in us-west-2. Regional event affects one channel but users can access service via the other.

**Trade-offs:**
- ✅ Reduces impact surface area of regional events
- ❌ Requires significant operational planning
- ❌ Shared downstream dependencies may still be single points of failure

**Best for:** Multi-channel applications, reducing simultaneous multi-app outages

---

### P4: Multi-AZ with Multi-Region DR

Two sub-patterns for disaster recovery:

#### Pilot Light (RTO/RPO: 10s of minutes)

```
┌─────────────────┐    ┌─────────────────┐
│ Primary Region  │    │    DR Region    │
│  ┌───────────┐  │    │  ┌───────────┐  │
│  │ Running   │  │    │  │  Stopped  │  │
│  │ Workload  │  │    │  │   Infra   │  │
│  └───────────┘  │    │  └───────────┘  │
│       │         │    │       │         │
│  ┌────┴────┐    │    │  ┌────┴────┐    │
│  │   DB    │────┼────┼─►│ Replica │    │
│  └─────────┘    │    │  └─────────┘    │
└─────────────────┘    └─────────────────┘
```

- Data actively replicated
- Infrastructure pre-provisioned but **OFF**
- Cost optimized - pay for storage, not compute
- Startup time during restore event

#### Warm Standby (RTO/RPO: minutes)

- Data actively replicated
- Infrastructure running at **reduced capacity**
- Faster restore - scale up vs. start up
- Higher cost than Pilot Light

**Trade-offs:**
- ✅ Mitigates regional service disruptions
- ✅ More cost-effective than active-active
- ❌ Increased deployment complexity (syncing infra changes)
- ❌ Testing resilience is complex

**Pro tip:** Use Infrastructure as Code to keep regions in sync

---

### P5: Multi-Region Active-Active

```
┌─────────────────┐    ┌─────────────────┐
│    Region A     │    │    Region B     │
│  ┌───────────┐  │    │  ┌───────────┐  │
│  │ Running   │◄─┼────┼─►│ Running   │  │
│  │ Workload  │  │    │  │ Workload  │  │
│  └─────────┬─┘  │    │  └─┬─────────┘  │
│            │    │    │    │            │
│       ┌────┴────┼────┼────┴────┐       │
│       │    DB Async Replication│       │
│       └─────────┴────┴─────────┘       │
└─────────────────┘    └─────────────────┘
              ▲
              │
         ┌────┴────┐
         │  Route  │
         │   53    │
         └─────────┘
```

**How it works:** Applications run simultaneously in multiple regions, serving traffic from all. Global load balancing distributes requests.

**Trade-offs:**
- ✅ RTO of near-zero
- ✅ RPO of near-zero data loss
- ❌ Most complex pattern
- ❌ Most expensive
- ❌ Async replication introduces data consistency challenges
- ❌ Requires very high process maturity

**Best for:** Zero-tolerance-for-downtime workloads (core banking, mission-critical CRM)

**Recommendation:** Build up to this gradually, starting with simpler patterns.

## Pattern Comparison

| Pattern | Downtime During Failure | Regional Resilience | Cost | Complexity |
|---------|------------------------|---------------------|------|------------|
| P1: Multi-AZ | Yes (re-provisioning) | No | $ | Low |
| P2: Multi-AZ Static | No | No | $$ | Medium |
| P3: Portfolio Dist. | Partial (one app) | Partial | $$ | Medium |
| P4: Multi-Region DR | Yes (recovery time) | Yes | $$-$$$ | High |
| P5: Active-Active | No | Yes | $$$$ | Very High |

## Decision Framework

1. **What's the business impact of downtime?** Revenue loss, reputation, regulatory fines
2. **What are your RTO/RPO requirements?** Drives P4 vs P5 choice
3. **What's your operational maturity?** Complex patterns need mature processes
4. **What's your budget?** Higher resilience = higher cost

## Related

- See `aws-arc-region-switch.md` for automating multi-region failovers
- See `aws-multi-tenancy-architecture.md` for related isolation patterns
- AWS Well-Architected Framework - Reliability Pillar
- [Disaster Recovery of Workloads on AWS](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html)
