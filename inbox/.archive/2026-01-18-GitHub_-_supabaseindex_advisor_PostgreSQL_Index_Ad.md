---
type: link
source: notion
url: https://github.com/supabase/index_advisor
notion_type: Software Repo
tags: ['Running']
created: 2024-04-14T05:14:00.000Z
---

# GitHub - supabase/index_advisor: PostgreSQL Index Advisor

## AI Summary (from Notion)
- Project Overview: PostgreSQL Index Advisor is a GitHub project aimed at recommending indexes to enhance query performance.
- Creation Date: The project was created on April 14, 2024.
- Status: The project is currently not started.
- Key Features:
- Supports generic parameters (e.g., $1, $2).
- Handles materialized views.
- Can identify tables and columns obscured by views.
- Functionality: The index_advisor function analyzes a SQL query and returns suggested create index statements to optimize execution time.
- Usage Example: A simple example demonstrating how to use the index_advisor with a single table query.
- Complex Queries: More complex SQL queries can yield multiple suggested indexes for performance improvement.
- Installation Requirements: Requires PostgreSQL with the hypopg extension installed.
- Testing: The project includes tests that can be run with make installcheck.

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


