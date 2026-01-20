# Tailscale Security Audit Report
**Date:** 2026-01-18
**Tool:** tailsnitch
**Tailnet:** tailnet-5165.ts.net

## Summary

| Severity | Count |
|----------|-------|
| Critical | 1 |
| High | 1 |
| Medium | 2 |
| Low | 2 |
| Info | 16 |
| **Total** | **22** |

---

## Critical Issues

### ACL-001: Default 'allow all' policy active
**Category:** Access Controls

Your ACL has a wildcard rule `src=[*] dst=[*:*]` that allows any device to access any other device on any port. This is the #1 security issue to fix.

**Fix:** Replace with explicit rules. Example:
```json
{
  "action": "accept",
  "src": ["group:home-users"],
  "dst": ["tag:server:22,443"]
}
```

**Admin URL:** https://login.tailscale.com/admin/acls/visual/general-access-rules

---

## High Severity Issues

### NET-001: Funnel exposes services to public internet
**Category:** Network Exposure

Funnel is enabled for `autogroup:member`, allowing any member to expose services to the public internet.

**Fix:** Restrict Funnel to specific users/tags who actually need it.

**Admin URL:** https://login.tailscale.com/admin/acls

---

## Medium Severity Issues

### DEV-003: Outdated Tailscale clients (7 devices)
Devices running very old versions (some 50-62 minor versions behind):

| Device | Version | Behind |
|--------|---------|--------|
| old-jrservices-dev | 1.30.0 | 62 versions |
| jumper-pro | 1.32.2 | 60 versions |
| jrdev-east-2 | 1.42.0 | 50 versions |
| jesse-c9-al2023 | 1.58.2 | 34 versions |
| jrdev | 1.60.1 | 32 versions |
| jumper-15 | 1.80.2 | 12 versions |
| jesse-c9-ubuntu20-dev | 1.84.0 | 8 versions |

**Expected version:** 1.92.5

### DEV-004: Stale devices not seen recently (7 devices)
These devices haven't connected in 60+ days:

| Device | Last Seen |
|--------|-----------|
| old-jrservices-dev | 1234 days ago |
| jumper-pro | 1161 days ago |
| jrdev-east-2 | 945 days ago |
| jesse-c9-al2023 | 676 days ago |
| jrdev | 615 days ago |
| jumper-15 | 312 days ago |
| jesse-c9-ubuntu20-dev | 63 days ago |

**Recommendation:** Remove devices that are no longer in use.

---

## Low Severity Issues

### ACL-003: No ACL tests defined
Add tests to catch accidental policy changes:
```json
"tests": [
  {"src": "jesse@jumpro.pe", "accept": ["server:22"]},
  {"src": "jesse@jumpro.pe", "deny": ["prod-db:5432"]}
]
```

### DEV-013: User device with key expiry disabled
`jrdev.tailnet-5165.ts.net` has key expiry disabled and never requires re-authentication.

---

## Info Items (16)

- LOG-001: Network flow logs disabled (Premium/Enterprise feature)
- LOG-002: Log streaming not configured
- LOG-005: Webhook secrets never expire
- LOG-006: OAuth clients persist after user removal
- LOG-007: SCIM API keys never expire
- LOG-008: No passkey-authenticated backup admin
- LOG-011: No security contact email configured
- LOG-012: Webhooks for critical events not configured
- USER-001: User roles should be reviewed periodically
- DEV-006: 1 external (shared) device in tailnet (hello.ts.net)
- DEV-009: Device approval configuration should be verified
- DEV-010: Tailnet Lock not enabled
- DEV-013: Device posture not configured (Enterprise feature)
- SSH-001: SSH session recording not enforced
- SSH-004: 1 SSH rule configured (check mode)
- ACL-008: No groups defined in ACL policy

---

## Recommended Actions (Priority Order)

1. **Fix ACL wildcard rule** - Replace `src=[*] dst=[*:*]` with specific rules
2. **Remove stale devices** - 7 devices haven't been seen in months/years
3. **Restrict Funnel access** - Limit who can expose services publicly
4. **Update old clients** - Enable auto-updates for remaining devices
5. **Add ACL tests** - Catch accidental policy changes
6. **Define groups** - Makes ACL management easier

---

## Raw JSON Output
See: audits/tailsnitch-2026-01-18.json
