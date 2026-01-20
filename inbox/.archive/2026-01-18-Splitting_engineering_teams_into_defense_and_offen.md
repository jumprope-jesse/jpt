---
type: link
source: notion
url: https://www.greptile.com/blog/how-we-engineer
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-11-30T15:55:00.000Z
---

# Splitting engineering teams into defense and offense | Greptile Blog

## Content (from Notion)

I’m Daksh, one of the co-founders of Greptile. We build AI that understands large codebases, which you can query via an API. Large software teams use it for things like AI-powered code reviews and diagnosing root causes for outages.

We are a team of 4 engineers. Our customers are often surprised to learn this, since they assume we must be much larger given the breadth of our product. While this is flattering, the truth is that our product is covered in warts, and our “lean” team is more a product of our inability to identify and hire great engineers, rather than an insistence on superhuman efficiency.

The result is that our product breaks more often than we’d like. The core functionality may remain largely intact but the periphery is often buggy, something we expect will improve only as our engineering headcount catches up to our product scope. Nevertheless, the reason we get anything done at all in these circumstances has to do with a specific way in which we structure our engineering team.

## Event-driven vs. long-running processes

15 years ago, Paul Graham wrote about the “maker vs. manager schedule”, the idea that makers, such as software developers, were different from managers in that they need long, uninterrupted hours to build great things. This essay resonated with engineers around the world who had been trying to squeeze their work in between endless mandatory meetings, and probably led to some sweeping changes at least at software-driven companies in favor of creating a “maker-schedule” for engineers.

Small startups don’t suffer from an excess of meetings and instead have a whole different problem. Customers!

Without dedicated technical support teams and usually with immature products, engineers take on a lot of support work - from hotfixes to building small features for large customers, to just helping customers navigate their products. With enough customers, there is very little time to build new features and make ambitious, complex changes to the codebase.

The engineering work that comes from customers, whether it is general support, bug fixes, or small modifications can be considered “event-driven” engineering.

The engineering work that includes longer-term (more than a week), ambitious projects, can be considered “long-running” engineering.

These two are at odds.

## The fortress

Our solution to this problem has been simple, but so far, effective. This is not meant to be prescriptive. Every engineering team is different.

We instruct half the team (2 engineers) at a given point to work on long-running tasks in 2-4 week blocks. This could be refactors, big features, etc. During this time, they don’t have to deal with any support tickets or bugs. Their only job is to focus on getting their big PR out.

The other half of engineers must simply protect the first two from any support work, bugs, etc. Their job is to maintain a fortress around the long-running processes, by catching all the event-driven engineering work. At the end of the cycle, we swap.

## Why this works

Remarkable things happen when you take distractions away from a craftsperson. They can spend more time in flow and keep a large amount of context on the “client-side” of their brains.

Critically, it takes only 1-2 short interruptions to dramatically reduce the amount of work an engineer can do in a day. This chart sums it up well.

Productivity chart

Impact of interruptions on developer productivity

It follows then that it’s far more useful to isolate interruptions to a few people rather than disperse them to “keep everyone productive”. If you’re spending some amount of time on support, incrementally more time spent on support will not affect your productivity much.

The impact of interruptions on productivity

## Defense/Offense engineering

A mental model that I have found useful is to view event-driven engineering as “defensive” and long-running processes as “offensive”. This tracks nicely to the effect that each has.

Defensive engineering exists to maintain your product, whereas offensive engineering exists to expand it.

Defensive engineering more strongly correlates with your retention and customer satisfaction, whereas offensive engineering arguably correlates a little more strongly with your ability to acquire new customers.

## Disclaimer

Not only am I not a professional engineering manager, this is also a very specific and usually ephemeral situation - a small team running a disproportionately fast growing product in a hyper-competitive and fast-evolving space. This is not advice, but rather an observation about how we run our engineering team.


