---
type: link
source: notion
url: https://www.ufried.com/blog/ironies_of_ai_2/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2025-12-14T13:50:00.000Z
---

# AI and the ironies of automation - Part 2

## Overview (from Notion)
- AI's Role in Daily Life: The insights on AI's limitations in automation highlight the importance of human oversight, especially in your roles as a father and founder—balancing tech with personal connections.

- Stress Management: The discussion on stress and decision-making can resonate with your daily challenges. Understanding how urgency affects productivity can help in managing both work and family life.

- Leadership Skills: The need for leadership training in directing AI aligns with the skills needed to guide your team effectively. This can influence how you approach mentoring others and managing your company.

- Unique Viewpoint: The irony that advanced automation still requires human intervention can prompt you to think about how you integrate technology into your family life, ensuring it enhances rather than complicates your personal interactions.

- Alternate Perspectives: While some may view AI as a replacement for human roles, this piece emphasizes collaboration. You might see this as a chance to cultivate a culture of teamwork in your company that values both AI and human contributions.

- Future Considerations: Keeping an eye on how AI evolves could shape your business strategy, especially in a tech-centric city like NYC, where innovation drives competition.

- Community Engagement: Discussing these ironies within your network could lead to insightful collaborations, potentially positioning you as a thought leader in both tech and family-oriented discussions.

## AI Summary (from Notion)
The text discusses the complexities and ironies of AI automation in white-collar work, emphasizing the need for human oversight despite AI's efficiency. It highlights the challenges of quick decision-making under stress, the inadequacies of current user interfaces for monitoring AI agents, and the paradox of training operators to intervene in unexpected situations. Additionally, it addresses the necessity for leadership skills in directing AI agents, suggesting that effective supervision requires a shift in approach from direct control to indirect guidance.

## Content (from Notion)

Some (well-known) consequences of AI automating work

View across several bushes and trees

In the previous post, we discussed several observations, Lisanne Bainbridge made in her much-noticed paper “The ironies of automation”, she published in 1983 and what they mean for the current “white-collar” work automation attempts leveraging LLMs and AI agents based on LLMs, still requiring humans in the loop. We stopped at the end of the first chapter, “Introduction”, of the paper.

In this post, we will continue with the second chapter, “Approaches to solutions”, and see what we can learn there.

## Comparing apples and oranges?

However, before we start: Some of the observations and recommendations made in the paper must be taken with a grain of salt when applying them to the AI-based automation attempts of today. When monitoring an industrial production plant, it is often a matter of seconds until a human operator must act if something goes wrong to avoid severe or even catastrophic accidents.

Therefore, it is of the highest importance to design industrial control stations in a way that a human operator can recognize deviations and malfunctions as easily as possible and immediately trigger countermeasures. A lot of work is put into the design of all the displays and controls, like, e.g., the well-known emergency stop switch in a screaming red color that is big enough to be punched with a flat hand, fist or alike within a fraction of a second if needed.

When it comes to AI-based solutions automating white-collar work, we usually do not face such critical conditions. However, this is not a reason to dismiss the observations and recommendations in the paper easily because, e.g.:

- Most companies are efficiency-obsessed. Hence, they also expect AI solutions to increase “productivity”, i.e., efficiency, to a superhuman level. If a human is meant to monitor the output of the AI and intervene if needed, this requires that the human needs to comprehend what the AI solution produced at superhuman speed – otherwise we are down to human speed. This presents a quandary that can only be solved if we enable the human to comprehend the AI output at superhuman speed (compared to producing the same output by traditional means).
- Most companies have a tradition of nurturing a culture of urgency and scarcity, resulting in a lot of pressure towards and stress for the employees. Stress is known to trigger the fight-or-flight mode (an ancient survival mechanism built into us to cope with dangerous situations) which massively reduces the normal cognitive capacity of a human. While this mechanism supports humans in making very quick decisions and taking quick actions (essential in dangerous situations), it deprives them of the ability to conduct any deeper analysis (not being essential in dangerous situations). If deeper analysis is required to make a decision, this may take a lot longer than without stress – if possible at all. This means we need to enable humans to conduct deeper analysis under stress as well or to provide the information in a way that eliminates the need for deeper analysis (which is not always possible).
If we let this sink in (plus a few other aspects, I did not write down here but you most likely will add in your mind), we quickly come to the conclusion that also in our AI-related automation context humans are often expected to make quick decisions and act based on them, often under conditions that make it hard (if not impossible) to conduct any in-depth analysis.

If we then also take into account, that depending on the situation a wrong result produced by an AI solution which eluded the human operator may have severe consequences in the worst case (e.g., assume a major security incident due to a missed wrongdoing of the AI solution), the situation is not that far away anymore from the situation in an industrial plant’s control station.

