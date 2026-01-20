---
type: link
source: notion
url: https://blog.glyph.im/2023/08/get-your-mac-python-from-python-dot-org.html
notion_type: Software Repo
tags: ['Running']
created: 2024-04-03T13:47:00.000Z
---

# Deciphering Glyph :: Get Your Mac Python From Python.org

## AI Summary (from Notion)
- Python Installation on macOS: The document discusses various ways to install Python on macOS, with a focus on the recommended method using the official Python.org installer.

- Importance of Choosing the Right Version: It emphasizes the confusion around different installation methods and the need to select one before starting to learn Python.

- Recommendation for Python.org:
- The official build from Python.org is recommended for most users due to its wide compatibility and ongoing updates by the core Python team.
- The builds are universal binaries, making them suitable for a range of macs.

- Security Updates:
- A downside is the lack of auto-update features; users need to manually check for security updates.
- The author suggests using a micro-tool called mopup to manage security updates easily.

- Virtual Environments:
- Users are advised to always use virtual environments to avoid conflicts between libraries and projects.
- The document provides a configuration tip for enforcing virtual environments in pip.

- Other Installation Methods:
- Various other methods are discussed, including Homebrew (not recommended for personal use), pyenv (for managing multiple Python versions), and Conda (often seen as essential for data science).

- Common Misconceptions:
- The document debunks myths about using the built-in Python on macOS and clarifies that it is not suitable for application development.

- Final Recommendations:
- Summarizes key takeaways: use Python.org, manage updates with mopup, use virtual environments, and avoid unnecessary installations like Homebrew for personal projects.

- Acknowledgments: Thanks to patrons and mentions the author's availability for consulting work.

## Content (from Notion)

There are many ways to get Python installed on macOS, but for most people the version that you download from Python.org is best.

pythonprogrammingsupported

One of the most unfortunate things about learning Python is that there are so many different ways to get it installed, and you need to choose one before you even begin. The differences can also be subtle and require technical depth to truly understand, which you don’t have yet.1 Even experts can be missing information about which one to use and why.

There are perhaps more of these on macOS than on any other platform, and that’s the platform I primarily use these days. If you’re using macOS, I’d like to make it simple for you.

## The One You Probably Want: Python.org

My recommendation is to use an official build from python.org.

I recommed the official installer for most uses, and if you were just looking for a choice about which one to use, you can stop reading now. Thanks for your time, and have fun with Python.

If you want to get into the nerdy nuances, read on.

For starters, the official builds are compiled in such a way that they will run on a wide range of macs, both new and old. They are universal2 binaries, unlike some other builds, which means you can distribute them as part of a mac application.

The main advantage that the Python.org build has, though, is very subtle, and not any concrete technical detail. It’s a social, structural issue: the Python.org builds are produced by the people who make CPython, who are more likely to know about the nuances of what options it can be built with, and who are more likely to adopt their own improvements as they are released. Third party builders who are focused on a more niche use-case may not realize that there are build options or environment requirements that could make their Pythons better.

I’m being a bit vague deliberately here, because at any particular moment in time, this may not be an advantage at all. Third party integrators generally catch up to changes, and eventually achieve parity. But for a specific upcoming example, PEP 703 will have extensive build-time implications, and I would trust the python.org team to be keeping pace with all those subtle details immediately as releases happen.

### (And Auto-Update It)

The one downside of the official build is that you have to return to the website to check for security updates. Unlike other options described below, there’s no built-in auto-updater for security patches. If you follow the normal process, you still have to click around in a GUI installer to update it once you’ve clicked around on the website to get the file.

I have written a micro-tool to address this and you can pip install
mopup and then periodically run mopup and it will install any security updates for your current version of Python, with no interaction besides entering your admin password.

### (And Always Use Virtual Environments)

Once you have installed Python from python.org, never pip install anything globally into that Python, even using the --user flag. Always, always use a virtual environment of some kind. In fact, I recommend configuring it so that it is not even possible to do so, by putting this in your ~/.pip/pip.conf:

This will avoid damaging your Python installation by polluting it with libraries that you install and then forget about. Any time you need to do something new, you should make a fresh virtual environment, and then you don’t have to worry about library conflicts between different projects that you may work on.

If you need to install tools written in Python, don’t manage those environments directly, install the tools with pipx. By using pipx, you allow each tool to maintain its own set dependencies, which means you don’t need to worry about whether two tools you use have conflicting version requirements, or whether the tools conflict with your own code.2

# The Others

There are, of course, several other ways to install Python, which you probably don’t want to use.

## The One For Running Other People’s Code, Not Yours: Homebrew

In general, Homebrew Python is not for you.

The purpose of Homebrew’s python is to support applications packaged within Homebrew, which have all been tested against the versions of python libraries also packaged within Homebrew. It may upgrade without warning on just about any brew operation, and you can’t downgrade it without breaking other parts of your install.

