---
type: link
source: notion
url: https://www.oneusefulthing.org/p/freeing-the-chatbot
notion_type: Software Repo
tags: ['Running']
created: 2024-05-11T02:38:00.000Z
---

# Freeing the chatbot - by Ethan Mollick - One Useful Thing

## AI Summary (from Notion)
- Chatbot Limitations: Current interactions with AI primarily occur through chatbots, which can be inefficient due to their lack of memory and context retention.
- Emergence of AI Devices: Dedicated AI devices are being developed, such as the Rabbit R1, Meta Ray-Ban smart glasses, Plaud, and AI-in-a-Box, each offering unique ways to interact with AI beyond traditional chat interfaces.
- Integration with Phones: Personal AI use is expected to center around smartphones, leveraging local AI capabilities while connecting to more powerful models online.
- Copilots and Agents: AI systems are evolving into copilots (task-specific AIs) and agents (autonomous AIs that can plan and execute tasks), representing a shift away from synchronous chatbot interactions.
- Future of AI Interaction: The potential for AIs to interact with users in real-world contexts (like using cameras to assess situations) suggests a move towards more intuitive and natural forms of AI assistance.
- Concerns About AI: While AI technology presents exciting opportunities, there are risks regarding user understanding of AI capabilities and potential collusion among AI agents in market scenarios.
- Ubiquitous Intelligence: The text envisions a future where AI is seamlessly integrated into daily life, allowing for “intelligence on demand” that enhances productivity and user experience.

## Content (from Notion)

For the last year and a half, the primary way that most people have experienced LLMs has been through chatbots. But when you think about it, chatbots are an odd way to interact with an AI. It is as if the only way for us to do work is through texting an intern… except you are texting a different intern in every chat, one who forgets everything you had previously discussed, and whose memory starts to fail after just a couple of pages of text.

I don’t think text-based chatbots are going away, but they are increasingly going to be only one way in which we talk to increasingly ubiquitous AIs. And that is going to change how, and when, we use AI overall.

# AI devices

I now have four dedicated AI devices, and, while none of them are completely successful, they do serve to illustrate what happens when you start to remove AI from the chatbot interface. (I am going to link to the devices and others below, but I bought all of them myself and, as always, I don’t take any money from any AI lab or product company)

I am not normally someone who reviews gadgets, so please forgive the bad photography

The little orange box is the one that has caused the most recent discussion and controversy online. It is a Rabbit R1, a $200 AI device that is so blindingly orange that it is hard to describe. If you want a detailed review of the Rabbit experience, you can look elsewhere, but I am happy to give you a non-detailed one: it has a swiveling camera and an unsatisfying scroll wheel and is fun to use and yet mostly not that useful. The Rabbit is designed to let you talk to a LLM (and show it pictures). It gives you fast, pretty solid answers that feel a bit like every other ChatGPT-3.5 class LLM’s response. Eventually, it is supposed to do a lot of other things, but the software isn’t there yet.

Just a year ago, the Rabbit R1 would have seemed miraculous—a tiny device providing a direct link to an AI with vast knowledge of the world. The problem is that I already have a device like that: my phone. There, I can access all three frontier models (Gemini Ultra, GPT-4, and Claude 3 Opus) in all of their capabilities through either their own apps or Poe, as well as models built for research (Perplexity), models optimized for chat (Pi) and even models that generate movies or songs (through Suno and Runway). I don’t think anyone is giving up their phone anytime soon, so I am a little confused about the utility of dedicated phone-like AI devices on top of them. (Though the Rabbit was distinctive enough that the people sitting next to us at a restaurant knew what it was and asked me about it)

Page 1 of my iPhone’s LLM folder

So, let’s move on to the next device, the Meta Ray-Ban smart glasses. They look a lot like regular Wayfarer sunglasses, and weigh just a bit more, but they have built-in speakers, microphones, and a camera (with lights that turn on when it is recording, to warn others they are being photographed). It connects to Meta’s Llama LLMs through a Bluetooth connection to my phone. I don’t use it for social media, but I do find it interesting as an AI device. In many ways, it does the exact same tricks as the Rabbit R1 - using the glasses, an LLM can talk to you and look at what you are seeing to comment on it. But the fact that I don’t have to look at a screen to interact with a multimodal AI feels quite different than the R1. It still is mostly a party trick. But as AI models get better and multimodal reasoning becomes faster, I can imagine glasses and voice being a reasonable mode for interacting with a personal AI.

Asking the Smart Glasses what I am seeing (this is right, by the way)

This theme of providing a unique set of specialized inputs and outputs for smarter LLMs to work with can also be seen in the tiny card in the image, a Plaud. Plaud does one thing - it records conversations and then uploads them to GPT-4 to get a transcript. With the transcript, GPT-4 can summarize or extract information from what has been recorded. The Plaud doesn’t talk back or have a screen, but, like the Meta glasses, it has value because it helps use the inherent capabilities of AI in the real-world, beyond the chat box.

