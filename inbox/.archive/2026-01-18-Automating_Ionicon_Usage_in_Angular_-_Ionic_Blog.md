---
type: link
source: notion
url: https://ionic.io/blog/automating-ionicon-usage-in-angular
notion_type: Software Repo
tags: ['Running']
created: 2024-05-22T21:38:00.000Z
---

# Automating Ionicon Usage in Angular - Ionic Blog

## AI Summary (from Notion)
- Purpose: The article addresses the challenge of reducing bundle size in Ionic applications by automating the usage of IonIcons.
- Key Problem: Manually managing addIcons for IonIcons can be repetitive and cumbersome for developers, impacting performance.
- Proposed Solution: Introduction of the ionic-angular-collect-icons package to streamline icon management and minimize bundle size.

- Installation Steps:
- Install the package with npm.
- Update npm scripts to include a prebuild command for automatic icon management.

- Understanding addIcons:
- Registers icons by mapping icon names to SVG code in the Window object.
- Efficient management of which icons are loaded can lead to quicker load times and a leaner bundle.

- Best Practices:
- Load only necessary icons at app launch rather than all available icons, which can bloat the bundle.
- Use a CLI tool to scan templates for used icons and generate a use-icons.ts file for easier management.

- Takeaway: Finding a balance between convenience during development and efficiency in production is crucial for optimal performance.
- Author's Background: Masahiko Sakakibara is an Ionic Developer Expert and a contributor to the Ionic community, particularly for the Japanese audience.

## Content (from Notion)

Masahiko Sakakibara is a member of the Ionic community, a recognized Ionic Developer Expert, and an organizer of the Ionic Japan User Group. Masahiko has also contributed substantially to the Ionic community through his work translating the documentation for Ionic Framework, Stencil, and Capacitor for the Japanese community.

In a modern development workflow, reducing bundle size to optimize performance is key to providing the best user experience. However, In the realm of Ionic Standalone Components, manually running addIcons to utilize IonIcons can be repetitive and cumbersome for developers.

To simplify this process, I’ve devised a custom approach that trims bundle size and improves app speed. I’ve included a brief tutorial below:

```plain text
@Component({
  ...,
  imports: [IonIcon,...]
})
export class ExamplePage {
  constructor(){
    addIcons({accessibilityOutline})
  }
}

```

The method shown above does trim down bundle size and speed up the app; however, the repetitive task of managing addIcons across multiple components adds extra overhead. To fix this, I’ve developed a solution: the ionic-angular-collect-icons package. This tool is designed to help minimize bundle size while improving the overall developer experience.

Begin by installing @rdlabo/ionic-angular-collect-icons and initializing it with the command below:

```plain text
npm install @rdlabo/ionic-angular-collect-icons --sve-dev
npx @rdlabo/ionic-angular-collect-icons --initialize true
```

And set npm script:

```plain text
  "scripts": {
    "ng": "ng",
    "start": "ng serve",
    "build": "ng build",
+   "prebuild": "npx @rdlabo/ionic-angular-collect-icons"
  },
```

Next, update your npm scripts as follows to eliminate manually managing addIcons:

### Behind the Scenes

1) The Role of addIcons:

addIcons is how you register icons—mapping icon names to SVG code—directly into Ionicons within the Window object. A quick example with addIcons({ accessibilityOutline }) looks something like this:

```plain text
window.Ionicons.accessibilityOutline = "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' class='ionicon' viewBox='0 0 512 512'><circle stroke-linejoin='round' cx='256' cy='56' r='40' class='ionicon-fill-none ionicon-stroke-width'/><path stroke-linejoin='round' d='M204.23 274.44c2.9-18.06 4.2-35.52-.5-47.59-4-10.38-12.7-16.19-23.2-20.15L88 176.76c-12-4-23.21-10.7-24-23.94-1-17 14-28 29-24 0 0 88 31.14 163 31.14s162-31 162-31c18-5 30 9 30 23.79 0 14.21-11 19.21-24 23.94l-88 31.91c-8 3-21 9-26 18.18-6 10.75-5 29.53-2.1 47.59l5.9 29.63 37.41 163.9c2.8 13.15-6.3 25.44-19.4 27.74S308 489 304.12 476.28l-37.56-115.93q-2.71-8.34-4.8-16.87L256 320l-5.3 21.65q-2.52 10.35-5.8 20.48L208 476.18c-4 12.85-14.5 21.75-27.6 19.46s-22.4-15.59-19.46-27.74l37.39-163.83z' class='ionicon-fill-none ionicon-stroke-width'/></svg>"
```

From this point forward, you can call Ionicons without the overhead of unnecessary SVGs cluttering your bundle, which translates to quicker load times.

2) Why Managing addIcons Matters:

The placement of addIcons—whether in ngOnInit, the constructor, or elsewhere—isn’t a big deal as long as it runs before the icon is needed. The trick lies in efficiently managing which icons are registered. Keeping your bundle lean means being diligent about removing unused icons and adding new ones only as needed.

Missed adding icons with addIcons but everything looks fine? That could be because they pre-loaded with the component, risking display issues on direct URL access.

Despite these nuances, judicious use of addIcons remains a solid strategy for keeping your app lean and mean.

3) The Lazy Way Out:

What’s the easiest, albeit least efficient, method? Simply use addIcons to load everything without a second thought:

```plain text
import * as allIcons from 'ionicons/icons';
addIcons(allIcons)
```

Sure, all your icons are on display, but at what cost? (Answer: a big bloated bundle)

4) A Balanced Approach:

Loading every single Ionicon is overkill, both in terms of size and headache. My compromise? Load just the icons used in your templates at app launch, using the following steps:

1. Load all component templates
1. Create a unique list of IonIcons in use in the template
1. run addIcons with the list at app launch
1. Create a CLI that automatically executes it
I’ve also put together a CLI to automate this, sparing you the manual toil.

For development, it’s okay to load all icons for convenience. But when it comes to production time, switch to this more selective method to keep things efficient.

### The CLI Magic:

This tool scans your templates for ion-icon elements, collects the used icons, and generates a use-icons.ts file. You then load this file once, and voilà—icon management made easy.

```plain text
import { environment } from '../environments/environment';
import { addIcons } from 'ionicons';
import * as allIcons from 'ionicons/icons';
import * as useIcons from '../use-icons';

addIcons(environment.production ? useIcons : allIcons);
```

### Initialization Made Easy:

Running the CLI with --initialize true sets everything up for you:

```plain text
npx @rdlabo/ionic-angular-collect-icons
```

This generates src/use-icons.ts. Import this file in your main setup, and you’re all set. Remember to clean up any other addIcons calls in your constructors.

### The Takeaway:

In the race to develop quickly and maintain speedy app performance, finding the right balance is key. Reducing bundle size can be critical in maximizing app speed and loading efficiency, but manually reducing it is often cumbersome. Hopefully this plugin makes that balancing act a bit easier.

To follow Masahiko and the work he does for the Japanese Ionic community, be sure to check out his Twitter!

### Masahiko Sakakibara


