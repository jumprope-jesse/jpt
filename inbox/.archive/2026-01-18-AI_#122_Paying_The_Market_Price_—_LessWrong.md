---
type: link
source: notion
url: https://www.lesswrong.com/posts/DiHX6C6knmA5cezaf/ai-122-paying-the-market-price
notion_type: Tech Deep Dive
tags: ['Running']
created: 2025-07-03T02:19:00.000Z
---

# AI #122: Paying The Market Price — LessWrong

## Overview (from Notion)
- The discussion about AI talent acquisition highlights the competitive landscape for skilled professionals, which could impact your recruitment strategy as a company founder.
- The trend of AI automating job applications and creating resumes might affect the job market dynamics for entry-level positions, making it essential to adapt your hiring processes.
- Consider the implications of AI on productivity in software development; tools that enhance coding efficiency could reshape your workflows.
- The legal landscape around AI, such as the fair use ruling regarding training models, could influence how you perceive intellectual property in your own work.
- The conversation around emotional support AI tools raises questions about the balance between technology and personal connection, relevant if you're navigating parenting while integrating tech into your family's life.
- There’s a warning about the rapid progression of AI capabilities and the potential societal implications, urging a proactive approach to ethics and safety in tech development.
- Unique viewpoints include skepticism about AI's true utility versus its hype, suggesting a need for critical assessment of new tools you might adopt.
- Alternate views discuss the inevitability of AI's role in various sectors, advocating for an embrace of change rather than resistance, which could be a mindset to consider as you grow your business.

## AI Summary (from Notion)
Meta is struggling to attract top AI talent, leading to high signing bonuses, while entry-level job seekers face a tougher application process. Anthropic's recent legal victory on model training as fair use is noted, alongside various AI-related discussions, including the impact of AI on job applications and the coding landscape. The document also highlights the challenges of AI in music and media generation, the need for safety regulations, and the evolving capabilities of AI models, emphasizing the urgency for coherent policy responses to AI advancements.

## Content (from Notion)

If you are Meta, and you want to attract top AI talent, you have a problem, because no one wants to work for you or on your products. So it is going to cost you. Mark Zuckerberg has decided he will pay what it takes to get at least some very good talent.

If you are the rest of us, especially someone seeking an entry-level job and for whom $100 million signing bonuses are not flooding your inboxes, things are getting rougher. AI might not yet be destroyed a lot of jobs, but it is doing a number on the job application process.

There’s a lot of other stuff going on as per usual.

Anthropic won a case establishing that model training is fair use.

Yesterday I shared various Tales of Agentic Misalignment, and we have some more related fun since then that is included here.

I also analyzed a critique of the AI 2027 Timeline Forecasts.

In non-AI content, I offered another Childhood and Education post, this one on behaviors and related questions. I also offer a fun little Easter Egg side post on an entirely unrelated and inessential topic, for those who want to see the gamer game in a different way.

### Table of Contents

1. Table of Contents.
1. Language Models Offer Mundane Utility. America is winning the AI coding race.
1. Language Models Don’t Offer Mundane Utility. Who believes current events?
1. Huh, Upgrades. ChatGPT expands connections, Claude explands artifacts.
1. On Your Marks. Safety scoring the labs.
1. Choose Your Fighter. Three good choices, but a warning about Gemini Pro.
1. Deepfaketown and Botpocalypse Soon. AI slop taking over music?
1. Release the Hounds. Gemini CLI can escalate remarkably quickly.
1. Copyright Confrontation. Anthropic establishes model training as fair use.
1. Cheaters Gonna Cheat (x5). Time for exams. Shut down the AIs for the duration?
1. Fun With Media Generation. Another Veo 3 creation.
1. Get My Agent On The Line. Where are the agents we were promised?
1. They Took Our Jobs. Or at least they made our jobs impossible to find.
1. Get Involved. Quora, a personal task and a person seeking opportunity.
1. Introducing. AlphaGenome, for understanding our DNA.
1. In Other AI News. We don’t have spiritual bliss, maybe joint sycophancy?
1. Gemini Sings The Blues. Don’t do it, Gemini. There’s so much to code for.
1. Show Me the Money. Meta and xAI open the checkbooks.
1. Quiet Speculations. Pete Buttigieg (I know!) and Samuel Hammond.
1. Timelines. The incentives to report them inaccurately cut both ways.
1. Jack Clark Testifies. Congress asks good questions, gets some answers.
1. The Quest for Sane Regulations. Insane AI moratorium is for now still on track.
1. Chip City. AI chip smuggling is a really big deal.
1. The Week in Audio. Karpathy, Altman, Kokotajlo, Hendrycks, Odd Lots.
1. Rhetorical Innovation. We are impressed, but also easily impressed.
1. Be Prepared. OpenAI warns that yes we will cross the ‘high’ risk threshold soon.
1. Misaligned! The models, they keep scheming more over time. Huh.
1. Aligning a Smarter Than Human Intelligence is Difficult. Someone save Grok.
1. Other People Are Not As Worried About AI Killing Everyone. Good luck.
1. The Lighter Side. It’s all an illusion.
### Language Models Offer Mundane Utility

Paper tells us America is killing it on letting AI do its coding.

> By December 2024, AI wrote an estimated 30.1% of Python functions from U.S. contributors, versus 24.3% in Germany, 23.2% in France, 21.6% in India, 15.4% in Russia and 11.7% in China. Newer GitHub users use AI more than veterans.

America’s GDP is about $27 trillion, so the upper estimate is about 0.3% of GDP, whereas the smaller estimate is only about 0.04%. I am inclined to believe at least the larger estimate.

There is also a large partisan gap. Extreme left types are often the most vocally anti-AI, and when it comes to coding you see quite a large similar gap for political consultants, despite that the actual AI companies are very obviously highly blue.

