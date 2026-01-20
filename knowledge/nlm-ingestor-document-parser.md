# nlm-ingestor - RAG-Optimized Document Parser

*Source: [GitHub - nlmatics/nlm-ingestor](https://github.com/nlmatics/nlm-ingestor) - Added: 2026-01-19*

Server-side document parsing for [llmsherpa](https://github.com/nlmatics/llmsherpa) API. Provides RAG-friendly parsers that create layout-aware chunks with structural information (sections, tables, lists) for better retrieval.

## Why It Matters

Most RAG systems use naive chunking (split every N characters), which breaks:
- Tables across chunks
- Section context
- List hierarchies
- Headers from their content

This parser uses text coordinates, fonts, and graphics to preserve document structure, making chunks more semantically meaningful.

## Supported Formats

### PDF (Primary Focus)
Rule-based parser using text coordinates from modified Apache Tika.

**Features:**
- Sections and subsections with hierarchy levels
- Paragraph detection (combines lines)
- Table extraction with section context
- Nested lists
- Content joining across pages
- Header/footer removal
- Watermark removal
- OCR with bounding boxes (optional)

### HTML
Layout-aware blocks for better chunking quality.

### Text
Pure text analysis to infer lists, tables, headers without visual information.

### Office Formats (DOCX, PPTX)
Via Apache Tika → HTML → HTML parser.

## Architecture

```
Document → Tika (text coords, fonts, graphics)
         → Parser (rule-based structure detection)
         → Structured chunks (sections, tables, lists)
         → RAG system
```

## Installation

### Option 1: Docker (Recommended)

```bash
# Pull image
docker pull ghcr.io/nlmatics/nlm-ingestor:latest

# Run (maps port 5001 → 5010)
docker run -p 5010:5001 ghcr.io/nlmatics/nlm-ingestor:latest
```

### Option 2: Direct

```bash
# 1. Install Java (required for Tika)
# Download from https://www.oracle.com/java/technologies/downloads/

# 2. Start Tika server
java -jar /path/to/nlm-ingestor/jars/tika-server-standard-nlm-modified-2.4.1_v6.jar

# 3. Install ingestor
pip install nlm-ingestor

# 4. Run daemon
python -m nlm_ingestor.ingestion_daemon
```

## Usage with llmsherpa

```python
from llmsherpa.readers import LayoutPDFReader

# Point to your local server
llmsherpa_api_url = "http://localhost:5010/api/parseDocument?renderFormat=all"
pdf_url = "https://example.com/document.pdf"  # or local file path
pdf_reader = LayoutPDFReader(llmsherpa_api_url)
doc = pdf_reader.read_pdf(pdf_url)

# Access structured content
for section in doc.sections():
    print(f"Section: {section.title}")
    for paragraph in section.paragraphs:
        print(paragraph.text)
    for table in section.tables:
        print(table.to_html())
```

## API Options

Base URL: `http://localhost:5010/api/parseDocument?renderFormat=all`

**Query parameters:**
- `&applyOcr=yes` - Enable OCR for scanned pages
- `&useNewIndentParser=yes` - Use improved header level detection algorithm

## Rule-Based vs Vision-Based Parsers

The team chose rule-based over YOLO vision parser despite having both:

**Rule-based advantages:**
- **100x faster** - No image rendering needed for text-layer PDFs
- **No special hardware** - Runs on minimal resources
- **More practical for large PDFs** - Hundreds of pages, text-heavy documents

**When vision parsers win:**
- OCR'd PDFs without text layer
- Small form-like documents
- Complex visual layouts

For large text-layer PDFs (contracts, reports, papers), rule-based is more practical.

## Technical Details

**Modified Apache Tika:**
Custom fork with enhanced PDF extraction: [nlmatics/nlm-tika](https://github.com/nlmatics/nlm-tika/tree/2.4.1-nlm)

**Key components:**
- `visual_ingestor` - Main PDF parser using bounding boxes
- `new_indent_parser` - Improved header hierarchy detection
- `line_parser` - Core sentence processing for all parsers
- OCR via Tesseract (when enabled)

## Production Considerations

- For development: Use directly as shown
- For production: Run behind nginx or cloud gateway for security
- No special hardware needed (unless using OCR)
- 15-min timeout recommended per document

## Use Cases

1. **Legal/Contract Analysis** - Preserve clause structure and table data
2. **Research Papers** - Maintain section hierarchy and citations
3. **Technical Documentation** - Keep code blocks, tables, and lists intact
4. **Financial Reports** - Extract tables with contextual headers
5. **Medical Records** - Preserve structured patient data

## Integration with RAG Pipelines

Fits into RAG maturity Level 6 (Advanced Data Handling):

```
Documents → nlm-ingestor (structure extraction)
          → Chunks with metadata (section, table_context, list_level)
          → Embed with structural context
          → Better retrieval (semantic + structural)
```

## Credits

Developed by nlmatics team over 4 years:
- **Ambika Sukla** - visual_ingestor, new_indent_parser, XML parser, line_parser
- **Reshav Abraham** - Tika modifications, text ingestor
- **Tom Liu** - Original indent parser, HTML parser
- **Yi Zhang** - Markdown parser
- **Kiran Panicker** - Performance, table parsing, reordering improvements

Built on Apache PDFBox and Tika.

## Related

- `rag-maturity-levels.md` - Where document parsing fits (Level 6)
- `cognita-rag-framework.md` - RAG framework that could use this parser
- `llmsherpa` - Python client for consuming this API
- `poppler-pdf-library.md` - Alternative PDF rendering library
