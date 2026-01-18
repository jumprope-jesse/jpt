---
type: link
source: notion
url: https://github.com/simstudioai/sim
notion_type: Software Repo
tags: ['Running']
created: 2025-12-12T04:15:00.000Z
---

# GitHub - simstudioai/sim: Open-source platform to build and deploy AI agent workflows.

## Overview (from Notion)
- Open-source platform like Sim allows for quick AI agent workflow creation, which can streamline tasks at home or work.
- The ability to visually design workflows might appeal to your creative side, making complex processes more intuitive.
- Integrating vector databases can enhance how you manage family or business data, answering questions based on specific content effortlessly.
- Using tools like Copilot can help you innovate faster, generating ideas and fixing issues in real-time, freeing up more time for family.
- Consider the sustainability aspect of using efficient tech solutions at home, aligning with modern environmental values.
- With the flexibility of self-hosting, you can maintain control over your data while experimenting with cutting-edge technologies.
- As a father, leveraging these technologies can create a more organized home environment, benefiting your family's daily routine.
- Alternate view: while the platform promotes efficiency, there's a learning curve that may take time away from family engagements initially.

## AI Summary (from Notion)
An open-source platform for building and deploying AI agent workflows, allowing users to design workflows visually, integrate vector databases, and utilize Copilot for enhanced functionality. It supports both cloud-hosted and self-hosted setups, requires Docker, and includes detailed instructions for installation and configuration. The tech stack features Next.js, PostgreSQL, and various modern tools for UI and state management. Contributions are welcomed, and the project is licensed under the Apache License 2.0.

## Content (from Notion)

Build and deploy AI agent workflows in minutes.

### Build Workflows with Ease

Design agent workflows visually on a canvas—connect agents, tools, and blocks, then run them instantly.

### Supercharge with Copilot

Leverage Copilot to generate nodes, fix errors, and iterate on flows directly from natural language.

### Integrate Vector Databases

Upload documents to a vector store and let agents answer questions grounded in your specific content.

## Quickstart

### Cloud-hosted: sim.ai

### Self-hosted: NPM Package

```plain text
npx simstudio
```

→ http://localhost:3000

### Note

Docker must be installed and running on your machine.

### Options

### Self-hosted: Docker Compose

```plain text
# Clone the repository
git clone https://github.com/simstudioai/sim.git

# Navigate to the project directory
cd sim

# Start Sim
docker compose -f docker-compose.prod.yml up -d
```

Access the application at http://localhost:3000/

### Using Local Models with Ollama

Run Sim with local AI models using Ollama - no external APIs required:

```plain text
# Start with GPU support (automatically downloads gemma3:4b model)
docker compose -f docker-compose.ollama.yml --profile setup up -d

# For CPU-only systems:
docker compose -f docker-compose.ollama.yml --profile cpu --profile setup up -d
```

Wait for the model to download, then visit http://localhost:3000. Add more models with:

```plain text
docker compose -f docker-compose.ollama.yml exec ollama ollama pull llama3.1:8b
```

### Using an External Ollama Instance

If you already have Ollama running on your host machine (outside Docker), you need to configure the OLLAMA_URL to use host.docker.internal instead of localhost:

```plain text
# Docker Desktop (macOS/Windows)
OLLAMA_URL=http://host.docker.internal:11434 docker compose -f docker-compose.prod.yml up -d

# Linux (add extra_hosts or use host IP)
docker compose -f docker-compose.prod.yml up -d  # Then set OLLAMA_URL to your host's IP
```

Why? When running inside Docker, localhost refers to the container itself, not your host machine. host.docker.internal is a special DNS name that resolves to the host.

For Linux users, you can either:

- Use your host machine's actual IP address (e.g., http://192.168.1.100:11434)
- Add extra_hosts: ["host.docker.internal:host-gateway"] to the simstudio service in your compose file
### Using vLLM

Sim also supports vLLM for self-hosted models with OpenAI-compatible API:

```plain text
# Set these environment variables
VLLM_BASE_URL=http://your-vllm-server:8000
VLLM_API_KEY=your_optional_api_key  # Only if your vLLM instance requires auth
```