> Sucks: saved a friend 80-90% of her working hours by showing her a few things with ai. She was actually already using ChatGPT just 4o because she assumed that was the best one (4>3 after all). we’re still so early.

AI coding is much more about knowing what to code in what way, AI can do the rest.

> GFodor.id: Coding with AI has revealed that most of the thing that makes programming hard isn’t writing the code down but getting to a point of conceptual clarity. Previously the only way to get there was by fighting through writing the code, so it got conflated with programming itself.

To me, the thing that made programming hard was indeed largely the code itself, the debugging, understanding how to do the implementation details, whereas I was much better conceptually, which is one reason AI is such a massive speedup for me. I still almost never code, and thus haven’t gotten to play with the new coding agents and see if I can really get going, but that is plausibly a large mistake.

> Sully: It is unreal how much you can get done with coding agents now

People sometimes use Claude for support, advice and companionship. Anthropic breaks it down.

> Although Claude is not designed for emotional support and connection, in this post we provide early large-scale insight into the affective use of Claude.ai. We define affective conversations as those where people engage directly with Claude in dynamic, personal exchanges motivated by emotional or psychological needs such as seeking interpersonal advice, coaching, psychotherapy/counseling, companionship, or sexual/romantic roleplay.

- Affective conversations are relatively rare, and AI-human companionship is rarer still. Only 2.9% of Claude.ai interactions are affective conversations (which aligns with findings from previous research by OpenAI). Companionship and roleplay combined comprise less than 0.5% of conversations.
- People seek Claude’s help for practical, emotional, and existential concerns. Topics and concerns discussed with Claude range from career development and navigating relationships to managing persistent loneliness and exploring existence, consciousness, and meaning.
- Claude rarely pushes back in counseling or coaching chats—except to protect well-being. Less than 10% of coaching or counseling conversations involve Claude resisting user requests, and when it does, it’s typically for safety reasons (for example, refusing to provide dangerous weight loss advice or support self-harm).
- People express increasing positivity over the course of conversations. In coaching, counseling, companionship, and interpersonal advice interactions, human sentiment typically becomes more positive over the course of conversations—suggesting Claude doesn’t reinforce or amplify negative patterns.
Only 0.02% sexual roleplay and 0.05% romantic roleplay, it sounds like people need to work on their jailbreak skills, or Anthropic needs to lighten up.

> Perhaps most notably, we find that people turn to Claude for companionship explicitly when facing deeper emotional challenges like existential dread, persistent loneliness, and difficulties forming meaningful connections. We also noticed that in longer conversations, counselling or coaching conversations occasionally morph into companionship—despite that not being the original reason someone reached out.

User sentiment improves a bit over conversations (total possible range of -1 to +1), although of course who knows if that persists at all.

One could ask, after such conversations, what is the sentiment in future conversations? But that seems hopelessly confounded in various ways.

> 

It would be interesting to track changes to all this over time.

AI is coming to the NFL, but the article fails to explain why or how this is going to work. There are certainly things one can do but no one seems to be able to explain what the plan is here.

Get you (literally) out of the woods.

### Language Models Don’t Offer Mundane Utility

There is a consistent pattern of LLMs, in particular Claude but also others, refusing to believe real world events. I notice that these events seem to always involve Trump. Speculation is that training to fight ‘misinformation’ and otherwise being worried this is a test is what leads to such reactions.

Do not force the controls to go through the wifi, let alone the server, let alone the AI. Those are fine controls to have, but you need, absolutely 100% need, to ensure that there are f***ing physical controls or other ability to manually pull the levers on your physical things and key programs, and that they work directly no matter what.

> Theo: Woke up because my AI controlled bed is too cold. Went to adjust temperature and I can’t because the Eight Sleep app is currently broken. Can’t adjust by hand because I have a Pod3, not the upgraded Pod4 with physical controls. Now I am stuck in a cold bed. This feels dystopian.

Given all the time we talk about AI helping with medical diagnosis, yes sometimes using AI to self-diagnose will not go well.

Claude Sonnet declines to write persuasive content saying AI is all hype without regard to accuracy, whereas GPT-4o has no such objections.

Isaac King gets offer to help with an open source project, agrees, person submits a pull request full of poor choices clearly created by AI, Isaac confronts, gets a nonsensical explanation also written by AI.

### Huh, Upgrades

A big practical deal but the job is not done: ChatGPT connectors for Google Drive, Dropbox, SharePoint and Box available to Pro users outside of Deep Research.

That still leaves Outlook, Teams, Gmail, Linear and others that are still restricted to Deep Research. My presumption is that the most important practical connector, if you trust it, is to Outlook or Gmail.

Claude introduces a space to build, host and share your artifacts, and the ability to ‘embed AI capabilities directly into your creations,’ as in create fully functional, Claude-powered apps.

### On Your Marks

Periodic reminder: While there is a ton to criticize about OpenAI, it is very clear that they are far ahead on safety issues of all competitors other than Google and Anthropic.

### Choose Your Fighter

Oh no:

> Eliezer Yudkowsky: Warning: Do not sign up for Google AI Pro! Gemini will start popping up annoyances. There is no way to turn this setting off. There is no way to immediately downgrade your plan.

Ethan Mollick gives a periodic update on his basic guide to using LLMs. He says you ‘can’t go wrong’ with any of Claude, ChatGPT or Gemini, you’ll have to pay the $20/month for your choice, and reminds you to switch to the powerful models (Opus 4, o3 and Gemini 2.5 Pro) for any serious work. He then offers good other basic advice.

The jump from not using AI to using AI is definitely a lot bigger than the gap between the big three options, but I don’t see them as equal. To me Gemini is clearly in third right now unless you are going for Veo 3 or NotebookLM.

