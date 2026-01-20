---
type: link
source: notion
url: https://kau.sh/blog/how-to-firefox/
notion_type: Software Repo
tags: ['Running']
created: 2025-07-22T13:33:00.000Z
---

# 🦊 How to Firefox - Kaushik Gopal's Website

## Overview (from Notion)
- Firefox is a strong alternative to Chrome, especially as ad-blocking capabilities are being hampered in mainstream browsers. This might resonate with your desire for a cleaner browsing experience, free of distractions.
- The open-source nature of Firefox allows for transparency and customization, appealing to your technical background. You can tinker and even contribute to the browser if you choose.
- The emphasis on privacy with features like Total Cookie Protection aligns with modern concerns about data security, particularly relevant in a tech-savvy environment like NYC.
- The ability to use extensions on mobile devices means you can maintain productivity on the go, which is essential for a busy lifestyle balancing family and work.
- Consider exploring features that enhance browsing efficiency, like Containers, which can help manage multiple online identities—useful for both personal and professional accounts.
- Unique add-ons like Dark Reader and Return YouTube Dislike can enhance your browsing aesthetics and functionality, making your online experience more enjoyable.
- An alternate view might be the argument that Firefox lacks the polish and user experience of Chrome or Safari, which can be a consideration if you're looking for seamless integration across devices.

## AI Summary (from Notion)
Firefox is a powerful, open-source browser that excels in privacy and customization, making it a strong alternative to Chrome, especially after recent changes affecting ad-blockers. Key features include seamless syncing for Android users, real browser extensions, and advanced privacy tools like Total Cookie Protection and Containers for managing multiple identities. Essential add-ons like uBlock Origin enhance browsing by blocking ads and trackers, while additional customizations improve user experience.

## Content (from Notion)

Chrome finally pulled the trigger on the web’s best ad-blocker, uBlock Origin.

Now that Chrome has hobbled uBO, Firefox—my beloved—1 is surging again. I want to do my part to convince you to switch to Firefox and show you how I use it.

Let’s get through the important talking points, in case you need a quick copy paste to convince a friend.

1. 100% open-source
1. Un-enshittify the web
1. Android users rejoice
1. Customize to your heart’s content
This section can be quick.

Here’s a github link to the source code of the Firefox browser. You can clone the repo, pop open your favorite AI code assistant and start asking questions about your browser - the most important app you use.

What libraries does their Android app use? libs.versions.toml boom! Also 8.11.1 on android gradle plugin? not bad Firefox.

Their license allows you to fork and distribute alternative versions. Vibe code a whole new browser.

## Un-enshittify the web

Most of the web today is enshittified with a cesspool of ads, popups, cookie notices, and tracking scripts. Our primary defense has been ad-blockers, with the most powerful being uBlock Origin.

uBO relies on community-curated filter lists that play a cat-and-mouse game to zap known ads, trackers, and other digital sludge. But with Chrome controlling the web, Google followed through on its promise to kneecap uBO with Manifest V3, effectively blocking the full version from its extension store.

Sure, there’s uBlock Origin “Lite” now, which does the same thing, right? Nope:

- Filter lists update only when the extension updates 
- No custom filters 
- Many filters are dropped at conversion time due to MV3’s limited filter syntax
- No strict-blocked pages
- No per-site switches
- No dynamic filtering
- No importing external lists
Did you know, uBlock Origin works best on Firefox. Why not just use the real thing then? My browsing experience is beautiful because I have most of the shit-bits blocked away.

On my Pixel too.

## Android users rejoice

With Firefox for Android, you get seamless sync of tabs, bookmarks, passwords between browser and phone2. Let’s face it, Safari between Mac and iPhone is a sublime experience. We can get that with Firefox.

### Real browser extensions for mobile

Here’s something the iPhone isn’t getting anytime soon: honest-to-god browser extensions that you use on your desktop, also on your phone. Which means… you can run uBlock Origin on Android, completely unnerfed.

Safari has extensions, but they still require an App Store review for distribution on Apple platforms. They also just got a version of the uBO “Lite” extension.

## Customize to your heart’s content

