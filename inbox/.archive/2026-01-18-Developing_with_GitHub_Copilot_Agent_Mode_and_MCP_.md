---
type: link
source: notion
url: https://austen.info/blog/github-copilot-agent-mcp/
notion_type: Software Repo
tags: ['Running']
created: 2025-07-04T11:07:00.000Z
---

# Developing with GitHub Copilot Agent Mode and MCP | Austen Stone

## Overview (from Notion)
- Embracing tools like GitHub Copilot Agent Mode can streamline your coding process, giving you more time to spend with family.
- Automating repetitive tasks lets you focus on higher-level problem-solving and innovation, essential for a company founder.
- The integration of Model Context Protocol (MCP) can enhance collaboration with team members, providing context-aware assistance that adapts to your specific projects.
- This approach fosters a more efficient work-life balance, allowing for more flexibility in your schedule as a parent in a bustling city.
- Consider how AI can serve as a partner in your coding journey, not just a tool—this mindset can shift how you approach software development.
- Explore combining AI capabilities with your unique insights into user needs, creating products that resonate more deeply with customers.
- While some may view reliance on AI as a crutch, think of it as an opportunity to elevate your work quality and creativity.
- Engage with your community about these technologies—sharing experiences might open avenues for collaboration and innovation.

## AI Summary (from Notion)
Utilizing GitHub Copilot Agent Mode and Model Context Protocol (MCP) enhances development efficiency by allowing customization of AI responses, integrating external tools, and streamlining workflows. Key phases include research, planning, implementation, course correction, and validation, with a focus on maintaining consistency, efficiency, and quality in code generation. The approach emphasizes the importance of context for AI to better align with developer needs, ultimately enabling more time for high-level design.

## Content (from Notion)

I'm always looking for ways to work more efficiently and deliver better code faster. Recently, The GitHub Copilot Agent Mode in combination with Model Context Protocol (MCP) has transformed my development workflow.

## Customizing Copilot

The magic starts with Customizing AI responses in VS Code. Instead of repeatedly explaining my preferences to the AI, I can now define:

- Custom instructions for consistent coding practices
- Custom prompts for reusable task templates
- Custom chat modes with specific tool configurations
This foundation allows me to create specialized AI assistants for different phases of development.

### VS Code Settings

Here are my VS Code settings. I have enabled experimental features and changed some settings to allow the agent to run without my intervention.

- github.copilot.chat.codeGeneration.instructions - I have custom instructions personal to me
- chat.agent.maxRequests - Let's me allow the agent to run longer without asking for permission
- chat.tools.autoApprove - Automatically approves run commands and tool requests from the agent
### MCP Tools

The Using Model Context Protocol (MCP) in VS Code allows me to provide the agent with access to external tools and data sources.

Some of the MCP servers I use include:

- Sequential Thinking - Dynamic and reflective problem-solving through thought sequences
- SearXNG - Integrates the SearXNG API, providing web search capabilities.
- Playwright - This MCP Server will help you run browser automation and webscraping using Playwright
- GitHub - Repository management, file operations, and GitHub API integration
- time - For getting the current time and date
- Fetch - Web content fetching and conversion for efficient LLM usage
The repo modelcontextprotocol/servers contains a list of available MCP servers.

## Development Workflow

### Research

Before diving into coding, I often need to research new concepts or technologies. For this, I use a custom chat mode called research that includes tools like web search, and sequential thinking.

### Planning

I start every project in a custom chat mode called plan that I have in my user space. The tools I want for are already selected and copilot can't edit my code even if it wanted to because I took away that tool. I find Gemini 2.5 Pro to be the best model for planning.

The goal of this phase is to generate a comprehensive .prompt.md file in .github/prompts/ that serves as a detailed blueprint for the implementation.

### Implementation

Once I have my planning prompt ready, I switch to regular agent mode with Claude Sonnet 4 and simply run /prompt-name. The beauty of this approach is that the AI has all the context it needs to execute the plan methodically.

