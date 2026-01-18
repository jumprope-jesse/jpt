---
type: link
source: notion
url: https://aws.amazon.com/blogs/aws/accelerate-serverless-testing-with-localstack-integration-in-vs-code-ide/
notion_type: Software Repo
tags: ['Running']
created: 2025-09-12T02:46:00.000Z
---

# Accelerate serverless testing with LocalStack integration in VS Code IDE | Amazon Web Services

## Overview (from Notion)
- The integration of LocalStack with VS Code can streamline your development process, saving time and reducing the complexity of managing multiple tools.
- This enhancement allows for local testing of serverless applications, which can be especially beneficial for balancing work and family commitments since it minimizes context switching.
- The seamless deployment experience to LocalStack mirrors traditional AWS processes, making it easier to develop and test applications without the delays of cloud deployments.
- As a founder, this integration can foster innovation by enabling rapid prototyping and iteration of new features in your software products.
- Consider the environmental impact of cloud computing; using local emulation may reduce unnecessary cloud resource consumption.
- On the flip side, reliance on local tools might limit exposure to real-world cloud environments, potentially leading to integration issues later in the development cycle.
- This tool can be seen as part of a broader shift toward more efficient, developer-friendly solutions in the tech industry, reflecting the increasing importance of user experience in software development.

## AI Summary (from Notion)
LocalStack integration in the AWS Toolkit for Visual Studio Code simplifies local testing and debugging of serverless applications by allowing developers to connect directly to LocalStack endpoints. This integration streamlines the development process, enabling end-to-end testing of event-driven workflows without complex configurations. Developers can easily set up LocalStack, deploy applications locally, and transition to cloud-based testing when needed, enhancing overall workflow efficiency. The new features are available in all commercial AWS Regions except GovCloud.

## Content (from Notion)

---

Today, we’re announcing LocalStack integration in the AWS Toolkit for Visual Studio Code that makes it easier than ever for developers to test and debug serverless applications locally. This enhancement builds upon our recent improvements to the AWS Lambda development experience, including the console to IDE integration and remote debugging capabilities we launched in July 2025, continuing our commitment to simplify serverless development on Amazon Web Services (AWS).

When building serverless applications, developers typically focus on three key areas to streamline their testing experience: unit testing, integration testing, and debugging resources running in the cloud. Although AWS Serverless Application Model Command Line Interface (AWS SAM CLI) provides excellent local unit testing capabilities for individual Lambda functions, developers working with event-driven architectures that involve multiple AWS services, such as Amazon Simple Queue Service (Amazon SQS), Amazon EventBridge, and Amazon DynamoDB, need a comprehensive solution for local integration testing. Although LocalStack provided local emulation of AWS services, developers had to previously manage it as a standalone tool, requiring complex configuration and frequent context switching between multiple interfaces, which slowed down the development cycle.

LocalStack integration in AWS Toolkit for VS CodeTo address these challenges, we’re introducing LocalStack integration so developers can connect AWS Toolkit for VS Code directly to LocalStack endpoints. With this integration, developers can test and debug serverless applications without switching between tools or managing complex LocalStack setups. Developers can now emulate end-to-end event-driven workflows involving services such as Lambda, Amazon SQS, and EventBridge locally, without needing to manage multiple tools, perform complex endpoint configurations, or deal with service boundary issues that previously required connecting to cloud resources.

The key benefit of this integration is that AWS Toolkit for VS Code can now connect to custom endpoints such as LocalStack, something that wasn’t possible before. Previously, to point AWS Toolkit for VS Code to their LocalStack environment, developers had to perform manual configuration and context switching between tools.

Getting started with LocalStack in VS Code is straightforward. Developers can begin with the LocalStack Free version, which provides local emulation for core AWS services ideal for early-stage development and testing. Using the guided application walkthrough in VS Code, developers can install LocalStack directly from the toolkit interface, which automatically installs the LocalStack extension and guides them through the setup process. When it’s configured, developers can deploy serverless applications directly to the emulated environment and test their functions locally, all without leaving their IDE.

Let’s try it outFirst, I’ll update my copy of the AWS Toolkit for VS Code to the latest version. Once, I’ve done this, I can see a new option when I go to Application Builder and click on Walkthrough of Application Builder. This allows me to install LocalStack with a single click.

Once I’ve completed the setup for LocalStack, I can start it up from the status bar and then I’ll be able to select LocalStack from the list of my configured AWS profiles. In this illustration, I am using Application Composer to build a simple serverless architecture using Amazon API Gateway, Lambda, and DynamoDB. Normally, I’d deploy this to AWS using AWS SAM. In this case, I’m going to use the same AWS SAM command to deploy my stack locally.

I just do `sam deploy –guided –profile localstack` from the command line and follow the usual prompts. Deploying to LocalStack using AWS SAM CLI provides the exact same experience I’m used to when deploying to AWS. In the screenshot below, I can see the standard output from AWS SAM, as well as my new LocalStack resources listed in the AWS Toolkit Explorer.

I can even go in to a Lambda function and edit the function code I’ve deployed locally!

Over on the LocalStack website, I can login and take a look at all the resources I have running locally. In the screenshot below, you can see the local DynamoDB table I just deployed.

Embed: <https://www.youtube-nocookie.com/embed/e2mokcAzDCY?feature=oembed>

Enhanced development workflowThese new capabilities complement our recently launched console-to-IDE integration and remote debugging features, creating a comprehensive development experience that addresses different testing needs throughout the development lifecycle. AWS SAM CLI provides excellent local testing for individual Lambda functions, handling unit testing scenarios effectively. For integration testing, the LocalStack integration enables testing of multiservice workflows locally without the complexity of AWS Identity and Access Management (IAM) permissions, Amazon Virtual Private Cloud (Amazon VPC) configurations, or service boundary issues that can slow down development velocity.

When developers need to test using AWS services in development environments, they can use our remote debugging capabilities, which provide full access to Amazon VPC resources and IAM roles. This tiered approach frees up developers to focus on business logic during early development phases using LocalStack, then seamlessly transition to cloud-based testing when they need to validate against AWS service behaviors and configurations. The integration eliminates the need to switch between multiple tools and environments, so developers can identify and fix issues faster while maintaining the flexibility to choose the right testing approach for their specific needs.

Now availableYou can start using these new features through the AWS Toolkit for VS Code by updating to v3.74.0. The LocalStack integration is available in all commercial AWS Regions except AWS GovCloud (US) Regions. To learn more, visit the AWS Toolkit for VS Code and Lambda documentation.

For developers who need broader service coverage or advanced capabilities, LocalStack offers additional tiers with expanded features. There are no additional costs from AWS for using this integration.

These enhancements represent another significant step forward in our ongoing commitment to simplifying the serverless development experience. Over the past year, we’ve focused on making VS Code the tool of choice for serverless developers, and this LocalStack integration continues that journey by providing tools for developers to build and test serverless applications more efficiently than ever before.


