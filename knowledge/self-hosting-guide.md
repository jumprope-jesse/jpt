# Self-Hosting Guide

*Source: [2026 is the year of self-hosting](https://fulghum.io/self-hosting) by Fulghum - Added: 2026-01-18*

## Why 2026 is Different

Three things converged to make self-hosting accessible to non-sysadmins:

1. **Affordable mini PCs** - Beelink Mini N150 (~$200) + 8TB NVMe SSD runs 13 services on 4GB RAM, minimal CPU
2. **Tailscale** - Secure networking without complex VPN setup
3. **CLI agents (Claude Code)** - The real unlock. Instead of stitching together blog posts from 2021, just describe what you want

**Key insight:** CLI agents make self-hosting dramatically easier and actually fun. First time it's recommendable to software-literate people who never wanted to become sysadmins.

## The Basic Flow

1. Install Linux on mini PC
2. Install Tailscale for secure remote access
3. Install Claude Code directly on the Linux box
4. Ask Claude Code to set things up:
   - Set up Docker
   - Create Docker Compose files
   - Install services
   - Put services behind Caddy (reverse proxy)
   - Persist data properly
   - Keep Docker images updated
   - Set up security packages
   - Configure restart on boot

No copy-pasting YAML from the internet. No deep Googling. Just ask.

## Recommended Services

### Core Services

| Service | Purpose | Notes |
|---------|---------|-------|
| **Vaultwarden** | Password management | Bitwarden-compatible, works with native apps/extensions, can be iOS default password manager |
| **Immich** | Google Photos replacement | Face recognition (local ML), timeline/map view, auto mobile uploads. "Not a compromise - better." See detailed setup notes below. |
| **Plex** | Media server | Stream your media anywhere |
| **ReadDeck** | Read-it-later (Pocket replacement) | Clean UI, remembers reading position, mobile shortcuts to save articles |

### Utilities

| Tool | Purpose |
|------|---------|
| **Lazydocker** | Terminal UI for Docker - see containers, logs, stats, restart/shell into anything |
| **Glances** | Full system view - CPU, memory, disk, network, all containers |
| **Uptime Kuma** | Monitoring with email alerts when services go down/up |
| **Caddy** | Reverse proxy with automatic HTTPS |
| **ntfy** | Push notifications via PUT/POST - self-hostable, open source |

## Hardware Specs (Reference)

- **Device**: Beelink Mini N150 (~$200)
- **Storage**: 8TB NVMe SSD (few hundred USD)
- **Usage**: 13 containers, 6% CPU, 32% memory (~4GB)
- **Characteristics**: Small, quiet, low power consumption

## Who This Is For

- Comfortable in a terminal
- Already paying for SaaS tools
- Like understanding how things work
- Don't want to become infra experts

## The Feeling

> "The feeling of ownership is powerful... I am spending time using software, learning, and having fun - instead of maintaining it and stressing out about it."

When something breaks: SSH in, ask the agent what's wrong, fix it.
When adding something new: describe it in plain English.

---

## Immich Setup Notes

*Source: [Self-hosting my photos with Immich](https://michael.stapelberg.ch/posts/2025-11-29-self-hosting-photos-with-immich/) by Michael Stapelberg - Added: 2026-01-18*

### Hardware Requirements
- Example: Ryzen 7 Mini PC (ASRock DeskMini X600), <10W idle, 64GB RAM, 1TB disk
- For initial import, allocate more CPU/RAM temporarily; 4 cores + 4GB sufficient for normal use
- Can run in a Proxmox VM

### NixOS Installation
```nix
services.immich = {
  enable = true;
};
```
- Default location: `/var/lib/immich`
- NixOS enables firewall by default; use Tailscale for access instead of opening ports

### Tailscale Integration
```bash
# Forward traffic to Immich via Tailscale
tailscale serve --bg http://localhost:2283
```
With MagicDNS + TLS cert provisioning: access via `https://photos.example.ts.net`

### Initial Photo Import

**Don't use `immich-cli`** for Google Takeout imports - it times out during background job processing and doesn't handle metadata JSON files.

**Use `immich-go` instead:**
```bash
immich-go \
  upload \
  from-google-photos \
  --server=https://photos.example.ts.net \
  --api-key=secret \
  ~/Downloads/takeout-*.zip
```
- Pauses background tasks during upload, restarts after
- Properly handles Google Takeout metadata JSON files

### iPhone App Setup
1. Install Immich app
2. Login via Tailscale URL
3. Enable automatic backup (top right icon)
4. **Disable notifications**: Settings → Apps → Immich → Notifications (not needed for background upload)
5. Live Photos go to "Live Photos" album; "Recent" covers other files

### Backup Strategy
Backup entire `/var/lib/immich`:
- `backups/` - SQL dumps
- `upload/`, `library/`, `profile/` - user data

Set up systemd timer with rsync to PC enrolled in 3-2-1 backup scheme.

### Limitations
- No built-in photo editing (rotate/crop) - use GIMP
- For sharing, may still need Google Photos depending on recipients

### Immich vs Ente
- Ente: larger scope, end-to-end encryption focus
- Immich: simpler, relies on existing encryption (Tailscale transit, LUKS disk)

---

## ntfy Push Notifications

*Source: [ntfy.sh](https://ntfy.sh/) - Added: 2026-01-18*

### What It Does
Send push notifications to phone/desktop via simple HTTP PUT/POST. Topics are created on-the-fly - no sign-up required (topic name acts as password if using public server).

### Basic Usage
```bash
# Send a notification
curl -d "Backup completed successfully" ntfy.sh/my-secret-topic

# With priority and tags
curl -H "Priority: high" -H "Tags: warning" -d "Disk 90% full" ntfy.sh/my-topic
```

### Key Features
- **Priorities**: Maps to different sounds/vibration patterns
- **Action buttons**: React to notifications directly
- **Attachments**: Send images, videos, files (e.g., surveillance camera pics)
- **Web app**: Subscribe to topics for desktop notifications
- **Tags/emojis**: Classify and personalize notifications

### Use Cases
- Cronjob completion alerts
- CI/CD pipeline notifications (GitHub Actions)
- Home automation alerts (security sensors, motion detection)
- Server monitoring (unauthorized logins, downloads complete)
- New episode notifications from media tools

### Self-Hosting
- Open source (Apache 2.0 / GPLv2)
- Self-hostable server component
- Apps available for iOS/Android/Desktop
- [GitHub](https://github.com/binwiederhier/ntfy) | [Discord/Matrix community]

### Integration
Simple HTTP API means it integrates with basically anything - scripts, automation tools, monitoring systems. Perfect complement to Uptime Kuma for custom application notifications.

---

## Onyx - Self-Hosted AI Platform

*Source: [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) - Added: 2026-01-18*

### What It Does
Self-hostable Chat UI that works with any LLM. Runs in completely airgapped environments.

### Key Features
- **Custom Agents**: Build AI agents with unique instructions, knowledge, and actions
- **Web Search**: Google PSE, Exa, Serper integration + built-in scraper/Firecrawl
- **RAG**: Hybrid search + knowledge graph for uploaded files and ingested documents
- **40+ Connectors**: Pull knowledge from external applications
- **Deep Research**: Agentic multi-step search for in-depth answers
- **MCP Support**: Give agents ability to interact with external systems
- **Code Interpreter**: Execute code, analyze data, render graphs
- **Image Generation**: Generate images from prompts

### LLM Compatibility
Works with all LLMs:
- Cloud: OpenAI, Anthropic, Gemini, etc.
- Self-hosted: Ollama, vLLM, etc.

### Deployment
```bash
# One-command install (Docker)
curl -fsSL https://raw.githubusercontent.com/onyx-dot-app/onyx/main/deployment/docker_compose/install.sh > install.sh && chmod +x install.sh && ./install.sh
```

Options: Docker (most users), Kubernetes (large teams), Terraform, cloud-specific guides (AWS EKS, Azure VMs)

### Enterprise Features
- Enterprise Search: Scales to tens of millions of documents
- Security: SSO (OIDC/SAML/OAuth2), RBAC, credential encryption
- User Management: Basic, curator, and admin roles
- Document Permissioning: Mirrors user access from external apps

### Licensing
- **Community Edition (CE)**: MIT license, free
- **Enterprise Edition (EE)**: Additional features for larger organizations

### Use Cases
- Team knowledge base with AI chat interface
- Internal search across company documents
- AI agents with access to private data sources
- Airgapped/secure environment AI deployment

---

## Ory Kratos - Self-Hosted Authentication

*Source: [ory/kratos](https://github.com/ory/kratos) - Added: 2026-01-18*

### What It Does
Headless, cloud-native authentication and identity management written in Go. Self-hosted alternative to Auth0, Okta, Firebase Auth.

### Key Features
- **Passkeys**: Modern passwordless authentication
- **Social Sign In**: OAuth2/OIDC providers (Google, GitHub, etc.)
- **Magic Links**: Email-based passwordless login
- **MFA**: TOTP, SMS, WebAuthn support
- **SAML**: Enterprise SSO integration
- **API-first**: Headless design - bring your own UI

### Why Self-Host Authentication?
- Full control over user data and privacy
- No vendor lock-in
- No per-user pricing that scales poorly
- Data stays in your infrastructure
- Aligns with self-hosting philosophy for other services

### Considerations
- More setup complexity vs managed services (Auth0/Okta)
- Requires maintaining security updates
- Need to handle scaling yourself (though it claims "billion+ users" scale)
- Good DX but still more work than dropping in a SaaS SDK

### Use Cases
- Self-hosted apps needing user authentication
- Privacy-focused projects
- Projects where data sovereignty matters
- Cost-sensitive scaling (avoid per-MAU pricing)

---

## Syllabi - AI Chatbot Platform with RAG

*Source: [syllabi-ai.com](https://www.syllabi-ai.com/) - Added: 2026-01-18*

### What It Does
Open-source AI chatbot platform for rich, interactive conversations that integrate documents, diagrams, code, and multimedia. Designed for transparency, privacy, and full control over AI infrastructure.

### Key Features
- **Rich conversations**: Goes beyond simple Q&A - documents, diagrams, code, multimedia in one place
- **RAG support**: Use documents as knowledge sources
- **Full customization**: Tailor chatbot to match brand and business needs
- **Tool integrations**: Connect to existing apps as knowledge sources, deployment channels, or workflow automation
- **Privacy-focused**: Built for teams who value transparency and control

### Use Cases
- Team knowledge base chatbot
- Customer-facing branded chatbots
- Internal documentation assistant
- Workflow automation with AI
- Educational tools for teaching AI/programming concepts

### Deployment
Self-hostable - allows full control over AI infrastructure without relying on third-party services.

### Considerations
- Developer-friendly focus means setup may require technical skills
- Good for teams wanting to avoid vendor lock-in on AI chat solutions
- Integrations work bidirectionally (knowledge sources AND action triggers)
