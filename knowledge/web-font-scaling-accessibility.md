# Web Font Scaling for Accessibility

Source: Airbnb Engineering Blog (May 2024)
https://medium.com/airbnb-engineering/rethinking-text-resizing-on-web-1047b12d2881

## The Problem

WCAG 1.4.4 Resize Text (Level AA) requires web content to remain functional when text is scaled to 200%. Browser zoom works well on desktop but causes severe usability issues on mobile web - scaling content into half the viewport width/height makes pages unusable.

**Key insight**: Font scaling (adjusting text size independently) is superior to browser zoom for mobile web accessibility.

## CSS Units for Font Scaling

| Unit | Behavior | Use Case |
|------|----------|----------|
| `px` | Fixed, doesn't scale | Avoid for text |
| `em` | Relative to parent font size | Can cascade unpredictably |
| `rem` | Relative to root (`html`) element | Preferred - consistent, predictable |

**Best practice**: Use `rem` units specifically for font-related properties, not everything (scaling everything = browser zoom behavior).

## Implementation Strategy

### Automation over Education

Instead of training developers to think in rem, Airbnb:
1. Continued authoring CSS in `px` units
2. Automated conversion to `rem` at build time
3. Provided escape hatch with capitalized `Px` or `PX` (ignored by converters, accepted by browsers)

### Linaria (CSS-in-JS)

```javascript
// Convert typography theme values from px to rem
const theme = css`
  ${getCssVariables({ typography: replacePxWithREMs(typography) })}
`;
// body-font-size: 16px → body-font-size: 1rem
```

Used `postcss-pxtorem` plugin with allowlist for gradual rollout.

### React-with-Styles

Higher-order component wrapper that converts styles:

```javascript
export const withRemStyles = (styleFn, options) => {
  if (options?.disableConvertToRemUnits) {
    return _withStyles(styleFn, options);
  }
  return _withStyles((theme) => {
    const styles = styleFn(theme);
    return convertToRem(styles);
  }, options);
};
```

## Mobile Safari Challenges

Mobile Safari has no font size preference, but supports `-apple-system-body`:

```css
/* Target only iOS/iPadOS */
@supports (font: -apple-system-body) and (-webkit-touch-callout: default) {
  :root {
    font: -apple-system-body;
  }
}
```

**Gotcha**: Safari's default is 17px, not 16px. Normalize with inline head script:

```javascript
if (style.fontSize === '17px') {
  documentElement.style.setProperty('font-size', '16px');
}
```

Use ResizeObserver to detect subsequent changes and maintain normalization.

## Testing

- **Text Resizer - Accessibility Checker**: Browser extension to simulate 2x font size during design
- **Screenshot testing**: Capture components at multiple root font sizes
- **Component docs plugin**: Set font-size on `html` element for testing

## Results

Over 80% reduction in Resize Text accessibility issues after site-wide rollout.

## Key Takeaways

1. Font scaling > browser zoom for mobile web accessibility
2. Use `rem` for font properties, not everything
3. Automate px→rem conversion rather than changing developer workflows
4. Mobile Safari requires special handling for Dynamic Type support
5. Test designs early with simulated font scaling
