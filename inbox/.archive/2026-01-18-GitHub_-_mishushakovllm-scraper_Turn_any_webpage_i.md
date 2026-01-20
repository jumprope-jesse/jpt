---
type: link
source: notion
url: https://github.com/mishushakov/llm-scraper
notion_type: Software Repo
tags: ['Running']
created: 2024-04-21T03:31:00.000Z
---

# GitHub - mishushakov/llm-scraper: Turn any webpage into structured data using LLMs

## AI Summary (from Notion)
- Project Overview: The LLM Scraper is a TypeScript library designed to convert any webpage into structured data using language models (LLMs).
- Creation Date: The project was created on April 21, 2024.
- Status: Currently marked as "Not started."
- Core Features:
- Utilizes OpenAI chat models for data extraction.
- Schemas are defined using Zod, ensuring full type safety with TypeScript.
- Built on the Playwright framework, allowing for seamless browser automation.
- Supports three input modes: html, text, and image.
- Offers a streaming capability for crawling multiple pages simultaneously.
- Getting Started: Users need to install dependencies, set an OpenAI API key, and create a browser instance to use the scraper.
- Example Use Case: Demonstrates how to extract top stories from HackerNews using the scraper with a defined schema.
- Community Engagement: The project encourages contributions from the community and welcomes feedback, issues, and pull requests.
- Interesting Fact: The scraper leverages function calling to transform web pages into structured data, showcasing a modern approach to web scraping.

## Content (from Notion)

# LLM Scraper

LLM Scraper is a TypeScript library that allows you to convert any webpages into structured data using LLMs.

Tip

Under the hood, it uses function calling to convert pages to structured data. You can find more about this approach here

### Features

- Uses OpenAI chat models
- Schemas defined with Zod
- Full type-safety with TypeScript
- Based on Playwright framework
- Streaming when crawling multiple pages
- Supports 3 input modes: 
Make sure to give it a star!

## Getting started

1.  
1.  
1.  
## Example

In this example, we're extracting top stories from HackerNews:

```plain text
import z from 'zod'
import { chromium } from 'playwright'
import LLMScraper from 'llm-scraper'

// Create a new browser instance
const browser = await chromium.launch()

// Initialize the LLMScraper instance
const scraper = new LLMScraper(browser)

// Define schema to extract contents into
const schema = z.object({
  top: z
    .array(
      z.object({
        title: z.string(),
        points: z.number(),
        by: z.string(),
        commentsURL: z.string(),
      })
    )
    .describe('Top stories on Hacker News'),
})

// URLs to scrape
const urls = ['https://news.ycombinator.com']

// Run the scraper
const pages = await scraper.run(urls, {
  model: 'gpt-4-turbo',
  schema,
  mode: 'html',
  closeOnFinish: true,
})

// Stream the result from LLM
for await (const page of pages) {
  console.log(page.data)
}
```

## Contributing

As an open-source project, we welcome contributions from the community. If you are experiencing any bugs or want to add some improvements, please feel free to open an issue or pull request.


