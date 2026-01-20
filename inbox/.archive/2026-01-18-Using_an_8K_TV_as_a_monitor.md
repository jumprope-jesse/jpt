---
type: link
source: notion
url: https://daniel.lawrence.lu/blog/y2023m12d15/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-11-20T05:04:00.000Z
---

# Using an 8K TV as a monitor

## Overview (from Notion)
- Using an 8K TV as a monitor could enhance your coding experience, allowing for a more streamlined workspace without the distractions of bezels from multiple monitors.
- The high resolution is beneficial for photo and video editing, especially if you have hobbies in that area or engage in personal projects.
- The versatility of an 8K TV can allow you to switch seamlessly between work, gaming, and family movie nights, making it a multifunctional investment.
- Consider how a larger screen can accommodate your busy life, enabling better multitasking and improving productivity while working from home.
- The cost can be justified if you would otherwise invest in multiple monitors and a separate TV, simplifying your setup.
- Be aware of potential quirks with connectivity and software; research compatibility with your current setup to avoid frustration.
- An alternative viewpoint is that traditional monitors may still offer better color accuracy for professional photo and video work, depending on your specific needs.
- Think about the desk space and viewing distance; larger screens can lead to a more immersive experience but may require adjustments to your workspace.

## AI Summary (from Notion)
Using an 8K TV as a monitor offers superior image quality and versatility for programming, word processing, and gaming compared to multiple 4K monitors. It provides a seamless display without bezels, enhancing productivity. While suitable for photo and video editing, it may require calibration for color accuracy. 8K TVs are also effective for gaming at 4K 120 Hz, though most GPUs struggle with 8K gaming. Considerations include desk space, potential image quality issues, and necessary connectivity settings for optimal performance.

## Content (from Notion)

A Samsung QN800A.

> TLDR: If your job is to write code all day or stare at Excel spreadsheets, buy an 8K TV instead of a multi-monitor setup. You can even use the same TV for 4K 120 Hz gaming or watching movies as a bonus!

For programming, word processing, and other productive work, consider getting an 8K TV instead of a multi-monitor setup. An 8K TV will have superior image quality, resolution, and versatility compared to multiple 4K displays, at roughly the same size. As a bonus, an 8K display is also suitable for gaming at 4K 120 Hz, or for full screen media consumption, which is not possible with multiple smaller monitors.

Currently 8K TVs are found in 55” and above. This is about the same width as getting two 27” monitors or two 32” monitors, both common setups for programmers and other professionals. This is also the same physical width as ultrawide screens, but with a superior resolution of 7680 px wide instead of the common upper limit of 5120 px for ultrawide screens.

## 1.1 For programming, word processing, etc

Three 27

FIGURE 3 Some random code displayed on an 8K display. Having seven evenly-spaced columns would be impossible on a dual 4K display setup due to bezels in the middle.

Many programmers use a multi-monitor setup, often with multiple 4K monitors. The bezels and gaps in between the monitors introduce distractions and one is limited in how one may arrange terminals and windows across multiple displays. With a single 8K display there is no such problem.

Consider using a tiling window manager to arrange your windows in a large display. Tiling window managers exist for all operating systems. Here are some examples that I enjoy:

- For Linux: i3, Sway. Note that although Nvidia was previously hostile to Wayland and Sway, it now works as of 2023. There are a lot more others.
- For MacOS: Yabai
Productivity is highly sensitive to the display of text. For this reason, many programmers prefer to use Apple products for their retina displays. An 8K display will have vastly superior text rendering compared to a single large 4K display, and equivalent text rendering to multiple smaller 4K displays.

TVs may have a different subpixel layout than monitors, so small text may suffer fringing. As of writing the Samsung VA and LG IPS panels such as the QN800A have a conventional RGB or BGR subpixel structure. One may also increase the font size or use hidpi scaling which will eliminate all pixel-level concerns.

## 1.2 For photo and video editing

Although the main motivation for getting the 8K display was for programming, it is quite nice for photography too. Apart from the obvious advantage of being able to see a large photo with a sharp resolution, having a high resolution display allows toolbars and such to be legible at a much smaller size relative to the size of the display. This improves productivity for photo editing. Of course, appropriate hidpi settings may be used to increase the size of toolbars if desired.

An 8K TV often supports the D65-P3 colour gamut, making it appropriate for photo and video editing. It may not arrive as well-calibrated as professional monitors out of the box, but it should be possible to calibrate any screen with a display calibrator. However, extremely colour-sensitive work should still use professional calibrated displays suited for that purpose.

## 1.3 For CAD work

