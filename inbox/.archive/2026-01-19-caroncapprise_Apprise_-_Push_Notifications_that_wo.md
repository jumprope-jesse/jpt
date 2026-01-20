---
type: link
source: notion
url: https://github.com/caronc/apprise
notion_type: Software Repo
tags: ['Running']
created: 2024-02-01T22:27:00.000Z
---

# caronc/apprise: Apprise - Push Notifications that work with just about every platform!

## AI Summary (from Notion)
- Project Overview: Apprise is a versatile library for sending push notifications across various platforms like Telegram, Discord, and Slack.
- Key Features:
- Single library for multiple notification services.
- Lightweight with fast response times due to asynchronous message handling.
- Supports images and attachments for compatible services.
- Target Audience:
- Developers looking for a unified solution for notification services.
- System administrators seeking a reliable notification tool via CLI.
- Installation:
- Installable via pip or through package managers like yum and dnf for Linux distributions.
- Command Line Interface (CLI):
- Allows sending notifications directly from the command line.
- Supports configuration files for secure credential management.
- Developer API:
- Easy integration into Python applications for sending notifications.
- Supports configuration files for API usage, allowing for flexible notification management.
- Custom Notifications:
- Users can create their own notification hooks by wrapping functions with a decorator.
- Supported Notification Services:
- Extensive list of supported services for notifications including AWS SES, IFTTT, and more.
- Interesting Fact:
- The library simplifies the complexity of managing multiple notification services into a single interface.
- Conclusion: Apprise streamlines the process of sending notifications, making it easier for developers and system administrators to manage communication across platforms.

## Content (from Notion)

ap·prise / verb

To inform or tell (someone). To make one aware of something.

Apprise allows you to send a notification to almost all of the most popular notification services available to us today such as: Telegram, Discord, Slack, Amazon SNS, Gotify, etc.

- One notification library to rule them all.
- A common and intuitive notification syntax.
- Supports the handling of images and attachments (to the notification services that will accept them).
- It's incredibly lightweight.
- Amazing response times because all messages sent asynchronously.
Developers who wish to provide a notification service no longer need to research each and every one out there. They no longer need to try to adapt to the new ones that comeout thereafter. They just need to include this one library and then they can immediately gain access to almost all of the notifications services available to us today.

System Administrators and DevOps who wish to send a notification now no longer need to find the right tool for the job. Everything is already wrapped and supported within the apprise command line tool (CLI) that ships with this product.

# Table of Contents

- Supported Notifications 
- Installation
- Command Line Usage 
- Developer API Usage 
- More Supported Links and Documentation
# Supported Notifications

The section identifies all of the services supported by this library. Check out the wiki for more information on the supported modules here.

## Productivity Based Notifications

The table below identifies the services this tool supports and some example service urls you need to use in order to take advantage of it. Click on any of the services listed below to get more details on how you can configure Apprise to access them.

## SMS Notifications

## Desktop Notifications

## Email Notifications

Apprise have some email services built right into it (such as yahoo, fastmail, hotmail, gmail, etc) that greatly simplify the mailto:// service. See more details here.

## Custom Notifications

# Installation

The easiest way is to install this package is from pypi:

```plain text
pip install apprise
```

Apprise is also packaged as an RPM and available through EPEL supporting CentOS, Redhat, Rocky, Oracle Linux, etc.

```plain text
# Follow instructions on https://docs.fedoraproject.org/en-US/epel
# to get your system connected up to EPEL and then:
# Redhat/CentOS 7.x users
yum install apprise

# Redhat/CentOS 8.x+ and/or Fedora Users
dnf install apprise
```

You can also check out the Graphical version of Apprise to centralize your configuration and notifications through a managable webpage.

# Command Line Usage

A small command line interface (CLI) tool is also provided with this package called apprise. If you know the server urls you wish to notify, you can simply provide them all on the command line and send your notifications that way:

```plain text
# Send a notification to as many servers as you want
# as you can easily chain one after another (the -vv provides some
# additional verbosity to help let you know what is going on):
apprise -vv -t 'my title' -b 'my notification body' \
   'mailto://myemail:mypass@gmail.com' \
   'pbul://o.gn5kj6nfhv736I7jC3cj3QLRiyhgl98b'

# If you don't specify a --body (-b) then stdin is used allowing
# you to use the tool as part of your every day administration:
cat /proc/cpuinfo | apprise -vv -t 'cpu info' \
   'mailto://myemail:mypass@gmail.com'

# The title field is totally optional
uptime | apprise -vv \
   'discord:///4174216298/JHMHI8qBe7bk2ZwO5U711o3dV_js'
```

## CLI Configuration Files

No one wants to put their credentials out for everyone to see on the command line. No problem apprise also supports configuration files. It can handle both a specific YAML format or a very simple TEXT format. You can also pull these configuration files via an HTTP query too! You can read more about the expected structure of the configuration files here.

