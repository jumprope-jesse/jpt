---
type: link
source: notion
url: https://docs.aws.amazon.com/dtconsole/latest/userguide/welcome-connections.html
notion_type: Software Repo
tags: ['Running']
created: 2024-03-30T02:16:00.000Z
---

# What are connections? - Developer Tools console

## AI Summary (from Notion)
- Connections Feature: Enables integration of AWS resources (e.g., CodePipeline) with external code repositories (e.g., Bitbucket, GitHub).
- API Reference: Utilizes the AWS CodeConnections API for managing connections.
- Resource Management: Each connection has a unique ARN and can be shared across multiple AWS services.
- Third-Party Providers: Supports various repositories, including Bitbucket Cloud, GitHub (multiple types), and GitLab (both cloud and self-managed).
- Region-Specific Requirements: To use connections in the Europe (Milan) region, a specific app must be installed and enabled.
- Connection States: Connections can be in a Pending, Available, or Error state, with specific workflows for transitioning between states.
- Global Resources: Connections are globally accessible across AWS regions, but host resources are region-specific.
- Setup Process: Requires installation of AWS authentication apps and completion of OAuth handshakes for finalizing connections.
- Documentation Links: Multiple references to AWS documentation for further understanding and step-by-step guides.
- Use Cases: Enables uniform management of access and integration across different AWS services and third-party providers.

## Content (from Notion)

You can use the connections feature in the Developer Tools console to connect AWS resources such as AWS CodePipeline to external code repositories. This feature has its own API, the AWS CodeConnections API reference. Each connection is a resource that you can give to AWS services to connect to a third-party repository, such as BitBucket. For example, you can add the connection in CodePipeline so that it triggers your pipeline when a code change is made to your third-party code repository. Each connection is named and associated with a unique Amazon Resource Name (ARN) that is used to reference the connection.

The service name AWS CodeStar Connections has been renamed. Resources created with the previous namespace codestar-connections will still be supported.

## What can I do with connections?

You can use connections to integrate third-party provider resources with your AWS resources in developer tools, including:

- 
- 
- 
## What third-party providers can I create connections for?

Connections can associate your AWS resources with the following third-party repositories:

- 
- 
- 
- 
-  Important
- 
For an overview of the connections workflow, see Workflow to create or update connections.

The steps to create connections for a cloud provider type, such as GitHub, are different from the steps for an installed provider type, such as GitHub Enterprise Server. For the high-level steps to create a connection by provider type, see Working with connections.

Note

To use connections in the Europe (Milan) AWS Region, you must:

1. 
1. 
This Region-specific app supports connections in the Europe (Milan) Region. It is published on the third-party provider site, and it is separate from the existing app supporting connections for other Regions. By installing this app, you authorize third-party providers to share your data with the service for this Region only, and you can revoke the permissions at any time by uninstalling the app.

The service will not process or store your data unless you enable the Region. By enabling this Region, you grant our service permissions to process and store your data.

Even if the Region is not enabled, third-party providers can still share your data with our service if the Region-specific app remains installed, so make sure to uninstall the app once you disable the Region. For more information, see  Enabling a Region.

## What AWS services integrate with connections?

You can use connections to integrate your third-party repository with other AWS services. To view the service integrations for connections, see Product and service integrations with AWS CodeConnections.

## How do connections work?

Before you can create a connection, you must first install, or provide access to, the AWS authentication app on your third-party account. After a connection is installed, it can be updated to use this installation. When you create a connection, you provide access to the AWS resource in your third-party account. This allows the connection to access content, such as source repositories, in the third-party account, on behalf of your AWS resources. You can then share that connection with other AWS services to provide secure OAuth connections between the resources.

If you want to create a connection to an installed provider type, such as GitHub Enterprise Server, you first create a host resource using the AWS Management Console.

Diagram showing the connections between AWS resources and a third-party repository using connection ARNs.

Connections are owned by the AWS account that creates them. Connections are identified by an ARN containing a connection ID. The connection ID is a UUID that cannot be changed or remapped. Deleting and re-establishing a connection results in a new connection ID, and therefore a new connection ARN. This means that connection ARNs are never reused.

A newly created connection is in a Pending state. A third-party handshake (OAuth flow) process is required to complete setup of the connection and for it to move from Pending to an Available state. After this is complete, a connection is Available and can be used with AWS services, such as CodePipeline.

A newly created host is in a Pending state. A third-party registration process is required to complete setup of the host and for it to move from Pending to an Available state. After this is complete, a host is Available and can be used for connections to installed provider types.

For an overview of the connections workflow, see Workflow to create or update connections. For an overview of the host creation workflow for installed providers, see Workflow to create or update a host. For the high-level steps to create a connection by provider type, see Working with connections.

### Global resources in AWS CodeConnections

Connections are global resources, meaning that the resource is replicated across all AWS Regions.

Although the connection ARN format reflects the Region name where it was created, the resource is not constrained to any Region. The Region where the connection resource was created is the Region where connection resource data updates are controlled. Examples of API operations that control updates to connection resource data include creating a connection, updating an installation, deleting a connection, or tagging a connection.

Host resources for connections are not globally available resources. You use host resources only in the Region where they were created.

- 
- 
- 
- 
- 
### Workflow to create or update a host

When you create a connection for an installed provider, you first create a host.

Hosts can have the following states:

- 
- 
Workflow: Creating or updating a host with the CLI, SDK, or AWS CloudFormation

You use the CreateHost API to create a host using the AWS Command Line Interface (AWS CLI), SDK, or AWS CloudFormation. After it is created, the host is in a pending state. You complete the process by using the console Set up option in the console.

Workflow: Creating or updating a host with the console

If you are creating a connection to an installed provider type, such as GitHub Enterprise Server or GitLab self-managed, you first create a host. If you are connecting to a cloud provider type, such as Bitbucket, you skip creating the host and continue to creating a connection.

Use the console to set up the host and change its status from pending to available.

Diagram showing the workflow of creating a connection to third-party provider.

### Workflow to create or update connections

When you create a connection, you also create or use an existing installation for the auth handshake with the third-party provider.

Connections can have the following states:

- 
- 
- 
Workflow: Creating or updating a connection with the CLI, SDK, or AWS CloudFormation

You use the CreateConnection API to create a connection using the AWS Command Line Interface (AWS CLI), SDK, or AWS CloudFormation. After it is created, the connection is in a pending state. You complete the process by using the console Set up pending connection option. The console prompts you to create an installation or use an existing installation for the connection. You then use the console to complete the handshake and move the connection to an available state by choosing Complete connection on the console.

Workflow: Creating or updating a connection with the console

If you are creating a connection to an installed provider type, such as GitHub Enterprise Server, you first create a host. If you are connecting to a cloud provider type, such as Bitbucket, you skip creating the host and continue to creating a connection.

To create or update a connection using the console, you use the CodePipeline edit action page on the console to choose your third-party provider. The console prompts you to create an installation or use an existing installation for the connection, and then use the console to create the connection. The console completes the handshake and moves the connection from pending to an available state automatically.

Diagram showing the workflow of creating a connection to third-party provider.

## How do I get started with connections?

To get started, here are some useful topics to review:

- 
- 
- 

