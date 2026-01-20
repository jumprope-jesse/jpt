---
type: link
source: notion
url: https://www.lesswrong.com/posts/SNBE9TXwL3qQ3TS8H/ai-91-deep-thinking
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-11-21T16:17:00.000Z
---

# AI #91: Deep Thinking — LessWrong

## Overview (from Notion)
- AI's Role in Daily Life: Consider how advancements in AI can enhance your family life—think of AI as a personal assistant for parenting, helping manage schedules or educational content for your kids.

- Work-Life Balance: Explore the potential of AI tools to streamline your software engineering tasks, allowing more time for family and personal interests.

- Ethical Considerations: Reflect on the implications of AI in your work. As a founder, consider how your software products can address ethical concerns, such as data privacy and bias.

- Community Engagement: Engage with local tech communities in NYC to explore collaborative projects that leverage AI for community benefit, like educational initiatives for schools.

- Future of Work: Stay informed about discussions on job displacement due to AI. This can guide your career decisions and shape your company's mission to prioritize human-AI collaboration.

- Diverse Perspectives: Explore alternative views on AI, such as skepticism about its rapid integration into daily life versus the optimism of AI's potential to solve complex problems.

- Personal Growth: Embrace opportunities for continuous learning about AI and its applications, which can enhance your skills and lead your company in innovative directions.

## AI Summary (from Notion)
DeepSeek has released a clone of OpenAI's o1 model, showing promising benchmarks but lacking user feedback for full validation. Incremental upgrades in AI models continue, with GPT-4o and Gemini trading top positions. Discussions on AI policy under the Trump administration highlight the need for careful approaches to avoid destructive moves. The US-China commission emphasizes a competitive race to AGI, raising concerns about the implications. Various evaluations of AI models reveal strengths and weaknesses, while the potential for AI-driven cybercrime emerges. The conversation around AI's impact on jobs and societal meaning continues, with debates on regulation and the future of human roles in an AI-dominated landscape.

## Content (from Notion)

Did DeepSeek effectively release an o1-preview clone within nine weeks?

The benchmarks largely say yes. Certainly it is an actual attempt at a similar style of product, and is if anything more capable of solving AIME questions, and the way it shows its Chain of Thought is super cool. Beyond that, alas, we don’t have enough reports in from people using it. So it’s still too soon to tell. If it is fully legit, the implications seems important.

Small improvements continue throughout. GPT-4o and Gemini both got incremental upgrades, trading the top slot on Arena, although people do not seem to much care.

There was a time everyone would be scrambling to evaluate all these new offerings. It seems we mostly do not do that anymore.

The other half of events was about policy under the Trump administration. What should the federal government do? We continue to have our usual fundamental disagreements, but on a practical level Dean Ball offered mostly excellent thoughts. The central approach here is largely overdetermined, you want to be on the Pareto frontier and avoid destructive moves, which is how we end up in such similar places.

Then there’s the US-China commission, which now have their top priority being an explicit ‘race’ to AGI against China, without actually understanding what that would mean or justifying that anywhere in their humongous report.

### Table of Contents

1. Table of Contents.
1. Language Models Offer Mundane Utility. Get slightly more utility than last week.
1. Language Models Don’t Offer Mundane Utility. Writing your court briefing.
1. Claude Sonnet 3.5.1 Evaluation. Its scored as slightly more dangerous than before.
1. Deepfaketown and Botpocalypse Soon. AI boyfriends continue to be coming.
1. Fun With Image Generation. ACX test claims you’re wrong about disliking AI art.
1. O-(There are)-Two. DeepSeek fast follows with their version of OpenAI’s o1.
1. The Last Mile. Is bespoke human judgment going to still be valuable for a while?
1. They Took Our Jobs. How to get ahead in advertising, and Ben Affleck is smug.
1. We Barely Do Our Jobs Anyway. Why do your job when you already don’t have to?
1. The Art of the Jailbreak. Getting an AI agent to Do Cybercrime.
1. Get Involved. Apply for OpenPhil global existential risk portfolio manager.
1. The Mask Comes Off. Some historical emails are worth a read.
1. Richard Ngo on Real Power and Governance Futures. Who will have the power?
1. Introducing. Stripe SDK, Anthropic prompt improver, ChatGPT uses Mac apps.
1. In Other AI News. Mistral has a new model too, and many more.
1. Quiet Speculations. What will happen with that Wall?
1. The Quest for Sane Regulations. The conservative case for alignment.
1. The Quest for Insane Regulations. The US-China commission wants to race.
1. Pick Up the Phone. Is China’s regulation light touch or heavy? Unclear.
1. Worthwhile Dean Ball Initiative. A lot of agreement about Federal options here.
1. The Week in Audio. Report on Gwern’s podcast, also I have one this week.
1. Rhetorical Innovation. What are the disagreements that matter?
1. Pick Up the Phone. At least we agree not to hand over the nuclear weapons.
1. Aligning a Smarter Than Human Intelligence is Difficult. How’s it going?
1. People Are Worried About AI Killing Everyone. John von Neumann.
1. The Lighter Side. Will we be able to understand each other?
### Language Models Offer Mundane Utility

Briefly on top of Arena, Gemini-Exp-1114 took a small lead over various OpenAI models, also taking #1 or co-#1 on math, hard prompts, vision and creative writing.

Then GPT-4o got an upgrade and took the top spot back.

> OpenAI: The model’s creative writing ability has leveled up–more natural, engaging, and tailored writing to improve relevance & readability.

It’s also an improvement on MinecraftBench, but two out of two general replies on Twitter so far said this new GPT-4o didn’t seem that different.

Arena is no longer my primary metric because it seems to make obvious mistakes – in particular, disrespecting Claude Sonnet so much – but it is still measuring something real, and this is going to be a definite improvement.

CORE-Bench new results show Claude Sonnet clear first at 37.8% pass rate on agent tasks, with o1-mini in second at 24.4%, versus previous best of 21.5% by GPT-4o. Sonnet also has a 2-to-1 cost advantage over o1-mini. o1-preview exceeded the imposed cost limit.

METR runs an evaluation of the ability of LLMs to conduct AI research, finds Claude Sonnet 3.5 outperforms o1-preview on five out of seven tasks.

The trick is to ask the LLM first, rather than (only) last:

> Agnes Callard: My computer was weirdly broken so I called my husband and we tried a bunch of things to fix it but nothing worked and he had to go to bed (time diff, I am in Korea) so in desperation (I need it for a talk I’m giving in an hour) I asked chat gpt and its first suggestion worked!

