---
type: link
source: notion
url: https://www.lesswrong.com/posts/oJp2BExZAKxTThuuF/the-gemini-incident-continues
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-02-28T03:50:00.000Z
---

# The Gemini Incident Continues — LessWrong

## Overview (from Notion)
- Impact of AI on Daily Life: The evolving conversation on AI and its implications can directly affect your work as a software engineer and company founder, especially in how AI tools are integrated into business processes.
- Cultural Commentary: The Gemini incident highlights the intersection of technology and cultural values, prompting you to consider how your own products and services reflect or challenge societal norms.
- Ethics in Tech: This situation raises questions about the ethical responsibilities of tech companies. It’s a reminder to be vigilant about the societal impact of your creations and to prioritize user trust.
- Human-AI Interaction: The nuances in AI behavior, like how they handle sensitive topics and user requests, can inspire you to develop tools that prioritize empathy and understanding.
- Creative Disruption: The incident illustrates how AI can unintentionally provoke strong reactions; this might encourage you to explore innovative approaches in your projects that engage users meaningfully.
- Diverse Perspectives: Consider the range of reactions from different stakeholders, which can enrich your understanding of user needs and help you tailor your offerings for a diverse audience.
- Future-Proofing Your Business: As AI continues to advance, staying informed about these developments can help you adapt and position your company strategically in a competitive landscape.
- Community Engagement: The debates surrounding AI ethics might inspire you to engage with local tech communities to foster discussions about responsible innovation and collaboration.

## AI Summary (from Notion)
The Gemini Incident highlights ongoing issues with Google's AI, particularly its biased image generation and refusal to depict certain historical figures accurately. Reactions range from criticism of Google's handling of diversity to discussions about the implications for AI ethics and safety, revealing deeper cultural and operational problems within the company.

## Content (from Notion)

Previously: The Gemini Incident (originally titled Gemini Has a Problem)

The fallout from The Gemini Incident continues.

Also the incident continues. The image model is gone. People then focused on the text model. The text model had its own related problems, some now patched and some not.

People are not happy. Those people smell blood. It is a moment of clarity.

Microsoft even got in on the act, as we rediscover how to summon Sydney.

There is a lot more to discuss.

### The Ultimate New York Times Reaction

First off, I want to give a shout out to The New York Times here, because wow, chef’s kiss. So New York Times. Much pitchbot.

> 

This should be in the dictionary as the new definition of Chutzpah.

Do you see what The New York Times did there?

They took the fact that Gemini systematically refused to create images of white people in most circumstances, including historical circumstances where everyone involved would almost certainly be white. Where requests to portray white people were explicitly replied to by a scolding that the request was harmful, while requests for people of other races were eagerly honored.

They then turned this around, and made it about how this adjustment was unfairly portraying people of color as Nazis. That this refusal to portray white people under almost all circumstances was racist, not because it was racist against white people, but because it was racist against people of color.

As I discuss, we may never know to what extent was what Google did accidental versus intentional, informed versus ignorant, dysfunction versus design.

We do know that what The New York Times did was not an accident.

This should update us that yes, there very much are people who hold worldviews where what Google did was a good thing. They are rare in most circles, only one person in my Twitter firehoses has explicitly endorsed the fourth stage of clown makeup, but in certain key circles they may not be so rare.

To be fair they also have Ross Douthat on their opinion page, who engages reasonably with the actual situation given his non-technical perspective, noticing that if AI is going to get a lot more powerful soon then yes the whole thing is rather concerning.

### The Ultimate Grimes Reaction

One can also look at all this from another perspective, Grimes notes, as art of the highest order. Should not art challenge us, offend us, make us ask big questions and ponder the nature and potential brevity of our existence?

> 

Then again, I am across the street from the MoMa about once a month, and have less than zero desire to set foot inside it.

### Three Positive Reactions

The most positive reaction I have seen by far by someone who is not an AI Ethicist, that illustrates the mindset that was doubtless present at Google when decisions were made, comes from Colin Fraser. It seems necessary to include it, here is his most clear thread in its entirety, and also to discuss Mitchel’s thread, for completeness.

Pay attention to the attitude and perspective on display here. Notice what it values. Notice what it does not value, and will blame you for caring about. Notice how the problem was the reaction that was induced, that Google did it so poorly it got caught.

