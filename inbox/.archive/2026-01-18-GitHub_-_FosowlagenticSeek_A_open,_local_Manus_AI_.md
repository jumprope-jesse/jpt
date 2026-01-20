---
type: link
source: notion
url: https://github.com/Fosowl/agenticSeek
notion_type: Software Repo
tags: ['Running']
created: 2025-04-29T21:11:00.000Z
---

# GitHub - Fosowl/agenticSeek: A open, local Manus AI alternative. No APIs, No $200 monthly bills. Enjoy an autonomous agent that thinks, browses the web, and code for the sole cost of electricity.

## Overview (from Notion)
- Local AI Solutions: Emphasizes privacy and control, offering an alternative to subscription-based services for AI tools you might use in your work and personal projects.
- Cost Efficiency: Reduces reliance on expensive APIs, which could benefit your startup budget and allow for more investment in other areas.
- Autonomous Assistant: Imagine having a personal AI that can handle coding tasks, web browsing, and file management—freeing up your time for family or strategic planning.
- Community Contribution: The project encourages collaboration and open-source contributions, aligning with a culture of innovation and sharing that can be inspiring for your own ventures.
- Cutting-edge Technology: Engaging with the latest in AI could fuel new ideas for your business, possibly leading to unique product offerings or improvements.
- Educational Tool: It can serve as a learning resource, helping your kids understand technology and coding in a hands-on manner.
- Alternate Views: Consider the implications of local AI versus cloud-based solutions—how does this shift affect data security, accessibility, and the future of tech entrepreneurship?

## AI Summary (from Notion)
AgenticSeek is a local AI assistant that operates entirely on your hardware, enabling coding, web browsing, and filesystem interaction without cloud dependency. It features autonomous coding capabilities, efficient memory management, and supports multiple programming languages, prioritizing user privacy and control.

## Content (from Notion)

English | 中文 | 繁體中文 | Français | 日本語

# AgenticSeek: Manus-like AI powered by Deepseek R1 Agents.

A fully local alternative to Manus AI, a voice-enabled AI assistant that codes, explores your filesystem, browse the web and correct it's mistakes all without sending a byte of data to the cloud. Built with reasoning models like DeepSeek R1, this autonomous agent runs entirely on your hardware, keeping your data private.

> 

> 

> 

> 

## Features:

- 
- 
- 
- 
- 
- 
- 
## Installation

Make sure you have chrome driver, docker and python3.10 (or newer) installed.

For issues related to chrome driver, see the Chromedriver section.

### 1️⃣ Clone the repository and setup

```plain text
git clone https://github.com/Fosowl/agenticSeek.git
cd agenticSeek
mv .env.example .env
```

### 2️ Create a virtual env

```plain text
python3 -m venv agentic_seek_env
source agentic_seek_env/bin/activate
# On Windows: agentic_seek_env\Scripts\activate
```

### 3️⃣ Install package

Automatic Installation:

```plain text
./install.sh
```

Manually:

```plain text
pip3 install -r requirements.txt
# or
python3 setup.py install
```

## Run locally on your machine

We recommend using at the very least Deepseek 14B, smaller models will struggle with tasks especially for web browsing.

### 1️⃣ Download Models

Make sure you have Ollama installed.

Download the deepseek-r1:14b model from DeepSeek

```plain text
ollama pull deepseek-r1:14b
```

### 2️ Run the Assistant (Ollama)

Start the ollama server

```plain text
ollama serve
```

Change the config.ini file to set the provider_name to ollama and provider_model to deepseek-r1:14b

NOTE: deepseek-r1:14bis an example, use a bigger model if your hardware allow it.

```plain text
[MAIN]
is_local = True
provider_name = ollama
provider_model = deepseek-r1:14b
provider_server_address = 127.0.0.1:11434
```

start all services :

```plain text
sudo ./start_services.sh # MacOS
start ./start_services.cmd # Window
```

Run the assistant:

```plain text
python3 main.py
```

See the Usage section if you don't understand how to use it

See the Known issues section if you are having issues

See the Run with an API section if your hardware can't run deepseek locally

See the Config section for detailled config file explanation.

## Usage

Make sure the services are up and running with ./start_services.sh and run the agenticSeek with python3 main.py

```plain text
sudo ./start_services.sh
python3 main.py
```

You will be prompted with >>>  This indicate agenticSeek await you type for instructions. You can also use speech to text by setting listen = True in the config.

To exit, simply say goodbye.

Here are some example usage:

### Coding/Bash

> 

> 

> 

### Web search

> 

> 

> 

### File system

> 

> 

> 

### Casual

> 

> 

> 

After you type your query, agenticSeek will allocate the best agent for the task.

Because this is an early prototype, the agent routing system might not always allocate the right agent based on your query.

Therefore, you should be very explicit in what you want and how the AI might proceed for example if you want it to conduct a web search, do not say:

Do you know some good countries for solo-travel?

Instead, ask:

Do a web search and find out which are the best country for solo-travel

## Run the LLM on your own server

If you have a powerful computer or a server that you can use, but you want to use it from your laptop you have the options to run the LLM on a remote server.

### 1️⃣ Set up and start the server scripts

On your "server" that will run the AI model, get the ip address

```plain text
ip a | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}' | cut -d/ -f1
```

Note: For Windows or macOS, use ipconfig or ifconfig respectively to find the IP address.

If you wish to use openai based provider follow the Run with an API section.

Clone the repository and enter the server/folder.

```plain text
git clone --depth 1 https://github.com/Fosowl/agenticSeek.git
cd agenticSeek/server/
```

Install server specific requirements:

```plain text
pip3 install -r requirements.txt
```

Run the server script.

```plain text
python3 app.py --provider ollama --port 3333
```

