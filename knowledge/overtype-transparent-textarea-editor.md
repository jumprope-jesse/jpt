# OverType: Transparent Textarea Markdown Editor

A minimalist approach to WYSIWYG markdown editing that avoids the complexity of typical rich text editors.

## The Concept

Instead of using ContentEditable or a virtual DOM, OverType layers a transparent `<textarea>` over a preview `<div>`. Users type in the textarea while seeing the rendered markdown beneath.

## Implementation Pattern

```javascript
// The core technique:
layerElements(textarea, preview)           // Position textarea over preview
applyIdenticalSpacing(textarea, preview)   // Match fonts, padding, line-height exactly

// Make textarea invisible but keep the cursor
textarea.style.background = 'transparent'
textarea.style.color = 'transparent'
textarea.style.caretColor = 'black'

// Keep them in sync
textarea.addEventListener('input', () => {
  preview.innerHTML = parseMarkdown(textarea.value)
  syncScroll(textarea, preview)
})
```

## Why This Works

- Native undo/redo, selection, and keyboard handling
- Mobile keyboards work correctly
- No ContentEditable quirks
- Tiny footprint (~45KB)
- No build step, no npm required

## Trade-offs

- Limited formatting capabilities vs. full rich text editors
- Alignment between textarea and preview requires precise styling
- Some advanced features (tables, embeds) harder to implement

## When to Use

- Documentation editors
- Note-taking apps
- Comment systems
- Any case where markdown + simplicity beats feature-completeness

## Source

- https://overtype.dev/
