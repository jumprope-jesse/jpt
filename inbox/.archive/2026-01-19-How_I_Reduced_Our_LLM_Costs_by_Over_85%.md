---
type: link
source: notion
url: https://jellypod.ai/blog/how-I-reduced-llm-costs
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-03-08T04:23:00.000Z
---

# How I Reduced Our LLM Costs by Over 85%

## AI Summary (from Notion)
- Cost Challenges: Building AI applications can be expensive, especially with models like GPT-4 costing significantly per token.
- Reliability Issues: Many AI applications currently lack reliability, often failing to provide consistent outputs.
- Redundancy in AI Interaction: The need for redundancy and error handling when working with non-deterministic models is emphasized.
- Backend Redesign: The author redesigned their application architecture (Jellypod) to improve output quality and reduce costs.
- Merging Topics: The system was designed to recognize and merge similar topics from multiple input documents for more coherent output.
- High Initial Costs: The initial architecture led to skyrocketing API call costs (O(n log n)).
- OpenPipe Tool: The author discovered OpenPipe, which allows fine-tuning of open-source models effectively.
- Significant Cost Reduction: By fine-tuning a Mistral 7B model, the author reduced costs by 88%, bringing inference costs down dramatically.
- Output Quality Maintained: The fine-tuned model's output quality matched that of GPT-4 based on evaluations and customer feedback.
- Architecture Consideration: The importance of considering output reliability and costs when building AI applications is stressed.
- Learning Experience: The author reflects on their learning journey and encourages others to think critically about architecture before starting AI projects.

## Content (from Notion)

Cover Image for How I Reduced Our LLM Costs by Over 85%

With AI apps popping up everywhere, it’s fair to think building one is both easy and cheap.

Unfortunately, you’d be (mostly) wrong.

I’m not saying it’s hard per se, but as of this writing, gpt-4-turbo costs $0.01/$0.03 per 1000 input/output tokens. This can quickly add up if you’re building a complex AI workflow.

Yes, you could use less expensive, worse performing models, like GPT 3.5 or an open-source one like Llama, stuff everything into one API call with excellent prompt engineering, and hope for the best. But this probably won’t turn out that great. This type of approach doesn’t really work in production—at least not yet with the current state of AI.

It could give you the right answer 90% or even 99% of the time. But that one time it decides to go off the rails, it’s really frustrating. As a developer and/or business, you know you must never break a user’s experience. It might be okay for a toy app or prototype but not for a production-grade application you charge for.

Imagine if Salesforce or any other established software company said its reliability was only one or two nines. That would be insane. No one would use it.

But this is the state of most AI applications today. They’re unreliable.

## AI isn’t a Universal Function

The non-deterministic nature of LLMs forces us to be more thoughtful about how we write our code. We should not just “hope” that an LLM will always correctly respond. We need to build redundancy and proper error handling. For some reason, many builders forget everything they learned about software engineering and treat AI like some magical universal function that doesn’t fail.

It’s not there yet.

To fix this limitation, we must write code that only interacts with AI when absolutely necessary—that is, when a system needs some sort of “human-level” analysis of unstructured data. Subsequently, whenever possible, we must force the LLM to return references to information (i.e., a pointer) instead of the data itself.

When I recognized these two things, I had to redesign the backend architecture of my personal software business completely.

## Rearchitecting Jellypod

For context, I started an app called Jellypod. It enables users to subscribe to email newsletters and get a daily summary of the most important topics from all of them as a single podcast.

This seems pretty simple on the outside—and the MVP honestly was. The app would just process each email individually, summarize it, convert it to speech, and stitch all the audio together, side-by-side, into a daily podcast.

The output was fine, but it needed to be better.

If two different newsletters discussed the same topic, the “podcast” would talk about it twice, not realizing we had already mentioned it. You could say, “Well, why don’t you just stuff all the newsletter content into one big LLM call to summarize everything?”

Well, that’s what I tried at first.

And it failed. Miserably.

Even with an extremely detailed prompt using all the best practices, I couldn’t guarantee that the LLM would always detect the most important topics, summarize everything, and consistently create an in-depth output. Also, the podcast always needed to be ~10 minutes long.

So I went back to the drawing board. How can I make this system better? And yes, we’re getting to the cost reduction part - don’t worry!

## Defining the Requirements

Jellypod must be able to process any number of input documents (newsletters) and create an output that always includes the top ten most important topics across all those inputs. If two subparts of any input are about the same topic, we should recognize that and merge the sections into one topic.

For example, if the Morning Brew has a section about US Elections and the Daily Brief also has a section on the current state of US Politics, they should be merged. I’ll skip over how I determined a similarity threshold (i.e., should two topics be merged or remain separate).

## Exploding Costs

I built on top of a few different approaches outlined in papers written by the LangChain community to semantic chunk and organize everything in a almost deterministic way.

But this was INSANELY expensive. The number of API calls grew at a rate of O(n log n), with n being the number of input chunks from all newsletters.

So, I had a dilemma. Do I keep this improved and more expensive architecture or throw it down the drain?

I decided to keep it and figure out how to reduce costs.

## Reducing Costs

That’s when I discovered a tool called OpenPipe that allows you to fine-tune open-source models almost too easily. It looked legit and was backed by YCombinator, so I gave it a try.

I swapped out the OpenAI SDK with their SDK (a drop-in replacement), which passed all my LLM API calls to OpenAI but recorded all inputs and outputs. This created unique datasets for each of my prompts, which I could use to fine-tune a cheaper open-source model.

After about a week of recording Jellypod’s LLM calls, I had about 50,000 rows of data. And with a few clicks, I fine-tuned a Mistral 7B model for each LLM call.

I replaced GPT-4 with the new fine-tuned model.

And it reduced the costs by 88%.

The cost of inference dropped from $10 per 1M input tokens to $1.20. And cost per output token dropped from $30 to $1.60.

I was blown away. I could now run Jellypod’s new architecture for approximately the same cost as the MVP’s trivial approach. I even confirmed that the fine-tuned Mistral output quality was just as high as GPT-4 by a series of evals and in-app customer feedback.

By redesigning the system to only use AI for the smallest unit of work it’s actually needed for, I could confidently deploy a fine-tuned model as a drop-in replacement for GPT 4. And by prompting to return pointers to data instead of the data itself, I could ensure data integrity while reducing the number of output tokens consumed.

## In Conclusion

If you’re considering building an AI application, I would encourage you to take a step back and think about your architecture’s output reliability and costs. What happens if the LLM doesn’t answer your prompt in the right way? Can you prompt the model to return data identifiers instead of raw data? And, is it possible to swap GPT-4 with a cheaper, fine-tuned model?

I wish I had these insights when I started, but hey, you live and learn.

I hope you found at least some parts of this interesting! I thought there were enough learnings to share. Feel free to reach out if you’re curious about the details.


