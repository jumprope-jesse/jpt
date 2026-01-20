# UI Density Framework

Source: [Matthew Ström - UI Density](https://matthewstrom.com/writing/ui-density/)

## Core Definition

**UI density = value a user gets from the interface / time and space the interface occupies**

Interfaces are becoming less dense over time (2000s → 2024 trend toward more spaced-out layouts).

## Five Types of Density

### 1. Visual Density
How much stuff is visible on screen. First, instinctual judgment but unreliable:
- Same number of dots can appear more or less dense based on arrangement
- Organized dots in grid look more dense than random scatter
- Grouping changes perception

Examples of high visual density: Bloomberg Terminal, Craigslist, McMaster-Carr

### 2. Information Density (Tufte)
Data-ink ratio: useful data elements / total "ink" used

Two ways to increase:
1. Add data-ink (more useful information)
2. Remove non-data-ink (eliminate decoration)

Tufte's Shrink Principle: "Graphics can be shrunk way down"

Example: Marey's 1885 train schedule - 260+ arrival/departure times in small space with near-1 data-ink ratio

### 3. Design Density
Based on Gestalt principles - measuring necessary design decisions vs total decisions:

Key Gestalt principles for UI:
- **Proximity**: close things = related group
- **Similarity**: same styling = same purpose
- **Closure**: minds fill gaps to see whole shapes
- **Symmetry**: symmetrical shapes = grouped around center
- **Common fate**: things moving together = related
- **Continuity**: perceive separate objects even when overlapping
- **Past experience**: recognize familiar patterns
- **Figure-ground**: interpret 2D as having foreground/background

### 4. Temporal Density
How much a user can do in a given amount of time. Loading times are the biggest factor.

Perception thresholds:
- **<100ms**: Feels simultaneous (animations may actually slow perception)
- **100ms - 1s**: Connection broken; animations/transitions help bridge gap
- **1s - 10s**: Users likely to abandon; use indeterminate loading indicators
- **10s - 1min**: Determinate progress bars (Apple Aqua stripes made waits feel 11% shorter)
- **>1min**: Let user leave, notify when done; blocking creates frustration

Bloomberg Terminal's real superpower: loads data almost instantaneously

### 5. Value Density
Providing highest value outcomes in smallest amount of time/space.

Counterintuitive implications:
- Breaking long forms into wizards may reduce visual density but increase value density (more completions)
- Google's sparse single search box was more value-dense than Yahoo's aggregated links
- Google: $23B (2004) → $2T today; Yahoo: $125B (2000) → sold for $4.8B

## Key Takeaways

1. Visual density is unreliable as a metric - perception varies with arrangement
2. Information density (Tufte) focuses on data-ink ratio but doesn't capture all UI needs
3. Design density accounts for intentional use of Gestalt principles
4. Temporal density through fast loading often more impactful than cramming more on screen
5. Value density is the ultimate measure - all other densities serve it
6. Sometimes less visual density = more value density

## Design Implications

- Speed, usability, consistency, predictability, information richness, and functionality all affect density
- Can't optimize visual density alone - must consider time and value
- Right design can manipulate time perception (progress bar animations)
- Blocking users >1 min creates frustration - use async patterns instead
