---
type: link
source: notion
url: https://jyn.dev/theory-building-without-a-mentor/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2025-12-22T02:41:00.000Z
---

# theory building without a mentor

## Overview (from Notion)
- The approach to theory building without a mentor emphasizes self-reliance and adaptability, valuable traits for balancing family life and entrepreneurship.
- It encourages developing a deep understanding of programs, which can parallel the ongoing learning required in parenting and managing a business.
- The emphasis on small, manageable changes in code reflects the need for incremental progress in personal and professional life.
- Unique viewpoint: The idea that recovering a theory solely from code is possible can inspire confidence in tackling challenges, both in software projects and in family life.
- Alternate view: Some may argue that mentorship provides invaluable insights that cannot be replicated through self-study, highlighting the importance of community and connections in both coding and parenting.
- The content underscores the importance of flexibility and adaptation, traits essential for navigating the complexities of family and business life in a dynamic city like New York.

## AI Summary (from Notion)
Theory building in programming involves understanding and creating a conceptual framework from code and documentation. It emphasizes that while recovering a theory solely from documentation is challenging, it is possible through focused investigation of specific code sections. The process includes identifying relevant parts, verifying understanding through experiments, and matching existing code patterns. Additionally, modifying theories over time is essential as team dynamics change, impacting software development. Effective theory building aids in debugging and feature enhancement.

## Content (from Notion)

NOTE: if you are just here for the how-to guide, click here to skip the philosophizing.

## theory building

Peter Naur wrote a famous article in 1985 called Programming as Theory Building. it has some excellent ideas, such as:

> 

> 

> 

i think this article is excellent, and highly recommend reading it in full. however, i want to discuss one particular idea Naur mentions:

> 

i do not think it is true that it is impossible to recover a theory of the program merely from the code and docs. my day job, and indeed one of my most prized skills when i interview for jobs, is creating a theory of programs from their text and documentation alone. this blog post is about how i do that, and how you can too.

## theory modification

Naur also says in the article:

> 

i think this is wrong: theory modification is exactly what Ward Cunningham describes as "consolidation" in his 1992 article on Technical Debt. i highly recommend the original article, but the basic idea is that over time, your understanding of how the program should behave changes, and you modify and refactor your program to match that idea. this happens in all programs, but the modification is easier in programs with little technical risk.

furthermore, this theory modification often happens unintentionally over time as people are added and removed from teams. as ceejbot puts it:

> 

i bring this up to note that you will never recover the same theory as the original programmers (at least, not without talking to them directly). the most you can do is to recover one similar enough that it does not require large changes to the program. in other words, you are creating a new theory of the program, and may end up having to adapt the program to your new theory.

## recreating a theory

this is useful both when fixing bugs and when adding new features; i will focus on new features because i want to emphasize that these skills are useful any time you modify a program. for a focus on debugging, see Julia Evans' Pocket Guide to Debugging.

this post is about creating theories at the "micro" level, for small portions of the program. i hope to make a post about the "macro" level in the future, since that's what really lets you start making design decisions about a program.

i recently made a PR to neovim, having never worked on neovim before; i'll use that as an example going forward. i highly recommend following along with a piece of code you want to learn more about. if you don't have one in mind, i have hidden all the examples behind a drop-down menu, so you can try to apply the ideas on your own before seeing how i use them. 
the investigation i did in this blog post was based off neovim commit 57d99a5. 
Click here to close all notes.

### where to start

to start off, you need an idea of what change you want to make to the program. almost always, programs are too large for you to get an idea of the whole program at once. instead, you need to focus on theory-building for the parts you care about, and only understand the rest of the program to the extent that the parts you care about interact with it.

in my neovim PR, i cared about the :drop command, which opens a file if it isn't loaded, or switches to the relevant buffer if it is. specifically i wanted to extend the "switch to the relevant buffer" part to also respect +cmd, so that i could pass it a line number.

### finding the parts you care about

there are several ways to get started here. the simplest is just finding the relevant part of the code or docs—if you can provoke an error that's related to the part of the code you're changing, you can search for that error directly. often, knowing how execution reaches that state is very helpful, which you can do by getting a backtrace. you can get backtraces for output from arbitrary programs with liberal use of rr, but if you're debugging rustc specifically, there's actually a built-in flag for this, so you can just use rustc file.rs -Z treat-err-as-bug.

for :drop, this didn't work: it was documented on neovim's site, but i didn't know a :drop-specific error to search for.

if this doesn't print an error message, or if it's not possible to get a recording of the program, things are harder. you want to look for something you already know the name of; search for literal strings with that name, or substrings that might form part of a template.

