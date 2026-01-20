---
type: link
source: notion
url: https://github.com/OneUptime/oneuptime/blob/master/App/FeatureSet/Docs/Content/installation/docker-compose.md
notion_type: Software Repo
tags: ['Running']
created: 2024-04-03T14:23:00.000Z
---

# oneuptime/App/FeatureSet/Docs/Content/installation/docker-compose.md at master · OneUptime/oneuptime · GitHub

## AI Summary (from Notion)
- Deployment Option: OneUptime can be hosted on a personal server using Docker Compose for increased control and customization.
- System Requirements:
- Recommended: 16GB RAM, 8 Core, 400 GB Disk, Ubuntu 22.04, Docker and Docker Compose installed.
- Homelab/Minimal: 8 GB RAM, 4 Core, 20 GB Disk, suitable for personal or experimental use.
- Prerequisites: A server running Debian, Ubuntu, or RHEL derivative with Docker and Docker Compose installed.
- Installation Steps:
- Clone the repository and navigate into it.
- Ensure you are on the release branch.
- Configure the environment variables.
- Start the application using npm or Docker Compose.
- Updating: Pull the latest changes and run an update command.
- Logging Considerations: Due to substantial log generation, it’s important to manage Docker logging to prevent storage issues.
- Access: OneUptime runs locally at http://localhost, requiring an account registration for use.
- HTTPS: To use HTTPS, a reverse proxy like Nginx is recommended.

## Content (from Notion)

# Deploy OneUptime completely free with Docker Compose

If you prefer to host OneUptime on your own server, you can use Docker Compose to deploy a single-server instance of OneUptime on Debian, Ubuntu, or RHEL. This option gives you more control and customization over your instance, but it also requires more technical skills and resources to deploy and maintain it.

### Choose Your System Requirements

Depending on your usage and budget, you can choose from different system requirements for your server. For optimal performance, we suggest using OneUptime with:

- Recommended System Requirements 
- Homelab / Minimal Requirements 
### Prerequisites for Single-Server Deployment

Before you start the deployment process, please make sure you have:

- A server running Debian, Ubuntu, or RHEL derivative
- Docker and Docker Compose installed on your server
To install OneUptime:

```plain text
# Clone this repo and cd into it.
git clone https://github.com/OneUptime/oneuptime.git
cd oneuptime

# Please make sure you're on release branch.
git checkout release

# Copy config.example.env to config.env
cp config.example.env config.env

# IMPORTANT: Edit config.env file. Please make sure you have random secrets.

npm start

```

If you don't like to use npm or do not have it installed, run this instead:

```plain text
# Read env vars from config.env file and run docker-compose up.
export $(grep -v '^#' config.env | xargs) && docker compose up --remove-orphans -d

```

To update:

```plain text
git checkout release # Please make sure you're on release branch.
git pull
npm run update

```

### Things to consider

- In our Docker setup, we employ a local logging driver. OneUptime, particularly within the probe and ingestor containers, generates a substantial amount of logs. To prevent your storage from becoming full, it's crucial to limit the logging storage in Docker. For detailed instructions on how to do this, please refer to the official Docker documentation here.
OneUptime should run at: http://localhost. You need to register a new account for your instance to start using it. If you would like to use https, please use a reverse proxy like Nginx.


