---
type: link
source: notion
url: https://aws.amazon.com/about-aws/whats-new/2024/07/amazon-sqs-cloudwatch-metrics-fifo-queues
notion_type: Tech Announcement
tags: ['Running']
created: 2024-07-08T22:20:00.000Z
---

# Amazon SQS introduces new Amazon CloudWatch metrics for FIFO queues - AWS

## AI Summary (from Notion)
- New Metrics Introduced: Amazon SQS now offers two new Amazon CloudWatch metrics specifically for FIFO queues.
- Enhanced Visibility: The metrics provide improved visibility into FIFO queue usage for SQS customers.
- Key Metrics:
- NumberOfDeduplicatedSentMessages: Indicates how many messages sent were deduplicated, helping identify if duplicate messages are being sent by producers.
- ApproximateNumberOfGroupsWithInflightMessages: Shows the approximate count of message groups with messages that are "in flight," aiding in troubleshooting and optimization of FIFO queue throughput.
- Per-Queue Basis: Metrics are available for individual queues, allowing for targeted analysis and monitoring.
- Global Availability: The metrics can be accessed in all AWS regions where Amazon SQS is offered.
- Resources for Further Information: Links provided for accessing metrics through SQS and CloudWatch consoles, as well as documentation for SQS metrics.

## Content (from Notion)

Amazon Simple Queue Service introduces two new Amazon CloudWatch metrics to improve the usage visibility of FIFO queues. Amazon SQS is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications.

With the new metrics, SQS customers have greater visibility into their FIFO usage. The new metrics are:

- NumberOfDeduplicatedSentMessages - The number of messages sent to a queue that were deduplicated. This metric helps in determining if a producer is sending duplicate messages to an SQS FIFO queue.
- ApproximateNumberOfGroupsWithInflightMessages - The approximate number of message groups with inflight messages, where a message is considered to be in flight after it is received from a queue by a consumer, but not yet deleted from the queue. This metric helps you troubleshoot and optimise your FIFO queue throughput by either increasing FIFO message groups or scaling your consumers.
Metrics are available on a per-queue basis, and can be accessed through SQS and CloudWatch consoles. These metrics are available in all AWS regions where Amazon SQS is available.

To learn more, see SQS Metrics Documentation.


