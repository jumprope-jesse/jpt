---
type: link
source: notion
url: https://github.com/IBM/mcp-context-forge
notion_type: Software Repo
tags: ['Running']
created: 2025-08-25T07:05:00.000Z
---

# GitHub - IBM/mcp-context-forge: A Model Context Protocol (MCP) Gateway & Registry. Serves as a central management point for tools, resources, and prompts that can be accessed by MCP-compatible LLM applications. Converts REST API endpoints to MCP, composes virtual MCP servers with added security and observability, and converts between protocols (stdio, SSE, Streamable HTTP).

## Overview (from Notion)
- The MCP Gateway simplifies integrating diverse AI tools, making it easier to manage and innovate within your tech ventures.
- Leveraging this technology can enhance your software products, potentially leading to improved user experiences and efficiencies.
- The ability to connect multiple protocols (like REST and MCP) means you can streamline operations, which is crucial for a busy entrepreneur and father.
- The focus on observability and security aligns with current industry needs, ensuring your projects are reliable and trustworthy.
- Consider how this gateway can be a part of your home automation or smart home projects, merging your personal interests with professional skills.
- The open-source nature allows you to customize and adapt it to your specific needs, fostering a hands-on approach that can be a great example for your kids.
- As a company founder, utilizing cutting-edge technology like this can position you ahead of competitors in the rapidly evolving AI landscape.
- Alternate views may include skepticism about relying too heavily on new technologies or concerns about the learning curve for implementing such a system in your projects.

## AI Summary (from Notion)
The ContextForge MCP Gateway is a comprehensive gateway and registry for Model Context Protocol (MCP) and REST APIs, enabling unified access for AI clients. It supports features like federation, virtualization of legacy APIs, and multiple transport protocols, while offering an admin UI for management. The project is in early beta, not production-ready, and requires careful security review before deployment. Quick start guides for installation via PyPI and containers are provided, along with extensive configuration options and API documentation for tool and resource management.

## Content (from Notion)

# MCP Gateway

> 

ContextForge MCP Gateway is a feature-rich gateway, proxy and MCP Registry that federates MCP and REST services - unifying discovery, auth, rate-limiting, observability, virtual servers, multi-transport protocols, and an optional Admin UI into one clean endpoint for your AI clients. It runs as a fully compliant MCP server, deployable via PyPI or Docker, and scales to multi-cluster environments on Kubernetes with Redis-backed federation and caching.

##   

## Table of Contents

## Table of Contents

- 
- 
-  
-  
-  
-  
-  
-  
-  
-  
- 
- 
-  
- 
- 
- 
- 
- 
-  
- 
- 
- 
- 
- 
## 🚀 Overview & Goals

ContextForge MCP Gateway is a gateway, registry, and proxy that sits in front of any Model Context Protocol (MCP) server or REST API-exposing a unified endpoint for all your AI clients.

⚠️ Caution: The current release (0.4.0) is considered alpha / early beta. It is not production-ready and should only be used for local development, testing, or experimentation. Features, APIs, and behaviors are subject to change without notice. Do not deploy in production environments without thorough security review, validation and additional security mechanisms. Many of the features required for secure, large-scale, or multi-tenant production deployments are still on the project roadmap - which is itself evolving.

It currently supports:

- Federation across multiple MCP and REST services
- Virtualization of legacy APIs as MCP-compliant tools and servers
- Transport over HTTP, JSON-RPC, WebSocket, SSE, stdio and streamable-HTTP
- An Admin UI for real-time management and configuration
- Built-in auth, observability, retries, and rate-limiting
- Scalable deployments via Docker or PyPI, Redis-backed caching, and multi-cluster federation
For a list of upcoming features, check out the ContextForge MCP Gateway Roadmap

⚠️ Important: MCP Gateway is not a standalone product - it is an open source component with NO OFFICIAL SUPPORT from IBM or its affiliates that can be integrated into your own solution architecture. If you choose to use it, you are responsible for evaluating its fit, securing the deployment, and managing its lifecycle. See SECURITY.md for more details.

## Quick Start - PyPI

MCP Gateway is published on PyPI as mcp-contextforge-gateway.

