---
type: link
source: notion
url: https://simonwillison.net/2023/Dec/1/datasette-enrichments/
notion_type: Software Repo
tags: ['Running']
created: 2024-01-24T21:00:00.000Z
---

# Datasette Enrichments: a new plugin framework for augmenting your data

## AI Summary (from Notion)
- Introduction of Datasette Enrichments: A new plugin framework designed to augment data in databases through "enrichments."
- Definition of Enrichment: Code that can transform existing data or fetch additional data from external sources, which can then be written back to the database.
- Example of Enrichment: Geocoding, where addresses are transformed into latitude and longitude using an API.
- Plugin System: Each enrichment functions as a plugin, allowing for easy extension and a variety of use-cases.
- Video Demonstration: A video showcases the capabilities of the new plugins, including geocoding and generating content with OpenAI's GPT models.
- Released Plugins:
- datasette-enrichments-gpt: Access to OpenAI models, allowing for prompt execution and structured data extraction.
- datasette-enrichments-opencage: Utilizes OpenCage geocoder, supporting open data projects and offering flexible API usage.
- datasette-enrichments-jinja: Executes Jinja templates against table rows, useful for data manipulation.
- datasette-enrichments-re2: Runs regular expressions on table values, offering multiple modes for data extraction and manipulation.
- Future Development: Encouragement for Python developers to build custom enrichment plugins, with resources provided for guidance.
- Community Engagement: Invitation to join a dedicated channel on the Datasette Discord for collaboration and idea sharing.
- Overall Theme: Emphasis on the potential of the new framework to enhance data capabilities and the ease of integrating new functionalities.

## Content (from Notion)

Today I’m releasing datasette-enrichments, a new feature for Datasette which provides a framework for applying “enrichments” that can augment your data.

An enrichment is code that can be run against rows in a database table. That code can transform existing data or fetch additional data from external sources, then write that augmented data back to the database.

A good example of an enrichment is geocoding: take a table with an address column, run each address through a geocoding API, then write the resulting location back to latitude and longitude columns on the same table.

Each enrichment is itself a plugin. The Datasette enrichments system is designed to be easily extended with new enrichment types, to serve a wide variety of use-cases.

### Demonstrating enrichments

I’ve made a video demo to demonstrate the new capabilities introduced by this plugin.

The video shows off two enrichments: datasette-enrichments-gpt for running prompts against OpenAI’s GPT language models, and datasette-enrichments-opencage for geocoding addresses.

In the video I demonstrate the following:

- Uploading a CSV file of Film Locations in San Francisco to create a table
- Running the OpenCage geocoder enrichment against those rows to populate latitude and longitude columns
- ... which results in a map being displayed on the table page using datasette-cluster-map
- Applying the GPT enrichment to write terrible haikus about every museum on my Niche Museums website
- Extracting JSON with key people and dates from each museum descriptions
- Using the GPT-4 Vision API to generate detailed descriptions of photographs displayed on the site
### Enrichments so far

I’m releasing four enrichment plugins today:

I’ve also published documentation on developing a new enrichment.

### datasette-enrichments-gpt

The most interesting enrichment I’m releasing today is datasette-enrichments-gpt. This enrichment provides access to various OpenAI language models, allowing you to do some really interesting things:

- Execute a prompt against data pulled from columns in each row of a table and store the result
- Run prompts against URLs to images using the GPT-4 Vision API
- Extract structured data from text
I demonstrated all three of these in the video. Here’s how I used JSON object mode to extract JSON structured data for people and years from the museum descriptions, using this prompt:

> 

I also ran GPT-4 Vision against images, with the prompt “describe this photo”. Here’s the description it gave for this photograph from the Bigfoot Discovery Museum:

> 

### datasette-enrichments-opencage

datasette-enrichments-opencage provides access to the OpenCage geocoder.

I really like OpenCage. Many geocoders have strict restrictions on what you can do with the data they return—some of them even prohibit storing the results long-term in a database!

OpenCage avoid this by carefully building on top of open data, and they also financially support some of the open data projects they rely on.

This plugin (and datasette-enrichments-gpt) both implement a pattern where you can configure an API key using plugin secrets, but if you don’t do that the key will be requested from you each time you run an enrichment.

### datasette-enrichments-jinja

I wanted to launch with an example of an enrichment that can execute arbitrary code against each row in a table.

Running code in a sandbox in Python is notoriously difficult. I decided to use the Jinja sandbox, which isn’t completely secure against malicious attackers but should be good enough to ensure trustworthy users don’t accidentally cause too much damage.

datasette-enrichments-jinja can execute a Jinja template against each row in a table and store the result.

It’s a small but powerful template language, and should prove useful for a number data manipulation tasks.

### datasette-enrichments-re2

datasette-enrichments-re2 provides an enrichment that can run a regular expression against a value from a table and store the result.

It offers four different modes:

- Execute a search and replace against a column
- Extract the first matching result and store that in the specified column (adding a column to the table if necessary)
- Extract all matching results and store them as a JSON array in the specified column. If the regular expression uses named capture groups this will be an array of objects, otherwise it will be an array of strings.
- Execute a regular expression with named capture groups and store the results in multiple columns, one for each of those named groups
That’s quite a lot of functionality bundled into one enrichment! I haven’t used this for much yet myself, but I’m looking forward to exploring it further and documenting some useful patterns.

### Writing your own enrichment plugin

The most exciting thing about enrichments is what they can unlock in the future.

I’ve tried to make it as easy as possible for Python developers to build their own enrichment plugins.

The Developing a new enrichment documentation walks through the process of building a new enrichment plugin from scratch.

Enrichments run inside Datasette using Python asyncio. This is a particularly good fit for enrichments that use external APIs, since HTTPX makes it easy to run multiple HTTP requests in parallel.

The -opencage and -gpt enrichments are two examples of enrichments that use HTTPX.

Interested in building one? Join the new #enrichments channel on the Datasette Discord to discuss ideas and talk about the new feature!

This is Datasette Enrichments: a new plugin framework for augmenting your data by Simon Willison, posted on 1st December 2023.

plugins 65   projects 336   datasette 375

Next: Weeknotes: datasette-enrichments, datasette-comments, sqlite-chronicle

Previous: llamafile is the new best way to run a LLM on your own computer


