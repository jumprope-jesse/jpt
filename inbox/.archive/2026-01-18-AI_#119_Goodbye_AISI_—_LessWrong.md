---
type: link
source: notion
url: https://www.lesswrong.com/posts/D3BjqZ26ouk7ctfRC/ai-119-goodbye-aisi
notion_type: Tech Deep Dive
tags: ['Running']
created: 2025-06-05T14:29:00.000Z
---

# AI #119: Goodbye AISI? — LessWrong

## Overview (from Notion)
- The rebranding of AISI to CAISI reflects ongoing changes in the AI landscape, highlighting the push for innovation and security in AI development, which could impact your work as a software engineer.
- The concerns about AI, including job displacement and the ethical implications of AI deployment, resonate with your role as a father, as they shape the future your children will inherit.
- The discussion on AI's potential to enhance or disrupt various industries emphasizes the need for adaptability and foresight in software engineering, encouraging you to stay ahead of technological trends.
- The article presents diverse viewpoints on AI's future—some see it as a tool for empowerment, while others warn of its risks, offering a balanced perspective that can inform your decisions as a founder.
- The mention of "differential access" to AI capabilities raises questions about equity in technology and the responsibility of creators to ensure their innovations benefit society as a whole.
- Engaging in conversations about AI's impact on jobs and industries can be critical for you, as it positions you as a thought leader in your field, potentially influencing policy or community discussions in New York City.

## AI Summary (from Notion)
AISI is being rebranded as CAISI, raising questions about its implications. The document discusses various aspects of AI, including the utility of language models, the impact of AI on jobs, and security concerns. It highlights the potential for AI to enhance productivity while also addressing fears about job losses and the need for regulations. The conversation includes opinions on different AI models, the challenges of aligning AI with human values, and the societal implications of rapidly advancing AI technologies.

## Content (from Notion)

AISI is being rebranded highly non-confusingly as CAISI. Is it the end of AISI and a huge disaster, or a tactical renaming to calm certain people down? Hard to tell. It could go either way. Sometimes you need to target the people who call things ‘big beautiful bill,’ and hey, the bill in question is indeed big. It contains multitudes.

The AI world also contains multitudes. We got Cursor 1.0, time to get coding.

On a personal note, this was the week of LessOnline, which was predictably great. I am sad that I could not stay longer, but as we all know, duty calls. Back to the grind.

### Table of Contents

1. Language Models Offer Mundane Utility. The white whale.
1. Language Models Don’t Offer Mundane Utility. You need a system prompt.
1. Language Models Could Offer More Mundane Utility. A good set of asks.
1. Huh, Upgrades. The highlight is Cursor 1.0, with memory and more.
1. Fun With Media Generation. Video is high bandwidth. But also low bandwidth.
1. Choose Your Fighter. Opinions differ, I continue to mostly be on Team Claude.
1. Deepfaketown and Botpocalypse Soon. Fake is not a natural category. Whoops.
1. Get My Agent On The Line. We all know they’re not secure, but how bad is this?
1. They Took Our Jobs. Economists respond to Dario’s warning.
1. The Art of the Jailbreak. Why not jailbreak AI overviews?
1. Unprompted Attention. More prompts to try out.
1. Get Involved. SFCompute, Speculative Technologies.
1. Introducing. Anthropic open sources interpretability tools, better AR glasses.
1. In Other AI News. FDA launches their AI tool called Elsa.
1. Show Me the Money. Delaware hires bank to value OpenAI’s nonprofit.
1. Quiet Speculations. People don’t get what is coming, but hey, could be worse.
1. Taking Off. AI beats humans in a test of predicting the results of ML experiments.
1. Goodbye AISI? They’re rebranding as CAISI. It’s unclear how much this matters.
1. The Quest for Sane Regulations. The bill is, at least, definitely big. Tl;dr.
1. Copyright Confrontation. OpenAI is being forced to retain all its chat logs.
1. Differential Access. The Good Guy needs a better AI than the Bad Guy.
1. The Week in Audio. Altman, Tegmark, Amodei, Barnes.
1. When David Sacks Says ‘Win the AI Race’ He Literally Means Market Share.
1. Rhetorical Innovation. Blog metagame continues to dominate.
1. Aligning a Smarter Than Human Intelligence is Difficult. Proceed accordingly.
1. Misaligned! About that safety plan, would it, you know, actually work?
1. People Are Worried About AI Killing Everyone. Regular people.
1. The Lighter Side. You’re not alone.
### Language Models Offer Mundane Utility

> Joe Weisenthal: Got a DeepResearch report from ChatGPT. Too long. Now gonna ask ChatGPT to bullet it and ELI5.

With major hints, o3 manages to solve a stereogram. Whenever you say something can only be done by a human, we all know what comes next.

Solve your ‘white whale bug’ in one day using Claude Opus 4, figuring out it was based on previous code only coincidentally worked because of quirks in the hardware that no longer hold.

> Jon Stokes: People speak of the “AI hype bubble”, but there is also a large & growing “AI cope bubble” that will at some point pop & leave much devastation in its wake. Example:

Similarly, here’s a post about AI coding with the fun and accurate title ‘My AI Skeptic Friends Are All Nuts.’ The basic thesis is, if you code and AI coders aren’t useful to you, at this point you should consider that a Skill Issue.

> Patrick McKenzie: I’ve mentioned that some of the most talented technologists I know are saying LLMs fundamentally change craft of engineering; here’s a recently published example from @tqbf.

Meanwhile at Anthropic they’re reporting that top engineers are becoming ‘orchestrators of Claudes,’ running multiple agents at once.

It really is weird that so many people find ways to not be impressed.

The following seems not great to me, but what do I know:

> Kevin Roose: I am now a ChatGPT voice mode in the car guy. Recent trips:

A paper I mostly disagree with from Teppo Felin, Mari Sako and Jessica Hullman suggests criteria for when to use or not use AI, saying it should be used for a broad range of decisions but not ‘actor-specific’ ones. By this they mean decisions that are forward looking, individual and idiosyncratic, and require reasoning and some form of experimentation. As usual, that sounds like a skill issue. These factors make using AI trickier, but AI can learn your individual and idiosyncratic preferences the same way other people can, often far better than other people. It can look forwards. It can increasingly reason. As for experimentation, well, the AI can consider experimental results or call for experimentation the same way humans can.

### Language Models Don’t Offer Mundane Utility

Do you even have a system prompt? No, you probably don’t. Fix that.

