---
type: link
source: notion
url: https://du.nkel.dev/blog/2024-02-10_keycloak-docker-compose-nginx/
notion_type: Software Repo
tags: ['Running']
created: 2024-02-11T14:05:00.000Z
---

# Keycloak SSO with docker compose and nginx - du.nkel.dev

## AI Summary (from Notion)
- Purpose: The document provides a guide for setting up Keycloak Single Sign-On (SSO) using Docker Compose and Nginx.
- Keycloak Overview: Keycloak is an open-source solution for identity and access management that supports major SSO protocols (OIDC, OAuth 2.0, SAML).
- Setup Complexity: The setup is described as not overly complicated but not straightforward, highlighting the need for detailed instructions.
- Conceptual Framework: The guide uses a central Nginx reverse proxy to direct traffic to different services, all running in isolated Docker environments.
- Preparation Requirements:
- Basic tools: SSH and a Linux VM.
- A domain or subdomain for adding DNS records.
- User Management: Emphasizes the importance of user management and security in web applications, especially in light of current security challenges.
- Installation Steps:
- Create a new non-root user for Keycloak.
- Set up Docker in rootless mode.
- Create necessary directories for persistent data.
- Configuration: Provides guidance on creating a docker-compose.yml file and an .env file for sensitive information.
- Testing: Instructions for testing the Docker Compose stack locally and accessing Keycloak via a browser.
- Nginx Integration: Steps for configuring Nginx as a reverse proxy and obtaining SSL certificates using Certbot.
- Debugging: Tips for troubleshooting issues, including checking logs for both Docker and Nginx.
- Customization: Information on building a custom Docker image for Keycloak to allow for further customization, such as theming.
- Next Steps: Suggestions for further configuration, such as adding realms and email settings in the Keycloak admin console.
- Call for Feedback: Encouragement for readers to share improvements or suggestions in the comments section.

## Content (from Notion)

Published: 2024-02-11, Revised: 2024-02-11

TL;DR I always hesitated to deploy an extra tool for user management and SSO, but the current state of the web makes it very difficult to keep up with security, CVEs etc. Why not trust one of the longest standing solutions for identity and access management? Keycloak is open source, interoperable with major SSO protocols (OpenID Connect (OIDC), OAuth 2.0, SAML), and robust. The setup with docker compose is not complicated, but it was not straight forward either. This is why I provide a summary of the process below.

Info

This is currently a stub. I thought I would share my docker-compose.yml and nginx.conf quickly and update the post later to add steps for theming and integration.

## Concept

You may have seen the concept below already in my previous post about Mastodon. We will use a standard setup of nginx as a central reverse proxy that forwards traffic through localhost to individual services, all running in their own rootless docker namespaces. I consider this the typical economical setup, by sharing resources of a single host but with maximally isolated environments. Adapt where this does not fit your usecase.

```plain text
                                                      Web
                                                       |
                                                       |
                                                  0.0.0.0:80
                                                  0.0.0.0:443
+------------------------------------------------------+-----------------------------------------------------+
|                                                      |                                                     |
|                                                      v                                                     |
|                +------------------------------- nginx/acme -----------------------------+                  |
|                |                                     |                                  |                  |
|        http://127.0.0.1:3000                         |                                  |                  |
|        http://127.0.0.1:4000                http://127.0.0.1:8080              http://127.0.0.1:9999       |
| +--------------+---------------+      +--------------+---------------+    +-------------+----------------+ |
| |              |               |      |              |               |    |             |                | |
| |   Rootless Docker Service    |      |   Rootless Docker Service    |    |   Rootless Docker Service    | |
| |    +---------+----------+    |      |    +---------+----------+    |    |    +--------+-----------+    | |
| |    |         |          |    |      |    |         |          |    |    |    |        |           |    | |
| |    |         v          |    |      |    |         v          |    |    |    |        v           |    | |
| |    |  Mastdon Docker    |    |      |    |  Keycloak Docker   |    |    |    |  Nextcloud Docker  |    | |
| |    |                    |    |      |    |                    |    |    |    |                    |    | |
| |    |                    |    |      |    |                    |    |    |    |                    |    | |
| |    +--------------------+    |      |    +--------------------+    |    |    +--------------------+    | |
| |                              |      |                              |    |                              | |
| +------------------------------+      +------------------------------+    +------------------------------+ |
|                                                                                                            |
+------------------------------------------------------------------------------------------------------------+


```

