---
type: link
source: notion
url: https://github.com/langroid/langroid
notion_type: Software Repo
tags: ['Running']
created: 2024-04-01T13:28:00.000Z
---

# GitHub - langroid/langroid: Harness LLMs with Multi-Agent Programming

## AI Summary (from Notion)
- Project Overview: Langroid is a Python framework for building applications powered by large language models (LLMs), developed by researchers from CMU and UW-Madison.

- Core Features:
- Multi-Agent Programming: Allows the creation of agents that can collaborate and exchange messages to solve problems.
- Simplified Developer Experience: Focuses on ease of use and does not rely on Langchain.
- Modular and Extensible: Users can create agents with specific functionalities and combine them flexibly.

- Installation: Requires Python 3.11+; can be installed via pip with optional packages for additional features.

- Usage Examples:
- Direct interaction with LLMs.
- Creating agents for specific tasks like document chatting and data querying from tables.

- Recent Updates: Regular updates with significant improvements, including support for local LLMs, enhanced performance, and new features for better user experience.

- Community Engagement: Encourages contributions and provides resources for documentation, examples, and community support via Discord.

- Consulting and Sponsorship: Offers consulting services for LLM applications and accepts sponsorship through GitHub.

- Interesting Fact: Langroid supports a wide range of LLMs, including local and remote options, with caching capabilities and integration with various vector stores for enhanced functionality.

## Content (from Notion)

###  Documentation ·  Examples Repo ·  Discord ·  Contributing 

Langroid is an intuitive, lightweight, extensible and principled Python framework to easily build LLM-powered applications, from ex-CMU and UW-Madison researchers. You set up Agents, equip them with optional components (LLM, vector-store and tools/functions), assign them tasks, and have them collaboratively solve a problem by exchanging messages. This Multi-Agent paradigm is inspired by the Actor Framework (but you do not need to know anything about this!).

Langroid is a fresh take on LLM app-development, where considerable thought has gone into simplifying the developer experience; it does not use Langchain.

🔥 See this Intro to Langroid blog post from the LanceDB team

We welcome contributions -- See the contributions document for ideas on what to contribute.

Are you building LLM Applications, or want help with Langroid for your company, or want to prioritize Langroid features for your company use-cases? Prasad Chalasani is available for consulting (advisory/development): pchalasani at gmail dot com.

Sponsorship is also accepted via GitHub Sponsors

Questions, Feedback, Ideas? Join us on Discord!

# Quick glimpse of coding with Langroid

This is just a teaser; there's much more, like function-calling/tools, Multi-Agent Collaboration, Structured Information Extraction, DocChatAgent (RAG), SQLChatAgent, non-OpenAI local/remote LLMs, etc. Scroll down or see docs for more. See the Langroid Quick-Start Colab that builds up to a 2-agent information-extraction example using the OpenAI ChatCompletion API. See also this version that uses the OpenAI Assistants API instead.

🔥 just released! Example script showing how you can use Langroid multi-agents and tools to extract structured information from a document using only a local LLM (Mistral-7b-instruct-v0.2).

```plain text
import langroid as lr
import langroid.language_models as lm

# set up LLM
llm_cfg = lm.OpenAIGPTConfig( # or OpenAIAssistant to use Assistant API
  # any model served via an OpenAI-compatible API
  chat_model=lm.OpenAIChatModel.GPT4_TURBO, # or, e.g., "ollama/mistral"
)
# use LLM directly
mdl = lm.OpenAIGPT(llm_cfg)
response = mdl.chat("What is the capital of Ontario?", max_tokens=10)

# use LLM in an Agent
agent_cfg = lr.ChatAgentConfig(llm=llm_cfg)
agent = lr.ChatAgent(agent_cfg)
agent.llm_response("What is the capital of China?")
response = agent.llm_response("And India?") # maintains conversation state

# wrap Agent in a Task to run interactive loop with user (or other agents)
task = lr.Task(agent, name="Bot", system_message="You are a helpful assistant")
task.run("Hello") # kick off with user saying "Hello"

# 2-Agent chat loop: Teacher Agent asks questions to Student Agent
teacher_agent = lr.ChatAgent(agent_cfg)
teacher_task = lr.Task(
  teacher_agent, name="Teacher",
  system_message="""
    Ask your student concise numbers questions, and give feedback.
    Start with a question.
    """
)
student_agent = lr.ChatAgent(agent_cfg)
student_task = lr.Task(
  student_agent, name="Student",
  system_message="Concisely answer the teacher's questions.",
  single_round=True,
)

teacher_task.add_sub_task(student_task)
teacher_task.run()
```

