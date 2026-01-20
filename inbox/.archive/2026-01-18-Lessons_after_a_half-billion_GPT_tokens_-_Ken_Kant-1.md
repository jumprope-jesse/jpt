---
type: link
source: notion
url: https://kenkantzer.com/lessons-after-a-half-billion-gpt-tokens/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-04-14T05:17:00.000Z
---

# Lessons after a half-billion GPT tokens - Ken Kantzer's Blog

## Overview (from Notion)
- The insights on using LLMs effectively can help streamline your software development processes, making your work more efficient and reducing time spent on repetitive tasks.
- Emphasizing simplicity in prompts might resonate with your experience in coding, where sometimes less complexity leads to better results.
- The discussion on user experience innovations, like variable-speed typing, could inspire you to enhance user interactions in your own products.
- The skepticism around using additional frameworks (like Langchain) might reflect your own journey in avoiding unnecessary complexity in your projects.
- The notion that GPT's hallucinations are minimal when given clear context aligns with your understanding of the importance of precise communication in both coding and parenting.
- The commentary on the future of AI suggests that staying adaptable is key, especially in a fast-paced environment like NYC where technology evolves rapidly.
- Consider the idea that achieving Gen AI might take longer than anticipated; it invites you to think about how to leverage current technologies wisely rather than chasing the next big thing.
- The viewpoint on vector databases being more suited for search rather than general use can help you focus on what truly adds value in your tech stack.
- Overall, these lessons challenge you to think critically about how you integrate AI into your life and work, balancing innovation with practicality.

## AI Summary (from Notion)
Key lessons from processing over 500 million GPT tokens include the effectiveness of vague prompts, the limited necessity of complex frameworks like Langchain, and the positive user experience from variable-speed text output. Additionally, hallucination is rare in specific extraction tasks, while context windows are misleadingly named, as output limits remain low. The author expresses skepticism about achieving general AI and anticipates incremental improvements with future models like GPT-5, emphasizing that current models are already quite useful.

## Content (from Notion)

CTO @ Truss | Former VP of Engineering and Head of Security @ FiscalNote | ex-PKC co-founder | princeton tiger '11 | writes on engineering, management, and security.

My startup (gettruss.io) released a few LLM-heavy features in the last six months, and the narrative around LLMs that I read on Hacker News is now starting to diverge from my reality, so I thought I’d share some of the more “surprising” lessons after churning through just north of 500 million tokens, by my estimate.

Some details first:

– we’re using the OpenAI models, see the Q&A at the bottom if you want my opinion of the others

– our usage is 85% GPT-4, and 15% GPT-3.5

– we deal exclusively with text, so no gpt-4-vision, Sora, whisper, etc.

– we have a B2B use case – strongly focused on summarize/analyze-extract, so YMMV

– 500M tokens actually isn’t as much as it seems – it’s about 750,000 pages of text, to put it in perspective

Lesson 1: When it comes to prompts, less is more

We consistently found that not enumerating an exact list or instructions in the prompt produced better results, if that thing was already common knowledge. GPT is not dumb, and it actually gets confused if you over-specify.

This is fundamentally different than coding, where everything has to be explicit.

Here’s an example where this bit us:

One part of our pipeline reads some block of text and asks GPT to classify it as relating to one of the 50 US states, or the Federal government. This is not a hard task – we probably could have used string/regex, but there’s enough weird corner cases that that would’ve taken longer. So our first attempt was (roughly) something like this:

```plain text
Here's a block of text. One field should be "locality_id", and it should be the ID of one of the 50 states, or federal, using this list:
[{"locality: "Alabama", "locality_id": 1}, {"locality: "Alaska", "locality_id": 2} ... ]
```

This worked sometimes (I’d estimate >98% of the time), but failed enough that we had to dig deeper.

While we were investigating, we noticed that another field, name, was consistently returning the full name of the state…the correct state – even though we hadn’t explicitly asked it to do that.

So we switched to a simple string search on the name to find the state, and it’s been working beautifully ever since.