## Preparations

You will need some basic tools:

- SSH
- A VM with Linux (Ubuntu; Debian etc.)
- A domain or subdomain where you can add an A (and optionally AAAA) record for your service
Follow the Mastodon post for basic setup of docker rootless to:

- create a new non-root user named keycloak, without password, with its home directory set to /srv/keycloak
- update /etc/subuid and /etc/subgid ranges with user keycloak (because e.g. the postgres container will need these to create a nested non-root user itself)
- install docker rootless through dockerd-rootless-setuptool.sh and configure automatic service start for the keycloak user
## Keycloak Setup

Login to the newly created keycloak user.

```plain text
machinectl shell keycloak@

```

Warning

We need to use machinectl to login, otherwise XDG_RUNTIME_DIR environment variables will not be available. Do not use (e.g.) sudo -u keycloak -H bash.

Create directories for persistent data (data/postgres16) and the docker files.

```plain text
cd ~ \
  && mkdir -p data/postgres16 \
  && mkdir docker && cd docker

```

### docker-compose.yml

The official docs provide some information here 1. But they use docker run, which would be unusual in production.

Going to a compose file is not complicated and allows us to have a more reproducable setup. There are some example docker-compose.ymls available, such as 2, 3 or 4.

We will start with a docker-compose.yml that directly uses the official keycloak image. This can be changed later.

Create an .env file with your sensitive and variable information:

Contents (change passwords):

The relevant documentation of all these variables can be found here 5.

## Test locally

At this stage, we can test the docker compose stack:

Afterwards, create a reverse SSH tunnel to your VM and the keycloak local port.

Open 127.0.0.1:8080 in your browser and you should be greeted with the keycloak welcome screen:

## nginx

Logout from the keycloak user with CTRL+D.

Follow the Mastodon post for setup of nginx as a system reverse proxy.

Create a new nginx .conf for the keycloak service.

We can find some relevant information in the keycloak docs 6.

Test the configuration and reload nginx.

Use certbot to request SSL certificates for your service.

This will automatically update necessary lines in your.tld.com.conf.

Edit your.tld.com.conf and uncomment ssl_trusted_certificate.

Reload nginx

## Debug

You can now open your.tld.com and login to keycloak using the admin user with the password from the .env file.

For debugging, the first stop are the docker compose logs.

For nginx, follow the access and error logs.

If you need to have a look at the keycloak database.

## Custom build with Dockerfile

So far, we are using the prebuild image from quay.io.

For any customization, e.g. in order to use themes and run the keycloak container in --optimized mode 8, we need to build our own image.

We will utilize a multi-stage docker build 9 starting with the official quay.io image.

Add a Dockerfile

.. with the following content.

Afterwards, edit the docker-compose.yml:

- remove or comment out the image: line
- uncomment build: .
- add command: start --optimized
Restart the docker stack afterwards with

This will build the image and start the service.

## Conclusions

We are now running a keycloak service in rootless docker behind our system nginx reverse proxy, which does the SSL termination for us.

For automatic updates of the docker container, see the Mastodon post.

The next step would be logging in to the keycloak services and adding an email under https://your.tld.com/admin/master/console/#/master/realm-settings/email.

Next comes (e.g.) adding a realm. Then theming, which can be done with keycloakify 10.

You can see that I already added the necessary lines to the Dockerfile:

If you find improvements to the instructions above, please add in the comments section!


