---
type: link
source: notion
url: https://aws.amazon.com/blogs/aws/amazon-q-business-now-generally-available-helps-boost-workforce-productivity-with-generative-ai/
notion_type: Tech Announcement
tags: ['Running']
created: 2024-05-06T15:30:00.000Z
---

# Amazon Q Business, now generally available, helps boost workforce productivity with generative AI | AWS News Blog

## AI Summary (from Notion)
- Amazon Q Business Launch: Generally available as a generative AI-powered assistant to enhance workforce productivity.
- Key Features:
- Connects to over 40 enterprise data sources.
- Web-based chat assistant for answering questions and summarizing data.
- Custom plugins and Amazon Q Apps allow users to create sharable applications without coding experience.
- User Experience:
- New content creation mode for creative tasks without accessing enterprise content.
- Enhanced security with enterprise-grade access controls and compliance with Federal Information Processing Standards (FIPS).
- Admin Controls:
- Global and topic-level controls to manage data accessibility and response generation.
- Options to restrict topics and manage user permissions.
- Pricing:
- Two subscription tiers: Amazon Q Business Lite ($3/user/month) and Amazon Business Pro ($20/user/month).
- Free trial available for 50 users for 60 days.
- Future Potential: Amazon Q Apps enable users to easily create applications based on company data, promoting innovation.
- Integration: Works with AWS services for secure data handling and user management.
- Feedback Mechanism: Encouragement for users to provide feedback through AWS support channels.

## Content (from Notion)

---

At AWS re:Invent 2023, we previewed Amazon Q Business, a generative artificial intelligence (generative AI)–powered assistant that can answer questions, provide summaries, generate content, and securely complete tasks based on data and information in your enterprise systems.

With Amazon Q Business, you can deploy a secure, private, generative AI assistant that empowers your organization’s users to be more creative, data-driven, efficient, prepared, and productive. During the preview, we heard lots of customer feedback and used that feedback to prioritize our enhancements to the service.

Today, we are announcing the general availability of Amazon Q Business with many new features, including custom plugins, and a preview of Amazon Q Apps, generative AI–powered customized and sharable applications using natural language in a single step for your organization.

In this blog post, I will briefly introduce the key features of Amazon Q Business with the new features now available and take a look at the features of Amazon Q Apps. Let’s get started!

Introducing Amazon Q Business

Amazon Q Business connects seamlessly to over 40 popular enterprise data sources and stores document and permission information, including Amazon Simple Storage Service (Amazon S3), Microsoft 365, and Salesforce. It ensures that you access content securely with existing credentials using single sign-on, according to your permissions, and also includes enterprise-level access controls.

Amazon Q Business makes it easy for users to get answers to questions like company policies, products, business results, or code, using its web-based chat assistant. You can point Amazon Q Business at your enterprise data repositories, and it’ll search across all data, summarize logically, analyze trends, and engage in dialog with users.

With Amazon Q Business, you can build secure and private generative AI assistants with enterprise-grade access controls at scale. You can also use administrative guardrails, document enrichment, and relevance tuning to customize and control responses that are consistent with your company’s guidelines.

Here are the key features of Amazon Q Business with new features now available:

End-user web experience

With the built-in web experience, you can ask a question, receive a response, and then ask follow-up questions and add new information with in-text source citations while keeping the context from the previous answer. You can only get a response from data sources that you have access to.

With general availability, we’re introducing a new content creation mode in the web experience. In this mode, Amazon Q Business does not use or access the enterprise content but instead uses generative AI models built into Amazon Q Business for creative use cases such as summarization of responses and crafting personalized emails. To use the content creation mode, you can turn off Respond from approved sources in the conversation settings.

To learn more, visit Using an Amazon Q Business web experience and Customizing an Amazon Q Business web experience in the AWS documentation.

Pre-built data connectors and plugins

You can connect, index, and sync your enterprise data using over 40 pre-built data connectors or an Amazon Kendra retriever, as well as web crawling or uploading your documents directly.

Amazon Q Business ingests content using a built-in semantic document retriever. It also retrieves and respects permission information such as access control lists (ACLs) to allow it to manage access to the data after retrieval. When the data is ingested, your data is secured with the Service-managed key of AWS Key Management Service (AWS KMS).

You can configure plugins to perform actions in enterprise systems, including Jira, Salesforce, ServiceNow, and Zendesk. Users can create a Jira issue or a Salesforce case while chatting in the chat assistant. You can also deploy a Microsoft Teams gateway or a Slack gateway to use an Amazon Q Business assistant in your teams or channels.

With general availability, you can build custom plugins to connect to any third-party application through APIs so that users can use natural language prompts to perform actions such as submitting time-off requests or sending meeting invites directly through Amazon Q Business assistant. Users can also search real-time data, such as time-off balances, scheduled meetings, and more.

When you choose Custom plugin, you can define an OpenAPI schema to connect your third-party application. You can upload the OpenAPI schema to Amazon S3 or copy it to the Amazon Q Business console in-line schema editor compatible with the Swagger OpenAPI specification.

To learn more, visit Data source connectors and Configure plugins in the AWS documentation.

Admin control and guardrails

