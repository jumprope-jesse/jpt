# Aurora Global Database Monitoring with CloudWatch Metrics Insights

*Source: https://aws.amazon.com/blogs/database/monitor-amazon-aurora-global-database-replication-at-scale-using-amazon-cloudwatch-metrics-insights/ - Added: 2026-01-19*

## What It Is

Comprehensive monitoring solution for Aurora Global Database replication lag using CloudWatch Metrics Insights. Allows monitoring multiple global database clusters across regions with a single alarm.

## The Problem

Aurora Global Databases replicate across up to 5 AWS regions for disaster recovery. To ensure resilience and meet RPO (Recovery Point Objective), you need to monitor replication lag across all these databases. Traditional alarms require one per database - doesn't scale.

## The Solution: Metrics Insights

CloudWatch Metrics Insights is a SQL-like query engine that enables:
- **Single alarm for multiple databases**: Monitor all Aurora global databases replicating from one region (e.g., us-east-1 → us-west-2) with one aggregated alarm
- **Threshold-based alerts**: Triggers when ANY database exceeds defined lag threshold
- **Visual dashboard**: Sorted view of all databases by replication lag

## Architecture

1. Aurora Global Database replication between two regions
2. CloudWatch Metrics Insights alarm monitors aggregated replication lag
3. Alarm triggers → SNS → Email notification
4. CloudWatch dashboard provides detailed view showing which specific database triggered alarm

## Key Metrics

- **AuroraGlobalDBReplicationLag**: Replication lag in milliseconds from primary to secondary region
- **AuroraGlobalDBDataTransferBytes**: Redo log data transferred between regions

Choose metric based on your use case.

## Implementation Pattern

### CloudWatch Dashboard

Create in **secondary region** (best practice):

```sql
-- Metrics Insights query
Namespace: AWS/RDS
Metric: AuroraGlobalDBReplicationLag
Filter by: SourceRegion = us-west-2
Group by: DBClusterIdentifier
Order by: DESC  -- Shows worst offenders first
```

Dashboard shows:
- X-axis: Database cluster names sorted by lag
- Y-axis: Replication lag in milliseconds
- Adjustable time window for historical view

### CloudWatch Alarm

Single alarm for all databases in a region pair:

```
Metric: AuroraGlobalDBReplicationLag (aggregated)
Filter: SourceRegion = us-west-2
Period: 5 minutes
Threshold: Set in milliseconds based on your RPO
```

**Limitation**: Aggregated alarm doesn't show which specific database exceeded threshold - that's why you need the dashboard.

**Pro tip**: Include dashboard URL in alarm description so email alerts link directly to troubleshooting view.

## Testing Alarms

```bash
# Temporarily set alarm to ALARM state for testing
aws cloudwatch set-alarm-state \
  --alarm-name "myalarm" \
  --state-value ALARM \
  --state-reason "testing purposes"
```

## Configuration Details

### Alarm Evaluation
- **Datapoints to alarm**: How many evaluation periods must breach before triggering
- **Missing data treatment**: How to handle gaps in metrics
- **Period**: Evaluation interval (e.g., 5 minutes)

### Dashboard Best Practices
- Create in **secondary region** of global cluster
- Dashboards are multi-region visible by default
- Adjust time window based on your monitoring needs
- Sort DESC to see problematic databases first

## Prerequisites

1. IAM user with CloudWatch, RDS, SNS privileges
2. Aurora Global Database setup
3. SNS topic with email subscription for notifications

## When to Use This

- Running Aurora Global Databases across multiple regions
- Need to monitor replication lag at scale (multiple database clusters)
- Want centralized monitoring with minimal alarm sprawl
- Building disaster recovery dashboards for operations teams

## Related

- See `aws-cloudwatch-application-signals.md` for application-level monitoring
- See `aws-aurora-database-activity-streams.md` for Aurora security monitoring
- See `wide-events-observability.md` for structured logging patterns

## The Value Proposition

Instead of:
- 10 databases × 2 region pairs = 20 individual alarms
- No visibility into which database is problematic without diving into metrics

You get:
- 1 alarm per region pair (2 total)
- Dashboard showing all databases sorted by lag
- Email alerts with direct link to troubleshooting view
- SQL-like queries for flexible metric aggregation

Scales from 1 database to hundreds without alarm proliferation.