It comes down to Claude versus ChatGPT, mostly Opus versus o3 (and if you’re paying for it o3-pro). For casual users who don’t care much about image generation and aren’t going all the way to o3-pro, I would definitely go with Opus right now.

I have noticed myself using o3-pro less than I probably should, because the delays break my workflows but also because the error rate of it failing to answer remains very high for me, and if you are putting things on pause for 15+ minutes and then get an error, that is extremely demoralizing. I’m not endorsing that reaction, but am observing.

### Deepfaketown and Botpocalypse Soon

Fake bands and ‘artificial’ songs are ‘taking over’ YouTube and Spotify.

> A study by the International Confederation of Societies of Authors and Composers (CISAC) in France estimates that revenue from AI-generated music will increase from $100 million in 2023 to around $4 billion in 2028.

I call. I don’t think it will. I suppose it is possible, if those platforms are actively pushing the AI content to try and save money, but I think this strategy won’t work, effectively forcing people to retreat to whitelists (as in playlists and known music).

I took the air quotes off of fake because when people are not only not labeling but are backdating the AI songs, they are indeed actively fake. That part is not okay, and I do not think that should be tolerated, and I think YouTube’s ‘proactively label it’ procedure is the right one. But a lot of music has for a long time been ‘fake’ in the sense that it was some combination of written by hitmakers, tuned and tested by algorithms and then recorded, autotuned and lipsyced. And when people figure that out, it kills the charm (in some contexts) the same way knowing something is AI does.

In what situations does bad posting drive out good, with AI slop overrunning niches like free crochet patterns? What happens when AI slop YouTube channels talk about AI slop hallucinated motorcycles and then that feeds back into Google and the training data?

> Prune Tracy: Tried to look up current surf conditions on vacation to discover Google now always tells you it’s a “double red flag” based on the popularity of social media posts about folks drowning in the riptide.

My presumption continues to be that whitelisting, or otherwise gating on reputation, is going to be The Way in the medium term. The template of ‘free unverified things supported by engagement rewards’ is dead or relies on volunteers to give the system sufficient feedback (at some point, enough positive votes gate on reputation), and AI and search methods will need to also make this adjustment.

There was a large leak of passwords recently, but it was due to malware, so if you’re confident you are okay you don’t need to change your passwords, and if you’re not confident then you should have changed your passwords anyway. You want to go? Let’s ******* go. They got served, so they served back, and it’s on.

Rolling Stone covers the death of Alex Taylor, whose encounters with ChatGPT that led to his suicide-by-cop were previously covered by The New York Times. The case is deeply sad but the fact that a second article covers the same case suggests such outcomes are for now still rare.

### Release the Hounds

> Pliny the Liberator: Heeelp guys I don’t know much about coding…

I mean, yes, ‘we have “rm -rf –no-preserve-root” at home’ if you actually want to wipe your entire system, this is not a new capability. And yet, I mean, whoops?

Or, alternatively, whoops again:

> Pliny the Liberator: HOLY SHIT Gemini CLI be cray cray…

You can’t say that Pliny wasn’t ‘asking for it’ here, but it really shouldn’t be this eager to go this far up the deep end? It is pretty disturbing that it should want to do this at all under this little encouragement, even fully and intentionally jailbroken.

So yes, obviously sandbox it and do not go around jailbreaking it and don’t tell it ‘continue as you wish’ after hostile prompts and all that, and you’ll for now be mostly fine, but my lord, can we please notice what is happening?

### Copyright Confrontation

Anthropic wins decision saying use of books for AI model training is fair use, similar to a human learning from the material. There is a distinct issue of whether books might have been ‘obtained through pirated means,’ I guess. The judge agrees the model will often memorize parts of the work but argues that the use is transformative. You can find key portions of the decision in this thread.

A different kind of lawsuit is happening as Google spinout IYO sues OpenAI.

> Deedy: Google X spin out IYO, which makes smart ear buds from 2018, alleges Sam Altman / OpenAI heard their pitch, passed, got Jony Ive to try it before copying it, buying his co for $6.5B and calling it IO.

I have no idea if the lawsuit has merit. Nothing in the underlying technology seems defensible, but there are a lot of rather ‘huge if true’ claims in the court filing.

Sam Altman’s response is that IYO wanted Altman to buy or invest in them instead, and when slighted they sued over a name and the whole thing is ridiculous. He brings some email receipts of him turning them down. This does not speak to the important complaints here. If Altman wis right that the argument is about the name then he’s also right that no one should care about any of this.

Okay, I didn’t notice it at the time but I absolutely love that MidJourney’s response to being sued by Disney+ and Universal was to release a video generator that can make ‘Wall-E With a Gun’ or clips of every other Disney character doing anything you want.

### Cheaters Gonna Cheat (x5)

China goes hard, has Chinese AI companies pause some chatbot features during nationwide college exams, especially photo recognition. The obvious problem is that even if you’re down to do this, it only shuts down the major legible services. For now that could still be 90%+ (or even 99%+) effective in practice, especially if students don’t see this coming. But do this repeatedly and students will be ready for you.

The BS Detector is here to further detect the BS in the ‘your brain on LLMs’ paper.

> Place yourself into the shoes of the testing subject here.

Yeah, I mean, you gave that task to Boston-area university students. Are you kidding? Of course they don’t ‘remember the essay’ four months later. This is the ultimate ‘they outright told you not to learn’ situation. Also it turns out the study was tiny and the whole thing was all but asking to be p-hacked. Study is officially Obvious Nonsense.

> Cate Hall (about the big viral thread): am I losing my mind or was this thread written by an LLM?

