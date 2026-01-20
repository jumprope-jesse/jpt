# AWS Passkey MFA for Root and IAM Users

AWS supports passkeys as a multi-factor authentication (MFA) option for root and IAM users.

## Key Points

- **Passkeys as second factor**: Used in addition to password (not as replacement)
- **Phishing resistant**: Cryptographic keys bound to specific web domain
- **Cross-device support**: QR code scanning allows using phone passkey to sign in on laptop
- **Cloud sync**: Passkeys stored in iCloud Keychain, Google accounts, or password managers like 1Password can be accessed across devices
- **Multiple MFA devices**: Can register multiple MFA devices per user for resilience

## How Passkeys Work

1. Key pair generated on client device during registration
2. Public key stored on AWS, private key stored on device or synced via cloud
3. Private key protected by PIN or biometric (Face ID, Touch ID, Windows Hello)
4. During auth, service sends challenge, device signs with private key
5. Signature verified against stored public key

## MFA Enforcement

AWS is progressively enforcing MFA for root users:
- Started with management accounts in AWS Organizations
- Rolling out to other accounts throughout 2024
- Grace period provided before becoming mandatory

## Best Practices

- Use AWS IAM Identity Center (SSO) for human console access instead of IAM users
- Register multiple MFA devices for account recovery
- Available in all regions except China and GovCloud (no root users there)

## Source
https://aws.amazon.com/blogs/aws/aws-adds-passkey-multi-factor-authentication-mfa-for-root-and-iam-users/