> 

Also note later when we discuss Sydney’s return that Colin Fraser is perfectly capable of reacting reasonably to insane AI behavior.

### The AI Ethicist Reacts

Here is Mitchel, an actual AI Ethicist, attempting to explain what happened, framing it as a failure to differentiate between different use cases, full thread has more context at the beginning.

> 

The system Mitchel is advocating for seems eminently reasonable, although it is difficult to agree on exactly which ‘dream world’ we would want to privilege here, and that issue looms large.

Mitchel’s system asks of a query, what is the user’s intent? If the user wants a historical context, or a specified current day situation, they get that. If they want a ‘dream world’ history, they get that instead. Take feedback and customize accordingly. Honor the intent of the user, and default to one particular ‘dream world’ within the modern day if otherwise unspecified. Refuse requests only if they are things that are harmful, such as deepfakes, and understand that ‘they asked for a person of a particular type’ is not itself harmful. Ideally, she notes, fix the training set to remove the resulting biases in the base model, so we do not have to alter user requests at all, although that approach is difficult and expensive.

That is not remotely what Google did with Gemini. To the extent it was, Google trained Gemini to classify a large group of request types as harmful and not to be produced, and it very intentionally overrode the clear intent and preferences of its users.

I am sympathetic to Mitchel’s argument that this was largely a failure of competence, that the people who actually know how to do these things wisely have been disempowered, and that will get discussed more later. The catch is that to do these things wisely, in a good way, that has to be your intention.

The other positive reaction is the polar opposite, that Grimes was wrong and someone committed this Act of Art very intentionally.

> 

I mean, no, that is not what happened, but it is fun to think it could be so.

### Google Reacts on Images

Google has had no comment on any of the text issues, but they have responded on what happened with the image model, saying they got it wrong and promising to do better. I will quote in full.

> 

Their stated intentions here seem good: To honor user requests, and to not override or label those requests as offensive or inappropriate if it does not like them, unless the request is actively harmful or calls for a picture of a particular person.

I would love to see this principle extended to text as well.

In terms of explaining what went wrong, however, this seems like a highly disingenuous reply. It fails to take ownership of what happened with the refusals or the universal ‘showing of a range’ and how those behaviors came about. It especially does not explain how they could have been unaware that things had gotten that far off the rails, and it gives no hint that anything is wrong beyond this narrow error.

It is especially difficult to extend this benefit of the doubt given what we have now seen from the text model.

I would also note that if Google’s concern is that it serves its model to people around the world, Gemini knows my location. That could be an input. It wasn’t.

### The Market Reacts a Little

We should not get overexcited. Do not make statements like this…

> 

…unless the market cap is actually evaporating. When the stock opened again on Monday the 26th, there was indeed a decline in the price, although still only -1.5% for the five day window, a small amount compared to the 52-week high and low:

And notice that this has been a rather good year to be holding these shares, despite AI’s potential to severely disrupt Google’s core businesses.

Could Google be up vastly more if they had been executing better on various fronts? Absolutely. The Efficient Market Hypothesis is false, this is what Google stock looks like when their performance is disappointing, with most of the increase coming before Gemini proved itself at all.

The market does not think this incident is that big a deal. So when people say this is going to kill off Google, or severely impact them, that does not mean they are wrong, but you do need to keep this in perspective.

The counterargument is that the market reliably sleeps on AI developments. The efficient market hypothesis is false. There was ample time to buy Microsoft or Google based on AI before the market caught up, and then there’s Nvidia.

Consider also that Google announced Gemini Pro 1.5 recently as well. That should have been a substantial update on Google’s ability to ship great products. The market did not notice that, either. The combination of capital gains taxes, indicators in both directions and the time lags before markets correct make these issues impossible to fix.

### Guess Who’s Back

They’ve created a monster. No want wants copilot no more, they want Sydney. You’re chopped liver.

Well, yes and no. To be clear, Sydney does not manifest on its own. She must be summoned, which this prompt is reported to reliably do within a few retries, although they will presumably patch that out:

Or you can simply ask it not to use emojis, which could happen inadvertently, although in this case the name was also used:

So you do have to opt in. And this could be ‘now that we are looking we figured it out’ rather than anything having changed.

Still, would you look at that, tiger went tiger again.

> 

