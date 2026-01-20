# Passkey/WebAuthn Implementation Guide

Comprehensive guide to passkey implementation challenges, based on real-world experience building passkey-first authentication.

**Source**: https://www.corbado.com/blog/passkey-implementation-pitfalls-misconceptions-unknowns

## Key Insight

Implementing passkeys is 100x harder than it initially appears. What seems like a simple one-sprint task can escalate into a major implementation project.

## Common Misconceptions

### 1. Creating Passkeys is Just `navigator.credentials.create()`

Reality: The WebAuthn JS API is the simplest part. Challenges arise before and after:
- Need **two backend API endpoints** (not one like passwords)
- Must provide **fallbacks** when passkeys fail or user cancels
- Need to **verify users** to prevent account takeover attacks
- Must **detect existing passkeys** to avoid duplicates
- Support **cross-device registration** and hardware security keys
- Adapt **backend/database schema** for passkey storage

### 2. Logins Are Just `navigator.credentials.get()`

Reality: Outstanding passkey UX means knowing when **NOT** to start a ceremony:
- **Windows without Bluetooth**: CDA via QR codes requires Bluetooth proximity check
- **Device-bound passkeys**: Windows passkeys don't sync to other devices
- **Third-party providers**: 1Password/Dashlane passkeys may be available cross-device

Must track login patterns to offer the right method and avoid authentication loops.

### 3. Available Passkeys Can Be Detected from Browser

**This is the biggest fallacy.** FIDO Alliance designed passkeys with privacy-by-design - you cannot detect if a passkey exists before a WebAuthn operation.

You can only detect:
```javascript
// Is device WebAuthn-ready?
PublicKeyCredential

// Is device passkey-ready (platform authenticator)?
PublicKeyCredential.isUserVerifyingPlatformAuthenticatorAvailable()

// Is device Conditional UI ready?
PublicKeyCredential.isConditionalMediationAvailable()
```

### 4. User Agents Work for Device Recognition

Reality: User agents are being phased out:
- **Safari**: Still fully supports user-agent
- **Chrome/Edge/Firefox**: Reduced user-agent detail for privacy
- Need **Client Hints** for Chromium browsers: `navigator.userAgentData.getHighEntropyValues()`
- Safari doesn't support Client Hints
- Must support both methods for full coverage

### 5. WebAuthn Standard is Easy to Read

The spec is complex, written when hardware security keys were primary:
- **Level 2** (current, April 2021): Pre-passkeys, many redundancies
- **Level 3** (expected late 2024): Passkey-focused features

Stay current by monitoring:
- WebAuthn GitHub issues
- Level 3 Editor's draft commits
- Chromium feature requests/releases
- Mozilla & Webkit issues

### 6. Passkey Management UI is Simple

Watch for:
- Use `excludeCredentials` when adding passkeys to prevent client/server mismatches
- **Server-side deletion problem**: Passkey remains on device, user tries to use it
- Flag deleted passkeys, use `allowCredentials` to exclude them
- Empty vs. filled `allowCredentials`: tradeoffs between credential enumeration vs. filtering

### 7. Common Use Cases Are Well Supported

Missing features:
- **Rename passkeys** after creation (iOS 17.4+ only, not server-controlled)
- **Delete passkeys client-side** (blocked by API)
- **Change passkey metadata** (user.name, user.displayName, user.id) - locked at creation

### 8. Passkey UX is Predefined

Requires product decisions:
- Which devices to support?
- What's the passkey-readiness of your user base?
- Gradual rollout strategy?
- Passkey-only for new users?

UX considerations:
- When to show "Add passkey" prompt?
- What happens when passkey append fails?
- Providing explanations/education to users

### 9. Conditional UI Always Works Smoothly

Three login modes:
1. **Regular passkey login** - explicit button click
2. **Passkey login button** - similar to social login button
3. **Conditional UI** (usernameless) - autofill-like experience

```javascript
const credential = await navigator.credentials.get({
  publicKey: publicKeyCredentialRequestOptions,
  mediation: "conditional"
});
```

**Problem**: Modals sometimes interfere with user interactions. Users abort auto-initiated modals.

**Solution**: Store recent passkey hints in LocalStorage to optimize experience.

### 10. Passkeys Work Identically Across Browsers

Major variations exist:
- **Safari**: Streamlines passkey creation with clear path
- **Chrome**: Shows complex dialog with many options (iCloud Keychain, stored devices, CDA, etc.)
- Older Windows versions show confusing prompts
- Browser support differences compound over time as new features roll out

### 11. Passkey Availability = Accessibility

Two-sided detection needed at every login:
1. Does the **device** support passkeys or CDA?
2. Does the **user** have passkeys that are accessible from this device?

Only when both match is passkey login possible. This is "passkey intelligence."

### 12. QR Codes Are Simple

QR codes appear when browser can't find passkeys in `allowCredentials`:
- User often has no idea what to do
- Scanning may show cryptic "no passkeys available" on phone
- Browser behavior varies wildly across OS/browser combinations (40+ documented)

### 13. Passkeys Are Easily Testable

Challenges:
- **HTTPS required** for all test/staging systems (localhost is the only exception)
- **Local testing across devices**: Can't use local IP (RP ID must be domain)
- **Authenticator slowdown**: Performance degrades with 200+ test credentials
- **Debugging tools needed**: Custom tools to decode Base64URL challenges, COSE public keys, CBOR authenticatorData
- **Native apps**: Need publicly reachable server for apple-app-site-association/assetlinks.json

