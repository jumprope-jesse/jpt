---
type: link
source: notion
url: https://aws.amazon.com/blogs/database/introducing-the-advanced-python-wrapper-driver-for-amazon-aurora/
notion_type: Software Repo
tags: ['Running']
created: 2024-06-11T21:27:00.000Z
---

# Introducing the Advanced Python Wrapper Driver for Amazon Aurora | AWS Database Blog

## AI Summary (from Notion)
- Introduction of Advanced Python Wrapper Driver: Aimed at enhancing scalability and resiliency for applications built with Python using Amazon Aurora.
- Key Features:
- Handles failover and authentication automatically.
- Reduces complexity by wrapping native PostgreSQL and MySQL drivers.
- Integrates with AWS IAM for token management and Secrets Manager for credential storage.
- Switchover Process: Automatic detection and switching to a new writer in less than 7 seconds during a switchover, compared to the usual 30 seconds.
- Code Examples:
- Demonstrates how to connect to Aurora using the Advanced Python Driver.
- Shows how to handle exceptions during failover scenarios.
- Installation Requirements: Requires installation of the Advanced Python Driver and its dependencies via pip.
- IAM and Secrets Manager Integration: Facilitates secure and automated authentication processes.
- Use Cases: Particularly useful for applications in eCommerce, financial services, and gaming that require high availability databases.
- Clean Up Reminder: Encourages deletion of any resources created during testing to avoid unnecessary charges.
- Future Content: Promises exploration of additional features in future posts.
- Author Background: Written by Dave Cramer, a Senior Software Engineer at AWS and a contributor to PostgreSQL.

## Content (from Notion)

Building upon our work with the Advanced JDBC (Java Database Connectivity) Wrapper Driver, we are continuing to enhance the scalability and resiliency of today’s modern applications that are built with Python. The ability to scale is critical to handle millions of users on demand, and with stateful applications such as eCommerce, financial services, and games, this means having highly available databases.

With the release of Amazon Aurora in 2015, customers could run relational databases in an Aurora cluster comprised of one writer and up to 15 low-latency reader nodes. This enables applications to scale reads and load balance among the replicas. However, as with any database supporting multiple instances, developers have built complex application logic to deal with special events such as switchover or failover.

Instead of writing complex endpoint logic into the application, the functionality to handle things like switchover or failover are now available in the Advanced Python Wrapper Driver. Additionally, the driver also integrates the handling of authentication using either AWS Secrets Manager or AWS Identity and Access Management (IAM). The Advanced Python Wrapper Driver has been released as an open-source project under the Apache 2.0 License. You can find the project on GitHub.

In this post, we provide details on how to use some of the features of the Advanced Python Wrapper Driver.

## Features of the Advanced Python Wrapper Driver

The Advanced Python Wrapper Driver wraps the native Psycopg or the MySQL Connector/Python drivers, adding failover and authentication features before delegating the function call to the underlying driver. Using the native driver to execute the API reduces the complexity of the code and focuses only on the additional features.

Aurora provides a cluster of DB instances instead of a single instance. Each connection is handled by a specific DB instance. When you connect to an Aurora cluster, the host name and port that you specify point to an intermediate handler called an endpoint. Aurora uses the endpoint mechanism to abstract these connections.

In the following sections, we discuss some of the challenges that the driver mitigates.

### Switchover

A switchover is when an Aurora Replica is promoted to a writer.

Clients have the option to connect to either the cluster writer endpoint or the cluster reader endpoint. Normally, they would connect to the writer endpoint. This endpoint is directed to the current writer instance. When a restart of the cluster occurs due to either a change in the parameters of the cluster or a failover, one of the readers is promoted to be the new writer. When this occurs, the cluster writer endpoint is updated to point to the new writer by updating the instance endpoint in the DNS. Due to inherent delays in DNS propagation, this can take up to 30 seconds to resolve. Normally, the application would require logic to reconnect after the temporary lack of availability of the database. The Advanced Python Wrapper Driver has built in the capability to automatically detect and switch the connection to the new writer. By using topology information inside the Aurora database, the driver can switch over the connection in 7 seconds or less.

### IAM integration

With IAM, you can specify which user can access services and resources in AWS, centrally manage fine-grained permissions, and analyze access to refine permissions across AWS. IAM enhances security by automatically changing the token (password) regularly. Although it’s completely acceptable to write the logic to acquire and use the IAM tokens in the application, this adds complexity because you have to deal with acquiring and caching the token. The driver caches and reuses the IAM tokens so that the application doesn’t have to deal with these complexities, even during switchover.

