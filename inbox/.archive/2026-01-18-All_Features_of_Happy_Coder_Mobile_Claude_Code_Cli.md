---
type: link
source: notion
url: https://happy.engineering/docs/features/
notion_type: Software Repo
tags: ['Running']
created: 2025-10-09T03:55:00.000Z
---

# All Features of Happy Coder: Mobile Claude Code Client

## Overview (from Notion)
- Seamless integration of mobile and desktop experiences can enhance productivity, allowing you to manage coding tasks while balancing family time.
- Real-time synchronization means you can start a coding session on your laptop and continue it on your phone, making it easier to code during breaks or while waiting for kids.
- The voice agent feature could transform brainstorming and planning, allowing for hands-free idea development while multitasking at home.
- Push notifications keep you informed of task progress, reducing the need to constantly check your devices and helping you focus on family activities.
- The offline capabilities ensure you can work even without a stable connection, ideal for commutes or busy family outings in the city.
- Consider the balance between tech and family; while these tools enhance productivity, they shouldn't overshadow quality time with loved ones.
- The focus on security and privacy in the app allows you to work on sensitive projects without fear, which is crucial for a founder managing proprietary code.
- An alternate view might argue that reliance on such tools could lead to distractions; finding a healthy balance is key.

## AI Summary (from Notion)
Happy Coder offers a mobile experience for Claude Code with features like real-time CLI synchronization, multi-session management, end-to-end encryption, and offline-first architecture. Developers can seamlessly switch between devices, manage multiple projects, and maintain security with permission prompts for sensitive operations. Additional features include a push notification system and voice agent integration for enhanced productivity and user experience.

## Content (from Notion)

Happy Coder provides a native mobile experience for Claude Code, including file mentions, slash commands, and custom agents. Happy Coder also provides many extra quality of life features, including voice coding, push notifications.

## Core Architecture Features

### 1. Real-Time CLI Synchronization

Engineering Description: Bidirectional real-time synchronization between the desktop CLI (happy) and mobile app through encrypted relay server. The CLI wraps Claude Code execution and streams terminal state, while mobile app provides input that flows back to the CLI seamlessly. Both devices can initiate conversations, send messages, and receive responses in the same shared session - there’s no distinction between “primary” and “secondary” devices.

> 

> 

> 

> 

> 

Technical Implementation:

- WebSocket connections for real-time bidirectional communication
- Terminal state serialization and synchronization
- Command history and context preservation
- Cross-device cursor position and selection state sync
### 2. Multi-Session Management

Engineering Description: Support for multiple concurrent Claude Code sessions with independent state management. Each session maintains its own project context, conversation history, and terminal state. Sessions can be paused, resumed, and switched between seamlessly.

> 

Technical Implementation:

- Session isolation with unique identifiers
- Project-specific context management
- Session persistence across app restarts
- Background session state preservation
### 3. End-to-End Encryption with Zero-Trust Architecture

Engineering Description: All communication between CLI and mobile app encrypted using shared secrets (scan a QR code). Relay server handles only encrypted blobs without access to plaintext data. Public key authentication with challenge-response protocol.

> 

Technical Implementation:

- AES encryption for all data in transit
- Key exchange via QR code scanning
- Zero round-trip authentication protocol
- Public key hashing for channel identification
- Open-source relay server for self-hosting
### 4. Offline-First Architecture with Encrypted Pub/Sub

Engineering Description: Asynchronous communication through encrypted relay server that acts as a message queue between desktop CLI and mobile app. Desktop CLI logs Claude Code activity, encrypts it, and uploads encrypted blobs to object storage. Mobile app fetches and decrypts these blobs to display progress. Commands flow in reverse - mobile encrypts instructions, uploads to relay, desktop downloads and decrypts to execute.

> 

> 

Technical Implementation:

- Encrypted blob storage on relay server (server cannot read contents)
- Desktop CLI writes encrypted activity logs to object storage
- Mobile app polls for encrypted updates and decrypts locally
- Bidirectional encrypted pub/sub messaging system
- Session persistence independent of network connectivity
- Simple relay server with no access to plaintext data
### 5. Permission Prompts for MCP Tools and Edit Operations

Engineering Description: Real-time permission system that intercepts MCP tool calls and file edit operations initiated by Claude Code, presenting mobile developers with contextual Allow/Deny prompts before execution. When Claude Code attempts to use MCP tools (Model Context Protocol integrations like JIRA, Linear, GitHub APIs) or perform sensitive file operations, the mobile app displays the exact operation details and waits for explicit user approval before proceeding.

> 

> 

> 

Technical Implementation:

- Interceptor middleware in CLI that pauses execution for permission-required operations
- Real-time permission request serialization and transmission to mobile app
- Mobile UI components for displaying operation context with Allow/Deny buttons
- Encrypted request/response flow through relay server maintaining zero-trust architecture
- Operation queuing system that preserves Claude Code session state during permission waits
- Granular permission categories (file operations, API calls, system commands, external integrations)
- Per-session permission memory with option to “Remember for this session”
### 6. File Mentions

### 7. Custom Slash Commands and Agent Library

Engineering Description: Complete Claude Code slash command and custom agent ecosystem accessible from mobile. All user-defined agents from ~/.claude/agents/ directory are synchronized and available through the mobile interface. The system provides intelligent autocomplete, command history, and seamless agent switching without requiring separate mobile-specific agent definitions.

> 

> 

> 

Technical Implementation:

- Real-time synchronization of ~/.claude/agents/ directory contents to mobile app
- Command autocomplete with fuzzy search across all available agents
- Agent metadata parsing (name, description, tools, model preferences)
- Session-aware agent switching that preserves context and conversation history
- Command history persistence across devices with intelligent suggestions
- Mobile-optimized agent selection UI with categorization and favorites
- Background agent definition updates without requiring app restart
## Mobile-Optimized User Experience Features

### 8. Push Notification System

Engineering Description: Push notifications triggered by Claude Code state changes. Notifications include session status updates, completion alerts, error notifications, and input requests. Unlike social media apps where notification fatigue is a concern, work-focused notifications prioritize immediate awareness over filtering - when you’re actively developing, you need to know when each async operation completes to make the next work mode decision.

> 

Technical Implementation:

- Comprehensive state change notifications (completion, error, input needed)
- Immediate delivery without smart filtering or bundling delays
- Deep linking to specific sessions and exact completion points
- Rich notification content with operation details
### 9. Voice Agent Integration

Engineering Description: AI-powered voice interface that acts as an intermediary between the user and Claude Code. The voice agent processes natural language input, maintains conversational context, and generates structured prompts for Claude Code execution.

User Stories:

> 

> 

Technical Implementation:

- Speech-to-text (STT) with Eleven Labs
- Text-to-speech (TTS) with Eleven Labs
- Conversation state management with its own context independent of claude code session.
- Agentic assistant (Claude Sonnet 4) that can send messages to claude code and has some special prompts to get better results in turning rubber duck style stream of conciousness planning into a concrete request for claude code to execute.