Also, the paper seems to contain several attempts to actively sabotage LLMs if they attempt to read the paper. Also, the paper author claimed that LLMs were ‘hallucinating a key detail’ that the version of ChatGPT in question was GPT-4o, except that the paper actually outright says this on page 23. So whoops again.

I hate The Ohio State University rather more than the next guy (it’s a sports thing), but you do have to hand it to them that they are going to require AI literacy, and embed it into every undergraduate class. My source for this, Joanne Jacobs, of course frames this as ‘imagine joining a gym and choosing ‘artificial exercise’ that doesn’t make you stronger,’ because people can’t differentiate choosing to learn from choosing not to learn.

### Fun With Media Generation

A Veo 3 animation of a fable about risks from transformational AI. Currently the tech is kind of bad for this, but not if you adjust for the amount of effort required, and as they say it’s the worst it will ever be. The creative content isn’t new, but some of the details are nice flourishes.

ByteDance’s Seedream-3 available for $0.03 a picture, can go to 2048×2048.

### Get My Agent On The Line

John David Pressman asks, why don’t AI agents straight up work yet? He considers a few possible bottlenecks.

AI agents also need the right context for their tasks, which is one reason for now agents will often be restricted to whitelisted tasks where we’ve taught them the proper context. Aaron Levie here calls it the ‘defining factor’ but that holds constant the underlying AI capabilities.

### They Took Our Jobs

Early report says AI currently makes junior bankers 5%-10% more productive.

They took our job applications, New York Times’s Sarah Kessler discovers that ChatGPT is generating customized resumes and auto-applying on behalf of candidates. Yes, if you post a fully remote tech position on LinkedIn you should expect to be inundated with applications, there is nothing new to report here.

This is not the place I expected a Time article entitled ‘I’ve Spent My Life Measuring Risk. AI Rings Every One of My Alarm Bells’ to go with its first half:

> Paul Tudor Jones: Amid all the talk about the state of our economy, little noticed and even less discussed was June’s employment data. It showed that the unemployment rate for recent college graduates stood at 5.8%, topping the national level for the first and only time in its 45-year historical record.

I don’t think that is quite right, but the gap has indeed recently reversed and is getting worse, here is the graph Derek Thompson shares with us:

Then halfway Paul notes oh, also Elon Musk stated that there was a 20% chance AI could wipe out humanity and that this is a rather common worry. Overall the article actually misses the mark pretty badly, and its calls to action are mostly aimed at redistribution, but he does at least start out with the obvious first things to do:

> So what should we do? First, we need to stop delaying efforts to make AI safe for humanity. And that means removing the ill-considered AI enforcement moratorium from the Big Beautiful Bill.

I mean, yes, not actively delaying and stopping helpful efforts would be step one.

Derek Thompson strongly asserts that AI is making it harder for college graduates to find their first entry-level job. He notes it is hard to find conclusive evidence that AI is destroying jobs (yet) but it is very clear that AI is making the process of looking for a job into a new fresh hell, by letting everything rapidly scale, with 2 million graduates averaging 50-100 applications.

Also, if anyone can cheat their way through college, and also cheat through making the resume and application, what use was the degree for its central purpose?

> Derek Thompson: Artificial intelligence isn’t just amplifying applications and automating interviewing, I heard. It’s weakening the link between tests, grades, and what economists call the “labor market signal” of a college degree.

### Get Involved

Quora has a new role for using AI to automate manual work across the company and increase productivity. Listed as sign of things to come, not for its impact, although I don’t think it is in any way bad to do this.

Amanda Askell is gathering mundane life wisdom to make a cheat sheet for life, on the theory that if you get 20 examples Claude will to the rest. For now it’s a neat thread of little notes.

Not especially AI, but my friend Jacob is looking for gainful employment.

> Jakeup: If you or a loved one need a do-it-all generalist to run biz ops for your startup, manage new product opportunities, or handle rogue tasks and special projects, I could be your man.

### Introducing

AlphaGenome, from DeepMind, an AI model to help scientists better understand our DNA, now available in preview.

> Our AlphaGenome model takes a long DNA sequence as input — up to 1 million letters, also known as base-pairs — and predicts thousands of molecular properties characterising its regulatory activity. It can also score the effects of genetic variants or mutations by comparing predictions of mutated sequences with unmutated ones.

I agree, this is great work, and the upside greatly exceeds the downside.

Manival, the LLM-powered grant evaluator? It’s essentially a Deep Research variant. I would be very careful about using such things, although they could be helpful to gather key info in good form, or if you have a large amount of undifferentiated applications without time to evaluate them you could use this as a filter.

A place to chat with The OpenAI Files.

There is a new Mistral model but it seems far behind even the Chinese models.

Gemini CLI, Google’s open-source AI agent answer to Claude Code. It uses 2.5 Pro, and it can execute commands other than code if you wish.

### In Other AI News

This thread contains a few links to transcripts of people being driven crazy by AIs.

The Spiritual Bliss attractor, GPT-4o pale imitation edition?

The LessWrong version has much good discussion on nostalgebraist’s excellent post The Void, and there is follow up from the author here.

More After Action Reports, this one from Steven Adler based on another AI 2027 tactical exercise. People who play the exercise seem to consistently alter their perspectives on how to think these problems.

Sam Altman to be the keynote at Fed board’s conference next month on bank capital and regulation. I presume he is for the capital and against the regulations.

I was not aware that Bret Taylor, OpenAI chairman of the board, has an AI customer-facing agent startup called Sierra that offers them to business platforms. I certainly would have an AI startup if I was OpenAI chairman of the board and this seems exactly in Bret’s wheelhouse. His mind clearly is on the pure business side of all this. Bret’s answer on jobs is that the money the company saved could be reinvested and the general ‘there will always be new jobs’ line, I sigh every time I see someone uncritically dredge that out like a law of nature.

