---
type: link
source: notion
url: https://val.packett.cool/blog/podfox/
notion_type: Software Repo
tags: ['Running']
created: 2025-05-09T00:25:00.000Z
---

# Podfox: World's First Container-Aware Browser - Home of Val Packett

## Overview (from Notion)
- Innovative Solutions: The concept of a container-aware browser challenges traditional development environments, which may resonate with your desire for efficiency and modern solutions in your work as a software engineer and founder.

- Work-Life Balance: Emphasizing the use of containers can simplify the setup of development environments, potentially freeing up time for family and personal interests amidst a busy New York City lifestyle.

- Community & Collaboration: The article highlights collaboration with other developers, which could inspire you to engage more with local tech communities or lead workshops to share knowledge.

- Tech Trends: Staying abreast of technologies like Podman and containerization can position your company at the forefront of industry trends, especially in a fast-paced city like NYC.

- Pragmatic Approach: The practical solutions discussed can encourage a more adaptable mindset towards problem-solving, which can be beneficial in both personal and professional scenarios.

- Alternative Views: While containerization offers many benefits, consider the potential downsides, such as complexity in debugging or issues with dependency management, which can create challenges in your projects.

- Future of Development: The emphasis on container technology hints at a shift in how software development might evolve, suggesting that embracing these tools could be pivotal for your company's growth and innovation.

## AI Summary (from Notion)
Podfox is a container-aware browser that eliminates port conflicts by allowing direct communication with container networks, simplifying the development process. It uses a SOCKS proxy to access services running in containers without needing traditional port forwarding, enhancing the efficiency of containerized environments. Additionally, it integrates with tools like Homebrew for a seamless development experience across different containers.

## Content (from Notion)

A port conflict pushed me to abolish container port forwarding once and for all, making my Firefox talk to Podman's whole network. Also: containerizing dev environments for command-line addicts.

Containers. Containers containers containers. Even if you were reluctant before, it’s likely that you use them at least for running various supporting infrastructure when working on projects that involve that kind of thing. Having a whole-system install of Postgres on a laptop shared between various different projects never actually felt right. Running podman run --rm -it -p 5432:5432 postgres:17 to pop up a temporary instance with no persistent state does.

These days, it’s very typical for any web backend or other kind of networked service project to include something like a docker-compose.yml file that makes it possible to just run all the service dependencies with one single command. And so I was running a Compose setup for one project, a serious business client consulting job thing, and I kept it in the background and I went to start up another project and—

oh no, that failed with EADDRINUSE. A port conflict.

Both projects involved RabbitMQ and both forwarded the management web UI port to the host:

```plain text
  queue:
    image: rabbitmq:3-management
    ports:
      - "15672:15672"

```

And as such, I couldn’t launch both projects without modifying the port numbers or something. So like any rational well-adjusted chill person, at that point I’ve decided that port forwarding Must. Be. ABOLISHED!!

Seriously though, we have Ptyxis as a container-aware terminal emulator… why isn’t there a container-aware web browser that would just communicate directly with the containers? (Does anyone remember Pow from the golden age of Rails that proposed the “just open yourapp.dev” experience?)

As the title suggests, now there kinda is a container-aware browser:

  Screenshot with a Firefox window on top showing a RabbitMQ management UI on http://myrabbit.randomtests.podman, and a terminal on the bottom shown launching podman run --rm -it --network randomtests --name myrabbit rabbitmq:3-management

Okay, the title is slightly exaggerated. It’s not that the browser itself was modified in any way. And no, it’s not just running inside of a Podman container. There’s a process running alongside everything that makes it possible, and it’s quite simple and tiny.

Can you already guess how it works? First, let’s see how we got here.

## How Do Containers Even Networking??

Back in the day, containering required root privileges and there was a daemon running as root, which always felt repulsive to me. It never was an inherent necessity, but Linux’s namespacing abilities weren’t good enough to run without privileges. These days —thankfully— they are, and Podman encourages running “rootless” (and daemonless).

In the old-school rootful setup, networking is pretty straightforward: the daemon can create bridge interfaces on the host, containers get assigned IP addresses on a bridged subnet, and they are accessible as if they were actual machines. And it’s possible to set up DNS on the host machine to resolve to container names but like… ugh, messing with DNS.

But as an unprivileged process we can’t just create bridges on the host (and I wouldn’t want anything to show up in the list of network interfaces, it bothers me to see Stuff there!) so what does Podman do?

You might’ve heard about networking being “all fake in userspace” with slirp4netns which is an amazing resurrection of early-90s modem era hacks that has just been replaced by a modern alternative called pasta (mm, tasty – wait, what’s that bypass4netns thing?). Heck, Podman’s actual “rootless tutorial” mentions these as the “rootless networking tools”. But… actually… that’s just the teeny tiny part that makes it possible for the unprivileged containers to reach out to the outside world.

The actual networking stack is the real Linux kernel one, namespaced.

Here’s what it actually looks like. Rootless Podman first creates a single network namespace called rootless-netns, inside of which it creates bridge networks, real Linux kernel bridges; and for each container that joins a network it spawns it makes a veth pair, one end of which is connected to the network’s bridge interface in the aforementioned common namespace, and the other end passed to the container’s own namespace.