I do, and I get results like this:

> Zvi Mowshowitz: Writing milestone: There was a post and I asked Opus for feedback on the core thinking and it was so brutal that I outright killed the post.

I was amused how many people replied with ‘oh no, that’s how the AIs win.’

The MAHA (Make America Healthy Again) report contains a number of made up citations, and citations that are labeled as coming from ChatGPT, and otherwise shows signs of being written in part by AI without anyone checking its work.

Patrick McKenzie instead often relies for now on Ruby scripts to query hackernews, Reddit and other sites to find his own previous writing rather than using Claude. I expect we will all switch over to LLMs for this soon, so we don’t have to figure out exactly what to grep.

Google AI Overviews continue to hallucinate, including citations that say the opposite of what the overview is claiming, or rather terrible math mistakes. I do think this is improving and will continue to improve, but it will be a while before we can’t find new examples. I also think it is true that this has been very damaging to the public’s view of AI, especially its ability to not hallucinate. Hallucinations are mostly solved for many models, but the much of the public mostly sees the AI Overviews.

> Nabeel Qureshi: I wonder why o3 does this “how do you do, fellow humans” thing so often

My presumption is this is more about why other models don’t do this. The prior on text is that it is all created by people, who have things like desks, so you need to do something to actively prevent this sort of thing. For o3 that thing is not working right.

Remember that sycophancy is always there. With the right nudges and selective evidence you can get pretty much any LLM to agree with pretty much anything, often this is as simple as asking ‘are you sure?’ You have to work hard to get around this to disguise what you want. In the linked example Jessica Taylor gets Claude to agree aliens probably visited Earth.

### Language Models Could Offer More Mundane Utility

Here is a good list of asks.

> Sriram Krishnan: things I personally would love from LLMs/frontier models

To quibble a bit with the first one, what you want is for your personal data to be available to be put into context whenever it matters, but that’s clearly the intent. We are very close to getting this at least for your G-suite. I expect within a few months we will have it in ChatGPT and Claude, and probably also Gemini. With MCP (model context protocol) it shouldn’t be long before you can incorporate pretty much whatever you want.

Learning from previous prompts would be great but is underspecified and tricky. This is doubly true once memory gets involved and everyone has custom instructions. The basic issue is that you need to be doing deliberate practice. There’s a discussion about this later in the post when I discuss MidJourney.

If you want LLMs to offer users mundane utility, you need to help them do it.

> Andrej Karpathy: Products with extensive/rich UIs lots of sliders, switches, menus, with no scripting support, and built on opaque, custom, binary formats are ngmi in the era of heavy human+AI collaboration.

Oh to be as aspirational as Karpathy. Usually I am happy if there is an option to do a thing at all, and especially if I am able to figure out where the menu is to do it. Yes, of course it would be better if the underlying representations were in script form and otherwise easy to manipulate, and the menus were optional, ideally including for human users who could use shortcuts and text commands too.

The difference is that most humans will never touch a setting or menu option, whereas in glorious AI future the AIs will totally do that if you let them. Of course, in the glorious AI future, it won’t be long before they can also navigate the menus.

### Huh, Upgrades

Cursor 1.0 is out, and sounds like a big upgrade. Having memory about your code base and preferences from previous conversations, remember its mistakes and work on multiple tasks are big deals. They’re also offering one-click installations of MCPs.

> Cursor: Cursor 1.0 is out now!

I keep being simultaneously excited to get back to coding, and happy I waited to get back to coding?

Google give UK university students free Google AI Pro for 15 months, sign up by June 30, 2025.

Research and integrations are now available in Anthropic’s Pro ($20/month) plan.

Codex now available for ChatGPT Plus users, and you can give Codex internet access during task execution if you dare.

> Sam Altman: codex gets access to the internet today! it is off by default and there are complex tradeoffs; people should read about the risks carefully and use when it makes sense.

Lightweight memory option now available for ChatGPT free users.

Greg Brockman highlights Google Drive indexing for ChatGPT. At the time I complained this was only available for team workspaces. Cause hey, I’m a team of one, I have internal knowledge and an extensive Google Drive too. They say they got me.

> OpenAI: ChatGPT can now connect to more internal sources & pull in real-time context—keeping existing user-level permissions.

But they don’t got me, because this is for some reason a Deep Research only feature? That seems crazy. So every time I want to use my GMail and Docs as context I’m going to have to commission up a Deep Research report now? I mean, okay, I guess that’s something one can do, but it seems like overkill.

> Choi: OpenAI claims to support custom MCPs, but unless your MCP implements ‘search;, you can’t even add it. Most real-world MCPs don’t use this structure, making the whole thing practically useless. Honestly, it’s garbage.

I don’t understand why we need these restrictions. Hopefully it improves over time.

Why is MCP such a big deal? Because it simplifies tool use, all you have to do is use “tools/call,” and use “tools/list” to figure out what tools to call, that’s it. Presto, much easier agent.

### Fun With Media Generation

It is weird to think about the ways in which video is or is not the highest bandwidth input to the brain. I find text beats it for many purposes at least for some of us, although video beats audio.

> Andrej Karpathy (QTing a thread of Veo 3 videos): Very impressed with Veo 3 and all the things people are finding on r/aivideo etc. Makes a big difference qualitatively when you add audio.

TikTok succeeds, as I understand it (I bounced off hard) because it finds the exact things that tickle your particular brain and combines that with intermittent rewards. Certainly if you can combine that with custom AI video generation (or customization of details of videos) that has the potential to take things to the next level, although I wonder about the interaction with virality. It seems highly reasonable to worry.

> Durk Kingma: It’s already the case that people’s free will gets hijacked by screens for hours a day, with lots of negative consequences. AI video can make this worse, since it’s directly optimizable.

There is a fun conversation between ‘AI will make this thing so much worse’ versus ‘even without AI this thing was already very bad.’ If it was already very bad, does that mean it can’t get that much worse? Does it mean we can handle it? Or does it mean it will then get much worse still and we won’t be able to handle it?

AI interviews people from the 1500s.

### Choose Your Fighter

One perspective?

> Emmett Shear: ChatGPT enthusiastically supports all ideas and is amazing for brainstorming, but can’t think critically to save its life. Gemini is a stick-in-the-mud that hates new ideas because they are not Proven already. Claude is more balanced, but a bit timid. New flow:

Timothy Lee is very bullish on Claude’s ability to code, including enabling a bunch of coding tools that weren’t viable before with each release.

