---
type: link
source: notion
url: https://spreadsheets-are-all-you-need.ai/index.html
notion_type: Software Repo
tags: ['Running']
created: 2024-03-15T04:17:00.000Z
---

# Spreadsheets are all you need.ai – A low-code way to learn AI

## AI Summary (from Notion)
- Spreadsheets as a Learning Tool: The project "Spreadsheets-are-all-you-need" offers a low-code introduction to understanding Large Language Models (LLMs) using Excel.

- Target Audience: Designed for a diverse group, including technical executives, marketers, developers transitioning to machine learning, and AI policymakers.

- Learning through Implementation: The project implements the forward pass of GPT-2 entirely within Excel, demonstrating the foundational architecture used by many modern LLMs like ChatGPT and Google's Bard.

- Resources and Tutorials:
- Offers video lessons covering key concepts of LLMs, such as tokenization and the architecture of GPT-2.
- Provides a hands-on experience with the Excel implementation to help users visualize and understand how LLMs work.

- Accessibility and Downloads: The Excel sheet is available for download, but users are cautioned about its size and potential performance issues, especially on Mac.

- Limitations:
- The implementation is designed for small workloads only, with limited context length and capabilities compared to full LLMs.
- The project initially started on Google Sheets but switched to Excel due to size constraints.

- FAQs Addressed:
- Explains why it can’t function like ChatGPT, highlighting the differences in context length and training methods.
- Discusses the play on words in the project’s name, referencing the influential "Attention Is All You Need" paper that introduced the Transformer architecture.

- Community Engagement: Encourages users to report bugs on GitHub and engage with the creator on social media for further inquiries.

## Content (from Notion)

## Watch the demo

Watch the 10 min demo from the Seattle AI Tinkerers meetup

### Sophisticated yet simple

Spreadsheets-are-all-you-need is a low-code introduction to the details behind today’s Large Language Models (LLMs) that’s ideal for:

- Technical executives, marketers, and product managers
- Developers and scientists transitioning into machine learning
- AI policy makers and ethicists
If you can understand a spreadsheet, then you can understand AI!

### Learn from a real LLM

Spreadsheets-are-all-you-need implements the forward pass of GPT2 (an ancestor of ChatGPT that was state of the art only a few years ago) entirely in Excel using standard spreadsheet functions.

This same Transformer architecture is the foundation for OpenAI’s ChatGPT, Anthropic’s Claude, Google’s Bard/Gemini, Meta’s Llama, and many other LLMs.

Yesterday I knew nothing about how AI works. But today that changed thanks to these two awesome resources 👇@karpathy's Intro to Large Language Models: https://t.co/gcWxKwdI0U@ianand's Spreadsheets-are-all-you-need: https://t.co/E9LIZDOQ9A

I'm constantly consuming…

## More lessons to come! Get notified!

Future videos will walk through more details on the internals of modern AI. Subscribe below to get notified about new tutorials and updates.

Email Address

## Watch the lessons

Enjoyed a video? Share it with a friend!

### Lesson 1: Demystifying GPT with Excel

In this 10-minute video we kick things off by walking through the high-level architecture of GPT-2 and witnessing each phase of the Transformer come to life in an Excel spreadsheet.

### Lesson 2: Byte Pair Encoding & Tokenization

In this lesson we dive into the first phase of GPT, the tokenization phase and the Byte Pair Encoding (BPE) algorithm used in models like ChatGPT. We cover

- Detailed walkthrough of the BPE algorithm, including its learning phase and application in language data tokenization.
- Spreadsheet Simulation: A hands-on demonstration of the GPT-2’s tokenization process via a spreadsheet model.
- Limitations and Alternatives: Discussion on the challenges of BPE and a look at other tokenization methods.
### Extra: An end-to-end walk through of the Excel sheet

This is a high level walk through of the Excel implementation. It is primarily geared to those who already understand Transformers and want to know how the standard architecture is mapped to the spreadsheet.

## Try it yourself

### Downloading

The sheet is available as an xlsb (Excel binary) file in the Releases section of the github repo. You should be able to download and run this file in Excel for Mac or PC.

### Using

If you’re quickly trying to orient yourself to the spreadsheet this walk through video may be helpful though it is not oriented to beginners. For beginners, it’s recommended to start with the lesson videos.

Please realize the implementation is just enough to run very small workloads:

- Full GPT2 small (124M parameters) model including byte pair encoding, embeddings, multi-headed attention, and multi-layer perceptron stages
- Inference/forward pass only (no training)
- Context is limited to 10 tokens in length
- 10 characters per word limit
- Zero temperature output only
This sheet is very big. Unfortunately, it is not unusual for Excel to lock up (but only on a Mac) while using this spreadsheet. It is highly recommended to use the manual calculation mode in Excel and the Windows version of Excel (either on a Windows directory or via Parallels on a Mac).

### Issues

Bugs are not out of the question. Please file issues on Github

### Contact

@ianand on Twitter

ianand/spreadsheets-are-all-you-need on Github

## FAQ

### What about Google Sheets?

This project actually started on Google Sheets but the full 124M model was too big and switched to Excel. I’m still exploring ways to make this work in Google Sheets but it is unlikely to fit into a single file as it can with Excel.

### Why can’t I chat with it like ChatGPT? It doesn’t match the output of ChatGPT?

Aside from the minuscule context length, it also lacks the instruction tuning and reinforcement learning from human feedback (RLHF) that turn a large language model into a chatbot.

### Why is it called Spreadsheets-are-all-you-need

The name is a play on the title of the famous Attention Is All You Need paper which first described the Transformer machine learning architecture that underlies ChatGPT, Claude, Bard, and many of the latest Generative AI tools.


