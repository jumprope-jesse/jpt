---
type: link
source: notion
url: https://github.com/synw/agent-smith
notion_type: Software Repo
tags: ['Running']
created: 2024-04-01T13:25:00.000Z
---

# GitHub - synw/agent-smith: An api to create local first human friendly agents

## AI Summary (from Notion)
- Project Overview: The document details an API called "Agent Smith" designed for creating local-first, human-friendly agents that can operate in browsers or Node.js.

- Creation Date: The project was created on April 1, 2024.

- Status: The project is currently not started.

- Key Features:
- Agents can interact, think, run jobs, and remember data using transient or semantic memory.
- The API emphasizes local-first operation and does not support major APIs like OpenAI.

- Components:
- The Body: Details installation, basic agent setup, and interaction methods (talking, components, confirm).
- The Brain: Covers agent basics, options, grammars, and templates.
- Jobs: Guides on job creation, configuration, and memory management.
- Memory Types: Includes transient and semantic memory management.

- Example Usage: A quick Node.js example demonstrates how to use the API to create an agent and execute an inference query.

- Powered By: Utilizes libraries like Nanostores for state management, Locallm for inference server management, and Modprompt for managing prompt templates.

- FAQ Highlights:
- Compatible with local inference servers like Llama.cpp, Koboldcpp, and Ollama.
- Does not support larger APIs to maintain a focus on local-first solutions.

- Documentation: Comprehensive documentation links are provided for further exploration of the project’s components and functionalities.

## Content (from Notion)

# Agent Smith

An api to create local first human friendly agents in the browser or Nodejs

📚 Read the documentation

- The body 
- The brain 
- Jobs 
- Transient memory 
- Semantic memory 
- Examples 
Check the 💻 Starter template

## What is an agent?

An agent is an anthropomorphic representation of a bot. It has these basic habilities:

- Interact: the agent can perform interactions with the user and get input and feedback
- Think: interact with some language model servers to perform inference queries
- Run jobs: manage long running jobs with multiple tasks
- Remember: use it's transient or semantic memory to store data
## Packages

## FAQ

- What local or remote inference servers can I use?
Actually it works with Llama.cpp, Koboldcpp and Ollama.

- Can I use this with OpenAI or other big apis?
Sorry no: this library favours local first or private remote inference servers

## Example

Quick Nodejs example:

```plain text
const expert = useLmExpert({
    name: "default",
    localLm: "koboldcpp",
    templateName: "mistral",
    onToken: (t) => process.stdout.write(t),
});
const brain = useAgentBrain([expert]);
const bob = useAgentSmith({
    name: "Bob",
    modules: [brain],
});
// auto discover if expert's inference servers are up
await bob.brain.discover();
// run an inference query
const _prompt = "list the planets of the solar sytem";
await bob.think(_prompt, { temperature: 0.2 });
```

## Libraries

Powered by:

- Nanostores for the state management and reactive variables
- Locallm for the inference servers management
- Modprompt for the prompt templates management

