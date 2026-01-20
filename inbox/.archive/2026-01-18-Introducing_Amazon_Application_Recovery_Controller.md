---
type: link
source: notion
url: https://aws.amazon.com/blogs/aws/introducing-amazon-application-recovery-controller-region-switch-a-multi-region-application-recovery-service/
notion_type: Tech Announcement
tags: ['Running']
created: 2025-08-02T03:21:00.000Z
---

# Introducing Amazon Application Recovery Controller Region switch: A multi-Region application recovery service | AWS News Blog

## Overview (from Notion)
- The Amazon Application Recovery Controller (ARC) Region switch can enhance your application resilience, which is crucial for any business, especially in a fast-paced environment like NYC.
- It offers a centralized solution to orchestrate recovery, reducing downtime and increasing reliability for your software applications—beneficial for user satisfaction and business continuity.
- The automation of recovery plans can save time and resources, allowing you to focus on innovation and growth rather than manual recovery processes.
- With its continuous validation of recovery plans, you can maintain confidence in your systems, knowing they will function during critical failures.
- The flexible pricing model allows for cost management, making it easier to scale resources as your company grows.
- Consider the implications of cloud dependency: while these tools offer great benefits, they also require a solid understanding of cloud architecture and the potential risks involved.
- Alternate views could argue that reliance on automated systems might lead to complacency; regular testing and human oversight are still vital for effective disaster recovery.

## AI Summary (from Notion)
Amazon Application Recovery Controller (ARC) Region switch is a managed service that enables organizations to confidently plan, practice, and execute Region switches for multi-Region applications on AWS. It automates recovery tasks across AWS services, reducing complexity and uncertainty. Users can create recovery plans with various execution blocks, monitor progress, and validate configurations regularly. The service is priced at $70 per month per plan and is available in all commercial AWS Regions.

## Content (from Notion)

---

As a developer advocate at AWS, I’ve worked with many enterprise organizations who operate critical applications across multiple AWS Regions. A key concern they often share is the lack of confidence in their Region failover strategy—whether it will work when needed, whether all dependencies have been identified, and whether their teams have practiced the procedures enough. Traditional approaches often leave them uncertain about their readiness for Regional switch.

Today, I’m excited to announce Amazon Application Recovery Controller (ARC) Region switch, a fully managed, highly available capability that enables organizations to plan, practice, and orchestrate Region switches with confidence, eliminating the uncertainty around cross-Region recovery operations. Region switch helps you orchestrate recovery for your multi-Region applications on AWS. It gives you a centralized solution to coordinate and automate recovery tasks across AWS services and accounts when you need to switch your application’s operations from one AWS Region to another.

Many customers deploy business-critical applications across multiple AWS Regions to meet their availability requirements. When an operational event impacts an application in one Region, switching operations to another Region involves coordinating multiple steps across different AWS services, such as compute, databases, and DNS. This coordination typically requires building and maintaining complex scripts that need regular testing and updates as applications evolve. Additionally, orchestrating and tracking the progress of Region switches across multiple applications and providing evidence of successful recovery for compliance purposes often involves manual data gathering.

Region switch is built on a Regional data plane architecture, where Region switch plans are executed from the Region being activated. This design eliminates dependencies on the impacted Region during the switch, providing a more resilient recovery process since the execution is independent of the Region you’re switching from.

Building a recovery plan with ARC Region switchWith ARC Region switch, you can create recovery plans that define the specific steps needed to switch your application between Regions. Each plan contains execution blocks that represent actions on AWS resources. At launch, Region switch supports nine types of execution blocks:

- ARC Region switch plan execution block–let you orchestrate the order in which multiple applications switch to the Region you want to activate by referencing other Region switch plans.
- Amazon EC2 Auto Scaling execution block–Scales Amazon EC2 compute resources in your target Region by matching a specified percentage of your source Region’s capacity.
- ARC routing controls execution block–Changes routing control states to redirect traffic using DNS health checks.
- Amazon Aurora global database execution block–Performs database failover with potential data loss or switchover with zero data loss for Aurora Global Database.
- Manual approval execution block–Adds approval checkpoints in your recovery workflow where team members can review and approve before proceeding.
- Custom Action AWS Lambda execution block–Adds custom recovery steps by executing Lambda functions in either the activating or deactivating Region.
- Amazon Route 53 health check execution block–Let you to specify which Regions your application’s traffic will be redirected to during failover. When executing your Region switch plan, the Amazon Route 53 health check state is updated and traffic is redirected based on your DNS configuration.
- Amazon Elastic Kubernetes Service (Amazon EKS) resource scaling execution block–Scales Kubernetes pods in your target Region during recovery by matching a specified percentage of your source Region’s capacity.
- Amazon Elastic Container Service (Amazon ECS) resource scaling execution block–Scales ECS tasks in your target Region by matching a specified percentage of your source Region’s capacity.
Region switch continually validates your plans by checking resource configurations and AWS Identity and Access Management (IAM) permissions every 30 minutes. During execution, Region switch monitors the progress of each step and provides detailed logs. You can view execution status through the Region switch dashboard and at the bottom of the execution details page.

To help you balance cost and reliability, Region switch offers flexibility in how you prepare your standby resources. You can configure the desired percentage of compute capacity to target in your destination Region during recovery using Region switch scaling execution blocks. For critical applications expecting surge traffic during recovery, you might choose to scale beyond 100 percent capacity, and setting a lower percentage can help achieve faster overall execution times. However, it’s important to note that using one of the scaling execution blocks does not guarantee capacity, and actual resource availability depends on the capacity in the destination Region at the time of recovery. To facilitate the best possible outcomes, we recommend regularly testing your recovery plans and maintaining appropriate Service Quotas in your standby Regions.

