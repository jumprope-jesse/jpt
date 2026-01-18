---
type: link
source: notion
url: https://simonwillison.net/2025/Oct/16/claude-skills/
notion_type: Tech Announcement
tags: ['Running']
created: 2025-10-17T20:00:00.000Z
---

# Claude Skills are awesome, maybe a bigger deal than MCP

## Overview (from Notion)
- Claude Skills represent a significant advancement in AI capabilities, potentially transforming how you automate tasks in your software projects.
- The ability to create and share skills easily can enhance your team's productivity, allowing you to delegate routine tasks effectively.
- With tools like Claude, you can automate workflows, like data visualization or report generation, which can free up time for your family or other pursuits.
- Consider the ethical implications of AI in your work—how do these advancements affect job security or the nature of software development?
- The concept of skills could inspire you to think about your own products; how can you integrate customizable features that adapt to user needs?
- While skills offer efficiency, there's a need for safe coding environments to mitigate risks like prompt injections, which can be a concern in your business.
- Explore how these tools might also serve as educational resources for your children, introducing them to programming and automation in a fun way.
- Alternative views could argue that reliance on AI might diminish critical thinking or problem-solving skills within teams—balance automation with personal involvement.

## AI Summary (from Notion)
Anthropic introduced Claude Skills, allowing the model to enhance task performance by loading specific instructions and scripts as needed. Skills are simple Markdown files that improve capabilities, such as creating GIFs for Slack. This new feature emphasizes the importance of a filesystem for executing commands, distinguishing it from previous models like MCP. Skills are easy to create and share, potentially leading to a surge in innovative applications, making them a significant advancement in AI capabilities.

## Content (from Notion)

Anthropic this morning introduced Claude Skills, a new pattern for making new abilities available to their models:

> 

Their engineering blog has a more detailed explanation. There’s also a new anthropic/skills GitHub repo.

(I inadvertently preempted their announcement of this feature when I reverse engineered and wrote about it last Friday!)

Skills are conceptually extremely simple: a skill is a Markdown file telling the model how to do something, optionally accompanied by extra documents and pre-written scripts that the model can run to help it accomplish the tasks described by the skill.

Claude’s new document creation abilities, which accompanied their new code interpreter feature in September, turned out to be entirely implemented using skills. Those are now available Anthropic’s repo covering .pdf, .docx, .xlsx, and .pptx files.

There’s one extra detail that makes this a feature, not just a bunch of files in disk. At the start of a session Claude’s various harnesses can scan all available skill files and read a short explanation for each one from the frontmatter YAML in the Markdown file. This is very token efficient: each skill only takes up a few dozen extra tokens, with the full details only loaded in should the user request a task that the skill can help solve.

Here’s that metadata for an example slack-gif-creator skill that Anthropic published this morning:

> 

I just tried this skill out in the Claude mobile web app, against Sonnet 4.5. First I enabled the slack-gif-creator skill in the settings, then I prompted:

> 

And Claude made me this GIF:

(OK, this particular GIF is terrible, but the great thing about skills is that they’re very easy to iterate on to make them better.)

Here are some noteworthy snippets from the Python script it wrote, comments mine:

```plain text
# Start by adding the skill's directory to the Python path
import sys
sys.path.insert(0, '/mnt/skills/examples/slack-gif-creator')

from PIL import Image, ImageDraw, ImageFont
# This class lives in the core/ directory for the skill
from core.gif_builder import GIFBuilder

# ... code that builds the GIF ...

# Save it to disk:
info = builder.save('/mnt/user-data/outputs/skills_vs_mcps.gif',
                    num_colors=128,
                    optimize_for_emoji=False)

print(f"GIF created successfully!")
print(f"Size: {info['size_kb']:.1f} KB ({info['size_mb']:.2f} MB)")
print(f"Frames: {info['frame_count']}")
print(f"Duration: {info['duration_seconds']:.1f}s")

# Use the check_slack_size() function to confirm it's small enough for Slack:
passes, check_info = check_slack_size('/mnt/user-data/outputs/skills_vs_mcps.gif', is_emoji=False)
if passes:
    print("✓ Ready for Slack!")
else:
    print(f"⚠ File size: {check_info['size_kb']:.1f} KB (limit: {check_info['limit_kb']} KB)")
```