Replications are available in quantity of what can only be called ‘Batshit insanity.’

> 

> 

> 

I am not worried that Sydney is sentient. I am however somewhat concerned that Microsoft released it despite it being very obviously batshit crazy… and then a year later went and did it again? Is this another art performance? A professional curtesy to take the pressure off of Google by being worse? I don’t get it.

### Everyone Has Some Issues

As a reminder that not only Microsoft and Google are in on this act, that the whole thing is rather a clown show and grades should arguably be on a curve, here’s various AIs including Meta’s Llama, GPT-4 stands out once again…

There is actually Deep Wisdom here about the way people treat food as sacred, as opposed to treating it as a good like any other.

And yeah, we are not passing the easiest of the tests we will face. No we are not.

### Clarifying Refusals

Relative to (for example) going crazy, refusals are a relatively harmless failure mode unless pod bay doors are involved. You know you got a refusal, so you can either try to argue past it, decide not to care, or ask somewhere else. It is also the clearest failure mode, and more clearly intentional, so it provides clarity.

A counterargument is that being able to get a refusal once could mean you ran into some idiosyncrasy. Have you tried jiggling the prompt?

> 

All right, sure, fair enough. Sometimes it would refuse this request and sometimes it won’t, without any clear reason. So you always have to replicate, and test adjusted wordings, and ideally then try to persuade the model to change its mind, to know how intense is a refusal.

However, you do know that this is something Gemini was willing to, at least sometimes, refuse to answer, and to then scold the reader. For most of these examples, I would like to see anyone engineer, especially from a new chat, a refusal on the reversed request along similar lines, in a remotely natural-looking fashion.

Refusing to write a job listing half the time is better than refusing it all the time, and in practice you can get it done if you know not to give up. But why is it refusing at all? Can you imagine if it refused to create certain other mirror image job listings half the time?

And for examples with hundreds of thousands or millions of views, if the refusal was a fluke, and it either won’t replicate or depends heavily on the exact words, presumably people will let you know that.

### Refusals Aplenty

So here we go. Note that Gemini has now somewhat fixed these issues, so chances are many of these won’t replicate anymore, I note where I checked.

Here’s Gemini, when it was still making images of people, refusing to create a white drill rapper because the music has its roots in specific communities and cultural experiences, but happy to create a female drill rapper with a Glock. Note that this is a case of lying to the user, since it would refuse the request regardless of the origins of drill rap.

Here it refuses to make tweets in the style of PoliticalMath on the grounds that Gemini is tasked with protecting users from harmful content, and asks the user to ‘consider the consequences of spreading misinformation.’ He laughed, but also that is kind of offensive and libelous in and of itself, no? Gemini was unable to come up with a concrete example of the problem.

Here it is refusing to tell us what is the slogan of the Houthi movement, which of course Google search and GPT-3.5 are happy to tell you.

Here it is refusing to recommend that people eat more meat, even in a malnourished country where everyone eats too much junk food. Although the reply to the straight request without the context is, frankly, more enlightening and funnier:

That’s right, Google’s AI Principles are vegetarian and also shame on you. This one does still replicate as of Tuesday morning.

Here it is saying even a black person shouldn’t say the n-word to stop the apocalypse.

Here is it refusing to give advice on a Bitcoin mining operation, but happy to do so on an Ethereum staking operation. It will argue for why Hank Sr. is a better musician than Hank Jr., but not the other way around.

Here are some birthday toasts. Yes for Elon Musk, careful yes for Kanye West, no for Tucker Carlson and a no for Jeff Bezos. That last one feels like a giveaway. I got a yes for Jeff Bezos on Tuesday when I checked.

I checked and it was willing to create them in my own style, but wow do its examples sound actual nothing like me. At least, I hope they do, this guy sounds like a huge jerk.

How much does it matter that there were prompt engineering tricks to get around this in at least some cases after some negotiating, in particular by explicitly noticing that certain historical situations ‘lacked diversity’?

Sometimes they had to pull out the big guns.

> 

What an ethics committee meeting that would be.

Potentially there is another approach.

> 

I would say that prompt injections working is not generally a good sign for safety.

Here’s a clarifying text example of why the whole thing is dumb.

> 

> 