ARC Region switch includes a global dashboard you can use to monitor the status of Region switch plans across your enterprise and Regions. Additionally, there’s a Regional executions dashboard that only displays executions within the current console Region. This dashboard is designed to be highly available across each Region so it can be used during operational events.

Region switch allows resources to be hosted in an account that is separate from the account that contains the Region switch plan. If the plan uses resources from an account that is different from the account that hosts the plan, then Region switch uses the executionRole to assume the crossAccountRole to access those resources. Additionally, Region switch plans can be centralized and shared across multiple accounts using AWS Resource Access Manager (AWS RAM), enabling efficient management of recovery plans across your organization.

Let’s see how it worksLet me show you how to create and execute a Region switch plan. There are three parts in this demo. First, I create a Region switch plan. Then, I define a workflow. Finally, I configure the triggers.

Step 1: Create a plan

I navigate to the Application Recovery Controller section of the AWS Management Console. I choose Region switch in the left navigation menu. Then, I choose Create Region switch plan.

ARC Region switch - 1

After I give a name to my plan, I specify a Multi-Region recovery approach (active/passive or active/active). In Active/Passive mode, two application replicas are deployed into two Regions, with traffic routed into the active Region only. The replica in the passive Region can be activated by executing the Region switch plan.

Then, I select the Primary Region and Standby Region. Optionally, I can enter a Desired recovery time objective (RTO). The service will use this value to provide insight into how long Region switch plan executions take in relation to my desired RTO.

ARC Region switch - create plan

I enter the Plan execution IAM role. This is the role that allows Region switch to call AWS services during execution. I make sure the role I choose has permissions to be invoked by the service and contains the minimum set of permissions allowing ARC to operate. Refer to the IAM permissions section of the documentation for the details.

ARC Region switch - create plan 2

Step 2: Create a workflow

When the two Plan evaluation status notifications are green, I create a workflow. I choose Build workflows to get started.

ARC Region switch - status

Plans enable you to build specific workflows that will recover your applications using Region switch execution blocks. You can build workflows with execution blocks that run sequentially or in parallel to orchestrate the order in which multiple applications or resources recover into the activating Region. A plan is made up of these workflows that allow you to activate or deactivate a specific Region.

For this demo, I use the graphical editor to create the workflow. But you can also define the workflow in JSON. This format is better suited for automation or when you want to store your workflow definition in a source code management system (SCMS) and your infrastructure as code (IaC) tools, such as AWS CloudFormation.

ARC - define workflows

I can alternate between the Design and the Code views by selecting the corresponding tab next to the Workflow builder title. The JSON view is read-only. I designed the workflow with the graphical editor and I copied the JSON equivalent to store it alongside my IaC project files.

ARC - define workflows as code

Region switch launches an evaluation to validate your recovery strategy every 30 minutes. It regularly checks that all actions defined in your workflows will succeed when executed. This proactive validation assesses various elements, including IAM permissions and resource states across accounts and Regions. By continually monitoring these dependencies, Region switch helps ensure your recovery plans remain viable and identifies potential issues before they impact your actual switch operations.

However, just as an untested backup is not a reliable backup, an untested recovery plan cannot be considered truly validated. While continuous evaluation provides a strong foundation, we strongly recommend regularly executing your plans in test scenarios to verify their effectiveness, understand actual recovery times, and ensure your teams are familiar with the recovery procedures. This hands-on testing is essential for maintaining confidence in your disaster recovery strategy.

Step 3: Create a trigger

A trigger defines the conditions to activate the workflows just created. It’s expressed as a set of CloudWatch alarms. Alarm-based triggers are optional. You can also use Region switch with manual triggers.

From the Region switch page in the console, I choose the Triggers tab and choose Add triggers.

ARC - Trigger

For each Region defined in my plan, I choose Add trigger to define the triggers that will activate the Region.

ARC - Trigger 2

Finally, I choose the alarms and their state (OK or Alarm) that Region switch will use to trigger the activation of the Region.

ARC - Trigger 3

I’m now ready to test the execution of the plan to switch Regions using Region switch. It’s important to execute the plan from the Region I’m activating (the target Region of the workflow) and use the data plane in that specific Region.

Here is how to execute a plan using the AWS Command Line Interface (AWS CLI):

```plain text
aws arc-region-switch start-plan-execution \
--plan-arn arn:aws:arc-region-switch::111122223333:plan/resource-id \
--target-region us-west-2 \
--action activate
```

Pricing and availabilityRegion switch is available in all commercial AWS Regions at $70 per month per plan. Each plan can include up to 100 execution blocks, or you can create parent plans to orchestrate up to 25 child plans.

Having seen firsthand the engineering effort that goes into building and maintaining multi-Region recovery solutions, I’m thrilled to see how Region switch will help automate this process for our customers. To get started with ARC Region switch, visit the ARC console and create your first Region switch plan. For more information about Region switch, visit the Amazon Application Recovery Controller (ARC) documentation. You can also reach out to your AWS account team with questions about using Region switch for your multi-Region applications.

I look forward to hearing about how you use Region switch to strengthen your multi-Region applications’ resilience.

— seb


