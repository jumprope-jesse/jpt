---
type: link
source: notion
url: https://applied-llms.org/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-06-02T02:57:00.000Z
---

# Applied LLMs - What We’ve Learned From A Year of Building with LLMs

## AI Summary (from Notion)
- Overview of LLMs: Large language models (LLMs) have become practical for real-world applications, improving in quality and decreasing in cost.
- Investment in AI: An estimated $200B investment in AI is projected by 2025, driven by increased accessibility and demonstrations on social media.
- Challenges: Despite easier access to LLMs, creating effective products remains challenging beyond simple demonstrations.
- Learning Experience: The authors share insights from a year of building with LLMs, highlighting the importance of learning from mistakes.
- Sections of Guidance:
- Tactical: Practical tips for prompting, RAG, flow engineering, evaluations, and monitoring for practitioners and hobbyists.
- Operational: Focus on day-to-day organizational concerns and building effective teams for product leaders.
- Strategic: Long-term perspectives, emphasizing “no GPU before PMF” and “focus on the system not the model” for founders and executives.
- Goal: The intent is to provide a practical guide for building successful LLM products based on experiences and industry examples.

## Content (from Notion)

It’s an exciting time to build with large language models (LLMs). Over the past year, LLMs have become “good enough” for real-world applications. And they’re getting better and cheaper every year. Coupled with a parade of demos on social media, there will be an estimated $200B investment in AI by 2025. Furthermore, provider APIs have made LLMs more accessible, allowing everyone, not just ML engineers and scientists, to build intelligence into their products. Nonetheless, while the barrier to entry for building with AI has been lowered, creating products and systems that are effective—beyond a demo—remains deceptively difficult.

We’ve spent the past year building, and have discovered many sharp edges along the way. While we don’t claim to speak for the entire industry, we’d like to share what we’ve learned to help you avoid our mistakes and iterate faster. These are organized into three sections:

- Tactical: Some practices for prompting, RAG, flow engineering, evals, and monitoring. Whether you’re a practitioner building with LLMs, or hacking on weekend projects, this section was written for you.
- Operational: The organizational, day-to-day concerns of shipping products, and how to build an effective team. For product/technical leaders looking to deploy sustainably and reliably.
- Strategic: The long-term, big-picture view, with opinionated takes such as “no GPU before PMF” and “focus on the system not the model”, and how to iterate. Written with founders and executives in mind.
Our intent is to make this a practical guide to building successful products with LLMs, drawing from our own experiences and pointing to examples from around the industry.

Ready to delve dive in? Let’s go.

Shankar, S., et al. (2024). Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human Preferences. Retrieved from https://arxiv.org/abs/2404.12272


