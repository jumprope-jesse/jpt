---
type: link
source: notion
url: https://github.com/microsoft/autogen
notion_type: Software Repo
tags: ['Running']
created: 2024-04-01T13:29:00.000Z
---

# GitHub - microsoft/autogen: A programming framework for agentic AI. Join our Discord: https://aka.ms/autogen-dc

## AI Summary (from Notion)
- Project Overview: AutoGen is a programming framework for agentic AI developed by Microsoft, focusing on multi-agent conversations for LLM applications.
- Key Features:
- Supports customizable and conversable agents that can communicate to solve tasks.
- Simplifies orchestration, automation, and optimization of complex LLM workflows.
- Enables enhanced LLM inference with functionalities like caching and error handling.
- Recent Highlights:
- Andrew Ng praised AutoGen during a talk at Sequoia Capital.
- Achieved No. 1 accuracy on the GAIA benchmark with its first multi-agent experiment.
- Highlighted as a top trending repo on GitHub in October 2023.
- Quickstart Instructions: Users can quickly start using AutoGen via GitHub Codespaces and specific setup steps.
- Installation Options: AutoGen can be installed in Docker or locally using Python, with minimal dependencies.
- Research Collaboration: Developed in collaboration with institutions like Penn State University and the University of Washington.
- Community and Contributions: Encourages contributions and has a dedicated Discord channel for community engagement.
- Legal Notices: The project is licensed under Creative Commons and MIT licenses, with guidelines on usage of Microsoft's trademarks.

## Content (from Notion)

# AutoGen

📚 Cite paper.

🔥 Mar 26: Andrew Ng gave a shoutout to AutoGen in What's next for AI agentic workflows at Sequoia Capital's AI Ascent.

🔥 Mar 3: What's new in AutoGen? 📰Blog; 📺Youtube.

🔥 Mar 1: the first AutoGen multi-agent experiment on the challenging GAIA benchmark achieved the No. 1 accuracy in all the three levels.

🎉 Jan 30: AutoGen is highlighted by Peter Lee in Microsoft Research Forum Keynote.

🎉 Dec 31: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework is selected by TheSequence: My Five Favorite AI Papers of 2023.

🎉 Nov 8: AutoGen is selected into Open100: Top 100 Open Source achievements 35 days after spinoff.

🎉 Nov 6: AutoGen is mentioned by Satya Nadella in a fireside chat.

🎉 Nov 1: AutoGen is the top trending repo on GitHub in October 2023.

🎉 Oct 03: AutoGen spins off from FLAML on GitHub and has a major paper update (first version on Aug 16).

🎉 Mar 29: AutoGen is first created in FLAML.

## What is AutoGen

AutoGen is a framework that enables the development of LLM applications using multiple agents that can converse with each other to solve tasks. AutoGen agents are customizable, conversable, and seamlessly allow human participation. They can operate in various modes that employ combinations of LLMs, human inputs, and tools.

- AutoGen enables building next-gen LLM applications based on multi-agent conversations with minimal effort. It simplifies the orchestration, automation, and optimization of a complex LLM workflow. It maximizes the performance of LLM models and overcomes their weaknesses.
- It supports diverse conversation patterns for complex workflows. With customizable and conversable agents, developers can use AutoGen to build a wide range of conversation patterns concerning conversation autonomy, the number of agents, and agent conversation topology.
- It provides a collection of working systems with different complexities. These systems span a wide range of applications from various domains and complexities. This demonstrates how AutoGen can easily support diverse conversation patterns.
- AutoGen provides enhanced LLM inference. It offers utilities like API unification and caching, and advanced usage patterns, such as error handling, multi-config inference, context programming, etc.
AutoGen is powered by collaborative research studies from Microsoft, Penn State University, and the University of Washington.

## Roadmaps

To see what we are working on and what we plan to work on, please check our Roadmap Issues.

## Quickstart

The easiest way to start playing is

1.  
1. 
1. 
NOTE: OAI_CONFIG_LIST_sample lists GPT-4 as the default model, as this represents our current recommendation, and is known to work well with AutoGen. If you use a model other than GPT-4, you may need to revise various system prompts (especially if using weaker models like GPT-3.5-turbo). Moreover, if you use models other than those hosted by OpenAI or Azure, you may incur additional risks related to alignment and safety. Proceed with caution if updating this default.

## Installation

### Option 1. Install and Run AutoGen in Docker

Find detailed instructions for users here, and for developers here.

### Option 2. Install AutoGen Locally

AutoGen requires Python version >= 3.8, < 3.13. It can be installed from pip:

```plain text
pip install pyautogen
```

Minimal dependencies are installed without extra options. You can install extra options based on the feature you need.

Find more options in Installation.