Specifically for creating redistributable binaries, Homebrew python is typically compiled only for your specific architecture, and thus will not create binaries that can be used on Intel macs if you have an Apple Silicon machine, or will run slower on Apple Silicon machines if you have an Intel mac. Also, if there are prebuilt wheels which don’t yet exist for Apple Silicon, you cannot easily arch -x86_64 python ... and just install them; you have to install a whole second copy of Homebrew in a different location, which is a headache.

In other words, homebrew is an alternative to pipx, not to Python. For that purpose, it’s fine.

## The One For When You Need 20 Different Pythons For Debugging: pyenv

Like Homebrew, pyenv will default to building a single-architecture binary. Even worse, it will not build a Framework build of Python, which means several things related to being a mac app just won’t work properly. Remember those build-time esoterica that the core team is on top of but third parties may not be? “Should I use a Framework build” is an enduring piece of said esoterica.

The purpose of pyenv is to provide a large matrix of different, precise legacy versions of python for library authors to test compatibility against those older Pythons. If you need to do that, particularly if you work on different projects where you may need to install some random super-old version of Python that you would not normally use to test something on, then pyenv is great. But if you only need one version of Python, it’s not a great way to get it.

## The Other One That’s Exactly Like pyenv: asdf-python

The issues are exactly the same as with pyenv, as the tool is a straightforward alternative for the exact same purpose. It’s a bit less focused on Python than pyenv, which has pros and cons; it has broader community support, but it’s less specifically tuned for Python. But a comparative exploration of their differences is beyond the scope of this post.

## The Built-In One That Isn’t Really Built-In: /usr/bin/python3

There is a binary in /usr/bin/python3 which might seem like an appealing option — it comes from Apple, after all! — but it is provided as a developer tool, for running things like build scripts. It isn’t for building applications with.

That binary is not a “system python”; the thing in the operating system itself is only a shim, which will determine if you have development tools, and shell out to a tool that will download the development tools for you if you don’t. There is unfortunately a lot of folk wisdom among older Python programmers who remember a time when apple did actually package an antedeluvian version of the interpreter that seemed to be supported forever, and might suggest it for things intended to be self-contained or have minimal bundled dependencies, but this is exactly the reason that Apple stopped shipping that.

If you use this option, it means that your Python might come from the Xcode Command Line Tools, or the Xcode application, depending on the state of xcode-select in your current environment and the order in which you installed them.

Upgrading Xcode via the app store or a developer.apple.com manual download — or its command-line tools, which are installed separately, and updated via the “settings” application in a completely different workflow — therefore also upgrades your version of Python without an easy way to downgrade, unless you manage multiple Xcode installs. Which, at 12G per install, is probably not an appealing option.3

## The One With The Data And The Science: Conda

As someone with a limited understanding of data science and scientific computing, I’m not really qualified to go into the detailed pros and cons here, but luckily, Itamar Turner-Trauring is, and he did.

My one coda to his detailed exploration here is that while there are good reasons to want to use Anaconda — particularly if you are managing a data-science workload across multiple platforms and you want a consistent, holistic development experience across a large team supporting heterogenous platforms — some people will tell you that you need Conda to get you your libraries if you want to do data science or numerical work with Python at all, because Conda is how you install those libraries, and otherwise things just won’t work.

This is a historical artifact that is no longer true. Over the last decade, Python Wheels have been comprehensively adopted across the Python community, and almost every popular library with an extension module ships pre-built binaries to multiple platforms. There may be some libraries that only have prebuilt binaries for conda, but they are sufficiently specialized that I don’t know what they are.

## The One for Being Consistent With Your Cloud Hosting

Another way to run Python on macOS is to not run it on macOS, but to get another computer inside your computer that isn’t running macOS, and instead run Python inside that, usually using Docker.4

There are good reasons to want to use a containerized configuration for development, but they start to drift away from the point of this post and into more complicated stuff about how to get your Python into the cloud.

So rather than saying “use Python.org native Python instead of Docker”, I am specifically not covering Docker as a replacement for a native mac Python here because in a lot of cases, it can’t be one. Many tools require native mac facilities like displaying GUIs or scripting applications, or want to be able to take a path name to a file without elaborate pre-work to allow the program to access it.

## Summary

If you didn’t want to read all of that, here’s the summary.

If you use a mac:

1. Get your Python interpreter from python.org.
1. Update it with mopup so you don’t fall behind on security updates.
1. Always use venvs for specific projects, never pip install anything directly.
1. Use pipx to manage your Python applications so you don’t have to worry about dependency conflicts.
1. Don’t worry if Homebrew also installs a python executable, but don’t use it for your own stuff.
1. You might need a different Python interpreter if you have any specialized requirements, but you’ll probably know if you do.
## Acknowledgements

Thank you to my patrons who are supporting my writing on this blog. If you like what you’ve read here and you’d like to read more of it, or you’d like to support my various open-source endeavors, you can support my work as a sponsor! I am also available for consulting work if you think your organization could benefit from expertise on topics like “which Python is the really good one”.

1. 
1. 
1. 
1. 

