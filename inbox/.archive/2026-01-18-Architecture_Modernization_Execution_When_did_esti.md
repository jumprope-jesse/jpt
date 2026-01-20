---
type: link
source: notion
url: https://domainanalysis.io/p/architecture-modernization-execution
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-11-20T03:40:00.000Z
---

# Architecture Modernization Execution: When did estimates turn into deadlines?

## Overview (from Notion)
- The journey through software modernization mirrors personal growth; both require patience and adaptability.
- The complexities of legacy systems can reflect the unpredictability of family life, where unforeseen challenges arise regularly.
- The insights on estimates as approximations can resonate with parenting, where expectations often shift based on real-world dynamics.
- Emphasizing leadership's role in fostering a supportive environment can parallel your approach as a father—nurturing resilience and problem-solving in your children.
- Consider the balance between control and flexibility; in both business and family, too much control can stifle creativity and growth.
- Exploring alternate views on failure as a learning opportunity can lead to more innovative solutions in both your professional and personal life.
- The narrative of navigating uncertainty in modernization can inspire you to embrace life's unpredictability, finding strength in adaptation.

## AI Summary (from Notion)
The author reflects on the complexities of software modernization, likening it to car repairs where unforeseen issues can arise, leading to increased costs and delays. They emphasize the importance of asking the right questions and adapting to new findings rather than strictly adhering to initial estimates. The piece discusses the need for leaders to embrace a flexible management style in complex contexts, allowing for experimentation and adaptation as challenges emerge during modernization efforts.

## Content (from Notion)

Can I please return to my vacation days in early October?

After my unforgettable and fun vacation in Seoul and Sokcho, my original plan was to write about Systems Thinking and the book I read, "Zen and the Art of Motorcycle Maintenance" by Robert Pirsig.

Thanks for reading DomainAnalysis.io! Subscribe for free to receive new posts and support my work.

The Great Buddha at Seoraksan National Park, South Korea

But all it takes is a moment, which has lasted more than two weeks, and I feel my life has turned upside down. The last two weeks have been quite literally a car wreck.

- First, the Sunday before the US elections, while pulling over for a paramedic, I got rear-ended by a monster pickup truck. I am fine, thankfully, but my car still is not.
- Second, I really believed that the company I work for, the New York Times, would avoid the ULP strike by the tech workers by agreeing to a fair contract before the US elections. That did not happen. And I don't want to discuss the US election results because that hurt will not go away anytime soon. Meanwhile, my colleagues and I went on an 8-day ULP strike. Since the company refused to bargain with us while we were on strike, we decided to end the strike and return to work earlier this week. We would like to get the contract we deserve soon.
- I am trying very hard to return back to functioning, I must be succeeding because here I am, able to write some words!
Estimates - Is it an Art or Science?

My car has been in the auto body repair shop for the past two weeks, and I am still trying to get an estimate of its damages. I am learning that it's an interesting domain:

- First, the insurance adjuster submits what they think is the damage to the car to the repair shop. Let's say this is $15000
- Next, the repair shop submits what they think is the damage back to the insurance company. Let's say it's $18000, and the shop estimates it would take 30 days to fix it.
- Eventually, the insurance adjuster and the repair shop expert meet to assess the damage together. Let's say the insurance adjuster approves this new estimate from the repair shop. The repair shop then starts with the repair process. At least this is my understanding so far.
Unforeseen Issues

But what if there is damage that can't be seen yet? Let's say the repair shop is in the process of doing the repairs they notice additional damage. Or they put the car on the frame machine to see if there is damage to the frame. In a unibody frame, it's not just the point of impact of the frame; some of the effects can also transfer to the back of the frame. So they'll have to inspect it to assess the full damage. They might start unassembling the car and notice more damage that was not originally on the estimate. Now what?

Emergent Solutions

Let's say, based on the new findings, it's going to cost an additional $20,000. They now need the approval of the insurance company to proceed. So they write up the new findings with the new cost and send a supplemental repair for approval. The insurance company will determine whether, at this point, it still makes sense to proceed with the repair or call it a total loss. And, of course, there are guidelines and rules to determine that. Let's assume it's not a total loss. The insurance company then approves the additional cost of repair.

Real Talk or Crazy Talk?

Can you imagine if the insurance company started arguing with the repair shop, asking them—no—telling them that they would only pay the $18,000 and not the additional $20,000 because that was the original estimate? Does that sound ridiculous to you? It does to me, too. Thank heavens, reality does not operate like this.

Isn't Complex Software Architecture Modernization the same?

When you are in the process of modernizing legacy software, you are in the realm of complex software. When you look at it from the outside, you see some obvious things, and based on experience and expertise, you come up with an initial estimate. This is the repair shop's original estimate of $18,000

