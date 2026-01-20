---
type: link
source: notion
url: https://aws.amazon.com/blogs/database/securely-connect-to-amazon-rds-for-postgresql-with-aws-session-manager-and-iam-authentication/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-06-24T04:04:00.000Z
---

# Securely connect to Amazon RDS for PostgreSQL with AWS Session Manager and IAM authentication | AWS Database Blog

## Overview (from Notion)
- The approach of using AWS Session Manager for secure database connections can simplify your life by reducing the complexity of managing multiple credentials and access points, making it easier to focus on your work and family.
- Leveraging IAM authentication enhances security, protecting sensitive data—crucial for any software engineer or company founder concerned about data integrity.
- The ability to connect to your database without exposing it to the public internet minimizes security risks, especially relevant for a business operating in the bustling tech landscape of New York City.
- This method promotes centralized management, which can simplify compliance and auditing, valuable for a founder navigating regulatory landscapes.
- Unique perspective: Embracing cloud technologies and modern security practices can set your business apart in a competitive market, helping create a reputation for reliability and innovation.
- Alternate view: Some might argue that traditional methods, like using bastion hosts, offer more control; however, the increased maintenance and security risks often outweigh these benefits.

## AI Summary (from Notion)
This article explains how to securely connect to Amazon RDS for PostgreSQL using AWS Session Manager and IAM authentication. It highlights the limitations of traditional methods like bastion hosts, which expose systems to security risks. By leveraging IAM Database Authentication and Session Manager, users can manage access without needing separate database credentials, enhancing security and simplifying compliance. The article provides detailed steps for setting up the connection, including creating security groups, IAM roles, and using port forwarding to connect securely to the RDS instance.

## Content (from Notion)

Company policies usually do not allow database instances to have a public endpoint unless there is a specific business requirement. Although that protects those resources from public access over the internet, it also limits how users can connect to them from their computers.

Frequently, database administrators and development teams try to overcome that restriction by using a bastion host that can receive requests over the internet and securely forward them to a database hosted in private subnets.

However, that approach has two big downsides:

- Increases the potential attack surface for malicious activities when a server is exposed to the public internet
- Introduces the need to store and maintain SSH keys
Additionally, database users have also to carry the burden of managing usernames and passwords for database authentication, which also increases the security risk exposure.

In this post, we walk you through a solution that offers several advantages over traditional database connection methods, bringing also enhanced security and simplified network and access management.

We will outline the necessary steps for connecting from your local machine to your Amazon Relational Database Service (Amazon RDS) instance by using Session Manager with port forwarding to a remote host, a capability of AWS Systems Manager, and AWS Identity and Access Management (IAM) authentication.

## Prerequisites

For this post, we use a terminal window to initiate the remote sessions.

You must have the following tools and services:

- The AWS Command Line Interface (AWS CLI)
- Access to the AWS Management Console
- The Session Manager plugin installed locally on your desktop or laptop
- Depending on which DB engine you choose, you need one of the following clients: MySQL (for MySQL and MariaDB) or psql (PostgreSQL)
- An IAM user with programmatic access to your AWS account
- An existing VPC via Amazon Virtual Private Cloud (Amazon VPC) with private subnets
- An existing RDS instance and DB security group (in this post, we use Amazon RDS for PostgreSQL, but the solution works for the other RDS engines as well)
- Access to Systems Manager
- VPC endpoints configured for the Systems Manager API calls (for more information, refer to Create VPC endpoints)
## Benefits of using IAM Database Authentication and Session Manager

By leveraging IAM Database Authentication, end-users can connect to your database using IAM entities, rather than separate database credentials. This means you can manage access to your Amazon RDS resources using IAM policies and granting or revoking permissions for specific users or groups as needed, without having to modify database-level user accounts or passwords. This flexibility is especially valuable in dynamic environments where access requirements change frequently. With Session Manager, a fully managed AWS service that helps providing instance management without the need to open any inbound ports, you can establish a secure connection to your RDS instance without exposing it directly to the public internet.

Session Manager with port forwarding allows you to create a secure connection, encrypting the traffic between your local machine and the RDS instance. This reduces your database’s attack surface, and helps preventing unauthorized access to it.

Another advantage of using IAM authentication and Session Manager is the centralized management and auditability it offers. IAM authentication allows you to have a central IAM user or role management system, enabling to easily manage and audit user access to your RDS databases. You can track who and when the database has been accessed and what actions have been performed.

Session Manager also provides you with the ability to audit session activity in your AWS account.

This centralized approach enhances security and simplifies compliance requirements.

## How to connect to your RDS instance with Session Manager

As a best practice for security at the network level, we recommend launching your RDS instances in private subnets and allow access only from the applications within the same VPC or a different VPC.

