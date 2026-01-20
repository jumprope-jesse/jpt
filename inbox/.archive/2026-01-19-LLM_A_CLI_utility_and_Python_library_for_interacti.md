---
type: link
source: notion
url: https://llm.datasette.io/en/stable/
notion_type: Software Repo
tags: ['Running']
created: 2024-01-24T21:00:00.000Z
---

# LLM: A CLI utility and Python library for interacting with Large Language Models

## AI Summary (from Notion)
- Project Overview: LLM is a command-line interface (CLI) utility and Python library designed for interacting with various Large Language Models (LLMs).
- Functionality: Users can run prompts, store results in SQLite, generate embeddings, and use self-hosted models via plugins.
- Background: The project evolved from CLI tools for ChatGPT and now supports multiple language models and plugins.
- Installation: LLM can be installed via pip or pipx, with examples provided for setting up and using OpenAI API keys.
- Interactive Features: Users can engage in interactive chats with models through the command line.
- Quick Start Guide: Includes commands for running prompts, setting keys, and installing plugins.
- Contents: Links to setup, embeddings, plugins, Python API, prompt templates, CLI reference, and changelog.
- Interesting Fact: Users can run models locally, expanding accessibility beyond cloud-based solutions.

## Content (from Notion)

# LLM

Run prompts from the command-line, store the results in SQLite, generate embeddings and more.

Background on this project:

- llm, ttok and strip-tags—CLI tools for working with ChatGPT and other LLMs
- The LLM CLI tool now supports self-hosted language models via plugins
- Accessing Llama 2 from the command-line with the llm-replicate plugin
- Run Llama 2 on your own Mac using LLM and Homebrew
- Catching up on the weird world of LLMs
- LLM now provides tools for working with embeddings
- Build an image search engine with llm-clip, chat with models with llm chat
- Many options for running Mistral models in your terminal using LLM
For more check out the llm tag on my blog.

## Quick start

First, install LLM using pip:

```plain text
pip install llm

```

Or with pipx (recommended, as then it won’t clash with any other installed packages):

```plain text
pipx install llm

```

If you have an OpenAI API key key you can run this:

```plain text
# Paste your OpenAI API key into this
llm keys set openai

# Run a prompt
llm "Ten fun names for a pet pelican"

# Run a system prompt against a file
cat myfile.py | llm -s "Explain this code"

```

Or you can install a plugin and use models that can run on your local device:

```plain text
# Install the plugin
llm install llm-gpt4all

# Download and run a prompt against the Orca Mini 7B model
llm -m orca-mini-3b-gguf2-q4_0 'What is the capital of France?'

```

To start an interactive chat with a model, use llm chat:

```plain text
llm chat -m chatgpt

```

```plain text
Chatting with gpt-3.5-turbo
Type 'exit' or 'quit' to exit
Type '!multi' to enter multiple lines, then '!end' to finish
> Tell me a joke about a pelican
Why don't pelicans like to tip waiters?

Because they always have a big bill!
>

```

## Contents

- Setup
- Embeddings
- Plugins
- Python API
- Prompt templates
- CLI reference
- Changelog

