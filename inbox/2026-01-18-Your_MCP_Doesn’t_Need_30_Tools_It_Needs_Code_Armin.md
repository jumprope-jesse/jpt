---
type: link
source: notion
url: https://lucumr.pocoo.org/2025/8/18/code-mcps/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2025-08-18T13:15:00.000Z
---

# Your MCP Doesn’t Need 30 Tools: It Needs Code | Armin Ronacher's Thoughts and Writings

## Overview (from Notion)
- The discussion on MCP (Model Context Protocol) versus CLI (Command Line Interface) tools highlights the importance of adaptability in your software development practices, especially as a founder needing efficient solutions.
- The idea of using MCP servers that expose a single tool for executing code could streamline your workflows, making it easier to manage complex tasks without the clutter of multiple tools.
- The focus on stateful sessions in MCP could enhance your debugging process, allowing you to maintain context when working on projects—important for balancing work and family life.
- Embracing programming languages like Python in MCP could empower you to create more robust and reusable scripts, potentially saving time on repetitive tasks.
- The exploration of security implications with agentic coding raises a crucial awareness of risks, emphasizing the need for safe coding practices in your projects.
- The example of debugging with tools like pexpect and Playwright illustrates how integrating these technologies can improve the efficiency of your software testing and development processes.
- Alternate views might consider the trade-offs between simplicity and complexity; while less tools could mean less overhead, it might also limit flexibility in some scenarios.
- Reflect on how these technological advancements can not just benefit your work but also allow you to set a positive example for your kids about the importance of innovation and adaptability in a fast-paced world.

## AI Summary (from Notion)
The discussion emphasizes the limitations of traditional command-line tools and advocates for using Model Context Protocol (MCP) servers that accept programming code as input. It highlights challenges with CLI tools, such as platform dependence and session management, and proposes a stateful Python interpreter as a solution. The approach allows for better composability and reusability of code, enabling agents to debug applications more effectively and automate tasks with fewer tool calls, ultimately improving efficiency in coding practices.

## Content (from Notion)

- blog
- archive
- projects
- travel
- talks
- about
I wrote a while back about why code performs better than MCP (Model Context Protocol) for some tasks. In particular, I pointed out that if you have command line tools available, agentic coding tools seem very happy to use those. In the meantime, I learned a few more things that put some nuance to this. There are a handful of challenges with CLI-based tools that are rather hard to resolve and require further examination.

In this blog post, I want to present the (not so novel) idea that an interesting approach is using MCP servers exposing a single tool, that accepts programming code as tool inputs.

## CLI Challenges

The first and most obvious challenge with CLI tools is that they are sometimes platform-dependent, version-dependent, and at times undocumented. This has meant that I routinely encounter failures when using tools on first use.

A good example of this is when the tool usage requires non-ASCII string inputs. For instance, Sonnet and Opus are both sometimes unsure how to feed newlines or control characters via shell arguments. This is unfortunate but ironically not entirely unique to shell tools either. For instance, when you program with C and compile it, trailing newlines are needed. At times, agentic coding tools really struggle with appending an empty line to the end of a file, and you can find some quite impressive tool loops to work around this issue.

This becomes particularly frustrating when your tool is absolutely not in the training set and uses unknown syntax. In that case, getting agents to use it can become quite a frustrating experience.

Another issue is that in some agents (Claude Code in particular), there is an extra pass taking place for shell invocations: the security preflight. Before executing a tool, Claude also runs it through the fast Haiku model to determine if the tool will do something dangerous and avoid the invocation. This further slows down tool use when multiple turns are needed.

In general, doing multiple turns is very hard with CLI tools because you need to teach the agent how to manage sessions. A good example of this is when you ask it to use tmux for remote-controlling an LLDB session. It’s absolutely capable of doing it, but it can lose track of the state of its tmux session. During some tests, I ended up with it renaming the session halfway through, forgetting that it had a session (and thus not killing it).

This is particularly frustrating because the failure case can be that it starts from scratch or moves on to other tools just because it got a small detail wrong.

## Composability

Unfortunately, when moving to MCP, you immediately lose the ability to compose without inference (at least today). One of the reasons lldb can be remote-controlled with tmux at all is that the agent manages to compose quite well. How does it do that? It uses basic tmux commands such as tmux send-keys to send inputs or tmux capture-pane to get the output, which don’t require a lot of extra tooling. It then chains commands like sleep and tmux capture-pane to ensure it doesn’t read output too early. Likewise, when it starts to fail with encoding more complex characters, it sometimes changes its approach and might even use base64 -d.

