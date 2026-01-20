# Feedsmith - JavaScript Feed Parser/Generator

Fast, robust JavaScript library for parsing and generating RSS, Atom, JSON Feed, and RDF feeds.

**Repo:** https://github.com/macieklamberski/feedsmith

## Key Features
- Universal parser (`parseFeed`) or format-specific parsers
- Preserves original feed structure (unlike libraries that normalize/merge fields)
- Supports namespaces: Dublin Core, iTunes, Podcast, Syndication, Content, Media RSS, GeoRSS, Slash, Creative Commons
- OPML support for feed lists
- TypeScript types, tree-shakable, 1200+ tests
- Works in Node.js and browsers

## Usage

```javascript
import { parseFeed } from 'feedsmith'

const { type, feed } = parseFeed('feed content')
// type: 'rss', 'atom', 'json', 'rdf'

// Format-specific
import { parseRssFeed, parseAtomFeed, parseJsonFeed } from 'feedsmith'

// OPML
import { parseOpml, generateOpml } from 'feedsmith'

// Generate JSON Feed
import { generateJsonFeed } from 'feedsmith'
```

## Why Feedsmith Over Alternatives
- Preserves namespace data (dc:creator, dc:date, etc.) separately
- Doesn't merge/lose information like many libraries do
- One of the fastest parsers (benchmarks in repo)
- Returns dates as strings (avoids parsing edge cases - use your own date library)

## Benchmarks
Top performer for RSS parsing (7.34 ops/sec vs next best 7.16), competitive for Atom and RDF.

*Saved 2026-01-18 from Notion inbox*
