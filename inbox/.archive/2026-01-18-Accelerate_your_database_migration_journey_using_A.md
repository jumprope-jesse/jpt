---
type: link
source: notion
url: https://aws.amazon.com/blogs/database/accelerate-your-database-migration-journey-using-aws-dms-schema-conversion/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-04-01T16:23:00.000Z
---

# Accelerate your database migration journey using AWS DMS Schema Conversion | Amazon Web Services

## AI Summary (from Notion)
- Overview of AWS DMS Schema Conversion (DMS SC): A tool designed to facilitate database migrations to AWS by supporting both homogeneous and heterogeneous migrations.
- Key Features:
- Converts and migrates database and code objects directly from the AWS DMS console.
- Currently supports Oracle and SQL Server as source databases and various AWS services as targets.
- Future updates will include more supported source and target platforms.

- Migration Process:
- Involves setting up prerequisites such as network configuration, storing database credentials in AWS Secrets Manager, and creating an Amazon S3 bucket for storing conversion metadata.
- Requires the creation of IAM roles for accessing AWS resources.

- Architecture:
- DMS SC assesses and converts database objects, generating an assessment summary and detailed actions for objects that require manual intervention.
- The migration project is serverless, with AWS DMS provisioning cloud resources automatically.

- Assessment and Conversion:
- Users can generate assessment reports to understand the migration effort and identify action items for unconverted objects.
- The conversion process involves selecting objects to convert, saving converted code, and applying changes directly to the target database.

- Monitoring and Cleanup:
- Progress of the migration can be monitored using Amazon CloudWatch for error tracking and diagnostics.
- Cleanup involves deleting migration projects, instance profiles, data providers, and associated S3 buckets to free resources.

- Authors:
- Contributions from Nelly Susanto, a Senior Database Migration Specialist, and Amit Arora, a Solutions Architect at AWS, highlighting their expertise in database migration and cloud solutions.

## Content (from Notion)

AWS Database Migration Service (AWS DMS) helps you accelerate your database migrations to AWS. It supports both homogeneous and heterogeneous migrations. Previously, you had to download the AWS Schema Conversion Tool (AWS SCT) to assess and convert your schema and code objects. Now, with AWS DMS Schema Conversion (DMS SC), you can assess, convert, and migrate your database and code objects from the AWS DMS console. As of this writing, DMS SC supports Oracle and SQL Server source databases, as well as Amazon Relational Database Service (Amazon RDS), Amazon Aurora, and Amazon Redshift target databases. More source and target platforms will be available in the future. For more information, refer to the complete list of supported sources and targets.

In this post, we demonstrate how to use DMS SC to convert an Amazon RDS for SQL Server database to Amazon Aurora PostgreSQL-Compatible Edition. We walk you through the setup and configuration of DMS SC, the assessment and conversion process, and how to find information if your conversion runs into an issue.

## Solution overview

DMS SC assesses and converts your database objects. It generates an assessment summary, an estimate of the level of effort, and detailed actions for objects that can’t be automatically converted. For heterogeneous migration, DMS SC attempts to convert schema and code objects to the syntax of the target engine. If no direct conversion is possible, it lists options to remediate.

The following architecture diagram shows how you can use DMS SC to assess and convert database objects from an RDS for SQL Server database to Amazon Aurora PostgreSQL.

The DMS SC configuration process includes the following high-level steps:

1. Prepare DMS SC
1. Generate and view the assessment report
1. Convert database objects
1. Monitor the migration project in DMS SC
## Prerequisites

In this section, we discuss the prerequisite steps you must complete before implementing this solution.

### Set up the network for DMS Schema Conversion

DMS SC provisions schema conversion resources in a VPC and subnet that you specify. You must set up connectivity to your source and target databases. Network configuration depends on where your source and target databases are located. The RDS for SQL Server and Aurora PostgreSQL databases used in this post are on the same VPC. We provision DMS SC in the same VPC and add an ingress rule to the security groups to allow inbound connections from DMS SC to Amazon RDS for SQL Server and Amazon Aurora PostgreSQL. To learn more about other network configurations, refer to Setting up a network for DMS Schema Conversion.

### Store database credentials in AWS Secrets Manager

DMS SC uses secrets stored in AWS Secrets Manager to connect to your database. For instructions to add source and target credentials to Secrets Manager, refer to Store database credentials in AWS Secrets Manager.

### Create an Amazon S3 bucket

