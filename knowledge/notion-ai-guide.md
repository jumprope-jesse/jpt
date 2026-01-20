# Notion AI Guide

**URL:** https://matthiasfrank.de/notion-features/notion-ai/
**Author:** Matthias Frank (same as notion-updates-resource.md)
**Added:** 2026-01-18
**Category:** Productivity Tools / AI Integration

## Overview

Comprehensive guide to Notion AI capabilities. Notion AI integrates LLMs (GPT-4, Claude) directly into the Notion workspace, providing AI assistance that understands your workspace context.

## Key Concept

Notion doesn't build its own LLM - it integrates existing models (OpenAI, Anthropic) and acts as an orchestration layer that:
- Selects the best model for each task
- Provides workspace context to the model
- Formats responses as native Notion elements (callouts, tables, etc.)

## Data Access

What Notion AI can access:
- All text content in pages you have access to
- AI Properties can work with database content
- Connected apps via Connectors (Slack, Google Drive, GitHub, Jira)

What it cannot access:
- Q&A feature cannot pull from database content directly
- External files (PDFs attached to pages)
- Web search / live internet

## Pricing (as of 2025)

- **Individual:** €9.50/month (€7.50/month annual)
- **Teams:** Per-seat pricing, must be workspace-wide
- **Education:** 50% discount with verification
- **Startups:** Free 6-month trial available

50% cheaper than ChatGPT Plus or Claude Pro (€19/month each).

## Core Features

### Block-Level AI
- Write/draft/edit any text
- Q&A search across workspace
- Explain complex topics
- Summarize highlighted text
- Translate to different languages
- Improve writing style/grammar
- Brainstorm ideas
- Visualize as flowcharts/tables
- Write code

### Database AI Properties
- **AI Summary:** Auto-summarize page content
- **AI Custom Autofill:** Custom prompts for any text generation
- **AI Translation:** Translate specific properties
- **AI Keywords:** Auto-generate tags/categories

### AI Database Builder (Feb 2025+)
Can create databases from natural language descriptions. Limitations:
- Single database at a time
- No relations between databases
- No formula generation
- Inconsistent with complex instructions

## Best Use Cases

1. **Knowledge Management Q&A** - Ask questions, get answers from your docs
2. **Style Guide Enforcement** - Reference @Brand Guidelines in prompts
3. **Meeting Note Processing** - Extract action items, summarize
4. **Content Translation** - Bulk translate via properties
5. **Data Organization** - Auto-tagging, categorization
6. **Hand-written Note Digitization** - Upload images, extract text
7. **Sample Data Generation** - Customer reviews, test data, etc.
8. **Sentiment Analysis** - Analyze customer feedback
9. **SOP Writing** - Generate step-by-step guides, then refine
10. **Red Teaming** - Generate counterarguments and risks

## AI Connectors

Available connectors (no extra cost):
- Slack (public channels only, 1 year history)
- Google Drive (docs, sheets, slides you have access to)
- GitHub (requires org membership, 1 year history)
- Jira
- Microsoft Teams (coming soon)

Setup: Settings → Connections → Workspace (36-72 hours to sync)

## Prompting Best Practices

1. Be extremely specific - LLMs can't read context clues
2. Use simple, clear language
3. A/B test prompt variations
4. Save working prompts as templates
5. Provide necessary context in the prompt
6. Ask for sources and verify them
7. Iterate and refine based on results

## Security

- Content not used for model training
- GDPR and CCPA compliant
- ISO 27001 certified
- Encryption during transfer and use
- Disconnecting a service deletes data within 24 hours

## Current Limitations

- Hallucination risk (always verify)
- Knowledge cutoff (late 2023 as of March 2025)
- No web search capability
- Cannot create pages programmatically
- No organization for chat history (unlike ChatGPT folders)
- Cannot read embedded PDFs

## ROI Calculation (from HBR study)

For 100-member team at €7.50/user/month:
- Cost: €9,000/year
- Estimated value: €92,400/year (based on 2.7 queries/day, 33% adoption)
- Theoretical ROI: 927%

Note: Assumes consistent usage and adoption. Real results will vary.

## Related

- See also: [[notion-updates-resource.md]] for feature tracking