# 🔥 Updates/Releases

Click to expand

- Mar 2024: 
- Feb 2024: 
- Jan 2024: 
- Dec 2023: 
- Nov 2023: 
- Oct 2023: 
- Sep 2023: 
- Aug 2023: 
- July 2023: 
# 🚀 Demo

Suppose you want to extract structured information about the key terms of a commercial lease document. You can easily do this with Langroid using a two-agent system, as we show in the langroid-examples repo. (See this script for a version with the same functionality using a local Mistral-7b model.) The demo showcases just a few of the many features of Langroid, such as:

- Multi-agent collaboration: LeaseExtractor is in charge of the task, and its LLM (GPT4) generates questions to be answered by the DocAgent.
- Retrieval augmented question-answering, with source-citation: DocAgent LLM (GPT4) uses retrieval from a vector-store to answer the LeaseExtractor's questions, cites the specific excerpt supporting the answer.
- Function-calling (also known as tool/plugin): When it has all the information it needs, the LeaseExtractor LLM presents the information in a structured format using a Function-call.
Here is what it looks like in action (a pausable mp4 video is here).

# ⚡ Highlights

(For a more up-to-date list see the release section above)

- Agents as first-class citizens: The Agent class encapsulates LLM conversation state, and optionally a vector-store and tools. Agents are a core abstraction in Langroid; Agents act as message transformers, and by default provide 3 responder methods, one corresponding to each entity: LLM, Agent, User.
- Tasks: A Task class wraps an Agent, and gives the agent instructions (or roles, or goals), manages iteration over an Agent's responder methods, and orchestrates multi-agent interactions via hierarchical, recursive task-delegation. The Task.run() method has the same type-signature as an Agent's responder's methods, and this is key to how a task of an agent can delegate to other sub-tasks: from the point of view of a Task, sub-tasks are simply additional responders, to be used in a round-robin fashion after the agent's own responders.
- Modularity, Reusabilily, Loose coupling: The Agent and Task abstractions allow users to design Agents with specific skills, wrap them in Tasks, and combine tasks in a flexible way.
- LLM Support: Langroid supports OpenAI LLMs as well as LLMs from hundreds of providers (local/open or remote/commercial) via proxy libraries and local model servers such as LiteLLM that in effect mimic the OpenAI API.
- Caching of LLM responses: Langroid supports Redis and Momento to cache LLM responses.
- Vector-stores: LanceDB, Qdrant, Chroma are currently supported. Vector stores allow for Retrieval-Augmented-Generation (RAG).
- Grounding and source-citation: Access to external documents via vector-stores allows for grounding and source-citation.
- Observability, Logging, Lineage: Langroid generates detailed logs of multi-agent interactions and maintains provenance/lineage of messages, so that you can trace back the origin of a message.
- Tools/Plugins/Function-calling: Langroid supports OpenAI's recently released function calling feature. In addition, Langroid has its own native equivalent, which we call tools (also known as "plugins" in other contexts). Function calling and tools have the same developer-facing interface, implemented using Pydantic, which makes it very easy to define tools/functions and enable agents to use them. Benefits of using Pydantic are that you never have to write complex JSON specs for function calling, and when the LLM hallucinates malformed JSON, the Pydantic error message is sent back to the LLM so it can fix it!
# ⚙️ Installation and Setup

### Install langroid

Langroid requires Python 3.11+. We recommend using a virtual environment. Use pip to install langroid (from PyPi) to your virtual environment:

```plain text
pip install langroid
```

