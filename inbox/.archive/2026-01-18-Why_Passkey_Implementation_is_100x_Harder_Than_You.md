---
type: link
source: notion
url: https://www.corbado.com/blog/passkey-implementation-pitfalls-misconceptions-unknowns
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-05-03T02:58:00.000Z
---

# Why Passkey Implementation is 100x Harder Than You Think – Misconceptions, Pitfalls and Unknown Unknowns

## AI Summary (from Notion)
- Main Topic: The complexity of implementing passkey authentication, which is more challenging than many developers anticipate.
- Key Misconceptions:
- Passkeys are not simply about calling navigator.credentials.create() or navigator.credentials.get().
- The belief that available passkeys can be detected from the browser is a fallacy.
- User agents are not reliable for device recognition due to privacy measures.
- Implementation Challenges:
- Need for multiple backend API endpoints for passkey creation.
- Requirement for fallbacks if passkeys fail or if the user cancels the process.
- Importance of verifying users to prevent account takeovers.
- Difficulty in detecting passkeys stored on different devices.
- User Experience (UX) Considerations:
- Complexities in passkey management UI, including how to handle deleted passkeys.
- Challenges with conditional UI, which may not always provide a smooth experience.
- Variability in browser behavior complicating the login experience.
- Testing Issues:
- Secure contexts required for all passkey systems, making local testing complex.
- Debugging and performance issues arise as the number of test credentials increases.
- Future of Passkeys:
- Passkeys are expected to become a dominant authentication method as users experience their benefits.
- Companies without passkey capabilities may become outdated as consumer preferences shift.
- Overall Message: While the adoption of passkeys offers significant advantages in security and user experience, the implementation process is intricate and requires careful planning and consideration of various factors.

## Content (from Notion)

Why Passkey Implementation is 100x Harder Than You Think

Implementation

## Read our learnings about passkey implementation challenges, pitfalls and misconceptions we faced while building passkey-first authentication

## Vincent

Created: April 27, 2024

“Ah yes passkeys, pretty cool technology and great that there’s already wide support, plus an open standard that they are built on. I’ll just grab one of the libraries for my framework and that should do the job. I don’t think I need any help or service. I’m a decent coder and have added auth packages dozens of times in the past.”

This is a typical conversation I had over the past 24 months with many developers. And I have to admit, that this was also my initial thought when I encountered passkeys for the first time in May 2022: It shouldn’t be too hard. It shouldn’t be too complicated. Hey, in the end, it’s just another way of doing (passwordless) authentication. And here I am in mid-2024, still discovering new cases you need to take care of in real-life applications. That’s the reality - which fascinates me.

With this blog post, I want to share with you the learnings on my way when working on a passkey-first auth solution with Corbado. All the hard truths, the unknown unknowns (factors that were not anticipated prior to my experience, essentially things we did not know we did not know), and the misconceptions should be uncovered, so that you know what to consider when implementing your own passkey-based authentication.

Whether you're at the initial stages of adoption, considering enhancing your existing systems with passkeys or starting a passkey-first authentication project, this guide will help you avoid common pitfalls.

## TL;DR:

“Can you add passkeys as new auth solution in our next sprint?” asks the product manager, as he’s heard about passkeys as the new passwordless login method that all the big players in the tech industry implement. No more password resets. Higher conversion rates. No more phishing attacks (also a dream of every IT security manager). Everyone is excited for this new way of authentication. Even the developer who has to implement it. Even though he’s read some controversial posts on Hacker News about passkeys, he still thinks it’s a cool concept and from the company’s perspective, it makes a ton of sense to add it as an option (though, no one should be forced to use it, of course, so let the users decide what they want!).

The developer starts his research on passkeys just as he would do for any other new feature that the product team has requested. He opens Google and types in “webauthn specification”, “passkey tutorial”, “how to implement passkeys”, “passkeys in react” and “passkey libraries”. This should be a good start. Skim through the specification to get a rough understanding, scroll through some tutorials and sample projects. Check if there are some libraries on GitHub that can be used. In the end, it will probably all come down to some backend API endpoints that need to be implemented, a quick frontend integration and then just use the session management that is already in place.

However, the more the developer researches the topics, the more things come to his mind: how do passkeys work on devices that are older? What if the user cancels the flow or loses the device where the passkey is stored? How can the new passkey login be tested on different devices, operating systems and browsers. He realizes that this might not be only a 1-sprint-task.

This is not an isolated story. Many developers that reached out to us and scratched below the surface of passkeys faced similar challenges. Implementing passkeys in a real-life project is 100x harder than you might initially think (trust us – we’ve gone through it).

Our mission is to help developers implement passkeys. That’s why we created this blog post. So, let’s take a look at the 15 most common misconceptions when implementing passkeys, so that you know what to take care of.

#1 Creating Passkeys is Just Triggering navigator.credentials.create()

#2 Passkeys Logins are Only About When to Trigger navigator.credentials.get()

#3 Available Passkeys can be Detected from the Browser

