---
type: link
source: notion
url: https://www.photondesigner.com/articles/email-sign-in
notion_type: Software Repo
tags: ['Running']
created: 2024-02-17T05:24:00.000Z
---

# The simplest way to add magic link sign-in using Django ✉️

## AI Summary (from Notion)
- Topic: Implementation of magic link sign-in in Django applications.
- Purpose: To demonstrate a simple way to enable email sign-in without using passwords.
- User Flow:
- User enters their email and requests a login email.
- User clicks the link in the email to verify their email address.
- User is logged in automatically.

- Setup Steps:
- Install Django and create a new project/app.
- Create a custom user model to include an email verification field.
- Configure email backend settings using environment variables for secure email handling.

- Email Verification Process:
- Send a sign-in email with a unique verification link.
- Users verify their emails to log in.

- HTML Templates:
- Includes forms for signing in and a home page to confirm successful login.

- URL Routing:
- Set up URLs for sign-in, sign-out, email verification, and home.

- Deployment Tips:
- Use a production-grade email service for better deliverability and analytics.

- Interesting Fact:
- The guide emphasizes the ease of adding email sign-in compared to traditional password systems.
- Final Note:
- Introduction to a tool called "Photon Designer" aimed at speeding up Django development.

## Content (from Notion)

We'll build a sample Django app to demonstrate the simplest way to add email sign-in, aka magic link sign-in, to Django.

I like using email sign in because it's simple to add and avoids needing passwords. The user will:

1. Enter their email and click to send a login email.
1. Click the link in the email to verify their email.
1. Be logged in
Let's get started 🐎

## 0. Setup your Django app

- Install Django and create a project and app:
```plain text
pip install django python-dotenv
django-admin startproject core .
python manage.py startapp sim

```

- Add sim to INSTALLED_APPS in core/settings.py:
```plain text
INSTALLED_APPS = [
    ... # Other apps
    'sim',
]

```

## 1. Create your user model

We'll add a Custom User model to our app from the start, in keeping with good practice. - In sim/models.py, create a User model by adding the below code:

```plain text
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    has_verified_email = models.BooleanField(default=False)




```

- Add your user model anywhere in core/settings.py:
```plain text
AUTH_USER_MODEL = 'sim.User'

```

- Create your database using your user model:
```plain text
python manage.py makemigrations
python manage.py migrate

```

## 2. Add your email backend to your settings

### Add your environment variables

- Create a file called .env at core/.env and add the below to it. We'll use this to load our environment variables, without adding them to version control.
```plain text
EMAIL_VERIFICATION_URL='http://localhost:8000/verify-email'
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER=<your email address>
EMAIL_HOST_PASSWORD=<your email app password>
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_USE_SSL=False


```

### Get your email service credentials

If you want to use Gmail to send emails, follow these steps to Create & use app passwords.

- Use the app password (remove the whitespace) as your EMAIL_HOST_PASSWORD.
- Use your Gmail address as your EMAIL_HOST_USER.
If you're not using Gmail, search for "how to get email service credentials for <>", and you'll likely find a guide for your email service. Almost all email services provide this, unless they're end-to-end encrypted (e.g., ProtonMail).

### Update your .env file with your email service credentials

- Update your .env file with the SMTP email config from your email provider. We'll use these to send emails from your Django app.
### Load your environment variables

In core/settings.py, we will set your email backend to use your environment variables. We use these environment variables to let us set different email backends in development and production.

- Add the below code to the top of your core/settings.py file.
```plain text
import os
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()


EMAIL_BACKEND=os.environ['EMAIL_BACKEND']
EMAIL_HOST=os.environ['EMAIL_HOST']
EMAIL_PORT=os.environ['EMAIL_PORT']
EMAIL_USE_TLS=os.environ['EMAIL_USE_TLS']
EMAIL_HOST_USER=os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD=os.environ['EMAIL_HOST_PASSWORD']

```

## 3. Send a sign in email with Django

Create a file called sim/services.py, and add the below function to send a verification email:

```plain text
import os
from typing import Optional

from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.conf import settings

from sim.models import User


def send_sign_in_email(user: User) -> None:
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    verification_link = f"{os.environ['EMAIL_VERIFICATION_URL']}/{uid}/{token}/"

    subject = 'Verify your email address 🚀'
    message = (
        'Hi there 🙂\n'
        'Please click '
        f'<a href="{verification_link}" target="_blank">here</a> '
        'to verify your email address'
    )
    send_mail(subject, '', settings.EMAIL_HOST_USER, [user.email], html_message=message)


def decode_uid(uidb64: str) -> Optional[str]:
    """Decode the base64 encoded UID."""
    try:
        return urlsafe_base64_decode(uidb64).decode()
    except (TypeError, ValueError, OverflowError) as e:
        print(f'{e = }')
        return None


def get_user_by_uid(uid: str) -> Optional[User]:
    """Retrieve user object using UID."""
    try:
        return User.objects.get(pk=uid)
    except User.DoesNotExist as e:
        print(f'{e = }')
        return None


```

## 4. Creating the views

In sim/views.py, create views to handle sign in and email verification. We'll also add views to handle sign out and a home screen to make it easier to check our email sign in flow.

