# AWS Break Glass Procedures for Small Teams

*Source: [r/aws discussion](https://www.reddit.com/r/aws/comments/1ay4025/aws_management_break_glass_procedure/) - Added: 2026-01-19*

Strategies for solo DevOps or small teams to handle AWS incidents when the primary person is unavailable.

## The Problem

Solo DevOps at small startups face a real risk: if an incident happens while you're asleep or unreachable, there's no one to respond. Even simple fixes like rebooting a server require someone with AWS access and knowledge.

## Options for Emergency Coverage

### 1. AWS Managed Services Provider (MSP)

AWS Partner Network has certified MSPs who offer 24/7 monitoring and incident response:
- Can be granted emergency access via IAM roles
- SNS topic integration for automated alerting
- Handle basic troubleshooting (reboots, scaling, health checks)
- Some offer "break glass" only contracts (emergency-only access)

**Considerations:**
- Cost varies widely ($500-5000+/month depending on scope)
- Onboarding time to document your infrastructure
- Need clear runbooks for common issues

### 2. AWS Infrastructure Event Management (IEM)

AWS offers IEM as a paid service (typically part of Enterprise Support):
- Proactive monitoring during critical events
- AWS Solution Architects on standby
- Good for planned high-traffic events, less for 24/7 coverage

### 3. Automated Self-Healing

Reduce the need for human intervention:
- **Auto Scaling groups** - instances recreate automatically
- **ECS/Fargate** - container orchestration handles failures
- **Lambda** - serverless means fewer servers to manage
- **RDS Multi-AZ** - automatic database failover
- **Route 53 health checks** - automatic DNS failover

### 4. Peer Support Network

Informal arrangements with other solo DevOps:
- Exchange AWS access and runbooks
- Share on-call responsibilities
- Works well for simple "reboot the server" scenarios
- Legal/trust considerations with credentials

### 5. Documented Runbooks + Non-Technical Backup

Train a co-founder or team member on basic recovery:
- Step-by-step AWS Console instructions with screenshots
- Cover 80% of incidents (reboots, scaling, rollbacks)
- Keep runbooks in shared location (not on the infrastructure itself)

## SNS-Based Alerting Setup

For any break glass solution, set up automated notifications:

```
CloudWatch Alarm → SNS Topic → Multiple Destinations
                              ├── Your phone (SMS)
                              ├── Your email
                              ├── PagerDuty/Opsgenie
                              └── MSP/backup contact
```

Key alarms to set up:
- Instance health checks (EC2 StatusCheckFailed)
- Target group unhealthy hosts (ALB/NLB)
- RDS/Aurora replication lag or connection failures
- 5xx error rate spikes (ALB)
- CPU/memory thresholds

## Risk vs. Control Trade-off

Outsourcing incident response means:
- **Benefit:** Coverage when you're unavailable
- **Risk:** Third party has access to your infrastructure
- **Mitigation:** Use assume-role with MFA, time-limited credentials, detailed CloudTrail logging

## For Startups: Pragmatic Approach

1. **Automate first** - Most common failures should self-heal
2. **Document** - Create runbooks even if you don't outsource
3. **Start small** - Begin with monitoring-only service, add response later
4. **Plan for growth** - What works at 10K customers won't at 100K

## Related

- See `aws-resiliency-patterns.md` for architecture patterns that reduce incident frequency
- AWS Well-Architected Framework - Reliability Pillar
- AWS Managed Services: https://aws.amazon.com/managed-services/
