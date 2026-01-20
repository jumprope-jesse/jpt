# AWS SQS Fair Queues

**Added:** 2026-01-18
**Source:** [AWS What's New](https://aws.amazon.com/about-aws/whats-new/2025/07/amazon-sqs-introduces-fair/)

## Overview

Amazon SQS fair queues mitigate "noisy neighbor" impact in multi-tenant standard queues. When one tenant sends too many messages or has messages requiring longer processing, fair queues keep other tenants' messages flowing without long delays.

## How It Works

- Include a **message group ID** when sending messages to standard queues
- No changes to message consumers required - can adopt in live systems with no interruption
- Fair queues reorder messages when a single tenant causes backlog
- Prioritizes delivering messages from other tenants
- Messages from backlog-causing tenant continue delivery but with increased dwell time based on available consumer capacity

## Key Concepts

- **Dwell time**: Time a message spends in the queue between being sent and received
- Fair queues maintain consistent dwell time across tenants by reordering during backlogs

## Use Cases

- SaaS applications serving multiple customers through shared queues
- Microservices processing events from multiple resources
- Applications handling messages for different request types

## Availability

Available in all AWS commercial and AWS GovCloud (US) Regions.

## Trade-offs

- Adds some complexity to system design (need to manage message group IDs)
- Messages from heavy-usage tenants will experience increased latency during backlogs
- Balance improved fairness with operational simplicity
