---
type: link
source: notion
url: https://github.com/macieklamberski/feedsmith
notion_type: Software Repo
tags: ['Running']
created: 2025-05-06T21:16:00.000Z
---

# GitHub - macieklamberski/feedsmith: Robust and fast parser and generator for RSS, Atom, JSON Feed, and RDF feeds, with support for Podcast, iTunes, Dublin Core, and OPML files.

## Overview (from Notion)
- Time-Saving: Use the Feedsmith library to efficiently manage and parse feeds, allowing you to spend less time on data handling and more on family or strategic business decisions.
- Staying Informed: Leverage RSS and JSON feeds to stay updated on industry trends, tech news, and parenting blogs without the noise of social media.
- Podcasting: If you're interested in podcasting, Feedsmith's podcast support can streamline your content generation, making it easier to share insights and experiences with a broader audience.
- Community Engagement: Engage with local tech communities in NYC by sharing your experiences with tools like Feedsmith, fostering connections with other founders and engineers.
- Open Source Contribution: Contributing to projects like Feedsmith can enhance your skills, expand your network, and provide a sense of accomplishment while setting a positive example for your kids about giving back.
- Unique Viewpoints: Balancing the fast-paced tech environment with the slower, more deliberate pace of parenting can offer insights into user experience design—understanding the needs of both busy professionals and families.
- Alternate Views: While some may prioritize flashy, all-in-one solutions, advocating for simplicity and reliability in tools (as Feedsmith does) can resonate with both tech-savvy users looking to minimize complexity and everyday users seeking straightforward solutions.

## AI Summary (from Notion)
Robust JavaScript parser and generator for RSS, Atom, JSON Feed, and RDF feeds, supporting various namespaces and OPML. It offers fast parsing, type safety, and maintains original feed structure while normalizing legacy elements.

## Content (from Notion)

# Feedsmith

Robust and fast JavaScript parser and generator for RSS, Atom, JSON Feed, and RDF feeds, with support for popular namespaces and OPML files. It provides both universal and format-specific parsers that maintain the original feed structure while offering helpful normalization.

Feedsmith maintains the original feed structure in a clean, object-oriented format. It intelligently normalizes legacy elements, providing you with complete access to all feed data without compromising simplicity.

Features · Installation · Parsing · Generating · Benchmarks · FAQ

### Leniency

- Normalizes legacy elements ✨ — Upgrades feed elements to their modern equivalents so that you never need to worry about reading feeds in older formats.
- CaSe INSENsiTive — Handles fields and attributes in any case (lowercase, uppercase, mixed).
### Performance and type-safety

- Fast parsing — One of the fastest feed parsers in JavaScript (see benchmarks).
- Type-safe API — TypeScript type definitions are available for each feed format, making it easy to work with the data.
- Tree-shakable — Only include the parts of the library you need, reducing bundle size.
- Well-tested — Comprehensive test suite with 1200+ tests and 99% code coverage.
### Compatibility

- Works in Node.js and all modern browsers.
- Works with plain JavaScript, you don't need to use TypeScript.
## Supported formats

✅ Available · ⌛️ Work in progress · 📋 Planned

### Feeds

### Namespaces

### Other

## Installation

```plain text
npm install feedsmith
```

## Parsing

### Universal feeds parser

The easiest way to parse any feed is to use the universal parseFeed function:

```plain text
import { parseFeed } from 'feedsmith'

const { type, feed } = parseFeed('feed content')

console.log('Feed type:', type) // → rss, atom, json, rdf
console.log('Feed title:', feed.title)

if (type === 'rss') {
  console.log('RSS feed link:', feed.link)
}
```

### Dedicated feeds parsers

If you know the format in advance, you can use the format-specific parsers:

```plain text
import { parseAtomFeed, parseJsonFeed, parseRssFeed, parseRdfFeed } from 'feedsmith'

// Parse the feed content
const atomFeed = parseAtomFeed('atom content')
const jsonFeed = parseJsonFeed('json content')
const rssFeed = parseRssFeed('rss content')
const rdfFeed = parseRdfFeed('rdf content')

// Then read the TypeScript suggestions for the specific feed type
rssFeed.title
rssFeed.dc?.creator
rssFeed.dc?.date
rssFeed.sy?.updateBase
rssFeed.items?.[0]?.title
```

### OPML parser