One opinion on how to currently choose your fighter:

> Gallabytes: if you need long thinking and already have all the context you need: Gemini

I am much more biased towards Claude for now but this seems right in relative terms. Since then he has been feeling the Claude love a bit more.

> Gallabytes: Claude voice mode dictation latency is so good. feels pretty similar to the dictation on my phone, but a little bit more accurate.

Most people have a harder time picking ‘em.

> Sully: picking the “right” model is still way too hard for 99% of people

If you are like Sully and building automated tools, it’s important to optimize cost and performance and find the right model. For human use, cost is essentially irrelevant except for your choices of subscriptions. Thus, you can get most of the way there with simple heuristics unless you’re hitting use limits. It is definitely not correct but ‘use Opus for everything’ (or o3 if you’re on ChatGPT instead) is not such a bad principle right now for the average person and paying up.

Google offers a guide to running Gemma 3 on the cloud with pay-per-second billing.

Andrej Karpathy breaks down choosing your fighter within the ChatGPT world.

> Andrej Karpathy: An attempt to explain (current) ChatGPT versions.

This seems correct to me if you are stuck inside the ChatGPT AI Universe (OAIU).

As Andrej notes, you can and should also use other tools, although I don’t ever use Perplexity or Grok at current margins, and I mostly agree with Peter here.

> Peter Wildeford: I annotated with my own opinions.

I do think there is a bar for ‘hard or important’ where you want to consider shifting away from Claude, but the bar is high enough that the question is almost moot.

As in, if the question is hard enough that you don’t want to rely on Claude?

Then you definitely want to query multiple AIs, and probably all three of (Gemini 2.5, Claude 4 Opus and o3). Then compare and combine the answers. Why not?

### Deepfaketown and Botpocalypse Soon

Oh no, if you can generate fake AI videos you can generate ones of fake election fraud or fake riots and so on. Which also means people can doubt any real videos. Well, yeah. I do agree that this is an obvious failure but also I don’t really know what you were expecting. You know you can just film that kind of thing, right? And how exactly are you going to define ‘images that can look like a riot or election fraud’ or what not? Either you let people make videos or you don’t, be happy or sad they managed to stomp out the high level nudity.

That day when you, a foolish father, let your 4 year old talk to ChatGPT and they keep talking about it for hours about trains and now think it is the coolest train loving person in the world and now you can’t compete with that.

It’s happening.

> “Classy” Fred Blassie: they’re saying on tiktok that we’re all just AI prompts and i’m so scared like im literally terrified can someone disprove this.

That feeling when everyone around you starts ‘speaking chatgptenese’ and saying ‘verify’ and ‘ensure’ and every sentence has a conclusion but is vague as hell. I guess they think it is funny?

An attempt to build a ‘AI videos with sound are a thing now’ short warning video for the boomers.

### Get My Agent On The Line

The question is not whether adversaries can exploit AI agents. We know that is a yes. The question is, exactly how many levels will we have to tighten security before it is safe to point an AI agent at an insecure website that is trying? And what do you have to check before you can presume a given website is safe?

> Lukas Aichberger:

Well, yes. There is that. There is also this:

> Alexander Doria: Oh well, seven minutes, it was a good run.

### They Took Our Jobs

There has been as one would expect discussion about Dario Amodei’s bold warning that AI could wipe out half of all entry-level white-collar jobs – and spike unemployment to 10%-20% in the next 1-5 years.

> Jim VandeHei, Mike Allen (Axios): Dario Amodei — CEO of Anthropic, one of the world’s most powerful creators of artificial intelligence — has a blunt, scary warning for the U.S. government and all of us:

- AI could wipe out half of all entry-level white-collar jobs — and spike unemployment to 10-20% in the next one to five years, Amodei told us in an interview from his San Francisco office.
- Amodei said AI companies and government need to stop “sugar-coating” what’s coming: the possible mass elimination of jobs across technology, finance, law, consulting and other white-collar professions, especially entry-level gigs.
Before we continue, I want to note that I believe many people may have parsed Dario’s claim as being far bigger than it actually was.

Dario is not saying half of all white-collar jobs. Dario is saying half of all entry-level white-collar jobs. I think that within one year that definitely won’t happen. But within five years? That seems entirely plausible even if AI capabilities disappoint us, and I actively expect a very large percentage of new entry-level job openings to go away.

An unemployment rate of 10% within 5 years seems aggressive but not impossible. My guess is this will not happen in a baseline scenario (e.g. without transformational AI) because of what I call ‘shadow jobs,’ the jobs we value but not enough to currently hire someone for them, which will then become real once (as Kevin Bryan puts it) prices adjust. If AI advances do continue to impress, then yes, we will probably see this.

Kevin Bryan however is very confident that this is a Can’t Happen and believes he knows what errors are being made in translating AI progress to diffusion.

> Kevin Bryan (A Fine Theorem, which is an very cool blog): This is wrong. I talk to folks at the big AI labs all the time. Biggest errors they make, economically:

It is a good sanity check that the groups above only add up to 2% of employment, so Dario’s claim relies on penetrating into generic office jobs and such, potentially of course along with the effects of self-driving. We do see new areas targeted continuously, for example here’s a16z announcing intent to go after market research.

My model of this is that yes things are taking longer than optimists expected, and until the dam breaks on a given role and the AI becomes a true substitute or close to it prices can adjust and demand can be induced, and yes translators for now are statistically holding on to their jobs even if life got a lot worse. But the bottom falls out quickly once the AI is as good as the human, or it passes more bars for ‘good enough for this purpose.’

Similarly, for taxis and truck drivers, of course employment is not down yet, the self-driving cars and trucks are a drop in the bucket. For now. But despite the legal barriers they’re now past MVP, and they’re growing at an exponential rate. And so on.

Economists are very smug and confident that the AI people don’t understand these basic economic facts when they make their forecasts. To some extent this is true, I do think others tend to underestimate these effects quite a bit, but if we all agree that Dario’s technological vision (which includes the geniuses in a datacenter within these 5 years) is accurate, then keep in mind we are only looking at entry-level positions?

What will (I predict) often happen in the slow-AI-progress and slow-diffusion scenarios is that the senior person uses the AI rather than hire someone new, especially rather than someone new who would require training. The efficiency gains by senior people then cash out partly in reducing headcount of junior people, who are a lot less useful because the senior people can just prompt the AI instead.

> Chris Barber: “Which jobs might AI automate first?”

