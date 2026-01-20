# PlutoPrint - HTML to PDF/Image Generation

*Source: https://github.com/plutoprint/plutoprint - Added: 2026-01-18*

PlutoPrint is a Python library for generating high-quality PDFs and images from HTML/XML content. Uses the PlutoBook rendering engine.

**Docs**: https://plutoprint.readthedocs.io
**Samples**: https://github.com/plutoprint/plutoprint-samples
**License**: MIT

## Installation

```bash
pip install plutoprint
```

Note: Depends on PlutoBook. Windows/Linux 64-bit get prebuilt binaries. Otherwise Meson builds from source (slower).

## CLI Usage

```bash
plutoprint input.html output.pdf --size=A4
```

## Python API

### Generate PDF

```python
import plutoprint

book = plutoprint.Book(plutoprint.PAGE_SIZE_A4)
book.load_url("input.html")
book.write_to_pdf("output.pdf")
```

### Generate PNG

```python
import plutoprint
import math

book = plutoprint.Book(media=plutoprint.MEDIA_TYPE_SCREEN)
book.load_html("<b>Hello World</b>", user_style="body { text-align: center }")

width = math.ceil(book.get_document_width())
height = math.ceil(book.get_document_height())

with plutoprint.ImageCanvas(width, height) as canvas:
    canvas.clear_surface(1, 1, 1)
    book.render_document(canvas)
    canvas.write_to_png("hello.png")
```

### Generate Charts with Matplotlib

Custom resource fetcher to embed Matplotlib charts:

```python
import plutoprint
import matplotlib.pyplot as plt
import urllib.parse
import io

class CustomResourceFetcher(plutoprint.ResourceFetcher):
    def fetch_url(self, url):
        if not url.startswith('chart:'):
            return super().fetch_url(url)
        values = [float(v) for v in urllib.parse.unquote(url[6:]).split(',')]
        labels = [chr(65 + i) for i in range(len(values))]

        plt.bar(labels, values)
        plt.title('Bar Chart')

        buffer = io.BytesIO()
        plt.savefig(buffer, format='svg', transparent=True)
        return plutoprint.ResourceData(buffer.getvalue(), "image/svg+xml", "utf-8")

book = plutoprint.Book(plutoprint.PAGE_SIZE_A4.landscape(), plutoprint.PAGE_MARGINS_NONE)
book.custom_resource_fetcher = CustomResourceFetcher()

book.load_html("<img src='chart:23,45,12,36,28'>", user_style="img { width: 100% }")
book.write_to_pdf("charts.pdf")
```

## Use Cases

- **Reports**: Generate PDF reports from HTML templates
- **Invoices**: Create invoices with dynamic data
- **Tickets**: Generate event tickets
- **Documentation**: Build docs with consistent styling
- **Data visualization**: Embed charts from Matplotlib/other libraries

## Why It's Interesting

- Simple API for HTML-to-PDF conversion
- Good quality rendering via PlutoBook engine
- Custom resource fetchers enable dynamic content (charts, etc.)
- MIT licensed - use freely in personal or commercial projects
- Both CLI and Python API available

## Alternatives

| Tool | Language | Approach |
|------|----------|----------|
| PlutoPrint | Python | PlutoBook rendering engine |
| WeasyPrint | Python | CSS Paged Media, good for print |
| wkhtmltopdf | CLI | Uses WebKit (deprecated) |
| Puppeteer | Node.js | Headless Chrome |
| Playwright | Multi | Headless browsers |
| pdfkit | Python | Wrapper around wkhtmltopdf |

## Related

- [[pdfly-pdf-cli-tool]] - PDF manipulation CLI
- [[poppler-pdf-library]] - PDF rendering library
- [[ai-pdf-tools]] - AI-powered PDF editing