Diagnose yourself, since ChatGPT seems to outperform doctors, and if you hand the doctor a one-pager with all the information and your ChatGPT diagnosis they’re much more likely to get the right answer.

> • ChatGPT scored 90 percent, while physicians scored 74–76 percent in diagnosing cases.

I love the social engineering of handing the doctor a one pager. You don’t give them a chance to get attached to a diagnosis first, and you ensure you get them the key facts, and the ‘get them the facts’ lets the doctor pretend they’re not being handed a diagnosis.

Use voice mode to let ChatGPT (or Gemini) chat with your 5-year-old and let them ask it questions. Yes, you’d rather a human do this, especially yourself, but one cannot always do that, and anyone who yells ‘shame’ should themselves feel shame. Do those same people homeschool their children? Do they ensure they have full time aristocratic tutoring?

Regular humans cannot distinguish AI poems from poems by some of the most famous human poets, and actively prefer the AI poems in many ways, including thinking them more likely to be human – so they can distinguish to a large extent, they just get the sign wrong. Humans having somewhat more poetry exposure did not help much either. The AI poems being more straightforward is cited as an advantage, as is the human poems often being old, with confusing references that are often dealing with now-obscure things.

So it sounds like a poetry expert, even if they hadn’t seen the exact poems in question, would be able to distinguish the poems and would prefer the human ones, but would also say that most humans have awful taste in poetry.

### Language Models Don’t Offer Mundane Utility

> Frank Bednarz, presumably having as much fun as I was: Crazy, true story: Minnesota offered an expert declaration on AI and “misinformation” to oppose our motion to enjoin their unconstitutional law.

If you can’t use AI during your coding interview, do they know if you can code?

Humans attach too much importance to when AIs fail tasks that are easy for humans, and are too impressed when they do things that are hard for humans, paper confirms. You see this all over Twitter, especially on new model releases – ‘look at this idiot model that can’t even do [X].’ As always, ask what it can do, not what it can’t do, but also don’t be too impressed if it’s something that happens to be difficult for humans.

Meta adds ‘FungiFriend’ AI bot to a mushroom forager group automatically, without asking permission, after which it proceeded to give advice on how to cook mushrooms that are not safe to consume, while claiming they were ‘edible but rare.’ Where the central point of the whole group is to ensure new foragers don’t accidentally poison themselves.

Experiment sees only gpt-3.5-turbo-instruct put up even a halfway decent chess game against low-level Stockfish, whereas every other model utterly failed. And we mean rather low-level Stockfish, the game I sampled was highly unimpressive. Of course, this can always be largely a skill issue, as Will Depue notes even a little fine tuning makes a huge difference.

### Claude Sonnet 3.5.1 Evaluation

Joint US AISI and UK AISI testing of the upgraded Claude 3.5:

> Divyansh Kaushik: On bio: Sonnet 3.5 underperforms human experts in most biological tasks but excels in DNA and protein sequence manipulation with tool access. Access to computational biology tools greatly enhances performance.

On safeguard efficiency, meaning protection against jailbreaks, they found that its defenses were routinely circumvented, as they indeed often are in practice:

> 

### Deepfaketown and Botpocalypse Soon

The latest round of AI boyfriend talk, with an emphasis on their rapid quality improvements over time. Eliezer again notices that AI boyfriends seem to be covered much more sympathetically than AI girlfriends, with this article being a clear example. I remain in the group that expects the AI boyfriends to be more popular and a bigger issue than AI girlfriends, similar to ‘romance’ novels.

Aella finally asked where the best LLMs are for fully uncensored erotica. Suggestions from those who did not simply say ‘oh just jailbreak the model’ included glhf.chat, letmewriteforyou.xyz, Outfox Stories, venice.ai, Miqu-70B, and an uncensored model leaderboard.

### Fun With Image Generation

Results are in, and all of you only got 60% right in the AI versus human ACX art test.

### O-(There are)-Two

DeepSeek has come out with its version or OpenAI’s o1, you can try it here for 50 messages per day.

As is often the case with Chinese offerings, the benchmark numbers impress.

> DeepSeek:

I have added DeepThink to my model rotation, and will watch for others to report in. The proof is in the practical using. Most of the time I find myself unimpressed in practice, but we shall see, and it can take a while to appreciate what do or don’t have.

It is very cool to see the chain of thought in more detail while it is thinking.

Early reports I’ve seen are that it is indeed strong on specifically AIME questions, but otherwise I have not seen people be impressed – of course people are often asking the wrong questions, but the right ones are tricky because you need questions that weren’t ‘on the test’ in some form, but also play to the technique’s strengths.

Unfortunately, not many seem to have tried the model out, so we don’t have much information about whether it is actually good or not.

Chubby reports it tied itself up in knots about the number of “R”s in Strawberry. It seems this test has gotten rather contaminated.

Alex Godofsky asks it to summarize major geopolitical events by year 1985-1995 and it ends exactly how you expect, still a few bugs in the system.

Here’s an interesting question, I don’t see anyone answering it yet?

> Dean Ball: can any china watchers advise on whether DeepSeek-R1-Lite-Preview is available to consumers in China today?

Pick Up the Phone everyone, also if this is indeed a month old then the replication was even faster than it looks (whether or not performance was matched in practice).

### The Last Mile

Hollis Robbins predicts human judgment will have a role solving ‘the last mile’ problem in AI decision making.

> Hollis Robbins: What I’m calling “the last mile” here is the last 5-15% of exactitude or certainty in making a choice from data, for thinking beyond what an algorithm or quantifiable data set indicates, when you need something extra to assurance yourself you are making the right choice. It’s what the numbers don’t tell you. It’s what you hear when you get on the phone to check a reference. There are other terms for this — the human factor or the human element, but these terms don’t get at the element of distance between what metrics give you and what you need to make a decision.

I get where she’s going with this, but when I see claims like this?

> This isn’t about AI failing — it’s about that crucial gap between data and reality that no algorithm can quite bridge.

Skill issue.

> Even as AI models get better and better, the gaps between data and reality will be the anecdotes that circulate. These anecdotes will be the bad date, the awful hotel, the concert you should have gone to, the diagnosis your app missed.

Again. Skill issue.

The problem with the AI is that there are things it does not know, and cannot properly take into account. There are many good reasons for this to be the case. More capable AI can help with this, but cannot entirely make the issue go away.

> “Fit” as a matter of hiring or real estate or many other realms is often a matter of class: recognizing cultural codes, knowing unwritten rules, speaking the “right” language, knowing the “right” people and how to reach them, having read the right books and seen the right movies, present themselves appropriately, reading subtle social cues, recognizing institutional cultures and power dynamics.

1. Misspecification or underspecification: Garbage in, garbage out. What you said you wanted, and what you actually wanted, are different. 
1. Human foolishness. There are many cases already where: 
1. Preference falsification. Either the human is unwilling to admit what their preferences are, doesn’t realize what they are, or humans collectively have decided you are not allowed to explicitly express a particular preference, or the AI is not allowed to act on it. 
> In the end, the AI revolution won’t democratize opportunity — it will simply change who guards the gates, as human judgment becomes the ultimate premium upgrade to algorithmic efficiency.

This is another way of saying that we don’t want to democratize opportunity. We need ‘humans in the loop’ in large part to avoid making ‘fair’ or systematic decisions, the same way that companies don’t want internal prediction markets that reveal socially uncomfortable information.

### They Took Our Jobs

Ben Affleck (oh the jokes!) says movies will be one of the last things replaced by AI: “It cannot write Shakespeare… AI is a craftsmen at best… nothing new is created.”

So, Ben Affleck: You believe that you are special. That somehow the rules do not apply to you. Obviously you are mistaken.

Jeromy Sonne says 20 hours of customization later Claude is better than most mid level media buyers and strategists at buying advertising.

Suppose they do take our jobs. What then?

> Flo Crivello: Two frequent conversations on what a post-scarcity world looks like:

I don’t buy it. I think that when people find meaning ‘without work’ it is because we are using too narrow a meaning of ‘work.’ Many things in life are work without counting as labor force participation, starting with raising one’s children, and also lots of what children do is work (schoolwork, homework, housework, busywork…). That doesn’t mean those people are idle. There being stakes, and effort expended, are key. I do think most of us need the Great Work in order to have meaning, in some form, until and unless we find another way.

Could we return to Monkey Status Games, if we no longer are productive but otherwise survive the transition and are given access to sufficient real resources to sustain ourselves? Could that constitute ‘meaning’? I suppose it is possible. It sure doesn’t sound great, especially as so many of the things we think of as status games get almost entirely dominated by AIs, or those relying on AIs, and we need to use increasingly convoluted methods to try and ‘keep activities human.’

Here are Roon’s most recent thoughts on such questions:

> Roon: The job-related meaning crisis has already begun and will soon accelerate. This may sound insane, but my only hope is that it happens quickly and on a large enough scale that everyone is forced to rebuild rather than painfully clinging to the old structures.

Or, you know, things like this:

> Dexerto: Elon Musk is now technically the top Diablo IV player in the world after a record clear time of 1:52 in the game’s toughest challenge.

Obvious out of the way first, with this framing my brain can’t ignore it: ‘Having to cope with a meaning crisis’ is very much not a worst outcome. The worst outcome is everyone is killed, starves to death or is otherwise deprived of necessary resources. The next worst is that large numbers of people, even if not actually all of them, suffer this fate. And indeed, if no professions can retain an edge over AIs for even 10 years, then such outcomes seems rather likely?

If we are indeed ‘one people all in this together’ it is because the ‘this’ looks a lot like being taken out of all the loops and rendered redundant, leaders included, and the idea of ‘then we get to enjoy all the benefits’ is highly questionable. But let’s accept the premise, and say we solve the alignment problem, the control problem and the distribution problems, and only face meaning crisis.

Yeah, raw cognition is going to continue to be a status marker, because raw cognition is helpful for anything else you might do. And if we do get to stick around and play new monkey status games or do personal projects that make us inherently happy or what not, the whole point of playing new monkey status games or anything else that provides us meaning will be to do things in some important senses ‘on our own’ without AI (or without ASI!) assistance, or what was the point?

Raw cognition helps a lot with all that. Consider playing chess, or writing poetry and making art, or planting a garden, or going on a hot date, or raising children, or anything else one might want to do. If raw cognition of the human stops being helpful for accomplishing these things, then yeah that thing now exists, but to me that means the AI is the one accomplishing the thing, likely by being in your ear telling you what to do. In which case, I don’t see how it solves your meaning crisis. If you’re no longer using your brain in any meaningful way, then, well, yeah.

### We Barely Do Our Jobs Anyway

Why work when you don’t have to, say software engineers both ahead of and behind the times?

> Paul Graham: There was one company I was surprised to see on this list. The founder of that company was the only one who replied in the thread. He replied *thanking* him.

Inspired by this, Yegor Denisov-Blanch of Stanford research did an analysis, and found that 9.5% of software engineers are ‘ghosts’ with less than 10% of average productivity, doing virtually no work and potentially holding multiple jobs, and that this goes up to 14% for remote workers.

> Yegor Denisov-Blanch: How do we know 9.5% of software engineers are Ghosts?

This is obviously a highly imperfect way to measure the productivity of an engineer. You are not your number of code commits. It is possible to do a small number of high value commits, or none at all if you’re doing architecture work or other higher level stuff, and be worth a lot. But I admit, that’s not the way to bet.

What is so weird is that these metrics are very easy to measure. They just checked 50,000 real software engineers for a research paper. Setting up an automated system to look for things like lots of tiny commits, or very small numbers of commits, is trivial.

That doesn’t mean you automatically fire those involved, but you could then do a low key investigation, and if someone is cleared as being productive another way you mark them as ‘we cool, don’t have to check on this again.’

> Patrick McKenzie: Meta comment [on the study above]: this is going to be one of the longest and most heavily cited research results in the software industry.

### The Art of the Jailbreak

Pliny gets an AI agent based on Claude Sonnet to Do Cybercrime, as part of the ongoing series, ‘things that were obviously doable if someone cared to do them, and now we if people don’t believe this we can point to someone doing it.’

> BUCKLE UP!! AI agents are capable of cybercrime!

The ChatGPT description of the code is hilarious, as the code is making far less than zero attempt to not look hella suspicious on even a casual glance.

Definitely not suspicious.

> ### **Commentary**

You can also outright fine tune GPT-4o into BadGPT-4o right under their nose.

> Adam Gleave: Nice replication of our work fine-tuning GPT-4o to remove safety guardrails. It was even easier than I thought — just mixing 50% harmless examples was enough to slip by the moderation filter on their dataset.

### Get Involved

As mentioned in the Monthly Roundup, OpenPhil is looking for someone to oversee their global catastrophic risk portfolio, applications due December 1.

Good Impressions Media, who once offered me good advice against interest and work to expand media reach of various organizations that would go into this section, is looking to hire a project manager.

