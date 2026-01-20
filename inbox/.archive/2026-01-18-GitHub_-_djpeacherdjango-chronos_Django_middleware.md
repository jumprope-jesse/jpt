---
type: link
source: notion
url: https://github.com/djpeacher/django-chronos
notion_type: Software Repo
tags: ['Running']
created: 2025-08-21T04:10:00.000Z
---

# GitHub - djpeacher/django-chronos: Django middleware that shows you how fast your pages load, right in your browser.

## Overview (from Notion)
- Performance Awareness: Understanding page load times can help optimize your software products, ensuring a better user experience for customers and reducing churn.
- Family Engagement: As a father, you might be interested in how technology can enhance family activities—faster websites mean more time for family bonding rather than waiting for pages to load.
- Local Impact: Being in NYC, you have access to a vibrant tech community—use tools like django-chronos to connect with local developers and lead discussions on performance optimization.
- Work-Life Balance: Streamlining your software can lead to less frustration at work and more time at home, making both your professional and personal life more satisfying.
- Innovation and Contribution: Consider contributing to open-source projects, such as django-chronos, which can enhance your skills and network while leaving a mark on the developer community.
- Alternative Perspectives: Some may argue that focusing too much on performance can detract from innovative design—finding a balance between aesthetics and speed could be an interesting challenge.

## AI Summary (from Notion)
Django Chronos is a middleware that displays page load times and query counts in the browser. Installation requires adding it to INSTALLED_APPS and configuring middleware in Django settings. It includes options to show stats in production, control how stats are inserted into responses, and customize the stats display. The project is open source under the MIT License, and contributions are welcome.

## Content (from Notion)

# django-chronos

Django middleware that shows you how fast your pages load, right in your browser. Displays request timing and query counts for your views and middleware.

## Installation

Install Django Chronos using pip:

```plain text
pip install django-chronos
```

## Quick Start

1. Add to INSTALLED_APPS in your Django settings:
```plain text
INSTALLED_APPS = [
    # ... your other apps
    'django_chronos',
]
```

1. Add middleware to your Django settings (order matters):
```plain text
MIDDLEWARE = [
    'django_chronos.middleware.ChronosStartMiddleware',  # Must be first
    # ... your other middleware
    'django_chronos.middleware.ChronosEndMiddleware',    # Must be last
]
```

1. Run your Django application and visit any page. You'll see a stats overlayed in the bottom-left corner.
## Configuration

### CHRONOS_SHOW_IN_PRODUCTION (default: False)

Controls whether stats are shown in production mode (DEBUG=False). Stats are only shown to superusers in production. Stats always show in DEBUG mode.

```plain text
CHRONOS_SHOW_IN_PRODUCTION = True
```

### CHRONOS_SWAP_METHOD (default: 'prepend')

Controls how the stats are inserted into the response:

- 'prepend': Insert stats before the target
- 'append': Insert stats after the target
- 'replace': Replace the target with stats
```plain text
CHRONOS_SWAP_METHOD = 'append'
```

### CHRONOS_SWAP_TARGET (default: '</body>')

The string in the response where stats will be swapped in. Stats will not be displayed if this string does not exist in the response.

```plain text
CHRONOS_SWAP_TARGET = '</body>'
```

### Customizing the Stats Display

You can override the default stats display by creating your own chronos/chronos.html template in your Django project.

The template receives the following context variables:

- middleware_cpu_time, middleware_sql_time, middleware_sql_count, middleware_total_time
- view_cpu_time, view_sql_time, view_sql_count, view_total_time
- total_cpu_time, total_sql_time, total_sql_count, total_time
Note: In production mode, the *_sql_time and *_sql_count variable values will be zero (why?). You can wrap these variables in {% if debug %} blocks to stop them from displaying in production.

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Appreciation

Adam Hill for the inspiration via his Mastodon thread.


