---
type: link
source: notion
url: https://github.com/plutoprint/plutoprint
notion_type: Software Repo
tags: ['Running']
created: 2025-08-21T02:01:00.000Z
---

# GitHub - plutoprint/plutoprint: A Python Library for Generating PDFs and Images from HTML, powered by PlutoBook

## Overview (from Notion)
- PlutoPrint allows you to generate professional-quality PDFs and images quickly, useful for reports and presentations, which can help streamline your workflow as a software engineer and founder.
- The ability to create invoices and documentation directly from HTML saves time, letting you focus more on your projects and family.
- Its integration with data visualization tools like Matplotlib can enhance your ability to present technical data in a visually appealing way, which might impress clients or stakeholders.
- The open-source nature and MIT License offer flexibility in using the library, enabling you to adapt it for personal or business needs without licensing concerns.
- Consider the impact of automated documentation generation on efficiency—could this technology help reduce the time spent on repetitive tasks?
- Alternate view: While the ease of use is appealing, you might wonder about the learning curve for team members unfamiliar with coding or the potential need for ongoing maintenance and updates.
- The community around PlutoPrint could provide valuable networking opportunities, connecting you with other tech enthusiasts and potential collaborators.

## AI Summary (from Notion)
PlutoPrint is a Python library for generating high-quality PDFs and images from HTML or XML content, utilizing the PlutoBook rendering engine. It offers a simple API for creating documents and supports installation via pip. Users can generate PDFs and PNGs through command line or Python scripts, and it includes functionality for creating charts with Matplotlib. Additional resources include documentation, sample projects, and a GitHub repository.

## Content (from Notion)

## PlutoPrint

PlutoPrint is a lightweight and easy-to-use Python library for generating high-quality PDFs and images directly from HTML or XML content. It is based on PlutoBook’s robust rendering engine and provides a simple API to convert your HTML into crisp PDF documents or vibrant image files. This makes it ideal for reports, invoices, or visual snapshots.

### Installation

```plain text
pip install plutoprint
```

PlutoPrint depends on PlutoBook. For faster installation, it is highly recommended to install PlutoBook and its dependencies manually beforehand. Otherwise, Meson will build them from source during installation, which can take significantly longer.

For Windows and Linux 64-bit users, PlutoPrint provides prebuilt binaries, so no additional setup is required.

### Quick Usage

Generate a PDF from the command line with the installed plutoprint script:

```plain text
plutoprint input.html output.pdf --size=A4
```

Generate PDF with Python

```plain text
import plutoprint

book = plutoprint.Book(plutoprint.PAGE_SIZE_A4)
book.load_url("input.html")
book.write_to_pdf("output.pdf")
```

Generate PNG with Python

```plain text
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

Generate Charts with Matplotlib

```plain text
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
        plt.xlabel('Labels')
        plt.ylabel('Values')

        buffer = io.BytesIO()
        plt.savefig(buffer, format='svg', transparent=True)

        return plutoprint.ResourceData(buffer.getvalue(), "image/svg+xml", "utf-8")

book = plutoprint.Book(plutoprint.PAGE_SIZE_A4.landscape(), plutoprint.PAGE_MARGINS_NONE)

book.custom_resource_fetcher = CustomResourceFetcher()

HTML_CONTENT = """
<div>
    <img src='chart:23,45,12,36,28,50'>
    <img src='chart:5,15,25,35,45'>
    <img src='chart:50,40,30,20,10'>
    <img src='chart:10,20,30,40,50,60,70'>
</div>
"""

USER_STYLE = """
div { display: flex; flex-wrap: wrap; justify-content: center; height: 98vh }
img { flex: 0 0 45%; height: 50%; background: #fff; border: 1px solid #ccc; }
body { background: #f7f7f7 }
"""

book.load_html(HTML_CONTENT, USER_STYLE)
book.write_to_png("charts.png")
book.write_to_pdf("charts.pdf")
```

Expected output:

## Samples

Invoices

Tickets

## Links & Resources

- Documentation: https://plutoprint.readthedocs.io
- Samples: https://github.com/plutoprint/plutoprint-samples
- Code: https://github.com/plutoprint/plutoprint
- Issues: https://github.com/plutoprint/plutoprint/issues
- Donation: https://github.com/sponsors/plutoprint
## License

PlutoPrint is licensed under the MIT License, allowing for both personal and commercial use.


