# Tilt - Kubernetes Local Development Tool

*Source: [tilt.dev](https://tilt.dev/) - Added: 2026-01-18*

## What It Does

Tilt streamlines Kubernetes development workflows with smart rebuilds and live updates. It manages your entire local development environment - services, databases, infrastructure - and provides continuous feedback as you code.

## Key Features

### Smart Rebuilds & Live Updates
- **live_update**: Deploys code to running containers in seconds, not minutes
- Works for compiled languages and dependency changes
- Continuous feedback loop with logs, broken builds, and runtime errors

### Unified Dev Environment
- See all services/components in one dashboard
- Trigger custom workflows (database seeding, infrastructure setup)
- Automated rebuilds as you edit in your IDE

### Tiltfile Configuration
Define your entire environment in a `Tiltfile`:

```python
# Deploy: tell Tilt what YAML to deploy
k8s_yaml('app.yaml')

# Build: tell Tilt what images to build
docker_build('companyname/api', 'api')
docker_build('companyname/web', 'web')

# Watch: configure local access
k8s_resource('api', port_forwards="5734:5000", labels=["backend"])
```

### Developer Experience
- No need to be a Kubernetes expert
- Replaces tedious `kubectl` interrogation
- Handles repetitive workflow parts automatically
- Instant error notifications and peripheral vision

### Team Collaboration
- **Snapshots**: Share your dev environment state instantly
- **Common dev path**: Codified best practices for reproducibility
- **Easy onboarding**: New hires just run `tilt up`
- Analytics to understand usage and fix slowdowns proactively

## Use Cases

- Local Kubernetes development with fast iteration
- Multi-service application development
- Onboarding new team members quickly
- Sharing development environment state for debugging

## How It Fits with Other Tools

| Tool | Purpose | Relationship to Tilt |
|------|---------|---------------------|
| OrbStack/Docker | Container runtime | Tilt builds on top of these |
| Podman | Container runtime | Alternative container backend |
| kubectl | K8s CLI | Tilt abstracts away kubectl commands |
| Skaffold | K8s dev tool | Alternative to Tilt (Google's) |
| Telepresence | K8s dev tool | Alternative approach (proxying) |

## Installation

Open source and available at [tilt.dev](https://tilt.dev/):

```bash
# macOS
brew install tilt-dev/tap/tilt

# Linux
curl -fsSL https://raw.githubusercontent.com/tilt-dev/tilt/master/scripts/install.sh | bash
```

## Considerations

- Requires Kubernetes cluster (local like minikube, kind, or remote)
- Learning curve for Tiltfile configuration
- Best suited for teams already committed to Kubernetes
- For simpler setups, Docker Compose might be sufficient
