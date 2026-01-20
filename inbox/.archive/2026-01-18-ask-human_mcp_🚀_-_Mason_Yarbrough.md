---
type: link
source: notion
url: https://masonyarbrough.com/blog/ask-human
notion_type: Software Repo
tags: ['Running']
created: 2025-06-05T23:50:00.000Z
---

# ask-human mcp 🚀 - Mason Yarbrough

## Overview (from Notion)
- The "ask-human mcp" tool addresses common frustrations with AI, particularly for software engineers dealing with unreliable outputs, which can resonate with your experiences in coding and debugging.
- It allows for a smoother workflow by enabling AI to ask for help instead of making erroneous assumptions, potentially saving you time and reducing frustration.
- As a founder, using such tools could enhance team productivity and foster a culture of collaboration, where even AI can seek guidance.
- The zero-config, cross-platform nature of the tool makes it accessible and easy to implement, fitting well into your busy lifestyle.
- The history tracking feature is beneficial for debugging, ensuring accountability and clarity in your projects, which is crucial when leading a team.
- Consider the implications of AI seeking help: it might change the way we perceive AI's role in problem-solving—less of a "fully autonomous" entity and more of a collaborative assistant.
- Lastly, think about how this could influence mentorship in tech: encouraging a mindset where asking questions is valued, even for AI, promotes a learning environment.

## AI Summary (from Notion)
A new tool, ask-human mcp, helps AI avoid hallucinations by allowing it to ask questions instead of making incorrect assumptions. It features easy installation, zero configuration, and provides instant feedback while maintaining a history of Q&A for debugging. The setup is quick and supports multiple agents.

## Content (from Notion)

I just shipped a tiny thing that keeps your ai from hallucinating and gives it an escape route when confused or issues arise

I built this while solo-founding  Kallro to help with a lot of the issues i've found using cursor.

## the pain:

ai blurts out an endpoint that never existed

the agent makes assumptions that are simply not true and has false confidence

repeat x100 errors and your day is spent debugging false confidence and issues when I simply could ask you a question

## the fix — ask-human mcp:

an mcp server that lets the agent raise its hand instead of hallucinating. feels like mentoring a sharp intern who actually asks before guessing.

```plain text
agent → ask_human()
⬇
question lands in ask_human.md
⬇
you swap "PENDING" for the answer
⬇
agent keeps coding

```

sample file:

you drop:

```plain text
answer: POST /api/v2/auth/login

```

boom flow continues and hopefully the issues are solved

## why it's good:

- pip install ask-human-mcp → done
- zero config, cross-platform
- watches the file, instant feedback
- multiple agents, no sweat
- locks + limits so nothing catches fire
- full q&a history in markdown (nice paper-trail for debugging)
## 30-sec setup:

```plain text
pip install ask-human-mcp
ask-human-mcp --help

```

.cursor/mcp.json:

```plain text
{
  "mcpServers": {
    "ask-human": { "command": "ask-human-mcp" }
  }
}

```

restart cursor and vibe


