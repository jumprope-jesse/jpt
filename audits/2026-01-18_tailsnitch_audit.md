# Tailsnitch Security Audit - 2026-01-18

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

### [CRITICAL] ACL-001: Default 'allow all' policy active

The ACL has a wildcard rule allowing unrestricted access:
- `src=[*] dst=[*:*]`

**Remediation:** Define explicit ACL rules following least privilege. Remove `src: ["*"]` or `dst: ["*:*"]` rules.

**Action URL:** https://login.tailscale.com/admin/acls/visual/general-access-rules

---

### [HIGH] NET-001: Funnel exposes services to public internet

Funnel is enabled for `autogroup:member`, exposing services to the public internet.

**Remediation:** Restrict Funnel to specific users/tags. Review `nodeAttrs` for funnel attribute.

**Action URL:** https://login.tailscale.com/admin/acls

---

## Medium Priority Findings

### [MEDIUM] DEV-003: Outdated Tailscale clients (7 devices)

Devices with significantly outdated clients:
- `jumper-pro`: 60 minor versions behind (1.32.2)
- `old-jrservices-dev`: 62 minor versions behind (1.30.0)
- `jrdev-east-2`: 50 minor versions behind (1.42.0)
- `jesse-c9-al2023`: 34 minor versions behind (1.58.2)
- `jrdev`: 32 minor versions behind (1.60.1)
- `jumper-15`: 12 minor versions behind (1.80.2)
- `jesse-c9-ubuntu20-dev`: 8 minor versions behind (1.84.0)

Note: 2 devices running < v1.34 cannot generate network flow logs.

### [MEDIUM] DEV-004: Stale devices (7 devices not seen in 60+ days)

| Device | Last Seen |
|--------|-----------|
| old-jrservices-dev | 1234 days ago |
| jumper-pro | 1161 days ago |
| jrdev-east-2 | 945 days ago |
| jesse-c9-al2023 | 676 days ago |
| jrdev | 615 days ago |
| jumper-15 | 312 days ago |
| jesse-c9-ubuntu20-dev | 63 days ago |

**Recommendation:** Remove unused devices to reduce attack surface.

---

## Low Priority Findings

- **ACL-003:** No ACL tests defined - add tests to catch accidental permission changes
- **DEV-013:** `jrdev.tailnet-5165.ts.net` has key expiry disabled

---

## Recommended Actions

1. **Immediate:** Replace default `allow all` ACL with explicit rules
2. **Immediate:** Review Funnel configuration - restrict if not needed
3. **Short-term:** Remove 7 stale devices (especially those not seen in 1+ years)
4. **Short-term:** Update outdated Tailscale clients
5. **Medium-term:** Add ACL tests, define user groups, enable session recording

---

*Audit performed with tailsnitch v.dev*
*Full JSON report: `audits/2026-01-18_tailsnitch_audit.json`*
