# pdfly - CLI Tool for PDF Manipulation

*Source: https://chezsoi.org/lucas/blog/spotlight-on-pdfly.html - Added: 2026-01-18*

pdfly is a Python CLI tool for manipulating PDF files. Part of the py-pdf organization, created by Martin Thoma in 2022. Built on fpdf2 and pypdf libraries.

**Project docs**: https://pdfly.readthedocs.io

## Installation

```bash
pip install pdfly
```

## Key Commands

### Metadata

```bash
# Display PDF metadata
pdfly meta document.pdf

# Display page-level metadata
pdfly pagemeta document.pdf
```

### Document Manipulation

```bash
# Merge PDFs
pdfly cat file1.pdf file2.pdf -o merged.pdf

# Extract specific pages
pdfly extract-annotated-pages document.pdf -o annotated-only.pdf

# Rotate pages
pdfly rotate document.pdf --pages 1,3,5 --angle 90
```

### Digital Signatures

```bash
# Sign a PDF
pdfly sign document.pdf --key private.key --cert certificate.pem

# Verify signature
pdfly check-sign document.pdf
```

## Why It's Useful

- **Free and open source** - no cost for basic PDF operations
- **Scriptable** - easy to automate PDF workflows
- **Extract annotated pages** - useful for reviewing/reworking sections of large documents
- **Digital signatures** - sign and verify PDFs from command line
- **Metadata inspection** - quickly see what's in a PDF

## Comparison to Other Tools

| Tool | Type | Best For |
|------|------|----------|
| pdfly | CLI, Python | Automation, scripting, batch operations |
| poppler-utils | CLI, C++ | Text extraction, conversion, merging |
| Nano PDF | AI-powered CLI | Natural language editing of content |
| PlutoPrint | Python | HTML-to-PDF generation |
| Preview (macOS) | GUI | Quick visual edits |
| Adobe Acrobat | GUI | Full-featured editing |

## Related

- [[ai-pdf-tools]] - AI-powered PDF tools like Nano PDF
- [[plutoprint-html-to-pdf]] - HTML-to-PDF/image generation
- [[poppler-pdf-library]] - C++ PDF library with CLI tools (poppler-utils)
- pypdf - Python library pdfly is built on
- fpdf2 - Another Python PDF library used by pdfly