But… Firefox doesn’t look as clean and minimal as Safari. You can claw the vertical tabs out of my cold dead Arc hands!

This is what my Firefox browser looks like:

It only takes about five minutes and a browser restart to get this look.

I’ll walk you through my setup now, from essential add-ons to privacy tweaks and a few “nice-to-have” extras.

This is my setup. I’m a nerd, so I find joy in tinkering. You don’t need to do all of this, but a few small tweaks can give you a massively better browser.

## The Essentials: uBlock Origin

Think of uBO as a powerful, wide-spectrum filter for the web. It uses community-maintained lists to block ads, trackers, cookie notices, and other digital sludge before it ever loads. Your browser stays faster and cleaner.

It can be confusing to know which filter lists to enable. I follow the advice of a uBO wizard on Reddit, and these settings alone make the web 90% better. Check the same boxes, and you’re good to go.

You're completely set with this.

For the truly privacy-conscious, uBO can block all outgoing traffic to specific domains, like Facebook.3 In the past, Firefox’s Facebook Container add-on helped by isolating your Facebook activity. But if any other site embedded a Facebook widget or tracker, your data could still leak to Meta’s servers, fingerprinting you even if you never visit Facebook directly.

With a custom uBO rule, you can sever that connection entirely from non-Facebook sites. This is a level of control other browsers don’t offer.

The other line you see there? That one-liner blocks all those “Sign in with Google?” pop-ups. This granular control is only possible with the full uBlock Origin, not the “Lite” version found on other browsers.

If you want to go deeper, this video is a great showcase of its advanced capabilities.

## Privacy power-up: Containers

Firefox now includes Total Cookie Protection by default. This automatically isolates cookies to the site that created them, giving each site its own “cookie jar”. This stops trackers from following you across the web.

This feature makes the old Multi-Account Containers (MAC) add-on redundant for basic anti-tracking. However, the container technology itself is still incredibly useful for managing multiple online identities.

Instead of juggling separate browser profiles, you can use “Containers” to stay logged into two different Gmail accounts (e.g., “Work” and “Personal”) in the same browser window, with zero overlap.

The old MAC add-on made this possible, but it was clunky to setup. For a seamless setup, you just need one about:config tweak: set privacy.userContext.newTabContainerOnLeftClick.enabled to true. Now, when you click the new tab button, you can choose which container to open. This works without the extra MAC add-on because the Container concept is baked natively into Firefox.

But what about links? A work link (like Datadog or Sentry) clicked from your email in a Work container, might open in the default container and use the wrong Google account. You could right click and say “Open in Container >” but that gets old fast. The optional Containerise add-on solves this by letting you create simple rules that force specific sites to always open in their designated container.

This combination of a native config tweak and the Containerise add-on provides a simple, but more powerful multi-profile setup (than even MAC).

## Gravy add-ons

These are also not essential, but they add a nice layer of polish.

- Dark Reader: For a consistent, customizable dark mode on every site.
- Stylus: To apply custom CSS. I use it to force my favorite monospace font on code blocks.
- Return YouTube Dislike: Does what it says on the tin.
- Obsidian Web Clipper: To save notes and clippings directly to Obsidian, from desktop or mobile.
- Auto Tab Discard: Suspends background tabs to save RAM. A holdover from my RAM-strapped MacBook days, but it still does its job silently.
## Other Customizations

Firefox is famously customizable via about:config. Besides the container tweak, I only use one other:

### browser.tabs.insertAfterCurrent → true

- New tabs open next to your current tab, not at the end.
I’m collecting in this section, some of the cooler Firefox features that’ll make you wonder why every browser doesn’t have them:

- Type / and start typing for quick find (vs ⌘F). But dig this, ' and Firefox will only match text for hyper links
- If you have an obnoxious site disable right click, just hold Shift and Firefox will bypass and show it to you. No add-one required.
- URL bar search shortcuts:  for bookmarks, % for open tabs, ^ for history
The web can still be beautiful. You just need the right tools to see it. Go download Firefox and make your web beautiful again.

If you try this setup or have suggestion, let me know in the comments.


