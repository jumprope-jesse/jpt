---
type: link
source: notion
url: https://docs.heyform.net/self-hosting
notion_type: Software Repo
tags: ['Running']
created: 2024-04-02T03:00:00.000Z
---

# Self-Hosting

## AI Summary (from Notion)
- Self-Hosting Overview: Instructions on how to self-host the HeyForm application using Docker.
- Prerequisites:
- Basic understanding of Docker and containerization.
- Installation of Docker and Docker Compose.
- Setup Steps:
1. Create a docker.env file for environment variables.
2. Install Docker and Docker Compose using Homebrew or Chocolatey.
3. Create a docker-compose.yml file with services for HeyForm, MongoDB, and Redis.
- Docker Compose Configuration:
- Defines services for HeyForm, MongoDB, and Redis with respective images and configurations.
- Running the Application:
- Start the application using docker-compose up -d.
- The command creates a database, runs migrations, and starts the HeyForm app on port 8000.
- Access: Navigate to http://<server ip>:8080 for the login screen.
- SSL Note: The application runs on unencrypted HTTP; a reverse proxy is needed for HTTPS.

## Content (from Notion)

Before you begin, ensure you have the following:

- Basic knowledge of Docker and containerization principles.
- Docker and Docker Compose are installed on your machine.
Using this sample file as a reference create a docker.env file to contain the environment variables for your installation.

1.Install Docker and Docker Compose:

```plain text
brew install docker docker-compose
```

```plain text
choco install docker-desktop docker-compose -y
```

2.Create a docker-compose.yml file, an example configuration with all dependencies dockerized and environment variables kept in docker.env is as follows.

```plain text
version: "3"

services:
  heyform:
    image: heyform/community-edition:latest
    env_file: ./docker.env
    ports:
      - "8000:8000"
    depends_on:
      - mongo
      - redis

  mongo:
    image: mongo:4.4.29
    restart: "always"
    ports:
      - "27017:27017"

  redis:
    image: redis
    restart: "always"
    command: "redis-server --appendonly yes"
    ports:
      - "6379:6379"
```

Make sure you are in the same directory as docker-compose.yml and start HeyForm:

```plain text
docker-compose up -d
```

When you run this command, by default, it does the following:

- Create a database
- Run the migrations
- Start the HeyForm web app on port 8000
You can now navigate to http://<server ip>:8080 and see the login screen. HeyForm itself does not perform SSL termination. It only runs on unencrypted HTTP. If you want to run on HTTPS you also need to set up a reverse proxy in front of the server.


