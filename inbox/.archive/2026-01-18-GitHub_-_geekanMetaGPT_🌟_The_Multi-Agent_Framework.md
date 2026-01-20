---
type: link
source: notion
url: https://github.com/geekan/MetaGPT
notion_type: Software Repo
tags: ['Running']
created: 2024-04-01T13:29:00.000Z
---

# GitHub - geekan/MetaGPT: 🌟 The Multi-Agent Framework: First AI Software Company, Towards Natural Language Programming

## AI Summary (from Notion)
- Project Overview: MetaGPT is a multi-agent framework designed to enhance software development by assigning various roles to AI agents (GPTs) for collaborative tasks.

- Key Features:
- Takes a single line requirement and generates comprehensive outputs like user stories, data structures, and APIs.
- Incorporates roles such as product managers, architects, and engineers to simulate a full software company environment.
- Emphasizes the importance of standard operating procedures (SOPs) in team collaboration.

- Recent Developments:
- Several versions released, introducing features like multi-language support, data interpretation, and improvements in LLM integration.
- The framework was recognized in the top 100 open source achievements and has gained significant popularity on GitHub.

- Installation and Usage:
- Easy installation via pip or GitHub.
- Configurable settings for different LLMs and API integrations.
- Can be used through command line interface or as a library in Python scripts.

- Community and Support:
- Encourages users to join their Discord channel for community engagement.
- Provides contact information for feedback and inquiries.

- Research and Citation:
- Papers on MetaGPT and its Data Interpreter have been submitted and accepted for presentations, highlighting its innovative approach in AI and software development.

- Interesting Fact: MetaGPT has topped GitHub Trending Monthly multiple times and is recognized for its contributions to open-source software development.

## Content (from Notion)

# MetaGPT: The Multi-Agent Framework

Assign different roles to GPTs to form a collaborative entity for complex tasks.

## News

🚀 Mar. 14, 2024: Our Data Interpreter paper is on arxiv. Check the example and code!

🚀 Feb. 08, 2024: v0.7.0 released, supporting assigning different LLMs to different Roles. We also introduced Data Interpreter, a powerful agent capable of solving a wide range of real-world problems.

🚀 Jan. 16, 2024: Our paper MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework  accepted for oral presentation (top 1.2%) at ICLR 2024, ranking #1 in the LLM-based Agent category.

🚀 Jan. 03, 2024: v0.6.0 released, new features include serialization, upgraded OpenAI package and supported multiple LLM, provided minimal example for debate etc.

🚀 Dec. 15, 2023: v0.5.0 released, introducing some experimental features such as incremental development, multilingual, multiple programming languages, etc.

🔥 Nov. 08, 2023: MetaGPT is selected into Open100: Top 100 Open Source achievements.

🔥 Sep. 01, 2023: MetaGPT tops GitHub Trending Monthly for the 17th time in August 2023.

🌟 Jun. 30, 2023: MetaGPT is now open source.

🌟 Apr. 24, 2023: First line of MetaGPT code committed.

## Software Company as Multi-Agent System

1. MetaGPT takes a one line requirement as input and outputs user stories / competitive analysis / requirements / data structures / APIs / documents, etc.
1. Internally, MetaGPT includes product managers / architects / project managers / engineers. It provides the entire process of a software company along with carefully orchestrated SOPs. 
Software Company Multi-Agent Schematic (Gradually Implementing)

## Get Started

### Installation

> 

```plain text
pip install --upgrade metagpt
# or `pip install --upgrade git+https://github.com/geekan/MetaGPT.git`
# or `git clone https://github.com/geekan/MetaGPT && cd MetaGPT && pip install --upgrade -e .`
```

For detailed installation guidance, please refer to cli_install or docker_install

### Configuration

You can init the config of MetaGPT by running the following command, or manually create ~/.metagpt/config2.yaml file:

```plain text
# Check https://docs.deepwisdom.ai/main/en/guide/get_started/configuration.html for more details
metagpt --init-config  # it will create ~/.metagpt/config2.yaml, just modify it to your needs
```

You can configure ~/.metagpt/config2.yaml according to the example and doc:

```plain text
llm:
  api_type: "openai"  # or azure / ollama / open_llm etc. Check LLMType for more options
  model: "gpt-4-turbo-preview"  # or gpt-3.5-turbo-1106 / gpt-4-1106-preview
  base_url: "https://api.openai.com/v1"  # or forward url / other llm url
  api_key: "YOUR_API_KEY"
```

### Usage

After installation, you can use MetaGPT at CLI

```plain text
metagpt "Create a 2048 game"  # this will create a repo in ./workspace
```

or use it as library

```plain text
from metagpt.software_company import generate_repo, ProjectRepo
repo: ProjectRepo = generate_repo("Create a 2048 game")  # or ProjectRepo("<path>")
print(repo)  # it will print the repo structure with files
```

You can also use its Data Interpreter

```plain text
import asyncio
from metagpt.roles.di.data_interpreter import DataInterpreter

async def main():
    di = DataInterpreter()
    await di.run("Run data analysis on sklearn Iris dataset, include a plot")

asyncio.run(main())  # or await main() in a jupyter notebook setting
```

### QuickStart & Demo Video

- Try it on MetaGPT Huggingface Space
- Matthew Berman: How To Install MetaGPT - Build A Startup With One Prompt!!
- Official Demo Video
customized_tasks_by_MetaGPT_v2.mp4

## Tutorial

- 🗒 Online Document
- 💻 Usage
- 🔎 What can MetaGPT do?
- 🛠 How to build your own agents? 
- 🧑‍💻 Contribution 
- 🔖 Use Cases 
- ❓ FAQs
## Support

### Discard Join US

📢 Join Our Discord Channel!

Looking forward to seeing you there! 🎉

### Contact Information

If you have any questions or feedback about this project, please feel free to contact us. We highly appreciate your suggestions!

- Email: alexanderwu@deepwisdom.ai
- GitHub Issues: For more technical inquiries, you can also create a new issue in our GitHub repository.
We will respond to all questions within 2-3 business days.

## Citation

To stay updated with the latest research and development, follow @MetaGPT_ on Twitter.

To cite MetaGPT or Data Interpreter in publications, please use the following BibTeX entries.

```plain text
@misc{hong2023metagpt,
      title={MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework},
      author={Sirui Hong and Mingchen Zhuge and Jonathan Chen and Xiawu Zheng and Yuheng Cheng and Ceyao Zhang and Jinlin Wang and Zili Wang and Steven Ka Shing Yau and Zijuan Lin and Liyang Zhou and Chenyu Ran and Lingfeng Xiao and Chenglin Wu and Jürgen Schmidhuber},
      year={2023},
      eprint={2308.00352},
      archivePrefix={arXiv},
      primaryClass={cs.AI}
}
@misc{hong2024data,
      title={Data Interpreter: An LLM Agent For Data Science},
      author={Sirui Hong and Yizhang Lin and Bang Liu and Bangbang Liu and Binhao Wu and Danyang Li and Jiaqi Chen and Jiayi Zhang and Jinlin Wang and Li Zhang and Lingyao Zhang and Min Yang and Mingchen Zhuge and Taicheng Guo and Tuo Zhou and Wei Tao and Wenyi Wang and Xiangru Tang and Xiangtao Lu and Xiawu Zheng and Xinbing Liang and Yaying Fei and Yuheng Cheng and Zongze Xu and Chenglin Wu},
      year={2024},
      eprint={2402.18679},
      archivePrefix={arXiv},
      primaryClass={cs.AI}
}

```


