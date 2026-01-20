# Jupyter Qt Console

## Overview
Lightweight GUI application that provides an enhanced terminal experience for Jupyter kernels. Feels like a terminal but adds GUI-only features like inline figures, multi-line editing with syntax highlighting, and graphical calltips.

## Key Features
- **Inline graphics**: Embed matplotlib plots directly in the console
- **Syntax highlighting**: Full highlighting via pygments, configurable styles
- **Multi-line editing**: Ctrl-Enter for multi-line input, Shift-Enter to force execution
- **Session export**: Save as HTML (PNG figures) or XHTML (SVG figures)
- **Two-process model**: Frontend doesn't block during kernel execution
- **Kernel restart**: Ctrl-. restarts kernel even during blocking execution

## Usage
```bash
# Start console
jupyter qtconsole

# Custom font
jupyter qtconsole --ConsoleWidget.font_family="Anonymous Pro" --ConsoleWidget.font_size=9

# Custom style (monokai, etc.)
jupyter qtconsole --style monokai

# Connect to existing kernel
jupyter qtconsole --existing kernel-12345.json
```

## Multiple Frontends
Multiple consoles can connect to the same kernel - useful for collaboration:
```python
# In running console, get connection info
%connect_info

# Connect another console
jupyter qtconsole --existing kernel-12345.json
```

## Inline Figure Format
```python
# Switch to SVG (required for XHTML export)
%config InlineBackend.figure_format = 'svg'
```

## Security Notes
- By default, kernel listens only on localhost
- Messages signed with HMAC (shared key never sent over network)
- Use SSH tunnels for remote connections:
```bash
jupyter qtconsole --ssh=worker --existing /path/to/kernel-12345.json
```

## Embedding in Qt Apps
Three options:
1. `RichJupyterWidget` - embed console, kernel in separate process
2. Start IPython kernel in PyQt app, connect external console
3. `InProcessKernel` - same process (not well supported)

## Limitations
- Cannot pass input to subprocesses via `!cmd` (pexpect limitation)
- Use terminal IPython for interactive subprocess commands

## Related
- marimo (reactive Python notebooks)
- Jupyter Lab (full IDE experience)
- IPython terminal (pure CLI)

## Links
- Documentation: https://qtconsole.readthedocs.io/
