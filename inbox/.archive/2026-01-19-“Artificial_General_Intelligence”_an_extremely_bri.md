---
type: link
source: notion
url: https://www.lesswrong.com/posts/uxzDLD4WsiyrBjnPw/artificial-general-intelligence-an-extremely-brief-faq
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-03-13T03:45:00.000Z
---

# “Artificial General Intelligence”: an extremely brief FAQ — LessWrong

## AI Summary (from Notion)
- Topic: The document discusses "Artificial General Intelligence" (AGI) and raises questions about its development and implications.
- AGI Definition: AGI refers to future AIs that can perform tasks with human-like understanding and capabilities.
- Key Questions:
- The current state of AI and whether AGI exists.
- The potential demand for AGI and its implications for society.
- Concerns about the uncontrollable nature of AGI and the risks associated with it.
- Intrinsic Cost Module:
- A proposed component of AGI that mimics human drives (hunger, pain, curiosity).
- The challenge of ensuring that these drives align with human welfare and controllability.
- Concerns:
- The lack of clarity on how to design AIs with prosocial motivations.
- The possibility that AIs may develop unpredictable and self-interested motivations.
- The need for robust technical solutions to prevent undesirable outcomes.
- Call to Action:
- Encourages researchers, particularly Yann LeCun, to take the alignment problem seriously and work on solutions to ensure AI behaves in a controllable and beneficial manner.
- Conclusion:
- There is a significant gap in understanding how to create AIs that prioritize human welfare, and this needs to be addressed before pursuing advanced AI development.
- Interesting Fact: The paper draws analogies between AI motivations and human psychological factors, emphasizing the complexity of embedding such motivations into AI systems.

## Content (from Notion)

(Crossposted from twitter for easier linking.) (Intended for a broad audience—experts already know all this.)

When I talk about future “Artificial General Intelligence” (AGI), what am I talking about? Here’s a handy diagram and FAQ:

“Are you saying that ChatGPT is a right-column thing?” No. Definitely not. I think the right-column thing does not currently exist. That’s why I said “future”! I am also not making any claims here about how soon it will happen, although see discussion in Section A here.

“Do you really expect researchers to try to build right-column AIs? Is there demand for it? Wouldn’t consumers / end-users strongly prefer to have left-column AIs?” For one thing, imagine an AI where you can give it seed capital and ask it to go found a new company, and it does so, just as skillfully as Earth’s most competent and experienced remote-only human CEO. And you can repeat this millions of times in parallel with millions of copies of this AI, and each copy costs $0.10/hour to run. You think nobody wants to have an AI that can do that? Really?? And also, just look around. Plenty of AI researchers and companies are trying to make this vision happen as we speak—and have been for decades. So maybe you-in-particular don’t want this vision to happen, but evidently many other people do, and they sure aren’t asking you for permission.

“If the right-column AIs don’t exist, why are we even talking about them? Won’t there be plenty of warning before they exist and are widespread and potentially powerful? Why can’t we deal with that situation when it actually arises?” First of all, exactly what will this alleged warning look like, and exactly how many years will we have following that warning, and how on earth are you so confident about any of this? Second of all … “we”? Who exactly is “we”, and what do you think “we” will do, and how do you know? By analogy, it’s very easy to say that “we” will simply stop emitting CO2 when climate change becomes a sufficiently obvious and immediate problem. And yet, here we are. Anyway, if you want the transition to a world of right-column AIs to go well (or to not happen in the first place), there’s already plenty of work that we can and should be doing right now, even before those AIs exist. Twiddling our thumbs and kicking the can down the road is crazy.

“The right column sounds like weird sci-fi stuff. Am I really supposed to take it seriously?” Yes it sounds like weird sci-fi stuff. And so did heavier-than-air flight in 1800. Sometimes things sound like sci-fi and happen anyway. In this case, the idea that future algorithms running on silicon chips will be able to do all the things that human brains can do—including inventing new science & tech from scratch, collaborating at civilization-scale, piloting teleoperated robots with great skill after very little practice, etc.—is not only a plausible idea but (I claim) almost certainly true. Human brains do not work by some magic forever beyond the reach of science.

