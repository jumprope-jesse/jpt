---
type: link
source: notion
url: https://zarar.dev/good-software-development-habits/
notion_type: Software Repo
tags: ['Running']
created: 2024-11-18T03:49:00.000Z
---

# Good software development habits | Zarar's blog

## Overview (from Notion)
- Emphasizing small commits aligns with the busy life of a parent, allowing you to manage code changes without feeling overwhelmed, similar to handling family tasks in manageable chunks.
- Continuous refactoring can mirror parenting—adapting and improving as you learn what works best for your family dynamics.
- Viewing all code as a liability underscores the importance of accountability, akin to responsibilities in family life; knowing what you produce is reliable can bring peace of mind.
- Trusting frameworks relates to trusting your instincts as a parent—sometimes, relying on established knowledge is crucial.
- Creating new modules instead of forcing code fits reflects the flexibility needed in both software and parenting; it's about finding the right solution for individual situations.
- Writing tests first encourages proactive problem-solving, much like preparing for family needs before they arise.
- Minimizing duplication in code is akin to finding efficient routines in family life, reducing chaos.
- Accepting that designs get stale may resonate with the ever-evolving nature of family life; adaptability is essential.
- Understanding technical debt can help prioritize both software and family responsibilities; focus on what directly impacts your current situation.
- The correlation between testability and good design might inspire you to create systems in your family life that are easier to manage and adapt.

## AI Summary (from Notion)
Good software development habits include keeping commits small, continuous refactoring, deploying often to ensure working software, avoiding unnecessary testing of frameworks, creating independent modules for unclear functions, writing tests first for APIs, limiting copy-paste to avoid duplication, accepting design changes, managing technical debt effectively, and ensuring testability correlates with good design. Emphasizing adaptability and continuous improvement is crucial in software development.

## Content (from Notion)

This post is not advice, it's what's working for me.

It's easy to pick up bad habits and hard to create good ones. Writing down what's working for me helps me maintain any good habits I've worked hard to develop. Here's an unordered list of 10 things that have helped me increase speed and maintain a respectable level of quality in the product I'm currently developing.

1. Keep commits small enough that you wonder if you're taking this "keep commits small" thing a little too far. You just never know when you have to revert a particular change and there's a sense of bliss knowing where you introduced a bug six days ago and only reverting that commit without going through the savagery of merge conflicts. My rule of thumb: compiling software should be commitable.
1. Live Kent Beck's holy words of wisdom: "for each desired change, make the change easy (warning: this may be hard), then make the easy change". Aim for at least half of all commits to be refactorings. Continuous refactoring is thinking of changes I can make in under 10 minutes that improve something. Doing this pays off whenever a bigger requirement comes in and you find yourself making a small change to satisfy it only because of those smaller improvements. Big refactorings are a bad idea.
1. All code is a liability. Undeployed code is the grim reaper of liabilities. I need to know if it works or at least doesn't break anything. Tests give you confidence, production gives you approval. The hosting costs might rack up a little with so many deploys but it's a small price to pay for knowing the last thing you did was a true sign of progression. Working software is the primary measure of progress, says one of the agile principles. Working and progress are doing a lot of heavy lifting in that sentence, so I've defined them for myself. Working is something being working enough to be deployed, and if it's code that's contributing to a capability, that's progress.
1. Know when you're testing the framework's capability. If you are, don't do it. The framework is already tested by people who know a lot more than you, and you have to trust them that the useState() hook does what it's supposed to do. If you keep components small, then you reduce the need for a lot of tests as the framework will be doing most of the heavy lifting in the component. If the component is big, then you introduce more complexity and now you need to write a lot of tests.
1. If a particular function doesn't fit anywhere, create a new module (or class or component) for it and you'll find a home for it later. It's better to create a new independent construct than to jam it into an existing module where you know deep down it doesn't make sense. Worst comes to worst, it lives as an independent module which isn't too bad anyway.
1. If you don't know what an API should look like, write the tests first as it'll force you to think of the "customer" which in this case is you. You'll invariably discover cases that you would not have thought of if you had just written the code first and tests after. You don't have to be religious about TDD and it's OK to work in larger batches (e.g., write more than just a couple lines of code before making it pass). The amount of code to write in a red/failing state doesn't always have to be small. You know what you're doing, don't let dogma get in the way of productivity.
1. Copy-paste is OK once. The second time you're introducing duplication (i.e., three copies), don't. You should have enough data points to create a good enough abstraction. The risk of diverging implementations of the same thing is too high at this point, and consolidation is needed. It's better to have some wonky parameterization than it is to have multiple implementations of nearly the same thing. Improving the parameters will be easier than to consolidate four different implementations if this situation comes up again.
1. Designs get stale. You can slow the rate at which they get stale by refactoring, but ultimately you'll need to change how things work. Don't feel too bad about moving away from something that was dear to you a while ago and something you felt proud about at the time. You did the right thing then and shouldn't beat yourself up for not getting it right enough that you wouldn't need to change anything. Most of the time writing software is changing software. Just accept it and move on. There's no such thing as the perfect design, and change is at the core of software development. How good you are at changing things is how good you are at software development.
1. Technical debt can be classified into three main types: 1) things that are preventing you from doing stuff now, 2) things that will prevent you from doing stuff later, and 3) things that might prevent you from doing stuff later. Every other classification is a subset of these three. Minimize having lots of stuff in #1 and try to focus on #2. Ignore #3.
1. Testability is correlated with good design. Something not being easily testable hints that the design needs to be changed. Sometimes that design is your test design. As an example, if you find yourself finding it difficult to mock em.getRepository(User).findOneOrFail({id}), then chances are you either need to put that call into its own function that can be mocked, or write a test utility which allows for easier mocking of the entity manager methods. Tests go unwritten when it's hard to test, not because you don't want to test.
There's probably a lot more, but 10 is a nice number.


