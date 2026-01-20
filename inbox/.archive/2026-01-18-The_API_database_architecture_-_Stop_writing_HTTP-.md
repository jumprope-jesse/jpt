---
type: link
source: notion
url: https://www.fabianzeindl.com/posts/the-api-database-architecture
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-05-11T01:29:00.000Z
---

# The API database architecture - Stop writing HTTP-GET endpoints

## AI Summary (from Notion)
- API Database Architecture: Advocates for using PostgREST to eliminate the need for writing HTTP GET endpoints in frameworks like Spring Boot.
- Data Retrieval vs. Modification: Emphasizes separating data retrieval (via GET) from data-modifying requests (POST, PUT, DELETE) to streamline architecture.
- Compatibility: Discusses how this architecture integrates with REST, CQRS, and GraphQL, highlighting its advantages in flexibility and performance.
- Adapting Existing Systems: Provides strategies for transitioning from monolithic systems and microservices to an API database architecture, focusing on minimizing disruption.
- Benefits:
- Simplified adjustments to APIs through SQL view versions.
- Improved performance management via database optimizations.
- Increased independence for frontend teams in data requests.
- Enhanced security with JWT tokens and row-level security in PostgreSQL.
- Consistent and up-to-date OpenAPI schema.
- Easy scalability options for large databases.
- Interesting Fact: PostgREST can serve 2000 requests per second on a low-end server, showcasing its efficiency.
- Hot Take: Suggests that GraphQL may not always be the best choice for data updates due to performance complications.

## Content (from Notion)

For discussion and comments please contact me.

## Table of contents

## Introduction

In a modern software stack based on PostgreSQL, there is no more need for writing HTTP GET endpoints with Spring Boot or any other framework. That's not because GET APIs aren't needed, but because they can be easily provided by using a simple server called PostgREST.

I call this approach the "API database architecture" and it can serve as the data-retrieval layer for an application. The name-giving PostgreSQL database is often already available and in systems where it is not, it can be easily introduced with minimal effort. Strategies to adapt existing architectures are discussed below.

PostgREST directly connects to a PostgreSQL database and serves its views and tables as a RESTful HTTP API. This dynamically created API supports filtering, sorting, paging, and JWT-based authentication out of the box. Aggregation and linking of objects into a combined response are done using a query syntax in the URL. It also supports on-the-fly modification of output formats, like serving a blob of bytes as an image. The API adheres perfectly to standards, serves its own OpenAPI schema, and is more flexible than one that is developed manually. It is also fast and able to serve 2000 requests per second on a single low-end server (see section 'Performance' in the manual).

### Data retrieval via PostgREST, data modification in the existing backend

Essential for the architecture is the conceptual split between data retrieval via HTTP GET and data-modifying requests which use the HTTP-verbs POST, PUT, PATCH, DELETE, or a different, non-HTTP mechanism. Data retrieval generally does not require any custom business logic, while data-modifying requests do. Data modification can be modeled using PostgREST by exposing stored procedures as POST endpoints, but I recommend using that capability only sparingly and instead developing business logic traditionally in the backend. Backend programming languages are much better suited than SQL when describing algorithms that update data step by step.

### Compatibility with REST, CQRS and GraphQL

Modern API development has more or less settled on three architectures, which can be transformed into the API database architecture:

- 
- 
- 
## Strategies for adapting existing architectures

The prerequisite for the API database architecture is to adapt all implementations of data-modifying APIs so that they populate the database with the data needed by the clients. There are various ways to achieve this depending on the existing system.

### Adapting a monolithic system with a single backend

### Monolith strategy 1: Processing the requests and updating the API database from the monolith backend

In a monolithic system with a single backend, all data-modifying APIs remain unchanged, while HTTP-GET requests are routed to PostgREST serving the API database. When working on a request the backend connects to the API database to update the records which are later used for viewing.

### Monolith strategy 2: Re-using the existing database

It is also possible to reuse an existing primary database as an API database. In that case, the backend does not need modification at all. PostgREST allows the configuration of which schema of the PostgreSQL database to expose, so a new schema containing public-facing views can be added, which internally map to existing tables.

### Monolith strategy 3: Updating the API database via batch job

Another possibility, albeit one where caching considerations need to be considered to avoid stale data, is using a batch job that periodically cycles through object IDs of the existing endpoints, requests the necessary data, and writes it into the API database.

### Monolith strategy 4: Pull-based data retrieval using foreign data wrappers