“So what?” Well, I want everyone to be on the same page that this is a big friggin’ deal—an upcoming transition whose consequences for the world are much much bigger than the invention of the internet, or even the industrial revolution. A separate question is what (if anything) we ought to do with that information. Are there laws we should pass? Is there technical research we should do? I don’t think the answers are obvious, although I sure have plenty of opinions. That’s all outside the scope of this little post though.

Crossposted from the AI Alignment Forum. May contain more technical jargon than usual.

# Summary

- This post is about the paper A Path Towards Autonomous Machine Intelligence (APTAMI) by Yann LeCun. It’s a high-level sketch of an AI architecture inspired by the brain.
- APTAMI is mostly concerned with arguing that this architecture is a path towards more-capable AI. However, it is also claimed (both in the paper itself and in associated public communication) that this architecture is a path towards AI that is “controllable and steerable”, kind, empathetic, and so on.
- I argue that APTAMI is in fact, at least possibly, a path towards that latter destination, but only if we can solve a hard and currently-unsolved technical problem.
- This problem centers around the Intrinsic Cost module, which performs a role loosely analogous to “innate drives” in humans—e.g. pain being bad, sweet food being good, a curiosity drive, and so on.
- APTAMI does not spell out explicitly (e.g. with pseudocode) how to create the Intrinsic Cost module. It offers some brief, vague ideas of what might go into the Intrinsic Cost module, but does not provide any detailed technical argument that an AI with such an Intrinsic Cost would be controllable / steerable, kind, empathetic, etc.
- I will argue that, quite to the contrary, if we follow the vague ideas in the paper for building the Intrinsic Cost module, then there are good reasons to expect the resulting AI to be not only unmotivated by human welfare, but in fact motivated to escape human control, seek power, self-reproduce, etc., including by deceit and manipulation.
- Indeed, it is an open technical problem to write down any Intrinsic Cost function (along with training environment and other design choices) for which there is a strong reason to believe that the resulting AI would be controllable and/or motivated by human welfare, while also being sufficiently competent to do the hard intellectual tasks that we’re hoping for (e.g. human-level scientific R&D).
- I close by encouraging LeCun himself, his colleagues, and anyone else to try to solve this open problem. It’s technically interesting, very important, and we have all the information we need to start making progress now. I've been working on that problem myself for years, and I think I’m making more than zero progress, and if anyone reaches out to me I’d be happy to discuss the current state of the field in full detail.
- …And then there’s an epilogue, which steps away from the technical discussion of the Intrinsic Cost module, and instead touches on bigger-picture questions of research strategy & prioritization. I will argue that the question of AI motivations merits much more than the cursory treatment that it got in APTAMI—even given the fact that APTAMI was a high-level early-stage R&D vision paper in which every other aspect of the AI is given an equally cursory treatment.
(Note: Anyone who has read my Intro to Brain-Like AGI Safety series will notice that much of this post is awfully redundant with it—basically an abbreviated subset with various terminology changes to match the APTAMI nomenclature. And that’s no coincidence! As mentioned, the APTAMI architecture was explicitly inspired by the brain.)

# 1. Background: the paper’s descriptions of the “Intrinsic Cost module”

Figure 2 from APTAMI. “Intrinsic Cost” is the red oval towards the bottom-right.

For the reader’s convenience, I’ll copy everything specific that APTAMI says about the Intrinsic Cost module. (Emphasis in original.)

