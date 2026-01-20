# Pingoo - Self-Hosted Load Balancer/Reverse Proxy

Source: https://github.com/pingooio/pingoo
Documentation: https://pingoo.io
License: MIT (fully open source, no enterprise edition)
Status: Beta (as of Oct 2025)

## What It Is

Modern, Rust-based load balancer / API gateway / reverse proxy designed to replace third-party cloud services while keeping traffic on your own servers.

## Key Features

- **Service Discovery** - Docker, DNS integration
- **Web Application Firewall (WAF)** - Built-in
- **Bot Protection** - Built-in management
- **GeoIP** - Country and ASN detection
- **Post-Quantum TLS** - Future-proof encryption
- **TCP Proxying** - Low-level connection handling
- **Static Site Serving** - Simple hosting capability
- **Data Compliance** - Traffic never leaves your servers

## Why It Exists

Open source load balancers (nginx, HAProxy) have slow development and reserve important features for enterprise editions. Pingoo aims to provide managed-service-level features while self-hosted.

## Quickstart

```bash
# Serve static site from ./www folder
docker run --rm -ti --network host -v `pwd`/www:/var/www ghcr.io/pingooio/pingoo
# Listens on http://0.0.0.0:8080
```

## Use Cases

- Replace Cloudflare/AWS ALB while maintaining data sovereignty
- Self-hosted API gateway with built-in security features
- Privacy-focused infrastructure (no third-party traffic inspection)

## Considerations

- Beta status - evaluate stability for production use
- Rust-based - performance benefits but smaller ecosystem
- Self-hosted means you manage uptime/scaling
