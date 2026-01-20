# Diagrams - Python Architecture Diagrams as Code

Python library for creating cloud architecture diagrams programmatically.

**Links:** [GitHub](https://github.com/mingrammer/diagrams) | [Docs](https://diagrams.mingrammer.com/)

## Installation

```bash
pip install diagrams
# Requires Graphviz
brew install graphviz  # macOS
```

## Basic Usage

```python
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("Web Service", show=False):
    ELB("lb") >> EC2("web") >> RDS("db")
```

Generates a PNG diagram automatically.

## Supported Providers

- **Cloud:** AWS, Azure, GCP, IBM Cloud, Alibaba Cloud, Oracle Cloud, DigitalOcean
- **On-Premise:** Generic infrastructure nodes
- **Kubernetes:** K8s components
- **OpenStack:** Cloud infrastructure
- **SaaS:** Snowflake, Slack, Teams, Telegram, Okta, etc.
- **Generic:** Custom nodes for anything not covered

## Key Features

- **Diagram as Code** - Version control your architecture diagrams
- **Automated docs** - Generate visuals from infrastructure definitions
- **Change tracking** - Git diffs show diagram evolution
- **Multi-cloud** - Support for all major providers in one diagram
- **Clusters** - Group nodes into logical clusters

## Comparison with Other Tools

| Tool | Approach | Best For |
|------|----------|----------|
| **Diagrams (Python)** | Code-first | Automated infra docs, CI pipelines |
| **Mermaid** | Text markup | GitHub READMEs, quick diagrams |
| **GG Charts** | GUI | Quick manual diagrams, privacy |
| **draw.io** | GUI | Complex manual diagrams |

## When to Use

- Documenting cloud architecture that changes frequently
- Generating diagrams in CI/CD pipelines
- Keeping architecture docs in sync with infrastructure as code
- Team standardization on diagram style
