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
| **Immich** | Google Photos replacement | Face recognition (local ML), timeline/map view, auto mobile uploads. "Not a compromise - better." |
| **Plex** | Media server | Stream your media anywhere |
| **ReadDeck** | Read-it-later (Pocket replacement) | Clean UI, remembers reading position, mobile shortcuts to save articles |

### Utilities

| Tool | Purpose |
|------|---------|
| **Lazydocker** | Terminal UI for Docker - see containers, logs, stats, restart/shell into anything |
| **Glances** | Full system view - CPU, memory, disk, network, all containers |
| **Uptime Kuma** | Monitoring with email alerts when services go down/up |
| **Caddy** | Reverse proxy with automatic HTTPS |

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
