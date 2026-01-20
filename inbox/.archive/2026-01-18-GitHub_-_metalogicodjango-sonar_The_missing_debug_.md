---
type: link
source: notion
url: https://github.com/metalogico/django-sonar
notion_type: Software Repo
tags: ['Running']
created: 2024-05-11T21:58:00.000Z
---

# GitHub - metalogico/django-sonar: The missing debug tool for django

## AI Summary (from Notion)
- Project Overview: DjangoSonar is a debugging and introspection tool for Django applications, inspired by Laravel Telescope.
- Motivation: The creator missed Laravel Telescope after switching from Laravel to Django, leading to the development of DjangoSonar.
- Key Features:
- Self-updating lists for requests, exceptions, queries, and dumps.
- Request insights including payload, authenticated user, session variables, and headers.
- Historical data storage that can be cleared.
- A simple and reactive user interface.
- Installation Steps:
- Install the package via pip.
- Add 'django_sonar' to the INSTALLED_APPS in the project settings.
- Update the urls.py to include the sonar dashboard.
- Configure exclusions to avoid excessive data collection.
- Run migrations to set up necessary tables.
- Add DjangoSonar middleware for data collection.
- Usage Notes:
- Access the dashboard through the /sonar/ URL.
- The tool can be used in production but should be managed carefully to avoid excessive data accumulation.
- Only authenticated superusers can access the dashboard.
- Functionality: Users can dump values to DjangoSonar using the sonar() helper function for debugging.
- Licensing: DjangoSonar is licensed under the MIT license.
- Support: The creator welcomes donations for the project.

## Content (from Notion)

# DjangoSonar

The missing debug tool for django.

DjangoSonar is a comprehensive debugging and introspection tool for Django applications, inspired by Laravel Telescope.

## 🥳 Motivation

Having spent years developing with Laravel before switching to Django, the first thing I missed from this change was the amazing Laravel Telescope. So, I decided to create it myself.

DjangoSonar is built using:

- Django
- Bootstrap 5
- htmx
If you use this project, please consider giving it a ⭐.

## ⭐ Features

- Self updating lists of: 
- Request insights: 
- Historical data (clearable)
- Simple and reactive UI
## 🛠️ How to install

1. First you need to install the package:
```plain text
pip install django-sonar
```

1. Then, to enable the dashboard, you will need to add the app to the INSTALLED_APPS in your project main settings file:
```plain text
INSTALLED_APPS = [
    ...
    'django_sonar',
    ...
]
```

1. Add the urls to the main urls.py file in your project folder:
```plain text
urlpatterns = [
    ...
    path('sonar/', include('django_sonar.urls')),
    ...
]
```

1. 🔔 Be sure to add the exclusions settings too, or you will get way too much data in your sonar dashboard:
```plain text
DJANGO_SONAR = {
    'excludes': [
        STATIC_URL,
        MEDIA_URL,
        '/sonar/',
        '/admin/',
        '/__reload__/',
    ],
}
```

In this example I'm excluding all the http requests to static files, uploads, the sonar dashboard itself, the django admin panels and the browser reload library. Update this setting accordingly, YMMW.

1. Now you should be able to execute the migrations to create the two tables that DjangoSonar will use to collect the data.
```plain text
python manage.py migrate
```

1. And finally add the DjangoSonar middleware to your middlewares to enable the data collection:
```plain text
MIDDLEWARE = [
  ...
  'django_sonar.middlewares.requests.RequestsMiddleware',
  ...
]
```

## 😎 How to use

### The Dashboard

To access the dashboard you will point your browser to the /sonar/ url (but you can change it as described before). The interface is very simple and self explanatory.

You could use DjangoSonar in production too, since it gives you an historical overview of all the requests, but be sure to clear the data and disable it when you have debugged the problem.

🔔 If you forget to disable/clear DjangoSonar you could end up with several gigabytes of data collected. So please use it with caution when in production 🔔

Only authenticated superusers can access sonar. If you are trying to access the dashboard with a wrong type of user, you will see an error page, otherwise you should see the DjangoSonar login page.

### sonar() - the dump helper

You can dump values to DjangoSonar using the sonar() helper function:

```plain text
from django_sonar.utils import sonar

sonar('something')
```

And you can also dump multiple values like this:

```plain text
from django_sonar.utils import sonar

sonar('something', self.request.GET, [1,2,3])
```

## ⚖️ License

DjangoSonar is open-sourced software licensed under the MIT license.

## 🍺 Donations

If you really like this project and you want to help me please consider buying me a beer 🍺


