---
type: link
source: notion
url: https://github.com/explorerhq/django-sql-explorer
notion_type: Software Repo
tags: ['Running']
created: 2024-07-05T12:56:00.000Z
---

# GitHub - explorerhq/django-sql-explorer: Easily share data across your company via SQL queries.

## AI Summary (from Notion)
- Project Overview: SQL Explorer is a Django-based application designed to facilitate the sharing and querying of data across organizations.
- Creation Date: The project was created on July 5, 2024, and is currently in the "Not started" status.
- Key Features:
- Supports multiple SQL database connections.
- AI-powered SQL assistant to help write and debug queries.
- In-browser pivot tables and the ability to snapshot queries on a schedule.
- User-friendly parameterized queries that generate a UI for non-SQL users.
- Offers quick access to schema information, query history, and logs.
- Allows sending query results via email and exposing saved queries as a JSON API.
- Development: Includes a test project for users to easily set up and explore the application locally.
- Licensing: The project is MIT licensed, welcoming pull requests from the community.
- Simplicity and Usability: Emphasizes intuitive use, unobtrusiveness, and stability to ensure a smooth user experience.
- Demo and Documentation: Links to a live demo, documentation, and a website are provided for users to explore further.

## Content (from Notion)

## SQL Explorer

- Live Demo
- Documentation
- Website
- Demo video:
SQL Explorer aims to make the flow of data between people fast, simple, and confusion-free. It is a Django-based application that you can add to an existing Django site, or use as a standalone business intelligence tool. It will happily connect to any SQL database that Django supports.

Quickly write and share SQL queries in a simple, usable SQL editor, view the results in the browser, and keep the information flowing!

Add an OpenAI (or other provider) API key and get an LLM-powered SQL assistant that can help write and debug queries. The assistant will automatically add relevant context and schema into the underlying LLM prompt.

SQL Explorer values simplicity, intuitive use, unobtrusiveness, stability, and the principle of least surprise. The project is MIT licensed, and pull requests are welcome.

Some key features include:

- Support for multiple connections
- AI-powered SQL assistant
- Quick access to schema information to make querying easier (including autocomplete)
- In-browser pivot tables (which can also be shared via URLs)
- Ability to snapshot queries on a regular schedule, capturing changing data
- Query history and logs
- Quick in-browser statistics, pivot tables, and scatter-plots (saving a trip to Excel for simple analyses)
- Basic code-completion in the SQL editor
- Parameterized queries that automatically generate a friendly UI for users who don't know SQL
- A playground area for quickly running ad-hoc queries
- Send query results via email
- Saved queries can be exposed as a quick-n-dirty JSON API if desired
- ...and more!
### Screenshots

Writing a query and viewing the schema helper

Using the SQL AI Assistant

Viewing all queries

Query results w/ stats summary

Pivot in browser

View logs

### Development

Included is a test_project that you can use to kick the tires. Just create a new virtualenv, cd into test_project and run start.sh (or walk through the steps yourself) to get a test instance of the app up and running.

You can now navigate to 127.0.0.1:8000/explorer/ and begin exploring!

running makemigrations --check failed due to a choices field not being in sync. This has no consequence for the application or the database, but some users have this as a CI step, which is now failing if SQL Explorer 5.0 is used.

Addresses #633


