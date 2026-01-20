---
type: link
source: notion
url: https://aws.amazon.com/about-aws/whats-new/2025/09/aws-x-ray-adaptive-sampling-automatic-error/
notion_type: Software Repo
tags: ['Running']
created: 2025-09-27T07:34:00.000Z
---

# AWS X-Ray introduces Adaptive Sampling for automatic optimized error detection - AWS

## Overview (from Notion)
- AWS X-Ray's adaptive sampling can help streamline your software development processes, allowing for quicker debugging and error detection, which is crucial for maintaining work-life balance.
- The ability to automatically adjust sampling rates means less manual oversight and potentially more time for family activities while ensuring your applications run smoothly.
- Implementing efficient error detection can lead to improved application performance, which can be a selling point for your company and enhance customer satisfaction.
- Consider how this technology could simplify your workflows, reducing the stress of managing software reliability in a bustling city environment.
- An alternate viewpoint could be the potential over-reliance on automated systems; maintaining a balance between automation and human insight is essential in a rapidly evolving tech landscape.
- Emphasize the importance of continuous learning; staying updated with tools like AWS X-Ray can give you a competitive edge as a founder in the tech industry.

## AI Summary (from Notion)
AWS X-Ray now features adaptive sampling, allowing automatic adjustment of sampling rates to capture critical traces during incidents while maintaining cost efficiency during normal operations. This includes two methods: Sampling Boost, which increases rates during anomalies, and Anomaly Span Capture, ensuring important spans are always captured. Adaptive sampling is available in all commercial regions where AWS X-Ray operates.

## Content (from Notion)

AWS X-Ray, a service that helps developers analyze and debug distributed applications by providing request tracing capabilities, now offers adaptive sampling to solve a common challenge for DevOps teams, Site Reliability Engineers (SREs), and application developers. These customers often face a difficult trade-off: setting sampling rates too low risks missing critical traces during incidents, while setting them too high unnecessarily increases observability costs during normal operations.

Today, with adaptive sampling, you can automatically adjust sampling rates within user-defined limits to ensure you capture the most important traces precisely when you need them. This helps development teams reduce mean time to resolution (MTTR) during incidents by providing comprehensive trace data for root cause analysis, while maintaining cost-efficient sampling rates during normal operations. Adaptive sampling supports two approaches, Sampling Boost and Anomaly Span Capture. These can be applied independently or can be combined together. Customers can use Sampling Boost to temporarily increase sampling rates when anomalies are detected to capture complete traces and Anomaly Span Capture to ensures anomaly-related spans are always captured, even when the full trace isn't sampled.

Adaptive sampling is currently available in all commercial regions where AWS X-Ray is offered. For more information, see the X-Ray documentation. and CloudWatch pricing page for X-ray pricing details.


