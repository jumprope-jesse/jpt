---
type: link
source: notion
url: https://github.com/yahorbarkouski/screencap
notion_type: Software Repo
tags: ['Running']
created: 2026-01-11T06:09:00.000Z
---

# GitHub - yahorbarkouski/screencap: To remember what happened yesterday, share progress and break addictions

## Overview (from Notion)
- Time Management: This app can help track daily productivity, offering insights into how time is spent, which is crucial when balancing family and work.
- Addiction Tracking: It allows monitoring of habits, such as screen time or gaming, helping to maintain a healthy work-life balance—important for family time.
- Project Milestones: Good for visualizing project progress, which can aid in managing a startup’s workflow and keeping the team aligned.
- Social Features: Connecting with peers can foster accountability and collaboration, which is essential in a competitive NYC tech landscape.
- Customization: The open-source nature means you can adapt it to fit your specific needs—ideal for a founder who values flexibility.
- Local-first Privacy: Given the importance of data privacy, this app’s focus on local storage can be appealing, especially for family data.
- End-of-Day Ritual: Incorporating a structured review can help reflect on daily accomplishments and set goals for family and work, promoting mental well-being.
- Potential Drawbacks: Consider the dependency on tech for tracking—an alternative viewpoint could stress the importance of unplugging and spending quality time without digital distractions.

## AI Summary (from Notion)
A macOS app that captures screenshots and app activity to create a timeline, track project progress, and monitor addictions. It features customizable event categorization, daily summaries, and an encrypted social feed for sharing milestones with friends. Users can automate captures, analyze productivity metrics, and utilize AI for classification while ensuring privacy through end-to-end encryption.

## Content (from Notion)

# Screencap

To understand where your day went

A macOS desktop app that captures screenshots, windows and apps (both background and foreground) on a schedule and transforms them into a timeline, daily summaries, project milestones, addiction tracking, with optional E2E-encrypted social feed. Screencap answers the questions like:

- What did I actually do today?
- How long did I really work?
- Am I spending too much time on Chess?
- What progress did I make on my project?
- What my colleagues are doing?
- What actual progress on project X has been made since September?
The idea behind this opensource is to inspire as many forks as possible. The project (both app and social backend) are fully free to use, enrouranging everyone to customise and build their own Screencaps. Project started as a background project tracker, as we all tend to have zero-to-little screenshots from projects we worked on for months. Then addiction tracker came it, the Spotify background played, End Of Day flow, activity popup, and social E2E network in tray (I couldn't help myself)

Download · Changelog · Security · E2EE & Sharing · Local LLM

## Features Summary

### Timeline

Time period (day), visualized as a stream of events

- Each card is an event — multiple captures with the same context and similar pixels merge into one time window
- Rich context extraction — app name, window title, browser URL, media playing, and per-app lower contexts like VS Code workspace
- Fully editable — relabel events, dismiss captures, copy screenshots, create per-app or per-website automation rules, mark as progress or addiction (by default done automatically via llms)
### Day Wrapped

The tray widget "what happened today?" with quick actions and different views available.

Quick actions:

- Capture now — trigger an immediate capture
- Capture project progress — save a milestone with a caption (screenshots active window and waits for a comment. would want to double-down and add loom-like view support one day)
### Journal

To turn your day into a narrative

- Dayline visualization — see your entire day at a glance with category colors
- Breakdown metrics — active time, focus percentage, longest streak, top apps/sites/projects
- End of Day — optional LLM-powered daily recap (or the one from End of Day flow below)
- Manual journaling — write reflections, embed event screenshots, create custom sections
### End of Day Flow

A guided ritual to close your day intentionally, guides you through:

1. Summary — metrics and dayline visualization
1. Progress Review — confirm or promote potential milestones
1. Addictions Review — acknowledge or dismiss flagged events
1. Write — compose custom sections with embedded event screenshots
Summary

---

---

active time, focus, progress milestones, addiction episodes.

---

Write

---

---

to compose with embedded screenshots and custom sections.

---

### Addictions

Define behaviors you want to track, then measure. Bullet chess in my case:) But is thought for games and porn too, so tricky events are well-covered.