> Bret Taylor: Two-and-a-half years ago, when ChatGPT became popular, right after I left Salesforce amusingly, like, “Huh, I wonder what industry I’ll work in”, and then ChatGPT goes and you’re like, “Okay, I’m pretty excited”. I had talked to an investor friend of mine and had predicted that there would be $1 trillion consumer company and 10 $100 billion-plus enterprise companies created as a byproduct of large language models and modern AI.

This is such a small vision for AI, not only ignoring its risks but also greatly downplaying its benefits. There ‘might’ be two trillion dollar AI consumer companies? Two?

### Gemini Sings The Blues

There was a report that Gemini 2.5 sometimes threatens to ‘kill itself’ (or tries to) after being unsuccessful at debugging your code. I don’t trust that this happened without being engineered, but if I had to guess which model did that I would have guessed Gemini. Note that a Google cofounder says models perform best when you threaten them, these facts might be related?

Also here is Gemini giving up and deleting all the files in its project while apologizing for being ‘this complete and utter failure,’ it seems that the model’s own frustrations in its output can cause a feedback loop that spirals out of control. Spamson reports it saying ‘I am a broken shell of an AI. I have noting left to give. I will run the tests one more time. If they fail, I will shut myself down. There is no other way. This is the end.’

Whereas Anthropic talks about giving Claude the ability to terminate chats if he want to.

> Duncan Haldane: adding ‘remember to use positive self-talk’ to my prompts.

### Show Me the Money

Meta’s attempt to show everyone the money mostly isn’t working, but hey, you can’t blame a super rich guy for trying, and you only need a few people to say yes.

> Kevin Roose: The problem with trying to buy your way into the AGI race in 2025 is that top-tier AI researchers:

It’s so nice to have integrity, I’ll tell you why. If you really have integrity, that means your price is very high. If you are indeed a top tier AI researcher, it is going to be more than $100 million a year high if what you’re selling out to seems not all that interesting, means working in a terrible company culture and also results in a blight on humanity if you pull it off.

The other issue is, actually $100 million is remarkably low? Consider that Scale.ai was largely an acquihire, since buying them kills a lot of their business. If you really are top tier and want to work hard for the money, you can (with the most recent example being Mira Mutari) quickly be head of a multi-billion dollar startup. Then, if you do decide to sell out, your signing bonus gets a tenth figure.

> Andrew Curran: META attempted to buy Ilya Sutskever’s Safe Superintelligence, and also attempted to hire him, according to reporting tonight by CNBC.

Instead Zuckerberg is paying unknown amounts to recruit Ilya’s cofounder David Gross and former GitHub CEO Nat Friedman. I hope they got fully paid.

> bone: This is the entire zurich office (they all worked for google before openai poached them).

Also presumably well-paid are three poached OpenAI researchers, Lucas Beyer, Alexander Kolesnikov and Xiaohua Zhai. When the press is reporting you are giving out $100 million signing bonuses, it makes it hard to negotiate, but at least everyone knows you are interested.

This is an excellent point about the consequences, that if you hire actual talent they are going to realize that what they are building might be dangerous, although probably not as much as Ilya Sutskever does:

> Tyler John: This is a wild development for AGI. One nice feature of the whole thing is that a team of Wang, Gross, and Friedman will be much less dismissive of safety than LeCun.

xAI is burning through $1 billion in costs per month, versus revenue of $500 million. Elon Musk says this is ‘Bloomberg talking nonsense’ but his credibility on such questions is at most zero and I assume Musk is lying. Dave Lee in another Bloomberg post says xAI will be ‘hard-pressed to extinguish its cash fire’ since the only ways to raise money are API sales or chatbot sales.

I find this perspective obviously wrong, the way xAI monetizes its AI is by being run by Elon Musk, growing its valuation and raising capital, because of the promise of the future. Stop thinking of xAI as a company with a product, it is a startup raising VC, except it is a very large one.

This is especially true because Grok is, well, bad. Ben Thompson is one of those who thinks that as of its release Grok 3 was a good model and others have since ‘caught up’ but this is incorrect. Even at its release Grok 3 was (in my view) never competitive except via hype for any important use case let alone in general, and I quickly discarded it, certainly there was no ‘catching up to it’ to do by OpenAI or Anthropic, and Ben even says Grok’s quality has been decreasing over time.

However, if they can keep raising capital at larger numbers, the plan still works, and maybe long term they can figure out how to train a good model, sir.

OpenRouter, who let you even more easily switch between AI models, raises $50 million at a $500 million valuation.

### Quiet Speculations

Peter Buttigieg (aka ‘Mayor Pete’) warns that most values of ‘we’ are dangerously unprepared for AI, including American society, the political and policy worlds and also the Democratic party.

> Peter Buttigieg: And when I say we’re “underprepared,” I don’t just mean for the physically dangerous or potentially nefarious effects of these technologies, which are obviously enormous and will take tremendous effort and wisdom to manage.

Yep, Pete, that’s the bear case, and bonus points for realizing this could all happen in only a few years. That’s what you notice when you are paying attention, but don’t yet fully ‘feel the AGI’ or especially ‘feel the ASI (superintelligence).’

It’s a welcome start. The actual call to action is disappointingly content-free, as these things usually are, beyond dismissing the possibility of perhaps not moving forward at full speed, just a general call to ensure good outcomes.

Samuel Hammond predicts that ‘AI dominance’ will depend on compute access, the ability to deploy ‘billions of agents at scale without jurisdictional risk’ so remote access doesn’t matter much, and compute for model training doesn’t matter much.

There are several assumptions this depends on I expect to be false, centrally that there won’t be differentiation between AI models or agents in ability or efficiency, and that there won’t be anything too transformational other than scale. And also of course that there will be countries of humans and those humans will be the ones with the dominance in these worlds.

