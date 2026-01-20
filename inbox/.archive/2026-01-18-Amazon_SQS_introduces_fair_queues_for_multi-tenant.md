---
type: link
source: notion
url: https://aws.amazon.com/about-aws/whats-new/2025/07/amazon-sqs-introduces-fair/
notion_type: Software Repo
tags: ['Running']
created: 2025-07-22T01:33:00.000Z
---

# Amazon SQS introduces fair queues for multi-tenant workloads - AWS

## Overview (from Notion)
- Fair Queues Improve User Experience: As a software engineer and founder, implementing fair queues can enhance the performance of applications, improving user satisfaction and reducing complaints from clients using shared systems.
- Scalability for Growth: In a bustling city like NYC, as your company grows, using fair queues can help manage increased loads without sacrificing service quality, allowing for smoother scaling.
- Multi-Tenant Applications: If you’re developing multi-tenant applications, fair queues can mitigate the impact of one client's heavy usage on others, ensuring equitable resource distribution, which is essential for maintaining customer trust.
- SaaS Opportunities: This feature could open new avenues for SaaS products, allowing you to cater to businesses that need robust, reliable messaging systems while managing their workloads effectively.
- Innovative Solutions: Fair queues offer a fresh perspective on managing message processing, encouraging a focus on resilience and adaptability in your software architecture.
- Consider Alternative Views: Some might argue that fair queues add complexity to the system design. Balancing the benefits of improved service with the need for streamlined operations could be a point of discussion.

## AI Summary (from Notion)
Amazon SQS introduces fair queues to reduce the impact of noisy neighbors in multi-tenant workloads, ensuring consistent message delivery and quality of service. By using a message group ID, fair queues prioritize messages from different tenants, maintaining throughput without requiring changes to message consumers. This feature is beneficial for SaaS applications and is available in all AWS regions.

## Content (from Notion)

Amazon Simple Queue Service (Amazon SQS) now offers fair queues, a new feature that mitigates noisy neighbor impact in multi-tenant standard queues. When one tenant (such as a customer, client application, or request type) sends too many messages or has messages that require longer processing time, fair queues help keep other tenants' messages flowing without long delays. This preserves quality of service for all tenants while maintaining the scalability and throughput of standard queues.

To enable fair queues, include a message group ID when sending messages to your Amazon SQS standard queues. No changes to message consumers are required, allowing you to adopt fair queues in live systems with no interruption or migration. Fair queues are particularly valuable for SaaS applications serving multiple customers through shared queues, microservices processing events from multiple resources, and applications handling messages for different request types. Fair queues help maintain consistent dwell time (the time a message spends in the queue between being sent and received) across tenants by reordering messages when a single tenant causes the queue to build a backlog. The queue then prioritizes delivering messages from other tenants. Messages from the tenant causing the backlog continue to be delivered to consumers, but their dwell time increases based on your available consumer capacity.

Fair queues are available in all AWS commercial and AWS GovCloud (US) Regions. For more information about Amazon SQS fair queues, read our blog post and visit Amazon SQS Developer Guide.


