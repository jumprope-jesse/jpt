# OAuth 2.0 Authorization Code Flow

Practical walkthrough of implementing OAuth using the Authorization Code grant type with Google.

**Source**: https://annotate.dev/p/hello-world/learn-oauth-2-0-by-building-your-own-oauth-client-U2HaZNtvQojn4F

## High-Level Flow

1. **User clicks "Log in with Google"** - Initiates the flow
2. **Your server redirects to Google** - With client ID identifying your app
3. **Google shows consent screen** - User agrees to share requested data (scopes)
4. **User consents, receives code** - Google redirects back with authorization code in URL
5. **Server exchanges code for token** - Server sends code + client secret to Google
6. **Server fetches user info** - Uses access token to get email, name, etc.

## Key Parameters

### Initial Redirect to Google

```
https://accounts.google.com/o/oauth2/auth?
  response_type=code
  &client_id=<your_client_id>
  &redirect_uri=http://localhost:3000/oauth/google/callback
  &scope=email
  &state=<random_string>
```

| Parameter | Purpose |
|-----------|---------|
| `response_type=code` | Authorization Code grant (server-based apps) |
| `client_id` | Identifies your application to Google |
| `redirect_uri` | Where Google redirects after consent (must be registered) |
| `scope` | What data you're requesting (email, profile, etc.) |
| `state` | CSRF protection - random string stored in cookie, verified on callback |

### Token Exchange (Server-to-Server)

POST to `https://oauth2.googleapis.com/token`:
- `grant_type=authorization_code`
- `code=<code from Google>`
- `redirect_uri=<same as original>` (verified, not used for redirect)
- `client_id` + `client_secret` (proves server identity)

Response includes `access_token` for API calls.

## Security Considerations

### Why client_secret stays on server
Including it in the initial redirect URL would expose it to users/attackers who could impersonate your app.

### State parameter prevents CSRF
1. Generate random string, store in cookie
2. Include in redirect to Google
3. Google returns it in callback URL
4. Verify cookie matches query param
5. If mismatch, abort - request didn't originate from your site

### Redirect URI registration
Must register exact URIs in Google console. Prevents attackers from redirecting auth codes to their servers.

## OAuth Terminology

| Informal | OAuth Term |
|----------|------------|
| User | Resource Owner |
| Browser | User Agent |
| Google | OAuth Provider |
| Your server | Client |
| Google's token endpoint | Authorization Server |
| Google's userinfo endpoint | Resource Server |

## Practical Advice

**Don't roll your own OAuth client** - Subtle bugs create serious security risks. Use well-tested open-source libraries instead.

Understanding the flow helps with:
- Configuring OAuth libraries correctly
- Debugging OAuth issues
- Learning other flows (PKCE, implicit, refresh tokens)
- Understanding OpenID Connect (OIDC) which builds on OAuth

## Related Flows

- **PKCE**: For mobile/SPA apps without secure client_secret storage
- **Implicit**: Deprecated flow for browser-only apps
- **Refresh tokens**: For long-lived sessions without re-auth
- **OpenID Connect (OIDC)**: Identity layer on top of OAuth for authentication (vs just authorization)
