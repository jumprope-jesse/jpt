# Open Source Chat UI Tools

## Chatbot UI (mckaywrigley)

**Repository**: https://github.com/mckaywrigley/chatbot-ui
**Status**: Active open source project (as of Dec 2023)
**Hosted Version**: Takeoff Chat (v2.0)

### Overview
Open source chat interface for AI models (primarily OpenAI). Provides a clean, deployable ChatGPT-like interface.

### Key Features
- Self-hostable ChatGPT UI
- Support for OpenAI API
- Docker deployment support (multi-platform: linux/amd64, linux/arm64)
- Vercel deployment option
- Environment variable configuration
- Planned features (as of Dec 2023): Sharing, "Bots"

### Deployment Options

**Vercel**:
- One-click deploy to Vercel hosting

**Docker**:
```bash
# Build locally
docker build -t chatgpt-ui .
docker run -e OPENAI_API_KEY=xxxxxxxx -p 3000:3000 chatgpt-ui

# Or pull from registry
docker run -e OPENAI_API_KEY=xxxxxxxx -p 3000:3000 ghcr.io/mckaywrigley/chatbot-ui:main
```

**Local Development**:
```bash
git clone https://github.com/mckaywrigley/chatbot-ui.git
npm i
# Create .env.local with OPENAI_API_KEY=YOUR_KEY
npm run dev
```

### Configuration
- `OPENAI_API_KEY`: Required for API access (users can provide their own if not set)
- Supports various environment variables for API hosts, models, parameters

### Use Cases
- Self-hosted ChatGPT alternative
- Custom AI chat interfaces
- Privacy-focused deployments
- Reference implementation for chat UIs

### Notes
- As of Dec 2023, v2.0 was being released as hosted product
- Open source version continues to be maintained
- Good starting point for building custom chat interfaces