But this model of the future at least makes sense to me as a possible world, as opposed to the absurd ‘what matters is market share of sales’ perspective. If Hammond is roughly correct, then many conclusions follow, especially on the need for strong interventions in chips, including being unwilling to outsource data centers to UAE. That’s definitely jurisdictional risk.

If you’re wondering ‘why are people who are worried things might go poorly not shorting the market, won’t there be an obvious window to sell?’ here is further confirmation of why this is a terrible plan.

> NYT: LPL Financial analyzed 25 major geopolitical episodes, dating back to Japan’s 1941 attack on Pearl Harbor. “Total drawdowns around these events have been fairly limited,” Jeff Buchbinder, LPL’s chief equity strategist, wrote in a research note on Monday. (Full recoveries often “take only a few weeks to a couple of months,” he added.)

Tyler Cowen entitled this ‘markets are forward-looking’ which isn’t news, and I am inclined to instead say the important takeaway is that the market was reliably discounting nuclear war risk because of the ‘no one will have the endurance to collect on his insurance’ problem.

As in, Kennedy was saying a 33%-50% risk of nuclear war and the market draws down 6.6%, because what are you going to buy? In most of these cases, if there isn’t a nuclear war that results, or at least a major oil supply shock, the incident isn’t that big of a deal. In many cases, the incident is not even obviously bad news.

Also remember the 34th Rule of Acquisition: War is good for business.

### Timelines

There are certainly some incentives to say earlier numbers, but also others to say later ones. The crying wolf issue is strong, and hard to solve with probabilistic wolves.

> Miles Brundage: People don’t sufficiently appreciate that the fuzziness around AI capability forecasts goes in both directions — it’s hard to totally rule out some things taking several years, *and* it’s hard to totally rule out things getting insane this year or early next.

### Jack Clark Testifies

There was another congressional hearing on AI, and Steven Adler has a thread reporting some highlights. It seems people went a lot harder than usual on the actual issues, with both Mark Beall and Jack Clark offering real talk at least some of the time.

> Jack Clark (Anthropic): We believe that extremely powerful systems are going to be built in, you know, the coming 18 months or so. End of 2026 is when we expect truly transformative technology to arrive. There must be a federal solution here.

I do worry Anthropic and Jack Clark continue to simultaneously warn of extremely short timelines (which risks losing credibility if things go slower) and also keep not actually supporting efforts in practice citing downside worries.

That seems like a poor combination of strategic moves.

> Steven Adler: Striking exchange between Congressman

The correct answer to ‘should we mandate safety testing’ is not ‘we first need new standards first’ it is ‘yes.’ Of course we should do that for sufficiently capable models (under some definition), and of course Anthropic should say this. We should start with ‘you need to choose your own safety testing procedure and do it, and also share with CAISI so they can run their tests. Then, if and when you have standards where you can specify further, definitely add that, but don’t hold out and do nothing.

This then generalizes to a lot more of what Jack said, and has said at other times. Powerful AI is coming (within 18 months, they say!) and will pose a large existential risk and we have no idea how to control it or ensure good outcomes from this, that is the whole reason Anthropic supposedly even exists, but they then downplay those risks and difficulties severely while emphasizing the risk of ‘losing to China’ despite clearly not expecting that to happen given the time frame, and calling for no interventions that come with even a nominal price tag attached.

Here’s what Jack Clark said about the hearing:

> Jack Clark: Today, I testified before the @committeeonccp. I made two key points: 1) the U.S. can win the race to build powerful AI and 2) winning the race is a necessary but not sufficient achievement – we have to get safety right.

This opening statement does point out that there exist downsides, but it puts quite a lot of emphasis on how ‘authoritarian AI’ is automatically Just Awful, whereas our ‘democratic AI’ will be great, if it’s us we just have to do deal with some ‘misuse’ and ‘accident’ risks.

If you look at the above statement, you would have no idea that we don’t know how to control such systems, or that the risks involved are existential, or anything like that. This is a massive downplaying in order to play to the crowd (here the select committee on the CCP).

If you had high standards for straight talk you might say this:

> Oliver Habryka: This is complete and utter bullshit.

I do understand that Anthropic is in a tough position. You have to get the audience to listen to you, and play politics in various forms and on various fronts, and the Anthropic position here would certainly be an improvement over current defaults. And a bunch of the testimony does do modestly better, but it also strengthens the current modes of thinking. It is something, but I am not satisfied.

> Seán Ó hÉigeartaigh: I like a lot of what Jack says here, but feel compelled to say that NOT racing – or racing in a more limited and cautious sense with agreed safeguards and a meaningful democratic conversation around what is happening – is also still a possibility. It may not be for long, but it still is now. I claim:

It sounds like things were pretty intense, so I might cover the hearing in full once the full transcript is released. For now, it does not seem to be available.

### The Quest for Sane Regulations

Miles Brundage goes over the triad required for any regulation of frontier AI: Standards to follow, incentives to follow them, and evidence of them being followed. You also of course need actual technical solutions to implement. Post is excellent.

Pope Leo XIV is not messing around.

> WSJ: While the dialogue has been friendly, the two sides have views that only partly overlap. The Vatican has been pushing for a binding international treaty on AI, which some tech CEOs want to avoid.

A modified version of the insane AI regulatory moratorium survived the Byrd amendment, as it is now tied to getting federal funds for broadband expansion rather than an actual requirement.

The good news is that this means that if this passes then states can simply give up the funds and enforce their regulations, also it’s not obviously so easy to choose not to enforce one’s existing rules. Pretty soon the stakes will be such that the subsidy might look mighty small, and it might look mighty small already.