PostgreSQL supports foreign data wrappers that transparently retrieve data from other systems when executing an SQL query. The API database will not store any actual data, but pull it from the existing backend databases or endpoints on demand. This has various performance implications, depending on the foreign data wrapper used, and is more of a theoretical strategy.

### Adapting (domain-driven) microservices with one or more databases

A popular way of structuring systems is splitting up logic into microservices. In a microservice architecture, a request from the front-facing API is processed by multiple services in the backend. The order in which they are called can be either orchestrated by a central service or a process engine that makes calls to other services in turn. These architectures often come with the introduction of domain-driven design even though the concepts do not relate and microservices weren't widely known when domain-driven design became popular.

### Consolidating write access to avoid the problem of distributed transactions

If a request involves multiple services connecting to a database or external APIs the request becomes a distributed transaction. Problems with distributed transactions occur when one microservice commits to a database and another service later in the call chain reverts that decision and needs to undo the transaction made earlier. There are various approaches to work around this problem like the saga pattern, but none of them is perfect. Allowing distributed transactions tends to make the entire architecture vastly more difficult to test and understand. They open the door to many questions and edge cases, which is why it is best to avoid them wherever possible and have only a single service update a database or commit data on an external service as part of a request.

### Microservices strategy 1: Central API database for all services

The most straightforward design for introducing an API database into a microservice architecture is to consolidate all data into a central database and refactor all data-modifying requests in a way that only a single backend writes to the database during the lifetime of a request.

- For each microservice (or each domain) two schemas inside the PostgreSQL database need to be created. One is for storing internal data, and one is for storing the views or tables that are exposed as API. They could be named with prefixes like "_api_myviewtable" and "_internal_mytable" to separate responsibilities cleanly and special PostgreSQL users can be configured so that each service is only allowed to write to tables of its domain.
- The view schemas are served via PostgREST
- Data-modifying requests are routed to an orchestrating microservice, that each domain provides. The service then can connect to various other backends but is responsible for opening the transaction to the API database and storing internal and view-related data. Other backends in the domain should not be allowed to access the database. If desired, the orchestrating microservice can also store all incoming requests in an event log for auditing or for a future transition toward an event-sourcing architecture.
### Microservices strategy 2: One API database for each domain

If multiple databases are used, it is necessary to refactor all requests so that all database transactions relating to one request are only ever done by a single service.

- Set up one or more databases for each domain with a PostgREST server connected to it. Like above their schemas should be split into views that are exposed as API and internal tables used by the backends.
- Use a reverse proxy to route the APIs to the correct PostgREST instances.
- Note that using separate PostgREST instances breaks the dynamic combination of resources since it is only possible to combine data within one database. A client would need to make calls to ask for data from the instances and combine it on the client side. Many frontends to client-side aggregation now, so such exceptions shouldn't prevent you from pursuing such an architecture it is still a vast improvement on the status quo. If such exceptions become necessary be sure to define and document them well.
## Benefits of the API database for the software development process

In summary, the introduction of the API database comes with a lot of benefits:

- Adjustments of HTTP-GET APIs can be done by providing a new version of a view in SQL. For mere data transformations, this avoids development time and has the bonus effect that business analysts who know SQL can work on variants of APIs themselves.
- Performance is transparent and thoroughly understood since all data is preprocessed and available in SQL. When optimizing data retrieval the knowledge of DBAs can be leveraged and there is no need to profile and optimize backends.
- Frontend teams can work more independently since their apps and websites can ask for filtered, sorted, paged, and aggregated data in the way and structure they need it.
- The API will support all features that PostgreSQL supports out of the box like full-text search (https://www.crunchydata.com/blog/postgres-full-text-search-a-search-engine-in-a-database) or geospatial operations via PostGIS.
- Security is cleanly separated. PostgREST uses JWT tokens for authentication and visibility of data can be defined via PostgreSQL users, row-level security, or other mechanisms.
- The API stays consistent and standard-compliant and its OpenAPI schema is always up to date
- During the deployment of new views there is never a mismatch between database migration and backend updates which needs to be considered. When the SQL migrations have been applied successfully the new version of the API is available and guaranteed to be working.
- All standard techniques for scaling PostgreSQL can be used to scale the API. If the API database ever becomes too large, it's possible to do sharding or have separate instances for individual APIs.
- PostgREST needs little configuration and is almost trivial to deploy.
In short, the API database architecture simplifies a system, removes many moving parts, and makes it more flexible and performant.


