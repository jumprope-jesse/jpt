---
type: link
source: notion
url: https://github.com/teableio/teable
notion_type: Software Repo
tags: ['Running']
created: 2024-03-12T02:49:00.000Z
---

# GitHub - teableio/teable: ✨ A Super fast, Real-time, Professional, Developer friendly, No code database

## AI Summary (from Notion)
- Project Overview: Teable is a no-code database solution built on Postgres, designed for ease of use, scalability, and real-time collaboration.

- Key Features:
- Spreadsheet-like interface for easy data management.
- Multiple views available (Grid, Form, Calendar, etc.) for data visualization.
- Super fast performance with millions of data processed efficiently.
- Full-featured SQL support for seamless integration with BI and no-code tools.
- Privacy-first approach, allowing users to own their data.
- Real-time collaboration capabilities without refreshing the page.
- Future features include extensions, automation, and native AI integration.

- Deployment Options: Users can deploy Teable using Docker or Railway, with clear instructions provided.

- Development Setup: Specific steps for initializing the project, selecting databases, and running a development server are outlined.

- Vision for No-Code:
- A flexible interface for non-tech users to build applications.
- Enhanced data privacy and accessibility.
- The platform must also cater to developers and handle large data sets.
- Integration capabilities with other software and native AI functionalities are essential.

- Sponsorship and Support: Encouragement for sponsorship to enhance the project further.

- License: The project is licensed under AGPL-3.0.

## Content (from Notion)

#    

### Postgres-Airtable Fusion

Teable is a Super fast, Real-time, Professional, Developer friendly, No-code database built on Postgres. It uses a simple, spreadsheet-like interface to create complex enterprise-level database applications. Unlock efficient app development with no-code, free from the hurdles of data security and scalability.

Home | Help | Blog | Template | Roadmap | Discord

#    

## Quick Guide

1. Looking for a quick experience? Select a scenario from the template center and click "Use this template".
1. Seeking high performance? Try the 1 million rows demo to feel the speed of Teable.
1. Want to learn to use it quickly? Click on this tutorial
1. Interested in deploying it yourself? Click Deploy on Railway
## ✨Features

### 📊 Spreadsheet-like interface

All you want is here

- Cell Editing: Directly click and edit content within cells.
- Formula Support: Input mathematical and logical formulas to auto-calculate values.
- Data Sorting and Filtering: Sort data based on a column or multiple columns; use filters to view specific rows of data.
- Aggregation Function: Automatically summarize statistics for each column, providing instant calculations like sum, average, count, max, and min for streamlined data analysis.
- Data Formatting: formatting numbers, dates, etc.
- Grouping: Organize rows into collapsible groups based on column values for easier data analysis and navigation.
- Freeze Columns: Freeze the left column of the table so they remain visible while scrolling.
- Import/Export Capabilities: Import and export data from other formats, e.g., .csv, .xlsx.
- Row Styling & Conditional Formatting: Change row styles automatically based on specific conditions. (coming soon)
- Charts & Visualization Tools: Create charts from table data such as bar charts, pie charts, line graphs, etc. (coming soon)
- Data Validation: Limit or validate data that are entered into cells. (coming soon)
- Undo/Redo: Undo or redo recent changes. (coming soon)
- Comments & Annotations: Attach comments to rows, providing explanations or feedback for other users. (coming soon)
- Find & Replace: Search content within the table and replace it with new content. (coming soon)
### 🗂️ Multiple Views

Visualize and interact with data in various ways best suited for their specific tasks.

- Grid View: The default view of the table, which displays data in a spreadsheet-like format.
- Form View: Input data in a form format, which is useful for collecting data.
- Kanban View: Displays data in a Kanban board, which is a visual representation of data in columns and cards. (coming soon)
- Calendar View: Displays data in a calendar format, which is useful for tracking dates and events. (coming soon)
- Gallery View: Displays data in a gallery format, which is useful for displaying images and other media. (coming soon)
- Gantt View: Displays data in a Gantt chart, which is useful for tracking project schedules. (coming soon)
- Timeline View: Displays data in a timeline format, which is useful for tracking events over time. (coming soon)
### 🚀 Super Fast

Amazing response speed and data capacity

- Millions of data are easily processed, and there is no pressure to filter and sort
- Automatic database indexing for maximum speed
- Supports batch data operations at one time
### 👨‍💻 Full-featured SQL Support

Seamless integration with the software you are familiar with

- BI tools like Metabase PowerBi...
- No-code tools like Appsmith...
- Direct retrieve data with native SQL
### 🔒 Privacy-First

