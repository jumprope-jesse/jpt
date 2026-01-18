# Localhost Tunneling Tools

Tools for exposing local web servers to the internet with public URLs.

## tunnl.gg

*Source: https://tunnl.gg/ - Added: 2026-01-18*

SSH-based localhost tunneling with no installation required.

### Key Features

- **No Installation** - Just SSH, nothing to download or install
- **Instant Public URLs** - Get a public URL for your local server immediately
- **v1.0 Released** - Production ready (as of late 2025)

### Use Cases

- Share local web projects with clients or collaborators
- Demo prototypes quickly without deployment
- Test webhooks and integrations that require public URLs
- Quick feedback loops during development

### How It Compares

| Feature | tunnl.gg | ngrok | Tailscale Funnel | Cloudflare Tunnel |
|---------|----------|-------|------------------|-------------------|
| Installation | None (SSH) | CLI required | CLI required | CLI required |
| Setup Complexity | Low | Low | Medium | Medium |
| Free Tier | Yes | Limited | Yes | Yes |
| Custom Domains | Unknown | Paid | Via Tailnet | Via Cloudflare |
| Auth Integration | Unknown | Yes | Yes (ACLs) | Yes (Access) |

### Security Considerations

- Exposing localhost means your dev environment is briefly accessible from the internet
- Consider what data/APIs are exposed on the tunneled port
- Use for dev/demo purposes, not production traffic
- Review security implications before sharing early-stage projects

### Notes

- Good for quick demos and client presentations
- Alternative to ngrok when you don't want to install anything
- SSH-based approach means it works anywhere SSH works
