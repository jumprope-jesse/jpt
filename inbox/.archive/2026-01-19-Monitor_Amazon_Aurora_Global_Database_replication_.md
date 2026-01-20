---
type: link
source: notion
url: https://aws.amazon.com/blogs/database/monitor-amazon-aurora-global-database-replication-at-scale-using-amazon-cloudwatch-metrics-insights/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-02-15T15:51:00.000Z
---

# Monitor Amazon Aurora Global Database replication at scale using Amazon CloudWatch Metrics Insights | Amazon Web Services

## AI Summary (from Notion)
- Purpose: The article discusses how to monitor Amazon Aurora Global Database replication using Amazon CloudWatch Metrics Insights.
- Key Features:
- Amazon Aurora is a high-performance, fully managed relational database service compatible with MySQL and PostgreSQL.
- The Global Database feature allows replication across multiple AWS Regions for enhanced disaster recovery.
- Monitoring Replication Lag:
- Monitoring replication lag is crucial for ensuring resilience and adherence to recovery point objectives (RPO).
- Amazon CloudWatch Metrics Insights can be used to set alarms and dashboards for tracking replication lag.
- Implementation Steps:
- Set up Aurora global database replication between Regions.
- Create CloudWatch alarms that trigger notifications based on defined replication lag thresholds.
- Use CloudWatch dashboards for a visual representation of the replication status.
- Best Practices:
- Recommended to create dashboards in the secondary Region of the Aurora global cluster for effective monitoring.
- Prerequisites:
- IAM user with necessary privileges, an Aurora global database setup, and an SNS topic for notifications.
- Walk-through: Detailed steps for creating CloudWatch dashboards and alarms to monitor replication lag effectively.
- Conclusion: Proper monitoring of replication lag enhances data latency management and supports a robust disaster recovery framework.
- Authors: Daxeshkumar Patel and Bhavesh Rathod, both Database Consultants at AWS.

## Content (from Notion)

Amazon Aurora is a high-performance, fully managed relational database service offered by AWS. It is compatible with MySQL and PostgreSQL, providing exceptional scalability, availability, and durability for your data. Amazon Aurora Global Database allows you to replicate up to five different AWS Regions and provides robust disaster recovery capabilities.

To ensure the resilience and recovery point objective (RPO) adherence of your Aurora global database, it’s essential to closely monitor the replication process to track the replication lag. To monitor the replication lag, you can take advantage of Amazon CloudWatch Metrics Insights alarms and dashboards.

Metrics Insights, a feature of Amazon CloudWatch, offers valuable capabilities for monitoring Aurora global database replication. Metrics Insights allows enterprises to better understand replication lag and detect anomalies in replication delays.

In this post, we show you how to use Metrics Insights alarms and dashboards to monitor Aurora global database replication. You can follow along with this video to guide you through the steps:

## Solution overview

The following diagram outlines the monitoring strategy for Aurora global database replication.

The high-level workflow to implement this solution is as follows:

1. Aurora global database replication is set up between two Regions.
1. A CloudWatch alarm triggers when the replication exceeds the defined replication lag thresholds.
1. The alarm sends a notification to Amazon Simple Notification Service (Amazon SNS).
1. Amazon SNS notifies users through email.
1. The CloudWatch dashboard provides users with a detailed view of the Aurora global database for which the CloudWatch alarm has been triggered.
This solution has two main parts: a CloudWatch alarm and a CloudWatch dashboard.

### CloudWatch alarms

Metrics Insights, a feature of Amazon CloudWatch, is a powerful structured query language (SQL) engine that allows you to efficiently query your metrics on a large scale by using a single alarm. With this feature, you can set up a single CloudWatch alarm to monitor all your Aurora global databases replicating from one Region, like us-east-1, to another Region, such as us-west-2. Likewise, you can set up another alarm to monitor replication between different Region pairs, for example, us-east-1 to us-east-2.

With Metrics Insights, we can create an aggregated CloudWatch alarm that consolidates the replication lag metric values of each Aurora global database cluster. This aggregated alarm provides real-time alerts when any database exceeds the defined threshold.

For example, if we have 10 Aurora global clusters, and if any single database cluster exceeds the defined threshold, it will trigger an alert. As the alarm works on an aggregated value, it doesn’t provide specific details such as the database name or ARN. In this post, we guide you through a process of using the CloudWatch dashboard to identify the specific database that has exceeded the defined threshold.

### CloudWatch dashboards

The CloudWatch dashboard solution discussed in this post offers a comprehensive and visual representation of your Aurora global database replication lag. This centralized monitoring solution enables real-time tracking of replication status for multiple databases. The dashboard lists all your Aurora global database clusters by name, allowing you to access cluster names and retrieve any other necessary information, such as the database name. Additionally, we can sort and display these clusters based on their replication lag time in either ascending or descending order.

For best practices in monitoring Aurora global database replication lag, we recommend creating the dashboard in the secondary Region of the Aurora global cluster.

In the following CloudWatch dashboard, the x-axis displays Aurora global database clusters (dbtest1-cluster-1, dbtest2-cluster-1, dbtest3-cluster-1) in descending order of their replication lag time, while the y-axis shows Aurora global database cluster replication lag time in milliseconds. It provides a history for the past hour.

Overall, this comprehensive solution of using a CloudWatch alarm and dashboard provides you with robust monitoring capabilities for Aurora global database replication lag, ensuring the continuous availability and performance of your database environment.

## Prerequisites

Before you get started, make sure you have the following prerequisites:

- An AWS Identity and Access Management (IAM) user with enough privileges for the services used in this solution.
- An Aurora global database. For setup instructions, refer to Getting started with Amazon Aurora global databases.
- Create an SNS topic and subscribe an email address for the CloudWatch alarm to use to send a notification. For setup instructions, refer to Configuring Amazon SNS.
## Walk-through

