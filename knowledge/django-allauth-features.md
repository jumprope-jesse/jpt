# django-allauth Features

Django authentication library with comprehensive social account support.

**Docs**: https://docs.allauth.org/

## Key Features (v64.0+)

### Authentication Methods
- **WebAuthn/Passkeys**: Security key and passkey login support (disabled by default)
- **Magic Code Login**: Email-based passwordless login
- **TOTP MFA**: Time-based one-time passwords with rate limiting
- **Social OAuth**: 50+ providers including Google One Tap Sign-In
- **SAML**: Enterprise SSO support (IdP-initiated disabled by default for security)

### Headless Mode
Official API for SPAs and mobile apps via `allauth.headless`:
- Token strategy with refresh tokens and `expires_in`
- `serialize_user()` adapter method for custom payloads
- TOTP URI in MFA activation response
- Proper HTTP status codes (409 for conflicts, 403 for closed signup)
- `HEADLESS_ONLY` mode to disable traditional views

### Security Features
- Rate limiting: `"5/m/user"`, `"5/m/ip"`, `"5/m/key"`, or combined `"20/m/ip,5/m/key"`
- Email notifications for security events (password changes with IP/user agent)
- Honeypot field for bot prevention
- `secure_admin_login()` decorator for Django admin protection
- Enumeration prevention on signup

### Email Handling
- All emails stored lowercase (case-insensitive lookups)
- Email confirmation cooldown via rate limits

## Configuration

```python
INSTALLED_APPS = [
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.headless',  # For SPA/mobile
    'allauth.mfa',       # For MFA
]

# Key settings
ACCOUNT_EMAIL_NOTIFICATIONS = True  # Security notifications
SOCIALACCOUNT_ONLY = True  # Disable local accounts
SOCIALACCOUNT_EMAIL_AUTHENTICATION = True  # Email-based social auth
```

## Version Notes
- v64.0+ uses semantic versioning (jumped from 0.x.y)
- Dropped Django 3.2, 4.0, 4.1 and Python 3.7
- Facebook default Graph API: v19.0

## Project History & Philosophy (2024)

### Origins (2010)
Started to consolidate fragmented authentication packages. Goal: single reusable solution for local + social accounts with integrated approach.

### Why Not SaaS?
- **Open source critical**: Authentication is too important to depend on proprietary services
- **Data ownership**: Self-hosted means you own your user data
- **Simplified deployment**: Fewer moving parts vs. self-hosting third-party auth services
- **Open Internet**: Prevents pushing users toward centralized auth solutions

### Evolution Challenge
External projects building on allauth (e.g., 2FA extensions) face compatibility issues. Solution: integrate essential features into core rather than external dependencies.

### 2024 Roadmap (NGI Zero Grant)
Funded by NGI Zero/NLnet foundation to go beyond maintenance:

1. **First-class API support**
   - Full OpenAPI specification
   - React example SPA showcasing all flows
   - Already in progress, expected first

2. **WebAuthn/Passkeys**
   - U2F as second factor
   - Passkey support for passwordless

**Philosophy**: Core authentication features (2FA, passwordless, SPA support) should be integrated, not bolted-on externally.

**Funding**: Liberapay and GitHub Sponsors
