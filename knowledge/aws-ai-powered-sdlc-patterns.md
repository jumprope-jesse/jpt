# AWS AI-Powered SDLC Patterns

*Source: https://github.com/aws-samples/sample-ai-powered-sdlc-patterns-with-aws*

A collection of patterns demonstrating how to integrate generative AI into different stages of the software development lifecycle using Amazon Q Developer, Amazon Q Business, and Amazon Bedrock.

## Key AWS Services Used

- Amazon Q Developer
- Amazon Q Business
- Amazon Bedrock

## Pattern Categories (by SDLC Phase)

1. **Requirement & Planning**
2. **Design & Architecture**
3. **Implementation**
4. **Testing**
5. **Deployment**
6. **Operation & Maintenance**

## Quick Start

```bash
git clone https://github.com/aws-samples/sample-ai-powered-sdlc-patterns-with-aws
# Each subdirectory contains additional installation and usage instructions
```

## Notes

- Sample code for learning - not recommended for production workloads
- AWS costs apply - check pricing for services used
- MIT-0 License

---

## Design & Architecture Pattern: Solution Architecture Agent

AI-powered tools for cloud architecture design using Amazon Bedrock.

## AWS Architecture-Designer Sample

*Source: https://github.com/aws-samples/sample-ai-powered-sdlc-patterns-with-aws/tree/main/design-and-architecture/design-solutionarchitecture-agent - Added: 2026-01-18*

A pattern from AWS samples demonstrating how to use GenAI for cloud architecture design. Part of the broader "AI-powered SDLC patterns with AWS" collection.

### Capabilities

- **Architecture Generation** - Generate AWS architecture designs from text requirements or uploaded Business Requirement Documents
- **Diagram Creation** - Creates Drawio architecture diagrams
- **CloudFormation Templates** - Generate infrastructure-as-code from designed architecture
- **Architecture Analysis** - Upload existing diagrams and get explanations
- **Cost Estimation** - Estimate costs for proposed architectures

### AWS Services Used

- Amazon Bedrock - AI agent powering the core functionality
- Amazon ECR - Container registry for the app
- Amazon S3 - Data storage
- AWS Lambda - Serverless compute
- AWS IAM - Security and access control
- Drawio - Architecture diagrams

### Tech Stack

- CDK for deployment
- Streamlit for the UI
- Python 3.8+
- Docker

### Quick Setup

```bash
# Clone and navigate
git clone git@github.com:aws-samples/sample-ai-powered-sdlc-patterns-with-aws.git
cd sample-ai-powered-sdlc-patterns-with-aws/design-and-architecture/design-solutionarchitecture-agent

# Virtual environment
python3 -m venv venv
source ./venv/bin/activate

# Install dependencies
cd functions/drawing_function/
pip install -r requirements.txt

# Make layer scripts executable
chmod +x make_pil_layer.sh make_request_layer.sh
./make_pil_layer.sh
./make_request_layer.sh

# Deploy with CDK
cd ../../cdk/
pip install -r requirements.txt
cdk bootstrap
cdk deploy

# Run Streamlit UI
cd ../streamlit/
pip install -r requirements.txt
# Edit agent2_tools.py and chatbot.py with your Agent ID
streamlit run chatbot.py
```

### Notes

- Sample code - not for production use
- Demo available at: http://demo-1085524942.us-west-2.elb.amazonaws.com/
- Part of a larger AI-powered SDLC patterns repository worth exploring
- The idea of generating architecture diagrams + CloudFormation from requirements is interesting for prototyping

### Related Patterns

The parent repo `sample-ai-powered-sdlc-patterns-with-aws` likely contains other useful patterns for AI-assisted development workflows worth exploring.
