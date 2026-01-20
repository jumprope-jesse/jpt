# Django SQL Explorer

Django-based SQL query tool for sharing data across an organization. MIT licensed.

GitHub: https://github.com/explorerhq/django-sql-explorer

## Key Features

- **Multiple database connections** - Query any SQL database Django supports
- **AI-powered SQL assistant** - Add OpenAI API key for LLM help writing/debugging queries
- **Schema browser** - Quick access to schema info with autocomplete
- **Pivot tables** - In-browser pivots, shareable via URL
- **Scheduled snapshots** - Capture query results on a schedule for trend tracking
- **Parameterized queries** - Auto-generates friendly UI for non-SQL users
- **Query history/logs** - Track what's been run
- **Email results** - Send query output via email
- **JSON API** - Expose saved queries as quick API endpoints
- **In-browser stats** - Basic statistics, scatter plots without leaving the browser

## Installation

```bash
pip install django-sql-explorer
```

Add to `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    'explorer',
]
```

Run migrations and visit `/explorer/`.

## Use Cases

- Business intelligence without full BI tool overhead
- Ad-hoc data exploration with guardrails
- Self-serve reporting for non-technical users via parameterized queries
- Quick data sharing across teams

## Notes

- Good for read-only analytics on read replicas
- AI assistant adds schema context to LLM prompts automatically
- Test project included in repo for local exploration
