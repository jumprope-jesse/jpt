---
type: link
source: notion
url: https://github.com/alexbatalov/fallout1-ce
notion_type: Software Repo
tags: ['Running']
created: 2024-04-23T18:44:00.000Z
---

# GitHub - alexbatalov/fallout1-ce: Fallout for modern operating systems

## AI Summary (from Notion)
- Project Title: Fallout Community Edition (fallout1-ce)
- Purpose: Re-implementation of the original Fallout game for modern operating systems.
- Status: Not started (as of April 23, 2024).
- Key Features:
- Maintains original gameplay with engine bug fixes and quality of life improvements.
- Compatible with multiple platforms (Windows, Linux, macOS, Android, iOS).
- Installation Requirements:
- Users must own the original game to play.
- Instructions provided for installation across various operating systems.
- Configuration:
- Main configuration file is fallout.cfg, with settings related to file names and music paths.
- Secondary configuration file f1_res.ini allows changes to game window size and fullscreen mode.
- Future Goals:
- Update to version 1.2 for improved multilingual support.
- Backport features from Fallout 2 to enhance the original game engine.
- License: Available under the Sustainable Use License.
- Interesting Fact: The project is based on the Reference Edition of Fallout, which was released in 1997.

## Content (from Notion)

# Fallout Community Edition

Fallout Community Edition is a fully working re-implementation of Fallout, with the same original gameplay, engine bugfixes, and some quality of life improvements, that works (mostly) hassle-free on multiple platforms.

There is also Fallout 2 Community Edition.

## Installation

You must own the game to play. Purchase your copy on GOG or Steam. Download latest release or build from source. You can also check latest debug build intended for testers.

### Windows

Download and copy fallout-ce.exe to your Fallout folder. It serves as a drop-in replacement for falloutw.exe.

### Linux

- 
- 
```plain text
$ sudo apt install innoextract
$ innoextract ~/Downloads/setup_fallout_2.1.0.18.exe -I app
$ mv app Fallout
```

- 
- 
```plain text
$ sudo apt install libsdl2-2.0-0
```

- Run ./fallout-ce.
### macOS

> 

- 
- 
- 
```plain text
$ brew install innoextract
$ innoextract ~/Downloads/setup_fallout_2.1.0.18.exe -I app
$ mv app /Applications/Fallout
```

- 
- 
### Android

> 

> 

- 
- 
- 
### iOS

> 

- 
- 
- 
## Configuration

The main configuration file is fallout.cfg. There are several important settings you might need to adjust for your installation. Depending on your Fallout distribution main game assets master.dat, critter.dat, and data folder might be either all lowercased, or all uppercased. You can either update master_dat, critter_dat, master_patches and critter_patches settings to match your file names, or rename files to match entries in your fallout.cfg.

The sound folder (with music folder inside) might be located either in data folder, or be in the Fallout folder. Update music_path1 setting to match your hierarchy, usually it's data/sound/music/ or sound/music/. Make sure it match your path exactly (so it might be SOUND/MUSIC/ if you've installed Fallout from CD). Music files themselves (with ACM extension) should be all uppercased, regardless of sound and music folders.

The second configuration file is f1_res.ini. Use it to change game window size and enable/disable fullscreen mode.

```plain text
[MAIN]
SCR_WIDTH=1280
SCR_HEIGHT=720
WINDOWED=1
```

Recommendations:

- Desktops: Use any size you see fit.
- Tablets: Set these values to logical resolution of your device, for example iPad Pro 11 is 1668x2388 (pixels), but it's logical resolution is 834x1194 (points).
- Mobile phones: Set height to 480, calculate width according to your device screen (aspect) ratio, for example Samsung S21 is 20:9 device, so the width should be 480 * 20 / 9 = 1067.
In time this stuff will receive in-game interface, right now you have to do it manually.

## Contributing

Here is a couple of current goals. Open up an issue if you have suggestion or feature request.

- 
- 
## License

The source code is this repository is available under the Sustainable Use License.


