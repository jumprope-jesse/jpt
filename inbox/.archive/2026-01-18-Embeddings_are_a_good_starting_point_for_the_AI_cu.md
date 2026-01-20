---
type: link
source: notion
url: https://bawolf.substack.com/p/embeddings-are-a-good-starting-point
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-04-18T02:31:00.000Z
---

# Embeddings are a good starting point for the AI curious app developer

## AI Summary (from Notion)
- Embeddings Overview: Vector embeddings are presented as a foundational technology for app developers interested in AI, simplifying complex search experiences.
- Key Features of Embeddings:
- They measure similarity effectively, even across different languages.
- Embed data into a manageable form for individual developers, consolidating what were once extensive projects.
- Tooling Choices:
- The author discusses using Pgvector, a Postgres extension, for embedding storage and queries, highlighting its integration with standard SQL.
- Search Implementation:
- Traditional search methods rely heavily on keyword matching, which can be fragile.
- Using embeddings allows for more robust similarity searches based on the cosine similarity of vectors.
- Filtering and Ranking:
- The application can filter search results by icon sets, enhancing the relevance of results.
- A proposed ranking algorithm combines embedding similarity with user interaction data to improve search accuracy over time.
- Conclusion:
- The author expresses gratitude towards the engineering community for advancements in embedding technology.
- The write-up serves as a guide for developers to implement embedding features in their applications.
- Interesting Facts:
- The project was developed in Typescript and used a combination of SQL and embedding operations to query icons.
- The author emphasizes that embeddings can yield relevant results even when queries are not in English or traditional keywords.

## Content (from Notion)

Vector embeddings have been an Overton window shifting experience for me, not because they’re sufficiently advanced technology indistinguishable from magic, but the opposite. Once I started using them, it felt obvious that this was what the search experience was always supposed to be: less “How did you do that?” and more mundanely, “Why isn’t this everywhere?”

This feels like the right place to start if you’re an app developer looking for an excuse to dip your toes into this new AI world. Embeddings are just arrays of numbers, but they contain a compressed form of a considerable amount of human knowledge and shrink features that used to be substantial specialized projects into ones that individual product engineers can take on.

There are a ton of tooling options available to use embeddings. I’ll highlight our choices and note where you might want to make different ones for your situation. Here are some points I hope you take away:

- Vector embeddings work for search and recommendations because they’re good at measuring similarity to arbitrary input. This even works for different spoken languages like French or Japanese.
- Pgvector is a Postgres extension that stores and queries embeddings without adding a new service. It’s powerful because it can combine standard SQL logic with embedding operations.
- Unlike LLMs, working with embeddings feels like regular deterministic code.
## The project

My friend Charlie Yuan and I built this mini icon app to help people discover icons. It’s pretty short and sweet. We have icon sets you can query, bookmark, and add to your project.

### Pgvector

There are a bunch of specialized vector databases to choose from. Instead, we chose Postgres with pgvector to blend embedding search with business logic like filtering and scoring. While it’s not the fastest vector database, we didn’t want to have to compare results across multiple data sources. Pgvector probably already has a library for your favorite database client. Our project was Typescript through and through, and we used drizzle-orm. The docs will be a more robust place for setup documentation, so I’m leaving out that part to focus on the features you can build.

### Creating embeddings

Once set up with pgvector, we created a strategy for encoding our icon data into vector embeddings. Embeddings are points in many-dimensional space, up to thousands of dimensions. Unfortunately, the axes of that grid are not humanly grokable ideas like “size” or “brightness.” They’re a bit of a black box. Luckily, like any good abstraction, they’re a black box with a good API.

The best practice seems to be finding the details that best represent what people want to search for and creating a function that outputs that as a string. Our icons can be a part of many use-case-based ‘categories’ and have many descriptive ‘tags’ associated with them. We encoded that information along with the icon name because that best represents what the icon is. Whereas the name of the icon set the icon belongs to, or its dimensions aren’t relevant. The strings we generated looked basically like this:

```plain text
const createIconEmbeddingsString = (icon) => `icon: "${icon.name}", categories: [${categories}] tags: [${tags}]`;
```

