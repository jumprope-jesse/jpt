---
type: link
source: notion
url: https://www.reddit.com/r/aws/comments/1pnfjs1/claude_code_codex_and_aws_cloudwatch_quicker/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2025-12-16T03:58:00.000Z
---

# Reddit - The heart of the internet

## Overview (from Notion)
- Automating repetitive tasks like CloudWatch alarm investigations can save significant time and reduce burnout, which is crucial for balancing work and family life.
- Utilizing AI tools like Claude Code and Codex can streamline debugging processes, allowing you to focus on high-level strategies and family engagements rather than getting bogged down in technical details.
- Living in NYC, the fast-paced environment might make such efficiencies even more valuable, contributing to a better work-life balance.
- Engaging with community insights about these tools can foster collaboration and innovation in your projects, enriching both professional and personal networks.
- Conversely, there can be concerns about over-reliance on automation—potential risks include reduced deep understanding of systems and reliance on tools that may not always be accurate.
- Exploring various viewpoints on AI's role in software development can help you stay informed and adaptable in your approach to technology and family priorities.

## AI Summary (from Notion)
Automating CloudWatch alert investigations with Claude Code and Codex on Slack has improved efficiency by diagnosing issues quickly, reducing the time spent on false alarms. Alerts are now processed with simple commands, allowing for faster identification of the offending codebases and optional PR creation. Security precautions include limiting IAM permissions for agents.

## Content (from Notion)

We're tuning metric filters right now and CloudWatch alarms hit our Slack constantly

The problem: everyone started ignoring dev/staging alerts because investigating each one meant 30-45 minutes of:

- 
- 
- 
- 
A lot of the times were false alarms which meant a simple change to a few console.logs or print statements, a change we couldn't be bothered to do (and of course punted it until later, which never comes...)

So we decided to automate this with Claude Code, Codex on Slack by using Blocks (https://blocks.team)

Now every time we have a new alert we hand it off to Codex (it does a great job for diagnosing issues):

```plain text
@blocks /codex Look through the associated CloudWatch logs and find the
offending code causing these errors. Give me the root cause analysis.
```

Which we condensed to

```plain text
@blocks /codex /alarm
```

And Codex identifies the offending codebases, code. At which point we sometimes pass it to Claude Code (our default agent) in the same Slack thread

```plain text
@blocks Create a PR for this
```

Which is of course optional, even when the suggested code fix isn't used verbatim, having an agent zoom in to the issue saves a lot of time

Security warning: Make sure to give your agents limited IAM permissions (read access to log events, specific log groups, ect.)

> 

Curious if anyone's getting value out of AWS's Q agent or how they are handling investigations augmented by agents


