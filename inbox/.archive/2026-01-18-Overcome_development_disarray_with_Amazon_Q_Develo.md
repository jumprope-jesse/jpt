---
type: link
source: notion
url: https://aws.amazon.com/blogs/devops/overcome-development-disarray-with-amazon-q-developer-cli-custom-agents/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2025-08-01T10:58:00.000Z
---

# Overcome development disarray with Amazon Q Developer CLI custom agents | AWS DevOps & Developer Productivity Blog

## Overview (from Notion)
- Embrace the flexibility of custom agents to manage multiple projects efficiently, allowing more time for family.
- Leverage the streamlined workflows to balance your responsibilities as a founder, enhancing productivity without sacrificing family time.
- The integration of tools like Amazon Q Developer CLI can simplify complex tasks, helping you stay organized amidst the chaos of city life.
- Consider the potential of teaching your kids about technology through your work, fostering their interest in STEM from an early age.
- Reflect on the importance of work-life balance: while custom agents enhance efficiency, ensure you prioritize family moments over tech.
- Explore alternative views on technology's role in parenting—how can tools be used to enhance family interaction instead of detracting from it?
- Think about the community aspect of your work: how can your experiences with technology contribute to local initiatives in NYC?

## AI Summary (from Notion)
Custom agents in the Amazon Q Developer CLI enhance workflow management by allowing developers to create tailored environments for different tasks, such as front-end and back-end development. This feature enables seamless switching between contexts, optimizing tool configurations and permissions, thereby reducing cognitive overhead and improving productivity in complex development scenarios.

## Content (from Notion)

As a developer who has embraced the power of the Model Context Protocol (MCP)to enhance my workflows, I’m thrilled to see the addition of custom agents in the Amazon Q Developer CLI. This new feature takes the capabilities I’ve come to rely on to a whole new level, allowing me to seamlessly manage different development contexts and easily switch between them.

In my previous post, I discussed how MCP servers have revolutionized the way I interact with AWS services, databases, and other essential tools. MCP integration in Amazon Q Developer allows me to query my database schemas, automate infrastructure deployments, and so much more. However, as I started juggling multiple projects, each with their own unique tech stacks and requirements, I found myself needing a more structured approach to managing these diverse development environments.

Enter custom agents. With this new feature, I can now create and use a custom agent by bringing together specific tools, prompt, context and tool permissions for tasks appropriate for the stage of development. In this post I will explain how to configure a cusom agent for front-end and back-end development. Allowing me to easily optimize Amazon Q Developer for each task.

## Background

Imagine that I am working on a multi-tier web application. The application has a React front-end written in Typescript and a FastAPI back-end written in Python. In addition to me, the team includes a designer that uses Figma, and the database administrator that manages a PostgreSQL database. There are subtle differences in how I communicate with the designer and the database administrator. For example, when I discuss a “table” with the designer, I’m likely referring to an HTML table and how the page is structured. However, when I discuss a table with the database administrator, I’m likely talking about a SQL table and how data is stored.

In the past, I had both the Figma Dev Mode MCP server and Amazon Aurora PostgreSQL MCP server configured in my environment. While this allowed me to easily work on either the front-end or back-end code, it introduced some challenges. If I asked Amazon Q Developer “how many tables do I have?” Amazon Q Developer would have to guess if I was talking about HTML tables or SQL tables. If the question is about HTML, it should use the Figma server. If the question is about SQL, it should use the Aurora server. This is not a technical limitation, it’s a language limitation. Just as I have to adjust my assumptions to talk with the designer and database administrator, Amazon Q Developer has to make the same adjustments.

Enter Amazon Q Developer CLI custom agents. Custom agents allow me to optimize Q Developer’s configuration for each scenario. Let’s walk through my front-end and back-end configuration to understand the impact.

## Front-end agent

My front-end custom agent is optimized for front-end web development using React and Figma. The following code example is the configuration for my front-end agent stored in ~/.aws/amazonq/agents/front-end.json. Let’s discuss the major sections of the configuration.

- mcpServers – Here I have configured the Figma Dev Mode MCP Server. This simply communicates with the Figma Web Design App installed locally. Note that this replaces the MCP configuration that was stored in ~/.aws/amazonq/mcp.json
- tools and allowedTools – These two sections are related, so I will discuss them together. tools defines the tools are available to Amazon Q Developer while allowedTools defines which tools are trusted. In other words, Q Developer is able to use all configured tools, and it does not have to ask my permission to use fs_read, fs_write, and @Figma. @Figma allows Amazon Q Developer to use all Figma tools without asking for permission. More on this in the next section.
- resources – Here I have configured the files that should be added to the context. I have included the README.md (stored in the project folder) and my own preferences for React (stored in my profile). You can read more in the context management section of the user guide.
- hooks – In addition to the resources, I have also included a hook. This hook will run a command and inject it into the context at runtime. In the example, I am adding the current git status. You can read more in the context hooks section of the user guide.
```plain text
{
  "description": "Optimized for front-end web development using React and Figma",
  "mcpServers": {
    "Figma": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "http://127.0.0.1:3845/sse"
      ]
    }
  },
  "tools": ["*"],
  "allowedTools": [
    "fs_read",
    "fs_write",
    "report_issues",
    "@Figma"
  ],
  "resources": [
    "file://README.md",
    "file://~/.aws/amazonq/react-preferences.md"
  ],
  "hooks": {
    "agentSpawn": [
      {
        "command": "git status"
      }
    ]
  }
}


```

