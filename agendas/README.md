# Meeting Agendas

This directory contains running agendas for meetings. Each file tracks:
- **NEXT** - Topics, questions, and items to share in the next meeting
- **Meetings** - History of past meetings with links to summaries/transcripts

## Naming Convention

- **1-on-1 meetings**: Use the other person's full name in kebab-case
  - `justin-meyer.md`
  - `andrea-lambert.md`
- **Recurring group meetings**: Use the meeting name in kebab-case
  - `jumprope-product-meeting.md`
  - `product-division-leadership.md`

## File Format

Each agenda uses YAML frontmatter for meeting title pattern matching:

```yaml
---
patterns:
  - jesse.*justin
  - justin.*1:1
person: Justin Meyer
frequency: Weekly
---
```

The `patterns` are regex patterns matched against meeting titles during processing.

## Adding Items

Use the `/agenda-add` command:
```
/agenda-add justin discuss 2025 tax prep
/agenda-add product-meeting review Q1 roadmap
```

Or edit the file directly - add items under `## NEXT > ### Topics`.

## Integration

When meetings are processed (`meetings/process_meeting.py`):
1. Agenda items are compared against the transcript
2. Missed items are noted in the meeting summary
3. Covered items get inline annotations with outcomes
4. Links to summary/transcript are added to the Meetings section
