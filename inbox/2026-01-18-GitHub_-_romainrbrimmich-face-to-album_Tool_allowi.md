---
type: link
source: notion
url: https://github.com/romainrbr/immich-face-to-album
notion_type: Software Repo
tags: ['Running']
created: 2025-10-02T11:38:00.000Z
---

# GitHub - romainrbr/immich-face-to-album: Tool allowing to sync Immich's user face to a specific album

## Overview (from Notion)
- The tool allows seamless organization of family photos by syncing images of specific faces to designated albums, making it easier to relive memories with loved ones.
- With its user-friendly setup, you can automate the photo management process, freeing up time for family activities or personal projects.
- Consider potential privacy concerns when using photo recognition technology—balancing convenience with security is crucial.
- Engaging with the open-source community could spark ideas for enhancing family albums or even inspire a project that combines tech with family storytelling.
- The concept of continuous sync may resonate with the busy lifestyle in NYC, where capturing and organizing moments quickly can be a challenge.
- Explore how similar automation could be applied to other aspects of life, such as organizing kids' activities or managing family schedules.

## AI Summary (from Notion)
Tool for syncing photos of detected faces into existing Immich albums, similar to Google Photos. Installation via pip or pipx, with command options for API key, server URL, and face IDs. Supports continuous sync or scheduled updates using cron. Docker usage is also provided for running the tool in containers.

## Content (from Notion)

# Immich Face To Album

Sync all photos belonging to one or more detected faces into an existing Immich album (similar to Google Photos “live / auto-updating albums”).

## Quick Start

```plain text
pipx install immich-face-to-album     # or: pip install immich-face-to-album

immich-face-to-album \
  --key YOUR_API_KEY \
  --server https://your-immich.example \
  --face PERSON_ID \
  --album ALBUM_ID
```

Add more faces by repeating --face.

## Installation

pipx (recommended for CLI isolation):

```plain text
pipx install immich-face-to-album
```

Or with pip:

```plain text
pip install immich-face-to-album
```

## Getting the IDs

- Person (face) ID: open a person in the Immich “People / Faces” section; the last path segment in the URL is the ID.
- Album ID: open the target album; the last path segment is the ID.
- Server URL: include scheme and port (e.g. http://immich.local:2283 or https://photos.example.com).
- API Key: generate in Immich settings.
The album must already exist (the tool only adds assets; it does not create albums).

## Command Options (summary)

Basic multi-face example:

```plain text
immich-face-to-album --key k --server https://s --face p1 --face p2 --album a123
```

Exclude a face (e.g. gather p1 + p2, but remove any asset that also belongs to p3):

```plain text
immich-face-to-album --key k --server https://s \
  --face p1 --face p2 --skip-face p3 --album a123
```

## Continuous Sync vs Cron

Two ways to keep an album updated:

1.  
1.   
Choose:

- Use -run-every-seconds when you want immediate repeated scans without external tooling.
- Use cron when you prefer isolated short-lived runs.
Default behavior is a single pass (no loop).

## Docker Usage

Image: rbrucker/immich-face-to-album

Single run:

```plain text
docker run --rm rbrucker/immich-face-to-album \
  immich-face-to-album --key K --server https://s --face P --album A
```

Continuous sync (every 10 minutes):

```plain text
docker run --rm rbrucker/immich-face-to-album \
  immich-face-to-album --key K --server https://s --face P --album A \
    --run-every-seconds 600
```

Multiple faces:

```plain text
docker run --rm rbrucker/immich-face-to-album \
  immich-face-to-album --key K --server https://s --face P1 --face P2 --album A
```

With host cron (every 2 hours):

```plain text
0 */2 * * * docker run --rm rbrucker/immich-face-to-album immich-face-to-album --key K --server https://s --face P --album A

```

## Examples

Run once (quiet):

```plain text
immich-face-to-album --key k --server https://s --face p --album a
```

Run every 5 minutes:

```plain text
immich-face-to-album --key k --server https://s --face p --album a --run-every-seconds 300
```

Run every 2 hours (loop):

```plain text
immich-face-to-album --key k --server https://s --face p --album a --run-every-seconds 7200
```

Test loop (every minute + debug):

```plain text
immich-face-to-album --key k --server https://s --face p --album a --run-every-seconds 60 --verbose
```

## Verbose Mode

Add --verbose to inspect bucket queries, asset retrieval, exclusions, and album add operations. Useful for:

- Verifying connectivity
- Seeing exact API responses
- Diagnosing missing or excluded assets
## Contributing

Issues and PRs welcome !


