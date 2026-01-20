# Ionic Framework Notes

Collection of Ionic development notes and updates.

---

## Ionic 8 Release (April 2024)

Key enhancements in the Ionic 8 release:

### Accessibility Improvements
- **AA Color Contrast**: Revised color palette meets WCAG AA contrast levels
- **AAA High Contrast Palette**: New `dark.high-contrast.css` for scenarios requiring highest contrast
- **Step Color Tokens**: New tokens for controlling text colors independently of backgrounds

### Built-in Palettes
Light and dark palettes now ship built-in (no more copy-paste of design tokens):

```javascript
// Auto-applies dark palette based on system preference
import '@ionic/react/css/palette/dark.system.css';
```

### New Components
- **ion-input-password-toggle**: Toggle password visibility in inputs
- **New Picker**: Inline picker (introduced in Ionic 6 Datetime) now available as standalone

### iOS 17 Design Updates
- Action Sheet buttons can now be disabled
- Various subtle design spec updates

### Migration
- Minimal breaking changes, most don't require code updates
- [Migration Guide](https://ionicframework.com/docs/intro/upgrading)

---

## Icon Optimization

Technique for reducing bundle size in Ionic Angular apps by automating IonIcon management.

## The Problem

Manually managing `addIcons()` for IonIcons is repetitive and error-prone. Loading all icons bloats the bundle.

## Solution: ionic-angular-collect-icons

Package that scans templates and generates a file with only the icons actually used.

### Installation

```bash
npm install @rdlabo/ionic-angular-collect-icons --save-dev
npx @rdlabo/ionic-angular-collect-icons --initialize true
```

### Setup npm scripts

```json
{
  "scripts": {
    "prebuild": "npx @rdlabo/ionic-angular-collect-icons"
  }
}
```

### Usage in main.ts

```typescript
import { environment } from '../environments/environment';
import { addIcons } from 'ionicons';
import * as allIcons from 'ionicons/icons';
import * as useIcons from '../use-icons';

// Load all icons in dev for convenience, only used icons in prod
addIcons(environment.production ? useIcons : allIcons);
```

## How addIcons Works

`addIcons()` registers icons by mapping icon names to SVG code in `window.Ionicons`. Only registered icons can be displayed.

```typescript
// This registers a single icon
addIcons({ accessibilityOutline })

// This registers ALL icons (bloated bundle)
import * as allIcons from 'ionicons/icons';
addIcons(allIcons)
```

## Key Points

- Placement of `addIcons()` doesn't matter as long as it runs before the icon is needed
- Missing `addIcons()` may not cause visible issues if icons pre-loaded with component, but can break on direct URL access
- The CLI scans templates for `ion-icon` elements and generates `src/use-icons.ts`

## Source

- Author: Masahiko Sakakibara (Ionic Developer Expert, Ionic Japan User Group organizer)
- Package: [@rdlabo/ionic-angular-collect-icons](https://www.npmjs.com/package/@rdlabo/ionic-angular-collect-icons)

---

## iOS 17.4 PWA Limitations (EU Only)

Apple significantly limited PWAs in iOS 17.4 for EU users.

### The Change

When using a third-party browser (any browser not using WebKit) and saving a web app to the home screen, iOS now opens it in the browser instead of a standalone app shell.

### Why Apple Did This

Apple claims this was necessary to comply with EU regulations requiring alternative browser support. Their reasoning: since users could use a non-WebKit browser, they can't guarantee security/privacy for home screen web apps, so they removed the standalone experience entirely for EU users.

### Ionic's Response: Use Capacitor

Ionic's native runtime **Capacitor** lets you convert a PWA to a native iOS app with no code changes:

1. Add Capacitor to your web project
2. Build as a native iOS app instead of PWA
3. Get full native capabilities while keeping web development workflow

This sidesteps Apple's PWA limitations entirely since you're shipping a real native app.

### When This Matters

- **Indie devs**: PWAs have been popular for simpler distribution
- **Enterprise**: Many orgs wanted PWAs for faster time-to-market
- **EU-only**: Currently only affects users in the EU

### Source

- [Ionic Blog - February 2024](https://ionic.io/blog/a-note-on-ios-17-4-and-pwas)
