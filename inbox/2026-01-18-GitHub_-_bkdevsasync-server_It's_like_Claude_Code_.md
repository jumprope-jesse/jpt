---
type: link
source: notion
url: https://github.com/bkdevs/async-server
notion_type: Software Repo
tags: ['Running']
created: 2025-08-27T03:39:00.000Z
---

# GitHub - bkdevs/async-server: It's like Claude Code + Linear + GitHub PR

## Overview (from Notion)
- Async-server streamlines coding tasks, which can help balance your work and family life by reducing the time spent on code reviews and task management.
- The integration of AI with traditional coding practices offers an innovative approach that could inspire you to adopt new technologies in your own company.
- The ability to execute code changes in the cloud without affecting local environments means you can work from anywhere, providing flexibility for family commitments.
- Its focus on planning and eliminating context switching could enhance productivity, allowing you to dedicate more quality time to family.
- Consider the impact of AI in your industry—while it can boost efficiency, it might also lead to concerns about job displacement or the need for continual upskilling.
- Unique viewpoint: Async-server's automation can be viewed as a tool that empowers developers to focus on creative problem-solving instead of getting bogged down in repetitive tasks.
- Alternate view: Emphasize the importance of human oversight in AI-driven processes to maintain quality and accountability in software development.

## AI Summary (from Notion)
Async is an open-source developer tool that integrates AI coding with task management and code review, allowing for automated research, execution of code changes in the cloud, and streamlined code reviews. It simplifies task tracking by importing GitHub issues, eliminates context switching, and requires upfront planning before executing tasks. The tool operates through a series of isolated Google Cloud Run jobs for task processing and supports various integrations, including GitHub and Stripe for payments.

## Content (from Notion)

An open-source developer tool that combines AI coding with task management and code review. Async integrates Claude Code + Linear + GitHub PRs into one opinionated workflow.

https://www.async.build/

## What Async Does

- Automatically researches coding tasks - analyzes your codebase and asks clarifying questions before execution
- Executes code changes in the cloud - runs in isolated environments without touching your local setup
- Breaks work into reviewable subtasks - creates stack diffs for easier code review
- Handles the full workflow - from GitHub issue to merged PR without leaving the app
## Why Async?

Traditional AI coding tools work great for new projects but struggle with mature codebases where you can't break things. Async solves the common problems:

- Forces upfront planning - always asks clarifying questions and requires confirmation before executing
- Eliminates context switching - executes asynchronously in the cloud while you work on other tasks
- Simple task tracking - automatically imports GitHub issues, no PM tool bloat
- Built-in code review - comment and iterate on stacked diffs without leaving the app
## How It Works

1. 
1. 
1. 
1. 
## Tech Stack

- Backend: FastAPI with async support
- AI Models: Claude Code for implementation, OpenAI/Anthropic/Google models for research
- Cloud: Google Cloud Platform with containerized execution
- Database: Firebase Firestore
- Integrations: GitHub App, Stripe payments, email notifications
- Frontend: Supports desktop and mobile
## Setup

Create and activate a virtual envirnoment:

```plain text
uv venv .venv
source .venv/bin/activate

```

To explicitly sync the environment, run the following command:

```plain text
uv sync

```

Then run the following to setup pre-commit lints

```plain text
pre-commit install

```

## Local Development

To run the agent locally, create a .env file (look at .env.local for example) in the root directory.

Create a firebase config file with name "async-firebase.json".

Run the following command to grant the default login to Google Cloud client libraries:

```plain text
gcloud auth application-default login

```

To start the server,

```plain text
uvicorn src.server:app --reload --port 8000

```

To lint, run the following command:

```plain text
uv run ruff format .
uv run ruff check . --fix

```

## Testing

To run all unit tests:

```plain text
python -m pytest

```

## API Documentation

The FastAPI server provides the following main endpoints:

### Authentication

- POST /auth/auth-with-github - Complete GitHub OAuth flow with access code
- POST /auth/verify-email - Send email verification code
- POST /auth/redeem-email-code - Validate email verification code
- POST /auth/invite-people - Send team invitations
- POST /auth/redeem-invite-code - Validate invitation codes
### GitHub Integration

- POST /github/handle-github-events - Process GitHub webhook events (issues, PRs, push)
- POST /github/submit-review - Submit code review with approve/request changes
### Task Management

- POST /task/schedule-job - Schedule task execution jobs (research, execute, revise, index)
- WebSocket /task/chat - Real-time task communication with AI agents
### Onboarding

- POST /onboarding/onboard-github - Complete GitHub App installation and repository setup
### Payment

- POST /payment/create-checkout-session - Create Stripe checkout for subscriptions
- POST /payment/create-portal-session - Access customer billing portal
- POST /payment/handle-stripe-events - Process Stripe webhook events
### Support

- POST /support/handle-contact-us - Submit contact form and create lead
## Google Cloud Run Jobs

The system uses isolated Google Cloud Run jobs for task processing:

### Job Types

-  
-  
-  
-  
Each job runs in an isolated environment with the repository cloned and all necessary dependencies installed.

## Deployment

### Prerequisites

- Google Cloud Platform account with Cloud Run enabled
- Firebase project with Firestore
- GitHub App configured for your organization
- Stripe account for payment processing
### Environment Variables

Configure the following in your production environment:

- ANTHROPIC_API_KEY - Claude API access
- OPENAI_API_KEY - OpenAI API access
- GOOGLE_API_KEY - Google AI API access
- STRIPE_SECRET_KEY - Stripe payment processing
- GITHUB_WEBHOOK_SECRET - GitHub webhook validation
- DB_URI - Database connection string
### Cloud Deployment

The application is designed to run on Google Cloud Run with automatic scaling and isolated task execution.

## Contributing

1. Fork the repository
1. Create a feature branch (git checkout -b feature/amazing-feature)
1. Make your changes
1. Run tests and linting
1. Commit your changes (git commit -m 'Add amazing feature')
1. Push to the branch (git push origin feature/amazing-feature)
1. Open a Pull Request
Please ensure your code follows the existing style and passes all tests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For questions or issues, please open a GitHub issue or contact the team.

Built for experienced developers who know their codebases deeply. Async is the last tool you'll need to build something great.


