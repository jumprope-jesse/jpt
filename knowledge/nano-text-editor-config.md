# Nano Text Editor Configuration

Reference for customizing the Nano text editor via `~/.nanorc`.

## Basic Setup

Edit the config file:
```bash
nano ~/.nanorc
```

## Recommended Settings

```bash
# Mouse support - click to place cursor, double-click to set mark
set mouse

# Tab size (default is 8)
set tabsize 2

# Replace tabs with spaces
set tabstospaces

# Remember cursor position for 200 most recent files
set positionlog

# Soft wrap long lines at whitespace
set softwrap
set atblanks

# Auto-indent new lines to match previous line
set autoindent

# Display line numbers
set linenumbers

# Display scrollbar indicator on right side
set indicator
```

## Source
- https://shafi.ddns.net/blog/customize-nano-text-editor
