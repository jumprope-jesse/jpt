---
type: link
source: notion
url: https://github.com/zeenolife/ai-baby-monitor
notion_type: Software Repo
tags: ['Running']
created: 2025-05-25T13:09:00.000Z
---

# GitHub - zeenolife/ai-baby-monitor: Local Video-LLM powered AI Baby Monitor

## Overview (from Notion)
- The AI Baby Monitor project offers a tech-savvy solution for parents juggling work and family, providing peace of mind through real-time monitoring.
- Leveraging local video LLMs ensures privacy, as all data stays within your network, aligning with modern concerns about data security.
- The minimal alert system focuses on subtlety—just a gentle beep—to avoid overwhelming notifications, perfect for a busy household.
- Its flexibility allows for easy customization of safety rules, making it adaptable to your family's unique needs and routines.
- The project emphasizes that it’s not a substitute for supervision, which can resonate with your perspective on the importance of active parenting despite technological aids.
- As a software engineer, the architecture and use of Docker highlight innovative approaches to home automation, blending software development with parenting in your daily life.
- Consider alternate views: some may argue that reliance on tech for monitoring children could lead to complacency, advocating for traditional supervision techniques instead.

## AI Summary (from Notion)
The AI Baby Monitor uses local video LLMs to monitor a baby's safety by watching a video stream and issuing a gentle beep if safety rules are broken. It operates locally for privacy, supports multiple rooms, and features a live dashboard for real-time monitoring. Users can easily configure rules and settings through YAML files. The project is not a substitute for adult supervision and is intended as an additional safety measure.

## Content (from Notion)

# 👶🧠 AI Baby Monitor (Local Video‑LLM Nanny)

> 

The AI Baby Monitor watches a video stream (webcam, RTSP camera, …) and a simple list of safety rules. If a rule is broken it issues a single gentle beep so you can quickly glance over and check on your baby.

## 📸 Demo

Obviously, I'm not going to put my child in danger just for the demo, so here're videos of:

1. People using smartphones, when rules say you shouldn't ❌
1. Baby being safe and playful with a parent ✅
## ✨ Features

## 🚀 Quick start

> 

```plain text
# 1 — clone
$ git clone https://github.com/zeenolife/ai-baby-monitor.git && cd ai-baby-monitor

# 2 — copy .env.template into .env
$ cp .env.template .env

# 3 — build & start all services (Redis, vLLM, video streamer, Streamlit viewer)
$ docker compose up --build -d

# 4 — start the watcher on the **host**. unfortunately playing sound in Docker container and propagating to host is really painful. so no docker compose here
$ uv run scripts/run_watcher.py --config-file configs/living_room.yaml

# 5 — open the dashboard 👉 http://localhost:8501. You can also open the dashboard on your phone http://{host_network_ip}:8501
```

> 

## 🛠 Configuration

Add or tweak rooms in configs/*.yaml:

```plain text
name: "living_room"

camera:
  uri: "0"            # webcam index or RTSP URI

instructions:          # natural‑language rules for the nanny model
  - "The baby shouldn't do anything dangerous."
  - "An adult should be in the room if the baby is awake."
```

- Multiple rooms? Edit docker-compose.yml and create stream_to_redis per room. Pass in new room config to streamlit viewer. Spawn new run_watcher.py process on host for new room config.
- Swap the model? Set LLM_MODEL_NAME in .env. Check vLLM supported models
## 🏗 Architecture (high level)

1. stream_to_redis.py captures frames and pushes them to Redis (short realtime & long subsampled frames queues).
1. run_watcher.py pulls latest N frames, encodes instructions and frames into prompt and sends them to local vLLM server, receives structured JSON, writes logs & plays a beep if receives should_alert = True.
1. Streamlit live‑updates the latest frame + llm logs.
## 🛑 Disclaimer

This project is NOT a replacement for adult supervision. You should NEVER leave your baby alone.

It's meant as an additional guard for situations when you inevitably get distracted for a tiny moment, and your child is doing something dangerous. Thus just a beep sound as a notification.

It’s an experimental hobby tool — use responsibly and at your own risk.

## 📝 License

MIT © 2025 @zeenolife

## Credits

Notification sound from Mixkit, used under the Mixkit Free Sound Effects License.

Videos used for demo from Pexels, used under their license


