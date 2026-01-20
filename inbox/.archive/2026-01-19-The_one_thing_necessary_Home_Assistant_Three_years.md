---
type: link
source: notion
url: https://eamonnsullivan.co.uk/posts-output/home-automation-three-years/2024-02-11-home-assistant-three-years-later/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-02-13T06:07:00.000Z
---

# The one thing necessary: Home Assistant: Three years later

## AI Summary (from Notion)
- Initial Motivation: The author began their journey with Home Assistant after receiving a Raspberry Pi, seeking to explore its potential.
- Evolution of Usage: Over three years, the author shifted from flashy automations to more subtle, practical applications that enhance daily life without being obtrusive.
- Reliability and Local Control: Emphasizes the importance of local automation solutions over cloud-dependent devices to avoid reliability issues.
- Device Preferences: A shift towards using devices that operate locally (e.g., Zigbee) rather than those relying on cloud services, due to concerns about future support and functionality.
- Increased Importance of Home Assistant: Transitioned from viewing Home Assistant as a hobby to considering it mission-critical for home automation.
- Zigbee Transition: Moved from Philips Hue to a more generic Zigbee system for better compatibility and control over various devices.
- Learning Curve and Challenges: Acknowledges the steep learning curve with Home Assistant, especially when troubleshooting issues, and the difficulties of debugging.
- Regrets: Reflects on past mistakes, such as reliance on cloud services and the choice of smart bulbs over integrated solutions.
- Overall Sentiment: Despite challenges and frustrations, the author enjoys the journey of learning and automating their home, viewing it as a rewarding hobby.

## Content (from Notion)

Almost three years ago, deep in the pandemic, my kids got me my first Raspberry Pi. That started me on an adventure with Home Assistant, mostly because it was one of the first search results for "what to do with a Raspberry Pi."

I'm still going, and learned much since then, so it is time for a quick update.

Hard disk space monitoring

## What hasn't changed

At the start, the foray into Home Assistant was tentative, but what attracted me to it then only got more compelling over time. Being able to use devices from many different manufacturers, without getting stuck in any walled gardens, is still hugely important. I don't have to decide between an Apple home, an Amazon home, a Philips home or a Google home. With Home Assistant, I can make my home out of the best bits from (almost) anyone, using Home Assistant's integrations.

The software continues to run on the exact same Raspberry Pi 4 the kids gave me, with a few tweaks (see below).

I'm also still using Node-RED for most of my automations. I remain more comfortable in Javascript than YAML (which is what Home Assistant's native automations are written in), even though Home Assistant has made many improvements to its built-in automation editor since I started.

The Node-RED flow for responding to motion in the master bedroom, taking into account the time of day and the day of the week.

I'm continuing to use the Home Assistant Cloud service, which is provided by the company behind Home Assistant and helps fund its development. It allows me to connect to my server securely while out of the house. It's possible (easy, even) to set that up yourself, but I want to contribute in some way.

## What has changed

The main thing that has changed is what I consider a good automation.

Three years ago, I was excited about things like flashing and colourful lights, getting notifications and making my speakers say things. I was aiming for something more like HAL 9000. My automations were heavy-handed and opinionated, and often annoyed my ever-patient wife and amused the kids, especially when they went wrong.

Nowadays, I'm using a lighter touch. I want the house to do the right thing, the expected thing, at the appropriate time. A good automation should be barely noticeable, almost invisible: The lights should turn on when you enter the room, if it's dark, and turn off again when they are not needed. The heating should come on when we wake up and turn off when we're out of the house or go to bed. Deviations, like keeping a light off or on, should be as simple as pressing a conveniently located button.

Most of my automations are not huge improvements over the simple light switch on the wall, and could hardly be described as life changing, but a small number are more substantive: We can tell the house "good night" (via a cheap, home-made voice control gadget) and lots of things happen -- some lights turn on, some off, the heating shuts down and the TV turns off. The house then waits for a quiet period (by checking motion sensors) before shutting all the lights and settling into "sleep" mode. The house does a similar "shut down" when it notices that no one is home, and "wakes" up when we return.

The Node-RED flow for shutting down the house at the end of the day.

### Local focus

My taste in devices has also become more discerning. At the beginning, I tried loads of things, from many manufacturers, most of which relied on cloud services. I quickly discovered how unreliable that was. I want to turn my lights off, even when my Internet connection is down.

In general, if we've learned anything over the years, it's that relying on the good will of any company is a really bad idea. If you buy an Alexa, a Google Nest, Hive thermostat or some other Internet-connect device, you are essentially renting a future paperweight -- features are withdrawn, companies go out of business and cloud services get shut down.