### 1 - Install & run (copy-paste friendly)

```plain text
# 1️⃣  Isolated env + install from pypi
mkdir mcpgateway && cd mcpgateway
python3 -m venv .venv && source .venv/bin/activate
pip install --upgrade pip
pip install mcp-contextforge-gateway

# 2️⃣  Launch on all interfaces with custom creds & secret key
# Enable the Admin API endpoints (true/false) - disabled by default
export MCPGATEWAY_UI_ENABLED=true
export MCPGATEWAY_ADMIN_API_ENABLED=true

BASIC_AUTH_PASSWORD=pass JWT_SECRET_KEY=my-test-key \
  mcpgateway --host 0.0.0.0 --port 4444 &   # admin/pass

# 3️⃣  Generate a bearer token & smoke-test the API
export MCPGATEWAY_BEARER_TOKEN=$(python3 -m mcpgateway.utils.create_jwt_token \
    --username admin --exp 10080 --secret my-test-key)

curl -s -H "Authorization: Bearer $MCPGATEWAY_BEARER_TOKEN" \
     http://127.0.0.1:4444/version | jq
```

## Quick Start - Containers

Use the official OCI image from GHCR with Docker or Podman.

### 🐳 Docker

### 1 - Minimum viable run

```plain text
docker run -d --name mcpgateway \
  -p 4444:4444 \
  -e MCPGATEWAY_UI_ENABLED=true \
  -e MCPGATEWAY_ADMIN_API_ENABLED=true \
  -e HOST=0.0.0.0 \
  -e JWT_SECRET_KEY=my-test-key \
  -e BASIC_AUTH_USER=admin \
  -e BASIC_AUTH_PASSWORD=changeme \
  -e AUTH_REQUIRED=true \
  -e DATABASE_URL=sqlite:///./mcp.db \
  ghcr.io/ibm/mcp-context-forge:0.4.0

# Tail logs (Ctrl+C to quit)
docker logs -f mcpgateway

# Generating an API key
docker run --rm -it ghcr.io/ibm/mcp-context-forge:0.4.0 \
  python3 -m mcpgateway.utils.create_jwt_token --username admin --exp 0 --secret my-test-key
```

Browse to http://localhost:4444/admin (user admin / pass changeme).

### 2 - Persist the SQLite database

```plain text
mkdir -p $(pwd)/data

touch $(pwd)/data/mcp.db

sudo chown -R :docker $(pwd)/data

chmod 777 $(pwd)/data

docker run -d --name mcpgateway \
  --restart unless-stopped \
  -p 4444:4444 \
  -v $(pwd)/data:/data \
  -e MCPGATEWAY_UI_ENABLED=true \
  -e MCPGATEWAY_ADMIN_API_ENABLED=true \
  -e DATABASE_URL=sqlite:////data/mcp.db \
  -e HOST=0.0.0.0 \
  -e JWT_SECRET_KEY=my-test-key \
  -e BASIC_AUTH_USER=admin \
  -e BASIC_AUTH_PASSWORD=changeme \
  ghcr.io/ibm/mcp-context-forge:0.4.0
```

SQLite now lives on the host at ./data/mcp.db.

### 3 - Local tool discovery (host network)

```plain text
mkdir -p $(pwd)/data

touch $(pwd)/data/mcp.db

sudo chown -R :docker $(pwd)/data

chmod 777 $(pwd)/data

docker run -d --name mcpgateway \
  --network=host \
  -e MCPGATEWAY_UI_ENABLED=true \
  -e MCPGATEWAY_ADMIN_API_ENABLED=true \
  -e HOST=0.0.0.0 \
  -e PORT=4444 \
  -e DATABASE_URL=sqlite:////data/mcp.db \
  -v $(pwd)/data:/data \
  ghcr.io/ibm/mcp-context-forge:0.4.0
```

Using --network=host allows Docker to access the local network, allowing you to add MCP servers running on your host. See Docker Host network driver documentation for more details.

### 🦭 Podman (rootless-friendly)

### 1 - Basic run