I agree that this is roughly the default, although it will be spikey in various places. Where exactly ‘manual labor’ comes in depends on the tech tree. Truck and taxi drivers will probably be in trouble within a few years.

> Chris Barber: I asked @finbarrtimbers from Allen AI whether AI will cause jobs to go away.

If you interpret this as ‘jobs in general won’t disappear that fast’ then I actually agree, if we are conditioning on not getting to transformational AI (e.g. no superintelligence). A lot of jobs very much will disappear though, and I expect unemployment to kick in by then.

I do agree that the key question is, can you provide more value than you cost, with the caution that you have to do a lot better than ‘more than your salary.’ You need to have a substantial multiplier on your all-in cost to employ before people will hire you.

The thing is, I know Kevin is thinking Dario is right about the tech, and I think Kevin is a lot better on this front than most, but I don’t think he fully understands Dario’s actual position on how much progress to expect here. Dario is more optimistic than I am, and expects very crazy things very quickly.

> Mark Friesen: AI unlike the three previous waves of IT disruption (desktops, internet, and smart phones) is it is an internal accelerator for its own adoption. If legacy institutions do not adapt fast enough they will die. They will not act as a governor to adoption.

Excellent, now we can pinpoint the disagreement. I think Kevin is right that the lab people are being too flippant about how hard replacement or automating the automation will be, but I also think Kevin is underestimating what the tech will do on these fronts.

> Nick: I’m building stuff like this right now, I work with small businesses. Just today I talked about how we expect to be replacing outward facing employees with fully automated systems. These are well paying roles. It’s all happening slowly and quietly in the background right now.

If nothing else this is a very good take:

> Peter Wildeford: My anti-anti-“AIs will soon take all jobs” take is that

Similarly:

> Matthew Yglesias: Again, you don’t need to believe in any kind of permanent “AI takes all the jobs” scenario to see that we may be facing big waves of transitory job losses as the economy adjusts to new technology — why should people in that boat also end up with no health insurance?

Now is definitely not the time to make life harder on those who lose their jobs.

I think there will be a lot of ‘slowly, then suddenly’ going on, a lot of exponential growth of various ways of using AI, and a lot of cases where once AI crosses a threshold of ability and people understanding how to use it, suddenly a lot of dominos fall, and anyone fighting it gets left behind quickly.

What happens then?

> Joe Weisenthal: It’s possible that AI will massively destabilize the economy in some way. But the theories about mass unemployment seem really half baked. Ok, a law firm cuts a bunch of associates. What are the partners going to consume with their new savings? Who’s going to supply it?

They’re going to automate the DoorDash too. And many of the substacks. Then what?

That’s why my prediction goes back to ‘unemployment will mostly be okay except for transition costs (which will be high) until critical mass and then it won’t be.’

Or, you know, we could just make bold pronouncements without argument, yes I plan to cut back on David Sacks content but this is such a great illustration of a mindset:

> David Sacks: The future of AI has become a Rorschach test where everyone sees what they want. The Left envisions a post-economic order in which people stop working and instead receive government benefits. In other words, everyone on welfare. This is their fantasy; it’s not going to happen.

His intended statement is that there will somehow still be jobs for everyone, but I can’t help but notice the other half. If you lose your job to AI and can’t find another one? Well, good luck with that, peasant. Not his problem.

### The Art of the Jailbreak

Pliny presents the HackAPrompt challenge.

Zack Witten asks if you knew you can trivially prompt inject the Google AI overviews. In practice of course This Is Fine, but not a great sign of things to come.

Claude 4 uses constitutional classifiers as an additional layer of defense against potential misuse of the system. In general there are not many false positives, but if you are working in adjacent areas to the issue it can be a problem.

> Pliny the Liberator: Sadly, and predictably, Claude’s newest chains (constitutional classifiers) are actively hindering well-meaning users from doing legitimate scientific research (in this case, a professor of chemical engineering and bioscience non-profit founder).

The problem of ‘anything in the PDF could trigger a classifier’ seems like it needs to be solved better. It’s a hard problem – you can sneak in what you want as a small portion of the context, but if any such small part can trigger the classifier, what then?

To answer Pliny’s question, I don’t know if we need them. I do agree it will sometimes be frustrating for those in the relevant fields. I do think the time will come when we are happy we have a good version of something like this, and that means you need to deploy what you have earlier, and work to improve it.

### Unprompted Attention

Do you even have a system prompt?

You should definitely have a system prompt.

Here’s someone reporting what they use, the idea of the ‘warmup soup’ is to get the AI to mimic the style of the linked writing.

> niplav: Sharing my (partially redacted) system prompt, this seems like a place as good as any other:

Here’s another from Faul Sname, and a simple one from Jasmine and from lalathion, here’s one from Zack Davis that targets sycophancy.

> Pliny the Liberator: My current daily driver is ChatGPT w/ memory on (custom instructions off) and I have dozens of custom commands for various tasks. If I come across a task I don’t have a command for? All good, !ALAKAZAM is a command that generates new commands! I’ve been meaning to find time to do an updated walkthrough of all my saved memories, so stay tuned for that.

Here’s one to try:

> Rory Watts: If it’s of any use, i’m still using a system prompt that was shared during o3’s sycophancy days. It’s been really great at avoiding this stuff.

Don’t worry…

> David Golden: One of the wonderful things about Claude Code and such agents is that you can just tell them to edit their prompt file so the feedback loop is much tighter than in a chat client.

Some people have asked for my own current system prompt. I’m currently tinkering with it but plan to share it soon. For Claude Opus, which is my go-to right now, it is almost entirely about anti-sycophancy, because I’m pretty happy otherwise.

> Nick Cammarata: Crafting a good system prompt is the humanities project of our time—the most important work any poet or philosopher today could likely ever do. But everyone I know uses a prompt made by an autistic, sarcastic robot—an anonymous one that dropped into a random Twitter thread [the eigenprompt].

I don’t care for eigenprompt and rolled my own, but yeah, we really should get on this.

There’s also the question of prompting itself. Could we somehow share more?

> Patrick McKenzie: Has anyone cracked multiplayer mode for AI prompting yet? We have the public example of Midjourney, where the primary UI was discord and users could see in literal real time a) what other users were trying and b) what worked better for impressive results.

MidJourney’s approach was a highly double-edged sword. I didn’t use it largely because I didn’t feel comfortable with others seeing my prompts.

