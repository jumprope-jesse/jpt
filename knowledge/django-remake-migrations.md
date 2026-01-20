# django-remake-migrations

Tool for recreating all migration files across an entire Django project.

## The Problem It Solves

Django's built-in `squashmigrations` only works on a single app at a time. For projects with cross-app dependencies, this becomes difficult to manage.

## How It Works

- Recreates all migration files from scratch for the entire project
- Marks old migrations as applied using the `replaces` attribute
- Guarantees:
  - All old migrations are marked as replaced once
  - All new migrations replace at least one old migration

## Important Trade-off

The tool does NOT guarantee correctness in setting the `replaces` attribute. This is acceptable **only if all environments are fully migrated** when you deploy the remade migrations.

## Links

- Docs: https://django-remake-migrations.readthedocs.io/
- Install: `pip install django-remake-migrations`

## When to Use

- Large projects with many apps and cross-app migration dependencies
- Migration history has become unwieldy
- All environments are in sync (fully migrated)
