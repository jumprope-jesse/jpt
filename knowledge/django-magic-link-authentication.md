# Django Magic Link Authentication (DIY)

Simple passwordless email authentication implementation for Django without external libraries.

**Source**: https://www.photondesigner.com/articles/email-sign-in

## Overview

Email-based "magic link" authentication that avoids passwords:
1. User enters email address
2. System sends email with unique verification link
3. User clicks link → email verified → logged in

**Alternative**: django-allauth v64.0+ includes built-in "Magic Code Login" - consider that for production apps.

## Implementation Pattern

### Custom User Model
```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    has_verified_email = models.BooleanField(default=False)
```

### Token Generation
Uses Django's built-in `default_token_generator`:
```python
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

token = default_token_generator.make_token(user)
uid = urlsafe_base64_encode(force_bytes(user.pk))
verification_link = f"{os.environ['EMAIL_VERIFICATION_URL']}/{uid}/{token}/"
```

### Email Backend Config
Environment variables for email settings:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = '<your-email>'
EMAIL_HOST_PASSWORD = '<app-password>'  # Gmail: Create app password in settings
EMAIL_PORT = 587
EMAIL_USE_TLS = True
```

### Verification Flow
```python
def verify_email(request, uidb64, token):
    uid = urlsafe_base64_decode(uidb64).decode()
    user = User.objects.get(pk=uid)

    if user and default_token_generator.check_token(user, token):
        user.has_verified_email = True
        user.save()
        login(request, user)
        return redirect('home')

    return redirect('sign_in')
```

### User Creation Pattern
Get-or-create pattern for email-only users:
```python
user, created = User.objects.get_or_create(
    email=data['email'],
    defaults={'username': data['email'], 'password': data['email']}
)
```

## Production Considerations

### Email Service Providers
Switch to production email service for:
- Higher deliverability (avoid spam filters)
- Monitoring and analytics
- Scalability
- Examples: Amazon SES, Mailgun, SendGrid

### Security Enhancements
- Add rate limiting on email sending
- Token expiration (django's tokens expire after PASSWORD_RESET_TIMEOUT, default 3 days)
- HTTPS-only links in production
- Consider adding email verification cooldown

### Token Validity
Django's `default_token_generator` includes:
- User's last login timestamp
- User's password hash
- User's primary key
- Secret key from settings

Token auto-invalidates when:
- User logs in (changes last_login)
- Exceeds PASSWORD_RESET_TIMEOUT (default 3 days)

## Comparison to django-allauth

| Aspect | DIY Implementation | django-allauth |
|--------|-------------------|----------------|
| Setup complexity | ~200 lines | Add to INSTALLED_APPS + config |
| Features | Basic magic link | Magic codes, social auth, MFA, passkeys |
| Rate limiting | Manual | Built-in (`"5/m/user"` syntax) |
| Security notifications | Manual | Built-in (password changes, IP tracking) |
| Headless API | Manual | Official API with tokens |
| Production-ready | Needs hardening | Battle-tested |

## When to Use DIY vs Library

**Use DIY when:**
- Learning Django authentication internals
- Minimal app with no other auth needs
- Want full control over every detail
- Avoiding dependencies

**Use django-allauth when:**
- Production application
- Need social auth, MFA, or passkeys later
- Want security best practices out of the box
- Value maintenance and updates

## Related Tools

**Photon Designer**: Visual editor for Django templates (product mentioned in article)
- Speeds up Django frontend development
- Creates templates faster than manual coding
