# CSS Centering and Font Metrics

Source: [Tonsky - Hardest Problem in Computer Science: Centering Things](https://tonsky.me/blog/centering/)

## The Problem

Text centering looks simple but fails constantly because font bounding boxes don't match visual text appearance. Even Apple, Microsoft, GitHub, and Google ship misaligned UI.

## Why Centering Fails

### Font Metrics Mismatch
Font bounding boxes include:
- Ascender space (above cap-height, for accents)
- Descender space (below baseline)

These are rarely balanced. Many popular fonts are 5-10% off:
- Segoe UI: 10% off (explains GitHub on Windows issues)
- SF Pro Text, Inter, Martian Mono: properly balanced

### Line Height Complications
Line-height adds extra complexity. Different controls have different defaults. See Vincent De Oliveira's "Deep dive CSS: font metrics, line-height and vertical-align" for details.

### Icon Alignment
Icons next to text inherit all text problems plus their own:
- CSS `vertical-align` has 13 values, none work well
- `vertical-align: middle` aligns to x-height, not cap-height
- Icon fonts make everything worse (variable sizes, padding, blur)

## Solutions

### For Designers (Figma)
Use tight bounding boxes - Figma supports this but not by default:
- Text > Vertical trim > Cap height to baseline

### For Font Designers
Set metrics so: `ascender - cap-height = descender`
This makes centering trivial without changing actual glyph design.

### For Web Developers
Calculate compensation based on font metrics:

```css
/* For IBM Plex Sans example */
/* Extra padding = (ascender - capHeight - descender) / UPM */
padding-bottom: 0.052em;
```

Get font metrics from: opentype.js.org/font-inspector.html
- Need: ascender, descender, sCapHeight values

### For Icon Alignment
1. Set `vertical-align: baseline`
2. Move down by: `(iconHeight - capHeight) / 2`
3. Requires knowing both font metrics and icon size

### Icon Fonts: Don't Use Them
Icon fonts have arbitrary empty space around glyphs - impossible to align consistently. Use actual images with known dimensions instead.

### Optical Compensation
For icons needing visual balancing (triangles, play buttons):
- Wrap in rectangle with sufficient padding
- Visually balance the icon inside the bounding box

## Quick Reference

```css
/* Basic centering (the easy part) */
display: flex;
justify-content: center;
align-items: center;

/* OR with grid */
display: grid;
justify-items: center;
align-items: center;
```

The hard part is compensating for font metrics and icon shapes.

## Well-Balanced Fonts
These center properly without extra work:
- SF Pro Text
- Inter
- Martian Mono

## See Also
- [UI Density Framework](ui-density-framework.md) - related concepts on visual design
