---
type: link
source: notion
url: https://medium.com/ambient-innovation/going-atomic-with-django-querysets-53f746418871
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-05-11T21:52:00.000Z
---

# Going atomic with Django QuerySets | by Ronny Vedrilla | ambient-digital | Apr, 2024 | Medium

## AI Summary (from Notion)
- Title: Going Atomic with Django QuerySets
- Author: Ronny Vedrilla
- Published: April 17, 2024, in ambient-digital
- Main Concept: Advocates for a clear pattern when using Django's ORM, specifically the separation of concerns by using distinct queryset methods for each database operation.

- Key Takeaways:
- Each database operation should correspond to exactly one queryset method, creating a clear internal API for models.
- This method improves simplicity, readability, and maintainability of code.
- Using custom queryset methods leads to better testability and less clutter in views.

- Advantages of CQS (Command Query Separation):
- Simplifies code by abstracting low-level ORM details.
- Enhances separation of concerns by keeping ORM logic within the model layer.
- Allows for easier unit testing of queryset methods.

- Critical Review:
- While initially more time-consuming to set up, using CQS will save time in the long run by reducing bugs and improving code quality.

- Final Note: Invites readers to share thoughts and experiences regarding structuring code and business logic in Django.

## Content (from Notion)

# Going atomic with Django QuerySets

## A straightforward pattern for greater simplicity and consistency

Ronny Vedrilla

·

Follow

Published in

ambient-digital

·

4 min read

·

Apr 17, 2024

- -
# TL;DR

Each database operation in your ORM should be reflected by exactly one queryset method. Filter for the user ID? One method. Excluding a number of project statuses? One method. As a result you’ll define an internal API for your models that’s easy to understand and easy to use.

Photo by Shavonne Yu on Unsplash

# Motivation

Still lingering in the top three most popular web frameworks in most online rankings, many people would obviously agree that working with Django is great. A solid architecture, maturity and great documentation all contribute to the continued success of this particular Python framework.

However, there are still many things out there that are not covered in the documentation. Where to put your custom business logic is one of them. How to structure your database communication another.

In theory, you can use the ORM from any part of your application: views, model properties, querysets and managers and custom parts of your codebase. In practice, this is exactly what you’ll see when you look at most Django projects.

Keeping the pattern “separation of concerns” in mind, having your database “layer” spread across the different parts of your system doesn’t sound like a great idea. So what can we do about it?

# Finding a suitable home

Before we can start reorganising our code, we need to find a place to put all our ORM stuff. Referring to the docs, managers seem like a good place to start. But managers are not just another class to put code in, they also allow you to customise the model’s QuerySet. So we need to be a little bit more precise than “ORM stuff goes into the manager”. Nevertheless, we seem to be in the right place, Django-wise.

# Separating managers and querysets

To be able to properly separate manager methods and (custom) queryset methods — CQS for short in the following paragraphs — we need a plan.

A simple and straightforward approach might be the as follows:

- A CQS method returns a QuerySet
- A CQS method will never modify any data (read-only)
If you either don’t return a QuerySet or write data, it belongs in a manager method.

The people at HackSoft have gone one step further and introduced the selector pattern for read-only access to data. While this sounds reasonable, we will focus on CQS here — but feel free to read about it.

# Custom queryset methods

As a result, manager methods can and will look quite heterogeneous. Some will objects, some will modify them and some will fetch data in a custom data structure.

A CQS method is much more restrictive due to our rules from the previous paragraph. Now you could think of your CQS not just as a place to conveniently put your ORM code but as a descriptive API for your database. If every read operation in your application is done through the CQS, you’ll end up with a comprehensive list of things you do (read) with your data.

In practice, you’ll end up doing a lot of rewriting of filters, fields and annotates. You’ll have many cases where you only want to query active users, or you want to avoid fetching archived projects. As the Zen of Python says, “explicit is better than implicit”, imagine how much more descriptive your CQS could be if you created a single method for each operation you’re doing.

```plain text
def filter_by_user(self, user_id: int) -> "MyModelQuerySet"
    """
    Fetches all instances of "MyModel" which belong to the given user
    """
    return self.filter(user_id=user_id)
```

This works well for “and” operations, as they are chainable easily. For “or” you can’t be so atomic. But as long as you’re consistent, it’s perfectly fine.

```plain text
def filter_active_users(self) -> "UserQuerySet"
    """
    Fetches all users which are currently active
    """
    return self.filter(Q(is_active=True) | Q(end_date__lte=timezone.now().date())
```

This means that in your view, viewset or any custom business logic, you’ll be trading this:

```plain text
from django.db.models import Count, F, Value, Q
from django.db.models.functions import Concat
...

class BlogListView(generic.ListView):
    model = BlogPost
    ...

    def get_queryset(self, queryset):
        return (
            BlogPost.objects
            .filter(user_id=self.request.user.id)
            .filter(category=self.request.GET["category"])
            .exclude(Q(publish_date__gt=timezone.now() | Q(reviewed=False))
            .annotate(qty_pictures=Count("pictures"))
            .annotate(author_name=Concat(F("user.first_name", Value(" "), F("user.last_name")))))
        )
```

for this:

```plain text
class BlogListView(generic.ListView):
    model = BlogPost
    ...

    def get_queryset(self, queryset):
        return (
            BlogPost.objects
            .filter_by_id(user_id=self.request.user.id)
            .filter_by_category(category=self.request.GET["category"])
            .only_active()
            .annotate_pictures()
            .annotate_author_name()
        )
```

The main advantages are:

- Simplicity. You don’t see — and don’t care about — the low-level details, so the code is easier to understand.
- Separation of concerns. Just have a look at how many ORM imports we avoid in our views.py. Put ORM stuff where ORM stuff belongs and keep other layers (mostly) free of it.
- Testability. You can test each part of your query separately with unit tests. This makes tests smaller, simpler and more accurate. Just do a quick integration test on the view, don’t test the edge cases.
# Critical review

The advantages of this approach are obvious. However, initially you’d save some time by just coding your queries wherever you need them and skipping the “overhead” of creating CQS methods and associated tests.

This being said, I’m 110% sure that you’ll spend a lot more time during the lifecycle of your project due to missing/bad tests, longer running pipelines and bloated business logic.

# Fin

I’d be happy to discuss your thoughts and experiences on this topic and engange in an informed exchange. Structuring your code, especially your business logic is hard and I’m pretty sure this approach is not the be-all and end-all.