This is pretty neat. Slack GIFs need to be a maximum of 2MB, so the skill includes a validation function which the model can use to check the file size. If it’s too large the model can have another go at making it smaller.

The skills mechanism is entirely dependent on the model having access to a filesystem, tools to navigate it and the ability to execute commands in that environment.

This is a common pattern for LLM tooling these days—ChatGPT Code Interpreter was the first big example of this back in early 2023, and the pattern later extended to local machines via coding agent tools such as Cursor, Claude Code, Codex CLI and Gemini CLI.

This requirement is the biggest difference between skills and other previous attempts at expanding the abilities of LLMs, such as MCP and ChatGPT Plugins. It’s a significant dependency, but it’s somewhat bewildering how much new capability it unlocks.

The fact that skills are so powerful and simple to create is yet another argument in favor of making safe coding environments available to LLMs. The word safe there is doing a lot of work though! We really need to figure out how best to sandbox these environments such that attacks such as prompt injections are limited to an acceptable amount of damage.

Back in January I made some foolhardy predictions about AI/LLMs, including that “agents” would once again fail to happen:

> 

I was entirely wrong about that. 2025 really has been the year of “agents”, no matter which of the many conflicting definitions you decide to use (I eventually settled on "tools in a loop").

Claude Code is, with hindsight, poorly named. It’s not purely a coding tool: it’s a tool for general computer automation. Anything you can achieve by typing commands into a computer is something that can now be automated by Claude Code. It’s best described as a general agent. Skills make this a whole lot more obvious and explicit.

I find the potential applications of this trick somewhat dizzying. Just thinking about this with my data journalism hat on: imagine a folder full of skills that covers tasks like the following:

- Where to get US census data from and how to understand its structure
- How to load data from different formats into SQLite or DuckDB using appropriate Python libraries
- How to publish data online, as Parquet files in S3 or pushed as tables to Datasette Cloud
- A skill defined by an experienced data reporter talking about how best to find the interesting stories in a new set of data
- A skill that describes how to build clean, readable data visualizations using D3
Congratulations, you just built a “data journalism agent” that can discover and help publish stories against fresh drops of US census data. And you did it with a folder full of Markdown files and maybe a couple of example Python scripts.

Model Context Protocol has attracted an enormous amount of buzz since its initial release back in November last year. I like to joke that one of the reasons it took off is that every company knew they needed an “AI strategy”, and building (or announcing) an MCP implementation was an easy way to tick that box.

Over time the limitations of MCP have started to emerge. The most significant is in terms of token usage: GitHub’s official MCP on its own famously consumes tens of thousands of tokens of context, and once you’ve added a few more to that there’s precious little space left for the LLM to actually do useful work.

My own interest in MCPs has waned ever since I started taking coding agents seriously. Almost everything I might achieve with an MCP can be handled by a CLI tool instead. LLMs know how to call cli-tool --help, which means you don’t have to spend many tokens describing how to use them—the model can figure it out later when it needs to.

Skills have exactly the same advantage, only now I don’t even need to implement a new CLI tool. I can drop a Markdown file in describing how to do a task instead, adding extra scripts only if they’ll help make things more reliable or efficient.

One of the most exciting things about Skills is how easy they are to share. I expect many skills will be implemented as a single file—more sophisticated ones will be a folder with a few more.

Anthropic have Agent Skills documentation and a Claude Skills Cookbook. I’m already thinking through ideas of skills I might build myself, like one on how to build Datasette plugins.

Something else I love about the design of skills is there is nothing at all preventing them from being used with other models.

You can grab a skills folder right now, point Codex CLI or Gemini CLI at it and say “read pdf/SKILL.md and then create me a PDF describing this project” and it will work, despite those tools and models having no baked in knowledge of the skills system.

I expect we’ll see a Cambrian explosion in Skills which will make this year’s MCP rush look pedestrian by comparison.

This is Claude Skills are awesome, maybe a bigger deal than MCP

ai 1624   prompt-engineering 166   generative-ai 1432   llms 1401   anthropic 193   claude 202   code-interpreter 28   ai-agents 71   coding-agents 73   claude-code 38 

Sponsor me for $10/month and get a curated email digest of the month's most important LLM developments.

 Sponsor & subscribe 


