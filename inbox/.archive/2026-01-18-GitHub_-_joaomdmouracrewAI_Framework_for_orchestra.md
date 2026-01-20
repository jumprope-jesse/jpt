---
type: link
source: notion
url: https://github.com/joaomdmoura/crewAI
notion_type: Software Repo
tags: ['Running']
created: 2024-04-01T13:22:00.000Z
---

# GitHub - joaomdmoura/crewAI: Framework for orchestrating role-playing, autonomous AI agents. By fostering collaborative intelligence, CrewAI empowers agents to work together seamlessly, tackling complex tasks.

## Overview (from Notion)
- CrewAI could streamline your projects by allowing multiple AI agents to collaborate, making your workflow more efficient as a software engineer and founder.
- The platform enables role-based task management, which can help in delegating tasks effectively, freeing up your time for family and personal interests.
- Unique design allows AI agents to autonomously communicate, simulating a team environment that mirrors real-world collaboration—beneficial for innovative project development.
- Consider how this AI-driven collaboration could enhance your startup's productivity, possibly leading to faster product iterations.
- Alternate views: while embracing AI collaboration, some might worry about dependency on technology or the potential loss of personal touch in team dynamics.
- Reflect on how adopting such technology could influence your parenting style—teaching your kids about AI and its applications in everyday life.

## AI Summary (from Notion)
CrewAI is an advanced framework for orchestrating role-playing, autonomous AI agents, enabling them to collaborate effectively on complex tasks. Key features include role-based agent design, autonomous task delegation, and flexible task management. Users can install CrewAI via pip, set up agents with specific roles, and utilize various models for enhanced functionality. The framework supports open-source models and emphasizes dynamic processes for production environments, making it adaptable for various applications like smart assistants and automated services.

## Content (from Notion)

# crewAI

🤖 crewAI: Cutting-edge framework for orchestrating role-playing, autonomous AI agents. By fostering collaborative intelligence, CrewAI empowers agents to work together seamlessly, tackling complex tasks.

### Homepage | Documentation | Chat with Docs | Examples | Discord

## Table of contents

- Why CrewAI?
- Getting Started
- Key Features
- Examples 
- Connecting Your Crew to a Model
- How CrewAI Compares
- Contribution
- Hire CrewAI
- Telemetry
- License
## Why CrewAI?

The power of AI collaboration has too much to offer. CrewAI is designed to enable AI agents to assume roles, share goals, and operate in a cohesive unit - much like a well-oiled crew. Whether you're building a smart assistant platform, an automated customer service ensemble, or a multi-agent research team, CrewAI provides the backbone for sophisticated multi-agent interactions.

## Getting Started

To get started with CrewAI, follow these simple steps:

### 1. Installation

```plain text
pip install crewai
```

If you want to also install crewai-tools, which is a package with tools that can be used by the agents, but more dependencies, you can install it with, example bellow uses it:

```plain text
pip install 'crewai[tools]'
```

### 2. Setting Up Your Crew

```plain text
import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool

os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY"
os.environ["SERPER_API_KEY"] = "Your Key" # serper.dev API key

# You can choose to use a local model through Ollama for example. See https://docs.crewai.com/how-to/LLM-Connections/ for more information.

# os.environ["OPENAI_API_BASE"] = 'http://localhost:11434/v1'
# os.environ["OPENAI_MODEL_NAME"] ='openhermes'  # Adjust based on available model
# os.environ["OPENAI_API_KEY"] ='sk-111111111111111111111111111111111111111111111111'

search_tool = SerperDevTool()

# Define your agents with roles and goals
researcher = Agent(
  role='Senior Research Analyst',
  goal='Uncover cutting-edge developments in AI and data science',
  backstory="""You work at a leading tech think tank.
  Your expertise lies in identifying emerging trends.
  You have a knack for dissecting complex data and presenting actionable insights.""",
  verbose=True,
  allow_delegation=False,
  tools=[search_tool]
  # You can pass an optional llm attribute specifying what mode you wanna use.
  # It can be a local model through Ollama / LM Studio or a remote
  # model like OpenAI, Mistral, Antrophic or others (https://docs.crewai.com/how-to/LLM-Connections/)
  #
  # import os
  # os.environ['OPENAI_MODEL_NAME'] = 'gpt-3.5-turbo'
  #
  # OR
  #
  # from langchain_openai import ChatOpenAI
  # llm=ChatOpenAI(model_name="gpt-3.5", temperature=0.7)
)
writer = Agent(
  role='Tech Content Strategist',
  goal='Craft compelling content on tech advancements',
  backstory="""You are a renowned Content Strategist, known for your insightful and engaging articles.
  You transform complex concepts into compelling narratives.""",
  verbose=True,
  allow_delegation=True
)

# Create tasks for your agents
task1 = Task(
  description="""Conduct a comprehensive analysis of the latest advancements in AI in 2024.
  Identify key trends, breakthrough technologies, and potential industry impacts.""",
  expected_output="Full analysis report in bullet points",
  agent=researcher
)

task2 = Task(
  description="""Using the insights provided, develop an engaging blog
  post that highlights the most significant AI advancements.
  Your post should be informative yet accessible, catering to a tech-savvy audience.
  Make it sound cool, avoid complex words so it doesn't sound like AI.""",
  expected_output="Full blog post of at least 4 paragraphs",
  agent=writer
)

# Instantiate your crew with a sequential process
crew = Crew(
  agents=[researcher, writer],
  tasks=[task1, task2],
  verbose=2, # You can set it to 1 or 2 to different logging levels
)

# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result)
```

