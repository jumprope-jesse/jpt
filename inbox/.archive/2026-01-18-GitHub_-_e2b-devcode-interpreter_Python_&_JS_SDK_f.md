---
type: link
source: notion
url: https://github.com/e2b-dev/code-interpreter
notion_type: Software Repo
tags: ['Running']
created: 2024-04-20T13:03:00.000Z
---

# GitHub - e2b-dev/code-interpreter: Python & JS SDK for building custom code interpreters. Built with E2B - Cloud Runtime for AI Agents.

## AI Summary (from Notion)
- Project Overview: The document describes the GitHub repository for the Code Interpreter SDK, which is designed for running AI-generated Python and JavaScript code with shared context across executions.

- Key Features:
- Works with any Language Learning Model (LLM) and AI framework.
- Supports streaming content, including charts and standard output/error.
- 100% open-source, including the infrastructure.

- Usage:
- Provides installation instructions for both Python and JavaScript.
- Includes examples illustrating how to run code, generate charts, and handle streaming outputs.

- Functionality:
- Maintains a shared context between code executions, mimicking a Jupyter Notebook environment.
- Allows for more efficient coding practices by referencing previous code blocks without losing context.

- Customization: Users can customize the Code Interpreter sandbox by following a provided guide to add preinstalled packages.

- Pre-installed Packages: A full list of pre-installed Python packages can be found in the requirements file.

- Interesting Fact: The code interpreter runs inside an E2B Sandbox, which is a secure micro VM specifically designed for executing untrusted code.

## Content (from Notion)

# Code Interpreter SDK

This Code Interpreter SDK allows you to run AI-generated Python code and each run share the context. That means that subsequent runs can reference to variables, definitions, etc from past code execution runs. The code interpreter runs inside the E2B Sandbox - an open-source secure micro VM made for running untrusted AI-generated code and AI agents.

- ✅ Works with any LLM and AI framework
- ✅ Supports streaming content like charts and stdout, stderr
- ✅ Python & JS SDK
- ✅ Runs on serverless and edge functions
- ✅ 100% open source (including infrastructure)
Follow E2B on X (Twitter)

## Custom E2B sandbox with Code Interpreter SDK

Follow this guide if you want to customize the Code Interprerter sandbox (e.g.: add a preinstalled package). The customization is done via custom E2B sandbox template.

## Installation

### Python

```plain text
pip install e2b-code-interpreter
```

### JavaScript

```plain text
npm install @e2b/code-interpreter
```

## Examples

### Minimal example with the sharing context

### Python

```plain text
from e2b_code_interpreter import CodeInterpreter

with CodeInterpreter() as sandbox:
    sandbox.notebook.exec_cell("x = 1")

    execution = sandbox.notebook.exec_cell("x+=1; x")
    print(execution.text)  # outputs 2
```

### JavaScript

```plain text
import { CodeInterpreter } from '@e2b/code-interpreter'

const sandbox = await CodeInterpreter.create()
await sandbox.notebook.execCell('x = 1')

const execution = await sandbox.notebook.execCell('x+=1; x')
console.log(execution.text)  // outputs 2

await sandbox.close()
```

### Get charts and any display-able data

### Python

```plain text
import base64
import io

from matplotlib import image as mpimg, pyplot as plt

from e2b_code_interpreter import CodeInterpreter

code = """
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)
y = np.sin(x)

plt.plot(x, y)
plt.show()
"""

with CodeInterpreter() as sandbox:
    # you can install dependencies in "jupyter notebook style"
    sandbox.notebook.exec_cell("!pip install matplotlib")

    # plot random graph
    execution = sandbox.notebook.exec_cell(code)

# there's your image
image = execution.results[0].png

# example how to show the image / prove it works
i = base64.b64decode(image)
i = io.BytesIO(i)
i = mpimg.imread(i, format='PNG')

plt.imshow(i, interpolation='nearest')
plt.show()
```

### JavaScript

```plain text
import { CodeInterpreter } from '@e2b/code-interpreter'

const sandbox = await CodeInterpreter.create()

const code = `
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)
y = np.sin(x)

plt.plot(x, y)
plt.show()
`;

// you can install dependencies in "jupyter notebook style"
await sandbox.notebook.execCell("!pip install matplotlib")

const execution = await sandbox.notebook.execCell(code)

// this contains the image data, you can e.g. save it to file or send to frontend
execution.results[0].png

await sandbox.close()
```

### Streaming code output

### Python

```plain text
from e2b_code_interpreter import CodeInterpreter

code = """
import time
import pandas as pd

print("hello")
time.sleep(3)
data = pd.DataFrame(data=[[1, 2], [3, 4]], columns=["A", "B"])
display(data.head(10))
time.sleep(3)
print("world")
"""

with CodeInterpreter() as sandbox:
    sandbox.notebook.exec_cell(code, on_stdout=print, on_stderr=print, on_result=(lambda result: print(result.text)))
```

### JavaScript

```plain text
import { CodeInterpreter } from '@e2b/code-interpreter'

const code = `
import time
import pandas as pd

print("hello")
time.sleep(3)
data = pd.DataFrame(data=[[1, 2], [3, 4]], columns=["A", "B"])
display(data.head(10))
time.sleep(3)
print("world")
`

const sandbox = await CodeInterpreter.create()

await sandbox.notebook.execCell(code, {
  onStdout: (out) => console.log(out),
  onStderr: (outErr) => console.error(outErr),
  onResult: (result) => console.log(result.text)
})

await sandbox.close()
```

## How the SDK works

The code generated by LLMs is often split into code blocks, where each subsequent block references the previous one. This is a common pattern in Jupyter notebooks, where each cell can reference the variables and definitions from the previous cells. In the classical sandbox each code execution is independent and does not share the context with the previous executions.

This is suboptimal for a lot of Python use cases with LLMs. Especially GPT-3.5 and 4 expects it runs in a Jupyter Notebook environment. Even when ones tries to convince it otherwise. In practice, LLMs will generate code blocks which have references to previous code blocks. This becomes an issue if a user wants to execute each code block separately which often is the use case.

This new code interpreter template runs a Jupyter server inside the sandbox, which allows for sharing context between code executions. Additionally, this new template also partly implements the Jupyter Kernel messaging protocol. This means that, for example, support for plotting charts is now improved and we don't need to do hack-ish solutions like in the current production version of our code interpreter.

## Pre-installed Python packages inside the sandbox

The full and always up-to-date list can be found in the requirements.txt file.


