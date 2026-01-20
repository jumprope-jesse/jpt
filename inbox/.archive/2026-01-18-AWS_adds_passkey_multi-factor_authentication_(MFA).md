---
type: link
source: notion
url: https://aws.amazon.com/blogs/aws/aws-adds-passkey-multi-factor-authentication-mfa-for-root-and-iam-users/
notion_type: Tech Announcement
tags: ['Running']
created: 2024-06-11T15:41:00.000Z
---

# AWS adds passkey multi-factor authentication (MFA) for root and IAM users | AWS News Blog

## AI Summary (from Notion)
- Launch of Passkey MFA: AWS introduces passkeys as a new multi-factor authentication (MFA) option for root and IAM users.
- Enhanced Security: Passkeys offer an additional layer of security, making accounts more resistant to unauthorized access and phishing attacks.
- MFA Enforcement: MFA will be enforced for the root user of AWS management accounts, rolling out progressively to other accounts throughout the year.
- Passkey Functionality: Passkeys consist of a pair of cryptographic keys, one public and one private, stored securely on the user's device.
- Convenience and Recovery: Users can easily recover passkeys through cloud services (e.g., iCloud, Google accounts), enhancing convenience.
- Cross-Device Authentication: Passkeys can be used across devices thanks to a QR code scanning feature, allowing for seamless authentication.
- User Experience Variation: The sign-in process will vary depending on the user's operating system and browser, highlighting the adaptability of the passkey system.
- Recommendation Against IAM for Human Access: AWS suggests using Single Sign-On (SSO) with AWS IAM Identity Center instead of IAM users for accessing the AWS console.
- Global Availability: Passkey MFA is available in all AWS regions except China and AWS GovCloud due to the absence of root users in those regions.

## Content (from Notion)

---

Security is our top priority at Amazon Web Services (AWS), and today, we’re launching two capabilities to help you strengthen the security posture of your AWS accounts:

- First, we’re adding passkeys to the list of supported multi-factor authentication (MFA) for your root and AWS Identity and Access Management (IAM) users.
- Second, we started to enforce MFA on your root users, starting with the most sensitive one: the root user of your management account in an AWS Organization. We will continue to roll out this change on your other accounts during the rest of the year.
MFA is one of the simplest and most effective ways to enhance account security, offering an additional layer of protection to help prevent unauthorized individuals from gaining access to systems or data.

MFA with passkey for your root and IAM usersPasskey is a general term used for the credentials created for FIDO2 authentication.

A passkey is a pair of cryptographic keys generated on your client device when you register for a service or a website. The key pair is bound to the web service domain and unique for each one.

The public part of the key is sent to the service and stored on their end. The private part of the key is either stored in a secured device, such as a security key, or securely shared across your devices connected to your user account when you use cloud services, such as iCloud Keychain, Google accounts, or a password manager such as 1Password.

Typically, the access to the private part of the key is protected by a PIN code or a biometric authentication, such as Apple Face ID or Touch ID or Microsoft Hello, depending on your devices.

When I try to authenticate on a service protected with passkeys, the service sends a challenge to my browser. The browser then requests my device sign the challenge with my private key. This triggers a PIN or biometric authentication to access the secured storage where the private key is stored. The browser returns the signature to the service. When the signature is valid, it confirms I own the private key that matches the public key stored on the service, and the authentication succeeds.

You can read more about this process and the various standards at work (FIDO2, CTAP, WebAuthn) in the post I wrote when AWS launched support for passkeys in AWS IAM Identity Center back in November 2020.

Passkeys can be used to replace passwords. However, for this initial release, we choose to use passkeys as a second factor authentication, in addition to your password. The password is something you know, and the passkey is something you have.

Passkeys are more resistant to phishing attacks than passwords. First, it’s much harder to gain access to a private key protected by your fingerprint, face, or a PIN code. Second, passkeys are bound to a specific web domain, reducing the scope in case of unintentional disclosure.

As an end user, you will benefit from the convenience of use and easy recoverability. You can use the built-in authenticators in your phones and laptops to unlock a cryptographically secured credential to your AWS sign-in experience. And when using a cloud service to store the passkey (such as iCloud keychain, Google accounts, or 1Password), the passkey can be accessed from any of your devices connected to your passkey provider account. This helps you to recover your passkey in the unfortunate case of losing a device.

How to enable passkey MFA for an IAM userTo enable passkey MFA, I navigate to the AWS Identity and Access Management (IAM) section of the console. I select a user, and I scroll down the page to the Multi-factor authentication (MFA) section. Then, I select Assign MFA device.

Note that to help you increase resilience and account recovery, you can have multiple MFA devices enabled for a user.

On the next page, I enter an MFA device name, and I select Passkey or security key. Then, I select next.

enable MFA : select passkey

When using a password manager application that supports passkeys, it will pop up and ask if you want to generate and store a passkey using that application. Otherwise, your browser will present you with a couple of options. The exact layout of the screen depends on the operating system (macOS or Windows) and the browser you use. Here is the screen I see on macOS with a Chromium-based browser.

Enable passkey : choose method

The rest of the experience depends on your selection. iCloud Keychain will prompt you for a Touch ID to generate and store the passkey.

In the context of this demo, I want to show you how to bootstrap the passkey on another device, such as a phone. I therefore select Use a phone, tablet, or security key instead. The browser presents me with a QR code. Then, I use my phone to scan the QR code. The phone authenticates me with Face ID and generates and stores the passkey.

This QR code-based flow allows a passkey from one device to be used to sign in on another device (a phone and my laptop in my demo). It is defined by the FIDO specification and known as

cross device authentication (CDA).

When everything goes well, the passkey is now registered with the IAM user.

Enable passkey : success

Note that we don’t recommend using IAM users to authenticate human beings to the AWS console. We recommend configuring single sign-on (SSO) with AWS IAM Identity Center instead.

What’s the sign-in experience?Once MFA is enabled and configured with a passkey, I try to sign in to my account.

The user experience differs based on the operating system, browser, and device you use.

For example, on macOS with iCloud Keychain enabled, the system prompts me for a touch on the Touch ID key. For this demo, I registered the passkey on my phone using CDA. Therefore, the system asks me to scan a QR code with my phone. Once scanned, the phone authenticates me with Face ID to unlock the passkey, and the AWS console terminates the sign-in procedure.

Authenticate with MFA and passkey

Enforcing MFA for root usersThe second announcement today is that we have started to enforce the use of MFA for the root user on some AWS accounts. This change was announced last year in a blog post from Stephen Schmidt, Chief Security Officer at Amazon.

To quote Stephen:

Verifying that the most privileged users in AWS are protected with MFA is just the latest step in our commitment to continuously enhance the security posture of AWS customers.

We started with your most sensitive account: your management account for AWS Organizations. The deployment of the policy is progressive, with just a few thousand accounts at a time. Over the coming months, we will progressively deploy the MFA enforcement policy on root users for the majority of the AWS accounts.

When you don’t have MFA enabled on your root user account, and your account is updated, a new message will pop up when you sign in, asking you to enable MFA. You will have a grace period, after which the MFA becomes mandatory.

You can start to use passkeys for multi-factor authentication today in all AWS Regions, except in China.

We’re enforcing the use of multi-factor authentication in all AWS Regions, except for the two regions in China (Beijing, Ningxia) and for AWS GovCloud (US), because the AWS accounts in these Regions have no root user.

Now go activate passkey MFA for your root user in your accounts.

- - seb

