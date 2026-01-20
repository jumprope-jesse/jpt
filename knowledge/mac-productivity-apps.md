# Mac Productivity Apps

## Web-to-App Converters

### Coherence X5
**URL:** https://www.bzgapps.com/coherence
**Status:** Evaluating / Running

Transforms websites into standalone Mac apps. Instead of running in a cluttered browser window, sites become standalone, lightweight apps — isolated for focus and security, yet powered by Chrome's speed and flexibility.

**Key Features:**
- Creates true Mac apps from URLs (not just browser shortcuts)
- Each app can have its own extensions, profiles, and settings
- Supports multiple Chromium-based browsers (Chrome, Edge, Brave, etc.)
- Two app modes:
  - **Standard apps**: Single, distraction-free window
  - **Tabbed apps**: Full browser with tab support (good for grouping related tools like Gmail, Calendar, Drive)
- **Link Forwarding**: Control which links open in app vs default browser
- Proper Dock behavior (click icon reopens/launches correctly)
- Icon customization tools
- App library management

**Use Cases:**
- Isolate work Gmail from personal Gmail
- Create dedicated apps for self-hosted services (Plex, TrueNAS, Proxmox)
- Make web apps like Office 365, Miro feel native
- Maintain work/home boundaries by isolating apps
- Works with USB Yubikey for MFA

**Related:** BZG also makes "Unite" for Safari-based web apps

**Built for:** macOS 26 Tahoe

## Window Layout Managers

### Spencer
**URL:** https://macspencer.app/
**Status:** Evaluating / Running

Save and restore window layouts on Mac—switch between task contexts without losing window positions.

**Key Features:**
- Save named workspace layouts (window positions, sizes, app visibility)
- Restore layouts with a single shortcut
- Hide non-essential apps while working
- Create custom profiles for different contexts (coding, meetings, personal)

**Use Cases:**
- Switch between "deep work" coding layout and "meetings" layout
- Restore workspace after laptop undock/redock
- Quickly hide distractions when switching focus
- Different setups for different projects or clients

## Troubleshooting / Performance

### Electron App Lag Detection (macOS Tahoe)
**Source:** https://gist.github.com/tkafka/e3eb63a5ec448e9be6701bfd1f1b1e58
**Affects:** macOS 15.0+ (Tahoe)

Certain outdated Electron versions contain code (`_cornerMask`) that causes significant system-wide lag on macOS Tahoe.

**Fixed Electron Versions:**
- 36.9.2+, 37.6.0+, 38.2.0+, 39.0.0+, and all versions above 39

**Detection Scripts:**
1. **Version-based detection** - Scans `/Applications`, `/System/Applications`, `~/Applications` for Electron apps and checks version numbers
2. **Binary pattern detection** - More reliable; searches Electron Framework binaries for the actual `_cornerMask` code pattern

**Temporary Workaround:**
```bash
# Disables window shadows (less polished look) but stops the bug
launchctl setenv CHROME_HEADLESS 1
```

For persistence across reboots, create a launch agent.

**Tracking Resources:**
- Avarayr's shamelectron dashboard - tracks affected/fixed apps
- GitHub issue: electron/electron#48311

## Diagramming / ASCII Art

### Monodraw
**URL:** https://monodraw.helftone.com/
**Status:** Running

ASCII art editor for creating text-based diagrams, flowcharts, and visual representations that work anywhere text does (code comments, READMEs, Slack, etc.).

**Key Features:**
- Native macOS ASCII art editor
- Create diagrams that render in any monospace font environment
- Command line tool included (website purchase only, not App Store version due to sandbox restrictions)
- No data collection / privacy-focused

**Requirements:**
- macOS 11 Big Sur or later
- Legacy version (v1.3) available for macOS 10.10 Yosemite

**Purchasing Notes:**
- Direct purchase from website includes CLI tool
- App Store version lacks CLI due to sandbox restrictions
- Educational pricing available on request

**Use Cases:**
- ASCII diagrams in code comments
- Text-based flowcharts in README files
- Architecture diagrams that work in terminals
- Documentation that doesn't require image rendering

