# Knowledge

Reference material processed from the inbox. General knowledge outside of direct work and personal life.

## What Goes Here

- Tech industry trends, tools, techniques
- Leadership and management insights
- Parenting approaches and resources
- Economics, finance, policy
- Books and ideas that shape thinking
- Anything worth remembering that isn't a task, person, or active project

## Structure

Files are organized organically by the **Knowledge Curator** (automated nightly agent). Subfolders are created when a topic cluster reaches 5+ files:

```
knowledge/
├── aws/            → AWS services and features
├── ai/             → AI/ML tools, agents, patterns
│   └── agents/     → Agent-specific architecture (max 2 levels deep)
├── django/         → Django framework and ecosystem
├── tools/          → Developer tools, productivity apps
└── (more as patterns emerge)
```

## File Naming

Use descriptive kebab-case names:
- `react-server-components.md`
- `engineering-leadership-principles.md`
- `toddler-sleep-training.md`

## Automated Curation

Two agents maintain this directory:

### Nightly Curator (`knowledge_curator.py`)
Runs at 2am daily. Analyzes recent changes and:
- Creates subfolders when clusters reach 5+ files
- Merges related small files into cohesive topics
- Moves files into appropriate subfolders
- Opens a **PR for review** (no auto-commit)

### Weekly Reviewer (`knowledge_reviewer.py`)
Runs Sunday 3am. Reviews for staleness using context-aware rules:
- **Philosophy/frameworks**: Rarely archive (compounds over time)
- **News/predictions**: Archive after 3-6 months if topic inactive
- **Tool docs**: Keep active tools, archive abandoned
- **Trends**: Archive when mainstream or dead

Opens a **PR for review** with archival recommendations.

### Manual Commands
```bash
# Nightly curator
python3 ~/jpt/lib/knowledge_curator.py status    # Show clusters
python3 ~/jpt/lib/knowledge_curator.py dry-run   # Preview changes
python3 ~/jpt/lib/knowledge_curator.py run       # Run and create PR

# Weekly reviewer
python3 ~/jpt/lib/knowledge_reviewer.py status   # Staleness report
python3 ~/jpt/lib/knowledge_reviewer.py dry-run  # Preview archival
python3 ~/jpt/lib/knowledge_reviewer.py run      # Run and create PR

# View logs
tail -f ~/jpt/lib/.curator.log
```

## Archive

Old or outdated knowledge moves to `.archive/` rather than being deleted. The weekly reviewer handles this automatically via PR.