#4 User Agents are Great for Device Recognition

#5 An Open Standard like WebAuthn is Easy-to-Read

#6 Passkey Management UI is Easy-to-Build

#7 Passkeys are New but Common Use Cases are Well Supported

#8 Passkey UX/UI is Great and Predefined

#9 Conditional UI Always Ensures a Smooth Login Experience

#10 Passkeys Work in All Browsers as Expected

#11 Passkeys' Availability Equals Accessibility

#12 QR Codes are Simple and Appear only When Needed

#13 Passkeys Are Universal and Thus Easily Testable

#14 Only Adding Passkeys to an Existing Auth Solution is Easy

#15 Please Help Me: I Think I Don't Want Passkeys Anymore

## #1 Creating Passkeys is Just Triggering navigator.credentials.create()

I’ve seen this WebAuthn JavaScript API where I can simply create a new passkey by calling navigator.credentials.create().

Not really! It’s one of biggest misconception that one API call is enough. Even though the WebAuthn JavaScript API (called with navigator.credentials.create()) is the simplest component and most straightforward part of any passkeys project, the real complexities arise before and after this API call. If you want to adopt a passkeys-first approach, you need to consider many more things, such as:

- Implement two backend API endpoints for one simple passkey creation: Developers who have mostly worked with password-based authentication often think that they simply need to call one backend API endpoint, like in the password world, and get a success / failure message returned. However, with WebAuthn you need to call two backend API endpoints with the JavaScript API call from above in between and then receive the response. For new starters, this can be quite complex as the information sent along needs to be in the right order and correctly encoded / formatted.
- Provide fallbacks if passkeys don’t work or the flow is canceled: You need alternative authentication options like email OTP, SMS OTP, social logins or passwords (if you don’t want to fully passwordless yet). They are needed in case the device is not passkey-ready or the user deliberately cancels the passkey registration flow. Then, you need to provide equally comfortable options for signing up.
- Verify the user to avoid account take-overs: Passkeys can also work in usernameless way. However, in real-life applications, you need to verify the user and their login identifier (e.g. email address or phone number) to avoid account take-over attacks. In the worst case, someone could simply create a passkey and use your email address as login identifier (so no verification took place). If the system is designed in such a way that you can use this email address (e.g., through a passkey append flow with an email OTP) to create another passkey on a different device, then an attacker could potentially use the first passkey to log into your account.
- Detect if passkeys are already stored on the device: It's important to know which devices have passkeys stored and which do not (in order to know where passkey creation / logins can be securely offered to users – more on that later). In the passkey creation case, allowing multiple passkeys per account could lead to major user confusion. We call these decision rules “passkey intelligence”, as a logic around passkeys, users and devices needs to be developed.
- Support cross-device registration & hardware security keys: Do you want to allow the creation of a passkey on a different device from the one you are currently using to access the application? Or do you need to support hardware / FIDO2 security keys (e.g. YubiKeys)? If yes, there are some important things to consider for your implementation, that have impact on the PublicKeyCredentialCreationOptions used in navigator.credentials.create(): 
- Adapt the backend & database: Choosing the WebAuthn server (basically a library) is pretty straightforward and so is the installation (e.g. npm install @simplewebauthn/server). But then the real challenge starts: 
- Implement passkey-specific UX: Creating passkeys is great for UX. But that only counts for the creation process itself when the Face ID modal comes up and the user just scans their face as they do countless times during the day. The challenge lies more often before and after this particular ceremony and requires a lot of additional user flows that need to be implemented: 
## #2 Passkeys Logins are Only About When to Trigger navigator.credentials.get()

Okay, there’s some more to creating a passkey but to login with a passkey, I simply call the WebAuthn JavaScript API via navigator.credentials.get(), as the passkey already exists.

