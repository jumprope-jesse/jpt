---
type: link
source: notion
url: https://olano.dev/blog/software-design-is-knowledge-building
notion_type: Tech Deep Dive
tags: ['Running']
created: 2025-01-01T21:10:00.000Z
---

# Software Design is Knowledge Building | olano.dev

## Content (from Notion)

/blog /projects

### 1. The Story

This is the story of system SVC from company ORG. It’s a true story, but I’ve smoothed out the details: by making it generic, I hope that it will be more familiar.

1. ORG relies on an integration service, SaaS, to decouple its business logic from vendor software dealing with billing, analytics, customer management, etc.
1. ORG shifts from assume we have infinite budget mode to we need to break even next year or we’ll die.
1. Some dutiful analyst notices that ORG spends an egregious amount of money on seemingly innocuous middleware SaaS.
1. Some dutiful executive figures that, seeing as they already spend a lot of money on software engineers, they should be able to replace SaaS with a system built in-house, to be called SVC.
1. Some dutiful manager tasks X, one of ORG ’s finest engineers, with the job of building SVC. X will be working alone and on a tight schedule, as the executive wants to get rid of SaaS before the next billing cycle kicks in.
1. X gets the job done in time, as everyone in ORG has come to expect from her. With SVC working and SaaS out of the way, X moves on to more important—or more pressing—matters and, eventually, leaves ORG.
1. TEAM takes over ownership of SVC. For all intents and purposes, development is done, they only need to keep the lights on.
1. Requirements change, assumptions are proven wrong, unknown unknowns are uncovered. A dutiful product owner realizes that the business now demands changes to SVC, so he writes down some tickets for TEAM to work on.
1. TEAM fails miserably to deliver. They don’t seem to know what they are doing, taking forever to apply the smallest changes, always side-tracked by bugs and production outages.
1. TEAM is, uh, restructured into TEAM++, of higher average seniority, and continues working on SVC.
1. GOTO 9.
This entire process takes less than a year.

### 2. Commentary

What is going on with SVC? Did X10 do a bad job? By all accounts, she did not. The project was finished on time, according to specifications; ORG will save a lot of money next year. X10 followed best practices, too: good test coverage, no over-engineering. Surely she cut some corners; she didn’t think twice about the design of the system. As in any project, there’s a lot of room for improvement, but nothing that a team of competent engineers couldn’t handle. But, if X10 got the hard part of the job done, how come not one but many teams of competent engineers fail to apply a few small changes to the system?

What fascinates me about this scenario is how a seemingly functional 6-month-old project automatically turns into a haunted forest just by changing hands. Regardless of its age, SVC is textbook legacy software because, more often than not, a question posed about the system, to any team member, results in the same answer: I don’t know.

The problem is that TEAM members don’t have enough elements to build a satisfactory mental model of SVC. They need to go by a mix of the client’s interpretation of what the system should be, and what they can tell from the code that the system actually is. These views can be disconnected and contradictory. The code may tell the what and the how, but it doesn’t tell the why. Only X10 could say what was a functional requirement, what a technical necessity, what a whim, what an accident. The team has to resort to reverse engineering, extrapolating, and guessing.

### 3. The Theory

Underlying the decision to move X10 out of the project once the system was operational, is the common misconception that software development consists of producing code; that, once working code exists, programmers should act as interchangeable operators of varying qualities1.

In his Software Aging paper, David Parnas warns against putting software in the hands of developers who haven’t contributed to (and thus don’t understand) its design:

> 

TEAM was bound to make what Parnas calls “ignorant surgery”, the system degrading over time. But that doesn’t quite explain why they were immediately helpless as they took over the project. I find a better characterization in Peter Naur’s Programming as Theory Building:

> 

> 

In this view, the mental model that allows the designer to map a subset of the world (the domain) to and from the system, and not the system itself, is the primary product of the software design activity:

> 

Naur defines software design as an intellectual activity, consisting of building and having a theory, where theory is understood as

> 

Notice the similarity to Zach Tellman’s thesis in his ongoing newsletter:

> 

> 

A more conventional way to define the software design activity is in terms of minimizing complexity. If we acknowledge that reducing ambiguity, obscurity, unknown unknowns, and cognitive load—all of them forms of removing complexity—also enables better understanding and easier explanations, then we should conclude that both models are compatible, if not equivalent.

### 4. Postscript

The theory-building view explains why TEAM couldn’t take ownership of SVC. When X10 left the company, taking the development context—the mental model—with her, the system deteriorated. In Naur’s terms, while still operational, the system was dead:

> 

TEAM ’s duty, then, is to revive the system by building a new theory of it. But reconstructing the model while keeping the system operational is a slow and difficult process—a hard sell for an organization convinced that development has just finished. Naur goes as far as saying that program revival, from code and documentation alone, is impossible. The program should preferably be discarded, and the new team should be given the opportunity to resolve the problem from scratch.

With three extra decades of hindsight, I tend to disagree. Revival is very hard, yes, but I’ve seen it happen. It may require that the new team ultimately rewrite every line of the original, one at a time. And I’ve seen fresh starts fail more consistently than that2.

Knowing that revival is a plausible future need has powerful consequences for our work. To approach it correctly, we should mind the people that one day will have to take the project out of its coma: in the style of the code and the structure of the system, but also in its paratexts—comments, docstrings, READMEs, Pull Requests, commit messages, Jira tickets, and Confluence pages.

Granted, my story was an all-too-perfect illustration of Naur’s thesis. I can’t prove it, but I suspect that we could benefit from accepting his theory as a law: the ultimate goal of software design should be (organizational) knowledge building.

So the next time you choose a name, or structure a project, or ponder whether to write or omit a certain comment, rather than thinking in terms of the burden on future maintainers, think: how much will this decision affect—how much will it help or hinder—their building of a mental model of the system, of the business, of the world.

### Notes

1

A misconception similarly made by those who intend to replace programmers with statistical models.

2

In my experience, developers advocate for greenfield rewrites to escape the operational annoyances of production systems. They, too, fall in the trap of assuming that clean code is the hard part of software development. Even in the unlikely case that they produce a replacement matching or improving on the original system, they won’t stick around to run it in production when development slows down. What is left is another stillborn like SVC.


