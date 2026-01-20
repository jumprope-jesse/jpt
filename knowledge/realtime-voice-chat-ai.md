# RealtimeVoiceChat - Local AI Voice Conversations

Open-source project for natural spoken conversations with LLMs.

**Repo:** https://github.com/KoljaB/RealtimeVoiceChat

## Architecture

Client-server system optimized for low-latency:
1. Browser captures voice via Web Audio API
2. Audio streams to Python backend via WebSockets
3. RealtimeSTT transcribes speech to text
4. LLM processes (Ollama or OpenAI)
5. RealtimeTTS synthesizes response
6. Audio streams back to browser

## Key Features

- Real-time feedback with partial transcriptions
- Smart turn-taking with dynamic silence detection
- Interruption handling
- Pluggable LLM backends (Ollama default, OpenAI supported)
- Multiple TTS engines: Kokoro, Coqui, Orpheus

## Tech Stack

- Backend: Python 3.x, FastAPI
- Frontend: Vanilla JS, Web Audio API, AudioWorklets
- Communication: WebSockets
- Deployment: Docker Compose recommended

## Requirements

- CUDA-enabled NVIDIA GPU recommended (for Whisper STT and Coqui TTS)
- Python 3.9+
- Docker (optional but recommended)
- Ollama (if using local LLM)

## Quick Start

```bash
git clone https://github.com/KoljaB/RealtimeVoiceChat.git
cd RealtimeVoiceChat
docker compose up -d
# Visit http://localhost:8000
```

## Use Cases

- Voice-first AI assistant
- Hands-free interaction with LLMs
- Natural conversation practice/testing

## Related Libraries

- RealtimeSTT - speech-to-text streaming
- RealtimeTTS - text-to-speech streaming