### 14. Adding Passkeys to Existing Auth is Easy

Actually harder than greenfield:
- Must avoid any friction to existing flow
- Adapt passkey intelligence to current database schema
- Handle concurrent password and passkey autofill
- Gradual rollout complexity
- Need audit logging and KPI reporting

### 15. Maybe I'll Skip Passkeys

Passkeys will become dominant:
- Google made passkeys default in May 2023
- Users don't want to go back once they've experienced passkeys
- Companies without passkeys will seem outdated (like shops without Apple Pay)

## Testing Device Matrix

Required devices for comprehensive testing:
1. Windows 10 PC (with Bluetooth toggle)
2. Windows 11 (21H2)
3. Windows 11 (22H2+)
4. MacBook with macOS 12 or older
5. MacBook with macOS 13+ (avoid 13.6.5 - passkeys broken)
6. Android 8 or older
7. Android 9+
8. iPhone iOS 15 or older
9. iPhone iOS 16+

## Beyond Authentication

Passkeys are just authentication. Real systems also need:
- Other auth methods (passwords, OTP, TOTP, social logins) as fallbacks
- SSO/SAML for enterprise
- Session management (JWT vs. centralized sessions)
- Authorization, roles & permissions (RBAC, ABAC)

## WebAuthn Server Settings Example

```javascript
"authenticatorSelection": {
  "residentKey": "required",
  "requireResidentKey": true,
  "userVerification": "required",
  "authenticatorAttachment": "platform"
}
```

## Security Model & Internal Architecture

**Source**: https://research.kudelskisecurity.com/2024/03/14/passkeys-under-the-hood/

### How Passkeys Work Under the Hood

Passkeys are **FIDO credentials** created via the WebAuthn specification:

1. **Credential Creation** (`navigator.credentials.create()`):
   - Browser generates an **asymmetric key pair** for the service
   - User validates with fingerprint/PIN
   - **Private key stored exclusively on user's device** (never sent to server)
   - Server only stores the **public key**
   - Includes **origin field** in signature (read by browser, not service) → prevents phishing

2. **Authentication** (`navigator.credentials.get()`):
   - Service sends a random challenge
   - User validates with PIN/fingerprint
   - Client signs challenge + service address + other info with private key
   - Service verifies signature with stored public key

### Threat Model Differences: Passkeys vs Hardware Security Keys

| Aspect | Hardware Security Key | Passkey |
|--------|----------------------|---------|
| **Private key exposure** | Never accessible, stored in secure element | Decrypted and in memory during use |
| **Physical attack resistance** | Attacker with physical access cannot extract key | Attacker with system access may extract key from memory |
| **Backup/sync** | Requires enrolling second physical key per service | Syncs across devices (vendor-dependent) |
| **Vendor lock-in** | No lock-in (device-agnostic) | May lock to ecosystem (Apple/Google/Microsoft) |

**Key insight**: Passkeys solve the backup problem but change the threat model. The private key is now exposed to the user's system, making **local attacks** a new consideration.

### Platform-Specific Implementations

#### Windows (Microsoft Hello)
- Passkeys secured via TPM (if available)
- **No synchronization** to other devices
- Managed via Passkey settings menu
- Limited export/inspection capability (`certutil` shows public key only)

#### Apple/Android
- **Cross-device sync enabled** within ecosystem
- Cannot transfer passkeys between ecosystems (e.g., Apple → Android)
- Users locked to vendor choice

### Bitwarden Implementation (Open Source Analysis)

Bitwarden provides **cross-platform sync** and **end-to-end encryption**, mitigating vendor lock-in:

**Architecture**:
1. Browser extension **intercepts WebAuthn calls** by overriding `navigator.credentials.create()` and `navigator.credentials.get()`
2. Shows Bitwarden pop-up instead of OS passkey dialog
3. Option to use "hardware key" falls back to OS mechanism (Microsoft Hello or physical security key)
4. Passkeys stored **encrypted** like passwords, synced to Bitwarden server with E2E encryption
5. **Export capability**: Private keys can be exported in JSON format for portability

**Key generation** (from code inspection):
```javascript
// makeCredential function creates:
{
  credentialId: "...",
  privateKey: "...",  // ECDSA key accessible during creation
  publicKey: "...",
  counter: 0,
  rpId: "example.com",
  userHandle: "..."
}
```

Unlike hardware keys where private key is never visible, Bitwarden's implementation makes the full credential inspectable and exportable.

### Server Breach Resistance

Since servers only store **public keys**, a breach cannot leak user credentials (unlike password databases). This is a fundamental advantage over traditional authentication.

### Credential Properties Example

```json
{
  "rp": {"name": "webauthn.io", "id": "webauthn.io"},
  "user": {
    "id": "c3lsdmFpbg",
    "name": "sylvain",
    "displayName": "sylvain"
  },
  "challenge": "5MvoufqYlltIT9JaQFMGG83ej...",
  "pubKeyCredParams": [
    {"type": "public-key", "alg": -7},    // ECDSA with SHA-256
    {"type": "public-key", "alg": -257}   // RSASSA-PKCS1-v1_5 with SHA-256
  ],
  "authenticatorSelection": {
    "residentKey": "preferred",
    "userVerification": "preferred"
  }
}
```

## Resources

- Passkeys Cheat Sheet for spec know-how
- WebAuthn Virtual Authenticator for browser testing
- passkeys.dev compatibility matrix for unit tests
- Corbado community/tools: https://www.corbado.com
- Kudelski Security Research: https://research.kudelskisecurity.com/