And we can manually enter that “parent” namespace —without entering “a container”, only entering the network namespace— by running podman unshare --rootless-netns.

Wait, how does that work? Tell me, almighty strace!

```plain text
open("/run/user/1000/libpod/tmp/pause.pid", O_RDONLY|O_LARGEFILE) = 4
read(4, "1809", 11)                     = 4
open("/proc/1809/ns/user", O_RDONLY|O_LARGEFILE|O_CLOEXEC) = 5
fcntl(5, F_SETFD, FD_CLOEXEC)           = 0
open("/proc/1809/ns/mnt", O_RDONLY|O_LARGEFILE|O_CLOEXEC) = 6
fcntl(6, F_SETFD, FD_CLOEXEC)           = 0
setns(5, 0)                             = 0
setns(6, 0)                             = 0

```

Oh, umm, that’s it?? Wait, where’s the netw—

```plain text
openat(AT_FDCWD, "/run/user/1000/containers/networks/rootless-netns/rootless-netns", O_RDONLY|O_CLOEXEC) = 8
[…]
setns(8, CLONE_NEWNET)                  = 0

```

Right, that explains the mnt namespace above.

So the key is the setns(2) system call, which “allows the calling thread to move into different namespaces”. When it’s the only thread in the process, mind you, so we can’t just have different threads in different namespaces. But no one said we can’t retain open sockets from the previous namespace before switching! Just realizing that opens a world of possibilities. Now we can build a very elegant and simple…

## Proxy! Ding ding ding ding ding

If you guessed “proxy” before reading all of the above, congratulations! You win! :)

That is what Podfox actually is. It’s a SOCKS proxy that starts listening on the host system and then enters Podman’s rootless networking namespace in order to talk to your containers. It’s a portal into the container world, running as one simple process, written in Rust.

There’s no need to do any DNS on the host, as a proxy can handle hostnames however it likes, so Podfox parses <container>.<network>.podman hostnames, queries podman network inspect with the network name to find the gateway address for the network, finally sends a DNS query for <container>.dns.podman to that network’s gateway, connects to the returned address and starts proxying.

Beautiful.

It just works.

And you can install it from crates.io right now:

```plain text
cargo install --locked podfox

```

And run it as just podfox, it would listen on port :42666 by default. (It also support systemd socket activation!)

Now, um, we haven’t actually touched the “fox” part of it all. The browser. When I was first testing, I was using Multi-Account Containers’ (heh) ability to assign proxies per Firefox container, but that was just for testing.

Later I made a WebExtension to make a global proxy rule that assigns the Podfox proxy to the fake .podman TLD. It’s probably the simplest Firefox add-on ever that’s actually useful, as all it contained was a one-liner (!) background script:

```plain text
browser.proxy.onRequest.addListener(() => ({ type: "socks", host: "localhost", port: 42666, proxyDNS: true }), { urls: ["*://*.podman/*"] });

```

But I’m not feeling like publishing a literal one-liner to addons.mozilla.org. I am considering making a tiny add-on for creating rules of this sort via a settings UI, but for now I’ve discovered a simpler solution that doesn’t require any add-on publishing at all.

Yeah, it’s PAC (Proxy Auto-Configuration). Another 90s comeback, just like SLiRP!

Place the following in a file directly accessible to Firefox (I’m saying that because mind the Flatpak – if running Flatpak Firefox, expose a new directory through Flatseal with just the file):

```plain text
function FindProxyForURL(url, host) {
  if (host.endsWith('.podman'))
    return 'SOCKS5 localhost:42666';
  return 'DIRECT';
}

```

Finally, configure Firefox to use it (and tick the checkbox to proxy DNS names):

  Screenshot of Firefox proxy settings, set to 'Automatic proxy configuration URL' with a path of 'file:///home/val/.config/podfox/podfox.pac', and at the bottom the 'Proxy DNS when using SOCKSv[45]' checkboxes are checked

Now you have this virtual .podman TLD always accessible in the browser, and as long as the Podfox proxy is running, you can open any port on any container in any network in your rootless Podman runtime!

## Bonus: Containerizing my CLI Development Environment

So with this ability to browse services running in containers, and without using port forwarding, the services under development must run in containers as well, of course.

There’s been an explosion of container dev tools in the recent years. I’ve heard of Tilt which provides a workflow where service containers by default get constantly rebuilt (and on top of that there’s an option for supporting live-reloading by copying changes into the container) and there’s a nice UI page for watching all the logs and the “most heavily suggested” runtime is a local Kubernetes cluster (even though just running in Podman is also possible). And the Development Container Specification™ from MicrosoftⓇ comes from the VSCode and GitHub Codespaces world and provides a manifest format that lets (typically) IDEs know how to set up a container where (typically) the Run button would run the app (and the language server and other related tools).

But I like my command-line environment and I don’t want it to be disrupted! I edit code in Helix —which runs language servers that might share their caches with the actual build— and run a variety of random tools, all from my fish shell configured with a prompt that I like and so on.

