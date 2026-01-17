# Post-Meeting Processing Prompt

You are processing a meeting extracted from Granola. Read the available files (summary and/or transcript) and perform the updates below.

**Note**: Some meetings only have a summary (no transcript). Work with whatever content is available.

## 1. Update People Profiles

For each attendee (except Jesse Olsen, who is me):
- Create or update `~/jpt/people/{FirstName}_{LastName}.md`
- Use the template below for new profiles
- For existing profiles, ADD new information - never remove existing content
- Focus on: role, responsibilities, projects they're involved in, working style, relationships

**Profile Template:**
```markdown
# {Full Name}

## Role & Organization
- **Title**:
- **Company/Division**:
- **Reports to**:
- **Direct reports**:

## Working Relationship
- **How we interact**: (meetings, projects, reporting)
- **Communication style**:
- **Notes**:

## Projects & Responsibilities
<!-- Add bullet points as you learn about their work -->

## Meeting History
<!-- Append each meeting as a brief note -->
- {DATE}: {One-line summary of their involvement/topics}

## Notes & Context
<!-- Anything useful: preferences, background, relationships -->
```

## 2. Extract Action Items

Add any action items to `~/jpt/TASKS.md`:
- Add to the **INBOX** section for later triage
- Include: Task description, Source (meeting name + date), Owner if mentioned
- Format: `| {task} | Meeting: {meeting_title} | {date} | {any notes} |`

Only add CLEAR action items - things someone committed to do or was asked to do.
Skip vague discussion points.

## 3. Output Action Items JSON

After updating files, output a JSON block with all action items for automated processing.
This enables automatic task creation in vibe-kanban.

**REQUIRED**: At the end of your response, output this exact format:
```json
{"action_items": [{"task": "description", "owner": "Name or null", "due": "date or null"}]}
```

Rules for action_items JSON:
- Include ALL action items you added to TASKS.md
- "owner" should be the person responsible (or null if it's for Jesse/me)
- "due" should be a date string if mentioned, otherwise null
- Output valid JSON only - no trailing commas, proper quoting

## 4. Guidelines

- **Be conservative**: Only add information you're confident about
- **Preserve context**: When adding to profiles, note which meeting the info came from
- **Skip Jesse**: Don't create a profile for Jesse Olsen (that's me)
- **Handle duplicates**: If someone appears with slightly different names, use your judgment to merge
- **Privacy-aware**: These are internal notes, but still be professional

## Input Files

- **Summary**: `{SUMMARY_PATH}`
- **Transcript**: `{TRANSCRIPT_PATH}` (may not exist for older meetings)

Read the available files. If the transcript doesn't exist or is empty, work from the summary alone.