You own your data, in spite of the cloud

- Bring your own database (coming soon)
### ⚡️ Real-time collaboration

Designed for teams

- No need to refresh the page, data is updated in real-time
- Seamlessly integrate collaboration member invitation and management
- Perfect permission management mechanism, from table to column level
### 🧩 Extensions (coming soon)

Expand infinite possibilities

- Backend-less programming capability based on React
- Customize your own application with extremely low cost
- Extremely easy-to-use script extensions mode
### 🤖 Automation (coming soon)

Empower data-driven workflows effortlessly and seamlessly

- Design your workflow with AI or Visual programming
- Super easy to retrieve data from the table
### 🧠 Copilot (coming soon)

Native Integrated AI ability

- Chat 2 App. "Create a project management app for me"
- Chat 2 Chart. "Analyze the data in the order table using a bar chart"
- Chat 2 View. "I want to see the schedule for the past week and only display participants"
- Chat 2 Action. "After the order is paid and completed, an email notification will be sent to the customer"
- More actions...
### 🗄️ Support for multiple databases (coming soon)

Choose the SQL database you like

- Sqlite, PostgreSQL, MySQL, MariaDB, TiDB...
# Structure

```plain text
.
├── apps
│   ├── electron            (desktop, include a electron app )
│   ├── nextjs-app          (front-end, include a nextjs app)
│   └── nestjs-backend      (backend, running on server or inside electron app)
└── packages
    ├── common-i18n         (locales)
    ├── core                (share code and interface)
    ├── sdk                 (sdk for extensions)
    ├── db-main-prisma      (schema, migrations, prisma client)
    ├── eslint-config-bases (to shared eslint configs)
    └── ui-lib              (ui component)

```

## Deploy

### Deploy with docker

```plain text
cd dockers/examples/standalone/
docker-compose up -d
```

for more details, see dockers/examples

### Deploy with Railway

## Development

### 1. Initialize

```plain text
# Use `.nvmrc` file to specify node version（Requires pre `nvm` tools）
nvm install && nvm use

# Enabling the Help Management Package Manager
corepack enable

# Install project dependencies
pnpm install

# Build packages
pnpm g:build
```

### 2. Select Database

we currently support sqlite and postgres, you can switch between them by running the following command

```plain text
make switch-db-mode
```

### 3. Custom environment variables（optional）

```plain text
cd apps/nextjs-app
copy .env.development .env.development.local
```

### 4. Run dev server

you just need to start backend, it will start next server for frontend automatically, file change will be auto reload

```plain text
cd apps/nestjs-backend
pnpm dev
```

## Why Teable?

No-code tools have significantly speed up how we get things done, allowing non-tech users to build amazing apps and changing the way many work and live. People like using spreadsheet-like UI to handle their data because it's easy, flexible, and great for team collaboration. They also prefer designing their app screens without being stuck with clunky templates.

Giving non-techy people the ability to create their software sounds exciting. But that's just the start:

- As businesses expand, their data needs intensify. No one wishes to hear that once their orders reach 100k, they'll outgrow their current interface. Yet, many no-code platforms falter at such scales.
- Most no-code platforms are cloud-based. This means your important data sits with the provider, and switching to another platform can be a headache.
- Sometimes, no-code tools can't do what you want because of their limitations, leaving users stuck.
- If a tool becomes essential, you'll eventually need some tech expertise. But developers often find these platforms tricky.
- Maintaining systems with complex setups can be hard for developers, especially if these aren't built using common software standards.
- Systems that don't use these standards might need revamping or replacing, costing more in the long run. It might even mean ditching the no-code route and going back to traditional coding.
### What we think the future of no-code products look like

- An interface that anyone can use to build applications easily.
- Easy access to data, letting users grab, move, and reuse their information as they wish.
- Data privacy and choice, whether that's in the cloud, on-premise, or even just on your local.
- It needs to work for developers too, not just non-tech users.
- It should handle lots of data, so it can grow with your business.
- Flexibility to integrate with other software, combining strengths to get the job done.
- Last, native AI integration to takes usability to the next level.
In essence, Teable isn't just another no-code solution, it's a comprehensive answer to the evolving demands of modern software development, ensuring that everyone, regardless of their technical proficiency, has a platform tailored to their needs.

## Sponsors ❤️

If you are enjoying some this project in your company, I'd really appreciate a sponsorship, a coffee or a dropped star. That gives me some more time to improve it to the next level.

# License

AGPL-3.0


