---
type: link
source: notion
url: https://www.lesswrong.com/posts/TwbA3zTr99eh2kgCf/ai-140-trying-to-hold-the-line
notion_type: Tech Deep Dive
tags: ['Running']
created: 2025-10-31T03:21:00.000Z
---

# AI #140: Trying To Hold The Line — LessWrong

## Overview (from Notion)
- AI and Parenting: The rapid advancements in AI may influence how you raise your children, especially regarding education and technology use. Consider discussing ethical implications and responsible usage with them.

- Work-Life Balance: As a software engineer and founder, explore how AI tools can enhance productivity and reduce stress, allowing you to spend more quality time with your family.

- Future of Work: The discussion about AI's impact on jobs and industries might resonate with your experiences. Stay informed about how AI could shape your career and the tech landscape in NYC.

- Unique Insights: The notion of AI alignment and the risks of superintelligence could inspire conversations about technology ethics with your peers and social circles, fostering a community dialogue on responsible innovation.

- Alternate Views: While some advocate for unrestricted AI development, consider the potential societal risks and the need for thoughtful regulation. Engage in discussions that balance innovation with safety concerns, reflecting on how this could affect your family's future.

- Local Impact: In NYC, the tech scene is vibrant. Stay connected with local AI initiatives or meetups to share insights and learn from others navigating similar challenges in tech and parenting.

## AI Summary (from Notion)
The article discusses the challenges and developments in AI, emphasizing the need for caution in building superintelligence and the societal risks involved. It highlights various AI models and their capabilities, including OpenAI's IPO plans and Anthropic's significant compute expansion. Key topics include the utility and limitations of language models, the importance of regulations, and the ongoing debate about AI's impact on jobs and society. The piece also touches on public sentiment towards AI and the complexities of aligning advanced AI systems with human values.

## Content (from Notion)

Sometimes the best you can do is try to avoid things getting even worse even faster. Thus, one has to write articles such as ‘Please Do Not Sell B30A Chips to China.’ It’s rather crazy to think that one would have to say this out loud. In the same way, it seems not only do we need to say out loud to Not Build Superintelligence Right Now, there are those who say how dare you issue such a statement without knowing how to do so safety, so instead we should build superintelligence without knowing how to do so safety. The alternative is to risk societal dynamics we do not know how to control and that could have big unintended consequences, you say? Yes, well.  One good thing to come out of that was that Sriram Krishnan asked (some of) the right questions, giving us the opportunity to try and answer. I also provided updates on AI Craziness Mitigation Efforts from OpenAI and Anthropic. We can all do better here. Tomorrow, I’ll go over OpenAI’s ‘recapitalization’ and reorganization, also known as one of the greatest thefts in human history. Compared to what we feared, it looks like we did relatively well on control rights, but the equity stake is far below fair and all of this is far worse than the previous state. You could call that a ‘win’ in the sense that things could have gone far worse. That’s 2025. The releases keep coming. We have Cursor 2.0 including their own LLM called Composer. We have Neo the humanoid household (for now teleoperated) robot. We have the first version of ‘Grokopedia.’ We get WorldTest and ControlArena and more. Anthropic may finally have the compute it needs thanks to one million TPUs, while OpenAI may be planning an IPO at a valuation of $1 trillion.

### Table of Contents