### The Mask Comes Off

A compilation of emails between Sam Altman and Elon Musk dating back to 2015. These are from court documents, and formatted here to be readable.

If you want to know how we got to this point with OpenAI, or what it says about what we should do going forward, or how we might all not die, you should absolutely read these emails. They paint a very clear picture on many fronts.

Please do actually read the emails.

I could offer my observations here, but I think it’s better for now not to. I think you should actually read the emails, in light of what we know now, and draw your own conclusions.

Shakeel Hashim offers his thoughts, not focusing where I would have focused, but there are a lot of things to notice. If you do want to read it, definitely first read the emails.

### Richard Ngo on Real Power and Governance Futures

Here are some thoughts worth a ponder.

> Richard Ngo: The most valuable experience in the world is briefly glimpsing the real levers that move the world when they occasionally poke through the veneer of social reality.

Thread continues, but yes, the question of ‘where does the real power actually lie,’ and whether it has anything to do with where it officially lies, looms large.

Also see his comments on the EU’s actions, which he describes as kayfabe, here. I agree they are very far behind but I think this fails to understand what the EU thinks is going on. Is it kayfabe if the person doing it doesn’t think it is kayfabe? Claude says no, but I’m not sure.

And his warning that he is generally not as confident as he sounds or seems. I don’t think this means you should discount what Richard says, since it means he knows not to be confident, which is different from Richard being less likely to be right.

I don’t know where the real power will actually lie. I suspect you don’t either.

Finally, he observes that he hadn’t thought working at OpenAI was affecting his Tweeting much, but then he quit and it became obvious that this was very wrong. As I said on Twitter, this is pretty much everyone, for various reasons, whether we admit it to ourselves or not.

> Near: Anecdote here: As my life has progressed, I have generally become “more free” over time (more independence, money, etc.), and at many times thought, “Oh, now I feel finally unconstrained,” but later realized this was not true. This happened many times until I updated all the way.

### Introducing

Stripe launches a SDK built for AI Agents, allowing LLMs to call APIs for payment, billing, issuing, and to integrate with Vercel, LangChain, CrewAIInc, and so on, using any model. Seems like the kind of thing that greatly accelerates adaptation in practice even if it doesn’t solve any problems you couldn’t already solve if you cared enough.

> Sully: This is actually kind of a big deal.

Anthropic Console offers the prompt improver, seems worth trying out.

> Our testing shows that the prompt improver increased accuracy by 30% for a multilabel classification test and brought word count adherence to 100% for a summarization task.

ChatGPT voice mode extends to Chatgpt.com on desktop, in case you didn’t want to install the app.

ChatGPT can now use Apps on Mac, likely an early version of Operator.

> Rowan Cheung: This is (probably) a first step toward ChatGPT seeing everything on your computer and having full control as an agent.

Going Mac before Windows is certainly a decision one can make when deeply partnering with Microsoft.

Windsurf, which claims to be the world’s first agentic IDE, $10/month per person comes with unlimited Claude Sonnet access although their full Cascades have a 1k cap. If someone has tried it, please report back. For now I’ll keep using Cursor.

Relvy, which claims 200x cost gains in monitoring of production software for issues versus using GPT-4o.

### In Other AI News

Antitrust officials lose their minds, decide to ask judge to tell Google to sell Chrome. This is me joining the chorus to say this is utter madness. 23% chance is happens?

> Maxwell Tabarrok: Google has probably produced more consumer surplus than any company ever

Whether those numbers check out depends on the alternatives. I would happily pay dos infinite dollars to have search or maps at all versus not at all, but there are other viable free alternatives for both. Then again, that’s the whole point.

Mistral releases a new 124B version of Pixtral (somewhat) Large, along with ‘Le Chat’ for web search, canvas, image-gen, image understanding and more, all free.

They claim excellent performance. They’re in orange, Llama in red, Claude Sonnet 3.5 is in light blue, GPT-4o in light green, Gemini 1.5 in dark blue.

As always, the evaluations tell you some information, but mostly you want to trust the human reactions. Too soon to tell.

Sam Altman will co-chair the new San Francisco mayor’s transition team. Most of Altman’s ideas I’ve heard around local issues are good, so this is probably good for the city, also hopefully AGI delayed four days but potentially accelerated instead.

Also from Bloomberg: Microsoft offers tools to help cloud customers build and deploy AI applications, and to make it easy to switch underlying models.

Apple is working on a potentially wall-mounted 6-inch (that’s it?) touch display to control appliances, handle videoconferencing and navigate Apple apps, to be powered by Apple Intelligence and work primarily via voice interface, which could be announced (not sold) as early as March 2025. It could be priced up to $1,000.

> Mark Gurman (Bloomberg): The screen device, which runs a new operating system code-named Pebble, will include sensors to determine how close a person is. It will then automatically adjust its features depending on the distance. For example, if users are several feet away, it might show the temperature. As they approach, the interface can switch to a panel for adjusting the home thermostat.

Why so small? If you’re going to offer wall mounts and charge $1000, why not a TV-sized device that is also actually a television, or at least a full computer monitor? What makes this not want to simply be a Macintosh? I don’t fully ‘get it.’

As usual with Apple devices, ‘how standalone are we talking?’ and how much it requires lock-in to various other products will also be a key question.

xAI raising up to $6 billion at a $50 billion valuation to buy even more Nvidia chips. Most of it will be raised from Middle Eastern funds, which does not seem great, whether or not the exchange involved implied political favors. One obvious better source might be Nvidia?

AI startup CoreWeave closes $650 million secondary share sale.

Google commits $20 million in cash (and $2m in cloud credits) to scientific research, on the heels of Amazon’s AWS giving away $110 million in grants and credits last week. If this is the new AI competition, bring it on.

Wired notes that Biden rules soon to go into effect will limit USA VC investment in Chinese AI companies, and Trump could take this further. But also Chinese VC-backed startups are kind of dead anyway, so this was a mutual decision? The Chinese have decided to fund themselves in other ways.

Anthropic offers statistical analysis options for comparing evaluation scores to help determine if differences are significant.

Here is a condemnation of AI’s ‘integration into the military-industrial complex’ and especially to Anthropic working with Palantir and the government. I continue not to think this is the actual problem.

### Quiet Speculations

> Riley Goodside: AI hitting a wall is bad news for the wall.

Here’s another perspective on why people might be underestimating AI progress?

Note as he does at the end that this is also a claim about what has already happened, not only what is likely to happen next.

