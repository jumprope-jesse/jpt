---
type: link
source: notion
url: https://blog.bymitch.com/posts/reject-cookies/
notion_type: Software Repo
tags: ['Running']
created: 2025-04-29T13:56:00.000Z
---

# Reject Cookies - The Pickwick Protocols

## Overview (from Notion)
- Privacy Concerns: As a software engineer, you're likely aware of the increasing scrutiny on data privacy. The extension addresses the annoyance of cookie consent banners while promoting user privacy, aligning with a growing demand for ethical tech solutions.

- User Experience: The frustration with cookie consent banners is universal. This tool enhances user experience by simplifying interactions with websites, which could resonate with your own experiences navigating online platforms.

- Regulatory Awareness: Understanding GDPR and its implications is crucial. This extension not only complies with regulations but also empowers users to take control over their online presence.

- Open Source Approach: The code being open source offers an opportunity for collaboration and innovation. As a founder, you might appreciate the community-driven aspect of software development and the potential for contributing to or improving the project.

- Market Gap: There's a unique position in the market for tools that reject non-essential cookies, differentiating from existing solutions that auto-accept. This could inspire new ideas or projects in your own work.

- Future of Extensions: The project could lead to broader discussions about the role of browser extensions in shaping web interactions, encouraging you to consider how your own products might enhance user experience in similar ways.

- Parenting Perspective: As a parent, the concept of digital literacy and teaching your children about online privacy and consent is increasingly important. This extension could serve as a talking point about responsible internet usage.

## AI Summary (from Notion)
A Chrome extension called "Reject Cookies" aims to automatically reject non-essential cookie consent pop-ups, enhancing user experience by reducing the frustration of cookie banners. It utilizes targeted selectors for various consent vendors and is open source, inviting user feedback and contributions for improvement.

## Content (from Notion)

Add the extension

## A Chrome Extension

Everyone can agree that cookie consent banners are frustrating. It might be one of the few unifying factors on the internet today. Even though it’s a couple clicks, the couple clicks are a pain, and the couple clicks can happen on many sites each day.

There are browser extensions out there that will auto-accept cookies like I don’t care about cookies and it’s open source fork I still don’t care about cookies. You can even chain this extension with another that will auto-clean up your cookies. This is an adequate solution and ascribes to unix philosophy.

Additionally, there are extensions like uBlock Origin with additional filters to help ignore these annoying pop ups. Or Privacy Badger to block cookie trackers. Although there is space to provide an extension that just auto-rejects non essential cookies.

That’s what led to the “Reject Cookies” chrome extension. It will first attempt to reject the cookies on the page. If that is unsuccessful, it will then attempt to close the cookie pop up or banner. To comply with the regulations governing cookies under the GDPR and the ePrivacy Directive you must

> 

So the omission of an acceptance should be on par with an explicit rejection. If you’re interested in how it works the code is open source and on github, but let’s step through it at a high level.

## How it’s implemented

Vibe coding is the answer. I leveraged Cursor and let it auto-select the model. This combination while extremely useful, did not serve me as well as recent past experience. On the project setup front, I had not previously written a Chrome extension. Having the Cursor agent set up the boilerplate was convenient. Although, it requested too liberal of permissions in the permissions to start and wouldn’t go and update them as the design of the app changed. Below is a snippet of the manifest.json to show what the permissions ended up looking like.

```plain text
{
  "permissions": ["activeTab", "sidePanel", "tabs"],
  "content_scripts": [
    {
      "matches": ["http://*/*", "https://*/*"],
      "js": ["content.js"]
    }
  ]
}

```

Next on the implementation side of things, it started with a set of common selectors that could possibly be relevant to non-essential cookies. The problem was once again these selectors were extremely liberal things like elements with the class “accept”. I opted to take a more targeted approach and aim the logic at specific cookie consent vendors that most sites seem to leverage. Cursor’s agent was, as expected, not able to help much with this implementation.

The extension will go through the configured providers.

```plain text
const findAndClickRejectButtons = () => {
	commonCookiePopupChecks.forEach(({ check, rejectOrClose }) => {
	  if (check()) {
		rejectOrClose();
		// assume that there is only one cookie consent provider and we can exit
		return;
	  }
	});
  }

```

A check for a provider will look for a specific element that identifies it.

```plain text
const checkForOneTrust = (): boolean => !!document.getElementById('onetrust-consent-sdk');

```

Then attempt to reject the cookies and fallback to removing the consent banner or popup if it’s not able to reject the non-essential cookies.

```plain text
const closeOrRejectOneTrust = () => {
  const rejectButton = document.getElementById('onetrust-reject-all-handler');
  if (rejectButton) {
    rejectButton.click();
    return true;
  }
  const consentSDK = document.getElementById('onetrust-consent-sdk');
  if (consentSDK) {
    consentSDK.remove();
    return true;
  }
  return false;
};

```

Not much more to it other than that.

## Help it get better

Reject Cookies is still a work in progress. It can use your support to help cover more use cases and report bugs. As mentioned the design targets specific cookie consent implementations from different vendors. There are more vendors out there and different flavors of each vendors implementation. The side panel allows you to report sites where the cookie consent rejection was missed along with a place to report bugs or issues with the extension. The side panel can be accessed by clicking on the chrome extension’s menu in Chrome. You can also feel free to reach out to [email protected] with any feedback.


