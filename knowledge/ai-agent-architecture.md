# AI Agent Architecture Patterns

## MetaGPT: Multi-Agent Software Company Simulation

*Source: [MetaGPT GitHub](https://github.com/geekan/MetaGPT) - Added: 2026-01-18*

MetaGPT is a multi-agent framework that simulates a software company by assigning specialized roles to different LLM agents. ICLR 2024 oral presentation (top 1.2%), ranked #1 in LLM-based Agent category.

### Core Concept

Takes a single-line requirement and outputs comprehensive deliverables:
- User stories and competitive analysis
- Requirements and data structures
- APIs and documentation

Internally assigns roles: product managers, architects, project managers, engineers. Emphasizes SOPs (Standard Operating Procedures) for agent collaboration.

### Quick Start

```bash
pip install --upgrade metagpt
metagpt --init-config  # creates ~/.metagpt/config2.yaml
```

Config example (`~/.metagpt/config2.yaml`):
```yaml
llm:
  api_type: "openai"  # or azure / ollama / open_llm
  model: "gpt-4-turbo-preview"
  base_url: "https://api.openai.com/v1"
  api_key: "YOUR_API_KEY"
```

### Usage

CLI:
```bash
metagpt "Create a 2048 game"  # outputs to ./workspace
```

Library:
```python
from metagpt.software_company import generate_repo, ProjectRepo
repo: ProjectRepo = generate_repo("Create a 2048 game")
```

Data Interpreter (for data science tasks):
```python
from metagpt.roles.di.data_interpreter import DataInterpreter
di = DataInterpreter()
await di.run("Run data analysis on sklearn Iris dataset, include a plot")
```

### Key Features (as of v0.7.0)

- Assign different LLMs to different roles
- Data Interpreter for real-world data science problems
- Serialization support
- Incremental development
- Multi-language support

---

## Microsoft AutoGen: Multi-Agent Conversation Framework

*Source: [AutoGen GitHub](https://github.com/microsoft/autogen) - Added: 2026-01-18*

AutoGen is Microsoft's framework for building LLM applications using multiple agents that converse to solve tasks. Developed with Penn State and University of Washington. Achieved #1 on GAIA benchmark.

### Core Concept

Enables multi-agent conversations where customizable, conversable agents:
- Communicate with each other to solve complex tasks
- Seamlessly integrate human participation
- Operate in various modes combining LLMs, human inputs, and tools

### Quick Start

```bash
pip install pyautogen  # Python 3.8 - 3.12
```

### Basic Example

```python
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")

assistant = AssistantAgent("assistant", llm_config={"config_list": config_list})
user_proxy = UserProxyAgent(
    "user_proxy",
    code_execution_config={"work_dir": "coding", "use_docker": False}
)

# Initiates automated chat between agents
user_proxy.initiate_chat(
    assistant,
    message="Plot a chart of NVDA and TESLA stock price change YTD."
)
```

### Key Features

- **Multi-agent conversations**: Agents communicate to solve tasks collaboratively
- **Customization**: Choose LLMs, human input modes, and tools per agent
- **Human-in-the-loop**: Seamless human participation when needed
- **Enhanced LLM inference**: API unification, caching, error handling, multi-config inference
- **Code execution**: Agents can write and execute code (Docker recommended)

### When to Use

Best for research-oriented projects and conversational agent workflows. Compare to MetaGPT (role-based simulation) or CrewAI (task-focused crews) depending on your use case.

---

## Browser-Based Data Management for Agents

*Source: [We Gave Our Browser Agent a 3MB Data Warehouse](https://100x.bot/a/we-gave-our-browser-agent-a-3mb-data-warehouse) via 100X.Bot - Added: 2026-01-18*

### The Problem

Traditional browser-based AI agents struggle with data management when scraping or collecting information from multiple sources. The standard answer of "just use a JSON array" fails at complexity, not performance:

- V8 can iterate 5,000 JSON objects in milliseconds
- But reconciling data from different sources in JavaScript means reinventing database logic
- You end up writing hash maps to simulate JOINs, complex reduce functions for moving averages
- Heavy libraries just for fuzzy string matching

**Key insight:** Agents don't need faster loops; they need a cortex. They need SQL.

### The Solution: PGLite (Postgres in WebAssembly)

Embedding PGLite directly in the browser treats data as a relational dataset rather than transient variables.

#### 1. Fuzzy Joins for Dirty Data

The hardest part of scraping is matching data that *should* be the same but isn't ("Apple Inc." vs "Apple Computer"). Using `pg_trgm` extension in-browser:

```sql
SELECT scraped.product_name, master.sku,
       similarity(scraped.product_name, master.name) as match_score
FROM scraped_products scraped
JOIN master_catalog master ON scraped.product_name % master.name
ORDER BY match_score DESC;
```

#### 2. Preserving Hierarchy with ltree

The web is a tree (DOM), but we flatten it into lists and lose context. Using `ltree` extension:

```sql
-- Find all comments in a specific sub-thread without recursion
SELECT * FROM comments WHERE path <@ 'root.123.456';
```

#### 3. Analytical Reasoning with Window Functions

Questions like "Is this price significantly lower than the average for this category?" require maintaining state in JS. In SQL, it's declarative:

```sql
SELECT product_name, price,
       AVG(price) OVER (
         PARTITION BY category
         ORDER BY scrape_date
         ROWS BETWEEN 5 PRECEDING AND CURRENT ROW
       ) as moving_avg
FROM pricing_history;
```

### How PGLite Works

- **Single-User Mode Hack**: Postgres normally needs multi-process architecture (forking). PGLite uses "single-user mode" (bootstrap mode for disaster recovery) to run as a single process in the browser tab.
- **Virtual File System**: Maps Postgres filesystem to IndexedDB for persistence across sessions.
- **Storage Limits**: Browser quotas constrain this - the sweet spot is keeping the "working set" lean (~3MB).

### Performance Characteristics

| Scale | Winner |
|-------|--------|
| Up to 10k rows | JavaScript faster |
| 100k+ rows | PGLite wins |

### Engineering Learnings

1. **Memory Wall**: Database file structure often loaded into memory. Browser tabs are hostile environments - keep working sets lean.

2. **Relaxed Durability is Mandatory**: Waiting for synchronous fsync to IndexedDB kills performance. Accept risk of losing last few milliseconds of data in exchange for 100x write performance.

3. **The Real Constraint**: Not compiling Postgres to WASM (ElectricSQL did that), but managing memory in browser's hostile environment.

### When to Use This Pattern

- Data scraping tasks needing reconciliation across sources
- Prototyping before building server infrastructure
- Privacy-sensitive apps where data shouldn't leave browser
- When JSON.filter isn't enough and you want declarative SQL

### Trade-offs

| Browser-Based (PGLite) | Server-Based |
|------------------------|--------------|
| Fast, local, no latency | Scalable, persistent, robust |
| ~3MB working set limit | Virtually unlimited |
| Session-scoped (IndexedDB) | Persistent across devices |
| Privacy-friendly | Centralized, easier backup |

---

## Multi-Agent Performance: The Sampling Hypothesis

*Source: ["More Agents Is All You Need" paper discussion](https://news.ycombinator.com/item?id=39955725) - Added: 2026-01-18*

### The Counterintuitive Finding

A paper titled "More Agents Is All You Need" challenges the effectiveness of sophisticated multi-agent setups like Chain-of-Thought and LLM-Debate. The surprising conclusion: **simply running the same query multiple times and picking the most common answer performs just as well (sometimes better) than complex multi-agent orchestration**.

### The Simple Alternative

Instead of elaborate multi-agent schemes:
1. Run the same query multiple times on a single LLM
2. No shared context across queries
3. Use a similarity algorithm to analyze the answers
4. Select the most common response

### Why This Works

The key insight is about the nature of LLM outputs:
- **Correct answers tend to be consistent** - Multiple runs converge on similar phrasing
- **Hallucinations are chaotic** - Each hallucination is unique/different
- **Majority voting filters noise** - Consensus emerges from correct answers

This is essentially a statistical filtering mechanism that exploits the consistency of correct responses.

### Implications for Multi-Agent Systems

The findings suggest that improvements attributed to clever multi-agent prompting may actually stem from:
1. **Repeated sampling** - Running the LLM multiple times
2. **Selection pressure** - Having the LLM choose among multiple options

The "debate" or "chain-of-thought" framing may be incidental, not causal.

### When Multi-Agent Still Makes Sense

This doesn't invalidate all multi-agent architectures:

| Use Case | Sampling Suffices? | Multi-Agent Adds Value? |
|----------|-------------------|------------------------|
| Factual accuracy | Yes | Minimal |
| Complex reasoning chains | Maybe | Possibly for decomposition |
| Tool orchestration | No | Yes (different capabilities needed) |
| Specialized knowledge | No | Yes (RAG with different domains) |
| Code generation + testing | No | Yes (generator vs. critic roles) |

### Practical Takeaway

Before building complex multi-agent systems, consider:
1. Does simple sampling + majority voting solve the problem?
2. Is the improvement from multi-agent actually from the orchestration, or just from running the LLM more times?
3. Are different agents actually bringing different capabilities, or just different prompts?

**Cost consideration:** Multiple samples of a cheaper model may outperform single queries to expensive models, while also providing a natural quality signal via answer consistency.

---

## Multi-Tenancy Patterns for AI/ML in SaaS

*Source: [Let's Architect! Discovering Generative AI on AWS](https://aws.amazon.com/blogs/architecture/lets-architect-generative-ai/) - Added: 2026-01-18*

### The Challenge

Working with AI/ML workloads and generative AI in a production SaaS environment requires careful design considerations:

- **Tenant separation** - How to isolate data and model access between tenants
- **Model mapping** - How different tenants are mapped to models (shared vs. dedicated)
- **Inference scaling** - How to scale inferencing based on tenant load
- **Integration** - How to connect with upstream/downstream services
- **Fine-tuning** - How LLMs can be fine-tuned for tenant-specific needs

### Key Patterns

**RAG for Tenant Context:**
- Use Retrieval-Augmented Generation to enrich LLMs with tenant-specific contextual information
- Each tenant can have their own knowledge base/vector store
- Allows personalization without fine-tuning the base model

**Fine-Tuning Strategies:**
- Shared base model with tenant-specific adapters (LoRA)
- Dedicated fine-tuned models for high-value tenants
- Trade-offs between cost, customization, and maintenance

### Resources

- [AWS Let's Architect video on SaaS meets AI/ML](https://aws.amazon.com/blogs/architecture/lets-architect-generative-ai/) - Deep dive into multi-tenancy patterns
- [Generative AI best practices post](https://aws.amazon.com/blogs/architecture/lets-architect-generative-ai/) - Implementation strategies

---

## Agent Configuration Validation: Fail Fast Patterns

*Source: [Reddit r/aws - AWS Security Agent Feedback](https://www.reddit.com/r/aws/comments/1qcyfwc/aws_security_agent_feedback_agent_should_validate/) - Added: 2026-01-18*

### The Problem

When AI agents operate within platform constraints (allowed URLs, permissions, etc.), they often can't distinguish between:
- **Configuration mismatch**: "I'm blocked from accessing this URL by my own platform's controls"
- **Actual failure**: "The credentials are invalid"

Example: AWS Security Agent was given authentication instructions pointing to `https://api.app.example.com`, but that URL wasn't in the allowed target list. The agent got `ERR_ACCESS_DENIED` and incorrectly concluded the credentials were invalid.

### The Improvement Pattern

**Cross-reference instructions against constraints before execution:**

1. Parse URLs/resources mentioned in natural language instructions
2. Validate against configured allowlists/blocklists
3. Fail fast with clear configuration error if mismatch detected

Instead of:
> "Authentication failed - invalid credentials"

Surface:
> "Configuration error: URL 'https://api.app.example.com' in your authentication instructions is not in the allowed target URLs list."

### Alternative: Pre-flight Validation

During setup/configuration phase:
- Extract all URLs referenced in instructions
- Validate against target URL list
- Surface mismatches before the agent starts executing

### Why This Matters

AI agents are excellent at adapting testing/execution strategy, but need visibility into their own platform's configuration constraints. Without this:
- Wasted compute on doomed attempts
- Misleading error messages
- Poor user experience debugging "why didn't it work"

### Generalized Principle

Any autonomous agent operating within constraints should:
1. **Know its boundaries** - Have access to its own configuration/permission model
2. **Validate early** - Check that instructions are achievable within constraints before attempting
3. **Report accurately** - Distinguish "I can't do this" from "this didn't work"

---

## FLUJO: Local Workflow Orchestration with MCP

*Source: [FLUJO](https://mario-andreschak.github.io/FLUJO/githubpages/index.html) - Added: 2026-01-18*

### What It Is

FLUJO is an open-source platform that bridges workflow orchestration, Model-Context-Protocol (MCP), and AI tool integration. Runs locally and provides a unified interface for managing AI models, MCP servers, and complex workflows.

**Status:** v0.1.4 (Preview)

### Key Features

| Feature | Description |
|---------|-------------|
| **API Key Management** | Encrypted storage for environment variables and API keys, usable across the application |
| **Model Management** | Configure multiple AI models simultaneously with custom system instructions |
| **MCP Server Integration** | Install MCP servers from GitHub or local filesystem, manage tools |
| **Visual Flow Builder** | Create and design complex workflows connecting different models |
| **Chat Interface** | Interact with flows via chat with file attachments |
| **OpenAI-Compatible Endpoint** | External tool integration for CLine, Roo, or other AI applications |

### When to Use FLUJO

**Good fit:**
- Need local, privacy-focused MCP orchestration
- Want visual flow building for multi-step AI workflows
- Experimenting with different models in a single workflow
- Building complex pipelines connecting multiple MCP servers
- Want an open-source alternative to cloud-hosted platforms

**Trade-offs:**
- Local-only (no cloud deployment option)
- Preview/early stage software
- Less ecosystem support than hosted alternatives

### Comparison with Other Approaches

| Platform | Hosting | Visual Builder | MCP Support | Best For |
|----------|---------|----------------|-------------|----------|
| FLUJO | Local | Yes | Yes | Local experimentation, privacy |
| Dedalus Labs | Cloud | No | Yes | Rapid prototyping, multi-model |
| ContextForge Gateway | Self | Admin UI | Yes | Federation, REST conversion |
| n8n / Zapier | Both | Yes | Limited | Traditional automation |

### Related

- Dedalus Labs (below) - Cloud-hosted MCP platform
- IBM MCP Context Forge Gateway (below) - Self-hosted gateway/registry

---

## MCP Tool Integration Platforms

*Source: [Dedalus Labs (YC S25) Launch HN](https://news.ycombinator.com/item?id=45054040) - Added: 2026-01-18*

### The Problem with MCP Integration Today

Building agentic AI apps that use tools is painful:
- Running local MCP servers
- Handwiring API authentication across OpenAI, Anthropic, Google SDKs
- Redeploys and networking configs for every change
- Hours wrestling with AWS setup instead of building product

**The pain point:** What should be `tools=code_execution` and "just work" takes 2 weeks of setup.

### Dedalus Labs Approach

Cloud platform that simplifies MCP tool integration to a single API endpoint:

```python
client = Dedalus()
runner = DedalusRunner(client)

result = runner.run(
    input=prompt,
    tools=[tool_1, tool_2],
    mcp_servers=["author/server-1", "author/server-2"],
    model=["openai/gpt-4.1", "anthropic/claude-sonnet-4-20250514"],
    stream=True,
)
```

**Key features:**
- Upload streamable HTTP MCP servers to their platform
- OpenAI-compatible SDKs drop into existing codebases
- Model-agnostic (OpenAI, Anthropic, Google)
- SDKs: Python, TypeScript, Go (all MIT licensed)

### MCP Security Concerns

The running joke: "The S in MCP stands for security."

**Current problem:** MCP servers are expected to act as both:
- Authentication server
- Resource server

This is too much burden on server writers who just want to expose a resource endpoint.

**Planned solutions:**
- Auth solution (launching soon as of Aug 2025)
- MCP marketplace with billing and rev-share for tool monetization

### When This Pattern Makes Sense

Use a hosted MCP platform when:
- Building products (not infrastructure)
- Need multi-model support without SDK gymnastics
- Want to avoid Docker/YAML/AWS complexity
- Rapid prototyping with tool-calling LLMs

Build your own when:
- Need fine-grained control over tool execution
- Security/compliance requires on-prem
- Building the infrastructure layer itself

### Similar Tools/Platforms

- **Klavis AI** - MCP integration for AI applications
- **AWS MCP Servers** - AWS-hosted MCP infrastructure
- **IBM MCP Context Forge Gateway** - Self-hosted MCP gateway/registry (see below)
- Self-hosted MCP with local servers (more control, more complexity)

---

## IBM MCP Context Forge Gateway

*Source: [GitHub - IBM/mcp-context-forge](https://github.com/IBM/mcp-context-forge) - Added: 2026-01-18*

### What It Is

ContextForge MCP Gateway is an open-source gateway, proxy, and registry that **federates MCP and REST services**—unifying discovery, auth, rate-limiting, observability, virtual servers, multi-transport protocols, and an optional Admin UI into one clean endpoint for AI clients.

**Status:** Alpha/early beta (v0.4.0). Not production-ready. No official IBM support.

### Key Capabilities

| Feature | Description |
|---------|-------------|
| **Federation** | Aggregate multiple MCP and REST services behind one endpoint |
| **REST-to-MCP Virtualization** | Expose legacy REST APIs as MCP-compliant tools |
| **Multi-Transport** | HTTP, JSON-RPC, WebSocket, SSE, stdio, streamable-HTTP |
| **Admin UI** | Real-time management and configuration dashboard |
| **Auth & Rate Limiting** | Built-in JWT authentication, rate limiting |
| **Scalability** | Redis-backed caching, multi-cluster federation on K8s |

### When to Use This

**Good fit:**
- Federating multiple MCP servers behind a single gateway
- Converting legacy REST APIs to MCP without rewriting them
- Need observability/rate-limiting across MCP tool calls
- Running multi-cluster deployments with Redis-backed federation
- Want an admin UI to manage MCP registrations

**Poor fit:**
- Simple single-server MCP setups (overkill)
- Production workloads (not ready yet)
- Need official vendor support

### Quick Start

```bash
# PyPI install
pip install mcp-contextforge-gateway

# Launch with auth
export MCPGATEWAY_UI_ENABLED=true
export MCPGATEWAY_ADMIN_API_ENABLED=true
BASIC_AUTH_PASSWORD=pass JWT_SECRET_KEY=my-test-key \
  mcpgateway --host 0.0.0.0 --port 4444

# Generate bearer token
export MCPGATEWAY_BEARER_TOKEN=$(python3 -m mcpgateway.utils.create_jwt_token \
    --username admin --exp 10080 --secret my-test-key)
```

Docker:
```bash
docker run -d --name mcpgateway \
  -p 4444:4444 \
  -e MCPGATEWAY_UI_ENABLED=true \
  -e MCPGATEWAY_ADMIN_API_ENABLED=true \
  -e JWT_SECRET_KEY=my-test-key \
  -e BASIC_AUTH_USER=admin \
  -e BASIC_AUTH_PASSWORD=changeme \
  ghcr.io/ibm/mcp-context-forge:0.4.0
```

### Using with Claude Desktop

The `mcpgateway.wrapper` module exposes gateway tools over stdio for clients that can't open authenticated SSE streams:

1. Configure in Claude Desktop: File → Settings → Developer → Edit Config
2. Point to the wrapper module with appropriate env vars
3. Restart the app

### Architecture Pattern: REST-to-MCP Conversion

One compelling use case is virtualizing legacy APIs:

```
┌─────────────┐     ┌──────────────────┐     ┌───────────────┐
│ AI Client   │────▶│ ContextForge     │────▶│ Legacy REST   │
│ (MCP)       │     │ Gateway          │     │ API           │
└─────────────┘     └──────────────────┘     └───────────────┘
                           │
                           ▼
                    ┌──────────────────┐
                    │ Native MCP       │
                    │ Servers          │
                    └──────────────────┘
```

The gateway handles translation, allowing gradual migration without rewriting existing services.

### Comparison with Other Approaches

| Approach | Hosting | Complexity | Best For |
|----------|---------|------------|----------|
| Direct MCP servers | Self | Low | Simple setups |
| ContextForge Gateway | Self | Medium | Federation, REST conversion |
| Dedalus Labs | Cloud | Low | Rapid prototyping |
| Klavis AI | Cloud | Low | Integration focus |
| AWS MCP Servers | AWS | Medium | AWS-native workloads |

---

## Customer-Facing Analytics Agents

*Source: [Inconvo](https://inconvo.com/) - Added: 2026-01-18*

### The Use Case

Embedding AI-powered analytics directly into products so end users can query their own data conversationally. Rather than building dashboards, let users ask natural language questions about their data.

### Inconvo Platform

A platform for developers to build and deploy AI analytics agents that can be embedded into existing products.

**Core workflow:**
1. Connect existing databases via API
2. Fine-tune the AI analytics agent for domain-specific questions
3. Embed into product through their API

**Example interactions:**
- "What was our most popular product last month?"
- "How much revenue did we make from those orders?"
- "What percentage was that of total revenue in the same period?"

### Design Philosophy

Analytics agents should be:
- **Powerful, fast, accurate** - Core functionality
- **Effortless for developers** - Simple integration
- **Visible to PMs** - Clear insight into user interactions
- **Controllable by designers** - Full UI customization

The "one-person-team" consideration: Works whether you have separate dev/PM/design roles or if you're a solo founder wearing all hats.

### When to Consider Customer-Facing Analytics

**Good fit:**
- Products with significant user data (usage metrics, transactions, content)
- Users who need answers but aren't analysts
- Self-service analytics reducing support burden
- Adding value through data insights without building dashboards

**Trade-offs:**
- Data accuracy requirements are high (wrong answers erode trust)
- Natural language ambiguity can lead to misinterpretation
- May need significant fine-tuning for domain vocabulary
- Consider when gut instinct/creativity matters more than data-driven decisions

### Comparison with Other Analytics Approaches

| Approach | Effort | Flexibility | User Skill Required |
|----------|--------|-------------|---------------------|
| Static dashboards | Low | Low | None |
| BI tools (Tableau, etc.) | Medium | High | Medium |
| Custom analytics | High | High | Variable |
| AI analytics agents | Medium | High | None (natural language) |

### Similar Platforms

- **Minusx** - AI for Metabase/existing BI tools
- **Amazon QuickSight Q** - AWS's natural language analytics
- **ThoughtSpot** - Search-driven analytics (enterprise)

---

## Voice Agents for Call Center Replacement

*Source: [Leaping AI](https://leapingai.com/) - Added: 2026-01-18*

### The Use Case

Replacing traditional call centers with AI voice agents that can handle customer calls with human-like conversation quality. The pitch: same or better customer satisfaction than human agents, but at scale.

### Leaping AI Platform

Enterprise-focused voice agent platform targeting complex call center replacement.

**Key claims:**
- Self-improving agents that learn from interactions
- Human-like conversational quality
- Customer satisfaction comparable to human agents
- Designed for enterprises and large retailers

### Enterprise-Grade Architecture

**In-house infrastructure approach:**
- All components managed internally: model deployment, telephony, data storage
- No external dependencies for core functionality
- Full control over data pipeline

**Security model:**
- Data stays private (no external data sharing)
- On-premise-like control despite cloud deployment
- Built for sensitive enterprise data requirements

### When Voice Agents Make Sense

**Good fit:**
- High call volume (economies of scale)
- Repetitive, predictable inquiry types
- Need for 24/7 availability
- Consistent quality at scale matters
- Cost reduction is a primary driver

**Trade-offs to consider:**
- Risk of losing personal touch in customer interactions
- Balance between automation efficiency and genuine human connection
- Complex edge cases may still need human escalation
- Customer perception of "talking to a robot"

### Comparison: Voice Agent Approaches

| Approach | Complexity | Control | Best For |
|----------|------------|---------|----------|
| IVR (Interactive Voice Response) | Low | High | Simple routing, basic info |
| Chatbots with voice synthesis | Medium | Medium | FAQ-style queries |
| Full voice agents (Leaping AI) | High | High | Complex call center replacement |
| Human + AI assist | Medium | Medium | Quality-critical interactions |

### Similar Platforms

- **Bland AI** - Voice AI for phone calls
- **Vapi** - Voice API for building voice agents
- **Retell AI** - Conversational voice AI
- **Air AI** - Autonomous phone agents

---

## Conversational AI Bot Platforms

*Source: [ChatBotKit](https://chatbotkit.com/) - Added: 2026-01-18*

### The Use Case

Building conversational AI interfaces (chatbots, messaging bots) that can be embedded into websites, apps, or integrated with messaging platforms. The goal: rapid deployment of AI assistants without building infrastructure from scratch.

### ChatBotKit Platform

A vertically integrated conversational AI platform with modular, reusable components.

**Scale:** 40,000+ makers, 10M+ messages processed monthly.

**Key capabilities:**
- **AI Agents** - Automate business processes and service delivery
- **AI Widgets** - Embeddable conversational interfaces for websites/apps
- **AI Messaging** - Native integration with Slack, Discord, WhatsApp, Messenger, Telegram
- **SDKs** - Developer tools for custom implementations
- **Enterprise features** - Advanced security, compliance, multi-agent coordination

**Technical architecture:**
- Modular components: datasets, skillsets, integrations
- OAuth and MCP (Model Context Protocol) support for external service connections
- Comprehensive logging and analytics dashboards
- Policy management and content filtering
- GDPR and CCPA compliance built-in

### When to Use a Bot Platform

**Good fit:**
- Customer service automation (FAQ, routing, basic support)
- Internal employee assistants (HR questions, IT help desk)
- Document-based Q&A systems
- Multi-channel deployment (web + messaging apps)
- Rapid prototyping without infrastructure investment

**Trade-offs:**
- Less control than building custom
- Platform lock-in risk
- May not handle complex multi-step workflows as well as custom agents
- Pricing can scale with usage

### Comparison: Conversational AI Platforms

| Approach | Complexity | Control | Best For |
|----------|------------|---------|----------|
| Bot platforms (ChatBotKit, etc.) | Low | Medium | Rapid deployment, multi-channel |
| Custom agents with SDKs | Medium-High | High | Complex workflows, custom UX |
| Voice agents (Leaping AI, Vapi) | Medium | High | Phone/voice interactions |
| Analytics agents (Inconvo) | Medium | Medium | Data queries, dashboards replacement |

### Similar Platforms

- **Voiceflow** - Visual conversation design (see section below)
- **Botpress** - Open-source bot platform
- **Dialogflow (Google)** - Enterprise conversational AI
- **Amazon Lex** - AWS bot building service
- **Rasa** - Open-source conversational AI framework

---

## Personal Memory Layers for LLMs

### memary: Knowledge Graph Memory for Agents

*Source: [GitHub - kingjulio8238/memary](https://github.com/kingjulio8238/memary) - Added: 2026-01-18*

memary is an open-source project that provides long-term memory for autonomous agents using knowledge graphs. It addresses the finite context window limitation by storing information in Neo4j knowledge graphs and retrieving relevant information for responses.

**Core Components:**

| Component | Description |
|-----------|-------------|
| **Routing Agent** | ReAct agent that routes queries among tools, reasoning over which tool to use next |
| **Knowledge Graph** | Neo4j-backed graph storing agent responses and entity relationships |
| **Memory Stream** | Tracks all entities in the knowledge graph - reflects user's *breadth* of knowledge |
| **Entity Knowledge Store** | Groups and ranks entities by frequency/recency - reflects user's *depth* of knowledge |

**Architecture Pattern:**

The system maintains two complementary memory structures:

1. **Memory Stream** - Entity extraction captures every concept the user has been exposed to (breadth). No depth inference - just exposure tracking.

2. **Entity Knowledge Store** - Tracks frequency and recency of entity references. Top N entities passed into context window, representing what the user knows deeply vs. superficially.

**Design Influence:** The memory module was influenced by Microsoft Research's K-LaMP (Knowledge-based Language Model Personalization) design.

**Quick Start:**

```bash
# Install dependencies
pip install -r requirements.txt

# Configure .env with API keys
OPENAI_API_KEY="YOUR_API_KEY"
NEO4J_PW="YOUR_NEO4J_PW"
NEO4J_URL="YOUR_NEO4J_URL"
PERPLEXITY_API_KEY="YOUR_API_KEY"
GOOGLEMAPS_API_KEY="YOUR_API_KEY"

# Run Streamlit demo
streamlit run app.py
```

**Future Roadmap:**
- Multiprocessing for simultaneous query processing
- Query decomposition (break complex queries into subqueries)
- Reranking of agent responses (ColBERT performs best in their tests)

**When to Use memary:**

| Good Fit | Poor Fit |
|----------|----------|
| Agents needing persistent user knowledge | Simple, stateless Q&A |
| Personalization based on user expertise depth | Privacy-sensitive without self-hosting Neo4j |
| Complex queries benefiting from entity relationships | Low-latency requirements (graph queries add overhead) |

**Comparison with Other Memory Approaches:**

| Approach | Knowledge Structure | Temporal Tracking | Depth vs Breadth |
|----------|---------------------|-------------------|------------------|
| memary | Knowledge graph (Neo4j) | Via entity recency | Explicit (Memory Stream vs Entity Store) |
| C.O.R.E (below) | Temporal knowledge graph | Full history | Implicit |
| Zep (below) | Facts + Summaries | Limited | Via summary generation |
| Vector RAG | Embeddings | None | None |

---

*Source: [GitHub - RedPlanetHQ/core](https://github.com/RedPlanetHQ/core) - Added: 2026-01-18*

### The Problem

LLMs lack persistent memory across conversations. Each session starts fresh without context about user preferences, past decisions, or accumulated knowledge. Memory solutions exist but most act like "basic sticky notes" - they only show what's true now, not the history of how things changed.

### C.O.R.E (Contextual Observation & Recall Engine)

A private, portable memory layer for LLMs that you own completely. Can run locally or hosted, then connect to tools like Cursor, Claude to share context across multiple applications.

**Key differentiator:** Built as a dynamic, living temporal knowledge graph rather than static key-value memory.

**Architecture:**
- Every fact is a first-class "Statement" with full history
- Each statement includes: what was said, who said it, when it happened, why it matters
- Full transparency: trace the source, see what changed, explore why the system "believes" something

### Use Case: Change Auditing

Ask: "What changed in our pricing since Q1?"

With temporal knowledge graph, you see:
- Exactly what prices changed
- Who approved them
- The context (meeting, email, document)
- When each update happened

This enables compliance, auditability, and insight across products, teams, and time.

Ask: "What does Mike know about Project Phoenix?" and get a timeline of meetings, decisions, and facts Mike was involved in, with full traceability.

### Integration Options

**Cloud Setup:**
1. Sign up to Core Cloud
2. Add text to save in memory graph
3. Connect Core Memory MCP with Cursor

**Local Setup:**
- Requires Docker + OpenAI API Key
- Self-hosted, fully private

**Cursor MCP Integration:**
After every interaction, update memory with user query and assistant response. Session ID should be conversation UUID.

**API Access:**
- Ingest API for adding data
- Search API for retrieval
- Workspace support for multi-tenant setups

### What to Store (and What Not To)

**Store:**
- Conversation history
- User preferences
- Task context
- Reference materials

**Don't Store:**
- Sensitive data (PII)
- Credentials
- System logs
- Temporary data

### Current Status (v1)

**Done:**
- Private memory space with ingest/search
- Workspace support for ingestion and search

**In Progress/Planned:**
- Multiple spaces with unique URLs
- User-controlled sharing and privacy
- Ingestion filter rules
- Granular API key permissions
- Audit logging
- Role-based access control
- Webhooks and notifications

### Trade-offs

**Considerations:**
- Relying on AI memory may create dependency that could hinder personal memory retention or critical thinking
- Balance technology with personal engagement
- The "family archive" use case: documenting conversations and memories for revisiting later

### Comparison: Memory Layer Approaches

| Approach | Persistence | Auditability | Control | Best For |
|----------|-------------|--------------|---------|----------|
| Session context only | None | None | N/A | Simple, stateless interactions |
| Key-value memory (most tools) | Yes | Limited | Variable | Basic preferences, facts |
| Temporal knowledge graph (C.O.R.E) | Yes | Full | High | Change tracking, compliance, rich context |
| Vector databases (RAG) | Yes | Limited | High | Document retrieval, semantic search |

### Similar Tools

- **Mem0** - Personal memory layer for AI
- **Zep** - Memory for AI assistants (see detailed section below)
- **Motorhead** - Long-term memory for LLMs
- **LangChain Memory** - Memory abstractions in agent frameworks
- **Dify LongTermMemory** - Dify-specific tool using Knowledge API for per-user memory (requires GPT-4+)

---

## Zep: Perpetual Memory for AI Assistants

*Source: [Zep Playground](https://app.getzep.com/playground) - Added: 2026-01-18*

### What It Is

Zep provides long-term memory for AI assistants through a high-level memory abstraction. Unlike simple chat history storage, Zep processes conversations into three distinct artifact types that can be semantically searched and composed into prompts.

### Three Memory Artifacts

| Artifact | Description | Trade-offs |
|----------|-------------|------------|
| **Facts** | Extracted from dialog, deduplicated and deconflicted in real-time | Precise, queryable, good for structured info |
| **Summaries** | Generated progressively as messages are added | More nuance than Facts, but lossy—older details may be lost |
| **Message History** | Raw conversation storage with simple retrieval | Complete but unprocessed |

### How It Works

**Facts:**
- Extracted automatically from conversation
- Deduplicated and deconflicted in real-time
- Developers can tune what facts are extracted and how conflicts are resolved
- Good for: user preferences, key decisions, stated constraints

**Summaries:**
- Generated progressively as new messages are added
- Can capture nuance that discrete Facts miss
- Lossy—may not include details from much earlier in conversation
- Developers can tune summary focus and generation strategy
- Good for: conversation context, relationship building, narrative continuity

**Message History:**
- Simple interface to retrieve most recent dialog
- Direct access to raw conversation for inclusion in prompts
- Good for: immediate context, debugging, exact quotes

### Prompt Template Pattern

```
System:
You are a very helpful assistant. Review the context from your prior
conversation with the user below, and then answer the user's question.

## Facts
{{facts}}

## Summary
{{summary}}

## Message History
{{message_history}}

User:
{{user_query}}
```

This layered approach lets you balance:
- **Precision** (Facts) - specific, structured information
- **Context** (Summaries) - narrative understanding
- **Recency** (Message History) - immediate conversation flow

### When to Use Zep

**Good fit:**
- AI assistants needing long-term user memory
- Applications where conversation context matters across sessions
- Want semantic search over memory artifacts
- Need tunable fact extraction and summary generation

**Trade-offs:**
- Another service dependency vs. building custom
- Summaries are lossy—important early details may be missed
- Requires account for advanced features (Dialog Classification, Structured Data Extraction)

### Comparison with Other Memory Approaches

| Approach | Fact Extraction | Summarization | Semantic Search | Control |
|----------|-----------------|---------------|-----------------|---------|
| Simple chat history | No | No | No | Full |
| Zep | Yes, real-time | Yes, progressive | Yes | Medium |
| C.O.R.E (above) | Yes, temporal | No | Yes | High |
| Vector DB + RAG | No | No | Yes | High |
| Dify LongTermMemory | Manual (user-stated) | No | Via Knowledge API | Platform-locked |

### Related

- C.O.R.E (above) - More emphasis on temporal knowledge graphs and auditability
- Mem0 - Alternative personal memory layer
- LangChain Memory - Framework-native memory abstractions

---

## EnrichMCP: Semantic Data Layer for MCP Servers

*Source: [GitHub - featureform/enrichmcp](https://github.com/featureform/enrichmcp) - Added: 2026-01-18*

### What It Is

EnrichMCP is a Python framework that adds a **semantic layer** to MCP servers, making it easier for AI agents to understand and navigate data. Think of it as "SQLAlchemy for AI agents."

**The core insight:** AI agents need more than raw database access—they need typed, discoverable tools with relationship navigation and schema understanding.

### Three Layers It Adds

1. **Semantic Layer** - AI agents understand what data means, not just its structure
2. **Data Layer** - Type-safe models with validation and relationships
3. **Control Layer** - Authentication, pagination, and business logic

### Key Features

| Feature | Description |
|---------|-------------|
| Automatic Schema Discovery | `explore_data_model()` returns complete schema with entities, fields, types, relationships |
| Relationship Navigation | Define once, AI traverses naturally: `user → orders → products → categories` |
| Type Safety | Full Pydantic validation on every interaction |
| Built-in Pagination | `PageResult[Order]` with page/page_size/total_items |
| Context & Auth | Pass auth, DB connections via `EnrichContext` |

### Three Integration Paths

**1. SQLAlchemy Models (fastest)**

```python
from enrichmcp import EnrichMCP
from enrichmcp.sqlalchemy import include_sqlalchemy_models, sqlalchemy_lifespan, EnrichSQLAlchemyMixin

class Base(DeclarativeBase, EnrichSQLAlchemyMixin):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    orders: Mapped[list["Order"]] = relationship(back_populates="user")

app = EnrichMCP("E-commerce Data", lifespan=sqlalchemy_lifespan(Base, engine))
include_sqlalchemy_models(app, Base)
app.run()
```

AI agents get: `list_users(status='active')`, `get_user(id=123)`, relationship navigation

**2. REST API Wrapping**

```python
@app.entity
class Customer(EnrichModel):
    id: int = Field(description="Unique customer ID")
    orders: list["Order"] = Relationship(description="Customer's purchase history")

@app.resource
async def get_customer(customer_id: int) -> Customer:
    response = await http.get(f"/api/customers/{customer_id}")
    return Customer(**response.json())

@Customer.orders.resolver
async def get_customer_orders(customer_id: int) -> list[Order]:
    response = await http.get(f"/api/customers/{customer_id}/orders")
    return [Order(**o) for o in response.json()]
```

**3. Full Custom Control**

Computed fields, ML-powered resolvers, complex business logic:

```python
@User.churn_risk.resolver
async def predict_churn_risk(user_id: int, context: EnrichContext) -> float:
    features = await gather_user_features(user_id)
    model = context.get("ml_models")["churn"]
    return float(model.predict_proba(features)[0][1])
```

### CRUD Operations

Fields are immutable by default. Mark as `mutable=True` for updates:

```python
@app.entity
class Customer(EnrichModel):
    id: int = Field(description="ID")
    email: str = Field(mutable=True, description="Email")

@app.update
async def update_customer(cid: int, patch: Customer.PatchModel) -> Customer:
    ...
```

### Installation

```bash
pip install enrichmcp
pip install enrichmcp[sqlalchemy]  # With SQLAlchemy support
```

### When to Use EnrichMCP

**Good fit:**
- Building MCP servers that expose database or API data
- Need typed, validated tools with relationship navigation
- Want AI agents to discover and understand your data schema
- SQLAlchemy-based applications (drop-in integration)
- Complex data models with entity relationships

**Trade-offs:**
- Additional abstraction layer (vs. raw MCP)
- Python-only (no JS/TS SDK)
- Less control than hand-rolled MCP tools

### Comparison with Other MCP Approaches

| Approach | Typing | Relationships | Schema Discovery | Best For |
|----------|--------|---------------|------------------|----------|
| Raw MCP tools | Manual | Manual | Manual | Simple tools |
| EnrichMCP | Automatic | Built-in | Built-in | Data-heavy applications |
| ContextForge Gateway | N/A | N/A | Partial | Federation, REST conversion |
| Dedalus Labs | Manual | Manual | Manual | Hosted MCP (any model) |

### Related

- `mcp-protocol-adoption.md` - MCP ecosystem overview
- IBM MCP Context Forge (above) - Federation and gateway patterns

---

## Mastra: TypeScript AI Agent Framework

*Source: [Mastra Course](https://mastra.ai/course) - Added: 2026-01-18*

### What It Is

Mastra is a TypeScript-based framework for building AI agents with tools, memory, and MCP integration. It's part of the emerging AG-UI protocol ecosystem alongside LangGraph and CrewAI.

### Core Concepts

The Mastra 101 course teaches three foundational capabilities:

**1. Building Your First Agent**
- Create an AI agent that reads external data sources
- Use custom tools for agent capabilities
- Deploy to a live playground for testing
- Ship to production

**2. Adding Tools via MCP**
- Connect agents to external services using MCP servers
- Search MCP registries to integrate tools for:
  - Email and social media
  - GitHub and news sources
  - Local files
- No custom code needed for standard integrations

**3. Adding Memory**
- Configure conversation history retention
- Implement semantic recall for relevant context
- Set up working memory for persistent state
- Create personalized, context-aware responses

### Unique Learning Approach

The course is delivered inside an agentic code editor where a code agent:
- Guides learners step-by-step
- Writes code collaboratively
- Helps build working agents from scratch

This is a meta-learning experience: learning about agents from an agent.

### When to Consider Mastra

**Good fit:**
- TypeScript/JavaScript environment
- Want hands-on learning by building
- Need MCP integration without writing boilerplate
- Building agents with memory requirements

**Comparison with other frameworks:**

| Framework | Language | Strength |
|-----------|----------|----------|
| Mastra | TypeScript | MCP integration, editor-native learning |
| LangGraph | Python | Complex state machines, workflow graphs |
| CrewAI | Python | Multi-agent orchestration |
| AutoGen | Python | Research-oriented, conversational agents |

### Resources

- Course: https://mastra.ai/course
- Framework integrates with AG-UI protocol (see `ag-ui-protocol.md`)

---

## Agentic RAG on Amazon Bedrock

*Source: [Agentic RAG in Amazon Bedrock: Building AI That Thinks and Acts](https://medium.com/@rijulnewalkar/agentic-rag-in-amazon-bedrock-building-ai-that-thinks-and-acts-e4bc1154f241) - Added: 2026-01-18*

### What is RAG?

Retrieval-Augmented Generation (RAG) enhances LLMs by giving them access to external knowledge sources (documents, product manuals, real-time data stores) rather than relying solely on training data.

**Basic RAG workflow:**
1. Retrieve relevant content from document store/vector database using semantic similarity
2. Inject retrieved context into LLM prompt
3. Generate response grounded in retrieved information

### The Evolution: Agentic RAG

**Agentic RAG** extends basic RAG by combining:
- **Reasoning** - LLM understands context and plans actions
- **Data retrieval** - Access to knowledge bases and external sources
- **Autonomous decision-making** - Agent can decide what to do next

The shift: You're not just building a chatbot—you're creating **autonomous digital agents** that retrieve information, generate answers, and take meaningful action.

### Amazon Bedrock Advantages

**Why Bedrock for Agentic RAG:**
- Enterprise-grade infrastructure
- Model flexibility (Claude, Titan, third-party models)
- Scalable orchestration
- Managed knowledge bases with vector search
- Built-in action groups for agent capabilities

### E-commerce Customer Support Use Case

**Scenario:** Customer support agent that can:
1. Retrieve product information from knowledge base
2. Check order status via API
3. Process returns or exchanges
4. Escalate to humans when needed

**Implementation pattern:**
```
┌─────────────────┐     ┌────────────────────┐     ┌──────────────────┐
│ Customer Query  │────▶│ Bedrock Agent      │────▶│ Knowledge Base   │
└─────────────────┘     │ (Orchestration)    │     │ (Product docs,   │
                        └────────────────────┘     │  FAQs, policies) │
                                │                  └──────────────────┘
                                │
                        ┌───────▼───────┐
                        │ Action Groups  │
                        │ (Lambda funcs) │
                        └───────────────┘
                                │
                    ┌───────────┴───────────┐
                    ▼                       ▼
            ┌──────────────┐       ┌──────────────┐
            │ Order API    │       │ Returns API  │
            └──────────────┘       └──────────────┘
```

### Key Implementation Considerations

**Business scalability:**
- Automate customer support to save time and resources
- Handle volume spikes without scaling human agents
- Maintain consistency across interactions

**Trade-offs:**
- Balance automation with human touch for trust/connection
- Consider when human escalation is necessary
- Data privacy and AI decision-making ethics

### When to Use Agentic RAG

**Good fit:**
- Customer support with product knowledge
- Internal documentation assistants
- Research assistants that need to retrieve and synthesize
- Any use case requiring grounded, accurate responses with action capability

**Comparison with other approaches:**

| Approach | Retrieval | Actions | Reasoning | Best For |
|----------|-----------|---------|-----------|----------|
| Basic RAG | Yes | No | Limited | Q&A over documents |
| Chatbot | No | Limited | Yes | Conversational interface |
| Agentic RAG | Yes | Yes | Yes | Autonomous task completion |
| Traditional APIs | No | Yes | No | Structured integrations |

### Related

- `aws-lambda-powertools-bedrock.md` - Powertools utility for Bedrock Agents
- IBM MCP Context Forge Gateway (above) - Alternative federation approach
- Customer-Facing Analytics Agents (above) - Similar autonomous data access pattern

---

## Airweave: Universal App Search for Agents

*Source: [GitHub - airweave-ai/airweave](https://github.com/airweave-ai/airweave) - Added: 2026-01-18*

### What It Is

Airweave lets AI agents semantically search any application or database. It's MCP-compatible and transforms contents from any app, database, or API into agent-ready knowledge.

**The pitch:** One queryable layer for building agents that need to find information across diverse sources.

### Core Capabilities

| Feature | Description |
|---------|-------------|
| **25+ integrations** | APIs, databases, apps, files—one unified search |
| **MCP compatible** | REST and MCP endpoints for retrieval |
| **Entity generators** | Each source defines `generate_entities()` yielding consistent format |
| **Automated sync** | Schedule or on-demand sync jobs |
| **Versioning & hashing** | Detects changes, updates only modified entities |
| **White-label multi-tenant** | OAuth2-based platform for SaaS builders |

### Architecture

```
┌─────────────┐     ┌──────────────────┐     ┌───────────────┐
│ AI Agent    │────▶│ Airweave         │────▶│ Source Apps   │
│ (MCP/REST)  │     │ (Search + Sync)  │     │ (Notion, DB,  │
└─────────────┘     └──────────────────┘     │  APIs, etc.)  │
                           │                 └───────────────┘
                           ▼
                    ┌──────────────────┐
                    │ Vector Database  │
                    │ (Configurable)   │
                    └──────────────────┘
```

### Quick Start

```bash
# Clone and run via Docker Compose
git clone https://github.com/airweave-ai/airweave.git
cd airweave
docker compose up -d
```

Access dashboard at `http://localhost:8080`:
- Add connections under **Sources**
- Configure sync schedules
- Monitor jobs
- Search via REST or MCP

### API Usage

| Endpoint | Purpose |
|----------|---------|
| `GET /sources` | List all available sources |
| `POST /connections/{short_name}` | Connect a new source |
| `POST /search` | Semantic search across connected sources |

Full Swagger docs at `http://localhost:8001/docs`.

### Technology Stack

- **Frontend:** React (JS/TS)
- **Backend:** FastAPI (Python)
- **Workers:** ARQ Redis for async background jobs
- **Databases:** Configurable vector DB via UI or API

### When to Use Airweave

**Good fit:**
- Building agents that need to search across multiple apps
- SaaS builders needing multi-tenant data sync
- Unifying structured + unstructured data for retrieval
- RAG pipelines with diverse sources
- Need MCP compatibility without building custom servers

**Trade-offs:**
- Self-hosted (vs. managed services like Dedalus Labs)
- Complexity increases with many sources
- Async-first design may require Redis for production scale

### Comparison with Other Approaches

| Approach | Hosting | Multi-Source | MCP | Best For |
|----------|---------|--------------|-----|----------|
| Airweave | Self | Yes (25+) | Yes | Universal app search |
| Dedalus Labs | Cloud | Via MCP servers | Yes | Rapid prototyping |
| ContextForge Gateway | Self | Via federation | Yes | REST-to-MCP conversion |
| Custom RAG pipeline | Self | Manual | Manual | Full control |

### Roadmap

- Additional integrations for popular SaaS APIs
- Redis & worker queues for production scale
- Webhooks for event-driven syncs
- Kubernetes Helm charts
- Enterprise features

### Related

- `mcp-protocol-adoption.md` - MCP ecosystem overview
- Agentic RAG on Bedrock (above) - Similar retrieval-augmented pattern
- EnrichMCP (above) - Semantic layer for MCP data access

---

## BLAST: Web Browsing AI Serving Engine

*Source: [GitHub - stanford-mast/blast](https://github.com/stanford-mast/blast) - Added: 2026-01-18*

### What It Is

BLAST (Browser-LLM Auto-Scaling Technology) is a high-performance serving engine for web browsing AI from Stanford's MAST research group. It provides infrastructure for serving browser-augmented LLMs with automatic optimization.

### Key Features

| Feature | Description |
|---------|-------------|
| **OpenAI-Compatible API** | Drop-in replacement for OpenAI's API |
| **Automatic Caching** | Reduces costs by caching repeated operations |
| **Parallelization** | Automatically parallelizes browser tasks for speed |
| **Streaming** | Stream real-time browser actions to users |
| **Concurrency** | Out-of-the-box multi-user support with resource management |
| **Local Mode** | Runs locally without cloud dependency |

### Quick Start

```bash
pip install blastai && blastai serve
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="not-needed",
    base_url="http://127.0.0.1:8000"
)

# Stream real-time browser actions
stream = client.responses.create(
    model="not-needed",
    input="Compare fried chicken reviews for top 10 fast food restaurants",
    stream=True
)

for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta if " " in event.delta else "<screenshot>", end="", flush=True)
```

### Use Cases

1. **Adding web browsing AI to apps** - OpenAI-compatible API with concurrency and streaming
2. **Workflow automation** - Auto-caching and parallelization keep costs down while enabling interactive latencies
3. **Local development** - Budget-aware, memory-conscious operation

### Performance Philosophy

BLAST focuses on two optimization axes:
- **Cost efficiency** - Caching reduces redundant LLM calls
- **Latency** - Parallelization enables interactive-level response times

The "auto-scaling" in the name refers to automatic resource management, not infrastructure scaling.

### Comparison: Web Browsing AI Approaches

| Approach | Hosting | API Compatibility | Best For |
|----------|---------|-------------------|----------|
| BLAST | Local | OpenAI-compatible | High-performance serving |
| Browser MCP servers | Self | MCP protocol | Tool integration |
| Herd trails | Browser | MCP protocol | Third-party automation |
| MCP-B | Browser | MCP protocol | Session-auth apps |

### When to Use BLAST

**Good fit:**
- Need OpenAI-compatible API for browser automation
- Want automatic cost optimization via caching
- Building multi-user applications with browser AI
- Local-first development without cloud dependencies

**Trade-offs:**
- Less control than custom MCP servers
- Focused on browser tasks (not general agent framework)
- Academic/research origin (may have different support expectations)

### Related

- MCP-B (see `mcp-browser-embedded.md`) - Browser-embedded MCP approach
- Herd browser automation (see `mcp-browser-embedded.md`) - Trail-based automation

---

## Toolkami: Minimal 7-Tool AI Agent

*Source: [GitHub - aperoc/toolkami](https://github.com/aperoc/toolkami) - Added: 2026-01-18*

### The Philosophy

"Seven tools is all you need." Toolkami takes a minimalist approach to AI agents, arguing that a small, well-chosen toolset is more effective than tool sprawl.

### Key Features

| Feature | Description |
|---------|-------------|
| **7 Core Tools** | Minimal toolset for general-purpose agent work |
| **Turbo Mode** | Full autonomy by disabling the `ask` tool - agent runs hands-free |
| **Hot-Reloading** | Self-modification capability via `--reload` flag |
| **MCP Server** | Standard MCP interface via FastMCP |
| **Devcontainer** | Ready-to-use development environment |

### Quick Start

```bash
# Install UV
curl -LsSf https://astral.sh/uv/install.sh | sh

# Start MCP server with hot-reloading
cd servers && PYTHONPATH=. uv run app.py --reload

# Start client (Gemini example)
./clients/gemini_client.py http://localhost:8081/sse
```

### Turbo Mode: Hands-Free Operation

By commenting out the `ask` tool, the agent runs fully autonomous without user confirmation:

```python
# @mcp.tool()
async def ask(question: str) -> str:
```

This is the "standard pace is for chumps" mode - useful for rapid prototyping or when you trust the agent's decisions.

### Roadmap

- OpenAI-compatible API
- Anthropic support
- System prompt guidelines with single-file project templates

### When to Use Toolkami

**Good fit:**
- Prototyping minimal agents quickly
- Learning MCP server patterns
- When you want explicit control over tool count
- Hands-free autonomous operation

**Trade-offs:**
- "Sharp tool" - limited guardrails
- Early stage, minimal documentation
- Gemini-focused client (other models coming)

### Comparison: Minimal vs. Feature-Rich Agents

| Approach | Tools | Philosophy | Best For |
|----------|-------|------------|----------|
| Toolkami | 7 | Minimal, focused | Learning, prototyping |
| Claude Code | Many | Production-grade | Real development work |
| Custom MCP | Variable | Full control | Specific use cases |

### Related

- FLUJO (above) - Visual workflow builder with MCP
- Dedalus Labs (above) - Hosted MCP platform
- `mcp-protocol-adoption.md` - MCP ecosystem overview

---

## AgenticSeek: Local Manus AI Alternative

*Source: [GitHub - Fosowl/agenticSeek](https://github.com/Fosowl/agenticSeek) - Added: 2026-01-18*

### What It Is

AgenticSeek is a fully local alternative to Manus AI, a voice-enabled AI assistant that codes, explores filesystem, browses the web, and self-corrects—all without sending data to the cloud. Built with reasoning models like DeepSeek R1, runs entirely on your hardware.

**Tagline:** "No APIs, No $200 monthly bills. Enjoy an autonomous agent that thinks, browses the web, and codes for the sole cost of electricity."

### Core Capabilities

| Feature | Description |
|---------|-------------|
| **Autonomous Coding** | Write, execute, and debug code in multiple languages |
| **Web Browsing** | Search and interact with websites via Chrome |
| **Filesystem Access** | Navigate, read, and manage local files |
| **Voice Input/Output** | Speech-to-text with trigger word activation, text-to-speech responses |
| **Self-Correction** | Detects and fixes its own mistakes |
| **Session Memory** | Save and recover conversation sessions |
| **100% Local** | All processing on your hardware—no data leaves your machine |

### Hardware Requirements

| Model Size | Minimum GPU |
|------------|-------------|
| 7B Model | 8GB VRAM |
| 14B Model | 12GB VRAM (e.g., RTX 3060) |
| 32B Model | 24GB+ VRAM |

**Recommendation:** At least DeepSeek 14B; smaller models struggle with web browsing tasks.

### Quick Start

```bash
# Clone and setup
git clone https://github.com/Fosowl/agenticSeek.git
cd agenticSeek
mv .env.example .env

# Create virtual env
python3 -m venv agentic_seek_env
source agentic_seek_env/bin/activate

# Install
./install.sh

# Download model
ollama pull deepseek-r1:14b
ollama serve

# Start services and run
sudo ./start_services.sh
python3 main.py
```

### Provider Options

| Provider | Local? | Use Case |
|----------|--------|----------|
| `ollama` | Yes | Local Ollama instance |
| `server` | Yes | Remote server running LLM |
| `lm-studio` | Yes | LM Studio backend |
| `deepseek-api` | No | DeepSeek cloud API |
| `openai` | No | OpenAI-compatible APIs |

### Configuration

Key settings in `config.ini`:

```ini
[MAIN]
is_local = True
provider_name = ollama
provider_model = deepseek-r1:14b
provider_server_address = 127.0.0.1:11434
agent_name = Friday
work_dir = /Users/user/Documents/ai_folder
speak = False
listen = False
jarvis_personality = False

[BROWSER]
headless_browser = False
stealth_mode = False
```

### Voice Interaction

When `listen = True`:
1. Say agent name ("Friday") to wake
2. Speak your query clearly
3. End with confirmation phrase: "do it", "go ahead", "execute", "thanks", etc.

### Usage Examples

**Coding:**
- "Make a snake game in Python"
- "Find and debug the issues in my code"
- "Explain this function"

**Web Search:**
- "Do a web search and find out which are the best countries for solo-travel"
- "Search for the latest news about AI"

**Filesystem:**
- "List all the Python files in my project"
- "Find and organize my documents"

**Tip:** Be explicit about method. Don't say "What are good solo-travel countries?" — say "Do a web search and find..."

### When to Use AgenticSeek

**Good fit:**
- Want Manus-like capabilities without API costs
- Privacy-conscious—data stays local
- Have decent GPU hardware (12GB+ VRAM)
- Enjoy JARVIS/Friday aesthetic
- Want voice-controlled AI assistant

**Trade-offs:**
- Requires significant local compute
- Smaller models may struggle with complex tasks
- Early prototype—agent routing not always accurate
- ChromeDriver setup can be finicky
- No cloud backup/sync

### Comparison: Local Agent Alternatives

| Tool | Model Support | Voice | Web | Code | Privacy |
|------|---------------|-------|-----|------|---------|
| AgenticSeek | Ollama, LM Studio, APIs | Yes | Yes | Yes | Full local |
| Open Interpreter | Various | No | Limited | Yes | Local option |
| Aider | Various | No | No | Yes | Local option |
| FLUJO (above) | Various | No | Via MCP | Via MCP | Local |
| Jan.ai | Various | No | No | No | Full local |

### Related

- FLUJO (above) - Visual workflow builder, local-first
- Toolkami (above) - Minimal 7-tool agent
- DeepSeek R1 - The reasoning model AgenticSeek recommends
- `local-llm-tools.md` - Local LLM ecosystem overview

---

## DSPy: Programming LLMs Instead of Prompting

*Source: [DSPy Documentation](https://dspy.ai/) - Added: 2026-01-18*

### What It Is

DSPy (Declarative Self-improving Python) is a framework for programming language models rather than prompting them. Instead of brittle prompts, you write compositional Python code and use DSPy to teach your LM to deliver high-quality outputs.

**The core insight:** Maintaining prompts makes iteration hard—changing your LM, metrics, or pipeline forces you to tinker with strings or data. DSPy decouples defining LM systems from messy incidental choices about specific LMs or prompting strategies.

### Three Core Principles

**1. Modules: Describe AI behavior as code, not strings**

For every AI component in your system:
- Specify input/output behavior as a **signature**
- Select a **module** to assign a strategy for invoking your LM
- DSPy expands signatures into prompts and parses typed outputs

This makes AI systems ergonomic, portable, and optimizable.

**2. Optimizers: Tune prompts and weights automatically**

Given representative inputs and a quality metric, DSPy optimizers can:
- Synthesize good few-shot examples for every module (`dspy.BootstrapRS`)
- Propose and explore better natural-language instructions (`dspy.MIPROv2`)
- Build datasets for modules and fine-tune LM weights (`dspy.BootstrapFinetune`)

**3. Ecosystem: Open-source, modular advancement**

DSPy's modular paradigm enables distributed improvement of:
- Compositional architectures
- Inference-time strategies
- Optimizers for LM programs

Programs get better over time by applying the latest optimizers or modules.

### History and Research

The DSPy research effort started at Stanford NLP in February 2022, building on early compound LM systems like ColBERT-QA, Baleen, and Hindsight.

**Timeline:**
- Feb 2022: Research started at Stanford NLP
- Dec 2022: First version released as "DSP"
- Oct 2023: Evolved into "DSPy"
- 250+ contributors since then

**Notable work from the community:**
- **Optimizers:** MIPROv2, BetterTogether, LeReT
- **Architectures:** STORM, IReRa, DSPy Assertions
- **Applications:** PAPILLON, PATH, WangLab@MEDIQA, UMD's Prompting Case Study, Haize's Red-Teaming Program

### When to Use DSPy

**Good fit:**
- Building compound LM systems (classifiers, RAG pipelines, agent loops)
- Need to iterate quickly on AI behavior
- Want automatic prompt optimization
- Changing models frequently (portability matters)
- Building production systems that need reliability

**Trade-offs:**
- Learning curve vs. direct prompting
- Additional abstraction layer
- May be overkill for simple single-prompt use cases

### Comparison with Other Approaches

| Approach | Abstraction | Optimization | Portability | Best For |
|----------|-------------|--------------|-------------|----------|
| Direct prompting | None | Manual | Low | Simple, one-off tasks |
| LangChain | Chains/tools | Manual | Medium | Tool integration, RAG |
| DSPy | Signatures/modules | Automatic | High | Modular, optimizable systems |
| Custom code | Full control | Manual | Variable | Specific requirements |

### Key Concepts

**Signatures:** Declarative specs of input/output behavior
```python
# Example: Question answering signature
class QA(dspy.Signature):
    question = dspy.InputField()
    answer = dspy.OutputField()
```

**Modules:** Strategies for invoking LMs
- `dspy.Predict` - Basic prediction
- `dspy.ChainOfThought` - Step-by-step reasoning
- `dspy.ReAct` - Reasoning + acting

**Optimizers:** Automatic tuning
- `BootstrapRS` - Few-shot example synthesis
- `MIPROv2` - Instruction optimization
- `BootstrapFinetune` - Weight fine-tuning

### Resources

- Documentation: https://dspy.ai/
- GitHub: https://github.com/stanfordnlp/dspy
- Discord: Community support and discussions

### Related

- LangChain/LangGraph - Alternative LLM framework (more tool-focused)
- Mastra (above) - TypeScript agent framework with MCP integration
- `prompt-engineering.md` - Traditional prompt techniques (what DSPy aims to replace)

---

## Voiceflow: Visual Conversation Design Platform

*Source: [Voiceflow Customer Experience](https://www.voiceflow.com/solutions/customer-experience) - Added: 2026-01-18*

### What It Is

Voiceflow is a platform for teams to design, test, and launch conversational AI agents (chat and voice). It emphasizes visual conversation design, collaborative workflows, and avoiding vendor lock-in.

### Core Capabilities

| Feature | Description |
|---------|-------------|
| **Knowledge Training** | Train AI agent on product catalogs, developer docs, any knowledge source |
| **Multi-Step Automation** | Layer business logic to execute complex actions (purchases, onboarding) |
| **API Integration** | Connect business and user data from any source to trigger personalized experiences |
| **Multi-LLM Control** | Manage prompting, system prompts, and business logic across different models |
| **Visual Flow Builder** | Design conversation flows visually with team collaboration |

### Enterprise Features

- Centralized platform for building, scaling, and collaborating on AI products
- Accelerated sprint cycles for shipping AI features
- Model-agnostic architecture—adapt to changing LLM/NLU technologies without lock-in
- API-first integrations with secure guardrails

### Use Cases

1. **Customer Support** - Automate tickets, enable live agent handoff, solve complex questions
2. **In-App Copilots** - Employee onboarding, HR FAQs, team activation
3. **Revenue Operations** - Accelerate manual revenue collection, protect revenue with custom agents
4. **Custom AI Agents** - Guide users through tools, recommend products, authenticate customers

### When to Use Voiceflow

**Good fit:**
- Need visual conversation flow design (non-engineers involved)
- Multi-channel deployment (chat + voice)
- Enterprise requiring centralized AI platform management
- Want model flexibility without vendor lock-in
- Teams that need to iterate quickly on conversational AI

**Trade-offs:**
- Platform dependency vs. building custom
- May be overkill for simple single-purpose bots
- Enterprise features likely require paid tier

### Comparison with Other Platforms

| Platform | Visual Builder | Voice | Multi-LLM | Best For |
|----------|----------------|-------|-----------|----------|
| Voiceflow | Yes | Yes | Yes | Visual design, enterprise teams |
| ChatBotKit | Limited | No | Yes | Quick deployment, messaging apps |
| Botpress | Yes | Limited | Yes | Open-source, self-hosted |
| Dialogflow | Yes | Yes | Google-only | Google ecosystem |
| Amazon Lex | Limited | Yes | AWS-only | AWS ecosystem |

### Personal Notes

Voiceflow's emphasis on avoiding vendor lock-in is notable—they explicitly position as "bet on AI, not single vendors." This aligns with the general pattern of preferring model-agnostic architectures. The visual flow builder could be useful for:
- Educational tools for kids (drag-and-drop conversation design)
- Home automation voice interfaces
- Family-facing assistants where the interaction should be conversational

### Related

- ChatBotKit (above) - Similar platform, more messaging-focused
- Voice Agents section (above) - For pure voice/call center use cases
- `ag-ui-protocol.md` - Agent-User Interaction Protocol (related ecosystem)

---

## Fast GraphRAG: Lightweight Graph-Based RAG

*Source: [GitHub - circlemind-ai/fast-graphrag](https://github.com/circlemind-ai/fast-graphrag) - Added: 2026-01-18*

### What It Is

Fast GraphRAG is a streamlined framework for high-precision retrieval workflows that uses knowledge graphs instead of traditional vector-only approaches. It provides interpretable, agent-driven retrieval with automatic graph generation.

**Key claim:** 6x cost savings vs. Microsoft's graphrag ($0.08 vs $0.48 on The Wizard of Oz), with savings improving at scale.

### Core Features

| Feature | Description |
|---------|-------------|
| **Interpretable Knowledge** | Human-navigable graphs that can be queried, visualized, and updated |
| **Cost Efficient** | Designed to run at scale without heavy resource requirements |
| **Dynamic Graphs** | Automatically generate and refine graphs to fit domain/ontology needs |
| **Incremental Updates** | Real-time updates as data evolves |
| **PageRank Exploration** | Uses PageRank-based graph exploration for enhanced accuracy |
| **Async & Typed** | Fully asynchronous with complete type support |

### Quick Start

```bash
pip install fast-graphrag
export OPENAI_API_KEY="sk-..."
```

```python
from fast_graphrag import GraphRAG

DOMAIN = "Analyze this story and identify the characters. Focus on how they interact with each other, the locations they explore, and their relationships."

EXAMPLE_QUERIES = [
    "What is the significance of Christmas Eve in A Christmas Carol?",
    "How does the setting of Victorian London contribute to the story's themes?",
]

ENTITY_TYPES = ["Character", "Animal", "Place", "Object", "Activity", "Event"]

grag = GraphRAG(
    working_dir="./book_example",
    domain=DOMAIN,
    example_queries="\n".join(EXAMPLE_QUERIES),
    entity_types=ENTITY_TYPES
)

with open("./book.txt") as f:
    grag.insert(f.read())

print(grag.query("Who is Scrooge?").response)
```

Knowledge persists automatically when reinitializing from the same working directory.

### When to Use Fast GraphRAG

**Good fit:**
- Need interpretable, debuggable knowledge retrieval
- Want to visualize relationships in your data
- Cost-sensitive RAG applications
- Domains with clear entity types and relationships (stories, documentation, knowledge bases)
- Incremental data ingestion (documents added over time)

**Trade-offs:**
- Requires defining domain, example queries, and entity types upfront
- OpenAI dependency (no local model support mentioned)
- Graph generation adds initial processing overhead
- Less mature than vector-only RAG approaches

### Graph RAG vs. Vector RAG

| Approach | Interpretability | Cost | Relationship Queries | Setup |
|----------|------------------|------|---------------------|-------|
| Vector RAG | Low (embeddings) | Medium | Poor | Simple |
| Microsoft GraphRAG | High | Higher | Good | Complex |
| Fast GraphRAG | High | Lower | Good | Medium |
| Hybrid (vector + graph) | Medium | Variable | Good | Complex |

### When Graph RAG Shines

1. **Multi-hop questions** - "How are Character A and Character C connected?" requires traversing relationships
2. **Domain exploration** - Understanding entity relationships, not just retrieving similar chunks
3. **Audit/debugging** - Need to explain *why* something was retrieved
4. **Evolving knowledge** - Incremental updates without full re-embedding

### Comparison with Other RAG Approaches

| Tool | Type | Strength | Cost |
|------|------|----------|------|
| Fast GraphRAG | Graph | Interpretable, cost-efficient | Low |
| Microsoft GraphRAG | Graph | Feature-rich, enterprise | High |
| LlamaIndex | Vector + Graph | Flexible, many integrations | Medium |
| LangChain RAG | Vector | Ecosystem, tooling | Medium |
| Airweave (above) | Vector | Multi-source sync | Medium |

### Managed Service

Circlemind offers a managed service with 100 free requests/month, then usage-based pricing. Useful for teams that want graph RAG without infrastructure management.

### Related

- Agentic RAG on Bedrock (above) - AWS-native RAG approach
- Airweave (above) - Multi-source search for agents
- EnrichMCP (above) - Semantic layer for MCP data access

---

## Experts.js: Multi-Agent Systems with OpenAI Assistants

*Source: [GitHub - metaskills/experts](https://github.com/metaskills/experts) - Added: 2026-01-18*

### What It Is

Experts.js is a framework for creating and deploying OpenAI's Assistants and linking them together as Tools to create "Panel of Experts" multi-agent systems with expanded memory and attention to detail.

**The core insight:** The Assistants API introduces managed threads (context windows), file handling, and 128-tool support. Experts.js removes the complexity of managing Run objects and allows Assistants to be linked as Tools—enabling orchestration patterns.

### Key Capabilities

| Feature | Description |
|---------|-------------|
| **Assistants as Tools** | Link Assistants together—each Tool is an LLM-backed Assistant with specialized roles |
| **Managed Threads** | Context windows with message/file storage, automatic parent→child thread relationships |
| **Large Instructions** | Up to 256,000 character instructions per Assistant |
| **Vector Store** | File search on up to 10,000 files per Assistant |
| **128 Tools** | Support for many tools per Assistant |
| **Streaming Events** | Real-time text, image, and tool outputs via server-sent events |

### Three Core Objects

```javascript
import { Assistant, Tool, Thread } from "experts";
```

- **Assistants** - Main AI agents with name, description, instructions
- **Tools** - Specialized Assistants that perform tasks for parent Assistants
- **Threads** - Managed context windows storing messages and files

### Basic Usage

```javascript
class MyAssistant extends Assistant {
  constructor() {
    const name = "My Assistant";
    const description = "...";
    const instructions = "..."
    super(name, description, instructions, {
      model: "gpt-4-turbo",
      tools: [{ type: "file_search" }],
      temperature: 0.1,
      tool_resources: {
        file_search: {
          vector_store_ids: [process.env.VECTOR_STORE_ID],
        },
      },
    });
  }
}

const thread = Thread.create();
const assistant = await MyAssistant.create();
const output = await assistant.ask("Say hello.", thread.id);
```

The `create()` function finds or creates the assistant by name and updates configurations.

### Assistants as Tools Pattern

The key architectural pattern—Tools are Assistants that can be called by parent Assistants:

```javascript
class EchoTool extends Tool {
  constructor() {
    super(name, description, instructions, {
      parentsTools: [
        {
          type: "function",
          function: {
            name: EchoTool.toolName,  // Critical: uses toolName getter
            description: description,
            parameters: {
              type: "object",
              properties: { message: { type: "string" } },
              required: ["message"],
            },
          },
        },
      ],
    });
  }
}

class MainAssistant extends Assistant {
  constructor() {
    super(name, description, instructions);
    this.addAssistantTool(EchoTool);  // Add Tool to Assistant
  }
}
```

**Important:** Tool class names are converted to snake_case (e.g., `ProductsOpenSearchTool` → `products_open_search`) and help the model decide which tool to call.

### Streaming Events

```javascript
const assistant = await MainAssistant.create();
assistant.on("textDelta", (delta, _snapshot) => {
  process.stdout.write(delta.value);
});

// Async events (after Run completes)
assistant.on("endAsync", async (metadata) => {
  await metadata.stream.finalMessages();
});
```

**Event types:**
- Standard: `event`, `textDelta`, `textDone`, `imageFileDone`, `toolCallDelta`, `runStepDone`, `toolCallDone`, `end`
- Async: `textDoneAsync`, `imageFileDoneAsync`, `runStepDoneAsync`, `toolCallDoneAsync`, `endAsync`

### Non-LLM Tools

For tools that don't need LLM backing (e.g., pure computation):

```javascript
class AnswerTwoTool extends Tool {
  constructor() {
    super(name, description, instructions, {
      llm: false,  // Disable LLM
      parentsTools: [...],
    });
  }
  async ask(message) {
    return computeAnswer(message);  // Return value becomes tool output
  }
}
```

### Controlling Tool Output

LLM-backed Tools can control what gets sent back to parent:

```javascript
// Option 1: Transform LLM output via answered()
async answered(output) {
  const args = JSON.parse(output);
  return await this.opensearchQuery(args);  // Return query results, not LLM text
}

// Option 2: Redirect tool outputs to parent
super(name, description, instructions, {
  outputs: "tools",  // Parent receives this Tool's tool outputs
  parentsTools: [...],
});
```

### Thread Management

Experts.js manages threads automatically to avoid locking issues:

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│ User Thread     │────▶│ Assistant       │────▶│ Tool Thread     │
│ (stored client) │     │ (finds/creates) │     │ (auto-managed)  │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

Parent→child thread relationships stored in OpenAI's thread metadata.

### Example: Three-Tier Agent System

```
┌─────────────────────┐
│ Company Assistant   │  ← Main entry point
└──────────┬──────────┘
           │
┌──────────▼──────────┐
│ Products Tool       │  ← Product catalog specialist
└──────────┬──────────┘
           │
┌──────────▼──────────┐
│ OpenSearch Tool     │  ← Converts queries to OpenSearch
└─────────────────────┘
```

Can answer: "Show me a bar chart with totals of all top level categories" or "Find men's accessories for a sophisticated comic book enthusiast."

### When to Use Experts.js

**Good fit:**
- Building multi-agent systems with OpenAI Assistants API
- Need managed context windows (threads) across agents
- Want file search/vector store integration
- Complex orchestration with specialized agent roles
- JavaScript/TypeScript environment

**Trade-offs:**
- OpenAI-only (no model portability)
- Managed threads mean less control over context
- Class-based ES6 pattern may not fit all codebases
- Assistants API has its own pricing/latency characteristics

### Comparison with Other Multi-Agent Frameworks

| Framework | Language | Model Support | Threads | Best For |
|-----------|----------|---------------|---------|----------|
| Experts.js | JS/TS | OpenAI only | Managed | OpenAI-native multi-agent |
| LangGraph | Python | Multi-model | Custom | Complex state machines |
| CrewAI | Python | Multi-model | Custom | Role-based collaboration |
| Mastra | TypeScript | Multi-model | Custom | MCP integration |
| AutoGen | Python | Multi-model | Custom | Research, conversations |

### Installation

```bash
npm install experts
```

### Related

- OpenAI Assistants API - The underlying API
- Mastra (above) - TypeScript framework with MCP focus
- LangGraph - Python alternative for complex agent graphs
- `coding-agent-tools.md` - Development agent ecosystem

---

## Dify: Open-Source LLM App Development Platform

*Source: [GitHub - langgenius/dify](https://github.com/langgenius/dify) - Added: 2026-01-19*

### What It Is

Dify is an open-source LLM app development platform with an intuitive visual interface. It combines AI workflow building, RAG pipelines, agent capabilities, model management, and observability features—letting you go from prototype to production quickly.

**Key differentiator:** Visual workflow builder combined with comprehensive model support and LLMOps observability. Bridges the gap between prototyping and production.

### Core Features

| Feature | Description |
|---------|-------------|
| **Visual Workflow Builder** | Design AI workflows on a canvas, connecting components visually |
| **Model Support** | Hundreds of proprietary/open-source LLMs (GPT, Mistral, Llama, any OpenAI-compatible API) |
| **Prompt IDE** | Craft prompts, compare model performance, add features like TTS |
| **RAG Pipeline** | Document ingestion to retrieval, with PDF/PPT extraction out of the box |
| **Agent Capabilities** | Define agents via Function Calling or ReAct; 50+ built-in tools (Google Search, DALL-E, Stable Diffusion, WolframAlpha) |
| **LLMOps** | Monitor logs and performance, improve prompts/datasets based on production data |
| **Backend-as-a-Service** | All features available via API for integration into existing systems |

### Quick Start

```bash
cd docker
docker compose up -d
```

Access dashboard at `http://localhost/install` and complete initialization.

### Deployment Options

1. **Dify Cloud** - Managed hosting with same capabilities as self-hosted
2. **Self-hosted** - Docker Compose or Kubernetes (community Helm charts available)
3. **Enterprise** - Dedicated support and compliance features

### When to Use Dify

**Good fit:**
- Need visual workflow builder for AI apps
- Want RAG with minimal infrastructure setup
- Building agents with multiple tool integrations
- Require observability/monitoring in production
- Team includes non-engineers who need to participate in workflow design
- Rapid prototyping with path to production

**Trade-offs:**
- Another platform to manage vs. code-first approaches
- Visual builder may be limiting for complex logic
- Self-hosting requires Docker/K8s knowledge
- Feature overlap with other tools in the ecosystem

### Comparison with Other Platforms

| Platform | Visual Builder | RAG | Agents | Self-Host | Best For |
|----------|----------------|-----|--------|-----------|----------|
| Dify | Yes | Built-in | Yes | Yes | Full-stack LLM apps |
| FLUJO (above) | Yes | Via MCP | Via MCP | Yes (local) | Local experimentation |
| LangChain/LangGraph | No (code) | Framework | Yes | N/A | Python developers |
| Flowise | Yes | Built-in | Limited | Yes | No-code LangChain |
| n8n AI | Yes | Via nodes | Limited | Yes | General automation |

### Architecture Pattern

Dify serves as a middle layer between LLM providers and your application:

```
┌─────────────────┐     ┌──────────────────┐     ┌───────────────┐
│ Your App        │────▶│ Dify             │────▶│ LLM Providers │
│ (via API)       │     │ (Orchestration)  │     │ (GPT, Claude, │
└─────────────────┘     └──────────────────┘     │  Llama, etc.) │
                               │                 └───────────────┘
                               ▼
                        ┌──────────────────┐
                        │ Knowledge Base   │
                        │ (RAG/Vector DB)  │
                        └──────────────────┘
```

### Integration with Memory Tools

Dify has a LongTermMemory plugin that uses the Knowledge API for per-user memory (requires GPT-4+). This allows agents to remember context across sessions.

### Resources

- Documentation: https://docs.dify.ai/
- GitHub: https://github.com/langgenius/dify
- Community: GitHub Discussions, Discord

### Related

- FLUJO (above) - Local-first visual workflow builder
- Voiceflow (above) - Visual conversation design (more voice-focused)
- `mcp-protocol-adoption.md` - MCP ecosystem (Dify can integrate via tools)

---

## AIOS: LLM Agent Operating System

*Source: [GitHub - agiresearch/AIOS](https://github.com/agiresearch/AIOS) - Added: 2026-01-18*

### What It Is

AIOS (LLM Agent Operating System) is a research project from AGI Research Lab that embeds large language models into operating systems, treating the LLM as the "brain" of the OS. The project aims to create an operating system "with soul" as a step toward AGI.

**Research focus:** Rather than building agents on top of existing infrastructure, AIOS explores what happens when you treat the OS itself as the agent orchestration layer.

### Core Capabilities

| Feature | Description |
|---------|-------------|
| **Resource Allocation** | OS-level optimization of resources across agents |
| **Context Switching** | Facilitate context switching between agents (like process scheduling) |
| **Concurrent Execution** | Enable multiple agents to run concurrently |
| **Tool Service** | Provide toolkits for agent developers |
| **Access Control** | Maintain access control for agents |

### Architectural Approach

AIOS treats agents like applications running on an operating system:
- **LLM as OS brain** - The LLM makes scheduling and resource decisions
- **Agents as apps** - Each agent is a "process" managed by the OS
- **Context as memory** - Agent context is managed like process memory

This is philosophically different from frameworks like LangChain or CrewAI which layer agents on top of existing OS abstractions.

### Quick Start

```bash
git clone https://github.com/agiresearch/AIOS.git
pip install -r requirements.txt

# Set up model (supports Gemma, Mixtral, Gemini-pro)
export HUGGING_FACE_HUB_TOKEN=<token>
export HF_HOME=<cache_dir>

# Interactive mode (Gemini-pro)
python main.py --llm_name gemini-pro

# Deployment mode (logs to files)
python simulator.py --llm_name gemini-pro --scheduler_log_mode file --agent_log_mode file
```

### Model Requirements

| Model | GPU Memory Required |
|-------|---------------------|
| gemma-2b-it | ~24GB |
| mixtral-8x7b-it | ~144GB (3x 48GB) |
| gemini-pro | API-based (no local GPU) |

### When to Consider AIOS

**Good fit:**
- Research into agent orchestration at OS level
- Exploring AGI architectures
- Understanding how LLMs can manage system resources
- Academic exploration of "LLM as OS" paradigm

**Trade-offs:**
- Research project, not production-ready
- High GPU requirements for local models
- Less practical than framework approaches for building actual agents
- Evolving rapidly (codebase structure may change)

### The "OS as Agent Orchestrator" Philosophy

The key insight from AIOS research papers:
- Traditional agents are applications running on generic OSes
- AIOS asks: what if the OS itself understood agent semantics?
- Potential benefits: better resource sharing, native context management, coordinated tool access

This connects to the broader question of whether LLM-native infrastructure (vs. adapted traditional infrastructure) will be a meaningful distinction as the field matures.

### Related Papers

- "AIOS: LLM Agent Operating System" (arXiv:2403.16971, March 2024)
- "LLM as OS, Agents as Apps: Envisioning AIOS, Agents and the AIOS-Agent Ecosystem" (arXiv:2312.03815, Dec 2023)

### Related

- Dify (above) - Practical platform for building LLM apps
- AgenticSeek (above) - Local agent alternative (application-level, not OS-level)
- `local-llm-tools.md` - Local LLM ecosystem

---

## Langroid: Multi-Agent LLM Framework

*Source: [GitHub - langroid/langroid](https://github.com/langroid/langroid) - Added: 2026-01-18*

Python framework for building LLM applications using multi-agent programming. Developed by researchers from CMU and UW-Madison. Notable for **not using LangChain** - it's a ground-up design with Actor Framework-inspired message passing.

### Core Concepts

| Concept | Description |
|---------|-------------|
| **Agent** | Encapsulates LLM, conversation state, optional vector-store, and tools |
| **Task** | Wraps an Agent with instructions/goals; orchestrates multi-agent interactions |
| **Message Passing** | Agents act as message transformers, inspired by Actor Framework |
| **Responders** | Each Agent has 3 responder methods: LLM, Agent, User |

### Quick Start

```bash
pip install langroid  # Requires Python 3.11+
pip install langroid[hf-embeddings]  # For HuggingFace embeddings
```

```python
import langroid as lr
import langroid.language_models as lm

# Configure LLM
llm_cfg = lm.OpenAIGPTConfig(
    chat_model=lm.OpenAIChatModel.GPT4_TURBO,  # or "ollama/mistral"
)

# Direct LLM usage
mdl = lm.OpenAIGPT(llm_cfg)
response = mdl.chat("What is the capital of Ontario?", max_tokens=10)

# Agent with conversation state
agent = lr.ChatAgent(lr.ChatAgentConfig(llm=llm_cfg))
agent.llm_response("What is the capital of China?")
agent.llm_response("And India?")  # Maintains state

# Interactive task
task = lr.Task(agent, name="Bot", system_message="You are a helpful assistant")
task.run("Hello")
```

### Multi-Agent Example

```python
# Teacher-Student collaboration
teacher_agent = lr.ChatAgent(agent_cfg)
teacher_task = lr.Task(
    teacher_agent, name="Teacher",
    system_message="Ask concise math questions, give feedback. Start with a question."
)

student_agent = lr.ChatAgent(agent_cfg)
student_task = lr.Task(
    student_agent, name="Student",
    system_message="Concisely answer the teacher's questions.",
    single_round=True,
)

teacher_task.add_sub_task(student_task)
teacher_task.run()
```

### Specialized Agents

| Agent Type | Use Case |
|------------|----------|
| **DocChatAgent** | RAG with vector-store, source citation, document sharding |
| **TableChatAgent** | Query tabular data (CSV, DataFrame) via Pandas code generation |
| **SQLChatAgent** | Chat with SQL databases |

### Tools/Function Calling

Uses Pydantic for schema definition (no JSON writing required). Malformed LLM JSON gets Pydantic errors sent back for auto-correction.

```python
class ProbeTool(lr.agent.ToolMessage):
    request: str = "probe"  # Handler method name
    purpose: str = "Find how many numbers <= specified number"
    number: int

class SpyGameAgent(lr.ChatAgent):
    def __init__(self, config):
        super().__init__(config)
        self.numbers = [3, 4, 8, 11, 15, 25, 40, 80, 90]

    def probe(self, msg: ProbeTool) -> str:
        return str(len([n for n in self.numbers if n <= msg.number]))

agent = SpyGameAgent(lr.ChatAgentConfig(use_functions_api=True))
agent.enable_message(ProbeTool)
```

### Key Features

- **LLM Support**: OpenAI, local models (via proxy), LiteLLM (hundreds of providers)
- **Vector Stores**: LanceDB (default), Qdrant, Chroma
- **Caching**: Redis, Momento
- **Observability**: Detailed logs, message lineage/provenance
- **RAG**: Built-in DocChatAgent with retrieval and source citation

### Comparison to Other Frameworks

| Feature | Langroid | LangChain | AutoGen | MetaGPT |
|---------|----------|-----------|---------|---------|
| Foundation | Actor-inspired | Chain of calls | Conversations | SOPs/Roles |
| Pydantic Tools | Native | Via OpenAI | Yes | Yes |
| No LangChain | Yes | - | Yes | Yes |
| Academic Origin | CMU/UW-Madison | Startup | Microsoft | ICLR Paper |
| Task Delegation | Hierarchical | Sequential | Conversation | Pipeline |

### When to Use Langroid

**Good fit:**
- Multi-agent systems with message passing paradigm
- RAG applications with source citation
- Structured extraction via function calling
- Teams familiar with Actor model concepts
- Want to avoid LangChain dependency

**Trade-offs:**
- Less ecosystem/community than LangChain
- Python 3.11+ requirement
- Learning curve for Actor-style thinking

### Related

- AutoGen (above) - Microsoft's conversation-based multi-agent
- MetaGPT (above) - Role-based software company simulation
- DSPy (above) - Programming LLMs instead of prompting

---

## CrewAI: Role-Playing Multi-Agent Orchestration

*Source: [CrewAI GitHub](https://github.com/joaomdmoura/crewAI) - Added: 2026-01-18*

CrewAI is a framework for orchestrating autonomous AI agents that assume roles, share goals, and collaborate on complex tasks. Designed for production use with dynamic, adaptable processes.

### Core Concept

Agents form "crews" - each agent has:
- **Role**: Job title/function (e.g., "Senior Research Analyst")
- **Goal**: What they're trying to achieve
- **Backstory**: Context that shapes their behavior
- **Tools**: External capabilities (search, APIs, etc.)

Agents can autonomously delegate tasks to each other, enabling emergent collaboration.

### Quick Start

```bash
pip install crewai
pip install 'crewai[tools]'  # includes crewai-tools
```

### Basic Example

```python
import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool

os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY"
os.environ["SERPER_API_KEY"] = "YOUR_SERPER_KEY"

search_tool = SerperDevTool()

# Define agents
researcher = Agent(
    role='Senior Research Analyst',
    goal='Uncover cutting-edge developments in AI',
    backstory="""You work at a leading tech think tank.
    Your expertise lies in identifying emerging trends.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool]
)

writer = Agent(
    role='Tech Content Strategist',
    goal='Craft compelling content on tech advancements',
    backstory="""You are a renowned Content Strategist.
    You transform complex concepts into compelling narratives.""",
    verbose=True,
    allow_delegation=True
)

# Define tasks
task1 = Task(
    description="Analyze latest AI advancements in 2024. Identify key trends.",
    expected_output="Full analysis report in bullet points",
    agent=researcher
)

task2 = Task(
    description="Using insights provided, write an engaging blog post.",
    expected_output="Full blog post of at least 4 paragraphs",
    agent=writer
)

# Run the crew
crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    verbose=2
)

result = crew.kickoff()
```

### Key Features

- **Role-based design**: Customize agents with specific personas and tools
- **Autonomous delegation**: Agents delegate and inquire among themselves
- **Flexible task management**: Dynamic tool assignment per task
- **Process types**: Sequential (default) and Hierarchical (auto-assigns manager)
- **Output handling**: Save to file, parse as Pydantic or JSON
- **Open-source model support**: Works with OpenAI, Ollama, local models

### Local Model Support

```python
import os
os.environ["OPENAI_API_BASE"] = 'http://localhost:11434/v1'
os.environ["OPENAI_MODEL_NAME"] = 'openhermes'
os.environ["OPENAI_API_KEY"] = 'sk-dummy'  # Ollama doesn't need real key
```

### Process Types

| Process | Description |
|---------|-------------|
| Sequential | Tasks executed in order, one after another |
| Hierarchical | Manager agent auto-created to coordinate delegation |
| Consensual | (In development) |
| Autonomous | (In development) |

### Telemetry Note

CrewAI collects anonymous usage data (versions, agent counts, roles, tool names). Does NOT collect prompts, task descriptions, backstories, API keys, or processed data. Opt-in full telemetry via `share_crew=True`.

### Example Use Cases

- Smart assistant platforms
- Automated customer service ensembles
- Multi-agent research teams
- Content generation pipelines

### Comparison to Other Frameworks

| Feature | CrewAI | AutoGen | MetaGPT | LangGraph |
|---------|--------|---------|---------|-----------|
| Paradigm | Role-based crews | Conversations | SOP-driven roles | State graphs |
| Delegation | Built-in, autonomous | Via conversation | Pipeline-based | Via nodes |
| Best For | Task-focused teamwork | Research, chat | Software generation | Complex workflows |
| Process Control | Sequential/Hierarchical | Flexible | Structured pipeline | Graph-based |

### When to Use CrewAI

**Good fit:**
- Task-focused multi-agent collaboration
- Role-playing scenarios with clear agent personas
- Production systems needing structured agent teams
- Teams wanting simpler setup than LangGraph

**Trade-offs:**
- Less granular state control than LangGraph
- Process types still maturing (consensual/autonomous in development)
- Relies on backstory prompts for agent behavior shaping
