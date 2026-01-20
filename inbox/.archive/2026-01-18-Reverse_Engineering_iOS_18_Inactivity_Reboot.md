---
type: link
source: notion
url: https://naehrdine.blogspot.com/2024/11/reverse-engineering-ios-18-inactivity.html
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-11-18T00:14:00.000Z
---

# Reverse Engineering iOS 18 Inactivity Reboot

## Overview (from Notion)
- The new inactivity reboot feature in iOS 18 enhances security by ensuring devices reboot after 3 days of inactivity, which could protect sensitive data from theft.
- As a software engineer and founder, understanding this security measure could influence how you approach app development, especially in terms of data protection.
- The trade-off between user privacy and security is significant; while the feature enhances security, it also raises concerns about user autonomy and control over device functionality.
- Consider the implications for your family—if a device unexpectedly reboots, it may disrupt access to important information or apps, especially during critical times.
- Unique viewpoint: This feature reflects a broader trend in technology prioritizing security over convenience, which could resonate with your entrepreneurial mindset.
- Alternate view: Some might argue this could inconvenience users, particularly those who leave their devices unattended for legitimate reasons, like during family vacations.
- The feature may spark discussions about the balance of law enforcement access versus user rights, relevant in a city like NYC with its own unique privacy concerns.

## AI Summary (from Notion)
iOS 18 introduces an inactivity reboot feature that enhances security by forcing devices to reboot after 3 days of inactivity, impacting user privacy and convenience. It complicates access for criminals but also affects law enforcement's ability to gather evidence. The Secure Enclave Processor tracks inactivity, and the reboot process is initiated by the AppleSEPKeyStore kernel module. This feature changes the threat landscape, potentially locking out thieves while increasing pressure on law enforcement to act quickly.

## Content (from Notion)

iOS 18 introduced a new inactivity reboot security feature. What does it protect from and how does it work? This blog post covers all the details down to a kernel extension and the Secure Enclave Processor.

## Security Before First Unlock / After First Unlock

Did you know that entering your passcode for the first time after your phone starts is something very different then entering it later on to unlock your phone?

When initially entering your passcode, this unlocks a key store in the Secure Enclave Processor (SEP) that encrypts your data on an iPhone.

The state before entering your passcode for the first time is also called Before First Unlock (BFU). Due to the encrypted user data, your iPhone behaves slightly differently to later unlocks. You'll see that Face ID and Touch ID won't work and that the passcode is required. But there's more subtle things you might notice: Since Wi-Fi passwords are encrypted, your iPhone won't connect to Wi-Fi networks. If your SIM is not PIN-protected, your iPhone will still connect to cellular networks. That means, technically, you can still receive phone calls. Yet, if you receive a call, even if that number is in your contacts, the contact name won't be shown, as the contacts haven't been decrypted yet. Similarly, when you receive notifications about new messages, you'll see that you got messages, but you won't see any message previews. You can easily try this yourself!

In the After First Unlock (AFU) state, user data is decrypted. You can imagine this like a key safe that is kept open while iOS is running. Even when you see a lock screen, certain keys remain available to the operating system. This way, you stay connected to Wi-Fi networks and receive message notification previews, even when your iPhone is locked.

While it's more convenient, the AFU state is more susceptible to attacks. An attacker who can somehow bypass the lock screen can get access to decrypted data on the iPhone. To bypass the lock screen, an attacker does not necessarily need to know the passcode. Security vulnerabilities within iOS can allow attackers to get code execution and extract from an iPhone, even while it appears to be "locked".

Attackers with physical access to an iPhone have more security vulnerabilities to choose from. The attack surface is larger, as such attackers can exploit vulnerabilities in the USB stack or within wireless protocols, such as Wi-Fi, Bluetooth, or cellular, or even more invasive hardware attacks that involve opening the device. This larger attack surface tends to make exploits for these vulnerabilities cheaper on the gray market, as there's potentially more supply. Another factor that makes attacks cheaper is time – vulnerabilities that are publicly known by the vendor and patched in more recent software versions won't unlock new iPhones, but can unlock iPhones that were kept in AFU state for a long time that didn't get any software updates.