:drop 
for :drop i searched for the literal string "drop", since something needs to parse commands and it's not super common for it to be on its own in a string. that pulled up the following hits: 

 
ex_docmd.c looked promising, so i read the code around there.

```plain text
$ rg '"drop"' src
src/nvim/ex_docmd.c:4196:  } else if (STRICMP(p, "drop") == 0) {
src/nvim/ex_docmd.c:4213:    "drop",
src/nvim/ex_docmd.c:4302:    // "drop".
src/nvim/eval.c:7146:    len += 7 + 4;  // " ++bad=" + "keep" or "drop"

```

sometimes triggering the condition is hard, so instead i read the source code to reverse-engineer the stack trace. seeing all possible call sites of a function is instructive in itself, and you can usually narrow it down to only a few callers by skimming what the callers are doing. i highly recommend using an LSP for this part since the advantage comes from seeing all possible callers, not just most, and regex is less reliable than proper name resolution.

:drop 
it turned out that none of the code i found in my search was for :drop itself, but i did find it was in a function named get_bad_opt. get_bad_opt had only one caller, getargopt. that was called by do_one_cmd. the doc-comment on do_one_cmd mentions that it parses the string, but i am not used to having documentation so i went up one level too far to do_cmdline. at that point, looking at the call site of do_one_cmd, i realized i had gone too far because it was passing in the whole string of the Ex command line. i found a more relevant part of the code by looking at the uses of cmdlinep in do_one_cmd: 

 
i got lucky - this was not actually the code i cared about, but the bit i did care about had a similar name, so i found it by searching for cmdname: 

 
from there i went to the definition of cmdnames (in build/src/nvim/auto/ex_cmds_defs.generated.h) and found "drop" in that file: 

 
and from there found that the function i cared about was called ex_drop. 
if i had been a little more careful, i could have found CMD_drop sooner with rg -ul '"drop"' (this time without filtering out hidden files or limiting to the source directory). but this way worked fine as well.

```plain text
      char *cmdname = after_modifier ? after_modifier : *cmdlinep;

```

```plain text
  // 6. Parse arguments.  Then check for errors.
  if (!IS_USER_CMDIDX(ea.cmdidx)) {
    ea.argt = cmdnames[(int)ea.cmdidx].cmd_argt;
  }

```

```plain text
  [CMD_drop] = {
    .cmd_name = "drop",
    .cmd_func = (ex_func_T)&ex_drop,
    .cmd_preview_func = NULL,
    .cmd_argt = 147854L,
    .cmd_addr_type = ADDR_NONE
  },

```

### verifying your understanding

do mini experiments: if you see an error emitted in nearby code, try to trigger it so that you verify you're looking in the right place. when debugging, i often use process of elimination to narrow down callers: if an error would have been emitted if a certain code path was taken, or if there would have been more or less logging, i can be sure that code i am looking at was not run.

the simplest experiment is just exit(1); it's easy to notice and doesn't change the state of the program, and it can't fail. other experiments could include "adding custom logging" or "change the behavior of the function", which let you perform multiple experiments at once and understand how the function impacts its callers.

for more complicated code, i like to use a debugger, which lets you see much more of the state at once. if possible, in-editor debuggers are really nice—vscode, and since recently, zed, have one built-in; for nvim i use nvim-dap-ui. you can also just use a debugger in a terminal. some experiments i like to try:

- breaking at a function to make sure it is executed
- printing local variables
- setting hardware watchpoints on memory to see where something is modified (this especially shines in combination with a time-travel debugger)
:drop 
for :drop, i was quite confident i had found the right code, so i didn't bother with any experiments. there are other cases where it's more useful; i made an earlier PR to tmux where there were many different places search happened, so verifying i was looking at the right one was very helpful. specifically i added exit(1) to the function i thought was the right place, since debug logging in tmux is non-trivial to access. 
i rarely use a debugger for adding new code; mostly i use it for debugging existing code. programs complicated enough that i need a debugger just to understand control flow usually have a client/server model that also makes them harder to debug, so i don't bother and just read the source code.

reading source code is also useful for finding examples of how to use an API. often it handles edge cases you wouldn't know about by skimming, and uses helper functions that make your life simpler. your goal is to make your change as similar to the existing codebase as possible, both to reduce the risk of bugs and to increase the chance the maintainer likes your change.

when i write new code, i will usually copy a small snippet from elsewhere in the codebase and modify it to my needs. i try to copy at most 10-15 lines; more than that indicates that i should try to reuse or create a higher-level API.