The core Langroid package lets you use OpenAI Embeddings models via their API. If you instead want to use the sentence-transformers embedding models from HuggingFace, install Langroid like this:

```plain text
pip install langroid[hf-embeddings]
```

If using zsh (or similar shells), you may need to escape the square brackets, e.g.:

```plain text
pip install langroid\[hf-embeddings\]

```

or use quotes:

```plain text
pip install "langroid[hf-embeddings]"

```

Optional Installs for using SQL Chat with a PostgreSQL DB

If you are using SQLChatAgent (e.g. the script examples/data-qa/sql-chat/sql_chat.py), with a postgres db, you will need to:

- Install PostgreSQL dev libraries for your platform, e.g. 
- Install langroid with the postgres extra, e.g. pip install langroid[postgres] or poetry add langroid[postgres] or poetry install -E postgres. If this gives you an error, try pip install psycopg2-binary in your virtualenv.
### Set up environment variables (API keys, etc)

To get started, all you need is an OpenAI API Key. If you don't have one, see this OpenAI Page. Currently only OpenAI models are supported. Others will be added later (Pull Requests welcome!).

In the root of the repo, copy the .env-template file to a new file .env:

```plain text
cp .env-template .env
```

Then insert your OpenAI API Key. Your .env file should look like this (the organization is optional but may be required in some scenarios).

```plain text
OPENAI_API_KEY=your-key-here-without-quotes
OPENAI_ORGANIZATION=optionally-your-organization-id
```

Alternatively, you can set this as an environment variable in your shell (you will need to do this every time you open a new shell):

```plain text
export OPENAI_API_KEY=your-key-here-without-quotes
```

Optional Setup Instructions (click to expand)

All of the following environment variable settings are optional, and some are only needed to use specific features (as noted below).

- Qdrant Vector Store API Key, URL. This is only required if you want to use Qdrant cloud. The default vector store in our RAG agent (DocChatAgent) is LanceDB which uses file storage, and you do not need to set up any environment variables for that. Alternatively Chroma is also currently supported. We use the local-storage version of Chroma, so there is no need for an API key.
- Redis Password, host, port: This is optional, and only needed to cache LLM API responses using Redis Cloud. Redis offers a free 30MB Redis account which is more than sufficient to try out Langroid and even beyond. If you don't set up these, Langroid will use a pure-python Redis in-memory cache via the Fakeredis library.
- Momento Serverless Caching of LLM API responses (as an alternative to Redis). To use Momento instead of Redis: 
- GitHub Personal Access Token (required for apps that need to analyze git repos; token-based API calls are less rate-limited). See this GitHub page.
- Google Custom Search API Credentials: Only needed to enable an Agent to use the GoogleSearchTool. To use Google Search as an LLM Tool/Plugin/function-call, you'll need to set up a Google API key, then setup a Google Custom Search Engine (CSE) and get the CSE ID. (Documentation for these can be challenging, we suggest asking GPT4 for a step-by-step guide.) After obtaining these credentials, store them as values of GOOGLE_API_KEY and GOOGLE_CSE_ID in your .env file. Full documentation on using this (and other such "stateless" tools) is coming soon, but in the meantime take a peek at this chat example, which shows how you can easily equip an Agent with a GoogleSearchtool.
If you add all of these optional variables, your .env file should look like this:

```plain text
OPENAI_API_KEY=your-key-here-without-quotes
GITHUB_ACCESS_TOKEN=your-personal-access-token-no-quotes
CACHE_TYPE=redis # or momento
REDIS_PASSWORD=your-redis-password-no-quotes
REDIS_HOST=your-redis-hostname-no-quotes
REDIS_PORT=your-redis-port-no-quotes
MOMENTO_AUTH_TOKEN=your-momento-token-no-quotes # instead of REDIS* variables
QDRANT_API_KEY=your-key
QDRANT_API_URL=https://your.url.here:6333 # note port number must be included
GOOGLE_API_KEY=your-key
GOOGLE_CSE_ID=your-cse-id
```

Optional setup instructions for Microsoft Azure OpenAI(click to expand)

