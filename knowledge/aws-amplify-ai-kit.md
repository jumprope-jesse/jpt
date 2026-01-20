# AWS Amplify AI Kit for Amazon Bedrock

*Source: [AWS What's New](https://aws.amazon.com/about-aws/whats-new/2024/11/aws-amplify-full-stack-ai-kit-amazon-bedrock) - Added: 2026-01-18*

## Overview

The AWS Amplify AI kit enables fullstack JavaScript/TypeScript developers to add AI features (chat, conversational search, summarization) to web apps without ML expertise. Works with React and Next.js.

## Key Features

1. **`<AIConversation>` React Component**
   - Pre-built, customizable chat UI
   - Real-time streaming responses
   - UI responses (not just plain text)
   - Chat history and resumable conversations

2. **Type-safe Bedrock Client**
   - Secure server-side access to Amazon Bedrock
   - Built on Amplify Gen 2 and AWS AppSync

3. **User Context Sharing**
   - Securely share user data with Bedrock models
   - Define tools with additional context for model invocation

## When to Use

- Adding chat/conversational AI to existing React/Next.js apps
- Building AI features without deep ML knowledge
- Need a quick path to production-ready AI chat UI

## Getting Started

```bash
npm install @aws-amplify/ui-react-ai
```

See the [launch blog](https://aws.amazon.com/blogs/mobile/amplify-ai-kit/) for setup details.

## Amplify Gen 2 Developer Experience

*Source: [Reddit discussion](https://www.reddit.com/r/aws/comments/1d4ucxf/aws_amplify_gen2_is_really_good_dx/) - June 2024*

Community feedback on Amplify Gen2 has been positive, particularly around:

- **Improved DX over Gen1** - Significant quality-of-life improvements
- **TypeScript-first approach** - Better type safety throughout the stack
- **CDK integration** - Uses AWS CDK under the hood for infrastructure
- **Simplified data modeling** - Define models in code, get GraphQL/REST APIs generated

Gen2 is a substantial rewrite that addresses many Gen1 pain points. The AI Kit (above) is built on top of Gen2's foundation.

## Related

- `aws-lambda-powertools-bedrock.md` - Backend Lambda integration with Bedrock Agents
- `aws-app-runner.md` - Alternative deployment option for containers
- Amazon Bedrock - The underlying AI model service
