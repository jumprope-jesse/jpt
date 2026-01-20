# AWS Verified Access

Zero-trust network access service that provides secure application access without VPN.

## What It Does

- Evaluates each application request in real-time against security requirements
- Grants access based on user identity AND device trust level
- Eliminates need for VPN while maintaining security posture

## Key Concepts

### Trust Providers
- Identity providers (AWS IAM Identity Center, third-party OIDC/SAML)
- Device management services (CrowdStrike, Jamf, etc.)
- Verified Access uses data from these to make access decisions

### Policies
- Cedar-based policies define who can access what
- Evaluated per-request, not just at login time
- Can combine identity claims with device posture

### Architecture
- Verified Access endpoints front your applications
- Traffic flows: User -> Verified Access -> Application (in VPC)
- Works with ALB, NLB, or network interfaces

## Benefits

1. **Better security** - Zero-trust means no lateral movement after compromise
2. **No VPN** - Users access apps directly, reducing support burden
3. **Granular control** - Per-application policies vs. network-level VPN rules
4. **Audit trail** - All access attempts logged for compliance

## Pricing

- Hourly charge per application endpoint
- Data processing charge per GB

## Use Cases

- Remote workforce accessing internal apps
- Contractor access with device compliance requirements
- Replacing legacy VPN infrastructure
- Apps requiring different trust levels (some need MFA + managed device, others just identity)

## Migration from Client VPN

AWS Client VPN (OpenVPN-based, 2018) and Verified Access (Zero Trust, 2023) can coexist during migration.

### Migration Stages

1. **Client VPN Only** - Apps behind private ALBs, accessible only via VPN
2. **Hybrid** - New apps on Verified Access, existing apps on VPN
3. **Gradual Migration** - Move existing apps one by one to Verified Access
4. **Verified Access Only** - Remove Client VPN infrastructure

### Key Configuration for Coexistence

**Client VPN Settings:**
- **Enable split-tunnel** - Only VPN-destined traffic goes through tunnel; Verified Access traffic goes direct
- **Custom DNS** - If using private hosted zones, need Route 53 Resolver inbound endpoint

**DNS Setup (when using both):**
- Create CNAME in **public hosted zone** pointing to Verified Access endpoint
- If using custom DNS on VPN, also create matching CNAME in **private hosted zone**
- Clients resolve app FQDNs to Verified Access endpoints whether on or off VPN

### Per-App Migration Steps

1. Create Verified Access endpoint for the app (specify DNS name + ACM cert)
2. Add CNAME in public hosted zone -> Verified Access endpoint
3. If custom DNS on VPN: add CNAME in private hosted zone too
4. (Optional) Lower TTL before DNS changes for faster rollback

### Current Limitations

- **HTTP/HTTPS only** - Non-HTTP protocols (SSH, etc.) still need VPN
- **Internal load balancers only** - Must use internal ALB/NLB, not internet-facing
- **No IPv6** - Verified Access doesn't support IPv6 traffic yet

### When to Keep Client VPN

- Applications using non-HTTP protocols
- Security requirements mandating VPN for specific workloads
- Backup connectivity method

## Links

- [AWS Docs](https://docs.aws.amazon.com/verified-access/latest/ug/what-is-verified-access.html)
- [Migration Patterns Blog Post](https://aws.amazon.com/blogs/networking-and-content-delivery/aws-client-vpn-and-aws-verified-access-migration-and-interoperability-patterns/)
- [Verified Access Workshop](https://catalog.workshops.aws/verified-access)
- [Client VPN Workshop](https://catalog.workshops.aws/client-vpn)
