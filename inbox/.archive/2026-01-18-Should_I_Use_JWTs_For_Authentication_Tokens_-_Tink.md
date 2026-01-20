---
type: link
source: notion
url: https://blog.ploetzli.ch/2024/should-i-use-jwt-for-authentication/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-05-28T11:57:00.000Z
---

# Should I Use JWTs For Authentication Tokens? - Tinker, Tamper, Alter, Fry

## AI Summary (from Notion)
- JWT Overview: JSON Web Tokens (JWTs) are a standard for authenticated tokens consisting of a header, payload, and signature.
- Core Functionality: JWTs allow verification of the token's authenticity without connecting to a user database, which is beneficial for large-scale environments like Google and Facebook.
- Short Token Lifespan: Authentication tokens should have a short lifespan (around 5 minutes), with refresh tokens used to request new authentication tokens.
- Common Misconception: The refresh token is the real session token, while the authentication token is for short-term use.
- Challenges for Non-Scale Environments: If you're not operating at a scale like Google, JWTs may introduce unnecessary complexity, such as maintaining allowlists or denylists for logouts and user blocking.
- Recommendation: For most applications, using a normal opaque session token stored in the database is simpler and more effective than JWTs.
- Benefits of Traditional Tokens:
- Eliminates workarounds required for JWT limitations.
- Reduces complexity related to key management.
- Avoids vulnerabilities associated with JWT libraries.
- Alternative Solutions: Consider using session mechanisms with redisvalkey for session data storage as a way to optimize performance without adopting JWTs.

## Content (from Notion)

No.

Not satisfied? Fine, fine. I’ll write a longer answer.

Let’s talk about what we’re talking about. JWT stands for JSON Web Tokens, a reasonably well defined standard for authenticated tokens. Specifically they have a header with format information, a payload, and a signature or message authentication code. The core idea is that whoever has the corresponding verification key can verify that the payload is authentic and has not been altered. What they do with that information is up to them.

The JWT spec (RFC 7519) makes suggestions by providing a few well-known registered claim names: issuer, audience, subject, expiration time, etc. A common usage pattern is that, after verifying the authenticity against whatever trust relationship they have with the issuer, the recipient checks whether they are the intended audience (if any is specified) and the expiration time has not yet passed, and then take the subject as an authenticated identity of the bearer of the token.

It’s perfectly designed for bearer token authentication! Or is it? Let me be clear: JWT as authentication tokens are constructed for Google/Facebook scale environments, and absolutely no one who is not Google/Facebook needs to put up with the ensuing tradeoffs. If you process less than 10k requests per second, you’re not Google nor are you Facebook.

The core benefit, proponents will tell you, is that the recipient of a JWT doesn’t need to connect to the user database to verify the token authenticity and render its service. In a large installation, like Google’s, that means that the JWT issuer, the authentication service, can be a dedicated service that is managed and scaled like other services, and is the only service that needs to access the centralized user database. All other services can act on the information stored in the JWT alone, and don’t need to go through the user database, which would represent a choke point.

What about logout/session invalidation? Well, in order for this model to work, the authentication token should have a fairly short lifetime. Maybe 5 minutes, max. The client is also issued a second token, the so-called refresh token, with which it can request a new authentication token from the authentication service. This gives the authentication service a chance to consult the user database to see whether the user or a specific session has been blocked in the meantime.

Here’s the twist that is rarely, if ever, spelled out: In this setup the refresh token, not the authentication token, is the real session token. The refresh token represents the session with the authentication service (which can be revoked), while the authentication tokens are just derived credentials to be used for a few requests at most. The beauty, from Google’s point of view, is that this delegates keeping the session alive to the client, i.e. not Google’s servers. Oh and by the way, the refresh token can be, and usually is, opaque, since it’s only ever consumed by the same service that creates it. That reduces a lot of complexity, by just using an opaque identifier stored in a database.

Now, let’s assume you are not Google. Check which of these apply to you:

- You wanted to implement log-out, so now you’re keeping an allowlist of valid JWTs, or a denylist of revoked JWTs. To check this you hit the database on each request.
- You need to be able to block users entirely, so you check a “user active” flag in the database. You hit the database on each request.
- You need additional relationships between the user object and other objects in the database. You hit the database on each request.
- Your service does anything at all with data in the database. You hit the database on each request.
Congratulations, if you confirmed any of the items above, you don’t need JWTs. You’re hitting the database anyway, and I’m pretty sure that you only have one database which stores both your user profiles and your application data. By just using a “normal” opaque session token and storing it in the database, the same way Google does with the refresh token, and dropping all JWT authentication token nonsense, you stand to reap these great benefits:

- No weird workarounds (allow/denylist) for shortcomings of JWT as authentication token
- Greatly reduced complexity. No need to manage a secure JWT signing/authentication key
- You get to pass on some interesting bugs.
Just use the normal session mechanism that comes with your web framework and that you were using before someone told you that Google uses JWT. It has stood the test of time and is probably fine.

If you need something to do to make you feel like you’re running a big deployment, you can probably configure your session mechanism to use redisvalkey to store the session data. You’re still going to use the authenticated user id to query the database, but for unauthenticated requests it may be faster/use less resources. It might not be. You’ll have to tune and measure that.

This site uses Akismet to reduce spam. Learn how your comment data is processed.


