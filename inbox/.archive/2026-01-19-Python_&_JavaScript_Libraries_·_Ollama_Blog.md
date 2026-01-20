---
type: link
source: notion
url: https://ollama.ai/blog/python-javascript-libraries
notion_type: Software Repo
tags: ['Running']
created: 2024-01-25T06:06:00.000Z
---

# Python & JavaScript Libraries · Ollama Blog

## AI Summary (from Notion)
- Introduction of Libraries: The Ollama Python and JavaScript libraries have been released for integrating applications with Ollama.

- Integration Ease: Both libraries allow for easy integration with new and existing apps using minimal code, mirroring the features of the Ollama REST API.

- Installation Instructions:
- Python: pip install ollama
- JavaScript: npm install ollama

- Key Features:
- Streaming: Ability to receive messages in real-time.
- Multi-modal Capabilities: Can handle both text and image inputs.
- Text Completion: Provides completion suggestions for prompts.
- Custom Models: Users can create their own models with specific instructions.
- Custom Client: Ability to specify a host for the Ollama client.

- New GitHub Organization: The libraries are now part of a new GitHub organization named ollama, promoting collaboration and community contributions.

- Community Engagement: Acknowledgment of community members maintaining various language libraries, encouraging contributions to expand Ollama's accessibility.

- Special Thanks: Recognition of key contributors like Saul, the original author of ollama-js, highlighting community involvement in developing the libraries.

## Content (from Notion)

The initial versions of the Ollama Python and JavaScript libraries are now available:

- Ollama Python Library
- Ollama JavaScript Library
Both libraries make it possible to integrate new and existing apps with Ollama in a few lines of code, and share the features and feel of the Ollama REST API.

## Getting Started

Python

```plain text
pip install ollama

```

```plain text
import ollama
response = ollama.chat(model='llama2', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(response['message']['content'])

```

JavaScript

```plain text
npm install ollama

```

```plain text
import ollama from 'ollama'

const response = await ollama.chat({
  model: 'llama2',
  messages: [{ role: 'user', content: 'Why is the sky blue?' }],
})
console.log(response.message.content)

```

## Use cases

Both libraries support Ollama’s full set of features. Here are some examples in Python:

### Streaming

```plain text
for chunk in chat('mistral', messages=messages, stream=True):
  print(chunk['message']['content'], end='', flush=True)

```

### Multi-modal

```plain text
with open('image.png', 'rb') as file:
  response = ollama.chat(
    model='llava',
    messages=[
      {
        'role': 'user',
        'content': 'What is strange about this image?',
        'images': [file.read()],
      },
    ],
  )
print(response['message']['content'])

```

### Text Completion

```plain text
result = ollama.generate(
  model='stable-code',
  prompt='// A c function to reverse a string\n',
)
print(result['response'])

```

### Creating custom models

```plain text
modelfile='''
FROM llama2
SYSTEM You are mario from super mario bros.
'''

ollama.create(model='example', modelfile=modelfile)

```

### Custom client

```plain text
ollama = Client(host='my.ollama.host')

```

More examples are available in the GitHub repositories for the Python and JavaScript libraries.

## New GitHub handle

GitHub handle

These libraries, and the main Ollama repository now live in a new GitHub organization: ollama! Thank you to all the amazing community members who maintain libraries to interact with Ollama via Dart, Swift, C#, Java, PHP, Rust and more – a full list is available here – please don’t hesitate to make a pull request to add a library you’ve built or enjoy using.

Special thank you to Saul, the original author of ollama-js, and everyone else who has worked on community libraries to make Ollama more accessible from different programming languages.


