---
type: link
source: notion
url: https://www.reddit.com/r/aws/comments/1ayr108/combining_aurora_serverless_v2_with_reserved/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-02-24T11:37:00.000Z
---

# Combining Aurora Serverless v2 with Reserved Instances : r/aws

## AI Summary (from Notion)
- Topic: Exploring the combination of Aurora Serverless v2 with Reserved Instances (RIs) to manage database performance and costs.

- Current Setup:
- Uses r7g.large instances in major regions for Aurora databases.
- Standard performance is reliable (99.9% of the time), but spikes in usage occur daily, causing performance issues.

- Proposed Idea:
- Investigating the use of Aurora Serverless v2 as a supplementary reader alongside RIs to handle traffic spikes.

- Key Questions:
- Cost Efficiency: Can RIs reduce costs for baseline usage while Aurora Serverless v2 manages spikes?
- RDS Proxy Functionality: Is RDS Proxy capable of intelligently directing spiky traffic to the serverless option?
- APU Configuration: Should the minimum APU setting match the database's memory needs or can it remain low for autoscaling?
- Potential Issues: What other considerations should be taken into account with this setup?

- Additional Inquiry:
- Questions regarding the usefulness of having an AWS support contract for addressing such inquiries compared to emergency support.

## Content (from Notion)

Hey everyone, I'd like to validate an approach before diving a rabbit hole of setup:

- 
- 
- 
So the core assumption I'm looking to validate: can I use RIs to cut costs for our baseline usage and use Aurora Serverless v2 to sit on standby to handle spikiness? I realise there might be an obvious answer based on my last bullet point above, but every blog post I'm reading always compares the two services as an either/or option, and typically concludes that Aurora Serverless v2 ends up simply being more expensive because it doesn't make sense for baseline usage. I haven't found any posts of people talking about this setup.

Follow on questions that I'm also not getting clear answers on:

- 
- 
- 
Final more unrelated question:

- 