## Clipboard & Bookmark Management

### DoubleMemory
**URL:** https://doublememory.com/
**Status:** Evaluating
**Platforms:** macOS, iOS

Offline-first clipboard history and bookmark manager with a visual Pinterest-style board layout. No accounts, no servers, no tracking.

**Key Features:**
- **⌘ + C + C capture**: Double-tap Command+C to save anything system-wide
- **⌘ + ⇧ + Space search**: Instant recall from anywhere
- **Offline-first**: Works without internet, syncs via iCloud when online
- **No registration**: Uses Apple ID, no extra accounts needed
- **Visual board**: Pinterest-like waterfall layout for saved content
- **Apple-native**: Built specifically for Apple devices, uses CloudKit
- **5× less memory** than Electron-based alternatives

**Capture Methods:**
- Double ⌘ + C
- Drag and drop
- Right-click → Services menu
- Share extensions

**Supported Content:**
- Text and links from any app
- Rich previews for Amazon, Spotify, Reddit, TikTok, etc.

**Planned Features (Roadmap):**
- Auto-importers (Safari Reading List, Twitter Bookmarks)
- Auto-tagging
- Image-to-text OCR (on-device)

**Privacy:**
- No accounts or servers
- No tracking
- Data stays on device + personal iCloud

**Note:** Pocket (Mozilla) shutting down July 8, 2025 - DoubleMemory offers migration tools

## Menu Bar Management

### Native Notch Workaround (MacBook Pro 14"/16")
**Source:** https://flaky.build/native-fix-for-applications-hiding-under-the-macbook-pro-notch
**Status:** Free native solution
**Requirements:** macOS with Terminal access

Free command-line solution to prevent menu bar icons from hiding behind the MacBook Pro notch. Adjusts spacing/padding to fit more icons without installing third-party apps like Bartender.

**Commands:**
```bash
# Reduce spacing to fit more icons (values 0-6, lower = tighter)
defaults -currentHost write -globalDomain NSStatusItemSelectionPadding -int 6
defaults -currentHost write -globalDomain NSStatusItemSpacing -int 6

# Log out and log back in for changes to take effect
```

**Revert to defaults:**
```bash
defaults -currentHost delete -globalDomain NSStatusItemSelectionPadding
defaults -currentHost delete -globalDomain NSStatusItemSpacing

# Log out and log back in
```

**Results:**
- Default: ~13 apps visible
- With spacing set to 6: Several more icons fit
- Adjust values 0-6 to personal preference (6 is a good balance)

**Why This Matters:**
Apple hasn't automatically adjusted menu bar icon spacing for notch models, causing icons to hide. This free solution avoids paying ~$20 for Bartender when you only need basic spacing adjustments.

**Complementary Tool:** Use with Ice (below) for full menu bar control—Ice for show/hide animations and organization, native spacing tweak for maximum visible icons.

### Ice
**URL:** https://github.com/jordanbaird/Ice
**Status:** Running
**License:** MIT (open source)
**Requirements:** macOS 14+

Powerful menu bar manager for macOS. Hides/shows menu bar items with smooth animations and provides extensive customization.

**Installation:**
```bash
brew install jordanbaird-ice
```

**Key Features:**
- **Item management**: Hide menu bar items, drag-and-drop reordering, custom spacing
- **"Always Hidden" section**: Items that stay hidden unless explicitly shown
- **Show triggers**: Hover over menu bar, click empty area, or scroll/swipe
- **Auto rehide**: Automatically hide items after a delay
- **Separate bar for hidden items**: Useful for MacBooks with notch
- **Application menu handling**: Hide app menus when they overlap with shown items

**Appearance Customization:**
- Menu bar tint (solid and gradient)
- Shadow effects
- Border styling
- Custom shapes (rounded, split)

**Hotkeys:**
- Toggle individual sections
- Toggle application menus
- Show/hide divider icons
- Temporarily show specific items
- Enable/disable auto rehide

**Why "Ice"?**
Menu bar items "slide away" like ice 🧊

**Note:** Requires macOS 14+ due to reliance on newer system APIs.

