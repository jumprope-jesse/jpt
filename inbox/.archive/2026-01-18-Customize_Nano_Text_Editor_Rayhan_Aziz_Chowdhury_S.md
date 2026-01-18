---
type: link
source: notion
url: https://shafi.ddns.net/blog/customize-nano-text-editor
notion_type: Software Repo
tags: ['Running']
created: 2025-11-05T04:07:00.000Z
---

# Customize Nano Text Editor | Rayhan Aziz Chowdhury Shafi

## Overview (from Notion)
- Enhancing productivity: Customizing Nano can streamline coding tasks, making it easier to manage multiple projects efficiently.
- Work-life balance: Simplified editing tools can free up time, allowing for more moments with family amidst a busy schedule.
- Technology adaptation: As a founder, staying updated with tools like Nano reflects a commitment to improving your coding environment, essential in a fast-paced tech landscape.
- Unique functionality: Features like mouse support and auto-indentation can simplify complex coding tasks, making the experience more enjoyable.
- Community engagement: Sharing these configurations with peers can foster collaboration and support within your network in NYC's tech scene.
- Alternate view: While Nano is powerful, exploring other editors (like VS Code) might offer even richer functionalities for modern development needs.

## AI Summary (from Notion)
Customize the Nano text editor by editing the .nanorc file to enhance user experience. Key configurations include enabling mouse support, setting tab size, replacing tabs with spaces, tracking cursor position in recently closed files, wrapping lines, auto-indentation, displaying line numbers, and adding scrollbars.

## Content (from Notion)

Nano is a great text editor that is available in every linux distros by default. Here's a few configs that would make your experience with nano even better!

To use the features listed below, you need to edit the .nanorc file in your home directory. You can open the terminal and write nano .nanorc to access the configurations file.

## Position Cursor With Mouse Click

Mouse clicks can be used to place the cursor, set the mark (with a double click), and execute shortcuts. Text can still be selected through dragging by holding down the Shift key.

```plain text
set mouse

```

## Set the Tab Size

Set the size (width) of a tab to number columns. The value of number must be greater than 0. The default value is 8.

```plain text
set tabsize 2

```

Replace Tabs With Spaces

```plain text
set tabstospaces

```

## Keep Track of Cursor Location for Recently Closed Files

For the 200 most recent files, log the last position of the cursor, and place it at that position again upon reopening such a file.

```plain text
set positionlog

```

## Wrap Lines

Display over multiple screen rows line that exceed the screen's width. (You can make this soft-wrapping occur at whitespace instead of rudely at the screen's edge, by using atblanks.

```plain text
set softwrap
set atblanks

```

## Auto Indentation

Automatically indent a newly created line to the same number of tabs and/or spaces as the previous line.

```plain text
set autoindent

```

## Display Line Numbers

Display line numbers to the left of the text area.

```plain text
set linenumbers

```

## Display Scrollbars

Display a "scrollbar" on the righthand side of the edit window. It shows the position of the viewport.

```plain text
set indicator

```