DMS SC saves items such as assessment reports, converted SQL code, and information about database schema objects in an Amazon Simple Storage Service (Amazon S3) bucket. Create an S3 bucket called dms-sc-demo with the following steps:

1. On the Amazon S3 console, choose Buckets in the navigation pane.
1. Choose Create bucket.
1. Name the bucket dms-sc-demo.
1. For AWS Region, choose the AWS Region where you are planning to launch DMS SC.
1. Choose Enable for Bucket Versioning.
1. Create the bucket.
### Create IAM roles

DMS SC uses AWS Identity and Access Management (IAM) roles to access Amazon S3 and the database credentials stored in Secrets Manager. For this post, we create two roles.

First, create the role sc-s3-role for DMS SC to access the S3 bucket with the following steps:

1. On the IAM console, choose Roles in the navigation pane.
1. Choose Create role.
1. For Trusted entity type, select AWS service.
1. For Service or use case, choose DMS.
1. Choose Next.
1. On the Add permissions page, select the policy AmazonS3FullAccess. DMS SC uses an S3 bucket to store artifacts such as database schema and code objects, assessment reports, and converted SQL code.
1. Choose Next.
1. For Role name, enter sc-s3-role.
1. Choose Create role.
1. On the sc-s3-role page, choose the Trust relationships tab. This will delegate access and allow the DMS service to perform actions on the S3 bucket.
1. Choose Edit trust policy.
1. Edit the trust relationships for the role to use the schema-conversion.dms.amazonaws.com service principal as the trusted entity.
1. Edit the trust policy for the role you created to include the Region name in the AWS DMS principal, for example dms.us-east-1.amazonaws.com, where us-east-1 is the Region where DMS SC will launch.
1. Choose Update policy.  Next, you create the role sc-secrets-manager-role for DMS SC to access Secrets Manager.
1. Choose Roles in the navigation pane.
1. Choose Create role.
1. For Trusted entity type, select AWS service.
1. For Service or use case, choose DMS.
1. For Use case, select DMS.
1. Choose Next.
1. On the Add permissions page, select the policy SecretsManagerReadWrite.
1. Choose Next.
1. For Role name, enter sc-secrets-manager-role.
1. Choose Create role.
1. The AWS DMS regional service principal has the format dms.region-name.amazonaws.com. Edit the trust policy for the role you created to include the Region name in the AWS DMS principal and add trust relationships for the role to use schema-conversion.dms.amazonaws.com.
With the prerequisites complete, you’re now ready to set up the solution.

## Prepare DMS Schema Conversion

In this section, we go through the steps to configure DMS SC.

### Set up an instance profile

An instance profile specifies the network, security, and Amazon S3 settings for DMS SC to use. Create an instance profile with the following steps:

1. On the AWS DMS console, choose Instance profiles in the navigation pane.
1. Choose Create instance profile.
1. For Name, enter a name (for example, dms-sc-profile).
1. For Network type, in this demo we will use IPv4. DMS SC has another option called Dual-Stack mode, which supports both IPv4 and IPv6.
1. For Virtual private cloud (VPC) for IPv4, choose Default VPC.
1. For Subnet group, choose your subnet group (for this post, dms-sc-subnet).
1. For VPC security groups, choose your security groups.
base

1. Specify the S3 bucket to store schema conversion metadata.
1. Create your instance profile.
### Add data providers

Data providers store database types and information about source and target databases for DMS SC to connect to. Configure data providers for the source and target databases with the following steps:

1. On the AWS DMS console, choose Data providers in the navigation pane.
1. Choose Create data provider.
1. To create your target, for Name, enter a name (for example, Aurora-PostgreSQL).
1. For Engine type¸ choose Amazon Aurora PostgreSQL.
1. For Engine configuration, select RDS database instance.
1. For Database from RDS, enter the IP address.
1. For Port, enter the port number.
1. For Database name¸ enter the name of your database.
1. Repeat similar steps to create your source data provider.
### Create a migration project

A DMS SC migration project defines migration entities, including instance profiles, source and target data providers, and migration rules. Create a migration project with the following steps:

1. On the AWS DMS console, choose Migration projects in the navigation pane.
1. Choose Create migration project.
1. For Name, enter a name to identify your migration project (for example, dmasc-demo).
1. For Instance profile, choose the instance profile you created.
1. In the Data providers section, enter the source and target data providers, Secrets Manager secret, and IAM roles.
1. In the Schema conversion settings section, enter the S3 URI and choose the applicable IAM role.
1. Choose Create migration project.
## Generate and view the assessment report

