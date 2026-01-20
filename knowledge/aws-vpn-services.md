# AWS VPN Services

AWS offers two managed VPN solutions for different connectivity needs.

## AWS Client VPN

OpenVPN-based managed service for remote user access to AWS and on-premises resources.

### Key Features
- **Fully managed** - No hardware or software-based VPN appliances to manage
- **Elastic scaling** - Automatically scales up/down based on concurrent user demand
- **Pay-as-you-go** - No capacity planning required
- **Standard protocols** - OpenVPN-based, works with standard clients

### Use Cases
- Remote workforce accessing AWS VPCs
- Contractors needing temporary access
- Users accessing both AWS and on-premises resources

### Integration Points
- **MDM integration** - Can reject devices not compliant with security policies
- **Authentication** - Supports Active Directory, SAML-based IdP, certificate-based auth
- **Split-tunnel** - Route only specific traffic through VPN

### Migration Path
AWS Verified Access is the newer zero-trust alternative that eliminates VPN for HTTP/HTTPS apps. See `aws-verified-access.md` for migration patterns.

## AWS Site-to-Site VPN

IPsec VPN connections between on-premises networks/data centers and AWS VPCs.

### Key Features
- **Secure tunnels** - IPsec encryption for data center to AWS connectivity
- **High availability** - Dual tunnels to two VPN endpoints for redundancy
- **Accelerated option** - Uses AWS Global Accelerator for improved performance
  - Better throughput for globally distributed applications
  - Reduces jitter and packet loss
  - Consistent network experience across regions

### Use Cases
- Hybrid cloud architectures
- Branch office connectivity to AWS
- Disaster recovery site connections
- Migration workloads (moving data to AWS)

### vs. Direct Connect
- **Site-to-Site VPN**: Internet-based, quick setup, moderate bandwidth, variable latency
- **Direct Connect**: Dedicated fiber, consistent performance, higher bandwidth, longer setup time
- Can combine both for redundancy

## Pricing Model

### Client VPN
- Per-endpoint-association hour
- Per-connection hour (active user connections)

### Site-to-Site VPN
- Per-VPN-connection hour
- Data transfer out charges (standard AWS rates)
- Accelerated VPN: Additional hourly charge for Global Accelerator

## Common Patterns

### Hybrid Access
Client VPN users can access both:
- Resources in AWS VPCs
- On-premises resources (via Site-to-Site VPN or Direct Connect from VPC)

### Multi-Region
- Client VPN endpoints are regional
- Can set up endpoints in multiple regions for geographic redundancy
- Users connect to nearest endpoint

## Related Services
- **AWS Verified Access** - Zero-trust alternative to Client VPN for HTTP/HTTPS apps
- **AWS Direct Connect** - Dedicated network connection (not VPN)
- **Transit Gateway** - Hub for connecting multiple VPCs and on-premises networks
- **VPN CloudHub** - Multiple Site-to-Site VPN connections with routing between sites

## Links
- [Client VPN Workshop](https://catalog.workshops.aws/client-vpn)
- [AWS VPN Overview](https://aws.amazon.com/vpn/)
