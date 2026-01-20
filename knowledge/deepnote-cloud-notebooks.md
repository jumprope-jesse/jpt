# Deepnote - Collaborative Cloud Data Notebooks

## Overview
Deepnote is a cloud-based collaborative notebook platform for data teams, combining Python, SQL, and R in one environment. Focus areas: team collaboration, enterprise security (HIPAA/SOC 2), and AI-assisted workflows.

## Key Features
- **Multi-language**: Python, SQL, R in same notebook
- **AI co-pilot**: Code generation, explanation, debugging, autocomplete (context-aware)
- **Notebook generation**: Create detailed notebooks from prompts
- **No-code visualizations**: Configure charts without code from DataFrames
- **Version control**: Full history of changes, notebook logs
- **Scheduling**: Hourly, daily, weekly, monthly notebook runs
- **Apps/dashboards**: Convert notebooks to interactive apps, hide code, add inputs/buttons

## Collaboration Features
- Cloud-based (no local setup)
- Real-time commenting on blocks
- Share via link or email invite
- Folder organization for projects
- Role-based access controls

## Security & Compliance
- HIPAA compliant
- SOC 2 Type II compliant
- Encrypted credentials (no sharing raw secrets)
- SSO via SAML/OIDC
- Directory sync

## Integrations
- Data warehouses: BigQuery, Snowflake, Redshift, etc.
- dbt metadata (Jinja, metrics browsing)
- CSV drag-and-drop upload
- Public API for automation

## Comparison to Alternatives
| Feature | Deepnote | Briefer | marimo | Pretzel | Jupyter |
|---------|----------|---------|--------|---------|---------|
| Hosting | Cloud | Cloud | Local | Local | Local |
| Storage | Cloud | Cloud | Pure Python | .ipynb | .ipynb |
| Multi-language | Python/SQL/R | Python/SQL | Python | Python | Multi via kernels |
| AI built-in | Yes | Yes | No | Yes | Extensions |
| Scheduling | Yes | Yes | External | No | External |
| Dashboards | Yes | Yes | Via apps | Planned | Via Voila |
| HIPAA/SOC 2 | Yes | No | N/A | N/A | N/A |
| Collaboration | Real-time | Comments | No | Planned | Via JupyterHub |

## Pricing
Free tier available. Enterprise pricing for compliance features.

## Links
- Website: https://deepnote.com/
- Community: 3,000+ members

## Related
- [[briefer-cloud-notebooks]] - Similar cloud notebook, simpler feature set
- [[marimo-python-notebook]] - Local-first reactive notebooks
- [[pretzel-ai-jupyter-fork]] - AI-enhanced local Jupyter
- Hex - Another cloud notebook platform
