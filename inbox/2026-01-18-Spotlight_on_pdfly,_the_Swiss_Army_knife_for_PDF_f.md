---
type: link
source: notion
url: https://chezsoi.org/lucas/blog/spotlight-on-pdfly.html
notion_type: Tech Deep Dive
tags: ['Running']
created: 2025-10-13T11:34:00.000Z
---

# Spotlight on pdfly, the Swiss Army knife for PDF files

## Overview (from Notion)
- Streamlined Workflow: pdfly can automate routine PDF tasks, saving you time for family and projects.
- Educational Tool: Use it to teach your kids about digital document management and organization.
- Cost-Effective: As a free tool, it helps keep operational costs down for your startup.
- Open-Source Contribution: Engage your children or team in open-source culture, fostering skills and community involvement.
- Unique Features: The ability to extract annotated pages or rotate documents can be particularly useful for presentations or family projects.
- Feedback Loop: Encourage a culture of feedback at work; the tool thrives on user input, promoting a collaborative atmosphere.
- Alternate Views: Consider the environmental impact of digital vs. physical documents; pdfly reduces paper waste.

## AI Summary (from Notion)
pdfly is a Python CLI tool for manipulating PDF files, offering features like displaying metadata, merging documents, extracting content, and fixing manually edited PDFs. The latest release (0.5.0) introduces new functionalities such as signing PDFs, extracting annotated pages, and rotating pages. The project encourages contributions and feedback from users, especially for new features aimed at enhancing usability.

## Content (from Notion)

pdfly logo

Project documentation: pdfly.readthedocs.io

pdfly is the youngest project of the py-pdf organization. It has been created by Martin Thoma in 2022.

It's simply a CLI tool to manipulate PDF files, written in Python and based on the fpdf2 & pypdf libraries.

I'm a maintainer of the project 🙂

## What can it do?

It has meany features, including:

- display PDF metadata using pdfly meta and pdfly pagemeta commands. Example:
```plain text
$ pdfly meta minimal-document.pdf
                      Operating System Data
┏━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃         Attribute ┃ Value                     ┃
┡━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│         File Name │ /tmp/minimal-document.pdf │
│  File Permissions │ -rw-r--r--                │
│         File Size │ 16,978 bytes              │
│     Creation Time │ 2025-10-13 09:44:32       │
│ Modification Time │ 2025-10-13 09:44:32       │
│       Access Time │ 2025-10-13 09:44:46       │
└───────────────────┴───────────────────────────┘
                       PDF Data
┏━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃          Attribute ┃ Value                                                    ┃
┡━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│       CreationDate │ 2022-04-03 18:05:42+02:00                                │
│            Creator │ TeX                                                      │
│           Producer │ pdfTeX-1.40.23                                           │
│              Pages │ 1                                                        │
│          Encrypted │ None                                                     │
│   PDF File Version │ %PDF-1.5                                                 │
│        Page Layout │                                                          │
│          Page Mode │                                                          │
│             PDF ID │ ID1=b'q\x96\xc3\xe3U\xc1|\x9fS\xba\x9a\r\xcap\xcd\xd0'   │
│                    │ ID2=b'q\x96\xc3\xe3U\xc1|\x9fS\xba\x9a\r\xcap\xcd\xd0'   │
│ Fonts (embedded) │                                                          │
│   Fonts (embedded) │ /KNEUFH+CMR10                                            │
│        Attachments │ []                                                       │
│             Images │ 0 images (0 bytes)                                       │
└────────────────────┴──────────────────────────────────────────────────────────┘

```

- 
- 
- 
## Release 0.5.0 & new features

Today we released a new version: pdfly release 0.5.0.

Thanks to several contributors, including developers taking part in Hacktoberfest, new exciting features have been added:

- pdfly sign allows you to easily sign PDF documents, while pdfly check-sign makes it easy to check a PDF document signature. Thanks to @moormaster for implementing this in PRs #165 & #166 👍🙏.
- pdfly extract-annotated-pages extract only annotated pages from a PDF, hence helping to review or rework pages from a large document iteratively. Thanks to Hal Wine (@hwine) for implementing this in PR #128 👍🙏.
- pdfly rotate rotate specific pages of a document. Thanks to Subhajit Sahu (@wolfram77) for implementing this in PR #98 👍🙏.
## What's next?

We have a bunch of feature ideas: up-for-grabs issues, including some good first issues aimed specially at new contributors, that are willing to help but new to open-source.

Personally, I think the pdfly sign & check-sign could become handy to many end-users, and I think we should continue to extend those commands usage options, as described in issue #71.

We would also be happy to get your feedbacks, bug reports & feature suggestions! 🙂


