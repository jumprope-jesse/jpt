# Aurora Serverless v2 + Reserved Instance Hybrid Pattern

*Source: [Reddit r/aws discussion](https://www.reddit.com/r/aws/comments/1ayr108/combining_aurora_serverless_v2_with_reserved/) - Feb 2024*

## The Pattern

Use Reserved Instances for stable baseline workload while adding Aurora Serverless v2 readers for burst/spike handling. This hybrid approach optimizes costs while maintaining performance during traffic spikes.

## When This Makes Sense

- **Predictable baseline + unpredictable spikes**: Daily usage is stable (covered by RIs) but periodic spikes cause performance issues
- **Cost optimization**: RIs for 99.9% of traffic, Serverless v2 for the remaining 0.1% burst capacity
- **Reader-scale workloads**: Spikes primarily affect read traffic (serverless reader can absorb read load)

## Implementation Questions

### RDS Proxy Traffic Routing

Can RDS Proxy intelligently route spiky traffic to the serverless reader?

- RDS Proxy can route reads to reader endpoints
- For intelligent load-based routing, may need application-level logic or connection weighting
- Consider: reader endpoint round-robin vs. custom routing

### Serverless v2 ACU Configuration

Should minimum ACU match the database's memory needs, or can it remain low for autoscaling?

- **Min ACU tradeoff**: Lower min = cheaper standby cost but slower scale-up
- Aurora Serverless v2 scales in increments of 0.5 ACU, adding capacity as needed
- If spikes are predictable, consider scheduled scaling events
- Memory-intensive queries may fail if ACU is too low during scale-up window

### Cost Calculation

Rough model:
- RI cost: Fixed monthly for baseline compute
- Serverless v2 cost: Per-ACU-hour for additional capacity
- Compare: Serverless burst cost vs. provisioning higher RI capacity

## Architecture Options

### Option 1: Serverless Reader for Spikes

```
Primary (RI) ──┬── Reader 1 (RI)        ← Baseline reads
               └── Reader 2 (Serverless v2) ← Spike absorption
```

### Option 2: Serverless Primary + RI Readers

Less common, but could work for write-heavy spike scenarios.

## Considerations

1. **Scale-up latency**: Serverless v2 scales quickly but not instantly - ensure min ACU can handle initial spike while scaling
2. **Connection management**: RDS Proxy helps manage connections during scaling
3. **Monitoring**: CloudWatch alarms for ACU utilization to understand burst patterns
4. **Reserved Instance coverage**: RIs apply to specific instance types; serverless ACU is separate billing

## Related Concepts

- Aurora Serverless v2 scaling behavior
- RDS Proxy connection pooling and routing
- AWS Reserved Instance coverage for RDS
- Read replica load balancing strategies

## Why This Pattern Isn't Common

Most blog posts compare Serverless v2 vs. RI as mutually exclusive options because:
1. Serverless v2 is typically more expensive at steady state
2. If you know your baseline, RI is more cost-effective for that portion
3. Hybrid adds operational complexity

The hybrid pattern makes sense when:
- Baseline is truly predictable
- Spikes are significant but infrequent
- You want to avoid over-provisioning RI capacity

## Open Questions

- Best practices for min ACU sizing when using as burst capacity
- Optimal RDS Proxy configuration for hybrid routing
- CloudWatch metrics to track RI vs. serverless utilization split
