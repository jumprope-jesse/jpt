---
type: link
source: notion
url: https://github.com/nucleuscloud/neosync
notion_type: Software Repo
tags: ['Running']
created: 2024-05-23T13:35:00.000Z
---

# GitHub - nucleuscloud/neosync: Open source data anonymization and synthetic data orchestration for developers. Create high fidelity synthetic data and sync it across your environments.

## AI Summary (from Notion)
- Project Overview: Neosync is an open-source tool designed for data anonymization and synthetic data orchestration, aimed at improving developer experience.
- Key Functions:
- Anonymizes PII to safely test code against production data.
- Generates synthetic data for testing, debugging, and compliance.
- Allows local reproduction of production bugs using anonymized data.
- Hydrates staging and QA environments with production-like data.
- Features:
- Generates synthetic data based on database schema.
- Handles asynchronous job pipelines with automatic retry and failure management.
- Supports referential integrity and GitOps-based configurations.
- Integrates with major data storage solutions like Postgres and S3.
- Getting Started:
- Easy setup with Docker using a provided compose.yml file.
- Commands to start and stop the service are simple (make compose-up and make compose-down).
- Deployment and Resources:
- Provides documentation, a Discord community for support, and resources for contributions.
- Licensing: The project is available under the MIT license, emphasizing a commitment to free and open-source software.

## Content (from Notion)

Open Source Data Anonymization and Synthetic Data Orchestration

| Website | Docs | Discord | Blog | Changelog |

## Introduction

Neosync is an open-source, developer-first way to anonymize PII, generate synthetic data and sync environments for better testing, debugging and developer experience.

Companies use Neosync to:

1. Safely test code against production data - Anonymize sensitive production data in order to safely use it locally for a better testing and developer experience
1. Easily reproduce production bugs locally - Anonymize and subset production data to get a safe, representative data set that you can use to locally reproduce production bugs quickly and efficiently
1. Fix broken staging environments - Catch bugs before they hit production when you hydrate your staging and QA environments with production-like data
1. Reduce your compliance scope - Use anonymized and synthetic data to reduce your compliance scope and easily comply with laws like HIPAA, GDPR, and DPDP
1. Seed development databases - Easily seed development databases with synthetic data for unit testing, demos and more
## Features

- Generate synthetic data based on your schema
- Anonymize existing production-data for a better developer experience
- Subset your production database for local and CI testing using any SQL query
- Complete async pipeline that automatically handles job retries, failures and playback using an event-sourcing model
- Referential integrity for your data automatically
- Declarative, GitOps based configs as a step in your CI pipeline to hydrate your CI DB
- Pre-built data transformers for all major data types
- Custom data transformers using javascript or LLMs
- Pre-built integrations with Postgres, Mysql, S3
## Getting started

Neosync is a fully dockerized setup which makes it easy to get up and running.

A compose.yml file at the root contains production image refs that allow you to get up and running with just a few commands without having to build anything on your system.

Neosync uses the newer docker compose command, so be sure to have that installed on your machine.

To start Neosync, clone the repo into a local directory, be sure to have docker insalled and running, and then run:

```plain text
make compose-up
```

To stop, run:

```plain text
make compose-down
```

Neosync will now be available on http://localhost:3000.

The production compose pre-seeds with connections and jobs to get you started! Simply run the generate and sync job to watch Neosync in action!

## Kubernetes, Auth Mode and more

For more in-depth details on environment variables, Kubernetes deployments, and a production-ready guide, check out the Deploy Neosync section of our Docs.

## Resources

Some resources to help you along the way:

- Docs for comprehensive documentation and guides
- Discord for discussion with the community and Neosync team
- X for the latest updates
## Contributing

We love contributions big and small. Here are just a few ways that you can contribute to Neosync.

- Join our Discord channel and ask us any questions there
- Open a PR (see our instructions on developing with Neosync locally)
- Submit a feature request or bug report
## Licensing

We strongly believe in free and open source software and make this repo is available under the MIT expat license.


