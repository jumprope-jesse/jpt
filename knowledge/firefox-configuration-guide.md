# Firefox Configuration Guide

**Source:** https://kau.sh/blog/how-to-firefox/
**Category:** Browser Configuration / Privacy Tools

## Why Firefox

- 100% open-source (can fork, inspect, contribute)
- Best platform for uBlock Origin (full version, not "Lite")
- Real browser extensions on Android (including uBlock Origin)
- Seamless sync between desktop and mobile
- Highly customizable via `about:config`

## Essential: uBlock Origin Setup

uBO is a wide-spectrum content blocker. After Chrome's Manifest V3, the full version only works properly on Firefox.

### Recommended Filter Lists

Follow uBO wizard recommendations on Reddit for filter list configuration. The key is enabling community-maintained lists that block:
- Ads
- Trackers
- Cookie notices
- Digital sludge

### Advanced uBO Rules

Block all Facebook tracking from non-Facebook sites:
- Custom rule to sever Meta connections entirely

Block "Sign in with Google?" popups:
- Single custom rule handles this

## Privacy: Containers

Firefox includes **Total Cookie Protection** by default - isolates cookies per-site automatically.

### Multi-Account Container Setup

Use containers to stay logged into multiple accounts (e.g., Work Gmail + Personal Gmail) in the same browser window.

**Setup without MAC add-on:**
1. Go to `about:config`
2. Set `privacy.userContext.newTabContainerOnLeftClick.enabled` to `true`
3. Click new tab button to choose container

**For automatic link routing:**
- Install **Containerise** add-on
- Create rules to force specific sites into designated containers
- Example: Datadog/Sentry links always open in Work container

## Recommended Add-ons

### Essential
- **uBlock Origin**: Ad/tracker blocking (not the Lite version)

### Privacy/Containers
- **Containerise**: Auto-route links to correct containers

### Quality of Life
- **Dark Reader**: Consistent dark mode on all sites
- **Stylus**: Apply custom CSS (e.g., force monospace font on code blocks)
- **Return YouTube Dislike**: Restores dislike counts
- **Obsidian Web Clipper**: Save to Obsidian from desktop or mobile
- **Auto Tab Discard**: Suspends background tabs to save RAM

## about:config Tweaks

| Setting | Value | Effect |
|---------|-------|--------|
| `privacy.userContext.newTabContainerOnLeftClick.enabled` | `true` | Choose container on new tab click |
| `browser.tabs.insertAfterCurrent` | `true` | New tabs open next to current tab |

## Hidden Features

- `/` then type: Quick find (vs Cmd+F)
- `'` then type: Match only hyperlink text
- Hold `Shift` + right-click: Bypass disabled right-click on sites
- URL bar shortcuts:
  - `*` for bookmarks
  - `%` for open tabs
  - `^` for history

## Android Sync

Firefox for Android provides:
- Tab sync with desktop
- Bookmark sync
- Password sync
- Full browser extensions (including uBlock Origin)

## Related

- **Deta Surf**: AI-powered research browser (see `/knowledge/deta-surf-ai-browser.md`)
- **Arc Browser**: Innovative browser with vertical tabs