## Rumors about Rebooting iPhones

In law enforcement scenarios, a lot of the forensically relevant data is available in the AFU state. Law enforcement takes advantage of this and often keeps seized iPhones powered on, but isolated from the Internet, until they can extract data. This time might be necessary to wait for an exploit to be available or for legal reasons, such as getting a warrant.

However, thieves and other criminals are also interested in getting this kind of access after stealing a device. It gives them access to bank accounts and other valuable information, by far exceeding what the iPhone itself would be worth, or which might be used for blackmail. People reuse their passwords often, and getting access to the iCloud account may allow a thief to reset activation lock for the device, increasing the resale value.

A recent news article by 404 media (while paywalled, the most important information is also contained in the related Tweet) reported on a law enforcement document about suspicious iPhone reboots. This document makes two interesting claims:

1. iPhones on iOS 18 will reboot, even when completely isolated from wireless networks.
1. iPhones on iOS 18 will tell other iPhones on lower iOS versions to reboot – wirelessly!
Especially the second claim would be huge if true. If anyone figured out how this works, they could build a large TV-Be-Gone for iPhones, forcing reboots over the air on hundreds of iPhones simultaneously. Would Apple really build such a feature into an iPhone?

Knowing a thing or two about the Apple wireless ecosystem, my interest was piqued, and I had to go down the rabbit hole!

## Discovery of Inactivity Reboot

When Apple adds new features, they usually don't hide this very well. Apple software contains a lot of debug strings, which hint at new functionality. Blacktop maintains a git repository of strings found in iOS, which keeps a nice version history. I decided to do the most low-effort thing I could think of: just search for "reboot".

Bingo, that third hit looks good: "inactivity_reboot". The fact that it's in keybagd is interesting: this daemon is related to the key store that is unlocked on the first unlock.

A second search for only inactivity reboot shows the string starts occurring in iOS 18.1 and iOS 18.2. In iOS 18.2, the string changed from "inactivity_reboot" to "inactivity_reboot_enabled", hinting towards more potential changes in the latest iOS 18.2 betas.

Something that was still unclear to me at that point is: How long does it take for inactivity reboot to be triggered? A new article by 404 media claimed that it was 3-4 days. So I updated my SRD to the latest beta and made a time lapse.

Turns out, the inactivity reboot triggers exactly after 3 days (72 hours). The iPhone would do so despite being connected to Wi-Fi. This confirms my suspicion that this feature had nothing to do with wireless connectivity.

## Reverse Engineering Inactivity Reboot

Let's reverse engineer what's changed! Which security guarantees does it provide?

Here is a high-level overview of what I found:

- The Secure Enclave Processor (SEP) keeps track on when your phone was last unlocked. If that last unlock time exceeds 3 days, the SEP tells the AppleSEPKeyStore kernel module that the time was exceeded.
- The AppleSEPKeyStore kernel module informs user space to initiate a reboot. SpringBoard will then gracefully terminate all user-space processes. This prevents potential data loss upon reboot.
- If the AppleSEPKeyStore kernel module finds the iPhone to still be powered on after it should have rebooted, the kernel will panic. This case should never happen, unless someone tries to tamper with inactivity reboot.
- The AppleSEPKeyStore kernel module writes an NVRAM variable aks-inactivity. After the iPhone rebooted, keybagd reads this variable and, if set, sends an analytics event to Apple including how long the iPhone was not unlocked.
The remainder of this post shows how I figured this out and what security implications the underlying design has.

## Indicators in Sysdiagnose

From my search in ipsw-diffs, I knew there were some log messages that are printed on reboot. At the same time as I started looking them statically, I knew I had to see them actually logged for myself.

After my phone rebooted after three days, I took a sysdiagnose and searched for these messages. When doing this yourself, make sure that you unlocked the device before making the sysdiagnose. Otherwise, events from before the reboot will be missing.

In the AppleSEPKeyStore messages, there are the following entries around the inactivity reboot:

default 2024-11-17 01:35:14.341697 +0100 kernel "AppleSEPKeyStore":3846:0: notifying user space of inactivity reboot