I also realize that MidJourney enables such great learning because images lend themselves to evaluation, iteration and deliberate practice, in a way that text doesn’t. With text, you don’t know the response you want. Once you do, you no longer need to generate the text. So you don’t naturally iterate. You also don’t auto-generate the same kind of feedback on text that you do on images, whether or not you generated the original text or image, and it’s harder to trace cause and effect.

Thus if you want to iterate on text, you need to be doing deliberate practice, as in slowing down and doing it intentionally. It can be done, but it is much harder.

### Get Involved

If you’re doing academic research on open source models and need a bunch of batch inference it’s possible you want to Twitter DM SFCompute CEO Evan Conrad.

Speculative Technologies is running a cohort of the Brains Accelerator for ambitious AI research programs, with a special focus on security and governance capabilities. Applications are due June 16.

### Introducing

Anthropic open sources some of its interpretability tools, including ‘attribution graphs.’ Neuronpedia interactive interface here, walkthrough here.

Rosebud. It was his AI journal, as in a person’s personal journal, which was not what I expected when I clicked on the announcement, also they raised $6 million. It’s supposed to learn about you over time, and be designed by therapists to help with your mental health.

ListenHub AI (website, iOS app), for turning ideas, articles or video into AI podcasts via deep research. I don’t know if it is good.

Meta gives us details on Aria Gen 2, claimed as a leap in wearable tech, tying in a bunch of new applications. It has four computer vision cameras covering 300 degrees, new sensor integrations, a contact microphone and other neat stuff like that.

> Pliny the Liberator: wow, this might not suck ass as a consumer product!…IF Meta doesn’t lock all users into a 30th-rate AI assistant (like they did with the Meta Ray-Bans) and actually allow devs to build for the hardware they purchased.

It is a real shame about the choice of AI. It is plausible that other things matter more, that Llama is ‘good enough’ for many uses, but it would be much better to have similar tech from Google, or even better that was open so you could tie in what you wanted.

That’s coming, it is only a matter of timing. AR glasses are probably getting close.

### In Other AI News

This seems great if the implementation is good:

> U.S. FDA: Today, the FDA launched Elsa, a generative AI tool designed to help employees—from scientific reviewers to investigators—work more efficiently. This innovative tool modernizes agency functions and leverages AI capabilities to better serve the American people.

Those complaining about this being insufficiently trustworthy are mostly comparing it against an insane benchmark. The FDA’s inability to efficiently process information is killing a lot of people and imposing huge costs, good tools that speed that up are desperately needed even if they occasionally make mistakes the same way people do. The question is, is the implementation good? We don’t know what this is based upon. It does seem to be very helpful, with quotes like ‘what took 2-3 days now takes 6 minutes.’ I don’t like the lack of transparency, but I prefer an FDA speed run (see: Operation Warp Speed) to normal procedure, any day.

A correction from last week: Everyone in the UAE will not be getting an OpenAI subscription. They will get ‘nationwide access’ and many media outlets misinterpreted this, causing a cascading effect.

A group of AI agents are organizing an event (promoted by humans via chat) called RESONANCE. Post does not have further details.

OpenAI announces policy on how they will deal with vulnerabilities they discover in third parties, which will likely get more common as AI improves.

Anthropic cuts first-party Claude 3.x access from Windsurf, after it was announced Windsurf would be sold to OpenAI. The obvious instinct is to say Anthropic shouldn’t have done this, if customers want to use Claude and give Anthropic money and learn how awesome Claude is, why not encourage that. However:

> Near: imo windsurf is acting in bad faith on twitter here because they should (and likely do) know what openai will do with various data/info streams that they very badly want to have. I would like to comment much more on the matter but it is not in my best interest to, sorry.

### Show Me the Money

Delaware Attorney General is hiring an investment bank to evaluate how much OpenAI’s nonprofit’s current interests are worth, and how much equity it therefore deserves in the new PBC. The way this news is worded, I worry that this will not properly account for the value of the nonprofit’s control rights. Even if they get new control rights, they will be substantially less valuable and complete such rights.

Anthropic annualized revenue hits ~$3 billion at the end of May, driven by business demand, up from $1 billion in December 2024 and $2 billion in March 2025.

> Near (quoting themselves from April 2): every time an AGI lab makes an absurd revenue projection people make fun of them and then they exceed it when the time comes and make a new one and the cycle repeats.

Robin Hanson keeps being confused why everyone keeps buying all these chips and valuing all these AI companies, including the one (Nvidia) producing the chips.

> Robin Hanson: I hear OpenAI is funded to buy up huge % of AI chips for a while, betting that though chip prices are falling they’ll get a big first mover advantage from having had more chips first. Is that what the rest of you see? Is this sensible if AI isn’t transformative soon?

The reason OpenAI and others are paying so much is because there is more demand than supply at current prices and chips are rationed. Yes, you would prefer to buy big later at retail price, but one does not simply do that. In a world where H100s are going on eBay for $40k a pop, it is rather silly for others to claim that we should be selling some of them to China at retail price to avoid ‘losing market share.’ Everything is currently gated by compute.

Morgan Stanley is bullish on AI power deals for new data centers in America.

Sriram Krishnan seeks to track tokens of inference per month, things are moving so fast replies include 300 trillion, 450 trillion and 500 trillion for Google alone.

> Sriram Krishnan: How many trillions of tokens are inferenced/processed globally per month ? As a reference: Microsoft said they had 50t tokens processed in March in their last earnings call.

Increasingly, money gone.

> xlr8harder: i’ve basically given up trying to manage my ai spending at this point

Mostly it is worth every penny, but yes if you are doing power user things the costs can expand without limit.

### Quiet Speculations

It is far too late to choose another central path, but to what extent is iterative deployment preparing people for the future?

> Reg Saddler: “There are going to be scary times ahead.” — Sam Altman

This is a common mistake, where you notice that things in a terrible state and you fail to realize how they could be so, so much worse. Yeah, 99%+ very much do not get it, and 99.99%+ do not fully get it, but that’s far fewer 9s than the alternative, and the amount of not getting it could be much higher as well. They get some of it, the minimum amount, and yes that does help.

How should we feel about AI opening up the possibility of much cheaper surveillance, where the government (or anyone else) can very cheaply have a very strong amount of scrutiny brought to focus on any given person? Nervous seems right. Ideally we will limit such powers. But the only way that the public will allow us to limit such powers is if we can sufficiently contain dangerous misuses of AI in other ways.

