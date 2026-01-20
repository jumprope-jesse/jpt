---
type: link
source: notion
url: https://overtype.dev/
notion_type: Software Repo
tags: ['Running']
created: 2025-08-17T22:53:00.000Z
---

# OverType - The Markdown Editor That's a Textarea

## Overview (from Notion)
- OverType's simplicity might resonate with your preference for efficiency in coding and parenting; sometimes less is more.
- The idea of a transparent textarea could inspire you to rethink how you approach user interfaces in your projects—prioritizing clarity and ease of use.
- As a founder, the low overhead of OverType (45KB) highlights the value of lean solutions in a world often focused on complexity.
- The focus on "no magic" aligns with a philosophy of transparency and straightforwardness in technology—a refreshing contrast to many modern tools that are overly complex.
- Consider how this minimalist approach could influence your software development practices, leading to quicker iterations and more user-friendly products.
- As a New Yorker, the fast-paced environment might benefit from tools that reduce friction and enhance productivity, allowing more time for family and personal interests.
- An alternate view might be that while simplicity is valuable, some users may crave advanced features that OverType intentionally omits; balancing simplicity with functionality could be a key challenge.

## AI Summary (from Notion)
OverType is a simple markdown editor that functions as a transparent textarea over rendered markdown, offering a straightforward WYSIWYG experience without complexity. It features a single layer of abstraction, allowing users to see rendered output directly beneath the textarea, with no virtual DOM or ContentEditable. The implementation is lightweight, requiring minimal understanding and customization compared to other editors, making it efficient and user-friendly.

## Content (from Notion)

OverType is a transparent textarea over rendered markdown.

Plain text simplicity, WYSIWYG beauty, zero complexity.

Hi HN! In my attempt to hack the standard WYSIWYG editor, I accidentally removed 90% of it and it still works ¯\_(ツ)_/¯

## AN UNDER-ENGINEERED SOLUTION

- A SINGLE LAYER OF ABSTRACTION - A textarea over a preview div
- AN OPEN BOX - Read, understand, and modify the code
- WYSIWYG WITHOUT THE HAIR-PULLING - Everything just works, it's native
## JUST A TEXTAREA

2. SEE RENDERED OUTPUT - Beautiful formatted text appears beneath

3. THAT'S IT - No virtual DOM, no ContentEditable

Everything just works: undo/redo, mobile keyboards, native selection - because it's really a textarea.

## THE BEST OF BOTH WORLDS

That's it. No npm. No build. No config.

## A PEAK UNDER THE HOOD

```plain text
// The entire trick:
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

// That's it. Everything else is polish.
```

That's it. A transparent textarea over a preview div. No virtual DOM. No ContentEditable. No magic.