default 2024-11-17 01:35:14.341766 +0100 kernel "AppleSEPKeyStore":12598:31: operation failed (sel: 35 ret: e00002f0)

default 2024-11-17 01:35:14.342053 +0100 kernel "AppleSEPKeyStore":12598:31: operation failed (sel: 35 ret: e00002f0)

default 2024-11-17 01:35:34.958218

[reboot occurs]

+0100 kernel "AppleSEPKeyStore":331:0: starting (BUILT: Oct 26 2024 08:16:35) ("normal" variant 🌽 , 1827.60.43)

default 2024-11-17 01:35:34.958381 +0100 kernel "AppleSEPKeyStore":476:0: _sep_enabled = 1

For more context, these are the unfiltered log messages before the reboot is initiated:

## Reverse Engineering the SEPKeyStore Kernel Extension

The latest iOS kernel can be downloaded using the following ipsw command:

ipsw download appledb --device iPhone17,3 --os iOS --version '18.2 beta 2' --kernel

This will download and decompress the kernel. For further analysis, I loaded the whole kernel cache into Binary Ninja. ipsw also supports splitting the kernel into its modules (called "extensions" on iOS). The latest version of Ghidra also has decent support for the iOS kernel. So there's a lot of tools to choose from for this analysis.

I also downloaded an older kernel where Apple accidentally included symbols and manually diffed these versions with a focus on the code related to inactivity reboot. The kernel has three strings relating to the feature:

"notifying user space of inactivity reboot" is the string we already know from the sysdiagnose. It belongs to the function AppleKeyStore::handle_events, which polls for SEP events in the background. The following screenshot shows it in more context after reverse engineering and some renaming of functions.

The first string, "max inactivity window expired, failed to reboot the device", is the kernel panic in case that the iPhone failed to reboot.

For more context, the panic is called by the function AppleKeyStore::handle_device_state_return. There are multiple paths that invoke this handler through many layers of abstraction, which have to do with the UserClient but also SEP states.

With the calltree plugin, we can see all the incoming calls to this function.

Now to the last string, "aks-inactivity". We can see that this is a property that is set in the IORegistry.

Its counterpart is in keybagd in user space. When keybagd is initialized, it checks for this variable, issues an analytics event, and then deletes it. This analytics event probably helps Apple optimize the time window, but we can ignore it for the core functionality.

Something that I couldn't find in the kernel, even with the knowledge that it was 72 hours, was this particular time window. I couldn't find any numbers that matched 72 hours. So how does the phone know when to reboot?

While there are some references to time-related functionality in the SEPKeyStore kernel extension, none of these compare a value to 72 hours. These references were quite simple to find and did not differ much from the older kernel version without inactivity reboot, so it doesn't seem like the functionality was added here.

However, the SEPKeyStore communicates with the SEP co-processor. In the functions I identified, reboots are related to some SEP states. Could it be the SEP itself that checks the time?

## Reverse Engineering the Secure Enclave Processor

The SEP is one of Apple's most protected secrets. In contrast to most other firmware on the iPhone, the firmware for the SEP is encrypted.

