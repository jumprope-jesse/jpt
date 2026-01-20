---
type: link
source: notion
url: https://aws.amazon.com/blogs/aws/amazon-codecatalyst-introduces-custom-blueprints-and-a-new-enterprise-tier/
notion_type: Product Website
tags: 
created: 2023-11-28T16:13:00.000Z
---

# Amazon CodeCatalyst introduces custom blueprints and a new enterprise tier | AWS News Blog

## AI Summary (from Notion)
- Introduction of Amazon CodeCatalyst Enterprise Tier: A new pricing tier offering advanced features for project management.
- Pricing: $20/user per month with included resources such as 1,500 compute minutes and 64GB of Dev Environment storage.
- Custom Blueprints: Users can define best practices for code, workflows, and infrastructure which can be published and used in project creation.
- Efficiency: Blueprints allow for quick project setup and integration of essential tools, reducing time spent on development operations.
- Automatic Updates: Changes made to custom blueprints can automatically update projects using them, ensuring consistency in best practices.
- Visibility for Admins: Admins can track which projects are utilizing specific blueprints, enhancing oversight on project standards.
- Creating Custom Blueprints: Steps provided for creating and managing blueprints within the CodeCatalyst console.
- Availability: The enterprise tier is currently available in US West (Oregon) and Europe (Ireland) Regions, with deployment options for other commercial regions.
- Encouragement to Explore: Concludes with an invitation to use the new features and build efficiently.

## Content (from Notion)

Today, I’m excited to introduce the new Amazon CodeCatalyst enterprise tier and custom blueprints.

Amazon CodeCatalyst enterprise tier is a new pricing tier that offers features like custom blueprints and project lifecycle management. The enterprise tier is $20/user per month, and each enterprise tier space gets 1,500 compute minutes, 160 Dev Environment hours, and 64GB of Dev Environment storage per paying user. You can use custom blueprints to define best practices for your application code, workflows, and infrastructure. You can publish these blueprints to your CodeCatalyst space, utilizing them for project creation or applying standards to existing projects.

Blueprints help you set up projects in minutes so you can get to work on code immediately. With just a few clicks, you can set up project files and configure built-in, fully integrated tools (for example, source repository, issue management, and continuous integration and delivery (CI/CD) pipeline) with best practices for your particular type of project. You can swap in popular tools like GitHub if needed, while maintaining the unified experience. You spend less time on building, integrating, or operating developer tools over the project’s lifetime.

With custom blueprints, you can define various elements of your CodeCatalyst project, like workflow definitions, infrastructure as code (IaC), and application code. When custom blueprints are updated, those changes are reflected in any project using the blueprint as a pull request update. This streamlined process reduces overhead in setting up your projects and ensures that best practices are consistently applied across your projects. As an admin, you can easily view details about which projects are using each blueprint in your CodeCatalyst space, giving you visibility into how standards are being applied across your projects.

Creating a custom blueprint in CodeCatalyst

I open the CodeCatalyst console and then I navigate to my space. On the Settings tab, I choose Blueprints on the left navigation pane, and then I select Create blueprint. At this point, I codify my best practices in this blueprint. When ready, I’ll publish it back to my space so my teams can use it to create projects.

After I publish my blueprint, I can view and manage it in my CodeCatalyst space in the Settings tab. In the left panel, I choose Blueprints. Then I select Space blueprints.

I select Create project > Space blueprints to create a CodeCatalyst project from my custom blueprint.

Availability

The Amazon CodeCatalyst enterprise tier is available in US West (Oregon) and Europe (Ireland) Regions, but you can deploy to any commercial Region. To learn more, visit the Amazon CodeCatalyst webpage.

Go build!

— Irshad


