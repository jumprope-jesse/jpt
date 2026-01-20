---
type: link
source: notion
url: https://github.com/DAGWorks-Inc/burr?tab=readme-ov-file
notion_type: Software Repo
tags: ['Running']
created: 2024-04-03T20:57:00.000Z
---

# GitHub - DAGWorks-Inc/burr: Build applications that make decisions (chatbots, agents, simulations, etc...). Monitor, persist, and execute on your own infrastructure.

## AI Summary (from Notion)
- Overview of Burr: A tool for developing applications that make decisions based on state, such as chatbots and simulations, using simple Python building blocks.
- UI Integration: Burr includes a user interface for real-time decision tracking and monitoring.
- Quick Start: Installation via pip and easy setup to run examples and explore the UI.
- State Machine Model: Burr allows users to express applications as state machines, facilitating state management across various contexts.
- Applications: Can be used for chatbots, machine learning pipelines, simulations, and more.
- Framework Comparisons: Burr is open-source and framework-agnostic, contrasting with other tools like Langchain and Temporal which do not explicitly model state machines.
- Name Origin: Named after Aaron Burr, highlighting the connection to the previous library, Hamilton, developed by DAGWorks.
- Roadmap: Future features include testing curation, efficiency improvements, cloud-based solutions, and storage integrations.
- Contributions: Open for contributions, with resources available for developers interested in contributing.

## Content (from Notion)

# Burr

Burr makes it easy to develop applications that make decisions based on state (chatbots, agents, simulations, etc...) from simple python building blocks. Burr includes a UI that can track/monitor those decisions in real time.

Link to documentation. Quick (<3min) video intro here. Longer video intro & walkthrough. Blog post here.

## 🏃Quick start

Install from pypi:

```plain text
pip install "burr[start]"
```

Then run the UI server:

```plain text
burr
```

This will open up Burr's telemetry UI. It comes loaded with some default data so you can click around. It also has a demo chat application to help demonstrate what the UI captures enabling you too see things changing in real-time. Hit the "Demos" side bar on the left and select chatbot. To chat it requires the OPENAI_API_KEY environment variable to be set, but you can still see how it works if you don't have an API key set.

Next, start coding / running examples:

```plain text
git clone https://github.com/dagworks-inc/burr && cd burr/examples/hello-world-counter
python application.py
```

You'll see the counter example running in the terminal, along with the trace being tracked in the UI. See if you can find it.

For more details see the getting started guide.

## 🔩 How does Burr work?

With Burr you express your application as a state machine (i.e. a graph/flowchart). You can (and should!) use it for anything where managing state can be hard. Hint: managing state is always hard! This is true across a wide array of contexts, from building RAG applications to power a chatbot, to running ML parameter tuning/evaluation workflows, to conducting a complex forecasting simulation.

Burr includes:

1. A (dependency-free) low abstraction python library that enables you to build and manage state machines with simple python functions
1. A UI you can use view execution telemetry for introspection and debugging
1. A set of integrations to make it easier to persist state, connect to telemetry, and integrate with other systems
## 💻️ What can you do with Burr?

Burr can be used to power a variety of applications, including:

1. A simple gpt-like chatbot
1. A stateful RAG-based chatbot
1. A machine learning pipeline
1. A simulation
And a lot more!

Using hooks and other integrations you can (a) integrate with any of your favorite vendors (LLM observability, storage, etc...), and (b) build custom actions that delegate to your favorite libraries (like Hamilton).

Burr will not tell you how to build your models, how to query APIs, or how to manage your data. It will help you tie all these together in a way that scales with your needs and makes following the logic of your system easy. Burr comes out of the box with a host of integrations including tooling to build a UI in streamlit and watch your state machine execute.

## 🏗 Start Building

See the documentation for getting started, and follow the example. Then read through some of the concepts and write your own application!

## 📃 Comparison against common frameworks

While Burr is attempting something (somewhat) unique, there are a variety of tools that occupy similar spaces:

## 🌯 Why the name Burr?

Burr is named after Aaron Burr, founding father, third VP of the United States, and murderer/arch-nemesis of Alexander Hamilton. What's the connection with Hamilton? This is DAGWorks' second open-source library release after the Hamilton library We imagine a world in which Burr and Hamilton lived in harmony and saw through their differences to better the union. We originally built Burr as a harness to handle state between executions of Hamilton DAGs (because DAGs don't have cycles), but realized that it has a wide array of applications and decided to release it more broadly.

## 🛣 Roadmap

While Burr is stable and well-tested, we have quite a few tools/features on our roadmap!

1. Testing & eval curation. Curating data with annotations and being able to export these annotations to create unit & integration tests.
1. Various efficiency/usability improvements for the core library (see planned capabilities for more details). This includes: 
1. Cloud-based checkpointing/restart for debugging or production use cases (save state to db and replay/warm start, backed by a configurable database)
1. Tooling for hosted execution of state machines, integrating with your infrastructure (Ray, modal, FastAPI + EC2, etc...)
1. Storage integrations. More integrations with technologies like Redis, MongoDB, MySQL, etc. so you can run Burr on top of what you have available.
If you want to avoid self-hosting the above solutions we're building Burr Cloud. To let us know you're interested sign up here for the waitlist to get access.

## 🤲 Contributing

We welcome contributors! To get started on developing, see the developer-facing docs.

## 👪 Contributors

- Elijah ben Izzy
- Stefan Krawczyk
- Joseph Booth
- Thierry Jean

