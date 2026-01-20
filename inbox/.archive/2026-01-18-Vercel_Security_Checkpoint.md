---
type: link
source: notion
url: https://www.lesswrong.com/posts/ZBoJaebKFEzxuhNGZ/on-dwarkesh-patel-s-podcast-with-andrej-karpathy
notion_type: Tech Deep Dive
tags: ['Running']
created: 2025-10-22T02:36:00.000Z
---

# Vercel Security Checkpoint

## Overview (from Notion)
- The discussion on AGI timelines suggests that while rapid advancement is expected, the impact on everyday life and work could be slow and gradual, allowing you to adapt as a software engineer and founder.
- Ideas around continual learning and model collapse relate directly to how you approach software development; consider how you foster a learning environment in your team.
- The podcast touches on the limitations of current AI tools, which might resonate with your experiences in coding and project management—tools can assist but often require human oversight.
- The debate between automation as a gradual transition versus a sudden leap can influence your business strategy; think about how to leverage incremental AI improvements without over-relying on them.
- The notion of human intelligence evolving alongside technology highlights the importance of personal growth and continuous education for you and your children in a rapidly changing world.
- Consider the implications of AI in education—it's a chance to rethink how you teach your kids about technology and critical thinking, preparing them for a future where AI plays a significant role.
- Different viewpoints on AGI's economic impact can help you strategize your business's direction; whether AI leads to job displacement or creates new opportunities will shape your planning and investments.
- Reflect on how AI might influence your family life—balancing screen time and learning could become even more crucial as technology evolves.

## AI Summary (from Notion)
The discussion revolves around the future of AI, particularly the timeline for achieving AGI, which Andrej Karpathy suggests is still a decade away. Key points include the limitations of current AI agents, the importance of continual learning, and the challenges in replicating human-like intelligence. The conversation also critiques the effectiveness of reinforcement learning and highlights the potential for AI to enhance productivity, despite skepticism about its immediate impact on GDP growth. Overall, there is a tension between optimistic and pessimistic views on AI's future capabilities and societal implications.

## Content (from Notion)

Some podcasts are self-recommending on the ‘yep, I’m going to be breaking this one down’ level. This was very clearly one of those. So here we go.

As usual for podcast posts, the baseline bullet points describe key points made, and then the nested statements are my commentary.

If I am quoting directly I use quote marks, otherwise assume paraphrases.

Rather than worry about timestamps, I’ll use YouTube’s section titles, as it’s not that hard to find things via the transcript as needed.

This was a fun one in many places, interesting throughout, frustrating in similar places to where other recent Dwarkesh interviews have been frustrating. It gave me a lot of ideas, some of which might even be good.

Double click to interact with video

### AGI Is Still a Decade Away

