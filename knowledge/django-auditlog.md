# django-auditlog

Django app for logging changes made to model objects.

## Overview

- **Repo**: https://github.com/jazzband/django-auditlog
- **Docs**: https://django-auditlog.readthedocs.org
- **License**: MIT

## Key Features

- Logs model changes along with the user (actor) who made them
- Stores change summaries in JSON format for easy tracking
- More flexible than Django's built-in admin logging (`django.contrib.admin`)
- Designed for simplicity and performance (minimal dependencies)
- Uses Python/Django built-ins as much as possible

## When to Use

- Need audit trails for compliance or debugging
- Want to track who changed what and when
- Django admin's built-in logging is too limited
- Don't need full version control (like django-reversion) - just change logs

## vs Django Admin Logging

Django admin logs are limited to admin actions. Auditlog works for any model changes regardless of where they originate (API, management commands, etc.).

## Migration Note

Check the "Upgrading to version 3" doc before upgrading from v2 to v3.
