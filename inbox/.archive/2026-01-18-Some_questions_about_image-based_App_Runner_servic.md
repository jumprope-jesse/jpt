---
type: link
source: notion
url: https://www.reddit.com/r/aws/comments/1fdt2uj/some_questions_about_imagebased_app_runner/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-09-11T03:19:00.000Z
---

# Some questions about image-based App Runner services, Lambdas, and private ECR Repositories : r/aws

## AI Summary (from Notion)
- Topic: Questions about image-based App Runner services, Lambdas, and private ECR repositories in AWS.
- Key Questions:
- Do multiple image-based App Runner services or Lambdas require a separate ECR repository for each?
- What are the best base images for App Runner and Lambda when using .NET or Node.js?
- Context: The author is exploring AWS to build a system using App Runner and Lambdas, guided by a specific blog entry.
- Planned Services: Three App Runner services (a front-end server and two mid-tier APIs) along with several Lambdas.
- Observations:
- Amazon publishes specific .NET and Node.js images for Lambdas; the author questions the benefits of using these over standard images.
- The author is looking for similar base images for App Runner but has not found any.

## Content (from Notion)

TL;DR: 1) If I want more than one image-based App Runner Services or image-based Lambdas, do I need a separate image repository for each service or lambda? 2) What are appropriate base images to use for app runner and lambda running either dotnet or nodejs?

More context: I am doing a deeper dive than I've ever done on AWS trying to build a system based around App Runner and Lambdas. I have been using this blog entry as a guide for some of my learning.

At present I have three Services planned for App Runner, a front end server and two mid-tier APIs, as well as several Lambdas. Do I need to establish a different ECR Repository for each service and lambda in order to always push the latest to the service/lambda?

Additionally, I noticed that the Amazon public repositories have a dotnet and node.js image published by Amazon just for lambdas. Should I use those rather than a standard node or dotnet image, and if so, why? What does that image get me that a standard base image for those environments won't?

And if the AWS lambda base image is the best choice, is there a similar image for App Runner? Because I looked, but couldn't find anything explicitly for App Runner.


