---
type: link
source: notion
url: https://github.com/PaulGilmartin/django-queryhunter
notion_type: Software Repo
tags: ['Running']
created: 2024-03-08T21:01:00.000Z
---

# GitHub - PaulGilmartin/django-queryhunter: Hunt down the lines of your Django application code which are responsible for executing the most queries.

## AI Summary (from Notion)
- Purpose: The django-queryhunter library helps identify lines of Django application code responsible for executing the most SQL queries.
- Functionality:
- Provides a context manager and middleware for profiling SQL queries.
- Offers detailed reporting on query execution, including line number, code, number of queries, and execution duration.
- Helps identify performance issues, such as missing select_related and prefetch_related calls.
- Installation: Can be installed via pip and requires setting QUERYHUNTER_BASE_DIR in the Django settings.
- Sample Output: Displays query execution details, making it easier to pinpoint problematic code.
- Middleware Feature: Profiles all requests made to the Django application, capturing additional metadata like request URL and method.
- Reporting Options: Configurable options for printing or logging profiling data, enabling customization based on specific needs or preferences.
- Limitations: While effective, the library has not been tested in production environments, so users should proceed cautiously.
- Custom Metadata: Users can add custom metadata to profiling outputs, which is useful for tracking specific requests or identifiers.
- Hot Take: This tool fills a gap left by other profiling libraries, making it invaluable for optimizing Django applications.
- Interesting Fact: The output can highlight performance issues that may be overlooked in large codebases, thereby facilitating code optimization.

## Content (from Notion)

# django-queryhunter

Hunt down the lines of your Django application code which are responsible for executing the most queries.

Libraries such as django-silk are excellent for profiling the queries executed by your Django application. We have found, however, that they do not provide a completely straightforward way to identify the lines of your application code which are responsible for executing the most queries. This library aims to fill that gap by providing a simple code-first approach to query profiling.

One particularly useful feature of this view of profiling is quickly identifying missing select_related and prefetch_related calls.

## Highlights

- Context manager and middleware for profiling queries which can provide a detailed report of the lines of your application code which are responsible for executing SQL queries, including data on: 
- Configurable options for filtering, sorting, printing or logging the results.
- Lightweight: queryhunter uses Django's database hooks and the built-in linecache module to provide a simple and efficient way to map SQL queries to the lines of your application code which executed them.
Here is some sample output:

```plain text
queryhunter/tests/my_module.py
====================================
Line no: 13 | Code: for post in posts: | Num. Queries: 1 | SQL: SELECT "tests_post"."id", "tests_post"."content", "tests_post"."author_id" FROM "tests_post" | Duration: 4.783299999999713e-05
Line no: 14 | Code: authors.append(post.author.name) | Num. Queries: 5 | SQL: SELECT "tests_author"."id", "tests_author"."name" FROM "tests_author" WHERE "tests_author"."id" = %s LIMIT 21 | Duration: 8.804199999801199e-05
```

## Limitations

We have used this on a production level code base and has outperformed similar libraries in diagnosing certain kinds of performance issues. We however have not yet enabled it in a production environment, so proceed with caution here. Note also that the aim of queryhunter is to identify the lines of your application code which result in SQL queries. It can however be configured to profile third party code with the appropriate choice of QUERYHUNTER_BASE_DIR, as explained in the Installation section below.

## Installation

```plain text
pip install django-queryhunter
```

You must then declare the QUERYHUNTER_BASE_DIR setting in your settings.py file. This is the way that queryhunter knows where to look for your application code (or rather, the point in the stack at which to report as being responsible for executing a query).

You can use the built-in callable queryhunter.default_base_dir to set it to be the project root or make it a string of your choosing.

```plain text
import queryhunter

QUERYHUNTER_BASE_DIR = queryhunter.default_base_dir(__file__)
```

## Usage via Example

Let's suppose we have a Django application with the following models (a fully functional example can be found in the queryhunter.tests directory):