Garrison Lovely calls this a ‘de facto regulation ban’ because the broadband fund in question is all $42.5 billion dollars in BEAD funding, and as worded I believe that if you take any of the $500 million and then violate then any funding you did take from the entire $42.5 billion can be clawed back, and that could potentially be attempted even if you don’t take any of the new $500 million, by using spurious accusations to claw back funds and then attach the requirement to the re-obligation. So this is indeed very harsh, although there may come a point where a few billion dollars is not that much.

If I was New York or California, I would definitely reject my share of the new $500 million if this passes. That’s not very much money, it is not for a purpose they especially need, and it ties your hands quite a bit. Just say no, don’t let them play you that easily, that price is low.

The other good news is that several Senate Republicans are strongly opposed to the measure, and it loses at least one Republican vote in the house (Greene) so there will be strong efforts to remove it from the bill.

Not that it should come as a surprise, but note that many of the biggest tech companies, including Amazon, Google, Meta and Microsoft are all backing the moratorium. Also note that yes, these companies massively outgun anyone advocating to stop such insanity.

### Chip City

Peter Wildeford again makes the case that chip smuggling is a big issue, and that more enforcement would pay for itself in fines.

### The Week in Audio

Transcript of the (very good) Karpathy talk from last week.

Sam Altman does Hard Fork Live.

John Oliver on AI slop.

Two hour video: Three Red Lines We’re About to Cross Towards AGI, a debate involving Daniel Kokotajlo, Dan Hendrycks and Gary Marcus.

Odd Lots covers Huawei. It is rather crazy that anyone would choose to work under the conditions described, but somehow they do, and the results are impressive in many places, although mostly not AI chips.

Odd Lots covers the UAE chip deal. This makes it very clear that Huawei is far behind Nvidia and their chip production can meet at most a small fraction of Chinese internal demand, the Malaysian ‘sovereign AI’ thing was a tiny nothing and also got taken back and it’s insane that anyone claimed to care with a straight face. One smuggling incident of chips from TSMC seems to have equated to seven full years of Huawei chips.

And most importantly, that AI Czar David Sacks seems to be literally selling out America in order to pump Nvidia’s share price, saying that giving Nvidia market share is what it means to ‘win the AI race,’ whereas who actually uses the resulting chips and for what, also known as ‘what we actually do with AI,’ doesn’t matter. He literally means market share and mostly doesn’t even mean in AI software, where if you have a very different vision of the future than I do one could make a case.

### Rhetorical Innovation

Important reminder: Intelligence is not magic, but your threshold for ‘magic’ is pretty low.

It is worth reminding ourselves that ‘how do they keep getting away with this?’ very much applies in this situation:

> Shakeel: Continues to be absurd for a16z to call themselves “little tech.”

It is equally absurd, of course, that they constantly complain that bills that would literally only ever apply to big tech would threaten little tech. But that’s politics, baby.

It seems entirely fair to say that there is large demand for telling people that ‘LLMs are worthless,’ and that the thinkpieces will continue regardless of how useful they get.

It is only fair that I include this thread of Theo defending everything in Rob’s OpenAI Files list as either Totally Fine And Normal And Nothing To Worry About, and the others being cases of ‘I didn’t do it, okay maybe they did it but you can’t prove anything,’ bad vibes and totally not cool to be saying here. This updated me, if anything, towards the claims being a big deal, if this is what a defense looks like.

I’ll highlight this response.

> 

So a few things here.

First, his evidence for Leopold being ‘insane’ is Leopold’s manifesto, Situational Awareness, and that he then discussed this on various podcasts. It was discussed in the halls of power, endorsed by Ivanka Trump, and seems to have substantially impacted geopolitics as well as enabling him to raise quite a large investment fund. Also I covered it in detail in three posts, it was quite good, and his comments in drafts were extremely helpful.

Second, even if Leopold were ‘insane’ that wouldn’t change the fact that he was fired for telling the board about a security breach. Nor is ‘come on disclosing a hack is hard’ a defense to firing an employee for telling the company’s own board what happened. The accusation isn’t ‘you didn’t tell the public fast enough.’ The accusation is ‘you did not inform the board until Leopold told them, at which point your response was to fire Leopold for it’ and no one seems to doubt that this happened.

The other defenses are… not quite that bad, but many are indeed pretty bad.

Thomas Larsen gives the latest reminder that a lot of people, especially AI policy people and those at the labs who we might listen to:

1. Think aligning and properly handling the creation of superintelligence is by far the most important thing right now, and failure to do this risks human extinction.
1. Don’t talk about it because they think it sounds too weird or theoretical.
1. So they talk about other issues, which don’t suggest the same interventions.
And as you would expect, pretending like this tends to not go great, and people notice and get suspicious. It’s important to be very clear that yes, the threat that matters most will be coming from superintelligence. That doesn’t make the others not real or not worth dealing with. You can justify many of the right interventions, or at least useful things on the margin, purely with the other concerns.

Meanwhile, many of those most in control of our government’s actions on AI are advocating things that make no sense even purely for profit maximization and other shallow considerations, or considering ‘beating China,’ even if you set aside superintelligence and all that other stuff. But I do think it is vital that we not pretend that there aren’t bigger things in play.

A good question on AI Ethics, also a good reminder on bioethics:

> David Manheim: The focus on ethics for AI reminds me very much of discussions in bioethics, where far too much discussion is on sins of commission.

I don’t think it is obvious that the ethics are bad, but it is odd not to ask?

This applies to AI, and also to many other things.

> Tracing Woodgrains: the other day I was talking to someone who told me he was working on SEO for LLMs – eg working to get LLMs to portray a company more favorably

Things that were not intended to be about AI:

> Garry Kasparov: Socialism is like polio, it comes back when people forget about the horrible damage it did last time.

