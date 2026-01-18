---
type: link
source: notion
url: https://100x.bot/a/we-gave-our-browser-agent-a-3mb-data-warehouse
notion_type: Software Repo
tags: ['Running']
created: 2026-01-17T02:59:00.000Z
---

# We Gave Our Browser Agent a 3MB Data Warehouse

## Overview (from Notion)
- This browser agent with a 3MB data warehouse can streamline your data scraping processes, making it easier to manage multiple sources without the frustration of spreadsheets.
- The integration of SQL allows for complex data manipulation directly in the browser, saving time and reducing reliance on backend systems.
- The fuzzy join capability can help reconcile imperfect data from different sources, enhancing your ability to analyze and make decisions quickly.
- Consider how this could optimize your work-life balance by reducing the time spent on data management, freeing you for family or personal projects.
- The approach of embedding a lightweight database in the browser reflects a shift towards more efficient, decentralized data handling, which may inspire you to innovate in your own software projects.
- Alternative viewpoints might argue that relying on browser-based solutions could limit scalability or robustness compared to traditional server-based databases, prompting a consideration of when to use each approach.

## AI Summary (from Notion)
The integration of PGLite into the 100x bot allows for efficient data scraping and storage in relational tables directly within the browser. This enables complex data reconciliations, fuzzy joins, and analytical queries using SQL, addressing the limitations of traditional JavaScript approaches. Key features include handling inconsistent data names, preserving hierarchical structures, and performing analytical reasoning without cumbersome state management. The implementation leverages WebAssembly for Postgres, optimizing performance while managing storage constraints inherent to browsers.

## Content (from Notion)

100x bot is an autonomous browser agent and with our latest release we integrated PGLite as its long term memory.

It allows you to:

- Scrape complex data and immediately store it in relational tables without leaving the current tab.
- Perform messy reconciliations (like fuzzy-joining product names across different websites) using native SQL extensions.
- Run analytical queries (window functions, aggregations) locally, replacing brittle JavaScript logic with declarative SQL.
## Why?

Honestly, we didn't build this because we love databases.

I was looking for a house on rent in Hayes Valley, SF and used 100x on top of redfin, zillow and blueground.

I scraped a few listings quickly but immediately hit a wall. To do anything useful with these, I had to export a CSV, open Excel and operate on it.

I don't like databases but I hate spreadsheets more.

For a long time, the standard engineering answer for browser storage was "just use a JSON array." And to be fair, modern V8 engines can iterate over 5,000 JSON objects in milliseconds. Performance wasn't the issue. Complexity was the issue.

When you try to reconcile data from two different sources in JavaScript, you end up reinventing database logic. You write hash maps to simulate JOINs. You write complex reduce functions to calculate moving averages. You import heavy libraries just to do fuzzy string matching. We realized our agent didn't need faster loops; it needed a cortex. It needed SQL.

## What's Possible Now

By embedding PGLite (Postgres in WASM) directly into the agent, we stop treating browser data as transient variables and start treating it as a relational dataset. Here is why marrying an AI agent with Postgres is necessary.

### 1. The Fuzzy Join

The hardest part of scraping is matching data that should be the same but isn't. "Apple Inc." on one site is "Apple Computer" on another. Writing a JS function to handle this reliably is a nightmare of edge cases.

With the pg_trgm extension running in the browser, the agent can perform fuzzy joins natively.

SQL

- The agent reconciles 'dirty' scraped data with a master listSELECT scraped.product_name, master.sku, similarity(scraped.product_name, master.name) as match_score
FROM scraped_products scraped

JOIN master_catalog master ON scraped.product_name % master.name - The magic operator WHERE scraped.product_name % master.name

ORDER BY match_score DESC;

### 2. Understanding Hierarchy

The web is a tree (DOM), but we usually flatten it into lists, losing context. If you scrape a threaded forum (like Hacker News) or an Amazon category tree, preserving that structure in a flat JSON file makes querying it painful.

Using the ltree extension, the agent can query the structure naturally.

SQL

- Find all comments in a specific sub-thread without recursion
SELECT FROM comments WHERE path <@ 'root.123.456';

### 3. Analytical Reasoning

Agents often need to answer questions like, "Is this price significantly lower than the average for this category over the last 10 scrapes?"

In JavaScript, this requires maintaining state variables and writing imperative loops. In SQL, it's a standard window function.

SQL

SELECT

product_name,

price,

AVG(price) OVER (

- PARTITION BY category
- ORDER BY scrape_date
- ROWS BETWEEN 5 PRECEDING AND CURRENT ROW
) as moving_avg

FROM pricing_history;

## How does it work?

We utilize PGLite, a build of PostgreSQL compiled to WebAssembly.

- The Single-User Hack: Postgres normally requires a multi-process architecture (forking), which browsers don't support. PGLite runs Postgres in "single-user mode": a bootstrap mode usually reserved for disaster recovery. This allows it to run as a single process inside the browser tab.
- Virtual File System (VFS): PGlite maps the Postgres filesystem to IndexedDB. This persists data across user sessions.
- Storage Limits: This is the hard engineering constraint. While Postgres can technically handle gigabytes, the browser has strict quotas:
That complexity is abstracted mostly, thanks to pglite. It's between indexeddb, browser and the user.

### Benchmarking

We did, however, ask 100x to:

Generate 10k rows of meaningful data for performance testing and load test PGLite against js implementation and give a performance comparison plot?

Till 10k records js performed better and as we scaled to 100k, pglite started winning!

## Our learnings

The most surprising hurdle wasn't compiling Postgres to WASM (the ElectricSQL team did the heavy lifting there), but dealing with the "Memory Wall."

In the browser VFS implementation, the database file structure is often loaded into memory. While modern machines have plenty of RAM, a browser tab is a hostile environment. We found that while we could process 100k rows, the sweet spot for a browser agent is keeping the "working set" lean. We aren't trying to replace your Snowflake data warehouse; we are giving the agent a working memory that is structured rather than chaotic.

We also learned that "Relaxed Durability" is mandatory. Waiting for a synchronous fsync to IndexedDB for every row insert brings the agent to a crawl. We accept the risk of losing the last few milliseconds of data in a crash in exchange for 100x write performance.

Here is what I tried.

1. Scrape hn posts using their public API
1. Create a Deep Dive Datagrid page analysing the dataset.
## Why you should try it

If you build browser automation or scrapers, you eventually hit the point where JSON.filter isn't enough. We built this so you can stop writing database code in JavaScript and just write SQL.


