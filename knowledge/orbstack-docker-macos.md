# OrbStack - Docker & Linux for macOS

*Source: [orbstack.dev](https://orbstack.dev/) - Added: 2026-01-18*

## What It Does

Fast, lightweight Docker Desktop alternative for macOS. Runs Docker containers and Linux VMs with minimal resource usage.

## Key Features

### Performance
- **Fast startup**: Containers start in seconds
- **VirtioFS file sharing**: Fast host-container file sync
- **Rosetta x86 emulation**: Smooth emulation on Apple Silicon
- **Optimized networking**: Turbocharged container networking

### Resource Efficiency
- **Low CPU usage**: Minimal background CPU drain
- **Low memory**: Less RAM consumption than Docker Desktop
- **Battery friendly**: Designed to not drain laptop battery
- **Native Swift app**: Small footprint, macOS-native

### Integration
- **Drop-in Docker replacement**: Works with existing docker/docker-compose commands
- **CLI integration**: Seamless terminal experience
- **SSH editing**: Remote editing into Linux machines
- **File sharing**: Easy host-container file access

### Additional Capabilities
- **Linux distros**: Run full Linux VMs alongside containers
- **Kubernetes**: Local K8s support
- **Menu bar app**: Manage containers/machines from anywhere
- **Robust networking**: IPv6 support, VPN-friendly, DNS works properly

## Why Use OrbStack vs Docker Desktop

| Aspect | OrbStack | Docker Desktop |
|--------|----------|----------------|
| Resource usage | Minimal | Higher |
| Startup time | Seconds | Slower |
| Battery impact | Low | Noticeable |
| App size | Smaller | Larger |
| Licensing | Freemium | Subscription required for business |

## vs Podman on macOS

Both OrbStack and Podman run in VMs on macOS (required for Linux containers).

**OrbStack**:
- Polished macOS-native experience
- Better GUI/menu bar integration
- Optimized specifically for Mac
- Commercial product (freemium model)

**Podman**:
- Open source, fully free
- Daemonless architecture (see `podman-container-runtime.md`)
- Better security model (rootless by default)
- Getting better on Mac with each release (5.6+)

**Recommendation**: OrbStack for "it just works" Mac experience; Podman for security-focused or cross-platform consistency.

## Use Cases

- **Local development**: Run dev databases, services, APIs
- **Docker Compose projects**: Drop-in replacement
- **Linux tooling**: Full Linux environment on Mac
- **Kubernetes development**: Local K8s testing

## Installation

Available from [orbstack.dev](https://orbstack.dev/) or via Homebrew:

```bash
brew install orbstack
```

## Considerations

- macOS only (not for Linux servers)
- Freemium model - check pricing for team use
- For production servers, use native Docker/Podman on Linux