```plain text
podman run -d --name mcpgateway \
  -p 4444:4444 \
  -e HOST=0.0.0.0 \
  -e DATABASE_URL=sqlite:///./mcp.db \
  ghcr.io/ibm/mcp-context-forge:0.4.0
```

### 2 - Persist SQLite

```plain text
mkdir -p $(pwd)/data

touch $(pwd)/data/mcp.db

sudo chown -R :docker $(pwd)/data

chmod 777 $(pwd)/data

podman run -d --name mcpgateway \
  --restart=on-failure \
  -p 4444:4444 \
  -v $(pwd)/data:/data \
  -e DATABASE_URL=sqlite:////data/mcp.db \
  ghcr.io/ibm/mcp-context-forge:0.4.0
```

### 3 - Host networking (rootless)

```plain text
mkdir -p $(pwd)/data

touch $(pwd)/data/mcp.db

sudo chown -R :docker $(pwd)/data

chmod 777 $(pwd)/data

podman run -d --name mcpgateway \
  --network=host \
  -v $(pwd)/data:/data \
  -e DATABASE_URL=sqlite:////data/mcp.db \
  ghcr.io/ibm/mcp-context-forge:0.4.0
```

## Testing mcpgateway.wrapper by hand:

Because the wrapper speaks JSON-RPC over stdin/stdout, you can interact with it using nothing more than a terminal or pipes.

```plain text
# Start the MCP Gateway Wrapper
export MCP_AUTH_TOKEN=${MCPGATEWAY_BEARER_TOKEN}
export MCP_SERVER_CATALOG_URLS=http://localhost:4444/servers/YOUR_SERVER_UUID
python3 -m mcpgateway.wrapper
```

### 🧩 Running from an MCP Client (mcpgateway.wrapper)

The mcpgateway.wrapper exposes everything your Gateway knows about over stdio, so any MCP client that can't (or shouldn't) open an authenticated SSE stream still gets full tool-calling power.

> 

### 🚀 Using with Claude Desktop (or any GUI MCP client)

1. Edit Config → File ▸ Settings ▸ Developer ▸ Edit Config
1. Paste one of the JSON blocks above (Docker / pipx / uvx).
1. Restart the app so the new stdio server is spawned.
1. Open logs in the same menu to verify mcpgateway-wrapper started and listed your tools.
Need help? See:

- MCP Debugging Guide - https://modelcontextprotocol.io/docs/tools/debugging
## 🚀 Quick Start: VS Code Dev Container

Spin up a fully-loaded dev environment (Python 3.11, Docker/Podman CLI, all project dependencies) in just two clicks.

## Quick Start (manual install)

### Prerequisites

- Python ≥ 3.10
- GNU Make (optional, but all common workflows are available as Make targets)
- Optional: Docker / Podman for containerized runs
### One-liner (dev)

```plain text
make venv install serve
```

What it does:

1. Creates / activates a .venv in your home folder ~/.venv/mcpgateway
1. Installs the gateway and necessary dependencies
1. Launches Gunicorn (Uvicorn workers) on http://localhost:4444
For development, you can use:

```plain text
make install-dev # Install development dependencies, ex: linters and test harness
make lint          # optional: run style checks (ruff, mypy, etc.)
```

### Containerized (self-signed TLS)

## Container Runtime Support

This project supports both Docker and Podman. The Makefile automatically detects which runtime is available and handles image naming differences.

### Auto-detection

```plain text
make container-build  # Uses podman if available, otherwise docker

> You can use docker or podman, ex:

```bash
make podman            # build production image
make podman-run-ssl    # run at https://localhost:4444
# or listen on port 4444 on your host directly, adds --network=host to podman
make podman-run-ssl-host
```

### Smoke-test the API

```plain text
curl -k -sX GET \
     -H "Authorization: Bearer $MCPGATEWAY_BEARER_TOKEN" \
     https://localhost:4444/tools | jq