When using Azure OpenAI, additional environment variables are required in the .env file. This page Microsoft Azure OpenAI provides more information, and you can set each environment variable as follows:

- AZURE_OPENAI_API_KEY, from the value of API_KEY
- AZURE_OPENAI_API_BASE from the value of ENDPOINT, typically looks like https://your.domain.azure.com.
- For AZURE_OPENAI_API_VERSION, you can use the default value in .env-template, and latest version can be found here
- AZURE_OPENAI_DEPLOYMENT_NAME is the name of the deployed model, which is defined by the user during the model setup
- AZURE_OPENAI_MODEL_NAME Azure OpenAI allows specific model names when you select the model for your deployment. You need to put precisly the exact model name that was selected. For example, GPT-3.5 (should be gpt-35-turbo-16k or gpt-35-turbo) or GPT-4 (should be gpt-4-32k or gpt-4).
- AZURE_OPENAI_MODEL_VERSION is required if AZURE_OPENAI_MODEL_NAME = gpt=4, which will assist Langroid to determine the cost of the model
# 🐳 Docker Instructions

We provide a containerized version of the langroid-examples repository via this Docker Image. All you need to do is set up environment variables in the .env file. Please follow these steps to setup the container:

```plain text
# get the .env file template from `langroid` repo
wget -O .env https://raw.githubusercontent.com/langroid/langroid/main/.env-template

# Edit the .env file with your favorite editor (here nano), and remove any un-used settings. E.g. there are "dummy" values like "your-redis-port" etc -- if you are not using them, you MUST remove them.
nano .env

# launch the container
docker run -it --rm  -v ./.env:/langroid/.env langroid/langroid

# Use this command to run any of the scripts in the `examples` directory
python examples/<Path/To/Example.py>
```

# 🎉 Usage Examples

These are quick teasers to give a glimpse of what you can do with Langroid and how your code would look.

⚠️ The code snippets below are intended to give a flavor of the code and they are not complete runnable examples! For that we encourage you to consult the langroid-examples repository.

ℹ️ The various LLM prompts and instructions in Langroid have been tested to work well with GPT4. Switching to GPT3.5-Turbo is easy via a config flag (e.g., cfg = OpenAIGPTConfig(chat_model=OpenAIChatModel.GPT3_5_TURBO)), and may suffice for some applications, but in general you may see inferior results.

📖 Also see the Getting Started Guide for a detailed tutorial.

Click to expand any of the code examples below. All of these can be run in a Colab notebook:

 Direct interaction with OpenAI LLM 

```plain text
import langroid.language_models as lm

mdl = lm.OpenAIGPT()

messages = [
  lm.LLMMessage(content="You are a helpful assistant",  role=lm.Role.SYSTEM),
  lm.LLMMessage(content="What is the capital of Ontario?",  role=lm.Role.USER),
]

response = mdl.chat(messages, max_tokens=200)
print(response.message)
```

 Interaction with non-OpenAI LLM (local or remote)   Local model: if model is served at `http://localhost:8000`:

```plain text
cfg = lm.OpenAIGPTConfig(
  chat_model="local/localhost:8000",
  chat_context_length=4096
)
mdl = lm.OpenAIGPT(cfg)
# now interact with it as above, or create an Agent + Task as shown below.
```

If the model is supported by liteLLM, then no need to launch the proxy server. Just set the chat_model param above to litellm/[provider]/[model], e.g. litellm/anthropic/claude-instant-1 and use the config object as above. Note that to use litellm you need to install langroid with the litellm extra: poetry install -E litellm or pip install langroid[litellm]. For remote models, you will typically need to set API Keys etc as environment variables. You can set those based on the LiteLLM docs. If any required environment variables are missing, Langroid gives a helpful error message indicating which ones are needed. Note that to use langroid with litellm you need to install the litellm extra, i.e. either pip install langroid[litellm] in your virtual env, or if you are developing within the langroid repo, poetry install -E litellm.

```plain text
pip install langroid[litellm]
```

 Define an agent, set up a task, and run it 