The prompt file acts as a contract between the planning phase and implementation phase, ensuring consistency and reducing the need for back-and-forth clarification.

### Course Correction

If the agent is close I will sometimes pause it and ask it to look at a specific resource or document to help it understand the problem better.

When the agent deviates from the desired behavior (which occasionally happens), I have a simple recovery process:

1. Clear my git diff to reset the changes
1. Modify the prompt file based on what I learned
1. Restart the implementation from scratch
This iterative refinement of prompts means I'm constantly improving my templates for future use.

### Validation

Finally (or maybe first if we're following TDD) I want to ensure the implementation works as expected. Ideally our output is testable but sometimes this is hard.

For browser interactions, I use the playwright MCP tool to automate testing. This is really cool because the agent can use a browser just like I can! This lets it understand how the UI works and what it looks like.

## Example

Let's walk though a real-world example. I want to add comments to my blog you're viewing right now.

### 1. Research

I start by in research mode using Gemini 2.5 Pro with a question:

```plain text
How would I add comments to my blog posts in this Docusaurus site?

```

Copilot starts by using sequentialthinking think about how to perform research

```plain text
{
"nextThoughtNeeded": true,
"thought": "I need to research how to add comments to a Docusaurus blog. I will start by searching for \"Docusaurus blog comments\" and analyze the results. I will look for official documentation and popular third-party solutions like Giscus, Disqus, or Utterances. Finally, I will synthesize the findings to provide a clear recommendation.",
"thoughtNumber": 1,
"totalThoughts": 2
}

```

Then Copilot starts searching the web using searxng_web_search and web_url_read tools.

It comes up with the idea to use Giscus as a commenting service.

> 

### 2. Planning

Now I switch to plan chat mode.

Copilot comes up with a structured plan for me.

### 3. Implementation

Now I switch to regular agent mode.

We're going to reuse our prompt file from earlier to write the plan as a .prompt.md file.

Copilot creates the .github/prompts/implement-giscus.prompt.md file.

Now I can switch to Claude Sonnet 4 and run the generated prompt file.

### Course Correction

I'm watching the agent work and it got hung up on how to pass front matter metadata to the Giscus component.

I paused and asked it to look at document on the topic

Copilot looked at my resource and found even more resources to help it understand how to access blog post metadata.

> 

Copilot figured out that the ideal solution was the reactHook useBlogPost() which I totally agree with.

### 4. Validation

I want to ensure the Giscus comments are working correctly so I ask Copilot to browse to a link knowing it will use the playwright MCP tool.

This tested the comments were working but I wanted it to actually make a comment on the blog post.

The comment on this blog post was actually the output of this prompt.

### Real Example

Copilot did complete my feature completely.

The full PR can be found at austenstone/portfolio/pull/36.

## Benefits

This workflow has transformed how I approach development:

1. Consistency: Custom instructions ensure all generated code follows my patterns
1. Efficiency: Pre-planned prompts eliminate repetitive explanations
1. Quality: Structured thinking leads to better architectural decisions
1. Testability: UI-aware testing tools create more comprehensive test suites
1. Reproducibility: Documented prompts make complex tasks repeatable
Ultimately I can spend more time on high-level design and less on low-level implementation details. The AI handles the grunt work, allowing me to focus on delivering value.

## The Future

This combination of Agent Mode and MCP represents a fundamental shift in how we can work with AI. Instead of treating AI as a simple code completion tool, we can create sophisticated, context-aware development partners that understand our specific needs and workflows.

The key insight is that the AI becomes more valuable when it has more context about our intentions, constraints, and environment. MCP provides that context, while custom prompts ensure consistent, high-quality outputs.

Have you experimented with Agent Mode and MCP in your development workflow? I'd love to hear about your experiences and any creative tool combinations you've discovered. Connect with me on GitHub or LinkedIn to continue the conversation.


