# Claude Code Project Guidelines

## LaunchAgents / launchd Services

When setting up launchd plist files for background services:

### PATH Environment
launchd does NOT inherit shell PATH. Always include an `EnvironmentVariables` section:

```xml
<key>EnvironmentVariables</key>
<dict>
    <key>PATH</key>
    <string>/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Users/jesse/Library/pnpm:/Users/jesse/.local/bin</string>
    <key>HOME</key>
    <string>/Users/jesse</string>
</dict>
```

### Binary Paths
Use full absolute paths for binaries in scripts called by launchd:
- Python: `/opt/homebrew/bin/python3`
- Node tools (claude, happy): `/Users/jesse/Library/pnpm/<tool>`
- ffmpeg: `/Users/jesse/.local/bin/ffmpeg`

### Common Commands
```bash
# Load service
launchctl load ~/Library/LaunchAgents/com.jpt.<service>.plist

# Unload service
launchctl unload ~/Library/LaunchAgents/com.jpt.<service>.plist

# Check status
launchctl list | grep jpt

# View logs (if configured)
tail -f ~/jpt/<service>/.processor.log
```

### Plist Template
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.jpt.SERVICE_NAME</string>
    <key>ProgramArguments</key>
    <array>
        <string>/opt/homebrew/bin/python3</string>
        <string>/Users/jesse/jpt/PATH/TO/script.py</string>
    </array>
    <key>EnvironmentVariables</key>
    <dict>
        <key>PATH</key>
        <string>/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Users/jesse/Library/pnpm:/Users/jesse/.local/bin</string>
        <key>HOME</key>
        <string>/Users/jesse</string>
    </dict>
    <key>StartInterval</key>
    <integer>120</integer>
    <key>RunAtLoad</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/Users/jesse/jpt/PATH/.service.log</string>
    <key>StandardErrorPath</key>
    <string>/Users/jesse/jpt/PATH/.service.log</string>
    <key>WorkingDirectory</key>
    <string>/Users/jesse/jpt</string>
</dict>
</plist>
```

## Claude CLI Usage

When calling Claude from scripts (for Claude Max users):

```python
# Use happy (Claude Code wrapper) with full path
happy_bin = Path.home() / "Library/pnpm/happy"
result = subprocess.run(
    [str(happy_bin), "--yolo", "--print", prompt],
    capture_output=True,
    text=True,
    timeout=180
)
```

- `--yolo` = skip permission prompts (equivalent to `--dangerously-skip-permissions`)
- `--print` = non-interactive mode, output to stdout
- Always use full binary path for launchd compatibility

## Active Services

| Service | Plist | Interval | Purpose |
|---------|-------|----------|---------|
| meeting-processor | `com.jpt.meeting-processor.plist` | 120s | Process Meetily transcripts |
