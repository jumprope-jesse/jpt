---
type: link
source: notion
url: https://burakku.com/blog/rye-test-and-python-tools/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-04-12T02:55:00.000Z
---

# Trying out Rye - ブラック

## AI Summary (from Notion)
- Testing Rye: The author is exploring the Rye tool for Python development, comparing it to Cargo in the Rust ecosystem.
- Initial Impressions: Rye bundles multiple tools, aiming to simplify Python project management by automating installation and environment setup.
- Key Tools Replaced:
- pyenv for managing Python versions
- pip for dependency management
- pipx for isolated tool installations
- Automatic virtual environment creation
- Initial Success: Successfully migrated pipx installs to Rye and structured a simple Python script project.
- Challenges with Django: Encountered issues when trying to integrate uWSGI due to Rye's use of static Python builds, which complicates C extensions.
- Custom Toolchain Issues: Attempted to register a Homebrew-installed Python version but faced complications.
- Static vs Dynamic Builds: Critiques Rye's reliance on static builds, suggesting that dynamic builds would be more suitable for development.
- Environment Variables: Expresses a desire for better integration of environment variables in Rye scripts.
- Mixed Feelings: While the design concepts are promising, the author notes significant rough edges and limitations that may deter experienced developers.
- Recommendation for New Users: Suggests that new Python developers may benefit from Rye's setup, but seasoned developers might find it lacking for now.
- Future Potential: Optimistic that Rye could improve significantly in the coming year, making it a tool to watch.

## Content (from Notion)

Testing out Rye and other Python tooling thoughts

The catch in the Rye.

One of my least popular takes as a Professional Python Developer™ seems to be that I don’t actually consider the Python ecosystem and its tooling to be "hot garbage". I also haven’t really bothered with project management tools like Poetry, since I think you can use virtual environments and pip and be just fine. Really, the only tools in my arsenal that I consider to be absolutely essential have been pipx, as distributing Python tools is kind of a pain, and pyenv, because Homebrew will absolutely break your Python installation without any mercy if you so much as blink. Of course, I do also use other tools too, but I don't consider them as essential as those two.

However, I do recognise that there is some value in one-stop-shop tools like Rust’s Cargo, which bakes in a lot more project management stuff into your Rust development workflow and is generally pretty nice to use. For this reason I was quite intrigued by Rye after watching Armin Ronacher’s demonstration video, since it seems like a version of Cargo (and to some degree Rustup) for the Python world.

On a conceptual level, it sounds very good. Instead of installing a bunch of tools and managing/using them individually, Rye would bundle together all sorts of tools and functionality, and let me write Python software with basically Rye alone. The number of different tools that I use and Rye would replace is actually rather long:

I started off by migrating all of my pipx installs to Rye and it worked great. All tools were ready and usable on my $PATH and I could even add optional dependencies with --extra-requirement flags. Not sure if there’s a handy way of adding those extra requirements after the fact like you can in pipx with pipx inject though. I imagine I could always just manually install them into the virtual environment but I’d prefer if there was a more straightforward and obvious way. Would make it even easier to use Rye as a drop-in replacement for pipx.

As for actual development, I decided to start off small and convert a tiny Python script I use for fetching data from an API to work with Rye. Since this was just a tiny script that I run in a Docker container, it wasn't exactly organized in the way that Rye would organize a script project, so I decided to also make it a bit more structured with a script entry-point and everything. This isn't actually a requirement but I figured that I should try to do it like Rye would want me to. For what it's worth, the default Rye-tastic way of organizing code is fairly logical and probably good starting point for people new to Python. Personally, I've never really used /src/ directories in Python but I don't hate it either.

For this tiny project, everything worked very nicely. Granted, there was only one dependency (requests), so it wasn't exactly a demanding test. But Rye would bootstrap whatever Python version I had in the .python-version text file, create a virtualenv out of it, install my dependencies into it and then allow me to run my script with just python like I didn't have a virtualenv at all.

And if I upgraded or downgraded my Python version by changing the value in the .python-version file, it would bootstrap everything again to make sure my development environment matched the requirements. This would make version upgrades a lot easier for projects with lots of different developers, as you could be pretty confident in everyone having an up-to-date development environment if they just run rye sync. I've had to work on projects that upgraded between major versions of Python, and you'd always have at least some issues bringing everyone up to speed.

Emboldened by the success of using Rye with this tiny script, I moved onto the next trial: using Rye to develop a Django project. And this is where the pain begins, and not (just) because I picked an example with an ancient Django 2.0 codebase.

I bootstrapped my Django project as a virtual package with Rye and managed to install all of the dependencies for my Django project that are required to run the application locally. Then I started to add the dependencies I need to actually serve it on the web and I step on the big fat LEGO brick lying in wait: I just can't install uWSGI. The reason for this is actually quite simple: uWSGI needs to compile C extensions, Rye uses static builds of Python, and static Python builds + compiling C extensions is a known house of pain.

