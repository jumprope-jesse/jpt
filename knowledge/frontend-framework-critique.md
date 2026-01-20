# Frontend Framework Critique: The Case Against React

Source: [If Not React, Then What?](https://infrequently.org/2024/11/if-not-react-then-what/) by Alex Russell (November 2024)

## Core Argument

React is legacy technology that continues appearing in greenfield applications. Nobody should start a new project in the 2020s based on React.

## The Rule of Least Client-Side Complexity

- Server-side code can be fully costed and controlled
- Client-side code runs on "The Devil's Computer" - nothing about latency, resources, or APIs is under developer control
- **Strategy**: Send less code to clients
- Prefer HTML and CSS over JavaScript (graceful degradation, better compression)
- Declarative forms generate more functional UI per byte

## When SPAs Are Actually Appropriate

The choice isn't between JavaScript frameworks - it's whether SPA-oriented tools should be entertained at all.

SPAs make sense when:
1. Long session lengths
2. Many incremental updates to primary UI data
3. Need for optimistic updates against local data model

### By Application Type

| Type | Recommendation |
|------|----------------|
| **Informational** (blogs, marketing, docs) | Static HTML, minimal JS. Use Hugo, Astro, 11ty, Jekyll |
| **E-commerce** | Server-generated HTML + progressive enhancement. Amazon outperforms React competitors |
| **Media** | Progressive enhancement + islands of interactivity. SPA only for mini-player UIs or offline playback |
| **Social** | Hybrid approach (Hotwire, HTMX). Islands for deep interactivity |
| **Productivity/Editors** | SPAs may be appropriate, but need extreme discipline on bundle size and phased loading |

## Common Pushbacks Debunked

### "We need to move fast"
- NPM-flung-together development causes teams to get stuck sooner than expected
- Finding product-market-fit requires making products widely available, then adding flourishes
- Low-quality experiences drag on core growth

### "Our teams already know React"
- React developers are web developers - HTML, CSS, JS, DOM are inescapable
- Moving between templating systems is what web devs have done for 30 years
- Anyone who masters React's baroque conventions can easily learn Preact, Svelte, Lit, Qwik, etc.

### "React is industry-standard"
- React isn't one thing - it's a lifestyle of choices: function vs class components, TypeScript, package managers (npm/yarn/pnpm), bundlers (webpack/esbuild/swc), meta-tools (vite/turbopack), state management...
- Across 100+ consulting engagements, never seen two identical React setups
- "Nothing standard about any of this"

### "The ecosystem..."
- Every NPM dependency is high-interest debt collateralized by future engineering capacity
- If you're not comfortable owning, patching, and improving every dependency, it shouldn't be in your stack

### "Next.js can be fast enough"
- Sites built with Next.js perform materially worse than HTML-first systems (11ty, Astro)
- Default delay-loaded JS competes with ads and business-critical deferred content
- "A fast way to lose money while getting locked into a VC-backed startup's proprietary APIs"

## Framework for Decision Making

1. **User focus**: Decision-makers accountable for engineering choices' results
2. **Evidence**: Better evidence must win. Use RUM data, Core Web Vitals, lab tests
3. **Guardrails**: Policies requiring progressive enhancement (like UK GDS)
4. **Bakeoffs**: Define critical user journeys, test how systems deliver for marginal users

## Key Concept: Frameworkism

The ideology that all user problems will be solved by framework adoption. The opposite of engineering (which designs solutions under known constraints). Solutions outside the framework's ecosystem become unavailable to adherents.

**Antidote**: RUM and bench data provide baselines to argue about, replacing faith-based framework investment with data-driven decisions.

## Recommended Resources

- [UK GDS: Building robust frontend using progressive enhancement](https://www.gov.uk/service-manual/technology/using-progressive-enhancement)
- "JavaScript dos and donts" by Mu-An Chiou
- "The Frontend Treadmill" by Marco Rogers
- "Questions for a new technology" by Kellan Elliott-McCrea
- Glyph's "Against Innovation Tokens"

---

# Google's Angular + Wiz Merger Strategy

Source: [Angular and Wiz Are Better Together](https://blog.angular.io/angular-and-wiz-are-better-together-91e633d8cd5a) (March 2024)

## The Two Frameworks

Google internally has two web frameworks serving different needs:

| Framework | Focus | Example Apps | Approach |
|-----------|-------|--------------|----------|
| **Wiz** | Performance-critical, low interactivity | Search, Photos, Payments | SSR-first, minimal JS, streaming rendering |
| **Angular** | Highly interactive apps | Gemini, Google Analytics | Developer experience, complex UIs |

## Wiz's Performance-First Architecture

Wiz optimizes for slow networks and low-end devices:
1. **Always SSR**: Everything rendered server-side via streaming
2. **Minimal JS**: Only loads code for interactive components actually on page
3. **Event replay**: Small inline library captures user events at root, replays them once JS loads

Tradeoff: Better UX performance at cost of increased developer complexity.

## The Blending Problem

- Performant apps need to ship features faster (more interactivity)
- Interactive apps shipping more JS (HTTPArchive: +37% desktop, +36% mobile over 6 years)
- Lines between framework use cases are blurring

## Cross-Pollination So Far

**Wiz → Angular:**
- Deferrable views
- Partial hydration exploration
- Fine-grained code loading patterns

**Angular → Wiz:**
- Angular Signals library now powers YouTube's UI
- Enables fine-grained UI updates
- Replaced memoization-dependent approach with reactive primitives

## Long-term Strategy

Google plans to gradually merge Angular and Wiz over "coming years":
- Open source Wiz features through Angular
- Public RFC process for community feedback
- SSR as core priority ("positively impacts end user experience when done correctly")

## Relevance to Framework Critique

This represents a different philosophy than the "avoid client-side complexity" argument. Google's approach:
- Acknowledges SSR importance (aligns with Russell's view)
- But still invests heavily in framework complexity to solve performance
- Betting on reactive primitives (Signals) and fine-grained loading rather than "send less JS"

The question: Is Google's engineering budget and talent pool a prerequisite for making this approach work at scale?
