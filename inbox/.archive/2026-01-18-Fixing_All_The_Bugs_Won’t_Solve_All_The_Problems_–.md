---
type: link
source: notion
url: https://shermanonsoftware.com/2024/04/08/fixing-all-the-bugs-wont-solve-all-the-problems-demings-path-of-frustration/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-04-12T03:06:00.000Z
---

# Fixing All The Bugs Won’t Solve All The Problems – Deming’s Path Of Frustration – Sherman On Software

## AI Summary (from Notion)
- Key Distinction: Problems in software can be categorized as bugs (special causes) or systemic issues (common causes).
- Bugs vs. Common Causes: Fixing bugs improves software quality, but does not address underlying common cause issues.
- Common Cause Issues Identified:
- Cloud-based software often resides in a single data center, causing latency for global users.
- Underprovisioned hardware leads to slow performance.
- Excessive unnecessary data transmission affects software speed.
- Inefficient data access patterns contribute to performance degradation.
- Main Takeaway: To truly enhance software quality, it is crucial to address both bugs and systemic design issues with equal urgency.
- Frustration Path: Deming’s Path of Frustration suggests a focus on system design and implementation to mitigate common cause issues.

## Content (from Notion)

> 

In software, as in manufacturing, some problems occur due to bugs or “special causes”, and some are “common cause” due to the nature of the system’s design and implementation. Fixing bugs is removing special causes. Removing bugs greatly improves software quality, but it won’t impact “common cause” issues.

Some “common cause” software performance issues I have encountered:

- The software is “in the cloud”, but really it is in one data center in the US. As a result the software is slow and laggy for customers in Europe and Asia.
- The software runs slowly because the hardware is underprovisioned.
- The software runs slowly because large amounts of unnecessary data are being sent to the users.
- The software runs slowly because of inefficient data access patterns.
Even with no bugs, “common cause” issues can result in low quality software.

The way off of Deming’s Path Of Frustration is to attack system design and implementation issues with the same fervor used to fight bugs.


