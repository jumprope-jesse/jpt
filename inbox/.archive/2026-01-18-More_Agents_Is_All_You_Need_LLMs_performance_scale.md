---
type: link
source: notion
url: https://news.ycombinator.com/item?id=39955725
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-04-07T02:23:00.000Z
---

# More Agents Is All You Need: LLMs performance scales with the number of agents | Hacker News

## AI Summary (from Notion)
- The paper challenges the effectiveness of multi-agent setups like Chain-of-thought and LLM-Debate.
- It proposes an alternative method of running the same query multiple times on a single LLM without shared context.
- A similarity algorithm is used to analyze the answers and select the most common response.
- The proposed method performs comparably or even better than traditional multi-agent algorithms.
- The findings suggest that improvements in multi-agent schemes may primarily stem from repeated queries rather than clever prompting techniques.
- The text emphasizes the distinction between "hallucinations" and correct answers, with correct answers showing more consistency.

## Content (from Notion)

I'm not sure people in these comments are reading this paper correctly.

This seems to essentially disprove the whole idea of multi-agent setups like Chain-of-thought and LLM-Debate.

Because this paper introduces their alternative method which simply runs the same query multiple times on the same LLM, without any context shared across queries. And then they run a similarity algorithm on the answers and pick the most common answer. (Which makes sense to me. If an LLM is giving you a mixture of "hallucinations" and correct answers, the correct answers will similar and the hallucinations will be chaotic)

And this simple algorithm preform just as well (and sometimes better) than all the other multi-agent algorithms.

This suggests that the other multi-agent schemes with their clever prompts aren't really doing anything special; Their improve results are coming mostly from the fact that the LLM is run multiple times, that the prompt asks the LLM to pick the best answer.