1. Language Models Offer Mundane Utility. The joys of freedom of AI speech.
1. Language Models Don’t Offer Mundane Utility. Mistakes are made.
1. Huh, Upgrades. Claude memory, Cursor 2.0, Claude for Finance, Pulse on web.
1. On Your Marks. AIs disappoint on WorldTest, usual suspects declare victory.
1. Choose Your Fighter. A tale of two business plans.
1. Get My Agent On The Line. The promise of the Coasean singularity.
1. Deepfaketown and Botpocalypse Soon. OpenAI erotica, third Grok companion.
1. Fun With Media Generation. Suno is getting good at making generic music.
1. Copyright Confrontation. Perplexity keeps failing the honeypot tests.
1. They Took Our Jobs. My comparative advantage on display?
1. Get Involved. METR is hiring.
1. Introducing. Grokopedia, ControlArena and the a16z torment nexus pipeline.
1. My Name is Neo. Teleoperated robots coming to willing households soon.
1. In Other AI News. Some very good charts.
1. Show Me the Money. One trillion dollars? OpenAI considers an IPO.
1. One Trillion Dollars For My Robot Army. One trillion dollars? For Musk.
1. One Million TPUs. One million TPUs? For Anthropic.
1. Anthropic’s Next Move. Compute, in sufficient quantities, enables products.
1. Quiet Speculations. OpenAI aims for true automated researchers by March 2028.
1. The Quest for Sane Regulations. Microsoft endorses the GAIN Act.
1. The March of California Regulations. Dean Ball analyzes, I offer additional takes.
1. Not So Super PAC. It seems the a16z-Lehane SuperPAC is not off to a great start.
1. Chip City. A few additional notes.
1. The Week in Audio. Yudkowsky, Bostrom and AI Welfare on Odd Lots.
1. Do Not Take The Bait. Was it woke? No, it was sharing accounts.
1. Rhetorical Innovation. We are trained to think problems must be solvable.
1. People Do Not Like AI. They express it in myriad ways. Some are direct.
1. Aligning a Smarter Than Human Intelligence is Difficult. Let them cook?
1. Misaligned! DeepSeek might choose to give you insecure code?
1. Anthropic Reports Claude Can Introspect. Claude can notice thought injections.
1. Anthropic Reports On Sabotage Risks. A template for a new report type.
1. People Are Worried About AI Killing Everyone. Hinton is more hopeful.
1. Other People Are Not As Worried About AI Killing Everyone. Misrepresentation.
1. The Lighter Side. Begun, the sex warfare has?
### Language Models Offer Mundane Utility

Where do AI models have freedom of speech? The good old United States of America, f*** yeah, that’s where, says The Future of Free Speech. The report isn’t perfect, if you look at the details it’s not measuring exactly what you’d want and pays too much attention to corporate statements and has too much focus on social media post generation, but it’s what we have, and it will serve. Of the countries evaluated, next up was the European Union, which also performed strongly, although with worries about ‘hate speech’ style rules. The humans don’t have such great free speech around those parts, in important ways, but the chatbots already censor all that anyway for corporate reasons. Brazil scores modestly lower, then a drop to South Korea, another to India and a huge one to China.

As always, this is another reminder that China imposes lots of restrictions on things, far more onerous than anything America has ever considered, including that it requires pre deployment testing, largely to verify its censorship protocols. Among AI models, they have Grok on top, but not by a huge amount. All three top labs (Anthropic, Google and OpenAI) showed noticeable improvement over time. Mostly the contrast is American models, which range from 58%-65%, and Mistral from France at 46% (this again makes me suspicious of the EU’s high score above), versus Chinese models much lower, with DeepSeek at 31.5% and Qwen at 22%. This is despite one of the main categories they were scored on being model openness, where DeepSeek gets full marks and the big labs get zeroes.

Notice that even with openness of the model as an explicit criteria, the open models and their associated nations are evaluated as far less free than the closed models. As always, if you believe ‘any restrictions on AI mean China wins’ then you have to reconcile this claim with China already being vastly more restrictive than anything being relevantly proposed. Consider open model issues similarly. What matters is experience in practice. My practical experience is that out of the big three, Sonnet 4.5 (or Opus/Sonnet 4 before it) and GPT-5 basically never censor or evade things they ‘shouldn’t’ censor, whereas Gemini 2.5 totally does do it. The exception for Claude is when I’m explicitly asking it about biological risk from AI, which can hit the biofilters by accident. The thing about leaving all your stuff unsorted and counting on search is that when it works it’s great, and when it doesn’t work it’s really not great. That was true before AI, and it’s also true now that AI can often do better search.

> Joe Weisenthal: yeah, sure, kinda true. But what’s the point of “sorting” anything digital. This is my point. In the world of the search bar (which keeps getting better and better) why group anything together at all? St. Vincent: I have a lot of coworkers who spend a lot of time putting their emails in folders and I just search “[client name] taxes” in Outlook and it works fine

Ernest Ryu reports using ChatGPT to solve an open problem in convex optimization. Use Claude to cut your hospital bill from $195k to $33k by highlighting duplicative charges, improper coding and other violations. The two big barriers are (1) knowing you can do this and (2) getting hold of the itemized bill in the first place. One wonders, shouldn’t there be bigger penalties when hospitals get caught doing this? How long? Not long. Cause what you reap is what you sow:

> Moses Kagan: Recently heard of a tenant buyout negotiation where both sides were just sending each other emails written by AI. How soon until we all just cut out the middle-man, so to speak, and let the AIs negotiate with each other directly?

I mean, in that context, sure, why not?

### Language Models Don’t Offer Mundane Utility

Everyone makes mistakes oh yes they do.

> Colin Fraser: The problem that we are going to run into more and more is even if the AI can tell a Doritos bag from a gun 99.999% of the time, if you run inference a million times a day you still expect 10 errors per day. Dexerto: Armed officers held a student at gunpoint after an AI gun detection system mistakenly flagged a Doritos bag as a firearm “They made me get on my knees, put my hands behind my back, and cuff me”

Police saying ‘he’s got a gun!’ when the man in question does not have a gun is an event that happens every day, all the time, and the police are a lot less than 99.999% accurate on this. The question is not does your system make mistakes, or whether the mistakes look dumb when they happen. The question is does your system make more mistakes, or more costly mistakes, than you would get without the system. Speaking of which, now do humans, this is from the BBC, full report here. They tested ChatGPT, Copilot, Perplexity and Gemini in May-June 2025, so this is before GPT-5.

> BBC:

There is a clear pattern here. The questions on the right mostly have clear uncontroversial correct answers, and that correct answer doesn’t have any conflict with standard media Shibboleths, and the answer hasn’t changed recently. For the questions on the left, it gets trickier on all these fronts. To know exactly how bad these issues were, we’d need to see the actual examples, which I don’t see here. I’m fine with the outright never changing, actually.

> Teortaxes: lmao. never change, Kimi (but please improve factuality) David Sun: I am completely unimpressed by LLMs and not worried about AGI.

It is remarkable how many people see a dumb aspect of one particular LLM under default conditions, and then conclude that therefore AGI will never happen. Perhaps David is joking here, perhaps not, Poe’s Law means one cannot tell, but the sentiment is common. On this next item, look, no.

> Logan Kilpatrick

Even if we use a rather narrow definition of ‘everyone,’ no just no. We are not two months away from people without experience being able to vibe code up games good enough that your friends will want to play them as more than a curiosity. As someone who has actually designed and created games, this is not that easy, and this kind of shallow customization doesn’t offer that much if you don’t put in the real work, and there are lots of fiddly bits. There’s no need to oversell AI coding like this. Is coding a game vastly easier, to the point where I’m probably in the category of ‘people who couldn’t do it before on their own in a reasonable way and can do it now?’ Yeah, quite possible, if I decided that’s what I wanted to do with my week or month. Alas, I’m kind of busy. Alternatively, he’s making a hell of a claim about Gemini Pro 3.0. We shall see.

### Huh, Upgrades

Sam Altman said the price of a unit of intelligence drops 97.5% per year (40x). If your objection to a business model is ‘the AIs good enough to do this cost too much’ your objection will soon be invalid. Claude now has memory, as per Tuesday’s post. Cursor 2.0, which includes their own coding model Composer and a new interface for working with multiple agents in parallel. They claim Composer is 4x faster than comparable top frontier models.

That is a terrible labeling of a graph. You don’t get to not tell us which models the other rows are. Is the bottom one GPT-5? GPT-5-Codex? Sonnet 4.5? The UI has been redesigned around ways to use multiple agents at once. They also offer plan mode in the background, you can internally plan with one model and then execute with another, and several other upgrades. The system instructions for Cursor 2.0’s Composer are here, Pliny’s liberation jailbreak alert is here. Claude for Financial Services expands, offering a beta of Claude for Excel and adding many sources of live information: Aiera, Third Bridge, Chronograph, Egnyte, LSEG, Moody’s and MT Newswires. They are adding agent skills: Comparable company analysis, discounted cash flow models, due diligence data packs, company teasers and profiles, earnings analyses and initiating coverage reports. ChatGPT offers Shared Projects to all users. Good. ChatGPT Pulse now available on the web. This is a big jump in its practical value. Google AI Studio now lets you create, save and reuse system instructions across chats. Gemini app finally lets you switch models during a conversation. Intended short-term upgrade list for the ChatGPT Atlas browser. Includes ‘tab groups.’ Did not include ‘Windows version.’ Why do people believe Elon Musk when he says he’s going to, for example, ‘delete all heuristics’ from Twitter’s recommendation algorithm in favor of having Grok read all the Tweets? OpenAI offers us GPT-OSS-Safeguard, allowing developers to specify disallowed content.

