---
type: link
source: notion
url: https://ionic.io/blog/ionic-8-is-here
notion_type: Tech Announcement
tags: ['Running']
created: 2024-04-17T22:54:00.000Z
---

# Ionic 8 is here! - Ionic Blog

## AI Summary (from Notion)
- Release Announcement: Ionic 8 launched after several betas and community feedback.
- Key Enhancements:
- Improved theming and accessibility features.
- Revised iOS designs.
- Introduction of a new Picker experience and password toggle component.
- Web Accessibility:
- Compliance with WCAG for mobile applications.
- New AA and AAA color contrast palettes for improved readability.
- Step color tokens introduced for better control of text colors.
- Built-in Palettes:
- Light and dark palettes are now included by default, simplifying implementation.
- Updated iOS 17 Design Specs: Adjustments made to match the latest iOS design specifications.
- New Component: Introduction of ion-input-password-toggle for password visibility control.
- Migration Process: Designed for minimal disruptions with many breaking changes not requiring code updates.
- Developer Resources: Guides available for migration and app creation.
- Community Support: Acknowledgement of community contributions and feedback during the beta phase.
- Future Outlook: More enhancements expected in 2024.

## Content (from Notion)

Today, we’re excited to announce the release of Ionic 8! This stable release comes after several betas and release candidates with improvements suggested by the Ionic community. Thanks to your contributions and the hard work of our team, we’re thrilled to launch Ionic 8.

What’s new? Enhancements to theming, accessibility, revised iOS designs, a new Picker experience, and a new password toggle component. For complete details and demos, please see the Ionic 8 beta announcement.

Let’s get into what’s new. 👇

## Web Accessibility Out-of-the-box

To help developers build accessible apps, Ionic UI components follow the Web Content Accessibility Guidelines (WCAG) pertaining to mobile applications. Two major accessibility features are included with Ionic 8.

### AA Color Contrast

To improve color contrast, we’ve shipped a revised color palette. When used with a proper contrast color, each color token (primary, secondary, success, etc.) now meets AA contrast levels as defined by the WCAG. This increases readability in your Ionic application, as users can more easily distinguish the foreground from the background. To showcase these new colors, we’ve updated the Color Generator.

### AAA High Contrast Palette

The revised color palette ensures AA level compliance for color contrast. For scenarios requiring even higher levels of color contrast, we are pleased to introduce the new high contrast light and dark palettes! With these palettes, each color token now meets AAA contrast levels for text when used with a proper contrast color.

We are also introducing a new set of step color tokens to support the high-contrast palette better. These step colors allow developers to control text colors independently of background colors.

Check out the new High Contrast Documentation and the Stepped Color Documentation for more information.

## Built-in Light and Dark Palettes

Ionic 8 now ships both the light and dark palettes built into the project. For added convenience, the light palette is automatically imported via the core.css file. Importing the dark theme is as simple as importing a single CSS file:

```plain text
import '@ionic/react/css/palette/dark.system.css';
```

In Ionic 7 and earlier, developers added light and dark palettes by manually copying and pasting design tokens into their applications. However, as Ionic evolved, we discovered that this solution was difficult for developers to maintain and challenging for us to scale.

The above stylesheet will apply the dark palette based on the system settings for a user’s preferred color scheme. With this approach, developers will always receive the latest and greatest light and dark palettes whenever they update Ionic. Additionally, developers can continue to customize our palettes! Learn how to apply the dark palette stylesheet.

## Updated iOS 17 Design Specs

iOS 17 design specifications have evolved since iOS 17 was first released, so we’ve updated Ionic components to match them. Most of these changes are fairly subtle, but one notable feature is the ability to disable Action Sheet buttons. Previously, all buttons in an Action Sheet were always enabled. We’ve also added this behavior to the Material Design variant of the Action Sheet so users can have a consistent experience across platforms.

## New Picker Experience

The new Datetime component, introduced in Ionic 6, included a new inline Picker. After a successful pilot period, this new experience is now available to all developers. Check out the Picker documentation for examples of all the great things you can do with this component.

## Spotted: A New Component?

We added a new component to Ionic 8 during the beta period! The ion-input-password-toggle component allows users to toggle text visibility in a password input.

Learn how to add it to your app.

## Easy Migration Process

It wouldn’t be Ionic without an easy migration process. We know how disruptive breaking changes can be, so we have kept them to a minimum in Ionic 8. In fact, many of the breaking changes do not require any code updates by developers.

## Upgrade to Ionic 8 Now

Developers can follow the Ionic 8 Migration Guide to update their existing Ionic 7 apps.

Looking to start with a brand new Ionic 8 app? Try our app creation wizard!

Please report any issues you encounter on our GitHub repo.

Ionic 8 is another huge step forward for Ionic applications with great enhancements to theming, accessibility, revised iOS designs, and the new Picker experience. We’d like to thank the community for their continued support of this project and feedback during the beta process. Stay tuned for more great improvements in 2024!


