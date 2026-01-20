# Poppler - PDF Rendering Library

*Source: https://en.wikipedia.org/wiki/Poppler_(software) - Added: 2026-01-18*

Poppler is a free and open-source PDF rendering library, primarily used on Linux systems and supported by freedesktop.org. It powers PDF viewers for GNOME and KDE desktop environments.

**Official site**: https://poppler.freedesktop.org/

## History

- Forked from Xpdf-3.0 by Kristian Hogsberg
- Goals: provide PDF rendering as a shared library, centralize maintenance
- By v0.18 (2011): complete implementation of ISO 32000-1 (PDF standard)
- First major free PDF library to support Acroforms and annotations
- Name comes from "The Problem with Popplers" Futurama episode

## Notable Applications Using Poppler

- Evince (GNOME document viewer)
- Okular (KDE document viewer)
- GIMP
- Inkscape
- LibreOffice
- Scribus
- Zathura

## Rendering Back-ends

| Back-end | Features |
|----------|----------|
| **Cairo** | Anti-aliasing of vector graphics, transparent objects |
| **Splash** | Minification filtering of bitmaps |
| **Arthur** | Qt4 painting framework (incomplete, no longer developed) |

Bindings exist for Glib and Qt5. Qt5 bindings only support Splash and Arthur back-ends.

## poppler-utils CLI Tools

Command-line utilities for PDF manipulation:

| Command | Purpose |
|---------|---------|
| `pdfattach` | Add embedded file (attachment) to PDF |
| `pdfdetach` | Extract embedded documents from PDF |
| `pdffonts` | List fonts used in PDF |
| `pdfimages` | Extract all embedded images at native resolution |
| `pdfinfo` | List all PDF metadata |
| `pdfseparate` | Extract single pages from PDF |
| `pdftocairo` | Convert pages to vector or bitmap formats |
| `pdftohtml` | Convert PDF to HTML with formatting |
| `pdftoppm` | Convert PDF page to bitmap |
| `pdftops` | Convert PDF to PostScript |
| `pdftotext` | Extract all text from PDF |
| `pdfunite` | Merge multiple PDFs |

## Installation

```bash
# macOS
brew install poppler

# Linux (Ubuntu/Debian)
sudo apt-get install poppler-utils

# Windows
choco install poppler
```

## Common Usage Examples

```bash
# Extract text from PDF
pdftotext document.pdf output.txt

# Search PDF content from command line
pdftotext file.pdf - | grep "search term"

# Get PDF metadata
pdfinfo document.pdf

# Merge PDFs
pdfunite file1.pdf file2.pdf merged.pdf

# Extract specific pages
pdfseparate document.pdf page-%d.pdf

# Convert PDF to images
pdftoppm -png document.pdf output

# Extract all images from PDF
pdfimages -all document.pdf images/
```

## Limitations

- Does not support JavaScript in PDFs
- No full XFA forms rendering (only Acroforms)
- Some advanced PDF features may not render perfectly

## Why It's Useful

- **Foundation for many tools**: Powers Nano PDF, many document viewers
- **Text extraction**: Quick command-line access to PDF content
- **Batch processing**: Easy to script PDF operations
- **Cross-platform**: Works on Linux, macOS, Windows
- **Open source**: Free, well-maintained, community-supported

## Related

- [[pdfly-pdf-cli-tool]] - Python CLI built on pypdf (different library)
- [[ai-pdf-tools]] - AI-powered PDF tools (Nano PDF uses Poppler)
- MuPDF - Another open-source PDF rendering engine
- Xpdf - Original project Poppler forked from
