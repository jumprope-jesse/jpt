---
type: link
source: notion
url: https://lucvandonkersgoed.com/2023/12/08/the-single-tenancy-to-multi-tenancy-spectrum/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-02-18T21:13:00.000Z
---

# The single-tenancy to multi-tenancy spectrum – Luc van Donkersgoed's Notes

## AI Summary (from Notion)
- Transition from Single-Tenancy to Multi-Tenancy: The author discusses their experience moving from a single-tenant to a multi-tenant architecture due to scalability issues.

- Single-Tenancy Architecture:
- Pros:
- Simplifies development and maintenance as resources are isolated per tenant.
- Reduces risks of cross-tenant resource access and simplifies routing logic.
- Allows for smaller deployment risks, minimizing the impact of failures (small blast radius).
- Cons:
- Limits on AWS resources (e.g., IAM roles, CloudFormation stacks) lead to operational constraints.
- Challenges with concurrency during deployments can cause failures.

- Multi-Tenancy Architecture:
- Benefits:
- Reduces the number of resources needed, leading to cost efficiency.
- Helps avoid hitting concurrency limits, allowing for faster deployments.
- Challenges:
- Increased complexity in service configuration at runtime.
- Greater potential blast radius affecting multiple tenants during incidents.

- Trade-offs: Choosing between single and multi-tenancy involves weighing isolation against scalability. While multi-tenancy can handle more users, it introduces complexity and potential risks.

- Middle Ground Solutions: The author suggests tiered architectures as a compromise, providing a balance between resource sharing and tenant isolation by creating segmented environments.

- Final Thoughts: The best architecture choice depends on business context, application lifecycle, and stakeholder priorities. Single-tenancy may be suitable for limited customer counts, while multi-tenancy is essential for scaling with many users.

## Content (from Notion)

In the past few years I have been building a multi-consumer application with a single-tenant architecture. Each consumer has a distinct, isolated stack of resources, leading to simplicity and small blast radiuses (radii?). However, we’re hitting scalability limits and will be moving to a multi-tenancy architecture soon. In this post we will cover the pros and cons of single-tenancy architecture, and how single-tenancy versus multi-tenancy is not a binary choice.

## Background

The application we’re covering is the Event-Broker e-Commerce, or EBE. This internal PostNL platform is responsible for receiving events from many applications, and routing the right events to the applications subscribed to them.

When we started developing this application we chose a single-tenancy architecture. In practice, this means every endpoint on the left side of the diagram, and every subscription on the left side, is a unique CloudFormation stack containing the resources required to receive, validate, and forward events. Obviously, this means the environment has a large number of stacks and a significant amount of duplication.

## Single-tenancy pros

The main reason we chose a single-tenancy architecture is speed of development. Single-tenancy is inherently simpler to understand and maintain: you can look at a queue, function, or bucket and will know with 100% certainty that its responsibilities and scope cover a single tenant. There is no risk of these resources accidentally connecting to another tenant’s endpoints, accessing another tenant’s resources, or using another tenant’s configuration. Single-tenancy also allows us to avoid complex routing logic: if a resource receives an event, there is only one processing path. We do not need to build and maintain any conditional logic based on the sender / receiver and their permissions.

In fact, this allows us to create stateless resources which have been configured once, at deploy time. The configuration is immutable, and the resources have no external control plane dependencies. This is nicely visualized in the Lambda environment variables: every consumer can have a different BACKOFF_RATE, and it is simply baked into each single-tenanted stack.

The second reason we chose a single-tenant architecture is the small blast radius of deployments: we can update the application code for a single tenant and verify its behavior before moving on to the next. The risk of a “big bang” deployment bringing down all our tenants at once is thus greatly reduced. Additionally, a single misbehaving tenant is less likely to affect other tenants – single-tenancy minimizes the noisy neighbor problem.

## Single-tenancy cons

The single-tenancy approach allowed us to reach our (internal) market quickly. From there, we were able to quickly grow and adjust our roadmap based on our users’ requirements. However, we also ran into a number of constraints we needed to mitigate. These constraints can broadly be categorized into two buckets:

- The maximum number of resources in an AWS account
- The maximum number of concurrent operations on an AWS service
The maximum number of IAM roles was one of the first hard limits we ran into. No AWS account can have more than 5000 roles, and standard practice prescribes a unique role per resource (e.g. state machine / lambda function). At 560 stacks, this limits us to at most 8 IAM roles per stack. When we almost hit this limit, we had to consolidate some roles, at the cost of the principle of least privilege. Now, some Lambda functions share the same role and permissions, which sometimes means a function has access to a resource it doesn’t need.

The maximum number of concurrent operations is a trickier problem. When we have an application update, we verify the functionality on a small number of canary stacks. When they are healthy, we update the bulk of the other stacks in parallel. When we reached about 100 stacks, this led to a number of unexpected side effects. These included the maximum number of concurrent CodeBuild containers, maximum deploy rate of API Gateway, maximum number of concurrent stack operations on CloudFormation, and maximum number of control plane operations per second on Lambda.

