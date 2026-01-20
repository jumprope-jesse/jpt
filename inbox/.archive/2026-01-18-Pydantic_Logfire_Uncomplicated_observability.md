---
type: link
source: notion
url: https://pydantic.dev/logfire
notion_type: Software Repo
tags: ['Running']
created: 2024-05-01T00:31:00.000Z
---

# Pydantic Logfire | Uncomplicated observability

## AI Summary (from Notion)
- Overview: Pydantic Logfire is an observability platform designed to simplify the monitoring of applications, particularly for Python developers.
- Core Belief: The platform is built on the belief that powerful tools can be user-friendly.
- Headaches Addressed:
- Complicated observability tools that don't align with code.
- Confusing logs and print statements.
- Uncertainty regarding performance issues in applications.
- Key Features:
- Intuitive setup with integrations for popular libraries.
- Performance insights to identify slow queries and function runtimes.
- Comprehensive visibility into application behavior, including request details and execution traces.
- Data-driven insights through visualizations and dashboards.
- SDK and OpenTelemetry:
- Built on OpenTelemetry for structured data and easy logging.
- Allows for direct SQL access to query structured data seamlessly.
- Developer Focus: Designed with developer experience in mind, making observability accessible for both novices and experts.
- Integration: Out-of-the-box integration with Pydantic for a tailored observability experience.
- Open Source: The SDK is open source under the MIT license, promoting community collaboration.
- Links for Access: Documentation, GitHub, and Slack support available for users.

## Content (from Notion)

From the team behind Pydantic, Logfire is a new type of observability platform built on the same belief as our open source library — that the most powerful tools can be easy to use.

Visit docs

Software developer? Then you’ve likely encountered these headaches

Working with over-complicated observability platforms that don't understand your code or application.

Sifting through endless print statements and decoding cryptic portrayals of Python objects in your logs.

Guessing at the performance hit from a specific function, or a mysterious slowdown of your app.

Whether you’re building an AI tool or any other cloud-based app, these frustrating scenarios are avoidable but all too real.

INTRODUCING LOGFIRE

## A more intuitive way to understand your

Pydantic Logfire is a window into the inner workings of your application. Smooth to set up and easy to understand, with ready integrations for many popular libraries.

view full example

Features

Python and beyond

While Pydantic Logfire is Python-first, it’s an observability platform that works just as well with other programming languages.

Performance insights

Transform garbled logs into actionable insights. Discover not just how long a function takes to run, but which queries slow down your app.

Comprehensive visibility

Understand your app’s behaviour — from request headers and bodies to the full trace of program execution.

Data-driven decisions

Turn your logs into visualizations, dashboards, and alerts that drive development forward.

Insights

### Faster fixes, deeper insights

With an SDK built on top of OpenTelemetry, structured data and an intuitive interface, Pydantic Logfire makes it easy to monitor the behavior of Python applications, at every level. Instrument your app using best practices and draw powerful insights — without hiring a dedicated analytics or observability team.

## Structured Data & Direct SQL Access

Ensure your Python objects and structured data are query-ready. Use tools like Pandas, SQLAlchemy, or psql for querying, integrate seamlessly with BI software, and leverage AI for SQL generation.

```plain text
SELECT
  attributes->>'campaign' as campaign,
  count(distinct attributes->>'track_id') as clicks,
  round(count(distinct attributes->>'track_id')::numeric/50*100, 2) as click_rate
FROM records
WHERE
  message ilike 'click%' and
  attributes->>'campaign' ilike 'c%'
GROUP BY attributes->>'campaign'
```

## Manual Tracing

You can use the logfire library to create logs and traces directly — it’s kind of like standard logging in Python, with a more modern interface and some extra capabilities. And a lot less painful than using OpenTelemetry directly.

```plain text
import logfire

logfire.info('Hello, {name}!', name='world')

advantages = 'timing', 'context', 'exception capturing'
with logfire.span('spans provide: {advantages}', advantages=advantages):
     logfire.warn('the next line will raise an exception')
     1 / 0
```

## OpenTelemetry

OpenTelemetry (OTel) is an open source observability framework, it provides libraries for Python and every other popular language to let you collect traces, logs and metrics.

OTel is a powerful tool that increasing numbers of developers want to use, but it can be time-consuming to set up and limited in the kinds of data it can collect.

Pydantic Logfire takes the best of OTel (instrumentation for popular Python packages, open standard for data transmission) and makes it easier to use and more flexible.

By harnessing OpenTelemetry, Pydantic Logfire offers automatic instrumentation for popular Python packages, enables cross-language data integration, and supports data export to any OpenTelemetry-compatible backend or proxy.

## Logfire is already making developers' lives easier

## From the creators of Pydantic, Crafted with the same developer obsession

Built with developer experience at its core, Pydantic Logfire brings the same balance of ease, sophistication and productivity that’s made Pydantic the most popular data validation library on planet earth. Whether you’re using observability for the first time or an expert, we make it easy.

Out-of-the-box integration

Use Pydantic Logfire to monitor the data that runs through Pydantic for a customized experience that goes way beyond generic observability platforms.

FOR DEVELOPERS

Ready to start building?

Logfire’s Python SDK is open source under the MIT license and wraps the OpenTelemetry Python package. By default, it will send data to the Logfire platform but you could send data to any OpenTelemetry Protocol (OTLP) compliant endpoint.

DocsDocs

GitHubGitHub

SlackSlack

### A window into your application


