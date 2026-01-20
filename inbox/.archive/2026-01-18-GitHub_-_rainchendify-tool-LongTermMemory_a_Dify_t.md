---
type: link
source: notion
url: https://github.com/rainchen/dify-tool-LongTermMemory
notion_type: Software Repo
tags: ['Running']
created: 2024-07-06T04:48:00.000Z
---

# GitHub - rainchen/dify-tool-LongTermMemory: a Dify tool for storing and retrieving long-term-memory, using Dify built-in Knowledge dataset for storing memories, each user has a standalone long-term-memory space

## AI Summary (from Notion)
- Project Overview: Dify tool for storing and retrieving long-term memory, allowing each user to have a unique memory space.
- Creation Date: July 6, 2024.
- Status: Not started.
- Core Functionality:
- Utilizes Dify Knowledge API to retrieve and store user-related document segments.
- Chatbot can remember customized information for each user.
- Workflow Logic:
- Begins with an HTTP request to retrieve user memory.
- Prepares agent prompts and extracts parameters for actions (reply, add, update).
- Updates or creates document segments based on user actions.
- Usage Steps:
- Create a Knowledge and document for long-term memory.
- Generate a secret key for API access.
- Import a YAML workflow file.
- Configure LLM model settings.
- Publish the workflow as "LongTermMemory."
- Create a chatbot using chatflow and integrate the LongTermMemory tool.
- Testing Scenarios:
- Scenario 1: Tests the chatbot's ability to remember user information (e.g., name, hobbies).
- Scenario 2: Tests retrieval of stored information.
- Scenario 3: Demonstrates that each user has a separate long-term memory space.
- Interesting Fact: The tool requires LLM performance to be at least GPT-4 for optimal functionality.

## Content (from Notion)

# About this repo

a Dify tool for storing and retrieving long-term-memory, using Dify built-in Knowledge dataset for storing memories, each user has a standalone long-term-memory space. Make chatbot can persistently remember customized information per user.

workflow view:

# How it works

Here is the major logic of this workflow:

1. 
1. 
1. 
1. 
1. 
# Demo Video

dify-tool-LongTermMemory-demo-20240705173656-1920x1080.mp4

# Usage Steps

## step 1: create a Knowledge and document for storing long-term-memory

create a new Knowledge and import an empty document

- 
- 
- 
## step 2: Create a new Secret key for accessing Knowledge API

## step 3: import the workflow DSL yaml

1. 
1. 
## step 4: publish the workflow as tool "LongTermMemory"

## step 5: create new a chatbot app using chatflow

## step 6: add the "LongTermMemory" tool

add the "LongTermMemory" tool before LLM node

## step 7: config parameters for "LongTermMemory" tool

notes for parameters:

- 
- 
- 
- 
- 
```plain text
<UserInfo>
  <name>${user_name}</name>
  <age>${user_age}</age>
  <hobbies>${user_hobbies}</hobbies>
  <any_user_info>${any_user_info}</any_user_info>
</UserInfo>

```

- user_input: {{#sys.query#}}
## step 8: Config LLM node

CONTEXT：select LongTermMemory node's text

SYSTEM prompt:

```plain text
{{#context#}}

```

# Test:

### Scenario 1: test long-term-memory remembering

user input:

-  
-  
-  
-  
### Scenario 2: test long-term-memory retrieving

Debug and Preview -> Restart (make sure to start a new conversion without chat history)

user input:

- what's my name? 
- what do I like? 
### Scenario 3: each user has a standalone long-term-memory space

Run App (You can use different browsers to access and impersonate different users)

user input:

- I'm Jerry
- I like eating 