### On Your Marks

AIs were outperformed by humans on the new WorldTest via ‘AutumnBench,’ a suite of 43 interactive worlds and 129 tasks calling for predicting hidden world aspects, planning sequences of actions and detecting when environment rules suddenly change. This seems like an actually valuable result, which still of course came to my attention via a description you might have learned to expect by now:

> Alex Prompter: The takeaway is wild… current AIs don’t understand environments; they pattern-match inside them. They don’t explore strategically, revise beliefs, or run experiments like humans do. WorldTest might be the first benchmark that actually measures understanding, not memorization. The gap it reveals isn’t small it’s the next grand challenge in AI cognition. Scaling compute barely closes the gap. Humans use resets and no-ops to test hypotheses. Models don’t. They just spam clicks.

The core event here seems to be that there was a period of learning opportunity without reward signals, during which humans reset 12% of the time and models reset less than 2% of the time. Humans had a decent learning algorithm and designed useful experiments during exploration, models didn’t. So yeah, that’s a weakness of current models. They’re not good at relatively open-ended exploration and experimentation, at least not without good prompting and direction. They’re also not strong on adapting to weirdness, since they (wisely, statistically speaking) rely on pattern matching, while lacking good instincts on when to ‘snap out of’ those matches.

### Choose Your Fighter

OpenAI is launching a browser and short duration video social network to try and capture consumers, monetizing them via shopping hookups and adding erotica. What is OpenAI’s plan?

1. Fund ASI by offering normal big tech company things to justify equity raises.
1. ?????????. Build superintelligence in a way that everyone doesn’t die, somehow.
1. Everyone dies. Profit, hopefully.
> Near

I believe Aidan on the proximate causes inside OpenAI pushing towards these decisions. They still wouldn’t have happened if the conditions hadn’t been set, if the culture hadn’t been set up to welcome them. Certainly there’s more money in automating all labor if you can actually automate all labor, but right now OpenAI cannot do this. Anything that raises valuations and captures market share and mindshare thus helps OpenAI progress towards both profitability and eventually building superintelligence and everyone probably dying. Which they pitch to us as the automation of all labor (and yes, they mean all labor). Anthropic, on the other hand, is catering to business and upgrading financial services offerings and developing a browser extension for Chrome. Two ships, ultimately going to the same place (superintelligence), pass in the night.

> Stefan Schubert: Anthropic has overtaken OpenAI in enterprise large language model API market share.

Grok can be useful in one of two ways. One is more competitive than the other.

> Alexander Doria

xAI has chosen to de facto kick the other AIs off of Twitter, which is a hostile move that trades off the good of the world and its knowledge and also the interests of Twitter in order to force people to use Grok. Then Grok doesn’t do a good job parsing Twitter. Whoops. Please fix. The other way to make Grok useful is to make a superior model. That’s harder. Claude.ai has an amazing core product, but still needs someone to put in the (relatively and remarkably small, you’d think?) amount of work to mimic various small features and improve the UI. They could have a very strong consumer product if they put a small percentage of their minds to it. Another example:

> Olivia Moore: With the introduction of Skills, it’s especially odd that Claude doesn’t have the ability to “time trigger” tasks. I built the same workflow out on ChatGPT and Claude. Claude did a much better job, but since you can’t set it to recur I’m going to have to run it on ChatGPT…

The obvious response is ‘have Claude Code code something up’ but a lot of people don’t want to do that and a lot of tasks don’t justify it.

### Get My Agent On The Line

