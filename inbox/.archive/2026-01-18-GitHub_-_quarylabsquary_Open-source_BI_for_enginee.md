---
type: link
source: notion
url: https://github.com/quarylabs/quary
notion_type: Software Repo
tags: ['Running']
created: 2024-05-16T11:21:00.000Z
---

# GitHub - quarylabs/quary: Open-source BI for engineers

## AI Summary (from Notion)
- Project Overview: Quary is an open-source Business Intelligence (BI) tool designed for engineers, facilitating data connection, transformation, and visualization.

- Key Features:
- Connects to databases and allows writing SQL queries.
- Supports creating charts, dashboards, and reports (currently in development).
- Enables version control for testing, collaboration, and iterative refactoring.
- Facilitates deployment of organized and documented models back to the database.

- Supported Asset Types:
- Sources: External data sources such as database tables, flat files, or APIs.
- Models: Transformative SQL-based datasets from raw data.
- Charts: Visual data representations using SQL.
- Dashboards and Reports: Work in progress for combining multiple charts and creating detailed reports.

- Installation and Usage:
- Available as a VSCode extension and a Rust-based CLI.
- Installation options include Homebrew and curl for Linux/Mac.
- Sample project creation and execution are straightforward with command-line instructions.

- Community and Support:
- A Slack channel is available for community interaction, ideas, and discussions.
- Support is offered through issue creation for troubleshooting.

- Interesting Fact: Quary is designed to simplify the BI process for engineers by allowing them to manage and manipulate data using familiar SQL queries.

## Content (from Notion)

# Quary

### Business Intelligence for Engineers 🅀

## With Quary, engineers can:

- 🔌 Connect to their Database
- 📖 Write SQL queries to transform, organize, and document tables in a database
- 📊 Create charts, dashboards and reports (in development)
- 🧪 Test, collaborate & refactor iteratively through version control
- 🚀 Deploy the organised, documented model back up to the database
View the documentation.

## 🗃️ Supported Databases

## 🏗️ Asset Types in Quary

Define and manage the following asset types as code:

- Sources: Define the external data sources that feed into Quary, such as database tables, flat files, or APIs (with DuckDB).
- Models: Transform raw data from sources into analysis-ready datasets using SQL, this lets engineers split complex queries into atomic components.
- Charts: Create visual representations of your data using SQL.
- 🚧 Dashboards (WIP): Combine multiple charts into a single view, allowing engineers to monitor and analyze data in one place.
- 🚧 Reports (WIP): Create detailed reports to share insights and findings with your team or stakeholders.
## 🚀 Getting Started

### Installation

Quary is a VSCode Extension (Interface) & Rust-based CLI (Core)

### Extension

The VSCode extension can be installed here. Note that it depends on the CLI being installed.

### CLI

### Homebrew installation

```plain text
brew install quarylabs/quary/quary

```

### Linux/Mac through curl

Quary can be installed using curl on Linux/Mac using the following command:

```plain text
curl -fsSL https://raw.githubusercontent.com/quarylabs/quary/main/install.sh | bash
```

### Other installations

Other builds are available in the releases page to download.

### Usage

Once installed, a sample project can be created and run as follows:

```plain text
mkdir example # create an empty project folder
cd example
quary init    # initialize DuckDB demo project with sample data
quary compile # validate the project structure and model references without database
quary build   # build and execute the model views/seeds against target database
quary test -s   # run defined tests against target database
```

## 🅀 Community

Join our Slack channel, for help, ideas, and discussions.

## Support

If you run into any problems using Quary, please let us know. We want Quary to be easy-to-use, so if you are getting confused, it is our fault, not yours. Create an issue and we'll be happy to help you out.

### Check out our other projects

SQRUFF, a compact, high-speed SQL linter, engineered with Rust efficiency.