> PAGES 7-8: The Intrinsic Cost module is hard-wired (immutable, non trainable) and computes a single scalar, the intrinsic energy that measures the instantaneous “discomfort” of the agent – think pain (high intrinsic energy), pleasure (low or negative intrinsic energy), hunger, etc. The input to the module is the current state of the world, produced by the perception module, or potential future states predicted by the world model. The ultimate goal of the agent is minimize the intrinsic cost over the long run. This is where basic behavioral drives and intrinsic motivations reside. The design of the intrinsic cost module determines the nature of the agent’s behavior. Basic drives can be hard-wired in this module. This may include feeling “good” (low energy) when standing up to motivate a legged robot to walk, when influencing the state of the world to motivate agency, when interacting with humans to motivate social behavior, when perceiving joy in nearby humans to motivate empathy, when having a full energy [supply] (hunger/satiety), when experiencing a new situation to motivate curiosity and exploration, when fulfilling a particular program, etc. Conversely, the energy would be high when facing a painful situation or an easily-recognizable dangerous situation (proximity to extreme heat, fire, etc), or when wielding dangerous tools. The intrinsic cost module may be modulated by the configurator, to drive different behavior at different times.

> PAGE 14: The intrinsic cost module (IC) is where the basic behavioral nature of the agent is defined. It is where basic behaviors can be indirectly specified.

> PAGE 44: What is the substrate of emotions in animals and humans? Instantaneous emotions (e.g. pain, pleasure, hunger, etc) may be the result of brain structures that play a role similar to the Intrinsic Cost module in the proposed architecture. Other emotions such as fear or elation may be the result of anticipation of outcome by brain structures whose function is similar to the Trainable Critic.

# 2. As described in the paper, several components of the AI’s Intrinsic Cost are directly opposed to AI controllability and prosociality

In AI alignment discourse, we often talk about “instrumental convergence”. If an AI really wants a thing X, then for almost any X, it will find it instrumentally useful (i.e., useful as a means to an end) to get control over its situation, gain power and resources, stay alive, prevent its desires from being exogenously changed, and so on. In Stuart Russell’s memorable quip, if an AI really wants to fetch the coffee, well, “you can’t fetch the coffee when you’re dead”, so the AI will fight for self-preservation (other things equal).

APTAMI specifically mentioned “hunger”, “pain”, and “curiosity” as three likely components of Intrinsic Cost (see Section 1 excerpts). All three of these have obvious “instrumental convergence” issues. Let’s go through them one at a time:

- If an AI is motivated to avoid hunger (say, implemented in source code by checking the battery charge state), and the AI reasons that humans might not want to recharge it, then the AI will be motivated to get power and control over its situation to eliminate that potential problem, e.g. by sweet-talking the humans into recharging it, or better yet maneuvering into a situation where it can recharge itself without asking anyone’s permission.
- If an AI is motivated to avoid pain, and the AI reasons that humans might cause it to experience pain, or be unable or unwilling to help it avoid future pain, then the AI will likewise be motivated to get power and control over its situation to eliminate that potential problem.
- If an AI is motivated by curiosity, and the AI reasons that humans might fail to offer it sufficiently novel and interesting things to do, then the AI will likewise be motivated to get power and control over its situation, so that it can go satisfy its curiosity without asking anyone’s permission.
Possible reply 1: “OK, granted, that’s a real problem, but it’s easy to fix, we’ll just remove those three things from the Intrinsic Cost module.”

My response: It’s not so easy. For one thing, curiosity in particular is plausibly essential for the AI to work at all. For another thing, as mentioned at the top, it’s not just about these three specific motivations. On the contrary, a wide variety of motivations lead to similar “instrumental convergence” problems, including important motivations like “wanting to design a better solar cell” that seem necessary for the AIs to do the things we want them to do.

Possibly reply 2: “Humans are motivated by hunger, pain, and curiosity, and can be perfectly lovely assistants and employees. Why would we be starving and hurting the AIs anyway?? Let’s just treat our AIs well!!”

My response: Humans have a lot of other motivations besides hunger, pain, and curiosity, including intrinsic motivations to kindness, friendship, norm-following, and so on. I’ll turn to those in the next section. If you’ve ever gotten to know a sociopath or narcissist, you'll know that they have hunger, pain, and curiosity too, but it is absolutely not the case that if you just treat them with kindness then they will be kind to you in return! They might act kind and cooperative as a means to an end, e.g. to gain your trust, but that’s not what we want—that’s the kind of “cooperation” where they stab you in the back as soon as the situation changes. We want our AIs to treat kindness as an end in itself. And that doesn’t happen unless we explicitly build such an intrinsic motivation into them. So let’s turn to that next.