When running with Docker, use host.docker.internal if vLLM is on your host machine (same as Ollama above).

### Self-hosted: Dev Containers

1. Open VS Code with the Remote - Containers extension
1. Open the project and click "Reopen in Container" when prompted
1. Run bun run dev:full in the terminal or use the sim-start alias 
### Self-hosted: Manual Setup

Requirements:

- Bun runtime
- PostgreSQL 12+ with pgvector extension (required for AI embeddings)
Note: Sim uses vector embeddings for AI features like knowledge bases and semantic search, which requires the pgvector PostgreSQL extension.

1. Clone and install dependencies:
```plain text
git clone https://github.com/simstudioai/sim.git
cd sim
bun install
```

1. Set up PostgreSQL with pgvector:
You need PostgreSQL with the vector extension for embedding support. Choose one option:

Option A: Using Docker (Recommended)

```plain text
# Start PostgreSQL with pgvector extension
docker run --name simstudio-db \
  -e POSTGRES_PASSWORD=your_password \
  -e POSTGRES_DB=simstudio \
  -p 5432:5432 -d \
  pgvector/pgvector:pg17
```

Option B: Manual Installation

- Install PostgreSQL 12+ and the pgvector extension
- See pgvector installation guide
1. Set up environment:
```plain text
cd apps/sim
cp .env.example .env  # Configure with required variables (DATABASE_URL, BETTER_AUTH_SECRET, BETTER_AUTH_URL)
```

Update your .env file with the database URL:

```plain text
DATABASE_URL="postgresql://postgres:your_password@localhost:5432/simstudio"
```

1. Set up the database:
First, configure the database package environment:

```plain text
cd packages/db
cp .env.example .env
```

Update your packages/db/.env file with the database URL:

```plain text
DATABASE_URL="postgresql://postgres:your_password@localhost:5432/simstudio"
```

Then run the migrations:

```plain text
bunx drizzle-kit migrate --config=./drizzle.config.ts
```

1. Start the development servers:
Recommended approach - run both servers together (from project root):

```plain text
bun run dev:full
```

This starts both the main Next.js application and the realtime socket server required for full functionality.

Alternative - run servers separately:

Next.js app (from project root):

```plain text
bun run dev
```

Realtime socket server (from apps/sim directory in a separate terminal):

```plain text
cd apps/sim
bun run dev:sockets
```

## Copilot API Keys

Copilot is a Sim-managed service. To use Copilot on a self-hosted instance:

- Go to https://sim.ai → Settings → Copilot and generate a Copilot API key
- Set COPILOT_API_KEY environment variable in your self-hosted apps/sim/.env file to that value
## Environment Variables

Key environment variables for self-hosted deployments (see apps/sim/.env.example for full list):

## Troubleshooting

### Ollama models not showing in dropdown (Docker)

If you're running Ollama on your host machine and Sim in Docker, change OLLAMA_URL from localhost to host.docker.internal:

```plain text
OLLAMA_URL=http://host.docker.internal:11434 docker compose -f docker-compose.prod.yml up -d
```

See Using an External Ollama Instance for details.

### Database connection issues

Ensure PostgreSQL has the pgvector extension installed. When using Docker, wait for the database to be healthy before running migrations.

### Port conflicts

If ports 3000, 3002, or 5432 are in use, configure alternatives:

```plain text
# Custom ports
NEXT_PUBLIC_APP_URL=http://localhost:3100 POSTGRES_PORT=5433 docker compose up -d
```

## Tech Stack

- Framework: Next.js (App Router)
- Runtime: Bun
- Database: PostgreSQL with Drizzle ORM
- Authentication: Better Auth
- UI: Shadcn, Tailwind CSS
- State Management: Zustand
- Flow Editor: ReactFlow
- Docs: Fumadocs
- Monorepo: Turborepo
- Realtime: Socket.io
- Background Jobs: Trigger.dev
- Remote Code Execution: E2B
## Contributing

We welcome contributions! Please see our Contributing Guide for details.

## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

Made with ❤️ by the Sim Team