I think in summary, a better approach would’ve been “You obviously know the 50 states, GPT, so just give me the full name of the state this pertains to, or Federal if this pertains to the US government.”

Why is this crazy? Well, it’s crazy that GPT’s quality and generalization can improve when you’re more vague – this is a quintessential marker of higher-order delegation / thinking.

(Random side note one: GPT was failing most often with the M states — Maryland, Maine, Massachusettes, Michigan — which you might expect of a fundamentally stochastic model.)

(Random side note two: when we asked GPT to choose an ID from a list of items, it got confused a lot less when we sent the list as prettified JSON, where each state was on its own line. I think \n is a stronger separator than a comma.)

Lesson 2: You don’t need langchain. You probably don’t even need anything else OpenAI has released in their API in the last year. Just chat. That’s it.

Langchain is the perfect example of premature abstraction. We started out thinking we had to use it because the internet said so. Instead, millions of tokens later, and probably 3-4 very diverse LLM features in production, and our openai_service file still has only one, 40-line function in it:

```plain text
def extract_json(prompt, variable_length_input, number_retries)
```

The only API we use is chat. We always extract json. We don’t need JSON mode, or function calling, or assistants (though we do all that). Heck, we don’t even use system prompts (maybe we should…). When a gpt-4-turbo was released, we updated one string in the codebase.

This is the beauty of a powerful generalized model – less is more.

Most of the 40 lines in that function are around error handling around OpenAI API’s regular 500s/socket closed (though it’s gotten better, and given their load, it’s not surprising).

There’s some auto-truncating we built in, so we don’t have to worry about context length limits. We have my own proprietary token-length estimator. Here it is:

```plain text
if s.length > model_context_size * 3
  # truncate it!
end
```

It fails in corner cases when there are a LOT of periods, or numbers (the token ratio is < 3 characters / token for those). So there’s another very proprietary try/catch retry logic:

```plain text
if response_error_code == "context_length_exceeded"
   s.truncate(model_context_size * 3 / 1.3)
```

We’ve gotten quite far with this approach, and it’s been flexible enough for our needs.

Lesson 3: improving the latency with streaming API and showing users variable-speed typed words is actually a big UX innovation with ChatGPT.

We thought this was a gimmick, but users react very positively to variable-speed “typed” characters – this feels like the mouse/cursor UX moment for AI.

Lesson 4: GPT is really bad at producing the null hypothesis

“Return nothing if you don’t find anything” – is probably the most error-prone prompting language we came across. Not only does GPT often choose to hallucinate rather than return nothing, it also causes it to just lack confidence a lot, returning blank more often than it should.

Most of our prompts are in the form:

> 

For a time, we had a bug where [block of text] could be empty. The hallucinations were bad. Incidentally, GPT loves to hallucinate bakeries, here are some great ones:

- Sunshine Bakery
- Golden Grain Bakery
- Bliss Bakery
Fortunately, the solution was to fix the bug and not send it a prompt at all if there was no text (duh!). But it’s harder when “it’s empty” is harder to define programmatically, and you actually do need GPT to weigh in.

Lesson 5: “Context windows” are a misnomer – and they are only growing larger for input, not output

Little known fact: GPT-4 may have a 128k token window for input, but it’s output window is still a measly 4k! Calling it a “context window” is confusing, clearly.

But the problem is even worse – we often ask GPT to give us back a list of JSON objects. Nothing complicated mind you: think, an array list of json tasks, where each task has a name and a label.

GPT really cannot give back more than 10 items. Trying to have it give you back 15 items? Maybe it does it 15% of the time.

We originally thought this was because of the 4k context window, but we were hitting 10 items, and it’d only be maybe 700-800 tokens, and GPT would just stop.

Now, you can of course trade in output for input by giving it a prompt, ask for a single task, then give it (prompt + task), ask for the next task, etc. But now you’re playing a game of telephone with GPT, and have to deal with things like Langchain.

Lesson 6: vector databases, and RAG/embeddings are mostly useless for us mere mortals

I tried. I really did. But every time I thought I had a killer use case for RAG / embeddings, I was confounded.

