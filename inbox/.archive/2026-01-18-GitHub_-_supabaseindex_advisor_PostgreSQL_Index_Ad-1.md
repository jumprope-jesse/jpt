---
type: link
source: notion
url: https://github.com/supabase/index_advisor
notion_type: Software Repo
tags: ['Running']
created: 2024-04-14T05:13:00.000Z
---

# GitHub - supabase/index_advisor: PostgreSQL Index Advisor

## AI Summary (from Notion)
- Project Overview: The document outlines the PostgreSQL Index Advisor, a tool designed to recommend indexes to improve query performance in PostgreSQL databases.
- Creation Date: The project was created on April 14, 2024.
- Current Status: The project is currently not started.
- Key Features:
- Supports generic parameters (e.g., $1, $2).
- Handles materialized views.
- Identifies tables and columns obscured by views.
- Functionality:
- The index_advisor(query text) function analyzes a given SQL query and returns suggested CREATE INDEX statements to enhance execution time.
- Examples:
- Simple example: A query on the book table with an unindexed column, showing the improvement in startup and total costs after applying suggested indexes.
- More complex example: A multi-table query involving book, author, publisher, and review, with multiple suggested indexes for performance optimization.
- Installation Requirements: Requires PostgreSQL with the hypopg extension installed.
- Testing: Instructions are provided for running tests on the installation.
- Repository Link: The project is hosted on GitHub at the provided URL.

## Content (from Notion)

# PostgreSQL Index Advisor

A PostgreSQL extension for recommending indexes to improve query performance.

## Features

- Supports generic parameters e.g. $1, $2
- Supports materialized views
- Identifies tables/columns obfuscaed by views
## API

### Description

For a given query, searches for a set of SQL DDL create index statements that improve the query's execution time;

### Signature

```plain text
index_advisor(query text)
returns
    table  (
        startup_cost_before jsonb,
        startup_cost_after jsonb,
        total_cost_before jsonb,
        total_cost_after jsonb,
        index_statements text[],
        errors text[]
    )
```

## Usage

For a minimal example, the index_advisor function can be given a single table query with a filter on an unindexed column.

```plain text
create extension if not exists index_advisor cascade;

create table book(
  id int primary key,
  title text not null
);

select
    *
from
  index_advisor('select book.id from book where title = $1');

```

```plain text
 startup_cost_before | startup_cost_after | total_cost_before | total_cost_after |                  index_statements                   | errors
---------------------+--------------------+-------------------+------------------+-----------------------------------------------------+--------
 0.00                | 1.17               | 25.88             | 6.40             | {"CREATE INDEX ON public.book USING btree (title)"},| {}

(1 row)
```

More complex queries may generate additional suggested indexes

```plain text
create extension if not exists index_advisor cascade;

create table author(
    id serial primary key,
    name text not null
);

create table publisher(
    id serial primary key,
    name text not null,
    corporate_address text
);

create table book(
    id serial primary key,
    author_id int not null references author(id),
    publisher_id int not null references publisher(id),
    title text
);

create table review(
    id serial primary key,
    book_id int references book(id),
    body text not null
);

select
    *
from
    index_advisor('
        select
            book.id,
            book.title,
            publisher.name as publisher_name,
            author.name as author_name,
            review.body review_body
        from
            book
            join publisher
                on book.publisher_id = publisher.id
            join author
                on book.author_id = author.id
            join review
                on book.id = review.book_id
        where
            author.id = $1
            and publisher.id = $2
    ');

```

```plain text
 startup_cost_before | startup_cost_after | total_cost_before | total_cost_after |                  index_statements                         | errors
---------------------+--------------------+-------------------+------------------+-----------------------------------------------------------+--------
 27.26               | 12.77              | 68.48             | 42.37            | {"CREATE INDEX ON public.book USING btree (author_id)",   | {}
                                                                                    "CREATE INDEX ON public.book USING btree (publisher_id)",
                                                                                    "CREATE INDEX ON public.review USING btree (book_id)"}
(3 rows)
```

## Install

Requires Postgres with hypopg installed.

```plain text
git clone https://github.com/supabase/index_advisor.git
cd index_advisor
sudo make install
```

## Run Tests

```plain text
make install; make installcheck
```