```

You should receive [] until you register a tool.

## Installation

### Via Make

```plain text
make venv install          # create .venv + install deps
make serve                 # gunicorn on :4444
```

### UV (alternative)

```plain text
uv venv && source .venv/bin/activate
uv pip install -e '.[dev]' # IMPORTANT: in zsh, quote to disable glob expansion!
```

### pip (alternative)

```plain text
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
```

### Optional (PostgreSQL adapter)

You can configure the gateway with SQLite, PostgreSQL (or any other compatible database) in .env.

When using PostgreSQL, you need to install psycopg2 driver.

```plain text
uv pip install psycopg2-binary   # dev convenience
# or
uv pip install psycopg2          # production build
```

### Quick Postgres container

```plain text
docker run --name mcp-postgres \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -e POSTGRES_DB=mcp \
  -p 5432:5432 -d postgres
```

A make compose-up target is provided along with a docker-compose.yml file to make this process simpler.

## Configuration (.env or env vars)

> 

You can get started by copying the provided .env.example to .env and making the necessary edits to fit your environment.

## Running

### Makefile

```plain text
 make serve               # Run production Gunicorn server on
 make serve-ssl           # Run Gunicorn behind HTTPS on :4444 (uses ./certs)
```

### Script helper

To run the development (uvicorn) server:

```plain text
make dev
# or
./run.sh --reload --log debug --workers 2
```

> 

Key flags:

### Manual (Uvicorn)

```plain text
uvicorn mcpgateway.main:app --host 0.0.0.0 --port 4444 --workers 4
```

## Authentication examples

```plain text
# Generate a JWT token using JWT_SECRET_KEY and export it as MCPGATEWAY_BEARER_TOKEN
# Note that the module needs to be installed. If running locally use:
export MCPGATEWAY_BEARER_TOKEN=$(JWT_SECRET_KEY=my-test-key python3 -m mcpgateway.utils.create_jwt_token)

# Use the JWT token in an API call
curl -H "Authorization: Bearer $MCPGATEWAY_BEARER_TOKEN" http://localhost:4444/tools
```

## ☁️ AWS / Azure / OpenShift

Deployment details can be found in the GitHub Pages.

## ☁️ IBM Cloud Code Engine Deployment

This project supports deployment to IBM Cloud Code Engine using the ibmcloud CLI and the IBM Container Registry.

## API Endpoints

You can test the API endpoints through curl, or Swagger UI, and check detailed documentation on ReDoc:

- Swagger UI → http://localhost:4444/docs
- ReDoc → http://localhost:4444/redoc
Generate an API Bearer token, and test the various API endpoints.

## Testing

```plain text
make test            # Run unit tests
make lint            # Run lint tools
```

## Doctest Coverage

MCP Context Forge implements comprehensive doctest coverage to ensure all code examples in documentation are tested and verified:

```plain text
make doctest         # Run all doctests
make doctest-verbose # Run with detailed output
make doctest-coverage # Generate coverage report
make doctest-check   # Check coverage percentage
```

Coverage Status:

- ✅ Transport Modules: 100% (base, stdio, SSE, WebSocket, streamable HTTP)
- ✅ Utility Functions: 100% (slug generation, JWT tokens, validation)
- ✅ Configuration: 100% (settings, environment variables)
- 🔄 Service Classes: ~60% (in progress)
- 🔄 Complex Classes: ~40% (in progress)
Benefits:

- All documented examples are automatically tested
- Documentation stays accurate and up-to-date
- Developers can run examples directly from docstrings
- Regression prevention through automated verification
For detailed information, see the Doctest Coverage Guide.

## Project Structure

## API Documentation

- Swagger UI → http://localhost:4444/docs
- ReDoc → http://localhost:4444/redoc
- Admin Panel → http://localhost:4444/admin
## Makefile targets

This project offer the following Makefile targets. Type make in the project root to show all targets.

## 🔍 Troubleshooting

## Contributing

1. Fork the repo, create a feature branch.
1. Run make lint and fix any issues.
1. Keep make test green and 100% coverage.
1. Open a PR - describe your changes clearly.
## See CONTRIBUTING.md for more details.

## Changelog

A complete changelog can be found here: CHANGELOG.md

## License

Licensed under the Apache License 2.0 - see LICENSE

## Core Authors and Maintainers

- Mihai Criveti - Distinguished Engineer, Agentic AI
Special thanks to our contributors for helping us improve ContextForge MCP Gateway:

## Star History and Project Activity


