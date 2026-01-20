---
type: link
source: notion
url: https://aws.amazon.com/blogs/aws/build-generative-ai-applications-with-amazon-bedrock-studio-preview/
notion_type: Software Repo
tags: ['Running']
created: 2024-05-07T21:20:00.000Z
---

# Build generative AI applications with Amazon Bedrock Studio (preview) | Amazon Web Services

## AI Summary (from Notion)
- Introduction of Amazon Bedrock Studio: A new web-based platform for developing generative AI applications, currently in public preview.
- Key Features:
- Rapid prototyping environment.
- Access to Amazon Bedrock features like Knowledge Bases, Agents, and Guardrails.
- User Access:
- Developers can use single sign-on credentials to sign in and start building applications.
- Administrators can control access to the platform, ensuring security.
- Getting Started:
- Administrators create a workspace and manage user access.
- Users can navigate the workspace to build generative AI applications.
- Building Applications:
- Users can select top-performing models, integrate company data, and experiment with settings.
- Functions can be used to make API calls to enhance model responses.
- Guardrails: Customizable safeguards to ensure safe interactions with generative AI applications.
- Availability: Currently available in AWS Regions US East (N. Virginia) and US West (Oregon).
- Community Engagement: Encouragement for user feedback and participation in the generative AI builder community.
- Visual Updates: Recent updates to the UI reflected in the screenshots provided.

## Content (from Notion)

---

Today, we’re introducing Amazon Bedrock Studio, a new web-based generative artificial intelligence (generative AI) development experience, in public preview. Amazon Bedrock Studio accelerates the development of generative AI applications by providing a rapid prototyping environment with key Amazon Bedrock features, including Knowledge Bases, Agents, and Guardrails.

As a developer, you can now use your company’s single sign-on credentials to sign in to Bedrock Studio and start experimenting. You can build applications using a wide array of top performing models, evaluate, and share your generative AI apps within Bedrock Studio. The user interface guides you through various steps to help improve a model’s responses. You can experiment with model settings, and securely integrate your company data sources, tools, and APIs, and set guardrails. You can collaborate with team members to ideate, experiment, and refine your generative AI applications—all without requiring advanced machine learning (ML) expertise or AWS Management Console access.

As an Amazon Web Services (AWS) administrator, you can be confident that developers will only have access to the features provided by Bedrock Studio, and won’t have broader access to AWS infrastructure and services.

Amazon Bedrock Studio

Now, let me show you how to get started with Amazon Bedrock Studio.

Get started with Amazon Bedrock StudioAs an AWS administrator, you first need to create an Amazon Bedrock Studio workspace, then select and add users you want to give access to the workspace. Once the workspace is created, you can share the workspace URL with the respective users. Users with access privileges can sign in to the workspace using single sign-on, create projects within their workspace, and start building generative AI applications.

Create Amazon Bedrock Studio workspaceNavigate to the Amazon Bedrock console and choose Bedrock Studio on the bottom left pane.

Amazon Bedrock Studio in the Bedrock console

Before creating a workspace, you need to configure and secure the single sign-on integration with your identity provider (IdP) using the AWS IAM Identity Center. For detailed instructions on how to configure various IdPs, such as AWS Directory Service for Microsoft Active Directory, Microsoft Entra ID, or Okta, check out the AWS IAM Identity Center User Guide. For this demo, I configured user access with the default IAM Identity Center directory.

Next, choose Create workspace, enter your workspace details, and create any required AWS Identity and Access Management (IAM) roles.

Amazon Bedrock Studio, workspace created

If you want, you can also select default generative AI models and embedding models for the workspace. Once you’re done, choose Create.

Amazon Bedrock Studio, workspace created

Next, select the created workspace.

Amazon Bedrock Studio, workspace created

Then, choose User management and Add users or groups to select the users you want to give access to this workspace.

Add users to your Amazon Bedrock Studio workspace

Back in the Overview tab, you can now copy the Bedrock Studio URL and share it with your users.

Amazon Bedrock Studio, share workspace URL

Build generative AI applications using Amazon Bedrock StudioAs a builder, you can now navigate to the provided Bedrock Studio URL and sign in with your single sign-on user credentials. Welcome to Amazon Bedrock Studio! Let me show you how to choose from industry leading FMs, bring your own data, use functions to make API calls, and safeguard your applications using guardrails.

Choose from multiple industry leading FMsBy choosing Explore, you can start selecting available FMs and explore the models using natural language prompts.

Amazon Bedrock Studio UI

If you choose Build, you can start building generative AI applications in a playground mode, experiment with model configurations, iterate on system prompts to define the behavior of your application, and prototype new features.

Amazon Bedrock Studio - start building applications

Bring your own dataWith Bedrock Studio, you can securely bring your own data to customize your application by providing a single file or by selecting a knowledge base created in Amazon Bedrock.

Amazon Bedrock Studio - start building applications

Use functions to make API calls and make model responses more relevantA function call allows the FM to dynamically access and incorporate external data or capabilities when responding to a prompt. The model determines which function it needs to call based on an OpenAPI schema that you provide.

Functions enable a model to include information in its response that it doesn’t have direct access to or prior knowledge of. For example, a function could allow the model to retrieve and include the current weather conditions in its response, even though the model itself doesn’t have that information stored.

Amazon Bedrock Studio - Add functions

Safeguard your applications using Guardrails for Amazon BedrockYou can create guardrails to promote safe interactions between users and your generative AI applications by implementing safeguards customized to your use cases and responsible AI policies.

Amazon Bedrock Studio - Add Guardrails

When you create applications in Amazon Bedrock Studio, the corresponding managed resources such as knowledge bases, agents, and guardrails are automatically deployed in your AWS account. You can use the Amazon Bedrock API to access those resources in downstream applications.

Here’s a short demo video of Amazon Bedrock Studio created by my colleague Banjo Obayomi.

Join the previewAmazon Bedrock Studio is available today in public preview in AWS Regions US East (N. Virginia) and US West (Oregon). To learn more, visit the Amazon Bedrock Studio page and User Guide.

Give Amazon Bedrock Studio a try today and let us know what you think! Send feedback to AWS re:Post for Amazon Bedrock or through your usual AWS contacts, and engage with the generative AI builder community at community.aws.

— Antje

May 7, 2024: Updated screenshots in this post to reflect recent updates to the UI.