```plain text
# queryhunter/tests/models.py
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    content = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

Now suppose we have another module my_module.py where we fetch our posts and collect their author's names in a list. We run this code under the queryhunter context manager, which will collect information on the lines of code responsible for executing SQL queries inside the context:

```plain text
# queryhunter/tests/my_module.py
from queryhunter.tests.models import Post, Author
from queryhunter import queryhunter

def get_authors() -> list[Author]:
    with queryhunter():
        authors = []
        posts = Post.objects.all()  # suppose we have 5 posts
        for post in posts:
            authors.append(post.author.name)
    return authors
```

Let's now run the code

```plain text
>>> from queryhunter.tests.my_module import get_authors
>>> get_authors()
```

and see what the output from the queryhunter is:

```plain text
queryhunter/tests/my_module.py
====================================
Line no: 8 | Code: for post in posts: | Num. Queries: 1 | SQL: SELECT "tests_post"."id", "tests_post"."content", "tests_post"."author_id" FROM "tests_post" | Duration: 4.783299999999713e-05
Line no: 9 | Code: authors.append(post.author.name) | Num. Queries: 5 | SQL: SELECT "tests_author"."id", "tests_author"."name" FROM "tests_author" WHERE "tests_author"."id" = %s LIMIT 21 | Duration: 8.804199999801199e-05
```

What can we learn from this output?

- There are 2 distinct lines of code responsible for executing SQL in the get_authors function.
- The line authors.append(post.author.name) was responsible for executing 5 SQL queries, one for each post.
- This is a quick way to identify that we are missing a select_related('author') call in our Post.objects.all() query.
This may have been obvious in this contrived example, but in a large code base, flushing out these kinds of issues can be very useful. Additional custom data can be added to the output as explained below in the Reporting Options section.

## Middleware

queryhunter also ships with a middleware which, when installed, will profile all requests to your Django application. To install the middleware, add queryhunter.middleware.QueryHunterMiddleware to your MIDDLEWARE setting:

```plain text
# settings.py
MIDDLEWARE = [
    # ...
    'queryhunter.middleware.QueryHunterMiddleware',
]
```

Under the hood, the middleware will run all requests under the queryhunter.queryhunter context manager. As well as the usual query data reported by queryhunter, the middleware will also report the URL and the method of the request which caused the queries to be executed. Here's some sample output:

```plain text
queryhunter/tests/my_module.py
====================================
Line no: 8 | Code: for post in posts: | Num. Queries: 1 | Duration: 0.04 | url: /authors | method: GET | SQL: SELECT "tests_post"."id", "tests_post"."content", "tests_post"."author_id" FROM "tests_post"
Line no: 9 | Code: authors.append(post.author.name) | Num. Queries: 5 | Duration: 0.05 | url: /authors | method: GET | SQL: SELECT "tests_author"."id", "tests_author"."name" FROM "tests_author" WHERE "tests_author"."id" = %s LIMIT 21
```

## Reporting Options

queryhunter can be configured with a number of options which dictate the way the profiling data is reported and displayed. We can declare the options globally via the QUERYHUNTER_REPORTING_OPTIONS setting in our settings.py file, or we can pass reporting options more granularly to the queryhunter context manager.

In either case, options are declared as an instance of either the PrintingOptions class or the LoggingOptions class.

By default, reporting will be based on the default values of PrintingOptions. If for example you wanted to set it so that your output is always so that the lines of code which execute the most queries are printed first, you would declare the following in your settings.py file:

```plain text
# settings.py
from queryhunter import PrintingOptions

QUERYHUNTER_REPORTING_OPTIONS = PrintingOptions(sort_by='-count')
```

or, alternatively, you could pass the instance into a specific context manager:

```plain text
from queryhunter import queryhunter, PrintingOptions

with queryhunter(reporting_options=PrintingOptions(sort_by='-count')):
    ...
