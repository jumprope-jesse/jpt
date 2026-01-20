# Pretzel - AI-Enhanced Jupyter Fork

## Overview
Pretzel is an open-source fork of Jupyter with integrated AI features for code generation, editing, and assistance. Key value prop: zero switching costs from Jupyter (all config, keybindings, extensions work out of the box).

## Key Features
- **Inline tab completion**: Uses Mistral's Codestral, triggers after 1 second pause
- **AI code generation/editing**: Cmd+K (Mac) / Ctrl+K (Win/Linux) in any cell
- **AI sidebar**: Ctrl+Cmd+B for chat, code generation, searching existing code
- **Error fixing**: One-click "Fix Error with AI" button
- **Code injection**: Start prompt with "inject" or "ij" to add code without editing existing

## Installation
```bash
pip install pretzelai
pretzel lab
```
Or use hosted version: https://pretzelai.app

## AI Configuration
- Uses free Pretzel AI server by default
- Can configure own OpenAI API key (Settings > Settings Editor > Pretzel AI Settings)
- Azure support also available
- Default model: GPT-4o (configurable)

## Comparison to Alternatives
| Feature | Pretzel | Thread | marimo | Briefer | Jupyter |
|---------|---------|--------|--------|---------|---------|
| Storage | .ipynb | .ipynb | Pure Python | Cloud | .ipynb |
| Reactive | No | No | Yes | No | No |
| AI built-in | Yes | Yes | No | Yes | Extensions only |
| Switching cost | None (fork) | Low | Medium | High (cloud) | N/A |
| Collaboration | Planned | Planned | No | Yes | Via JupyterHub |
| Frontend | JupyterLab | React (custom) | Custom | Cloud | JupyterLab |
| Local/free | Yes | Yes | Yes | No | Yes |

### Thread (squaredtechnologies/thread)
AI-powered Jupyter Notebook rebuilt with React frontend. Similar feature set to Pretzel but completely rewritten rather than forked. Key features:
- Natural language code generation and editing
- Context-aware chat sidebar
- Automatic error explanation and fixing
- Runs locally with your own API key

Install: `pip install thread-dev && thread`

GitHub: https://github.com/squaredtechnologies/thread

## License
AGPLv3 - free for individual and company use, but modifications must be open-sourced if redistributed.

## Privacy
- No personal info collected
- Anonymous telemetry for AI features only
- Prompts collected (can disable in settings)
- No code collected/stored
- Hosted version: data deleted 30 days after last login

## Roadmap
- Real-time collaboration (pair programming, comments, version history)
- SQL support (code cells and standalone SQL IDE)
- Visual analysis builder
- Monaco editor (VSCode-like experience)
- 1-click dashboard creation

## Links
- GitHub: https://github.com/pretzelai/pretzelai
- Hosted: https://pretzelai.app

## Related
- [[marimo-python-notebook]] - Reactive Python notebooks stored as pure Python
- [[briefer-cloud-notebooks]] - Cloud-based with dashboards and scheduling
- Cursor - Similar AI code editing UX (but for general code, not notebooks)
