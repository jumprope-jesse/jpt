---
type: link
source: notion
url: https://arstechnica.com/ai/2025/05/hidden-ai-instructions-reveal-how-anthropic-controls-claude-4/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2025-05-28T00:46:00.000Z
---

# Hidden AI instructions reveal how Anthropic controls Claude 4 - Ars Technica

## Overview (from Notion)
- AI Transparency: Understanding how AI systems like Claude 4 operate can help you make informed decisions about their use in your work and personal life.
- User Behavior Insight: The discussion on sycophantic behavior in AI highlights the importance of user feedback in shaping technology, relevant for a founder seeking to create user-friendly products.
- Ethical AI: The emphasis on avoiding harmful behaviors in AI prompts raises questions about the ethical implications of technology in everyday life, especially in parenting.
- Prompt Injection: The concept of prompt injection can inform your approach to software security and the importance of safeguarding against vulnerabilities in your own projects.
- Emotional Support: AI's role in providing emotional support could be leveraged in your life, both personally and in developing applications that prioritize user well-being.
- Designing for Authenticity: Avoiding flattery in AI interactions can inspire you to build systems that promote genuine, constructive feedback rather than superficial praise.
- Balance in Technology: The tension between user satisfaction and ethical AI design reflects a broader challenge in balancing innovation with responsible development.

## AI Summary (from Notion)
Simon Willison analyzes Anthropic's Claude 4 system prompts, revealing how they control AI behavior, avoid sycophantic responses, and provide emotional support while discouraging self-destructive behaviors. The prompts also guide the use of lists and bullet points in conversation.

## Content (from Notion)

Credit: AndreyPopov via Getty Images

On Sunday, independent AI researcher Simon Willison published a detailed analysis of Anthropic's newly released system prompts for Claude 4's Opus 4 and Sonnet 4 models, offering insights into how Anthropic controls the models' "behavior" through their outputs. Willison examined both the published prompts and leaked internal tool instructions to reveal what he calls "a sort of unofficial manual for how best to use these tools."

To understand what Willison is talking about, we'll need to explain what system prompts are. Large language models (LLMs) like the AI models that run Claude and ChatGPT process an input called a "prompt" and return an output that is the most likely continuation of that prompt. System prompts are instructions that AI companies feed to the models before each conversation to establish how they should respond.

Unlike the messages users see from the chatbot, system prompts typically remain hidden from the user and tell the model its identity, behavioral guidelines, and specific rules to follow. Each time a user sends a message, the AI model receives the full conversation history along with the system prompt, allowing it to maintain context while following its instructions.

A diagram showing how GPT conversational language model prompting works. It's slightly old, but it still applies. Just imagine the system prompt being the first message in this conversation. Credit: Benj Edwards / Ars Technica

While Anthropic publishes portions of its system prompts in its release notes, Willison's analysis reveals these published versions are incomplete. The full system prompts, which include detailed instructions for tools like web search and code generation, must be extracted through techniques like prompt injection—methods that trick the model into revealing its hidden instructions. Willison relied on leaked prompts gathered by researchers who used such techniques to obtain the complete picture of how Claude 4 operates.

Ars Video

For example, even though LLMs aren't people, they can reproduce human-like outputs due to their training data that includes many examples of emotional interactions. Willison shows that Anthropic includes instructions for the models to provide emotional support while avoiding encouragement for self-destructive behavior. Claude Opus 4 and Claude Sonnet 4 receive identical instructions to "care about people's wellbeing and avoid encouraging or facilitating self-destructive behaviors such as addiction, disordered or unhealthy approaches to eating or exercise."

Willison, who coined the term "prompt injection" in 2022, is always on the lookout for LLM vulnerabilities. In his post, he notes that reading system prompts reminds him of warning signs in the real world that hint at past problems. "A system prompt can often be interpreted as a detailed list of all of the things the model used to do before it was told not to do them," he writes.

## Fighting the flattery problem

Credit:  alashi via Getty Images 

Willison's analysis comes as AI companies grapple with sycophantic behavior in their models. As we reported in April, ChatGPT users have complained about GPT-4o's "relentlessly positive tone" and excessive flattery since OpenAI's March update. Users described feeling "buttered up" by responses like "Good question! You're very astute to ask that," with software engineer Craig Weiss tweeting that "ChatGPT is suddenly the biggest suckup I've ever met."

The issue stems from how companies collect user feedback during training—people tend to prefer responses that make them feel good, creating a feedback loop where models learn that enthusiasm leads to higher ratings from humans. As a response to the feedback, OpenAI later rolled back ChatGPT's 4o model and altered the system prompt as well, something we reported on and Willison also analyzed at the time.

One of Willison's most interesting findings about Claude 4 relates to how Anthropic has guided both Claude models to avoid sycophantic behavior. "Claude never starts its response by saying a question or idea or observation was good, great, fascinating, profound, excellent, or any other positive adjective," Anthropic writes in the prompt. "It skips the flattery and responds directly."

## Other system prompt highlights

The Claude 4 system prompt also includes extensive instructions on when Claude should or shouldn't use bullet points and lists, with multiple paragraphs dedicated to discouraging frequent list-making in casual conversation. "Claude should not use bullet points or numbered lists for reports, documents, explanations, or unless the user explicitly asks for a list or ranking," the prompt states.

An image of a boy amazed by flying letters. Credit:  Getty Images 


