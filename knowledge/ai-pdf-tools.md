# AI-Powered PDF Tools

Tools for editing and manipulating PDF files using AI.

## Nano PDF

*Source: https://github.com/gavrielc/Nano-PDF - Added: 2026-01-18*

A CLI tool for editing PDF slides using natural language prompts, powered by Google's Gemini 3 Pro Image ("Nano Banana") model.

### Features

- **Natural Language Editing**: "Update the graph to include data from 2025", "Change the chart to a bar graph"
- **Add New Slides**: Generate entirely new slides that match your deck's visual style
- **Non-Destructive**: Preserves the searchable text layer using OCR re-hydration
- **Multi-page & Parallel**: Edit multiple pages in a single command with concurrent processing

### How It Works

1. **Page Rendering**: Converts target PDF pages to images using Poppler
2. **Style References**: Optionally includes style reference pages with generation request
3. **AI Generation**: Sends images + prompts to Gemini 3 Pro Image
4. **OCR Re-hydration**: Uses Tesseract to restore searchable text layer
5. **PDF Stitching**: Replaces original pages with AI-edited versions

### Installation

```bash
pip install nano-pdf
```

**System Dependencies:**
```bash
# macOS
brew install poppler tesseract

# Linux (Ubuntu/Debian)
sudo apt-get install poppler-utils tesseract-ocr

# Windows
choco install poppler tesseract
```

### Configuration

Requires a **paid** Google Gemini API key with billing enabled (free tier doesn't support image generation):

```bash
export GEMINI_API_KEY="your_api_key_here"
```

### Usage Examples

**Basic edit:**
```bash
nano-pdf edit my_deck.pdf 2 "Change the title to 'Q3 Results'"
```

**Multi-page edit:**
```bash
nano-pdf edit my_deck.pdf \
  1 "Update date to Oct 2025" \
  5 "Add company logo" \
  10 "Fix typo in footer"
```

**Add new slide:**
```bash
# Add a title slide at the beginning
nano-pdf add my_deck.pdf 0 "Title slide with 'Q3 2025 Review'"

# Add a slide after page 5
nano-pdf add my_deck.pdf 5 "Summary slide with key takeaways as bullet points"
```

**With style references:**
```bash
nano-pdf edit slides.pdf 1 "Make the header background blue" \
  --style-refs "2,3" --output branded_slides.pdf
```

### Options

| Option | Description |
|--------|-------------|
| `-use-context` | Include full PDF text as context (default for `add`) |
| `-no-use-context` | Disable context (default for `edit`) |
| `-style-refs "1,5"` | Specify pages to use as style references |
| `-output "new.pdf"` | Specify output filename |
| `-resolution "4K"` | Image resolution: "4K" (default), "2K", or "1K" |
| `-disable-google-search` | Prevent model from using Google Search |

### Troubleshooting

- **"Missing system dependencies"**: Install poppler and tesseract, restart terminal
- **"GEMINI_API_KEY not found"**: Set the environment variable
- **"PAID API key required"**: Enable billing on your Google Cloud project
- **Style mismatch**: Use `--style-refs` to specify reference pages
- **Slow processing**: Use lower resolution (`-resolution "2K"` or `"1K"`)

### Why It's Interesting

- Solves the common problem of making quick edits to presentation PDFs
- Non-destructive approach preserves text searchability
- Could save significant time for frequent deck updates
- Good for family projects (school presentations, event materials)

### Considerations

- Requires paid Gemini API - not free for casual use
- Quality depends on source PDF resolution and complexity
- OCR may not be perfect for stylized fonts or small text
- External dependencies (Poppler, Tesseract) required

### Related

- **Poppler**: PDF rendering library used by Nano PDF (see separate entry if added)
- **Tesseract**: OCR engine for text layer restoration
