# GitHub Actions Runners

## Alternative Runner Providers

### Blacksmith (blacksmith.sh)
Third-party GitHub Actions runner service offering faster, cheaper CI/CD.

**Key claims:**
- Up to 2x faster than GitHub-hosted runners (uses high-performance gaming CPUs)
- Over 50% cheaper than GitHub
- Unlimited concurrency
- One-line code change to migrate (`runs-on: ubuntu-latest` → Blacksmith equivalent)

**Features:**
- **Docker builds**: 40x faster with NVMe-backed cache for layer persistence
- **Colocated cache**: 4x faster test setup (drop-in replacement for `actions/cache`)
- **Instant provisioning**: No "Waiting for a runner" delays
- **CI analytics**: Out-of-the-box performance and cost monitoring

**Custom Actions:**
```yaml
# Docker builds
- uses: useblacksmith/build-push-action@v1  # replaces docker/build-push-action@v3

# Caching
- uses: useblacksmith/cache@v5  # replaces actions/cache@v3
```

**Security:**
- SOC2 Type 2 and GDPR compliant
- No access to GitHub secrets
- Single-use GitHub access tokens per job
- Isolated, ephemeral VMs per job execution

**Pricing:** 3,000 free minutes/month, no credit card required

**Source:** https://www.blacksmith.sh/ (saved 2025-05-14)

## Considerations

When evaluating third-party runners:
- Vendor lock-in through custom actions (cache, docker build)
- Data residency and security compliance needs
- Support responsiveness for production issues
- Migration path back to GitHub-hosted if needed