```plain text
import langroid as lr

agent = lr.ChatAgent()

# get response from agent's LLM, and put this in an interactive loop...
# answer = agent.llm_response("What is the capital of Ontario?")
  # ... OR instead, set up a task (which has a built-in loop) and run it
task = lr.Task(agent, name="Bot")
task.run() # ... a loop seeking response from LLM or User at each turn
```

 Three communicating agents

A toy numbers game, where when given a number n:

- repeater_task's LLM simply returns n,
- even_task's LLM returns n/2 if n is even, else says "DO-NOT-KNOW"
- odd_task's LLM returns 3*n+1 if n is odd, else says "DO-NOT-KNOW"
Each of these Tasks automatically configures a default ChatAgent.

```plain text
import langroid as lr
from langroid.utils.constants import NO_ANSWER

repeater_task = lr.Task(
    name = "Repeater",
    system_message="""
    Your job is to repeat whatever number you receive.
    """,
    llm_delegate=True, # LLM takes charge of task
    single_round=False,
)

even_task = lr.Task(
    name = "EvenHandler",
    system_message=f"""
    You will be given a number.
    If it is even, divide by 2 and say the result, nothing else.
    If it is odd, say {NO_ANSWER}
    """,
    single_round=True,  # task done after 1 step() with valid response
)

odd_task = lr.Task(
    name = "OddHandler",
    system_message=f"""
    You will be given a number n.
    If it is odd, return (n*3+1), say nothing else.
    If it is even, say {NO_ANSWER}
    """,
    single_round=True,  # task done after 1 step() with valid response
)
```

Then add the even_task and odd_task as sub-tasks of repeater_task, and run the repeater_task, kicking it off with a number as input:

```plain text
repeater_task.add_sub_task([even_task, odd_task])
repeater_task.run("3")
```

 Simple Tool/Function-calling example

Langroid leverages Pydantic to support OpenAI's Function-calling API as well as its own native tools. The benefits are that you don't have to write any JSON to specify the schema, and also if the LLM hallucinates a malformed tool syntax, Langroid sends the Pydantic validation error (suitably sanitized) to the LLM so it can fix it!

Simple example: Say the agent has a secret list of numbers, and we want the LLM to find the smallest number in the list. We want to give the LLM a probe tool/function which takes a single number n as argument. The tool handler method in the agent returns how many numbers in its list are at most n.

First define the tool using Langroid's ToolMessage class:

```plain text
import langroid as lr

class ProbeTool(lr.agent.ToolMessage):
  request: str = "probe" # specifies which agent method handles this tool
  purpose: str = """
        To find how many numbers in my list are less than or equal to
        the <number> you specify.
        """ # description used to instruct the LLM on when/how to use the tool
  number: int  # required argument to the tool
```

Then define a SpyGameAgent as a subclass of ChatAgent, with a method probe that handles this tool:

```plain text
class SpyGameAgent(lr.ChatAgent):
  def __init__(self, config: lr.ChatAgentConfig):
    super().__init__(config)
    self.numbers = [3, 4, 8, 11, 15, 25, 40, 80, 90]

  def probe(self, msg: ProbeTool) -> str:
    # return how many numbers in self.numbers are less or equal to msg.number
    return str(len([n for n in self.numbers if n <= msg.number]))
```

We then instantiate the agent and enable it to use and respond to the tool:

```plain text
spy_game_agent = SpyGameAgent(
    lr.ChatAgentConfig(
        name="Spy",
        vecdb=None,
        use_tools=False, #  don't use Langroid native tool
        use_functions_api=True, # use OpenAI function-call API
    )
)
spy_game_agent.enable_message(ProbeTool)
```

For a full working example see the chat-agent-tool.py script in the langroid-examples repo.

Tool/Function-calling to extract structured information from text 

Suppose you want an agent to extract the key terms of a lease, from a lease document, as a nested JSON structure. First define the desired structure via Pydantic models:

```plain text
from pydantic import BaseModel
class LeasePeriod(BaseModel):
    start_date: str
    end_date: str


class LeaseFinancials(BaseModel):
    monthly_rent: str
    deposit: str

class Lease(BaseModel):
    period: LeasePeriod
    financials: LeaseFinancials
    address: str
```

