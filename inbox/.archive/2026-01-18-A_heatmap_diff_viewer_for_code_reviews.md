---
type: link
source: notion
url: https://0github.com/
notion_type: Software Repo
tags: ['Running']
created: 2025-10-30T18:32:00.000Z
---

# A heatmap diff viewer for code reviews

## Overview (from Notion)
- The heatmap diff viewer can significantly streamline your code review process, allowing you to focus on the most critical changes.
- It can help you teach your children about coding, making it a fun way to engage with their interests in technology.
- As a founder, adopting cutting-edge tools like this can enhance your team's productivity and foster a culture of innovation.
- The emphasis on identifying "what's worth a second look" encourages a more thoughtful approach to code quality, which can lead to better products.
- Consider how this tool can be integrated into your daily workflow to reduce stress and free up time for family activities.
- Alternate views might focus on the potential over-reliance on automated tools, emphasizing the need for human intuition in code reviews.

## AI Summary (from Notion)
A heatmap tool color-codes code diffs based on the attention they require, flagging issues beyond just bugs, such as hard-coded secrets or complex logic. It uses a VM and GPT-5 Codex to generate a JSON structure for visualization. The tool is open source and can be tested by modifying GitHub URLs.

## Content (from Notion)

← Back to cmux

Heatmap color-codes every diff line/token by how much human attention it probably needs. Unlike PR-review bots, we try to flag not just by “is it a bug?” but by “is it worth a second look?” (examples: hard-coded secret, weird crypto mode, gnarly logic).

To try it, replace github.com with 0github.com in any GitHub pull request url. Under the hood, we clone the repo into a VM, spin up gpt-5-codex for every diff, and ask it to output a JSON data structure that we parse into a colored heatmap.

Heatmap is open source:

Heatmap diff viewer example showing color-coded code changes


