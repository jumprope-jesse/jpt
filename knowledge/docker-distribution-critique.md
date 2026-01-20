# The Curse of Docker as a Distribution Method

*Source: [computer.rip - The Curse of Docker](https://computer.rip/2023-11-25-the-curse-of-docker.html) - Added: 2026-01-19*

## Core Thesis

Docker containers are excellent for DevOps/orchestration environments, but terrible as a "lowest common effort" approach to distributing end-user server software. The problems that traditional package management solved (dependency hell, version conflicts) get replaced with new problems at a higher abstraction layer.

## The Irony

Docker was heralded as the solution to "works for me" syndrome, yet now produces the same problem at a higher configuration level. Distribution via Docker image often signals an **immature project** lacking proper distribution expertise.

## Configuration Hell

### The Problem
No consistent conventions for configuration in Docker-distributed software, unlike traditional Linux software's predictable text file approach.

### Common Anti-Patterns

**Environment Variables (12-factor app style)**
- ✅ Easy to provide on command line
- ❌ Terrible for structured data
- ❌ Shell scripts have clumsy handling of complex values
- Works for simple DevOps but breaks down for end-user software

**Configuration Files with Complications**
- Multiple ways to mount them (bind mounts, volumes, configmaps)
- Inconsistent documentation on which method to use
- Ownership and permission caveats

**Entrypoint Script Hell**
- Scripts generate config from "simpler" input
- Often poorly documented or undocumented
- Abstraction makes troubleshooting harder
- Common scenario: software fails referencing a config key you never provided, forcing you to dig through entrypoint script source

**Opinionated Scripts**
- "Opinionated" = "unsuitable for any configuration except the developer's"
- Author has rebuilt Docker images dozens of times to fix/augment entrypoint scripts that don't expose parameters the underlying software supports

**Worst Case**
- No documentation at all
- Shell into container to find actual config file location
- **Mandatory**: Docker images MUST provide basic README on configuration

## Filesystem Problems

### Sandbox + Linux Filesystems = Pain
Docker's isolation has same problems as all sandboxes - Linux filesystems don't play nice.

**Named Volumes**:
- Need dummy containers to interact with volume files
- Complicates backups and troubleshooting
- Inconsistent behavior between Docker versions and Podman

**The UID Sin**:
- Docker normalized running as **root** (terrible practice)
- Defense in depth means even with isolation, root is bad
- User UID mapping creates NFS-style puzzles
- Hostmounts with non-root users = UID mapping hell
- Often forces container rebuilds to fix UID issues

## Non-Portable Containers

The irony: Docker promises portability but common practices destroy it.

### Common Portability Failures

**Network Assumptions**:
- Non-default networks in Docker Compose often fail on complex network setups
- Assumes default ports are available
- Hard-codes well-known ports

**Feature Over-Enabling**:
- Enables features without disable options
- Assumes common values that don't work everywhere

### TLS Nightmare

**The Problem**: Many Docker images assume they'll individually handle TLS.

**Why This is Terrible**:
1. **Security**: Private keys should be closely guarded, stored in ONE place, accessible to ONE principal
2. **Complexity**: TLS is complicated to configure
3. **Virtual Hosting**: Most self-hosters use SNI/virtual hosting with wildcards
4. **Best Practice**: Single point for TLS termination

**The Madness**: Docker Compose stacks that want to use ACME to issue their own certificates!

**Author's Principle**: Docker containers should NEVER terminate TLS.

**Reverse Proxy Benefits**:
- Centralized TLS
- Defense in depth
- Would never expose container directly to internet anyway

## The Single-Purpose Computer Fallacy

### The "Raspberry Pi Effect"

**Problem**: Cheap single-board computers have addled hobbyists' minds.

Self-hosted software packages assume dedicated hardware:
- Software with "pi" in the name = big red flag
- No documentation for running on shared devices
- Author prefers computers that perform MULTIPLE tasks, especially 24/7 ones

### Examples

**HomeAssistant**:
- Actively resists running with neighbors
- Pops "unsupported software detected" warning after every update
- Author's reaction: "Can you imagine if Postfix whined in its logs if it detected neighbors?"

**NextCloud**:
- Author burned 2 hours trying to get all-in-one Docker image working
- Gave up, installed manually
- Discovered it was "plain old PHP application of the type I was regularly setting up in 2007"
- **Question**: "Is this a problem with kids these days? Do they not know how to fill in config.php?"

## Hiding Sins

### The Low Barrier Problem

Creating an RPM or Debian package has a barrier to entry. Docker is too easy.

**Result**: Distributing only as Docker image often means:
- Relatively immature project
- No one specializes in distribution
- Expect friction in nonstandard environments

### The Mistake

Docker was supposed to be "simple" - but this led to:
- Large projects with corporate backing
- Still distribute as "decidedly amateurish Docker Compose stack"
- Lack of distribution engineering personnel
- Changing landscape makes Docker stacks more palatable than VM appliances

## Historical Context

### Linux Package Management Philosophy

Traditional Linux distributions consolidated on:
- **Centralized dependencies**: Libraries in common locations
- **Version compatibility**: Main challenge of distro maintenance
- **Mutual compatibility**: Stable distros (RHEL) provide reliable but infrequent updates

### The Pain Points

**For Software Maintainers**:
- Deal with multiple distros
- Multiple old versions
- Various build/config quirks

**For Package Maintainers**:
- Bend upstream software to comply with distro policy
- Solve version/dependency problems

**Result**: Wild scramble, everyone gets mad.

### Desktop Solutions Work Better

Flatpak, Snap, AppImage work reasonably well because:
- Desktop apps interact mostly with users
- Configuration via own interface
- Limited interaction surface (GUI window)
- Easier to sandbox

**Server Software is Different**:
- Complex configuration needs
- Network interactions
- Filesystem requirements
- Service integration

## When Docker Works

**Good Use Cases**:
- DevOps environments with central planning/management
- Container orchestration (original use case)
- Environments where TLS is terminated elsewhere
- Standardized deployments

**Docker images that work correctly with minimal effort don't make for billable hours** (author is DevOps consultant).

## The Taxonomy of Docker Gone Bad

1. **Configuration inconsistency** - no conventions
2. **Filesystem friction** - UID hell, volume complexity
3. **Portability failures** - network assumptions, TLS hubris
4. **Single-purpose mindset** - Pi-brain syndrome
5. **Immature distribution** - hiding lack of expertise

## Key Insights

> "It is a palpable irony that Docker was once heralded as the ultimate solution to 'works for me' and yet seems to just lead to the same situation existing at a higher level of configuration."

> "Distributing an application only as a Docker image is often evidence of a relatively immature project, or at least one without anyone who specializes in distribution."

> "I would probably never expose a Docker container with some application directly to the internet. There are too many advantages to having a reverse proxy in front of it."

## Author's Aging Cantankerousness

The author acknowledges this is mostly opinion and admits to getting "older and thus more cantankerous." 15 years ago might have written nearly identical article about RPMs from small projects.

**But**: Surprised that projects can reach large size with substantial corporate backing and still distribute as amateurish Docker Compose stack.

## Related Topics

- See `podman-container-runtime.md` for security-focused Docker alternative
- See `orbstack-docker-macos.md` for improved Docker experience on macOS
- Traditional package management philosophy
- DevOps vs. end-user software distribution patterns
