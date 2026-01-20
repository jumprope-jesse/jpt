# Browser Automation with LLMs

## Skyvern - LLM-Powered Browser Automation

*Source: https://github.com/Skyvern-AI/skyvern*
*Added: 2026-01-19*

### Overview

Skyvern automates browser workflows using LLMs and computer vision, eliminating the need for brittle XPath-based scripts. Inspired by BabyAGI/AutoGPT task-driven agent design, but with browser automation capabilities via Playwright.

**Key innovation**: Instead of code-defined selectors, uses computer vision + LLMs to:
- Parse visual elements in viewport in real-time
- Create interaction plans
- Execute actions

### Advantages Over Traditional Automation

1. **Works on unseen websites** - Maps visual elements to actions without custom code
2. **Resistant to layout changes** - No pre-determined XPaths/selectors
3. **Handles complexity** - LLM reasoning for edge cases (dropdowns, radio buttons, ambiguous forms)

### Architecture

- **Task**: API request (e.g., "get insurance quote")
- **Steps**: Individual webpage interactions
- **Actions**: Specific interactions (click, type, select) with reasoning

Built-in visualizer shows 1:1 action-to-screenshot mapping for debugging.

### Use Cases

- **Procurement automation** - Navigate supplier sites, fill forms
- **Government forms** - Account registration, submissions
- **Insurance quotes** - Multi-step forms in any language
- **Data extraction** - Scrape structured data with natural language goals

### API Example

```bash
curl -X POST -H 'Content-Type: application/json' \
  -H 'x-api-key: YOUR_KEY' \
  -d '{
    "url": "https://example.com",
    "navigation_goal": "Fill out contact form with provided data",
    "data_extraction_goal": "Extract confirmation number",
    "navigation_payload": "{\"name\": \"Jesse\", \"email\": \"test@example.com\"}"
  }' http://localhost:8000/api/v1/tasks
```

### Setup Requirements

- Python 3.11
- PostgreSQL 14
- Poetry for dependency management
- Playwright (installed via setup script)

```bash
git clone https://github.com/Skyvern-AI/skyvern
cd skyvern
./setup.sh
./run_skyvern.sh    # Start API server
./run_ui.sh         # Start Streamlit UI on localhost:8501
```

### Cloud vs Self-Hosted

**Self-hosted** (AGPL-3.0):
- Core automation logic
- Run locally or on your infrastructure

**Skyvern Cloud** (private beta):
- Parallel execution at scale
- Anti-bot detection
- Proxy network
- CAPTCHA solving

### Comparison to Other Tools

**vs Traditional Selenium/Playwright**:
- No selector maintenance
- Works across website redesigns
- Higher per-action cost (LLM calls)

**vs Playwright MCP** (see [claude-code-configuration.md](claude-code-configuration.md)):
- Playwright MCP: Write code → execute (one LLM call upfront)
- Skyvern: Inference at every step (higher cost, more adaptive)

**vs Manual Scripting**:
- Skyvern: Natural language task → automated
- Scripting: Full control, no LLM costs, breaks on layout changes

### When to Use

✅ **Good for**:
- One-off automations on unfamiliar sites
- Sites that frequently change layout
- Complex multi-step workflows with conditional logic
- Extracting data where structure isn't known upfront

❌ **Avoid for**:
- High-volume, cost-sensitive scraping (use traditional tools)
- Sites you control (write Playwright scripts directly)
- Simple, repetitive tasks on static sites

### Roadmap (as of 2024)

- Workflow chaining (multiple Skyvern calls in sequence)
- Prompt caching for cost savings
- React UI replacing Streamlit
- LLM observability integration
- Langchain integration

### Related Tools

- **Playwright** - Underlying browser automation
- **BabyAGI/AutoGPT** - Architectural inspiration
- **Claude Code Playwright Skill** - Similar concept, different execution model
