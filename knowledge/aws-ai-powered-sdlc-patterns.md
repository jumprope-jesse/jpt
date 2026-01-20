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

---

## Amazon CodeCatalyst + Amazon Q Task Breakdown

*Source: AWS What's New, April 2024*

Amazon Q in CodeCatalyst can analyze issues for complexity and propose splitting work into separate tasks.

### How It Works

1. Assign an issue to Amazon Q in CodeCatalyst
2. Amazon Q analyzes and summarizes issue complexity
3. For complex issues, suggests a list of smaller tasks
4. Each suggested task can be assigned to a user or back to Amazon Q

### Availability

- Currently limited to US West (Oregon) region
- Requires CodeCatalyst project/space

### Notes

- Interesting pattern: AI assesses its own ability to handle a task and breaks down what's too complex
- Similar concept to how modern coding agents (Claude Code, Cursor) handle complex tasks via subtasks

---

## Amazon CodeCatalyst Bedrock GenAI Chatbot Blueprint

*Source: AWS What's New, March 2024*

Blueprint for quickly building a generative AI chatbot with Amazon Bedrock and Anthropic's Claude.

### What It Does

- Creates a secure, login-protected LLM playground
- Includes source repo, sample code, CI/CD workflows, build/test reports, issue tracking
- Blueprint auto-updates with best practices and can regenerate relevant codebase parts

### Customization Options

- **Custom instructions** - Personalize chatbot behavior
- **External knowledge** - Connect documentation and code repositories
- **Knowledge base chatbot** - Build chatbot-driven knowledge bases on top of your docs

### Links

- [CodeCatalyst Documentation](https://docs.aws.amazon.com/codecatalyst/)
- [Bedrock GenAI Chatbot Blueprint docs](https://docs.aws.amazon.com/codecatalyst/latest/userguide/deploy-genai-rag-blueprint.html)

---

## Amazon CodeCatalyst Enterprise Tier & Custom Blueprints

*Source: https://aws.amazon.com/blogs/aws/amazon-codecatalyst-introduces-custom-blueprints-and-a-new-enterprise-tier/ - Added: November 2023*

Amazon CodeCatalyst enterprise tier offers advanced project management features including custom blueprints and project lifecycle management.

### Pricing

- **$20/user per month** (enterprise tier)
- Included resources per paying user:
  - 1,500 compute minutes
  - 160 Dev Environment hours
  - 64 GB Dev Environment storage

### Custom Blueprints

Define and codify best practices for:
- Application code structure
- Workflow definitions
- Infrastructure as code (IaC)
- CI/CD pipelines

**Key Features:**
- Publish blueprints to your CodeCatalyst space for project creation
- Apply standards to existing projects
- Automatic pull request updates when blueprints change
- Admin visibility into which projects use each blueprint

### How It Works

1. **Create Blueprint** - In CodeCatalyst console → Settings → Blueprints → Create blueprint
2. **Codify Best Practices** - Define project structure, workflows, IaC
3. **Publish** - Make available to teams in your space
4. **Use** - Create projects from blueprint or apply to existing projects
5. **Auto-Update** - Blueprint changes propagate as PRs to all projects using it

### Benefits

- **Rapid Setup** - Projects ready in minutes with integrated tools (repo, issues, CI/CD)
- **Consistency** - Best practices automatically applied across projects
- **Less DevOps Overhead** - Reduced time building/integrating/operating dev tools
- **Tool Flexibility** - Can swap in tools like GitHub while maintaining unified experience

### Availability

- US West (Oregon) and Europe (Ireland) Regions
- Can deploy to any commercial AWS Region

### Notes

This is interesting as an infrastructure-as-code approach to *project templates* themselves. The auto-update via PR mechanism is clever - it's like Dependabot but for organizational standards. Could be powerful for large orgs trying to maintain consistency across many microservices.
