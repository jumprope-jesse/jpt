---
type: link
source: notion
url: https://codesmash.dev/why-i-ditched-docker-for-podman-and-you-should-too
notion_type: Tech Deep Dive
tags: ['Running']
created: 2025-09-05T14:28:00.000Z
---

# Switching from Docker to Podman

## Overview (from Notion)
- Switching from Docker to Podman could streamline your development processes, making deployments safer and more efficient, helping you spend more time with family.
- Podman's daemonless architecture reduces overhead, which might resonate with your desire for simplicity in both work and home life.
- The focus on security in Podman aligns with the responsibility of protecting your family's digital environment.
- Emphasizing systemd integration allows better management of services, freeing you to focus on your startup’s growth.
- The ease of migration means you can adapt quickly without disrupting your workflow, ideal for a busy parent balancing multiple roles.
- Unique viewpoints: Podman’s alignment with Kubernetes may prepare you for future tech trends, enhancing your company’s competitiveness.
- Alternate views: Docker has a vast ecosystem; some may argue against switching due to the inertia of existing projects and community support.

## AI Summary (from Notion)
The transition from Docker to Podman offers significant security benefits by eliminating the need for a persistent daemon, thus reducing vulnerabilities. Podman runs containers under user privileges, enhancing security and stability, while also integrating seamlessly with systemd and Kubernetes. The migration process is straightforward, with existing Dockerfiles typically requiring no changes. Podman’s architecture allows for cleaner resource management and better alignment with Linux practices, making it a compelling choice for modern container workflows.

## Content (from Notion)

I'm old enough to remember when Vagrant looked like a promised land where every development environment would look the same. Differences between language versions, as well as some unusual OS version differences, resulted in a few days of unproductive debugging of your development environment. I've had similar excitement when I started my first Docker Swarm (who uses that these days?!) - it felt revolutionary. Docker wasn't just a tool - it fundamentally changed how we thought about application development and deployment. Having a repeatable, separated environment from your local system was refreshing and looked like a superpower. It has become a must-have tool for every engineer. "Just Dockerize it" became my go-to solution for pretty much everything. Sure, architecture or defining a new Docker image could be a bit finicky at times, but hey, that's just how things worked. Is the persistent dockerd daemon eating upresources in the background with root privileges, just the price of doing business? I thought so.

If you are in this industry long enough, there is one pattern that emerges every day. Everybody begins questioning the "that's just how it's done" mentality. Along the way, the quiet Docker daemon running in the background felt less like a comfortable constant and more like a ticking bomb. More and more ways to explore this vulnerability emerged:

2019-02-11 - CVE-2019-5736 (runC container escape): lets a process in a container overwrite the host’s runc binary → full host compromise if exploited.

2022-03-07 - CVE-2022-0847 “Dirty Pipe” (Linux kernel): read-only file overwrite in kernel; practical container-to-host abuse scenarios documented by Docker/Sysdig.

2022-03-07 - CVE-2022-0492 (cgroups v1 release_agent): privilege escalation / container escape via cgroups v1; mitigations via seccomp/AppArmor/SELinux.

2024-01-31 - CVE-2024-21626 (runC “Leaky Vessels”): fd leak + process.cwd issues enabling host FS access and potential escape; fixed in runC 1.1.12 (Docker Engine ≥ 25.0.2).

2024-02-01 - CVE-2024-23651/23652/23653 (BuildKit, “Leaky Vessels”): build-time issues that can affect host files; fixed in BuildKit 0.12.5.

2024-09-23 - In-the-wild cryptojacking campaign: attackers targeted exposed Docker APIs and microservices.

2024-10-01 - Docker API swarm botnet campaign: cryptojacking via exposed Docker Engine API (details).

I had been seeking an alternative (I assumed that someone had already questioned the status quo), and that's how I stumbled into Podman territory. It began as casual curiosity - "Hey, let me check out this thing" - turned into a complete overhaul of my container workflows and pulled me into using Fedora in my home lab. And honestly? I wish I'd made the switch sooner.

Here's the fundamental issue that kept me awake: Docker's entire architecture is built around a persistent background service - the dockerd daemon. Whenever you run a docker command, you're actually talking to this daemon, which then does the heavy lifting. Sounds about right?

Yes?!

Or rather NO, because this daemon runs with root privileges. Always. And if something goes south with a daemon - innocent bug, a crash, or worst case scenario, a security exploit - your entire container ecosystem is potentially compromised. Not just the containers, daemon, or resource that you assigned to it, but the whole host system. It was a huge relief that Podman threw this model out the window. No daemon, no processes running in the background. When you run podman run my-app, the container becomes a direct child of your command. And it is running under your user privileges. Simple architecture change with huge implications:

Remember those late-night security advisories about Docker daemon vulnerabilities (ex., when dockerd was misconfigured to listen on TCP:2375 without TLS, attackers could spin up privileged containers remotely)? With Podman, even if someone somehow escalates privileges inside a container to root level, they're still just an unprivileged user on the actual host. It significantly reduces the surface of an attack.

Usually Docker daemon runs just fine. But when hiccups kick in - oh boy, hold your hats, as it will take down multiple containers at once. With Podman when one container crashed, the other kept running like nothing happened. It makes so much sense, and it's built in the spirit of hermetization.

I had been surprised when my MacBook M2 Pro started to get warmer when left unattended. After a brief investigation (with Activity Monitor), it was obvious - Docker never knows when to stop. No constantly running daemon means less memory usage. Unfortunately, running a container using Podman can be a different story (ekhm: blog.podman.io/2025/06/podman-and-apple-ros..) - yet the thing is getting better: blog.podman.io/2025/08/podman-5-6-released-...

Beyond the obvious daemon advantages, Podman brings some genuinely clever features that make day-to-day container work more pleasant:

Systemd integration that doesn't suck: This one's huge if you're working on Linux servers (most of us are). Podman justgenerates proper systemd unit files. Boom, your container is a first-class citizen in the Linux service ecosystem. Boot dependencies, automatic restarts, resource limits - it all just works. I can run podman generate systemd --name my-app and get a clean service file. Afterwards, I can enable, start, stop, and monitor with standard systemctl commands. Say bye-bye to third-party process managers.

Kubernetes alignment that's not just marketing: Since Red Hat (the folks behind Podman) is also a major Kubernetes contributor, the tool feels like it was designed with K8s in mind from day one. The native pod support isn't just a bolt-on feature - it's central to how Podman works. I do not need to run k3s or any local substitute for Kubernetes. Now, I can prototype multi-container applications as Podman pods locally. Then I just generate Kubernetes YAML directly from those pods with podman generate kube. My local development environment actually looks like what I'm going to deploy. This was revolutionary when I had to take over the responsibility of managing and developing a quite complex cluster.

The Unix philosophy done right: Instead of trying to be everything to everyone, Podman focuses on running containers well and delegates specialized tasks to purpose - built tools. Need to build images with fine - grained control? That's Buildah. Want to inspect or copy images between registries? Skopeo's your friend. I can use the best tool for each job. I'm no longer stuck with whatever image-building quirks Docker decides to implement.

## The Migration That Wasn't Really a Migration

Here's the part that surprised me most: switching from Docker to Podman was almost seamless. The Podman folks clearly understood that creating the next standard would not let them win the market, and they just adhered to the known CLI tool. I literally just aliased docker=podman in my shell and carried on with life. podman run, podman build, podman ps - they all behave exactly like their Docker counterparts. My existing Dockerfiles worked without modification. My muscle memory didn't need retraining.

Though there were a few places where I did hit differences that were actually improvements in disguise:

- Privileged ports in rootless mode not working? Good! That's security working as intended. A reverse proxy setup is a better architecture anyway.
- Some volume permission quirks? Yes - but it's a small price, and again - if you do it right, you are limiting the scope of possible attack.
- A few legacy tools that expected the Docker socket? If there is no support by now, just remember that Podman can expose a Docker-compatible API if needed.
- If your Docker Compose workflow is overly complex, just convert it to Kubernetes YAML. We all use Kubernetes these days, so why even bother about this? Having the same layout for development and production is a huge bonus of doing so.
After six months of running Podman in production, here's what I've noticed:

I'm sleeping much better. Because I'm personally responsible for security, I do not have to check if every container is running in rootless mode. Something that I did not think I would benefit from is that my monitoring dashboards show cleaner resource usage patterns. Don't get me wrong - Docker isn't going anywhere. It has massive momentum, a mature ecosystem, and plenty of organizational inertia keeping it in place. But for new projects, or if you are able to make technical decisions based on merit rather than legacy, Podman represents a clear evolution in container technology. More secure by design, more aligned with Linux system management practices, and more thoughtfully architected for the way we actually deploy containers in 2025. The best way forward is to question the assumptions you didn't even realize you were making.

Just to prove how easy transition can be, here's a practical walkthrough of migrating a FastAPI application from Docker to Podman.

Your existing FastAPI project with its Dockerfile and requirements.txt

Podman is installed on your system:

- Ubuntu/Debian: sudo apt update && sudo apt install podman
- Fedora/RHEL: sudo dnf install podman
- macOS: Grab Podman Desktop for a GUI experience
- Windows: If you are not a C# developer - stop doing this to yourself and just use Linux: youtube.com/watch?v=S_RqZG6YR5M
### Step 1: Your Dockerfile Probably Just Works

This is the beautiful part—Podman uses the same OCI container format as Docker. Your existing Dockerfile should work without any changes. Here's a typical FastAPI setup:

Instead of docker build, just run:

That's it. Same flags, same behavior, same output. If you want to ease the transition, create an alias:

Now you can use your existing docker build commands without thinking about it.

For development and testing:

For background services:

Your app should be accessible at localhost:8000 just like before.

Important note: By default, Podman runs in rootless mode. This is a security win, but it means you can't bind directly to privileged ports (below 1024). For production, you'll want a reverse proxy anyway, so this pushes you toward better architecture.

### Step 4: Production Deployment with Systemd

This is where Podman really shines. Instead of wrestling with custom service management, generate a proper systemd unit file:

Now your FastAPI app is managed like any other system service. It'll start on boot, restart on failure, and integrate with standard Linux logging and monitoring tools.

For server deployments where you want the service to persist even when you're not logged in:

loginctl enable-linger $(whoami)

### Step 5: Multi-Service Applications with Pods

If your FastAPI app needs a database or other services, Podman's pod concept is cleaner than Docker Compose for simple setups:

Now your FastAPI app can reach PostgreSQL at localhost:5432 because they share the same network namespace.

### Step 6: Docker Compose Compatibility

For existing Docker Compose setups, you have options:

Option 1: Use podman-compose as a drop-in replacement:

Option 2: Convert to Kubernetes YAML for a more cloud-native approach:

This second option is particularly nice if you're planning to deploy to Kubernetes eventually.

Common Gotchas and Solutions

Volume permissions: If you hit permission issues with mounted volumes, remember that rootless containers run as your user. Make sure your user owns the directories you're mounting:

Legacy tooling: Some tools expect the Docker socket at /var/run/docker.sock. Podman can provide a compatible API:

Performance tuning: For production workloads, you might want to tune the rootless networking stack or consider running specific containers in rootful mode for maximum performance.

The migration process is usually much smoother than people expect. Start with a development environment, get comfortable with the workflow differences, then gradually move production workloads. The security and operational benefits make it worth the effort.


