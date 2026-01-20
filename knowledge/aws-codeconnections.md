# AWS CodeConnections

AWS CodeConnections enables connecting AWS services (like CodePipeline) to external code repositories.

## Overview

- Each connection is a resource with a unique ARN
- Connections can be shared across multiple AWS services
- Previously named "AWS CodeStar Connections" (resources with `codestar-connections` namespace still supported)

## Supported Providers

**Cloud providers:**
- Bitbucket Cloud
- GitHub
- GitHub Enterprise Cloud
- GitLab.com

**Installed providers (require host resource):**
- GitHub Enterprise Server
- GitLab self-managed

## Connection States

- **Pending** - Newly created, awaiting OAuth handshake
- **Available** - Ready to use with AWS services
- **Error** - Setup failed

## Key Concepts

### Global Resources
Connections are replicated across all AWS regions. The ARN includes the region where created, but the resource works globally. Host resources are NOT global - they only work in the region where created.

### Setup Workflow
1. Install AWS authentication app on third-party account
2. Create connection (via console, CLI, SDK, or CloudFormation)
3. Complete OAuth handshake to move from Pending → Available
4. For installed providers: create host resource first

### Hosts
Required only for installed provider types (GitHub Enterprise Server, GitLab self-managed). Hosts have Pending or Available states.

## API

Uses the AWS CodeConnections API reference. Key operations:
- `CreateConnection`
- `CreateHost` (for installed providers)

## Integration Points

Works with:
- AWS CodePipeline
- AWS CodeBuild
- Other Developer Tools services

## Regional Considerations

Europe (Milan) region requires installing a region-specific app from the third-party provider site. This is separate from the app used for other regions.

## Links

- [AWS Documentation](https://docs.aws.amazon.com/dtconsole/latest/userguide/welcome-connections.html)
