# AWS Application Recovery Controller (ARC) Region Switch

Multi-region application recovery service for orchestrating AWS Region failovers.

## What It Does

- Centralized solution to coordinate and automate recovery tasks across AWS services when switching operations between Regions
- Automates the complex coordination of compute, databases, DNS, and other services during failover
- Built on a Regional data plane architecture - executes from the Region being activated (no dependency on impacted Region)

## Key Components

### Recovery Plans
Define specific steps to switch application between Regions. Plans contain execution blocks for actions on AWS resources.

### Supported Execution Blocks (9 types at launch)
1. **ARC Region switch plan** - Orchestrate order of multiple application switches by referencing other plans
2. **EC2 Auto Scaling** - Scale EC2 in target Region to match percentage of source capacity
3. **ARC routing controls** - Change routing control states to redirect traffic via DNS health checks
4. **Aurora global database** - Failover (potential data loss) or switchover (zero data loss)
5. **Manual approval** - Checkpoint for team review before proceeding
6. **Custom Action Lambda** - Execute Lambda functions in either Region
7. **Route 53 health check** - Update health check state to redirect traffic based on DNS config
8. **EKS resource scaling** - Scale Kubernetes pods to match percentage of source capacity
9. **ECS resource scaling** - Scale ECS tasks to match percentage of source capacity

### Continuous Validation
- Validates plans every 30 minutes
- Checks resource configurations and IAM permissions
- Identifies potential issues before actual failover

### Triggers
- Alarm-based (CloudWatch alarms)
- Manual triggers

## Architecture Approaches

- **Active/Passive**: Two replicas, traffic to active only; passive activated via Region switch
- **Active/Active**: Both Regions serving traffic

## Pricing

- **$70/month per plan**
- Each plan supports up to 100 execution blocks
- Parent plans can orchestrate up to 25 child plans

## CLI Example

```bash
aws arc-region-switch start-plan-execution \
  --plan-arn arn:aws:arc-region-switch::111122223333:plan/resource-id \
  --target-region us-west-2 \
  --action activate
```

## Best Practices

- Regularly test recovery plans (untested plans cannot be truly validated)
- Maintain appropriate Service Quotas in standby Regions
- Consider scaling beyond 100% for critical apps expecting surge traffic during recovery
- Use JSON workflow definitions for IaC/source control integration
- Cross-account resource support via IAM roles (executionRole, crossAccountRole)

## Availability

Available in all commercial AWS Regions.

## Source

https://aws.amazon.com/blogs/aws/introducing-amazon-application-recovery-controller-region-switch-a-multi-region-application-recovery-service/
