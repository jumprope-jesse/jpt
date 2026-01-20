# Trigger.dev - TypeScript Background Jobs Platform

*Source: [Trigger.dev](https://trigger.dev/) - Added: 2026-01-18*

## What It Is

Trigger.dev is a platform for building background jobs and AI workflows in TypeScript. It handles long-running tasks with retries, queues, observability, and elastic scaling - without managing infrastructure.

## Key Features

- **No timeouts** - Unlike Lambda's 15-minute or Vercel's 60-second limits
- **Automatic retries** - Built-in retry logic with configurable policies
- **Queues** - Manage concurrent execution and rate limiting
- **Observability** - Tracing and debugging built in
- **Elastic scaling** - Scales workers automatically
- **Uses existing code** - Works with Node.js SDKs from your repo

## AI Workflow Patterns Supported

| Pattern | Description |
|---------|-------------|
| **Autonomous agents** | Agents that perform complex open-ended tasks with judgment |
| **Prompt chaining** | Multi-stage AI processing flows |
| **Routing** | Smart task distribution to specialized models based on content |
| **Parallelization** | Concurrent execution of multiple AI tasks |
| **Orchestrator** | Coordinate multiple agents for complex objectives |
| **Evaluator-optimizer** | Iterative feedback loops that refine AI outputs |

## Realtime Status

Can display run status (in progress, completed, failed) and metadata in your app for real-time user feedback.

## Deployment Targets

Works with: Vercel, AWS, Remix, Nuxt, SvelteKit, Fastify, RedwoodJS, Cloudflare, Express, Astro, Google Cloud, Azure, Netlify, Next.js

## Why It's Useful

**Problem it solves:** Setting up reliable background jobs traditionally requires:
- ECS or Lambda configuration
- Queue infrastructure (SQS, Redis/BullMQ)
- Retry logic
- Monitoring/alerting
- Horizontal scaling decisions

Trigger.dev packages all of this with a TypeScript-first DX.

## Notable Use Cases (from testimonials)

- **Magic Patterns**: Heavy usage for various workflows, replaced homegrown cron solution
- **MagicSchool AI**: Summarized 1M+ student interactions in weeks
- **Icon**: Video processing - "thousands of videos at once using FFmpeg, ad generation sub-5 minutes with parallel processing"
- **Midday**: "Missing piece to go fully serverless"
- **Papermark**: Document processing - 6,000 documents/month using MuPDF

## Comparison Context

| Alternative | Difference |
|-------------|------------|
| Lambda/Vercel Functions | Trigger.dev has no timeouts, better long-running support |
| BullMQ + Redis + Heroku | Trigger.dev is managed, no infra to maintain |
| Inngest | Similar space; Trigger.dev is more TypeScript-native |
| Zapier/n8n | Trigger.dev is code-first vs UI-based; better for complex automations |

## Relevance to Current Stack

Could be useful for:
- AI processing pipelines that exceed serverless timeouts
- Replacing custom queue/worker setups
- Any TypeScript project needing reliable background jobs

The emphasis on "no timeouts" and "automatic retries" addresses real pain points when building AI features that call external APIs or run multi-step workflows.
