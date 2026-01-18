---
type: link
source: notion
url: https://github.com/ServiceStack/llms
notion_type: Software Repo
tags: ['Running']
created: 2025-11-03T14:53:00.000Z
---

# GitHub - ServiceStack/llms: LLM Client, Server API and UI

## Overview (from Notion)
- Leverage the lightweight CLI and multi-provider support to optimize your coding projects, saving time and resources.
- Utilize the OpenAI-compatible server for seamless integration into your development workflow, enhancing productivity.
- Embrace the flexibility of querying multiple LLM providers to find the best solutions for coding challenges or project planning.
- The environmentally friendly aspects of the tool align with a growing trend toward sustainability in tech, appealing to personal values.
- Explore the potential for educational applications—using LLMs to assist in teaching your kids coding or other subjects in an engaging way.
- Consider the unique collaboration opportunities this technology presents for startups, enabling rapid prototyping and development.
- Alternate views could include concerns about over-reliance on AI tools—balancing technology with traditional problem-solving skills remains essential.

## AI Summary (from Notion)
Lightweight CLI and server for querying multiple Large Language Model (LLM) providers, supporting local and API models. Features include a simple command-line interface, server mode for OpenAI-compatible HTTP requests, image and audio processing capabilities, and customizable chat templates. Configuration management allows easy enabling/disabling of providers, and it supports over 160 different LLMs. Users can set API keys, run the UI, and utilize various models for diverse tasks, including text, image, and audio inputs.

## Content (from Notion)

# llms.py

Lightweight CLI and OpenAI-compatible server for querying multiple Large Language Model (LLM) providers.

Configure additional providers and models in llms.json

- Mix and match local models with models from different API providers
- Requests automatically routed to available providers that supports the requested model (in defined order)
- Define free/cheapest/local providers first to save on costs
- Any failures are automatically retried on the next available provider
## Features

- Lightweight: Single llms.py Python file with single aiohttp dependency
- Multi-Provider Support: OpenRouter, Ollama, Anthropic, Google, OpenAI, Grok, Groq, Qwen, Z.ai, Mistral
- OpenAI-Compatible API: Works with any client that supports OpenAI's chat completion API
- Configuration Management: Easy provider enable/disable and configuration management
- CLI Interface: Simple command-line interface for quick interactions
- Server Mode: Run an OpenAI-compatible HTTP server at http://localhost:{PORT}/v1/chat/completions
- Image Support: Process images through vision-capable models
- Audio Support: Process audio through audio-capable models
- Custom Chat Templates: Configurable chat completion request templates for different modalities
- Auto-Discovery: Automatically discover available Ollama models
- Unified Models: Define custom model names that map to different provider-specific names
- Multi-Model Support: Support for over 160+ different LLMs
## llms.py UI

Simple ChatGPT-like UI to access ALL Your LLMs, Locally or Remotely!

Read the Introductory Blog Post.

## Installation

```plain text
pip install llms-py
```

## Quick Start

### 1. Set API Keys

Set environment variables for the providers you want to use:

```plain text
export OPENROUTER_API_KEY="..."
```

### 2. Enable Providers

Enable the providers you want to use:

```plain text
# Enable providers with free models and free tiers
llms --enable openrouter_free google_free groq

# Enable paid providers
llms --enable openrouter anthropic google openai mistral grok qwen
```

### 3. Run UI

Start the UI and an OpenAI compatible API on port 8000:

```plain text
llms --serve 8000
```

Launches the UI at http://localhost:8000 and an OpenAI Endpoint at http://localhost:8000/v1/chat/completions.

### 4. Use llms.py CLI

```plain text
llms "What is the capital of France?"
```

## Configuration

The configuration file llms.json is saved to ~/.llms/llms.json and defines available providers, models, and default settings. Key sections:

### Defaults

- headers: Common HTTP headers for all requests
- text: Default chat completion request template for text prompts
### Providers

Each provider configuration includes:

- enabled: Whether the provider is active
- type: Provider class (OpenAiProvider, GoogleProvider, etc.)
- api_key: API key (supports environment variables with $VAR_NAME)
- base_url: API endpoint URL
- models: Model name mappings (local name → provider name)
## Command Line Usage

### Basic Chat

```plain text
# Simple question
llms "Explain quantum computing"

# With specific model
llms -m gemini-2.5-pro "Write a Python function to sort a list"
llms -m grok-4 "Explain this code with humor"
llms -m qwen3-max "Translate this to Chinese"

# With system prompt
llms -s "You are a helpful coding assistant" "How do I reverse a string in Python?"

# With image (vision models)
llms --image image.jpg "What's in this image?"
llms --image https://example.com/photo.png "Describe this photo"

# Display full JSON Response
llms "Explain quantum computing" --raw
```

### Using a Chat Template

By default llms uses the defaults/text chat completion request defined in llms.json.

You can instead use a custom chat completion request with --chat, e.g:

```plain text
# Load chat completion request from JSON file
llms --chat request.json

# Override user message
llms --chat request.json "New user message"

# Override model
llms -m kimi-k2 --chat request.json
```

Example request.json:

```plain text
{
  "model": "kimi-k2",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user",   "content": ""}
  ],
  "temperature": 0.7,
  "max_tokens": 150
}
```

### Image Requests

Send images to vision-capable models using the --image option:

```plain text
# Use defaults/image Chat Template (Describe the key features of the input image)
llms --image ./screenshot.png

# Local image file
llms --image ./screenshot.png "What's in this image?"

# Remote image URL
llms --image https://example.org/photo.jpg "Describe this photo"

# Data URI
llms --image "data:image/png;base64,$(base64 -w 0 image.png)" "Describe this image"

# With a specific vision model
llms -m gemini-2.5-flash --image chart.png "Analyze this chart"
llms -m qwen2.5vl --image document.jpg "Extract text from this document"

# Combined with system prompt
llms -s "You are a data analyst" --image graph.png "What trends do you see?"

# With custom chat template
llms --chat image-request.json --image photo.jpg
```

Example of image-request.json:

```plain text
{
    "model": "qwen2.5vl",
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": ""
                    }
                },
                {
                    "type": "text",
                    "text": "Caption this image"
                }
            ]
        }
    ]
}
```

Supported image formats: PNG, WEBP, JPG, JPEG, GIF, BMP, TIFF, ICO

Image sources:

- Local files: Absolute paths (/path/to/image.jpg) or relative paths (./image.png, ../image.jpg)
- Remote URLs: HTTP/HTTPS URLs are automatically downloaded
- Data URIs: Base64-encoded images (data:image/png;base64,...)
Images are automatically processed and converted to base64 data URIs before being sent to the model.

### Vision-Capable Models

Popular models that support image analysis:

- OpenAI: GPT-4o, GPT-4o-mini, GPT-4.1
- Anthropic: Claude Sonnet 4.0, Claude Opus 4.1
- Google: Gemini 2.5 Pro, Gemini Flash
- Qwen: Qwen2.5-VL, Qwen3-VL, QVQ-max
- Ollama: qwen2.5vl, llava
Images are automatically downloaded and converted to base64 data URIs.

### Audio Requests

Send audio files to audio-capable models using the --audio option:

```plain text
# Use defaults/audio Chat Template (Transcribe the audio)
llms --audio ./recording.mp3

# Local audio file
llms --audio ./meeting.wav "Summarize this meeting recording"

# Remote audio URL
llms --audio https://example.org/podcast.mp3 "What are the key points discussed?"

# With a specific audio model
llms -m gpt-4o-audio-preview --audio interview.mp3 "Extract the main topics"
llms -m gemini-2.5-flash --audio interview.mp3 "Extract the main topics"

# Combined with system prompt
llms -s "You're a transcription specialist" --audio talk.mp3 "Provide a detailed transcript"

# With custom chat template
llms --chat audio-request.json --audio speech.wav
```

Example of audio-request.json:

```plain text
{
    "model": "gpt-4o-audio-preview",
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "input_audio",
                    "input_audio": {
                        "data": "",
                        "format": "mp3"
                    }
                },
                {
                    "type": "text",
                    "text": "Please transcribe this audio"
                }
            ]
        }
    ]
}
```

Supported audio formats: MP3, WAV

Audio sources:

- Local files: Absolute paths (/path/to/audio.mp3) or relative paths (./audio.wav, ../recording.m4a)
- Remote URLs: HTTP/HTTPS URLs are automatically downloaded
- Base64 Data: Base64-encoded audio
Audio files are automatically processed and converted to base64 data before being sent to the model.

### Audio-Capable Models

Popular models that support audio processing:

- OpenAI: gpt-4o-audio-preview
- Google: gemini-2.5-pro, gemini-2.5-flash, gemini-2.5-flash-lite
Audio files are automatically downloaded and converted to base64 data URIs with appropriate format detection.

### File Requests

Send documents (e.g. PDFs) to file-capable models using the --file option:

```plain text
# Use defaults/file Chat Template (Summarize the document)
llms --file ./docs/handbook.pdf

# Local PDF file
llms --file ./docs/policy.pdf "Summarize the key changes"

# Remote PDF URL
llms --file https://example.org/whitepaper.pdf "What are the main findings?"

# With specific file-capable models
llms -m gpt-5               --file ./policy.pdf   "Summarize the key changes"
llms -m gemini-flash-latest --file ./report.pdf   "Extract action items"
llms -m qwen2.5vl           --file ./manual.pdf   "List key sections and their purpose"

# Combined with system prompt
llms -s "You're a compliance analyst" --file ./policy.pdf "Identify compliance risks"

# With custom chat template
llms --chat file-request.json --file ./docs/handbook.pdf
```

Example of file-request.json:


