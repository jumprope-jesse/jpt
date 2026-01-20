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

## LLM by Simon Willison

*Source: https://llm.datasette.io/en/stable/ - Added: 2026-01-19*
*Blog: https://simonwillison.net/2023/Dec/18/mistral/*
*Related: https://simonwillison.net/tags/llm/*

A command-line tool and Python library for interacting with Large Language Models. Designed with plugin architecture for easy extensibility across local and hosted models. Created by Simon Willison (co-creator of Django).

### Key Features

- **Plugin System** - 19+ plugins for different model providers and local inference engines
- **Multiple Inference Backends** - llama.cpp, GPT4All, MLC, Llamafile support
- **Unified Interface** - Single CLI for local models (Mistral, Mixtral) and APIs (OpenAI, Anthropic, Mistral)
- **Template System** - Custom prompt templates and saved prompts
- **Conversation History** - SQLite-backed conversation logging with full result storage
- **Embeddings** - Generate and store embeddings for semantic search (via llm-clip and other plugins)
- **Interactive Chat** - `llm chat` command for conversational sessions
- **Python Library** - Full Python API alongside CLI tool

### Installation

```bash
# Core tool (via pipx recommended - avoids package conflicts)
pipx install llm
# OR via pip
pip install llm

# Set API key for OpenAI
llm keys set openai
# Paste your key when prompted

# Install plugins as needed
llm install llm-llama-cpp    # llama.cpp backend
llm install llm-gpt4all      # GPT4All backend (easiest for local models)
llm install llm-mlc          # MLC backend
llm install llm-mistral      # Mistral API
llm install llm-replicate    # Replicate API
llm install llm-anyscale-endpoints  # Anyscale
llm install llm-openrouter   # OpenRouter
llm install llm-clip         # Image search/embeddings
```

### Basic Usage

```bash
# Run a prompt
llm "Ten fun names for a pet pelican"

# System prompt against a file
cat myfile.py | llm -s "Explain this code"

# Interactive chat
llm chat -m chatgpt

# Local model with plugin
llm -m orca-mini-3b-gguf2-q4_0 'What is the capital of France?'
```

### Running Mistral Models Locally

**Option 1: llama.cpp (most flexible)**

```bash
# Install plugin
llm install llm-llama-cpp

# Install llama-cpp-python (Apple Silicon)
CMAKE_ARGS="-DLLAMA_METAL=on" pip install --force-reinstall \
  --no-cache-dir llama-cpp-python

# Download Mixtral 8x7B GGUF (36GB Q6_K quantization)
# From TheBloke: https://huggingface.co/TheBloke/Mixtral-8x7B-Instruct-v0.1-GGUF

# Run with path to downloaded GGUF
llm -m gguf -o path mixtral-8x7b-instruct-v0.1.Q6_K.gguf \
  '[INST] what are some ways to reduce latency in AI applications [/INST]'
```

**Option 2: GPT4All (easiest)**

```bash
# Install and run - model downloads automatically
llm install llm-gpt4all
llm -m mistral-7b-instruct 'explain rust ownership'
```

**Option 3: MLC**

```bash
# Follow plugin README for installation
llm install llm-mlc
llm -m mistral-7b-v0.2 'write a haiku about compilers'
```

### Running Mistral API Models

Mistral AI's hosted API offers three tiers:
- **Mistral-tiny** - Mistral 7B (renamed)
- **Mistral-small** - Mixtral 8x7B (renamed)
- **Mistral-medium** - Larger proprietary model (beats GPT-3.5 on benchmarks)

```bash
# Install Mistral plugin
llm install llm-mistral

# Set API key
llm keys set mistral
# <paste API key>

# Run models
llm -m mistral-tiny 'explain transformers'
llm -m mistral-small 'write production-ready error handling'
llm -m mistral-medium 'design a distributed caching system'
```

### Benchmark Performance (Mistral Medium vs GPT-3.5)

| Benchmark | GPT-3.5 | Mistral Small | Mistral Medium |
|-----------|---------|---------------|----------------|
| MMLU (57 subjects) | 70.0% | 70.6% | **75.3%** |
| HellaSwag (10-shot) | 85.5% | 86.7% | **88.0%** |
| ARC Challenge (25-shot) | 85.2% | 85.8% | **89.9%** |
| WinoGrande (5-shot) | 81.6% | 81.2% | **88.0%** |
| MBPP (pass@1) | 52.2% | 60.7% | **62.3%** |
| GSM-8K (5-shot) | 57.1% | 58.4% | **66.7%** |
| MT Bench | 8.32 | 8.30 | **8.61** |

Mistral Medium's 8.61 MT Bench score places it between GPT-3.5 (8.32) and GPT-4 (higher).

### Alternative API Providers

Since Mistral 7B and Mixtral 8x7B are Apache 2 licensed, many providers offer hosted versions:

**Replicate:**
```bash
llm install llm-replicate
llm keys set replicate
llm replicate add mistralai/mistral-7b-v0.1
llm -m replicate-mistralai-mistral-7b-v0.1 'complete this: the three laws of robotics are'
```

**Anyscale Endpoints:**
```bash
llm install llm-anyscale-endpoints
llm keys set anyscale-endpoints
llm -m mistralai/Mixtral-8x7B-Instruct-v0.1 'explain kubernetes pods'
llm -m mistralai/Mistral-7B-Instruct-v0.1 'write a dockerfile for a python app'
```

**OpenRouter:**
```bash
llm install llm-openrouter
llm keys set openrouter
llm -m openrouter/mistralai/mistral-7b-instruct 'three reasons to use rust'
```

OpenRouter was offering Mistral/Mixtral free ($0.00/1M tokens) at time of article—great for initial experiments.

### Llamafile Integration

Llamafile packages LLMs as single executables with built-in OpenAI-compatible API server:

```bash
# Download and start Mixtral llamafile
curl -L -o mixtral.llamafile \
  https://huggingface.co/Mozilla/Mixtral-8x7B-Instruct-v0.1-llamafile/resolve/main/mixtral-8x7b-instruct-v0.1.Q5_K_M-server.llamafile

chmod 755 mixtral.llamafile
./mixtral.llamafile  # Starts server on localhost:8080

# Configure LLM to use it
# Add to ~/Library/Application Support/io.datasette.llm/extra-openai-models.yaml:
- model_id: llamafile
  model_name: llamafile
  api_base: "http://localhost:8080/v1"

# Use it
llm -m llamafile 'explain why llamafile is interesting'
```

The `llamafile` alias works with any llamafile model running on port 8080.

### Plugin Development

LLM's plugin system makes it easy to add support for new models:

1. **Local models** - Implement model loading and inference interface
2. **Remote APIs** - Wrap API calls with LLM plugin structure
3. **Custom prompts** - Define prompt templates for specific model formats

See the [plugin author tutorial](https://llm.datasette.io/en/stable/plugins/tutorial-model-plugin.html) and existing plugins for examples.

**Resources:**
- Documentation: https://llm.datasette.io/en/stable/
  - Setup guide
  - Plugins directory (19+ plugins)
  - Python API reference
  - Prompt templates
  - Embeddings guide
  - Changelog
- Blog posts: https://simonwillison.net/tags/llm/
- Discord: #llm channel
- GitHub: https://github.com/simonw/llm

### Why It's Useful

- **Unified CLI** - Single interface for dozens of models (local and hosted)
- **Easy local inference** - Run Mistral/Mixtral on Mac with simple commands
- **Plugin ecosystem** - Community-driven support for new models
- **Conversation logging** - Built-in SQLite storage for chat history
- **Cost-effective experimentation** - Mix free providers (OpenRouter) with local models
- **Template system** - Save and reuse complex prompts
- **Llamafile support** - Use llamafile's portable executables seamlessly

### Architecture Notes

Mistral's **Mixtral 8x7B** is the first truly convincing open Sparse Mixture of Experts (SMoE) implementation. GPT-4 is rumored to use MoE architecture, and Mixtral demonstrates this approach can work at smaller scales.

The model uses 8 expert networks but only activates ~2 per token, giving 47B total parameters with 13B active per token—balancing capability with inference speed.

---

## Datasette & Datasette Enrichments

*Source: https://simonwillison.net/2023/Dec/1/datasette-enrichments/ - Added: 2026-01-19*
*Related: https://datasette.io/*
*Creator: Simon Willison (Django co-creator)*

A tool for exploring and publishing data, with a plugin system for "enrichments" that can augment data in-place.

### What Is Datasette?

Datasette is an open-source tool for exploring and publishing datasets. It provides an instant web UI for SQLite databases, with powerful querying, visualization, and sharing capabilities.

**Core features:**
- Instant web UI for SQLite databases
- No-code SQL query interface
- CSV upload and import
- Data visualization (maps, charts)
- API endpoint generation
- Publishing and sharing capabilities

### Datasette Enrichments Framework

**Enrichments** are plugins that can transform or augment data in database tables. Each enrichment runs against selected rows and can:
- Transform existing data (e.g., normalize addresses)
- Fetch data from external APIs (e.g., geocoding)
- Apply LLM prompts to generate new data
- Extract structured information from text

**Key innovation:** Run code against batches of rows with results written back to the database, all through a web UI.

### Installation & Quick Start

```bash
# Install Datasette
pip install datasette

# Install enrichment plugins
pip install datasette-enrichments
pip install datasette-enrichments-gpt
pip install datasette-enrichments-opencage
pip install datasette-enrichments-jinja
pip install datasette-enrichments-re2

# Start Datasette with a database
datasette mydata.db

# Or upload CSV through web UI at http://localhost:8001
```

### Key Enrichment Plugins

**datasette-enrichments-gpt** - OpenAI integration

Three main capabilities:
1. **Execute prompts against column data** - Generate new content from existing rows
2. **GPT-4 Vision against image URLs** - Describe images stored in URL columns
3. **Extract structured JSON** - Pull structured data from unstructured text

```python
# Example 1: Extract people and dates from museum descriptions
# Model: gpt-4-turbo
# Prompt: "{{ description }}"
# System: "Return JSON: {\"people\": ..., \"years\": ...}
#          Each person should be {\"name\": \"...\", \"bio\": \"One line bio\"}
#          Each year should be {\"year\": 1893, \"description\": \"What happened\"}"
# Result stored in 'extracted' column as JSON

# Example 2: GPT-4 Vision on photos
# Prompt: "describe this photo"
# Input: {{ photo_url }}
# Result: "The image shows a large Bigfoot statue standing in what appears
#          to be a small museum or gift shop. The statue is brown and furry..."

# Example 3: Generate haikus about museums
# Prompt: "Write a haiku about {{ museum_name }}"
# Result: Three-line poem stored in new column
```

**datasette-enrichments-opencage** - Geocoding

OpenCage is geocoder-friendly for data storage (many APIs prohibit long-term storage of results). Built on open data and financially supports open source projects.

```python
# Workflow:
# 1. Upload CSV with address column
# 2. Select rows to geocode
# 3. Configure OpenCage enrichment:
#    - Input template: "{{ Locations }}, San Francisco, California"
#    - Optionally store full JSON response
# 4. Run enrichment → creates lat/lng columns
# 5. datasette-cluster-map automatically displays map

# Result: 2,084 film locations geocoded and displayed on interactive map
```

**datasette-enrichments-jinja** - Template execution

Execute arbitrary Jinja templates against each row. Uses Jinja sandbox for safety (not cryptographically secure, but prevents accidental damage).

```python
# Example: Combine multiple columns
# Template: "{{ first_name }} {{ last_name }} ({{ year }})"
# Result: "John Smith (1923)"

# Example: Conditional formatting
# Template: "{% if score > 80 %}Excellent{% elif score > 60 %}Good{% else %}Needs improvement{% endif %}"

# Example: List processing
# Template: "{{ tags | join(', ') | upper }}"
```

**datasette-enrichments-re2** - Regular expressions

Four distinct modes for regex operations:

```python
# Mode 1: Search and replace
# Input: "version 1.2.3 released"
# Pattern: r"version (\d+\.\d+\.\d+)"
# Replace: "v$1"
# Result: "v1.2.3 released"

# Mode 2: Extract first match to new column
# Input: "Build #12345 succeeded"
# Pattern: r"#(\d+)"
# Result: "12345" in new 'build_number' column

# Mode 3: Extract all matches to JSON array
# Input: "Tags: python, data, api"
# Pattern: r"\w+"
# Result: ["Tags", "python", "data", "api"]

# Mode 4: Named capture groups → multiple columns
# Input: "version 2.7.1"
# Pattern: r"version (?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)"
# Result: Creates three columns: major=2, minor=7, patch=1
```

### API Key Management

Enrichments that need API keys (GPT, OpenCage) support two modes:
1. **Plugin secrets** - Configure once in Datasette metadata, use everywhere
2. **Per-run entry** - Prompted each time you run the enrichment (good for occasional use or shared instances)

### Real-World Use Cases

**Example 1: Film Location Mapping**
1. Upload "Film Locations in San Francisco" CSV
2. Run OpenCage geocoding on address column
3. Instantly see map visualization (via datasette-cluster-map plugin)
4. Query: "Find all films shot within 1 mile of Golden Gate Park"

**Example 2: Museum Content Generation**
1. Table of 110 museums with descriptions
2. Run GPT enrichment to extract {people, years} JSON from each description
3. Run separate GPT enrichment to generate haikus
4. Run GPT-4 Vision to describe museum photos
5. Result: Structured metadata + generated content alongside original data

**Example 3: Data Normalization**
1. Table with messy address formats
2. Use Jinja enrichment to normalize: "{{ street | title }}, {{ city | upper }}, {{ state }}"
3. Use regex enrichment to extract zip codes to dedicated column
4. Geocode normalized addresses

### Building Custom Enrichments

Enrichments are Python plugins using asyncio for parallel execution.

**Plugin structure:**
```python
from datasette import hookimpl
from datasette_enrichments import Enrichment

@hookimpl
def register_enrichments():
    return [MyEnrichment()]

class MyEnrichment(Enrichment):
    name = "My Custom Enrichment"
    slug = "my-enrichment"

    async def get_config_form(self, datasette, db, table):
        # Return HTML form for configuration
        pass

    async def enrich_batch(self, rows, config):
        # Process batch of rows
        # Return dict mapping row IDs to new column values
        pass
```

**Best practices:**
- Use HTTPX for async HTTP requests (parallel API calls)
- Batch operations when possible (e.g., 50 rows per API request)
- Return clear error messages for individual row failures
- Support both creating new columns and updating existing ones

**Development resources:**
- [Developing a new enrichment guide](https://datasette.io/plugins/enrichments)
- Example plugins: datasette-enrichments-gpt, datasette-enrichments-opencage
- Discord #enrichments channel for discussion
- GitHub: https://github.com/simonw/datasette

### Why It's Useful

**No-code data transformation:**
- Non-programmers can apply complex transformations
- Visual interface for selecting rows and configuring operations
- Immediate feedback (run on sample first, then full dataset)

**LLM integration without code:**
- Apply GPT models to tabular data through UI
- Extract structured data from unstructured text at scale
- Vision model support for image analysis

**Data augmentation in-place:**
- Transform data directly in your database
- No export/import cycle
- Results versioned with database

**Geocoding friendly:**
- OpenCage allows storing results (unlike Google/Mapbox which prohibit it in ToS)
- One-time API cost for long-term data storage
- Built-in map visualization

**Async performance:**
- Parallel API calls for fast batch processing
- Progress tracking for long-running operations
- Interruptible (stop mid-batch, results already saved)

### Integration with Broader Datasette Ecosystem

Enrichments complement Datasette's existing features:

**Visualization plugins:**
- **datasette-cluster-map** - Auto-displays maps when lat/lng columns exist
- **datasette-vega** - Charts and graphs
- **datasette-leaflet** - Custom map layers

**Data import:**
- CSV upload through UI
- JSON import
- SQL database connection

**Workflow:**
- Upload CSV → Run enrichment → Visualize → Share public link
- Query with SQL → Select subset → Enrich → Re-query enriched data

**Publishing:**
- `datasette publish` → Deploy to Vercel/Heroku/Cloud Run
- Share enriched datasets with others
- API endpoints auto-generated for all tables

### Architecture Notes

**Plugin design principles:**
- Each enrichment is a separate plugin (composable)
- Consistent UI/UX across all enrichments
- Sandboxed execution (Jinja) or external APIs (GPT, OpenCage)
- Async-first for I/O-bound operations (network requests)

**Performance:**
- Enrichments run in batches (not row-by-row)
- Progress tracking with estimated completion time
- Failed rows logged separately (don't block batch)
- Can retry failed rows independently

**Safety:**
- Jinja sandbox prevents code execution (mostly safe)
- API keys stored securely or entered per-session
- Dry-run mode: preview on first N rows before full batch
- Undo: keep original columns, write to new columns

**Video demo:** https://simonwillison.net/2023/Dec/1/datasette-enrichments/ (shows geocoding + GPT enrichments in action)

### Datasette Cloud (Hosted SaaS)

*Source: https://www.datasette.cloud/ - Added: 2026-01-19*

Datasette Cloud is the official hosted version of Datasette—upload CSV/SQLite files and get instant web app + API without deployment.

**Key features:**
- **No setup required** - Upload CSVs or SQLite databases through web UI
- **Zero coding** - Full-featured data exploration without writing code
- **Automatic backups** - Data automatically backed up and secured
- **Access control** - Granular permissions for team data sharing
- **Same features as self-hosted** - Faceting, filtering, sorting, searching, enrichments
- **API endpoints** - Instant REST API for all uploaded data

**Workflow:**
1. Upload CSV or SQLite file via web UI
2. Datasette Cloud creates instant web interface
3. Share with team (configurable access controls)
4. Run enrichments (GPT, geocoding, etc.) on data
5. Export results or consume via API

**Pricing:**
- Currently in preview/early access
- Request access at https://www.datasette.cloud/

**When to use:**
- Quick data exploration without local setup
- Sharing datasets with non-technical stakeholders
- Teams that need collaborative data analysis
- Projects requiring instant API for CSV data

**When to use self-hosted Datasette instead:**
- Full control over infrastructure
- Custom plugin development
- Large datasets (cost considerations)
- Air-gapped or compliance-restricted environments

---

## RecurseChat (Mac GUI)

*Source: https://recurse.chat/ - Added: 2026-01-19*

Native Mac app for running local LLMs with zero configuration. Good option for non-technical users or when you want a polished GUI without terminal setup.

### Key Features

- **Local-first, offline capable** - No config setup, works entirely offline
- **Full-text search** - Fast search across thousands of messages
- **ChatGPT history import** - Continue conversations with local AI
- **Multi-model sessions** - Chat with multiple models in one conversation
- **Multi-modal** - Chat with images using LLaVA model
- **macOS App Sandbox** - Secure and private, no data leaves device
- **Customizable** - AI personality, appearance, use your own GGUF models

### When to Use

**RecurseChat over CLI tools:**
- Want macOS-native GUI without terminal
- Prefer desktop app UX (search, history, persistence)
- Need to import ChatGPT history
- Multi-model conversations

**CLI tools over RecurseChat:**
- Script automation and pipelines
- Need specific model configurations
- Integration with other tools
- Prefer command-line workflow

### Comparison with Other Local LLM Options

| Feature | RecurseChat | Ollama | LLM CLI | Llamafile |
|---------|-------------|--------|---------|-----------|
| Mac GUI | ✅ Native | ❌ (web only) | ❌ | ❌ (web) |
| Offline | ✅ | ✅ | Depends | ✅ |
| Multi-model chat | ✅ | ❌ | ❌ | ❌ |
| Custom GGUF | ✅ | ✅ | ✅ | ❌ |
| API/scripting | ❌ | ✅ | ✅ | ✅ |
| ChatGPT import | ✅ | ❌ | ❌ | ❌ |

---

## Ollama Python & JavaScript Libraries

*Source: https://ollama.ai/blog/python-javascript-libraries - Added: 2026-01-19*

Official libraries for integrating applications with Ollama. Mirror the features of the Ollama REST API with minimal code.

### Installation

**Python:**
```bash
pip install ollama
```

**JavaScript:**
```bash
npm install ollama
```

### Quick Start

**Python:**
```python
import ollama

response = ollama.chat(model='llama2', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(response['message']['content'])
```

**JavaScript:**
```javascript
import ollama from 'ollama'

const response = await ollama.chat({
  model: 'llama2',
  messages: [{ role: 'user', content: 'Why is the sky blue?' }],
})
console.log(response.message.content)
```

### Key Features

Both libraries support Ollama's full feature set:

**Streaming:**
```python
for chunk in chat('mistral', messages=messages, stream=True):
  print(chunk['message']['content'], end='', flush=True)
```

**Multi-modal (images):**
```python
with open('image.png', 'rb') as file:
  response = ollama.chat(
    model='llava',
    messages=[{
      'role': 'user',
      'content': 'What is strange about this image?',
      'images': [file.read()],
    }],
  )
```

**Text completion:**
```python
result = ollama.generate(
  model='stable-code',
  prompt='// A c function to reverse a string\n',
)
print(result['response'])
```

**Creating custom models:**
```python
modelfile = '''
FROM llama2
SYSTEM You are mario from super mario bros.
'''

ollama.create(model='example', modelfile=modelfile)
```

**Custom client (specify host):**
```python
ollama = Client(host='my.ollama.host')
```

### Resources

- Python library: https://github.com/ollama/ollama-python
- JavaScript library: https://github.com/ollama/ollama-js
- Community libraries: Available for Dart, Swift, C#, Java, PHP, Rust, and more

### Why It's Useful

- Minimal code integration with local LLMs
- Full streaming support for real-time responses
- Multi-modal capabilities (text + images)
- Custom model creation with modelfiles
- Native Python and JavaScript support (no REST API boilerplate)
- Works with locally-hosted Ollama instance (no API keys needed)

---
