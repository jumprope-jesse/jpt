# AWS App Runner

Fully managed service for deploying containerized web applications and APIs with minimal configuration. Positioned as a simpler alternative to ECS Fargate.

## Key Features

- **Simple deployment**: CLI command or console, provide ECR image URL or GitHub repo
- **Auto-scaling**: Scales based on traffic automatically
- **Built-in**: SSL, load balancing, health checks, networking
- **HTTPS endpoint**: Get a URL immediately, can add custom domains later

## Sources

1. **Container Registry** (ECR): Push Docker image, App Runner pulls it
2. **Source Code** (GitHub): Connect repo, provide build/start commands, App Runner builds and deploys

## Pricing

Pay-as-you-go model:
- Charged for memory and CPU consumed
- When no requests, CPU is idle (not charged), memory still reserved
- Additional charges for deployment triggers and build times
- ~$5/month for small app with test traffic

## Deployment via ECR

```bash
# Authenticate Docker to ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <account>.dkr.ecr.<region>.amazonaws.com

# Build, tag, and push
docker build -t myapi .
docker tag myapi:latest <account>.dkr.ecr.<region>.amazonaws.com/myapi:latest
docker push <account>.dkr.ecr.<region>.amazonaws.com/myapi:latest
```

## Deployment via GitHub

Build settings for .NET 6 example:
- **Runtime**: .NET 6
- **Build command**: `dotnet publish -c Release -o release`
- **Start command**: `dotnet release/MyApp.dll --urls=http://0.0.0.0:80`
- **Port**: 80

Automatic deployment triggers on push to branch.

## Auto-Scaling Configuration

Set concurrency threshold (e.g., 5 requests per instance). App Runner spins up new instances when exceeded. No downtime during deployments - new containers come up before old ones go down.

## When to Use

**Good fit:**
- Small to mid-load applications
- Simple web APIs
- Rapid prototyping to production
- When you want minimal infrastructure configuration

**Not ideal:**
- Complex architectures needing fine-grained control
- Very high-scale applications where ECS/EKS flexibility matters

## Region Availability

Not available in all regions (e.g., ap-south as of 2023). Check availability before planning.

## Health Checks

Configurable at intervals using HTTP or TCP protocols.

## ECR Repository Strategy

**One ECR repo per service/Lambda** is the recommended pattern. Each App Runner service or Lambda function should have its own dedicated ECR repository. This allows:
- Independent versioning and deployment
- Clear tagging (`:latest` always points to current version for that service)
- Simpler IAM policies per service
- Cleaner rollback strategy

For a typical setup (3 App Runner services + several Lambdas), create separate repos like:
- `myapp-frontend`
- `myapp-api-1`
- `myapp-api-2`
- `myapp-lambda-processor`
- etc.

## Base Images

**For Lambda:**
AWS provides purpose-built base images in the public ECR gallery. Use them over standard images because they include:
- Lambda Runtime Interface Client (RIC) - handles Lambda invoke events
- Lambda Runtime Interface Emulator (RIE) - for local testing
- Optimized cold start performance
- Proper signal handling for Lambda lifecycle

Find them at: `public.ecr.aws/lambda/dotnet` or `public.ecr.aws/lambda/nodejs`

**For App Runner:**
No AWS-specific base images exist. Use standard images:
- .NET: `mcr.microsoft.com/dotnet/aspnet:8.0` (or appropriate version)
- Node.js: `node:20-alpine` or `node:20-slim`

App Runner doesn't need special runtime interfaces - it just runs your container and routes HTTP traffic to it.

## Reference

- Pricing: https://aws.amazon.com/apprunner/pricing/
- Example repo: https://github.com/iammukeshm/deploying-aspnet-core-webapi-to-aws-apprunner
- Lambda base images: https://gallery.ecr.aws/lambda
