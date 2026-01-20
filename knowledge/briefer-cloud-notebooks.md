# Briefer - Cloud-Based Data Notebooks

## Overview
Briefer is a cloud-based notebook platform designed for data analysis, supporting SQL and Python in a collaborative environment. Launched July 2024. Key differentiator: combines notebook workflow with dashboard publishing and built-in AI assistance.

## Key Features
- **Block-based structure**: Text, SQL queries, Python code, file uploads, inputs, visualizations
- **SQL + Python integration**: Query databases directly, results auto-convert to Pandas dataframes
- **File support**: Upload CSV, XLSX, Parquet files and query them with SQL
- **AI assistant**: Built into SQL and Python blocks for suggestions and error fixing
- **Scheduling**: Run notebooks on intervals (hourly, daily, weekly) with email/Slack notifications
- **Version control**: Automatic snapshots on publish and scheduled runs
- **Collaboration**: Comments, configurable access permissions, public sharing links
- **Dashboards**: Convert notebook outputs to dashboards (hide code, expose results)

## Database Connections
Supports Postgres, BigQuery, Redshift, Athena, and others.

## Comparison to Alternatives
| Feature | Briefer | Deepnote | marimo | Jupyter |
|---------|---------|----------|--------|---------|
| Storage | Cloud | Cloud | Pure Python files | JSON (.ipynb) |
| Reactive | No | No | Yes | No |
| SQL native | Yes | Yes | Yes | Via extensions |
| Dashboards | Built-in | Built-in | Via apps | Via Voila/Panel |
| Scheduling | Built-in | Built-in | External | External |
| AI assist | Built-in | Built-in | No | Via extensions |
| HIPAA/SOC 2 | No | Yes | N/A | N/A |

## Use Cases
- Team data analysis with non-technical stakeholders (dashboard sharing)
- Scheduled data reports with notifications
- Quick SQL exploration without local setup
- Combining data from multiple sources (files + databases)

## Links
- Website: https://briefer.cloud/

## Related
- [[marimo-python-notebook]] - Local-first reactive Python notebooks
- [[deepnote-cloud-notebooks]] - Similar cloud notebook, more enterprise features (HIPAA/SOC 2)
- Hex (similar cloud notebook platform)
