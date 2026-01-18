# Ratatui TUI Tools

Terminal user interface (TUI) applications built with Ratatui (Rust library). These tools provide productivity and utility features accessible from the command line.

*Source: https://ratatui.rs/showcase/apps/ - Added: 2026-01-18*

## Productivity & Data Tools

### csvlens
CSV file viewer for the terminal. Like `less` but designed for CSV files.

### dua
Disk space analysis tool designed for speed. Uses parallel processing for fast disk usage analysis and allows faster deletion of unnecessary data compared to standard `rm`.

### Television
Fast and versatile fuzzy finder TUI. Search through any data source (files, git repositories, environment variables, docker images) using fuzzy matching. Designed to be easily extensible.

## Git & Development

### Git TUI
TUI for git written in Rust.

### gpg-tui
Terminal User Interface for GnuPG key management.

## AI & Communication

### Oatmeal
Terminal UI chat application for LLMs with slash commands and chat bubbles. Supports multiple backends (ChatGPT, Ollama). Works standalone or paired with Neovim.

## DevOps & Infrastructure

### Docker TUI
Simple TUI to view and control Docker containers.

### Database TUI
Lightweight terminal-based tool for interacting with databases.

### Yozefu (Kafka Explorer)
Interactive TUI for exploring Kafka cluster data. Alternative to AKHQ, Redpanda Console, or JetBrains Kafka plugin. Includes SQL-inspired query language for fine-grained filtering.

## Network & Diagnostics

### Trippy
Network diagnostic tool combining traceroute and ping functionality. Designed to assist with networking issue analysis.

### oha
Load testing tool that sends traffic to web applications with realtime TUI display.

### Bandwhich
CLI utility for displaying current network utilization by process, connection, and remote IP/hostname.

## File Management

### Joshuto
Ranger-like terminal file manager written in Rust.

### yazi
Blazing fast terminal file manager based on async I/O.

### xplr
Hackable, minimal, fast TUI file explorer.

## Shell & History

### Atuin
Replaces shell history with a SQLite database and records additional context for commands.

## Utilities

### fzf-make
Execute make targets using fuzzy finder with preview window.

### rainfrog
Database management TUI (Postgres-focused).

### Slumber
Terminal HTTP/REST client.

### Posting
API client for the terminal.

### taskwarrior-tui
Terminal user interface for taskwarrior.

### openapi-tui
View OpenAPI documentation in your terminal.

## Misc

### binwalk-rs
Binary analysis in the terminal.

### bottom
Customizable cross-platform graphical process/system monitor for the terminal.

### Crossterm Crossword
Play crossword puzzles in the terminal.

### Minesweeper
Mine sweeping game written in Rust.

### Material Colors
Material design color palette for the terminal.

### Oscilloscope
Oscilloscope/vectorscope/spectroscope for the terminal.

### Notes TUI
Markdown note manager with HTML compilation.

---

## Why Ratatui TUIs?

- Rust-based: Fast, memory-safe, cross-platform
- Consistent aesthetics across tools
- Minimalist approach - do one thing well
- Keyboard-driven workflows
- Good for remote/SSH work (no GUI required)
