---
type: link
source: notion
url: https://github.com/pretzelai/pretzelai/blob/main/README.md
notion_type: Software Repo
tags: ['Running']
created: 2024-07-03T09:18:00.000Z
---

# pretzelai/README.md at main · pretzelai/pretzelai · GitHub

## AI Summary (from Notion)
- Project Overview: Pretzel is an open-source alternative to Jupyter, enhancing its capabilities with features like AI code generation and inline tab completion.

- Key Features:
- AI code generation and editing.
- Inline tab completions for cells.
- AI sidebar for chat and code generation.
- Easy transition from Jupyter with compatibility for existing configurations.

- Installation:
- Can be installed using pip install pretzelai.
- A hosted version is available at pretzelai.app.

- Usage Instructions:
- Start typing in a cell for inline completions.
- Use "Ask AI" for code generation or editing prompts.
- The AI can modify existing code or inject new code based on prompts.

- Roadmap: Future features include:
- Real-time collaboration tools.
- SQL support and visual analysis tools.
- Enhanced code writing experience using Monaco editor.

- Privacy Policy: No personal information is collected; only anonymous telemetry for AI features is used. Users can delete their data anytime.

- Licensing: Uses AGPLv3 to prevent proprietary use of the code while allowing free use for individuals and companies.

- Company Plan: A hosted version will be available for companies with additional features, ensuring the individual version remains free.

- Interesting Facts:
- The project aims to improve the user experience for data professionals by minimizing switching costs from Jupyter.
- The founders emphasize rapid development and feature shipping, leading to a divergence from the Jupyter codebase.

## Content (from Notion)

### Pretzel 🥨

Modern, open-source Jupyter alternative.

Try it here »

Discord · Website · Issues · Contact

Pretzel.AI.Overview.with.Subtitles.mp4

Pretzel is a fork of Jupyter with the goal to improve Jupyter's capabilities. For our first few features, we've added AI code generation and editing, inline tab completion, sidebar chat and error fixing to Jupyter.

Switching to Pretzel from Jupyter is extremely easy since it's simply an improved version of Jupyter. All of your Jupyter config, settings, keybindings, and extensions will work out of the box.

## Quick Start

- Installation: pip install pretzelai then run pretzel lab to open the web interface. OR, use our free hosted version: pretzelai.app
- Simply start typing in a cell to get inline tab completions
- In any Jupyter cell, click “Ask AI” or press Cmd+K (Mac) / Ctrl+K (Linux/Windows) to prompt AI
- Use the AI Sidebar with Ctrl+Cmd+B (Mac) or Ctrl+Alt+B (Linux/Windows) to chat with AI, generate code, and ask questions
- To switch to your own OpenAI API key, see the Configuration section
Our roadmap includes building features such as:

- Native AI code generation and understanding features similar to Cursor
- Frictionless realtime collaboration: pair-programming, comments, version history, etc.
- SQL support (both in code cells and as a standalone SQL IDE)
- Visual analysis builder (see more here)
- VSCode like code-writing experience using Monaco
- 1-click dashboard creation and sharing from Jupyter notebooks
## Installation

You can install Pretzel by using pip:

```plain text
pip install pretzelai

```

If using conda, first install pip with conda install pip followed by pip install pretzelai.

Then, start Pretzel with:

```plain text
pretzel lab

```

Just as with Jupyter, you should see a URL to access the Pretzel interface.

To use your own OpenAI API key, see the Configuration section.

Bleeding Edge Version

Bugs possible. To use the latest version of Pretzel:

- Make sure Node.js is installed and is version 20
- Clone and install the package
```plain text
git clone https://github.com/pretzelai/pretzelai.git
cd pretzelai
pip install .

```

## Usage

### Inline Tab Completion

- Start typing in a cell to get inline tab completions with Mistral's Codestral
- Wait for 1 second to trigger completions
### Generating and editing code in notebook cells

- In a cell, press Cmd+K (Mac) / Ctrl+K (Windows/Linux) or click "Ask AI" to open AI prompt textbox and write your code generation/editing instruction 
- If there's existing code in a cell, the prompt will edit the existing code 
- You can accept/reject the response or edit your prompt if you want to re-submit with modifications
- Use ↑ / ↓ to cycle through prompt history
### Using the AI Sidebar

- Use Ctrl+Cmd+B (Mac) / Ctrl+Alt+B (Linux/Windows) or the Pretzel Icon on the right sidebar to activate the AI Sidebar
- You can ask questions, generate code, or search for existing code
- The AI always uses the code in the active cell as context. If you highlight some code in the active cell, only the highlighted code will be used as context
- Mention @notebook to send additional relevant code in the current notebook as context to the AI
Example uses of AI Sidebar:

- "Modify the function my_function in @notebook to be more efficient" ← this will search for the function my_function in the whole notebook and modify it
- "Where is the code in @notebook that removes outliers"? ← this will search for code that removes outliers in the whole notebook
- "Can you explain what this code does?" ← this will explain the code in the current cell
### Adding code in the middle of existing code

- Put your cursor either on an empty line or an existing line of code. Bring up the AI prompting text box with Cmd+K
- Start your prompt with the word inject or ij (case-insensitive) - this tells the AI to only add new code and not edit the existing code in the cell
- Code will be added one line below where your cursor was placed
### Fix errors with AI