1. Andrej calls this the ‘decade of agents’ contrary to (among others who have said it) the Greg Brockman declaration that 2025 is the ‘year of agents,’ as there is so much work left to be done. Think of AI agents as employees or interns, that right now mostly can’t do the things due to deficits of intelligence and context. 
1. Dwarkesh points to lack of continual learning or multimodality, but notes it’s hard to tell how long it will take. Andrej says ‘well I have 15 years of prediction experience and intuition and I average things out and it feels like a decade to me.’ 
1. AI has had a bunch of seismic shifts, Andrej has seen at least two and they seem to come with regularity. Neural nets used to be a niche thing before AlexNet but they were still trained per-task, the focus on Atari and other games was a mistake because you want to interact with the ‘real world’. Then LLMs. The common mistake was trying to “get the full thing too early” and especially aiming at agents too soon. 
1. Dwarkesh asks what about the Sutton perspective, should you be able to throw an AI out there into the world the way you would a human or animal and just work with and ‘grow up’ via sensory data? Andrej points to his response to Sutton, that biological brains work via a very different process, we’re building ghosts not animals, although we should make them more ‘animal-like’ over time. But animals don’t do what Sutton suggests, they use an evolutionary outer loop. Animals only use RL for non-intelligence tasks, things like motor skills. 
1. Dwarkesh contrasts pre-training with evolution in that evolution compacts all info into 3 GB of DNA, thus evolution is closer to finding a lifetime learning algorithm. Andrej agrees there is miraculous compression in DNA and that it includes learning algorithms, but we’re not here to build animals, only useful things, and they’re ‘crappy’ but what know how to build are the ghosts. Dwarkesh says evolution does not give us knowledge, it gives us the algorithm to find knowledge a la Sutton. 
1. Andrej draws a distinction between the neural net picking up all the knowledge in its training data versus it becoming more intelligent, and often you don’t even want the knowledge, we rely on it too much, and this is part of why agents are bad at “going off the data manifold of what exists on the internet.” We want the “cognitive core.” 
1. Dwarkesh reiterates in-context learning as ‘the real intelligence’ as distinct from gradient descent. Andrej agrees it’s not explicit, it’s “pattern completion within a token window” but notes there’s tons of patterns on the internet that get into the weights, and it’s possible in-context learning runs a small gradient descent loop inside the neural network. Dwarkesh asks, “why does it feel like with in-context learning we’re getting to this continual learning, real intelligence-like thing? Whereas you don’t get the analogous feeling just from pre-training.” 
1. Dwarkesh asks, how much of the information from training gets stored in the model? He compares KV cache of 320 kilobytes to a full 70B model trained on 15 trillion tokens. Andrej thinks models get a ‘hazy recollection’ of what happened in training, the compression is dramatic to get 15T tokens into 70B parameters. 
1. What part about human intelligence have we most failed to replicate? Andrej says ‘a lot of it’ and starts discussing physical brain components causing “these cognitive deficits that we all intuitively feel when we talk to them models.” 
1. Dwarkesh turns back to continual learning, asks if it will emerge spontaneously if the model gets the right incentives. Andrej says no, that sleep does this for humans where ‘the context window sometimes sticks around’ and there’s no natural analog, but we want a way to do this, and points to sparse attention. 
1. Andrej kind of goes Lindy, pointing to translation invariance to expect algorithmic and other changes at a similar rate to the past, and pointing to the many places he says we’d need gains in order to make further progress, that various things are ‘all surprisingly equal,’ it needs to improve ‘across the board.’ 
### LLM Cognitive Deficits

1. Andrej found LLMs of little help when assembling his new repo nanochat, which is a an 8k-line set of all the things you need for a minimal ChatGPT clone. He still used autocomplete, but vibe coding only works with boilerplate stuff. In particular, the models ‘remember wrong’ from all the standard internet ways of doing things, that he wasn’t using. For example, he did his own version of a DDP container inside the code, and the models couldn’t comprehend that and kept trying to use DDP instead. Whereas he only used vibe coding for a few boilerplate style areas. 
1. “I also feel like it’s annoying to have to type out what I want in English because it’s too much typing. If I just navigate to the part of the code that I want, and I go where I know the code has to appear and I start typing out the first few letters, autocomplete gets it and just gives you the code. This is a very high information bandwidth to specify what you want.” 
1. Putting it together: LLMs are very good at code that has been written many times before, and poor at code that has not been written before, in terms of the structure and conditions behind the code. Code that has been written before on rare occasions is in between. The modes are still amazing, and can often help. On the vibe coding: “I feel like the industry is making too big of a jump and is trying to pretend like this is amazing, and it’s not. It’s slop.” 
1. Andrej sees all of computing as a big recursive self-improvement via things like code editors and syntax highlighting and even data checking and search engines, in a way that is continuous with AI. Better autocomplete is the next such step. We’re abstracting, but it is slow. 
### RL Is Terrible