## Media Controls (Menu Bar)

### SoundSeer
**URL:** https://github.com/jonathangarelick/SoundSeer
**Status:** Running
**Platforms:** macOS 13+
**Availability:** Mac App Store

Simple menu bar app that displays currently playing Spotify track with quick controls.

**Key Features:**
- Shows currently playing song in menu bar
- Skip track controls
- Direct links to song/artist/album in Spotify
- Copy URL for sharing

**Use Cases:**
- Quick Spotify control without switching windows
- Share what you're listening to
- Minimal alternative to full Spotify window

**Note:** Pairs well with Ice (menu bar manager) to show/hide when needed.

## Status Bar Enhancements

### DynamicLake
**URL:** https://www.dynamiclake.com/
**Status:** Not started
**Author:** Aviorrok

Brings Apple's Dynamic Island concept to Mac. Displays contextual status information in a notch-like UI element.

**Technical Notes:**
- Uses FFmpeg (LGPLv3.0 licensed)
- Source code available

**Use Cases:**
- Visual status indicators for running processes
- Media playback controls in a compact UI
- Timer/notification integration

## App Launchers

### Monarch
**URL:** https://www.monarchlauncher.com/
**Status:** Evaluating
**Pricing:** $20 one-time (Luna license - lifetime updates), $30 after v1.0

Spotlight-replacement launcher with integrated calculator, clipboard history, notes, and more. Privacy-focused (no telemetry, no data collection).

**Key Features:**
- **App launcher**: Open/quit apps via ⌥ Space
- **Calculator**: Natural language math, date calculations, timezone comparisons, unit/currency conversion
- **Clipboard history**: Unlimited, searchable, filterable by app/content type, renameable items
- **Monarch Notes**: Quick notes with markdown, ⌘ + dot from anywhere (works with Obsidian)
- **Browser bookmarks**: Access bookmarks with control over how/where they open
- **System controls**: Access macOS settings, hide apps, lock screen, volume/mic control
- **Superlinks**: Custom commands for any website/app with dynamic values
- **Color picker**: Search by hex/RGB
- **Emoji picker**: Type `:fire` to get 🔥

**Design Philosophy:**
- One hotkey (⌥ Space) to access everything
- Tab to switch between UI modes
- Works out of the box, no configuration required
- Hide irrelevant results with ⌘ H

**Privacy:**
- No VCs, no subscriptions
- No telemetry or data collection
- No login required
- Only external request is license validation

**Comparison to Raycast/Alfred:**
- Simpler, more focused feature set
- One-time purchase vs subscription
- Privacy-first approach
- Designed to change UI based on task at hand (not a command palette)

**Luna License (v0.x):**
- Special early-adopter license with free upgrades forever
- Limited availability - ends when v1.0 releases

## Video Presentation & Production

### CueCam Presenter
**URL:** https://cuecam-presenter.com/
**Status:** Not started
**Platforms:** macOS (with iPhone/iPad companion apps)
**Pricing:** Suite plan includes Shoot Pro and Video Pencil

Professional video presentation tool that transforms Mac, iPhone, and iPad into a polished production studio. Creates a virtual camera and microphone for bringing content into video calls without screen sharing.

**Core Concept:**
Replaces traditional screen sharing with a virtual camera feed that combines your webcam, content, teleprompter, and media—giving OBS-level production quality without complex configuration.

**Key Features:**
- **Virtual camera & mic**: Works with Zoom, Teams, Google Meet, etc.
- **Smart scripts**: Plan presentations with cue cards, slides, videos, screen shares
- **Built-in teleprompter**: Always see your notes without breaking eye contact
- **Zero configuration**: Best practices baked in, works immediately
- **Portable scripts**: Share projects including videos/images (no export/import hassle)
- **Editless production**: Present directly to camera, skip video editing
- **Multi-device integration**: iPhone as camera+teleprompter, iPad for drawing/annotations

**Companion Apps (Suite Plan):**
1. **Shoot Pro (iPhone/iPad)**
   - Use iPhone (2015+) as external camera
   - Mirror Mac windows to iPhone screen
   - See presenter notes while maintaining eye contact
   - Functions as production monitor and teleprompter