- When there's an error, you'll see a button on top-right "Fix Error with AI". Click it try fixing the error
## Configuration

Pretzel works out-of-the-box, no configuration needed.

Pretzel uses our free AI server by default. You can configure it to use your own OpenAI/Azure API key instead.

OpenAI Support

- Open the Settings menu in the top menubar, then click Settings Editor
- Search for Pretzel and select Pretzel AI Settings on the left bar
- From the AI Service dropdown, select OpenAI API Key and fill out your API key under OpenAI Settings > API Key.
- If your company uses OpenAI Enterprise, then you can also enter the base URL for OpenAI call under OpenAI Settings
- We use GPT-4o as the default model. You can change this with the OpenAI Model dropdown.
Azure Support Just as with OpenAI settings, you can also use Azure hosted models if you select Use Azure API in the AI Service dropdown. We haven't tested this yet so there may be bugs.

## Feedback, bugs and docs

- Please report bugs here: https://github.com/pretzelai/pretzelai/issues
- Have any feedback? Any complains? We'd love feedback: founders@withpretzel.com
## Jupyter specific information

The original Jupyter documentation is available here and the Jupyterlab README is available here.

## Privacy Policy, Data Collection and Retention

We collect no personal information. We use basic telemetry for only the AI features we've built - for example, when you click on "Ask AI", we receive an event that someone clicked on "Ask AI". We only associate an anonymous ID to your user. If you allow cookies, that helps us tell that it's the same user across multiple browser sessions (which is very helpful!). If you don't allow cookies, every time you open a browser, you're a new anonymous user to us.

We also collect prompts (but not the responses) for the AI features we've built. This can be turned off in the settings (Settings > Pretzel AI > Uncheck Prompt Telemetry) but we'd really appreciate if you didn't - this is very helpful in improving our prompts.

We do not collect any code whatsoever. Even when you use Pretzel's cloud AI server for completions, we don't store any of this code.

If you use the hosted version of Pretzel (https://pretzelai.app), we create a user for you based on your email address. You can always simply log-in and delete any data you may have stored on our hosted server. We make no backups or copies of your data.

Our hosted server is free to use. However, we will delete your data and your account 30 days after your last login. If you'd like to delete your account sooner, please email us at founders@withpretzel.com with the subject line "Account Deletion" and we'll delete your account immediately.

## FAQ

Q. What happened to the old version of Pretzel AI - the visual, in-browser data manipulation tool?

A. It's available in the pretzelai_visual folder here. Please see this PR for more info.

Q. What AI model does Pretzel use?

A. Pretzel uses different AI models for various tasks:

1.  
1.  
1.  
We're continuing to experiment with models and supporting local models and Anthropic's Claude is at the top of our list.

Q. What about feature X?

A. There's a ton we want to build. Please open an issue and tell us what you want us to build!

Q. Where's the roadmap?

A. We have a rough roadmap at the top of this README. There are many features we'd like to build, but there's just two of us. So, we're collecting feedback about what would be most helpful. Please open an issue or just email us with your feedback! Based on what we find, we'll prioritize our roadmap.

Q. Why are you using the AGPL license? Or, why not use MIT/BSD3 licenses?

A. Our goal with building Pretzel is to make an amazing data tool that is free for both individuals and companies to use. That said, we are a two-person startup - and we don't want some third party to just take our code and sell a hosted version of it without giving back to the community. Jupyter code is licensed as BSD-3 and if we keep our new code BSD-3 licensed, there would be no way to stop a third party from doing this. As a result, we went with the AGPLv3 license for all the new code. This ensures that if someone else does want to take our code and sell it (SaaS or otherwise), they have to open-source all of their modifications under AGPLv3 as well.

Q. Why a fork of Jupyter? Why not contribute into Jupyter directly?

A. This deserves a longer answer but here's the short answer: We've set out to make the new de-facto, modern, open-source data tool. Initially, we wanted to start from scratch. However, after talking to several data professionals, we realized it will be very hard to get people to switch to a new tool, no matter how good. The best way to get people to switch is to not have them switch at all. That's why we decided to fork Jupyter - for the near zero switching costs. Also, Jupyter is a mature product, and we're shipping feature really fast - frankly, at the pace we're shipping features, the code we write won't be accepted into the Jupyter codebase 😅. There are also many downsides to this decision - we've had to spend considerable time understanding the whole Jupyter ecosystem and multiple codebases, the complex release processes, the various APIs etc. However, we think this is the right decision for us.

Q. My company is worried about using an AGPLv3 licensed tool. What can I do?

A. The AGPL is a barrier ONLY IF you're modifying Pretzel AND redistributing it to the public. If you're simply using it as a tool in your company (even with modifications), the AGPL DOES NOT ask you to share your code. Still, if AGPL is an issue for you, please contact us, and we can figure out something that works.

Q. How are you planning on making money? OR, how are you free? I'm worried that you'll make this tool paid in the future.

A. We're planning on selling a hosted version of the tool to companies to make money. This hosted version will probably have some company specific features that individuals don't want or need such as data access controls, connectors for data sources, integration with GitHub, hosted and shareable dashboard, scalable and on-demand compute for large data jobs etc. We will not retroactively make Pretzel's individual version paid.