Then define the LeaseMessage tool as a subclass of Langroid's ToolMessage. Note the tool has a required argument terms of type Lease:

```plain text
import langroid as lr

class LeaseMessage(lr.agent.ToolMessage):
    request: str = "lease_info"
    purpose: str = """
        Collect information about a Commercial Lease.
        """
    terms: Lease
```

Then define a LeaseExtractorAgent with a method lease_info that handles this tool, instantiate the agent, and enable it to use and respond to this tool:

```plain text
class LeaseExtractorAgent(lr.ChatAgent):
    def lease_info(self, message: LeaseMessage) -> str:
        print(
            f"""
        DONE! Successfully extracted Lease Info:
        {message.terms}
        """
        )
        return json.dumps(message.terms.dict())

lease_extractor_agent = LeaseExtractorAgent()
lease_extractor_agent.enable_message(LeaseMessage)
```

See the chat_multi_extract.py script in the langroid-examples repo for a full working example.

 Chat with documents (file paths, URLs, etc)

Langroid provides a specialized agent class DocChatAgent for this purpose. It incorporates document sharding, embedding, storage in a vector-DB, and retrieval-augmented query-answer generation. Using this class to chat with a collection of documents is easy. First create a DocChatAgentConfig instance, with a doc_paths field that specifies the documents to chat with.

```plain text
import langroid as lr
from langroid.agent.special import DocChatAgentConfig, DocChatAgent

config = DocChatAgentConfig(
  doc_paths = [
    "https://en.wikipedia.org/wiki/Language_model",
    "https://en.wikipedia.org/wiki/N-gram_language_model",
    "/path/to/my/notes-on-language-models.txt",
  ],
  vecdb=lr.vector_store.LanceDBConfig(),
)
```

Then instantiate the DocChatAgent (this ingests the docs into the vector-store):

```plain text
agent = DocChatAgent(config)
```

Then we can either ask the agent one-off questions,

```plain text
agent.llm_response("What is a language model?")
```

or wrap it in a Task and run an interactive loop with the user:

```plain text
task = lr.Task(agent)
task.run()
```

See full working scripts in the docqa folder of the langroid-examples repo.

 🔥 Chat with tabular data (file paths, URLs, dataframes)

Using Langroid you can set up a TableChatAgent with a dataset (file path, URL or dataframe), and query it. The Agent's LLM generates Pandas code to answer the query, via function-calling (or tool/plugin), and the Agent's function-handling method executes the code and returns the answer.

Here is how you can do this:

```plain text
import langroid as lr
from langroid.agent.special import TableChatAgent, TableChatAgentConfig
```

Set up a TableChatAgent for a data file, URL or dataframe (Ensure the data table has a header row; the delimiter/separator is auto-detected):

```plain text
dataset =  "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
# or dataset = "/path/to/my/data.csv"
# or dataset = pd.read_csv("/path/to/my/data.csv")
agent = TableChatAgent(
    config=TableChatAgentConfig(
        data=dataset,
    )
)
```

Set up a task, and ask one-off questions like this:

```plain text
task = lr.Task(
  agent,
  name = "DataAssistant",
  default_human_response="", # to avoid waiting for user input
)
result = task.run(
  "What is the average alcohol content of wines with a quality rating above 7?",
  turns=2 # return after user question, LLM fun-call/tool response, Agent code-exec result
)
print(result.content)
```

Or alternatively, set up a task and run it in an interactive loop with the user:

```plain text
task = lr.Task(agent, name="DataAssistant")
task.run()
```

For a full working example see the table_chat.py script in the langroid-examples repo.

# ❤️ Thank you to our supporters

If you like this project, please give it a star ⭐ and 📢 spread the word in your network or social media:

Your support will help build Langroid's momentum and community.

# Langroid Co-Founders

- Prasad Chalasani (IIT BTech/CS, CMU PhD/ML; Independent ML Consultant)
- Somesh Jha (IIT BTech/CS, CMU PhD/CS; Professor of CS, U Wisc at Madison)

