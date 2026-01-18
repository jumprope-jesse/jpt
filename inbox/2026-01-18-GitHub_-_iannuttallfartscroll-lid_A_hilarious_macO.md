---
type: link
source: notion
url: https://github.com/iannuttall/fartscroll-lid
notion_type: Software Repo
tags: ['Running']
created: 2025-09-11T23:20:00.000Z
---

# GitHub - iannuttall/fartscroll-lid: A hilarious macOS app that plays fart sounds as you open and close your MacBook lid

## Overview (from Notion)
- This app can serve as a lighthearted way to bond with your kids, offering a humorous break from daily routines.
- It reflects a playful side of technology, showcasing how software can be both functional and fun.
- The unique concept taps into nostalgia for classic prank apps, making it a conversation starter among peers or at family gatherings.
- Consider how humor and creativity can enhance workplace culture, even in a tech-driven environment.
- While some may see it as just a silly novelty, others might appreciate its potential for stress relief and laughter in a fast-paced city life.
- Alternate views might argue that it's not suitable for professional settings, highlighting the importance of context in tech applications.
- Ultimately, it’s a reminder of the joy that can come from simple, sometimes ridiculous, ideas in our tech-centric lives.

## AI Summary (from Notion)
A humorous macOS app that plays fart sounds based on the MacBook lid angle. It features dynamic sound modulation, motion activation, and real-time monitoring. Users can install it by building from source or downloading a release, and it's designed for entertainment, especially in lighthearted settings.

## Content (from Notion)

# FartScrollLid 💨

A hilarious macOS app that plays fart sounds as you open and close your MacBook lid - inspired by the classic "fart scroll" browser extension!

## Features

- 🎵 Dynamic Fart Sounds - Pitch changes based on lid angle (deep bass when closed, high squeaks when open)
- 🎯 Motion-Activated - Only farts when you're actively moving the lid
- 📊 Real-Time Monitoring - Shows lid angle, velocity, and fart parameters
- 😄 Funny Status Messages - "Maximum pressure!", "Gas escaping!", and more
## How It Works

FartScrollLid uses the MacBook's internal lid angle sensor (discovered through reverse engineering) to detect the angle between your laptop lid and base. When you move the lid, it triggers fart sounds with:

- Pitch modulation based on lid angle (0-130 degrees)
- Volume control based on movement speed
- Instant response - farts stop immediately when you stop moving
## Requirements

- macOS 11.5 or later
- MacBook with lid angle sensor (most modern MacBooks)
- A sense of humor
## Installation

### Option 1: Build from Source

1. Clone this repository:
```plain text
git clone https://github.com/iannuttall/fartscroll-lid.git
cd fartscroll-lid
```

1. Open in Xcode:
```plain text
open FartScrollLid.xcodeproj
```

1. Build and run (Cmd+R)
### Option 2: Download Release

Download the latest .app from the Releases page.

## Usage

1. Launch FartScrollLid
1. Click "Start Farting"
1. Move your MacBook lid up and down
1. Enjoy the symphony of farts!
1. Stop moving to silence the farts
1. Click "Stop Farting" when you've had enough fun
## Technical Details

### Lid Angle Sensor

- Device: Apple HID device (VID=0x05AC, PID=0x8104)
- HID Usage: Sensor page (0x0020), Orientation usage (0x008A)
- Data format: 16-bit angle value in centidegrees (0.01° resolution)
- Range: 0-360 degrees
### Audio Engine

- Uses AVFoundation for real-time audio playback
- Varispeed unit for pitch modulation (0.5x to 2.0x)
- Smooth parameter ramping to avoid audio artifacts
- Movement threshold: 2 deg/s minimum to trigger farts
## Project Structure

```plain text
FartScrollLid/
├── FartScrollLid.xcodeproj/    # Xcode project
├── FartScrollLid/              # Source code
│   ├── AppDelegate.m/h         # Main app controller
│   ├── FartScrollLid.m/h       # Lid angle sensor interface
│   ├── FartAudioEngine.m/h     # Fart sound engine
│   ├── NSLabel.m/h             # Custom label class
│   └── FART.wav                # Fart sound file
└── README.md                   # This file

```

## Credits

- Based on the original LidAngleSensor app by Sam Henri Gold
- Fart sound from fart.js
- Inspired by the original fart scroll browser extension by The Onion
- Built with assistance from Factory Droid
## License

MIT License - see LICENSE file for details

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

Ideas for improvements:

- Additional fart sound variations
- Customizable pitch/volume curves
- Fart statistics tracking
- Network multiplayer farting
- Apple Watch companion app
## Disclaimer

This app is for entertainment purposes only. Please use responsibly in appropriate settings. Not recommended for:

- Business meetings
- Libraries
- First dates
- Job interviews
- Funerals
But highly recommended for:

- Pranking friends
- Amusing children
- Breaking awkward silences
- General tomfoolery
## Author

Created by Ian Nuttall with Factory Droid

Remember: Life is too short not to laugh at fart sounds from your laptop 💨😄


