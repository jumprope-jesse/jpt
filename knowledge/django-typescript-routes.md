# django-typescript-routes

Library that generates TypeScript route helpers from Django URL configurations. Spiritual successor to django-js-reverse.

**Repo**: https://github.com/buttondown/django-typescript-routes

## What It Does

Converts Django URL patterns into typed TypeScript functions:

```python
# Django urls.py
urls = [
    path(r"about", about, name="about"),
    path(r"/<str:username>", subscribe, name="subscribe"),
    path(r"/<str:username>/subscribers/<pk:uuid>/success", subscription_success, name="subscription-success"),
]
```

Generates:

```typescript
const URLS = {
  about: () => `/`,
  subscribe: (username: string) => `/${username}`,
  "subscription-success": (username: string, pk: string) =>
    `/${username}/subscribers/${pk}/success`,
};
```

## Installation

```bash
poetry add --dev django-typescript-routes
```

Add to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...,
    "typescript_routes",
]
```

## Usage

Generate the TypeScript file:

```bash
python manage.py generate_typescript_routes --urlconf projectname.urls > assets/urls.ts
```

## Why Use It

- Type-safe URL building in frontend code
- Single source of truth for routes (Django defines them)
- Catches route mismatches at compile time instead of runtime
- Replaces string interpolation with typed function calls