Eh nope. It’s the other way around. Outstanding passkey experience during authentication means to figure out when not to start a passkey authentication ceremony in the first place to prevent dead-ends and unnecessary loops. Yes, this can even happen on devices that support passkeys in general if there is no passkey available at this device (see also #3)! Don’t believe us? Then, take a look the following examples:

- Example 1 “Windows 10 or 11 desktop without Bluetooth”: A user signs up and creates a passkey on their iPhone with iOS 17. Then, the users uses their desktop that runs on Windows 11. Although Windows 11 supports passkeys, the computer lacks Bluetooth, which is required for WebAuthn Cross-Device Authentication (CDA) via QR codes (it's a security measure to ensure both devices are in proximity).
- Example 2 “Device-bound passkeys”: Often, workplace computers run on Windows 10 or Windows 11. Passkeys created on these systems are not synced to other devices (-> device-bound passkeys). Attempts to login with a passkey on another device will fail because the user does not have an alternative passkey on a mobile device for CDA.
However, the scenario can also reverse:

- Example 3 “Third-party passkey providers”: Some users might use password managers like 1Password, KeePassXC or Dashlane, which now also store passkeys as third-party passkeys providers across operating systems. If the passkey from example 1 or 2 is stored in one of these password managers, the passkey login should be permitted. Therefore, you need to know where the passkey was created, whether the current device has the password manager installed and active, and if the passkey is synced, to provide a convenient login experience without locking the user out.
To ensure a seamless passkey login experience, it’s essential to be highly certain that the login process will succeed before initiating the passkey login ceremony. This helps avoid false positives (thus, it's necessary to track how often and how a user logs in to influence the decision on which login method to offer), minimizes disruptions, and prevents inefficient authentication loops that could frustrate users and lower conversion rates.

## #3 Available Passkeys can be Detected from the Browser

Okay, I understand that I need to check if a passkey is available before triggering a login. This should be fairly easy with some other browser feature or JavaScript API, right?

Absolutely not. This is a big fallacy – if not the biggest – and it actually causes many of the subsequent fallacies or is related to them. Knowing in advance (before any WebAuthn ceremony starts) whether a passkey is available on a device would be a tremendous help in facilitating the login, as you would then know that there can’t be a mismatch or error in the login process. Without this knowledge, you need to use other factors that help improve the UX and avoid any unexpected failures that disrupt the login experience.

Let’s understand why available passkeys on a device cannot be detected from the browser. Passkeys and the FIDO Alliance, as the driving force behind them, have a strong privacy-by-design mindset. All passkey operations are designed to prevent identification of users and the revealing of any privacy-related data based on their available passkeys. Only after an authentication on the device using fingerprint scanning or Face ID, which is treated like explicitly providing user consent, more information is given. That’s why you can test for passkey-readiness of a device and browser with one of the following methods but it is impossible to directly detect whether a passkey already exists on a specific device prior to any WebAuthn operation:

- Is my device & browser WebAuthn-ready: PublicKeyCredential
- Is my device & browser passkey-ready (platforma-authenticator-ready): PublicKeyCredential.isUserVerifyingPlatformAuthenticatorAvailable()
- Is my device & browser Conditional-UI-ready: PublicKeyCredential.isConditionalMediationAvailable()
## #4 User Agents are Great for Device Recognition

I see that there is no feature to directly detect passkey availability from the browser, so I think I’ll just use the good older user agent to manage devices and passkeys.

Good idea – might just not work as easy, especially not on all browsers! After reading through the first fallacies, you might consider implementing a proper device management system (in this context called passkey intelligence) to detect where passkeys were created and from where the user might try to login with a passkey. Building such a passkey intelligence to detect devices in 2024 is not as easy as it used to be:

- User agents are phased out: A robust user-agent parsing library is essential to accurately detect the operating system, browser, and device type (mobile or desktop) from the user-agent HTTP header. Unfortunately, this method remains fully effective only for Safari. All other browsers are about to phase out the user agent soon (or have already done so).
- Chromium’s user-agent reduction initiative: Chromium-based browsers (e.g. Chrome, Edge) and Firefox have significantly reduced the level of detail in their user-agent strings as part of their user-agent reduction initiative (primarily to avoid tracking and protect user privacy). To effectively recognize devices using Chrome, Edge or Firefox, the usage of client hints (e.g. via navigator.userAgentData.getHighEntropyValues()) is necessary. This JavaScript API is used for the precise distinction between operating systems and browsers (+ corresponding versions). Note that Safari does not support this API, and also that client hints cannot be retrieved via HTTP headers out-of-the-box.
Consequently, to provide passkey intelligence for all browsers, you need to support both methods (user agent & client hint parsing). Implementing these APIs in your passkey intelligence is a lot of work and don’t forget: devices and browsers update continuously. That’s why you need passkey intelligence that supports updates for operating systems and browsers.

## #5 An Open Standard like WebAuthn is Easy-to-Read

The WebAuthn specification should facilitate the use of secure and simple authentication. Therefore, it will be probably easy-to-read and understandable.

Nope – unless you are an expert authentication or have a PhD in cyber security. Cryptographic protocols and authentication standards are difficult to read and understand. And so is WebAuthn. There are a lot of complexities to be understood, when you want to implement passkeys / WebAuthn. You’ll need a lot of know-how that is not part of the WebAuthn standard. How come? To answer this question, you need to understand the different WebAuthn Levels, especially from a chronological perspective and that the older ones were written in a time where hardware security keys were the primary method for WebAuthn (and not platform authenticators like Face ID or Windows Hello):

- WebAuthn Level 2 (current version; since April 2021): Passkeys were initially not included in this released version, as the term 'passkeys' and the sync feature were introduced in 2022. There is significant industry effort, especially by the FIDO Alliance, to make the WebAuthn standard in general more passkey-like. As a result, many features have been incorporated into the draft of WebAuthn Level 3, which has not yet been released. But passkeys are already available today, so the WebAuthn level 2 is still the official version. This add complexity (especially as some aspects are no longer in the passkey-era or are redundant, e.g. requireResidentKey vs. residentKey or recommendations regarding the usage of attestation).
- WebAuthn Level 3 (expected from the end of 2024 onwards): The WebAuthn Level 3 standard is supported by a wide range of industry players. When the Web Authentication Working Group agrees on a new feature and organizations like Google, Apple, Microsoft, and Mozilla implement this feature in their browsers, it immediately becomes the de facto standard. Usually, the market pressure is significant when Apple (with Safari, iOS, and macOS) and Google (with Chrome and Android) implement the feature, as they control the majority of the desktop and mobile browser market, along with their respective operating systems.
To stay up-to-date with the WebAuthn standard and keep pace with the passkey usability of larger platforms (e.g., Android, iOS, macOS, Windows), it is necessary to monitor a variety of input sources besides the existing (and continuously updated) WebAuthn spec:

- Follow the WebAuthn GitHub issues to anticipate new passkey / WebAuthn features early on and understand why they might or might not be introduced.
- Regularly take a look at WebAuthn Level 3: Editor's draft commits to see how the standard changes
- Check Chromium feature requests and releases to test new features and adapt your auth solution accordingly
- Review Mozilla & Webkit issues to test new features and understand browser behavior
As the passkey / WebAuthn ecosystem is highly heterogeneous, the standard is interpreted and implemented differently. Therefore, depending on the WebAuthn server library used, you need to handle various WebAuthn levels in your ceremonies. Since new passkeys are continuously being developed, it’s almost certain that there will be new changes in the future, which will further complicate matters. To feel this heterogeneity and complexity yourself, feel free to research the following topics in the context of WebAuthn and check the corresponding discussions:

- Passkeys themselves (especially the sync feature)
- Conditional UI
- supplementalPubKeys
- PublicKeyCredentialHints (to deprecate AuthenticatorAttachment)
## #6 Passkey Management UI is Easy-to-Build

Building a passkey management UI and the corresponding functionality to create, edit and delete passkeys should be rather simple.

Yes and no – while building a passkey management UI isn’t too hard there are some things which are rather counter-intuitive. Industry best practice for managing passkeys is to list all available passkeys for a user in the account settings. Thanks to resources like https://passkeys.dev, having access to a comprehensive list of passkey providers with logos and names is straightforward. It can be used to display passkey-provider-specific information for a passkey. However, managing passkeys involves more:

- Exclude credentials when adding passkeys: When offering an “Add passkey” button in the account settings, the excludeCredentials PublicKeyCredentialRequestOption property must be used correctly to prevent mismatches between the user's passkeys on the client-side on their device and those stored server-side in the backend.
- Deleting passkeys server-side could lead to confusion: Deleting a passkey in the account settings (server-side) is more complex. A good UI typically includes a delete button for each listed passkey. When a passkey is deleted server-side, it remains on the client-side (on the device). The user might still attempt to log in with it, which is problematic. The passkey should be flagged as deleted on the server-side. Additionally, to prevent future confusion, the AllowCredentials list of the PublicKeyCredentialRequestOptions in the authentication ceremony should not be left blank if a passkey was deleted server-side. Instead, AllowCredentials should be filled with all passkeys except the deleted ones. Implementing such a logic requires intelligent passkey management on the server-side.
In general, we have often received questions about whether the AllowCredentials list should be left empty or filled with credentials. The answer depends on the specific security and operational needs:

- Empty AllowCredentials: This approach avoids credential enumeration, reducing the risk of exposing user information to attackers. It also maximizes the available options for the user, as it allows any stored credential to be used for authentication.
- Filled AllowCredentials: Filling the AllowCredentials list with credentials enables the backend to filter out deleted passkeys. This is especially useful in scenarios where the user identifier is known when the WebAuthn login ceremony starts (thus not possible in usernameless login scenarios). This allows the system to list only those passkeys that match this identifier and are not deleted. This targeted approach enhances security by restricting the authentication process to specific credentials.
As you see, there is no clear answer to this question and you need to decide based on your specific requirements.

## #7 Passkeys are New but Common Use Cases are Well Supported

Even though passkeys are new, they are backed by some of the most UX-oriented companies, so the most common use cases for supporting passkey authentication should be well supported.

Yes, passkeys are a relatively new technology, and while they effectively support the most important use cases, particularly the plain sign-up and login process, and rise in adoption, they fall short on other common real-life cases:

-  
- 
- Use Case 3: Change passkey-associated meta data: When a passkey is created, the following meta data is associated with the passkey and stored on the client: 
user.name, user.displayName, user.id, response.userHandle, and Credential ID can be major sources of confusion and errors if not thoroughly understood in the beginning of your passkey implementation.

While these three use cases may be less relevant for smaller user bases, they become increasingly common as the user base grows, particularly where unused passkeys pose challenges for passkey intelligence operations (see #2 and #12).

## #8 Passkey UX/UI is Great and Predefined

Okay I get it: developing passkey authentication is technically complex, but once it's implemented, the process becomes quite straightforward, right?

- Passkey icon: The good news is the FIDO alliance has created an icon for you.
- Product management decisions: As in any other project, where UX plays an important role (and authentication is probably one the most crucial ones in regard to UX), the product management team wants to provide a significant input. The most common questions from a product management perspective are:
- Which devices to support?: What kind of devices can we expect among our users? How high will the coverage of passkey-ready devices be? To answer these questions, we recommend any organization to start analyzing the passkey-readiness of their user base’s devices prior to any passkey launch. 
- UX/UI best practices: To provide a really appealing passkey UX/UI, a few more things need to be considered before the rollout: 
In conclusion, while passkeys are technically complex to implement, do not underestimate the effort required to address various product management aspects.

## #9 Conditional UI Always Ensures a Smooth Login Experience

I love Conditional UI as it’s the most seamless login I’ve ever seen. I don’t even need to provide a username anymore and it works so smoothly on supported devices.

Indeed, Conditional UI provides one of the smoothest login experiences. There are however some things to consider or even improve on top. In general, one of the best things about passkeys is that the user does not need to explicitly come up and memorize passwords anymore. Passkeys are automatically saved by the operating system (or by a third party passkey provider like 1Password, KeePassXC or Dashlane) from where they can be used in any future login attempt. Generally, with passkeys, there are three modes to log in:

-  
Regular Passkey Login

Regular passkey login

Regular Passkey Login Email Input

Regular passkey login with filled email address

Regular Passkey Login Authenticator

Connect to the authenticator for login

-  
Passkey Login Button

- Conditional UI Login: Conditional UI, also known as usernameless login, behaves differently depending on the operating system. For example, Safari on iOS might display a modal suggesting the last used passkey, while Chrome on Windows shows a dropdown of all available passkeys for immediate login. These dropdowns are initiated with the navigator.credentials.get() call, using the ‘mediation: “conditional”’ flag:
```plain text
// Availability of `window.PublicKeyCredential` means WebAuthn is usable.
if (
  window.PublicKeyCredential &&
  PublicKeyCredential.isConditionalMediationAvailable
) {
// Check if conditional mediation is available.
const isCMA = await PublicKeyCredential.isConditionalMediationAvailable();
if (isCMA) {
// Call WebAuthn authentication
const publicKeyCredentialRequestOptions = {
// Server generated challenge
      challenge: ****,
// The same RP ID as used during registration
      rpId: "example.com",
    };

const credential = await navigator.credentials.get({
      publicKey: publicKeyCredentialRequestOptions,
      signal: abortController.signal,
// Specify 'conditional' to activate conditional UI
      mediation: "conditional",
    });
  }
}

```

In the source-code sample above, no username is transmitted initially. The WebAuthn server simply creates a challenge. If the user selects an account from the Conditional UI list, the browser signs the challenge. The assertion includes the user.id (as response.userHandle) and the private key is used to sign the challenge. The backend then verifies the challenge and logs in to the correct account.

Well, seeing these different login options sounds very promising so far, but there are some caveats. From our user testing and funnel analysis of passkeys, we've observed that passkey modals / popups sometimes interfere with user interactions. Users might abort the automatically initiated modals / popups, and moreover, Conditional UI is not supported on all platforms. Therefore, we recommend leveraging LocalStorage information to optimize the passkey login experience:

- Store recently used passkey hints in LocalStorage: Storing information about recently used passkeys (e.g. credential IDs and login identifier) can help to optimize user experience. This information can also be leveraged as input to the passkey intelligence (further improving: #2, #11, #12). Users can log in to a 'recently accessed' account with a single click, bypassing dropdowns or modals. If the user wishes to access a different account, the UI then switches to Conditional UI.
Passkey Login Client Hint

The information displayed can be increasingly precise: For example, if a mobile device was used for Cross-Device Authentication, this detail could be included in the message to guide the user to the correct device.

## #10 Passkeys Work in All Browsers as Expected

As passkeys are supported by all major browsers, the behavior and UX should be the same everywhere.

Well no. In general, for passkeys to work, there are two different things to consider:

1. Available passkeys on the login device: The operating system and the browser must support passkeys (moreover the different versions of operating system and browser play an important role). This can be detected using PublicKeyCredential.isUserVerifyingPlatformAuthenticatorAvailable().
1. Passkeys in Cross-Device Authentication or Registration: Support from the operating system or browser for Cross-Device Authentication is required. Unfortunately, this cannot be detected with PublicKeyCredential.isUserVerifyingPlatformAuthenticatorAvailable(). It may erroneously return false for devices that are capable of proceeding with Cross-Device Authentication (CDA). You also need to check for Bluetooth availability (e.g. Bluetooth.getAvailability()note that even if this function returns true, it does not imply that Bluetooth is activated currently) and provide the right PublicKeyCredentialRequestOptions for the WebAuthn server (both of which can hold their own problems) – see #4 for more details.
While the UI for biometric authentication modals in the operating system cannot be altered, browsers have implemented dialogs that appear before these operating system UIs. These dialogs vary based on your WebAuthn server settings (especially for authenticatorAttachment). Consider the following cross-device (and simultaneously cross-platform) example where you want to use an Android to log into a MacBook. Besides, hardware security keys (e.g. YubiKeys) could be used. Therefore, we define the following WebAuthn server settings:

```plain text
"authenticatorSelection": {
"residentKey": "required",
"requireResidentKey": true,
"userVerification": "required",
"authenticatorAttachment": "platform"
}
```

The user interfaces vary significantly for these WebAuthn server settings, as illustrated in the following screenshots. For example, Safari (first screenshot) streamlines the process of creating passkeys by presenting a clear path, with a subtle hint for additional options at the bottom. Consequently, most users are likely to use Touch ID right away to proceed.

In contrast, Chrome (second screenshot) displays a dialog that might be complex to understand for inexperienced users, as you can decide between “iCloud Keychain” (the first-party passkey provider), “S21 von Vincent” (a stored device), “Other smartphone, other table or other security key” (CDA or hardware security key) or “My Chrome Profile”. On top of that, there’s a button on the bottom left to “Manage Devices” which even increases number of clickable options for the user. Where should a non-technical user click to log in the most seamless way?

Create Passkey Safari

Create Passkey Chrome

When building your passkey experience, all different browsers as well as all operating systems and platforms have to be kept in mind. Most importantly, you need to also take operating systems and browsers into consideration that do not (fully) support passkeys (e.g. Linux, ChromeOS and older versions of Firefox).

Moreover, one might expect that browser support for passkeys will increase over time, leading many current problems to resolve naturally. However, what we have witnessed is somewhat different. While most users (depending on their devices and technical savviness) will see improvements, support must also continue for those using older browsers on outdated devices. This situation only complicates things, as newer versions introduce advanced passkey features. Still, the most crucial aspect is ensuring that every user enjoys a superior login experience with passkeys compared to traditional password-based methods.

## #11 Passkeys’ Availability Equals Accessibility

Passkeys are supported by Apple, Google and Microsoft. So, no matter which device I use, I should be able to use them for logins.

That’s only the half truth. Passkeys are widely adopted by the most popular operating systems and browser (mainly due the backing by Apple, Google & Microsoft that control devices, operating systems and browsers).

However, this universal availability and support does not mean that during an authentication event, you can simply look up public keys of passkeys in the database. It’s a two-side detection that needs to happen during each login event, as each login event depends on the registered passkeys and used device. The following two questions are posed during each login:

- Are passkeys and / or CDA supported?: Does the device itself support passkey authentication? If not, does it support WebAuthn Cross-Device Authentication (CDA) via QR codes & Bluetooth?
- Are passkeys available?: Does the user trying to log in possess any passkeys? If yes, can these passkeys be used in Cross-Device Authentication (e.g. they might be stored on a mobile device only)? Are these passkeys synced in some form (e.g., from an iPhone to a Macbook via iCloud Keychain, or from Macbook to Windows desktop via a password manager like Dashlane)?
Passkeys are considered truly available and accessible only if there's a match in both aspects: the device is passkey-ready and passkeys are available. Only then, passkey login can be possible. This is what passkey intelligence is for: It combines all available information for passkey decisions and is built on top of any WebAuthn server / client library.

## #12 QR Codes are Simple and Appear only When Needed

The passkey login via QR code looks a like a great and user-friendly way to facilitate authentication across-devices. Most users should be able to understand and use it.

Yes and no. While Cross-Device Authentication (CDA) and registration with QR codes can be incredibly effective and powerful tools when used correctly, there is also a significant downside: QR codes often appear when the browser cannot find the passkeys (on the device) that the server has suggested in the allowCredentials list of the PublicKeyCredentialRequestOptions. If the passkeys are not found on the local device, the browser assumes they might exist on an another mobile device, potentially available for cross-device authentication. This assumption can lead to UX surprises with QR codes:

macOS Safari QR Code

The problem is: The user has no idea what to do in case they don’t have a passkey available. They might scan the QR code and then get this cryptic popup on their smartphone.

Android no Passkeys Available

We have listed over 40 of the combinations of WebAuthn PublicKeyCredentialRequestOptions, operating systems (+ versions) and browsers (+versions) here for you. A summary of the different browser behavior can be found below:

WebAuthn Transports Overview

On older Windows versions, the popups / screen, a user might face, can be even more confusing when the device / browser does not support passkeys. See the following screenshot from an authentication process with Windows 10 (21H2; not-passkeys-ready) on Chrome. This might be case not to neglect, as Windows continues to account for the vast majority of the desktop device market share:

Passkey Login Windows 10 Windows Hello

This demonstrates the importance of passkey intelligence in order to avoid unusable QR codes and other confusing screens resulting from passkey logins that should have been avoided (see #11).

## #13 Passkeys Are Universal and Thus Easily Testable

Nice, passkeys are available on most devices. That should also make testing not a big deal.

Well, that’s not the full story. Passkeys are great as they introduce the first phishing-resistant auth method, that is also user-friendly. They can only be used on the domain where they have been created for. This is great in real-life, but makes development and testing of passkey-based applications painful:

- Secure context (https) required for all systems: Passkeys only work in secure contexts (https is required). This also implies that all testing and staging systems need to be set up to work with https.
- Local testing is complex: Local testing of passkeys (localhost) is possible and the only exception to the secure context requirement. The thing is that usually, you want to test your passkey-based app from different, real-life operating system / browser combinations. Especially if cross-device authentication is involved, the entire local test setup presents a significant challenge, as local web applications are often not reachable from other devices than the device they are being developed on. Using a local IP address, if you are in the same Wi-Fi, is no option, as Relying Party IDs cannot be IP addresses, but need to be domains. Also setting up a tunnel or using a service like ngrok might be only short-term solution. Each time you get a new ngrok URL, you need to change the Relying Party ID in your WebAuthn server settings.
- Authenticator performance decreases with number of test credentials: Testing typically involves setting up passkeys on authenticators and frequently re-registering them, whether it’s because you've flushed the database, changed the Relying Party ID, or simply wish to conduct multiple tests of the passkey creation process. One issue is that some authenticators, especially on Windows, tend to slow down as the number of passkeys they need to handle increases (e.g., 200+).
- Debugging is cumbersome: To properly debug your backend, you typically need a set of custom-developed tools that parse and decode details and properties of passkeys. These tools help investigate issues with your passkey intelligence, such as decoding WebAuthn challenges in Base64URL, decoding public keys in COSE format, or deserializing authenticatorData information in CBOR.
- Native app testing requires a publicly reachable server: If you develop for a native app (e.g. iOS or Android), new things become important during testing. You need to have the apple-app-site-association file or the assetlinks.json file hosted on a server and this association file needs to be reachable by Apple and Google (to check its validity). This implies that only having a local relying party server is no option (contrary to web apps where this would suffice). Plus, things become even more complex when you want to test a scenario with a web app and native app that should share the same passkeys (thus needing to have the same relying party ID).
While many libraries and code snippets support basic WebAuthn server implementation and client-side functionality, there is a notable lack of documentation for real-life use cases such as Cross-Device Authentication, end-to-end passkey testing, or general passkey debugging.

## #14 Only Adding Passkeys to an Existing Auth Solution is Easy

Okay, I understand that designing and implementing a full-fledged passkey-first authentication solution might be tricky, but simply adding passkey as an authentication option to our current auth solution should be a lot easier.

That’s sadly not the full story. From what we have experienced with existing apps that already have larger user bases, avoiding friction in any kind and offering a seamless passkeys experience are even more important than in to-be-built apps. Here, it’s crucial to provide an easy-to-understand onboarding to passkeys and avoid friction to today’s authentication process at any cost. To fulfil these requirements, there is usually a ton of additional things to develop that are no fun and will distract you from actually building your core product features. The following things need to be built or adapted:

- Adapt the passkey intelligence to fit current database fields and login flows: All issues when developing your passkey intelligence also apply to the case of simply plugging passkeys into existing authentication flows. It can sometimes be even more complicated when existing fields for password-based authentication need to remain as they are. That’s going to be particularly interesting in the case of autofill, where password and passkey autofill may be used concurrently (Conditional UI can facilitate the process but sometimes it does not work or email fields are autofilled via LocalStorage).
- Gradual device-, user- or cohort-based rollout: Product managers usually want to gradually start their passkey rollout and provide users the possibility to opt in to passkeys. The “Do you want to add a passkey” popup becomes the center of attention and developers will face questions from the product department like: 
- Audit logging & KPI reporting: The aspects mentioned above are usually not exhaustive. Once the initial launch is successfully completed, the product team requires KPIs for various purposes, and the IT security / compliance team needs logs for auditing purposes. From product-side, the following KPIs are among the most-requested ones: 
The more users there are, the more additional features – such as gradual rollout, logging, analytics, and reporting – are needed to control risk. Implementing these features in mature systems is no fun for developers due to the significant additional overhead (remember you just wanted to add passkeys to the product?).

## #15 Please Help Me: I Think I Don’t Want Passkeys Anymore

Okay, after reading the article, I think I’ll stick with my current password-based auth solution and do not implement passkeys, as it seems like too much implementation work.

We understand the challenges that come with rapidly evolving technology and the introduction of new features. However, rest assured, we've got your back. Passkeys are set to become the most popular login method shortly. Once consumers experience the speed and simplicity of using passkeys, there’s no turning back. The demand for passkeys and biometric authentication is only expected to grow as more people realize their immediate benefits (refer to the Google Trends screenshot below—the significant spike occurred when Google made passkeys the default login method for all their accounts in May 2023). We often joke that passkeys are like a drug – once you've experienced them, you don't want to go back to using passwords.

Passkey Google Trend

Moreover, most consumers cannot tell the difference between websites/apps secured with local biometric authentication (e.g., Face ID) and those protected with passkeys (when explaining passkeys to friends, no matter how technical their background, they often mention that this isn’t a new feature because their iCloud Keychain has had such a biometric feature to log them in automatically on websites and apps for several years). We have to admit: both methods – passkeys and local biometric authentication – are similar and instinctively natural to users. That’s also why we strongly believe that it's only a matter of time before companies without passkey capabilities will seem outdated. Just think of:

- Stationary shops that don't support Apple / Google Pay
- People using SMS instead of messenger apps like WhatsApp or Telegram
- People unlocking their smartphone with a password instead of biometrics / PIN pattern
Ultimately, consumers drive market changes, and they are clearly signaling that passkeys are the future.

Implementing passkeys is hard. The devil is in the unknown unknowns. What might initially seem like a simple one sprint task could escalate into a major implementation project if you aim to fully leverage all the benefits of passkeys.

To help address this challenge at scale, we want to help all developers in implementing passkeys quickly and for free with our community plan. Our components and SDKs are easy to integrate and customizable, enabling you to provide your users with the most secure and most convenient login. If you’re interested, you can get started here. Feel free to also join our Passkeys Community or subscribe to our Passkeys Substack. Let’s make the Internet a safer place together!

## Bonus #1: Prepare Your Setup

To help you get a set of devices needed to properly test your self-built passkey authentication solution, we have compiled a list of devices that we use for internal testing. Trust us, using BrowserStack and other emulators works only to a certain extent:

1. PC with Windows 10 (where Bluetooth can be switched on and off)
1. PC with Windows 11 (21H2)
1. PC with Windows 11 (22H2+)
1. MacBook with macOS <=12 (Monterey or older)
1. MacBook with macOS 13+ (Ventura or newer; but not with version 13.6.5 where passkey auth is broken)
1. Android with Android <=8 (Oreo or older)
1. Android with Android 9+ (Pie or newer)
1. iPhone with iOS <=15
1. iPhone with iOS 16+
Moreover, the following resources are required or useful in your passkey development efforts:

- WebAuthn Server: See our guide for finding your WebAuthn server here (also this WebAuthn server needs to be reachable during your local development, so you need a tunnel or tool like ngrok - with all the fun that comes with local relying party IDs)
- Database Schema: See our introduction guide on databases here.
- Passkeys Cheat Sheet: Speed up your development with the most important passkey / WebAuthn know-how from the specification including examples.
- WebAuthn Virtual Authenticator: Browser dev tool to simulate passkey / WebAuthn sign-ups and logins and save time / resources for real authenticators.
- End-2-End Testing Framework: See here how we do it.
- Unit Test Set for Passkey Intelligence: The test set should cover most use cases (probably at least 50). A good start point is the compatibility matrix from passkeys.dev
## Bonus #2: Passkeys are Only Authentication but You Need More

So far, we have only described the considerations you need to address when implementing passkeys. However, passkeys represent just one authentication option in modern systems. In real-life scenarios, to truly leverage most of the value of passkeys, there are additional things you need to implement, which can complicate matters.

- Combine passkeys with other auth methods: Depending on your requirements, you might need to provide other auth options (e.g. passwords, OTPs via email / SMS, TOTP, social logins) – be it as fallback or as an adequate alternative the user can choose from. Specifically, in the context of B2B enterprise software, there might the requirement to integrate SSO / SAML along passkeys, which could be another major endeavor.
- Add secure and efficient session management: Authentication using passkeys is the initial step, but to avoid requiring users to re-authenticate at every page load, you need to implement session management. This is a complex field in itself, with various approaches, such as decentralized JWTs versus centrally-stored sessions.
- Introduce authorization, roles & permissions: Anyone who needs authentication and works in enterprise workforce contexts will soon also require authorization. It's essential to provide your users with roles and different permissions. Additionally, please familiarize yourself with prominent concepts like Role-Based Access Control (RBAC) and Attribute-Based Access Control (ABAC).
Enjoyed this read?

### 🤝 Join our passkeys community

Best place to share passkeys implementation tips and get support to free the world from passwords.

Join for free

### 🚀 Stay up to date

Get the latest news, strategies, and insights about passkeys sent straight to your inbox.

Subscribe for free

We provide UI components, SDKs and guides to help you add passkeys to your app in <1 hour

### Start for free

Recent Articles

Industry

### #1 Developer Tool of the Week @ Product Hunt: How we did it

Lukas R. - February 26, 2024

Passkeys

### September 2023 Update & Insights into Passkey-Readiness

Vincent - September 1, 2023

Implementation

### Passkeys E2E Playwright Testing via WebAuthn Virtual Authenticator

Anders - March 30, 2024

Implementation

### Passkeys Cheat Sheet for Developers

Lukas R. - March 6, 2024

NIST Passkeys

Industry

### NIST Passkeys: Synced Passkeys Recognized as AAL2-Compliant

Vincent - April 24, 2024

Passkeys

### WebAuthn Cross-Device-Authentication: Passkeys via Mobile-First Strategy

Vincent - April 9, 2024