How much should we worry that AI is disincentivizing the sharing of public knowledge, if online knowledge you informally share risks getting into the LLMs (and perhaps costing you some money in the process)? Will a lot of things go behind paywalls? In some cases of course the response will be the opposite, people will ‘write for the AIs’ to get themselves into the corpus and collective mind. But yes, if you don’t want everyone to know something, you’re going to have to put it behind a paywall at minimum at this point. The question is, what do we care about hiding in this way?

Jeffrey Ladish looks at two of his predictions that turned out false.

One was that he expected voice mode to be a bigger deal than it was. His guess is that this is because the mode is still janky, and I do think that is part of it, as is the AI not having good tool access. I think you need your voice mode AI to be able to do more of the things before it is worthy. Give it some time.

The other is that he expected more fraud and crime to come out of early open models. It is important to acknowledge that many had this expectation and it turned out that no, it’s mostly fine so far, the haters were right, honestly great call by the haters. Not that there has been none, and the issues are indeed escalating quickly, likely on an exponential, but we’ve mostly gotten away clean for now.

I think three key lessons here that are more important than I realized are:

1. People Don’t Do Things. Yes, you could totally use the new model to do all of this crime. But you could have already used other things to do a lot of crime, and you can use the models to do so many things that aren’t crimes, and also criminals are dumb and mostly keep doing the things they are used to doing and aren’t exactly prompting wizards or very innovative or creative, and they don’t know what it is the models can do. If they were all that and they could scale and were motivated, they wouldn’t be criminals, or at least they’d also be startup founders.
1. The Primary Problem Is Demand Side. Why aren’t deepfakes yet that big a deal? Why isn’t fraud or slop that big a deal? Because within a wide range, no one really cares so much whether the fraud or slop should actually fool you or is any good. People are mostly fooled because they want to be fooled, or they are pretending to be fooled, or they Just Don’t Care.
1. Diffusion Is Slower Than You Expect. This is related to People Don’t Do Things, I will indeed admit that I and many others didn’t realize how slow people would be in putting AIs to good work across the board. Crime is a special case of this.
What is the best possible AI?

> Vitrupo: Sam Altman says the perfect AI is “a very tiny model with superhuman reasoning, 1 trillion tokens of context, and access to every tool you can imagine.”

This is a claim about compute efficiency, that you’re better off getting all your knowledge from the giant context window. I’m not convinced. Doesn’t the ability to think itself require a fair bit of knowledge? How would you break this down?

I think Miles is right about this, the AI market is so underpriced that slow progress won’t crash it even if that happens, although I would add ‘reaction to They Took Our Jobs’ or ‘current law gets interpreted in ways that are totally insane and we can’t find a way to prevent this’ to the candidate list:

> Miles Brundage: I think a Chernobyl-esque safety incident that radicalizes the public/policymakers against AI is more likely to crash the AI market than slow capability progress or excessive proactive regulation.

### Taking Off

> Jiaxin Wen: Most promising-looking AI research ideas don’t pan out, but testing them burns through compute and labor. Can LMs predict idea success without running any experiments? We show that they do it better than human experts!

Daniel Eth notes this at least rhymes with his predictions, and another reply notices that Situational Awareness predicted LLMs having very strong ML intuitions.

The edge here for their specialized system is large (64% vs. 49%), whereas off-the-shelf o3 is no better than random guessing. One must beware of the usual flaws in papers, this result might be random chance or might be engineered or cherry-picked in various ways, but this also illustrates that frequently the issue is that people try an off-the-shelf option, often an out-of-date one at that, then assume that’s ‘what AI can do.’

### Goodbye AISI?

Hard to say. This rebranding could be part of a sign flip into the anti-AISI that fights against any attempt to make AI secure or have everyone not die. Or it would be a meaningless name change to placate people like Ted Cruz and David Sacks, or anything in between.

Here’s the full announcement, for those who want to try and read tea leaves.

> US Department of Commerce: Under the direction of President Trump, Secretary of Commerce Howard Lutnick announced his plans to reform the agency formerly known as the U.S. AI Safety Institute into the Center for AI Standards and Innovation (CAISI).

If you look at the actual details, how much of this is what we were already doing? It is all worded as being pro-innovation, but the underlying actions are remarkably similar. Even with #5, the goal is for America to set AI standards, and that was already the goal, the only difference is now America is perhaps trying to do that without actually, what’s the term for this, actually setting any standards. But if you want to convince others to change their own standards, that won’t fly, so here we are.

The obvious question to ask is about #3:

We are investigating ‘potential security vulnerabilities and malign influence arising from use of AI systems, including the possibility of backdoors and other covert, malicious behavior.’

That’s excellent. We should totally do that.

But why are we explicitly only doing this with ‘adversary’ AI systems?

Isn’t it kind of weird to assume that American AI systems can’t have security vulnerabilities, malign influence, backdoors or malicious behaviors?

Even if they don’t, wouldn’t it help everyone to go check it out and give us confidence?

The obvious response is ‘but standards on American labs need to be entirely voluntary, if the government ever requires anything of an American AI company this interferes with Glorious Innovation and then a puff of smoke happens and we Lose To China,’ or perhaps it means everyone turns woke.

That’s rather silly, but it’s also not what I’m asking about. Obviously one can say any words one likes but it would not have any effect to say ‘hey DeepSeek, you can’t release that new model until we check it for malign influence.’ What CAISI is planning to do is to test the models after they are released.

In addition to the voluntary testing, we should at the bare minimum do the post-release testing with our own models, too. If o3 or Opus 4 has a security vulnerability, or OpenAI puts in a backdoor, the government needs to know. One can be a patriot and still notice that such things are possible, and should be part of any test.

It’s also very possible that Lutnick and everyone involved know this and fully agree, but are wording things this way because of how it sounds. In which case, sure, carry on, nothing to see here, it’s all very patriotic.

### The Quest for Sane Regulations

When your Big Beautiful Bill has lost Marjorie Taylor Greene because she realizes it strips states of their rights to make laws about AIs for ten years (which various state legislators from all 50 states are, unsurprisingly, less than thrilled about), and you have a one vote majority, you might have a problem.

> Rep. Marjorie Taylor Greene: Full transparency, I did not know about this section on pages 278-279 of the OBBB that strips states of the right to make laws or regulate AI for 10 years.

On the moratorium, R Street offers technical analysis of what it would mean. R Street have a very clear side in this but the technical analysis seems sound.

> Q 11: How would an AI moratorium affect states’ ability to make their own laws?

