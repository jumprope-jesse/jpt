---
type: link
source: notion
url: https://github.com/open-webui/open-webui
notion_type: Software Repo
tags: ['Running']
created: 2024-05-22T21:35:00.000Z
---

# GitHub - open-webui/open-webui: User-friendly WebUI for LLMs (Formerly Ollama WebUI)

## AI Summary (from Notion)
- Project Overview: Open WebUI is a self-hosted, user-friendly web interface designed for LLMs (Large Language Models), previously known as Ollama WebUI.
- Key Features:
- Intuitive interface inspired by ChatGPT.
- Responsive design for desktop and mobile.
- Fast performance and effortless setup using Docker/Kubernetes.
- Supports theme customization, code syntax highlighting, and full Markdown/LaTeX.
- Local Retrieval Augmented Generation (RAG) integration for document interactions.
- Multi-model support, enabling users to switch between different chat models.
- Collaborative chat capabilities and voice input support.
- Security features include role-based access control and trusted email authentication.
- Installation Options: Various methods including Docker, Docker Compose, and native installations, with specific commands provided for different configurations (e.g., with/without GPU support).
- Community and Support: Encouragement to join the Open WebUI Community for additional resources and to explore customized modelfiles.
- Future Developments: Commitment to continuous updates, with a roadmap for upcoming features available in the documentation.
- Acknowledgments: Thanks to mentors and supporters who contributed to the project.
- License: The project is licensed under the MIT License.
- Support: Users are encouraged to engage with the community for questions and suggestions.

## Content (from Notion)

# Open WebUI (Formerly Ollama WebUI) 👋

Open WebUI is an extensible, feature-rich, and user-friendly self-hosted WebUI designed to operate entirely offline. It supports various LLM runners, including Ollama and OpenAI-compatible APIs. For more information, be sure to check out our Open WebUI Documentation.

## Features ⭐

- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
## 🔗 Also Check Out Open WebUI Community!

Don't forget to explore our sibling project, Open WebUI Community, where you can discover, download, and explore customized Modelfiles. Open WebUI Community offers a wide range of exciting possibilities for enhancing your chat interactions with Open WebUI! 🚀

## How to Install 🚀

Note

Please note that for certain Docker environments, additional configurations might be needed. If you encounter any connection issues, our detailed guide on Open WebUI Documentation is ready to assist you.

### Quick Start with Docker 🐳

Warning

When using Docker to install Open WebUI, make sure to include the -v open-webui:/app/backend/data in your Docker command. This step is crucial as it ensures your database is properly mounted and prevents any loss of data.

Tip

If you wish to utilize Open WebUI with Ollama included or CUDA acceleration, we recommend utilizing our official images tagged with either :cuda or :ollama. To enable CUDA, you must install the Nvidia CUDA container toolkit on your Linux/WSL system.

### Installation with Default Configuration

-  
-     
### Installation for OpenAI API Usage Only

-  
### Installing Open WebUI with Bundled Ollama Support

This installation method uses a single container image that bundles Open WebUI with Ollama, allowing for a streamlined setup via a single command. Choose the appropriate command based on your hardware setup:

-  
-  
Both commands facilitate a built-in, hassle-free installation of both Open WebUI and Ollama, ensuring that you can get everything up and running swiftly.

After installation, you can access Open WebUI at http://localhost:3000. Enjoy! 😄

### Other Installation Methods

We offer various installation alternatives, including non-Docker native installation methods, Docker Compose, Kustomize, and Helm. Visit our Open WebUI Documentation or join our Discord community for comprehensive guidance.

### Troubleshooting

Encountering connection issues? Our Open WebUI Documentation has got you covered. For further assistance and to join our vibrant community, visit the Open WebUI Discord.

### Open WebUI: Server Connection Error

If you're experiencing connection issues, it’s often due to the WebUI docker container not being able to reach the Ollama server at 127.0.0.1:11434 (host.docker.internal:11434) inside the container . Use the --network=host flag in your docker command to resolve this. Note that the port changes from 3000 to 8080, resulting in the link: http://localhost:8080.

Example Docker Command:

```plain text
docker run -d --network=host -v open-webui:/app/backend/data -e OLLAMA_BASE_URL=http://127.0.0.1:11434 --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

### Keeping Your Docker Installation Up-to-Date

In case you want to update your local Docker installation to the latest version, you can do it with Watchtower:

```plain text
docker run --rm --volume /var/run/docker.sock:/var/run/docker.sock containrrr/watchtower --run-once open-webui
```

In the last part of the command, replace open-webui with your container name if it is different.

### Moving from Ollama WebUI to Open WebUI

Check our Migration Guide available in our Open WebUI Documentation.

## What's Next? 🌟

Discover upcoming features on our roadmap in the Open WebUI Documentation.

## Supporters ✨

A big shoutout to our amazing supporters who's helping to make this project possible! 🙏

### Platinum Sponsors 🤍

- We're looking for Sponsors!
### Acknowledgments

Special thanks to Prof. Lawrence Kim and Prof. Nick Vincent for their invaluable support and guidance in shaping this project into a research endeavor. Grateful for your mentorship throughout the journey! 🙌

## License 📜

This project is licensed under the MIT License - see the LICENSE file for details. 📄

## Support 💬

If you have any questions, suggestions, or need assistance, please open an issue or join our Open WebUI Discord community to connect with us! 🤝

## Star History

Created by Timothy J. Baek - Let's make Open WebUI even more amazing together! 💪