I think vector databases / RAG are really meant for Search. And only search. Not search as in “oh – retrieving chunks is kind of like search, so it’ll work!”, real google-and-bing search. Here’s some reasons why:

1. there’s no cutoff for relevancy. There are some solutions out there, and you can create your own cutoff heuristics for relevancy, but they’re going to be unreliable. This really kills RAG in my opinion – you always risk poisoning your retrieval with irrelevant results, or being too conservative, you miss important results.
1. why would you put your vectors in a specialized, proprietary database, away from all your other data? Unless you are dealing at a google/bing scale, this loss of context absolutely isn’t worth the tradeoff.
1. unless you are doing a very open-ended search, of say – the whole internet – users typically don’t like semantic searches that return things they didn’t directly type. For most applications of search within business apps, your users are domain experts – they don’t need you to guess what they might have meant – they’ll let you know!
It seems to me (this is untested) that a much better use of LLMS for most search cases is to use a normal completion prompt to convert a user’s search into a faceted-search, or even a more complex query (or heck, even SQL!). But this is not RAG at all.

Lesson 7: Hallucination basically doesn’t happen.

Every use case we have is essentially “Here’s a block of text, extract something from it.” As a rule, if you ask GPT to give you the names of companies mentioned in a block of text, it will not give you a random company (unless there are no companies in the text – there’s that null hypothesis problem!).

Similarly — and I’m sure you’ve noticed this if you’re an engineer — GPT doesn’t really hallucinate code – in the sense that it doesn’t make up variables, or randomly introduce a typo in the middle of re-writing a block of code you sent it. It does hallucinate the existence of standard library functions when you ask it to give you something, but again, I see that more as the null hypothesis. It doesn’t know how to say “I don’t know”.

But if your use case is entirely, “here’s the full context of details, analyze / summarize / extract” – it’s extremely reliable. I think you can see a lot of product releases recently that emphasize this exact use case.

So it’s all about good data in, good GPT tokens responses out.

Where do I think all this is heading?

Rather than responding with some long-form post, here’s a quick Q&A:

Are we going to achieve Gen AI?

No. Not with this transformers + the data of the internet + $XB infrastructure approach.

Is GPT-4 actually useful, or is it all marketing?

It is 100% useful. This is the early days of the internet still. Will it fire everyone? No. Primarily, I see this lowering the barrier of entry to ML/AI that was previously only available to Google.

Have you tried Claude, Gemini, etc?

Yeah, meh. Actually in all seriousness, we haven’t done any serious A/B testing, but I’ve tested these with my day to day coding, and it doesn’t feel even close. It’s the subtle things mostly, like intuiting intention.

How do I keep up to date with all the stuff happening with LLMs/AI these days?

You don’t need to. I’ve been thinking a lot about The Bitter Lesson – that general improvements to model performance outweigh niche improvements. If that’s true, all you need to worry about is when GPT-5 is coming out. Nothing else matters, and everything else being released by OpenAI in the meantime (not including Sora, etc, that’s a whooolle separate thing) are basically noise.

So when will GPT-5 come out, and how good will it be?

I’ve been trying to read the signs with OpenAI, as has everyone else. I think we’re going to see incremental improvement, sadly. I don’t have a lot of hope that GPT-5 is going to “change everything”. There are fundamental economic reasons for that: between GPT-3 and GPT-3.5, I thought we might be in a scenario where the models were getting hyper-linear improvement with training: train it 2x as hard, it gets 2.2x better.

But that’s not the case, apparently. Instead, what we’re seeing is logarithmic. And in fact, token speed and cost per token is growing exponentially for incremental improvements.

If that’s the case, there’s some Pareto-optimal curve we’re on, and GPT-4 might be optimal: whereas I was willing to pay 20x for GPT-4 over GPT-3.5, I honestly don’t think I’d pay 20x per token to go from GPT-4 to GPT-5, not for the set of tasks that GPT-4 is used for.

GPT-5 may break that. Or, it may be the iPhone 5 to the iPhone 4. I don’t think that’s a loss!