CAD work is highly dependent on visualizing fine details. In particular, a wireframe rendering may become unintelligible if it is of insufficient resolution. A high resolution display will allow fine details to be seen even while viewing multiple viewports without having to maximize the viewport. However the viewport may be maximized to occupy the full screen nonetheless, a great advantage compared to multi-monitor setups.

## 1.4 For gaming/media

Although this post is mostly focused on productivity, most if not all 8K TVs can be run in 4K at 120 Hz. Modern TVs have decent input lag in the ballpark of 10 ms and may support FreeSync. So these are excellent for gaming on the big screen when one needs to take a break from work. Of course, this may not suffice for competitive professional FPS twitch shooters, but it is pretty darn good. Multi monitor productivity setups using 4k 60 Hz monitors simply cannot achieve this.

An 8K TV will also natively support 1440p gaming and media at an exact integer ratio of 3:1 without scaling artifacts that a 4K display would introduce. Perfect for playing the latest titles that your GPU isn’t fast enough to run in 4K.

Please bear in mind that most GPUs will not run games performantly in 8K and there are basically no 8K movies.

For watching movies, I set my TV to 4K 120 Hz mode as well. The 120 Hz is divisible by both 24 fps and 30 fps. Furthermore, if the media player lags and delays by one frame for some reason, it is still a lot smoother to delay by 1/120 s rather than 1/24 s.

## 1.5 Cost

8K TVs tend to start at around $1500 to $2000 for a 65” one. This is about the same as getting four 32” 4K monitors.

However, many people who get a multi-monitor productivity setup also buy a separate 4K TV just for gaming or media consumption. In this case, having one screen that does it all may save some money.

## 1.6 Connectivity

8K TVs may be driven at 8K 60 Hz with no chroma subsampling by using HDMI 2.1, which is available on all current (Nvidia RTX 4000 series and AMD 7000 series) and previous gen (Nvidia RTX 3000 series, AMD 6000 series) graphics cards. Older computers with GPUs outputting DisplayPort 1.4 may use adapters such as the Club3D one to achieve 8K 60 Hz.

## 2.1 Desk and mounting

FIGURE 5 My 75” × 42” desk is bigger than a single bed.

When purchasing a large display, one may need to sit farther back from the display when viewing full-screen content. As such, a deeper desk may be needed. Most desks are only 30” (76 cm) deep, which is an insufficient distance to sit from the screen. Please take into consideration the potential extra costs of buying a bigger desk, or consider wall-mounting the display.

My desk is an Uplift four leg standing desk with a custom 75” × 42” dimension. You could also buy a large butcher’s block or door and mount it on a desk frame. Large dining tables or conference room tables work well too.

## 2.2 Image quality issues

### 2.2.1 Uniformity

Due to manufacturing variance, there may be some nonuniformity in high resolution displays, leading to what is called the “dirty screen effect”. This is not expected to be an issue for programming work, but can be distracting or harmful for photographic work or media consumption. An appropriate calibration can mitigate the problem but it is still recommended to obtain a uniform, professional display for colour-critical work.

> The Samsung QN800A has good gray uniformity. Although the screen is fairly uniform throughout, there’s a bit of dirty screen effect in the center, which could be distracting during sports. The screen is much more uniform in near-dark scenes. Keep in mind that uniformity may vary between units.

Ratings sites such as RTINGS.com have good measurements of uniformity.

FIGURE 6 50% Gray uniformity test from RTINGS.com. Source: RTINGS.com.

### 2.2.2 Checkerboard effect

Some 8K TVs have a subtle “checkerboard” effect visible at the 1px scale, such as the Samsung QN700B and QN800A unless you have variable refresh rate (VRR) enabled. The problem is completely gone once you enable VRR. This is typically called “Game Mode” on most TVs.

Due to the rather hidden nature of this quirk, many people, including me, forgot to enable Game Mode and this has led to some review comments such as this Best Buy review comment.

This does not affect most text rendering, but I have noticed this effect when editing photos.

Again, the problem is completely gone once you enable VRR/Game Mode on the TV, so be sure to enable it!

## 2.3 Random software issues

Since TVs are rarely designed for PC usage as a first class citizen, there may be some weird quirks or bugs.

### 2.3.1 Nvidia Linux drivers

Currently, it works perfectly with modern Nvidia graphics cards with current drivers.

If using Nvidia on Linux, to get 8K 60 Hz working, you need driver version 535 or later on Linux, which was released in May 2023. Versions prior to that would only do 8K 30 Hz.

Although Nvidia on Windows has supported 8K 60 Hz as soon as the RTX 3000 series came out, on Linux it took about two years for 8K 60 Hz support to work, spawning a salty thread on GitHub.

So please make sure to update your drivers!

As a minor concern, there may be some slight vertical screen tearing between the left and right halves of the display.

### 2.3.2 AMD Linux drivers

Unfortunately, as of writing, on Linux, AMD GPUs do not have HDMI 2.1 so you cannot use an 8K TV in 8K 60 Hz mode unless you use a DisplayPort to HDMI adapter. It works fine on AMD on Windows, however.

The AMD on Linux fiasco is because the HDMI Forum has prohibited AMD from implementing HDMI 2.1 in their open source Linux drivers.

### 2.3.3 Input Signal Plus

To get 8K 60 Hz working, you need to go into TV menus and enable “Input Signal Plus”, “Enhanced HDMI”, or something similar. For some silly reason, this may be disabled by default, which will relegate you to only 4K or 30 Hz. As mentioned in the checkerboard effect section, also be sure to turn on Game Mode or variable refresh rate (VRR).

### 2.3.4 Wake up bugs

Sometimes if your computer goes to sleep or turns the monitor off to save energy, when waking up the TV will not detect it. Worse, sometimes when waking up, the TV will revert to only 4K mode, and you’d have to go into the menus to toggle the “Input Signal Plus” setting to make it work properly again. This is pretty annoying but I just disabled turning off the monitor in my OS.

### 2.3.5 Having another DisplayPort device

When having another DisplayPort device plugged into your GPU, your computer may favor the DisplayPort device upon boot. This means that when booting up, the BIOS menu, bootloader, and such will get sent to the DisplayPort device instead of the HDMI device.

This was annoying for me because I have a Valve Index VR headset which uses DisplayPort whereas the TV, using HDMI, is my main display. I had to unplug the Valve Index, but if anyone knows any other methods then I would be interested to hear them.

## 2.4 Display types

Currently, 8K TVs are generally available as “full array backlight” IPS or VA panels. These will have equivalent or superior contrast compared to most IPS desktop monitors, but will have inferior contrast compared with OLED displays. OLED 8K TVs exist, but are prohibitively expensive at $30,000 as of writing. However, OLED displays are prone to burn in when used for productivity work and may have features such as automatic dimming for static scenes, which can be distracting while performing lengthy tasks like programming.

## 2.5 Coatings

TVs tend to have a glossy coating for superior image quality. However for brightly lit rooms there may be unavoidable reflections. For my use case, even though my TV is right next to a window, I have never found any issues focusing on my code with a dark theme.

Unfortunately, there are very few 8K displays on the market, and many decent ones (such as the 55” Samsung QN700B) are discontinued. Some 8K TVs include:

- Samsung Q900 series (55” to 82”)
- Samsung Q800T series
- Samsung Q900TS series
- Samsung Q950TS series
- Samsung QN700B series
- Samsung QN800A/B/C/D series
- Samsung QN900A/B/C/D
- LG Nanocell 97 series
- LG Nanocell 99 series
- Sony Z8H series
- Sony Z9G series
- TCL Class 6-series 8K
There are also some crazy $30,000 OLED displays and even crazier huge 262” microled displays that cost millions.

There is also a Dell UP3218K, but it costs the same as an 8K TV and is much smaller and has many problems. So I do not recommend it unless you really don’t have the desk space. Sitting further back from a bigger screen provides the same field of view as sitting close to a smaller display, and may have less eye strain.

I am excited about upcoming TCL 8K displays.

> Isn’t it too big?

The width and pixel density is the same as two 32” monitors.

Using the i3 window manager, I usually arrange the most frequently used terminals on the bottom half to minimize neck craning. For example, when coding in C++, it’s nice to have the header file open on the top half where I occasionally glance at the class members and function signatures while implementing it in the bottom half.

Also, thanks to my large desk, I do sit sufficiently far from it so that I don’t have to rotate my neck too much.

> But there are no 8K movies

I don’t usually watch movies on this, but when I do, I set it to 4K 120 Hz mode. The 120 Hz is nice as it is divisible by both 24 fps and 30 fps, which are common framerates for movies, although The Hobbit running at 48 Hz would benefit from Variable Refresh Rate (which does work).

> But can your GPU even run 8K games?

I play games in 4K 120 Hz mode. Actually, some games like Factorio could benefit from 8K 60 Hz mode, but those are not graphically intensive. Theoretically, Age of Empires II would be interesting too since you could see a lot of the map at once.

> How about a projector?

There are no affordable 8K projectors and the pixel density for displaying lots of text is a main motivation for getting an 8K display.

I have just learnt on Hacker News that there are fancy 8K projectors such as the JVC DLA-VS8000G, but it is discontinued and obviously not a consumer product. Apparently, it’s made for Boeing flight simulators!

> How about the Apple Vision Pro?

Despite having much better pixel density than other VR headsets, the pixel density isn’t quite there yet for looking at lots of text such as spreadsheets.


