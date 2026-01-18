---
type: link
source: notion
url: https://www.reddit.com/r/aws/comments/1pnfjs1/claude_code_codex_and_aws_cloudwatch_quicker/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2025-12-16T03:58:00.000Z
---

# Claude Code, Codex, and AWS Cloudwatch: Quicker investigation cycles : r/aws

## Overview (from Notion)
- Automating alerts with AI tools like Claude Code and Codex can drastically reduce investigation time, freeing up hours for family and personal projects.
- The integration with Slack makes it easier to stay connected with your team while managing a busy home life.
- Improved efficiency in handling AWS alerts could lead to better work-life balance, allowing for more time spent with family.
- Unique viewpoint: Leveraging AI doesn't just enhance productivity; it enables a more thoughtful approach to work, giving you the mental space for creativity and innovation.
- Alternate view: Relying too heavily on automation might cause a disconnect from the underlying issues, potentially leading to complacency in understanding the codebase.
- This tech could be a conversation starter with other parents or tech enthusiasts, bridging personal interests with professional insights.

## AI Summary (from Notion)
The team is automating the investigation of AWS CloudWatch alerts using Claude Code and Codex on Slack to reduce the time spent on false alarms. By condensing the alert response process, they can quickly diagnose issues and create pull requests for code fixes, while ensuring agents have limited IAM permissions for security.

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

sidebar promoted post thumbnail