:drop 
once in ex_drop, i skimmed the code and found a snippet looked like it was handling existing files: 

 
the bug here is not any code that is present; instead it's code that's missing. i had to figure out where +cmd was stored and how to process it. so, i repeated a similar process for +cmd. this time i had something more to start with - i knew the command structure was named eap and had type exarg_t. looking at the definition of struct exarg showed me what i wanted: 

 
looking for do_ecmd_cmd, i found do_exbuffer (with a helpful comment saying it was responsible for :buffer) which called do_cmdline_cmd, and in turn do_cmdline. looking at the callers of do_cmdline i found do_ecmd, which handles :edit. :edit has exactly the behavior i wanted for :drop, so i copied its behavior:  
out of caution, i also looked at the other places in the function that handled command, and it's a good thing i did, because i found this wild snippet above: 

 
i refactored this into a helper function and then called it from both the original :edit command and my new code in :drop.

```plain text
  FOR_ALL_TAB_WINDOWS(tp, wp) {
    if (wp->w_buffer == buf) {
      goto_tabpage_win(tp, wp);
      curwin->w_arg_idx = 0;
      if (!bufIsChanged(curbuf)) {
        const int save_ar = curbuf->b_p_ar;
        // reload the file if it is newer
        curbuf->b_p_ar = true;
        buf_check_timestamp(curbuf);
        curbuf->b_p_ar = save_ar;
      }
      if (curbuf->b_ml.ml_flags & ML_EMPTY) {
        ex_rewind(eap);
      }
      return;
    }
  }

```

```plain text
  char *do_ecmd_cmd;            ///< +command arg to be used in edited file

```

```plain text
  if ((command != NULL || newlnum > 0)
      && *get_vim_var_str(VV_SWAPCOMMAND) == NUL) {
    // Set v:swapcommand for the SwapExists autocommands.
    const size_t len = (command != NULL) ? strlen(command) + 3 : 30;
    char *const p = xmalloc(len);
    if (command != NULL) {
      vim_snprintf(p, len, ":%s\r", command);
    } else {
      vim_snprintf(p, len, "%" PRId64 "G", (int64_t)newlnum);
    }
    set_vim_var_string(VV_SWAPCOMMAND, p, -1);
    did_set_swapcommand = true;
    xfree(p);
  }

```

this works in much the same way. try to find existing tests by using the same techniques as finding the code you care about. read them; write them using existing examples. tests are also code, after all.

test suites usually have better documentation than the code itself, since adding new tests is much more common than modifying any particular section of code; see if you can find the docs. i look for CONTRIBUTING.md files, and if i don't find them i fall back to skimming the readme. sometimes there are is also a README.md in the folder where the tests are located, although these tend to be somewhat out of date.

i care a lot about iteration times, so i try and find how to run individual tests. that info is usually in the README, or sometime you can figure it out from the test command's --help output.

run your tests! ideally, create and run your tests before modifying the code so that you can see that they start to pass after your change. tests are extra important when you don't already understand the code, because they help you verify that your new theory is correct. run existing tests as well; run those before you make changes so you know which failures are spurious (a surprisingly high number of codebases have flaky or environment-dependent tests).

i started by looking for existing tests for :drop: 

 
fortunately this had results right away and i was able to start adding my new test. CONTRIBUTING.md had a pointer to test/README.md which documented TEST_FILE and mak functionaltest. neovim has very good internal tooling and when my screen:expect() call failed it gave me a very helpful pointer to screen:snapshot_util.

```plain text
$ rg :drop test
test/functional/ex_cmds/drop_spec.lua:8:describe(':drop', function()
test/functional/ex_cmds/drop_spec.lua:75:      :drop Xdrop_modified.txt           |
test/old/testdir/test_winfixbuf.vim:1094:" Fail :drop but :drop! is allowed
test/old/testdir/test_excmd.vim:92:" Test for the :drop command
test/old/testdir/test_excmd.vim:775:  call term_sendkeys(buf, ":drop Xdrop_modified.txt\<CR>")

```

## what have we learned?

- recovering a theory from code and docs alone is hard, but possible.
- most programs are too large for you to understand them all at once. decide on your goal and learn just enough to accomplish it.
- reading source code is surprisingly rewarding.
- match the existing code as closely as you can until you are sure you have a working theory.
hopefully this was helpful! i am told by my friends that i am unusually good at this skill, so i am interested whether this post was effective at teaching it. if you have any questions, or if you just want to get in contact, feel free to reach out via email.


