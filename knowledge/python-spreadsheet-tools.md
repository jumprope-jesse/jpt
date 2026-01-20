# Python Spreadsheet Tools

Browser-based tools combining spreadsheet interfaces with Python data analysis.

## PySheets

https://pysheets.app/

Spreadsheet UI for Python with client-side execution. Everything runs in the browser including PySheets itself (built with Python/Pyodide).

### Key Features
- Import/export Excel sheets
- Pandas for data exploration
- Matplotlib for visualizations
- AI-driven analysis assistance
- Collaboration on shared sheets
- No server/kernel setup required
- Can load arbitrary Python packages and JS modules

### Pricing (as of 2024)
- **Free**: 5 sheets, 100 AI generations
- **Pro**: $19.99/month - unlimited sheets, collaboration
- **Enterprise**: On-prem, SSO, custom solutions

### Notes
- Public beta launched April 2024
- Built on LTK (open source Python UI toolkit)
- Aimed at bridging non-technical analysts and data scientists

---

## Probly

https://probly-ai.readthedocs.io/en/latest/features/overview/

Data analysis tool combining spreadsheets, Python, and AI assistance.

### Key Features
- **Spreadsheet interface**: Handsontable + HyperFormula (formulas, import/export, cell references)
- **AI assistant**: Natural language queries, formula generation, data transformation suggestions
- **Python integration**: Run pandas/numpy code directly on spreadsheet data, no setup required
- **Visualizations**: Bar, line, pie, scatter charts with AI-generated suggestions
- **Context-aware**: Remembers previous interactions and analysis patterns

### How It Works
The AI uses a tool-based approach for:
- Spreadsheet cell updates
- Chart creation
- Python code execution
- Extensible with more tools

---

## Comparison

| Feature | PySheets | Probly |
|---------|----------|--------|
| Client-side Python | Yes (Pyodide) | Yes |
| Excel import/export | Yes | Yes |
| AI assistance | Yes | Yes |
| Collaboration | Yes (Pro) | Unknown |
| Free tier | 5 sheets | Yes |
| Open source | No (uses OSS LTK) | Partial |

## Use Cases
- Quick data exploration without local Python setup
- Bridging spreadsheet users and data analysis
- Ad-hoc analysis and prototyping
- Teaching/demos (no install required)

## Related
- marimo - reactive Python notebooks (different paradigm, file-based)
- Jupyter notebooks - traditional computational notebooks
- Google Sheets + Apps Script - spreadsheet with scripting
