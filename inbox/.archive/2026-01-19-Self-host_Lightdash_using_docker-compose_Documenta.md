---
type: link
source: notion
url: https://docs.lightdash.com/self-host/self-host-lightdash-docker-compose
notion_type: Software Repo
tags: ['Running']
created: 2024-02-14T15:43:00.000Z
---

# Self-host Lightdash using docker-compose | Documentation | Lightdash

## AI Summary (from Notion)
- Purpose: The document serves as a guide to self-host Lightdash using Docker and Docker Compose for local use.
- Accessibility: The Lightdash instance will be accessible only from the local machine, useful for proof-of-concept projects.
- Prerequisites:
- Requires installation of Docker and Docker Compose.
- Key Steps:
- Clone the Repository: The user should clone the Lightdash GitHub repository to create a local directory.
- Update ENV Configuration: Users need to edit the .env file to set environment variables for their setup.
- Create Containers: Users must set environment variables for the PostgreSQL password and Lightdash secret, followed by running Docker Compose to start the containers.
- Important Note: Windows users may encounter an error related to Docker daemon settings, which can be resolved by enabling the option to expose the daemon on a specified TCP port.

## Content (from Notion)

This guide will give you a minimal Lightdash instance running on your local machine. It will not be accessible from the internet, but it will be accessible from your local machine. This is a great way to get started with Lightdash for a proof-of-concept without needing access to kubernetes.

## Prerequisites

- Docker
- Docker Compose
## 1. Clone the Lightdash repository

Clone the Lightdash code to your local machine. This will create a new directory called ./lightdash (the Lightdash directory).

```plain text
# Clone the Lightdash repo
git clone https://github.com/lightdash/lightdash
cd lightdash

```

## 2. Update your ENV config

Edit all the ENV variables in .env to match your setup, eg:

```plain text
PGHOST=db
PGPORT=5432
PGUSER=pg_user *OR* machine username if no prior postgres set up
PGPASSWORD=pg_password *OR* blank if no prior postgres set up
PGDATABASE=postgres
DBT_DEMO_DIR=/*path*/*to*/lightdash/project/examples/full-jaffle-shop-demo
LIGHTDASH_CONFIG_FILE=/*path*/*to*/lightdash/lightdash.yml

```

## 3. Create containers

You must set the following two environment variables:

- PGPASSWORD is the password used for the internal postgres database
- LIGHTDASH_SECRET is the secret used to encrypt data at rest in the database. If you lose this secret, you will not be able to access your data in Lightdash.
```plain text
export LIGHTDASH_SECRET="not very secret"
export PGPASSWORD="password"
docker-compose -f docker-compose.yml --env-file .env up --detach --remove-orphans

```

info

If you have a Windows machine and get the error Error response from daemon: i/o timeout. Go to Docker > Settings > General and enable the option Expose daemon on tcp://localhost:2375 without TLS