1. How should we think about humans being able to build a rich world model from interactions with the environment, without needing final reward? Andrej says they don’t do RL, they do something different, whereas RL is terrible but everything else we’ve tried has been worse. All RL can do is check the final answers, and say ‘do more of this’ when it works. A human would evaluate parts of the process, an LLM can’t and won’t do this. 
1. Dwarkesh does ask why, or at least about process supervision. Andrej says it is tricky how to do that properly, how do you assign credit to partial solutions? Labs are trying to use LLM judges but this is actually subtle, and you’ll run into adversarial examples if you do it for too long. It finds out that dhdhdhdh was an adversarial example so it starts outputting that, or whatever. 
1. So train models to be more robust? Find the adversarial examples and fix them one at a time won’t work, there will always be another one. 
### How Do Humans Learn?

1. What about the thing where humans sleep or daydream, or reflect? Is there some LLM analogy? Andrej says basically no. When an LLM reads a book it predicts the next token, when a human does they do synthetic data generation, talk about it with their friends, manipulate the info to gain knowledge. But doing this with LLMs is nontrivial, for reasons that are subtle and hard to understand, and if you generate synthetic data to train on that makes the model worse, because the examples are silently collapsed, similar to how they know like 3 total jokes. LLMs don’t retain entropy, and we don’t know how to get them to retain it. “I guess what I’m saying is, say we have a chapter of a book and I ask an LLM to think about it, it will give you something that looks very reasonable. But if I ask it 10 times, you’ll notice that all of them are the same. Any individual sample will look okay, but the distribution of it is quite terrible.” 
1. “I think that there’s possibly no fundamental solution to this. I also think humans collapse over time. These analogies are surprisingly good. Humans collapse during the course of their lives. This is why children, they haven’t overfit yet… We end up revisiting the same thoughts. We end up saying more and more of the same stuff, and the learning rates go down, and the collapse continues to get worse, and then everything deteriorates.” 
1. Could dreaming be a way to avoid mode collapse by going out of distribution? 
1. Andrej notes you should always be seeking entropy in your life, suggesting talking to other people. 
1. What’s up with children being great at learning, especially things like languages, but terrible at remembering experiences or specific information? LLMs are much better than humans at memorization, and this can be a distraction. 
1. How do you solve model collapse? Andrej doesn’t know, the models be collapsed, and Dwarkesh points out RL punishes output diversity. Perhaps you could regularize entropy to be higher, it’s all tricky.
1. Andrej says state of the art models have gotten smaller, and he still thinks they memorized too much and we should seek a small cognitive core. 
1. Most of the internet tokens are total garbage, stock tickers, symbols, huge amounts of slop, and you basically don’t want that information. 
1. They go back and forth over the size of the supposed cognitive core, Dwarkesh asks why not under 1 billion, Andrej says you probably need a billion knobs and he’s already contrarian being that low. 
### AGI Will Blend Into 2% GDP Growth

Wait what?

Note: The 2% number doesn’t actually come up until the next section on ASI.

1. How to measure progress? Andrej doesn’t like education level as a measure of AI progress (I agree), he’s also not a fan of the famous METR horizon length graph and is tempted to reject the whole question. He’s sticking with AGI as ‘can do any economically valuable task at human performance or better.’ 
1. He says only 10%-20% of the economy is ‘only knowledge work.’ 
1. Andrej points to the famous predictions of automating radiology, and suggests what we’ll do more often is have AI do 80% of the volume, then delegate 20% to humans. 
1. Dwarkesh compares radiologists to early Waymos where they had a guy in the front seat that never did anything so people felt better, and similarly if an AI can do 99% of a job the human doing the 1% can still be super valuable because bottleneck. Andrej points out radiology turns out to be a bad example for various reasons, suggests call centers. 
1. Dwarkesh points out that we don’t seem to be on an AGI paradigm, we’re not seeing large productivity improvements for consultants and accountants. Whereas coding was a perfect fit for a first task, with lots of ready-made places to slot in an AI. 
1. Dwarkesh says Andy Matuschak tried 50 billion things to get LLMs to write good spaced repetition prompts, and they couldn’t do it. 
### ASI

1. What about superintelligence? “I see it as a progression of automation in society. Extrapolating the trend of computing, there will be a gradual automation of a lot of things, and superintelligence will an extrapolation of that. We expect more and more autonomous entities over time that are doing a lot of the digital work and then eventually even the physical work some amount of time later. Basically I see it as just automation, roughly speaking.” 
1. Dwarkesh pushes back: “But automation includes the things humans can already do, and superintelligence implies things humans can’t do.” Andrej gives a strange answer: “But one of the things that people do is invent new things, which I would just put into the automation if that makes sense.” 
1. Andrej worries about a gradual loss of control and understanding of what is happening, and thinks this is the most likely outcome. Multiple competing entities, initially competing on behalf of people, that gradually become more autonomous, some go rogue, others fight them off. They still get out of control. 
1. Dwarkesh asks, will we see an intelligence explosion if we have a million copies of you running in parallel super fast? Andrej says yes, but best believe in intelligence explosions because you’re already living in one and have been for decades, that’s why GDP grows, this is all continuous with the existing hyper-exponential trend, previous techs also didn’t make GDP go up much, everything was slow diffusion. 
1. “We’re still going to have an exponential that’s going to get extremely vertical. It’s going to be very foreign to live in that kind of an environment.” … “Yes, my expectation is that it stays in the same [2% GDP growth rate] pattern.” 
1. “Self-driving as an example is also computers doing labor. That’s already been playing out. It’s still business as usual.” 
1. Karpathy keeps saying this will all be gradual capabilities gains and gradual diffusion, with no discrete jump. He suggests you would need some kind of overhang being unlocked such as a new energy source to see a big boost. 
I won’t go further into the same GDP growth or intelligence explosion arguments I seem to discuss in many Dwarkesh Patel podcast posts. I don’t think Andrej has a defensible position here, in the sense that he is doing some combination of denying the premise of AGI/ASI, not taking into account its implications in some places while acknowledging the same dynamics in others.

Most of all, this echoes the common state of the discourse on such questions, which seems to involve:

1. You, the overly optimistic fool, say AGI will arrive in 2 years, or 5 years, and you say that when it happens it will be a discrete event and then everything changes. 
1. I, the wise world weary realist, say AGI will only arrive in 10 years, and it will be a gradual, continuous thing with no discrete jumps, facing physical bottlenecks and slow diffusion.
1. So therefore we won’t see a substantial change to GDP growth, your life will mostly seem normal, there’s no risk of extinction or loss of control, and so on, building sufficiently advanced technology of minds smarter, faster, cheaper and more competitive than ourselves along an increasing set of tasks will go great.
1. Alternatively, I, the proper cynic, realize AI is simply a ‘normal technology’ and it’s ‘just automation of some tasks’ and they will remain ‘mere tools’ and what are you getting on about, let’s go build some economic models.
I’m fine with those who expect to at first encounter story #2 instead of story #1.

Except it totally, absolutely does not imply #3. Yes, these factors can slow things down, and 10 years are more than 2-5 years, but 10 years is still not that much time, and a continuous transition ends up in the same place, and tacking on some years for diffusion also ends up in the same place. It buys you some time, which we might be able to use well, or we might not, but that’s it.

What about story #4, which to be clear is not Karpathy’s or Patel’s? It’s possible that AI progress stalls out soon and we get a normal technology, but I find it rather unlikely and don’t see why we should expect that. I think that it is quite poor form to treat this as any sort of baseline scenario.

### Evolution of Intelligence and Culture

1. Dwarkesh pivots to Nick Lane. Andrej is surprised evolution found intelligence and expects it to be a rare event among similar worlds. Dwarkesh suggests we got ‘squirrel intelligence’ right after the oxygenation of the atmosphere, which Sutton said was most of the way to human intelligence, yet human intelligence took a lot longer. They go over different animals and their intelligences. You need things worth learning but not worth hardcoding.
1. Andrej notes LLMs don’t have a culture, suggests it could be a giant scratchpad. 
1. Andrej mentions self-play, says that he thinks the models can’t create culture because they’re ‘still kids.’ Savant kids, but still kids. 
### Why Self Driving Took So Long

1. Andrej was at Tesla leading self-driving from 2017 to 2022. Why did self-driving take a decade? Andrej says it isn’t done. It’s a march of nines (of reliability). Waymo isn’t economical yet, Tesla’s approach is more scalable, and to be truly done would mean people wouldn’t need a driver’s license anymore. But he agrees it is ‘kind of real.’ 
1. They draw parallels to AI and from AI to previous techs. Andrej worries we may be overbuilding compute, he isn’t sure, says he’s bullish on the tech but a lot of what he sees on Twitter makes no sense and is about fundraising or attention. 
1. “I’m just reacting to some of the very fast timelines that people continue to say incorrectly. I’ve heard many, many times over the course of my 15 years in AI where very reputable people keep getting this wrong all the time. I want this to be properly calibrated, and some of this also has geopolitical ramifications and things like that with some of these questions. I don’t want people to make mistakes in that sphere of things. I do want us to be grounded in the reality of what technology is and isn’t.” 
### Future Of Education

1. Dwarkesh asks about Eureka Labs. Why not AI research? Andrej says he’s not sure he could improve what the labs are doing. He’s afraid of a WALL-E or Idiocracy problem where humans are disempowered and don’t do things. He’s trying to build Starfleet Academy. 
1. Dwarkesh Patel hasn’t seen Star Trek. 
1. Andrej thinks AI will fundamentally change education, and it’s still early. Right now you have an LLM, you ask it questions, that’s already super valuable but it still feels like slop, he wants an actual tutor experience. He learned Korean from a tutor 1-on-1 and that was so much better than a 10-to-1 class or learning on the internet. The tutor figured out where he was as a student, asked the right questions, and no LLM currently comes close. Right now they can’t. 
1. His first class is LLM-101-N, with Nanochat as the capstone. 
1. Dwarkesh points out that if you can self-probe well enough you can avoid being stuck. Andrej contrasts LLM-101-N with his CS231n at Stanford on deep learning, that LLMs really empower him and help him go faster. Right now he’s hiring faculty but over time some TAs can become AIs.
1. “I often say that pre-AGI education is useful. Post-AGI education is fun. In a similar way, people go to the gym today. We don’t need their physical strength to manipulate heavy objects because we have machines that do that. They still go to the gym. Why do they go to the gym? Because it’s fun, it’s healthy, and you look hot when you have a six-pack. It’s attractive for people to do that in a very deep, psychological, evolutionary sense for humanity. Education will play out in the same way. You’ll go to school like you go to the gym.”
1. “If you look at, for example, aristocrats, or you look at ancient Greece or something like that, whenever you had little pocket environments that were post-AGI in a certain sense, people have spent a lot of their time flourishing in a certain way, either physically or cognitively. I feel okay about the prospects of that. If this is false and I’m wrong and we end up in a WALL-E or Idiocracy future, then I don’t even care if there are Dyson spheres. This is a terrible outcome. I really do care about humanity. Everyone has to just be superhuman in a certain sense.” 
1. “I think there will be a transitional period where we are going to be able to be in the loop and advance things if we understand a lot of stuff. In the long-term, that probably goes away.” 
1. Dwarkesh asks about teaching. Andrej says everyone should learn physics early, since early education is about booting up a brain. He looks for first or second order terms of everything. Find the core of the thing and understand it. 
1. Curse of knowledge is a big problem, if you’re an expert in a field often you don’t know what others don’t know. Could be helpful to see other people’s dumb questions that they ask an LLM?
1. From Dwarkesh: “Another trick that just works astoundingly well. If somebody writes a paper or a blog post or an announcement, it is in 100% of cases that just the narration or the transcription of how they would explain it to you over lunch is way more, not only understandable, but actually also more accurate and scientific, in the sense that people have a bias to explain things in the most abstract, jargon-filled way possible and to clear their throat for four paragraphs before they explain the central idea. But there’s something about communicating one-on-one with a person which compels you to just say the thing.” 
### Reactions

Peter Wildeford offers his one page summary, which I endorse as a summary.

Sriram Krishnan highlights part of the section on education, which I agree was excellent, and recommends the overall podcast highly.

Andrej Karpathy offered his post-podcast reactions here, including a bunch of distillations, highlights and helpful links.

Here’s his summary on the timelines question:

> Andrej Karpathy: Basically my AI timelines are about 5-10X pessimistic w.r.t. what you’ll find in your neighborhood SF AI house party or on your twitter timeline, but still quite optimistic w.r.t. a rising tide of AI deniers and skeptics

Those house parties must be crazy, as must his particular slice of Twitter. He has AGI 10 years away and he’s saying that’s 5-10X pessimistic. Do the math.

My slice currently overall has 4-10 year expectations. The AI 2027 crowd has some people modestly shorter, but even they are now out in 2029 or so I think.

That’s how it should work, evidence should move the numbers back and forth, and if you had a very aggressive timeline six months or a year ago recent events should slow your roll. You can say ‘those people were getting ahead of themselves and messed up’ and that’s a reasonable perspective, but I don’t think it was obviously a large mistake given what we knew at the time.

> Peter Wildeford: I’m desperate for a worldview where we agree both are true:

I agree with the second point (with error bars). The first point I would rate as ‘somewhat true.’ Much of the marketing is BS and much of the output is slop, no question, but much of it is not on either front and the models are already extremely helpful to those who use them.

> Peter Wildeford: If the debate truly has become

Similarly, the first position here is obviously wrong, and the second position could be right on the substance but has one hell of a Missing Mood, 10-20 years before all jobs get automated is kind of the biggest thing that happened in the history of history even if the process doesn’t kill or diempower us.

> Rob Miles: It’s strange that the “anti hype” position is now “AGI is one decade away”. That… would still be a very alarming situation to be in? It’s not at all obvious that that would be enough time to prepare.

It’s so crazy the amount to which vibes can supposedly shift when objectively nothing has happened and even the newly expressed opinions aren’t so different from what everyone was saying before, it’s that now we’re phrasing it as ‘this is long timelines’ as opposed to ‘this is short timelines.’

> John Coogan: It’s over. Andrej Karpathy popped the AI bubble. It’s time to rotate out of AI stocks and focus on investing in food, water, shelter, and guns. AI is fake, the internet is overhyped, computers are pretty much useless, even the steam engine is mid. We’re going back to sticks and stones.

Yep, I read Altman as ~10 years there as well. Except that Altman was approaching that correctly as ‘quickly, there’s no time’ rather than ‘we have all the time in the world.’

> There’s a whole chain of AGI-soon bears who feel vindicated by Andrej’s comments and the general vibe shift. Yann LeCun, Tyler Cowen, and many others on the side of “progress will be incremental” look great at this moment in time.

It’s so crazy to think a big tech company would think ‘oops, it’s over, Dwarkesh interviews said so’ and regret or pull back on investment, also yeah it’s weird that Amazon was up 1.6% while AWS was down.

> Danielle Fong: aws down, amazon up

Why would you give Hotz credit for ‘GPT-12 won’t be AGI’ here, when the timeline for GPT-12 (assuming GPT-11 wasn’t AGI, so we’re not accelerating releases yet) is something like 2039? Seems deeply silly. And yet here we are. Similarly, people supposedly ‘look great’ when others echo previous talking points? In my book, you look good based on actual outcomes versus predictions, not when others also predict, unless you are trading the market.

I definitely share the frustration Liron had here:

> Liron Shapira: Dwarkesh asked Karpathy about the Yudkowskian observation that exponential economic growth to date has been achieved with *constant* human-level thinking ability.

In short, I don’t think a reasonable extrapolation from above plus AGI is ~2%.

But hey, that’s the way it goes. It’s been a fun one.


