# AWS Secrets Manager Agent

Local HTTP service for reading and caching secrets from AWS Secrets Manager in compute environments.

## What It Does

- Provides standardized secrets access across Lambda, ECS, EKS, EC2
- Caches secrets in memory (reduces API calls to Secrets Manager)
- Read-only - cannot modify secrets
- Protects against SSRF with required token header

## Key Configuration

| Setting | Default | Range | Notes |
|---------|---------|-------|-------|
| `http_port` | 2773 | 1024-65535 | Local endpoint port |
| `ttl_seconds` | 300 | 1-3600 | Cache TTL |
| `cache_size` | 1000 | 0-1000 | 0 = no caching |
| `max_conn` | 800 | 1-1000 | Max HTTP client connections |

Config via TOML file: `./aws-secrets-manager-agent --config config.toml`

## Usage

Requires SSRF token header for all requests:

```bash
curl -H "X-Aws-Parameters-Secrets-Token: $(</var/run/awssmatoken)" \
  'http://localhost:2773/secretsmanager/get?secretId=my-secret'
```

```python
import requests

with open('/var/run/awssmatoken') as fp:
    token = fp.read()

response = requests.get(
    "http://localhost:2773/secretsmanager/get?secretId=my-secret",
    headers={"X-Aws-Parameters-Secrets-Token": token.strip()}
)
secret = response.text
```

## Required IAM Permissions

- `secretsmanager:DescribeSecret`
- `secretsmanager:GetSecretValue`

## Security Considerations

- Secrets are NOT encrypted in cache
- Anyone with access to compute environment + SSRF token can read cached secrets
- Domain of trust = wherever agent endpoint and token are accessible
- For security-conscious apps not already using an agent pattern, prefer language-specific SDKs

## Installation Options

- Docker sidecar container
- Lambda extension (via layer)
- ECS/EKS sidecar
- Direct install on EC2

## Logging

- Local only: `logs/secrets_manager_agent.log`
- Max 10 MB per file, 5 files retained
- Does NOT log to CloudWatch/CloudTrail (agent requests)
- Calls from agent TO Secrets Manager do appear in CloudTrail

## Source

https://github.com/aws/aws-secretsmanager-agent