### Secrets Manager integration

Secrets Manager enables storing and managing credentials centrally. Storing the credentials centrally provides the ability to rotate them according to your security requirements. Secrets Manager can be used to store the user name and password for connection authentication. If this feature is enabled, the driver fetches and uses the credentials from Secrets Manager for connection authentication.

## Solution overview

Without the Advanced Python Driver, the typical Python code to connect and query a database looks like the following:

```plain text
with psycopg.connect("host=database.cluster-xyz.us-east-1.rds.amazonaws.com dbname=postgres user=john password=pwd") as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT aurora_db_instance_identifier()")
        cur.fetchone()
        for record in cur:
            print(record)
        conn.commit()
```

When the connection fails due to a switchover, the attempt to acquire a connection will fail until the new writer comes online. Without the AWS Advanced Python Driver, the connection must wait for the DNS to propagate, and the application would be offline for upwards of 30 seconds.

With the advanced driver, the reconnection is handled automatically. On the initial connection, the driver reads the topology of the cluster and gets the instance endpoints so that if the connection fails, the driver knows the IP addresses of all the instances in the cluster. When the connection fails on the user application, the driver starts polling the instances to get a connection. While polling for the new writer the application will wait for a new connection. As soon as a connection is established, we can read the new topology and get the IP address of the new writer and connect. Because this is all done inside the driver, the user application never sees the dropped connection or the connection failure. The driver throws an exception to let the user application know that the connection has been switched to a new server. In the event of a failure in the middle of an in-flight transaction, an exception is thrown to the user application to indicate that the transaction failed and has to be retried. Small changes in the user application are required to identify and handle the exception appropriately.

The following code demonstrates how to connect to an Aurora PostgreSQL cluster and configure failover:

```plain text
try:
    with AwsWrapperConnection.connect(
            psycopg.Connection.connect,
            host="database.cluster-xyz.us-east-1.rds.amazonaws.com",
            dbname="postgres",
            user="john",
            password="pwd",
            plugins="failover",
            wrapper_dialect="aurora-pg",
            autocommit=True
    ) as awsconn:
        cursor = awsconn.cursor()
        cursor.execute("SELECT aurora_db_instance_identifier(")
        res = cursor.fetchall()
        for record in res:
            print(record)

except FailoverSuccessError:
    # Query execution failed and AWS Advanced Python Driver successfully failed over to an available instance.
    # Since the connection was re-established we can safely ignore this error, create the cursor again and re-execute the query.
    cursor = awsconn.cursor()
    cursor.execute("SELECT aurora_db_instance_identifier(")
    res = cursor.fetchall()
    for record in res:
        print(record)

except FailoverFailedError as e:
    # At this point the driver was unable to re-establish the connection.
    # We will need to create a new connection.
    raise e
```

Because we are looking for the new writer using the instance endpoints and doesn’t depend on the DNS cache, the driver is able to reconnect much faster, typically around 7 seconds or less after the driver notices the failure.

## Prerequisites

The Advanced Python Wrapper is implemented using the PEP 249 – Python Database API Specification 2.0 pattern. This means that the native Psycopg or the MySQL Connector/Python drivers are required to be added as dependencies.

Installation of the driver requires pip. For more information, see Installing Packages.

## Creating an application that uses the Advanced Python Wrapper Driver

The following section outlines the steps required to create an application that uses the Advanced Python Wrapper Driver.

### Obtaining the Advanced Python Wrapper Driver

Install the Advanced Python Driver using pip:

```plain text
pip install aws-advanced-python-wrapper
```

Since the Advanced Python Driver is a wrapper on top of a native Psycopg or the MySQL Connector/Python Driver, you also need to install the respective one to your database.

For instance, if you want to use the Advanced Python Driver with Psycopg, install it using:

```plain text
pip install psycopg
```

If you want to use the IAM plugin and the Secrets Manager plugin, you need to install Boto3, the AWS SDK for Python. You can do so using pip:

```plain text
pip install boto3
```

### Update your code

After you have the correct dependencies, there are a few changes that require your application to use the Advanced Python Driver.

You need to wrap the original Python driver’s connect method in the AwsWrapperConnection’s connect method.

For instance, Psycopg, instead of connecting via:

```plain text
psycopg.connect("host=database.cluster-xyz.us-east-1.rds.amazonaws.com dbname=postgres user=john password=pwd")
```

You need to do:

```plain text
AwsWrapperConnection.connect(
        psycopg.Connection.connect,
        "host=database.cluster-xyz.us-east-1.rds.amazonaws.com dbname=postgres user=john password=pwd")
```

### Specify driver features

Determine the features of the driver you want to use. The AWS Advanced Python Driver uses plugins to run database methods. You can think of a plugin as an extensible code module that adds extra logic around any database method calls. The AWS Advanced Python Wrapper Driver has a number of built-in plugins. This is configured in the plugins driver property. For more information, see Connection Plugin Manager Parameters. The default setting for this is aurora_connection_tracker,failover,host_monitoring.

The aurora_connection_tracker plugin makes sure that all open connections to the failed node are closed in the event of a failover. The failover plugin handles the actual failover detection and reconnection. The host_monitoring plugin actively monitors the hosts to decrease the reconnection time upon failover.

## Secrets Manager integration

AWS provides a service to store secrets. The AWS Advanced Python Wrapper Driver provides a plugin that facilitates storing the values for username and password in a secret and accessing it to provide the values for USER and PASSWORD for authentication.

The only three properties required are secrets_manager_region, secrets_manager_secret_id, and plugins.

The following code block shows an example:

```plain text
with AwsWrapperConnection.connect(
        psycopg.Connection.connect,
        host="database.cluster-xyz.us-east-1.rds.amazonaws.com",
        dbname="postgres",
        secrets_manager_secret_id="arn:aws:secretsmanager:<Region>:<AccountId>:secret:Secre78tName-6RandomCharacters",
        secrets_manager_region="us-east-2",
        plugins="aws_secrets_manager"
) as awsconn, awsconn.cursor() as cursor:
    cursor.execute("SELECT aurora_db_instance_identifier()")
    for record in cursor.fetchone():
        print(record)
```

## IAM authentication integratation

The AWS Advanced Python Driver supports IAM authentication. When using IAM database authentication, the host URL must be a valid Amazon endpoint, and not a custom domain or an IP address. For example: db-identifier.cluster-XYZ.us-east-2.rds.amazonaws.com.

IAM authentication requires Boto3, the AWS SDK for Python. Boto3 is a runtime dependency and must be resolved. It can be installed via pip:

```plain text
pip install boto3
```

For Boto3, you will be required to set up your AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY to authenticate.

IAM database authentication is limited to certain database engines. For more information on limitations and recommendations, refer to IAM database authentication for MariaDB, MySQL, and PostgreSQL.

### Configure IAM authentication

Complete the following steps to set up IAM authentication:

1. Enable IAM database authentication on an existing database or create a new database with IAM database authentication in the Amazon RDS console.
1. Set up an IAM policy for IAM database authentication.
1. Create a database account using IAM database authentication. Connect to your database of choice using primary logins: 
### Use IAM authentication with the Advanced Python Wrapper Driver

The following code provides an example of how to use IAM authentication with the driver:

```plain text
with AwsWrapperConnection.connect(
        psycopg.Connection.connect,
        host="database.cluster-xyz.us-east-1.rds.amazonaws.com",
        dbname="postgres",
        user="john",
        plugins="iam"
) as awsconn, awsconn.cursor() as awscursor:

    awscursor.execute("CREATE TABLE IF NOT EXISTS bank_test (name varchar(40), account_balance int)")
    cursor.execute("SELECT aurora_db_instance_identifier(")
    for record in res:
        print(record)
```

## Clean up

If you have created any Aurora clusters, IAM credentials, or Secrets Manager credentials while following this post, make sure you delete them.

## Summary

The AWS Advanced Python Driver uses IAM or Secrets Manager from AWS and cluster configuration provided by Aurora to provide a solution for authentication and failover. Additionally, by taking advantage of the features in Aurora, the driver reduces failover time from 30 seconds to 7 seconds or less. There are many more features of the driver, which we will explore in future posts. Stay tuned! In the meantime, please share your comments on this post and visit the GitHub project for more details and examples.

### About the author

Dave Cramer is a Senior Software Engineer for Amazon Web Services. He is also a major contributor to PostgreSQL as the maintainer of the PostgreSQL JDBC driver. His passion is client interfaces and working with clients.