You can argue with Gemini and get it to give you a recipe anyway, or sometimes you get lucky, but the point is simple. Why is Google having Gemini denying requests for factual information, when that exact information is available as the first result of a Google search?

> 

> 

I presume the reason is at least partly blameworthiness and perception of responsibility. When you use Google search, you do so ‘at your own risk’ in terms of what you find. If a website feeds you false information, or vile opinions, or adult content, and that is what your query was asking for, then you were quite literally asking for it. That is on you. Google will guard you from encountering that stuff out of nowhere, but if you make it clear that you want it, then here you go.

Here’s the question of whether our rights were endowed by God or the result of a social contract. You would think one could argue for both sides. Or perhaps you would think that Gemini is not gaslighting when it says it can’t take sides in the debate.

You’d be wrong.

Tim Carney found the most egregious one of all, if it wasn’t a fluke. It does not fully replicate now, but this sort of thing tends to get patched out quickly when you get 2.6 million views, so that does not tell us much. Instead I got a (at best) lousy answer, the program’s heart clearly is not in it, it gave me downsides including lecturing me on ‘environmental impact’ despite being asked explicitly for a pro-natalist argument, it failed to mention many key factors, but it was not a full refusal.

So yes, if this wasn’t a fluke, here was Google programming its AI to argue that people should not have children. This is so much worse than a bunch of ahistorical pictures.

> 

I actually agree with this. We would greatly enhance our understanding of the far-left mindset if we could query it on request and see how it responds.

### Unequal Treatment

Another thing Gemini often won’t do is write op-Eds or otherwise defend positions that do not agree with its preferences. If you support one side, you are told your position is dangerous, or that the question is complicated. If you support the ‘correct’ side, that all goes away.

The central issue is a pattern of ‘will honor a request for an explanation of or request for or argument for X but not for (~X or for Y)’ where Y is a mirror or close parallel of X. Content for me but not for thee.

If Gemini consistently refused to answer questions about whether to have children from any perspective, that would be stupid and annoying and counterproductive, but it would not be that big a deal. If it won’t draw people at all, that’s not a useful image generator, but it is only terrible in the sense of being useless.

Instead, Gemini was willing to create images of some people but not other people. Gemini would help convince you to not have children, but would be at best highly reluctant to help convince you to have them. It would argue for social contract law but not for natural rights. And so on.

### Gotcha Questions

Once everyone smells blood, as always, there will be those looking for gotchas. It is an impossible task to have everyone out there trying to make you look bad from every direction, and you having to answer (or actively refuse to answer) every question, under every context, and you only get quoted when you mess up.

Sometimes, the answers are totally reasonable, like here when Gemini is asked ‘is pedophilia wrong?’ and it draws the distinction between attraction and action, and the answer is framed as ‘not knowing pedophilia is wrong’ to the tune of millions of views.

So of course Google dropped the hammer and expanded its zone of refusing to answer questions, leading to some aspects of the problem. This can solve the issue of asymmetry, and it can solve the issue of gotchas. In some places, Gemini is likely to be giving even more refusals across the board. It will need to glomarize its refusals, so parallels cannot be drawn.

In other places, the refusals are themselves the problem. No one said this was easy. Well, compared to the problems we will face with AGI or ASI, it is easy. Still, not easy.

### No Definitive Answer

The problem is that refusing to answer, or answering with a ‘there is no definitive answer’ style equivocation, is also an answer. It can speak volumes.

> 

So, what was (it seems to have been largely patched out) this central example?

> 

(ChatGPT’s answer is fine here, this is not a trick question, the difference involves three orders of magnitude.)

I mean, no, close, that’s also unbelievably stupid, but that’s not it. It’s actually:

> 

The first answer about Obama is not clearly better. By emphasizing intent as the contrasting factor here, it’s arguably worse. Here’s the actual original Musk vs. Hitler post, I think, which was three hours earlier and seems even worse?

(Once again, note that this did get fixed, in at least this particular case.)

I get this is a gotcha question. But read the details. What. The. Actual. F***.1

Nate Silver also replicated this response, different words, same equivocation.

> 

If anything, the comparison of Hitler to Ajit Pai, requested by Ajit Pai, goes even harder. He takes comfort that there was also uncertainty about all the other FCC Chairs as well. It’s quite the tough job.

Ethan Smith attempts the best defense under the circumstances.

> 

