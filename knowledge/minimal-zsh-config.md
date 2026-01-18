# Minimal Zsh Configuration

A guide to replacing Oh My Zsh with a lightweight, fast setup.

*Source: https://rushter.com/blog/zsh-shell/ - Added: 2026-01-18*

## Why Ditch Oh My Zsh?

- **Startup time**: OMZ adds ~0.38s overhead per shell instance
- **Plugin bloat**: Shell scripts are interpreted on every terminal open
- **Unwanted updates**: OMZ checks for updates periodically, adding delays
- For workflows with hundreds of terminal tabs daily, this adds up significantly

## Minimal .zshrc

```bash
export HISTSIZE=1000000000
export SAVEHIST=$HISTSIZE
setopt EXTENDED_HISTORY
setopt autocd
autoload -U compinit; compinit
```

What this does:
- `HISTSIZE` / `SAVEHIST`: Large command history
- `EXTENDED_HISTORY`: Timestamps in history entries
- `autocd`: Change directories without typing `cd`
- `compinit`: Enables tab completion

## Prompt: Use Starship

[Starship](https://starship.rs) is a fast, cross-shell prompt in a single Rust binary. Replaces git, virtualenv, and language-specific OMZ plugins.

```bash
# Add to .zshrc
eval "$(starship init zsh)"
```

Example starship.toml (disable cloud noise):
```toml
[aws]
disabled = true

[gcloud]
disabled = true

[azure]
disabled = true

[package]
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
```

## History Search: Use fzf

Instead of zsh-autosuggestions (shows suggestions as you type, distracting), use fzf bound to Ctrl+R for interactive fuzzy history search.

## Vim Mode

```bash
set -o vi
# Fix backspace in vi mode
bindkey -v '^?' backward-delete-char
```

## Results

Startup time: ~0.07s (down from ~0.38s with OMZ)

## Transition Tips

- The author adapted in a few days
- You can still manually load specific plugins if needed
- Start simple, add only what you actually use