Parsing OPML files is as simple:

```plain text
import { parseOpml } from 'feedsmith'

// Parse the OPML content
const opml = parseOpml('opml content')

// Then read the TypeScript suggestions
opml.head?.title
opml.body?.outlines?.[0].text
opml.body?.outlines?.[1].xmlUrl
```

### Returned values

The objects returned from the parser functions are highly comprehensive, aiming to recreate the actual feed structure and its values, including all the supported namespaces. Below are some examples of what is available.

```plain text
import { parseAtomFeed } from 'feedsmith'

const atomFeed = parseAtomFeed(`
  <?xml version="1.0" encoding="utf-8"?>
  <feed xmlns="http://www.w3.org/2005/Atom">
    <title>Example Feed</title>
    <id>example-feed</id>
    <dc:creator>John Doe</dc:creator>
    <dc:contributor>Jane Smith</dc:contributor>
    <dc:date>2022-01-01T12:00+00:00</dc:date>
    <dc:description>This is an example of description.</dc:description>
    <sy:updateBase>2000-01-01T12:00+00:00</sy:updateBase>
    <sy:updatePeriod>hourly</sy:updatePeriod>
    <sy:updateFrequency>1</sy:updateFrequency>
    <entry>
      <title>Example Entry</title>
      <id>example-entry</id>
      <dc:creator>Jack Jackson</dc:creator>
      <dc:date>2022-01-01T12:00+00:00</dc:date>
    </entry>
  </feed>
`)

atomFeed.title // → Example Feed
atomFeed.dc?.contributor // → Jane Smith
atomFeed.dc?.date // → 2022-01-01T12:00+00:00
atomFeed.sy?.updateFrequency // → 1
atomFeed.entries?.[0]?.title // → Example Entry
atomFeed.entries?.[0]?.dc?.creator // → Jack Jackson
```

Returns:

```plain text
{
  "id": "example-feed",
  "title": "Example Feed",
  "entries": [
    {
      "id": "example-entry",
      "title": "Example Entry",
      "dc": {
        "creator": "Jack Jackson",
        "date": "2022-01-01T12:00+00:00"
      }
    }
  ],
  "dc": {
    "creator": "John Doe",
    "description": "This is an example of description.",
    "contributor": "Jane Smith",
    "date": "2022-01-01T12:00+00:00"
  },
  "sy": {
    "updatePeriod": "hourly",
    "updateFrequency": 1,
    "updateBase": "2000-01-01T12:00+00:00"
  }
}
```

For more examples, check the */references folders in the source code. There, you'll find the complete objects returned from the parser functions for the various feed formats and versions.

- Atom examples: src/feeds/atom/references,
- RSS examples: src/feeds/rss/references,
- RDF examples: src/feeds/rdf/references.
- OPML examples: src/opml/references.
### Error handling

If the feed is unrecognized or invalid, an Error will be thrown with a descriptive message.

```plain text
import { parseFeed, parseJsonFeed } from 'feedsmith'

try {
  const universalFeed = parseFeed('<not-a-feed></not-a-feed>')
} catch (error) {
  // Error: Unrecognized feed format
}

try {
  const jsonFeed = parseJsonFeed('{}')
} catch (error) {
  // Error: Invalid feed format
}
```

### Format detection

You can detect feed formats without parsing them.

```plain text
import { detectAtomFeed, detectJsonFeed, detectRssFeed, detectRdfFeed } from 'feedsmith'

if (detectAtomFeed(content)) {
  console.log('This is an Atom feed')
}

if (detectJsonFeed(content)) {
  console.log('This is a JSON feed')
}

if (detectRssFeed(content)) {
  console.log('This is an RSS feed')
}

if (detectRdfFeed(content)) {
  console.log('This is an RDF feed')
}
```

Warning

Detect functions are designed to quickly identify the feed format by looking for its signature, such as the <rss> tag in the case of RSS feeds. However, the function may detect an RSS feed even if it is invalid. The feed will be fully validated only when using the parseRssFeed function.

## Generating

### Generating JSON Feed

Although JSON feeds are simply JSON objects that can be easily generated manually, the generateJsonFeed function provides helpful type hints, which can aid in feed generation. Additionally, you can use Date objects for dates, which are automatically converted to the correct format in the background.

```plain text
import { generateJsonFeed } from 'feedsmith'

const jsonFeed = generateJsonFeed({
  title: 'My Example Feed',
  feed_url: 'https://example.com/feed.json',
  authors: [
    {
      name: 'John Doe',
      url: 'https://example.com/johndoe',
    },
  ],
  items: [
    {
      id: '1',
      content_html: '<p>Hello world</p>',
      url: 'https://example.com/post/1',
      title: 'First post',
      date_published: new Date('2019-03-07T00:00:00+01:00'),
      language: 'en-US',
    },
  ],
})
```

Will output:

```plain text
{
  "version": "https://jsonfeed.org/version/1.1",
  "title": "My Example Feed",
  "feed_url": "https://example.com/feed.json",
  "authors": [
    {
      "name": "John Doe",
      "url": "https://example.com/johndoe",
    },
  ],
  "items": [
    {
      "id": "1",
      "content_html": "<p>Hello world</p>",
      "url": "https://example.com/post/1",
      "title": "First post",
      "date_published": "2019-03-06T23:00:00.000Z",
      "language": "en-US",
    },
  ],
}
```

Note

The functionality for generating the remaining feed formats is currently under development and will be introduced gradually. For more information, see the Supported formats.

### Generating OPML

```plain text
import { generateOpml } from 'feedsmith'

const opml = generateOpml({
  head: {
    title: 'My Feed',
    dateCreated: new Date(),
  },
  body: {
    outlines: [
      {
        text: 'My Feed',
        type: 'rss',
        xmlUrl: 'https://example.com/feed.xml',
        htmlUrl: 'https://example.com',
      },
    ],
  },
})
```

Will output:

```plain text
<?xml version="1.0" encoding="utf-8"?>
<opml version="2.0">
  <head>
    <title>My Feed</title>
    <dateCreated>Fri, 11 Apr 2025 13:05:26 GMT</dateCreated>
  </head>
  <body>
    <outline text="My Feed" type="rss" xmlUrl="https://example.com/feed.xml" htmlUrl="https://example.com"/>
  </body>
</opml>
```

## Benchmarks

A comprehensive set of benchmarks, categorized by various file sizes, is available in the /benchmarks directory. These benchmarks were conducted using both Tinybench and Benchmark.js.

See full benchmark results →

For a quick overview, here are the results of parsing RSS, Atom, and RDF feeds using various JS packages with Tinybench. Feedsmith's results are marked with an asterisk (*).

