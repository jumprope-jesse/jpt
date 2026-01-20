---
type: link
source: notion
url: https://github.com/fingerthief/recommendarr
notion_type: Software Repo
tags: ['Running']
created: 2025-05-21T04:31:00.000Z
---

# GitHub - fingerthief/recommendarr: An LLM driven recommendation system based on Radarr and Sonarr library or watch history information

## Overview (from Notion)
- Personalized Entertainment: Discovering new TV shows and movies tailored to your interests can enhance family movie nights, making them more enjoyable and engaging for everyone.

- Time-Saving: The AI-driven recommendations can save you time in searching for content amidst an overwhelming amount of options, allowing you to focus more on family and work.

- Integration with Existing Services: If you already use services like Plex or Jellyfin, this tool can seamlessly enhance your media experience without requiring a complete overhaul of your current setup.

- Community Engagement: Joining the Discord community fosters connections with others who share similar interests, which can lead to new friendships and collaboration opportunities.

- Tech Savvy Parenting: Staying on top of new technologies like AI recommendations can help you better understand the digital landscape your kids are growing up in, enabling informed discussions about media consumption.

- Alternate Viewpoints: While AI recommendations are convenient, some argue that they can create echo chambers, limiting exposure to diverse content. Balancing AI suggestions with curated family picks can provide a richer viewing experience.

- Future-Proofing: As a founder, understanding and leveraging emerging technologies like AI in entertainment can inspire innovative ideas for your own projects, keeping you ahead in the competitive landscape.

## AI Summary (from Notion)
Recommendarr is an AI-driven web application that provides personalized TV and movie recommendations by integrating with media libraries like Sonarr, Radarr, Plex, and Jellyfin. It features customizable options, supports various AI services, and requires specific configurations for optimal use.

## Content (from Notion)

# Recommendarr

Recommendarr is a web application that generates personalized TV show and movie recommendations based on your Sonarr, Radarr, Plex, and Jellyfin libraries using AI.

For detailed documentation, please visit the Recommendarr Wiki.

## 🎮 Join our Discord Community!

> 

> 

## 🌟 Features

- AI-Powered Recommendations: Get personalized TV show and movie suggestions based on your existing library.
- Sonarr & Radarr Integration: Connects directly to your media servers to analyze your TV and movie collections.
- Plex, Jellyfin, Tautulli & Trakt Integration: Analyzes your watch history for better recommendations.
- Flexible AI Support: Works with OpenAI, local models (Ollama/LM Studio), or any OpenAI-compatible API. See Compatible AI Services.
- Customization Options: Adjust recommendation count, model parameters, and more.
- Dark/Light Mode: Toggle between themes based on your preference.
- Poster Images: Displays media posters with fallback generation.
For a full list, see Features.

## 📋 Prerequisites

Before installing, ensure you have the necessary services and access. See the Prerequisites page on the wiki for details.

## 🚀 Quick Start (Docker Hub - Easiest)

The simplest way to get started with Recommendarr:

```plain text
# Pull and run with default port 3000
docker run -d \
  --name recommendarr \
  -p 3000:3000 \
  -v recommendarr-data:/app/server/data \
  tannermiddleton/recommendarr:latest
```

Then visit http://localhost:3000 in your browser.

Default Login:

- Username: admin
- Password: 1234 (Change immediately after first login!)
For other installation methods (Docker Compose, Build from Source, Manual), please see the Installation page on the wiki.

## 🔧 Configuration & Usage

After installation, you'll need to connect your media services and set up an AI provider.

- Connecting Services: Connect Sonarr, Radarr, Plex, Jellyfin, Tautulli, Trakt.
- AI Service Setup: Configure OpenAI, Ollama, LM Studio, or other compatible services.
- Authentication Setup (Optional): Set up OAuth login with Google, GitHub, etc.
- Usage: Learn how to generate recommendations.
## 🌐 Advanced Setup

- Reverse Proxy Setup: Run Recommendarr securely behind Nginx, Traefik, etc.
- Environment Variables: Full list of configuration options.
## 🔧 Troubleshooting

Encountering issues? Check the Troubleshooting page on the wiki for common problems and solutions.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

- Vue.js
- Sonarr
- Radarr
- Plex
- Jellyfin
- Tautulli
- Trakt
- OpenRouter