Today I buy and use devices that work locally, without an Internet connection. That means using local protocols, like Zigbee or my WiFi. I avoid anything that requires the cloud. It's OK to have a proprietary app, but I shouldn't be required to use it for important features. I haven't thrown out some of my past mistakes, like my Ring doorbell, but I won't buy more. I'm gradually transitioning, as I can afford to.

Unfortunately, this approach is antithetical to the interests of most companies, no matter how "not evil" they seem, so it is a bit of a struggle and will probably remain that way. I have hopes about Matter (a very new, local-focused standard for home automation), and will try it when supporting devices become more widely available, but I'm only cautiously optimistic. If it's possible to get an edge and keep the customer tethered, Google, Apple, Amazon, etc., will find a way.

### Reliability

One important shift in my attitude is that I now consider Home Assistant to be very important, even mission-critical, rather than just an experiment or a hobby. If that Pi gives up the ghost, it would be a real pain. I've beefed it up a bit: The Home Assistant software now runs on a hard disk (using an internal SSD like this and a new case), but the operating system (Ubuntu) is still running on an SD card that will crap out at the most inconvenient time.

I use the very slightly "advanced" container-based installation option for Home Assistant, which might help a bit. Originally, I used this method to learn docker and docker compose, but I've stuck with it because I like the flexibility. I could move services from one Pi to another, swiftly revert to a previous version or (assuming I've backed up the data volume recently) recover quickly from a hardware failure.

Still, I've only started to put some thought into what will replace this server hardware.

### Zigbee

At the start, the main way I managed all of my lights and motion sensors was via Home Assistant's Philips Hue integration. Under the hood, Philips Hue uses a light-weight, mesh protocol call Zigbee, but with some proprietary features accessible from an app. Almost everything I owned was through this integration. So much so that, other than a couple of buttons and speakers, I could have just used the Hue app to control things. This was Plan B, if Home Assistant didn't work out.

I've now switched to a more generic Zigbee system, using the SkyConnect dongle, and Home Assistant's own Zigbee Home Automation, because I wanted to start using devices that don't fit into the Philips Hue worldview, such as thermostats and radiator valves.

The transition wasn't easy. The SkyConnect was a lot fiddlier to get working and was more susceptible to network interference than the Hue hub (which had its own power supply and a bigger antenna).

I fixed the interference problems by buying a long (five-metre), shielded USB extension and moving the SkyConnect far away from the Raspberry Pi (and its USB3 connected hard drive), the WiFi router and other sources of interference. I had to monitor the airwaves in the house and switch Zigbee channels until I found a quiet place in the radio spectrum. Finally, I bought some Zigbee network extenders (like this one) to increase coverage and reliability.

## What I don't like

Knock on wood, everything in the house seems to be working now, but every big change seems to involve a bit of swearing and moving things around (or channel-changing) until things are stable again. Because of this, I'm becoming reluctant to fiddle -- or at least not until I have some time on my hands. I still enjoy the tinkering, but it has to be more carefully considered.

While Home Assistant is well documented compared with most open-source software, if something goes wrong, it can be difficult to debug. There's a lot of moving parts! The log messages are hard to decipher, and must be inscrutable to a non-programmer. The forums and Discord chats are friendly, but busy. Unless you catch the attention of someone who knows, your pleas for help quickly sink into the ether. Home Assistant users are a small percentage of most manufacturers customer base, so help is spotty as well from official tech support. I'm usually reduced to searching for the error messages in Github issues, hoping for a workaround.

Compared with my day job as a software engineer, I find automating my house a bit like tightrope walking without a net. It's basically impossible to be test-driven, or at least automated tests. Typically, after a big refactor, it'll take me a few days to find and fix simple bugs like copy and paste errors.

But, overall, my experience has been very positive. Home Assistant is such a large and diverse project that I'm still discovering new features almost every day.

## Regrets

When I look back, there are a few things that I would do differently. I might have leaned more toward smart switches and integrated wall sockets than smart bulbs and dongle-like plugs. And I could have saved myself a lot of heartache by avoiding cloud services. But the flexibility of Home Assistant and its thousands of integrations have meant that I can work through those issues and make do with almost anything -- there aren't many dead ends.

Would I do it all over again? That's a more complicated question. Nothing quite disturbs your peace as sitting in a dark room, or having a light turn on in the middle of the night, because an automation has gone wrong. Hardware, in general, is also crap and I've spent too many hours trying to fix that faulty light strip, dodgy motion sensor or misbehaving sensor.

But I've also quite enjoyed learning about it all. It's been a great hobby, particularly over the pandemic, when I had a lot of time on my hands. I'd do it again, and I'm looking forward to the next few years.