## Back-end agent

My back-end custom agent is optimized for back-end development with Python and PostgreSQL. The following code example is the configuration for my back-end agent stored in ~/.aws/amazonq/agents/back-end.json. Rather than describing the sections, as I did earlier, I will focus on the differences between the front-end and back-end.

- mcpServers – Here I have configured the Amazon Aurora PostgreSQL MCP Server. This allows Amazon Q Developer to query my dev database to learn about the schema. Notice that I have configured a read-only connection to ensure that I don’t accidentally update the database.
- tools and allowedTools – Once again, I have enabled Amazon Q Developer to use all tools. However, notice that I am more restrictive about what tools are trusted. Amazon Q Developer will need to ask permission to use fs_write or @PostgreSQL/run_query. Notice that I can allow the entire MCP server as I did with Figma or specific tools as I did here.
- resources – Again, I have included the README.md (stored in the project folder) and my own preferences for Python and SQL (both stored in my profile). Note that I can also use glob patterns here. For example, file://.amazonq/rules/**/*.md would include the rules created by the Amazon Q Developer IDE plugins.
- hooks – Finally, I have also included the hook for the front-end and back-end. However, I could have included project specific options such as npm run for the front-end and pip freeze for the back-end.
```plain text
{
  "description": "Optimized for back-end development with Python and PostgreSQL",
  "mcpServers": {
    "PostgreSQL": {
      "command": "uvx",
      "args": [
        "awslabs.postgres-mcp-server@latest",
        "--resource_arn", "arn:aws:rds:us-east-1:xxxxxxxxxxxx:cluster:xxxxxx",
        "--secret_arn", "arn:aws:secretsmanager:us-east-1:xxxxxxxxxxxx:secret:rds!cluster-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx-xxxxxx",
        "--database", "dev",
        "--region", "us-east-1",
        "--readonly", "True"
      ]
    }
  },
  "tools": ["*"],
  "allowedTools": [
    "fs_read",
    "report_issues",
    "@PostgreSQL/get_table_schema"
  ],
  "resources": [
    "file://README.md",
    "file://~/.aws/amazonq/python-preferences.md",
    "file://~/.aws/amazonq/sql-preferences.md"
  ],
  "hooks": {
    "agentSpawn": [
      {
        "command": "git status"
      }
    ]
  }
}
```

## Using custom agents

The real power of agents becomes evident when I need to switch between these different development contexts. I can now simply run q chat --agent front-end when I am working on React and Figma or q chat --agent back-end when I am working with Python and SQL. Amazon Q Developer will configure the correct agent with all my preferences.

In the following image, you can see the configuration in the Amazon Q Developer CLI. Notice that the front-end agent has an additional tool called Figma while the back-end agent has an additional tool called PostgreSQL. In addition, the front-end agent trusts fs_write and all of the Figma tools while the back-end agent will ask permission to use fs_write and only trusts one of the two PostgreSQL tools.

A split terminal view showing tool permissions for front-end and back-end environments. Both displays list built-in commands like execute_bash, fs_read, fs_write, report_issue, and use_aws, along with their permission status (trusted, not trusted, or trust read-only commands). The front-end environment also shows Figma (MCP) related permissions, while the back-end shows PostgreSQL (MCP) permissions. At the bottom of each view is a note that trusted tools will run without confirmation and instructions to use "/tools help" to edit permissions.

Similarly, let’s look at the context configuration in both the front-end and back-end agents. In the following image, I have included my React preferences for front-end development, and both Python and SQL preferences for back-end development.

A split terminal view showing the output of "/context show" command for both front-end and back-end environments. The front-end agent shows matches for "~/.aws/amazonq/react-preferences.md" and "README.md", while the back-end agent shows matches for "~/.aws/amazonq/python-preferences.md", "~/.aws/amazonq/sql-preferences.md", and "README.md". Each file is marked with "(1 match)" in green text.

As you can see, custom agents allow me to optimize the Amazon Q Developer CLI for each task. Of course, front-end and back-end agents are just an example. You might have a developer and testing agents, data science and analytics agents, etc. Custom agents allow you to tailor the configuration to most any task.

## Conclusion

Amazon Q Developer CLI custom agents represent a significant improvement in managing complex development environments. By allowing developers to seamlessly switch between different contexts, they eliminate the cognitive overhead of manually reconfiguring tools and permissions for different tasks. Ready to streamline your development workflow? Get started with Amazon Q Developer today.