- Create rules — define what counts as an addiction
- AI detection — the LLM surfaces candidates based on content (either image OCR or image itself + Accessibility context)
- Calendar view — see patterns across weeks
- Streak tracking — visualize consecutive clean days
- Episode timeline — drill into specific incidents with screenshots
### Project Progress

A dedicated timeline for milestones and momentum, the foundation for multiplayer collaboration

- Automatic detection — AI identifies progress-worthy captures
- Manual milestones — ⌘⇧P to capture and caption a moment
- Git integration — link local repositories to see commits alongside work sessions
- Multi-project filtering — track progress across all projects or focus on one
Sharing: Projects can be shared with friends via encrypted rooms. Invite collaborators by username, and everyone sees each other's milestones in a unified timeline. All shared content is end-to-end encrypted; the server never sees your screenshots or captions, but just in case you can selfhost and set your own backend, for a better guide see screencap-website project

### Social & Friends

So you can feel-not-ask each other:)

The flow is simple:

- Choose a username
- Add friends
- Share Day Wrapped — let friends see your dayline in real-time
- Shared projects — invite friends to project rooms, see their milestones
- Comments — react to shared events with threaded messages
- Activity feed — see what friends are working on
### Context Providers

Screencap extracts rich context from your active window:

With accessibility + automation permissions, we can get pretty much precise context

### LLM Classification

When enabled, events go through a multi-step classification pipeline:

1. Cache reuse — instant match by fingerprint + context
1. Local retrieval — match against your own history
1. Local LLM — Ollama, LM Studio, or any OpenAI-compatible server
1. Cloud text — OpenRouter with context + OCR (no images)
1. Cloud vision — OpenRouter with screenshots (if enabled)
1. Fallback — baseline classification from context alone
Classification output:

- Category — Work, Study, Leisure, Social, Chores, Unknown
- Project — detected project name
- Caption — human-readable description
- Addiction candidate — potential matches against your rules
- Progress detection — milestone-worthy content
### Automation Rules

Fine-grained control over capture and classification:

Create rules from any event card or in Settings->Automation.

## Privacy & Security

Local-first overall, but for LLM classification both local and remote (openrouter/openai) options are available.

### What stays local

- SQLite database under ~/Library/Application Support/Screencap/
- All screenshots (thumbnails + originals)
- Settings and encryption keys (Keychain-encrypted)
### What can go to the network (opt-in)

### End-to-End Encryption

All shared content (screenshots, captions, chat) is encrypted on your device before upload.

- Device identity — Ed25519 signing key + X25519 key agreement key
- Room keys — 32-byte secrets, per-recipient-device encrypted envelopes
- Event encryption — AES-256-GCM with keys derived via HKDF
- Chat encryption — DMs use X25519 shared secret; rooms use room key
The server sees ciphertext, metadata (timestamps, usernames, project names), and encrypted blobs. It cannot read content.

See Security & Privacy: Sharing and E2EE Crypto Spec.

## Install

### Requirements

- macOS 13+ (Ventura or later)
- Screen Recording permission (required)
- Accessibility permission (recommended)
- Automation permissions (recommended)
### Download

1. Grab the latest DMG from Releases
1. Open the DMG and drag Screencap.app to Applications
1. Launch — the onboarding wizard guides you through permissions and setup
### Permissions

## First Run

The onboarding wizard walks you through:

1. Screen Recording — grant the core permission
1. Accessibility — enable rich window context
1. Automation — allow per-app context extraction
1. AI Setup — choose Cloud, Local, or Disabled
1. First Capture — see what Screencap captures
After onboarding:

- Capture interval is set in Settings -> Capture
- Retention period is set in Settings -> Data
- Global shortcuts are customizable in Settings -> Capture -> Shortcuts
## Shortcuts

All shortcuts are configurable in Settings -> Capture -> Shortcuts.

## How Capture Works

Screencap uses dominant activity scheduling:

1. Sample context every second — which app, window, URL is in focus
1. Wait for stability — context must be stable for ~10 seconds
1. Capture candidate — take a multi-display screenshot
1. Keep the dominant — at the end of the interval, save the most representative capture
1. Merge similar events — captures with same context + similar pixels become one event
This means:

- Quick app switches don't produce captures
- You get one clean event per sustained activity
- Storage usage stays reasonable
The overall capturing algo is still in very rough and can be very much improved

