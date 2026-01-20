---
type: link
source: notion
url: https://news.ycombinator.com/item?id=45054040
notion_type: Tech Announcement
tags: ['Running']
created: 2025-08-29T04:23:00.000Z
---

# Launch HN: Dedalus Labs (YC S25) – Vercel for Agents | Hacker News

## Overview (from Notion)
- Dedalus Labs offers a cloud platform simplifying the integration of AI applications, potentially making your work as a software engineer more efficient.
- The SDK allows seamless connection of LLMs to tools without complex setups, which could save you significant time when developing projects or working on startup ideas.
- The focus on streamlining API interactions aligns with the growing trend of low-code/no-code solutions, which could inspire you to think about how to make your own projects more accessible.
- The community aspect, encouraging feedback on barriers to integration, fosters collaboration, which could be valuable in your network.
- As a company founder, the potential for monetizing tools through an MCP marketplace could present new business opportunities and revenue streams.
- An alternate view could be skepticism about the security and reliability of cloud-based solutions, especially regarding the management of authentication and resource access.
- Consider how the evolving landscape of AI tools can impact your parenting—understanding these technologies can shape how you educate your children about their future in a tech-driven world.

## AI Summary (from Notion)
Dedalus Labs offers a cloud platform for building agentic AI applications, simplifying the integration of LLMs with MCP tools through a single API endpoint. The platform allows for quick setup and deployment of streamable HTTP MCP servers, enabling developers to use powerful tools for function calling without extensive configuration. Future plans include launching an authentication solution and an MCP marketplace for monetizing tools. Feedback on barriers to integrating MCP servers is welcomed.

## Content (from Notion)

Hey HN! We are Windsor and Cathy of Dedalus Labs (https://www.dedaluslabs.ai/), a cloud platform for developers to build agentic AI applications. Our SDK allows you to connect any LLM to any MCP tools – local or hosted by us. No Dockerfiles or YAML configs required.

Here’s a demo: https://youtu.be/s2khf1Monho?si=yiWnZh5OP4HQcAwL&t=11

Last October, I was trying to build a stateful code execution sandbox in the cloud that LLMs could tool-call into. This was before MCP was released, and let’s just say it was super annoying to build… I was thinking to myself the entire time “Why can’t I just pass in `tools=code_execution` to the model and just have it…work?

Even with MCP, you’re stuck running local servers and handwiring API auth and formatting across OpenAI, Anthropic, Google, etc. before you can ship anything. Every change means redeploys, networking configs, and hours lost wrangling AWS. Hours of reading docs and wrestling with cloud setup is not what you want when building your product!

Dedalus simplifies this to just one API endpoint, so what used to take 2 weeks of setup can take 5 minutes. We allow you to upload streamable HTTP MCP servers to our platform. Once deployed, we offer OpenAI-compatible SDKs that you can drop into your codebase to use MCP-powered LLMs. The idea is to let anyone, anywhere, equip their LLMs with powerful tools for function calling.

The code you write looks something like this:

```plain text
  python
  client = Dedalus()
  runner = DedalusRunner(client)

  result = runner.run(
    input=prompt,
    tools=[tool_1, tool_2],
    mcp_servers=["author/server-1”, “author/server-2”],
    model=["openai/gpt-4.1”, “anthropic/claude-sonnet-4-20250514”],  # Defaults to first model in list
    stream=True,
  )
  stream_sync(result)  # Streams result, supports tool calling too

```

Our docs start at https://docs.dedaluslabs.ai. Here’s a simple Hello World example: https://docs.dedaluslabs.ai/examples/01-hello-world. For basic tool execution, see https://docs.dedaluslabs.ai/examples/02-basic-tools. There are lots more examples on the site, including more complex ones like using the Open Meteo MCP to do weather forecasts: https://docs.dedaluslabs.ai/examples/use-case/weather-foreca....

There are still a bunch of issues in the MCP landscape, no doubt. One big one is authentication (we joke that the “S” in MCP stands for “security”). MCP servers right now are expected to act as both the authentication server and the resource server. That is too much to ask of server writers. People just want to expose a resource endpoint and be done.

Still, we are bullish on MCP. Current shortcomings are not irrecoverable, and we expect future amendments to resolve them. We think that useful AI agents are bound to be habitual tool callers, and MCP is a pretty decent way to equip models with tools.

We aren’t quite yet at the stateful code execution sandbox that I wanted last October, but we’re getting there! Shipping secure and stateful MCP servers is high on our priority list, and we’ll be launching our auth solution next month. We’re also working on an MCP marketplace, so people can monetize their tools, while we handle billing and rev-share.

We’re big on open sourcing things and have these SDKs so far (MIT licensed):

https://github.com/dedalus-labs/dedalus-sdk-python

https://github.com/dedalus-labs/dedalus-sdk-typescript

https://github.com/dedalus-labs/dedalus-sdk-go

https://github.com/dedalus-labs/dedalus-openapi

We would love feedback on what you guys think are the biggest barriers that keep you from integrating MCP servers or using tool calling LLMs into your current workflow.

Thanks HN!


