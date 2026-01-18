---
type: link
source: notion
url: https://granda.org/en/2026/01/02/claude-code-on-the-go/
notion_type: Software Repo
tags: ['Running']
created: 2026-01-05T00:45:00.000Z
---

# Claude Code On-The-Go - granda

## Overview (from Notion)
- Embrace the flexibility of mobile development—code from anywhere, whether it's a park in NYC or your living room.
- Efficiently manage time between family and work; tackle small tasks while waiting for your child’s activity to finish.
- Leverage tools like Tailscale and Termius to maintain a secure, private development environment, prioritizing both family time and security.
- Consider the cost-effectiveness of cloud solutions; only pay for what you use, making it easier to budget amidst family expenses.
- Explore the potential of async development; this model allows you to engage with your kids while still progressing on projects.
- Think about how this setup can encourage a better work-life balance, allowing for spontaneous moments with family without sacrificing productivity.
- View mobile development as a way to challenge traditional notions of being "tied" to a desk—embrace a more dynamic work style.
- Reflect on how this tech-savvy approach might inspire your children; show them the possibilities of technology in everyday life.

## AI Summary (from Notion)
The setup allows running six Claude Code agents in parallel on a phone using Termius and a Vultr VM. Key components include Tailscale for secure access, mosh for network resilience, and tmux for session persistence. Push notifications enable mobile development by alerting users when input is needed, allowing for asynchronous work from anywhere. The system is cost-effective, charging only for active use, and isolates development from production systems to enhance security.

## Content (from Notion)

I run six Claude Code agents in parallel from my phone. No laptop, no desktop—just Termius on iOS and a cloud VM.

## The Setup

```plain text
#mermaid-1767454337108{font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:16px;fill:#333;}#mermaid-1767454337108 .error-icon{fill:#552222;}#mermaid-1767454337108 .error-text{fill:#552222;stroke:#552222;}#mermaid-1767454337108 .edge-thickness-normal{stroke-width:2px;}#mermaid-1767454337108 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-1767454337108 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-1767454337108 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-1767454337108 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-1767454337108 .marker{fill:#333333;stroke:#333333;}#mermaid-1767454337108 .marker.cross{stroke:#333333;}#mermaid-1767454337108 svg{font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:16px;}#mermaid-1767454337108 .label{font-family:"trebuchet ms",verdana,arial,sans-serif;color:#333;}#mermaid-1767454337108 .cluster-label text{fill:#333;}#mermaid-1767454337108 .cluster-label span,#mermaid-1767454337108 p{color:#333;}#mermaid-1767454337108 .label text,#mermaid-1767454337108 span,#mermaid-1767454337108 p{fill:#333;color:#333;}#mermaid-1767454337108 .node rect,#mermaid-1767454337108 .node circle,#mermaid-1767454337108 .node ellipse,#mermaid-1767454337108 .node polygon,#mermaid-1767454337108 .node path{fill:#ECECFF;stroke:#9370DB;stroke-width:1px;}#mermaid-1767454337108 .flowchart-label text{text-anchor:middle;}#mermaid-1767454337108 .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-1767454337108 .node .label{text-align:center;}#mermaid-1767454337108 .node.clickable{cursor:pointer;}#mermaid-1767454337108 .arrowheadPath{fill:#333333;}#mermaid-1767454337108 .edgePath .path{stroke:#333333;stroke-width:2.0px;}#mermaid-1767454337108 .flowchart-link{stroke:#333333;fill:none;}#mermaid-1767454337108 .edgeLabel{background-color:#e8e8e8;text-align:center;}#mermaid-1767454337108 .edgeLabel rect{opacity:0.5;background-color:#e8e8e8;fill:#e8e8e8;}#mermaid-1767454337108 .labelBkg{background-color:rgba(232, 232, 232, 0.5);}#mermaid-1767454337108 .cluster rect{fill:#ffffde;stroke:#aaaa33;stroke-width:1px;}#mermaid-1767454337108 .cluster text{fill:#333;}#mermaid-1767454337108 .cluster span,#mermaid-1767454337108 p{color:#333;}#mermaid-1767454337108 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:12px;background:hsl(80, 100%, 96.2745098039%);border:1px solid #aaaa33;border-radius:2px;pointer-events:none;z-index:100;}#mermaid-1767454337108 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#333;}#mermaid-1767454337108 :root{--mermaid-font-family:"trebuchet ms",verdana,arial,sans-serif;}Termius + moshPreToolUse hookPush notificationPhoneTailscale VPNVultr VMClaude CodePoke webhook
```

The loop is: kick off a task, pocket the phone, get notified when Claude needs input. Async development from anywhere.

## Infrastructure

A Vultr VM in Silicon Valley:

I pay only when working. Two scripts handle lifecycle:

```plain text
vm-start   # Start VM, wait for Tailscale, connect via mosh
vm-stop    # Halt VM

```

I also have an iOS Shortcut that calls the Vultr API directly—start the VM from my phone before I even open Termius.

The VM’s public IP has no SSH listener. All access goes through Tailscale’s private network. Defense in depth: cloud firewall blocks everything except Tailscale coordination, local nftables as backup, fail2ban for good measure.

## Mobile Terminal

Termius handles SSH and mosh on iOS/Android. Mosh is the key—it survives network transitions. Switch from WiFi to cellular, walk through a dead zone, put the phone to sleep. The connection persists.

```plain text
mosh --ssh="ssh -p 47892" mgranda@100.107.156.125

```

One gotcha: mosh doesn’t forward SSH agent. For git operations that need GitHub auth, I use regular SSH inside tmux.

## Session Persistence

The shell auto-attaches to tmux on login. Close Termius, reopen hours later, everything’s still there.

```plain text
# In .zshrc
if [[ -z "$TMUX" ]]; then
    tmux attach -t main 2>/dev/null || tmux new -s main
fi

```

Multiple Claude agents run in parallel windows. C-a c for new window, C-a n to cycle. Works well on a phone keyboard.

## Push Notifications

This is what makes mobile development practical. Without notifications, you’d constantly check the terminal. With them, you can walk away.

The hook in ~/.claude/settings.json:

```plain text
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "AskUserQuestion",
      "hooks": [{
        "type": "command",
        "command": "~/.claude/hooks/poke-notify.sh question"
      }]
    }]
  }
}

```

When Claude calls AskUserQuestion, the hook fires. A simple script extracts the question and POSTs to Poke’s webhook:

Phone buzzes. Notification shows the question. Tap, respond, continue.

## Trust Model

I run Claude Code in permissive mode. The VM is isolated—no access to production systems, no secrets beyond what’s needed for development. Worst case: Claude does something unexpected on a disposable VM.

Cost control adds another layer. The VM costs $0.29/hr. Even if something runs away, the daily cap is bounded.

## Parallel Development

Git worktrees let me run multiple features simultaneously:

```plain text
~/Code/myproject/              # main
~/Code/myproject-sidebar/      # feature branch
~/Code/myproject-dark-mode/    # another feature

```

Each worktree gets its own tmux window with a Claude agent. Port allocation is hash-based—deterministic from branch name, no conflicts:

Six agents, six features, one phone.

## What This Enables

Review PRs while waiting for coffee. Kick off a refactor on the train. Fix a bug from the couch while watching TV.

The pattern: start a task that will take Claude 10-20 minutes, do something else, get notified, respond, repeat. Development fits into the gaps of the day instead of requiring dedicated desk time.

## The Components

The setup took one Claude Code session to build—gave it my Vultr API key and access to gh, asked for a secure dev VM. Now I code from my phone.


