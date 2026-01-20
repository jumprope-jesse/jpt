# AWS Lambda: History and Original PR/FAQ

## Overview
In November 2024, AWS Lambda celebrated its 10th anniversary. Werner Vogels shared the original PR/FAQ document that launched the service, providing a rare look at Amazon's product development process and the evolution of serverless computing.

Source: [All Things Distributed - AWS Lambda turns 10](https://www.allthingsdistributed.com/2024/11/aws-lambda-turns-10-a-rare-look-at-the-doc-that-started-it.html)

## The Origin Story
Lambda was born from observing customer behavior: entire EC2 fleets sitting idle, waiting to run simple functions like writing to a database or processing a file. AWS challenged themselves to build a service that eliminated this inefficiency.

## Amazon's Documentation Culture
Key insight: Writing forces clarity. At Amazon, anyone with a good idea is expected to put pen to paper:
- One-pagers, two-pagers, six-pagers, PR/FAQs
- Writing forces the author to be clear, precise, and detailed
- "A good idea backed by a crisp doc has proven it can produce wonderful products"
- No one gets it right the first time - iteration is expected

## Lambda's Evolution Timeline

### Billing Granularity
- Original goal: 250ms billing increments
- Launch (2014): 100ms increments
- Today: 1ms billing with no minimums

### Runtime Support
- Nov 2014: Node.js only (strategic choice to validate programming model)
- June 2015: Java
- Oct 2015: Python
- Dec 2016: .NET
- Jan 2018: Go
- Nov 2018: Ruby + Custom Runtimes

### Key Feature Milestones
- 2018: Lambda Layers for reusable code/libraries
- 2020: Container support (up to 10GB images)
- 2020: SAM CLI for local development
- 2022: SnapStart (90% cold start reduction for Java)

## Original Lambda Tenets
1. **Security without complexity** - Protect customer data, up-to-date patches without action
2. **Simple and easy** - "NoOps" service, reasonable defaults, few options
3. **Scales up and down (to zero)** - No code changes needed, 1/month to 1000/sec both supported
4. **Cost effective at any scale** - Fine-grained pay-for-use, no idle charges
5. **AWS integration** - Easy access to other AWS services
6. **Reliable** - Predictable operational performance, resilience to failure

## Security Philosophy
When Lambda launched, security was non-negotiable even with trade-offs:
- Initially used single-tenant EC2 instances (expensive but secure)
- No two customers shared an instance
- Later, Firecracker microVMs enabled packing thousands of secure microVMs on single bare metal instances

Jeff Bezos quote from article: "If you're going to do anything new or innovative, you have to be willing to be misunderstood."

## Unexpected Innovation
Marc Brooker insight: Customers consistently come up with unexpected use cases that weren't in any PR/FAQ. This drives innovation as engineers work to enable these patterns.

## Technical References
- [Marc Brooker's USENIX ATC '23 talk on on-demand container loading](https://www.usenix.org/conference/atc23)
- AWS Developer Podcast episode on Lambda evolution
