# Tailscale Security Auditing

## Tailsnitch

**Repo:** https://github.com/Adversis/tailsnitch

A security auditor for Tailscale configurations that scans your tailnet for 50+ misconfigurations, overly permissive access controls, and security best practice violations.

### Key Features

- **52 security checks** across 7 categories (access controls, authentication, device security, network exposure, SSH, logging)
- **Interactive fix mode** - remediate issues directly via Tailscale API
- **SOC 2 evidence export** - generates reports with Common Criteria (CC) control mappings
- **CI/CD integration** - catch security regressions in pipelines
- **Ignore file support** - suppress known-accepted risks via `.tailsnitch-ignore`

### Quick Start

```bash
# Install
go install github.com/Adversis/tailsnitch@latest

# Set credentials (OAuth preferred)
export TS_OAUTH_CLIENT_ID="..."
export TS_OAUTH_CLIENT_SECRET="tskey-client-..."

# Or use API key
export TSKEY="tskey-api-..."

# Run audit
tailsnitch

# High severity only
tailsnitch --severity high

# Interactive fix mode
tailsnitch --fix
```

### Authentication Options

**OAuth (Recommended)** - Scoped, auditable access that doesn't expire when employees leave.
- Create at: https://login.tailscale.com/admin/settings/oauth
- Required scopes: `all:read` or individually: `policy_file:read`, `devices:core:read`, `dns:read`, `auth_keys:read`
- Fix mode needs: `devices:core`, `auth_keys`

**API Key** - Inherits creating user's permissions.
- Create at: https://login.tailscale.com/admin/settings/keys

### Critical Checks Include

- Default 'allow all' policy detection
- Tailnet lock not enabled
- Reusable auth keys
- Stale/inactive devices
- Overly permissive ACLs

### SOC 2 Evidence

```bash
tailsnitch --soc2 json > soc2-evidence.json
tailsnitch --soc2 csv > soc2-evidence.csv
```

Includes per-resource test results, CC code mappings (CC6.1, CC6.2, etc.), pass/fail status, and timestamps.

### CI/CD Example

```yaml
- name: Audit Tailscale Security
  env:
    TS_OAUTH_CLIENT_ID: ${{ secrets.TS_OAUTH_CLIENT_ID }}
    TS_OAUTH_CLIENT_SECRET: ${{ secrets.TS_OAUTH_CLIENT_SECRET }}
  run: |
    tailsnitch --json > audit.json
    if tailsnitch --severity high --json | jq -e '.summary.critical + .summary.high > 0' > /dev/null; then
      echo "Critical or high severity issues found!"
      exit 1
    fi
```
