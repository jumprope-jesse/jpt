---
type: link
source: notion
url: https://www.reddit.com/r/aws/comments/1ay4025/aws_management_break_glass_procedure/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-02-24T06:02:00.000Z
---

# AWS Management & "Break glass procedure" : r/aws

## Overview (from Notion)
- Managing AWS infrastructure solo can lead to significant stress, especially when downtime could impact your customers and business reputation.
- Consider the value of delegating some responsibilities to an AWS management service—frees up time for family and strategic planning.
- Implementing an SNS topic for downtime notifications could help you stay proactive, allowing you to focus on family while ensuring the business runs smoothly.
- Explore community resources or local meetups in NYC for networking—connecting with other founders could provide insights and support.
- Think about the balance between work and family life—how can better infrastructure management lead to more quality time with loved ones?
- Alternate view: Some may argue that outsourcing management could lead to loss of control; weigh the risks versus benefits carefully.

## AI Summary (from Notion)
A solo DevOps at a small B2C startup is seeking recommendations for agencies or services that can manage AWS in emergencies, particularly for troubleshooting and rebooting servers. They experienced a near downtime incident and want to set up an SNS topic for notifications about outages.

## Content (from Notion)

I'm a solo DevOps of a very small B2C startup. We have around 10000 customers, and I am the only person 'owning' our cloud infrastructure (on AWS). Our team is under 5 people, and our infrastructure is pretty simple so that's why it's just me.

We had an incident a while back which I caught just before I went to sleep. If it had happened 10 minutes later, we could've had 10-12 hours of downtime.

If this happened, or I was unreachable for some other reason, does anyone know any agencies / services that provide an AWS management option where they can be contacted in an emergency and granted access and do basic troubleshooting like rebooting a server etc?

Bonus points if we can set up an SNS topic that notifies them of downtime.

Any advice would be really appreciated.


