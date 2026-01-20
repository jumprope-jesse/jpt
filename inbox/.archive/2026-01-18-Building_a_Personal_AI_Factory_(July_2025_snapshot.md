---
type: link
source: notion
url: https://john-rush.com/posts/ai-20250701.html
notion_type: Software Repo
tags: ['Running']
created: 2025-07-02T04:21:00.000Z
---

# Building a Personal AI Factory (July 2025 snapshot)

## Overview (from Notion)
- Leverage AI to streamline daily tasks and coding, allowing for more time with family and personal interests.
- Use the factory model to encourage a mindset of continuous improvement, both in coding practices and in personal projects.
- Explore the balance between automation and personal touch—while AI can handle repetitive tasks, your unique insights as a founder and father are irreplaceable.
- Consider the implications of rapid AI advancements on job security and the need for lifelong learning in tech.
- Embrace the iterative approach outlined in the factory model: apply it to parenting and entrepreneurship—adjust inputs (strategies) based on outcomes (results).
- Reflect on how the scalability of AI can parallel the growth of your family and business, emphasizing the need for adaptable systems.
- Challenge the notion that you always need to “fix” problems; sometimes adjusting the approach is more effective.
- Stay aware of the ethical considerations in AI development and implementation, especially as a leader in the tech space.

## AI Summary (from Notion)
The workflow for building a personal AI factory involves planning tasks with Claude Code, executing them with Sonnet models, and verifying the output to improve future iterations. The process emphasizes fixing inputs rather than outputs, allowing the factory to self-improve over time. Scaling the factory includes creating specialized agents for specific tasks and automating workflow management, while focusing on higher-level abstractions in business documentation to enhance agent effectiveness.

## Content (from Notion)

AI Factory

I keep several claude code windows open, each on its own git-worktree. o3 and sonnet 4 create plans, sonnet 3.7 or sonnet 4 execute the plan, and o3 checks the results against the original ask. Any issues found are fed back into the plan template and the code is regenerated. The factory improves itself.

Read on to see what might be useful for you.

When something goes wrong, I don’t hand-patch the generated code. I don’t argue with claude. Instead, I adjust the plan, the prompts, or the agent mix so the next run is correct by construction.

If you know Factorio you know it’s all about building a factory that can produce itself. If not, picture a top-down sandbox where conveyor belts and machines endlessly craft parts because the factory must grow. Do the same thing with AI agents: build a factory of agents that can produce code, verify it, and improve themselves over time.

## Basic day to day workflow - building the factory

My main interface is claude code. It’s my computer now. I also have a local mcp which runs Goose and o3. Goose only because I’ve already got it setup to use the models hosted in our Azure OpenAI subscription. Looking to improve this at some point, but it works for now.

### Step 1: Planning

I’ll give a high level task to claude code, which calls over to o3 to generate a plan. o3 is a good planner and can ask a bunch of good questions to clarify the job to be done. I then have it write out a <task>-plan.md file with both my original ask and an implementation plan.

### Step 2: Execution

First, sonnet 4 reads the plan, verifies it, and turns it into a task list. Next claude code execute the plan, either with sonnet 3.7 or sonnet 4 depending on the complexity of the task. Because most of my day-to-day is in clojure I tend to use sonnet 4 to get the parens right. One important instruction is to have claude write commits as it goes for each task step. This way either claude or I can revert to a previous state if something goes wrong.

### Step 3: Verification → Feedback into Inputs

Once the code is generated, I have sonnet 4 verify the code against the original plan. Then I have o3 verify the code against the original plan and original ask. o3 is uncompromising. Claude wants to please, so will keep unnecessary backwards compatibility code in place. o3 will call that out and ask for it to be removed. Claude also tends to add “lint ignore flags” to the code which o3 will also call out. Having both models verify the code catches issues and saves me back and forth with claude.

Any issue sonnet 4 or o3 finds gets baked back into the plan template, not fixed inline.

Git worktrees let me open concurrent claude code instances and build multiple features at once. I still merge manually, but I’m no longer babysitting a single agent.

- Outputs are disposable; plans and prompts compound.
- Debugging at the source scales across every future task.
- It transforms agents from code printers into self-improving colleagues.
Example: an agent once wrote code that would load an entire CSV into memory. I made it switch to streaming and had the agent write instructions to the plan to always use streaming for CSVs. Now, my plan checker flags any code that doesn’t use streaming for CSVs, and I don’t have to remember this in every PR review. The factory improves itself.

## Scaling the factory

I’ve started to encode more complex workflows, where I have specific agents (behind mcps) for building specific tasks.

One MCP will sweep all the clojure code generated and then apply our local style rules. These rules are part of the instructions for the original plan and agent but often the generated code will have style issues. Especially once claude gets in the lint/test/debug cycle. This focused agent means we have tighter behavior and can apply our style rules consistently.

I’ve started doing this for internal libraries as well. It’s good at looking at generated code and replacing things like retries and Thread/sleep with our retry library.

I’m also building out a collection of these small agents. Each one can take a small specific task, and by composing them together I can build more complex workflows. For example, I can take an api doc, and a set of internally defined business cases and have a composition of agents build integrations, tests, and documentation for the api. This is a powerful way to build out features and integrations without having to do all the work by hand.

You don’t get there in one big step. Here’s the secret sauce: iterate the inputs

It’s essentially free to fire off a dozen attempts at a task - so I do. All agents run in parallel. When one fails, stalls, or lacks context, I feed that lesson into the next iteration. I resist the urge to fix outputs, instead I fix the inputs.

That loop is the factory: the code itself is disposable; the instructions and agents are the real asset.

I’m working on a few things to improve the factory:

- Better overall coordination of the agents. I tend to kick things off manually, but I want to have a more automated way to manage the workflow and dependencies between agents.
- Aligning our business docs with the agents. Changing the information we capture to be at a higher level of abstraction so that the agents can use it more effectively. This means moving away from low level implementation details and focusing on use cases.
- More complex workflows. I’ve been able to build some pretty complex workflows with the current setup, but I want to push it further. This means more agents, more coordination, and more complex interactions between them.
- Maximize token usage across providers. I’m pretty limited by bedrock’s token limits especially for sonnet 4. Going to need to be able to switch between the claude max plan and bedrock w/out interruption.
That’s where my factory sits today: good enough to ship code while I refill my coffee, not yet good enough to bump me off the payroll. Constraints will shift, but the core principle remains: fix inputs, not outputs.