Summarizing, we surely need to add the necessary grain of salt, i.e., ask ourselves how strict the timing constraints in our specific setting are to avoid comparing apples and oranges in the worst case. However, in general we need to consider the whole range of possible settings which will – probably more often than we think – include that humans need to make decisions in a very short time under stressful conditions (which makes things more precarious).

## The worst UI possible

This brings us immediately to Lisanne Bainbridge’s first recommendation:

> 

In other words, the system must support the human operator as well as possible in detecting a problem, especially if it tends to occur rarely. It is a consequence of the “monitoring fatigue” problem we discussed in the previous post.

Due to the learnings people have made, a lot of effort has been put into the design of the displays, the controls and also the alerting mechanisms of industrial production control stations, making sure the human operators can make their jobs as good, as stress-free and as reliable as possible.

Enter AI agents.

The usual idea is that a single human controls a fleet of AI agents that are designed to do some kind of job, e.g., writing code. Sometimes, most agents are generic “workers”, orchestrated by some kind of supervisor that delegates parts of the work to the worker agents. Sometimes, the different agents are “specialists”, each for a certain aspect of the job to be done, that collaborate using some kind of choreography (or are also orchestrated by a supervisor). While the generic workers are easier to set up, the specialized workers usually produce more accurate results.

Because these AI-based agents sometimes produce errors, a human – in our example a software developer – needs to supervise the AI agent fleet and ideally intervenes before the AI agents do something they should not do. Therefore, the AI agents typically create a plan of what they intend to do first (which as a side effect also increases the likelihood that they do not drift off). Then, the human verifies the plan and approves it if it is correct, and the AI agents execute the plan. If the plan is not correct, the human rejects it and sends the agents back to replanning, providing information about what needs to be altered.

Let us take Lisanne Bainbridge’s recommendation and compare it to this approach that is currently “best practice” to control an AI agent fleet.

Unless we tell them to act differently, LLMs and also AI agents based on them are quite chatty. Additionally, they tend to communicate with an air of utter conviction. Thus, they present to you this highly detailed, multi-step plan of what they intend to do, including lots of explanations, in this perfectly convinced tone. Often, these plans are more than 50 or 100 lines of text, sometimes even several hundred lines.

Most of the time, the plans are fine. However, sometimes the AI agents mess things up. They make wrong conclusions, or they forget what they are told to do and drift off – not very often, but it happens. Sometimes the problem is obvious at first sight. But more often, it is neatly hidden somewhere behind line 123: “… and because 2 is bigger than 3, it is clear, we need to < do something critical >”. But because it is so much text the agents flood you with all the time and because the error is hidden so well behind this wall of conviction, we miss it – and the AI agent does something critical wrong.

We cannot blame the person for missing the error in the plan. The problem is that this is probably the worst UI and UX possible for anyone who is responsible for avoiding errors in a system that rarely produces errors.

But LLM-based agents make errors all the time, you may say. Well, not all the time. Sometimes they do. And the better the instructions and the setup of the interacting agents, the fewer errors they produce. Additionally, we can expect more specialized and refined agents in the future that become increasingly better in their respective areas of expertise. Still, most likely they will never become completely error-free because of the underlying technology that cannot guarantee consistent correctness.

This is the setting we need to ponder if we talk about the user interface for a human observer: a setting where the agent fleet only rarely makes errors but we still need a human monitoring and intervening if things should go wrong. It is not yet clear how such an interface should look like, but most definitely not as it looks now. Probably we could harvest some good insights from our UX/UI design colleagues for industrial production plant control stations. We would need only to ask them …

## The training paradox

Lisanne Bainbridge then makes several recommendations regarding the required training of the human operator. This again is a rich section, and I can only recommend reading it on your own because it contains several subtle yet important hints that are hard to bring across without citing the whole chapter. Here, I will highlight only a few aspects. She starts with:

> 

Then she talks about letting the human operator take over control regularly, i.e., do the job instead of the machine as a very effective training option. Actually, without doing hands-on work regularly, the skills of a human expert deteriorate surprisingly fast.

But if taking over the work regularly is not an option, e.g., because we want continuous superhuman productivity leveraging AI agents (no matter if it makes sense or not), we still need to make sure that the human operator can take over if needed. In such a setting, training must take place in some other way, usually using some kind of simulator.

However, there is a problem with simulators, especially if human intervention is only needed (and wanted) if things do not work as expected:

> 

The consequence of this issue is:

> 

However:

> 

Which leaves us with the irony:

> 

This is a problem we will need to face with AI agents and their supervising humans in the future, too. The supervising experts are meant to intervene whenever things become messy, whenever the AI agents get stuck, often in unforeseen ways. These are not regular tasks. Often, these are also not the issues we expect an AI agent to run into and thus can provide training for. These are extraordinary situations, the ones we do not expect – and the more refined and specialized the AI agents will become in the future, the more often the issues that require human intervention will be of this kind.

The question is twofold:

1. How can we train human operators at all to be able to intervene skillfully in exceptional, usually hard to solve situations?
1. How can we train a human operator so that their skills remain sharp over time and they remain able to address an exceptional situation quickly and resourcefully?
The questions seem to hint at a sort of paradox, and an answer to both questions is all but obvious. At the moment, we still have enough experienced subject matter experts that the questions may feel of lower importance. But if we only start to address the questions when they become pressing, they will be even harder – if not impossible – to solve.

To end this consideration with the words of Lisanne Bainbridge:

> 

In other words, we cannot simply take a few available human experts and make them supervise agents that took over their work without any further investments in the humans. Instead, we need to train them continuously, and the better the agents become, the more expensive the training of the supervisors will become. I highly doubt that decision makers who primarily think about saving money when it comes to AI agents are aware of this irony.

## Interlude

As I wrote in the beginning of first part of this blog series, “The ironies of automation” is a very rich and dense paper. We are still only at the end of the second chapter “Approaches to solutions” which is two and a half pages into the paper and there is still a whole third chapter called “Human-computer collaboration” which takes up another page until we get to the conclusion.

While this third chapter also contains a lot of valuable advice that goes well beyond our focus here, I will leave it to you to read it on your own. As I indicated at the beginning, this paper is more than worth the time spent on it.

## The leadership dilemma

However, before finishing this little blog series, I would like to mention a new kind of dilemma that Lisanne Bainbridge did not discuss in her paper because the situation was a bit different with industrial production plant automation than with AI-agent-based automation. But as this topic fits nicely into the just-finished training paradox section, I decided to add it here.

The issue is that just monitoring an AI agent fleet doing its work and intervening if things go wrong usually is not sufficient, at least not yet. All the things discussed before apply, but there is more to interacting with AI agents because we cannot simply be reactive with AI agents. We cannot simply watch them doing their work and only intervene if things go wrong. Instead, we additionally need to be proactive with them: We need to direct them.

We need to tell the AI agents what to do, what not to do, which chunks to pick and so on. This is basically a leadership role. While you do not lead humans, the kind of work is quite similar: You are responsible for the result; you are allowed to set directions and constraints, but you do not immediately control the work. You only control it through communicating with the agents and trying to direct them in the right direction with orders, with feedback, with changed orders, with setting different constraints, etcetera.

This is a skill set most people do not have naturally. Usually, they need to develop it over time. Typically, before people are put in a leadership role directing humans, they will get a lot of leadership training teaching them the skills and tools needed to lead successfully. For most people, this is essential because if they come from the receiving end of orders (in the most general sense of “orders”), typically they are not used to setting direction and constraints. This tends to be a completely new skill they need to learn.

This does not apply only to leading humans but also to leading AI agents. While AI agents are not humans, and thus leadership will be different in detail, the basic skills and tools needed are the same. This is, BTW, one of the reasons why the people who praise agentic AI on LinkedIn and the like are very often managers who lead (human) teams. For them, leading an AI agent fleet feels very natural because it is very close to the work they do every day. However, for the people currently doing the work, leading an AI agent fleet usually does not feel natural at all.

However, I have not yet seen anyone receiving any kind of leadership training before being left alone with a fleet of AI agents, and I still see little discussion about the issue. “If it does not work properly, you need better prompts” is the usual response if someone struggles with directing agents successfully.

Sorry, but it is not that easy. The issue is much bigger than just optimizing a few prompts. The issue is that people have to change their approach completely to get any piece of work done. Instead of doing it directly, they need to learn how to get it done indirectly. They need to learn how to direct a group of AI agents effectively, how to lead them.

This also adds to the training irony of the previous topic. Maybe the AI agent fleets will become good enough in the future that we can omit the proactive part of the work and only need to focus on the reactive part of the work, the monitor-and-intervene part. But until then, we need to teach human supervisors of AI agent fleets how to lead them effectively.

## Moving on

We discussed several ironies and paradoxes from Lisanne Bainbridge’s “The ironies of automation” and how they also apply to agentic AI. We looked at the unlearning and recall dilemma and what it means for the next generation of human supervisors. We discussed monitoring fatigue and the status issue. We looked at the UX and UI deficiencies of current AI agents and the training paradox. And we finally looked at the leadership dilemma, which Lisanne Bainbridge did not discuss in her paper but which complements the training paradox.

I would like to conclude with the conclusion of Lisanne Bainbridge:

> 

I could not agree more.

I think over time we will become clear on how much “The ironies of automation” also applies to automation done with AI agents and that we cannot ignore the insights known for more than 40 years meanwhile. I am also really curious how the solutions to the ironies and paradoxes will look like.

Until then, I hope I gave you a bit of food for thought to ponder. If you should have some good ideas regarding the ironies and how to address them, please do not hesitate to share them with the community. We learn best by sharing and discussing, and maybe your contribution will be a step towards solving the issues discussed …


