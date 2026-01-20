# AWS SQS FIFO Queue CloudWatch Metrics

**Added:** 2026-01-18
**Source:** [AWS What's New](https://aws.amazon.com/about-aws/whats-new/2024/07/amazon-sqs-cloudwatch-metrics-fifo-queues)

## Overview

Amazon SQS provides two CloudWatch metrics specifically for FIFO queues to improve visibility into queue behavior and help with troubleshooting.

## Metrics

### NumberOfDeduplicatedSentMessages

Counts messages sent to a queue that were deduplicated.

**Use case:** Determine if a producer is sending duplicate messages. High numbers indicate producer-side issues (retries without proper idempotency, bugs in message generation).

### ApproximateNumberOfGroupsWithInflightMessages

Approximate count of message groups with "in flight" messages (received by consumer but not yet deleted).

**Use case:** Troubleshoot and optimize FIFO throughput:
- High count with low throughput → consumers may be slow
- Low count with available capacity → add more message groups to parallelize
- Helps identify if you need to scale consumers or increase message group diversity

## Key Concepts

- **In flight message**: Received from queue but not yet deleted (consumer is processing it)
- **Message group**: FIFO queues process messages within a group in order; different groups can be processed in parallel
- Metrics available per-queue via SQS and CloudWatch consoles

## Availability

All AWS regions where Amazon SQS is available.

## Operational Tips

- Monitor `NumberOfDeduplicatedSentMessages` spikes after deployments to catch producer bugs early
- Use `ApproximateNumberOfGroupsWithInflightMessages` to right-size consumer fleet
- Combine with existing SQS metrics like `ApproximateAgeOfOldestMessage` for complete picture
