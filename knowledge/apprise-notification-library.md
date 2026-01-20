# Apprise - Universal Notification Library

**Repo:** https://github.com/caronc/apprise
**Type:** Python library + CLI tool
**Added:** 2026-01-19

## What It Does

Unified notification library that sends to 90+ services via a single API. One library to replace all individual notification integrations.

> *"ap·prise (verb): To inform or tell someone. To make one aware of something."*

## Key Features

- **Single unified syntax** for 90+ notification services
- **Asynchronous messaging** for fast response times
- **Attachment support** (images, files) for compatible services
- **CLI tool** + Python API
- **Configuration files** (YAML/TEXT) for credential management
- **Custom plugin system** with decorator-based hooks

## Supported Services

### Productivity
- Slack, Discord, Microsoft Teams
- Notion, Jira, GitHub Issues
- Trello, Asana

### SMS
- Twilio, AWS SNS, Vonage
- Clickatell, MessageBird

### Email
- Gmail, Yahoo, Outlook/Hotmail
- FastMail, ProtonMail
- Generic SMTP/IMAP

### Push
- Pushbullet, Pushover, Gotify
- ntfy, FCM, APNS

### Desktop
- Linux (D-Bus), macOS, Windows
- System tray notifications

### Other
- IFTTT, Zapier webhooks
- AWS SES, Amazon SNS
- Telegram, WhatsApp

[Full list](https://github.com/caronc/apprise#supported-notifications)

## Installation

```bash
# Via pip
pip install apprise

# RHEL/CentOS/Rocky (EPEL)
dnf install apprise
```

## CLI Usage

```bash
# Send to multiple services at once
apprise -vv -t 'Server Alert' -b 'Disk usage at 90%' \
  'mailto://user:pass@gmail.com' \
  'discord:///webhook-id/token' \
  'slack://token-a/token-b/token-c'

# Pipe output from commands
uptime | apprise -t 'System Status' 'pbul://pushbullet-token'

# With attachments
apprise --title 'Security Alert' \
  --body 'Motion detected' \
  --attach http://camera/snapshot.jpg \
  'mailto://admin@example.com'
```

### Configuration Files

Store credentials securely instead of command line:

```yaml
# ~/.apprise.yml
urls:
  - mailto://user:pass@gmail.com
  - discord:///webhook-id/token
  - slack://token-a/token-b/token-c:
    - tag: admin
```

Then simply:
```bash
apprise -t 'Title' -b 'Body'  # Uses default config
apprise -t 'Admin Alert' -b 'Message' --tag admin
```

**Default config paths:**
- `~/.apprise` or `~/.apprise.yml`
- `~/.config/apprise` or `~/.config/apprise.yml`
- `/etc/apprise` or `/etc/apprise.yml`

Can also load from HTTP:
```bash
apprise --config https://myserver/apprise/config.yml
```

## Python API

```python
import apprise

# Create instance
apobj = apprise.Apprise()

# Add services
apobj.add('mailto://user:pass@gmail.com')
apobj.add('pbul://pushbullet-token')
apobj.add('slack://token-a/token-b/token-c', tag='admin')

# Notify all services
apobj.notify(
    title='Deployment Complete',
    body='Version 2.3.1 deployed successfully'
)

# Notify specific tags
apobj.notify(
    title='Critical Error',
    body='Database connection failed',
    tag='admin'
)

# With attachments
apobj.notify(
    title='Daily Report',
    body='See attached CSV',
    attach='/path/to/report.csv'
)
```

### With Configuration Files

```python
import apprise

apobj = apprise.Apprise()
config = apprise.AppriseConfig()

# Load from file
config.add('/path/to/config.yml')
config.add('https://server/config')

# Add config to apprise
apobj.add(config)

# Mix with direct entries
apobj.add('mailto://user:pass@gmail.com', tag='fallback')

apobj.notify(title='Alert', body='Message')
```

## Custom Plugins

Create your own notification hooks:

```python
from apprise.decorators import notify

@notify(on="foobar", name="My Custom Plugin")
def my_custom_notification(body, title, notify_type, *args, **kwargs):
    """Triggers on foobar:// URLs"""
    print(f"{notify_type}: {title} - {body}")
    # Your custom logic here
    return True  # Success
```

**Plugin paths:**
- `~/.apprise/plugins`
- `~/.config/apprise/plugins`
- `/var/lib/apprise/plugins`

Load custom plugins:
```bash
apprise --plugin-path /path/to/plugin.py foobar://
```

Or in Python:
```python
from apprise import Apprise, AppriseAsset

asset = AppriseAsset(plugin_paths="/path/to/plugins")
apobj = Apprise(asset=asset)
apobj.add('foobar://')
```

## Use Cases

### System Monitoring
```bash
# Cron job completion
0 2 * * * /backup.sh && apprise -t 'Backup OK' -b "$(date)" \
  || apprise -t 'Backup FAILED' -b "Check logs"
```

### CI/CD Pipelines
```python
# GitHub Actions, Jenkins, etc.
import apprise
apobj = apprise.Apprise()
apobj.add('slack://token')

if build_successful:
    apobj.notify(title='Build #123 Passed', body='Ready to deploy')
else:
    apobj.notify(title='Build #123 Failed', body='See logs')
```

### Home Automation
```python
# Motion detected on security camera
apobj.notify(
    title='Motion Detected - Front Door',
    body='Check camera feed',
    attach='http://camera/snapshot.jpg'
)
```

### Application Alerts
```python
# Django/Flask error handler
import apprise

def notify_error(error_msg, traceback):
    apobj = apprise.Apprise()
    apobj.add('discord://webhook', tag='errors')
    apobj.notify(
        title='Application Error',
        body=f"{error_msg}\n\n{traceback[:500]}"
    )
```

## Comparison to Alternatives

### vs. ntfy
- **ntfy**: Simple pub/sub, one service, perfect for personal use
- **Apprise**: Multi-service aggregator, enterprise-ready, plugin ecosystem

### vs. Individual SDKs
- Replace 90+ individual libraries with one unified interface
- Consistent API across all services
- Easy to add/remove/swap notification backends without code changes

### vs. Zapier/IFTTT
- **Zapier/IFTTT**: No-code webhooks, cloud-based
- **Apprise**: Code/CLI-based, self-hosted, no external dependencies

## Integration Ideas for JPT

1. **Meeting Processor**: Send daily digest summaries to Slack/Discord
2. **Notion Agent**: Alert when AI tasks complete (success/failure)
3. **Knowledge Curator**: Notify when PR opened for review
4. **Inbox Processor**: Alert on high-priority items that need attention
5. **System Monitoring**: launchd service failures, disk space warnings

## Notes

- **Lightweight**: Fast async messaging, minimal overhead
- **No vendor lock-in**: Swap notification backends via config changes
- **Extensible**: Custom plugins for internal services
- **Battle-tested**: Mature project, widely used
- **Graphical UI**: Separate [Apprise API](https://github.com/caronc/apprise-api) project for web management

## Related

- [django-generic-notifications.md](django-generic-notifications.md) - Django-specific in-app notification system
- [self-hosting-guide.md](self-hosting-guide.md) - Contains ntfy setup for simple push notifications
