---
type: link
source: notion
url: https://github.com/aws-samples/sample-ai-powered-sdlc-patterns-with-aws/tree/main/design-and-architecture/design-solutionarchitecture-agent
notion_type: Software Repo
tags: ['Running']
created: 2025-11-01T13:29:00.000Z
---

# sample-ai-powered-sdlc-patterns-with-aws/design-and-architecture/design-solutionarchitecture-agent at main · aws-samples/sample-ai-powered-sdlc-patterns-with-aws · GitHub

## Overview (from Notion)
- Leveraging AI in cloud architecture can streamline processes, saving time for family and personal projects.
- Understanding AWS tools like Amazon Bedrock can enhance your capabilities as a software engineer, improving your business solutions.
- The emphasis on compliance and security aligns with the growing importance of data privacy, especially for family-related tech.
- Collaborative tools foster teamwork, which is essential in a startup environment, allowing for efficient project management.
- The integration of visual aids like Drawio can make complex ideas more accessible, useful for explaining tech concepts to non-technical family members.
- Alternate view: While automation is powerful, consider the human aspects of software engineering—team dynamics and mentoring can’t be replaced by AI.
- Balancing work with family life might be easier with tools that improve efficiency, enabling more quality time at home.

## AI Summary (from Notion)
The solution leverages Amazon Bedrock to enhance cloud architecture design by generating standardized patterns, optimizing resources, ensuring compliance, and automating tasks. Key AWS services used include Amazon ECR, S3, Lambda, and IAM. The setup involves cloning a repository, configuring environments, and deploying stacks with CDK. A Streamlit UI allows for executing architecture-related commands, and a manual setup option is available. The architecture sample is intended for learning and is not recommended for production use.

## Content (from Notion)

# AWS Architecture-Designer

## Leveraging Amazon Bedrock for Cloud Architecture Design

This pattern demonstrates how to leverage Generative AI to accelerate and optimize cloud architecture design processes. The solution enables architects and development teams to generate standardized architecture patterns, optimize resource configurations, ensure compliance, and create detailed documentation. The implementation utilizes Amazon Bedrock capabilities to access enterprise data, generate recommendations, and automate architecture-related tasks while maintaining security and compliance requirements. This solution uses the following AWS services:

- Amazon Bedrock for AI-powered assistance and automation
- Amazon ECR
- Amazon S3 for data storage
- AWS Lambda
- AWS IAM for security and access control
- Drawio for drawings
The pattern addresses common challenges in cloud architecture design, including:

- Accelerating architecture design processes
- Ensuring compliance with best practices
- Visualisation and guidence of architecture design with Drawio
- Optimizing resource utilization and costs
- Maintaining consistent documentation
- Enabling collaboration across teams
This solution is particularly valuable for organizations seeking to streamline their cloud architecture design process while maintaining high standards of quality and compliance. With the help of this tool you can:

- Generate an AWS architecture Design and drawing by either providing the technical requirements as a text or you can upload a Business Requirement Document by upload function to provide details.
- Generate Cloud formation Template based on the designed architecture
- Upload your architectural drawings and ask the tool for explaning the details of the architecture
- Estimate costs for the proposed architecture.
You can access the working demo of this pattern through: http://demo-1085524942.us-west-2.elb.amazonaws.com/

## Solution Architecture

## Prerequisites

- AWS CLI & CDK configured with appropriate permissions
- Docker installed and running
- Python 3.8 or later
- Node.js 14 or later (for CDK)
- npm install -g aws-cdk@latest
## Setup

1. Clone the repository:
```plain text
git clone git@github.com:aws-samples/sample-ai-powered-sdlc-patterns-with-aws.git

cd sample-ai-powered-sdlc-patterns-with-aws/design-and-architecture/design-solutionarchitecture-agent


```

1. Create and activate a virtual environment:
```plain text
 python3 -m venv venv
 source ./venv/bin/activate


```

1. Install dependencies:
```plain text
 cd functions/drawing_function/
 pip install -r requirements.txt


```

1. Before moving to cdk setup; In the functions/drawing_function folder, run below commands:
```plain text
   chmod +x make_pil_layer.sh
   chmod +x make_request_layer.sh
   ./make_pil_layer.sh
   ./make_request_layer.sh

```

1. Bootstrap your AWS environment (if not already done):
```plain text
cd ../../cdk/
pip install -r requirements.txt
cdk bootstrap


```

## Deployment

To deploy the stack:

```plain text
$ cdk deploy


```

- Note the Agent ID and S3 bucket name contains "satoolassetsbucket" in it and run the below commands accordingly:
Set environment variables

```plain text
export AWS_DEFAULT_REGION=us-west-2
export AGENT_ID= XXXXXXXX # WRITE YOUR BEDROCK AGENT ID
Aws configure # SET ALSO AWS CREDENTIALS


```

This will:

- Build and push the Docker image to ECR
- Create the Lambda function
- Set up the S3 bucket
- Create the Bedrock agent with the OpenAPI schema
## Useful commands

- cdk ls list all stacks in the app
- cdk synth emits the synthesized CloudFormation template
- cdk deploy deploy this stack to your default AWS account/region
- cdk diff compare deployed stack with current state
- cdk docs open CDK documentation
### Streamlit UI for AWS SA AGENT

Then, in any other terminal, navigate to the streamlit folder to run the Streamlit UI app and execute architecture-related commands.

```plain text

cd ../../streamlit/


```

Install Python dependencies

```plain text
pip install -r requirements.txt

```

Edit Enviroment Variables

- Edit the agent2_tools.py file and change the Agent ID.
- Edit the chatbot.py and change the Agent ID and S3 bucket name crated above
Run the Streamlit app:

```plain text
streamlit run chatbot.py


```

### Manual Setup

If you prefer to install everything manually, follow the steps outlined in the README-ManualSetup.md file.

## Clean up

Move to the cdk folder

```plain text
cd cdk

```

Run the following command to destroy the Amazon Q Application

```plain text
cdk destroy --all

```

## Security

See CONTRIBUTING for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

## Disclaimer

The solution architecture sample code is provided without any guarantees, and you're not recommended to use it for production-grade workloads. The intention is to provide content to build and learn. Be sure of reading the licensing terms.


