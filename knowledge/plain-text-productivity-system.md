# Plain Text Productivity System (Jeff Huang)

*Source: https://jeffhuang.com/productivity_text_file/ - Added: 2026-01-19*

A 14-year-old productivity system using a single, ever-growing text file as combined todo list, meeting notes, research notebook, and work log.

## Core Philosophy

- No app fragmentation - everything in one searchable file
- Daily lists become historical records
- Calendar as the only external tool (for future scheduling)
- Tasks sized to fit a single day

## Daily Workflow

**Night before:**
1. Copy next day's calendar items to end of text file
2. Size tasks - break big ones down, shuffle others to future dates
3. Wake up knowing exactly what to do

**During day:**
1. Work through list
2. Take notes directly on list items
3. Todo list becomes "what done" list

**Email handling:**
- Red flag: deal with today
- Orange flag: needs thinking or waiting on someone
- Yellow flag: sent emails awaiting reply
- Quick evening review of flags

## File Structure Example

```
2021-11-31
11am meet with Head TAs
- where are things at with inviting portfolio reviewers? A: got 7/29 replies
- need 3 TAs for Thursday lab
11:30am meet with student Enya (interested in research)
- they're a little inexperienced, suggested applying next year
review and release A/B Testing assignment grading
[...]
```

## Tags and Searchability

- `#idea` - new ideas to revisit
- `#annual` - things for annual reports
- `#cv` - accomplishments to add to CV
- `#nextui` - things for next course iteration
- Search "meet with" to find all meetings (3000+ in his case)

## Key Properties

1. **Immediate clarity** - wake up, look at list, know what to do
2. **No mental overhead** - future items live in calendar, not head
3. **Easy recall** - search any past meeting, decision, or idea
4. **No zombie tasks** - nothing pushed back day after day
5. **Workload control** - reduce by unflagging emails, dropping calendar items

## Stats After 14 Years

- 51,690 handwritten lines
- 3,000+ scheduled meetings documented
- Complete record of every person met and what was discussed

## Why It Works

- Text is infinitely flexible
- No feature bloat or app lock-in
- Quick glance shows done vs. remaining (empty line separator)
- Aggregate stats via text editor search
- Works on any device via Remote Desktop

## Trade-offs

- May miss some questions or interesting tangents
- Requires discipline to transfer calendar nightly
- No fancy visualizations or reminders

## Relevance to Jesse's System

This is essentially a manual, pre-digital version of what Jesse's JPT system automates:
- Meeting notes → `meetings/` processing
- Todo lists → Notion tasks
- Knowledge capture → `knowledge/` files
- Searchable history → git + file organization

The single-file approach has elegance but doesn't scale to the multi-source intake (Readwise, Meetily, etc.) Jesse's system handles.
