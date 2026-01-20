---
type: link
source: notion
url: https://github.com/buttondown/django-typescript-routes
notion_type: Software Repo
tags: ['Running']
created: 2024-04-13T19:55:00.000Z
---

# GitHub - buttondown/django-typescript-routes: Generate Typescript routes from a Django URLconf

## AI Summary (from Notion)
- Project Overview: django-typescript-routes is a tool designed to generate TypeScript routes from Django URL configurations, serving as a successor to django-js-reverse.

- Functionality: It converts Django URL patterns into a manageable TypeScript object that can be used for routing in front-end applications.

- Installation:
- The tool can be added to a project using Poetry with the command: poetry add --dev django-typescript-routes.
- It must be included in the INSTALLED_APPS of the Django settings.

- Usage: A management command allows users to generate a TypeScript file that contains the routes, making integration into front-end code seamless.

- Quick Start Steps:
1. Install the package.
2. Update Django settings.
3. Run the management command to generate the TypeScript routes.

- Key Takeaway: This tool enhances the efficiency of managing routes between Django back-end and TypeScript front-end, facilitating better integration and reducing the likelihood of errors in route handling.

## Content (from Notion)

# django-typescript-routes

Meant as a spiritual successor to django-js-reverse, django-typescript-routes is meant to answer to the following question:

> 

django-typescript-routes is how! At a high level, it turns:

```plain text
urls = [
    path(
        r"about",
        about,
        name="about",
    ),
    path(
        r"/<str:username>",
        subscribe,
        name="subscribe",
    ),
    path(
        r"/<str:username>/subscribers/<pk:uuid>/success",
        subscription_success,
        name="subscription-success",
    ),
]
```

into:

```plain text
const URLS = {
  about: () => `/`,
  subscribe: (username: string) => `/${username}`,
  "subscription-success": (username: string, pk: string) =>
    `/${username}/subscribers/${pk}/success`,
};
```

## Quick start

1. Install:
```plain text
poetry add --dev django-typescript-routes
```

1. Add django-typescript-routes to your INSTALLED_APPS setting:
```plain text
INSTALLED_APPS = [
    ...,
    "typescript_routes",
    ...
]
```

1. Run the management command to print out the typescript file:
```plain text
python manage.py generate_typescript_routes --urlconf projectname.urls > assets/urls.ts
```


