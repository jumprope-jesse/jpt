# AWS X-Ray Adaptive Sampling

*Source: https://aws.amazon.com/about-aws/whats-new/2025/09/aws-x-ray-adaptive-sampling-automatic-error/ - Added: 2026-01-18*

## The Problem

DevOps teams and SREs face a classic trade-off with trace sampling:
- **Sample rate too low** → Miss critical traces during incidents
- **Sample rate too high** → Unnecessary observability costs during normal operations

## Solution: Adaptive Sampling

AWS X-Ray now automatically adjusts sampling rates within user-defined limits to capture important traces when needed while maintaining cost efficiency during normal operations.

## Two Approaches

### 1. Sampling Boost
Temporarily increases sampling rates when anomalies are detected. Captures complete traces during incidents for root cause analysis.

### 2. Anomaly Span Capture
Ensures anomaly-related spans are always captured, even when the full trace isn't sampled. Useful for catching errors without full trace overhead.

These can be used independently or combined.

## Benefits

- **Reduced MTTR**: Comprehensive trace data available during incidents for faster root cause analysis
- **Cost efficiency**: Normal operations use lower sampling rates
- **Automatic**: No manual intervention needed to increase sampling during problems

## Availability

Available in all commercial AWS regions where X-Ray is offered.

## Related

- See `wide-events-observability.md` for tail sampling patterns in application code
- X-Ray integrates with CloudWatch for unified observability
