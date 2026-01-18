---
type: link
source: notion
url: https://github.com/zappa/Zappa/pull/1367
notion_type: Software Repo
tags: ['Running']
created: 2025-12-05T15:42:00.000Z
---

# Add support for Lambda SnapStart by wangsha · Pull Request #1367 · zappa/Zappa · GitHub

## Overview (from Notion)
- The introduction of Lambda SnapStart can significantly enhance application performance, reducing startup times which is crucial for user experience—something to consider if you're developing customer-facing applications.
- As a software engineer and founder, this change could allow you to optimize your deployments, leading to cost savings and improved efficiency for your business.
- The integration of SnapStart with Zappa means you can leverage serverless architecture more effectively, potentially freeing up your time for family activities while your applications run smoothly.
- Unique viewpoint: Embracing new technologies like SnapStart can position your company as an innovator in the competitive NYC tech scene, attracting talent and customers alike.
- Alternate view: While the benefits are clear, consider the complexities of integrating new features and ensure your team is prepared for the transition to avoid disruption.

## AI Summary (from Notion)
This pull request introduces support for AWS Lambda SnapStart in the Zappa project, enhancing startup performance. Key updates include adding a snap_start attribute in the CLI class, modifying core functions for Lambda configuration, and implementing new tests to verify SnapStart functionality. Configuration files have also been updated to reflect SnapStart stages.

## Content (from Notion)

## Description

https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html

Lambda SnapStart can provide as low as sub-second startup performance. This pull request introduces support for SnapStart configuration in the Zappa project. The changes include updates to the configuration files, the main CLI class, and the core functions for creating and updating Lambda functions. Additionally, new tests have been added to ensure the correct functionality of the SnapStart feature.

Key changes include:

### SnapStart Configuration Support:

- zappa/cli.py: Added snap_start attribute to the ZappaCLI class and incorporated it in the update and load_settings methods. [1] [2] [3]
- zappa/core.py: Updated create_lambda_function and update_lambda_configuration methods to handle the SnapStart configuration. [1] [2] [3] [4]
### Configuration File Updates:

- tests/test_settings.yaml: Added new stages for SnapStart enabled and disabled configurations.
### Testing:

- tests/tests.py: Added test_snap_start_configuration method to verify the correct setting and passing of SnapStart configuration in various scenarios.
- Minor formatting changes for consistency.

