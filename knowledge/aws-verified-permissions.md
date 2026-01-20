# AWS Verified Permissions

Fine-grained authorization service for applications using Cedar policy language.

## Core Concept

Instead of implementing permissions in application code, define them as Cedar policies. Call Verified Permissions to authorize access to APIs and resources.

## Cognito Integration (May 2024)

- Authorize using OIDC tokens from Amazon Cognito
- Write Cedar policies based on Cognito group memberships
- `IsAuthorizedWithToken` API evaluates Cedar policies against token claims

## Batch Authorization

`batchIsAuthorizedWithToken` API - multiple authorization requests in a single call.

**Use cases:**
- Determine which action buttons to enable on a page
- Filter which resources to display in a list
- Reduce latency and cost for permission-heavy UIs

**Pricing:** Based on API calls, not number of requests batched within each call.

## Links

- [API Reference](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/)
- [Pricing](https://aws.amazon.com/verified-permissions/pricing/)
