---
type: link
source: notion
url: https://github.com/matthiask/django-admin-ordering/blob/main/admin_ordering/models.py
notion_type: Software Repo
tags: ['Running']
created: 2024-06-15T04:07:00.000Z
---

# django-admin-ordering/admin_ordering/models.py at main · matthiask/django-admin-ordering · GitHub

## AI Summary (from Notion)
- Project Overview: The document pertains to the models.py file of the django-admin-ordering project hosted on GitHub.
- Status: The project is currently marked as "Not started."
- File Details:
- Contains 51 lines of code.
- Implements an abstract class OrderableModel for managing ordering in Django models.
- Key Components:
- Ordering Field: Uses a positive integer field called ordering for sorting.
- Management of Ordering: Automatically sets the ordering field if not provided during save.
- Error Checking: Includes checks to ensure models derived from OrderableModel have the ordering defined.
- Commit and History: The document references the history of commits made to the file.
- Navigation: Provides links to various sections and actions within the GitHub repository, such as issues, pull requests, and file structure.
- Interesting Fact: The file leverages Django's built-in functionalities and integrates error checking to maintain data integrity.

## Content (from Notion)

## Navigation Menu

- Pricing
Sign in

Sign up

/  django-admin-ordering  Public

-  Code
-  Issues 2
-  Pull requests
-  Actions
-  Projects
-  Security
-  Insights
## Files

- .github
- admin_ordering
- tests
- .editorconfig
- .gitignore
- .pre-commit-config.yaml
- AUTHORS
- CHANGELOG.rst
- CONTRIBUTING.rst
- LICENSE
- README.rst
- biome.json
- pyproject.toml
- tox.ini
## Breadcrumbs

1. django-admin-ordering
1. /admin_ordering
/

# models.py

## Latest commit

## History

History

## File metadata and controls

51 lines (43 loc) · 1.63 KB

Raw

from functools import total_ordering from django.core import checks from django.db import models from django.db.models import Max from django.utils.translation import gettext_lazy as _ @total_ordering class OrderableModel(models.Model): ordering = models.PositiveIntegerField(_("ordering"), default=0, db_index=True) class Meta: abstract = True ordering = ["ordering"] def save(self, *args, **kwargs): if not self.ordering: max = self.__class__._default_manager.aggregate(m=Max("ordering"))["m"] self.ordering = 10 + (max or 0) super().save(*args, **kwargs) save.alters_data = True def __lt__(self, other): return ( self.ordering < other.ordering if isinstance(other, type(self)) else False ) @classmethod def check(cls, **kwargs): errors = super().check(**kwargs) if not cls._meta.ordering: errors.append( checks.Error( f'The ordering of "{cls._meta.label}" is undefined.', obj=cls, id="admin_ordering.E002", hint="Make the inner Meta class inherit OrderableModel.Meta.", ) ) elif cls._meta.ordering[0] not in {"ordering", "-ordering"}: errors.append( checks.Warning( f'"{cls._meta.label}" isn\'t ordered by the ordering field.', obj=cls, id="admin_ordering.W003", hint="Make the inner Meta class inherit OrderableModel.Meta.", ) ) return errors

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

40

41

42

43

44

45

46

47

48

49

50

51


