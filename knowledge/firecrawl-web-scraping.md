# FireCrawl - Web Scraping to LLM-Ready Markdown

https://www.firecrawl.dev/

Web crawling and data conversion tool that transforms websites into clean, LLM-ready markdown.

## Key Features

- **JS Rendering**: Handles dynamic content rendered with JavaScript (unlike traditional scrapers)
- **Sitemap-Free Crawling**: Crawls all accessible subpages even without a sitemap
- **Clean Output**: Advanced algorithms clean and structure scraped data into readable markdown
- **Anti-Scraping Handling**: Manages proxies, rate limits, caching, and JS-blocked content
- **robots.txt Compliant**: Respects rules; user agent is "FireCrawlAgent"

## Best Use Cases

- Business websites, documentation, and help centers
- Training data collection for LLMs
- Market research and content aggregation
- Data preparation for AI applications

## Example Output

```json
[
  {
    "url": "https://example.com/",
    "markdown": "## Welcome\nClean markdown content..."
  },
  {
    "url": "https://example.com/features",
    "markdown": "## Features\nMore clean content..."
  }
]
```

## Pricing

- Free trial: 100 pages
- Scale plan available for millions of pages
- Features caching and scheduled syncs for enterprise use

## Open Source

GitHub repo available (early development stage). Can self-host or use hosted service.

## Related

- Used by Directus AI Web Scraper extension
- Integrated into self-hosted AI stacks (Open WebUI, etc.)