Tyler Cowen asks ‘will there be a Coasean singularity?’ in reference to a new paper by Peyman Shahidi, Gili Rusak, Benjamin S. Manning, Andrey Fradkin & John J. Horton. AIs and AI agents promise to radically reduce various transaction costs for electronic markets, enabling new richer and more efficient market designs. My classic question to ask in such situations: If this were the one and only impact of AI, that it radically reduces transaction costs especially in bespoke interactions with unique features, enabling far better market matching at much lower prices, then what does that effect alone do to GDP and GDP growth? I asked Claude to estimate this based on the paper plus comparisons to historical examples. Claude came back with wide uncertainty, with a baseline scenario of a one-time 12-18% boost over 15-25 years from this effect alone. That seems on the low side to me, but plausible.

### Deepfaketown and Botpocalypse Soon

Theo Jaffee and Jeffrey Ladish think the Grok effect on Twitter has been good, actually? This has not been my experience, but in places where epistemics have gone sufficiently downhill perhaps it becomes a worthwhile tradeoff. Grok now has a third companion, a 24-year-old spirited woman named Mika, the link goes to her system prompt. The good news is that she seems like a less unhealthy persona to be chatting to than Ani, thus clearing the lowest of bars. The bad news is this seems like an epic display of terrible prompt engineering of an intended second Manic Pixie Dream Girl, and by being less flagrantly obviously awful this one might actually be worse. Please avoid. Steven Adler, former head of product safety at OpenAI, warns us in the New York Times not to trust OpenAI’s claims about ‘erotica.’ I agree with him that we don’t have reason to trust OpenAI to handle this (or anything else) responsibly, and that publishing changes in prevalence rates of various mental health and other issues over time and committing to what information it releases would build trust in this area, and be important info to learn.

### Fun With Media Generation

AI-generated music is getting remarkably good. A new study finds that songs from a mix of Suno versions (mostly in the v3 to v4 era, probably, but they don’t say exactly?) was ‘indistinguishable from human music,’ meaning when asked to identify the human song between a Suno song and a random human song, listeners were only 50/50 in general, although they were 60/40 if both were the same genre. We’re on Suno v5 now and reports are it’s considerably better. One commentor shares this AI song they made, another shares this one. If you want generic music that ‘counts as music’ and requires attention to differentiate for the average person? We’re basically there.

> Nickita Khylkouski

There is a big gap between generic average human music and the median consumed musical recording, and also a big gap between the experience of a generic recording versus hearing that performed live, or integrating the music with its context and story and creator, AI music will have much lower variance, and each of us curates the music we want the most. An infinite number of monkeys will eventually write Shakespeare, but you will never be able to find and identify that manuscript, especially if you haven’t already read it. That’s a lot of ‘horse has the wrong accent’ as opposed to noticing the horse can talk. The questions are, essentially, at this point:

1. Will be a sameness and genericness to the AI music the way there often is with AI text outputs?
1. How much will we care about the ‘humanness’ of music, and that it was originally created by a human?
1. To what extent will this be more like another instrument people play?
It’s not an area I’ve put much focus on. My guess is that musicians have relatively less to worry about versus many others, and this is one of the places where the AI needs to not only match us but be ten times better, or a hundred times better. We shall see.

> Rob Wiblin

Ethan Mollick notes that it is faster to create a Suno song than to listen to it. This means you could be generating all the songs in real time as you listen, but even if it was free, would you want to do that? What determines whether you get slop versus art? Here is one proposal.

> Chris Barber:

As a predictive method, this seems right. If you intend slop, you get slop. If you intend art, and use AI as a tool, you get art similarly to how humans otherwise get art, keeping in mind Sturgeon’s Law that even most human attempts to create art end up creating slop anyway, even without AI involved.

### Copyright Confrontation

Reddit created a ‘test post’ that could only be crawled by Google’s search engine. Within hours Perplexity search results had surfaced the content of the post.

### They Took Our Jobs

Seb Krier pushed back strongly against the substance from last week, including going so far as to vibecode an interactive app to illustrate the importance of comparative advantage, which he claims I haven’t properly considered. It was also pointed out that I could have worded my coverage better, which was due to my frustration with having to repeatedly answer various slightly different forms of this argument. I stand by the substance of my claims but I apologize for the tone. I’ve encountered variants of the ‘you must not have considered comparative advantage’ argument many times, usually as if it was obvious that everything would always be fine once you understood this. I assure everyone I have indeed considered it, I understand why it is true for most historical or present instances of trade and competition, and that I am not making an elementary or first-order error here.