```plain text
📊 RSS feed parsing (50 files × 100KB–5MB)
┌───┬───────────────────────────────┬─────────┬──────────────┬──────────┬──────────┬──────┐
│   │ Package                       │ Ops/sec │ Average (ms) │ Min (ms) │ Max (ms) │ Runs │
├───┼───────────────────────────────┼─────────┼──────────────┼──────────┼──────────┼──────┤
│ 0 │ feedsmith *                   │ 7.34    │ 136.167      │ 128.479  │ 173.223  │ 111  │
│ 1 │ @rowanmanning/feed-parser     │ 7.16    │ 139.678      │ 128.722  │ 170.903  │ 108  │
│ 2 │ @ulisesgascon/rss-feed-parser │ 4.14    │ 241.405      │ 230.806  │ 278.534  │ 63   │
│ 3 │ feedparser                    │ 2.50    │ 399.824      │ 374.049  │ 459.730  │ 38   │
│ 4 │ @extractus/feed-extractor     │ 2.26    │ 443.065      │ 430.349  │ 460.195  │ 34   │
│ 5 │ feedme.js                     │ 2.05    │ 487.222      │ 443.837  │ 535.029  │ 31   │
│ 6 │ rss-parser                    │ 1.66    │ 603.044      │ 573.516  │ 653.683  │ 25   │
│ 7 │ @gaphub/feed                  │ 0.94    │ 1068.621     │ 995.044  │ 1138.913 │ 15   │
└───┴───────────────────────────────┴─────────┴──────────────┴──────────┴──────────┴──────┘

📊 Atom feed parsing (50 files × 100KB–5MB)
┌───┬───────────────────────────┬─────────┬──────────────┬──────────┬──────────┬──────┐
│   │ Package                   │ Ops/sec │ Average (ms) │ Min (ms) │ Max (ms) │ Runs │
├───┼───────────────────────────┼─────────┼──────────────┼──────────┼──────────┼──────┤
│ 0 │ feedsmith *               │ 0.98    │ 1020.035     │ 998.660  │ 1084.180 │ 15   │
│ 1 │ @gaphub/feed              │ 0.95    │ 1058.126     │ 989.001  │ 1150.486 │ 15   │
│ 2 │ @rowanmanning/feed-parser │ 0.63    │ 1580.462     │ 1563.357 │ 1607.379 │ 10   │
│ 3 │ feedparser                │ 0.37    │ 2687.488     │ 2624.427 │ 2751.504 │ 6    │
│ 4 │ @extractus/feed-extractor │ 0.32    │ 3136.880     │ 3107.170 │ 3228.099 │ 5    │
│ 5 │ feedme.js                 │ 0.26    │ 3812.545     │ 3759.928 │ 3843.974 │ 4    │
│ 6 │ rss-parser                │ 0.18    │ 5539.014     │ 5479.560 │ 5609.397 │ 3    │
└───┴───────────────────────────┴─────────┴──────────────┴──────────┴──────────┴──────┘

📊 RDF feed parsing (50 files × 100KB–5MB)
┌───┬───────────────────────────┬─────────┬──────────────┬──────────┬──────────┬──────┐
│   │ Package                   │ Ops/sec │ Average (ms) │ Min (ms) │ Max (ms) │ Runs │
├───┼───────────────────────────┼─────────┼──────────────┼──────────┼──────────┼──────┤
│ 0 │ @rowanmanning/feed-parser │ 13.52   │ 73.990       │ 69.404   │ 89.504   │ 203  │
│ 1 │ feedsmith *               │ 10.16   │ 98.396       │ 92.418   │ 118.053  │ 153  │
│ 2 │ @extractus/feed-extractor │ 3.83    │ 260.946      │ 252.991  │ 274.432  │ 58   │
│ 3 │ feedparser                │ 1.96    │ 509.686      │ 494.823  │ 530.224  │ 30   │
│ 4 │ feedme.js                 │ 1.40    │ 714.442      │ 661.440  │ 789.395  │ 22   │
│ 5 │ rss-parser                │ 0.97    │ 1028.245     │ 985.521  │ 1107.122 │ 15   │
│ 6 │ @gaphub/feed              │ 0.97    │ 1031.579     │ 1008.220 │ 1060.322 │ 15   │
└───┴───────────────────────────┴─────────┴──────────────┴──────────┴──────────┴──────┘

```

## FAQ

### Why should I use Feedsmith instead of alternative packages?

The key advantage of Feedsmith is that it preserves the original feed structure exactly as provided in each specific feed format.

Many alternative packages attempt to normalize data by:

- Merging distinct fields like author, dc:creator, and creator into a single property.
- Combining date fields such as dc:date and pubDate without preserving their sources.
- Handling multiple <atom:link> elements inconsistently, sometimes keeping only the first or last one or ignoring different rel attributes.
- Some libraries try to combine different feed formats into one universal structure.
While this approach can be useful for quick reading of feed data, it often results in a loss of information that may be crucial for certain applications, such as reading data from specific namespaces.

### Why are date fields returned as strings?

In the course of parsing hundreds of thousands of feeds, I have found that dates in feeds use many different formats. Rather than attempting to parse them all (and potentially introducing errors), dates are returned in their original string form. This approach allows you to use your preferred date parsing library or simply the Date object.

### Does Feedsmith validate feeds?

Feedsmith focuses on parsing feeds rather than validating them. It will extract whatever valid data it can find, even from partially valid feeds. This approach makes it more resilient when dealing with feeds found in the wild.

It will only fail if the feed is completely invalid or it does not contain all the fields required according to the specification.

### How does Feedsmith handle missing or incomplete data?

Feedsmith is designed to be forgiving. It will extract whatever valid data it can find and ignore missing or invalid elements. This makes it suitable for use with real-world feeds that may not strictly follow specifications.

### Does Feedsmith work in the browser?

Even though Feedsmith is more suited for the Node.js environments, it was also tested in modern browsers where it works seamlessly. It's provided as an ES module.

## Acknowledgements

- The library API is inspired by the FeedKit library for Swift.
- XML parsing is provided by fast-xml-parser.
- HTML entity decoding is handled by entities.
## License

Licensed under the MIT license.

Copyright 2025 Maciej Lamberski