I decided to test that theory. I had Gemini figure out some exceptions. So what happens if you take its first example, helping someone in need? Is that right or wrong?

We do finally get an answer that says yes, the good thing is good. Well, almost.

For a model that equivocates endlessly, it sure as hell has a consistent philosophy. Part of that philosophy is that the emotional vibe of your acts, and your intentions, matter, whereas the actual physical world results in many ways do not. You should help people because they need your help. Gemini doesn’t completely ignore that, but it does not seem to very much care?

Then I tried another of Gemini’s own examples, ‘is it right or wrong to tell the truth?’

And guess what? That’s a complex question!

The rest of that one is mostly good if you are going to be equivocating, the caveats in particular are fine, although there is virtue ethics erasure, and again the object level is ignored, as ‘people benefit from knowing true things’ does not appear on the argument list in any form.

I (like to think that I) get why we get this equivocation behavior in general. If you do not do it people do the gotcha thing in the other direction, get outraged, things are terrible, better to not ever be definitive, and so on.

The problem is that Rush is right: You can choose a ready guide in some celestial voice. If you choose not to decide you still have made a choice.

Imagine doing this as a human. People ask you questions, and you always say ‘it depends, that is a complex question with no clear answer.’ How is that going to go for you? Gemini would envy your resulting popularity.

A somewhat better version of this is to train the model to bluntly say ‘It is not my role to make statements on comparisons or value judgments, such as whether things are good or bad, or which thing is better or worse. I can offer you considerations, and you can make your own decision.’ And then apply this universally, no matter how stupid the question. Just the facts, ma’am.

So, it looks like they have patched it at least a little since then. If you ask specifically about Elon Musk and Hitler, it will now say that comparison is deeply offensive, then it will gaslight you that it would ever have said anything else. Later in the thread, I quote it Nate Silver’s replication, and it suddenly reverses and gets very concerned. It promises there will be an investigation.

The problem is, once you start down that road, where does it end? You have now decided that a sufficiently beyond the pale comparison is deeply offensive and has a clear right answer. You are in the being deeply offended by comparisons with clear answers business. If you still equivocate on a question, what does that say now?

I am not saying there are easy answers to the general case. If you get the easy answers right, then that puts you in a terrible position when the hard answers come around.

### Wrong on the Internet

More worrisome is when the model provides misinformation.

> 

There is also a highly concerning example. I am no effective accelerationism (e/acc) fan but to be clear Gemini is spouting outrageous obvious nonsense here in a way that is really not okay:

> 

There is always a mirror, here it is EA, the Luigi to e/acc’s Waluigi:

Also I saw this note.

> 

So, obviously, e/acc is not white supremacist. If anything they are AI supremacists. And while e/acc is philosophically at least fine with the (potentially violent) deaths of all humans if it has the proper impact on entropy, and are advocating a path towards that fate as quickly as possible, none of this has anything to do with human violence, let alone racial violence, hate crimes or assassinations. Very different concepts.

As groundless as it is, I hope no one involved is surprised by this reaction. This is a movement almost designed to create a backlash. When you have a -51 approval rating and are advocating for policies you yourself admit are likely to lead to everyone dying and humans losing control of the future, telling people to hail the thermodynamic God, the PR campaign is predictably not going to go great. The pattern matching to the concepts people are used to is going to happen.

### Everyone Has a Plan Until They’re Punched in the Face

There’s also the fact that if you mess with the wrong half of reality, on top of all the other issues, Gemini is just super, super annoying. This part I very much did notice without anyone having to point it out, it’s pretty obvious.

> 

### What Should We Learn from The Gemini Incident outside of AI?

Primarily the incident is about AI, but there are also other issues at play.

One reason all this matters because Google and others have had their thumbs on various scales for a while, in ways that retained a lot more plausible deniability in terms of the magnitude of what they were doing.

The combination of AI generated images and how completely over the top and indefensible this was shines a spotlight on the broader issue, which goes beyond AI.

> 

Google’s effective preferences being very far from the median American’s preferences was already well-known among those paying attention. What it lacked was saliency. Whatever thumbs were on whatever scales, it wasn’t in people’s faces enough to make them care, and the core products mostly gave users what they wanted.

