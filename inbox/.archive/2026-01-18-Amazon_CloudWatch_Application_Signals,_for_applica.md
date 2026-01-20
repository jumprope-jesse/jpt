---
type: link
source: notion
url: https://aws.amazon.com/about-aws/whats-new/2024/06/amazon-cloudwatch-application-signals-application-monitoring/
notion_type: Tech Announcement
tags: ['Running']
created: 2024-06-11T03:19:00.000Z
---

# Amazon CloudWatch Application Signals, for application monitoring (APM) is generally available - AWS

## AI Summary (from Notion)
- Announcement: AWS has launched Amazon CloudWatch Application Signals, now generally available for application performance monitoring (APM).
- Integration: Compatible with OpenTelemetry (OTeL), allowing for automatic instrumentation and tracking of application performance.
- Dashboard Features: Provides a pre-built, standardized dashboard highlighting key metrics such as volume, availability, latency, faults, and errors.
- Troubleshooting: Correlates telemetry across metrics, traces, logs, real-user monitoring, and synthetic monitoring to enhance troubleshooting and minimize disruptions.
- Use Case: Example of a payment processing application where developers can identify latency spikes and their causes.
- Container Insights: Integration with Container Insights helps identify root causes like memory shortages or high CPU usage.
- Availability: Available in 28 AWS commercial regions, excluding specific regions like CA West, AWS GovCloud, and China.
- Pricing Information: Pricing details are available on the Amazon CloudWatch pricing page.
- Workshops and Documentation: Offers resources like the AWS One Observability Workshop and documentation for enabling Application Signals across various platforms (Amazon EKS, Amazon EC2, etc.).

## Content (from Notion)

Today, AWS announces the general availability of Amazon CloudWatch Application Signals, an OpenTelemetry (OTeL) compatible application performance monitoring (APM) feature in CloudWatch, that makes it easy to automatically instrument and track application performance against their most important business or service level objectives (SLOs) for applications on AWS. With no manual effort, no custom code, and no custom dashboards, Application Signals provides service operators with a pre-built, standardized dashboard showing the most important metrics for application performance – volume, availability, latency, faults, and errors – for each of their applications on AWS.

By correlating telemetry across metrics, traces, logs, real-user monitoring, and synthetic monitoring, Application Signals enables customers to speed up troubleshooting and reduce application disruption. For example, an application developer operating a payment processing application can see if payment processing latency is spiking and drill into the precisely correlated trace contributing to the spike to establish cause in application code or dependency. Developers that use Container Insights to monitor container infrastructure, can further identify root cause such as a memory shortage or a high CPU utilization on the container pod running the application code causing the spike.

Application Signals is generally available in 28 commercial AWS Regions, except CA West (Calgary) Region, AWS GovCloud (US) Regions and China Regions. For pricing, see Amazon CloudWatch pricing.

Try Application Signals with the AWS One Observability Workshop sample application. To learn more, see documentation to enable Amazon CloudWatch Application Signals for Amazon EKS, Amazon EC2, native Kubernetes and custom instrumentation for other platforms.