In order to allow user access to these restricted resources, it is required to have a bastion host through which the users connect to access the database. However, granting access to these bastion hosts sometimes requires exposing them directly to the internet, as they need to be placed on a public subnet, or complex network topologies so that the traffic can be routed from on premises, using services like AWS Direct Connect or a VPN.

Session Manager with remote port forwarding removes the need for a direct connection to the bastion host or to the database, while keeping the security aspects intact.

The following diagram explains the components involved in the architecture and the necessary steps to establish the connection.

The different stages of the workflow are as follows:

1. Start a Session Manager session to one of the Amazon Elastic Compute Cloud (Amazon EC2) Systems Manager managed instances by using the AWS-StartPortForwardingSessionToRemoteHost Systems Manager document and the AWS credentials owned by the user.
1. The SSM agent running on the SSM managed instances processes the user’s request from Systems Manager. That communication is possible via the SSM VPC endpoints configured for that purpose.
1. The port forwarding is established and the user can now open a new terminal and send any commands to the remote host through the established tunnel.
1. The user calls Amazon RDS to generate a database authentication token using its IAM credentials.
1. The user connects to the database through the tunnel using the database authentication token previously generated by Amazon RDS.
## Initial setup

In this section, we walk you through the initial setup steps.

### Create the security group for the EC2 instance

To create your security group, complete the following steps:

1. On the Amazon EC2 console, choose Security groups in the navigation panel.
1. Choose Create security group.
1. Enter a name and description for your security group.
1. For VPC, enter your VPC.
1. In order for the EC2 instance to communicate with the SSM VPC endpoint interfaces, it’s also necessary to enable the outbound traffic from port 443 (HTTPS). In both rules, add as a destination your VPC CIDR range.
1. Choose Create security group.
### Create the IAM role for the EC2 instance

Now we create the IAM role for the EC2 instance:

1. On the IAM console, choose Roles in the navigation panel.
1. Choose Create role.
1. Select AWS service for Trusted entity type.
1. Choose EC2 for Common use cases.
1. Choose Next.
1. In the Add permissions section, select the policy AmazonSSMManagedInstanceCore.
1. Choose Next.
1. Enter a name for the role, a short description, and if necessary, add any required tags. In this post we will use EC2-RDS-AccessRole as a role name.
1. Choose Create role.
### Create the EC2 instance (bastion host)

To provision your EC2 instance, complete the following steps:

1. On the Amazon EC2 console, choose Launch instances in the navigation panel.
1. Enter a name and any required tags for you EC2 instance.
1. Choose the latest Amazon Linux AMI.
1. Choose an instance type (for example, a t3.micro instance class).
1. Choose Proceed without a key pair. Because we’re using Session Manager to handle the connection, we don’t need to create or use an existing key pair.
1. For Network Settings, choose one of the private subnets configured in your Amazon Virtual Private Cloud (VPC).
1. For Auto-assign public IP, choose Disable.
1. For Security groups, choose the security group you created.
1. In the Advanced details section, for IAM instance profile, choose the IAM role created earlier, EC2-RDS-AccessRole.
1. Proceed now with the creation of your instance by choosing Launch instance.
If everything was successful and all the requirements were satisfied, the newly launched instance will appear under Managed Instances (Fleet Manager) and will be ready to be used with Systems Manager.

## IAM database authentication

To set up IAM database authentication in your RDS for PostgreSQL database using IAM roles, follow these steps:

1. Enable IAM DB authentication on the RDS for PostgreSQL instance.
1. Create a database user account that will be used to connect to the DB instance using IAM database authentication. Make sure that the database user (in the example, db_user) is granted with the rds_iam role as shown in the following code:   
1. On the IAM console, in the left navigation panel, choose Policies.
1. Choose Create policy.
1. In the Policy editor, on the JSON tab, enter the following JSON document:   
1. Choose Review policy and enter a name for the policy, for example, rds-db-iam.
1. You can optionally enter a description.
1. Choose Create policy.
1. Choose the name of the IAM user or role to which you would like to attach the policy.
1. Select Add permissions and then Attach existing policies directly.
1. Search for the IAM policy that was just created and select the policy.
1. Choose Next: Review.
1. Make sure that the policy is correct and choose Add permissions.
1. Generate an IAM authentication token using the AWS CLI:   
Because the authentication token consists of several hundred characters and it can be cumbersome on the command line, it’s recommended to save it to an environment variable, and use that variable later when connecting to the database.

The following example shows how to generate a DB authentication token for the database user db_user and store it in a PGPASSWORD environment variable. The PGPASSWORD variable will behave the same as the password connection parameter.

```plain text
export RDSHOST="rdspostgres.123456789012.eu-central-1.rds.amazonaws.com"
export PGPASSWORD="$(aws rds generate-db-auth-token --hostname $RDSHOST --port 5432 --region eu-central-1 --username db_user)"
```

After you generate an authentication token, it is valid for 15 minutes before it expires. If you try to connect to your database using an expired token, the connection request is denied. Note that the DB authentication token is only required to establish the connection to your database and does not determine, in any case, how long the existing connection can last for.

## Create a remote port forwarding session

In this section, we create a Systems Manager port forwarding session to a remote host using Systems Manager and connect to the RDS for PostgreSQL instance.

1. Open a terminal in your computer, and make sure your AWS credentials are valid and you can access your AWS account.
1. Update your /etc/hosts to resolve your $RDSHOST to 127.0.0.1: 
1. Create a remote port forwarding Systems Manager session to the RDS database using the EC2 instance (bastion host) deployed before. In the following example, we reuse the RDSHOST environment variable created in the earlier section. The localPortNumber represents the local port on the client where the traffic should be redirected, such as 1053:   
## Connect to your RDS for PostgreSQL database instance with IAM authentication

To connect to your RDS for PostgreSQL database instance through the port forwarding session created in the previous section, you must have the psql command line tool installed in your computer.

Additionally, when you connect to your PostgreSQL DB instance over SSL, it’s necessary to download an SSL certificate. See Using SSL/TLS to encrypt a connection to a DB instance for more details.

After your certificate has been downloaded to your computer, you can reference it using the sslrootcert parameter from your psql command line tool.

You can now connect to your PostgreSQL DB instance using TLS with psql by following these steps:

1. Open a new terminal in your computer and make sure that your AWS credentials are valid and you can access your AWS account.
1. Connect now to your PostgreSQL DB instance over SSL by running the following command:   
Note that if TLS certificate verification is enabled, then the TLS certificate includes the DB instance endpoint as the Common Name (CN) for the TLS certificate to protect against spoofing attacks. That is the reason why, when connecting with your psql command line tool through the port forwarding session, you have to use the RDS DB instance endpoint as a host, instead of localhost, otherwise the SSL verification will fail.

```plain text
psql: error: connection to server at "localhost" (::1), port 1053 failed: Connection refused
Is the server running on that host and accepting TCP/IP connections?
connection to server at "localhost" (127.0.0.1), port 1053 failed: server certificate for "rdspostgres.123456789012.eu-central-1.rds.amazonaws.com" does not match host name "localhost"
```

If the connection to your PostgreSQL DB instance using IAM authentication has been successful, you should see the following prompt:

```plain text
psql (14.7 (Homebrew), server 14.6)
SSL connection (protocol: TLSv1.2, cipher: ECDHE-RSA-AES256-GCM-SHA384, bits: 256, compression: off)
Type "help" for help.

postgres=>
```

## Clean up unneeded resources

To prevent unwanted charges to your AWS account, make sure to delete any EC2 instances you launched to walk through this example. Also remove both, the EC2 instance’s security group and IAM role created during the initial setup steps.

To terminate an instance (console)

1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
1. In the navigation panel, choose Instances.
1. Select the check box for your SSM managed instance.
1. Choose Instance state, and then Terminate instance.
1. Choose Terminate to confirm the deletion.
To delete a security group (console)

1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
1. In the navigation panel, choose Security Groups.
1. Select the security group created in the steps above and choose Actions and Delete security groups.
1. Choose Delete when prompted for confirmation.
To delete an IAM role (console)

1. Open the Amazon IAM console at https://console.aws.amazon.com/iam/.
1. In the navigation panel, choose Roles, and then select the check box next to the role name that you want to delete (in our example above EC2-RDS-AccessRole).
1. Choose Delete at the top of the page.
1. In the confirmation dialog box, enter the role name in the text input field, and choose Delete.
## Conclusion

In this post, we showed how to connect to RDS databases using IAM authentication and Session Manager with the remote port forwarding capability. This solution, when compared to the traditional database connection mechanisms with bastion hosts publicly exposed to the internet, reduces your system’s attack surface while also simplifying your network architecture.

It also simplifies the operational overhead of managing usernames and passwords for your databases by ensuring secure and controlled access to your Amazon RDS resources with IAM policies.

To learn more about IAM database authentication for different DB engines, refer to IAM database authentication for MariaDB, MySQL, and PostgreSQL.

For further information about Systems Manager capabilities, refer to AWS Systems Manager Operational Capabilities.

If you have any questions, comments, or suggestions, leave a comment.

### About the Authors

Adria Morgado is a Cloud Infrastructure Architect at Amazon Web Services. He is specialized in designing and implementing robust, scalable, and secure solutions for large enterprise customers.

Alan Oberto Jimenez is a cloud architect/developer specialized in assisting customers in architecting, developing, and reengineering applications that can fully take advantage of the AWS Cloud.


