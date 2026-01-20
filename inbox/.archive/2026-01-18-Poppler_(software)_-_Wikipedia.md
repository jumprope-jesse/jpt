---
type: link
source: notion
url: https://en.wikipedia.org/wiki/Poppler_(software)#poppler-utils
notion_type: Software Repo
tags: ['Running']
created: 2025-10-13T11:34:00.000Z
---

# Poppler (software) - Wikipedia

## Overview (from Notion)
- Poppler is a free and open-source PDF rendering library that can enhance your document handling and processing tasks in software development.
- With its robust features, it allows for easy integration of PDF functionalities into applications, beneficial for creating tools or platforms that involve document management.
- The library supports various back-ends, which means you can optimize performance based on your specific needs, whether on Linux or other platforms.
- Using Poppler's command-line utilities can streamline workflows, such as converting documents, extracting text, or managing PDF attachments—ideal for automating tasks in a busy life.
- The emphasis on open-source software aligns with community-driven development, which can inspire you as a founder to contribute to or build upon existing projects.
- Consider the implications of efficient document management in a bustling city like NYC, where quick access to information can save time and enhance productivity.
- An alternate view might consider the dependence on proprietary software, questioning the trade-offs between ease of use and the flexibility offered by open-source alternatives like Poppler.

## AI Summary (from Notion)
Poppler is a free and open-source software library for rendering PDF documents, primarily used on Linux systems and supported by freedesktop.org. It originated as a fork of Xpdf and aims to centralize PDF rendering functionalities. Notable applications using Poppler include Evince, GIMP, and LibreOffice. It features multiple back-ends for drawing PDFs, supports basic annotations and Acroforms, and includes a suite of command-line utilities for managing PDFs, such as pdfinfo and pdftotext.

## Content (from Notion)

Poppler is a free and open-source software library for rendering Portable Document Format (PDF) documents. Its development is supported by freedesktop.org. Commonly used on Linux systems,[4] it powers the PDF viewers of the GNOME and KDE desktop environments.

## History

[edit]

The project was started by Kristian Høgsberg with two goals:[5] to provide PDF rendering functionality as a shared library, to centralize maintenance effort and to go beyond the goals of Xpdf, and to integrate with functionality provided by modern operating systems.

By the version 0.18 release in 2011, the poppler library represented a complete implementation of ISO 32000-1,[4] the PDF format standard, and was the first major free PDF library to support its forms (only Acroforms but not full XFA forms)[6][7] and annotations features.[4]

Poppler is a fork of Xpdf-3.0, a PDF file viewer developed by Derek Noonburg of Glyph and Cog, LLC.[5][8]

The name Poppler comes from "The Problem with Popplers," an episode of the animated series Futurama.[8]

## Applications

[edit]

Notable free software applications using Poppler to render PDF documents include:[9]

## Features

[edit]

Poppler can use two back-ends for drawing PDF documents, Cairo and Splash. Its features may depend on which back-end it employs. A third back-end based on Qt4's painting framework "Arthur", is available, but is incomplete and no longer under active development.[11] Bindings exist for Glib and Qt5, that provide interfaces to the Poppler backends, although the Qt5 bindings support only the Splash and Arthur backends. There is a patchset available to add support for the Cairo backend to the Qt5 bindings,[12] but the Poppler project does not currently wish to integrate the feature into the library proper.[13]

Some characteristics of the back-ends include:

- Cairo: Anti-aliasing of vector graphics, and transparent objects.
- Splash: Supports minification filtering of bitmaps.
Poppler comes with a text-rendering back-end as well, which can be invoked from the command line utility pdftotext. It is useful for searching for strings in PDFs from the command line, using the utility grep, for instance.[14]

Example:

```plain text
pdftotext file.pdf - | grep string

```

Poppler partially supports annotations and Acroforms. It does not support JavaScript[15] nor the rendering of full XFA forms.[6]

## poppler-utils

[edit]

poppler-utils is a collection of command-line utilities built on Poppler's library API, to manage PDF and extract contents:

- pdfattach – add a new embedded file (attachment) to an existing PDF
- pdfdetach – extract embedded documents from a PDF
- pdffonts – lists the fonts used in a PDF
- pdfimages – extract all embedded images at native resolution from a PDF
- pdfinfo – list all information of a PDF
- pdfseparate – extract single pages from a PDF
- pdftocairo – convert single pages from a PDF to vector or bitmap formats using cairo
- pdftohtml – convert PDF to HTML format retaining formatting
- pdftoppm – convert a PDF page to a bitmap
- pdftops – convert PDF to printable PS format
- pdftotext – extract all text from PDF
- pdfunite – merges several PDFs
## See also

[edit]

- List of PDF software
- iText – another free and open-source PDF library
- MuPDF – a free and open-source rendering engine for PDF, XPS, and EPUB
## Notes

[edit]

[edit]

## External links

[edit]

- Official website
- Qt Quarterly: Poppler: Displaying PDF Files with Qt
- Poppler Utils 0.68.0 compiled for x86 Windows

