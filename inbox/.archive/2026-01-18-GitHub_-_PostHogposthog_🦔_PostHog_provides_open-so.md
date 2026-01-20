---
type: link
source: notion
url: https://github.com/PostHog/posthog
notion_type: Software Repo
tags: ['Running']
created: 2024-06-03T17:20:00.000Z
---

# GitHub - PostHog/posthog: 🦔 PostHog provides open-source product analytics, session recording, feature flagging and A/B testing that you can self-host.

## AI Summary (from Notion)
- Overview of PostHog: An open-source platform for product analytics, session recording, feature flagging, and A/B testing that can be self-hosted.
- Key Features:
- Event-based analytics with autocapture.
- Session replays and user behavior monitoring.
- A/B testing and feature flag management.
- Customizable surveys for user feedback.
- SQL access for detailed data analysis.
- Free Tier: Offers a generous free tier including 1 million product analytics events and 5,000 session replays monthly.
- Deployment Options:
- Cloud-based (recommended for ease of use).
- Open-source hobby deployment for advanced users.
- Data Privacy Focus: Emphasizes user data control, avoiding third-party analytics tools that compromise privacy.
- Community and Contribution: Open for contributions and encourages users to engage in the development process.
- Job Opportunities: Actively hiring to expand their team.
- License: Available under the MIT license, with a pure open-source version available.
- Continuous Development: Regularly adding new features and functionalities, with web analytics and data warehousing in beta.

## Content (from Notion)

Docs - Community - Roadmap - Changelog - Bug reports

See PostHog in action

## PostHog is an all-in-one, open source platform for building better products

- Specify events manually, or use autocapture to get started quickly
- Analyze data with ready-made visualizations, or do it yourself with SQL
- Gather insights by capturing session replays, console logs, and network monitoring
- Improve your product with A/B testing that automatically analyzes performance
- Safely roll out features to select users or cohorts with feature flags
- Send out fully customizable surveys to specific cohorts of users
- Connect to external services and manage data flows with PostHog CDP
PostHog is available with hosting in the EU or US and is fully SOC 2 compliant. It's free to get started and comes with a generous monthly free tier:

- 1 million product analytics events
- 5k session replays
- 1 million feature flag requests
- 250 survey responses
We're constantly adding new features, with web analytics and data warehouse now in beta!

## Table of Contents

- Get started for free
- Docs
- Contributing
- Philosophy
- Open-source vs paid
## Get started for free

### PostHog Cloud (Recommended)

The fastest and most reliable way to get started with PostHog is signing up for free to PostHog Cloud or PostHog Cloud EU. Your first 1 million events (and 5k replays) are free every month, after which you pay based on usage.

### Open-source hobby deploy (Advanced)

You can deploy a hobby instance in one line on Linux with Docker (recommended 4GB memory):

```plain text
 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/posthog/posthog/HEAD/bin/deploy-hobby)"
```

Open source deployments should scale to approximately 100k events per month, after which we recommend migrating to a PostHog Cloud instance. See our docs for more info and limitations. Please note that we do not provide customer support for open source deployments.

## Docs

Want to find out more? Request a demo!

PostHog brings all the tools and data you need to build better products.

### Analytics and optimization tools

- Event-based analytics: Capture your product's usage automatically, or customize it to your needs
- User and group tracking: Understand the people and groups behind the events and track properties about them
- Data visualizations: Create and share graphs, funnels, paths, retention, and dashboards
- SQL access: Use SQL to get a deeper understanding of your users, breakdown information and create completely tailored visualizations
- Session replays: Watch videos of your users' behavior, with fine-grained filters and privacy controls, as well as network monitoring and captured console logs
- Heatmaps: See where users click and get a visual representation of their behaviour with the PostHog Toolbar
- Feature flags: Test and manage the rollout of new features to specific users and groups, or deploy flags as kill-switches
- A/B and multivariate experimentation: run simple or complex changes as experiments and get automatic significance calculations
- Correlation analysis: Discover what events and properties correlate with success and failure
- Surveys: Collect qualitative feedback from your users using fully customizable surveys
### Data and infrastructure tools

- Import and export your data: Import from and export to the services that matter to you with the PostHog CDP
- Ready-made libraries: We’ve built libraries for JavaScript, Python, Ruby, Node, Go, Android, iOS, PHP, Flutter, React Native, Elixir, Nim, and an API for anything else
- Plays nicely with data warehouses: import events or user data from your warehouse by writing a simple transformation plugin, and export data with pre-built apps - such as BigQuery, Redshift, Snowflake, and S3
Read a full list of PostHog features.

## Contributing

We <3 contributions big and small. In priority order (although everything is appreciated) with the most helpful first:

- Vote on features or get early access to beta functionality in our roadmap
- Open a PR (see our instructions on developing PostHog locally)
- Submit a feature request or bug report
## Philosophy

Our mission is to increase the number of successful products in the world. To do that, we build product and data tools that help you understand user behavior without losing control of your data.

In our view, third-party analytics tools do not work in a world of cookie deprecation, GDPR, HIPAA, CCPA, and many other four-letter acronyms. PostHog is the alternative to sending all of your customers' personal information and usage data to third-parties.

PostHog gives you every tool you need to understand user behavior, develop and test improvements, and release changes to make your product more successful.

PostHog operates in public as much as possible. We detail how we work and our learning on building and running a fast-growing, product-focused startup in our handbook.

## Open-source vs. paid

This repo is available under the MIT expat license, except for the ee directory (which has it's license here) if applicable.

Need absolutely 💯% FOSS? Check out our posthog-foss repository, which is purged of all proprietary code and features.

To learn more, book a demo or see our pricing page.

### We’re hiring!

Come help us make PostHog even better. We're growing fast and would love for you to join us.

## Contributors 🦸


