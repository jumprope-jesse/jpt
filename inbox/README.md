# Inbox

Clearinghouse for all incoming captures. Items here get processed automatically and routed to the appropriate destination.

## How to Add Items

Create a markdown file with any name. The processor will pick it up within 2 minutes.

### Suggested Format

```markdown
---
type: link | thought | task | note
source: manual | notion | email | teams
url: (if applicable)
created: 2024-01-18T10:30:00
---

# Title or summary

Content, notes, why this matters...
```

The frontmatter is optional - the processor will figure out what to do with plain text too.

## What Happens to Items

The processor (Claude) reads each item and routes it appropriately:

- **Tasks** → Appended to `TASKS.md`
- **Knowledge** → Created/updated in `knowledge/`
- **People insights** → Added to `people/{Name}.md`
- **Personal notes** → Routed to `personal/`
- **Work notes** → Routed to `work/`

A single item may generate multiple outputs (e.g., an article might create tasks AND knowledge AND people updates).

After processing, items are moved to `.archive/` for reference.

## Quick Capture Examples

**Link:**
```markdown
---
type: link
url: https://example.com/article
---

# Interesting article about X

My notes on why this matters...
```

**Thought:**
```markdown
---
type: thought
---

Random idea: what if we tried X approach for the Y problem?
```

**Task:**
```markdown
---
type: task
---

Remember to follow up with John about the Q1 planning doc
```
