---
type: link
source: notion
url: https://github.com/KoljaB/RealtimeVoiceChat
notion_type: Software Repo
tags: ['Running']
created: 2025-05-05T23:37:00.000Z
---

# GitHub - KoljaB/RealtimeVoiceChat: Have a natural, spoken conversation with AI!

## Overview (from Notion)
- Everyday Communication: As a father, using AI voice chat could help facilitate natural conversations with your kids, making learning and interaction more engaging.
- Tech Savvy Parenting: Embracing this technology showcases a modern approach to parenting, encouraging your children to explore AI and tech.
- Professional Edge: As a software engineer and founder, leveraging AI in communication can enhance productivity and foster innovation within your company.
- Networking Opportunities: This tool can facilitate smoother conversations in networking scenarios, potentially opening doors to collaborations or partnerships.
- Unique User Experience: The project emphasizes low-latency interactions, providing a more fluid and human-like conversation, which can be appealing in both personal and professional contexts.
- Personal Assistant: The AI could serve as a voice-activated personal assistant, managing tasks and reminders, freeing up valuable time for you as a busy parent and entrepreneur.
- Alternative Views:
- Privacy Concerns: Consider the implications of using AI that processes voice data—be mindful of privacy and data security.
- Screen Time: Balance the use of AI tools with face-to-face interactions to avoid over-reliance on technology in family life.
- Technological Dependency: Reflect on the potential downsides of relying too heavily on AI for conversations, particularly in developing social skills in children.

## AI Summary (from Notion)
A project enabling real-time voice conversations with AI using a client-server system, featuring low-latency interaction, customizable voices, and support for various LLM backends. Installation can be done via Docker or manually, with detailed setup instructions provided.

## Content (from Notion)

# Real-Time AI Voice Chat 🎤💬🧠🔊

Have a natural, spoken conversation with an AI!

This project lets you chat with a Large Language Model (LLM) using just your voice, receiving spoken responses in near real-time. Think of it as your own digital conversation partner.

(early preview - first reasonably stable version)

## What's Under the Hood?

A sophisticated client-server system built for low-latency interaction:

1. 🎙️ Capture: Your voice is captured by your browser.
1. ➡️ Stream: Audio chunks are whisked away via WebSockets to a Python backend.
1. ✍️ Transcribe: RealtimeSTT rapidly converts your speech to text.
1. 🤔 Think: The text is sent to an LLM (like Ollama or OpenAI) for processing.
1. 🗣️ Synthesize: The AI's text response is turned back into speech using RealtimeTTS.
1. ⬅️ Return: The generated audio is streamed back to your browser for playback.
1. 🔄 Interrupt: Jump in anytime! The system handles interruptions gracefully.
## Key Features ✨

- Fluid Conversation: Speak and listen, just like a real chat.
- Real-Time Feedback: See partial transcriptions and AI responses as they happen.
- Low Latency Focus: Optimized architecture using audio chunk streaming.
- Smart Turn-Taking: Dynamic silence detection (turndetect.py) adapts to the conversation pace.
- Flexible AI Brains: Pluggable LLM backends (Ollama default, OpenAI support via llm_module.py).
- Customizable Voices: Choose from different Text-to-Speech engines (Kokoro, Coqui, Orpheus via audio_module.py).
- Web Interface: Clean and simple UI using Vanilla JS and the Web Audio API.
- Dockerized Deployment: Recommended setup using Docker Compose for easier dependency management.
## Technology Stack 🛠️

- Backend: Python 3.x, FastAPI
- Frontend: HTML, CSS, JavaScript (Vanilla JS, Web Audio API, AudioWorklets)
- Communication: WebSockets
- Containerization: Docker, Docker Compose
- Core AI/ML Libraries: 
- Audio Processing: numpy, scipy
## Before You Dive In: Prerequisites 🏊‍♀️

This project leverages powerful AI models, which have some requirements:

- Operating System: 
- 🐍 Python: 3.9 or higher (if setting up manually).
- 🚀 GPU: A powerful CUDA-enabled NVIDIA GPU is highly recommended, especially for faster STT (Whisper) and TTS (Coqui). Performance on CPU-only or weaker GPUs will be significantly slower. 
- 🐳 Docker (Optional but Recommended): Docker Engine and Docker Compose v2+ for the containerized setup.
- 🧠 Ollama (Optional): If using the Ollama backend without Docker, install it separately and pull your desired models. The Docker setup includes an Ollama service.
- 🔑 OpenAI API Key (Optional): If using the OpenAI backend, set the OPENAI_API_KEY environment variable (e.g., in a .env file or passed to Docker).
## Getting Started: Installation & Setup ⚙️

Clone the repository first:

```plain text
git clone https://github.com/KoljaB/RealtimeVoiceChat.git
cd RealtimeVoiceChat
```

Now, choose your adventure:

## Running the Application ▶️

If using Docker: Your application is already running via docker compose up -d! Check logs using docker compose logs -f app.

If using Manual/Script Installation:

1. Activate your virtual environment (if not already active): 
1. Navigate to the code directory (if not already there): 
1. Start the FastAPI server: 
Accessing the Client (Both Methods):

1. Open your web browser to http://localhost:8000 (or your server's IP if running remotely/in Docker on another machine).
1. Grant microphone permissions when prompted.
1. Click "Start" to begin chatting! Use "Stop" to end and "Reset" to clear the conversation.
## Configuration Deep Dive 🔧

Want to tweak the AI's voice, brain, or how it listens? Modify the Python files in the code/ directory.

⚠️ Important Docker Note: If using Docker, make any configuration changes before running docker compose build to ensure they are included in the image.

-  
-  
-  
-  
-   
## Contributing 🤝

Got ideas or found a bug? Contributions are welcome! Feel free to open issues or submit pull requests.

## License 📜

The core codebase of this project is released under the MIT License (see the LICENSE file for details).

This project relies on external specific TTS engines (like Coqui XTTSv2) and LLM providers which have their own licensing terms. Please ensure you comply with the licenses of all components you use.