In addition to the sequential process, you can use the hierarchical process, which automatically assigns a manager to the defined crew to properly coordinate the planning and execution of tasks through delegation and validation of results. See more about the processes here.

## Key Features

- Role-Based Agent Design: Customize agents with specific roles, goals, and tools.
- Autonomous Inter-Agent Delegation: Agents can autonomously delegate tasks and inquire amongst themselves, enhancing problem-solving efficiency.
- Flexible Task Management: Define tasks with customizable tools and assign them to agents dynamically.
- Processes Driven: Currently only supports sequential task execution and hierarchical processes, but more complex processes like consensual and autonomous are being worked on.
- Save output as file: Save the output of individual tasks as a file, so you can use it later.
- Parse output as Pydantic or Json: Parse the output of individual tasks as a Pydantic model or as a Json if you want to.
- Works with Open Source Models: Run your crew using Open AI or open source models refer to the Connect crewAI to LLMs page for details on configuring your agents' connections to models, even ones running locally!
## Examples

You can test different real life examples of AI crews in the crewAI-examples repo:

- Landing Page Generator
- Having Human input on the execution
- Trip Planner
- Stock Analysis
### Quick Tutorial

### Write Job Descriptions

Check out code for this example or watch a video below:

### Trip Planner

Check out code for this example or watch a video below:

### Stock Analysis

Check out code for this example or watch a video below:

## Connecting Your Crew to a Model

crewAI supports using various LLMs through a variety of connection options. By default your agents will use the OpenAI API when querying the model. However, there are several other ways to allow your agents to connect to models. For example, you can configure your agents to use a local model via the Ollama tool.

Please refer to the Connect crewAI to LLMs page for details on configuring you agents' connections to models.

## How CrewAI Compares

- 
- 
CrewAI's Advantage: CrewAI is built with production in mind. It offers the flexibility of Autogen's conversational agents and the structured process approach of ChatDev, but without the rigidity. CrewAI's processes are designed to be dynamic and adaptable, fitting seamlessly into both development and production workflows.

## Contribution

CrewAI is open-source and we welcome contributions. If you're looking to contribute, please:

- Fork the repository.
- Create a new branch for your feature.
- Add your feature or improvement.
- Send a pull request.
- We appreciate your input!
### Installing Dependencies

```plain text
poetry lock
poetry install
```

### Virtual Env

```plain text
poetry shell
```

### Pre-commit hooks

```plain text
pre-commit install
```

### Running Tests

```plain text
poetry run pytest
```

### Running static type checks

```plain text
poetry run pyright
```

### Packaging

```plain text
poetry build
```

### Installing Locally

```plain text
pip install dist/*.tar.gz
```

## Hire CrewAI

We're a company developing crewAI and crewAI Enterprise, we for a limited time are offer consulting with selected customers, to get them early access to our enterprise solution If you are interested on having access to it and hiring weekly hours with our team, feel free to email us at joao@crewai.com.

## Telemetry

CrewAI uses anonymous telemetry to collect usage data with the main purpose of helping us improve the library by focusing our efforts on the most used features, integrations and tools.

There is NO data being collected on the prompts, tasks descriptions agents backstories or goals nor tools usage, no API calls, nor responses nor any data that is being processed by the agents, nor any secrets and env vars.

Data collected includes:

- Version of crewAI 
- Version of Python 
- General OS (e.g. number of CPUs, macOS/Windows/Linux) 
- Number of agents and tasks in a crew 
- Crew Process being used 
- If Agents are using memory or allowing delegation 
- If Tasks are being executed in parallel or sequentially 
- Language model being used 
- Roles of agents in a crew 
- Tools names available 
Users can opt-in sharing the complete telemetry data by setting the share_crew attribute to True on their Crews.

## License

CrewAI is released under the MIT License.


