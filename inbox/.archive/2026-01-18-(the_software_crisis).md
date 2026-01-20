---
type: link
source: notion
url: https://wryl.tech/log/2024/the-software-crisis.html
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-07-06T00:15:00.000Z
---

# (the software crisis)

## AI Summary (from Notion)
- The term "software crisis" was first coined at the NATO Software Engineering conference in 1968, highlighting the challenges in software development due to increasing hardware complexity.
- Edsger Dijkstra identified the crisis as stemming from the rapid advancement of computing power without corresponding advancements in software organization.
- Despite advancements in programming practices, there is a prevailing sense of comfort that masks underlying issues in software complexity and usability.
- Users and developers often rely on abstract models that do not reflect the reality of software systems, leading to catastrophic failures when assumptions are incorrect.
- The common approach to address the software crisis has been to "abstract it away," which often results in performance costs and a disconnect from the underlying hardware.
- The popularity of personal computing and faster hardware release cycles has accelerated the move towards abstraction, complicating software construction and user control.
- The document argues for a need to constrain the layers of abstraction in software development, ensuring that users retain agency and understanding of the tools they use.
- Movements like Handmade and Permacomputing are emerging to address and raise awareness about the software crisis, indicating a resurgence of interest in fundamental computing principles.
- The final takeaway emphasizes the potential for improvement in the software field, advocating for deeper engagement with software construction and a return to more understandable, composable systems.

## Content (from Notion)

crisis [ˈkraɪ sɪs] (noun): a turning point

In 1968, at the first NATO Software Engineering conference, the term "software crisis" was coined. These conferences were pivotal moments in computing history, as they were some of the first efforts to pin down and codify the current practices in programming automatic computing machines. On July 16th, 1969, the Apollo 11 mission launched, sporting some of the most advanced engineering practices known at the time. The last NATO Software Engineering conference was held in October of the same year. I can imagine enthusiastic conversations about guidance control, redundancy, and general speculation around how the Apollo program's approach to constructing programs worked. In his 1972 Turing Award lecture, Edsger Dijkstra made clear the perceived cause of the software crisis: an increase in computing hardware complexity and speed, without the organizational methods to address the growing complexity of software that utilized this hardware.

"The major cause of the software crisis is that the machines have become several orders of magnitude more powerful! To put it quite bluntly: as long as there were no machines, programming was no problem at all; when we had a few weak computers, programming became a mild problem, and now we have gigantic computers, programming has become an equally gigantic problem."

Edsger Dijkstra

The term "software crisis" isn't featured much in current conversation around programming practices. We generally think we've "figured it out", with some minor difficulties that are deemed "essential" or "tolerable". Time and distance from the "problems of the past", along with the development of new languages and organizational methods, has pushed us into a state of comfort. Our ecosystems are teeming with life and new software.

We've figured it out by now, right? Right?

It seems as if this state of comfort is due to a sense of defeat and acceptance, rather than of a true, genuine comfort. We peer endlessly at the machines in front of us, and we establish mental models for their inner workings. From seasoned programmers and technology enthusiasts to the passively invested users of technology, we form shortcuts, abstract models that allow us to avoid thinking about the millions of moving parts that make up the things we use.

Very rarely do these models reflect reality. It's a nice coincidence when they do. It's catastrophic when they don't.

Various efforts have been made to address pieces of the software crisis, but they all follow the same pattern of "abstract it away". If we sweep the unsavory details into structures we can control, we can achieve some level of "independence" at the cost of performance. However, much of the early advancements in computing and adjacent fields occurred on machines where building towers of abstraction had a direct cost, and in contexts where that cost couldn't be paid. Every roadblock that was hit was met with a hardware upgrade. In theory, this is a natural growth cycle. As we learn how to utilize our resources more efficiently, we hit a point where the current restrictions cannot be bypassed, necessitating a hardware upgrade. In practice, we grow hungry for capacity long before we've understood its limitations. That hunger for ability was slow to grow before the advent of commercialization of personal computing, but companies selling equipment don't make money waiting for their users to master their products. The growth cycle accelerated, and accelerated, and accelerated...

As personal computing grew more popular, and hardware release cycles grew faster, "abstract it away" became the default mode of thinking. Out of sight, out of mind.

We developed methods of building nested layers of abstractions, hiding information at multiple levels. We took the problem of constructing software and morphed it into towering layers. We integrated these layers into the software required to use our computers, and the software that drives our lives. The wider software industry accelerated its release cycles and capital influence, bringing about the proverbial death of the individual developer. We lament the easy access to fundamental features of a machine, like graphics and sound. It is no longer easy to build software, and nothing comes with a manual. If curious developers can no longer build software without scaling mountains, what hope is there for the broader problem? The software crisis doesn't just apply to the profession of building software, but to anybody that uses software. Users have little to no control, save for things afforded to them by the author.

"Don't have good ideas if you aren't willing to be responsible for them."

Alan Perlis

Those who construct software are placed in a unique blind spot. We produce tools that we may not understand the true potential of for decades. We are often caught in fits of creative problem solving, the passion of the craft, or the pressure of peers.

We forget that software construction, just like software usage, is a human activity.

We are separated from the responsibility of the tools that we build. This has been the norm for several decades, with the perceived stakes being lowered as commercialization took hold. We continue reaching for abstraction as a tool to avoid the hard thoughts, and this has bled into how people develop and use software. When machines were small, and we couldn't afford endless abstractions (unless they were "free"), we knew the cost of sweeping things under the rug. Small inefficiencies added up. There was a limit to how far you could separate yourself from the machine. Newcomers had a low-cost entry point, if they were curious enough.

The water was shallow enough to learn to swim in.

The solution to the software crisis will not be a reversion to more constrained platforms, but a constraint on the number of layers of abstraction we are allowed to apply, as well as the requirement of information preservation between these layers. We must narrow the (semantic gap) so that everyone may scale it. Programming models, user interfaces, and foundational hardware can, and must, be shallow and composable. We must, as a profession, give agency to the users of the tools we produce. Relying on towering, monolithic structures sprayed with endless coats of paint cannot last. We cannot move or reconfigure them without tearing them down. There have been movements to bring awareness to the software crisis, such as (Handmade), (Permacomputing), and various retro-computing circles. We're starting to realize just how deep in this crisis we are. Counterculture movements are health signals, and a fever is brewing.

Things can be better. I'll show you how.

⦶ -------- (back)

...... ... .. ... .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. ... .. ... ......

wryl © 2024


