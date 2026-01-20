# Defuddle - Web Content Extraction

Defuddle extracts main content from web pages by removing clutter (comments, sidebars, headers, footers). Created by kepano for Obsidian Web Clipper.

**Repo:** https://github.com/kepano/defuddle
**Playground:** Available for testing

## Key Features

- More forgiving than Mozilla Readability, removes fewer uncertain elements
- Consistent output for footnotes, math, code blocks
- Uses mobile styles to identify unnecessary elements
- Extracts schema.org metadata
- Can output Markdown (Node.js bundle)

## Usage

```javascript
// Browser
import { Defuddle } from 'defuddle';
const result = new Defuddle(document).parse();

// Node.js
import { JSDOM } from 'jsdom';
import { Defuddle } from 'defuddle/node';
const result = await Defuddle(html, { markdown: true });
```

## Output

Returns: `content`, `title`, `author`, plus metadata.

## Bundles

| Bundle | Use Case |
|--------|----------|
| `defuddle` | Browser, no deps |
| `defuddle/full` | Math equation parsing |
| `defuddle/node` | Node.js with JSDOM, full features |

## HTML Standardization

- Removes duplicate H1/H2 matching title
- Converts H1s to H2s
- Standardizes code blocks with language detection
- Normalizes footnotes
- Converts MathJax/KaTeX to MathML

## Comparison to Readability

Defuddle is designed as a Readability replacement that's more forgiving and produces cleaner, more consistent output for downstream Markdown conversion.
