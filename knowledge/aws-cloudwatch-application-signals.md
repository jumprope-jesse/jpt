# AWS CloudWatch Application Signals

*Source: https://aws.amazon.com/about-aws/whats-new/2024/06/amazon-cloudwatch-application-signals-application-monitoring/ - Added: 2026-01-18*

## What It Is

OpenTelemetry-compatible APM feature in CloudWatch that automatically instruments applications and tracks performance against SLOs. Generally available since June 2024.

## Key Features

- **Auto-instrumentation**: No custom code required
- **Pre-built dashboard**: Shows volume, availability, latency, faults, and errors
- **Correlated telemetry**: Connects metrics, traces, logs, RUM, and synthetic monitoring
- **SLO tracking**: Define and track service level objectives

## The Debugging Workflow

Example scenario: Payment processing latency spike

1. Application Signals dashboard shows latency increase
2. Drill into correlated trace to see which component is slow
3. If using Container Insights, identify infrastructure root cause (memory shortage, high CPU)
4. Root cause identified without log archaeology

## Integration Points

- **Container Insights**: Correlate app performance with container metrics (CPU, memory, pod issues)
- **OpenTelemetry**: Standard instrumentation, no vendor lock-in
- **X-Ray**: Tracing backend for distributed request flows

## Availability

28 commercial AWS regions. Not available in:
- CA West (Calgary)
- AWS GovCloud (US)
- China regions

## When to Consider

- Running containerized workloads on EKS/ECS
- Need APM without instrumenting every service manually
- Already invested in CloudWatch ecosystem
- Want correlation between app metrics and container infrastructure
- Defining SLOs for critical services

## Related

- See `wide-events-observability.md` for implementing rich observability in application code
- See `aws-xray-adaptive-sampling.md` for intelligent trace sampling

## Resources

- [One Observability Workshop](https://catalog.workshops.aws/observability/) - Sample app to try Application Signals
- [Enable for Amazon EKS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-Enable-EKS.html)
- [Enable for Amazon EC2](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-Enable-EC2.html)
