# Personal Productivity & Time Tracking Tools

Apps and tools for understanding where time goes, tracking habits, and measuring productivity.

## Screencap (yahorbarkouski)

*Source: https://github.com/yahorbarkouski/screencap - Added: 2026-01-18*

A macOS desktop app that captures screenshots and app activity to create a timeline of your day. Answers questions like "What did I actually do today?" and "Am I spending too much time on Chess?"

### Core Features

- **Timeline View** - Day visualized as a stream of events; captures with same context merge into time windows
- **Rich Context Extraction** - App name, window title, browser URL, media playing, VS Code workspace, etc.
- **Journal & Day Wrapped** - Daily metrics (active time, focus %, longest streak, top apps/sites)
- **End of Day Flow** - Guided ritual: summary, progress review, addictions review, reflection writing

### Unique Features

- **Addiction Tracking** - Define behaviors to monitor (games, distracting sites), AI surfaces candidates, calendar view shows patterns across weeks, streak tracking for clean days
- **Project Progress** - Automatic milestone detection, manual capture with `Cmd+Shift+P`, git commit integration
- **Social Feed (E2E Encrypted)** - Share day wrapped/milestones with friends, real-time activity feed

### How Capture Works

1. Sample context every second (which app/window/URL in focus)
2. Wait for stability (~10 seconds of same context)
3. Take multi-display screenshot
4. Keep the most representative capture at end of interval
5. Merge similar events (same context + similar pixels = one event)

Result: Quick app switches don't produce captures, one clean event per sustained activity.

### LLM Classification Pipeline

Events go through multi-step classification:

1. Cache reuse (instant match by fingerprint + context)
2. Local retrieval (match against own history)
3. Local LLM (Ollama, LM Studio, any OpenAI-compatible)
4. Cloud text (OpenRouter with context + OCR, no images)
5. Cloud vision (OpenRouter with screenshots, if enabled)
6. Fallback (baseline from context alone)

**Classification output:** Category, Project, Caption, Addiction candidate, Progress detection

### Privacy

- **Local-first** - SQLite database + screenshots in `~/Library/Application Support/Screencap/`
- **Keys in Keychain** - Encryption keys stored securely
- **E2EE for Social** - Ed25519 signing + X25519 key agreement, AES-256-GCM encryption

### Why It's Interesting

- **Time Management** - Track daily productivity, understand where time actually goes
- **Habit Breaking** - Monitor screen time, gaming, or other behaviors you want to reduce
- **Work-Life Balance** - Visual evidence of how time is spent can inform family/work decisions
- **Project Documentation** - Automatic progress capture creates a visual history of work
- **Local-first Privacy** - All data stays on your machine unless you opt into social features

### Considerations

- **macOS only** (uses AppleScript, macOS Vision, Apple-specific APIs)
- **AI costs can spike** - Up to 2 LLM calls per screenshot, no rate limiting or cost caps
- **Retention is time-based only** - Important events purged alongside noise past retention window
- **Many hardcoded thresholds** - Fingerprint similarity, stability window (10s), merge gap, HQ image retention (12h)

### Installation

1. Download DMG from GitHub Releases
2. Drag to Applications
3. Grant permissions: Screen Recording (required), Accessibility (recommended), Automation (recommended)
4. Configure AI (Cloud/Local/Disabled) and capture interval in Settings

### Links

- Repository: https://github.com/yahorbarkouski/screencap
- License: Not specified (check repo)
- Requirements: macOS 13+ (Ventura or later)
