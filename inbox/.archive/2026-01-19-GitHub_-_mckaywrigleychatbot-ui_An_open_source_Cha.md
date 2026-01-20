---
type: link
source: notion
url: https://github.com/mckaywrigley/chatbot-ui
notion_type: Product Website
tags: 
created: 2023-12-02T14:38:00.000Z
---

# GitHub - mckaywrigley/chatbot-ui: An open source ChatGPT UI.

## AI Summary (from Notion)
- Project Overview: GitHub repository for an open source ChatGPT UI called Chatbot UI.
- Creation Date: December 2, 2023.
- Status: Not started.
- Key Updates:
- Chatbot UI 2.0 is released as an updated, hosted product.
- An open source version is coming soon.
- About the Project:
- Chatbot UI is designed for AI models and facilitates chatting capabilities.
- Deployment Options:
- Vercel: Host a live version.
- Docker: Build and run locally.
- Local Setup Steps:
- Clone the repository, install dependencies, provide OpenAI API key, and run the application.
- Configuration Options: Environment variables can be set for API keys, hosts, models, and other parameters.
- Contact: Users can reach out to Mckay on Twitter for inquiries.
- Community Engagement: User feedback and contributions are encouraged; recent comments highlight enhancements like multi-platform Docker support.
- Interesting Fact: The project allows customization of various parameters, enabling flexibility in deployment and usage.

## Content (from Notion)

# Chatbot UI

## News

Chatbot UI 2.0 is out as an updated, hosted product!

Check out Takeoff Chat.

Open source version coming soon!

## About

Chatbot UI is an open source chat UI for AI models.

See a demo.

## Updates

Chatbot UI will be updated over time.

Expect frequent improvements.

Next up:

- Sharing
- "Bots"
## Deploy

Vercel

Host your own live version of Chatbot UI with Vercel.

Docker

Build locally:

```plain text
docker build -t chatgpt-ui .
docker run -e OPENAI_API_KEY=xxxxxxxx -p 3000:3000 chatgpt-ui
```

Pull from ghcr:

```plain text
docker run -e OPENAI_API_KEY=xxxxxxxx -p 3000:3000 ghcr.io/mckaywrigley/chatbot-ui:main

```

## Running Locally

1. Clone Repo

```plain text
git clone https://github.com/mckaywrigley/chatbot-ui.git
```

2. Install Dependencies

```plain text
npm i
```

3. Provide OpenAI API Key

Create a .env.local file in the root of the repo with your OpenAI API Key:

```plain text
OPENAI_API_KEY=YOUR_KEY
```

> 

> 

4. Run App

```plain text
npm run dev
```

5. Use It

You should be able to start chatting.

## Configuration

When deploying the application, the following environment variables can be set:

If you do not provide an OpenAI API key with OPENAI_API_KEY, users will have to provide their own key.

If you don't have an OpenAI API key, you can get one here.

## Contact

If you have any questions, feel free to reach out to Mckay on Twitter.

## Conversation

###  fox91  commented Apr 12, 2023

Docker: add support to linux/arm64 and release it as a multi-platform image.

Added support to docker multi-platform image, close #518

ff76ae0


