---
type: link
source: notion
url: https://ionic.io/blog/announcing-ionic-8-4
notion_type: Tech Announcement
tags: ['Running']
created: 2024-11-20T17:45:00.000Z
---

# Announcing Ionic 8.4 - Ionic Blog

## Overview (from Notion)
- Ionic 8.4 introduces flexible components like the Modal interface for Select menus, enhancing user interactions and making your apps more intuitive.
- The new swipeable Segment content allows for fluid navigation, making it easier to create engaging user experiences—ideal for apps catering to busy parents.
- Improved accessibility features mean your applications can be more inclusive, ensuring usability for everyone, including those with disabilities.
- The robust handling of menu events adds more control over user interactions, allowing for a seamless experience in apps where quick access is key.
- As a founder, leveraging these updates can keep your products competitive and in tune with modern development practices, ensuring you meet user expectations.
- Consider exploring the impact of these features on user retention—how can a smoother interface keep users engaged longer?
- In a fast-paced city like New York, optimizing app performance to cater to on-the-go users can lead to significant advantages in your market.
- Alternative views might suggest focusing on niche markets or specific user needs rather than broad updates—how might you prioritize features based on your audience?

## AI Summary (from Notion)
Ionic 8.4 introduces significant updates, including a Modal interface for the Select component, new swipeable Segment content, and enhanced menu event data for better interaction tracking. Accessibility improvements have been made to the Alert component, ensuring better compatibility with screen readers. Additional updates include improved input support, bug fixes in Vue navigation, and standalone functionality for Tabs in Vue and React, all aimed at enhancing developer experience and usability.

## Content (from Notion)

We are thrilled to introduce Ionic 8.4, packed with exciting updates to core components like Alert, Select, and Segment, as well as accessibility enhancements and developer experience improvements. This release adds two new components and enhanced functionality to improve usability and deliver a smoother experience across the board.

Here’s what’s new 👇

## Select Modal Interface

Ionic 8.4 now supports a Modal interface with the Select component, adding flexibility to how users interact with Select menus.

Previously, Select could only use the Alert, Action Sheet, or Popover interface. With this update, the Modal interface offers a fresh option for displaying Selects.

By default, the Modal appears full-screen on mobile devices and as an inset view on tablets and desktop views. Developers can further customize the Modal’s appearance using the interfaceOptions property to present it as a card or sheet modal.

See the Select documentation for more information.

## Swipeable Segment Content

This release also introduces Segment View and Segment Content, two new components that seamlessly integrate with the Segment component to enable swipeable content.

These additions make it easier than ever to build tab-like experiences with fluid, responsive transitions. To navigate between Segments, users can swipe left or right within the content area, or they can click on the individual Segment Button to see its related content.

See the Segment documentation for more information.

## Menu Event Data

Handling menu events has become more robust with additional role data emitted in the ionWillClose and ionDidClose events. This role property helps developers identify how a menu was closed:

- When closed by clicking the backdrop or pressing the esc key, the role will be 'backdrop'.
- If closed by a drag gesture, the role will be 'gesture'.
- When closed using a button inside the menu or any other way, the role will be undefined.
This additional context enhances flexibility when handling menu interactions.

## Alert Accessibility

Accessibility continues to be a top priority in Ionic. In version 8.4, we’ve updated the heading structure within the Alert component for improved screen reader compatibility.

- The header continues to renders as an <h2> element.
- If header is undefined, the subHeader will render as an <h2>.
- When both header and subHeader are defined, header renders as an <h2>, and subHeader renders as an <h3>.
These adjustments ensure that the heading hierarchy remains logical and accessible for users relying on assistive technologies.

## Other Improvements

Ionic 8.4 includes a range of additional updates from previous versions that enhance accessibility, developer experience, and functionality:

- Accessibility Improvements: Inputs and overlays now offer improved screen reader support, including announcing helper and error text for inputs and resolving issues with aria-hidden on backdrops used by overlays.
- Bug Fixes: A navigation issue in Vue where the wrong view was rendered when using router.go has been resolved. Thank you to bentleyo and xxllxhdj for their work on this!
- Tabs Updates: Tabs and Tab Bar components now function as standalone components in Vue and React, eliminating the dependency on the router for simpler integration.
We’re continuing our mission to provide a fast, accessible, and developer-friendly framework that evolves with your needs. We can’t wait to see how you use these new features in your apps!