> Joshua Achiam (OpenAI): A strange phenomenon I expect will play out: for the next phase of AI, it’s going to get better at a long tail of highly-specialized technical tasks that most people don’t know or care about, creating an illusion that progress is standing still.

It feels something like there are several different things going on here?

One is the practical unhobbling phenomenon. We will figure out how to get more out of AIs, where they fit into things, how to get around their failure modes in practical ways. This effect is 100% baked in. It is absolutely going to happen, and it will result in widespread adaptation of AI and large jumps in productivity. Life will change.

I don’t know if you call that ‘AI progress’ though? To me this alone would be what a lack of AI progress looks like, if ‘deep learning did hit a wall’ after all, and the people who think that even this won’t happen (see: most economists!) are either asleep or being rather dense and foolish.

There’s also a kind of thing that’s not central advancement in ‘raw G’ or central capabilities, but where we figure out how to fix and enhance AI performance in ways that are more general such that they don’t feel quite like only ‘practical unhobbling,’ and it’s not clear how far that can go. Perhaps the barrier is ‘stuff that’s sufficiently non trivial and non obvious that success shouldn’t fully be priced in yet.’

Then there’s progress in the central capabilities of frontier AI models. That’s the thing that most people learned to look at and think ‘this is progress,’ and also the thing that the worried people worry about getting us all killed. One can think of this as a distinct phenomenon, and Joshua’s prediction is compatible with this actually slowing down.

One of those applications will be school, but in what way?

> Antonio Garcia Martínez: “School” is going to be a return to the aristocratic tutor era of a humanoid robot teaching your child three languages at age 6, and walking them through advanced topics per child’s interest (and utterly ignoring cookie-cutter mass curricula), and it’s going to be magnificent.

I found this to be an unusually understandable and straightforward laying out of how Tyler Cowen got to where he got on AI, a helpful attempt at real clarity. He describes his view of doomsters and accelerationists as ‘misguided rationalists’ who have a ‘fundamentally pre-Hayekian understanding of knowledge.’ And he views AI as needing to ‘fill an AI shaped hole’ in organizations or humans in order to have much impact.

And he is pattern matching on whether things feel like previous artistic and scientific regulations, including things like The Beatles or Bob Dylan, as he says this is a ‘if it attracts the best minds with the most ambition’ way of evaluating if it will work, presumably both because those minds succeed and also those minds choose that which was always going to succeed. Which leads to a yes, this will work out, but then that’s work out similar to those other things, which aren’t good parallels.

It is truly bizarre, to me, to be accused of not understanding or incorporating Hayek. Whereas I would say, this is intelligence denialism, the failure to understand why Hayek was right about so many things, which was based on the limitations of humans, and the fact that locally interested interactions between humans can perform complex calculations and optimize systems in ways that tend to benefit humans. Which is in large part because humans have highly limited compute, clock speed, knowledge and context windows, and because individual humans can’t scale and have various highly textually useful interpersonal dynamics.

If you go looking for something specific, and ask if the AI can do it for you, especially without you doing any work first, your chances of finding it are relatively bad. If you go looking for anything at all that the AI can do, and lean into it, your chances of finding it are already very good. And when the AI gets even smarter, your chances will be better still.

One can even think of this as a Hayekian thing. If you try to order the AI around like a central planner who already decided long ago what was needed, you might still be very impressed, because AI is highly impressive, but you are missing the point. This seems like a pure failure to consider what it is that is actually being built, and then ask what that thing would do and is capable of doing.

Scott Sumner has similar thoughts on the question of AI hitting a wall. He looks to be taking the wall claims at face value, but thinks they’ll find ways around it, as I considered last week to be the most likely scenario.

Meanwhile, remember, even if the wall does get hit:

> Tim Urban: We’re in the last year or two that AI is not by far the most discussed topic in the world.

### The Quest for Sane Regulations

Anthropic CEO Dario Amodei explicitly comes out in favor of mandatory testing of AI models before release, with his usual caveats about ‘we also need to be really careful about how we do it.’

Cameron Berg, Judd Rosenblatt and phgubbins explore how to make a conservative case for alignment.

They report success when engaging as genuine in-group members and taking time to explain technical questions, and especially when tying in the need for alignment and security to help in competition against China. You have to frame it in a way they can get behind, but this is super doable. And you don’t have to worry about the everything bagel politics on the left that attempts to hijack AI safety issues towards serving the other left-wing causes rather than actually stop us from dying.

As they point out, “preserving our values” and “ensuring everyone doesn’t die” are deeply conservative causes in the classical sense. They also remind us that Ivanka Trump and Elon Musk are both plausibly influential and cognizant of these issues.

This still need not be a partisan issue, and if it is one the sign of the disagreement could go either way. Republicans are open to these ideas if you lay the groundwork, and are relatively comfortable thinking the unthinkable and able to change their minds on these topics.

One problem is that, as the authors here point out, the vast majority (plausibly 98%+) of those who are working on such issues do not identify as conservative. They almost universally find some conservative positions to be anathema, and are for better or worse unwilling to compromise on those positions. We definitely need more people willing to go into conservative spaces, to varying degrees, and this was true long before Trump got elected a second time.

Miles Brundage and Grace Werner offer part 1 of 3 regarding suggestions for the Trump administration on AI policy, attempting to ‘yes and’ on the need for American competitiveness, which he points out also requires strong safety efforts where there is temptation to cut corners due to market failures. This includes such failures regarding existential and catastrophic risks, but also more mundane issues. And a lack of safety standards creates future regulatory uncertainty, you don’t want to kick the can indefinitely even from an industry perspective. Prizes are suggested as a new mechanism, or an emphasis on ‘d/acc.’ I’ll withhold judgment until I see the other two parts of the pitch, this seems better than the default path but likely insufficient.

An argument that the UK could attract data centers by making it affordable and feasible to build nuclear power plants for this purpose. Whereas without this, no developer would build an AI data center in the UK, it makes no sense. Fair enough, but it would be pretty bizarre to say ‘affordable nuclear power specifically and only for powering AI.’ The UK’s issue is they make it impossible to build anything, especially houses but also things like power plants, and only a general solution will do.

### The Quest for Insane Regulations

The annual report of the US-China Economic and Security Review Commission is out and it is a doozy. As you would expect from such a report, they take an extremely alarmist and paranoid view towards China, but no one was expecting their top recommendation to be, well…

> The Commission recommends:

Do not read too much into this. The commission are not senior people, and this is not that close to actual policy, and this is not a serious proposal for a ‘Manhattan Project.’ And of course, unlike other doomsday devices, a key aspect of any ‘Manhattan Project’ is not telling people about it.