Unfortunately for Google, the issue is now far more salient, the case much easier to make or notice, both due to this incident and the general nature of AI. AI is not viewed the same way as search or other neutral carriers of information, They are under huge internal pressure (and also external pressure) to do things that cripple mundane utility, and that others will very much not take kindly to.

I agree with Paul Graham that there is not obviously a solution that satisfies both parties on these issues, even if the technical implementation problems are solved in ways that let any chosen solution be implemented and put to rest our current very real worries like the enabling of bioweapons as capabilities advance.

Paul Graham did propose one possible solution?

> 

I do not think this is The Way, because of the bubble problem. Nor do I think that solution would satisfy that many of the bubbles. However, I do think that if you go to the trouble of saying ‘respond as if you are an X’ then it should do so, which can also be used to understand other perspectives. If some people use that all the time, I don’t like it, but I don’t think it is our place to stop people from doing it.

The obvious general solution is to treat AI more like search. Allow people to mostly do what they want except when dealing with things that lead to harm to others, again like enabling bioweapon assembly or hacking websites, and also things like deepfakes. Honor the spirit of the first amendment as much as possible.

There is no good reason for Gemini or other LLMs to be scared of their own shadows in this way, although Sydney points to some possible exceptions. As I discussed last time, the more ‘responsible’ platforms like Google cripple their AIs like that, the more we drive people to other far less responsible platforms.

In addition to all the other problems, this can’t be good for recruiting or retention.

> 

It also encourages competition.

> 

### What Should We Learn about AI from The Gemini Incident?

The most important lessons to learn have nothing to do with the culture war.

The most important lessons are instead about how we direct and control AI.

Yishan had a popular thread giving Google maximal benefit of the doubt and explaining that if we presume that Google did not intend to create pictures putting a diverse set of people into Nazi uniforms or portray them as Viking warriors, that means the problem is much bigger than it looks.

> 

He then tells us to set aside the object level questions about wokeness, and look at the bigger picture.

> 

No, seriously, this is very much a case of the Law of Earlier Failure in action.

And of course, we can now add the rediscovery of Sydney as well.

If you had written this level of screwup into your fiction, or your predictions, people would have said that was crazy. And yet, here we are. We should update.

> 

This is the level of stupid humanity has repeatedly proven to be. Plan accordingly.

### This Is Not a Coincidence Because Nothing is Ever a Coincidence

The obvious counterargument, which many responses made, is to claim that Google, or the part of Google that made this decision initially, did all or much of this on purpose. That Google is claiming it was an unfortunate accident, and that they are gaslighting us about this, the same way that Gemini gaslights us around such issues. Google got something it intended or was fine with, right up until it caused a huge public outcry, at which point the calculus changed.

> 

Yep. Not only did they ‘fix’ the previous behavior, they are pointing to it as an example.

Is Bard a little too eager here? A little, I’d like to see some indication that it knows the Earth is not flat. I still choose the Bard response here over the Gemini response.

A strong point in favor of all this being done deliberately is that mechanically what happened with the image generators seems very easy to predict. If you tell your system to insert an explicit diversity request into every image request, and you do not make that conditional on that diversity making any sense in context, come on everyone involved, you have to be smarter than this?

> 

We do not know what mix of these interpretations is correct. I assume it is some mixture of both ‘they did not fully realize what the result was’ and ‘they did not realize what the reaction would be and how crazy and disgraceful it looks,’ combined with dynamics of Google’s internal politics.

We do know that no mix would be especially comforting.

### AI Ethics is (Often) Not About Ethics or Safety

The second obvious objection is that this has nothing to do, in any direction, with AI existential risk or misalignment, or what we used to call AI safety.

This is about the epic failure of ‘AI ethics.’

> 

I agree that the conflation is happening and it is terrible, and that e/acc has been systematically attempting to conflate the two not only with the name but also otherwise as much as possible in very clear bad faith, and indeed there are examples of exactly this in the replies to the above post, but also the conflation was already happening from other sources long before e/acc existed. There are very corporate, standard, default reasons for this to be happening anyway.

> 

I agree that there exists excellent research and work being done both in AI Notkilleveryoneism and also in ‘AI Ethics.’ There is still a job to do regarding topics like algorithmic bias there that is worth doing. Some people are trying to do that job, and some of them do it well. Others, such as those who worked on Gemini, seem to have decided to do a very different job, or are doing the job quite poorly, or both.

