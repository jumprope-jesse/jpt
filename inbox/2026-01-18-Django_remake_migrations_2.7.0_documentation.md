---
type: link
source: notion
url: https://django-remake-migrations.readthedocs.io/en/latest/index.html?featured_on=pythonbytes
notion_type: Software Repo
tags: ['Running']
created: 2025-08-21T04:09:00.000Z
---

# Django remake migrations 2.7.0 documentation

## Overview (from Notion)
- Streamlining migration processes can save you time and reduce headaches, allowing you to focus on family and business growth.
- The concept of replacing multiple old migrations with new ones can be likened to simplifying life’s complexities—finding more efficient ways to manage both work and family obligations.
- This method encourages a proactive approach to software engineering, which may inspire you to tackle challenges with your startup more creatively.
- The trade-off in accuracy for efficiency reflects the balance often necessary in entrepreneurship—sometimes speed is crucial, even if it means accepting some imperfections.
- Alternate views might suggest sticking with traditional methods for accuracy, but in a fast-paced city like NYC, innovation often requires embracing calculated risks.

## AI Summary (from Notion)
The squashmigrations command in Django is limited to a single app, making it difficult for projects with cross-app dependencies. A new command aims to recreate all migration files for the entire project and mark them as applied, with the trade-off that it does not ensure correctness in setting the replaces attribute. It guarantees that old migrations are marked as replaced once and that new migrations replace at least one old migration, provided all environments are fully migrated upon deployment.

## Content (from Notion)

## The problem

The built-in squashmigrations command is great, but it only work on a single app at a time, which means that you need to run it for each app in your project. On a project with enough cross-apps dependencies, it can be tricky to run.

This command aims at solving this problem, by recreating all the migration files in the whole project, from scratch, and mark them as applied by using the replaces attribute.

It makes an important trade-off though: it does NOT try to be correct when setting the replaces attribute. The only guarantees are that:

- all old migrations are marked as replaced once.
- all new migrations replace at least one of the old migrations
This is OK to make this trade-off as long as all your environments are fully migrated when you deploy the remade migrations.

## Contributors ✨

Thanks goes to these wonderful people (emoji key):

This project follows the all-contributors specification. Contributions of any kind welcome!