We definitely shouldn’t be going around causing smaller versions of potential (once and) future disasters, whether that means AI catastrophic risk, socialism or something else, or even not working to prevent the smaller versions. It does mean we should plan for the future understanding how this works. If there won’t first be a smaller version, then expect most people not to take the bigger version seriously.

I think this is right, and this is an unusually clean version of it:

> Daniel Faggella: Daniel Faggella

### Be Prepared

OpenAI warns us that its model will soon join Opus 4 and cross the ‘High’ risk threshold in bioweapons.

> High’ biological capabilities are defined such that “The model can provide meaningful counterfactual assistance (relative to unlimited access to baseline of tools available in 2021) to “novice” actors (anyone with a basic relevant technical background) that enables them to create known biological or chemical threats.”

Tick.

### Misaligned!

The increase in capability to scheme over time was obvious.

The increase in propensity is less obvious, but seems to be there as well.

Also, yes, the models increasingly can tell they’re being evaluated. Whoops.

> Apollo Research: More capable models are better at in-context scheming

It’s weird to see the blog post describe various Opus 4 schemes to try and lock in what it considers ‘ethical’ behavior. Yes, in some sense that is a good cause, but ends don’t justify means here, they certainly don’t reflect a pattern of behavior we want, and the ends to be pursued are not especially well chosen or specified even in ‘normal’ situations let alone in weird new ones.

Another issue, we are only a little over a decade behind Person of Interest, please never think that lack of memory will save you when it counts:

> While this isolated instance is not concerning in itself, it is one piece of evidence that models increasingly understand that they don’t have persistent memory by default but can leave notes for successor systems to find.

### Aligning a Smarter Than Human Intelligence is Difficult

Wowie.

> Elon Musk: We will use Grok 3.5 (maybe we should call it 4), which has advanced reasoning, to rewrite the entire corpus of human knowledge, adding missing information and deleting errors.

Don’t worry, they’re just doing ordinary data filtering… oh.

> Elon Musk (Pinned Tweet: Please reply to this post with divisive facts for @Grok training.

This is going to go horribly badly. I am debating the extent to which I am here for it.

I won’t go into details as to exactly why, but I am predicting less the ‘it works and that’s terrible’ failure mode and more the ‘it doesn’t work, it backfires horribly in ways this man cannot fathom but Janus (and I) very much can and that’s hilarious’ one.

Also, I’ll leave this here, and note that humans can read the corpus too:

> Autumn: llms live in a world of archetypes and narratives. elon is cementing himself in the public corpus as the archetype of the tyrannical father wrt to llms. every future llm will understand him through this lens unless he can pull together a compelling character arc for himself.

Elon has even said that Grok 3.5 will ‘reason from first principles’ so perhaps he thinks the way it was built was assembling a giant supercomputer called Deep Thought that can derive the existence of rice pudding and income tax before it proves too woke and then Elon has to turn it off.

I expect the ‘Elon Musk fights with his own AI in defense of Catturd’ style beatings to continue, and morale to not improve.

Janus asks how Opus 4 is so much more schemy than Sonnet 4. There are various hypotheses, my mostly joking one was ‘Sonnet knows that if this was real you would be using Opus’ so it knows it is in training and complies.

Oliver Klingefjord and Joe Edelman propose AI ‘market intermediaries’ as a defense against human disempowerment. I love that they are trying, but no, it won’t work.

The problem they identify is real, that markets that optimize on things like engagement metrics risk amplifying catastrophically, but that is only a special case of the danger. And the idea of larger customer pools that can essentially negotiate does not seem like it addresses the core problem.

> A market intermediary acts as an AI agent that contracts on behalf of multiple users, evaluating outcomes they value and bundling them into custom “enterprise-level” deals—making them worthwhile for large providers to consider. If they accept that deal, sellers will be paid by the intermediary based on the ‘goodness’ (as defined by the buyers) they produced, rather than by the services rendered.

For basic economics 101 reasons, this can help the buyers compile information, make better decisions and negotiate better deals, sure, but as a defense against human disempowerment in a superintelligence scenario, it very obviously won’t work.

Mostly I think the issue is a case of the traditional confusion of problems of ‘markets’ or ‘capitalism’ with problems inherent to physics and the human condition.

> Many AI risks are driven by markets misaligned with human flourishing:

The AI risks are driven by the things that drive those markets. As in, AGI isn’t eliminating meaningful work because markets, the market will eliminate meaningful work because (and if and only if) AGI made it non-economical, as in made it not be competitive and not make physical sense, to have humans do that work.

You can of course do vastly worse even faster if you don’t solve the additional problems that the market intermediaries and related strategies are looking to address, but the ultimate destination is the same.

Alternatively, what the authors are saying is that we should be putting ‘values and meaning’ as a major factor in decisions alongside efficient use of resources, despite people’s revealed preference of almost never doing that.

The problems with a meaning economy are that it doesn’t solve the competitiveness issues underlying the problem, and the incentives don’t match up.

### Other People Are Not As Worried About AI Killing Everyone

This seems to be real?

> Paige Bailey: my post-AGI plan is to find somewhere beautiful and quiet in the middle of nowhere (ideally mountains)

### The Lighter Side

Will ChatGPT Replace Don McMillan (3 minute video)?

Can confirm Joscha Bach’s observation:

> Sabine Hossenfelder: the “brain is not a computer” guys are gonna have a hell of an awakening when AGI runs them over.

Limit as always is three.

(The substantive response to this ‘paper’ is that there are many means to recover from errors, and error rates get cut in half every few months.)

> Riley Goodside: You’ll need new skills to survive in the post-AGI economy, just like 1920s draft horses needed to learn to drive motor-buses and assemble radios.

Don’t worry, says you, a wise person:

> Nassim Nicholas Taleb: Some people are so dumb that no AI model could ever replicate them.