The final device is the least capable and least useful, but, in many ways, the most interesting. It is the AI-in-a-Box - a small computer with a screen that is capable of running the not-very-good Orca Mini 3b LLM. It can do live translations and captioning, and, as you can see in the image, provides mediocre responses to prompts. Nothing about it is that useful. So why is it interesting? It is not connected to the internet; it runs my own personal LLM with the assurance of absolute control and privacy (not that I have confided any secrets to Orca 3b). With the growing capabilities of freely available open-source AI systems, including large models that are better than GPT-3.5 (and soon, maybe, GPT-4) and small models that can be run directly on phones, there is a new space for specialized, private AIs of which the AI-in-a-Box is a precursor.

All of these AI devices are flawed, but they suggest both opportunities for specialized devices that extend LLM abilities into the world (like Plaud) and those that give us new ways to interact with AIs (like the glasses). They also show the power of conversation as an AI interface. If you haven’t tried it, I suggest either experimenting with Pi, a voice-focused AI, or else creating a shortcut to active ChatGPT Plus’s excellent voice conversation mode on your phone. You will quickly see that, even if the devices are flawed, the idea of interacting with AI via voice is very powerful.

I have been surprised at how many more uses I find for AI now that I can call up a voice chat by pushing the side button on my iPhone.

Given these experiences, I suspect that personal AI use will actually be centered on our phone, though not necessarily through apps. Small, local AIs running on your phone’s hardware (something both Microsoft and Apple have demonstrated) can already do much better than Siri at basic assistant tasks, and they can connect to more powerful AIs over the network to handle more difficult requests. For most people, this will be all the AI they need. They can make a request of their local phone AI, and the system will decide how much computing power to put into it. It is a model of ubiquitous AI that does not actually require most users to change habits or devices.

Get my book!

# Copilots and agents

For work, another way that AI has escaped the chat box is through the growth of copilots. These are AIs narrowly focused to help with a specialized task or application. Microsoft is all-in on this approach with Copilot, formerly Bing, a version of ChatGPT Plus (and the only free way to access a GPT-4 class model right now, if you use it in purple “creative” mode). But Microsoft also has a Word Copilot that helps you write and a PowerPoint Copilot that makes presentations and a Windows Copilot that does Windows things (I am not quite sure what to use it for, to be honest) and many others. While they vary in utility, they make using AI easy. Instead of prompting a chatbot, the AI just completes a task for you.

A little work, a lot of output from Word Copilot

I have written about the large implications of Copilot before. Their value, and risk, comes from the fact that they make AI easy to use, but in doing so, may distance users from understanding the underlying LLM's capabilities and limitations. Using a chatbot directly gives you more control (and helps you spot errors better), but requires experimentation and experience. Those trade-offs need to be managed, as do their wider implications for writing and work. There definitely seems to be a role for copilots, but I think they may just be a bridge to agents.

If you have been reading this newsletter, you have certainly seen me discuss AI agents. Agents are AI systems that are given the capability to plan and use tools. If you give them a goal (“launch a webpage explaining agents”) they autonomously plan and execute on that goal, coming back to you only when the task is done of if they have questions. I have generally been demonstrating Devin, an early GPT-4 powered agent with a big feature set, but now there are open source agents available, like Devika. Devika is a lot more limited than Devin (for now), but shows that the agent idea is spreading. OpenAI is explicitly working towards making agents work better in future GPT models.

Devika at work (it doesn’t work that well yet, though)

Agents might represent the clearest example yet of freeing AI from the chat box. Rather than doing synchronous real-time interactions, where you send a command and wait for a response, the agent just acts on your behalf behind the scenes, executing on your goals. Agents can be set off to code a website for you, plan trips, get you those concert tickets, or help make sure that your business is charging the right price given changing market conditions. There are a lot of open questions about how a world of autonomous agents may work, but it is likely to have a lot of unexpected outcomes. For example, consider the pricing agent I mentioned. This paper found that AI agents are great at figuring out what price a merchant should charge, but when it is possible to establish an oligarchy, multiple LLM agents spontaneously collude on pricing to the detriment of customers!

# Intelligence in the Air

Of course, current AI systems remain limited, and working with agents or AI devices remains frustrating. However, the pieces for a very different future of ubiquitously available “intelligence on demand” are already falling into place. AIs can already see video in near-real time and make strong inferences based on images. AIs can talk in realistic voices and respond to human speech with minimal delays. Assuming future advances in LLM capabilities (which is not assured), this will all come together in a new form of AI.

Why limit yourself to a chatbox when you have these abilities? It is far more natural to ask for something and have your personal AI agent “look around” through a camera to assess the situation and make a plan. Then it can decide what resources are needed to solve the problem, and then get to work following instructions. It is not even hard to imagine this assistant-focused future - this was the dream for Alexa or Siri, even if they could never achieve it.

Even if AI progress plateaus soon, we are still going to see an explosion of different approaches to working with the AIs we do have. The Rabbit R1, as flawed as it is, represents one bold vision for the future of AI, as does the Ray-Ban glasses. They show that the nature of AI interaction is not going to be confined to chat boxes anymore but move into the world around us, an invisible but increasingly ubiquitous presence - for better or worse.


