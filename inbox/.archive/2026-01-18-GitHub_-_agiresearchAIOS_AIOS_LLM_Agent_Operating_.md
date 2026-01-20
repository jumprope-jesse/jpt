---
type: link
source: notion
url: https://github.com/agiresearch/AIOS
notion_type: Software Repo
tags: ['Running']
created: 2024-04-08T03:40:00.000Z
---

# GitHub - agiresearch/AIOS: AIOS: LLM Agent Operating System

## AI Summary (from Notion)
- Project Overview: AIOS (LLM Agent Operating System) integrates large language models into operating systems to enhance functionality and move toward artificial general intelligence (AGI).

- Key Features:
- Optimizes resource allocation and context switching between agents.
- Enables concurrent execution and provides various toolkits for developers.

- Recent Updates:
- New shell simulator and API features added to the codebase as of April 5, 2024.
- Active Discord community for discussions and brainstorming.
- Recent publications related to AIOS and its ecosystem.

- Installation Instructions:
- Requires Python 3.9 to 3.11.
- Instructions for cloning the repository and installing dependencies.

- Modes of Operation:
- Interactive Mode: Allows real-time interaction with AIOS and agents.
- Deployment Mode: Runs agents and logs outputs to files, suitable for resource monitoring.

- References: Cites academic papers that provide foundational context for the project.

- Contributions: Open for collaboration, with clear guidelines for contributions and community involvement.

- Contact Information: Provides emails for direct contact regarding development issues.

- Interesting Fact: AIOS aims to create an operating system "with soul," highlighting its ambitious goal of advancing AI capabilities.

## Content (from Notion)

# AIOS: LLM Agent Operating System

AIOS, a Large Language Model (LLM) Agent operating system, embeds large language model into Operating Systems (OS) as the brain of the OS, enabling an operating system "with soul" -- an important step towards AGI. AIOS is designed to optimize resource allocation, facilitate context switch across agents, enable concurrent execution of agents, provide tool service for agents, maintain access control for agents, and provide a rich set of toolkits for LLM Agent developers.

## 🏠 Architecture of AIOS

## 📰 News

- [2024-04-05] 🛠️ AIOS codebase has been updated to add shell simulator, rapid API calls, and pre-commit test cases. Please see CONTRIBUTE for how to test your contributions and create pull requests.
- [2024-04-02] 🌟 AIOS Discord Community is up. Welcome to join the community for discussions, brainstorming, development, or just random chats!
- [2024-03-25] ✈️ Our paper AIOS: LLM Agent Operating System is released and AIOS repository is officially launched!
- [2023-12-06] 📋 After several months of working, our perspective paper LLM as OS, Agents as Apps: Envisioning AIOS, Agents and the AIOS-Agent Ecosystem is officially released.
## ✈️ Getting Started

### Installation

```plain text
git clone https://github.com/agiresearch/AIOS.git
```

Make sure you have Python >= 3.9 and <= 3.11 Install the required packages using pip

```plain text
pip install -r requirements.txt
```

### Usage

If you use open-sourced models from huggingface, you need to setup your Hugging Face token and cache directory

```plain text
export HUGGING_FACE_HUB_TOKEN=<YOUR READ TOKEN>
export HF_HOME=<YOUR CACHE DIRECTORY>
```

If you use LLM APIs like Gemini-pro, you need to setup your Gemini API Key

```plain text
export GEMINI_API_KEY=<YOUR GEMINI API KEY>
```

Here we provide two modes to run the AIOS: interactive mode and deployment mode

### Interactive Mode

In the interactive mode, you can interact with AIOS to see the output of each step in running multiple agents

```plain text
# Use Gemma-2b-it, replace the max_gpu_memory and eval_device with your own and run
python main.py --llm_name gemma-2b-it --max_gpu_memory '{"0": "24GB"}' --eval_device "cuda:0" --max_new_tokens 256
```

```plain text
# Use Mixtral-8x7b-it, replace the max_gpu_memory and eval_device with your own and run
python main.py --llm_name mixtral-8x7b-it --max_gpu_memory '{"0": "48GB", "1": "48GB", "2": "48GB"}' --eval_device "cuda:0" --max_new_tokens 256
```

```plain text
# Use Gemini-pro, run with Gemini-pro
python main.py --llm_name gemini-pro
```

### Deployment Mode

In the deployment mode, the outputs of running agents are stored in files. And in this mode, you are provided with multiple commands to run agents and see resource usage of agents (e.g., run <xxxAgent>: <YOUR TASK>, print agent)

```plain text
# Use Gemma-2b-it, replace the max_gpu_memory and eval_device with your own and run
python simulator.py --llm_name gemma-2b-it --max_gpu_memory '{"0": "24GB"}' --eval_device "cuda:0" --max_new_tokens 256 --scheduler_log_mode file --agent_log_mode file
```

```plain text
# Use Mixtral-8x7b-it
python simulator.py --llm_name mixtral-8x7b-it --max_gpu_memory '{"0": "48GB", "1": "48GB", "2": "48GB"}' --eval_device "cuda:0" --max_new_tokens 256 --scheduler_log_mode file --agent_log_mode file
```

```plain text
# Use Gemini-pro
python simulator.py --llm_name gemini-pro --scheduler_log_mode file --agent_log_mode file
```

## 🖋️ References

```plain text
@article{mei2024aios,
  title={AIOS: LLM Agent Operating System},
  author={Mei, Kai and Li, Zelong and Xu, Shuyuan and Ye, Ruosong and Ge, Yingqiang and Zhang, Yongfeng}
  journal={arXiv:2403.16971},
  year={2024}
}
@article{ge2023llm,
  title={LLM as OS, Agents as Apps: Envisioning AIOS, Agents and the AIOS-Agent Ecosystem},
  author={Ge, Yingqiang and Ren, Yujie and Hua, Wenyue and Xu, Shuyuan and Tan, Juntao and Zhang, Yongfeng},
  journal={arXiv:2312.03815},
  year={2023}
}

```

## 🚀 Contributions

AIOS is dedicated to facilitating LLM agents' development and deployment in a systematic way, collaborators and contributions are always welcome to foster a cohesive, effective and efficient AIOS-Agent ecosystem!

For detailed information on how to contribute, see CONTRIBUTE. If you would like to contribute to the codebase, issues or pull requests are always welcome!

## 🌟 Discord Channel

If you would like to join the community, ask questions, chat with fellows, learn about or propose new features, and participate in future developments, join our Discord Community!

## 📪 Contact

For issues related to AIOS development, we encourage submtting issues, pull requests, or initiating discussions in the AIOS Discord Channel. For other issues please feel free to contact Kai Mei (marknju2018@gmail.com) and Yongfeng Zhang (yongfeng@email.com).

## 🌍 AIOS Contributors