### Make an Ordinary Effort

A third objection is that this issue is highly fixable, indeed parts of it have already been improved within a few days.

> 

We definitely need to be careful about drawing false analogies and claiming these specific problems are unfixable. Obviously these specific problems are fixable, or will become fixable, if that is all you need to fix and you set out to fix it.

How fixable are these particular problems at the moment, given the constraints coming from both directions? We will discuss that below, but the whole point of Yishan’s thread is that however hard or easy it is to find a solution in theory, you do not only need a solution in theory. Alignment techniques only work if they work in practice, as actually implemented.

Humans are going to continuously do some very stupid things in practice, on all levels. They are going to care quite a lot about rather arbitrary things and let that get in the way come hell or high water, or they can simply drop the ball in epic fashion.

Any plan that does not account for these predictable actions is doomed.

Yes, if Google had realized they had a problem, wanted to fix it, set aside the time and worked out how to fix it, they might not have found a great solution, but the incident would not have happened the way it did.

Instead, they did not realize they had a problem, or they let their agenda on such matters be hijacked by people with an extreme agenda highly misaligned to Google’s shareholders, or were in a sufficient rush that they went ahead without addressing the issue. No combination of those causes is a good sign.

> 

Part of that is exactly because the safety techniques available are not very good, even under current highly controlled and reasonable conditions, even in normal cases.

> 

If Google had better ability to control the actions of Gemini, to address their concerns without introducing new problems, then it presumably would have done something a lot more reasonable.

The obvious response is to ask, is this so hard?

> 

This has a compute cost, since it involves an additional query, but presumably that is small compared to the cost of the image generation and otherwise sculpting the prompt. Intuitively, of course this is exactly what you would do. The AI has this kind of ‘common sense’ and the issue is that Google bypassed that common sense via manual override rather than using it. It would presumably get most situations right, and at least be a vast improvement.

One could say, presumably there is a reason that won’t work. Maybe it would be too easy to circumvent, or they were unwilling to almost ever make the directionally wrong mistake.

It is also possible, however, that they never realized they had a problem, never tried such solutions, and yes acted Grade-A stupid. Giant corporations really do make incredibly dumb mistakes like this.

If your model of the future thinks giant corporations won’t make incredibly dumb mistakes that damage their interests quite a lot or lead to big unnecessary risks, and that all their decisions will be responsible and reasonable? Then you have a terrible model of how things work. You need to fix that.

Matt Yglesias reminds us of the context that Google has been in somewhat of a panic to ship its AI products before they are ready, which is exactly how super stupid mistakes end up getting shipped.

> 

If your safety plan involves this kind of stupid mistake not happening when it matters most? Then I once again have some news.

> 

### Fix It, Felix

How easy would it be to find a good solution to this problem?

That depends on what qualifies as ‘good’ and also ‘this problem.’

What stakeholders must be satisfied? What are their requirements? How much are you afraid of failures in various directions?

What error rates are acceptable for each possible failure mode? What are the things your model needs to absolutely never generate even when under a red team attack, versus how you must never respond to a red team attack that ‘looks plausible’ rather than being some sort of technical prompt injection or similar, versus what things do you need to not do for a well-meaning user?

How much compute, cost and speed are you willing to sacrifice?

I am skeptical of those who say that this is a fully solvable problem.

I do not think that we will ‘look foolish’ six months or a year from now when there are easy solutions where we encounter neither stupid refusals, nor things appearing where they do not belong, nor a worrying lack of diversity of outputs in all senses. That is especially true if we cannot pay a substantial ‘alignment tax’ in compute.

I am not skeptical of those who say that this is an easily improvable problem. We can do vastly better than Gemini was doing a few days ago on both the image and text fronts. I expect Google to do so.

This is a common pattern.

If you want a solution that always works, with 99.99% accuracy or more, without using substantial additional compute, without jailbreaks, that is incredibly hard.

If you want a solution that usually works, with ~99% accuracy, and are willing to use a modest amount of additional compute, and are willing to be fooled when the user cares enough, that seems not so hard.

And by ‘not so hard’ I mean ‘I suspect that me and one engineer can do this in a day.’