The Rye FAQ even admits how the situation when it comes to C extensions is a problem, and one with no real solution at the moment. It does however offer a workaround: register a non-static Python build that you've obtained from somewhere as a Rye toolchain. Since Homebrew has decided to grace my Mac Studio with a Python 3.9 installation suitable for my purposes*, I decided to register that.

- Technically Django 2.0 doesn't actually support Python 3.9 but fortune favours the bold.
```plain text
$ which python3.9
/opt/homebrew/bin/python3.9
$ rye toolchain register --name=homebrew /opt/homebrew/bin/python3.9
Registered /opt/homebrew/bin/python3.9 as homebrew@3.9.18

```

Obviously I would never recommend actually using Homebrew-supplied Python installations for any kind of development work, but I figured it'd be fine for testing. Now I can just pin my custom toolchain to my project and create the virtualenv from that.

```plain text
$ rye pin homebrew@3.9.18
pinned homebrew@3.9.18 in project/.python-version
$ rye sync
Python version mismatch (found cpython@3.9.18, expected homebrew@3.9.18), recreating.
error: failed fetching toolchain ahead of sync

Caused by:
    unknown version homebrew-aarch64-macos@3.9.18

```

Oops.

Turns out that Rye is so set on managing your (static) Python toolchains that it will even attempt to download a toolchain already on your machine, and then fail because your custom toolchain doesn't actually exist beyond your machine. It won't even work even if you omit the custom name from rye toolchain register.

So yeah, Rye kinda sucks and is all sorts of broken if you ever need dependencies that compile C code. Obviously I didn't test out a wide array of C extensions, but considering that it's a very well-known problem with static builds, you'll probably trip up yourself sooner or later if you do a lot of Python development.

On one hand, I do understand that compiling software sucks because you need to hoard compile-time requirements and compiling software takes forever and makes your laptop burn your thighs and so on. However, I do think that compiling software like your Python development environment has some very significant upsides, such as the fact that your build of Python will reference paths actually present on your actual computer. Static Python builds are fine for some stuff but I feel like they're a bad idea to be the default and a truly awful idea to be the only option. The support for static compilation of Python just isn't there yet.

Even if the custom toolchain registering worked like it's supposed to, I find this design approach to completely water down the "one-stop-shop for all Python users" idea put forth by Rye, since I'm still required to install pyenv on my machine in order to have a toolchain to register in the first place. I think Rye would be a much better tool if it offered pyenv-style compilation of Python, and preferably made that the default option. Or at the very least ask me which style I prefer during the installation process. It already asks you how you want the python command work outside Rye-managed projects, so it's not unthinkable to have an option for compilation too.

In terms of ergonomics when it came to the Django project (the parts that worked), I also kinda miss the environment variable plugin that VirtualFish had, where it would set environment variables when you activated a virtualenv. As far as I can see, the way you're supposed to integrate environment variables as part of your Python development is by adding them to your Rye scripts. So if I want to set DJANGO_SETTINGS_MODULE for when I run any of the Django management commands, I'd chuck it in a separate file like .env and add this to my pyproject.toml file:

```plain text
[tool.rye.scripts]
manage = { call = "manage", env-file = ".env" }

```

You could also add environment variables directly to the script definition but that sounds very not-portable if you work with other developers. But now I can run tests against my development settings module. I just need to use rye run manage to invoke the test management command instead of for example the manage.py script that Django will give you.

```plain text
$ rye run manage test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..................
---------------------------------------------------------------------
Ran 18 tests in 0.215s

OK
Destroying test database for alias 'default'...

```

I think this is totally reasonable and maybe juggling shell session environment variables isn't the job of a Python development tool anyway, but I do still kinda wish for there to be some kind of a better way for it.

All in all, I have mixed feelings about Rye. On one hand, many of the design ideas are good and I think I'd like to use a Cargo-but-for-Python to develop software, since I also like using Cargo. However, the insistence on using static Python builds leads to suffering and won't let me uninstall pyenv anyways. There's also some rough edges in implementation to cut yourself up further, like my attempt at getting Rye and Homebrew-Python to mingle shows. The fact that rye test is also just an alias to run pytest with no possibility for any other testing tool like the built-in unittest module, which is totally and absolutely a fine tool for testing that you get out of the box, seems very indicative of just how early in Rye's life we are at the moment.

If you have a working Python development environment, no matter how rudimentary its feature set might be, it might not be worth it to try out Rye now. Its best value at the moment would probably rather be for newbs, who can benefit from its easy setup and sane defaults for many things (like not using the system Python if you've got one). However, I think that there's also a good chance that Rye will actually be all-around great in like 12 months, so I also wouldn't invest too heavily in an alternative tool like Poetry if you're shopping around for project management tools.

Nevertheless, Python is still a fun programming language and the tooling is fine.


