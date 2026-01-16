# Notion Database Schema for Meeting Sync

Create a Notion database with the following properties for syncing Granola meetings.

## Database Properties

| Property Name | Type | Description |
|---------------|------|-------------|
| **Title** | Title | Meeting title (built-in title property) |
| **Date** | Date | Meeting date and time |
| **Attendees** | Multi-select | Meeting participants |
| **Summary** | Rich text | AI-generated meeting summary |
| **Transcript** | Rich text | Full meeting transcript |
| **Source** | Select | Where the meeting came from: `Granola`, `Manual`, etc. |
| **Synced** | Checkbox | Whether this has been synced to local markdown |
| **GranolaID** | Text | Original Granola document ID (for deduplication) |
| **MeetingURL** | URL | Link to original meeting (Granola share link, etc.) |

## Zapier Integration Setup

1. **Trigger**: Granola → "Note Added to Folder" or "Note Shared to Zapier"
2. **Action**: Create Notion Database Item with these mappings:
   - Title → Meeting Title
   - Date → Meeting Start Time
   - Summary → AI Summary
   - Transcript → Full Transcript
   - Attendees → Participant Names
   - GranolaID → Document ID
   - Source → "Granola" (static)
   - Synced → false (unchecked)

## Alternative: Make.com / n8n

Same field mappings apply. The key is:
- Trigger fires when meeting is **complete** (has summary)
- Maps all fields to Notion database
- Sets `Synced = false` so the polling script picks it up

## Polling Script Behavior

The `notion_sync.py` script will:
1. Query the database for items where `Synced = false`
2. Extract Title, Date, Summary, Transcript, Attendees
3. Write markdown file to `meetings/transcripts/`
4. Mark `Synced = true` in Notion

## Required API Access

You'll need a Notion integration with:
- Read access to the database
- Write access (to update Synced checkbox)

Get your integration token at: https://www.notion.so/my-integrations
