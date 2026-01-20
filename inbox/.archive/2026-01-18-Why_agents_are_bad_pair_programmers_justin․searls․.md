---
type: link
source: notion
url: https://justin.searls.co/posts/why-agents-are-bad-pair-programmers/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2025-06-10T13:27:00.000Z
---

# Why agents are bad pair programmers | justin․searls․co

## Overview (from Notion)
- The article discusses how LLM (Large Language Model) agents can be less effective as pair programmers because they operate at a speed that outpaces human comprehension, leading to disengagement and miscommunication.
- It highlights the nostalgia for effective human pair programming experiences, contrasting it with the challenges posed by AI agents who may not facilitate a collaborative environment.
- Ideas such as asynchronous workflows, throttling down to turn-based editing, and improving AI interaction to be more human-like could resonate with your experiences in managing teams and projects.
- As a software engineer and founder, consider the implications of AI tools in your own coding practices and team dynamics. You might find value in advocating for AI tools that prioritize collaboration over speed.
- Unique viewpoints include the need for AI to adapt its approach to enhance human-AI interactions, suggesting that developers should design features that mimic human-like behaviors in coding sessions.
- Alternate views might argue that AI's speed is a significant advantage, and that humans should adapt to keep up, rather than expect AI to slow down. However, this could lead to burnout and inefficiency in team settings.

## AI Summary (from Notion)
LLM agents can hinder pair programming due to their speed, which often outpaces human comprehension, leading to disengagement and miscommunication. Instead of relying on agentic pairing, it's suggested to break tasks into smaller components for independent work and review, or to use slower, more collaborative modes of interaction. Features that promote a more human-like collaboration, such as adjustable output speed and opportunities for discussion, could enhance the effectiveness of AI agents in pair programming scenarios.

## Content (from Notion)

LLM agents make bad pairs because they code faster than humans think.

I'll admit, I've had a lot of fun using GitHub Copilot's agent mode in VS Code this month. It's invigorating to watch it effortlessly write a working method on the first try. It's a relief when the agent unblocks me by reaching for a framework API I didn't even know existed. It's motivating to pair with someone even more tirelessly committed to my goal than I am.

In fact, pairing with top LLMs evokes many memories of pairing with top human programmers.

The worst memories.

Memories of my pair grabbing the keyboard and—in total and unhelpful silence—hammering out code faster than I could ever hope to read it. Memories of slowly, inevitably becoming disengaged after expending all my mental energy in a futile attempt to keep up. Memories of my pair hitting a roadblock and finally looking to me for help, only to catch me off guard and without a clue as to what had been going on in the preceding minutes, hours, or days. Memories of gradually realizing my pair had been building the wrong thing all along and then suddenly realizing the task now fell to me to remediate a boatload of incidental complexity in order to hit a deadline.

So yes, pairing with an AI agent can be uncannily similar to pairing with an expert programmer.

## The path forward

What should we do instead? Two things:

1. The same thing I did with human pair programmers who wanted to take the ball and run with it: I let them have it. In a perfect world, pairing might lead to a better solution, but there's no point in forcing it when both parties aren't bought in. Instead, I'd break the work down into discrete sub-components for my colleague to build independently. I would then review those pieces as pull requests. Translating that advice to LLM-based tools: give up on editor-based agentic pairing in favor of asynchronous workflows like GitHub's new Coding Agent, whose work you can also review via pull request
1. Continue to practice pair-programming with your editor, but throttle down from the semi-autonomous "Agent" mode to the turn-based "Edit" or "Ask" modes. You'll go slower, and that's the point. Also, just like pairing with humans, try to establish a rigorously consistent workflow as opposed to only reaching for AI to troubleshoot. I've found that ping-pong pairing with an AI in Edit mode (where the LLM can propose individual edits but you must manually accept them) strikes the best balance between accelerated productivity and continuous quality control
Give people a few more months with agents and I think (hope) others will arrive at similar conclusions about their suitability as pair programmers. My advice to the AI tool-makers would be to introduce features to make pairing with an AI agent more qualitatively similar to pairing with a human. Agentic pair programmers are not inherently bad, but their lightning-fast speed has the unintended consequence of undercutting any opportunity for collaborating with us mere mortals. If an agent were designed to type at a slower pace, pause and discuss periodically, and frankly expect more of us as equal partners, that could make for a hell of a product offering.

Just imagining it now, any of these features would make agent-based pairing much more effective:

- Let users set how many lines-per-minute of code—or words-per-minute of prose—the agent outputs
- Allow users to pause the agent to ask a clarifying question or push back on its direction without derailing the entire activity or train of thought
- Expand beyond the chat metaphor by adding UI primitives that mirror the work to be done. Enable users to pin the current working session to a particular GitHub issue. Integrate a built-in to-do list to tick off before the feature is complete. That sort of thing
- Design agents to act with less self-confidence and more self-doubt. They should frequently stop to converse: validate why we're building this, solicit advice on the best approach, and express concern when we're going in the wrong direction
- Introduce advanced voice chat to better emulate human-to-human pairing, which would allow the user both to keep their eyes on the code (instead of darting back and forth between an editor and a chat sidebar) and to light up the parts of the brain that find mouth-words more engaging than text
Anyway, that's how I see it from where I'm sitting the morning of Friday, May 30th, 2025. Who knows where these tools will be in a week or month or year, but I'm fairly confident you could find worse advice on meeting this moment.

As always, if you have thoughts, e-mail 'em.


