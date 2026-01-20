---
type: link
source: notion
url: https://www.jeffgeerling.com/blog/2025/upgrading-m4-pro-mac-minis-storage-half-price
notion_type: Physical Product Review
tags: ['Running']
created: 2025-07-12T14:27:00.000Z
---

# Upgrading an M4 Pro Mac mini's storage for half the price | Jeff Geerling

## Overview (from Notion)
- Upgrading your Mac mini’s storage can save you significant money compared to Apple's pricing, making it a practical choice for personal and professional use.
- The DIY process of upgrading allows for hands-on engagement with your technology, which can be fulfilling and educational, especially for your kids to see tech in action.
- The performance benefits of the upgrade can enhance productivity, particularly if you're handling large files or video editing, crucial for your work as a software engineer.
- Consider the sustainability angle: upgrading instead of buying new aligns with eco-friendly practices—a lesson you can pass on to your family.
- The discussion around proprietary technology highlights the balance between security and accessibility, prompting a broader conversation about tech choices in your household.
- For a city dweller, the compact nature of the Mac mini and its upgradeability make it an ideal fit for small living spaces without sacrificing performance.

## AI Summary (from Notion)
An upgrade from a 512 GB to a 4 TB SSD in the M4 Pro Mac mini is possible using a proprietary upgrade kit, which requires a DFU restore process. The upgrade is straightforward but involves careful disassembly. Performance tests show the upgraded SSD performs better in write speeds compared to external drives, although the internal storage is consistently fast. The upgrade costs $699, significantly less than Apple's $1,200 option.

## Content (from Notion)

A few months ago, I upgraded my M4 Mac mini from 1 to 2 TB of internal storage, using a then-$269 DIY upgrade kit from ExpandMacMini.

At the time, there was no option for upgrading the M4 Pro Mac mini, despite it also using a user-replaceable, socketed storage drive.

M4 Pro Mac mini guts with M4-SSD 4TB Upgrade Installed

But the folks at M4-SSD reached out and asked if I'd be willing to test out one of their new M4 Pro upgrades, in this case, upgrading the mini I use at the studio for editing from a stock 512 GB SSD to 4 TB.

I said yes, and here we are!

I documented the entire upgrade—along with taking my old M4 mini 1TB SSD and putting it in my Dad's M4 mini—in today's video:

But please continue reading, if you prefer text over video, like I do :)

The upgrade process itself is straightforward (if you've ever worked on laptop hardware before, at least), though removing the rear plastic cover (which also has the power button attached) is a bit annoying.

There are four metal pegs that are retained in clips in the bottom metal cover, and you have to slide a thin piece of metal / pry tool into the very minimal gap between the plastic bottom cover and the aluminum case, then pry it up. And if you're not careful on that step, you'll not only scratch the aluminum (and maybe crack the plastic bottom), but there's a good chance you rip the fragile (and tiny) power button connector too!

Besides that, it's a matter of removing a number of small torx screws; all the bits I needed were present in the cheapest iFixit assortment I have at my desk.

The only substantial difference between the M4 and M4 Pro mini SSD is the size and relative location—the M4 Pro has a much longer slot, a little more than a standard 2242-size NVMe SSD, while the M4 has a shorter slot, closer to a 2230.

## DFU Restore

Speaking of standards... you have to do a full DFU (Device Firmware Update) restore, because unlike conventional M.2 NVMe storage, the M4 uses a proprietary connector, a proprietary-sized slot, and splits up the typical layout—the card that's user-replaceable is actually just flash chips and supporting power circuits, while the storage controller (the NVMe 'brains') is part of the M4 SoC (System on a Chip). Apple could use standard NVMe slots, but they seem to think the controller being part of the SoC brings better security... it certainly doesn't bring any cost savings, resiliency in terms of quick recovery from failure in the field, or performance advantage!

Since DFU restore is necessary, in my earlier video, I suggested you need an Apple Silicon mac (M1 or later) as the other computer.

But I was corrected by my viewers, who mentioned you can use many Intel Macs as well—I believe as long as a T2 chip is present, you're good to go. Just connect to the middle Thunderbolt port on the rear of the Mac mini, then press and hold the power button while plugging it into AC power. The other Mac should pop up an 'Allow this device to connect?' dialog and then you can proceed to the DFU process from there.

> 

I've done three upgrades (two on M4 minis, one on an M4 Pro mini), and all three were easy. The second one, I thought I had an issue, but it was just a confirmation dialog that wound up behind the active window.

## Performance

I decided to also use an external Thunderbolt 5 NVMe enclosure from M4-SSD along with my (rather expensive) 8TB Sabrent Rocket Q SSD, and do a performance comparison.

See the video at the beginning of this post for some more detail (like all the numbers from AmorphousDiskMark and Blackmagic Disk Speed Test), but here are the raw numbers for large file copy performance:

M4 Pro mac mini benchmark performance SSDs

The upgraded 4TB module performed noticeably better in writes, likely because it has more flash chips on it to spread out the write activity. Reads were pretty close to the same, with minor variance in performance across different file sizes and access patterns.

The external TB5 drive was the laggard, but is still ridiculously fast (by my standards, editing 4K video). And it would likely be faster if I used a good PCIe Gen 4x4 drive (the Rocket Q is Gen 3x4).

But the internal storage on these Mac minis is very fast, and even better, very consistently fast. The external Thunderbolt drive would slow down briefly every minute or so, after 100+ GB were copied—and I verified both with smartctl and my thermal camera that the drive was not overheating.

This is likely due to the internal DRAM cache on the NVMe SSD not being able to keep up with the high transfer speeds over long periods of time.

## Conclusion

I was provided the $699 M4 Pro 4TB SSD upgrade by M4-SSD. It's quite expensive (especially compared to normal 4TB NVMe SSDs, which range from $200-400)...

But it's not nearly as expensive as Apple's own offering, which at the time of this writing is $1,200!

Apple M4 Pro mac mini upgrade pricing 1200


