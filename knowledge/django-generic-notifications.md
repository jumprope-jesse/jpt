# Django Generic Notifications

A flexible, multi-channel notification system for Django applications with built-in support for email digests, user preferences, and extensible delivery channels.

**Repo:** https://github.com/loopwerk/django-generic-notifications

## Key Features

- **Multi-channel delivery**: Website, email, and custom channels (SMS, push, etc.)
- **Flexible email frequencies**: Real-time and digest emails (daily, weekly, custom)
- **Notification grouping**: Prevent spam by grouping similar notifications
- **User preferences**: Fine-grained control per notification type and channel
- **Extensible architecture**: Easy to add custom notification types, channels, frequencies
- **Generic relations**: Link notifications to any Django model
- **Full type hints**: Complete type annotations

## Installation

```bash
uv add django-generic-notifications
```

Add to `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    "generic_notifications",
    ...
]
```

Run migrations:
```bash
python manage.py migrate generic_notifications
```

## Quick Start

### Define a notification type

```python
# myapp/notifications.py
from generic_notifications.types import NotificationType, register

@register
class CommentNotification(NotificationType):
    key = "comment"
    name = "Comment Notifications"
    description = "When someone comments on your posts"
```

### Send a notification

```python
from generic_notifications import send_notification
from myapp.notifications import CommentNotification

notification = send_notification(
    recipient=post.author,
    notification_type=CommentNotification,
    actor=comment.user,
    target=post,
    subject=f"{comment.user.get_full_name()} commented on your post",
    text=f"{comment.user.get_full_name()} left a comment: {comment.text[:100]}",
    url=f"/posts/{post.id}#comment-{comment.id}",
)
```

### Send digest emails (cron job)

```bash
# Daily digests at 9 AM
0 9 * * * cd /path/to/project && python manage.py send_digest_emails --frequency daily
```

## Custom Channels

```python
from generic_notifications.channels import NotificationChannel, register

@register
class SMSChannel(NotificationChannel):
    key = "sms"
    name = "SMS"

    def process(self, notification):
        send_sms(
            to=notification.recipient.phone_number,
            message=notification.get_text()
        )
```

## Notification Grouping

Prevent notification spam by updating existing notifications instead of creating new ones:

```python
@register
class CommentNotification(NotificationType):
    key = "comment"
    name = "Comment Notifications"
    description = "When someone comments on your posts"

    @classmethod
    def should_save(cls, notification):
        existing = Notification.objects.filter(
            recipient=notification.recipient,
            notification_type=notification.notification_type,
            actor=notification.actor,
            content_type_id=notification.content_type_id,
            object_id=notification.object_id,
            read__isnull=True,
        ).first()

        if existing:
            count = existing.metadata.get("count", 1)
            existing.metadata["count"] = count + 1
            existing.save()
            return False  # Don't create new notification
        return True

    def get_text(self, notification):
        count = notification.metadata.get("count", 1)
        actor_name = notification.actor.get_full_name()
        if count == 1:
            return f"{actor_name} commented on your post"
        return f"{actor_name} left {count} comments on your post"
```

## Required Channels (for critical notifications)

```python
from generic_notifications.channels import EmailChannel

@register
class SecurityAlert(NotificationType):
    key = "security_alert"
    name = "Security Alerts"
    description = "Important security notifications"
    required_channels = [EmailChannel]  # Cannot be disabled by users
```

## User Preferences

```python
from generic_notifications.preferences import (
    get_notification_preferences,
    save_notification_preferences
)

# Get preferences for UI display
preferences = get_notification_preferences(user)

# Save from form (field format: {type_key}__{channel_key})
save_notification_preferences(user, request.POST)
```

## Querying Notifications

```python
from generic_notifications.lib import get_unread_count, get_notifications, mark_notifications_as_read

unread_count = get_unread_count(user=user, channel=WebsiteChannel)
unread = get_notifications(user=user, channel=WebsiteChannel, unread_only=True)
mark_notifications_as_read(user=user)
```

## Performance Tips

1. **Avoid N+1 queries**: Don't rely on `notification.target` for dynamic text generation - store subject/text/url directly on the notification
2. **Non-blocking emails**: Use django-mailer for queued email sending instead of blocking SMTP calls

## Notes

This is a complete rewrite of an older django-generic-notifications package. The old version predates Django migrations (used South).
