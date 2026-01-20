# AWS Lambda Secrets Management Guide

Comprehensive comparison of secret storage options for Lambda functions.

## Options at a Glance

| Option | Cost | Security | Rotation | Latency |
|--------|------|----------|----------|---------|
| **Environment Variables** | Free | Basic (encrypted at rest) | Manual redeploy | ~25ms cold start |
| **Parameter Store (Standard)** | Free (<40 req/s) | Good | Manual | ~217ms cold, ~39ms warm |
| **Parameter Store (Advanced)** | $0.05/mo/param | Good | TTL policies | Same as Standard |
| **Secrets Manager** | $0.40/mo/secret | Best | Auto-rotation | ~177ms cold, ~29ms warm |
| **KMS Direct** | $1/mo/key | Good | DIY | ~64ms cold, ~6ms warm |

API calls: $0.03/10k (KMS), $0.05/10k (Parameter Store, Secrets Manager)

## Environment Variables

**Pros:**
- Fastest option (minimal cold start overhead)
- Free, no additional services
- Encrypted at rest by Lambda

**Cons:**
- Visible in console via `GetFunctionConfiguration`
- Exposed in CloudFormation templates
- No individual secret auditing in CloudTrail (all decrypted together)
- 4KB total limit

**Best for:** Low-risk secrets like telemetry API keys with small blast radius

## Parameter Store

**Standard vs Advanced:**
- Standard: 4KB, 10k params/region, free storage, free <40 req/s
- Advanced: 8KB, 100k params/region, $0.05/mo, TTL policies, cross-account sharing

**Best for:** Shared secrets that may need updating without redeploy

```python
# With AWS Lambda Powertools
from aws_lambda_powertools.utilities import parameters
value = parameters.get_parameter("/my/secret", decrypt=True)
```

## Secrets Manager

**Unique Features:**
- Automatic rotation on schedule
- Cross-region replication
- 65KB max secret size
- Native CloudTrail auditing

**Best for:** PCI-DSS/HIPAA compliance, secrets requiring rotation

## KMS Direct

Best performance for static secrets. Use envelope encryption for multiple secrets:

1. Create KMS key
2. Generate AES key per application
3. Encrypt secrets with AES key
4. Encrypt AES key with KMS key
5. Store encrypted blob in Lambda (env var, zip, or S3)

**Best for:** Large static secrets like PEM files, signing keys

## Recommended Patterns

### Secure Environment Variables

Use CloudFormation dynamic references to avoid plaintext in templates:

```yaml
Environment:
  Variables:
    MY_SECRET: '{{resolve:ssm-secure:/my/secret:1}}'
```

Secret stored in Parameter Store, resolved at deploy time, never visible in CloudFormation.

### Decision Framework

| Secret Type | Blast Radius | Recommended Storage |
|-------------|--------------|---------------------|
| Telemetry API key | Small (write-only) | Environment variable |
| DB credentials (shared) | Medium | Parameter Store |
| GitHub App private key | Large (repo access) | Parameter Store or KMS |
| Regulated credentials | Compliance req | Secrets Manager |

## Performance Notes

- Cold connection includes TCP setup (~100ms overhead)
- KMS direct is fastest because ciphertext already present locally
- Lambda Parameters/Secrets Extension caches values but isn't open source

## Best Practices

1. Never hardcode plaintext secrets in code/source control
2. Principle of least privilege - limit secret access to runtime only
3. One secret per application/stack when possible (limits blast radius)
4. Use dynamic references in CloudFormation
5. Deny `lambda:GetFunctionConfiguration` from console users if concerned about visibility

## Source

AJ Stuyvenberg (March 2024): https://aaronstuyvenberg.com/posts/ultimate-lambda-secrets-guide