The Lambda rate limit was especially nasty. We were able to update 100 CloudFormation stacks simultaneously, and each of those stacks had a number of Lambda functions. Updating them all at the same time crossed the maximum of 15 Lambda control plane requests per second, resulting in a CloudFormation UPDATE_FAILED status. CloudFormation would then enter rollback mode, but the rollback would also update Lambda functions, leading to additional rate limits, and finally an UPDATE_ROLLBACK_FAILED state. Anyone who has ever been there knows the pain.

In the end we were able to mitigate all these problems by limiting the concurrency of deployments to 50. To achieve this we use an outer and inner Step Functions state machine. The inner state machine performs the actual CDK deployment and all related actions. The outer state machine is triggered by external systems, and will first check the actual concurrency of the inner state machine. If it is above 50, it will backoff and retry until a slot is available.

While the concurrency limiter solved all rate limiting problems, it – obviously – slows down deployments. In practice, a large update might require 500 stacks to be deployed. The maximum concurrency is 50, so the deployment roughly takes 10 waves. Each of these waves takes up to five minutes, so a full redeployment can take up to almost an hour.

## The multi-tenancy solution

We know we have reached the ceiling of what a single-tenancy solution can support. The IAM roles are a clear example of a hard limit we cannot cross. Others are the maximum number of CloudFormation stacks, or the amount of CloudWatch alarms and metrics we are willing to pay for. If single-tenancy no longer suffices, multi-tenancy is the logical next step.

In this design, our customers no longer have dedicated infrastructure. Instead, a single ingress service is responsible for receiving all events, and a single egress service is responsible for forwarding all events.

The principal benefits of a multi-tenant solution are:

- Reduced amount of resources
- Reduced chance of hitting concurrency limits
- Increased deployment speed
However, it also introduces new challenges:

- The services can no longer be configured at deploy time. Instead they need to retrieve the latest configuration at runtime through a push or pull mechanism, and keep it in local state.
- The blast radius is significantly increased, for: 
- The complexity of the services, and thus the risk of bugs, increases.
## Everything is a trade-off

No article about architecture would be complete without talking about trade-offs, and this one is no exception. As we have learned above, there are pros and cons to both single and multi-tenant solutions. From a purely technical standpoint, multi-tenant systems are the preferred approach. They are scalable and have limited side-effects. In fact, every single AWS service is a multi-tenant solution – there is simply no other way to achieve the scales at which they operate.

But we’re not all AWS, and not every system needs to be designed for a million users. In our case, single-tenancy allowed us to achieve great isolation with minimal effort. Additionally, it significantly reduced our time to market and allowed us to find our product fit as soon as possible. It has brought us where we are, and now it’s time to evolve to the next phase.

This chart shows the (unscientific) relationship between single-tenancy and multi-tenancy. It visualizes the trade-offs that come with choosing either end of the spectrum, and everything in between. Only you can decide where on this diagram your application belongs. If you know the number of tenants will always be limited, you might stay on the left. If you’re expecting many tenants in a short amount of time, move to the right.

## The choice is not binary

In this article we have posited single-tenant architecture against multi-tenant architecture. These are the two extremes on the spectrum: every tenant has their own infrastructure on one end, while all infrastructure is shared on the other end. As we have covered, both ends have pros and cons. The most significant downside of multi-tenant solutions is the potential broad impact of incidents.

Luckily, there are also solutions in the middle of the spectrum. These architectures balance the scalability of multi-tenant system with the isolation associated with single-tenant systems. Examples include regional, zonal, tiered, or cell-based architectures. All these solutions follow the same basic approach; they take a large, multi-tenanted system and divide it up into smaller chunks. These chunks can still be very large, such as two entirely separate regions, or very small, such as a given rack or even physical server in a datacenter. Regardless of size, each of these smaller chunks still needs to be a multi-tenant system, with well-implemented isolation and consistency measures.

In case of the EBE, we’re considering a tiered architecture: Tier 3 are internal tenants, purely intended for testing and validation. Tier 2 contains non-mission critical tenants, and Tier 1 includes mission-critical production workloads. Each of these tiers is a multi-tenant service covering multiple, widely varied tenant configurations. Any deployment will cover the higher tier first, and only when they have proven to be stable is the deployment promoted to the next tier. The result is a much smaller blast radius and much better isolation, at the cost of slightly more resources and slower deployment times.

## Conclusion

In this article we have covered the pros and cons of single-tenant and multi-tenant solutions. We have seen how single-tenancy is a good option to get started quickly, but has a clear and solid growth ceiling. Single-tenancy might be a good long-term solution if you know you only need to handle a limited number of customers.

Multi-tenant architectures are the preferred solution for services which require unbounded scale. Multi-tenancy is the only way to serve a large number of customers within the resource limits set by your cloud provider. However, multi-tenant systems are inherently more complex, which affects speed of development and operational overhead. They also increase the potential blast radius of incidents.

The blast radius can be reduced by applying a zonal or cellular design to your multi-tenanted systems. This will limit the impact of incidents and will allow your developers to detect issues before they hit your most critical systems. However, it also adds additional complexity, and reduces some of the benefits gained from multi-tenancy.

In the end, which solution fits your application best fully depends on your business context, the stage in your application’s lifecycle, and the priorities set by your stakeholders. I hope this article will help you make an informed decision.