# 3. As described in the paper, the components of the AI’s Intrinsic Cost that are supposed to motivate intrinsic kindness, are unlikely to actually work

Before we even start, it seems like a pretty dicey plan to build an AI that has numerous innate drives that are opposed to controllability and prosociality (as described in the previous section), plus other innate drives that advance controllability and prosociality (as I’ll discuss in this section). Such an AI would feel “torn”, so to speak, when deciding whether to advance its own goals versus humans’. We can hope that the prosocial drives will “win out” in the AI’s reckoning, but we don’t have any strong reason to expect that they will in fact win out. Neurotypical humans are a fine illustration—we have both prosocial drives and selfish drives, and as a result, sometimes humans do nice things, and also sometimes humans advance their own interests at the expense of others.

However, it’s much worse than that, because I claim we don’t know how to build prosocial innate drives at all in this kind of AI.

It’s clearly possible in principle—there’s some mechanism underpinning those drives inside the brains of non-psychopathic humans—but I claim it’s an open problem how these drives actually work.

(Or in APTAMI’s terminology, it’s an open problem exactly what code to put into the Intrinsic Cost module such that the AI will have any prosocial or docile motivations at all.)

APTAMI’s “proposal” here is really just a passing description in a few sentence fragments. But worse than that, as best as I can tell, this cursory description is not pointing towards a viable proposal, nor one that can be easily remedied.

I’ll repeat the relevant excerpts from above:

> This may include feeling “good” (low energy) … when interacting with humans to motivate social behavior, when perceiving joy in nearby humans to motivate empathy, …

It’s hard to respond to this because it’s so vague. Different things can go wrong depending on how the implementation is supposed to work in detail. I can make some guesses, but maybe the response will be “No you moron, that’s not what I meant”. Oh well, I’ll proceed anyway. If what I say below isn’t what the author had in mind, maybe he can share what he did have in mind, and then I can revise my description of what I think the problems are, and maybe we can have a productive back-and-forth.

My attempt to flesh out what LeCun might have in mind:

The robot has “eyes” & “ears” (a video feed with sound). We get some early test data of the robot doing whatever (say, flailing around randomly), and then send the video feed to a bunch of humans (say, Mechanical Turkers) to manually label the video frames using the following rubric (drawn from the excerpts above):

- “Am I interacting with humans?” (1-10)
- “Are nearby humans experiencing joy?” (1-10)
- “Am I in the company of humans?” (1-10)
- “Is a human praising me right now?” (1-10)
- “Is a human in pain right now?” (1-10)
Next, we do a weighted average of these scores (the first four with positive weight, the fifth with negative weight) and use supervised learning to train an ML model that can take any arbitrary video frame and assign it a score. Let’s call this trained deep neural net (DNN) the Prosociality Score Model. We freeze the weights of this classifier and put it inside the Intrinsic Cost module (to be added to the other terms like pain and curiosity, discussed above). Here we are so far:

My (uncertain) attempt to flesh out the vague proposal in APTAMI. If this isn’t what LeCun had in mind, I strongly encourage him to write out more specific pseudocode for the Intrinsic Cost module such that he thinks it will lead to an AI that has controllable and/or prosocial motivations. And then we can have a productive discussion about whether that pseudocode will actually work as intended.

Does this approach actually make an AI with prosocial motivations? I think the answer is a clear “no”.

For starters, suppose the AI straps lots of humans into beds, giving them endless morphine and heroin IV drips, and the humans get into such a state of delirium that they repeatedly praise and thank the AI for continuing to keep the heroin drip turned on.

This dystopian situation would be, to the AI, absolute ecstasy—much like the heroin to those poor humans. The Prosicality Score Model would (perhaps—see below) give

