---
type: link
source: notion
url: https://rushter.com/blog/zsh-shell/
notion_type: Software Repo
tags: ['Running']
created: 2026-01-10T05:25:00.000Z
---

# You probably don't need Oh My Zsh | Artem Golubin

## Overview (from Notion)
- Oh My Zsh can slow down your terminal workflow, which can be frustrating when managing multiple tasks daily.
- Minimal setups can enhance productivity by reducing distractions, allowing you to focus on your coding and business decisions.
- Customizing prompts and utilizing tools like starship can streamline your work environment, reflecting your personal style while remaining efficient.
- Alternatives like fzf for history search can improve your workflow, providing a more interactive experience compared to traditional plugins.
- Embracing a simpler setup may lead to better performance and quicker startup times, helping you make the most of your limited time for coding and fatherhood.
- Consider the balance between convenience and performance—adding too many features can hinder rather than help.
- This approach resonates with the fast-paced life in NYC, where efficiency is key, and every second counts in both parenting and running a business.

## AI Summary (from Notion)
Oh My Zsh adds unnecessary bloat that slows down shell startup times. A minimal Zsh configuration is recommended, emphasizing essential features without plugins. Customization can be achieved using the starship prompt for simplicity and clarity. For history search, using fzf is preferred over zsh-autosuggestions. Enabling Vim mode can enhance command editing efficiency. Transitioning from Oh My Zsh to a simpler setup can improve performance significantly.

## Content (from Notion)

Oh My Zsh is still getting recommended a lot. The main problem with Oh My Zsh is that it adds a lot of unnecessary bloat that affects shell startup time.

Since OMZ is written in shell scripts, every time you open a new terminal tab, it has to interpret all those scripts. Most likely, you don't need OMZ at all.

Here are the timings from the default setup with a few plugins:

```plain text
➜  ~ /usr/bin/time -f "%e seconds" zsh -i -c exit
0.38 seconds

```

And that's only for prompt and a new shell instance! Creating a new tab takes some time for your terminal too. It feels like a whole second to me.

My workflows involve opening and closing up to hundreds of terminal or tmux tabs a day. I do everything from the terminal. Just imagine that opening a new tab in a text editor would take half a second every time.

Once in a while, it also checks for updates, which can take up to a few seconds when you open a new tab.

I see no reason in frequent updates for my shell configuration. Especially, when a lot of third-party plugins are getting updates too. Why would you want you shell to fetch updates?

My advice is to start simple and only add what you really need.

### Minimal Zsh configuration

Here is the minimal Zsh configuration that works well as a starting point:

```plain text
export HISTSIZE=1000000000
export SAVEHIST=$HISTSIZE
setopt EXTENDED_HISTORY
setopt autocd
autoload -U compinit; compinit

```

It's an already pretty good setup with completions!

Some details about this configuration:

- HISTSIZE and SAVEHIST set the size of your history.
- EXTENDED_HISTORY adds timestamps to your history entries.
- autocd allows you to change directories without typing cd.
- compinit initializes the Zsh completion system.
### Prompt customization

You also want to customize your prompt. For prompts, I'm using starship which is a fast and minimal prompt packed into a single binary.

The very old way of doing this in Oh My Zsh was to use plugins and custom themes. With starship, it's very simple and easy now. It replaces git, virtual environment and language specific plugins.

Here is my config for starship:

```plain text
[aws]
disabled = true

[package]
disabled = true

[gcloud]
disabled = true

[azure]
disabled = true


[nodejs]
disabled = true

[character]
success_symbol = '[➜](bold green)'

[cmd_duration]
min_time = 500
format = 'underwent [$duration](bold yellow)'

[directory]
truncation_length = 255
truncate_to_repo = false
use_logical_path = false

```

Because cloud services are available globally, I've disabled them. I don't want them to be displayed on every prompt, since this adds visual noise.

Here is how my prompt looks like now:

This project uses both Python and Rust, they are highlighted in the prompt. When you run a command, it also shows how long it took to execute.

To enable it, add the following line to your .zshrc:

```plain text
eval "$(starship init zsh)"

```

### History search

A lot of people use zsh-autosuggestions plugin for history search. I find it distracting, because it shows all suggestions as you type.

Instead, I prefer using fzf binded to Ctrl+R for searching history. It gives an interactive fuzzy search.

To enable it, add the following lines to your .zshrc:

### Final startup time

After these changes, the startup should look as follows:

```plain text
❯ /usr/bin/time -f "%e seconds" zsh -i -c exit
0.07 seconds

```

### Miscellaneous tips

For Vim users, I also suggest enabling Vim mode in Zsh. It makes editing commands much faster.

```plain text
set -o vi
# Fix for backspace in vi mode
bindkey -v '^?' backward-delete-char

```

It works the same way as in Vim. By default, zle (the library that reads the shell input) uses Emacs keybindings.

### Conclusion

After switching from OMZ a year ago, it only took me a few days to get used to the new workflow. If you still missing some of the plugins, you can always load them manually.

If you have any questions, feel free to ask them via e-mail displayed in the footer.


