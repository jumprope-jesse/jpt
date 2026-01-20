# Tailscale Security Audit - 2026-01-18

Audit performed with [Tailsnitch](https://github.com/Adversis/tailsnitch).

## Summary

| Severity | Count |
|----------|-------|
| Critical | 1 |
| High | 1 |
| Medium | 2 |
| Low | 2 |
| Info | 16 |
| **Total** | **22** |

## Critical & High Priority Findings

### CRITICAL: Default 'allow all' policy active (ACL-001)
The ACL has a wildcard rule `src=[*] dst=[*:*]` allowing unrestricted access between all devices.

**Remediation:** Define explicit ACL rules following least privilege. Remove `src: ["*"]` and `dst: ["*:*"]` rules.
- [Admin Console](https://login.tailscale.com/admin/acls/visual/general-access-rules)
- [ACL Samples](https://tailscale.com/kb/1192/acl-samples)

### HIGH: Funnel exposes services to public internet (NET-001)
Funnel is enabled for `autogroup:member`, exposing services publicly.

**Remediation:** Restrict Funnel to specific users/tags. Ensure only intended services are exposed.
- [Funnel Docs](https://tailscale.com/kb/1223/funnel)

## Medium Priority Findings

### Outdated Tailscale clients (DEV-003)
7 devices running outdated clients (8-62 minor versions behind):
- `jumper-pro`: 1.32.2 (60 versions behind)
- `old-jrservices-dev`: 1.30.0 (62 versions behind)
- `jrdev-east-2`: 1.42.0 (50 versions behind)
- `jesse-c9-al2023`: 1.58.2 (34 versions behind)
- `jrdev`: 1.60.1 (32 versions behind)
- `jumper-15`: 1.80.2 (12 versions behind)
- `jesse-c9-ubuntu20-dev`: 1.84.0 (8 versions behind)

**Note:** 2 devices are older than v1.34 and cannot generate network flow logs.

### Stale devices (DEV-004)
7 devices not seen in 60+ days:
- `old-jrservices-dev`: 1234 days ago
- `jumper-pro`: 1161 days ago
- `jrdev-east-2`: 945 days ago
- `jesse-c9-al2023`: 676 days ago
- `jrdev`: 615 days ago
- `jumper-15`: 312 days ago
- `jesse-c9-ubuntu20-dev`: 63 days ago

**Remediation:** Review and remove unused devices at [Machines](https://login.tailscale.com/admin/machines).

## Low Priority Findings

- **ACL-003:** No ACL tests defined - add tests to prevent accidental permission changes
- **DEV-013:** 1 device (`jrdev`) has key expiry disabled

## Recommended Actions

1. **Immediate:** Replace default 'allow all' ACL with explicit rules
2. **This week:** Remove 7 stale devices that haven't been seen in 60+ days
3. **This week:** Review Funnel configuration and restrict if not needed
4. **Ongoing:** Update outdated Tailscale clients, enable auto-updates
5. **Consider:** Enable Tailnet Lock, add ACL tests, configure groups

## Files

- Full JSON report: `audits/tailscale-audit-2026-01-18.json`