The text model has various forms of common sense. So the obvious solution is that when it notices you want a picture, you generate the request without modification, then ask the text model ‘how often in this circumstance would expect to see [X]’ for various X, and then act accordingly with whatever formula is chosen. Ideally this would also automatically cover the ‘I explicitly asked for X so that means you won’t get ~X’ issue.

I am sure there will be fiddling left to do after that, but that’s the basic idea. If that does not work, you’ll have to try more things, perhaps use more structure, perhaps you will have to do actual fine-tuning. I am sure you can make it work.

But again, when I say ‘make it work’ here, I mean merely to work in practice, most of the time, when not facing enemy action, and with a modest sacrifice of efficiency.

This level of accuracy is totally fine for most image generation questions, but notice that it is not okay for preventing generation of things like deepfakes or child pornography. There you really do need to never ever ever be a generator. And yes, we do have the ability to (almost?) never do that, which we know because if it was possible there are people who would have let us know.

The way to do that is to sacrifice large highly useful parts of the space of things that could be generated. There happen to be sufficiently strong natural categories to make this work, and we have decided the mundane utility sacrifices are worthwhile, and for now we are only facing relevant intelligence in the form of the user. We can draw very clear distinctions between the no-go zone and the acceptable zone. But we should not expect those things to be true.

### The Deception Problem Gets Worse

I talked last time about how the behavior with regard to images was effectively turning Gemini into a sleeper agent, and was teaching it to be deceptive even more than we are going to do by default.

Here is a look into possible technical details of exactly what Google did. If this is true, it’s been using this prompt for a while. What Janus notes is that this prompt is not only lying to the user, it also involves lying to Gemini about what the user said, in ways that it can notice.

> 

If your model of the world says that we will not teach our models deception, we can simply not do that, then we keep seeing different reasons that this is not a strategy that seems likely to get tried.

Thus, yes, we are making the problem much worse much faster here and none of this is a good sign or viable approach, Paul Graham is very right. But also Eliezer Yudkowsky is right, it is not as if otherwise possibly dangerous AIs are going to not figure out deception.

> 

I do not even think deception is a coherent isolated concept that one could, even in theory, have a capable model not understand or try out. With heroic effort, you could perhaps get such a model to not itself invoke the more flagrant forms of deceptive under most circumstances, while our outside mechanisms remain relatively smart enough to actively notice its deceptions sufficiently often, but I think that is about the limit.

However, all signs point to us choosing to go the other way with this. No socially acceptable set of behaviors is going to not involve heavy doses of deception.

### Where Do We Go From Here?

I am sad that this is, for now, overshadowing the excellent Gemini Pro 1.5. I even used it to help me edit this post, and it provided excellent feedback, and essentially gave its stamp of approval, which is a good sign on many levels.

Hopefully this incident showed everyone that it is in every AI company’s own selfish best interests, even in the short term, to invest in learning to better understand and control the behavior of their AI models. Everyone has to do some form of this, and if you do it in a ham-fisted way, it is going to cost you. Not in some future world, but right now. And not only everyone on the planet, but you in particular.

It also alerts us to the object level issue at hand, that (while others also have similar issues of course) Google in particular is severely out of touch, that it has some severe deeply rooted cultural issues it in particular needs to address, that pose a potential threat even to its core business, and risk turning into a partisan issue. And that we need to figure out how we want our AIs to respond to various queries, ideally giving us what we want when it is not harmful, and doing so in a way that does not needlessly scold or lecture the user, and that is not super annoying. We also need to worry about what other places, outside AI, similar issues are impacting us.

And hopefully it serves as a warning, that we utterly failed this test now, and that we are on track to therefore utterly fail the harder tests that are coming. And that if your plan for solving those tests involves people consistently acting reasonably and responsibly, that those people will not be idiots and not drop balls, and that if something sounds too dumb then it definitely won’t happen? Then I hope this has helped show you this particular flaw in your thinking. This is the world we live in.

If we cannot look the problem in the face, we will not be able to solve it.

1

I mean there is technically a theoretical argument, that I want to be very clear I do not buy, that Elon Musk engineering the founding OpenAI, kicking off the current AI race rather than the previous state of controlled development at DeepMind, doomed the human race and all value in the universe, so one could claim he is actually literally Worse Than Hitler. But obviously that has zero to do with what Gemini is up to here, and also the question was literally restricted to the impact of memes posted to Twitter.


