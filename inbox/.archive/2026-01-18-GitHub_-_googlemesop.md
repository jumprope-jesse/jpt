---
type: link
source: notion
url: https://github.com/google/mesop
notion_type: Software Repo
tags: ['Running']
created: 2024-06-10T02:15:00.000Z
---

# GitHub - google/mesop

## AI Summary (from Notion)
- Project Title: Mesop
- Creation Date: June 10, 2024
- Status: Not started
- Tags: Running
- Purpose: A Python-based UI framework for rapid web app development, primarily for internal use at Google.

- Key Features:
- User-Friendly: Designed for UI novices with an idiomatic Python approach.
- Reactive UI Paradigm: Easy to understand and utilize.
- Developer Efficiency: Offers hot reload and rich IDE support.

- Flexibility:
- Allows building custom UIs without needing JavaScript, CSS, or HTML.
- UI components are defined as Python functions.

- Quick Start:
- Users can write their first Mesop app in under 10 lines of code.

- Installation & Usage:
- Install via pip and run with a simple command.

- Collaboration with Google Colab:
- Users can experiment with Mesop on Colab easily.

- Disclaimer:
- Note that this is not an officially supported Google product.

## Content (from Notion)

# Mesop: Build delightful web apps quickly in Python 🚀

### Used at Google for rapid internal app development

Mesop is a Python-based UI framework that allows you to rapidly build web apps like demos and internal apps:

Intuitive for UI novices ✨

- Write UI in idiomatic Python code
- Easy to understand reactive UI paradigm
- Ready to use components
Frictionless developer workflows 🏎️

- Hot reload so the browser automatically reloads and preserves state
- Rich IDE support with strong type safety
Flexible for delightful demos 🤩

- Build custom UIs without writing Javascript/CSS/HTML
- Compose your UI into components, which are just Python functions
## Write your first Mesop app in less than 10 lines of code...

Demo app

```plain text
import time

import mesop as me
import mesop.labs as mel


@me.page(path="/text_to_text", title="Text I/O Example")
def app():
  mel.text_to_text(
    upper_case_stream,
    title="Text I/O Example",
  )


def upper_case_stream(s: str):
  yield s.capitalize()
  time.sleep(0.5)
  yield "Done"
```

## Try it

### Colab

You can try Mesop on Colab!

### Locally

Step 1: Install it

```plain text
$ pip install mesop
```

Step 2: Copy the example above into main.py

Step 3: Run the app

```plain text
$ mesop main.py
```

Learn more in Getting Started.

## Disclaimer

This is not an officially supported Google product.


