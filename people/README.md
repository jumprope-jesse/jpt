# People

Professional and personal contacts. Profiles are created and updated automatically from meeting transcripts.

## Profile Structure

Each profile follows a consistent template:

```markdown
# Person Name

## Role & Organization
- **Title**: Their role
- **Company**: Where they work
- **Reports to**: Their manager
- **Direct reports**: Their team

## Working Relationship
- How we interact
- Communication style
- General notes

## Projects & Responsibilities
- Current projects
- Key responsibilities

## Meeting History
- YYYY-MM-DD: Meeting name - Summary

## Notes & Context
- Personal details
- Contact info
- Miscellaneous observations
```

## File Naming

Use `Firstname_Lastname.md` format:
- `Justin_Meyer.md`
- `Sarah_Chen.md`

First-name-only files are automatically renamed when full names become available.

## Automated Curation

The **People Curator** (`lib/people_curator.py`) runs weekly (Sunday 4am) and:

1. **Generates a digest** of weekly changes → posted to Notion as a task
2. **Archives inactive profiles** - Sparse profiles with no meetings in 6+ months
3. **Merges duplicates** - Same person, different filenames (transcription errors)
4. **Renames files** - First-name-only → full name when header contains it
5. **Flags inconsistencies** - Conflicting info across profiles

Opens a **PR for review** (no auto-commit).

### Manual Commands
```bash
python3 ~/jpt/lib/people_curator.py status    # Profile analysis
python3 ~/jpt/lib/people_curator.py dry-run   # Preview changes
python3 ~/jpt/lib/people_curator.py run       # Run and create PR
python3 ~/jpt/lib/people_curator.py digest    # Generate digest only

# View logs
tail -f ~/jpt/lib/.curator.log
```

## Archive

Inactive profiles move to `.archive/` rather than being deleted.
