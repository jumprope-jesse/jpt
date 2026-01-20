---
type: link
source: notion
url: https://utcc.utoronto.ca/~cks/space/blog/python/PyPyQuietlyWorking
notion_type: Software Repo
tags: ['Running']
created: 2024-05-30T11:51:00.000Z
---

# Chris's Wiki :: blog/python/PyPyQuietlyWorking

## Overview (from Notion)
- Embracing tools like PyPy can enhance your efficiency as a software engineer, allowing you to focus on building solutions rather than troubleshooting dependencies.
- The seamless integration of PyPy with pipx highlights the importance of using modern workflows that simplify development and deployment, which can be especially valuable for a founder managing multiple projects.
- The experience of running a complex Python package without realizing it was on PyPy speaks to the maturity of the ecosystem—technology should just work, enhancing productivity without headaches.
- As a father, you might appreciate the time saved by using effective tools, allowing you to balance work with family life more effectively.
- Consider alternative views on dependency management; while PyPy offers speed and compatibility, traditional methods may have their merits in certain legacy systems or specific projects.
- Engaging with the Python community and keeping up with trends can provide insights into best practices and innovations that may benefit your projects.

## AI Summary (from Notion)
After switching to pipx for installing Python programs, all installations on the server have been running under PyPy instead of CPython without issues. This transition has proven successful, as significant packages are likely tested under PyPy, allowing for seamless operation of various tools, including a cloud provider's CLI tool.

## Content (from Notion)

A number of years ago I switched to installing various Python programs through pipx so that each of them got their own automatically managed virtual environment, rather than me having to wrestle with various issues from alternate approaches. On our Ubuntu servers, it wound up being simpler to do this using my own version of PyPy instead of Ubuntu's CPython, for various reasons. I've been operating this way for long enough that I didn't really remember how long.

Recently we got our first cloud server, and I wound up installing our cloud provider's basic CLI tool. This CLI tool has a number of official ways of installing it, but when the dust settles I discovered it was a Python package (with a bunch of additional complicated dependencies) and this package is available on PyPi. So I decided to see if 'pipx install <x>' would work, which it did. Only much later did it occur to me that this very large Python and stuff tool was running happily under PyPy, because this is the default if I just 'pipx install' something.

As it turns out, everything I have installed through pipx on our servers is currently installed using PyPy instead of CPython, and all of it works fine. I've been running all sorts of code with PyPy for years without noticing anything different. There is definitely code that will notice (I used to have some), but either I haven't encountered any of it yet or significant packages are now routinely tested under PyPy and hardened against things like deferred garbage collection of open files.

(Some current Python idioms, such as the 'with' statement, avoid this sort of problem, because they explicitly close files and otherwise release resources as you're done with them.)

In a way there's nothing remarkable about this. PyPy's goal is to be a replacement for CPython that simply works while generally being faster. In another way, it's nice to see that PyPy has been basically completely successful in this for me, to the extent that I can forget that my pipx-installed things are all running under PyPy and that a big cloud vendor thing just worked.

Written on 29 May 2024.


