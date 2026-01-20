---
type: link
source: notion
url: https://www.embedding.io/
notion_type: Tech Announcement
tags: ['Running']
created: 2024-08-01T04:46:00.000Z
---

# Turn websites into knowledge bases | Embedding.io

## AI Summary (from Notion)
- Purpose: Embedding.io allows users to crawl, chunk, and vectorize website content for use with language learning models (LLMs).
- Creation of Collections: Users can create collections to store web pages or websites through an API or web interface.
- Content Ingestion: The platform automatically handles updates when web pages are added to a collection.
- Querying: Once a collection is set up, users can query it via the API to retrieve updated information.
- Public Collections: Embedding.io offers various public collections, including documentation for WordPress, Laravel, and notable figures like Paul Graham and Tim Ferriss.
- Pricing:
- Free Plan: $0/month for up to 1,000 pages and monthly updates.
- Enterprise Plan: Custom pricing for unlimited pages and hourly updates.
- Interesting Fact: The ability to keep data updated automatically is a significant feature, enhancing the utility of the service for users interested in the latest information.

## Content (from Notion)

Crawl, chunk, and vectorize any websites so you can use their content with LLMs.

Start for Free  How it works →

```plain text
curl --request POST \
    --url https://api.embedding.io/v0/query \
    --header 'Authorization: Bearer V09XIFlPVSdSRSBBIEhBQ0tFUg==' \
    --json '{
        "collection": "col_lPMjKLBRLZ4qVe",
        "query": "Why should I avoid sunflower oil?"
    }'
```

## How it works

### Create a Collection

Use our API or web interface to make a collection. This holds the pages or websites you want to use.

```plain text
curl --request POST \
    --url https://api.embedding.io/v0/collections \
    --header 'Authorization: Bearer V09XIFlPVSdSRSBBIEhBQ0tFUg==' \
    --json '{
        "name": "Health Gurus"
    }'
```

### Ingest Content

Add web pages to your collection. We will handle the rest, including updates.

```plain text
curl --request POST \
    --url https://api.embedding.io/v0/collections/col_lPMjKLBRLZ4qVe/websites \
    --header 'Authorization: Bearer V09XIFlPVSdSRSBBIEhBQ0tFUg==' \
    --json '{
    	"domains": [
     	   "https://peterattiamd.com/",
            "https://www.foundmyfitness.com/"
    	]
    }'
```

### Query your Collection

Once your collection is ready, query it using our API. We keep the data updated for you.

```plain text
curl --request POST \
    --url https://api.embedding.io/v0/query \
    --header 'Authorization: Bearer V09XIFlPVSdSRSBBIEhBQ0tFUg==' \
    --json '{
        "collection": "col_lPMjKLBRLZ4qVe",
        "query": "Why should I avoid sunflower oil?"
    }'
```

## Public collections

Try our public collections

###  WordPress Documentation 

###  Laravel 11.x Documentation 

###  Embedding.io Documentation 

PG

###  Paul Graham 

PM

###  Patrick McKenzie (patio11) 

TF

###  Tim Ferriss 

## Pricing

Get started for free.

### Free

Start for free

$0 /month

Sign up for free

- Up to 1,000 pages per month
- Monthly updates
- API access
### Enterprise

Custom pricing

Custom

Contact us

- Unlimited pages
- Hourly updates

