---
type: link
source: notion
url: https://www.oneusefulthing.org/p/what-just-happened-what-is-happening
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-05-11T03:11:00.000Z
---

# What just happened, what is happening next

## AI Summary (from Notion)
- Rapid Improvement of AI: Large Language Models (LLMs) are improving at an unprecedented rate, with capabilities doubling every 5 to 14 months.
- Current Models: As of now, three major models exist: Claude 3, GPT-4, and Google’s Gemini, with expectations for models surpassing GPT-4 soon.
- Exploration of Capabilities: Many capabilities of existing AIs remain unexplored, as people often stop experimenting when initial approaches fail.
- Superhuman Performance: AIs are beginning to exceed human performance in specific tasks, including persuasive debates and medical data processing.
- Persuasion Abilities: Research indicates that AIs, particularly GPT-4, can significantly influence human beliefs, raising ethical concerns.
- Real-World Impact: AI shows potential in various fields, such as business and healthcare, suggesting that tasks thought to be uniquely human may soon be automated.
- Rise of Autonomous Agents: AI agents capable of planning and using tools are emerging, representing a shift in how AI can be integrated into organizations.
- Future Implications: The advancements in AI could lead to significant changes in industries, including marketing and job roles, as well as potential misuse in scams and unethical practices.
- Call for Awareness: There is a need for vigilance regarding biases and weaknesses in AI systems as their capabilities grow, and preparation for future changes in professions is essential.

## Content (from Notion)

The current best estimates of the rate of improvement in Large Language Models show capabilities doubling ever 5 to 14 months. This incredibly rapid pace was on my mind as I put the finishing touches on my book (available at every major bookstore and now, with its bestseller status, apparently discounted 33% at Amazon) back at the end of December. Given that I knew it would release in April, I wrote it in a way that would be relatively timeless, but I also had to make a couple forecasts on where the future would be heading. Fortunately, I think I predicted correctly, and, as a result, the book still encompasses the current state-of-the-art. But that doesn’t mean that nothing has changed in the last four months. So, I wanted to go over the last few months of AI and take stock of what we have learned about what AI models can do, and especially, what AI might do soon.

# We Still Don’t Know the Full Capabilities of Current Frontier Models

At the time I finished the book, there was one frontier model, GPT-4. Now have three GPT-4 class models, all of roughly similar abilities but with unique strengths and weaknesses: Claude 3, GPT-4, and Google’s Gemini (confusingly Gemini 1.0 Advanced and Gemini 1.5 Pro are both GPT-4 class models, but Gemini 1.0 Pro is not). While the release of the first models to clearly surpass GPT-4 are expected to occur in the coming months, one thing we have learned is that we have not come close to exhausting the abilities of even existing AIs.

In fact, it is often very hard to know what these models can’t do, because most people stop experimenting when an approach doesn’t work. Yet careful prompting can often make an AI do something that seemed impossible. For example, this weekend, programmer Victor Taelin made a bet. He argued that "GPTs will NEVER solve the A::B problem" because they can’t learn how to reason over new information. He offered $10,000 to anyone who could get an AI to solve the problem in the image below (he called it a “braindead question that most children should be able to read, learn and solve in a minute,” though I am not sure it is that simple, but you should try it.)

Multiple people figured out how to get AI to solve the problem within the day using prompts alone. I had a bit of a similar experience where I could not make an AI solve the New York Times crossword, and, after sharing my belief that this was a hard problem, Prof. Arvind Narayanan showed it was doable by GPT-4.

In fact, even the creators of the LLMs do not really know what these systems are capable of. Here, for example, is a three-page prompt we developed that turns GPT-4 or Claude 3 into a negotiation simulator, complete with grading and integrated lessons (we have a lot more educational prompts coming soon in a new paper, but you can find this one, like our previous prompts, in our prompt library, released under creative commons license or try it as a GPT). We have demonstrated this, and similar prompts, to people within the major AI labs who did not realize their own models were capable of such sophisticated interactions from a prompt alone.

This doesn’t mean the systems are capable of every human task, of course, but merely that it is hard to prove that they don’t do something well from simple experiments. At the same time, there is no single best way to prompt AIs (researchers keep discovering new techniques and approaches), making trying to show that AI can do something dependent on a mix of art, skill, and motivation. And this doesn’t even include the added element of tool use - when you give AI access to things like Google search, the systems can actually outperform humans at fact-checking, an area where AIs without tools are notoriously weak.

# More Signs of “Superhuman Performance” at Human Tasks

Indeed, over the past few months we have begun to see more careful papers indicating that AIs can exceed human performance at very human tasks, a phenomenon some researchers call “superhuman performance.” To be fair, it isn’t exactly clear what “superhuman” performance is where AIs are concerned (better than the average human? better than the best human?) but it at least suggests capabilities that begin to have radical impacts.