2. **Video Pencil (iPad)**
   - Draw, point, zoom on content in real-time
   - See exactly what you're sharing
   - Remote control for Mac presentation
   - Live titles and telestrator features

**Use Cases:**
- **Teaching**: Quick educational presentations with mixed media
- **Sales demos**: Product walkthroughs with teleprompter for key talking points
- **Client presentations**: Polished design reviews with annotations
- **Sports coaching**: Game film analysis with drawing tools
- **Recorded videos**: Present to camera with structure, skip editing entirely

**Why It's Different:**
- No screen share permissions needed (it's your camera)
- Audience always sees you looking at them (via iPhone teleprompter)
- Seamlessly switch between content types (slides, video, screen, camera)
- Add YouTube videos with audio to calls
- ChatGPT script generation integration

**Technical Notes:**
- Requires separate hardware for best experience (iPhone, iPad)
- Works with older iPhones (2015+)
- Revives old Apple devices as production equipment

**Community Support:**
- Discord server
- YouTube channel with tutorials
- Weekly live Q&A with founder Michael Forrest
- User guide documentation

**Comparison to Alternatives:**
- **vs OBS**: Much simpler, no configuration, integrated teleprompter
- **vs Screen Share**: Cleaner presentation, no browser tabs/notifications visible, maintains eye contact
- **vs Zoom/Teams native**: Professional production quality, multiple camera angles, scripted presentations

**Note:** Particularly useful for anyone doing regular video calls, presentations, teaching, or content creation. The teleprompter + eye contact feature (via iPhone) is the killer feature—makes you appear naturally engaged while following detailed notes.

## Voice Memos & Transcription

### Cleft Notes
**URL:** https://www.cleftnotes.com/
**Status:** Not started
**Platforms:** macOS, iOS (TestFlight), visionOS
**Pricing:** Desktop $30/year, Cloud AI $5/month (both free for limited time)

Voice memo app that transforms spoken thoughts into AI-optimized, shareable notes. Focused on quick idea capture without typing.

**Key Features:**
- **Voice-to-notes**: Record voice memos, get organized summaries
- **AI optimization**: Uses OpenAI for transcription and summarization
- **BYOK option**: Bring your own OpenAI key + on-device transcription (Desktop license)
- **Cloud sync**: Multi-device sync for notes across Mac/iOS/Vision Pro
- **Sharing**: Easily share processed notes

**License Tiers:**
1. **Desktop License ($30/year)**
   - Native macOS app
   - Bring your own OpenAI key
   - On-device transcription
   - 1 year of updates

2. **Cleft Cloud AI ($5/month)**
   - Optimized AI & transcription (no API key needed)
   - Cloud sync across devices
   - iOS & Vision Pro apps

**Use Cases:**
- Capture ideas while walking/commuting
- Async communication without typing
- Meeting notes and planning
- Personal ideation and brainstorming

**Note:** Not a collaboration tool or shared knowledge base—focused on personal note capture.

## Note-Taking & Knowledge Management

### AFFiNE
**URL:** https://affine.pro/
**GitHub:** https://github.com/toeverything/AFFiNE
**Status:** Not started
**Platforms:** macOS, Windows, Linux, Web
**Pricing:** Free (self-hosted), Cloud plans available
**License:** Open source

All-in-one knowledge operating system combining documents, whiteboards, and databases. Positioned as an open-source alternative to Notion with AI capabilities.

**Key Features:**
- **Documents**: Rich text editing with Markdown support
- **Whiteboards (Edgeless Mode)**: Infinite canvas for drawing, diagramming, brainstorming
- **Databases**: Structured data management (Notion-style)
- **Local-first**: Works offline with local workspace option
- **AI Assistant**: Inline AI for writing, drawing, and presenting
- **Open source**: Self-hostable, data ownership

**AI Features:**
- Inline AI assistant in page mode
- AI assistance in edgeless/whiteboard mode
- Free trial available

**Related Projects:**
- BlockSuite (editor framework)
- OctoBase (local-first database)

**Comparison to Notion:**
- Open source vs proprietary
- Local-first vs cloud-first
- Integrated whiteboard vs separate tools
- Self-hostable option

### Agenda
**URL:** https://agenda.com/
**Status:** Not started
**Platforms:** macOS, iOS, iPadOS
**Pricing:** Free with optional Premium features

Date-focused note-taking app that integrates with calendar events. Unique approach of organizing notes into a timeline rather than just folders.

**Key Features:**
- **Timeline organization**: Notes ordered chronologically, linked to past/present/future
- **Calendar integration**: Attach notes directly to calendar events
- **"On the Agenda" status**: Mark notes as active for quick access
- **Styled-text editing**: Rich text with headings, lists, tables, tags—Markdown-style input with polished output
- **Reminders integration**: Add reminders to tasks, view alongside calendar in unified timeline
- **Sharing**: Encrypted note sharing with others, integrates with Messages "Shared with You"
- **iCloud/Dropbox sync**: Notes stay on personal cloud, not Agenda's servers
- **Templates & automation**: Callback links, actions for power users
- **Apple Pencil support**: Draw directly in notes on iPad

**Export Formats:**
- PDF, RTF, Markdown
- Agenda archive format for exact duplication

**Use Cases:**
- Meeting notes linked to calendar events
- Project tracking with timeline view
- Daily planning with calendar context
- Shared notes for collaboration (grocery lists, vacation planning)

**Privacy:**
- Notes stored in personal iCloud/Dropbox only
- End-to-end encrypted sharing
- No access by Agenda to user data

**Languages:** English, Dutch, French, German, Italian, Spanish, Polish, Portuguese, Russian, Chinese, Afrikaans

**Requirements:** macOS 10.14+ / iOS 13+ / iPadOS 13+

## macOS Sequoia Features & Quirks

### Built-in Window Tiling (macOS 15+)
**Status:** Available

Apple added simple window tiling similar to Windows:
- Drag windows to edges/corners to snap to half or quarter of screen
- Hold Option while dragging to see placement preview immediately
- Click+hold green button for quick arrangement options
- Keyboard shortcuts via Globe key (Apple keyboards only)
- Windows return to previous size/shape when dragged back out

**Limitations:**
- Only halves and quarters (no thirds)
- Globe key shortcuts require Apple keyboard
- No keyboard shortcuts for quarter-screen tiling

For more control, use third-party tools like Moom.

### iPhone Mirroring
**Status:** Available

View and control iPhone from Mac via Continuity:
- iPhone stays locked (Lock Screen or StandBy mode)
- Mac keyboard/trackpad work as expected, including swipes
- Touch ID on Mac handles authentication
- Audio plays through Mac speakers
- iPhone notifications appear on Mac, clicking launches iPhone Mirroring

**Gotchas:**
- Requires Bluetooth range initially, then uses Wi-Fi
- Can't force rotation (only auto-rotates when app requires it)
- Video playback may be blocked (DRM)
- Initial connection can be finicky

### Passwords App
**Status:** Available

Full password manager extracted from Settings/Keychain Access:
- Cross-platform: Mac, iOS, iPadOS, visionOS, Windows (via iCloud)
- Shows web logins, Wi-Fi passwords, TOTP codes, Passkeys
- Group sharing with unlimited arbitrary groups
- Drag items to groups in sidebar to share

**Limitations vs 1Password:**
- No secure notes (use Notes app instead)
- No credit cards (use Wallet settings)
- No catch-all for passport numbers, serial numbers, SSH keys
- Large imports can be slow/unreliable (may duplicate items)

### Security UX Friction (Unsigned Apps)
**Source:** Six Colors macOS Sequoia review
**Status:** Current behavior

Opening unsigned/non-notarized apps now requires 5+ steps:

1. Double-click app → "Apple could not verify" warning → only options are Done or Trash
2. Open Settings → Privacy & Security → scroll to bottom → find "[App] was blocked"
3. Click "Open Anyway" button
4. Return to Finder, double-click app again
5. Another warning dialog → choose "Open Anyway" again
6. Admin authentication required
7. Finally launches

**Note:** This repeats after app updates. The old right-click → Open shortcut no longer works.

**Workaround for developers:** Get apps notarized through Apple's process.

**Philosophy:** Apple prioritizing security over usability. The friction is intentional to discourage running unsigned software.

## RSS Readers & Feed Aggregators

### Project Tapestry (Iconfactory)
**URL:** https://www.kickstarter.com/projects/iconfactory/project-tapestry
**Status:** In development (Kickstarter funded)
**Platforms:** iOS (iPad/iPhone), macOS (stretch goal at $250K)
**Developer:** Iconfactory (makers of Twitterrific, Linea Sketch)

Universal chronological timeline app that aggregates content from multiple social media and information sources into a single, algorithm-free feed.

**Key Features:**
- **Unified timeline**: All sources in chronological order, no algorithmic curation
- **Service-agnostic**: Works with any publicly available data source
- **Plugin architecture**: JavaScript-based plugins translate between native app and web services
- **Custom plugins**: Build your own data source connectors (e.g., Raspberry Pi sensors)
- **Open to apps**: Click through to engage/reply in your preferred dedicated app
- **Reading position memory**: Remembers where you left off

**Supported Sources:**
- ✅ Mastodon, Tumblr, Bluesky, Micro.blog
- ✅ Any RSS feed (blogs, news)
- ✅ USGS Earthquakes, NOAA Satellite
- ✅ GO Comics
- ✅ Custom sources via plugin API

**NOT Supported (walled gardens):**
- ❌ Facebook, Instagram, Threads, Twitter/X

**Stretch Goals (Kickstarter):**
- $150K: Muffling/muting, plugin sharing mechanism
- $175K: Advanced filtering, search, bookmarking
- $250K: Native macOS support, activity overview/summary feature

**Use Cases:**
- Consolidate fragmented social media consumption
- See chronological view across platforms
- Complement (not replace) dedicated apps like Ivory, NetNewsWire
- Focus attention without algorithm manipulation

**Philosophy:**
- Community-funded (no VC)
- User-centered approach
- Overview app, not a posting/engagement tool

**Team:** Craig Hockenberry (code), Sean Heber (code), Gedeon Maheux, Dave Brasgalla, Talos Tsui, Anthony Piraino (design), Cheryl Cicha (PM)

**Note:** From the creators of Twitterrific—experienced team with 25+ years of iOS/Mac development. Expected 9-12 month development timeline from funding.

### Unread
**URL:** https://www.goldenhillsoftware.com/unread/
**Status:** Not started
**Platforms:** macOS, iOS, iPadOS
**Developer:** Golden Hill Software (Jared Sinclair)

Beautifully designed RSS reader focused on typography and distraction-free reading. Praised by Daring Fireball, MacStories, and other notable Apple bloggers.

**Key Features:**
- **Syncing Options**:
  - Unread Cloud (free, Sign in with Apple)
  - Third-party: Feedbin, Feedly, Fever-compatible, Inoreader, NewsBlur
  - Local accounts (no sync)
- **Automatic Full-Text**: Retrieves full articles from feeds that only provide summaries
- **Offline Caching**: Pre-caches webpage text and images (Premium)
- **Home Screen Widgets**: Recent articles, unread counts by feed/folder
- **Color Themes**: Multiple themes for different lighting conditions (light/dark mode)
- **Link Article Support**: Shows full text of both link post and quoted article (Daring Fireball style)
- **Full Keyboard/Trackpad Support**: iPad power user friendly

**Share Extensions:**
- **Subscribe in Unread**: Subscribe to feeds from any browser
- **Save to Unread**: Create articles from any webpage (Premium)

**Premium Features** (subscription):
- Caching for offline access
- Save to Unread share extension
- 32 custom app icons
- Article actions: Instapaper, Pinboard, Plinky, Pocket, Raindrop.io, Readwise, Safari Reading List, email, iMessage
- Widget customization
- Priority support
- Family Sharing supported

**Testimonials:**
- "A really great native experience... really fast" — Niléane, MacStories
- "An RSS reader made with taste" — David Sparks, MacSparky
- "Focused on eliminating chrome — it is a pure reading app" — John Gruber, Daring Fireball
- "Not only a pleasure to use visually but also from a VoiceOver perspective" — Ernest Rudak, Just Text

**Why Consider:**
- Native AppKit on Mac (not Electron/Catalyst)
- Typography-focused reading experience
- Works with existing RSS services (Feedbin, Feedly)
- Strong accessibility support (VoiceOver)
- Integrates with Readwise for spaced repetition/highlighting

**Related:** knowledge/feedsmith-feed-parser.md (if building RSS tools)

## Apple Native Productivity Stack

### Reminders + Numbers + Notes (as Notion Alternative)
**Source:** [Joan Westenberg - Medium](https://medium.com/the-realist/how-i-replaced-notion-with-reminders-numbers-and-notes-38282543b29b)
**Status:** Reference only (using Notion-based system)

Some users replace Notion with Apple's built-in trio:

**Advantages:**
- No subscription cost
- Native iCloud sync across all Apple devices
- Seamless integration between apps
- Data stays in Apple ecosystem (better privacy/control)
- No risk of third-party service discontinuation (Evernote cautionary tale)

**App Roles:**
- **Reminders**: Task management, lists, due dates
- **Numbers**: Databases, tracking, spreadsheet-style data
- **Notes**: Documentation, reference material, rich text

**Considerations:**
- Works best if fully in Apple ecosystem
- Less flexible than Notion's database/relation features
- No API access for automation (vs Notion's API)
- Simpler but less powerful for complex workflows

**Relevance:** Interesting minimalist alternative, but current system relies heavily on Notion API integration (tasks, agent automation, meeting sync). Native apps would break those workflows.

## Screen Recording & Memory

### Unlost
**URL:** https://unlost.ai/
**Status:** Not started
**Platforms:** macOS (Apple Silicon M1/2)

Screen capture and intelligent recall tool. Records your screen activity and lets you search through it with natural language. Alternative to Rewind AI with focus on privacy and intelligent capture.

**Key Features:**
- **Intelligent recording**: Understands screen layout and content (not just pixels)
- **Natural language search**: Query like "user interview questions from last week @chrome"
- **App/site filtering**: Exclude specific apps, websites, or pause entirely
- **Meeting transcript search**: Works with Zoom, Google Meet, Teams (web and native)
- **OCR/text extraction**: Crop areas from screenshots to copy text
- **Privacy respecting**: Auto-stops when copyright content detected (Netflix, etc.)

**Privacy & Security:**
- **Local-first**: All data collection, processing, and storage on-device
- **Offline capable**: Works without internet
- **Minimal data collection**: Only collects email address
- **Default exclusions**: Password managers and private browsers excluded automatically
- **User control**: Full control over what gets captured

**Access:**
- Quick search: Configurable keyboard shortcut
- Operates in background, discreetly

**Comparison to Rewind AI:**
- Similar core concept (screen memory + search)
- Emphasis on privacy/local processing
- Intelligent content understanding (not just screen recording)
- Free tier available (Rewind has moved toward paid model)

**Use Cases:**
- "What was that link I saw yesterday?"
- Recall meeting discussions without note-taking
- Find information seen in any app
- Search across browser tabs by content

**Note:** Privacy-conscious alternative for those wary of cloud-based screen recording services. Good fit for security-minded users who want recall capabilities.

## Time Tracking

### Unnamed Time Tracking Menubar App
**Source:** https://www.reddit.com/r/macapps/s/NbByCnWy6b
**Status:** In development (Feb 2024)
**Author:** Small utility developer in r/macapps

Time tracking menubar app for Mac inspired by Rewind AI. Details sparse as of Feb 2024, but creator seeking beta testers from community.

**Known Features:**
- Menubar utility for time tracking
- Inspired by Rewind AI's approach (likely automated tracking vs manual entry)

**Development Status:**
- Posted to r/macapps Feb 17, 2024
- Creator soliciting feedback and testers
- No public release yet

**Note:** Monitor r/macapps for updates if interested in lightweight time tracking alternatives to RescueTime/Timing.

## Mac App Store CLI

### mas
**URL:** https://github.com/mas-cli/mas
**Homebrew:** https://formulae.brew.sh/formula/mas
**Status:** Running
**License:** MIT

Command-line interface for the Mac App Store. Enables scripted installation, updates, and management of Mac App Store apps—essential for automated Mac setup and maintenance.

**Installation:**
```bash
brew install mas
```

**Requirements:**
- macOS
- Xcode >= 12.0 (build dependency)

**Key Commands:**
```bash
mas search <query>      # Search for apps
mas list                # List installed apps
mas install <app_id>    # Install by App Store ID
mas upgrade             # Upgrade all outdated apps
mas outdated            # List apps with pending updates
mas signin              # Sign in to App Store (if needed)
mas account             # Show signed-in Apple ID
```

**Use Cases:**
- **Dotfiles/setup scripts**: Install Mac App Store apps via Homebrew Bundle or shell scripts
- **New Mac setup**: Script the installation of all your paid apps
- **Automated updates**: Run `mas upgrade` in a cron job or LaunchAgent
- **App ID lookup**: Find App Store IDs for scripting

**Example (Brewfile integration):**
```ruby
# In your Brewfile
mas "1Password", id: 1569813296
mas "Things 3", id: 904280696
mas "Xcode", id: 497799835
```

**Tip:** App IDs are visible in App Store URLs (e.g., `apps.apple.com/app/id1569813296`)

## System Monitoring

### iPulse
**URL:** https://ipulseapp.com/
**Status:** Evaluating
**Platforms:** macOS

System monitoring app that provides real-time visual feedback on Mac performance metrics. Displays CPU, memory, network, disk activity, and other system stats in customizable widgets.

**Key Features:**
- Real-time system monitoring (CPU, RAM, disk, network)
- Customizable visual displays (graphs, gauges, meters)
- Menu bar or desktop widget placement
- Low resource footprint
- Native macOS integration

**Use Cases:**
- Monitor system performance during development
- Track resource usage of running apps
- Keep an eye on network activity
- Identify performance bottlenecks
- System health at-a-glance

**Note:** Alternative to Activity Monitor with more visual/customizable interface. Useful for developers and power users who want persistent system stats visible.

## Text Editors

### BBEdit
**URL:** https://www.barebones.com/
**Status:** Not started
**Version:** 15.0 (major release, March 2024)
**Platforms:** macOS
**Developer:** Bare Bones Software

Professional text editor for macOS designed for developers and content creators working with code, markup languages, and text documents. Long-standing Mac-native editor with deep system integration.

**Key Features (15.0 Release):**
- **Project Management**: Projects as top-level items with Workspace settings for functional root directories
- **Git Integration**: Push/pull branches, improved revision navigation
- **ChatGPT Worksheets**: Built-in conversational interface with ChatGPT API, history preservation, customizable models
- **Minimap Palette**: Scaled-down document view for navigation and selection management
- **Text Merge Command**: Batch text transformations using grep patterns + substitution tables
- **Language Protocol Server**: Improved LSP integration for modern development workflows
- **FTP/SFTP**: Identity file support for secure file transfers
- **Cheat Sheets**: Quick reference system
- **Accessibility**: Enhanced VoiceOver and accessibility support

**Use Cases:**
- Code editing with LSP support
- Text processing and batch transformations (grep-based workflows)
- Git-integrated development projects
- AI-assisted coding (ChatGPT integration)
- Remote file editing (FTP/SFTP)
- Markup language editing (HTML, Markdown, XML)

**Why BBEdit:**
- Native macOS app (not Electron)
- Decades of refinement (first released 1992)
- Advanced text manipulation tools (grep, text factories)
- Tight system integration
- Powerful for both code and prose

**Note:** BBEdit has a free trial and a paid license. There's also a free mode called "BBEdit Free Mode" with reduced features. Well-regarded in Mac development circles as a Vim/Emacs alternative with GUI polish.
