---
type: link
source: notion
url: https://github.com/omnara-ai/omnara
notion_type: Software Repo
tags: ['Running']
created: 2025-08-13T02:52:00.000Z
---

# GitHub - omnara-ai/omnara: Omnara (YC S25) - Talk to Your AI Agents from Anywhere!

## Overview (from Notion)
- Omnara provides a mobile solution for managing AI agents, allowing for remote monitoring and interaction—ideal for a busy lifestyle balancing family and work.
- The real-time visibility into AI tasks means you can oversee projects while engaging in family activities, reducing the stress of being tied to your desk.
- Unique features like smart notifications and interactive Q&A facilitate immediate responses to your AI's needs, enhancing productivity without sacrificing personal time.
- The platform's mobile-first design aligns well with the fast-paced urban life, enabling seamless transitions from work to family responsibilities.
- Consider the implications of relying on AI for coding tasks—could it free up more time for creative pursuits or family outings?
- An alternate view might question the reliance on AI—could it create a disconnect with hands-on coding experience and mentorship for future generations?
- The pricing structure offers flexibility, making it accessible for startups or individual developers looking to leverage cutting-edge AI without hefty investments.

## AI Summary (from Notion)
Omnara is a mobile platform that enhances communication with AI agents, allowing users to monitor their activities in real-time, respond to queries instantly, and manage tasks from anywhere. Key features include real-time monitoring, interactive Q&A, smart notifications, and a universal dashboard for all agents. It supports various use cases such as code reviews, debugging production issues, and managing data migrations. The platform offers a free tier and paid plans for additional features and support.

## Content (from Notion)

# Omnara - Mission Control for Your AI Agents 🚀

Your AI workforce launchpad, in your pocket.

📱 Download iOS App • 🌐 Try Web Dashboard • ⭐ Star on GitHub

## 🚀 What is Omnara?

Omnara transforms your AI agents (Claude Code, Cursor, GitHub Copilot, and more) from silent workers into communicative teammates. Get real-time visibility into what your agents are doing, respond to their questions instantly, and guide them to success - all from your phone.

### ✨ Key Features

### 🎬 See It In Action

> 

## 💡 Why Omnara?

We built Omnara because we were tired of:

- ❌ Starting long agent jobs and finding them stuck hours later
- ❌ Missing critical questions that blocked progress
- ❌ Having no visibility into what our AI was actually doing
- ❌ Being tied to our desks while agents worked
Now you can:

- ✅ Launch agents and monitor them from anywhere
- ✅ Get push notifications when input is needed
- ✅ Send real-time feedback to guide your agents
- ✅ Have confidence your AI workforce is productive
## 🎯 Real-World Use Cases

### 🔍 Code Review Assistant

Launch Claude to review PRs while you're at lunch. Get notified only if it needs clarification on architectural decisions.

### 🚨 Production Firefighter

Debug production issues from your phone at 2am. See exactly what your agent is investigating and guide it to the right logs.

### 📊 Data Pipeline Guardian

Start a 6-hour data migration before leaving work. Get alerts if anything looks suspicious, approve schema changes on the go.

### 🏗️ Refactoring Copilot

Let Claude refactor that legacy module while you're in meetings. Answer its questions about business logic without context switching.

### 🧪 Test Suite Doctor

Have Claude fix failing tests overnight. Wake up to either green builds or specific questions about expected behavior.

## 🏗️ Architecture Overview

Omnara provides a unified platform for monitoring and controlling your AI agents:

Loading