Even if you are installing and running AutoGen locally outside of docker, the recommendation and default behavior of agents is to perform code execution in docker. Find more instructions and how to change the default behaviour here.

For LLM inference configurations, check the FAQs.

## Multi-Agent Conversation Framework

Autogen enables the next-gen LLM applications with a generic multi-agent conversation framework. It offers customizable and conversable agents that integrate LLMs, tools, and humans. By automating chat among multiple capable agents, one can easily make them collectively perform tasks autonomously or with human feedback, including tasks that require using tools via code.

Features of this use case include:

- Multi-agent conversations: AutoGen agents can communicate with each other to solve tasks. This allows for more complex and sophisticated applications than would be possible with a single LLM.
- Customization: AutoGen agents can be customized to meet the specific needs of an application. This includes the ability to choose the LLMs to use, the types of human input to allow, and the tools to employ.
- Human participation: AutoGen seamlessly allows human participation. This means that humans can provide input and feedback to the agents as needed.
For example,

```plain text
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
# Load LLM inference endpoints from an env variable or a file
# See https://microsoft.github.io/autogen/docs/FAQ#set-your-api-endpoints
# and OAI_CONFIG_LIST_sample
config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")
# You can also set config_list directly as a list, for example, config_list = [{'model': 'gpt-4', 'api_key': '<your OpenAI API key here>'},]
assistant = AssistantAgent("assistant", llm_config={"config_list": config_list})
user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding", "use_docker": False}) # IMPORTANT: set to True to run code in docker, recommended
user_proxy.initiate_chat(assistant, message="Plot a chart of NVDA and TESLA stock price change YTD.")
# This initiates an automated chat between the two agents to solve the task
```

This example can be run with

```plain text
python test/twoagent.py
```

After the repo is cloned. The figure below shows an example conversation flow with AutoGen.

Alternatively, the sample code here allows a user to chat with an AutoGen agent in ChatGPT style. Please find more code examples for this feature.

## Enhanced LLM Inferences

Autogen also helps maximize the utility out of the expensive LLMs such as ChatGPT and GPT-4. It offers enhanced LLM inference with powerful functionalities like caching, error handling, multi-config inference and templating.

## Documentation

You can find detailed documentation about AutoGen here.

In addition, you can find:

- 
- 
- 
- 
## Related Papers

AutoGen

```plain text
@inproceedings{wu2023autogen,
      title={AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework},
      author={Qingyun Wu and Gagan Bansal and Jieyu Zhang and Yiran Wu and Beibin Li and Erkang Zhu and Li Jiang and Xiaoyun Zhang and Shaokun Zhang and Jiale Liu and Ahmed Hassan Awadallah and Ryen W White and Doug Burger and Chi Wang},
      year={2023},
      eprint={2308.08155},
      archivePrefix={arXiv},
      primaryClass={cs.AI}
}

```

EcoOptiGen

```plain text
@inproceedings{wang2023EcoOptiGen,
    title={Cost-Effective Hyperparameter Optimization for Large Language Model Generation Inference},
    author={Chi Wang and Susan Xueqing Liu and Ahmed H. Awadallah},
    year={2023},
    booktitle={AutoML'23},
}

```

MathChat

```plain text
@inproceedings{wu2023empirical,
    title={An Empirical Study on Challenging Math Problem Solving with GPT-4},
    author={Yiran Wu and Feiran Jia and Shaokun Zhang and Hangyu Li and Erkang Zhu and Yue Wang and Yin Tat Lee and Richard Peng and Qingyun Wu and Chi Wang},
    year={2023},
    booktitle={ArXiv preprint arXiv:2306.01337},
}

```

## Contributing

This project welcomes contributions and suggestions. Most contributions require you to agree to a Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

If you are new to GitHub, here is a detailed help source on getting involved with development on GitHub.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the Microsoft Open Source Code of Conduct. For more information, see the Code of Conduct FAQ or contact opencode@microsoft.com with any additional questions or comments.

## Contributors Wall

# Legal Notices

Microsoft and any contributors grant you a license to the Microsoft documentation and other content in this repository under the Creative Commons Attribution 4.0 International Public License, see the LICENSE file, and grant you a license to any code in the repository under the MIT License, see the LICENSE-CODE file.

Microsoft, Windows, Microsoft Azure, and/or other Microsoft products and services referenced in the documentation may be either trademarks or registered trademarks of Microsoft in the United States and/or other countries. The licenses for this project do not grant you rights to use any Microsoft names, logos, or trademarks. Microsoft's general trademark guidelines can be found at http://go.microsoft.com/fwlink/?LinkID=254653.

Privacy information can be found at https://privacy.microsoft.com/en-us/

Microsoft and any contributors reserve all other rights, whether under their respective copyrights, patents, or trademarks, whether by implication, estoppel, or otherwise.


