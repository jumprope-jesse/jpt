---
type: link
source: notion
url: https://github.com/llmware-ai/llmware/tree/main/examples/SLIM-Agents
notion_type: Software Repo
tags: ['Running']
created: 2024-04-07T02:22:00.000Z
---

# llmware/examples/SLIM-Agents at main · llmware-ai/llmware · GitHub

## AI Summary (from Notion)
- SLIM Overview: SLIMs (Structured Language Instruction Models) are specialized 1-3B parameter LLMs designed for generating structured outputs that can be used in multi-step workflows on local CPUs.
- New Releases: Recently released SLIM models include slim-extract, slim-summarize, slim-xsum, slim-sa-ner, slim-boolean, and slim-tags-3b.
- Examples: The repository provides various ready-to-run examples demonstrating the use of SLIM models, including:
- Document clustering and multi-faceted automated analysis.
- Function-calling agents that generate structured reports.
- Text-to-SQL conversions for natural language queries.
- Model Packages: Each SLIM model comes in two versions: a Pytorch/Huggingface FP16 model and a quantized "tool" for fast inference.
- Setup Requirements: Easy installation of llmware >=0.2.6 is required; no special setup is needed.
- Supported Platforms: Compatible with Mac M1, Windows, and Linux (preferably Ubuntu 22), with a minimum of 16 GB RAM.
- Educational Resources: Introductory videos and detailed examples are available to help users get started.
- Key Features: SLIM models can handle various tasks, such as named entity recognition, sentiment analysis, and generating topics or ratings.
- Note on Availability: The document includes links to model cards and additional resources for users interested in more information about SLIM functionalities.

## Content (from Notion)

# 🚀 Start Building Multi-Model Agents Locally on a Laptop 🚀

What is a SLIM?

SLIMs are Structured Language Instruction Models, which are small, specialized 1-3B parameter LLMs, finetuned to generate structured outputs (Python dictionaries and lists, JSON and SQL) that can be handled programmatically, and stacked together in multi-step, multi-model Agent workflows - all running on a local CPU.

New SLIMS Just released - check out slim-extract, slim-summarize, slim-xsum, slim-sa-ner, slim-boolean and slim-tags-3b

Check out the new examples below marked with ⭐

🔥🔥🔥 Web Services & Function Calls (code) 🔥🔥🔥

Check out the Intro videos

SLIM Intro Video

There are 16 SLIM models, each delivered in two packages - a Pytorch/Huggingface FP16 model, and a

quantized "tool" designed for fast inference on a CPU, using LLMWare's embedded GGUF inference engine. In most cases, we would recommend that you start with the "tools" version of the models.

Getting Started

We have several ready-to-run examples in this repository:

For information on all of the SLIM models, check out LLMWare SLIM Model Collection.

Models List

If you would like more information about any of the SLIM models, please check out their model card:

- extract - extract custom keys - slim-extract & slim-extract-tool
- summary - summarize function call - slim-summary & slim-summary-tool
- xsum - title/headline function call - slim-xsum & slim-xsum-tool
- ner - extract named entities - slim-ner & slim-ner-tool
- sentiment - evaluate sentiment - slim-sentiment & slim-sentiment-tool
- topics - generate topic - slim-topics & slim-topics-tool
- sa-ner - combo model (sentiment + named entities) - slim-sa-ner & slim-sa-ner-tool
- boolean - provides a yes/no output with explanation - slim-boolean & slim-boolean-tool
- ratings - apply 1 (low) - 5 (high) rating - slim-ratings & slim-ratings-tool
- emotions - assess emotions - slim-emotions & slim-emotions-tool
- tags - auto-generate list of tags - slim-tags & slim-tags-tool
- tags-3b - enhanced auto-generation tagging model - slim-tags-3b & slim-tags-3b-tool
- intent - identify intent - slim-intent & slim-intent-tool
- category - high-level category - slim-category & slim-category-tool
- nli - assess if evidence supports conclusion - slim-nli & slim-nli-tool
- sql - convert text into sql - slim-sql & slim-sql-tool
You may also want to check out these quantized 'answer' tools, which work well in conjunction with SLIMs for question-answer and summarization:

- bling-stablelm-3b-tool - 3b quantized RAG model - bling-stablelm-3b-gguf
- bling-answer-tool - 1b quantized RAG model - bling-answer-tool
- dragon-yi-answer-tool - 6b quantized RAG model - dragon-yi-answer-tool
- dragon-mistral-answer-tool - 7b quantized RAG model - dragon-mistral-answer-tool
- dragon-llama-answer-tool - 7b quantized RAG model - dragon-llama-answer-tool
Set up

No special setup for SLIMs is required other than to install llmware >=0.2.6, e.g., pip3 install llmware.

Platforms:

- Mac M1, Mac x86, Windows, Linux (Ubuntu 22 preferred, supported on Ubuntu 20 +)
- RAM: 16 GB minimum
- Python 3.9, 3.10, 3.11 (note: not supported on 3.12 yet)
- llmware >= 0.2.6 version
### Let's get started! 🚀