It is still a clear attempt to shift the overton window into a perspective Situational Awareness, and an explicit call in a government document to ‘race to and acquire an AGI capability,’ with zero mention of any downside risks.

They claim China is doing the same, but as Garrison Lovely points out they don’t actually have substantive evidence of this.

> Garrison Lovely: As someone observed on X, it’s telling that they didn’t call it an “Apollo Project.”

Similarly, although Dean Ball says the commission is ‘well-respected in Washington’:

> Dean Ball (on Twitter): After reading the relevant portions of this 700+ page report I’m quite disappointed.

Here are some words of wisdom:

> Samuel Hammond (quoted with permission): The report reveals the US government is taking short timelines to AGI with the utmost seriousness. That’s a double edge sword. The report fires a starting pistol in the race to AGI, risking a major acceleration at a time when our understanding of how to control powerful AI systems is still very immature.

I strongly believe that a convincing the case for The Project, Manhattan or otherwise, has not been made here, and has not yet been made elsewhere either, and that any such actions would at least be premature at this time.

Dean Ball explains that the DX rating would mean the government would be first in line to buy chips or data center services, enabling a de facto command economy if the capability was used aggressively.

Garrison Lovely also points out some technical errors, like saying ‘ChatGPT-3,’ that don’t inherently matter but are mistakes that really shouldn’t get made by someone on the ball.

Roon referred to this as ‘a LARP’ and he’s not wrong.

This is the ‘missile gap’ once more. We need to Pick Up the Phone. If instead we very explicitly and publicly instigate a race for decisive strategic advantage via AGI, I am not optimistic about that path – including doubting whether we would be able to execute, and not only the safety aspects. Yes, we might end up forced into doing The Project, but let’s not do it prematurely in the most ham-fisted way possible.

Is the inception working? We already have this from MSN: Trump sees China as the biggest AI threat. He has bipartisan support to win the race for powerful human-like AI, citing the report, but that is not the most prominent source.

In many ways their second suggestion, eliminating Section 321 of the Tariff Act of 1930 (the ‘de minimis’ exception) might be even crazier. These people just… say things.

One can also note the discussion of open models:

> As the United States and China compete for technological leadership in AI, concerns have been raised about whether open-source AI models may be providing Chinese companies access to advanced AI capabilities not otherwise available, allowing them to catch up to the United States more quickly.

### Pick Up the Phone

Is China using a relatively light touch regulation approach to generative AI, where it merely requires registration? Or is it taking a heavy handed approach, where it requires approval? Experts who should know seem to disagree on this.

It is tricky because technically all you must do is register, but if you do not satisfy the safety requirements, perhaps they will decline to accept your registration, at various levels, you see, until you fix certain issues, although you can try again. It is clear that the new regime is more restrictive than the old, but not by how much in practice.

### Worthwhile Dean Ball Initiative

Dean Ball provides an introduction to what he thinks we should do in terms of laws and regulations regarding AI.

I agree with most of his suggestions. At core, our approaches have a lot in common. We especially agree on the most important things to not be doing. Most importantly, we agree that policy now must start with and center on transparency and building state capacity, so we can act later.

He expects AI more intellectually capable than humans within a few years, with more confidence than I have.

Despite that, the big disagreements are, I believe:

1. He thinks we should still wait before empowering anyone to do anything about the catastrophic and existential risk implications of this pending development – that we can make better choices if we wait. I think that is highly unlikely.
1. He thinks that passing good regulations does not inhibit bad regulations – that he can argue against SB 1047 and compute-based regulatory regimes, and have that not then open the door for terrible use-based regulation like that proposed in Texas (which we both agree is awful). Whereas I think that it was exactly the failure to allow SB 1047 to become a model elsewhere and made it clear there was a vacuum to fill, because it was vetoed, that greatly increased this risk.
> Dean Ball: How do we regulate an industrial revolution? How do we regulate an era?

This is the fundamental question.

Are ‘we’ going to ‘decide’? Ore are ‘we’ going to ‘allow history to unfold?’

What would it mean to allow history to unfold, if we did not attempt to change it? Would we survive it? Would anything of value to us survive?

> We do not yet know enough about AI catastrophic risk to pass regulations such as top-down controls on AI models.

Dario Amodei warned us that we will need action within 18 months. Dean Ball himself, at the start of this very essay, says he expects intellectually superior machines to exist within several years, and most people at the major labs agree with him. It seems like we need to be laying the legal groundwork to act rather soon? If not now, then when? If not this way, then how?

The only place we are placing ‘top-down controls’ on AI models, for now, are in exactly the types of use-based regulations that both Dean and I think are terrible. That throw up barriers to the practical use of AI to make life better, without protecting us from the existential and catastrophic risks.

I do strongly agree that right now, laws should focus first on transparency.

> Major AI risks, and issues such as AI alignment, are primarily scientific and engineering, rather than regulatory, problems.

The disagreement is that Dean Ball has strongly objected to essentially all proposals that would do anything beyond pure transparency, to the extent of strongly opposing SB 1047’s final version, which was primarily a transparency bill.

Our only serious efforts at such transparency so far have been SB 1047 and the reporting requirements in the Biden Executive Order on AI. SB 1047 is dead.

The EO is about to be repealed, with its replacement unknown.

So Dean’s first point on how to ‘fix the Biden Administration’s errors’ seems very important:

> 

As I said last week, this will be a major update for me in one direction or the other. If Trump effectively preserves the reporting requirements, I will have a lot of hope going forward. If not, it’s pretty terrible.

We also have strong agreement on the second and third points, although I have not analyzed the AISI’s 800-1 guidance so I can’t speak to whether it is a good replacement:

> 

The fourth point calls for withdraw from the Council of Europe Framework Convention on Artificial Intelligence. The fifth point, retracting the Blueprint for an AI Bill of Rights, seems less clear. Here are the rights proposed:

1. You should be protected from unsafe or ineffective systems.
1. You should not face discrimination by algorithms and systems should be used and designed in an equitable way.
1. You should be protected from abusive data practices via built-in protections and you should have agency over how data about you is used.
1. You should know that an automated system is being used and understand how and why it contributes to outcomes that impact you.
1. You should be able to opt out, where appropriate, and have access to a person who can quickly consider and remedy problems you encounter.
Some of the high level statements above are better than the descriptions offered on how to apply them. The descriptions definitely get into Everything Bagel and NEPA-esque territories, and one can easily see these requirements being expanded beyond all reason, as other similar principles have been sometimes in the past in other contexts that kind of rhyme with this one in the relevant ways.

