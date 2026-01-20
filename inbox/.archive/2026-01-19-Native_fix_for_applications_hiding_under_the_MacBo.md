---
type: link
source: notion
url: https://flaky.build/native-fix-for-applications-hiding-under-the-macbook-pro-notch
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-02-12T16:13:00.000Z
---

# Native fix for applications hiding under the MacBook Pro notch

## AI Summary (from Notion)
- Issue: New MacBook Pro models have a notch that hides menu bar icons when multiple apps are open.
- Common Solution: Many recommend purchasing Bartender, a paid application, to manage menu bar icons.
- Native Solution: A free, native macOS solution exists that adjusts the menu bar settings without extra software.
- Command Line Adjustment: Users can modify menu bar whitespace settings using Terminal commands to fit more icons:
- Commands to change padding and spacing allow customization from 0 to 6.
- Reverting Changes: Users can revert to original settings with simple commands, ensuring flexibility.
- Takeaway: This solution enhances usability without additional costs, highlighting a workaround for Apple's design oversight.

## Content (from Notion)

TL;DR: You can adjust MacOS whitespace settings from the command line to display more application icons in the top right section of the menu bar.

## Hidden Apps Beneath the 14” and 16” MacBook Pro Notch

A frustrating aspect of the new MacBook Pro models is the notch. The notch itself isn't the problem; rather, it's that Apple hasn't automatically adjusted the menu bar icons so they don't hide behind the notch when many apps are running.

My colleagues often suggest purchasing Bartender for about 20€ to solve this issue. While it offers many features, I've refused to pay for a solution to Apple's poor design decision. Recently, I discovered a free, native macOS solution that doesn't require installing Bartender or any other additional apps. See the results in the images below:

With the default settings, the MacBook top menu bar can only accommodate 13 different apps.

After adjusting the whitespace settings, it can fit several more.

### Adjusting the Menu Bar Whitespace Settings from the Command Line

You can modify the default padding and spacing in the Menu bar by opening Terminal.app and executing the following commands:

```plain text
# Change the whitespace settings value
defaults -currentHost write -globalDomain NSStatusItemSelectionPadding -int 6
defaults -currentHost write -globalDomain NSStatusItemSpacing -int 6

# After running these commands, you need to log out and log back in
```

You can adjust the values from 0 to 6 to accommodate even more icons. Personally, I found 6 to be a good fit.

### Reverting to the Original Values

If you're unhappy with the results, you can delete the settings by executing the following commands:

```plain text
# Revert to the original values
defaults -currentHost delete -globalDomain NSStatusItemSelectionPadding
defaults -currentHost delete -globalDomain NSStatusItemSpacing

# After running these commands, you need to log out and log back in
```

### Sources

I first learned about these settings in this answer on the Apple-themed Stack Exchange, Ask Different:


