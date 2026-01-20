# snapDOM - Fast DOM Capture Library

JavaScript library for capturing DOM elements as high-fidelity SVG/PNG/JPG/WebP images.

**Repo:** https://github.com/zumerlab/snapdom

## Key Features

- Converts any HTML element into scalable SVG images
- Preserves styles, fonts, backgrounds, shadow DOM, pseudo-elements
- Export formats: SVG, PNG, JPG, WebP, or canvas
- Zero dependencies, uses standard Web APIs
- Dramatically faster than alternatives for large/complex DOM

## Quick Usage

```javascript
import { snapdom } from '@zumer/snapdom';

// Basic SVG capture
const svgDataUrl = await snapdom(document.querySelector("#myElement"));

// PNG with 2x scale
const img = await snapdom.toPng(element, 2);

// JPG with quality setting
const jpg = await snapdom.toJpg(element, 1, 0.8);
```

## Installation

```bash
# CDN
<script src="https://unpkg.com/@zumer/snapdom@latest/dist/snapdom.min.js"></script>

# ES Module
import { snapdom } from '@zumer/snapdom';
```

## When to Use

- Capturing full-page views or complex layouts
- Modal windows, components with shadow DOM
- UI screenshots for documentation or sharing
- Zoom-based view transitions (originally built for Zumly framework)

## Limitations

- External images must be CORS-accessible
- Fonts must be loaded before capture (awaits `document.fonts.ready`)
- Iframes not supported

## Performance

Benchmarks show snapDOM significantly outperforms html2canvas and dom-to-image for large DOM structures. modern-screenshot is slightly faster for tiny elements but snapDOM wins as complexity grows.