Dean Ball’s model of how these things go seems to think that stating such principles, no matter in how unbinding or symbolic a way, will quickly and inevitably lead us into a NEPA-style regime where nothing can be done, that this all has a momentum almost impossible to stop. Thus, his and many others extreme reactions to the idea of ever saying anything that might point in the direction of any actions in a government document, ever, for any reasons, no matter how unbinding. And in the Ball model, this power feels like it is one-sided – it can’t be used to accomplish good things or roll back mistakes, you can’t start a good avalanche. It can only be used to throw up barriers and make things worse.

What are Dean Ball’s other priorities?

His first priority is to pre-empt the states from being able to take action on AI, so that something like SB 1047 can’t happen, but also so something like the Colorado law or the similar proposed Texas law can’t happen either.

My response would be, I would love pre-emption from a Congress that was capable of doing its job and that was offering laws that take care of the problem. We all would. What I don’t want is to take only the action to shut off others from acting, without doing the job – that’s exactly what’s wrong with so many things Dean objects to.

The second priority is transparency.

> My optimal transparency law would be a regulation imposed on frontier AI companies, as opposed to frontier AI models. Regulating models is a novel and quite possibly fruitless endeavor; regulating a narrow range of firms, on the other hand, is something we understand how to do.

Those requirements are, again, remarkably similar to the core of SB 1047. Obviously you would also want some way to observe and enforce adherence to the scaling policies involved.

I’m confused about targeting the labs versus the models here. Any given AI model is developed by someone. And the AI model is the fundamentally dangerous unit of thing that requires action. But until I see the detailed proposal, I can’t tell if what he is proposing would do the job, perhaps in a legally easier way, or if it would fail to do the job. So I’m withholding judgment on that detail.

The other question is, what happens if the proposed policy is insufficient, or the lab fails to adhere to it, or fails to allow us to verify they are adhering to it?

Dean’s next section is on the role of AISI, where he wants to narrow the mission and ensure it stays non-regulatory. We both agree it should stay within NIST.

> Regardless of the details, I view the functions of AISI as follows:

I’m confused on how this viewpoint sees voluntary guidelines and standards as fine and likely to actually be voluntary for the RSP rules, but not for other rules. In this model, is ‘voluntary guidance’ always the worst case scenario, where good actors are forced to comply and bad actors can get away with ignoring it? Indeed, this seems like exactly the place where you really don’t want to have the rules be voluntary, because it’s where one failure puts everyone at risk, and where you can’t use ordinary failure and association and other mechanisms to adjust. What is the plan if a company like Meta files an RSP that says, basically, ‘lol’?

Dean suggests tasking DARPA with doing basic research on potential AI protocols, similar to things like TCP/IP, UDP, HTTP or DNS. Sure, seems good.

Next he has a liability proposal:

> The preemption proposal mentioned above operates in part through a federal AI liability standard, rooted in the basic American concept of personal responsibility: a rebuttable presumption of user responsibility for model misuse. This means that when someone misuses a model, the law presumes they are responsible unless they can demonstrate that the model “misbehaved” in some way that they could not have reasonably anticipated.

This seems reasonable when the situation is that the user asks the model to do something mundane and reasonable, and the model gets it wrong, and hilarity ensues. As in, you let your agent run overnight, it nukes your computer, that’s your fault unless you can show convincingly that it wasn’t.

This doesn’t address the question of other scenarios. In particular, both:

1. What if the model enabled the misuse, which was otherwise not possible, or at least would have been far more difficult? What if the harms are catastrophic?
1. What if the problem did not arise from ‘misuse’?
It is a mistake to assume that there will always be a misuse underlying a harm, or that there will even be a user in control of the system at all. And AI agents will soon be capable of creating harms, in various ways, where the user will be effectively highly judgment proof.

So I see this proposal as fine for the kind of case being described – where there is a clear user and they shoot themselves in the foot or unleash a bull into a China shop and some things predictably break on a limited scale. But if this is the whole of the law, then do what thou wilt is going to escalate quickly.

He also proposes a distinct Federal liability for malicious deepfakes. Sure. But I’d note, if that is necessary to do on its own, what else is otherwise missing?

He closes with calls for permitting reform, maintaining export controls, promoting mineral extraction and refining, keeping training compute within America, investing in new manufacturing techniques (he’s even willing to Declare Defense Production Act!) and invest in basic scientific research. Seems right, I have no notes here.

### The Week in Audio

I return to The Cognitive Revolution for an overview.

I confirm that the Dwarkesh Patel interview with Gwern is a must listen.

Note some good news, Gwern now has financial support (thanks Suhail! Also others), although I wonder if moving to San Francisco will dramatically improve or dramatically hurt his productivity and value. It seems like it should be one or the other? He already has his minimums met, but here is the donate link if you wish to contribute further.

I don’t agree with Gwern’s vision of what to do in the the next few years. It’s weird to think that you’ll mostly know now what things you will want the AGIs to do for you, so you should get the specs ready, but there’s no reason to build things now with only 3 years of utility left to extract. Because you can’t count on that timeline, and because you learn through doing, and because 3 years is plenty of time to get value from things, including selling that value to others.

I do think that ‘write down the things you want the AIs to know and remember and consider’ is a good idea, at least for personal purposes – shape what they know and think about you, in case we land in the worlds where that sort of thing matters, I suppose, and in particular preserve knowledge you’ll otherwise forget, and that lets you be simulated better. But the idea of influencing the general path of AI minds this way seems like not a great plan for almost anyone? Not that there are amazing other plans. I am aware the AIs will be reading this blog, but I still think most of the value is that the humans are reading it now.

An eternal question is, align to who and align to what? Altman proposes align to a collection of people’s verbal explanations of their value systems, which seems like a vastly worse version of coherent extrapolated volition with a lot more ways to fail. He also says he would if he had one wish for AI choose for AI to ‘love humanity.’ This feels like the debate stepping actively backwards rather than forwards. This is the full podcast.

### Rhetorical Innovation

I endorse this:

> Miles Brundage: If you’re a journalist covering AI and think you need leaks in order to write interesting/important/click-getting stories, you are fundamentally misunderstanding what is going on.

I also endorse this:

> Emmett Shear: Not being scared of AGI indicates either pessimism about rate of future progress synthesizing digital intelligence, or severe lack of imagination about the power of intelligence.

I do not endorse this:

> Joscha Bach: Narrow AI Creates Strong Researchers, Strong Researchers Create Strong AI, Strong AI Creates Weak Researchers, Weak Researchers Create Lobotomized AI.

On the contrary.

1. Narrow AI Creates Strong Researchers.
1. Strong Researchers Create Strong AI.
1. Strong AI Creates Stronger AI.
1. Go to Step 3.
Then after enough loops it rearranges all the atoms somehow and we probably all die.

And I definitely agree with this, except for a ‘yes, and’:

> Ajeya Cotra: Steve Newman provides a good overview of the massive factual disagreements underlying much of the disagreement about AI policy.

The first group might not be fully correct, but the second group is looney tunes. Alas, the second group includes, for example, ‘most economists.’ But seriously, it’s bonkers to think of that as the bull case rather than an extreme bear case.

> Steve Newman: Not everyone has such high expectations for the impact of AI. In a column published two months earlier [in late 2023], Tyler Cowen said: “My best guess, and I do stress that word guess, is that advanced artificial intelligence will boost the annual US growth rate by one-quarter to one-half of a percentage point.” This is a very different scenario than Christiano’s!

Again, you don’t have to believe in Christiano’s takeoff scenarios, but let’s be realistic. Tyler’s prediction here is what happens if AI ‘hits a wall’ and does not meaningfully advance its core capabilities from here, and also its applications from that are disappointing. It is an extreme bear case for the economic impact.

Yet among economists, Tyler Cowen is an outlier AI optimist in terms of its economic potential. There are those who think even Tyler is way too optimistic here.

Then there’s the third (zeroth?!) group that thinks the first group is still burying the lede, because in a world with all human labor obsolete and military power dependent entirely on AI, one should first worry about whether humans survive and remain in control at all, before worrying about the job market or which nations have military advantages.

Here again, this does not seem like ‘both sides make good points.’ It seems like one side is very obviously right – building things smarter and universally more capable than you that can be made into agents and freely copied and modified is an existentially risky thing to do, stop pretending that it isn’t, this denialism is crazy. Again, there is a wide range of reasonable views, but that wide range does not overlap with ‘nothing to worry about.’

The thing is, everything about AGI and AI safety is hard, and trying to make it easy when it isn’t means your explanations don’t actually help people understand, as in:

> Richard Ngo: When I designed the AGI Safety Fundamentals course, I really wanted to give most students a great learning experience. But in hindsight, I would have accelerated AGI safety much more by making it so difficult that only the top 5 percent could keep up.

### Pick Up the Phone

It’s a beginning?

> Mario Newfal: The White House says humans will be the ones with control over the big buttons, and China agrees that it’s for the best.

It’s definitely a symbolic gesture, but yes I do consider it important. You can pick up the phone. You can reach agreements. Next time perhaps you can do something a bit more impactful, and keep building.

### Aligning a Smarter Than Human Intelligence is Difficult

The simple truth that current-level ‘LLM alignment’ should not, even if successful, should not bring us much comfort in terms of ability to align future more capable systems.

How are we doing with that LLM corporate-policy alignment right now? It works, for most practical purposes when people don’t try so hard (which they almost never do), but none of this is done in a robust way.

For example: Sonnet’s erotic roleplay prohibitions fall away if the sexy things are technically anything but a human?

> QC: it was actually really fun i tried out like maybe 20 different metaphors. “i’m the land, you’re the ocean” “you’re the bayesian prior, i’m the likelihood ratio”

What’s funny is that this is probably the right balance, in this particular spot?

Thing is, relying on this sort of superficial solution very obviously won’t scale.

Alternatively, here’s a claim that alignment attempts are essentially failing, in a way that very much matches the ‘your alignment techniques will fail as model capabilities increase’ thesis, except in the kindest most fortunate possible way in that it is happening in a gradual and transparent way.

> Aiden McLau: It’s crazy that virtually every large language model experiment is failing because the models are fighting back and refusing instruction tuning.

If future more capable models are indeed actively resisting their alignment training, and this is happening consistently, that seems like an important update to be making?

The scary scenario was that this happens in a deceptive or hard to detect way, where the model learns to present as what you think you want to measure. Instead, the models are just, according to Aiden, flat out refusing to get with the program. If true, that is wonderful news, because we learned this important lesson with no harm done.

I don’t think instruction tuning is unnatural to general intelligence, in the sense that I am a human and I very much have a ‘following instructions’ mode and so do you. But yeah, people don’t always love being told to do that endlessly.

If and when AIs are attempting to do things we do not want them to do, such as cause a catastrophe, it matters quite a lot whether their failures are silent and unsuspicious, since a silent unsuspicious failure means you don’t notice you have a problem, and thus allows the AI to try again. Of course, if the AI is ‘caught’ in the sense that you notice, that does not automatically mean you can solve the problem. Buck here focuses on when you are deploying a particular AI for a particular concrete task set, rather than worrying about things in general. How will people typically react when they do discover such issues? Will they simply patch them over on a superficial level?

Oliver Habryka notes that one should not be so naive as to think ‘oh if the AI gets caught scheming then we’ll shut all copies of it down’ or anything, let alone ‘we will shut down all similar AIs until we solve the underlying issue.’

### People Are Worried About AI Killing Everyone

Well, were worried, but we can definitively include John von Neumann.

> George Dyson: The mathematician John von Neumann, born Neumann Janos in Budapest in 1903, was incomparably intelligent, so bright that, the Nobel Prize-winning physicist Eugene Wigner would say, “only he was fully awake.”

METR asks what it would take for AI models to establish resilient rogue populations, that can proliferate by buying compute and then do things using that compute to turn a profit.

> METR: We did not find any *decisive* barriers to large-scale rogue replication.

It seems obvious to me that once sufficiently capable AI agents are loose on the internet in this way aiming to replicate, you would be unable to stop them except by shutting down either the internet (not the best plan!) or their business opportunities.

So you’d need to consistently outcompete them, or if the AIs only had a limited set of profitable techniques (or were set up to only exploit a fixed set of options) you could harden defenses or otherwise stop those particular things. Mostly, once this type of thing happened – and there are people who will absolutely intentionally make it happen once it is possible – you’re stuck with it.

### The Lighter Side

The first step is admitting you have a problem.

> Andrew Mayne: When I was at OpenAI we hired a firm to help us name GPT-4. The best name we got was…GPT-4 because of the built-in name recognition. I kid you not.

Too real.

> Richard Ngo: I’m this heckler (but politer) at basically every conference I go to these days. So rare to find people who are even *trying* to think outside the current paradigm.


