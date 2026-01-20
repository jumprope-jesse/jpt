---
type: link
source: notion
url: https://github.com/mdivani/better-auth-serverless
notion_type: Software Repo
tags: ['Running']
created: 2025-07-27T12:22:00.000Z
---

# GitHub - mdivani/better-auth-serverless: Better Auth/Express template served as aws lambda proxy, with basic lambda authorizer configured

## Overview (from Notion)
- Embracing serverless architecture can significantly reduce operational overhead, allowing you to focus on building features that matter to your users and family.
- The integration of BetterAuth with AWS Lambda offers a scalable solution for managing authentication, which can be a game-changer for startups looking to streamline their processes.
- The ability to customize and extend services like BetterAuth means you can tailor solutions to fit your unique needs, reflecting a hands-on approach to problem-solving that can inspire your kids.
- Living in New York City, leveraging tech innovations like these can keep you at the forefront of industry trends, helping you make informed decisions as a founder.
- Consider the environmental impact of tech choices; serverless solutions may offer efficiency that aligns with sustainable practices.
- Engaging in the developer community around projects like this can introduce you to valuable networking opportunities that benefit both your career and personal growth.
- The flexibility of working with these technologies can provide more time for family, as you can deploy and manage applications more efficiently from anywhere.

## AI Summary (from Notion)
A serverless authentication service using BetterAuth, Express.js, and AWS Lambda, featuring a custom Lambda authorizer for API Gateway. It includes setup instructions, architecture details, API endpoints for authentication, and options for extending functionality with custom routes and database models. Key prerequisites include Node.js, Yarn, PostgreSQL, and an AWS account.

## Content (from Notion)

# Auth Service

A serverless authentication service built with BetterAuth, Express.js, and AWS Lambda. This service provides scalable authentication with a custom Lambda authorizer for API Gateway.

## Stack

- AWS Lambda - Serverless compute
- Express.js - Web framework
- BetterAuth - Authentication library
- Prisma - PostgreSQL ORM
- Serverless Framework v4 - Deployment
- Node.js 22 - Runtime
## Quick Start

### Prerequisites

- Node.js 22+
- Yarn 4+ (corepack enable)
- PostgreSQL database
- AWS account (for deployment)
### Setup

1.  
1.  
1.  
1.  
The service will be available at http://localhost:3000/auth/

## Architecture

```plain text
API Gateway → Lambda Authorizer → Lambda Function → Express.js → BetterAuth → PostgreSQL

```

### Custom Lambda Authorizer

The service includes a custom Lambda authorizer (src/functions/auth/authorizer/handler.ts) that validates JWT tokens from BetterAuth for API Gateway requests.

## Deployment

### Local Development

```plain text
yarn start
```

### AWS Deployment

```plain text
yarn deploy
yarn deploy --stage prod
```

## Configuration

### BetterAuth Setup

Edit src/lib/auth.ts to configure authentication options. For detailed BetterAuth configuration options, see the official documentation.

### Environment Variables

## API Endpoints

BetterAuth automatically generates authentication endpoints:

- POST /auth/signin - Sign in
- POST /auth/signup - Sign up
- POST /auth/signout - Sign out
- GET /auth/session - Get session
- POST /auth/verify-email - Verify email
- GET /auth/oauth/{provider} - OAuth flow
- POST /auth/forgot-password - Password reset
- POST /auth/2fa/enable - Enable 2FA
## Extending

### Custom Routes

Add new Lambda functions in src/functions/ and register them in serverless.ts.

### BetterAuth Extensions

This service can be extended according to the BetterAuth documentation. Add custom plugins, hooks, and configurations in src/lib/auth.ts.

### Database Extensions

Add custom models to prisma/schema.prisma and run yarn migrate:dev.

## Testing

```plain text
yarn test
yarn test:watch
```

## Scripts

- yarn start - Start development server
- yarn deploy - Deploy to AWS
- yarn test - Run tests
- yarn migrate:dev - Run database migrations
- yarn lint - Lint code
- yarn format - Format code
## License

ISC License