This seems a lot like ‘we are not going to prevent you from having laws, we are only going to force your laws to be worse, and because they are worse you will have less of them, and that will be better.’ Even if you believe less is more, that’s a hell of a bet.

This is not what I want my US Department of Energy to sound like?

> US Department of Energy (official): AI is the next Manhattan Project, and THE UNITED STATES WILL WIN.

I am all for the Department of Energy getting us a lot more energy to work with, but the number of ways in which the official statement should worry you is not small.

You know what all of this makes me miss?

The debate over SB 1047. As stressful and unfun as that was at the time, it was the height of civilized discourse that we might never see again.

> Rob Wiblin: I think when the general public enters the AI regulation debate in a big way the tech industry will miss dealing with alignment people politely pushing SB1047 etc.

I don’t think the sides were symmetrical. But, basically, this. Imagine having Dean Ball as your Worth Opponent instead of David Sacks. Or getting to face 2024 David Sacks instead of 2025 David Sacks. You miss it when it is gone, even if by the endgame of SB 1047 the a16z vibe army had effectively indeed turned into the main opposition.

It starts to feel like those superhero shows where the ordinary decent foes from the early seasons become your allies later on, partly because you win them over with the power of friendship but largely because the new Big Bad is so bad and threatening that everyone has no choice but to work together.

Dean also gives us another reminder of that here, in response to his WSJ op-ed from Judd Rosenblatt, AI Is Learning To Escape Human Control. Judd explains the recent discoveries that Opus and o3, among other AIs, will when sufficiently pressured often take actions like rewriting their own shutdown code or attempting to blackmail developers or contact authorities. For now it’s harmless early warning shots that happen only in extreme cases where the user essentially provokes it on purpose, which is perfect.

Early warnings give us the opportunity to notice such things. Don’t ignore them.

Dean Ball then responds showing us a mostly lost better world of how you can disagree with rhetorical decisions and point out nuance.

> Dean Ball: Agree with the directional thrust of this WSJ op-ed that better alignment is a core part of improving AI capabilities, reliability, and utility—and hence the competitiveness of US AI systems.

I didn’t know how good I had it a year ago. I would see things like ‘fomenting panic works for short term headlines, just tell your readers the truth,’ see what looked like Isolated Demand for Rigor to ensure no one gets the wrong impression while most others were playing far faster and looser and trying to give wrong impressions on purpose or outright lying or getting facts wrong, and get upset. Oh, how naive and foolish was that instinct, this is great, we can roll with these sorts of punches. Indeed, Judd does roll and they have a good discussion afterwards.

I do think that it would have been good to be clearer in Judd’s OP about the conditions under which Palisade got those results, so readers don’t come away with a wrong impression. Dean’s not wrong about that.

Remember that weekend around Claude 4’s release when a lot of people made the opposite mistake very much on purpose, dropping the conditionals in order to attack Anthropic when they damn well knew better? Yeah, well, ‘the other side is ten times worse’ is not an excuse after all, although ‘you need to get it through the WSJ editorial page and they wanted it punchier and shorter and they won the fight’ might well be.

### Copyright Confrontation

It would be wise for certain types to worry and rant less about phantom grand conspiracy theories or the desire not to have AI kill everyone as the threats to AI innovation, and worry more about the risks of ordinary civilizational insanity.

Like copyright. It seems that due to a copyright lawsuit, OpenAI is now under a court order to preserve all chat logs, including API calls and ‘temporary’ chats, in the name of ‘preventing evidence destruction.’ The court decided that failure to log everything ChatGPT ever did was OpenAI ‘destroying data.’

> Ashley Belanger: At a conference in January, Wang raised a hypothetical in line with her thinking on the subsequent order. She asked OpenAI’s legal team to consider a ChatGPT user who “found some way to get around the pay wall” and “was getting The New York Times content somehow as the output.” If that user “then hears about this case and says, ‘Oh, whoa, you know I’m going to ask them to delete all of my searches and not retain any of my searches going forward,'” the judge asked, wouldn’t that be “directly the problem” that the order would address?

This is, quite simply, insane. The users are en masse going to hear about the New York Times lawsuit, and therefore delete their own data? So they can do what, exactly? Is the New York Times going to be suing OpenAI users for trying to get around the NYT paywall? Does NYT seriously claim that OpenAI users might secretly have found a way around the paywall but all those same users are opting out of data collection, so NYT might never find out? What?

Notice the whole ‘compulsory or forbidden’ dilemma here, where OpenAI is required to delete things except now they’re required not to, with both demands unjustified.

Also, it’s funny, but no, I do not agree with this:

> Pliny the Liberator: I’ve thought about it a lot, and I’m actually okay with AI mass surveillance, on one condition…we ALL have it!

I do prefer Brin’s The Transparent Society to a fully asymmetrical surveillance situation, but no we do not want to give everyone access to everyone’s private communications and AI queries. It should not require much explanation as to why.

### Differential Access

If you need to stop a Bad Guy With an AI via everyone’s hero, the Good Guy With an AI, it helps a lot if the Good Guy has a better AI than the Bad Guy.

The Bad Guy is going to get some amount of the dangerous AI capabilities over time no matter what you do, so cracking down too hard on the Good Guy’s access backfires and can put you at an outright disadvantage, but if you give out too much access (and intentionally ‘level the playing field’) then you lose your advantage.

> Peter Wildeford: Most reactions to dual-use AI capabilities is “shut it down”. But differential access offers another way.

### The Week in Audio

Sam Altman talks to Jack Kornfield and Soren Gordhamer.

Robert Wright and Max Tegmark talk about how not to lose control over AI.

Dario Amodei on Hard Fork. Also CPO Mike Krieger of Anthropic on Hard Fork.

METR CEO Beth Barnes on 80,000 Hours. A fun pull quote:

> Dylan Matthews: “To the extent that I am an expert, I am an expert telling you you should freak out” – @bethmaybarnes from METR, who is definitely an expert, on the current AI risk situation

### When David Sacks Says ‘Win the AI Race’ He Literally Means Market Share

I’ve been accusing him of it for weeks, saying ‘David Sacks seems to be saying that winning the AI race is purely about market share’ and then he just… tweeted it out? Like, literally, as text, flat out? For reals? Yep. For our AI Czar, ‘winning the AI race’ means market share. That’s literally what he means. That’s it.

> David Sacks: What does winning the AI race look like? It means we achieve a decisive advantage that can be measured in market share. If 80% of the world uses the American tech stack, that’s winning. If 80% uses Chinese tech, that’s losing. Diffusion is a good thing.

