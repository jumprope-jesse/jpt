# B2B SaaS Authentication

Authentication for business software (B2B) differs fundamentally from consumer software (B2C) in tenancy models, priorities, and required features.

**Source**: https://tesseral.com/blog/b2b-auth-isnt-that-similar-to-b2c-auth

## Tenancy Models

### B2C: User-First Tenancy
- Customers = individual users who control their own accounts
- Data lives at the account level
- User alone exercises control over their content
- Simple, intuitive isolation model

### B2B: Organization-First Tenancy
- Customer = a company, not an end user
- Companies want control over their users' access
- Need a "tenancy firewall" between organizations
- Users belong to organizations (workspaces, tenants)
- Bolting on B2B multitenancy after the fact is complicated - get it right from the start

## Different Priorities

| Aspect | B2C | B2B |
|--------|-----|-----|
| **Scale** | Billions of users possible (Meta: 3.35B DAP) | Sharding is usually an option |
| **UX Priority** | Critical - users choose products | Less critical - employers choose software |
| **Security Friction** | Avoid at all costs | Acceptable if it serves business needs |
| **Support Economics** | Low ARPU (~$7/user for Pinterest) | High ARPU (~$1,380/user for Zendesk Pro) |
| **Support Model** | Labyrinthine self-service | Can afford 1:1 support, user impersonation |

### Threat Models

**B2C Threats:**
- Phishing and scams
- Account sharing (Uber driver background check circumvention)
- Bots and abuse
- Need identity resolution to link banned accounts

**B2B Threats:**
- Insider attacks (disgruntled employees)
- Credential retention after departure
- Sabotage (Terry Childs incident - locked out all SF municipal employees)

## Required B2B Features

### Enterprise Identity Provider Support
- Businesses use centralized IDPs (Okta, Entra, ADFS, Sailpoint) to manage employee access
- IDPs act like databases: employees, applications, associations
- Must support a broad range of IDPs, including legacy custom builds

### Enterprise SSO (SAML)
- Nearly universal enterprise requirement
- Users authenticate once in IDP, extend context to third-party software
- SAML is archaic but ubiquitous due to history
- Careful implementation needed - easy to introduce security vulnerabilities
- Every customer needs manual configuration (not like "Login with Google")

### SCIM Provisioning
- Automate user provisioning/deprovisioning
- Critical for security: departed employees retaining credentials is a huge problem
- Example: Disney ex-employee edited park menus maliciously after termination

### Role-Based Access Control (RBAC)
- Different users need different permissions within an organization
- Define actions → map to roles → assign roles to users
- Can get complex (Salesforce has arbitrarily complex custom roles)

### Organization-Level Controls
Customer requests like:
- Disable email login for our org
- Prevent user self-invites
- Require Yubikeys for MFA
- Block logins from specific countries

Avoid per-customer if statements - build configurable controls.

### API Keys
- B2B often needs public APIs even at small scale
- Consumers don't typically write code

### Audit Logs
- Comprehensive logs of all actions within an organization
- Legal: evidence for litigation, criminal enquiries
- Security: detect credential stuffing attacks, integrate with SIEM systems
- Need reliable user identification for logs to be useful

## Vendor Selection
Auth vendors rarely do both B2B and B2C well. Choose one focused on your market.

### Open Source Options

**Tesseral** (https://tesseral.com/docs)
- Focused on B2B specifically

**Ory Kratos** (https://www.ory.sh/kratos/)
- Cloud-native identity and user management system
- Headless, API-first design - bring your own UI
- Written in Go, SDKs for all major languages
- Features:
  - Self-service login/registration
  - MFA: TOTP, FIDO2, WebAuthn (Yubikeys, FaceID)
  - Social login (any OIDC provider)
  - Custom identity models (define your own fields)
  - Account verification and recovery flows
  - Webhooks for extensibility
- No UI included - you build the frontend, it provides the API
- Good for teams wanting full control over the auth experience
- Active open source community (GitHub, Slack)
- Part of the Ory ecosystem (also includes Hydra for OAuth2, Oathkeeper for access proxy)
