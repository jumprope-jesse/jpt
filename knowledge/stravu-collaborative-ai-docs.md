# Stravu - Collaborative AI Document Platform

**URL:** https://stravu.com/
**Category:** AI Tools / Collaborative Writing / Knowledge Work
**Added:** 2026-01-18

## Overview

Stravu is a collaborative AI platform focused on editable, approvable AI-generated content. Unlike chatbot-style AI tools, Stravu emphasizes human control over AI outputs with diff/approval workflows and multi-person collaboration.

## Key Differentiators

- **Editable AI Output**: Generate text, tables, diagrams, and formulas that you can manually edit
- **Diff & Approval Workflow**: AI additions shown in green, cuts in red - review and approve changes
- **Confidence Scoring**: AI rates its confidence in research results, hides low-confidence answers
- **Team Collaboration**: Multi-person doc editing with AI, collaborative chat threads
- **Project Context**: Groups notebooks, documents, and websites so AI understands your domain

## Content Types

| Type | Description |
|------|-------------|
| Text | Generate and edit prose, have AI revise |
| Tables | Create tables, edit cells/rows/columns, filter and arrange |
| Diagrams | Generate and manually edit diagrams |
| 2x2 Comparisons | Turn research into editable comparison matrices |
| Formulas | AI-generated computational formulas that auto-recalculate |

## Features

- **Notebook AI Agents**: Chat with AI that can research web + your documents, update notebooks
- **Multi-person editing**: Real-time collaboration with team and AI simultaneously
- **Reusable prompts**: Build consistent, repeatable AI workflows
- **Search**: Search workspace for keywords, chats, notebooks, projects
- **Privacy**: Hosted on AWS, does not train on user data

## Potential Use Cases

- Collaborative research documents with approval gates
- Team knowledge bases with AI assistance
- Business analysis with confidence-scored research
- Document workflows needing human review of AI changes

## Related: Crystal (Claude Code Session Manager)

Stravu also built **Crystal**, a macOS desktop app for managing multiple Claude Code sessions in parallel. It uses git worktrees for isolation and integrates with Stravu's notebook system for business/dev team collaboration. See `knowledge/coding-agent-tools.md` for full details.

## Notes

- Differentiates from pure chatbot tools by emphasizing human editing/approval
- Confidence scoring addresses hallucination concerns
- Project context feature could help with domain-specific accuracy
