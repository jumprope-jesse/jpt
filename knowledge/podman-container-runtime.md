# Podman Container Runtime

*Source: [Why I Ditched Docker for Podman](https://codesmash.dev/why-i-ditched-docker-for-podman-and-you-should-too) - Added: 2026-01-18*

## Why Switch from Docker to Podman?

### The Docker Daemon Problem

Docker's architecture relies on a persistent daemon (`dockerd`) that:
- Runs with **root privileges** always
- Acts as intermediary for all container operations
- If compromised, exposes the entire host system
- When it crashes, takes down all containers

### Notable Docker Security Vulnerabilities

- **CVE-2019-5736** (runC escape) - Container process could overwrite host's runc binary
- **CVE-2022-0847** "Dirty Pipe" - Kernel flaw enabling container-to-host abuse
- **CVE-2022-0492** (cgroups v1) - Privilege escalation via release_agent
- **CVE-2024-21626** "Leaky Vessels" - fd leak enabling host FS access
- **2024** - Active cryptojacking campaigns targeting exposed Docker APIs

### Podman's Architecture

**Daemonless** - no persistent background service. Each `podman run` spawns a direct child process.

**Benefits:**
- Containers run under user privileges (rootless by default)
- Even root inside container = unprivileged on host
- One container crash doesn't affect others
- Reduced attack surface
- Lower resource usage (no daemon overhead)

## Key Podman Features

### Systemd Integration
Generate proper systemd unit files directly:
```bash
podman generate systemd --name my-app > /etc/systemd/system/my-app.service
systemctl enable --now my-app
```
First-class Linux service management: boot dependencies, auto-restart, resource limits.

### Kubernetes Alignment
- Native pod support (Red Hat maintains both Podman and K8s components)
- Generate K8s YAML from local pods:
```bash
podman generate kube my-pod > deployment.yaml
```
- Local dev environment matches production deployment

### Toolchain Philosophy
Instead of monolithic Docker:
- **Podman** - Run containers
- **Buildah** - Fine-grained image building
- **Skopeo** - Inspect/copy images between registries

## Migration Guide

### fly-to-podman Migration Script

*Source: [Edu4rdSHL/fly-to-podman](https://github.com/Edu4rdSHL/fly-to-podman) - Added: 2026-01-18*

A bash script for migrating from Docker to Podman that preserves:
- Container data
- Configurations (mounts, ports, etc.)
- Images and volumes

```bash
# See full blog post: "From Docker to Podman: full migration to rootless"
# by the script author
```

Useful for bulk migration rather than manually recreating each container.

### CLI Compatibility
Podman is CLI-compatible with Docker:
```bash
# Option 1: Alias
alias docker=podman

# Option 2: Just use podman directly
podman build -t my-app .
podman run -d -p 8000:8000 my-app
podman ps
```

Existing Dockerfiles work without modification.

### Docker Compose Options

**Option 1: podman-compose**
```bash
pip install podman-compose
podman-compose up -d
```

**Option 2: Convert to K8s YAML**
```bash
podman-compose up -d  # start services
podman generate kube my-service > k8s.yaml
```

### Pods for Multi-Container Apps
```bash
# Create a pod
podman pod create --name my-app -p 8000:8000

# Add containers to the pod (shared network namespace)
podman run -d --pod my-app --name db postgres
podman run -d --pod my-app --name api my-app:latest
# API can reach DB at localhost:5432
```

### Production Deployment
```bash
# Generate systemd service
podman generate systemd --name my-app --files --new

# Enable user services to persist without login
loginctl enable-linger $(whoami)

# Enable service
systemctl --user enable --now container-my-app.service
```

## Common Gotchas

### Privileged Ports (< 1024)
Rootless containers can't bind to privileged ports. Solutions:
- Use a reverse proxy (recommended anyway)
- Use higher ports (e.g., 8080 instead of 80)
- Run specific containers in rootful mode if needed

### Volume Permissions
Rootless containers run as your user. Ensure ownership:
```bash
mkdir -p ./data && chown $(id -u):$(id -g) ./data
```

### Docker Socket Compatibility
For tools expecting `/var/run/docker.sock`:
```bash
# Start Podman's Docker-compatible API
podman system service --time=0 unix:///tmp/podman.sock &

# Or for system-wide
systemctl enable --now podman.socket
```

### macOS/Apple Silicon Notes
Podman runs in a VM on macOS. Performance considerations:
- Check Podman Desktop for GUI experience
- Some overhead due to Rosetta emulation on Apple Silicon
- Getting better with each release (especially 5.6+)

## Installation

| Platform | Command |
|----------|---------|
| Ubuntu/Debian | `sudo apt update && sudo apt install podman` |
| Fedora/RHEL | `sudo dnf install podman` |
| macOS | `brew install podman` or Podman Desktop |

## When Docker Still Makes Sense

- Existing large ecosystem/tooling investment
- Team familiarity
- Some edge cases with specialized tooling
- If inertia outweighs security benefits for your use case

## Summary

Podman offers:
- Rootless by default (better security)
- No daemon (cleaner architecture, less resource usage)
- Kubernetes-native design
- Drop-in Docker CLI replacement
- First-class systemd integration

For new projects or security-conscious environments, Podman is the clear evolution.

---

## Podfox: Container-Aware Browser Proxy

*Source: [Podfox: World's First Container-Aware Browser](https://val.packett.cool/blog/podfox/) - Added: 2026-01-18*

### The Port Conflict Problem

When running multiple docker-compose projects, port conflicts are inevitable:
```yaml
# Project A
queue:
  image: rabbitmq:3-management
  ports:
    - "15672:15672"

# Project B - CONFLICT!
queue:
  image: rabbitmq:3-management
  ports:
    - "15672:15672"
```

**Solution**: Abolish port forwarding entirely with container-aware networking.

### How Rootless Podman Networking Actually Works

Despite common belief that rootless networking is "all fake in userspace" via slirp4netns/pasta, the actual networking stack uses real Linux kernel bridges:

1. Podman creates a single network namespace called `rootless-netns`
2. Inside that namespace, it creates real Linux kernel bridge networks
3. For each container joining a network, it creates a veth pair:
   - One end connects to the network's bridge in the common namespace
   - Other end passes to the container's own namespace

**Key insight**: You can enter this "parent" namespace with:
```bash
podman unshare --rootless-netns
```

This uses `setns(2)` syscall to move into different namespaces. Sockets opened before switching namespace remain valid - enabling elegant proxy solutions.

### Podfox Architecture

A SOCKS proxy that:
1. Starts listening on the host system
2. Enters Podman's rootless networking namespace
3. Talks directly to containers without port forwarding

**How hostname resolution works**:
- Parses `<container>.<network>.podman` hostnames
- Queries `podman network inspect` to find gateway address
- Sends DNS query to `<container>.dns.podman` via that gateway
- Connects to returned address and proxies

### Installation & Setup

```bash
# Install
cargo install --locked podfox

# Run (listens on port 42666 by default)
podfox
```

**Firefox Configuration** (PAC file at `~/.config/podfox/podfox.pac`):
```javascript
function FindProxyForURL(url, host) {
  if (host.endsWith('.podman'))
    return 'SOCKS5 localhost:42666';
  return 'DIRECT';
}
```

Configure Firefox: Settings → Network → Automatic proxy configuration URL → `file:///path/to/podfox.pac`
Enable "Proxy DNS when using SOCKS v5"

**Result**: Access any container at `http://containername.networkname.podman`

---

## Containerized CLI Development Environments

*From same Podfox article*

### Bringing Your Environment Into Containers

Instead of building project-specific images with your tools, **mount them**:

```bash
podman run --rm -it \
  -v /home/linuxbrew:/home/linuxbrew:ro \
  --env-merge PATH=\${PATH}:/home/linuxbrew/.linuxbrew/sbin:/home/linuxbrew/.linuxbrew/bin \
  -v $HOME/.config:$HOME/.config:ro \
  -v $PWD:$PWD \
  -w $PWD \
  --entrypoint $(which fish) \
  haskell:9.10.1
```

**Key mounts**:
- `/home/linuxbrew` - Homebrew prefix (read-only)
- `$HOME/.config` - Dotfiles/configs (read-only)
- `$PWD` - Current project directory

**Why Homebrew?**
- Self-contained `/home/linuxbrew/.linuxbrew` prefix
- Prebuilt packages designed for unprivileged use
- Works across different base container images

### Philosophy: Ephemeral Composition

This is NOT Distrobox (a persistent "pet" container). This is:

> "Runtime COMPOSITION of an ephemeral/'cattle' project-specific dev container that just has the project's toolchain, and a 'pet' user environment, mounted read-only."

Benefits:
- No redundant copies that get outdated
- No delay for copying/installing
- Instant entry into any container with full tooling

### Podchamp Config Format

Project config file (`.podchamp` or `.podchamp.local`):
```
image mycoolproject-dev:latest
pod pod_mycoolproject
network mycoolproject_app-network
name mycoolproject-dev
persist /var/cache/rust
env CARGO_TARGET_DIR=/var/cache/rust
requires mycoolproject_postgres mycoolproject_rabbitmq
```

### Terminal Container Awareness

**Ptyxis** (GNOME terminal): Container-aware, can spawn new tabs in same container as current tab.

Uses OSC 777 sequences to indicate which container is active. Support coming to:
- Ghostty (prototype exists)
- WezTerm (in progress)
