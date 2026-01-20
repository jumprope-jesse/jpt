# Self-Hosting Guide

*Source: [2026 is the year of self-hosting](https://fulghum.io/self-hosting) by Fulghum - Added: 2026-01-18*

## Why 2026 is Different

Three things converged to make self-hosting accessible to non-sysadmins:

1. **Affordable mini PCs** - Beelink Mini N150 (~$200) + 8TB NVMe SSD runs 13 services on 4GB RAM, minimal CPU
2. **Tailscale** - Secure networking without complex VPN setup
3. **CLI agents (Claude Code)** - The real unlock. Instead of stitching together blog posts from 2021, just describe what you want

**Key insight:** CLI agents make self-hosting dramatically easier and actually fun. First time it's recommendable to software-literate people who never wanted to become sysadmins.

## The Basic Flow

1. Install Linux on mini PC
2. Install Tailscale for secure remote access
3. Install Claude Code directly on the Linux box
4. Ask Claude Code to set things up:
   - Set up Docker
   - Create Docker Compose files
   - Install services
   - Put services behind Caddy (reverse proxy)
   - Persist data properly
   - Keep Docker images updated
   - Set up security packages
   - Configure restart on boot

No copy-pasting YAML from the internet. No deep Googling. Just ask.

## Recommended Services

### Core Services

| Service | Purpose | Notes |
|---------|---------|-------|
| **Vaultwarden** | Password management | Bitwarden-compatible, works with native apps/extensions, can be iOS default password manager |
| **Immich** | Google Photos replacement | Face recognition (local ML), timeline/map view, auto mobile uploads. "Not a compromise - better." See detailed setup notes below. |
| **Plex** | Media server | Stream your media anywhere |
| **ReadDeck** | Read-it-later (Pocket replacement) | Clean UI, remembers reading position, mobile shortcuts to save articles |
| **Karakeep** | Bookmarking / read-it-later | Formerly "Hoarder" (rebranded May 2025 due to trademark). AI-powered bookmark manager with auto-tagging. karakeep.app |
| **Grist** | Relational spreadsheet | Spreadsheet + database hybrid. Python formulas, SQLite-based portable format, access control, REST API. Open source (Apache 2.0). [gristlabs/grist-core](https://github.com/gristlabs/grist-core) |
| **Teable** | Postgres-Airtable fusion | No-code database with spreadsheet UI, Postgres backend. Handles millions of rows, real-time collaboration, full SQL access for BI tools. Multiple views (Grid, Form, Kanban coming). AGPL-3.0. [teableio/teable](https://github.com/teableio/teable) |

### Utilities

| Tool | Purpose |
|------|---------|
| **Lazydocker** | Terminal UI for Docker - see containers, logs, stats, restart/shell into anything |
| **Glances** | Full system view - CPU, memory, disk, network, all containers |
| **Uptime Kuma** | Monitoring with email alerts when services go down/up |
| **OneUptime** | Full observability platform - uptime monitoring, status pages, incident management, on-call scheduling. PagerDuty/Datadog alternative. Heavier (16GB RAM recommended, 8GB minimum). [GitHub](https://github.com/OneUptime/oneuptime) |
| **Kener** | Modern open source status page - public-facing status pages for your services. Lightweight, static site generation with real-time monitors. [kener.ing](https://kener.ing) |
| **Caddy** | Reverse proxy with automatic HTTPS |
| **ntfy** | Push notifications via PUT/POST - self-hostable, open source |

## Hardware Specs (Reference)

- **Device**: Beelink Mini N150 (~$200)
- **Storage**: 8TB NVMe SSD (few hundred USD)
- **Usage**: 13 containers, 6% CPU, 32% memory (~4GB)
- **Characteristics**: Small, quiet, low power consumption

## Who This Is For

- Comfortable in a terminal
- Already paying for SaaS tools
- Like understanding how things work
- Don't want to become infra experts

## The Feeling

> "The feeling of ownership is powerful... I am spending time using software, learning, and having fun - instead of maintaining it and stressing out about it."

When something breaks: SSH in, ask the agent what's wrong, fix it.
When adding something new: describe it in plain English.

---

## Readeck - Read-It-Later Service

*Source: [readeck.org](https://readeck.org/en/) - Added: 2026-01-18*

### What It Does

Self-hosted read-it-later service (Pocket/Instapaper alternative). Save articles, videos, and web content for offline reading with highlights and annotations.

### Key Features

- **Bookmarks**: Save articles, photos, videos for later access
- **Labels & Collections**: Organize content with tags, favorites, and dynamic collections
- **Highlights**: Mark key passages in text content, browse highlights across all saved items
- **Video Transcripts**: Save video links and Readeck retrieves transcripts when available - read, highlight, and search transcripts as if they were articles
- **E-Book Export**: Export articles or entire collections as ebooks for e-readers; provides standard OPDS catalog for supported devices
- **Reading Customization**: Adjustable font, text size, line height; remembers preferences
- **Browser Extension**: Save while browsing, including content from sites requiring authentication that Readeck can't access directly
- **Search**: Full-text search across all saved content

### Installation

Latest release: [Readeck 0.18](https://readeck.org/en/blog/)

```bash
# Docker (recommended)
docker run -d \
  --name readeck \
  -p 8000:8000 \
  -v /path/to/data:/data \
  codeberg.org/readeck/readeck:latest
```

### Why Use Over Pocket

- **Self-hosted**: Your reading history stays private
- **No account required**: No sign-up, no tracking
- **Video transcripts**: Unique feature for video bookmarks
- **E-book export**: Take collections offline
- **Clean reading experience**: Focused on readability, not social features

### Integration with Stack

Pairs well with:
- **Karakeep**: AI-powered bookmarking with auto-tagging (different use case - more for quick saves with AI organization)
- **Audiobookshelf**: Podcasts and audiobooks
- **Calibre**: E-books

### Family Use Case

- Save educational articles for kids to read later
- Build collections on topics (science, history) for family learning
- Export to e-reader for screen-free reading time
- Archive meaningful content for future reference ("digital legacy")

---

## Grist - Relational Spreadsheet

*Source: [gristlabs/grist-core](https://github.com/gristlabs/grist-core) - Added: 2026-01-18*

### What It Does

Modern relational spreadsheet that combines spreadsheet flexibility with database robustness. Open source alternative to Airtable.

### Key Features

- **Hybrid model**: Columns work like database columns (named, typed), formulas update automatically like spreadsheets
- **Python formulas**: Full Python support for complex calculations, plus many Excel functions
- **Portable format**: Self-contained SQLite-based files - your data stays yours
- **Access control**: Granular permissions and user management
- **REST API**: Full API access plus Zapier integration
- **Drag-and-drop dashboards**: Build visualizations and linked views
- **Multi-language**: Translated to many languages

### Deployment Options

1. **grist-core** (this): Self-hosted server for full functionality
2. **grist-electron**: Desktop app for local files (Linux/macOS/Windows)
3. **grist-static**: Browser-only build for displaying spreadsheets on websites

### Quick Start

```bash
# Basic run
docker run -p 8484:8484 -it gristlabs/grist

# With persistence
docker run -p 8484:8484 -v $PWD/persist:/persist -it gristlabs/grist

# With gVisor sandboxing (recommended for untrusted docs)
docker run -p 8484:8484 -v $PWD/persist:/persist --env GRIST_SANDBOX_FLAVOR=gvisor -it gristlabs/grist
```

Visit http://localhost:8484 after starting.

### Authentication

Default: Anonymous mode with sign-in attributing work to a default email. For production:
- Set `GRIST_DEFAULT_EMAIL` for single-user
- Connect SAML, forward auth, or SSO (tested with Authentik, Auth0, Google/Microsoft via Dex) for multi-user

### Use Cases

- Inventory management
- Project tracking
- CRM / contact management
- Research data collection
- Anything you'd use Airtable or Notion databases for

### Why Self-Host

- **Data portability**: SQLite format, easy export
- **Independence**: Not dependent on Grist Labs business
- **Extensibility**: Build custom widgets, integrate via API
- **Price**: Free for self-hosted, no per-seat fees

---

## Immich Setup Notes

*Source: [Self-hosting my photos with Immich](https://michael.stapelberg.ch/posts/2025-11-29-self-hosting-photos-with-immich/) by Michael Stapelberg - Added: 2026-01-18*

### Hardware Requirements
- Example: Ryzen 7 Mini PC (ASRock DeskMini X600), <10W idle, 64GB RAM, 1TB disk
- For initial import, allocate more CPU/RAM temporarily; 4 cores + 4GB sufficient for normal use
- Can run in a Proxmox VM

### NixOS Installation
```nix
services.immich = {
  enable = true;
};
```
- Default location: `/var/lib/immich`
- NixOS enables firewall by default; use Tailscale for access instead of opening ports

### Tailscale Integration
```bash
# Forward traffic to Immich via Tailscale
tailscale serve --bg http://localhost:2283
```
With MagicDNS + TLS cert provisioning: access via `https://photos.example.ts.net`

### Initial Photo Import

**Don't use `immich-cli`** for Google Takeout imports - it times out during background job processing and doesn't handle metadata JSON files.

**Use `immich-go` instead:**
```bash
immich-go \
  upload \
  from-google-photos \
  --server=https://photos.example.ts.net \
  --api-key=secret \
  ~/Downloads/takeout-*.zip
```
- Pauses background tasks during upload, restarts after
- Properly handles Google Takeout metadata JSON files

### iPhone App Setup
1. Install Immich app
2. Login via Tailscale URL
3. Enable automatic backup (top right icon)
4. **Disable notifications**: Settings → Apps → Immich → Notifications (not needed for background upload)
5. Live Photos go to "Live Photos" album; "Recent" covers other files

### Backup Strategy
Backup entire `/var/lib/immich`:
- `backups/` - SQL dumps
- `upload/`, `library/`, `profile/` - user data

Set up systemd timer with rsync to PC enrolled in 3-2-1 backup scheme.

### Limitations
- No built-in photo editing (rotate/crop) - use GIMP
- For sharing, may still need Google Photos depending on recipients

### Face-to-Album Auto Sync

*Source: [immich-face-to-album](https://github.com/romainrbr/immich-face-to-album) - Added: 2026-01-18*

Automatically sync photos of detected faces into Immich albums (similar to Google Photos "live albums").

**Installation:**
```bash
pipx install immich-face-to-album
```

**Basic usage:**
```bash
immich-face-to-album \
  --key YOUR_API_KEY \
  --server https://your-immich.example \
  --face PERSON_ID \
  --album ALBUM_ID
```

**Getting IDs:**
- Person ID: Open person in Immich "People / Faces" - last URL segment
- Album ID: Open album - last URL segment
- Album must already exist (tool only adds assets)

**Multiple faces / exclusions:**
```bash
# Multiple faces in one album
--face p1 --face p2 --album a123

# Exclude a face (e.g., get p1+p2 but remove any with p3)
--face p1 --face p2 --skip-face p3 --album a123
```

**Continuous sync options:**
- `--run-every-seconds 300` - Built-in loop (every 5 min)
- Cron: `0 */2 * * *` for isolated runs every 2 hours

**Docker:**
```bash
docker run --rm rbrucker/immich-face-to-album \
  immich-face-to-album --key K --server https://s --face P --album A \
    --run-every-seconds 600
```

**Use case:** Auto-updating "kids album" for grandparents - add kids' face IDs, optionally exclude other family members, share album link.

### Power User Tips

*Source: [HN discussion](https://news.ycombinator.com/item?id=45447614) - Added: 2026-01-18*

**ZFS Snapshots for Safety:**
Use ZFS (or other snapshotting filesystem) to take snapshots before updates or large imports. Makes Immich essentially bullet-proof - retry imports with different flags if unhappy with results.

**Import Methods:**
- `immich-cli` - Official CLI, works well for basic imports. Can use folder names as albums.
- `immich-go` - Better for Google Takeout imports (see above). Use `--folder-as-album` equivalent flags.

**Performance Notes:**
- Initial import will peg CPU for days (ML models processing faces, objects, etc.)
- Facial recognition is excellent
- Object recognition (dogs, etc.) less impressive
- Normal operation: 4 cores + 4GB RAM sufficient

**Support Package:**
Immich offers a "support package" for purchase that doesn't add features - purely financial support. Future feature: seamless encrypted off-site backups.

### Immich vs Ente
- Ente: larger scope, end-to-end encryption focus
- Immich: simpler, relies on existing encryption (Tailscale transit, LUKS disk)

### Memories (Nextcloud Photo App)

*Source: [memories.gallery](https://memories.gallery/) - Added: 2026-01-19*

For those already running Nextcloud, **Memories** is a Google Photos-like app that runs on top of your existing Nextcloud instance.

**Key Features:**
- Timeline view optimized for large libraries (hundreds of thousands of photos)
- Auto-upload via official Nextcloud iOS/Android apps (extracts EXIF metadata)
- Albums with sharing and multi-user collaboration
- AI tagging via Recognize and Face Recognition Nextcloud apps
- Map view with GPS plotting and reverse geocoding
- Video transcoding with VA-API/NVENC hardware acceleration
- EXIF metadata editing (bulk editing supported)
- E-book export (OPDS catalog for e-readers)

**Why Consider Memories:**
- **No lock-in**: Metadata stored in EXIF headers, easy migration
- **Performance**: Optimized for modest hardware (Raspberry Pi capable)
- **Existing Nextcloud users**: No separate service to maintain
- **Encryption**: Can encrypt data with secret key

**Immich vs Memories:**
- Immich: Standalone, purpose-built, more polished mobile apps
- Memories: Requires Nextcloud, but integrates with Nextcloud ecosystem (files, sharing, etc.)

---

## ntfy Push Notifications

*Source: [ntfy.sh](https://ntfy.sh/) - Added: 2026-01-18*

### What It Does
Send push notifications to phone/desktop via simple HTTP PUT/POST. Topics are created on-the-fly - no sign-up required (topic name acts as password if using public server).

### Basic Usage
```bash
# Send a notification
curl -d "Backup completed successfully" ntfy.sh/my-secret-topic

# With priority and tags
curl -H "Priority: high" -H "Tags: warning" -d "Disk 90% full" ntfy.sh/my-topic
```

### Key Features
- **Priorities**: Maps to different sounds/vibration patterns
- **Action buttons**: React to notifications directly
- **Attachments**: Send images, videos, files (e.g., surveillance camera pics)
- **Web app**: Subscribe to topics for desktop notifications
- **Tags/emojis**: Classify and personalize notifications

### Use Cases
- Cronjob completion alerts
- CI/CD pipeline notifications (GitHub Actions)
- Home automation alerts (security sensors, motion detection)
- Server monitoring (unauthorized logins, downloads complete)
- New episode notifications from media tools

### Self-Hosting
- Open source (Apache 2.0 / GPLv2)
- Self-hostable server component
- Apps available for iOS/Android/Desktop
- [GitHub](https://github.com/binwiederhier/ntfy) | [Discord/Matrix community]

### Integration
Simple HTTP API means it integrates with basically anything - scripts, automation tools, monitoring systems. Perfect complement to Uptime Kuma for custom application notifications.

---

## Stirling-PDF - Self-Hosted PDF Tools

*Source: [Stirling-Tools/Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF) - Added: 2026-01-18*

### What It Does

Locally hosted web-based PDF manipulation tool. Handle all PDF operations without uploading files to third-party services.

### Key Features

**Page Operations:**
- View/annotate PDFs with custom viewer
- Merge multiple PDFs into one
- Split PDFs at specified pages or extract all pages
- Rotate, remove, reorganize pages
- Multi-page layout (combine pages)
- Crop, scale, adjust contrast

**Conversion:**
- PDF ↔ Images
- Common files → PDF (via LibreOffice)
- PDF → Word/PowerPoint
- HTML/URL/Markdown → PDF

**Security:**
- Add/remove passwords
- Set PDF permissions
- Add watermarks
- Sign/certify PDFs
- Sanitize PDFs
- Auto-redact text

**Other:**
- OCR (via OCRMyPDF)
- Compress PDFs
- Extract images
- Compare two PDFs
- Repair corrupt PDFs
- PDF/A conversion

### Privacy Model

- No outbound calls for tracking
- Files exist client-side or in server memory only during task execution
- Downloaded files deleted from server immediately

### Quick Start (Docker)

```bash
docker run -d \
  -p 8080:8080 \
  -v /path/to/configs:/configs \
  -e DOCKER_ENABLE_SECURITY=false \
  --name stirling-pdf \
  frooodle/s-pdf:latest
```

**Docker Compose:**
```yaml
services:
  stirling-pdf:
    image: frooodle/s-pdf:latest
    ports:
      - '8080:8080'
    volumes:
      - ./stirling-configs:/configs
      - ./stirling-training:/usr/share/tessdata  # for OCR languages
    environment:
      - DOCKER_ENABLE_SECURITY=false
```

### Image Variants

| Variant | Use Case |
|---------|----------|
| `latest` | Full features, larger image |
| `latest-lite` | Smaller, no LibreOffice |
| `latest-ultra-lite` | Minimal, basic PDF ops only |

### Customization

Via `settings.yml` in `/configs` or environment variables:

```yaml
system:
  defaultLocale: 'en-US'
  googlevisibility: false

endpoints:
  toRemove: []  # Disable specific features
  groupsToRemove: []  # e.g., ['LibreOffice']
```

### Optional Login

1. Set `DOCKER_ENABLE_SECURITY=true`
2. Default login: admin / stirling
3. Forced password change on first login

API access via `X-API-Key` header after login.

### Use Cases

- **Family documents**: Merge school permission slips, organize medical records
- **Privacy**: Handle sensitive PDFs without cloud services
- **Bulk operations**: Batch compress, convert, or watermark files
- **Teaching kids**: Demo digital document security (passwords, redaction)

### NGINX Notes

If behind NGINX, set `client_max_body_size` (default 1MB is too small):
```nginx
client_max_body_size 50M;
```

For large files, also set `proxy_read_timeout 3600;`

---

## YourSpotify - Self-Hosted Spotify Tracking

*Source: [GitHub - Yooooomi/your_spotify](https://github.com/Yooooomi/your_spotify) - Added: 2026-01-18*

### What It Does

Self-hosted application that tracks your Spotify listening history and provides a dashboard to explore statistics. Polls the Spotify API periodically to collect data.

### Architecture

- **Server**: Node.js server that polls Spotify API
- **Client**: Web dashboard for exploring statistics
- **Database**: MongoDB for storage

### Quick Start (Docker)

```yaml
version: "3"

services:
  server:
    image: yooooomi/your_spotify_server
    restart: always
    ports:
      - "8080:8080"
    links:
      - mongo
    depends_on:
      - mongo
    environment:
      API_ENDPOINT: http://localhost:8080
      CLIENT_ENDPOINT: http://localhost:3000
      SPOTIFY_PUBLIC: __your_spotify_client_id__
      SPOTIFY_SECRET: __your_spotify_secret__

  mongo:
    image: mongo:6
    volumes:
      - ./your_spotify_db:/data/db

  web:
    image: yooooomi/your_spotify_client
    restart: always
    ports:
      - "3000:3000"
    environment:
      API_ENDPOINT: http://localhost:8080
```

### Setup Requirements

1. Create Spotify application at [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Set redirect URI: `http://<your-server>:8080/oauth/spotify/callback`
3. Copy Client ID and Client Secret to environment variables
4. Register users in Spotify dashboard (except app creator)

### Importing Historical Data

By default, only captures last 24 hours. To import history:

**Full Privacy Data (recommended):**
1. Request full privacy data from Spotify (Settings → Privacy → Request data)
2. Wait for email with download link (can take days/weeks)
3. Upload `endsongX.json` files via Settings page

**Regular Privacy Data:**
- Covers past year only
- Upload `StreamingHistoryX.json` files

### Use Cases

- See listening trends over time
- Track favorite artists/albums/genres
- Compare listening habits across periods
- Own your listening data (vs relying on Spotify Wrapped)

### Integration Notes

Pairs well with:
- **Plex**: If you have local music library alongside streaming
- **ntfy**: Notify on interesting listening milestones

---

## The Case Against Self-Hosting (Critique)

*Source: [The Future is NOT Self-Hosted](https://www.drewlyton.com/story/the-future-is-not-self-hosted/) by Drew Lyton - Added: 2026-01-18*

### The Argument

Self-hosting offers control and ownership, but ultimately leads to **isolation and inefficiency**. The author argues for community-hosted solutions instead.

### The Suburban Internet Analogy

Self-hosting creates "internet suburbia" where everyone maintains their own server:
- Requires mass duplicate, unused infrastructure
- Each household individually responsible for maintenance
- Silos people and makes sharing resources harder
- Creates worse experience than cloud services for collaborative features

**Example problem:** How do you create a shared photo album with friends on your self-hosted Immich? You'd need to expose services publicly, force friends to sign up for your app, or... just use Google Photos anyway.

### Key Insights

> "Self-hosting assumes isolated, independent systems are virtuous. But in reality, this simply makes them hugely inconvenient."

> "Self-reliance isn't freedom — it's the luxury of retreating from a system that others can't escape."

### The Author's Journey

Built home server with:
- Immich (Google Photos)
- Calibre-web (eBooks)
- Audiobookshelf
- Jellyfin

**Conclusion:** Fun project, provides peace of mind as backup, but realized how privileged the skills required are, and how unsustainable self-hosting is as a mass solution.

### The Alternative Vision: Community-Hosted

**Proposal:** Publicly funded, accessible, at-cost cloud services. Imagine:
- Library card includes 100GB encrypted storage, photo-sharing, media streaming
- End-to-end encryption standard
- Standardized protocols for switching between services
- Metered usage like utilities

**Why this could work:**
- Libraries already provide streaming services (Libby, Kanopy, Hoopla)
- Precedent exists for public digital infrastructure
- Non-profits or cooperatives could fill the gap if public funding isn't available

### Practical Takeaway

Self-hosting is valuable for:
- **Learning** how infrastructure works
- **Backup** as a safety net
- **Privacy** for sensitive data

But it's not a scalable solution to corporate tech dominance. True freedom requires collective infrastructure, not individual homesteads.

### Balanced View

Consider self-hosting as **one tool in the toolkit**, not the entire solution:
- Use it for personal/family data you want full control over
- Accept that collaborative features may still need cloud services
- Support community-hosted alternatives when they emerge
- Don't feel guilty about using cloud services for sharing

---

## Onyx - Self-Hosted AI Platform

*Source: [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) - Added: 2026-01-18*

### What It Does
Self-hostable Chat UI that works with any LLM. Runs in completely airgapped environments.

### Key Features
- **Custom Agents**: Build AI agents with unique instructions, knowledge, and actions
- **Web Search**: Google PSE, Exa, Serper integration + built-in scraper/Firecrawl
- **RAG**: Hybrid search + knowledge graph for uploaded files and ingested documents
- **40+ Connectors**: Pull knowledge from external applications
- **Deep Research**: Agentic multi-step search for in-depth answers
- **MCP Support**: Give agents ability to interact with external systems
- **Code Interpreter**: Execute code, analyze data, render graphs
- **Image Generation**: Generate images from prompts

### LLM Compatibility
Works with all LLMs:
- Cloud: OpenAI, Anthropic, Gemini, etc.
- Self-hosted: Ollama, vLLM, etc.

### Deployment
```bash
# One-command install (Docker)
curl -fsSL https://raw.githubusercontent.com/onyx-dot-app/onyx/main/deployment/docker_compose/install.sh > install.sh && chmod +x install.sh && ./install.sh
```

Options: Docker (most users), Kubernetes (large teams), Terraform, cloud-specific guides (AWS EKS, Azure VMs)

### Enterprise Features
- Enterprise Search: Scales to tens of millions of documents
- Security: SSO (OIDC/SAML/OAuth2), RBAC, credential encryption
- User Management: Basic, curator, and admin roles
- Document Permissioning: Mirrors user access from external apps

### Licensing
- **Community Edition (CE)**: MIT license, free
- **Enterprise Edition (EE)**: Additional features for larger organizations

### Use Cases
- **Internal Search**: The average worker spends 9.3 hours/week looking for information - unblock teams with GenAI search across all company docs and apps
- **Customer Support**: Instant answers across entire product documentation
- **Developer Productivity**: Devs ship faster with instant access to internal knowledge
- **Sales Enablement**: Close deals faster with access to customer conversations and product updates
- **Enterprise Scale**: Handles tens of millions of documents
- AI agents with access to private data sources
- Airgapped/secure environment AI deployment

---

## Ory Kratos - Self-Hosted Authentication

*Source: [ory/kratos](https://github.com/ory/kratos) - Added: 2026-01-18*

### What It Does
Headless, cloud-native authentication and identity management written in Go. Self-hosted alternative to Auth0, Okta, Firebase Auth.

### Key Features
- **Passkeys**: Modern passwordless authentication
- **Social Sign In**: OAuth2/OIDC providers (Google, GitHub, etc.)
- **Magic Links**: Email-based passwordless login
- **MFA**: TOTP, SMS, WebAuthn support
- **SAML**: Enterprise SSO integration
- **API-first**: Headless design - bring your own UI

### Why Self-Host Authentication?
- Full control over user data and privacy
- No vendor lock-in
- No per-user pricing that scales poorly
- Data stays in your infrastructure
- Aligns with self-hosting philosophy for other services

### Considerations
- More setup complexity vs managed services (Auth0/Okta)
- Requires maintaining security updates
- Need to handle scaling yourself (though it claims "billion+ users" scale)
- Good DX but still more work than dropping in a SaaS SDK

### Use Cases
- Self-hosted apps needing user authentication
- Privacy-focused projects
- Projects where data sovereignty matters
- Cost-sensitive scaling (avoid per-MAU pricing)

---

## Syllabi - AI Chatbot Platform with RAG

*Source: [syllabi-ai.com](https://www.syllabi-ai.com/) - Added: 2026-01-18*

### What It Does
Open-source AI chatbot platform for rich, interactive conversations that integrate documents, diagrams, code, and multimedia. Designed for transparency, privacy, and full control over AI infrastructure.

### Key Features
- **Rich conversations**: Goes beyond simple Q&A - documents, diagrams, code, multimedia in one place
- **RAG support**: Use documents as knowledge sources
- **Full customization**: Tailor chatbot to match brand and business needs
- **Tool integrations**: Connect to existing apps as knowledge sources, deployment channels, or workflow automation
- **Privacy-focused**: Built for teams who value transparency and control

### Use Cases
- Team knowledge base chatbot
- Customer-facing branded chatbots
- Internal documentation assistant
- Workflow automation with AI
- Educational tools for teaching AI/programming concepts

### Deployment
Self-hostable - allows full control over AI infrastructure without relying on third-party services.

### Considerations
- Developer-friendly focus means setup may require technical skills
- Good for teams wanting to avoid vendor lock-in on AI chat solutions
- Integrations work bidirectionally (knowledge sources AND action triggers)

---

## Docker Swarm - Simple Container Orchestration

*Source: [Docker Swarm in 2022](https://www.yvesdennels.com/posts/docker-swarm-in-2022/) by Yves Dennels - Added: 2026-01-18*

### When to Use It

Docker Swarm is a solid choice for **single-server web app deployments** where:
- No multi-node or HA requirements
- You want something simpler than Kubernetes
- You have existing docker-compose.yml files to leverage

Despite perception that it's "dead," it works reliably for straightforward use cases.

### Why It Works Well

**Key advantage:** Deploy apps using standard docker-compose files. Most projects already include `docker-compose.yml`, making deployment trivial vs. translating to K8s manifests.

Setup is fast—author had multiple apps running in a couple hours with everything working on first try.

### Recommended Setup

Follow [Docker Swarm Rocks](https://dockerswarm.rocks/) approach:
- Traefik as reverse proxy
- Standard compose-based deployments
- Easy SSL/TLS with Let's Encrypt

### Trade-offs

**Pros:**
- Fastest path from docker-compose to production
- Minimal learning curve if you know Docker
- Good enough for "a good chunk of web app deployments out there"

**Cons:**
- Not actively developed
- Smaller community (but this matters less when setup is trivial)
- Won't scale to multi-node production clusters

### When to Consider Alternatives

- **Kubernetes**: When you need multi-node, HA, or complex orchestration
- **Nomad**: HashiCorp alternative, more flexible but steeper learning curve
- **Podman pods**: For single-server with better security (see Podman notes)

### The Pragmatic View

> "The speed at which I could deploy my infrastructure makes it worth the bet. And if I have to migrate to another solution later on, I won't have lost a lot of time anyway."

For personal infrastructure or small projects, Docker Swarm's simplicity beats premature complexity.

---

## One-Click App Platforms (Sandstorm Alternatives)

*Source: Notion inbox item - Added: 2026-01-18*

### Overview

For home servers with one-click installs and user management, several platforms exist as alternatives to Sandstorm. Most can run alongside other services without monopolizing the server.

### Platform Comparison

| Platform | Best For | Notes |
|----------|----------|-------|
| **Cloudron** | Managed app experience | Strong user management, automatic updates, built-in SSO |
| **CapRover** | Developers | PaaS-style, deploys via git or Docker, Heroku-like experience |
| **Umbrel** | Home users | Beautiful UI, Bitcoin-focused but expanding, very beginner-friendly |
| **Runtipi** | Beginners | 200+ one-click apps, auto SSL, simple web UI, free/open-source. [runtipi.io](https://runtipi.io) |
| **Unraid** | NAS + apps | Primarily a NAS OS, app store is secondary feature |
| **TrueNAS SCALE** | ZFS + apps | Apps via Kubernetes (SCALE), enterprise-grade storage |
| **Portainer** | Docker power users | App templates, but more of a Docker management UI |

### Considerations

**Pros:**
- User management and SSO built-in (especially Cloudron)
- One-click installs reduce maintenance burden
- Good for non-technical family members or shared hosting

**Cons:**
- May introduce complexity/maintenance overhead vs. bare Docker
- Some lock-in to platform's way of doing things
- Resource overhead from platform itself

### Family Use Case

These platforms can facilitate family projects:
- Kids can learn on managed environments
- Parents maintain control without deep sysadmin knowledge
- Shared apps (photo libraries, media servers) with proper user accounts

---

## Sandstorm Platform

*Source: [sandstorm.org/features](https://sandstorm.org/features) - Added: 2026-01-18*

### What It Does

Self-hostable platform that simplifies app management with 93+ apps in its App Market. Each app instance runs in its own secure sandbox.

### Key Features

- **Single Sign-On**: One login for all apps, eliminates password fatigue
- **Unified Sharing**: Consistent access control across all apps - share documents/projects with same UI
- **Automatic Updates**: Apps update themselves, minimal maintenance
- **Easy Backups**: Simple data backup for all hosted apps
- **Powerbox UI**: Unique feature - secure, intuitive interactions between apps (capability-based security)

### Security Model

- **Sandboxed Apps**: Each grain (app instance) runs isolated
- **Protection Against Bugs**: App vulnerabilities don't compromise other apps or system
- **Auditable Access**: Clear visibility into who has access to what
- **External Identity Sharing**: Connect external identities for collaboration

### Unique Concepts

- **Grains**: Individual instances of apps (e.g., one grain = one document)
- **Capability-Based Security**: Apps request specific permissions through Powerbox rather than having blanket access
- **Decentralized Trust**: No central administrator needed for daily operations

### Trade-offs

**Pros:**
- Most "app platform" feel of all alternatives
- Strong security model by design
- Good for non-technical users once set up

**Cons:**
- Smaller app ecosystem (93 apps vs. unlimited Docker containers)
- Less active development recently
- Apps must be specifically packaged for Sandstorm

---

## Octelium - Zero Trust Access Platform

*Source: [octelium/octelium](https://github.com/octelium/octelium) - Added: 2026-01-18*

### What It Does

Free and open source zero trust access platform. Self-hosted alternative to:
- **Remote Access VPNs**: OpenVPN Access Server, Twingate, Tailscale
- **ZTNA**: Cloudflare Access, Teleport, Google BeyondCorp
- **Secure Tunnels**: ngrok, Cloudflare Tunnel
- **API Gateways**: Kong Gateway, Apigee

### Key Features

- **Zero Trust Architecture**: Identity-based, L7-aware access control on a per-request basis
- **Client-based & Clientless Access**: WireGuard/QUIC tunnels OR BeyondCorp-style browser access
- **Secret-less Authentication**: Eliminates distributing long-lived API keys
- **Policy-as-Code**: Dynamic, context-aware access control
- **Continuous Authentication**: Not just at login, but throughout the session

### Use Cases

| Use Case | What It Replaces |
|----------|------------------|
| Modern remote access VPN | OpenVPN, Tailscale, Twingate |
| ZTNA/BeyondCorp | Cloudflare Access, Zscaler |
| Self-hosted secure tunnels | ngrok |
| Self-hosted PaaS | Vercel, Netlify |
| API gateway | Kong, Apigee |
| AI gateway | Route to LLM providers with access control |
| MCP gateway | Secure infrastructure for Model Context Protocol |
| Homelab infrastructure | Unified access to all devices behind NAT |

### Homelab Relevance

Connect and provide secure remote access to:
- All devices behind NAT (laptops, IoT, Raspberry Pis, routers)
- Cloud provider resources
- Privately host websites, APIs, blogs
- Remote access to heavy containers (Ollama, databases, Pi-hole)

### Deployment

Runs on Kubernetes. Minimum: cheap cloud VM/VPS with 2GB RAM, 20GB disk, Ubuntu 24.04+.

```bash
# SSH into VPS as root, then:
curl -o install-demo-cluster.sh https://octelium.com/install-demo-cluster.sh
chmod +x install-demo-cluster.sh
./install-demo-cluster.sh --domain YOUR_DOMAIN
```

### Licensing

- **Client-side components**: Apache 2.0 (open source)
- **Cluster-side components**: AGPLv3 (with commercial license option)

### When to Use vs Tailscale

**Tailscale** (simpler):
- Quick mesh networking between devices
- Zero config VPN for personal use
- Good enough for most homelab access

**Octelium** (more powerful):
- Need L7-aware access control (per-request policies)
- Want to expose services publicly with BeyondCorp-style auth
- Running MCP/AI agent infrastructure needing identity management
- Want ngrok-style tunnels without per-tunnel costs
- Multi-tenant or team scenarios with complex access policies

### Status

Currently in public beta. Good for development, personal, or undemanding production use cases

---

## The Philosophy of Tech Independence

*Source: [Self-Host & Tech Independence](https://www.ssp.sh/blog/self-host-self-independence/) by ssp.sh - Added: 2026-01-18*

### Why It Matters

Tech independence means not depending on any particular company or software. The premise: by learning Linux fundamentals, you can host most things yourself—not because you need to, but because you want to.

### The Compounding Domain Strategy

> "If people ask me how they should start writing or how to get a job, I always say to buy a domain first."

**The problem with platform-hopping:**
- WordPress → Medium → Substack → Ghost
- Each migration risks losing backlinks, content history
- Compare: A 10-year blog with same domain vs. starting over every few years

**The solution:**
- Buy a domain first (don't overthink the name)
- Host your own blog if technical
- Migrate domain later if needed—but you can't do that without owning it

### The Joy Factor

What makes self-hosting rewarding:
- **Using what you built** - satisfaction from running your own infrastructure
- **Subscription fatigue escape** - not paying recurring fees for basics
- **The learning journey** - "Initially everything seems hard, but once you know how, it's kind of obvious"
- **Open-source community** - meeting like-minded people, giving and receiving feedback

### Starting Points

**For terminal comfort:** Learning vim/Neovim puts you in terminal-land where Linux commands become second nature.

**Derek Sivers' approach (deep tech independence):**
- Self-host email
- Self-host contacts & calendar
- Self-host backup storage

**Start smaller:**
1. Buy your own domain
2. Host a simple blog
3. Add services incrementally

### The Open-Source Gratitude Chain

One person's open-source project enables another's:
- **Quartz** (Jacky Zhao) → open-source Obsidian Publish alternative
- **GoatCounter** (Martin Tournoij) → privacy-respecting analytics
- **Listmonk** (Kailash Nadh) → self-hosted newsletter
- **listmonk-rss** (Stephan Heuel) → auto-send emails on new blog posts

> "I understand that everyone needs to make money, but in a perfect world, everyone would just work collaboratively on open-source software to make the world a better place."

### Practical Homelab Starting Point

You don't need expensive hardware:
- Buy a cheap, old client server and refurbish it
- Old hardware + good OS = capable homelab
- Start with a few services, expand as you learn

### Additional Self-Hosted Services Worth Exploring

| Service | Purpose |
|---------|---------|
| **Paperless** | Digital document management with OCR |
| **PhotoPrism** | Google Photos alternative (see Immich above) |
| **Pi-hole** | Network-wide ad blocking |
| **Nginx Proxy Manager** | Web-based reverse proxy management |
| **Audiobookshelf** | Audiobook and podcast server (see detailed section below) |
| **Calibre** | E-book management and serving |
| **Syncthing** | Decentralized file sync |
| **Gitea/Forgejo** | Lightweight self-hosted Git (Forgejo is the community fork, recommended) |

### The Markdown Unifier

Common thread across self-hosting: **Markdown everywhere**
- GitHub documentation
- Static site generators (Hugo, etc.)
- Newsletters (Listmonk)
- Note-taking (Obsidian)
- No rich-text conversion headaches between tools

---

## The Five Hidden Taxes of SaaS Integration

*Source: [SaaS Is Just Vendor Lock-In with Better Branding](https://rwsdk.com/blog/saas-is-just-vendor-lock-in-with-better-branding) by RedwoodSDK - Added: 2026-01-18*

### The Premise

Developers are told "focus on the product" and let SaaS handle the rest. But integrating third-party services (auth, queues, file storage, image optimization) comes with hidden costs beyond dollars—time, friction, and mental overhead.

### The Five Taxes

**1. Discovery Tax**
Before writing code, you must research:
- What problem does this actually solve?
- Compatible with my stack?
- Is pricing sane at my scale?
- Are docs clear? Any implementation weirdness?

This research is non-transferable. What you learn about one service doesn't help with the next.

**2. Sign-Up Tax**
- Usage-based vs lock-in tiers?
- Can team members access the dashboard without paying more?
- Can you even test without hitting a paywall?

You're now on the hook before writing any code.

**3. Integration Tax**
The real work:
- Read the docs
- Install libraries
- Wire into framework
- Figure out edge cases the docs don't mention (docs are marketing)

Often fighting your tooling—they target lowest common denominator.

**4. Local Development Tax**
- Does it offer a local emulator?
- Can you stub it in tests?
- Need to tunnel to cloud to test one feature?

Now you've got branching configuration: production, staging, local...

**5. Production Tax**
You're "done" but not:
- Works in staging? PR previews?
- Securely manage API keys
- Monitoring, logging, alerting
- Debug why it worked on laptop but fails in prod

### The Lock-In Reality

> "No matter what choice you make, it's always going to be vendor-locked in. Switching out something, even if it's open source and self-hosted, means you're rewriting a lot of code."

### The Integrated Platform Alternative

Instead of paying these taxes repeatedly, pick a platform where everything speaks the same language:

**Examples:** Cloudflare, Supabase, Vercel

**Benefits:**
- No context switching between vendors
- No API key wrangling
- No compatibility hacks or configuration forks
- Local-feeling integrations that work same in dev and production

> "They collapse the distance between your code and your services. And in doing so, they give you back the one thing no SaaS vendor can sell you: Flow."

### How This Relates to Self-Hosting

| Approach | Taxes Paid | Trade-off |
|----------|-----------|-----------|
| **Multiple SaaS** | All five, repeatedly | Maximum convenience per service, maximum integration overhead |
| **Integrated Platform** | Mostly avoided | Simpler DX, but platform lock-in instead of service lock-in |
| **Self-Hosting** | Integration + Production | Full control, but you own all maintenance |

**The insight:** The question isn't "SaaS vs self-hosting" but rather "scattered dependencies vs cohesive platform." Both integrated SaaS platforms (Cloudflare) and self-hosted stacks (Docker + unified tooling) solve the same problem: reducing the cognitive load of managing many independent services.

**For self-hosters:** This reinforces the value of standardized infrastructure (Docker Compose, Traefik/Caddy, shared auth) that creates the same "everything speaks the same language" benefit.

---

## WhoDB - Database Management Tool

*Source: [clidey/whodb](https://github.com/clidey/whodb) - Added: 2026-01-18*

### What It Does

Lightweight database management tool (<50MB) combining Adminer-like simplicity with modern UX. Built with GoLang for speed. Natural language queries via Ollama, ChatGPT, or Anthropic integration.

### Key Features

- **Natural Language Queries**: Talk to your data instead of writing SQL
- **Schema Visualization**: Interactive graphs to visualize database structure
- **Inline Editing**: Edit and preview data directly in the interface
- **Scratchpad**: Jupyter notebook-like interface for database queries
- **Lazy Loading**: Smooth performance with large datasets
- **Multi-Database Support**: PostgreSQL, MySQL, SQLite3, MongoDB, Redis, MariaDB, ElasticSearch, ClickHouse

### Quick Start (Docker)

```bash
docker run -it -p 8080:8080 clidey/whodb
```

Or with AI integration:

```yaml
version: "3.8"
services:
  whodb:
    image: clidey/whodb
    environment:
      # Ollama (local LLM)
      # - WHODB_OLLAMA_HOST=localhost
      # - WHODB_OLLAMA_PORT=11434

      # OpenAI
      - WHODB_OPENAI_API_KEY=...
      # - WHODB_OPENAI_ENDPOINT=https://api.openai.com/v1

      # Anthropic
      - WHODB_ANTHROPIC_API_KEY=...
      # - WHODB_ANTHROPIC_ENDPOINT=https://api.anthropic.com/v1
    ports:
      - "8080:8080"
```

Access at `http://localhost:8080`

### Why It's Useful for Self-Hosters

- **Lightweight**: Runs on minimal resources, perfect for home servers
- **No SQL Required**: Natural language makes database management accessible
- **Consistent UI**: Same interface across all database types
- **Local AI**: Pair with Ollama for fully offline database queries

### vs DBeaver

- DBeaver: Feature-rich but resource-heavy
- WhoDB: Lightweight, runs on minimal resources, designed for smaller setups

### Considerations

- Better suited for development/admin tasks than production frontends
- AI query accuracy depends on model quality
- Balance automation with understanding—don't lose SQL skills entirely

---

## Homepage - Application Dashboard

*Source: [gethomepage/homepage](https://github.com/gethomepage/homepage) - Added: 2026-01-18*

### What It Does

Modern, customizable application dashboard with Docker integration and 100+ service widgets. Serves as a central landing page for all self-hosted services.

### Key Features

- **Service Integrations**: 100+ widgets for popular apps (Plex, Jellyfin, Sonarr, Radarr, all *arr apps, etc.)
- **Docker Auto-Discovery**: Automatically detects and displays services via Docker labels
- **Information Widgets**: Weather, calendar, time, search, system stats
- **Fast & Secure**: Statically generated, proxies API requests to hide keys
- **YAML Configuration**: Simple file-based setup (no database)
- **Multi-Platform**: AMD64, ARM64 images available

### Quick Start (Docker)

```yaml
services:
  homepage:
    image: ghcr.io/gethomepage/homepage:latest
    container_name: homepage
    environment:
      HOMEPAGE_ALLOWED_HOSTS: your-domain.com
      PUID: 1000
      PGID: 1000
    ports:
      - 3000:3000
    volumes:
      - /path/to/config:/app/config
      - /var/run/docker.sock:/var/run/docker.sock:ro
    restart: unless-stopped
```

### Configuration

All config via YAML files in `/app/config`:
- `services.yaml` - Define services and widgets
- `widgets.yaml` - Configure information widgets
- `settings.yaml` - Theme, layout, general settings
- `bookmarks.yaml` - Quick links

### Security Note

Homepage has **no built-in authentication**. Deploy behind:
- Reverse proxy with auth (Caddy + OAuth, Authelia)
- VPN (Tailscale)
- Both

### vs Alternatives

| Dashboard | Best For |
|-----------|----------|
| **Homepage** | Most polished, best widget support |
| **Homarr** | Drag-and-drop editing |
| **Organizr** | Tab-based organization |
| **Dashy** | Highly configurable, complex setup |

### Family Use Case

Great for family homelab:
- Central hub for all services (Plex, Immich, etc.)
- Calendar widget for family scheduling
- Weather at a glance
- Kids can find services without remembering URLs

---

## Recommendarr - AI Media Recommendations

*Source: [fingerthief/recommendarr](https://github.com/fingerthief/recommendarr) - Added: 2026-01-18*

### What It Does

AI-powered recommendation engine for TV shows and movies based on your existing media library. Analyzes what you have and suggests what you'd like.

### Key Features

- **AI-Powered**: Uses LLMs to generate personalized recommendations
- **Library Integration**: Connects to Sonarr/Radarr to analyze your collection
- **Watch History**: Integrates with Plex, Jellyfin, Tautulli, Trakt for viewing patterns
- **Flexible AI Backend**: OpenAI, Ollama, LM Studio, or any OpenAI-compatible API
- **Dark/Light Mode**: Theme preferences
- **Poster Images**: Visual display with fallback generation

### Quick Start (Docker)

```bash
docker run -d \
  --name recommendarr \
  -p 3000:3000 \
  -v recommendarr-data:/app/server/data \
  tannermiddleton/recommendarr:latest
```

Access at `http://localhost:3000`

**Default credentials:** admin / 1234 (change immediately!)

### Configuration

After install, connect:
1. **Media Services**: Sonarr, Radarr for library analysis
2. **Watch History**: Plex, Jellyfin, Tautulli, Trakt for viewing patterns
3. **AI Provider**: OpenAI API, Ollama (local), LM Studio, or compatible service
4. **Optional**: OAuth login (Google, GitHub, etc.)

### Why It's Useful for Self-Hosters

Complements existing media stack:
- **Have**: Plex/Jellyfin + Sonarr/Radarr + *arr stack
- **Add**: AI recommendations based on what you already own

Instead of relying on streaming service algorithms or manually searching for "similar to X," get personalized suggestions from your own library data.

### Considerations

- Requires AI API (OpenAI) or local model (Ollama) for inference
- Quality of recommendations depends on model and library size
- Works best with established libraries and watch history
- Self-hosted = your viewing data stays private

---

## Calendarr - Media Release Notifications

*Source: [jordanlambrecht/calendarr](https://github.com/jordanlambrecht/calendarr) - Added: 2026-01-18*

### What It Does

Docker container that fetches TV and movie release calendars from Sonarr and Radarr, posting updates to Discord or Slack on a customizable schedule. Keeps family informed about upcoming releases without manual tracking.

### Key Features

- **Multi-Calendar Aggregation**: Combines multiple Sonarr and Radarr feeds
- **Grouped by Day**: Organizes shows and movies by day of week
- **Flexible Scheduling**: Daily or weekly notifications
- **Discord + Slack**: Supports both notification platforms
- **Custom Footers**: Add markdown footers to announcements
- **Event Deduplication**: No duplicate notifications

### Quick Start (Docker Compose)

```yaml
version: "3.8"
name: calendarr
services:
  calendarr:
    image: ghcr.io/jordanlambrecht/calendarr:latest
    container_name: calendarr
    restart: unless-stopped
    environment:
      USE_DISCORD: "true"
      DISCORD_WEBHOOK_URL: ${DISCORD_WEBHOOK_URL}
      CALENDAR_URLS: >
        [{
          "url":"${ICS_URL_SONARR_1}",
          "type":"tv"
        },
        {
          "url":"${ICS_URL_RADARR_1}",
          "type":"movie"
        }]
      CUSTOM_HEADER: "TV Guide - What's Up This Week"
      TZ: "America/Chicago"
      SCHEDULE_TYPE: "WEEKLY"  # or "DAILY"
      RUN_TIME: "09:00"
    volumes:
      - ./logs:/app/logs:rw
```

### Getting Calendar URLs

**Sonarr:**
1. Go to Calendar > iCal Link
2. Leave checkboxes blank (optionally set tags)
3. Copy the iCal link

**Radarr:**
1. Go to Calendar > iCal Link
2. Leave checkboxes blank (optionally set tags)
3. Copy the iCal link

### Configuration Options

| Variable | Required | Description |
|----------|----------|-------------|
| `DISCORD_WEBHOOK_URL` | Yes (if Discord) | Discord webhook URL |
| `SLACK_WEBHOOK_URL` | Yes (if Slack) | Slack webhook URL |
| `CALENDAR_URLS` | Yes | JSON array of calendar feeds |
| `SCHEDULE_TYPE` | No | "DAILY" or "WEEKLY" |
| `RUN_TIME` | No | When to run (HH:MM, 24-hour) |
| `CALENDAR_RANGE` | No | "AUTO", "DAY", or "WEEK" |
| `CUSTOM_HEADER` | No | Custom title for announcements |
| `RUN_ON_STARTUP` | No | Run immediately on container start |

### Manual Run

```bash
docker exec calendarr python /app/main.py
```

### Family Use Case

Perfect for family media coordination:
- Weekly announcement of upcoming episodes and movie releases
- Kids stay informed about favorite shows
- Reduces "when does X come out?" questions
- Shared Discord channel keeps everyone on same page

### Why It Fits the Stack

Complements existing *arr ecosystem:
- **Sonarr/Radarr**: Track and download media
- **Plex/Jellyfin**: Stream media
- **Recommendarr**: AI suggestions for new content
- **Calendarr**: Keep family informed about releases

Low-maintenance addition that adds family-facing value to the media stack.

---

## Audiobookshelf - Audiobook & Podcast Server

*Source: [audiobookshelf.org](https://www.audiobookshelf.org/) - Added: 2026-01-18*

### What It Does

Self-hosted audiobook and podcast server. Manage personal media libraries without reliance on commercial streaming services. Open source, active community.

### Key Features

- **Audiobook Management**: Organize audiobook collections with metadata, progress tracking, bookmarks
- **Podcast Support**: Subscribe to and download podcasts, manage feeds
- **Multi-User**: Multiple users with individual progress tracking
- **Streaming & Sync**: Stream from server, sync progress across devices
- **Web Interface**: Browser-based access to full library

### Client Apps

| Platform | Availability |
|----------|-------------|
| Android | Google Play Store |
| iOS | TestFlight (beta) |
| Web | Any browser |

### Quick Start (Docker)

```bash
docker run -d \
  --name audiobookshelf \
  -p 13378:80 \
  -v /path/to/audiobooks:/audiobooks \
  -v /path/to/podcasts:/podcasts \
  -v /path/to/config:/config \
  -v /path/to/metadata:/metadata \
  advplyr/audiobookshelf
```

Or with Docker Compose:

```yaml
version: "3.7"
services:
  audiobookshelf:
    image: advplyr/audiobookshelf
    container_name: audiobookshelf
    ports:
      - 13378:80
    volumes:
      - /path/to/audiobooks:/audiobooks
      - /path/to/podcasts:/podcasts
      - ./config:/config
      - ./metadata:/metadata
    restart: unless-stopped
```

### Family Use Case

Audiobookshelf fits well into family self-hosting:
- **Kids**: Age-appropriate audiobooks without ads or subscription fees
- **Commute listening**: Parents can stream during travel
- **Shared library**: Family audiobook collection accessible to everyone
- **Reading encouragement**: Audiobooks as gateway to literature for reluctant readers
- **Parenting**: Convenient way to consume books while juggling responsibilities

### Integration with Stack

Complements other self-hosted media:
- **Calibre/Calibre-web**: E-books
- **Audiobookshelf**: Audiobooks + podcasts
- **Plex/Jellyfin**: Movies/TV
- **Immich**: Photos

---

## Self-Hosting Community Insights (2024 Survey)

*Source: [Ars Technica - Self-hosting is having a moment](https://arstechnica.com/gadgets/2025/05/self-hosting-is-having-a-moment-ethan-sholly-knows-why/) - Added: 2026-01-18*

### Ethan Sholly and selfh.st

Ethan Sholly runs [selfh.st](https://selfh.st) - a site, newsletter, and podcast covering the self-hosting scene. He works in finance (not tech) but started as a CS minor with "just enough knowledge to get Plex working." His journey:

1. Desktop PC running Plex ("Can you turn your desktop on—it's movie night")
2. Tower server with 10TB drives
3. "What else can I self-host?" exploration
4. Assembled bookmarked GitHub repos into a central resource
5. Started writing about the scene with personality and punch

### Why Self-Hosting is Growing

From ~3,700 survey responses in 2024 (nearly double 2023):

**Top motivations (ranked):**
1. Hobby
2. Privacy
3. Education
4. Flexibility
5. Cost
6. Convenience
7. Business (small)

**Hardware used:**
1. Low-powered devices (~2,000 responses)
2. Consumer hardware (~1,600)
3. Desktop PC / Custom build (~1,300 each)
4. Enterprise, server, laptop, cloud VPS trailing

### What Drove the Trend

Sholly identified several factors:
- **Privacy concerns** for photos, files, and personal data
- **Cost of cloud hosting** and storage subscriptions
- **Better accessibility** through GitHub, Reddit, sites like selfh.st
- **Docker** as a game-changer for installation
- **Unraid** making server management approachable
- **SBCs like Raspberry Pi** - affordable entry points
- **Mini PCs and NUCs** - pandemic-popular hardware
- **Piracy** (the elephant in the room) - "*arr stack" usage, newcomer questions often about "media files"

### Favorite Self-Hosted Apps (2024)

1. Jellyfin
2. Home Assistant
3. Plex

### The Donation Gap

Despite relying on these projects:
- 60% of respondents had NOT donated to a single self-hosted project in the past year
- This came up after Plex increased subscription prices and changed its business model in March 2024

### Home Lab vs Self-Hosting

Per Sholly:
- **Home labs**: More focused on hardware and networking, often professional skills brought home
- **Self-hosting**: Could technically run on a laptop in a closet—less infrastructure-focused

### The Mature View

> "It's not the end-goal, and we need to push on companies to fix the way they host their services. Convenience shouldn't be an add-on; privacy shouldn't be a value-add. A lot of services people are self-hosting, they might gladly pay for if companies gave them more organization and control."

### Resources

- [selfh.st](https://selfh.st) - Site, newsletter, podcast
- [r/selfhosted](https://reddit.com/r/selfhosted) - Subreddit community
- [AlternativeOSS](https://alternativeoss.com/) - Directory of open source alternatives to popular software (weekly newsletter available)
- GitHub project pages linked from the above

---

## WireGuard - Advanced Configuration

*Source: [HN Discussion](https://news.ycombinator.com/item?id=42229299) - Added: 2026-01-18*

### Beyond Basic Setup

WireGuard is elegant and simple for basic use, but advanced scenarios require understanding its limitations and workarounds.

### Key Management Challenge

The biggest friction point: manual key distribution. Unlike Tailscale (which handles this automatically), WireGuard requires you to:
- Generate key pairs for each device
- Distribute public keys to all peers
- Configure each device individually

**Tools that help:**
- **[Subspace](https://github.com/subspacecloud/subspace)** - Web UI for WireGuard config management, generates QR codes for mobile, SAML integration
- **wg-easy** - All-in-one WireGuard + Web UI solution

### Network Architecture Complexity

A WireGuard interface is essentially **point-to-multipoint non-broadcast** (similar to Frame Relay/ATM). This creates headaches for:

- **Dynamic routing**: Must hand-configure OSPF neighbors
- **Failover**: Interface stays "up" even when connection is dead—no automatic backup route switching

**Workarounds:**
- One interface per peer (point-to-point) instead of multipoint
- Layer GRE or L2TP on top of WireGuard
- Note: These workarounds sacrifice simplicity

### WireGuard vs Tailscale

| Aspect | WireGuard | Tailscale |
|--------|-----------|-----------|
| Key management | Manual | Automatic |
| NAT traversal | Manual config | Built-in (DERP relays) |
| Subnet routing | Manual iptables | "Subnet Routers" feature |
| Magic DNS | DIY | Built-in |
| Simplicity | Simple protocol, complex operations | Complex service, simple operations |

**When WireGuard makes sense:**
- Full control over infrastructure required
- Airgapped environments
- Cost sensitivity at scale
- Learning/understanding VPN fundamentals

**When Tailscale makes sense:**
- Quick setup for personal/small team
- Devices behind multiple NATs
- Don't want to manage key distribution

### The Unix Philosophy View

> "WireGuard is beautifully designed to be security fail-safe with no moving parts. However, that simplicity means a lot more leans on the rest of the ecosystem around WireGuard."

WireGuard does one thing well (encrypted tunnels) and leaves the rest to other components—contrast with OpenVPN's "everything and the kitchen sink" approach.

### FreeBSD Setup Notes

```bash
# Server config contains only private key + client public keys
# Client config contains client private key + server public key
doas pkg install wireguard
```

### Practical Recommendations

1. **Start with Tailscale** for homelab—it's WireGuard under the hood with managed complexity
2. **Graduate to raw WireGuard** when you need fine-grained control or cost savings at scale
3. **Use Subspace or wg-easy** if managing WireGuard directly—don't suffer manual config files
4. **Monitor connections externally**—WireGuard won't tell you when a peer is unreachable

### Wag - WireGuard with MFA

*Source: [NHAS/wag](https://github.com/NHAS/wag) - Added: 2026-01-18*

Adds multi-factor authentication, route restrictions, and device enrollment to WireGuard. Useful when you need more access control than basic WireGuard provides but don't want a full zero-trust platform.

**Key Features:**
- Define routes requiring MFA authorization vs always-accessible public routes
- Easy API for registering new clients
- High availability clustering support
- Multiple MFA options: TOTP, WebAuthn (passkeys), OIDC, PAM
- Web management UI for administration
- ACL-based access control with per-user/group policies

**Requirements:**
- Linux kernel 5.9+ (for eBPF support)
- iptables, libpam
- Run as root

**Quick Start:**
```bash
# Binary release
curl -L $(curl -s https://api.github.com/repos/NHAS/wag/releases/latest | jq -M -r '.assets[0].browser_download_url') -o wag
sudo ./wag gen-config
sudo ./wag start -config <generated_config_name>
```

**Registration Workflow:**
```bash
# Create registration token
./wag registration -add -username tester

# Client fetches config
curl http://public.server.address:8080/register_device?key=<token>
# Returns templated WireGuard config
```

**ACL Example:**
```json
{
  "Acls": {
    "Policies": {
      "*": {
        "Mfa": ["10.0.0.0/16"],
        "Allow": ["10.0.1.1/32"]
      },
      "group:admins": {
        "Allow": ["192.168.0.0/24"],
        "Deny": ["192.168.0.5/32 22/tcp"]
      }
    }
  }
}
```

**When to Use:**
- Need MFA for VPN access (compliance, security policy)
- Want route-level access control (some routes public, some require MFA)
- Managing multiple users/devices with different permission levels
- Don't want full complexity of Octelium or similar zero-trust platforms

**Limitations:**
- Only supports clients with single AllowedIP
- IPv4 only
- Linux only

---

## Home Assistant Green - Dedicated Smart Home Hub

*Source: [Home Assistant Green](https://www.home-assistant.io/green/) - Added: 2026-01-18*

### What It Does

Plug-and-play device with Home Assistant pre-installed. Easiest entry point for Home Assistant—no Linux knowledge or Docker setup required.

### Key Specs

| Component | Specification |
|-----------|---------------|
| SoC | Rockchip RK3566, quad-core ARM Cortex-A55 |
| CPU | 1.8 GHz |
| RAM | 4 GB LPDDR4X |
| Storage | 32 GB eMMC |
| Connectivity | Gigabit Ethernet |
| USB | 2x USB 2.0 Type-A (for Zigbee/Z-Wave dongles) |
| Power | 12V DC, 1A (~1.7W idle, ~3W load) |
| Dimensions | 112mm x 112mm x 32mm |

### What's Included

- Gigabit Ethernet cable
- Universal power supply (EU, US, UK adapters)
- Quick start guide

### Setup

1. Plug in power and Ethernet
2. Download Home Assistant app (iOS/Android) or use web interface
3. Follow guided setup

No configuration, no Docker, no Linux. Just works.

### When to Use vs DIY Setup

**Home Assistant Green:**
- Want appliance experience (plug and play)
- Don't want to maintain Linux/Docker
- Sharing with less technical family members
- Budget-conscious entry point

**DIY (Mini PC + Docker):**
- Already have hardware
- Want more power/storage
- Running multiple services
- Learning infrastructure skills

### Add-ons Needed

Home Assistant Green has **no built-in Zigbee/Z-Wave radio**. For smart home device control, add:
- **Home Assistant Connect ZBT-1** (SkyConnect) - USB dongle for Zigbee + Thread
- Or other compatible Zigbee/Z-Wave USB coordinators

### vs Home Assistant Yellow

| Feature | Green | Yellow |
|---------|-------|--------|
| Price | Lower (~$99) | Higher (~$150+) |
| Built-in Zigbee | No | Yes |
| NVMe slot | No | Yes |
| Target user | Beginners | Power users |

### Long-term Support

Home Assistant Foundation (Nabu Casa) commits to long-term support. Same entity that develops Home Assistant and offers cloud subscription. Not a fly-by-night product.

---

## Dokploy - Self-Hosted PaaS

*Source: [Dokploy/dokploy](https://github.com/Dokploy/dokploy) - Added: 2026-01-18*

### What It Does

Open-source, self-hostable Platform as a Service (PaaS). Alternative to Vercel, Netlify, and Heroku for deploying applications and databases on your own VPS.

### Key Features

- **Multi-Language Support**: Deploy Node.js, PHP, Python, Go, Ruby, and more
- **Database Management**: MySQL, PostgreSQL, MongoDB, MariaDB, Redis with built-in provisioning
- **Automated Backups**: Schedule database backups to external storage
- **Docker Compose Support**: Native support for complex multi-container applications
- **Multi-Node Scaling**: Docker Swarm integration for horizontal scaling
- **One-Click Templates**: Deploy Plausible, Pocketbase, Cal.com, and other open-source apps instantly
- **Traefik Integration**: Automatic routing and load balancing
- **Real-time Monitoring**: CPU, memory, storage, network usage per resource
- **CLI/API**: Full programmatic control over deployments
- **Notifications**: Slack, Discord, Telegram, Email alerts for deployment status

### Quick Start

```bash
curl -sSL https://dokploy.com/install.sh | sh
```

That's it. Run on any VPS to get a full PaaS dashboard.

### When to Use vs Alternatives

| Platform | Best For |
|----------|----------|
| **Dokploy** | Self-hosted Heroku experience, multi-app deployments, team dashboards |
| **Docker Swarm** | Simpler single-server deployments via compose files |
| **Coolify** | Similar PaaS, different UX/feature set |
| **CapRover** | Git-based deployments, more developer-focused |

### Why It Fits the Stack

Dokploy bridges the gap between "raw Docker Compose on a server" and "managed platforms like Vercel":
- Get the convenience of push-to-deploy without vendor lock-in
- Manage multiple applications from a single dashboard
- Built-in database management eliminates separate provisioning
- Traefik handles SSL/routing automatically

### Considerations

- Requires a VPS with decent specs (not suitable for Raspberry Pi)
- Learning curve for platform-specific concepts (though simpler than Kubernetes)
- Community-driven—check activity before relying on for production
- Good for staging environments and personal projects; evaluate carefully for business-critical production

### Documentation

Full docs at [docs.dokploy.com](https://docs.dokploy.com)

---

## Dokku - Personal Heroku-Like PaaS

*Source: [Hamel's Blog](https://hamel.dev/blog/posts/dokku/) - Added: 2026-01-18*

### What It Does

Open-source PaaS that runs on a single VPS. Deploy apps with git push, get Heroku-like experience on a $7/month server. Ideal for developers who need to deploy many applications without Heroku's costs.

### Why Use Dokku

- **Cost-effective**: Run on cheap VPS ($7/month OVHcloud works fine for non-GPU workloads)
- **Heroku-familiar**: Same git-push workflow
- **Automatic SSL**: Let's Encrypt integration
- **Basic Auth**: Password-protect sites easily
- **Scale easily**: `dokku ps:scale myapp web=2`
- **Flexible**: Docker containers, static sites, any runtime
- **Plugin ecosystem**: Official plugins for most needs

### Installation

Install Dokku on your VPS, then configure SSH access:

```bash
# ~/.ssh/config
Host dokku
  HostName <your-dokku-server-ip>
  User ubuntu
  IdentityFile ~/.ssh/dokku
```

### Deploy a Docker App

**1. Create Dockerfile in your repo:**

```dockerfile
FROM python:3.10
COPY . /app
WORKDIR /app
RUN pip install .
ENTRYPOINT ["./entrypoint.sh"]
```

**entrypoint.sh:**
```bash
#!/bin/bash
exec uvicorn main:app --port "$PORT" --host 0.0.0.0
```

**2. Create app on Dokku host:**
```bash
dokku apps:create myapp
```

**3. Deploy from local:**
```bash
git remote add dokku dokku@dokku:myapp
git push dokku main
```

App runs at `myapp.yourdomain.com`.

### Deploy Static Sites

Great for private GitHub repos that need password protection (GitHub Pages Enterprise alternative).

**On Dokku host:**
```bash
dokku apps:create mysite
dokku config:set mysite NGINX_ROOT=_site
sudo dokku plugin:install https://github.com/dokku/dokku-http-auth.git
sudo chmod +x /home/dokku
```

**In your repo (assuming static site in `_site/` folder):**
```bash
touch .static
echo BUILDPACK_URL=https://github.com/dokku/buildpack-nginx > .env
git remote add dokku dokku@dokku:mysite
git push dokku main
```

**Add password protection:**
```bash
dokku http-auth:enable mysite <username> <password>
```

### SSL with Let's Encrypt

```bash
# On Dokku host
dokku plugin:install https://github.com/dokku/dokku-letsencrypt.git
dokku letsencrypt:enable myapp
```

Note: If using Cloudflare proxy, let Cloudflare handle SSL instead.

### GitHub Actions Deployment

```yaml
name: Deploy to Dokku
on:
  push:
    branches: [main]

concurrency:
  group: ${{ github.ref }}
  cancel-in-progress: true

jobs:
  deploy-dokku:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
        with:
          fetch-depth: 0

      - name: Install SSH key
        run: |
          echo "${{ secrets.DOKKU_SSH_PRIVATE_KEY }}" > private_key.pem
          chmod 600 private_key.pem

      - name: Push to Dokku
        run: |
          git remote add dokku dokku@yourhost.co:myapp
          GIT_SSH_COMMAND="ssh -i private_key.pem -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no" git push dokku main -f
```

### Useful Commands

```bash
# Run commands remotely (no SSH needed)
ssh dokku@yourhost.co apps:list

# Clear Docker cache for fresh build
ssh dokku@yourhost.co repo:purge-cache myapp

# Rebuild without pushing
ssh dokku@yourhost.co ps:rebuild myapp

# Scale workers
dokku ps:scale myapp web=2
```

### Dokku vs Other PaaS Options

| Platform | Best For |
|----------|----------|
| **Dokku** | Single-server, Heroku-like simplicity, git-push workflow |
| **Dokploy** | Web dashboard, multi-app management, team features |
| **CapRover** | Similar to Dokku but with web UI |
| **Docker Swarm** | Pure compose-file deployments |

### When to Use Dokku

- You're comfortable with CLI over web dashboards
- Want Heroku workflow without Heroku costs
- Deploying multiple small-to-medium apps on one server
- Need private static site hosting with auth
- Familiar with Docker already

---

## Server Setup Basics

*Source: [becomesovran.com/blog/server-setup-basics](https://becomesovran.com/blog/server-setup-basics.html) - Added: 2026-01-18*

Foundational server setup guide for self-hosting. Covers the groundwork before deploying any apps.

### SSH Setup

**Never use username/password login.** Set up SSH key authentication:

```bash
# On local machine - generate key
ssh-keygen -t ed25519 -C "your_email@example.com"

# Copy public key to server
ssh-copy-id -i ~/.ssh/id_ed25519.pub newuser@your_server_ip
```

**Lock down SSH config** (`/etc/ssh/sshd_config`):

```bash
Port 2222                          # Change default port
PermitRootLogin no                 # Disable root login
PasswordAuthentication no          # Disable password auth
PubkeyAuthentication yes           # Enable public key auth
AllowUsers newuser                 # Only allow specific users
MaxAuthTries 3                     # Limit auth attempts
ClientAliveInterval 300            # Client alive interval
ClientAliveCountMax 2              # Max client alive count
```

After changes: `sudo service ssh restart`

### User Management - Principle of Least Privilege

Create dedicated users for each app—limits damage if compromised, aids auditing:

```bash
# Create app user (no login shell)
sudo useradd -rms /usr/sbin/nologin -c "Running Nextcloud" appuser

# Create app directory
sudo mkdir /opt/myapp

# Set ownership
sudo chown appuser:appuser /opt/myapp
```

### Log Management

Set up log rotation to prevent disk fill and ease troubleshooting.

**Example NGINX logrotate config** (`/etc/logrotate.d/nginx`):

```
/var/log/nginx/*.log {
    weekly
    missingok
    rotate 52
    compress
    delaycompress
    notifempty
    create 0640 www-data adm
    sharedscripts
    postrotate
        [ -f /var/run/nginx.pid ] && kill -USR1 `cat /var/run/nginx.pid`
    endscript
}
```

Test with: `sudo logrotate -d /etc/logrotate.conf`

For multi-server setups, look into: Grafana Loki, Graylog, Fluentd.

### Backup Strategy

**The 3-2-1 Rule:**
- **3** copies of your data
- **2** different storage types
- **1** offsite backup (most important—protects against ransomware/catastrophe)

**Backup types:**
- **Full**: Complete copy, easiest restore, most space
- **Differential**: Changes since last full backup, middle ground
- **Incremental**: Changes since last backup (any type), fastest, complex restore

**Rule of thumb:**
- Incremental: frequently edited files (photos, documents, projects)
- Full: entire server/disk backups
- Differential: critical folders (`/etc`, `/opt`, logs)

**Critical**: A backup is not a backup unless you test it.

### Network Security - UFW + Fail2Ban

#### UFW (Uncomplicated Firewall)

```bash
# Install
sudo apt install ufw

# Default policies
sudo ufw default deny incoming
sudo ufw allow outgoing

# Allow essential services
sudo ufw allow ssh          # or specific port if changed
sudo ufw allow 80           # HTTP
sudo ufw allow 443          # HTTPS

# Useful commands
sudo ufw status verbose     # Check status
sudo ufw status numbered    # List rules with numbers
sudo ufw delete NUMBER      # Delete by number
sudo ufw limit ssh          # Rate limit (6 connections/30 sec from single IP)
sudo ufw allow from 192.168.1.100 to any port 22  # IP-specific access
sudo ufw enable             # Enable firewall
```

#### Fail2Ban

```bash
sudo apt install fail2ban

# Create local config
sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
sudo nano /etc/fail2ban/jail.local
```

**Basic settings in `[DEFAULT]`:**

```bash
bantime = 10m    # How long IP is banned
findtime = 10m   # Time window for failures
maxretry = 5     # Failures before ban
```

### NGINX Configuration

NGINX excels at serving static content, reverse proxying, and load balancing.

**Directory structure:**
- `/etc/nginx/nginx.conf` - Global config
- `/etc/nginx/sites-available/` - Staging configs
- `/etc/nginx/sites-enabled/` - Live configs (symlinked from sites-available)

**Go live workflow:**
```bash
# Link config to sites-enabled
ln -s /etc/nginx/sites-available/yoursite /etc/nginx/sites-enabled

# Reload and verify
sudo systemctl reload nginx
sudo systemctl status nginx
```

#### Static Site Config

```nginx
server {
    listen 80;
    listen [::]:80;
    server_name example.com www.example.com;
    root /var/www/example.com/html;
    index index.html index.htm;

    location / {
        try_files $uri $uri/ =404;
    }

    # Security headers
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header Referrer-Policy "no-referrer-when-downgrade" always;
    add_header Content-Security-Policy "default-src 'self' http: https: data: blob: 'unsafe-inline'" always;

    # Logging
    access_log /var/log/nginx/example.com.access.log;
    error_log /var/log/nginx/example.com.error.log warn;
}
```

#### Reverse Proxy Config

```nginx
server {
    listen 80;
    server_name app.example.com;

    location / {
        proxy_pass http://localhost:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

#### WebSocket Config

```nginx
server {
    listen 80;
    server_name ws.example.com;

    location / {
        proxy_pass http://localhost:8080;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        # WebSocket timeouts
        proxy_read_timeout 300s;
        proxy_send_timeout 300s;
    }
}
```

### SSL with Certbot

```bash
# Install
sudo apt install certbot python3-certbot-nginx

# Run (auto-detects sites-enabled configs)
certbot

# Verify auto-renewal
sudo systemctl status certbot.timer
```

Certbot handles renewal automatically when installed via apt on systemd systems.

### Quality of Life Tools

| Tool | Purpose | Install |
|------|---------|---------|
| **Btop** | Real-time CPU/RAM/disk/network monitor (must-have) | `apt install btop` |
| **NCDU** | Disk usage analyzer to find space hogs (must-have) | `apt install ncdu` |
| **Midnight Commander (mc)** | Two-panel file manager | `apt install mc` |
| **GoAccess** | Real-time web log analyzer | `apt install goaccess` |
| **Neoss** | Connection monitor (replaces `ss`) | `npm install -g neoss` |

### DNS Basics

**A Record**: Points domain to IP address. For VPS with static IP, set once and forget.

**Dynamic DNS (DDNS)**: For home servers without static IP. Client checks IP periodically and updates DNS if changed.

DDNS providers/tools: DuckDNS, No-IP, Cloudflare API, self-hosted solutions.

### Docker: Pros and Cons

**Pros:**
- Consistency between dev/test/prod
- Isolation between apps
- Lighter than traditional VMs
- Large community and ready-to-use images
- Easy to scale containers

**Cons:**
- Resource overhead vs running directly on host
- Kernel sharing = compromised app could affect system
- Persistent data adds complexity (can cause data loss for new users)
- Networking complexity
- **Bypasses UFW/firewalld** (only works with iptables directly)
- Monitoring/debugging across containers more complex

**Bottom line**: Great for testing and consistent deployments. For production, weigh complexity against benefits based on your needs

---

## Open WebUI - Self-Hosted LLM Interface

*Source: [open-webui/open-webui](https://github.com/open-webui/open-webui) - Added: 2026-01-18*

### What It Does

Extensible, user-friendly web interface for LLMs. Supports Ollama (local models) and OpenAI-compatible APIs. Operates entirely offline when paired with local models.

### Key Features

- **ChatGPT-like Interface**: Intuitive UI familiar to ChatGPT users
- **Responsive Design**: Works on desktop and mobile
- **Multi-Modal**: Images, voice input support
- **Local RAG**: Document interactions in chat (still in alpha)
- **Markdown/LaTeX**: Full support for enhanced formatting
- **Role-Based Access Control**: User management with model whitelisting
- **Webhook Integration**: Real-time notifications on user sign-ups
- **Offline Operation**: Runs entirely locally with Ollama

### Quick Start (Docker)

**Standard installation:**
```bash
docker run -d -p 3000:3000 \
  -v open-webui:/app/backend/data \
  --name open-webui \
  --restart always \
  ghcr.io/open-webui/open-webui:main
```

**With bundled Ollama (CUDA):**
```bash
docker run -d -p 3000:3000 \
  --gpus all \
  -v open-webui:/app/backend/data \
  --name open-webui \
  --restart always \
  ghcr.io/open-webui/open-webui:cuda
```

**With bundled Ollama (CPU only):**
```bash
docker run -d -p 3000:3000 \
  -v open-webui:/app/backend/data \
  --name open-webui \
  --restart always \
  ghcr.io/open-webui/open-webui:ollama
```

Access at `http://localhost:3000`

### Common Issue: Connection Error

If WebUI can't reach Ollama at 127.0.0.1:11434, use `--network=host`:

```bash
docker run -d --network=host \
  -v open-webui:/app/backend/data \
  -e OLLAMA_BASE_URL=http://127.0.0.1:11434 \
  --name open-webui \
  --restart always \
  ghcr.io/open-webui/open-webui:main
```

Note: Port changes from 3000 to 8080 with `--network=host`.

### Keeping Updated

```bash
docker run --rm \
  --volume /var/run/docker.sock:/var/run/docker.sock \
  containrrr/watchtower --run-once open-webui
```

### vs Other Self-Hosted LLM UIs

| Tool | Best For |
|------|----------|
| **Open WebUI** | ChatGPT-like experience, Ollama integration, feature-rich |
| **Onyx** | Enterprise features, RAG with 40+ connectors, airgapped environments |
| **text-generation-webui** | Power users, model loading/fine-tuning |
| **LM Studio** | Desktop app (not self-hosted), easy model management |

### When to Use

- Want a polished ChatGPT-like interface for local models
- Running Ollama and need a web UI
- Multi-user setup with access control
- Need offline LLM access

### Resources

- [Open WebUI Documentation](https://docs.openwebui.com/)
- [Open WebUI Community](https://openwebui.com/) - Custom modelfiles
- [Discord](https://discord.gg/openwebui) - Support and community

---

## PostHog - Self-Hosted Product Analytics

*Source: [PostHog/posthog](https://github.com/PostHog/posthog) - Added: 2026-01-18*

### What It Does

Open-source platform for product analytics, session recording, feature flagging, and A/B testing. Self-hostable alternative to Amplitude, Mixpanel, and LaunchDarkly.

### Key Features

- **Event-based Analytics**: Autocapture or manual event tracking
- **Session Replays**: Watch user behavior with console logs and network monitoring
- **Feature Flags**: Roll out features to specific users/cohorts, use as kill-switches
- **A/B Testing**: Multivariate experiments with automatic significance calculations
- **Surveys**: Customizable user feedback collection
- **Correlation Analysis**: Discover what events correlate with success/failure
- **SQL Access**: Direct data analysis beyond pre-built visualizations
- **Heatmaps**: Visual representation of user clicks via PostHog Toolbar
- **CDP (Customer Data Platform)**: Import/export data to external services

### Free Tier (Cloud)

Generous monthly free tier:
- 1 million product analytics events
- 5,000 session replays
- 1 million feature flag requests
- 250 survey responses

### Self-Hosted Deployment

**Hobby deploy (Docker, single server):**

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/posthog/posthog/HEAD/bin/deploy-hobby)"
```

Requirements: Linux with Docker, 4GB RAM recommended.

**Limitations:**
- Scales to ~100k events/month
- No customer support for self-hosted
- Recommended to migrate to PostHog Cloud for larger scale

### Data Integrations

**Built-in libraries:** JavaScript, Python, Ruby, Node, Go, Android, iOS, PHP, Flutter, React Native, Elixir, Nim, and REST API.

**Warehouse integrations:** BigQuery, Redshift, Snowflake, S3 for data export. Can import from warehouses via transformation plugins.

### When to Self-Host vs Cloud

**Self-host:**
- Privacy requirements (data stays on your infrastructure)
- Learning/experimentation
- Cost-sensitive with low event volume (<100k/month)
- Airgapped environments

**Cloud (recommended):**
- Higher event volumes
- Want managed infrastructure
- Need customer support
- SOC 2 compliance requirement (PostHog Cloud is compliant)

### Licensing

- **MIT license** for core repository
- **Enterprise features** in `/ee` directory have separate license
- **posthog-foss** repo available for 100% FOSS needs (purged of proprietary code)

### Comparison with Other Analytics

| Tool | Self-Hosted | Session Replay | Feature Flags | A/B Testing |
|------|-------------|----------------|---------------|-------------|
| **PostHog** | Yes | Yes | Yes | Yes |
| **Plausible** | Yes | No | No | No |
| **Umami** | Yes | No | No | No |
| **Matomo** | Yes | Yes (paid) | No | Yes (paid) |
| **Mixpanel** | No | No | No | Yes |

PostHog is unique in combining all these features in one self-hostable package.

### Why It Matters for Self-Hosters

Traditional analytics (Google Analytics, Mixpanel) send user data to third parties. PostHog gives you:
- Full control over user data
- GDPR/CCPA compliance by design
- No cookie consent nightmares (first-party data collection)
- Feature flags and A/B testing without separate services (LaunchDarkly, Optimizely)

---

## Jellyfin - Open Source Media Server

*Source: [Jellyfin 10.9.0 Release Notes](https://jellyfin.org/posts/jellyfin-release-10.9.0/) - Added: 2026-01-18*

### What It Does

Free, open-source media server. Self-hosted alternative to Plex without paid tiers or account requirements. Streams movies, TV shows, music, and photos to any device.

### Jellyfin 10.9.0 Key Changes

Major release with 1100+ pull requests merged. **Back up your data before upgrading.**

#### Breaking Changes

- **Ubuntu**: Only LTS versions supported (non-LTS dropped)
- **RPM Packages**: Official Fedora/CentOS/RHEL packages dropped - use RPMFusion or Docker instead
- **EasyPassword (PIN)**: Removed due to security risks - use full passwords
- **Docker**: GitHub Container Registry now available as alternative

#### Major Features Added

- **Trickplay**: Live video scrubbing with thumbnail previews
- **DLNA**: Moved to plugin system for improved support
- **Multiple Subtitles**: Web player now supports multiple subtitle tracks
- **New Image Formats**: AVIF and WEBP support for picture libraries
- **In-Process Restart**: Server can restart without full process restart

#### Transcoding Improvements

- New audio codec support
- Direct stream playback of DVD and BluRay data
- Enhanced hardware acceleration (Intel, AMD, NVIDIA)
- Upgraded to .NET 8 for better performance

### Docker Quick Start

```yaml
version: "3"
services:
  jellyfin:
    image: jellyfin/jellyfin:latest
    container_name: jellyfin
    network_mode: host
    volumes:
      - /path/to/config:/config
      - /path/to/cache:/cache
      - /path/to/media:/media:ro
    restart: unless-stopped
    # For hardware acceleration, add:
    # devices:
    #   - /dev/dri:/dev/dri  # Intel/AMD
```

Or via GitHub Container Registry:
```bash
docker pull ghcr.io/jellyfin/jellyfin:latest
```

### Jellyfin vs Plex

| Feature | Jellyfin | Plex |
|---------|----------|------|
| Cost | Free | Free tier + Plex Pass ($5/mo or $120 lifetime) |
| Account Required | No | Yes (cloud-dependent features) |
| Hardware Transcoding | Free | Plex Pass only |
| Live TV/DVR | Free | Plex Pass only |
| Skip Intro | Community plugin | Plex Pass only |
| Mobile Sync | Free | Plex Pass only |
| Development | Community-driven | Corporate |

**When to choose Jellyfin:**
- Want fully free, no-account-required solution
- Value privacy (no cloud dependency)
- Comfortable with community support
- Don't want to pay for features like hardware transcoding

**When to choose Plex:**
- Want polished UX out of the box
- Need better device/app compatibility
- Value commercial support
- Already have Plex Pass

### Client Apps

- **Web**: Built-in web interface
- **Android/iOS**: Official apps (free, no unlock needed unlike Plex)
- **Android TV**: Dedicated app
- **Roku**: Community-maintained
- **Kodi**: Jellyfin for Kodi add-on
- **Desktop**: Jellyfin Media Player (MPV-based)

### Release Cadence

10.9.0 was a long cycle (2+ years). Team aims for 10.10.0 within 6 months to establish faster release cadence.

### Community & Contributing

Over 100 contributors to 10.9.0. Project actively seeking frontend developers for design changes. Open-source, community-driven development.

---

## Traefik - Reverse Proxy Without Containers

*Source: [Why you should take a look at traefik, even if you don't use containers](https://j6b72.de/article/why-you-should-take-a-look-at-traefik/) - Added: 2026-01-18*

### What It Does

Traefik is a reverse proxy comparable to HAProxy (not nginx/caddy/apache2). It forwards requests to services and returns responses, can modify headers, but can't serve static files. Popular in homelab/container world but works great without containers.

### Common Misconceptions

**"Traefik needs containers"**: False. Written in Golang, compiles to a single binary. Download from releases page, run with systemd. No Docker required.

**"Traefik needs container labels for config"**: False. Supports full configuration via YAML files. Many find this cleaner than container labels anyway.

### Why It Works Well Without Containers

- **Single binary deployment**: Download, configure, run
- **Static + Dynamic config split**: Entrypoints and cert providers are "static"; routers/services/middlewares are "dynamic" and hot-reload on file changes
- **Excellent documentation**: Concepts explained clearly, config examples for each approach
- **Robust**: Warns about invalid configs, easy to understand request flow, minimal logging by default

### Key Features

**TLS Passthrough**: Forward traffic to services that handle their own TLS certs without terminating on proxy. Uses Server Name Indication (SNI) for routing since Host header is encrypted.

**PROXY Protocol**: HAProxy's protocol for securely transmitting client info (replaces X-Forwarded-* headers). More secure when configured properly. Requires target service support (apache2, nginx support it).

### Configuration Example

**Static config** (`/etc/traefik/traefik.yml`):

```yaml
providers:
  file:
    filename: /etc/traefik/dynamic.yml
    watch: true
entryPoints:
  https:
    address: :443
  http:
    address: :80
    http:
      redirections:
        entryPoint:
          to: https
          scheme: https
certificatesResolvers:
  le:
    acme:
      email: you@example.com
      storage: /etc/traefik/acme.json
      tlsChallenge: {}
```

**Dynamic config** (`/etc/traefik/dynamic.yml`):

```yaml
tcp:
  routers:
    nextcloud-router:
      rule: "HostSNI(`cloud.example.com`)"
      service: nextcloud
      entrypoints:
        - https
      tls:
        passthrough: true
  services:
    nextcloud:
      loadBalancer:
        servers:
          - address: 10.33.1.2:4433
        proxyProtocol:
          version: 2

http:
  routers:
    gitea:
      rule: "Host(`git.example.com`)"
      entrypoints:
        - https
      service: gitea
      middlewares:
        - noindex
      tls:
        certResolver: le
  middlewares:
    noindex:
      headers:
        customResponseHeaders:
          X-Robots-Tag: noindex, nofollow, nosnippet, noarchive
  services:
    gitea:
      loadBalancer:
        servers:
          - url: http://127.0.0.1:3000
```

### Limitations

**Authentication**: No built-in OAuth integration. Options:
- Keycloak (complex setup)
- traefik-forward-auth (abandoned, last update 2020)
- oauth2-proxy (adds another proxy layer)
- Roll your own ForwardAuth handler (Traefik's ForwardAuth is simple)

**User Agent / IP Blocking**: Only via third-party plugins or IPAllowList middleware workaround. Can't directly block specific IPs or user agents without plugins.

### Traefik vs Caddy

| Feature | Traefik | Caddy |
|---------|---------|-------|
| Static file serving | No | Yes |
| Config approach | YAML/TOML + providers | Caddyfile or JSON |
| Container integration | Excellent | Good |
| Non-container use | Good | Excellent |
| Automatic HTTPS | Yes | Yes |
| Complexity | Higher | Lower |

**Use Traefik when:**
- Already using containers and want auto-discovery
- Need TLS passthrough or PROXY protocol
- Want fine-grained middleware control

**Use Caddy when:**
- Serving static files + reverse proxy
- Want simplest possible config
- Don't need container integration

---

## Harbormaster - Lightweight Docker Compose Orchestrator

*Source: [harbormaster.readthedocs.io](https://harbormaster.readthedocs.io/en/latest/) - Added: 2026-01-18*

### What It Does

Small container orchestrator that runs multiple Docker Compose applications on a single host with automatic deploys/restarts by pushing to a git repo. Sits between raw Docker Compose and full PaaS solutions like Dokku.

### When to Use

Kubernetes too heavy? Dokku/Dokploy too opinionated? Harbormaster is the minimal option:
- Already have Docker Compose apps in git repos
- Want auto-deploy on git push without CI/CD setup
- Single server, multiple apps
- Don't need ingress management (bring your own)

### Quick Start

```bash
# Create config directory
mkdir mydir && cd mydir

# Create harbormaster.yml
cat > harbormaster.yml << 'EOF'
apps:
  hello_world:
    url: https://gitlab.com/stavros/harbormaster.git
    compose_config:
    - apps/hello_world/docker-compose.yml
EOF

# Run Harbormaster (no install needed)
docker run \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v $(pwd):/config \
    -v $(pwd):/main \
    stavros/harbormaster
```

Visit `http://localhost:8000` to see the hello world app.

### How It Works

1. Point Harbormaster at a git repo containing a `docker-compose.yml`
2. Harbormaster clones the repo and runs `docker compose up`
3. Periodically polls the repo for changes
4. Pulls and restarts containers on changes

### Data Persistence

Harbormaster provides environment variables for data directories:

```yaml
# In your docker-compose.yml
services:
  main:
    build: .
    volumes:
      - ${HM_DATA_DIR}/data:/app_data
      - ${HM_CACHE_DIR}/cache:/cache
```

- `${HM_DATA_DIR}` → `harbormaster-main/data/<appname>/`
- `${HM_CACHE_DIR}` → `harbormaster-main/cache/<appname>/`

All app data stays organized under Harbormaster's directory structure.

### Configuration

```yaml
apps:
  myapp:
    url: github.com/yourusername/myapp.git
    # Optional: specify compose file path
    compose_config:
    - docker-compose.yml
```

### Limitations

- **No ingress**: You must set up your own reverse proxy (Traefik, Caddy, nginx)
- **No secrets management**: Handle secrets yourself
- **Git-based only**: No direct image deployments

### vs Other Options

| Tool | Best For |
|------|----------|
| **Harbormaster** | Minimal orchestration, git-push deploys, compose files as-is |
| **Docker Swarm** | Single-server with compose, built-in networking |
| **Dokku** | Heroku-like git-push workflow, more features |
| **Dokploy** | Web dashboard, team features, one-click templates |

### When Harbormaster Shines

- You have 3-5 apps in separate repos, each with `docker-compose.yml`
- You want zero learning curve beyond Docker Compose
- You handle ingress separately (maybe Tailscale + Caddy)
- You want the simplest possible "push to deploy" setup

---

## HeyForm - Self-Hosted Form Builder

*Source: [heyform.net/self-hosting](https://docs.heyform.net/self-hosting) - Added: 2026-01-18*

### What It Does

Open-source form builder for surveys, questionnaires, and data collection. Typeform/Google Forms alternative.

### Quick Start (Docker Compose)

1. Create `docker.env` with environment variables (see [sample file](https://docs.heyform.net/self-hosting))

2. Create `docker-compose.yml`:

```yaml
version: "3"

services:
  heyform:
    image: heyform/community-edition:latest
    env_file: ./docker.env
    ports:
      - "8000:8000"
    depends_on:
      - mongo
      - redis

  mongo:
    image: mongo:4.4.29
    restart: "always"
    ports:
      - "27017:27017"

  redis:
    image: redis
    restart: "always"
    command: "redis-server --appendonly yes"
    ports:
      - "6379:6379"
```

3. Start: `docker-compose up -d`

4. Access at `http://<server-ip>:8000`

### Dependencies

- **MongoDB 4.4** - Data storage
- **Redis** - Caching/sessions

### SSL Note

HeyForm runs on unencrypted HTTP only. Put behind Caddy or NGINX for HTTPS.

### When to Use

- Need privacy-focused form collection
- Want to own your survey data
- Replacing Typeform/Google Forms/Tally

---

## Keycloak - Self-Hosted SSO/Identity Management

*Source: [Keycloak SSO with docker compose and nginx](https://du.nkel.dev/blog/2024-02-10_keycloak-docker-compose-nginx/) - Added: 2026-01-19*

### What It Is

Open-source identity and access management solution. Provides Single Sign-On (SSO) and centralized authentication for all your self-hosted services.

### Why Self-Host SSO

- Consolidate user management across all services
- Single login for everything
- Better security than managing passwords per-service
- Interoperable with major protocols: OpenID Connect (OIDC), OAuth 2.0, SAML

### Key Features

- **SSO Protocols**: OIDC, OAuth 2.0, SAML support
- **User Management**: Centralized user database
- **Theming**: Customizable login pages
- **Social Login**: Optional integration with Google, GitHub, etc.
- **2FA/MFA**: Built-in multi-factor authentication
- **Admin Console**: Web-based user/role management

### Architecture Pattern

Uses standard nginx reverse proxy setup:
- Nginx handles SSL termination (port 80/443)
- Forwards to Keycloak on localhost:8080
- Keycloak runs in rootless Docker namespace
- PostgreSQL backend for user data

```
Internet (443) → nginx → localhost:8080 → Keycloak Docker
                                        → PostgreSQL Docker
```

### Docker Compose Setup

**Directory structure:**
```bash
~/keycloak/
  docker/
    docker-compose.yml
    .env
    Dockerfile  # optional, for custom builds
  data/
    postgres16/  # persistent DB storage
```

**Minimal docker-compose.yml:**
```yaml
version: '3.8'

services:
  postgres:
    image: postgres:16
    volumes:
      - ../data/postgres16:/var/lib/postgresql/data
    environment:
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}

  keycloak:
    image: quay.io/keycloak/keycloak:latest
    environment:
      KC_DB: postgres
      KC_DB_URL: jdbc:postgresql://postgres/${POSTGRES_DB}
      KC_DB_USERNAME: ${POSTGRES_USER}
      KC_DB_PASSWORD: ${POSTGRES_PASSWORD}
      KC_HOSTNAME: ${KEYCLOAK_HOSTNAME}
      KC_PROXY: edge
      KEYCLOAK_ADMIN: ${KEYCLOAK_ADMIN}
      KEYCLOAK_ADMIN_PASSWORD: ${KEYCLOAK_ADMIN_PASSWORD}
    command: start
    depends_on:
      - postgres
    ports:
      - "127.0.0.1:8080:8080"
```

**Required .env variables:**
```bash
POSTGRES_DB=keycloak
POSTGRES_USER=keycloak
POSTGRES_PASSWORD=<strong-password>
KEYCLOAK_HOSTNAME=sso.yourdomain.com
KEYCLOAK_ADMIN=admin
KEYCLOAK_ADMIN_PASSWORD=<strong-admin-password>
```

### Nginx Configuration

```nginx
server {
    server_name sso.yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-Host $host;
        proxy_set_header X-Forwarded-Port $server_port;
    }

    listen 443 ssl;
    ssl_certificate /etc/letsencrypt/live/sso.yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/sso.yourdomain.com/privkey.pem;
}
```

Get SSL certificate:
```bash
certbot --nginx -d sso.yourdomain.com
```

### Customization with Dockerfile

For themes or optimized mode, build custom image:

```dockerfile
FROM quay.io/keycloak/keycloak:latest as builder

# Enable health and metrics
ENV KC_HEALTH_ENABLED=true
ENV KC_METRICS_ENABLED=true

# Configure database
ENV KC_DB=postgres

WORKDIR /opt/keycloak

# Custom theme (optional)
# COPY theme-name/ /opt/keycloak/themes/theme-name/

# Build optimized image
RUN /opt/keycloak/bin/kc.sh build

FROM quay.io/keycloak/keycloak:latest
COPY --from=builder /opt/keycloak/ /opt/keycloak/

ENTRYPOINT ["/opt/keycloak/bin/kc.sh"]
```

Update docker-compose.yml:
```yaml
keycloak:
  build: .
  command: start --optimized
  # ... rest of config
```

### Quick Start

1. **Create user and directories:**
   ```bash
   sudo useradd -m -d /srv/keycloak keycloak
   sudo -u keycloak bash
   cd ~
   mkdir -p data/postgres16 docker
   cd docker
   ```

2. **Create .env and docker-compose.yml** (see above)

3. **Test locally:**
   ```bash
   docker compose up
   # Open http://localhost:8080 in browser
   ```

4. **Set up nginx** (see config above)

5. **Get SSL certificate:**
   ```bash
   sudo certbot --nginx -d sso.yourdomain.com
   ```

6. **Access admin console:**
   - URL: https://sso.yourdomain.com
   - Username: admin (from .env)
   - Password: (from .env)

### Post-Setup

1. **Configure email** in admin console (Realm Settings → Email)
2. **Create a realm** for your services (e.g., "homelab")
3. **Add clients** for each service you want to integrate
4. **Configure users/roles** as needed

### Integration with Services

Services that support OIDC/OAuth2 can authenticate via Keycloak:
- Immich (photo management)
- Nextcloud (file storage)
- Grist (spreadsheets)
- Gitea (git hosting)
- Any app supporting OAuth2/OIDC

Each service becomes a "client" in Keycloak with its own redirect URLs.

### Theming

Use [Keycloakify](https://www.keycloakify.dev/) to create custom login page themes. Add to Dockerfile before build step.

### Debugging

**View logs:**
```bash
docker compose logs -f keycloak
docker compose logs -f postgres
```

**Check nginx:**
```bash
sudo tail -f /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log
```

**Access database:**
```bash
docker compose exec postgres psql -U keycloak
```

### When to Use

- You have 3+ self-hosted services needing authentication
- Tired of managing separate passwords for each service
- Want centralized user management
- Need SSO for family members accessing services
- Want to add OAuth2/OIDC to custom apps

### Resources

- [Official Keycloak Docs](https://www.keycloak.org/documentation)
- [Keycloak on Containers Guide](https://www.keycloak.org/server/containers)
- [Keycloakify Theming](https://www.keycloakify.dev/)
