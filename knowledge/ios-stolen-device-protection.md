# iOS Stolen Device Protection

Security feature introduced in iOS 17.3 (January 2024) that protects against a specific threat model: thieves who trick victims into revealing their passcode before stealing the device.

Source: [The Verge - iOS 17.3 Stolen Device Protection](https://www.theverge.com/2024/1/22/24047063/iphone-ios-17-3-update-stolen-device-protection)

## The Threat Model

**Traditional vulnerability:**
- Thieves observe or trick victims into entering passcode
- Steal device with known passcode
- Quickly take over iCloud account, bank access, email, etc.
- Passcode alone was sufficient for sensitive operations

## How Stolen Device Protection Works

**Biometric requirement for sensitive actions:**
- Viewing saved passwords
- Applying for new Apple Card
- Using payment methods saved in Safari
- Turning off Lost Mode
- Erasing all content and settings
- Taking certain actions in Passwords in Settings
- Using iPhone to set up a new device

**Security Delay for critical changes:**
- Changing Apple ID password
- Changing iPhone passcode
- Adding/removing Face ID or Touch ID
- Turning off Find My
- Turning off Stolen Device Protection itself

Requires: Face ID/Touch ID → **1 hour wait** → Face ID/Touch ID again

**Location awareness:**
- Only activates when away from "familiar locations" (home, work)
- Learns locations where you regularly use your device
- At familiar locations, normal passcode authentication works

## Enabling the Feature

Settings → Face ID & Passcode → Enter passcode → Toggle "Stolen Device Protection"

## Design Philosophy

**Assumes compromise:**
- Passcode is known to attacker
- Device is in attacker's possession
- Attacker is in unfamiliar location

**Defense layers:**
1. Biometrics can't be observed/shoulder-surfed
2. Time delay prevents quick account takeover
3. Second biometric confirms attacker didn't just use stolen finger/face
4. Location context prevents usability impact at trusted locations

**Asymmetric impact:**
- Legitimate user: minimal friction at home/work
- Thief: cannot proceed even with passcode

## Related iOS Security Features

- **Inactivity Reboot** (iOS 18): Forces BFU state after 72h of no unlock
- **Find My**: Remote lock and erase
- **Activation Lock**: Prevents device reactivation without Apple ID

## iOS 17.3 Additional Features

- Collaborative playlists in Apple Music
- AirPlay to hotel TVs (select hotels)
- Security updates backported to iOS 9, 15, 16