Famously, Sam Altman mentioned that AI may be capable of superhuman persuasion in the near future. New research suggests he might be right already.

In a randomized, controlled, pre-registered study GPT-4 was better able to change people’s minds during a conversational debate than other humans, at least when it is given access to personal information about the person it is debating (people given the same information were not more persuasive). The effects were significant: the AI increased the chance of someone changing their mind by 87% over a human debater. This might be why a second paper found that GPT-4 could accomplish a famously difficult conversational task: arguing with conspiracy theorists. That controlled trial found that a three-round debate, with GPT-4 arguing the other side, robustly lowers conspiracy theory beliefs. Even more surprisingly, the effects persist over time, even for true believers.

Lowering conspiratorial beliefs might be a good use of AI persuasion, but the high levels of AI persuasiveness also suggest some concerns about what AIs might be able to talk humans into doing. As Altman wrote, highly persuasive bots “may lead to some very strange outcomes,” which might be an understatement. I suspect major changes in the world of marketing, at a minimum. After all, it is now trivial to build a vending machine that can engage you in discussion and be very persuasive about it.

Persuasion is not the only area that AI competes with humans. In the book, I discuss business, legal, and medical uses for LLMs, and the evidence for the value of AI in these spaces continues to accumulate. AI seem to do all sorts of specialized tasks that it was not necessarily trained for at very high levels. Claude 3, for example, was given this test which was designed to be particularly challenging for AIs. It is really hard for humans as well. PhDs with access to the internet and unlimited time got 34% of the questions outside their specialty right on the exam and typically scored 65%-75% on the questions in their field. Yet Claude 3 gets 60% overall.

These are some of the questions, they were developed for the test and they were kept hidden so they did not appear in training data.

These results are also occurring outside of tests, in real-world settings. A new study in JAMA Internal Medicine finds that AI was better than physicians in processing medical data and doing clinical reasoning on real patient cases. That doesn’t mean that AI can replace doctors, of course, but it does suggest something else that is very important. To quote from one of the paper authors, the research shows “that LLMs are capable of mimicking some of the powerful processes that we use to make diagnoses — processes that, until basically last year, we physicians thought were unique to us.”

I think it is worth paying attention to that conclusion, because you are going to see it in many places: things that we thought were uniquely human a year ago are going to be done by machines in the coming years, often at a “superhuman” level. We need to be ready for that to occur, while also watching out for the biases and weaknesses of these systems that might be hidden by their seemingly impressive abilities (for example, GPT-4 has many biases when asked to evaluate candidates for hiring). Professions that begin to prepare for this future (I like this self-reflective study by professors of data science as an example) will do better than those that ignore the coming change.

Get my book!

# Agents and Everything After

Agents are AI systems given the ability to plan and use tools, allowing them to act autonomously. I mention them in the book but was not expecting them to advance as rapidly as they have. Agents like Devin “the software developer” and open-source alternatives suggest that we are close to a new paradigm of AI use than I thought a few months ago.

I increasingly suspect that agents may also be a key to integrating AIs with organizations, at least in the short term. Organizations are often reluctant to empower their workers to use AI, but agents fit more naturally into the existing structure of organizations. Because you assign them tasks, like humans, they can work as “AI contract workers” who are delegated jobs. Agents also represent the first break away from the chatbot and copilot models for interacting with AI. There is something compelling about assigning a task to an agent like Devin, and then not worrying about it again because you know it is on it and will message you if it has any questions.

But the human-like way in which you interact with agents also suggests bigger changes ahead. I asked the Devin AI agent to go on Reddit and offer to build websites for people. Over the next couple hours, it did that, solving numerous problems along the way, including navigating the complex social rules associated with posting on a Reddit forum.

Devin sets up a plan and asks me questions while quietly doing the work.

Here is what it posted… you can see it pretended to be a person and spontaneously decided to charge for its work! The agent was already starting to respond to some posters and was figuring out ways to help them when I took the posting down (I was worried it would actually start billing people).

This is what Devin posted, the text and nature of the post was entirely decided by the AI.

To be clear, I know that Devin would not have been able to actually complete all of the tasks it was taking on. The system makes mistakes and gets stuck often. It is not yet close to human performance. Devin’s limits are ultimately the capabilities of the GPT-4 class models that power them. If AI development pauses at this level, agents will be useful, but limited in their ability to truly act autonomously. One of the biggest questions about the current state of AI is whether the next generation of models are going to significantly improve over the existing ones. I suspect we will know the answer soon.

If new AIs are much better than current ones, the three threads I have outlined - unclear upper capabilities, “superhuman” abilities in some areas, and autonomous agents - begin to matter a lot. Entrepreneurs can deploy agents as virtual employees, creating large companies with few real people. Criminals can use agents to conduct mass scams, relying on their abilities to convince their marks at low cost. And that is just the start. If these trends continue, superhumanly persuasive vending machines will be one of the least weird consequences of AI.


