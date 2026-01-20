---
type: link
source: notion
url: https://github.com/nlmatics/nlm-ingestor
notion_type: Software Repo
tags: ['Example']
created: 2024-01-24T12:06:00.000Z
---

# nlmatics/nlm-ingestor: This repo provides the server side code for llmsherpa API to connect. It includes parsers for varioius file formats.

## AI Summary (from Notion)
- Repo Purpose: Provides server-side code for llmsherpa API, including parsers for various file formats.
- Key Parsers:
- PDF Parser: Utilizes text coordinates and offers OCR capabilities; designed for structured data extraction.
- HTML Parser: Creates layout-aware blocks to enhance RAG performance.
- Text Parser: Analyzes text to identify lists, tables, and headers without visual input.
- Support for DOCX, PPTX: Processes these formats using HTML output from Tika.
- Nlm Modified Tika: Custom version of Tika included in the repo, with a compiled JAR file provided.
- Installation: Steps to install Java, run Tika server, and use Docker for deployment.
- Performance Insights: Rule-based parser is significantly faster than model-based parsers and requires minimal hardware.
- Development Philosophy: Preference for rule-based approaches due to their speed and reliability, especially for large text-layer PDFs.
- Credits and Contributions: Acknowledges various contributors to the project and highlights the foundational tools used (Apache PDFBox and Tika).
- Important Links: References to notebooks for experimenting with the PDF parser and testing the server.

## Content (from Notion)

# About

This repo provides the service code for llmsherpa API to connect. This repo contains custom RAG (retrieval augmented generation) friendly parsers for the following file formats:

### PDF

The PDF parser is a rule based parser which uses text co-ordinates (boundary box), graphics and font data from nlmatics modified version of tika found here https://github.com/nlmatics/nlm-tika. The PDF parser works off text layer and also offers a OCR option (apply_ocr) to automatically use OCR if there are scanned pages in your PDFs. The OCR feature is based off a nlmatics modified version of tika which uses tesseract underneath. Check out the notebook pdf_visual_ingestor_step_by_step to experiment directly with the PDF parser.

The PDF Parser offers the following features:

1. Sections and subsections along with their levels.
1. Paragraphs - combines lines.
1. Links between sections and paragraphs.
1. Tables along with the section the tables are found in.
1. Lists and nested lists.
1. Join content spread across pages.
1. Removal of repeating headers and footers.
1. Watermark removal.
1. OCR with boundary boxes
### HTML

A special HTML parser that creates layout aware blocks to make RAG performance better with higher quality chunks.

### Text

A special text parser which tries to figure out lists, tables, headers etc. purely by looking at the text and no visual, font or bbox information.

### DOCX, PPTX and any other format supported by Apache Tika

There are two ways to process these types of documents

- html output from tika for these file types is used and parsed by the html parser
## Nlm Modified Tika

Nlm modified version of Tika can be found in the 2.4.1-nlm branch here https://github.com/nlmatics/nlm-tika/tree/2.4.1-nlm For convenience, a compiled jar file of the code is included in this repo in jars/ folder. In some cases, your PDFs may result in errors in the Java server and you will need to modify the code there to resolve the issue and recompile the jar file.

## Installation steps:

### Run each step directly

1. Install latest version of java from https://www.oracle.com/java/technologies/downloads/
1. Run the tika server:
```plain text
 java -jar <path_to_nlm_ingestor>/jars/tika-server-standard-nlm-modified-2.4.1_v6.jar

```

1. Install the ingestor
```plain text
!pip install nlm-ingestor

```

1. Run the ingestor
```plain text
python -m nlm_ingestor.ingestion_daemon

```

### Run the docker file

A docker image is available via public github container registry.

Pull the docker image

```plain text
docker pull ghcr.io/nlmatics/nlm-ingestor:latest

```

Run the docker image mapping the port 5001 to port of your choice.

```plain text
docker run -p 5010:5001 ghcr.io/nlmatics/nlm-ingestor:latest-<version>

```

Once you have the server running, your llmsherpa url will be: "http://localhost:5010/api/parseDocument?renderFormat=all"

- to apply OCR add &applyOcr=yes
- to use the new indent parser which uses a different alogrithm to assign header levels, add &useNewIndentParser=yes
- this server is good for your development - in production it is recommended to run this behind a secure gateway using nginx or cloud gateways
### Test the ingestor server

Sample test code to test the server with llmsherpa parser is in this notebook.

## Rule based parser vs model based parser

Over the course of 4 years, nlmatics team evaluated a variety of options including a yolo based vision parser developed by Tom Liu and Yi Zhang. Ultimately, we settled with the rule based parser due to the following reasons.

1. It is substantially (100x) faster compared to any vision parser as bare miniumum you have to create images out of all pages of a PDF (even for the ones with text layer) to use a vision parser. It is our opinion that vision parser is a better option for OCRd PDF without a text layer, or for small PDF files consisting form like data, but for larger text layer PDFs, spanning hundreds of pages, a rule based parser like ours is more practical.
1. No special hardware is needed to run this parser if you are not using the PDF OCR feature. You can run this with hardware from early 2000s!
1. We found vision parser (or any parser for that matter including this) to be error prone and the solution to fix errors in a model were not pretty: 
## Credits

The PDFparser visual_ingestor and new_indent_parser was written by Ambika Sukla with additional contributions from Reshav Abraham who wrote the initial code to modify tika, Tom Liu who wrote the original Indent Parser and Kiran Panicker who made several improvements to the parsing speed, table parsing accuracy, indent parsing accuracy and reordering accuracy.

The HTML Ingestor was written by Tom Liu.

The Markdown Parser was written by Yi Zhang.

The Text Ingestor was written by Reshav Abraham.

The XML Ingestor was written by Ambika Sukla primarily to process PubMed XMLs.

The line_parser which serves as a core sentence processing utility for all the other parsers was written by Ambika Sukla.

Also we are thankful to the Apache PDFBox and Tika developer community for their years of work in providing the base for the PDF Parser.


