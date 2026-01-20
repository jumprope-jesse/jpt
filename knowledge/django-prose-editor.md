# django-prose-editor: ProseMirror-based WYSIWYG for Django Admin

*Source: [Matthias Kestenholz's blog](https://406.ch/writing/django-prose-editor-prose-editing-component-for-the-django-admin/) - Added: 2026-01-19*

## Overview

A Django admin WYSIWYG component built on ProseMirror, created as a replacement for the dying django-ckeditor.

**Install:** `pip install django-prose-editor`
**GitHub:** https://github.com/matthiask/django-prose-editor
**PyPI:** https://pypi.org/project/django-prose-editor/

## Why This Exists

CKEditor 5's switch to GPL effectively killed django-ckeditor. Author evaluated alternatives:

| Editor | Issue |
|--------|-------|
| CKEditor 5 | GPL license change |
| TinyMCE 7 | Moving to GPL |
| Froala | Free trial only (commercial) |
| django-summernote | No dedicated maintainer |
| Trix | Buggy freeze states requiring page reload |
| Markdown editors | Not CMS-user-friendly |

ProseMirror was chosen because:
- Open source with sustainable licensing
- Used by major projects (indicates long-term maintenance)
- Author has deep experience since 2015
- Can implement custom functionality (annotations, interactive elements, cloze deletions)

## Current Status (as of 2024-03)

- Active development
- Available on PyPI
- Not yet in production use (staging/preview only at time of writing)
- Configurable server-side HTML sanitization
- Philosophy: Keep complexity low, add features slowly

## ProseMirror Learning Curve

Author notes the steep learning curve:

> "I haven't worked with another library which was so hard to get started with. It is my conviction that the reason for this is that rich-text editing is actually a hard problem."

But once it clicks, the architecture makes sense for complex requirements.

## When to Consider

- Replacing django-ckeditor in existing projects
- Need simple WYSIWYG without licensing concerns
- Want ProseMirror's power with Django integration
- Don't need extensive configuration (at least not yet)

## Related

- See `prosemirror-async-upload-pattern.md` for ProseMirror deep-dive on decorations
- Alternative: Consider Tiptap (ProseMirror-based with nicer API) if not Django-specific