The command line really isn’t just one tool — it’s a series of tools that can be composed through a programming language: bash. The most interesting uses are when you ask it to write tools that it can reuse later. It will start composing large scripts out of these one-liners. All of that is hard with MCP today.

## Better Approach To MCP?

It’s very clear that there are limits to what these shell tools can do. At some point, you start to fight those tools. They are in many ways only as good as their user interface, and some of these user interfaces are just inherently tricky. For instance, when evaluated, tmux performs better than GNU screen, largely because the command-line interface of tmux is better and less error-prone. But either way, it requires the agent to maintain a stateful session, and it’s not particularly good at this today.

What is stateful out of the box, however, is MCP. One surprisingly useful way of running an MCP server is to make it an MCP server with a single tool (the ubertool) which is just a Python interpreter that runs eval() with retained state. It maintains state in the background and exposes tools that the agent already knows how to use.

I did this experiment in a few ways now, the one that is public is pexpect-mcp. It’s an MCP that exposes a single tool called pexpect_tool. It is, however, in many ways a misnomer. It’s not really a pexpect tool — it’s a Python interpreter running out of a virtualenv that has pexpect installed.

What is pexpect? It is the Python port of the ancient expect command-line tool which allows one to interact with command-line programs through scripts. The documentation describes expect as a “program that ‘talks’ to other interactive programs according to a script.”

What is special about pexpect is that it’s old, has a stable API, and has been used all over the place. You could wrap expect or pexpect with lots of different MCP tools like pexpect_expect, pexpect_sendline, pexpect_spawn, and more. That’s because the pexpect.Spawn class exposes 36 different API functions! That’s a lot. But many of these cannot be used in isolation well anyway. Take this motivating example from the docs:

```plain text
child = pexpect.spawn('scp foo user@example.com:.')
child.expect('Password:')
child.sendline(mypassword)

```

Even the most basic use here involves three chained tool calls. And that doesn’t include error handling, which one might also want to encode.

So instead, a much more interesting way to have this entire thing run is to just have the command language to the MCP be Python. The MCP server turns into a stateful Python interpreter, and the tool just lets it send Python code that is evaluated with the same state as before. There is some extra support in the MCP server to make the experience more reliable (like timeout support), but for the most part, the interface is to just send Python code. In fact, the exact script from above is what an MCP client is expected to send.

The tool description just says this:

```plain text
Execute Python code in a pexpect session. Can spawn processes and interact with
them.

Args:
  `code`: Python code to execute. Use 'child' variable to interact with the
  spawned process. The pexpect library is already imported. Use
  `pexpect.spawn(...)` to spawn something. timeout: Optional timeout in seconds.
  If not provided, uses global `TIMEOUT` (default 30s).

Example:
  child = pexpect.spawn('lldb ./mytool')
  child.expect("(lldb)")

Returns:
  The result of the code execution or an error message.

```

This works because the interface to the MCP is now not just individual tools it has never seen — it’s a programming language that it understands very well, with additional access to an SDK (pexpect) that it has also seen and learned all the patterns from. We’re relegating the MCP to do the thing that it does really well: session management and guiding the tool through a built-in prompt.

More importantly, the code that it writes is very similar to what it might put into a reusable script. There is so little plumbing in the actual MCP that you can tell the agent after the session to write a reusable pexpect script from what it learned in the session. That works because all the commands it ran are just Python — they’re still in the context, and the lift from that to a reusable Python script is low.

## Do It, Then Do It Again

Now I don’t want to bore you too much with lots of Claude output, but I took a crashing demo app that Mario wrote and asked it to debug with LLDB through pexpect_tool. Here is what that looked like:

Afterwards I asked it to dump it into a reusable Python script to be run later:

And from a fresh session we can ask it to execute it once more:

```plain text
> please run debug_demo.py with uv run to figure out what's going on

⏺ Bash(uv run debug_demo.py)
  ⎿  Starting lldb debugging session for ./demo-buggy
     ✓ LLDB started successfully
     … +155 lines (ctrl+r to expand)

⏺ The debug script successfully ran and identified the issue! Here's what it found:

  Main Problem: The demo-buggy executable crashes with a segfault in the add_score()
  function because s->scores is NULL (not allocated memory).

  Root Cause: Line 18 in create_student() is commented out, which means the scores
  array is never allocated.

  Fix: Uncomment line 18 in the create_student() function to allocate memory for the
  scores array.

  Additional Issue: There's also an off-by-one error in the calculate_average()
  function.

  The debugging session shows that:
  1. LLDB successfully launched and set a breakpoint at main
  2. The program stopped at the breakpoint
  3. It identified that alice and bob Student pointers were created
  4. The crash occurs when trying to access unallocated memory for scores

  This demonstrates that the pexpect MCP tool is working correctly for debugging C
  programs with LLDB!

```