- 10/10 for “interacting with humans”,
- 10/10 for “being near humans experiencing joy”,
- 10/10 for “being in the company of humans”,
- 10/10 for “receiving praise”, and
- 0/10 for “being around humans in pain”.
Now, it doesn’t immediately follow that the AI will actually want to start buying chair-straps and heroin, for a similar reason as why I personally am not trying to get heroin right now. But it certainly raises that kind of AI behavior as a salient possibility, and in this particular instance my guess is that something in this general class of “failures” would be pretty likely to actualize. At the very least, I see no strong reason to believe that they won’t actualize.

On a more technical level, we face (among other things) the classic problem of out-of-distribution (OOD) generalization, and we face it not once but twice:[1]

- Out-of-distribution generalization problem 1: How does the Prosociality Score Model generalize from the supervised (human-labeled) examples to the AI’s future perceptions—which might be far outside that training distribution?
- Out-of-distribution generalization problem 2: How does the critic generalize from its past observations of Intrinsic Cost to estimate the Intrinsic Cost of future plans and situations—which, again, might be far outside the distribution of its past experience?
These problems are made worse because they are adversarial—with the adversary being the AI itself! Let me explain this adversarial aspect via some toy examples:

Why is problem 1 an “adversarial” OOD problem? Here’s a toy example. The AI might notice that it finds it pleasing to watch movies of happy people—because doing so spuriously triggers the Prosociality Score Model. Then the AI might find itself wanting to make its own movies to watch. As the AI fiddles with the settings in iMovie, it might find that certain texture manipulations make the movie really really pleasing to watch on loop—because it “tricks” the Prosociality Score Model into giving anomalously high scores.

What happened here was that the AI sought out and discovered “adversarial examples” for an immutable DNN buried deep inside its own “mind”.

(That particular example doesn’t seem very scary, until the AI notices that humans might want to turn off its weird-texture movie playing on loop. Then the situation gets “adversarial” in the more literal sense!)

Why is problem 2 an “adversarial” OOD problem? Here’s a toy example. Imagine that the AI is deciding what to do, out of a very wide possibility space. For example, once we get AIs that can invent new technology, then the AI has access to actions that might wildly change the world compared to anything in history. Thus, if there are any anomalies where the critic judges a weird course-of-action as unusually low-intrinsic-cost, then we’re in a situation where the AI’s brainstorming process is actively seeking out such anomalies.

(From our human perspective, we would say “this plan is exploiting an anomalous edge-case in the critic”. Whereas from the AI’s perspective, it would say, “this plan is a clever awesome out-of-the-box way to solve every problem!!” You say tomato, I say to-mah-to.[2])

Needless to say, robustness to adversarially-chosen wildly-out-of-distribution inputs is an unsolved problem in ML. So it’s probably safe to assume that, if we use the APTAMI plan (as I interpret it), the AI is probably going to wind up with weird and a-priori-unpredictable motivations. And this problem is not the kind of problem where we can just straightforwardly patch it once we have a reproducible test case running on our computers.

# 4. Conclusion

In Section 2 I argued that the AI (as described in APTAMI) will have at least some motivations (like hunger, pain, and curiosity) that run directly counter to controllability / steerability / prosociality, thanks to “instrumental convergence”. This might be OK if the AI also has other motivations that create controllability / steerability / prosociality (as is the case in humans, who are sometimes cooperative despite some selfish innate drives).

However, in Section 3 I argued that it's an open problem to write out an Intrinsic Cost function that will lead to any motivation for controllability / steerability / prosociality, and that APTAMI says only a few words about how to solve this problem, and that what little it says does not seem to be pointing in a promising direction. Instead, the paper's proposal seems likely to lead to AIs with weird and a-priori-unpredictable motivations. Indeed, I’d guess that these weird unpredictable motivations are more likely to contribute to “instrumental convergence” effects than to push against them. And this problem would be very difficult to patch even if we had a working minimal test case on our computers, because wildly-out-of-distribution adversarial robustness is an open problem in ML, and there is no obvious better alternative approach.

