---
type: link
source: notion
url: https://blog.bmispelon.rocks/articles/2024/2024-04-06-sentry-initialization-in-a-django-project.html?utm_campaign=Django%2BNewsletter&utm_medium=rss&utm_source=Django_Newsletter_227
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-04-13T19:53:00.000Z
---

# Sentry initialization in a Django project | Baptiste Mispelon

## AI Summary (from Notion)
- Introduction to Sentry in Django: The author discusses the use of Sentry for monitoring errors in production at their workplace.
- Initial Setup: Sentry was integrated following official documentation, leading to effective error reporting.
- Unexpected Errors: Reports of SyntaxError and SystemExit exceptions were generated when using the Django shell, causing annoyance.
- Exploring Entry Points: The author considered alternative entry points for Sentry initialization to avoid reporting errors from the shell, including wsgi.py and manage.py.
- Challenges of Entry Points: No single entry point could effectively exclude shell usage while still supporting web workers, management commands, and Celery tasks.
- Conditional Initialization: The author implemented a solution to conditionally initialize Sentry in settings.py based on the command being run (excluding shell).
- Ongoing Adjustments: While the conditional check improved the situation, the author acknowledges the need for ongoing adjustments to account for other commands like shell_plus.
- Conclusion: The author settled on the second approach as a suitable, albeit imperfect, solution and invites others to share their experiences or solutions.

## Content (from Notion)

At $DAYJOB we use Sentry to monitor errors in production. It works really well but our particular setup caused an annoyance that was surprisingly tricky to fix.

## The annoyance

Following Sentry's official documentation, we added the following code to our settings file:

```plain text
import sentry_sdk
sentry_sdk.init(...)  # credentials etc
```

This works perfectly fine, and once that snippet was in place error reports started showing up in the Sentry interface as they happened in production. So far so good.

But after some time we started getting reports for some strange errors. Every once in a while, Sentry would start reporting exceptions like SyntaxError or SystemExit. What was going on?

The answer was quite logical once I understood it, but it did take me by suprise. By putting the sentry_sdk.init(...) in our settings, it means that Sentry error reporting is active any time the project is loaded. That's a good thing overall as it means you catch a lot of potential problems, but there was once situation for us where that behavior was undesirable: the shell.

These errors I was observing were the result of one of my coworkers starting a shell (./manage.py shell) on the server. If they made a typo, Python would throw a SyntaxError exception which would be diligently caught and reported by Sentry. The same thing also happened when they exited the shell, as Python then throws a SystemExit exception.

At first it was pretty fun being able to tease my coworker about their typos, but it got annoying quite fast and I started looking into how to exclude the shell from Sentry's error reporting.

## Attempt 1: a better entry point?

My first idea was to find a better place than settings.py where I could call sentry_sdk.init(). I figured there must be a file that gets loaded when running the website, but not when running a shell.

After thinking about it for a while, I came up with 3 files that could be good candidates:

settings.py Our current solution (and the one recommended by the official docs). wsgi.py  Created automatically by Django, this is the file that your webserver (gunicorn, uwsgi, ...) will load.  manage.py  This file is created automatically by Django when you start a project, and it's very rarely modified but it can be a nifty entry point. 

At first glance, wsgi.py seemed like a good entry point for what I wanted, but I quickly realized that it had a major drawback which ended up being a dealbreaker for me: Celery workers.

As it turns out, there's more usecases to take into account than just web workers and management commands:

Web workers  The main usecase for most Django projects I would guess (Django is a webframework after all).  Management commands  Your classic ./manage.py COMMAND (collectstatic, createsuperuser, migrate, ...). Either called manually, or scheduled with something like CRON.  Celery workers Or any kind of asynchronous task system. Most projects will have one when they reach a certain size. Random python scripts  Probably not a good practice in general, but for some one-off tasks it's hard to beat the convenience of running a plain python script. 

3 entry points, 4 different uses cases. If my math is right, that's 12 different scenarios to consider (✅ means the file is loaded, ❌ means it isn't):

- * Unless you use something like django-webserver or django-prodserver.
- ** But only if you use ./manage.py COMMAND and not python -m django COMMAND.
- *** If you call django.setup() in your script, which you probably want to do anyway.
As we can see from the table above, there's not really a better entry point that would trigger with web and celery workers, but not with management commands or scripts. So we're back at square one 😩.

## Attempt 2: detecting if we're running in a shell 🐌

My second idea was to keep the initialization code in settings.py, but only execute it if we were not running in a shell. So how do you check which management command you're running? As is often the case, when I have a weird Django question there's a blog article by Adam Johnson that has exactly the answer I want. This time was no different: How to Check the Running Django Command.

So followings Adam's advice, here's what we end up with:

```plain text
import sys
import sentry_sdk
...
if sys.argv[1:2] != ["shell"]:
    sentry_sdk.init(...)
```

Now we're getting somewhere!

We haven't reached perfection yet though. One issue for example is that some of my colleagues like to use the shell_plus command from django-extensions instead of the plain shell. That means the if needs to be tweaked a bit. And what about other commands? I'm sure that as time goes by I will figure out that more commands need to be excluded and it could get annoying having to maintain a blocklist/allowlist.

## Attempt 3?

To be honest I ended up sticking with option 2. It's not perfect, but the limitations seemed acceptable to me and it was a net improvement compared to what we had before.

If you've run into this issue and found a solution that worked for you please let me know (you can find ways to contact me on my "about" page).


