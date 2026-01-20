---
type: link
source: notion
url: https://aws.amazon.com/blogs/aws/customize-amazon-q-developer-in-your-ide-with-your-private-code-base/
notion_type: Tech Announcement
tags: ['Running']
created: 2024-07-11T04:47:00.000Z
---

# Customize Amazon Q Developer (in your IDE) with your private code base | AWS News Blog

## AI Summary (from Notion)
- Amazon Q Developer Launch: The capability for customization in Amazon Q Developer for inline code completion is now generally available, along with a preview for chat customization.

- Functionality: Amazon Q serves as an AI coding companion, providing code recommendations based on existing comments and code in IDEs like JetBrains, Visual Studio Code, and Visual Studio.

- Customization Benefits: Developers can customize Amazon Q to generate code recommendations from their private code repositories, ensuring relevance to their organization's internal libraries.

- Use Case Example: A developer can ask Amazon Q to create specific functions or retrieve data, enhancing productivity and easing onboarding for new team members.

- Data Privacy: Customizations are kept private to each organization, with no use of shared code for training Amazon Q's foundation model.

- Update Process: Administrators can easily update customizations through the AWS Management Console, allowing for regular updates based on the latest commits.

- Chat Customization: Developers can interact in chat to get explanations for code snippets or ask general questions related to their code base.

- Performance Monitoring: Customization effectiveness can be tracked through user activity and metrics published on Amazon CloudWatch.

- Supported Languages: Customizations currently support Java, JavaScript, TypeScript, and Python, with other languages excluded from the customization process.

- Cost and Access: The Amazon Q customization feature is included at no extra charge in the Amazon Q Developer Professional subscription, allowing up to eight customizations per account.

## Content (from Notion)

---

Today, we’re making the Amazon Q Developer (in your IDE) customization capability generally available for inline code completion, and we’re launching a preview of customization for the chat. You can now customize Amazon Q to generate specific code recommendations from private code repositories in the IDE code editor and in the chat.

Amazon Q Developer is an artificial intelligence (AI) coding companion. It helps software developers accelerate application development by offering code recommendations in their integrated development environments (IDE) derived from existing comments and code. Behind the scenes, Amazon Q uses large language models (LLMs) trained on billions of lines of code from Amazon and open source projects.

Amazon Q is available in your IDE, and you can download the extension for JetBrains, Visual Studio Code, and Visual Studio (preview). In the IDE text editor, it suggests code as you type or write entire functions from a comment you enter. You can also chat with Q Developer and ask it to generate code for specific tasks or explain code snippets from a code base you’re discovering.

With the new customization capability, developers can now receive even more relevant code recommendations that are based on their organization’s internal libraries, APIs, packages, classes, and methods.

For example, let’s imagine that a developer working for a financial company is tasked to write a function to compute the total portfolio value for a customer. The developer can now describe the intent in a comment or type a function name such as computePortfolioValue(customerId: String), and Amazon Q will suggest code to implement that function based on the examples it learned from your organization’s private code base.

The developer can also ask questions about their organization’s code in the chat. In the example above, let’s imagine the developer is new to the team and doesn’t know how to retrieve a customer ID. He can ask the question in the chat in plain English: how do I connect to the database to retrieve the customerId for a specific customer? Amazon Q chat could answer: I found a function to retrieve customerId based on customer first and last name which uses the database connection XYZ…

As an administrator, you create customizations built from your internal git repositories (such as GitHub, GitLab, or BitBucket) or an Amazon Simple Storage Service (Amazon S3) bucket. It helps Amazon Q understand the intent, determine which internal and public APIs are best suited to the task, and generate code recommendations.

Amazon Q customization capability meets the strong data privacy and security you expect from AWS. The code base you share with Amazon Q stays private to your organization. We don’t use it to train our foundation model. Once customizations are deployed, the inference endpoint is private for the developers in your organization. Recommendations based on your code won’t pop up in another company’s developer IDE. You decide which developers have access to each individual customization, and you can follow metrics to measure the performance of the customizations you deployed.

We built the Amazon Q customization capability based on leading technical techniques, such as Retrieval Augmented Generation (RAG). This very detailed blog post shares more details about the science behind the Amazon Q customizations capability.

Since we launched the preview on October 17 last year, we’ve added two new capabilities: the ability to update a customization and the ability to customize the chat in the IDE.

Your organization’s code base is constantly evolving, and you want Amazon Q to always suggest up-to-date code snippets. Amazon Q administrator can now start an update process with one step in the AWS Management Console. Administrators can schedule regular updates based on the latest commits on code repositories to ensure developers always receive highly accurate code suggestions.

With the new chat customization (in preview), developers in your organization can select a portion of code in their IDE and send it to the chat to ask for an explanation of what the selected code does. Developers can also ask generic questions relative to their organization’s code base, like “How do I connect to the database to retrieve customerId for a specific customer?”

Let’s see how to use it

In this demo, I decided to focus on the new customization update capability that is generally available today. To quickly learn how to create a customization, activate it, and grant access to developers, read the excellent post from my colleague Donnie.

To update an existing customization, I navigate to the Customizations section of the Amazon Q console page. I select the customization I want to update. Then, I select Actions and Create new version.

Similarly to what I did when I created the customization, I choose the source code repository and select Create.

Creating a new version of the customization might take a while because depends on the quantity of code to ingest. When ready, a new version appears under the Versions tab. You can compare the Evaluation score of the new version with the previous versions and decide to activate it to make it available to your developers. At any point, you can revert to a previous version.

One of the aspects I like about active customizations is that I can monitor their effectiveness to help increase developer productivity in my organization.

On the Dashboard page, I track the User activity. I can track how many Daily active users there are, how many Lines of code have been generated, how many Security scans were performed, and so on. If, like me, you have used Amazon CodeWhisperer Professional in the past, when you use it now, you might still see the name CodeWhisperer appear on some pages. It will progressively be replaced with the new name: Amazon Q Developer.

Amazon Q generates more metrics and publishes them on Amazon CloudWatch. I can build CloudWatch dashboards to monitor the performance of the customizations I deployed. For example, here is a custom CloudWatch dashboard that monitors the code suggestions’ Block Accept Rate and Line Accept Rate, broken down per programming language.

Supported programming languagesCurrently, you can customize Amazon Q recommendations on codebases written in Java, JavaScript, TypeScript, and Python. Files written in other languages supported by Amazon Q, such as C#, Go, Rust, PHP, Ruby, Kotlin, C, C++, Shell scripting, SQL, and Scala will not be used when creating the customization or when providing customized recommendations in the IDE.

Pricing and availabilityAmazon Q is AWS Region agnostic and available to developers worldwide. Amazon Q is currently hosted in US East (N. Virginia). Amazon Q administrators can configure Amazon Q as an authorized cross-Region application if you have AWS IAM Identity Center in other Regions.

The Amazon Q customization capability is available at no additional charge within the Amazon Q Developer Professional subscription. You can create up to eight customizations per AWS account and keep up to two customizations active.

Now go build, and start to propose Amazon Q customizations to your organization’s developers.

- - seb

