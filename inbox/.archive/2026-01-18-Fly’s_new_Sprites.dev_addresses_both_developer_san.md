---
type: link
source: notion
url: https://simonwillison.net/2026/Jan/9/sprites-dev/
notion_type: Software Repo
tags: ['Running']
created: 2026-01-11T06:46:00.000Z
---

# Fly’s new Sprites.dev addresses both developer sandboxes and API sandboxes at the same time

## Overview (from Notion)
- Developer Sandboxes: Think of how Sprites.dev could streamline your coding projects, allowing you to experiment safely without risking your main environment, especially useful with kids around when time is limited.

- API for Untrusted Code: This could enable you to build innovative applications that safely run untrusted user inputs, perfect for interactive projects or educational tools for your children.

- Checkpoints: The ability to save and restore environments could save you from the frustration of setup time, letting you quickly switch contexts as a founder juggling multiple projects.

- Scale-to-Zero: Cost-effective for a startup, you only pay when your environments are active, making it easier to manage expenses while exploring new ideas.

- Sustainability: Leveraging these technologies might align with your values of creating efficient, eco-friendly solutions in your ventures.

- Alternate Viewpoints: Some might argue that such powerful sandbox environments could lead to misuse or security risks if not managed properly, raising questions about the balance between flexibility and control in coding practices.

## AI Summary (from Notion)
Fly.io has launched Sprites.dev, a platform that provides stateful sandbox environments for developers and secure APIs for running untrusted code. It allows users to create persistent development environments with tools pre-installed, supports checkpointing for easy rollback, and offers a JSON API for managing sandboxes. The service features scale-to-zero billing, making it cost-effective for intermittent use. Sprites.dev addresses the need for safe coding agent environments while also facilitating the execution of untrusted code securely.

## Content (from Notion)

New from Fly.io today: Sprites.dev. Here’s their blog post and YouTube demo. It’s an interesting new product that’s quite difficult to explain—Fly call it “Stateful sandbox environments with checkpoint & restore” but I see it as hitting two of my current favorite problems: a safe development environment for running coding agents and an API for running untrusted code in a secure sandbox.

Disclosure: Fly sponsor some of my work. They did not ask me to write about Sprites and I didn’t get preview access prior to the launch. My enthusiasm here is genuine.

- Developer sandboxes
- Storage and checkpoints
- Really clever use of Claude Skills
- A sandbox API
- Scale-to-zero billing
- Two of my favorite problems at once
I predicted earlier this week that “we’re due a Challenger disaster with respect to coding agent security” due to the terrifying way most of us are using coding agents like Claude Code and Codex CLI. Running them in --dangerously-skip-permissions mode (aka YOLO mode, where the agent acts without constantly seeking approval first) unlocks so much more power, but also means that a mistake or a malicious prompt injection can cause all sorts of damage to your system and data.

The safe way to run YOLO mode is in a robust sandbox, where the worst thing that can happen is the sandbox gets messed up and you have to throw it away and get another one.

That’s the first problem Sprites solves:

```plain text
curl https://sprites.dev/install.sh | bash

sprite login
sprite create my-dev-environment
sprite console -s my-dev-environment
```

That’s all it takes to get SSH connected to a fresh environment, running in an ~8GB RAM, 8 CPU server. And... Claude Code and Codex and Gemini CLI and Python 3.13 and Node.js 22.20 and a bunch of other tools are already installed.

The first time you run claude it neatly signs you in to your existing account with Anthropic. The Sprites VM is persistent so future runs of sprite console -s will get you back to where you were before.

... and it automatically sets up port forwarding, so you can run a localhost server on your Sprite and access it from localhost:8080 on your machine.

There’s also a command you can run to assign a public URL to your Sprite, so anyone else can access it if they know the secret URL.

### Storage and checkpoints #

In the blog post Kurt Mackey argues that ephemeral, disposable sandboxes are not the best fit for coding agents:

> 

Each Sprite gets a proper filesystem which persists in between sessions, even while the Sprite itself shuts down after inactivity. It sounds like they’re doing some clever filesystem tricks here, I’m looking forward to learning more about those in the future.

There are some clues on the homepage:

> 

The really clever feature is checkpoints. You (or your coding agent) can trigger a checkpoint which takes around 300ms. This captures the entire disk state and can then be rolled back to later.

For more on how that works, run this in a Sprite:

```plain text
cat /.sprite/docs/agent-context.md

```

Here’s the relevant section:

```plain text
## Checkpoints
- Point-in-time checkpoints and restores available
- Copy-on-write implementation for storage efficiency
- Last 5 checkpoints mounted at `/.sprite/checkpoints`
- Checkpoints capture only the writable overlay, not the base image

```

Or run this to see the --help for the command used to manage them:

Which looks like this:

```plain text
sprite-env checkpoints - Manage environment checkpoints

USAGE:
    sprite-env checkpoints <subcommand> [options]

SUBCOMMANDS:
    list [--history <ver>]  List all checkpoints (optionally filter by history version)
    get <id>                Get checkpoint details (e.g., v0, v1, v2)
    create                  Create a new checkpoint (auto-versioned)
    restore <id>            Restore from a checkpoint (e.g., v1)

NOTE:
    Checkpoints are versioned as v0, v1, v2, etc.
    Restore returns immediately and triggers an async restore that restarts the environment.
    The last 5 checkpoints are mounted at /.sprite/checkpoints for direct file access.

EXAMPLES:
    sprite-env checkpoints list
    sprite-env checkpoints list --history v1.2.3
    sprite-env checkpoints get v2
    sprite-env checkpoints create
    sprite-env checkpoints restore v1

```

I’m a big fan of Skills, the mechanism whereby Claude Code (and increasingly other agents too) can be given additional capabilities by describing them in Markdown files in a specific directory structure.

In a smart piece of design, Sprites uses pre-installed skills to teach Claude how Sprites itself works. This means you can ask Claude on the machine how to do things like open up ports and it will talk you through the process.

There’s all sorts of interesting stuff in the /.sprite folder on that machine—digging in there is a great way to learn more about how Sprites works.

### A sandbox API #

Also from my predictions post earlier this week: “We’re finally going to solve sandboxing”. I am obsessed with this problem: I want to be able to run untrusted code safely, both on my personal devices and in the context of web services I’m building for other people to use.

I have so many things I want to build that depend on being able to take untrusted code—from users or from LLMs or from LLMs-driven-by-users—and run that code in a sandbox where I can be confident that the blast radius if something goes wrong is tightly contained.

Sprites offers a clean JSON API for doing exactly that, plus client libraries in Go and TypeScript and coming-soon Python and Elixir.

From their quick start:

```plain text
# Create a new sprite
curl -X PUT https://api.sprites.dev/v1/sprites/my-sprite \
-H "Authorization: Bearer $SPRITES_TOKEN"

# Execute a command
curl -X POST https://api.sprites.dev/v1/sprites/my-sprite/exec \
-H "Authorization: Bearer $SPRITES_TOKEN" \
-d '{"command": "echo hello"}'

```

You can also checkpoint and rollback via the API, so you can get your environment exactly how you like it, checkpoint it, run a bunch of untrusted code, then roll back to the clean checkpoint when you’re done.

Managing network access is an important part of maintaining a good sandbox. The Sprites API lets you configure network access policies using a DNS-based allow/deny list like this:

```plain text
curl -X POST \
  "https://api.sprites.dev/v1/sprites/{name}/policy/network" \
  -H "Authorization: Bearer $SPRITES_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "rules": [
      {
        "action": "allow",
        "domain": "github.com"
      },
      {
        "action": "allow",
        "domain": "*.npmjs.org"
      }
    ]
  }'
```

Sprites have scale-to-zero baked into the architecture. They go to sleep after 30 seconds of inactivity, wake up quickly when needed and bill you for just the CPU hours, RAM hours and GB-hours of storage you use while the Sprite is awake.

Fly estimate a 4 hour intensive coding session as costing around 46 cents, and a low traffic web app with 30 hours of wake time per month at ~$4.

(I calculate that a web app that consumes all 8 CPUs and all 8GBs of RAM 24/7 for a month would cost ((7 cents * 8 * 24 * 30) + (4.375 cents * 8 * 24 * 30)) / 100 = $655.2 per month, so don’t necessarily use these as your primary web hosting solution for an app that soaks up all available CPU and RAM!)

I was hopeful that Fly would enter the developer-friendly sandbox API market, especially given other entrants from companies like Cloudflare and Modal and E2B.

I did not expect that they’d tackle the developer sandbox problem at the same time, and with the same product!

My one concern here is that it makes the product itself a little harder to explain.

I’m already spinning up some prototypes of sandbox-adjacent things I’ve always wanted to build, and early signs are very promising. I’ll write more about these as they turn into useful projects.