```

If a context manager uses an explicit instance of PrintingOptions or LoggingOptions, it will override the global QUERYHUNTER_REPORTING_OPTIONS setting.

### PrintingOptions

Use the PrintingOptions class if you want to print the profiling results to the console. PrintingOptions class can be configured via the attributes below:

- sort_by: A string valued property which determines the order in which each line of code is printed for each module profiled. Options are line_no, -line_no, count, -count, duration, -duration. The default is line_no.
- modules: An optional list of strings which can be used to filter the modules which are profiled. The default is None, which means all modules touched within the context are profiled.
- max_sql_length: An optional integer valued property which determines the maximum length of the SQL query printed. The default is None, meaning the entire SQL query is printed.
- count_highlighting_threshold: An integer valued property which determines the threshold for the number of queries executed on a line of code before it is highlighted red in the output. The default is 5.
- duration_highlighting_threshold: A float valued property which determines the threshold for the no. of seconds a line of code can spend executing before it is highlighted red in the output. The default is 0.1.
- count_threshold: An integer valued property which determines the threshold for the number of queries executed on a line of code before it is printed. The default is 1.
- duration_threshold: A float valued property which determines the threshold for the no. of seconds a line of code can spend executing before it is printed. The default is 0.0.
### LoggingOptions

Use the LoggingOptions class if you want to log the profiling results to a file. LoggingOptions class can be configured via the attributes below:

- logger_name: A string valued property which determines the name of the logger which will be used to log the output. The default is queryhunter.
- sort_by: A string valued property which determines the order in which each line of code is printed for each module profiled. Options are line_no, -line_no, count, -count, duration, -duration. The default is line_no.
- modules: An optional list of strings which can be used to filter the modules which are profiled. The default is None, which means all modules touched within the context are profiled.
- max_sql_length: An optional integer valued property which determines the maximum length of the SQL query printed. The default is None, meaning the entire SQL query is printed.
- count_threshold: An integer valued property which determines the threshold for the number of queries executed on a line of code before it is logged. The default is 1.
- duration_threshold: A float valued property which determines the threshold for the no. of seconds a line of code can spend executing before it is logged. The default is 0.0.
Logging is compatible with the standard Python logging library and its Django extension. For example, to have queryhunter log to a file called queryhunter.log, we can add the following to our settings.py file:

```plain text
QUERYHUNTER_REPORTING_OPTIONS = LoggingOptions(logger_name='queryhunter', sort_by='-count')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(message)s'
        },
    },
    'handlers': {
        'queryhunter_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': QUERYHUNTER_BASE_DIR + '/queryhunter.log',
            'formatter': 'standard',
        },
    },
    'loggers': {
        QUERYHUNTER_REPORTING_OPTIONS.logger_name: {
            'handlers': ['queryhunter_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
```

This will produce a log file queryhunter.log which has content like below:

```plain text
2024-02-18 07:04:16,182 - Module: django-queryhunter/queryhunter/tests/my_module.py | Line no: 14 | Code: authors.append(post.author.name) | Num. Queries: 5 | SQL: SELECT "tests_author"."id", "tests_author"."name" FROM "tests_author" WHERE "tests_author"."id" = %s LIMIT 21 | Duration: 3.174999999999706e-05 | url: /authors/ | method: GET
2024-02-18 07:04:16,182 - Module: django-queryhunter/queryhunter/tests/my_module.py | Line no: 13 | Code: for post in posts: | Num. Queries: 1 | SQL: SELECT "tests_post"."id", "tests_post"."content", "tests_post"."author_id" FROM "tests_post" | Duration: 1.2500000000026379e-05 | url: /authors/ | method: GET
```

## Custom Metadata

You can add custom metadata to queryhunter's output by passing in the metadata argument to the queryhunter context manager. In fact, this is precisely what the middleware does to add the URL and method of the request:

```plain text
from queryhunter import queryhunter

with queryhunter(meta_data=dict(url=request.path, method=request.method)):
    ...
```

Adding custom meta data can be particularly useful when you want to associate an identifier with the profiling data.