As you are in the process, you start uncovering additional complexity. This complexity could be similar to some hidden damages the repair shop discovered after un-assembling the parts, or this could be significant frame damage that the repair shop discovered. What do you do? You need additional approvals to proceed at this point.

Good Leaders Ask the Right Questions

The right questions are asked if you are in a healthy software development environment when you bubble these problems up. How complex is this problem? What are the different ways of solving this? What are the tradeoffs? Are there workarounds or alternate solutions to this?

Suppose the questions start leading to how you did not see this complexity, how you missed this, why it is taking so long, and you are beholden to the original estimated dates? May the force be with you and your team to give you the strength to see this through. Hopefully, your modernization journey will be a short and successful one.

To Proceed or call it a Total Loss?

I have been involved in both types of modernization projects. Cases where the supplemental cost gets approved, and work proceeds until the next step, rinse and repeat until the project has come to completion. I've also seen total loss, i.e. the project got canned because it was too expensive to proceed, and it would cost more than it was worth. It's not easy deciding this, and there are frameworks and decision workshops to try and choose the direction.

Is this a complex context or a complicated context?

I urge you to read the excellent article from David J Snowden and Mary E Boone on, “A Leaders Framework for Decision Making”. Using the Cynefin framework, motorcycle maintenance or auto repair might fall under the complicated context. In order to fix the car, the expert technician, after having listened to how the collision happened, also has to analyze and test multiple factors, such as unseen damage, frame damage, etc., to determine the best course of action for the car.

However, in a complex context, you can only decide whether or not it is right or wrong in hindsight, i.e. after you've tried the thing. Does this jive more and more with complex legacy modernization software projects? I.e. you try something and learn that the integration you thought would work doesn’t work or you uncover a completely new behavior you never knew existed and you now have to account for it?

There is no fixed path when modernizing a complex legacy system. There is no rulebook to follow. You try, experiment, discover, solve, and move on to the next piece until you're done.

Denial - Anger - Bargaining - Depression - Acceptance??

When modernizing applications, if we understand that this effort falls somewhere between Complex and Complicated Contexts, we can implement the right sort of gauges to see how to proceed and determine success. Applying the process of estimates for a complex context is wrong. It’s like trying to use a hammer as a solution for every screw or a lug nut! Sometimes you need a screwdriver and sometimes you need a wrench!

Curveballs in modernization projects are just a reality. You can't foresee every outcome ahead of time. No amount of upfront analysis would lead you to a perfect data model. There will be new learnings almost every step of the way. Data Models will have to change based on the complexity you have uncovered. So it's a matter of when, not if, for curveballs. When a curveball hits and the estimate changes, take a step forward instead of getting angry or blaming folks or trying to do a what-if analysis on how best to bring the schedule in.

When you’re dealing with curveballs, which Ron Westrum’s defined model of culture does your organization adopt? Power-Oriented where messengers who inform about the curveballs are shot and failure leads to scapegoated, Rule-Oriented where the messengers who inform about the curveballs are ignored and failure leads to justice or Performance- Oriented where the messengers who inform about the curveballs are trained and failure leads to enquiry?

As long as the problem you're trying to solve is still relevant and still meets the business needs, take it one step at a time. Ultimately the software you are trying to modernize is for users.

Tip for Leaders Leading Modernization Initiatives

To quote from the same article, "Leaders who don't recognize that a complex domain requires a more experimental mode of management may become impatient when they don't seem to be achieving the results they were aiming for. They may also find it difficult to tolerate failure, an essential aspect of experimental understanding. If they try to overcontrol the organization, they will preempt the opportunity for informative patterns to emerge. Leaders who try to impose order in a complex context will fail. Still, those who set the stage, step back a bit, allow patterns to emerge, and determine which ones are desirable will succeed".

A New Hope

Either way I will be ok, whether the repair company is able to fix my car or the insurance company deems it a total loss. The system works. I wish I could say the same for modernization projects and the awful industry practice about how much ceremony we attribute to estimates, completely forgetting that an estimate means an approximate of the actual. I hope more and more software companies and leadership use the proper framework for measuring success. I hope this leaves you with some ideas on implementing changes or at least questioning the practices if they seem wrong.

"I've wondered why it took us so long to catch on. We saw it, and yet we didn't see it. Or rather we were trained not to see it. Conned perhaps into thinking that the real action was metropolitan and all this was just boring hinterland. It was a puzzling thing. The truth knocks on the door and you say, "Go away. I'm looking for the truth." And so it goes away. Puzzling."

― Robert Pirsig