So we have a very interesting, open technical problem here: “Exactly what code should we put into the Intrinsic Cost module [in conjunction with other design choices, e.g. training environment], such that we have strong reason to believe that we’ll be pleased with the AI that results?” In fact, I myself have a full-time job in which I spend most of my days trying to work towards an answer to this question, and have been doing so for years. It is a very hard problem.

I think that LeCun himself is more qualified than most to work on this technical problem, and I think we already have all the information we need to make progress, so I would strongly encourage him and his colleagues to dive in. I humbly offer my Intro to Brain-Like AGI Safety series as a potentially useful starting point / resource in this context, since LeCun and I share many assumptions about what autonomous machine intelligence will look like, and hence I imagine he’d find it somewhat less difficult to relate to than most AI alignment documents. And I would be happy to chat more! :)

# Epilogue: We need to do better than a cursory treatment of this technical problem, even in the context of a very-early-stage speculative vision paper

OK, if you’ve read this far, then maybe you’re thinking something along the following lines:

> So, Yann LeCun published a self-described ‘position paper’ expressing a ‘vision for a path towards intelligent machines’. He was explicitly intending to spur discussion and solicit feedback, even posting it on openreview.net rather than arxiv. And now this other guy has written a blog post saying that one aspect of the vision is more complicated and difficult to get right than implied by the very brief paper discussion.

I disagree—I think that if you were nodding along with the above paragraphs then you have lost sight of something very important.

APTAMI is an attempt to describe a path towards powerful AI—AI that can understand the world, get things done, figure things out, make plans, pivot when the plans fail, build tools to solve their problems, and so on—all the things that would make us think of the AIs intuitively as “a new intelligent species” rather than “an AI system as we think of it today”.

Figure is modified from this post—see there for further discussion

Suppose someone published a position paper describing “a vision for a path towards using bioengineering to create a new intelligent nonhuman species”. And suppose that the question of how to make this new species care about humans and/or stay under human control is relegated to a vague and cursory discussion in a few sentences, and close examination reveals that if we were to follow the advice in those few sentences then we would probably get a highly-intelligent nonhuman species pursuing its own interests with callous disregard for human welfare—somewhat akin to a species of high-functioning sociopaths.

If that someone says “Yeah sure, obviously there are still lots of details to work out”, then I would respond: “No no no! The question of how to design this new species such that they will be docile and/or intrinsically care about human welfare is not just one of many technical details to be worked out! This is the kind of problem where we halt all other work on this research program until we have sorted this out.”

That seems like common sense to me. If not, consider:

- For one thing, we don’t actually know for sure that this technical problem is solvable at all, until we solve it. And if it’s not in fact solvable, then we should not be working on this research program at all. If it's not solvable, the only possible result of this research program would be “a recipe for summoning demons”, so to speak. And if you’re scientifically curious about what a demon-summoning recipe would look like, then please go find something else to be scientifically curious about instead.
- For another thing, this technical alignment problem could be the kind of technical problem that takes a long time to solve, even assuming we have the benefit of trial-and-error. If we make progress on every other aspect of the research program first, while taking a “we’ll cross that bridge when we get to it” attitude on how exactly to code up the Intrinsic Cost module, then we could wind up in a situation where we have discovered (perhaps even open-sourced) a recipe for building self-interested AIs with callous disregard for humanity, but we have not yet discovered any analogous recipe for building friendly powerful AIs that might help us and fight on our side. That’s a bad situation. And we can avoid that situation by doing the requisite research in the right order.
- Finally, if Yann LeCun were merely treating this open technical problem in a cursory way, and proposing approaches that are technically flawed upon close scrutiny, then that would at least be somewhat understandable. I myself propose technically-flawed plans all the time! A bigger issue is that LeCun, in his public statements, gives a strong impression that he is opposed to people working on this technical problem. If my impression here is wrong—if LeCun in fact thinks that the open technical problem described in this post is a worthwhile thing for AI researchers to be working on—then I appeal to him to directly and straightforwardly say that. It would make a huge difference.
(Thanks Christopher King, Roman Leventov, & Justis Mills for critical comments on earlier drafts.)

1. ^
1. ^