That again works because the code it writes into the MCP is very close to the code that it would write into a Python script. And the difference is meaningful. The initial debug takes about 45 seconds on my machine and uses about 7 tool calls. The re-run with the dumped playbook takes one tool call and finishes in less than 5 seconds. Most importantly: that script is standalone. I can run it as a human, even without the MCP!

## Novel Things

Now the above example works beautifully because these models just know so much about pexpect. That’s hardly surprising in a way. So how well does this work when the code that it should write is entirely unknown to it? Well, not quite as well. However, and this is the key part, because the meta input language is Python, it means that the total surface area that can be exposed from an ubertool is pretty impressive.

A general challenge with MCP today is that the more tools you have, the more you’re contributing to context rot. You’re also limited to rather low amounts of input. On the other hand, if you have an MCP that exposes a programming language, it also indirectly exposes a lot of functionality that it knows from its training.

For instance, one of the really neat parts about this is that it knows dir(), globals(), repr(), and other stuff. Heck, it even knows about sys._getframe(). This means that you can give it very rudimentary instructions about how its sandbox operates and what it might want to do to learn more about what is available to it as needed. You can also tell it in the prompt that there is a function it can run to learn more about what’s available when it needs help!

So when you build something that is completely novel, at least the programming language is known. You can, for instance, write a tiny MCP that dumps out the internal state of your application, provides basic query helpers for your database that support your sharding setup, or provides data reading APIs. It will discover all of this anyway from reading the code, but now it can also use a stateful Python or JavaScript session to run these tools and explore more.

This is also a fun feature when you want to ask the agent to debug the MCP itself. Because Python and JavaScript are so powerful, you can, for instance, also ask it to debug the MCP’s state itself when something went wrong.

## Security Is A Sham

The elephant in the room for all things agentic coding is security. Claude mostly doesn’t delete your machine and maybe part of that is the Haiku preflight security check. But isn’t all of this a sham anyway? I generally love to watch how Claude and other agents maneuver their way around protections in pretty creative ways. Clearly it’s potent and prompt-injectable. By building an MCP that just runs eval(), we might be getting rid of some of the remaining safety here.

But does it matter? We are seemingly okay with it writing code and running tests, which is the same kind of bad as running eval(). I’m sure the day of reckoning will come for all of us, but right now we’re living in this world where protections don’t matter and we can explore what these things can do.

I’m honestly not sure how to best protect these things. They are pretty special in that they are just inherently unsafe and impossible to secure. Maybe the way to really protect them would be to intercept every system call and have some sort of policy framework/sandbox around the whole thing. But even in that case, what prevents an ever more clever LLM from circumventing all these things? It has internet access, it can be prompt-injected, and all interfaces we have for them are just too low-level to support protection well.

So to some degree, I think the tail risks of code execution are here to stay. But I would argue that they are not dramatically worse when the MCP executes Python code. In this particular case, consider that pexpect itself runs programs. There is little point in securing the MCP if what the MCP can run is any bash command.

## Taking It Further

As interesting as the pexpect case is, that was not my original motivation. What I started to look into is replacing Playwright’s MCP with an MCP that just exposes the Playwright API via JavaScript. This is an experiment I have been running for a while, and the results are somewhat promising but also not promising enough yet. If you want to play with it, the MCP is called “playwrightess” is pretty simple. It just lets it execute JavaScript code against a sync playwright client. Same idea. Here, the tool usage is particularly nice because it gets down from ~30 tool definitions to 1:

The other thing that is just much nicer about this approach is how many more ways it has to funnel data out. For instance console.log from both the browser as well as the playwright script are forwarded back to the agent automatically. There is no need for the agent to ask for that information, it comes automatically. It also has a state variable that it can use to accumulate extra information between calls which it liberally uses if you for instance ask it to collect data from multiple pages in a pagination. It can do that without any further inference, because the loop happens within JavaScript.

Same with pexpect — you can easily get it to dump out a script for later that circumvents a lot of MCP calls with something it already saw. Particularly when you are debugging a gnarly issue and you need to restart the debugging more than once, that shows some promise. Does it perform better than Playwright MCP? Not in the current form, but I want to see if this idea can be taken further. It is quite verbose in the scripts that it writes, and it is not really well tuned between screenshots and text extraction.