Luckily for us, @nyan_satan recently leaked SEP firmware encryption keys for iOS 18.1 beta 6, just eta wen Apple introduced inactivity reboot. (Thank you!! 🎉 And Apple, if you're reading this, why not ship the SEP unencrypted?) Using ipsw, we can download the SEP firmware as follows:

ipsw download appledb --device iPhone16,1 --os iOS --version '18.1 beta 6' --pattern "sep-firmware.d83.RELEASE.im4p"

With the leaked keys, we can decrypt the firmware:

pyimg4 im4p extract --iv 6705fb216080e19667dbcf71f532ae73 --key 4ea9db4c2e63a316a6854c83e2f5c81fd102ad40160b8998b5f9b16838b7116e -i sep-firmware.d83.RELEASE.im4p -o sep-firmware.d83.RELEASE.im4p.e

Loading this into Binary Ninja is a bit tricky. We can guess that the architecture is 64-bit ARM little endian. But there's no metadata where the firmware has to be loaded to. Being lazy and not wanting to spend time on writing a firmware loader, I used Binary Ninja's Triage feature to auto-detect the most likely address. Note that the firmware seems to have multiple fragments and there's multiple potential load addresses. I picked 0x80090000ffc80000, which worked well for me.

There's only little known about the SEP. The best information I could come up with is a presentation dating back to 2016 – but that's better than nothing! What's good to know is that the SEP firmware is structured into apps, so I'm guessing the other base addresses the triage found may correspond to the other apps' address spaces. The app that communicates with the SEPKeyStore is called sks (see slide 86 of the presentation). Not a lot of information, but enough to start reverse engineering!

Looking at strings, it looks like the architecture of apps running inside the SEP hasn't changed much since 2016. The SEPKeyStore-related app is still called sks:

The SEP has almost no debug strings, making it tougher to reverse engineer. Here is what the initialization function for the SEPKeyStore looks like after some manual annotations ("sth" stands for "something" – I didn't go too deep into understanding the specifics here):

Within its main function, we can find multiple other functions executed before a service workloop starts. However, there's plenty of code. How do we focus on things that are related to the inactivity reboot?

Let's recall that we're looking for something that resembles 72 hours. In the kernel, times are usually measured in seconds or in microseconds. For example 72 hours are 259200 seconds (0x3f480). But looking for this value (or for 259200000000, in microseconds, or any other sensible units) in the binary won't return any matches.

Using the compiler explorer, we can see why: Optimizations...

Rather than looking the full time in bytes in reverse byte order, we're looking for assembly instructions that load parts of the timespan into a register.

Binary Ninja knows how to reverse this optimization, and allows us to search in its intermediate representations, instead of looking for raw bytes. In our case, we know that we're looking for a constant.

We find only two matches:

And here it is – a function that compares various times, including 3 days, which is related to the sks application's main function. The result of this time comparison is used to create a message, which is likely sent to the SEPKeyStore kernel extension. Creating a new enum makes it more readable:

enum times : uint32_t

{

_3_days = 0x3f480,

_2_days = 0x2a301,

_1_days = 0x15181,

`_2.5h` = 0xe11

};

This function is used in a context to initialize a struct, which is likely a message being sent from the SEP to the kernel extension.

I didn't end up reverse engineering much more of the SEP, but this seems to confirm that it's really the SEP that keeps track of how long the phone hasn't been unlocked. This design makes sense to me, since the SEP is involved in every unlock, and is also hardened against tampering, even if an exploit against the main kernel is used, so it's a good place to anchor a mitigation like this.

## A Mitigation Only Against Cops?

## While the media coverage so far framed this mitigation as primarily targeting law enforcement, it also a huge security improvement against theft. Outdated law enforcement equipment often finds its way to eBay and other similar platforms for rather cheap price tags. However, thieves won't have the financial and legal means to obtain up-to-date exploits to unlock iPhones within 3 days of getting them. That's another reason why it's important to keep your device updated!On the other hand, law enforcement can and will have to adjust their process, and act faster than before. The first forensic tooling companies already announced that they're able to coordinate these steps within 24 hours! (Note that this also indicates that they only have exploits for AFU state... 🤡)

## Key Takeaways

This feature is not at all related to wireless activity. The law enforcement document's conclusion that the reboot is due to phones wirelessly communicating with each other is implausible. The older iPhones before iOS 18 likely rebooted due to another reason, such as a software bug.

The time measurement and triggering of the reboot is in the SEP, which communicates with the SEPKeyStore kernel extension to perform the reboot. It is likely that using an external time source provided over the Internet or cellular networks to tamper with timekeeping will not influence the 3-day timer.

Security-wise, this is a very powerful mitigation. An attacker must have kernel code execution to prevent an inactivity reboot. This means that a forensic analyst might be able to delay the reboot for the actual data extraction, but the initial exploit must be run within the first three days.

Inactivity reboot will change the threat landscape for both thieves and forensic analysts, but asymmetrically so: while law enforcement is under more time pressure, it likely completely locks out criminals from accessing your data to get into your bank accounts and other valuable information stored on your iPhone.

Interested in reverse engineering? Follow me on YouTube and BlueSky for updates.


