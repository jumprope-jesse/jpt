---
type: link
source: notion
url: https://github.com/octelium/octelium
notion_type: Software Repo
tags: ['Running']
created: 2025-06-29T15:02:00.000Z
---

# GitHub - octelium/octelium: A next-gen FOSS self-hosted unified zero trust secure access platform that can operate as a remote access VPN, a ZTNA/BeyondCorp architecture, API/AI gateway, a PaaS, an infrastructure for MCP & A2A architectures or even as an ngrok-alternative and a homelab infrastructure.

## Overview (from Notion)
- Octelium could enhance your home office setup by providing secure remote access to your work resources, especially if you juggle multiple projects.
- It offers an alternative to traditional VPNs, emphasizing a zero trust architecture that might resonate with your focus on security and efficiency in tech.
- The self-hosted aspect aligns with a DIY ethos, allowing you to tailor solutions to fit your needs without vendor lock-in.
- With its scalability, you could deploy Octelium for personal projects or within your startup, enabling seamless access for remote teams or family members.
- The dynamic, context-aware access control could simplify managing permissions for various users in your household or work environment.
- Consider the implications of open-source software in fostering community and collaboration versus proprietary solutions, especially as you navigate entrepreneurship in a competitive landscape.
- Explore the balance between technology adoption and family life; how can a tool like Octelium streamline your digital life while ensuring your family's online safety?

## AI Summary (from Notion)
Octelium is a free and open-source platform for secure zero trust access, functioning as a remote access VPN, ZTNA architecture, API gateway, and PaaS. It allows for dynamic, context-aware access control, secret-less authentication, and is designed for self-hosting on Kubernetes. Key features include scalable architecture, continuous authentication, and the ability to manage containerized applications effortlessly. The project is currently in public beta and aims to provide a comprehensive solution for secure resource access without traditional VPN limitations.

## Content (from Notion)

# Octelium

## Table of Contents

- What is Octelium?
- Use Cases
- Main Features
- Try Octelium in a Codespace
- Install CLI Tools
- Install your First Cluster
- Useful Links
- License
- Support
- Frequently Asked Questions
- Legal
## What is Octelium?

Octelium is a free and open source, self-hosted, unified platform for zero trust resource access that is primarily meant to be a modern alternative to remote access VPNs and similar tools. It is built to be generic enough to not only operate as a zero-config remote access VPN (i.e. alternative to OpenVPN Access Server, Twingate, Tailscale, etc...), a ZTNA platform (i.e. alternative to Cloudflare Access, Teleport, Google BeyondCorp, etc...), a scalable infrastructure for secure tunnels (i.e. alternative to ngrok), but can also operate as an API gateway, an AI gateway, an infrastructure for MCP gateways and A2A architectures, a PaaS-like platform for secure as well as anonymous hosting and deployment for containerized applications, a Kubernetes gateway/ingress/load balancer and even as an infrastructure for your own homelab. Octelium provides a scalable zero trust architecture (ZTA) for identity-based, application-layer (L7) aware secret-less secure access, via both private client-based access over WireGuard/QUIC tunnels as well as public clientless access (i.e. BeyondCorp), for users, both humans and workloads, to any private/internal resource behind NAT in any environment as well as to publicly protected resources such as SaaS APIs and databases via context-aware access control on a per-request basis through policy-as-code.

## Use Cases

Octelium is designed to be generic enough (check out the main features below for more details) to be completely or partially used as a solution for various use cases depending on your needs/requirements, notably:

- Modern remote access VPN A modern zero trust L-7 aware alternative to commercial remote access/corporate VPNs to provide zero-config client-based over WireGuard/QUIC tunnels as well as client-less secret-less access via dynamic identity-based, L-7 aware, context-aware access control via policy-as-code (i.e. alternative to OpenVPN Access Server, Twingate, Tailscale, etc...).
- Unified ZTNA/BeyondCorp architecture A Zero Trust Network Access (ZTNA) platform/ BeyondCorp architecture (i.e. alternative to Cloudflare Access, Google BeyondCorp, Zscaler Private Access, Teleport, Fortinet, etc...).
- Self-hosted infrastructure for secure tunnels A self-hosted secure tunnels and reverse proxy programmable infrastructure (i.e. alternative to ngrok, Cloudflare Tunnel, etc...). You can see an example here.
- Self-hosted PaaS A scalable PaaS-like hosting/deployment platform to deploy, scale and provide both secure as well as anonymous public hosting for your containerized applications (i.e. similar to Vercel, Netlify, etc...). You can see examples for Next.js/Vite apps, remote VSCode, remote Ollama and Pi-hole.
- API gateway A self-hosted, scalable, secure API gateway that takes care of access, routing, deployment and scaling of containerized microservices, authentication, L-7 aware/context aware authorization and visibility (i.e. alternative to Kong Gateway, Apigee, etc...). You can see an example here.
- AI gateway A scalable AI gateway to any AI LLM providers with identity-based, context-aware access control, routing and visibility (see an example here).
- Unified Zero Trust Access to SaaS APIs Unified, secret-less that eliminates distributing and sharing the typically long-lived/over-privileged API keys and access tokens, access to all HTTP-based SaaS APIs for teams and workloads/applications where you can control access on a per-request basis via policy-as-code. Octelium also supports secret-less access to Kubernetes clusters, PostgreSQL/MySQL-based databases as well as to SSH servers (see the main features here for more information and links).
- MCP gateways and A2A-based architectures A secure infrastructure for Model Context Protocol (MCP) gateways and Agent2Agent Protocol (A2A)based architectures that provides identity management, authentication over standard OAuth2 client credentials and bearer authentication, secure remote access and deployment as well as identity-based, L7-aware access control via policy-as-code and visibility (see an example here).
- Kubernetes ingress alternative A much more advanced alternative to Kubernetes Ingress and load balancers where you can route to any remotely accessible internal resources from anywhere, not just Kubernetes services running on the same cluster, via much more than just path prefixes (e.g. identity, request headers, body content, context such as time of the day, etc...) via dynamic policy-as-code.
- Homelab A unified self-hosted Homelab infrastructure to connect and provide secure remote access to all your resources behind NAT from anywhere (e.g. all your devices including your laptop, IoT, cloud providers, Raspberry Pis, routers, etc...) as well as a secure deployment platform to deploy and privately as well as publicly host your websites, blogs, APIs or to remotely test heavy containers (e.g. LLM runtimes such as Ollama, databases such as ClickHouse and Elasticsearch, Pi-hole, etc...).
## Main Features

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
## Try Octelium in a Codespace

You can install and manage a demo Octelium Cluster inside a GitHub Codespace without having to install it on a real VM/machine/Kubernetes cluster and simply use it as a playground to get familiar of how the Cluster is managed. Visit the playground GitHub repository here and run it in a Codespace then follow the README instructions there to install the Cluster and start interacting with it.

## Install CLI Tools

You can see all available options here. You can quickly install the CLIs of the pre-built binaries as follows:

For Linux and MacOS

```plain text
curl -fsSL https://octelium.com/install.sh | sh
```

For Windows in Powershell

```plain text
iwr https://octelium.com/install.ps1 -useb | iex
```

## Install your First Cluster

Read this quick guide here to install a single-node Octelium Cluster on top of any cheap cloud VM/VPS instance (e.g. DigitalOcean Droplet, Hetzner server, AWS EC2, Vultr, etc...) or a local Linux machine/Linux VM inside a MacOS/Windows machine with at least 2GB of RAM and 20GB of disk storage running a recent Linux distribution (Ubuntu 24.04 LTS or later, Debian 12+, etc...), which is good enough for most development, personal or undemanding production use cases that do not require highly available multi-node Clusters. Once you SSH into your VPS/VM as root, you can install the Cluster as follows:

```plain text
curl -o install-demo-cluster.sh https://octelium.com/install-demo-cluster.sh
chmod +x install-demo-cluster.sh

# Replace <DOMAIN> with your actual domain
./install-demo-cluster.sh --domain <DOMAIN>
```

Once the Cluster is installed. You can start managing it as shown in the guide here.

## Useful Links

- What is Octelium?
- What is Zero Trust?
- How Octelium works
- First Steps Managing the Cluster
- Policies and Access Control
## License

Octelium is free and open source software:

- The Client-side components are licensed with the Apache 2.0 License. This includes: 
- The Cluster-side components (all the components in the /cluster directory) are licensed with the GNU Affero General Public (AGPLv3) License. Octelium Labs also provides a commercial license as an alternative for businesses that do not want to comply with the AGPLv3 license (read more here).
## Support

- Octelium Docs
- Discord Community
- Slack Community
- Contact via Email
- Reddit Community
## Frequently Asked Questions

-  
-  
-  
-  
-  
-  
-  
## Legal

Octelium and Octelium logo are trademarks of Octelium Labs, LLC.

WireGuard is a registered trademark of Jason A. Donenfeld.