Next, we chose an embedding model. OpenAI’s embedding models will probably work just fine. We’re using their `text-embedding-3-small`. If you want to dive in, check out the leaderboard and pick the model that best meets your needs. Whether you use an embeddings API or self-host an open source option, the interface should be text in and embeddings out.

## Implementing search

Many sites implement search, but most icon sites implement search by text matching or full-text search. If you’re looking for a dog icon, they search over the icon metadata for icons that have ‘dog’ in them. If they want to get craftier, they come up with a bag of words related to ‘dog,’ like maybe ‘k9’, ‘puppy,’ and ‘woof’ to catch near misses. That’s pretty fragile. Someone has to choose tags for each icon; if they miss an important one, users won’t find what they’re looking for.

### Similarity search

Our app gets relevant results when searching for ‘dog.’ We also get solid results for ‘puppy’ without a bag of words by measuring the cosine similarity between the embeddings of your search query and each icon. There are multiple ways to measure how similar embeddings are to each other, but OpenAI’s embeddings are designed to work well with cosine distance. Cosine similarity is just the opposite of cosine distance. Order by cosine distance wherever you can to take advantage of indexes.

```plain text
cosine_similarity(x,y) = 1 - cosine distance(x,y)
```

You can even try dog breeds like ‘hound,’ ‘poodle,’ or my favorite ‘samoyed.’ It pretty much just works. But that’s not all; it also works for other languages. Try ‘chien’ and even ‘犬’1! With pgvector, we can get these results with simple SQL queries.

```plain text
SELECT
  1 - cosine_distance (search_query.embedding,
    icon.embedding) as similarity,
  *
FROM
  icon
  join search_query on search_query.text = 'dog'
ORDER BY
  cosine_distance (search_query.embedding, icon.embedding) ASC
LIMIT 50;
```

Since we’re ordering by distance, every search returns every result in the table in order of closeness. We cut off results by a fixed number to make this manageable, limiting the query to the top 50. Using an arbitrary distance cut-off is tempting, like querying for results with a cosine similarity of less than 0.8. Unfortunately, the absolute distance for one query to produce correct-feeling results might differ drastically from another. We limit by the number of results, not by a minimum value, whenever possible.

### Filtering

If we only wanted similarity search, any vector database would be fine, but Postgres allowed us to layer more features on top. The initial search looks across all icons in all icon sets, but our user’s style might only match some of the icon sets. We can filter by values like in any other Postgres query.

```plain text
SELECT
  1 - cosine_distance (search_query.embedding,
    icon.embedding) AS similarity,
  *
FROM
  icon
  JOIN search_query ON search_query.text = 'dog'
  JOIN icon_set ON icon_set.slug = icon.icon_set_slug
WHERE
  icon_set.slug in('lucide', 'mdi')
ORDER BY
  cosine_distance (search_query.embedding,
    icon.embedding) ASC
LIMIT 50;
```

This is deterministic; everyone searching for a ‘dog’ will get the same results. However, the inputs are still unbounded, so embedding search doesn’t guarantee that the best results will be produced for every input. We can try different embedding models or ways of encoding icons into embeddings to improve the system.

### A more complex algorithm

The embedding search usually puts the correct icon on the page, but the correct icon isn’t always the first result. We could make a simple algorithm that adjusts to user feedback and improves over time. To do this, we’d count every time a user clicks on an icon for a particular search query. When ranking search results, we’d create a score for each icon that combines the embedding search with the click data.

Here’s a simple ranking algorithm. The details look messy because there’s some null checking and unit conversions2, but here are the basics.

1. Get the cosine similarity of the icon for the search query. It will be a number between 0 and 1. Multiply it by 0.5.
1. Divide the number of clicks for each icon by the icon with the most clicks for that query. This normalizes the most clicked icon to 1, and the least clicked to 0. Multiply by 0.5.
1. The final score is these two values added together for a range between 0-1.3
```plain text
SELECT
  (
    0.5 * COALESCE(      -- so nulls are turned into 0
     1 - cosine_distance (search_query.embedding, icon.embedding),
     0
    ) + 0.5 *     -- so clicks matter less than embeddings.
    COALESCE(
      search_query_selection. "count"::decimal /
        max(search_query_selection. "count") OVER (),
    0)
  ) AS score,
  icon.*
FROM
  icon
  LEFT JOIN search_query_selection
    ON icon.id = search_query_selection.icon_id
  LEFT JOIN search_query
    ON search_query.text = 'dog'
      AND search_query.id = search_query_selection.search_query_id
  ORDER BY score DESC
  LIMIT 50;
```

