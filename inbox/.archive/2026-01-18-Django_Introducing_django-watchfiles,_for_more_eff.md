---
type: link
source: notion
url: https://adamj.eu/tech/2025/09/22/introducing-django-watchfiles/?utm_campaign=Django%2BNewsletter&utm_medium=rss&utm_source=Django_Newsletter_304
notion_type: Tech Deep Dive
tags: ['Running']
created: 2025-10-02T12:08:00.000Z
---

# Django: Introducing django-watchfiles, for more efficient runserver autoreloading - Adam Johnson

## Overview (from Notion)
- The introduction of django-watchfiles can significantly enhance your development efficiency, allowing you to focus more on coding and less on waiting for server restarts.
- This tool aligns with a busy lifestyle, enabling quicker iterations, which is essential for balancing work with family time.
- Living in a fast-paced environment like New York City, adopting tools that optimize workflows can lead to more productive days, giving you more free time to spend with your kids.
- The move towards more eco-efficient programming (like reduced CPU usage) reflects a broader trend in tech toward sustainability, which could resonate with your values as someone raising a family.
- Unique viewpoint: Embracing new technology like django-watchfiles could inspire your kids to explore coding, showing them the practical benefits of programming in everyday life.
- Alternate view: While the shift to new tools can be beneficial, consider the time investment in learning and integrating them into existing projects—balance is key to avoid overwhelming yourself.

## AI Summary (from Notion)
Django's runserver now integrates with django-watchfiles, a cross-platform file-watching library, to improve autoreloading efficiency by using OS-specific file watching APIs instead of constant polling. This change significantly reduces CPU usage, enhancing performance during development. To implement, users need to install the package and add it to their Django settings, which will allow for faster and more reliable reloads.

## Content (from Notion)

Watch out! It’s another development experience boosting tool!

Django’s runserver automatically reloads when you change Python files. Without this autoreloading feature, you’d need to manually restart the server every time you made a code change.

However, the default autoreloading implementation is inefficient, as it constantly polls the filesystem for changes. The alternative to polling is to use your operating system’s file watching APIs, which can efficiently notify the server when files change. Using this technique saves CPU and power, while making reloads faster and more reliable—all in all, a big win! But since these APIs are OS-specific, it’s best for Django to use a cross-platform library that wraps them.

Django provides an integration with Facebook’s Watchman, which works as a file watching server. While I appreciate this integration, it does require installing, running, and maintaining an extra tool (Watchman itself). Additionally, the Python client library for Watchman, pywatchman, seems to be rather unmaintained. Most notably, it was broken on Python 3.10, and the fix was not released for 2.5 years, after Python 3.12 was released.

I promoted the Watchman integration on this blog and in the first version of Boost Your Django DX, which came out just after Python 3.10 was released. But since pywatchman was broken, my book offered advice that quickly became unusable, so I was open to finding alternatives. (I later removed that section, after it was clear that pywatchman wasn’t getting fixed any time soon.)

Thankfully, watchfiles was released around that time, a cross-platform file-watching library for Python. It’s powered by Rust and the widely used Notify crate, and created by Samuel Colvin, the author of Pydantic.

I started django-watchfiles in 2022, to integrate Django’s autoreloader with watchfiles. In 2023, Tom Forbes (the author of Django’s Watchman integration) helped me improve it beyond alpha quality, and I released the first stable version in 2024. However, it’s only today, after a final sprint on some remaining issues and release 1.4.0, that I feel confident to announce and promote the package for wide use.

## Try it out

To use django-watchfiles in your project:

1. Install the package. 
1. Install its app. 
django-watchfiles patches Django’s autoreloader to always use the included watchfiles class. You’ll be able to tell this patch is working because runserver will report it’s using WatchfilesReloader at startup, as opposed to StatReloader:

```plain text
$ ./manage.py runserver
Watching for file changes with WatchfilesReloader
...

```

Then, you should be able to enjoy faster and more efficient reloading!

A quick benchmark on a medium-sized project (385,000 lines plus 206 installed packages) using an M1 MacBook shows Django’s default reloader using ~10% of a CPU every other second, while django-watchfiles uses 0%. That can translate into a lot of saved battery life when developing on an unplugged laptop.

## Fin

Please try out django-watchfiles today, and let me know what you think! The README contains more details about its benefits, as well as a full history of Django’s autoreloader.

When django-watchfiles is more established and proven, I may propose adding a watchfiles integration to Django core.

Watch this space,

—Adam

Learn how to make your tests run quickly in my book Speed Up Your Django Tests.

One summary email a week, no spam, I pinky promise.

Related posts:


