---
type: link
source: notion
url: https://www.lesswrong.com/posts/fjgoMaBenyXcRDrbX/boundaries-membranes-and-ai-safety-compilation
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-03-14T15:55:00.000Z
---

# «Boundaries/Membranes» and AI safety compilation — LessWrong

## AI Summary (from Notion)
- Topic: Compilation of posts connecting the concept of "Boundaries/Membranes" with AI safety.
- Purpose: To explore and compile various viewpoints regarding how boundaries can contribute to AI safety, particularly in the context of transformative AI.
- Key Contributors:
- Davidad: Integrates "Boundaries" into his Open Agency Architecture for AI alignment, emphasizing the importance of respecting boundaries to ensure existential safety.
- Andrew Critch: Author of the "Boundaries" Sequence, discussing boundaries as a fundamental concept for AI alignment, including mathematical formalizations.
- Scott Garrabrant: Connects boundaries to Cartesian Frames and emphasizes their importance in understanding agent behavior in AI.
- Mark Miller: Focuses on using boundaries in computer security and AI safety, advocating for secure systems that respect boundaries.
- Major Themes:
- Importance of Boundaries: Seen as crucial for defining safe interactions between AI and humans, as well as ensuring the integrity of sentient beings.
- A Growing Interest: Recognition of the increasing relevance of this topic within the AI safety community.
- Practical Applications: Discussions on how boundaries can be modeled mathematically and practically to address AI alignment challenges.
- Interesting Facts:
- The concept of "Boundaries" extends beyond social norms to encompass physical and abstract separations.
- Workshop on "Boundaries/Membranes" related to AI safety is actively being organized.
- A Twitter thread compiling Davidad’s insights on boundaries has been created for further dissemination.
- Call to Action: Readers encouraged to engage with the topic, share insights, and keep updated on further developments.

## Content (from Notion)

In this post I outline every post I could find that meaningfully connects the concept of «Boundaries/Membranes» (tag) with AI safety.[1] This seems to be a booming subtopic: interest has picked up substantially within the past year.

Update (2023 Dec): we're now running a workshop on this topic!

Perhaps most notably, Davidad includes the concept in his Open Agency Architecture for Safe Transformative AI alignment paradigm. For a preview of the salience of this approach, see this comment by Davidad (2023 Jan):

> “defend the boundaries of existing sentient beings,” which is my current favourite. It’s nowhere near as ambitious or idiosyncratic as “human values”, yet nowhere near as anti-natural or buck-passing as corrigibility.

This post also compiles work from Andrew Critch, Scott Garrabrant, Mark Miller, and others. But first I will recap what «Boundaries» are:

# «Boundaries» definition recap:

You can see «Boundaries» Sequence for a longer explanation, but I will excerpt from a more recent post by Andrew Critch, 2023 March:

> By boundaries, I just mean the approximate causal separation of regions in some kind of physical space (e.g., spacetime) or abstract space (e.g., cyberspace). Here are some examples from my «Boundaries» Sequence:

Also, beware:

> When I say boundary, I don't just mean an arbitrary constraint or social norm.

Update: see Agent membranes and causal distance for a better exposition of the agent membranes/boundaries idea.

# Posts & researchers that link «Boundaries» and AI safety

All bolding in the excerpts below is mine.

## Davidad’s OAA

Saliently, Davidad uses «Boundaries» for one of the four hypotheses he outlines in An Open Agency Architecture for Safe Transformative AI (2022 Dec)

> Deontic Sufficiency Hypothesis: There exists a human-understandable set of features of finite trajectories in such a world-model, taking values in (−∞,0], such that we can be reasonably confident that all these features being near 0 implies high probability of existential safety, and such that saturating them at 0 is feasible[2] with high probability, using scientifically-accessible technologies.I am optimistic about this largely because of recent progress toward formalizing a natural abstraction of boundaries by Critch and Garrabrant. I find it quite plausible that there is some natural abstraction property Q of world-model trajectories that lies somewhere strictly within the vast moral gulf of

Further explanation of this can be found in Davidad's Bold Plan for Alignment: An In-Depth Explanation (2023 Apr) by Charbel-Raphaël and Gabin:

> Getting traction on the deontic feasibility hypothesis

Also:

> (*) Elicitors: Language models assist humans in expressing their desires using the formal language of the world model. […] Davidad proposes to represent most of these desiderata as violations of Markov blankets. Most of those desiderata are formulated as negative constraints because we just want to avoid a catastrophe, not solve the full value problem. But some of the desiderata will represent the pivotal process that we want the model to accomplish.

Also see this comment by Davidad (2023 Jan):

> Not listed among your potential targets is “end the acute risk period” or more specifically “defend the boundaries of existing sentient beings,” which is my current favourite. It’s nowhere near as ambitious or idiosyncratic as “human values”, yet nowhere near as anti-natural or buck-passing as corrigibility.

Reframing inner alignment by Davidad (2022 Dec):

> I'm also excited about Boundaries as a tool for specifying a core safety property to model-check policies against—one which would imply (at least) nonfatality—relative to alien and shifting predictive ontologies.

I’ve also collected all of Davidad’s tweets about «Boundaries» into this twitter thread.

Update 2023 May: I've written a post about how Davidad conceives of «boundaries» applying to alignment: «Boundaries» for formalizing a bare-bones morality.

Update 2023 August: Davidad explains this most directly in A list of core AI safety problems and how I hope to solve them:

> 9. Humans cannot be first-class parties to a superintelligence values handshake.

Update 2024 Jan 28: See Davidad's reply to this comment about specific examples of boundary violations.

## Andrew Critch

Andrew Critch has written «Boundaries» Sequence with four posts to date:

- «Boundaries», Part 1: a key missing concept from utility theory (2022 Jul)
- «Boundaries», Part 2: trends in EA's handling of boundaries (2022 Aug)
- Part 3a: Defining boundaries as directed Markov blankets (2022 Oct)
- Part 3b: «Boundaries», Part 3b: Alignment problems in terms of boundaries (2022 Dec):
> AI alignment is a notoriously murky problem area, which I think can be elucidated by rethinking its foundations in terms of boundaries between systems, including soft boundaries and directional boundaries. […] I'm doing that now, for the following problem areas:

Critch also included «Boundaries» in his plan for Encultured AI (2022 Aug):

> boundaries may be treated as constraints, but they are more specific than that: they delineate regions or features of the world in which the functioning of a living system occurs. We believe many attempts to mollify the negative impacts of AI technology in terms of “minimizing side effects” or “avoiding over-optimizing” can often be more specifically operationalized as respecting boundaries. Moreover, we believe there are abstract principles for respecting boundaries that are not unique to humans, and that are simple enough to be transferable across species and scales of organization. […]

And most recently, Critch wrote Acausal normalcy (2023 March):

> Which human values are most likely to be acausally normal?

## Scott Garrabrant

Andrew Critch connects «Boundaries» to Scott Garrabrant’s Cartesian Frames (in Part 3a of his «Boundaries» Sequence):

> The formalism here is lot like a time-extended version of a Cartesian Frame (Garrabrant, 2020), except that what Scott calls an "agent" is further subdivided here into its "boundary" and its "viscera".

See Cartesian Frames (Intro) (2020 Oct) for a related formalization of the «Boundaries» core concept.

> Cartesian frames are a way to add a first-person perspective (with choices, uncertainty, etc.) on top of a third-person "here is the set of all possible worlds," in such a way that many of these problems either disappear or become easier to address.

Note: See this summary by Rohin Shah for a conceptual summary of Cartesian Frames.

Scott Garrabrant also wrote Boundaries vs Frames (2022 Oct) which compares the two concepts.

Note: I suspect Garrabrant’s work on Embedded Agency (pre- Cartesian Frames) and Finite Factored Sets (post- Cartesian Frames) are also related, but I haven’t looked into this myself.

## Mark Miller

Mark Miller, Senior Fellow at the Foresight Institute (wiki), has worked on the Object-capability model, which applies «boundaries» to create secure systems (computer security). The goal is to make sure that only the processes that should have read and/or write permissions to a resource have those permissions. This can then be enforced with cryptography.

- Key concepts
- Boundaries-based security and AI safety approaches — LessWrong by Allison Duettmann (2023 Apr)
- AFAICT, Mark thinks that the problem of AI safety has little intrinsically to do with artificial intelligence, but instead to do with gross power imbalance. My understanding is that he thinks that safety comes not from the absence of threats, but from good security (eg in computer systems). See his 2023 talk on Misdiagnosing AGI risk.
- «Boundaries»-like ideas are also central in Gaming the Future
## Other researchers interested:

John Wentworth (@johnswentworth)

John Wentworth lists boundaries in a comment addressing “what's my list of open problems in understanding agents?”:

> I claim that, once you dig past the early surface-level questions about alignment, basically the whole cluster of "how do agents work?"-style questions and subquestions form the main barrier to useful alignment progress. So with that in mind, here are some of my open questions about understanding agents (and the even deeper problems one runs into when trying to understand agents)

He also wrote in this comment that he considers boundaries to be prerequisite for understanding ‘agenty’ phenomena (2023 Apr).

Also see: Content and Takeaways from SERI MATS Training Program with John Wentworth: Week 4, Day 1 - Boundaries Exercises (2022 Dec) where the «Boundaries» concept is used as a SERI MATS training exercise.

[There is likely to be other content I’ve missed from John Wentworth.]

Vladimir Nesov (@Vladimir_Nesov)

- eg this comment and this comment and also this comment
## Miscellaneous connections

- Consequentialists: One-Way Pattern Trap: Principled Cartesian Boundaries Keep the Good Stuff Inside by David Udell (2023 Jan)
- The Learning-Theoretic Agenda: Status 2023: Agent Detection by Vanessa Kosoy (2023 Apr)
- Causal Incentives Working Group (site)
I’ve also created a “Boundaries [technical]” tag, and tagged all of «Boundaries»-related[2] LW posts I could find.

## What I may have missed

There are surely many topics which I haven’t yet looked into which deserve to be linked in this post. I have noted those that I think are likely to be related below.

- Embedded Agency
- Finite Factored Sets
- Natural Abstractions (John Wentworth)
- Free Energy Principle and Active Inference (see Critch 3a)
- Corrigibility (also see: Arbital page — particularly, “side effects”)
- Markov blankets
If you know of any other posts I should link in this post, let me know and I’ll add them.

# Closing notes

I’m personally extremely excited about this topic, and I will be covering further developments.

I am also writing several more posts on the topic. Subscribe to my posts and/or the boundaries [technical] tag to get notified.

Please contact me with any «Boundaries»-related tips, ideas, or requests.

Post last edited: 2023-05-30.

1. ^
1. ^

