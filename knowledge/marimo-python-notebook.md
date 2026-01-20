# marimo - Next-Generation Python Notebook

## Overview
marimo is an AI-native reactive Python notebook that addresses key pain points of traditional Jupyter notebooks. It stores notebooks as pure Python files (Git-friendly) and supports reactive execution where cells automatically re-run when dependencies change.

## Key Features
- **Reactive execution**: Cells automatically update when upstream dependencies change
- **Pure Python storage**: Notebooks are stored as `.py` files, enabling proper version control
- **Git-friendly**: No JSON merge conflicts like with `.ipynb` files
- **Reproducible**: Deterministic execution order based on cell dependencies
- **Multi-modal**: Run as notebooks, scripts, pipelines, or web apps
- **AI-native**: Built with AI/ML workflows in mind
- **SQL support**: Native SQL query capabilities

## Use Cases
- Data transformation and exploration
- Model training and experimentation
- Building data apps and dashboards
- Teaching/learning Python (reactive feedback)

## Installation
```bash
# With uv
uvx marimo edit

# With pip
pip install marimo
marimo edit
```

## Notable Users
- Johns Hopkins
- UC Berkeley
- Mozilla AI

## Links
- Website: https://marimo.io/
- Documentation: https://docs.marimo.io/

## Related
- Jupyter notebooks (traditional approach)
- Observable (reactive notebooks for JavaScript)
- Streamlit (Python apps, but not notebook-style)