You can configure global controls to give users the option to either generate large language model (LLM)-only responses or generate responses from connected data sources. You can specify whether all chat responses will be generated using only enterprise data or whether your application can also use its underlying LLM to generate responses when it can’t find answers in your enterprise data. You can also block specific words.

With topic-level controls, you can specify restricted topics and configure behavior rules in response to the topics, such as answering using enterprise data or blocking completely.

To learn more, visit Admin control and guardrails in the AWS documentation.

You can alter document metadata or attributes and content during the document ingestion process by configuring basic logic to specify a metadata field name, select a condition, and enter or select a value and target actions, such as update or delete. You can also use AWS Lambda functions to manipulate document fields and content, such as using optical character recognition (OCR) to extract text from images.

To learn more, visit Document attributes and types in Amazon Q Business and Document enrichment in Amazon Q Business in the AWS documentation.

Enhanced enterprise-grade security and management

Starting April 30, you will need to use AWS IAM Identity Center for user identity management of all new applications rather than using the legacy identity management. You can securely connect your workforce to Amazon Q Business applications either in the web experience or your own interface.

You can also centrally manage workforce access using IAM Identity Center alongside your existing IAM roles and policies. As the number of your accounts scales, IAM Identity Center gives you the option to use it as a single place to manage user access to all your applications. To learn more, visit Setting up Amazon Q Business with IAM Identity Center in the AWS documentation.

At general availability, Amazon Q Business is now integrated with various AWS services to securely connect and store the data and easily deploy and track access logs.

You can use AWS PrivateLink to access Amazon Q Business securely in your Amazon Virtual Private Cloud (Amazon VPC) environment using a VPC endpoint. You can use the Amazon Q Business template for AWS CloudFormation to easily automate the creation and provisioning of infrastructure resources. You can also use AWS CloudTrail to record actions taken by a user, role, or AWS service in Amazon Q Business.

Also, we support Federal Information Processing Standards (FIPS) endpoints, based on the United States and Canadian government standards and security requirements for cryptographic modules that protect sensitive information.

To learn more, visit Security in Amazon Q Business and Monitoring Amazon Q Business in the AWS documentation.

Build and share apps with new Amazon Q Apps (preview)

Today we are announcing the preview of Amazon Q Apps, a new capability within Amazon Q Business for your organization’s users to easily and quickly create generative AI-powered apps based on company data, without requiring any prior coding experience.

With Amazon Q Apps, users simply describe the app they want, in natural language, or they can take an existing conversation where Amazon Q Business helped them solve a problem. With a few clicks, Amazon Q Business will instantly generate an app that accomplishes their desired task that can be easily shared across their organization.

If you are familiar with PartyRock, you can easily use this code-free builder with the added benefit of connecting it to your enterprise data already with Amazon Q Business.

To create a new Amazon Q App, choose Apps in your web experience and enter a simple text expression for a task in the input box. You can try out samples, such as a content creator, interview question generator, meeting note summarizer, and grammar checker.

I will make a document assistant to review and correct a document using the following prompt:

> 

When you choose the Generate button, a document editing assistant app will be automatically generated with two cards—one to upload a document file as an input and another text output card that gives edit suggestions.

When you choose the Add card button, you can add more cards, such as a user input, text output, file upload, or pre-configured plugin by your administrator. If you want to create a Jira ticket to request publishing a post in the corporate blog channel as an author, you can add a Jira Plugin with the result of edited suggestions from the uploaded file.

Once you are ready to share the app, choose the Publish button. You can securely share this app to your organization’s catalog for others to use, enhancing productivity. Your colleagues can choose shared apps, modify them, and publish their own versions to the organizational catalog instead of starting from scratch.

Choose Library to see all of the published Amazon Q Apps. You can search the catalog by labels and open your favorite apps.

Amazon Q Apps inherit robust security and governance controls from Amazon Q Business, including user authentication and access controls, which empower organizations to safely share apps across functions that warrant governed collaboration and innovation.

In the administrator console, you can see your Amazon Q Apps and control or remove them from the library.

To learn more, visit Amazon Q Apps in the AWS documentation.

Now available

Amazon Q Business is generally available today in the US East (N. Virginia) and US West (Oregon) Regions. We are launching two pricing subscription options.

The Amazon Q Business Lite ($3/user/month) subscription provides users access to the basic functionality of Amazon Q Business.

The Amazon Business Pro ($20/user/month) subscription gets users access to all features of Amazon Q Business, as well as Amazon Q Apps (preview) and Amazon Q in QuickSight (Reader Pro), which enhances business analyst and business user productivity using generative business intelligence capabilities.

You can use the free trial (50 users for 60 days) to experiment with Amazon Q Business. For more information about pricing options, visit Amazon Q Business Plan page.

To learn more about Amazon Q Business, you can study Amazon Q Business Getting Started, a free, self-paced digital course on AWS Skill Builder and Amazon Q Developer Center to get more sample codes.

Give it a try in the Amazon Q Business console today! For more information, visit the Amazon Q Business product page and the User Guide in the AWS documentation. Provide feedback to AWS re:Post for Amazon Q or through your usual AWS support contacts.

— Channy