You have the choice between using ollama and llamacpp as a LLM service.

### 2️⃣ Run it

Now on your personal computer:

Change the config.ini file to set the provider_name to server and provider_model to deepseek-r1:14b. Set the provider_server_address to the ip address of the machine that will run the model.

```plain text
[MAIN]
is_local = False
provider_name = server
provider_model = deepseek-r1:14b
provider_server_address = x.x.x.x:3333
```

Run the assistant:

```plain text
sudo ./start_services.sh # start_services.cmd on windows
python3 main.py
```

## Run with an API

Set the desired provider in the config.ini

```plain text
[MAIN]
is_local = False
provider_name = openai
provider_model = gpt-4o
provider_server_address = 127.0.0.1:5000
```

WARNING: Make sure there is not trailing space in the config.

Set is_local to True if using a local openai-based api.

Change the IP address if your openai-based api run on your own server.

Run the assistant:

```plain text
sudo ./start_services.sh # start_services.cmd on windows
python3 main.py
```

## Speech to Text

The speech-to-text functionality is disabled by default. To enable it, set the listen option to True in the config.ini file:

```plain text
listen = True

```

When enabled, the speech-to-text feature listens for a trigger keyword, which is the agent's name, before it begins processing your input. You can customize the agent's name by updating the agent_name value in the config.ini file:

```plain text
agent_name = Friday

```

For optimal recognition, we recommend using a common English name like "John" or "Emma" as the agent name

Once you see the transcript start to appear, say the agent's name aloud to wake it up (e.g., "Friday").

Speak your query clearly.

End your request with a confirmation phrase to signal the system to proceed. Examples of confirmation phrases include:

```plain text
"do it", "go ahead", "execute", "run", "start", "thanks", "would ya", "please", "okay?", "proceed", "continue", "go on", "do that", "go it", "do you understand?"

```

## Config

Example config:

```plain text
[MAIN]
is_local = True
provider_name = ollama
provider_model = deepseek-r1:1.5b
provider_server_address = 127.0.0.1:11434
agent_name = Friday
recover_last_session = False
save_session = False
speak = False
listen = False
work_dir =  /Users/mlg/Documents/ai_folder
jarvis_personality = False
[BROWSER]
headless_browser = False
stealth_mode = False

```

Explanation:

- is_local -> Runs the agent locally (True) or on a remote server (False).
- provider_name -> The provider to use (one of: ollama, server, lm-studio, deepseek-api)
- provider_model -> The model used, e.g., deepseek-r1:1.5b.
- provider_server_address -> Server address, e.g., 127.0.0.1:11434 for local. Set to anything for non-local API.
- agent_name -> Name of the agent, e.g., Friday. Used as a trigger word for TTS.
- recover_last_session -> Restarts from last session (True) or not (False).
- save_session -> Saves session data (True) or not (False).
- speak -> Enables voice output (True) or not (False).
- listen -> listen to voice input (True) or not (False).
- work_dir -> Folder the AI will have access to. eg: /Users/user/Documents/.
- jarvis_personality -> Uses a JARVIS-like personality (True) or not (False). This simply change the prompt file.
- languages -> The list of supported language, needed for the llm router to work properly, avoid putting too many or too similar languages.
- headless_browser -> Runs browser without a visible window (True) or not (False).
- stealth_mode -> Make bot detector time harder. Only downside is you have to manually install the anticaptcha extension.
## Providers

The table below show the available providers:

To select a provider change the config.ini:

```plain text
is_local = False
provider_name = openai
provider_model = gpt-4o
provider_server_address = 127.0.0.1:5000

```

is_local: should be True for any locally running LLM, otherwise False.

provider_name: Select the provider to use by it's name, see the provider list above.

provider_model: Set the model to use by the agent.

provider_server_address: can be set to anything if you are not using the server provider.

# Known issues

## Chromedriver Issues

Known error #1: chromedriver mismatch

Exception: Failed to initialize browser: Message: session not created: This version of ChromeDriver only supports Chrome version 113 Current browser version is 134.0.6998.89 with binary path

This happen if there is a mismatch between your browser and chromedriver version.

You need to navigate to download the latest version:

https://developer.chrome.com/docs/chromedriver/downloads

If you're using Chrome version 115 or newer go to:

https://googlechromelabs.github.io/chrome-for-testing/

And download the chromedriver version matching your OS.

If this section is incomplete please raise an issue.

## FAQ

Q: What hardware do I need?

7B Model: GPU with 8GB VRAM. 14B Model: 12GB GPU (e.g., RTX 3060). 32B Model: 24GB+ VRAM.

Q: Why Deepseek R1 over other models?

Deepseek R1 excels at reasoning and tool use for its size. We think it’s a solid fit for our needs other models work fine, but Deepseek is our primary pick.

Q: I get an error running main.py. What do I do?

Ensure Ollama is running (ollama serve), your config.ini matches your provider, and dependencies are installed. If none work feel free to raise an issue.

Q: Can it really run 100% locally?

Yes with Ollama or Server providers, all speech to text, LLM and text to speech model run locally. Non-local options (OpenAI or others API) are optional.

Q: Why should I use AgenticSeek when I have Manus?

This started as Side-Project we did out of interest about AI agents. What’s special about it is that we want to use local model and avoid APIs. We draw inspiration from Jarvis and Friday (Iron man movies) to make it "cool" but for functionnality we take more inspiration from Manus, because that's what people want in the first place: a local manus alternative. Unlike Manus, AgenticSeek prioritizes independence from external systems, giving you more control, privacy and avoid api cost.

## Contribute

We’re looking for developers to improve AgenticSeek! Check out open issues or discussion.

## Maintainers:

> 