```plain text
# By default if no url or configuration is specified apprise will attempt to load
# configuration files (if present) from:
#  ~/.apprise
#  ~/.apprise.yml
#  ~/.config/apprise
#  ~/.config/apprise.yml
#  /etc/apprise
#  /etc/apprise.yml

# Also a subdirectory handling allows you to leverage plugins
#  ~/.apprise/apprise
#  ~/.apprise/apprise.yml
#  ~/.config/apprise/apprise
#  ~/.config/apprise/apprise.yml
#  /etc/apprise/apprise
#  /etc/apprise/apprise.yml

# Windows users can store their default configuration files here:
#  %APPDATA%/Apprise/apprise
#  %APPDATA%/Apprise/apprise.yml
#  %LOCALAPPDATA%/Apprise/apprise
#  %LOCALAPPDATA%/Apprise/apprise.yml
#  %ALLUSERSPROFILE%\Apprise\apprise
#  %ALLUSERSPROFILE%\Apprise\apprise.yml
#  %PROGRAMFILES%\Apprise\apprise
#  %PROGRAMFILES%\Apprise\apprise.yml
#  %COMMONPROGRAMFILES%\Apprise\apprise
#  %COMMONPROGRAMFILES%\Apprise\apprise.yml

# If you loaded one of those files, your command line gets really easy:
apprise -vv -t 'my title' -b 'my notification body'

# If you want to deviate from the default paths or specify more than one,
# just specify them using the --config switch:
apprise -vv -t 'my title' -b 'my notification body' \
   --config=/path/to/my/config.yml

# Got lots of configuration locations? No problem, you can specify them all:
# Apprise can even fetch the configuration from over a network!
apprise -vv -t 'my title' -b 'my notification body' \
   --config=/path/to/my/config.yml \
   --config=https://localhost/my/apprise/config
```

## CLI File Attachments

Apprise also supports file attachments too! Specify as many attachments to a notification as you want.

```plain text
# Send a funny image you found on the internet to a colleague:
apprise -vv --title 'Agile Joke' \
        --body 'Did you see this one yet?' \
        --attach https://i.redd.it/my2t4d2fx0u31.jpg \
        'mailto://myemail:mypass@gmail.com'

# Easily send an update from a critical server to your dev team
apprise -vv --title 'system crash' \
        --body 'I do not think Jim fixed the bug; see attached...' \
        --attach /var/log/myprogram.log \
        --attach /var/debug/core.2345 \
        --tag devteam
```

## CLI Loading Custom Notifications/Hooks

To create your own custom schema:// hook so that you can trigger your own custom code, simply include the @notify decorator to wrap your function.

```plain text
from apprise.decorators import notify
#
# The below assumes you want to catch foobar:// calls:
#
@notify(on="foobar", name="My Custom Foobar Plugin")
def my_custom_notification_wrapper(body, title, notify_type, *args, **kwargs):
    """My custom notification function that triggers on all foobar:// calls
    """
    # Write all of your code here... as an example...
    print("{}: {} - {}".format(notify_type.upper(), title, body))

    # Returning True/False is a way to relay your status back to Apprise.
    # Returning nothing (None by default) is always interpreted as a Success
```

Once you've defined your custom hook, you just need to tell Apprise where it is at runtime.

```plain text
# By default if no plugin path is specified apprise will attempt to load
# all plugin files (if present) from the following directory paths:
#  ~/.apprise/plugins
#  ~/.config/apprise/plugins
#  /var/lib/apprise/plugins

# Windows users can store their default plugin files in these directories:
#  %APPDATA%/Apprise/plugins
#  %LOCALAPPDATA%/Apprise/plugins
#  %ALLUSERSPROFILE%\Apprise\plugins
#  %PROGRAMFILES%\Apprise\plugins
#  %COMMONPROGRAMFILES%\Apprise\plugins

# If you placed your plugin file within one of the directories already defined
# above, then your call simply needs to look like:
apprise -vv --title 'custom override' \
        --body 'the body of my message' \
        foobar:\\

# However you can over-ride the path like so
apprise -vv --title 'custom override' \
        --body 'the body of my message' \
        --plugin-path /path/to/my/plugin.py \
        foobar:\\
```

You can read more about creating your own custom notifications and/or hooks here.

# Developer API Usage

To send a notification from within your python application, just do the following:

```plain text
import apprise

# Create an Apprise instance
apobj = apprise.Apprise()

# Add all of the notification services by their server url.
# A sample email notification:
apobj.add('mailto://myuserid:mypass@gmail.com')

# A sample pushbullet notification
apobj.add('pbul://o.gn5kj6nfhv736I7jC3cj3QLRiyhgl98b')

# Then notify these services any time you desire. The below would
# notify all of the services loaded into our Apprise object.
apobj.notify(
    body='what a great notification service!',
    title='my notification title',
)
```

## API Configuration Files

Developers need access to configuration files too. The good news is their use just involves declaring another object (called AppriseConfig) that the Apprise object can ingest. You can also freely mix and match config and notification entries as often as you wish! You can read more about the expected structure of the configuration files here.

