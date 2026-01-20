# Tailsnitch Security Audit Report
**Date:** 2026-01-18
**Tailnet:** jesse's home network

## Summary
| Severity | Count |
|----------|-------|
| Critical | 1 |
| High | 1 |
| Medium | 2 |
| Low | 2 |
| Info | 16 |
| **Total** | **22** |

## Critical Issues

### ACL-001: Default 'allow all' policy active
Your ACL has `src=[*] dst=[*:*]` - any device can reach any other device on any port. This is the most permissive (and risky) configuration.

**Fix:** Define explicit ACL rules following least privilege. Example:
```json
{
  "acls": [
    {"action": "accept", "src": ["group:admins"], "dst": ["*:*"]},
    {"action": "accept", "src": ["autogroup:member"], "dst": ["tag:servers:22,443"]}
  ]
}
```

## High Issues

### NET-001: Funnel exposes services to public internet
Funnel is enabled for `autogroup:member`, meaning any member can expose services publicly.

**Fix:** Restrict Funnel to specific users or tags in nodeAttrs.

## Medium Issues

### DEV-003: Outdated Tailscale clients (7 devices)
Several devices are 30-60+ minor versions behind:
- `jumper-pro`: v1.32.2 (60 versions behind)
- `old-jrservices-dev`: v1.30.0 (62 versions behind)
- `jrdev-east-2`: v1.42.0 (50 versions behind)

### DEV-004: Stale devices (7 devices)
Devices not seen in 60+ days:
- `jumper-pro`: 1161 days (3+ years!)
- `old-jrservices-dev`: 1234 days
- `jrdev-east-2`: 945 days

**Recommendation:** Remove these stale AWS dev instances.

## Low Issues

### ACL-003: No ACL tests defined
Add tests to validate your ACL changes don't accidentally break access.

### DEV-013: Key expiry disabled
`jrdev.tailnet-5165.ts.net` has key expiry disabled (never re-authenticates).

## Recommendations (Priority Order)

1. **Remove stale devices** - 7 devices haven't been seen in months/years
2. **Tighten ACLs** - Replace `*:*` with explicit rules
3. **Restrict Funnel** - Limit who can expose services publicly
4. **Update clients** - Enable auto-updates
5. **Add ACL tests** - Prevent accidental misconfigurations
