---
type: link
source: notion
url: https://github.com/gethomepage/homepage
notion_type: Software Repo
tags: ['Running']
created: 2025-05-21T04:20:00.000Z
---

# GitHub - gethomepage/homepage: A highly customizable homepage (or startpage / application dashboard) with Docker and service API integrations.

## Overview (from Notion)
- Efficiency and Customization: The highly customizable dashboard could streamline your daily tasks, consolidating information and services you rely on as a busy professional and parent.
- Service Integrations: With over 100 service integrations, easily manage work and family needs, from scheduling to home automation, all in one place.
- Performance Focus: The emphasis on speed and security means you can trust the platform to handle sensitive information, crucial for both your professional and personal life.
- Family-Friendly Features: Consider utilizing the weather and calendar widgets to keep your family organized, especially with kids’ activities and events.
- Remote Work Compatibility: As a company founder, the Docker integration can enhance your development workflow, enabling smoother collaboration with remote teams.
- Security Awareness: The security notice highlights the importance of protecting personal data, an essential consideration for your family's digital safety.
- Community Contributions: Engaging in the open-source community could provide networking opportunities and insights into innovative practices that could benefit your business.
- Sustainability Considerations: The project’s use of Docker and static site generation aligns with modern software practices that emphasize efficiency and sustainability, reflecting a growing trend in tech.

Alternate Views:
- Complexity vs. Usability: While highly customizable, the complexity may overwhelm some users; simpler solutions might be more suitable for those less tech-savvy.
- Dependence on Technology: Relying heavily on such integrations might lead to over-dependence on technology for daily tasks, potentially impacting personal interactions.

## AI Summary (from Notion)
A highly customizable application dashboard with Docker support, featuring over 100 service integrations, quick search, bookmarks, and a focus on performance, security, and multilingual support. Configuration is done via YAML or Docker labels, and it is recommended to deploy behind a reverse proxy for security. Documentation and support are available online.

## Content (from Notion)

A modern, fully static, fast, secure fully proxied, highly customizable application dashboard with integrations for over 100 services and translations into multiple languages. Easily configured via YAML files or through docker label discovery.

Homepage builds are kindly powered by DigitalOcean.

# Features

With features like quick search, bookmarks, weather support, a wide range of integrations and widgets, an elegant and modern design, and a focus on performance, Homepage is your ideal start to the day and a handy companion throughout it.

- Fast - The site is statically generated at build time for instant load times.
- Secure - All API requests to backend services are proxied, keeping your API keys hidden. Constantly reviewed for security by the community.
- For Everyone - Images built for AMD64, ARM64.
- Full i18n - Support for over 40 languages.
- Service & Web Bookmarks - Add custom links to the homepage.
- Docker Integration - Container status and stats. Automatic service discovery via labels.
- Service Integration - Over 100 service integrations, including popular starr and self-hosted apps.
- Information & Utility Widgets - Weather, time, date, search, and more.
- And much more...
## Docker Integration

Homepage has built-in support for Docker, and can automatically discover and add services to the homepage based on labels. See the Docker Service Discovery page for more information.

## Service Widgets

Homepage also has support for hundreds of 3rd-party services, including all popular *arr apps, and most popular self-hosted apps. Some examples include: Radarr, Sonarr, Lidarr, Bazarr, Ombi, Tautulli, Plex, Jellyfin, Emby, Transmission, qBittorrent, Deluge, Jackett, NZBGet, SABnzbd, etc. As well as service integrations, Homepage also has a number of information providers, sourcing information from a variety of external 3rd-party APIs. See the Service page for more information.

## Information Widgets

Homepage has built-in support for a number of information providers, including weather, time, date, search, glances and more. System and status information presented at the top of the page. See the Information Providers page for more information.

## Customization

Homepage is highly customizable, with support for custom themes, custom CSS & JS, custom layouts, formatting, localization and more. See the Settings page for more information.

# Getting Started

For configuration options, examples and more, please check out the homepage documentation.

## Security Notice 🔒

Please note that when using features such as widgets, Homepage can access personal information (for example from your home automation system) and Homepage currently does not (and is not planned to) include any authentication layer itself. Thus, we recommend homepage be deployed behind a reverse proxy including authentication, SSL etc, and / or behind a VPN.

## With Docker

Using docker compose:

```plain text
services:
  homepage:
    image: ghcr.io/gethomepage/homepage:latest
    container_name: homepage
    environment:
      HOMEPAGE_ALLOWED_HOSTS: gethomepage.dev # required, may need port. See gethomepage.dev/installation/#homepage_allowed_hosts
      PUID: 1000 # optional, your user id
      PGID: 1000 # optional, your group id
    ports:
      - 3000:3000
    volumes:
      - /path/to/config:/app/config # Make sure your local config directory exists
      - /var/run/docker.sock:/var/run/docker.sock:ro # optional, for docker integrations
    restart: unless-stopped
```

or docker run:

```plain text
docker run --name homepage \
  -e HOMEPAGE_ALLOWED_HOSTS=gethomepage.dev \
  -e PUID=1000 \
  -e PGID=1000 \
  -p 3000:3000 \
  -v /path/to/config:/app/config \
  -v /var/run/docker.sock:/var/run/docker.sock:ro \
  --restart unless-stopped \
  ghcr.io/gethomepage/homepage:latest
```

## From Source

First, clone the repository:

```plain text
git clone https://github.com/gethomepage/homepage.git
```

Then install dependencies and build the production bundle:

```plain text
pnpm install
pnpm build
```

If this is your first time starting, copy the src/skeleton directory to config/ to populate initial example config files.

Finally, run the server in production mode:

```plain text
pnpm start
```

# Configuration

Please refer to the homepage documentation website for more information. Everything you need to know about configuring Homepage is there. Please read everything carefully before asking for help, as most questions are answered there or are simple YAML configuration issues.

# Development

Install NPM packages, this project uses pnpm (and so should you!):

```plain text
pnpm install
```

Start the development server:

```plain text
pnpm dev
```

Open http://localhost:3000 to start.

This is a Next.js application, see their documentation for more information.

# Documentation

The homepage documentation is available at https://gethomepage.dev/.

Homepage uses Material for MkDocs for documentation. To run the documentation locally, first install the dependencies:

```plain text
pip install -r requirements.txt
```

Then run the development server:

```plain text
mkdocs serve # or build, to build the static site
```

# Support & Suggestions

If you have any questions, suggestions, or general issues, please start a discussion on the Discussions page.

## Troubleshooting

In addition to the docs, the troubleshooting guide can help reveal many basic config or network issues. If you're having a problem, it's a good place to start.

## Contributing & Contributors

Contributions are welcome! Please see the CONTRIBUTING.md file for more information.

Thanks to the over 200 contributors who have helped make this project what it is today!

Especially huge thanks to @shamoon, who has been the backbone of this community from the very start.