In this section we show how to create a CloudWatch dashboard and a CloudWatch alarm to implement this solution.

## Create a CloudWatch dashboard

In this post, we create CloudWatch resources while connected to the secondary Region of the Aurora global database cluster, us-east-1 in our example. Note that CloudWatch dashboards are multi-region by design and will be visible from the primary region as well. For more information, refer to Creating a CloudWatch dashboard.

1. On the CloudWatch console, in the navigation pane, choose Dashboards, then choose Create dashboard.
1. In the Create new dashboard dialog box, enter a name for the dashboard, then choose Create dashboard.
1. In the Add widget section, choose Line and choose Metrics for the data source, then choose Next.
1. In the Add metric graph dialog box, on the Query tab, navigate to Metrics Insights – query builder.
1. In the query builder, for Namespace, choose AWS/RDS.
1. For Metric name, choose your metric (for this post, AuroraGlobalDBReplicationLag).
1. For Filter by, choose your source Region (for this post, SourceRegion = us-west-2).
1. For Group by, choose DBClusterIdentifier.
1. For Order by, choose DESC.This displays the Aurora global database cluster names on the dashboard in descending order of their replication lag time.
1. Choose Run, then choose Create widget.
1. Adjust the display time on the dashboard according to your use case and requirements.
1. Choose Save dashboard.
After successfully setting up the dashboard, you should see the Aurora global databases listed on the x-axis. They are arranged in descending or ascending order based on the replication lag time you have selected. By adjusting the time on the dashboard, you can view the corresponding historical data.

## Create a CloudWatch alarm

Complete the following steps to create the CloudWatch alarm in the secondary Region of the Aurora global database cluster. For more information, refer to Create a CloudWatch alarm based on a static threshold.

1. On the CloudWatch console, in the navigation pane, under Alarms, choose All alarms.
1. Choose Create alarm.
1. Choose Select Metric.
1. On the Query tab, navigate to Metrics Insights – query builder.
1. For Namespace, choose AWS/RDS.
1. For Metric name, choose your metric (for this post, we chose AuroraGlobalDBReplicationLag).Different types of Aurora cluster-level metrics are available for monitoring Aurora global database replication. Consider selecting the most suitable metric based on your specific use case to monitor the replication effectively. For example, AuroraGlobalDBReplicationLag measures the replication lag in milliseconds from the primary Region to a secondary Region, while AuroraGlobalDBDataTransferBytes measures the redo log data transferred between the primary and secondary Region.
1. For Filter by, choose your source Region of the Aurora global database cluster (for this post, we chose SourceRegion = us-west-2).
1. Choose Run.
1. Choose Select metric.The Specify metric and conditions page appears, showing a graph and other information.
1. For Period, select the appropriate time period (for this post, we chose 5 minutes).
1. Under Conditions, specify the following: Specify the threshold values based on your specific requirements and the selected metric for your use case. For instance, for the AuroraGlobalDBReplicationLag metric, ensure that the threshold values are set in milliseconds.Choose Additional configuration, in Datapoints to alarm, specify how many evaluation periods (data points) must be in the ALARM state to trigger the alarm (for this post, we keep the default value).For more information, see Evaluating an alarm.For Missing data treatment, choose how to have the alarm behave when some data points are missing (for this post, we keep the default value). For more information, see Configuring how CloudWatch alarms treat missing data.
1. Choose Next.
1. Under Notification, select the SNS topic created in the prerequisites section to notify when the alarm is in ALARM state, then choose Next.
1. Enter a name for the alarm. Within the description, you can include the dashboard’s URL which was created as part of an earlier section of this post. This will enable convenient access to the dashboard immediately upon receiving an email alert via an SNS notification.
1. Choose Next.
1. Under Preview and create, confirm that the information and conditions are what you want, then choose Create alarm.
After setting up the alarm successfully, you will receive an email alert for any Aurora global database that exceeds replication lag thresholds.

If you want to test the alarm, the following example uses the set-alarm-state command to temporarily change the state of an Amazon CloudWatch alarm named myalarm and set it to the ALARM state. For more information, see set-alarm-state

```plain text
aws cloudwatch set-alarm-state --alarm-name "myalarm" --state-value ALARM --state-reason "testing purposes"
```

Since we’ve included the dashboard’s URL in the alarm’s description during its creation, the alerts will contain this URL. Opening the URL takes you to the CloudWatch dashboard, which provides details about the affected Aurora global database. This proactive approach enables efficient monitoring and management of Aurora global database replication lag.

## Clean up

To avoid incurring future charges, delete the resources you created as part of this post:

1. Delete the Aurora global database cluster. For instructions, refer to Deleting Aurora DB clusters and DB instances.
1. Delete the CloudWatch alarm. For instructions, refer to Editing or deleting a CloudWatch alarm.
1. On the CloudWatch console, choose Dashboards in the navigation pane, then select the dashboard you created and choose Delete.
## Conclusion

In this post, we demonstrated how to set up a CloudWatch alarm and CloudWatch dashboard using the capabilities of Metrics Insights, enabling efficient monitoring of Aurora global database replication. Monitoring the replication lag of Aurora global databases provides essential insights to manage data latency, and maintain a robust database disaster recovery framework. This proactive approach enhances overall system resiliency and user experience.

We invite you to leave your feedback in the comments sections.

### About the Authors

Daxeshkumar Patel is a Database Consultant at Professional Services team at Amazon Web Services. He works with customers and partners in their journey to the AWS Cloud with a focus on database migration and modernization programs.

Bhavesh Rathod is a Principal Database Consultant with the Professional Services team at Amazon Web Services. He works as a database migration specialist to help Amazon customers migrate their on-premises database environment to AWS Cloud database solutions.