In this section, you generate and view the assessment report.

### Launch DMS Schema Conversion

The migration project in DMS SC is serverless. AWS DMS automatically provisions the cloud resources for your migration projects, connects to the source and target databases, and fetches source and target database metadata. We use the AdventureWorks database from Microsoft throughout this post.

Launch DMS SC with the following steps:

1. On the AWS DMS console, choose Migration projects in the navigation pane.
1. Choose the migration project you created.
1. On the Schema conversion tab, choose Launch schema conversion.
The schema conversion project will be ready when the launch is complete. The left navigation tree represents the source database, and the right navigation tree represents the target database.

### Generate the assessment report

Generate an assessment report with the following steps:

1. Select the database or schema in the source data provider that you would like to assess.
1. Choose Actions under Source data providers and choose Assess.
### View the assessment report

When the assessment is complete, the assessment report is accessible in the middle pane. DMS SC provides a high-level overview of the migration effort; the Action items tab provides details on specific actions and recommendations for unconverted objects.

You can export these reports to share or view on other devices outside of DMS SC. You can export a detailed report in CSV format and the summary report in PDF format.

The location of the S3 bucket to which the assessment report will be exported is displayed in a pop-up confirmation message, as seen in the following screenshot.

## Convert database objects

Select the objects you want to convert, and then choose Convert on the Actions menu to convert the source objects to the target database.

This opens up a modal window confirming your request to convert the schema. For example, it displays a message to confirm whether you would like to convert the Person schema in the AdventureWorks2019 database to Amazon Aurora PostgreSQL.

The conversion process may take some time depending on the number and complexity of the selected objects. When it’s complete, the middle pane displays information on the auto-conversion as well as any action items requiring manual resolution.

You can save the converted code to the S3 bucket that you created earlier in the prerequisite steps. To save the SQL scripts, select the object in the target database tree. Choose Save as SQL on the Actions menu.

A dialog box appears confirming your selection, along with S3 bucket details.

As a next step, download the .zip SQL file created in the previous step and validate the scripts. Look at the action items for each object in the DMS SC middle pane and perform manual updates as needed.

After you finalize the scripts, run them manually in the target database.

Alternatively, you can apply the scripts directly to the database using DMS SC. Select the specific schema in the target database, and on the Actions menu, choose Apply changes.

This will apply the auto-converted code to the target database. For objects that require action items, DMS SC flags them and provides details of action items in the middle pane.

For the items that require resolution, perform manual changes and apply the converted changes directly to the target database.

## Monitor the migration project in DMS SC

If you have a large database to convert or need to drill down into issues that might arise during the conversion, you can monitor the progress of the migration project in DMS SC by using Amazon CloudWatch. The first step is to find the ARN of the DMS SC migration project and then find all the logs in the CloudWatch log groups.

You can see the log group with a name similar to dms-tasks-sct-xxxx.

When you run DMS SC, it creates multiple logs in CloudWatch, which provide details regarding the progress of the conversion, including any errors like connection failures, and more. The following screenshot shows four different types of logs generated in CloudWatch that can help you monitor conversion operations.

You can find the details of any issues by searching for keywords like Failed or Error and taking corrective actions based on the error details.

## Clean up

When you’re done with the migration, you can perform a cleanup to free up resources. Complete the following steps:

1. On the AWS DMS console, choose Migration projects in the navigation pane.
1. Select the migration project you created and choose Delete.
1. Choose Instance profiles in the navigation pane.
1. Select the instance profile you created and choose Delete.
1. Choose Data providers in the navigation pane.
1. Select the data providers you created and choose Delete.
1. On the Amazon S3 console, delete the bucket where the migration files were saved.
## Conclusion

With DMS Schema Conversion, you can plan, assess, convert, and migrate your database under a centralized DMS. In this post, we walked through how to prepare DMS SC, create migration projects, generate and view assessment reports, and convert schema objects.

To learn more, refer to Converting database schemas using DMS Schema Conversion.

### About the Authors

Nelly Susanto is a Senior Database Migration Specialist at AWS Database Migration Accelerator. She has over 10 years of technical experience focusing on migrating and replicating databases and data warehouse workloads. She is passionate about helping customers on their cloud journey.

Amit Arora is a Solutions Architect with a focus on database and analytics at AWS. He works with our financial technology and global energy customers and AWS certified partners to provide technical assistance and design customer solutions on cloud migration projects, helping customers migrate and modernize their existing databases to the AWS Cloud.


