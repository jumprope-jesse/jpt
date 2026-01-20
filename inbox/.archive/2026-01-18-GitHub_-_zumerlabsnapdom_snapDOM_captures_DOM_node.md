---
type: link
source: notion
url: https://github.com/zumerlab/snapdom
notion_type: Software Repo
tags: ['Running']
created: 2025-04-28T04:30:00.000Z
---

# GitHub - zumerlab/snapdom: snapDOM captures DOM nodes as images with exceptional speed avoiding bottlenecks and long tasks.

## Overview (from Notion)
- Efficiency in Development: SnapDOM's speed in capturing DOM elements can significantly streamline your workflow, allowing for faster prototyping and testing of web applications.
- Visual Communication: Use snapDOM to create high-fidelity visual representations of UI elements for client presentations or team discussions, enhancing your ability to communicate design ideas.
- Experimentation with Zoom Effects: As a founder, leveraging snapDOM can help in developing unique zoom-based transitions that set your applications apart from competitors.
- Educational Tool: Consider using snapDOM in workshops or coding bootcamps to teach developers about DOM manipulation and capture techniques.
- Performance Benchmarking: The performance comparison with other libraries provides insights into optimizing your applications, ensuring they run smoothly even under heavy load.
- Innovative Product Features: Think about integrating snapDOM's capabilities into your products, such as enabling users to capture and share their screens or specific elements seamlessly.
- CORS Challenges: Be aware of external image accessibility issues; this can impact how you handle assets in your applications.
- Community Engagement: Engage with the open-source community around snapDOM to contribute or gain insights, fostering collaboration and innovation in your projects.

## AI Summary (from Notion)
snapDOM is a fast DOM capture tool that converts HTML elements into scalable SVG images, preserving styles and content. It supports various export formats and includes features for capturing shadow DOM and pseudo-elements, making it ideal for complex layouts and animations.

## Content (from Notion)

# snapDOM

snapDOM is a high-fidelity DOM capture tool, developed as part of the animation engine for Zumly — a framework for creating smooth zoom-based view transitions.

It converts any HTML element into a scalable SVG image, preserving styles, fonts, backgrounds, shadow DOM content, pseudo-elements, and more.

- 📸 Full DOM capture
- 🎨 Embedded styles, pseudo-elements, and fonts
- 🖼️ Export to SVG, PNG, JPG, WebP, or canvas
- ⚡ Lightweight, no dependencies
- 📦 100% based on standard Web APIs
## Installation

You can use snapDOM by including it via CDN, script tag, or by importing it as a module.

### CDN

```plain text
<script src="https://unpkg.com/@zumer/snapdom@latest/dist/snapdom.min.js"></script>
```

### Script tag (local)

```plain text
<script src="snapdom.js"></script>
```

The global object snapdom will be available.

### ES Module

```plain text
import { snapdom } from './snapdom.mjs';
```

### Script Tag (Type Module)

```plain text
<script type="module">
  import { snapdom } from 'https://unpkg.com/@zumer/snapdom@latest/dist/snapdom.mjs';
</script>
```

Now you can call snapdom(el), snapdom.toPng(el), etc., directly in your JavaScript.

## Basic usage

```plain text
// Capture an element as SVG Data URL
const svgDataUrl = await snapdom(document.querySelector("#myElement"));

// Insert the captured image into the page
const img = new Image();
img.src = svgDataUrl;
document.body.appendChild(img);
```

## API

The main API is exposed as snapdom and offers multiple capture methods:

Parameters:

- el: DOM element to capture.
- scale: Scale factor (default is 1).
- quality: Compression quality for JPG/WebP (range 0–1).
## Special features

- Shadow DOM: Captures content inside Web Components and shadowRoot.
- Pseudo-elements: Captures ::before and ::after, including background images.
- Backgrounds and images: Inlines external images as Data URLs.
- Fonts: Replicates applied font families without needing external font files.
- Placeholder and Exclusion: 
## Full example

```plain text
<div id="captureMe">
  <h1 style="color: tomato;">Hello World!</h1>
  <p>This content will be captured.</p>
</div>

<script type="module">
  import { snapdom } from './snapdom.esm.js';

  const button = document.createElement('button');
  button.textContent = "Capture";
  button.onclick = async () => {
    const img = await snapdom.toPng(document.getElementById('captureMe'), 2);
    document.body.appendChild(img);
  };
  document.body.appendChild(button);
</script>
```

## Limitations

- External images must be CORS-accessible.
- Fonts must be fully loaded before capturing (document.fonts.ready is automatically awaited).
- Iframes are not captured.
## Benchmark

snapDOM is not only highly accurate — it's also extremely fast at capturing large or complex DOM structures.

In benchmark tests against popular libraries:

✅ Key insight:

While modern-screenshot is yet slightly faster for very small elements, snapDOM dramatically outperforms all others as the DOM size grows.

✅ Perfect for:

- Capturing full-page views
- Capturing modal windows
- Complex layouts with custom fonts, backgrounds, or shadow DOM
## License

MIT © Juan Martín Muda - Zumerlab