Should vector embedding distance and clicks be equally weighted? Should the order of magnitude of clicks matter more than the raw number? The algorithm might need tuning, but this is just an example of how the database handles the calculation nicely.

With a separate vector database, we might have to get values for all icons from both databases before comparing them in application code or making tradeoffs like pulling 100 results from the vector db and filtering the Postgres query for click score to those results or vice versa. Instead, we simply query for results and display them.

## Similar recommendations

Additionally, we include a content forward section of each icon page with other icons in the same icon set and category. That way, you can see other ‘navigation’ icons when looking at `arrow-up` in case you need those. Unfortunately, not all of our icon sets have categories. In these cases, we make a similar icons section using embeddings. Instead of getting an embedding from user input, we can compare the same cosine similarity measure against the selected icon’s embedding.

```plain text
WITH current_icon AS (
    SELECT
      embedding,
      slug,
      icon_set_slug
    FROM
      icon
    WHERE
      icon_set_slug = 'lucide'
      AND slug = 'activity'
)
SELECT
    *
FROM
    icon
INNER JOIN current_icon ON
icon.icon_set_slug = current_icon.icon_set_slug
AND icon.slug != current_icon.slug
ORDER BY
    1 - cosine_distance (
    icon.embedding,
    current_icon.embedding
)
LIMIT 50;
```

# Conclusion

I hope you have a good experience playing with our app and vector embeddings! We owe a big thanks to all the engineers who pushed the state of the art so far that we can stand on their shoulders. I hope this modest contribution helps make adding embedding features to your app approachable!

Here is a summary of our implementation decisions and some sources for other options.

### Vector database

We chose pgvector/Postgres, but there are plenty of other choices, including some for other standard databases like MongoDB.

### Pgvector client

We worked in Typescript and chose drizzle-orm. I’ve also worked in the Phoenix elixir ecosystem using the elixir library with Ecto. You can find a library for your client of choice here.

### Database host

Our app is hosted on Neon. I’ve also used fly.io, though their option wasn’t really a managed instance at the time. Now, they have a managed solution with Supabase. If you want to look up someone else, Pgvector has a clumsy list of hosts that support it in this git issue.

### Embedding model

We chose OpenAI’s `text-embedding-3-small`. If you want to try something else, check out Huggingface’s leaderboard.

### Embedding string

We embedded strings of key and value pairs for the attributes we thought best described our icons. It doesn’t seem like any of the major players are doing anything crazy here; the significant knobs appear to be whether or not to embed keys or just values and which attributes of your records are relevant. Other examples in OpenAI’s cookbook show other choices.

### Distance metric

We used cosine similarity as our distance function because that’s what OpenAI recommends for their embeddings. Other embeddings may be optimized for different strategies. Pgvector supports l2 distance, inner product, and cosine distance.

### Search Size

In these examples, we limited our queries to the top 50 results. You can also limit your search to be above or below a certain distance threshold. That doesn’t seem super reliable. Relative distances seem more meaningful than discrete amounts. If you’re set on using a threshold, I’d recommend keeping it pretty wide, like 0.1 or 0.05, and using it with a limit. You may get some mileage using a wide range to avoid returning irrelevant long-tail results.

1

Even when the results aren’t icons of dogs, they still feel relevant to the query, like how the ‘snowshoeing’ or ‘snowman’ icons rank highly for ‘samoyed,’ a type of dog bred for sled pulling.

2

COALESCE is just there, so null values become 0. `over ()` is a window function, so we can get the `max` of our desired subset of clicks without using `group by.` If you don’t cast the count to a decimal, the division will truncate, and 0.45 will be rounded to 0.

3

This algorithm is similar to the one used to rank relevant memories in the Simulacra paper, which describes a 0-player game in which AI agents take on the role of 8-bit characters in a simulated town.


