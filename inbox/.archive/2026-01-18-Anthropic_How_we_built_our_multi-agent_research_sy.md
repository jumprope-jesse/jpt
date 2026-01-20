---
type: link
source: notion
url: https://simonwillison.net/2025/Jun/14/multi-agent-research-system/
notion_type: Software Repo
tags: ['Running']
created: 2025-06-18T14:46:00.000Z
---

# Anthropic: How we built our multi-agent research system

## Overview (from Notion)
- Multi-agent systems can enhance productivity by enabling parallel processing of tasks, which could streamline your workflow as a software engineer and company founder.
- The ability to break down complex queries into subtasks allows for more efficient research and development, potentially saving time on projects.
- The insights on token management and resource optimization could influence how you approach software architecture, especially in resource-constrained environments.
- Consider the balance between the efficiency of multi-agent systems and the increased token costs; this could affect budgeting for cloud resources in your startup.
- The article highlights the importance of prompt engineering, which could inspire you to refine your coding practices and improve your team's output.
- It presents an innovative perspective on how to leverage AI tools, which may be applicable to both your personal projects and family life, such as automating mundane tasks at home.
- An alternate view might question the practicality of implementing such systems in everyday scenarios, suggesting that simpler solutions could suffice for many tasks.

## AI Summary (from Notion)
Anthropic's multi-agent research system utilizes multiple agents to enhance research efficiency by operating in parallel, allowing for broader exploration of queries. The system has shown a significant performance improvement over single-agent systems, particularly for complex tasks, despite the higher token usage. Key strategies include effective prompt engineering, memory management, and parallelization techniques, which collectively reduce research time and improve the quality of information retrieved.

## Content (from Notion)

. OK, I'm sold on multi-agent LLM systems now.

I've been pretty skeptical of these until recently: why make your life more complicated by running multiple different prompts in parallel when you can usually get something useful done with a single, carefully-crafted prompt against a frontier model?

This detailed description from Anthropic about how they engineered their "Claude Research" tool has cured me of that skepticism.

Reverse engineering Claude Code had already shown me a mechanism where certain coding research tasks were passed off to a "sub-agent" using a tool call. This new article describes a more sophisticated approach.

They start strong by proving a clear definition of how they'll be using the term "agent" here:

> 

Why use multiple agents for a research system?

> 

As anyone who has spent time with Claude Code will already have noticed, the downside of this architecture is that it can burn a lot more tokens:

> 

The key benefit is all about managing that 200,000 token context limit. Each sub-task has its own separate context, allowing much larger volumes of content to be processed as part of the research task.

Providing a "memory" mechanism is important as well:

> 

The rest of the article provides a detailed description of the prompt engineering process needed to build a truly effective system:

> 

They got good results from having special agents help optimize those crucial tool descriptions:

> 

Sub-agents can run in parallel which provides significant performance boosts:

> 

There also an extensive section about their approach to evals - they found that LLM-as-a-judge worked well for them, but human evaluation was essential as well:

> 

There's so much useful, actionable advice in this piece. I haven't seen anything else about multi-agent system design that's anywhere near this practical.

They even added some example prompts from their Research system to their open source prompting cookbook. Here's the bit that encourages parallel tool use:

> 

And an interesting description of the OODA research loop used by the sub-agents:

> 

## Recent articles

- Design Patterns for Securing LLM Agents against Prompt Injections - 13th June 2025
- Comma v0.1 1T and 2T - 7B LLMs trained on openly licensed text - 7th June 2025
- The last six months in LLMs, illustrated by pelicans on bicycles - 6th June 2025
ai-assisted-search 27   anthropic 155   claude 166   evals 26   ai-agents 49   llm-tool-use 46   ai 1363   llms 1169   prompt-engineering 144   generative-ai 1188   paper-review 9 

### Monthly briefing

Sponsor me for $10/month and get a curated email digest of the month's most important LLM developments.

Pay me to send you less!

Sponsor & subscribe 