```plain text
import apprise

# Create an Apprise instance
apobj = apprise.Apprise()

# Create an Config instance
config = apprise.AppriseConfig()

# Add a configuration source:
config.add('/path/to/my/config.yml')

# Add another...
config.add('https://myserver:8080/path/to/config')

# Make sure to add our config into our apprise object
apobj.add(config)

# You can mix and match; add an entry directly if you want too
# In this entry we associate the 'admin' tag with our notification
apobj.add('mailto://myuser:mypass@hotmail.com', tag='admin')

# Then notify these services any time you desire. The below would
# notify all of the services that have not been bound to any specific
# tag.
apobj.notify(
    body='what a great notification service!',
    title='my notification title',
)

# Tagging allows you to specifically target only specific notification
# services you've loaded:
apobj.notify(
    body='send a notification to our admin group',
    title='Attention Admins',
    # notify any services tagged with the 'admin' tag
    tag='admin',
)

# If you want to notify absolutely everything (regardless of whether
# it's been tagged or not), just use the reserved tag of 'all':
apobj.notify(
    body='send a notification to our admin group',
    title='Attention Admins',
    # notify absolutely everything loaded, regardless on wether
    # it has a tag associated with it or not:
    tag='all',
)
```

## API File Attachments

Attachments are very easy to send using the Apprise API:

```plain text
import apprise

# Create an Apprise instance
apobj = apprise.Apprise()

# Add at least one service you want to notify
apobj.add('mailto://myuser:mypass@hotmail.com')

# Then send your attachment.
apobj.notify(
    title='A great photo of our family',
    body='The flash caused Jane to close her eyes! hah! :)',
    attach='/local/path/to/my/DSC_003.jpg',
)

# Send a web based attachment too! In the below example, we connect to a home
# security camera and send a live image to an email. By default remote web
# content is cached, but for a security camera we might want to call notify
# again later in our code, so we want our last image retrieved to expire(in
# this case after 3 seconds).
apobj.notify(
    title='Latest security image',
    attach='http://admin:password@hikvision-cam01/ISAPI/Streaming/channels/101/picture?cache=3'
)
```

To send more than one attachment, just use a list, set, or tuple instead:

```plain text
import apprise

# Create an Apprise instance
apobj = apprise.Apprise()

# Add at least one service you want to notify
apobj.add('mailto://myuser:mypass@hotmail.com')

# Now add all of the entries we're interested in:
attach = (
    # ?name= allows us to rename the actual jpeg as found on the site
    # to be another name when sent to our receipient(s)
    'https://i.redd.it/my2t4d2fx0u31.jpg?name=FlyingToMars.jpg',

    # Now add another:
    '/path/to/funny/joke.gif',
)

# Send your multiple attachments with a single notify call:
apobj.notify(
    title='Some good jokes.',
    body='Hey guys, check out these!',
    attach=attach,
)
```

## API Loading Custom Notifications/Hooks

By default, no custom plugins are loaded at all for those building from within the Apprise API. It's at the developers discretion to load custom modules. But should you choose to do so, it's as easy as including the path reference in the AppriseAsset() object prior to the initialization of your Apprise() instance.

For example:

```plain text
from apprise import Apprise
from apprise import AppriseAsset

# Prepare your Asset object so that you can enable the custom plugins to
# be loaded for your instance of Apprise...
asset = AppriseAsset(plugin_paths="/path/to/scan")

# OR You can also generate scan more then one file too:
asset = AppriseAsset(
    plugin_paths=[
        # Iterate over all python libraries found in the root of the
        # specified path. This is NOT a recursive (directory) scan; only
        # the first level is parsed. HOWEVER, if a directory containing
        # an __init__.py is found, it will be included in the load.
        "/dir/containing/many/python/libraries",

        # An absolute path to a plugin.py to exclusively load
        "/path/to/plugin.py",

        # if you point to a directory that has an __init__.py file found in
        # it, then only that file is loaded (it's similar to point to a
        # absolute .py file. Hence, there is no (level 1) scanning at all
        # within the directory specified.
        "/path/to/dir/library"
    ]
)

# Now that we've got our asset, we just work with our Apprise object as we
# normally do
aobj = Apprise(asset=asset)

# If our new custom `foobar://` library was loaded (presuming we prepared
# one like in the examples above).  then you would be able to safely add it
# into Apprise at this point
aobj.add('foobar://')

# Send our notification out through our foobar://
aobj.notify("test")
```

You can read more about creating your own custom notifications and/or hooks here.

# Want To Learn More?

If you're interested in reading more about this and other methods on how to customize your own notifications, please check out the following links:

- 📣 Using the CLI
- 🛠️ Development API
- 🔧 Troubleshooting
- ⚙️ Configuration File Help
- ⚡ Create Your Own Custom Notifications
- 🌎 Apprise API/Web Interface
- 🎉 Showcase
Want to help make Apprise better?

- 💡 Contribute to the Apprise Code Base
- ❤️ Sponsorship and Donations