Trying to run just-the-project-parts like the compiler, the service itself, the language server and language-specific tools like linters and formatters inside of the container sounds kinda painful, as for example Helix doesn’t have a “wrap all the tools in something” option, and configuring the PATH to include containerized tools or wrapping invocations manually sounds very annoying. I’d rather… bring my whole environment into each container!

Running a container with my dotfiles is surprisingly easy: -v $HOME/.config:$HOME/.config:ro – thankfully pretty much everything I use supports XDG directories and doesn’t pollute ~ with random paths. But what about the shell, the editor, the random tools? Building my own containers per project that add my tools on top of the project’s image sounds annoying, slow and heavy. Installing them in an overlay volume that wouldn’t even be a container image (which seems to be how VSCode dev containers do stuff) feels like a “dirtier” version of the same. Can’t I just -v mount them?

Well, with how my setup already was, most of my tools were installed by an updatetools script into ~/.local directories. However, of course, they’re built for the host system — dynamically linking, currently, to Chimera’s musl libc, LLVM libc++, and occasionally to various other system-wide libraries. They weren’t going to work in a random Debian-based container, unless packed with sharun or whatever was the tool that I saw ages ago, but the whole point is to avoid “weird stuff” like this. And I don’t want to build static binaries either. Not everything can work as static binaries, even.

That’s when it hit me.

The answer is to get Homebrew.

Yes, that same package manager that came from the macOS world and always had to consider the host OS as sorta immutable, which in the old days was seen as a workaround for a proprietary OS, but now is a huge asset. Homebrew manages a separate unprivileged prefix, and has prebuilt packages with a fixed one, currently /home/linuxbrew/.linuxbrew on Linux. (It also does GoboLinux-style multi-versioning, which I like to jokingly call “Nix for those of us who touch grass”, but that’s not very relevant right now.)

With containers, we can just mount Homebrew’s prefix: -v /home/linuxbrew:/home/linuxbrew:ro. And append it to the PATH with Podman’s nice env-merge feature: --env-merge PATH=\${PATH}:/home/linuxbrew/.linuxbrew/sbin:/home/linuxbrew/.linuxbrew/bin. And now we can change the --entrypoint to the homebrewed fish… and we’re off to the races!

  Screenshot of a terminal, first running fastfetch that shows Chimera Linux, then running 'podman run --rm -it --tz local -v /home/linuxbrew:/home/linuxbrew:ro --env-merge PATH=${PATH}:/home/linuxbrew/.linuxbrew/sbin:/home/linuxbrew/.linuxbrew/bin -e XDG_CONFIG_HOME=$HOME/.config -v $HOME/.config:$HOME/.config:ro -v $PWD:$PWD -w $PWD --entrypoint (which fish) haskell:9.10.1', the same shell prompt appears, fastfetch is run and shows Debian

Now THAT’S what I call “distro hopping”!

Despite the superficial similarity with Distrobox the above screenshot has at a glance, this is a different idea. Remember, we’re still talking about project-specific dev containers. This is not a persistent “pet” container where you persistently install packages from another distro,

this is a runtime COMPOSITION of an ephemeral/“cattle” project-specific dev container that just has the project’s toolchain, and a “pet” user environment, mounted read-only.

And because it’s mounted, there are no redundant copies that can get outdated and no delay for copying/installing stuff! This is really cool. I can just enter any container image while bringing all my comfy stuff with me, instantly.

I went all-in on Homebrew, mostly replacing my custom tool installation/update script with a Brewfile, and I’m really happy about it. As a bonus, it also makes the original full-system kind of distro hopping easier! If I use Homebrew for all my CLI stuff and Flatpak for all my GUI stuff, I could be using something as fixed and bare-bones as GNOME OS for the host! Though I’m currently most intrigued by AerynOS which reflects a lot of my engineering values and choices.

Anyway, so, I started by writing out these long podman run invocations and quickly felt the need to automate them. The result is called Podchamp (current version permalink) as a silly internet reference. It’s just a fish script that lives in my dotfiles, I’m not releasing it as a Real Project™ since it’s tiny and relatively specific to the way I personally do things, but what it does is simple: it finds the first .podchamp[.local] config file above the working directory (in a “project root”), reads container-running instructions and either runs a podman container or execs into an existing one. The instructions look like:

```plain text
image mycoolproject-dev:latest
pod pod_mycoolproject
network mycoolproject_app-network
name mycoolproject-dev
persist /var/cache/rust
env CARGO_TARGET_DIR=/var/cache/rust
requires mycoolproject_postgres mycoolproject_rabbitmq

```

so it’s basically a bunch of convenience to store the per-project development container configuration in an actual file and not in shell history. And it’s been working great for me!

It also emits OSC 777 sequences to indicate to Ptyxis which container has been just entered, which (for now) Podman itself doesn’t do. The container-awareness in the terminal emulator is really nice for being able to spawn new tabs in the same container as the current tab – yes, not that much more, but that’s huge for UX. It would be nice to have the same experience in other terminals — there’s a prototype for Ghostty already, and I’m looking into making it work in WezTerm.


