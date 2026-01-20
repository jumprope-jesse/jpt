# nh3 - Python HTML Sanitization Library

Python bindings to the Rust [ammonia](https://github.com/rust-ammonia/ammonia) HTML sanitization library.

**Docs:** https://nh3.readthedocs.io/en/latest/

## Why Use It

- Prevents XSS attacks by sanitizing user-generated HTML
- Written in Rust (fast, memory-safe)
- Highly customizable sanitization rules
- Can strip comments, filter styles, control allowed tags/attributes

## Basic Usage

```python
import nh3

# Basic sanitization
clean_html = nh3.clean("<script>evil()</script><b>safe</b>")
# Returns: '<b>safe</b>'

# Only allow specific tags
clean_html = nh3.clean("<b>bold</b> <i>italic</i>", tags={"b"})
# Returns: '<b>bold</b> italic'
```

## Key Functions

- `nh3.clean(html, **options)` - Sanitize HTML fragment
- `nh3.Cleaner(**options)` - Create reusable sanitizer with preset options
- `nh3.escape(text)` - Escape text to safe HTML (like `html.escape()`)
- `nh3.is_html(text)` - Check if string contains HTML syntax

## Common Options

| Option | Description |
|--------|-------------|
| `tags` | Set of allowed tag names |
| `attributes` | Dict mapping tags to allowed attributes (`*` = any tag) |
| `clean_content_tags` | Tags whose content is completely removed |
| `strip_comments` | Remove HTML comments (default: True) |
| `link_rel` | Rel attribute added to links (default: `noopener noreferrer`) |
| `url_schemes` | Allowed URL schemes for href/src |
| `allowed_classes` | CSS classes allowed per tag |
| `filter_style_properties` | Allowed CSS properties in style attributes |

## Link Rel Values

Common `rel` values for security:
- `noopener` - Prevents XSS via `window.opener`
- `noreferrer` - Hides referrer from linked site
- `nofollow` - Tells search engines not to follow

## Default Allowed Tags

Access defaults for customization:
```python
# Get default allowed tags
default_tags = nh3.ALLOWED_TAGS

# Add to defaults
my_tags = nh3.ALLOWED_TAGS | {"custom-element"}

# Get default attributes
default_attrs = nh3.ALLOWED_ATTRIBUTES
```

## When to Use

- Rendering user-submitted HTML (comments, rich text editors)
- Cleaning HTML from external sources
- Email content sanitization
- Any place untrusted HTML is displayed
