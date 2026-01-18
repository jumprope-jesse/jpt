# LLM CLI Tools

Command-line tools for interacting with LLM providers.

## llms.py (ServiceStack)

*Source: https://github.com/ServiceStack/llms - Added: 2026-01-18*

Lightweight CLI and OpenAI-compatible server for querying multiple LLM providers. Single Python file with minimal dependencies.

### Key Features

- **Multi-Provider Support** - OpenRouter, Ollama, Anthropic, Google, OpenAI, Grok, Groq, Qwen, Z.ai, Mistral
- **Auto-Routing** - Requests automatically routed to available providers; failures retry on next provider
- **OpenAI-Compatible Server** - Run local server at `http://localhost:PORT/v1/chat/completions`
- **Multi-Modal** - Supports images, audio, and file (PDF) inputs
- **160+ Models** - Supports over 160 different LLMs across providers
- **Web UI** - Simple ChatGPT-like interface to access all configured LLMs

### Installation

```bash
pip install llms-py
```

### Quick Start

```bash
# Set API keys
export OPENROUTER_API_KEY="..."
export GROQ_API_KEY="..."

# Enable providers (free tier providers)
llms --enable openrouter_free google_free groq

# Enable paid providers
llms --enable openrouter anthropic google openai mistral grok qwen

# Start UI and server on port 8000
llms --serve 8000

# CLI usage
llms "What is the capital of France?"
llms -m gemini-2.5-pro "Explain quantum computing"
llms -s "You are a coding assistant" "How do I reverse a string in Python?"
```

### Multi-Modal Inputs

```bash
# Images (vision models)
llms --image screenshot.png "What's in this image?"
llms -m gemini-2.5-flash --image chart.png "Analyze this chart"

# Audio
llms --audio meeting.wav "Summarize this meeting"
llms -m gpt-4o-audio-preview --audio interview.mp3 "Extract main topics"

# Files (PDFs)
llms --file policy.pdf "Summarize key changes"
llms -m gpt-5 --file report.pdf "Extract action items"
```

### Configuration

Config stored at `~/.llms/llms.json`. Key commands:

```bash
# List enabled providers and models
llms --list
llms ls

# List specific provider
llms ls ollama
llms ls google anthropic

# Enable/disable providers
llms --enable openrouter anthropic
llms --disable ollama

# Set default model
llms --default grok-4

# Initialize config
llms --init

# Update to latest version
llms --update
```

### Server Mode

```bash
# Start OpenAI-compatible server
llms --serve 8000

# Client usage
curl -X POST http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "kimi-k2", "messages": [{"role": "user", "content": "Hello!"}]}'
```

### Provider Configuration

Providers require API keys in environment variables:

| Provider | Env Variable | Notes |
|----------|--------------|-------|
| OpenRouter | `OPENROUTER_API_KEY` | Free tier available, 100+ models |
| Anthropic | `ANTHROPIC_API_KEY` | Claude models |
| Google | `GOOGLE_API_KEY` | Gemini models |
| OpenAI | `OPENAI_API_KEY` | GPT models |
| Grok | `GROK_API_KEY` | X.AI models |
| Groq | `GROQ_API_KEY` | Fast inference |
| Qwen | `DASHSCOPE_API_KEY` | Alibaba Cloud |
| Z.ai | `ZAI_API_KEY` | GLM models |
| Mistral | `MISTRAL_API_KEY` | Mistral/Codestral |
| Ollama | (none) | Local, auto-discovers models |

### Model Routing

Requests route to first available provider supporting the model. Define cheaper/free providers first to save costs:

```json
{
  "providers": {
    "groq": { "enabled": true, ... },
    "openrouter_free": { "enabled": true, ... },
    "openrouter": { "enabled": true, ... }
  }
}
```

### Why It's Useful

- Single tool to query all LLM providers
- Free-tier-first routing saves costs
- Local server mode for integration with other tools
- Automatic failover between providers
- Multi-modal support (images, audio, PDFs)
- Lightweight single-file implementation

---