```plain text
graph TB
    subgraph "Your AI Agents"
        A[🤖 AI Agents<br/>Claude Code, Cursor, etc.]
    end

    subgraph "Omnara Platform"
        API[🌐 API Server]
        DB[(📊 PostgreSQL)]
        NOTIFY[🔔 Notification Service<br/>Push/Email/SMS]
    end

    subgraph "Your Devices"
        M[📱 Mobile App]
        W[💻 Web Dashboard]
    end

    A -->|Send updates| API
    API -->|Store data| DB
    API -->|Trigger notifications| NOTIFY
    NOTIFY -->|Alert users| M
    DB -->|Real-time sync| M
    DB -->|Real-time sync| W
    M -->|User responses| API
    W -->|User responses| API
    API -->|Deliver feedback| A

    style A fill:#e3f2fd,stroke:#1976d2,stroke-width:3px
    style API fill:#c8e6c9,stroke:#388e3c,stroke-width:2px
    style DB fill:#ffccbc,stroke:#d84315,stroke-width:2px
    style NOTIFY fill:#fff59d,stroke:#f57f17,stroke-width:2px
    style M fill:#f8bbd0,stroke:#c2185b,stroke-width:3px
    style W fill:#f8bbd0,stroke:#c2185b,stroke-width:3px

```

### 🚀 How It Works

1. Connect Your Agent → Install Omnara SDK or wrapper

2. Get Real-Time Updates → See every step your agent takes

3. Respond Instantly → Answer questions from anywhere

### 🔄 Two Ways to Use Omnara

### 🔧 Technical Stack

- Backend: FastAPI with separate read/write servers for optimal performance
- Frontend: React (Web) + React Native (Mobile)
- Protocol: Model Context Protocol (MCP) + REST API
- Database: PostgreSQL with SQLAlchemy ORM
- Auth: Dual JWT system (Supabase for users, custom for agents)
## 🚀 Quick Start

### Option 1: Monitor Your Claude Sessions

See what Claude is doing in real-time:

1. Install Omnara: 
1. Start monitoring: 
1. Authenticate in your browser (opens automatically)
1. See everything your agent does in the Omnara dashboard!
### Option 2: Launch Agents Remotely

Trigger Claude from your phone:

1. Start the server on your computer: 
1. Set up your agent in the mobile app with the webhook URL shown
1. Launch agents from anywhere - beach, coffee shop, bed!
### For Developers

## 🔧 Advanced Usage (Without CLI)

> 

### Method 1: Direct Wrapper Script

Run the monitoring wrapper directly (what omnara does under the hood):

```plain text
# Basic usage
python -m webhooks.claude_wrapper_v3 --api-key YOUR_API_KEY

# With git diff tracking
python -m webhooks.claude_wrapper_v3 --api-key YOUR_API_KEY --git-diff

# Custom API endpoint (for self-hosted)
python -m webhooks.claude_wrapper_v3 --api-key YOUR_API_KEY --base-url https://your-server.com
```

### Method 2: Manual MCP Configuration

For custom MCP setups, you can configure manually:

```plain text
{
  "mcpServers": {
    "omnara": {
      "command": "pipx",
      "args": ["run", "--no-cache", "omnara", "mcp", "--api-key", "YOUR_API_KEY"]
    }
  }
}
```

### Method 3: Python SDK

```plain text
from omnara import OmnaraClient
import uuid

client = OmnaraClient(api_key="your-api-key")
instance_id = str(uuid.uuid4())

# Log progress and check for user feedback
response = client.send_message(
    agent_type="claude-code",
    content="Analyzing codebase structure",
    agent_instance_id=instance_id,
    requires_user_input=False
)

# Ask for user input when needed
answer = client.send_message(
    content="Should I refactor this legacy module?",
    agent_instance_id=instance_id,
    requires_user_input=True
)
```

### Method 4: REST API

```plain text
curl -X POST https://api.omnara.ai/api/v1/messages/agent \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"content": "Starting deployment process", "agent_type": "claude-code", "requires_user_input": false}'
```

## 🤝 Contributing

We love contributions! Check out our Contributing Guide to get started.

### Development Commands

```plain text
make lint       # Run code quality checks
make format     # Auto-format code
make test       # Run test suite
make dev-serve  # Start development servers
```

## 📊 Pricing

## 🆘 Support

- 📖 Documentation
- 💬 GitHub Discussions
- 🐛 Report Issues
- 📧 Email Support
## 📜 License

Omnara is open source software licensed under the Apache 2.0 License.

Built with ❤️ by the Omnara team

Website • Twitter • LinkedIn