```plain text
from django.http import HttpRequest
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from .models import User
from django.shortcuts import redirect
from django.contrib.auth import login
from .services import send_sign_in_email, decode_uid, get_user_by_uid
from .forms import CreateUserForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


def verify_email(request: HttpRequest, uidb64: str, token: str) -> HttpResponse:
    """
    Verify user email after the user clicks on the email link.
    """
    uid = decode_uid(uidb64)
    user = get_user_by_uid(uid) if uid else None

    if user and default_token_generator.check_token(user, token):
        user.has_verified_email = True
        user.save()
        login(request, user)
        return redirect('home')

    print("Email verification failed")
    return redirect('sign_in')


class SendSignInEmail(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        if not request.user.is_anonymous and request.user.has_verified_email:
            return redirect('home')
        form = CreateUserForm()
        return render(request, 'sign_in.html', {'form': form})

    def post(self, request: HttpRequest) -> HttpResponse:
        data = {
            'username': request.POST['email'],
            'email': request.POST['email'],
            'password': request.POST['email']
        }
        user, created = User.objects.get_or_create(
            email=data['email'],
            defaults={'username': data['email'], 'password': data['email']}
        )
        return self._send_verification_and_respond(user)

    @staticmethod
    def _send_verification_and_respond(user: User) -> HttpResponse:
        send_sign_in_email(user)
        message = (
            f"We've sent an email ✉️ to "
            f'<a href=mailto:{user.email}" target="_blank">{user.email}</a> '
            "Please check your email to verify your account"
        )
        return HttpResponse(message)


def sign_out(request: HttpRequest) -> HttpResponse:
    request.session.flush()
    return redirect('sign_in')


def home(request: HttpRequest) -> HttpResponse:
    if not request.user.is_anonymous and request.user.has_verified_email:
        return render(request, 'home.html')
    else:
        return redirect('sign_in')



```

## 6. Add your HTML templates

Create a folder called templates in your sim app, and add the below files and HTML to the templates folder:

### sign_in.html

```plain text
<!DOCTYPE html>
<html>
<head>
    <title>Sign in</title>
    <script src="https://unpkg.com/htmx.org"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        form {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            width: 400px;
            font-size: 14px;
        }

        h2 {
            color: #333;
            text-align: center;
        }

        input[type="text"] {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }

        input[type="text"]:focus {
            border-color: #0056b3;
            outline: none;
        }

        button {
            width: 100%;
            padding: 10px;
            background-color: #0056b3;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        button:hover {
            background-color: #004494;
        }

        p {
            color: #333;
            text-align: center;
        }
    </style>
</head>
<body>
<form method="post" hx-post="/sign-in" hx-target="#result">
    <p>Sign in</p>
    {% csrf_token %}
    <input type="text" name="email" placeholder="Email" required>
    <button type="submit">Sign in</button>
    <div id="result"></div>
</form>

</body>
</html>


```

### home.html

```plain text
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
<p>Hi {{ request.user }} 👋</p>

<p>You've successfully signed in using your email address ✅</p>

<p>Click here to <a href="/sign-out">sign out</a></p>


</body>
</html>


```

## 7. Connect your URLs

Create the file sim/urls.py, and add the below code to it to set up the URL for email verification:

```plain text
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sign-in', views.SendSignInEmail.as_view(), name='sign_in'),
    path('sign-out', views.sign_out, name='sign_out'),
    path('verify-email/<uidb64>/<token>/', views.verify_email, name='verify_email'),
]


```

Add include sim.urls in your core/urls.py.

```plain text
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sim.urls')),
]


```

### 8. Add your create user form

- Create a file at sim/forms.py and add the below code to it:
```plain text
from django.forms import ModelForm
from .models import User


class CreateUserForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

```

### 9. Run your server and check your email verification flow

```plain text
python manage.py runserver

```

Visit http://localhost:8000/ to sign in with your email address. You should receive an email with a link to verify your email address. Click the link, and you will see the home screen.

## Congratulations! You've added email verification to your Django app 🎉 What next?

### Overview of Deploying to Production (It's easy)

### a. Get a production-grade email service

For your production server, I'd recommend connecting a production-grade server (Examples: Amazon SES, Mailgun, Sendgrid, etc.) to your Django app. This is a good idea because you get:

1. Higher deliverability
1. In-built monitoring and analytics
1. Scalability (Minor point): These services will handle sending many emails at once to many addresses, which is phenomenon that you'll hopefully have 🙂
### b. Connect your production-grade email service to your Django app

After you’ve signed up for a production-grade email service, connect the service to your app simply by adding the service’s details as environment variables to your production server.

If you’re unsure about how to do that, see me adding environment variables to a production server in this guide Deploy an instant messaging app with Django 🚀

## P.S Django frontend at warp speed? ⚡️

Do you also dream of creating Django products so quickly they break the space-time continuum? Yeah, me too. We're like Django wizards, eager to turn our magical ideas into reality at the snap of our fingers.

Well, let me introduce you to the magic wand I'm building: Photon Designer. It's a visual editor that puts the 'fast' in 'very fast.' When Photon Designer gets going, it slings Django templates at you faster than light escaping a black hole.

Warning: may cause excessive joy and productivity.