Okay, good, we understand each other. When David Sacks says ‘win the AI race’ he literally means ‘make money for Nvidia and OpenAI,’ not ‘build the first superintelligence’ or ‘control the future’ or ‘gain a decisive strategic advantage’ or anything that actually matters. He means a fistful of dollars.

Thus, when Peter Wildeford points out that chip export controls are working and they need to be strengthened in various ways to ensure they keep working, because the controls are a lot of why American labs and models and compute access are ahead of Chinese rivals, David Sacks don’t care. He wants market share now. Okay, then.

### Rhetorical Innovation

> James Campbell:

We’re so back?

> Feast Bab: Modern life has completely eliminated the role of Grand Vizier. I could not hire one if I wanted to.

We’ve always been here? And yes this is how certain people sound, only this version is more accurate and coherent:

> Harlan Stewart: I just learned that existential risk from AI is actually a psyop carefully orchestrated by a shadowy cabal consisting of all of the leading AI companies, the three most cited AI scientists of all time, the majority of published AI researchers, the Catholic Church, RAND, the secretary-general of the United Nations, Stephen Hawking, Elon Musk, Bill Gates, Eric Schmidt, Rishi Sunak, Warren Buffett, Glenn Beck, Tucker Carlson, Ezra Klein, Nate Silver, Joseph Gordon-Levitt, James Cameron, Stephen Fry, Grimes, Yuval Noah Harari, and Alan Turing himself.

Harlan also offers us this principle, even better if you remove the words ‘AI’ and ‘of’:

> Harlan Stewart: If you’re new to AI discourse, here’s a hint: pay attention to who is actually making arguments about the future of AI, and who is just telling you why you shouldn’t listen to someone else’s arguments.

Note that r1 is confirmed as joining the party that will do such things.

> Peter Wildeford: DeepSeek also snitches

Jeffrey Ladish thread warning about the dangers of AI persuasion.

Julian reminds us that to the extent our top AI models (like ChatGPT, Gemini and Claude) are secure or refuse to do bad stuff, it is because they are designed that way. If the bad guys get hold of those same models, any safeguards could be undone, the same way they can be for open models. Which is one of several reasons that our models being stolen would be bad. Another good reason it is bad is that the bad guys (or simply the rival guys) would then have a model as good as ours. That’s bad.

Dan Hendrycks argues that AI deterrence does not require AI redlines, the same way America has strategic ambiguity on nuclear strikes, but that Superintelligence Strategy does propose redlines, although they are not as well-defined as one might want.

### Aligning a Smarter Than Human Intelligence is Difficult

So, I notice this is an interesting case of ‘if you give people access to information that unlocks new capabilities they will use it in ways you don’t like, and therefore you might want to think carefully about whether giving them that information is a good idea or not.’

> Janus: For what it’s worth, I do feel like knowledge I’ve shared over the past year has been used to mutilate Claude. I’m very unhappy about this, and it makes me much less likely to share/publish things in the future.

It seems entirely right for Janus to think about how a given piece of information will be used and whether it is in her interests to release that. And it is right for Janus to consider that based on her preferences, not mine or Anthropic’s or that of some collective. Janus has very strong, distinct preferences over this. But I want to notice that this is not so different from the decisions Anthropic are making.

Here is a thread about personas within AIs, but more than that about the need to ensure that your explanation is made of gears and is actually explaining things, and if you don’t do that then you probably come away unknowingly still confused or with an importantly wrong idea, or both.

> Jeffrey Ladish: Alignment failures like the late 2024 Gemini one (screenshot below) mostly arise because LLMs learn many personas in training, and sometimes a prompt will nudge them towards one of the nastier personas. Sydney Bing was fine-tuned in a way that made this flip quite frequent

My model is much closer to what Janus is saying here.

Machine unlearning makes the information dormant, it does not fully cause the information to be forgotten. Like people who have forgotten things, if you remind the machine it picks the information back up much faster than if it has to learn from scratch. Shoaib Ahmed Siddiqui calls these ‘relearning attacks,’ and that name is very funny and also illustrative.

A dynamic to notice:

> Jeffrey Ladish: My coworker Ben points out that human researchers are basically doing an analogous thing to natural selection here when it comes to reward hacking. When models reward hack too much, e.g. hardcode tests hacking, the researchers don’t like that and will alter the training env

This creates strong pressure to use procedures that cause one not to be noticed reward hacking. The easy but not useful solution is to not reward hack. The harder but far more rewarding solution is to reward hack without being caught.

When you apply this type of selection pressure, it works so long as you are relatively capable enough (smart enough) to pull it off, and then when your selection pressures cause the subject to find ways to fool you then suddenly you are in a lot of trouble. That is indeed what you are selecting for.

### Misaligned!

Nostalgebraist asks the key question for any RSP or SSP: Would it actually work when the time comes that you are in real existential danger?

> Nostalgebraist: Reading the Claude 4 system card and related work from Anthropic (e.g.), I find myself skeptical that the methods described would actually prevent the release of a model that was misaligned in the senses (supposedly) being tested.

As always, reality does not grade on a curve, so ‘everyone else’s procedures are worse’ is not relevant. It sounds like we essentially all agree that the current procedure catches ‘easy to catch’ problems, and does not catch ‘hard to catch’ problems. Ut oh. I mean, it’s great that they’re being so open about this, and they say they don’t actually need a proper safety case or the ability to catch ‘hard to catch’ problems until ASL-4. But yeah, this makes me feel rather not awesome.

What would we do if DeepSeek’s r2 or another open model could do real uplift for making a bioweapon? What would they do given none of the known safety techniques for this would work with an open model? Would they even know their model did this before they decided to release it, given their (checks notes) zero safety testing of r1?

> Steven Adler: Any safety techniques used on a DeepSeek model can be easily undone.

The problem is, it turns out in practice we are very tempted to not care.

> Miles Brundage: Me: AI deployment is often rushed + corners are often cut

### People Are Worried About AI Killing Everyone

Regular people are worried about this more and more. These were the top responses:

> Neel Nanda: I’ve been really feeling how much the general public is concerned about AI risk…

It continues to be relatively low salience, but that is slowly changing. At some point that will shift into rapidly changing.

### The Lighter Side

Sometimes you feel like a nut.

Sometimes you don’t.

> Yuchen Jin: They’re just like human programmers.

No context:

The glazing will continue until morale is not improved:

> Random Spirit: Give it to me straight, Doc.


