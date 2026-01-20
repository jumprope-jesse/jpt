# Django Atomic QuerySet Methods

Pattern for organizing Django ORM code with clear separation of concerns.

Source: [Going atomic with Django QuerySets](https://medium.com/ambient-innovation/going-atomic-with-django-querysets-53f746418871) by Ronny Vedrilla (April 2024)

## Core Principle

Each database operation should correspond to exactly one custom queryset method. This creates an internal API for your models.

## Rules for Custom QuerySet Methods

1. A CQS method returns a QuerySet
2. A CQS method never modifies data (read-only)
3. If it doesn't return a QuerySet or writes data, it belongs in a manager method

## Example Pattern

Instead of inline ORM in views:

```python
# BAD: ORM logic scattered in views
from django.db.models import Count, F, Value, Q
from django.db.models.functions import Concat

class BlogListView(generic.ListView):
    def get_queryset(self):
        return (
            BlogPost.objects
            .filter(user_id=self.request.user.id)
            .filter(category=self.request.GET["category"])
            .exclude(Q(publish_date__gt=timezone.now()) | Q(reviewed=False))
            .annotate(qty_pictures=Count("pictures"))
            .annotate(author_name=Concat(F("user__first_name"), Value(" "), F("user__last_name")))
        )
```

Create atomic queryset methods:

```python
# GOOD: Atomic queryset methods
class BlogPostQuerySet(models.QuerySet):
    def filter_by_user(self, user_id: int) -> "BlogPostQuerySet":
        """Fetches all posts belonging to the given user"""
        return self.filter(user_id=user_id)

    def filter_by_category(self, category: str) -> "BlogPostQuerySet":
        return self.filter(category=category)

    def only_active(self) -> "BlogPostQuerySet":
        """Excludes unpublished and unreviewed posts"""
        return self.exclude(
            Q(publish_date__gt=timezone.now()) | Q(reviewed=False)
        )

    def annotate_pictures(self) -> "BlogPostQuerySet":
        return self.annotate(qty_pictures=Count("pictures"))

    def annotate_author_name(self) -> "BlogPostQuerySet":
        return self.annotate(
            author_name=Concat(F("user__first_name"), Value(" "), F("user__last_name"))
        )

# Clean view code
class BlogListView(generic.ListView):
    def get_queryset(self):
        return (
            BlogPost.objects
            .filter_by_user(self.request.user.id)
            .filter_by_category(self.request.GET["category"])
            .only_active()
            .annotate_pictures()
            .annotate_author_name()
        )
```

## Benefits

- **Simplicity**: Hide low-level ORM details, easier to understand
- **Separation of concerns**: Keep ORM imports out of views
- **Testability**: Unit test each queryset method separately
- **Reusability**: Compose methods across different views
- **Consistency**: Descriptive API for all data access

## Handling OR Operations

For AND operations, methods chain naturally. For OR operations, combine in a single method:

```python
def filter_active_users(self) -> "UserQuerySet":
    """Fetches users who are active or haven't reached end date"""
    return self.filter(
        Q(is_active=True) | Q(end_date__lte=timezone.now().date())
    )
```

## Trade-offs

- Initial setup takes more time than inline queries
- Pays off over project lifecycle through better tests and maintainability
- Related pattern: HackSoft's "selector pattern" for read-only data access