## LLM Configuration

### Cloud LLM (OpenRouter / OpenAI)

Screencap uses OpenRouter by default, but any OpenAI-compatible API works

1. Get an API key from openrouter.ai/keys or platform.openai.com
1. Settings -> AI -> Cloud LLM -> paste your key
1. Choose a model (default: openai/gpt-5-mini)
1. Toggle Allow vision uploads if you want image-based classification
OpenRouter gives you access to many models (Claude, GPT-5, Gemini, open-source) through one API key, so very much recommended

### Local LLM (Ollama / LM Studio)

1. Run a local OpenAI-compatible server
1. Settings -> AI -> Local LLM -> enable and configure:
- Base URL: http://localhost:11434/v1 (Ollama) or http://localhost:1234/v1 (LM Studio)
- Model: the model name from /v1/models
1. Click Test to verify
See Local LLM Guide for detailed setup.

### Disable AI

Settings -> AI -> Classification -> Off

Captures still happen, but no LLM calls. Events get basic category from context only.

## Social Setup

### Create Your Identity

1. Open the tray popup -> Social tab
1. Choose a username (alphanumeric, unique)
1. Your device generates E2EE keys automatically
### Add Friends

1. Click + in the Social tab
1. Enter their username
1. They accept your request
### Share Day Wrapped

Settings -> Social -> Day Wrapped Sharing -> Enable

Friends see your dayline in their feed. You control what's shared:

- Categories (always)
- App names (optional)
- Addiction flags (optional)
### Share Projects

1. Open Projects -> select a project -> Share
1. Invite friends by username
1. They accept the room invite and see your milestones
## Self-Hosting

Screencap's backend is open source. Run your own:

1. Settings -> System -> Custom Backend -> Enable
1. Enter your backend URL
1. See Self-Hosted Backend Guide
Your data, your server, full control.

## Development

### Requirements

- macOS
- Node.js 20+
- npm
### Setup

```plain text
git clone https://github.com/yahorbarkouski/screencap.git
cd screencap
npm install
```

### Run

```plain text
npm run dev
```

### Test

```plain text
npm test
```

### Build

```plain text
npm run build
npm run preview
```

### Package

```plain text
npx electron-builder --config electron-builder.yml
```

## Architecture

```plain text
screencap/
├── electron/
│   ├── main/           # Main process
│   │   ├── app/        # Window, tray, popup, lifecycle
│   │   ├── features/   # Capture, AI, context, social, sync
│   │   ├── infra/      # Settings, logging, storage
│   │   └── ipc/        # Secure IPC handlers
│   ├── preload/        # Context bridge (window.api)
│   └── shared/         # IPC channels, shared types
├── src/                # React renderer
│   ├── components/     # UI components
│   ├── hooks/          # React hooks
│   ├── lib/            # Utilities
│   └── stores/         # Zustand stores
└── docs/               # Documentation

```

### Key Services

## Contributing

Read Security Practices before adding new IPC handlers or file access surfaces.

Key principles:

- Treat IPC as a security boundary
- Validate all renderer inputs with Zod
- Use the secureHandle wrapper for new handlers
- Prefer allowlists over blocklists
## Known Limitations and Pitfalls

> 

### AI Usage Can Spike Unexpectedly

The classification pipeline can make up to 2 LLM calls per screenshot (one for general classification, another for addiction verification). There's no rate limiting or cost tracking - if you capture frequently, your API bill can grow fast. Small models work best tho, but be thoughtful about this for a while

What's needed: smarter classification logic, caching improvements, and optional cost caps.

### Event Trimming is Time-Based Only

Retention cleanup deletes old data based on time thresholds, not activity relevance. Important events get purged alongside noise if they're past the retention window.

What's needed: activity-aware or user-marked retention. Really curious one.

### Hardcoded Thresholds

Many parameters are fixed /theoretically/:

- Fingerprint similarity thresholds
- Capture stability window (10s)
- Merge gap for events (~2× capture interval)
- HQ image retention (12 hours)
These may not fit all workflows and require some good practice to make sense / become dynamic

### macOS Only

The entire context system uses AppleScript, macOS Vision, and Apple-specific APIs

If any of these bother you, PRs are very welcome

## License

MIT


