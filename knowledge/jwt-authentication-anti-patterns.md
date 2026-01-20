# JWT Authentication Anti-Patterns

Source: [Should I Use JWTs For Authentication Tokens?](https://blog.ploetzli.ch/2024/should-i-use-jwt-for-authentication/)

## TL;DR

Don't use JWTs for authentication tokens unless you're at Google/Facebook scale (10k+ requests/second). Use opaque session tokens stored in your database instead.

## Why JWTs Exist

JWTs are designed for massive scale environments where:
- Authentication service is a dedicated, separately scaled service
- Only the auth service needs access to the user database
- Other services verify tokens without database calls

## The Refresh Token Truth

What's rarely spelled out:
- **Refresh token** = the real session token (represents session with auth service, can be revoked)
- **Authentication token** = short-lived derived credential (5 min max)
- Refresh tokens are usually opaque identifiers stored in a database
- This delegates session keepalive to the client

## Signs You Don't Need JWTs

If any of these apply, just use opaque session tokens:
- You implement logout with allow/denylists (hitting DB anyway)
- You check "user active" flags (hitting DB anyway)
- You need user relationships with other DB objects (hitting DB anyway)
- Your service does anything with database data (hitting DB anyway)

## Benefits of Traditional Sessions

- No weird workarounds for JWT shortcomings
- No JWT signing key management complexity
- Avoid JWT library vulnerabilities
- Battle-tested session mechanisms from web frameworks

## If You Want to Feel Enterprise

Use Redis/Valkey for session storage. Still query DB for user data on authenticated requests, but may be faster for unauthenticated requests. Measure before assuming.
