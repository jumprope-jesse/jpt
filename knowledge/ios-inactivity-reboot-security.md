# iOS 18 Inactivity Reboot Security Feature

Deep technical analysis of iOS 18's security feature that forces device reboot after 72 hours of inactivity. Source: [Reverse Engineering iOS 18 Inactivity Reboot](https://naehrdine.blogspot.com/2024/11/reverse-engineering-ios-18-inactivity.html)

## BFU vs AFU States

**Before First Unlock (BFU):**
- Encrypted user data inaccessible
- No Face ID/Touch ID (passcode required)
- No Wi-Fi (passwords encrypted)
- Cellular works (if SIM not PIN-protected)
- Calls show numbers but not contact names
- Messages show notifications but no previews

**After First Unlock (AFU):**
- Key store kept "open" while iOS runs
- Data decrypted even when lock screen shown
- More vulnerable to attacks - attacker bypassing lock screen gets decrypted data
- Larger attack surface: USB, Wi-Fi, Bluetooth, cellular, hardware attacks
- Older exploits work on devices kept in AFU without updates

## How Inactivity Reboot Works

**Architecture:**
1. Secure Enclave Processor (SEP) tracks last unlock time
2. SEP tells AppleSEPKeyStore kernel module when 72h exceeded
3. Kernel module notifies user space to initiate reboot
4. SpringBoard gracefully terminates processes
5. If reboot doesn't happen, kernel panics (anti-tampering)

**NVRAM variable `aks-inactivity`:**
- Set by kernel before reboot
- Read by keybagd after boot
- Sends analytics to Apple about unlock duration
- Then deleted

## Key Security Properties

**What it protects:**
- Forces device back to BFU state after 3 days
- Thieves can't wait indefinitely for exploit availability
- Criminals locked out of bank accounts, iCloud access
- Reduces window for gray market exploits

**Design choices:**
- Timer runs in SEP, not main CPU - resistant to kernel exploits
- External time sources (internet/cellular) cannot influence timer
- Attacker needs kernel code execution to prevent reboot
- Initial exploit must run within 3 days

## Forensics/Law Enforcement Implications

- Law enforcement traditionally keeps seized phones powered on in AFU
- Must now act within 72 hours
- Some forensic tooling companies claim 24-hour exploit coordination
- Asymmetric impact: locks out criminals completely, adds time pressure for LE

## Debunked Rumors

The law enforcement document claiming phones "wirelessly tell other iPhones to reboot" is **implausible**. This feature:
- Has nothing to do with wireless connectivity
- Works when completely isolated from networks
- Is purely time-based, measured by SEP
- Older phones on pre-iOS 18 likely rebooted due to unrelated bugs

## Technical Details

**Timer value:** 259200 seconds (0x3f480) = 72 hours exactly

**Components involved:**
- `keybagd` daemon (key store related)
- `AppleSEPKeyStore` kernel extension
- SEP firmware (specifically `sks` app)
- SpringBoard (handles graceful shutdown)

**Log messages to look for:**
```
"AppleSEPKeyStore":3846:0: notifying user space of inactivity reboot
```
