# Mihai Parparita - Projects Portfolio

Source: https://blog.persistent.info/p/projects.html

Mihai Parparita is a founding engineer at Quip (acquired by Salesforce 2016), former Chrome Apps tech lead at Google, and early Google Reader team member. His project portfolio spans 2003-2023 with interesting technical depth.

## Notable Projects

### Infinite Mac (2022)
WebAssembly/Emscripten port of classic Mac emulators with web API integration for fast loading, data import/export, and networking. Available at:
- system7.app
- macos8.app
- infinitemac.org

Source code available. Shows how to bring legacy software to the web via WASM.

### RetroGit (2014)
Sends daily/weekly digest of your GitHub commits from years past. "Timehop for your codebase." Good example of a simple, focused tool that provides value. Still running.
- Source: https://github.com/nicknick/retrogit

### Git Resource Fork Hooks (2021)
Pre-commit and post-checkout hooks that extract Mac resource forks into parallel `.r` files for structured diffs. Built to archive late-90s Mac software to Git while preserving resource forks.

### Quip TypeScript Migration (2019)
Led migration from JSDoc-annotated JavaScript with Closure Compiler to TypeScript with Vite/Rollup. Involved migrating from React.createClass + mixins to ES6 classes/modules through "flag day" migrations.

### Closure Compiler support for React (2015)
Custom compiler pass to extract React component type definitions and apply them at creation time. Extended over years to support props (2016), size optimizations (2017), state (2018), ES6 modules/classes (2019).

### Quip Live Apps (2017)
Embedded interactive, offline-capable, mobile-friendly third-party content in documents. Research included making rich text editing available to third-party apps and allowing iframed content to extend beyond rectangles.

## Historical/Archived Projects

- **Google Reader 1.0** (2005) - Initial team member, worked on frontend
- **Chrome Apps** (2011-2012) - Tech lead, built packaged apps (proto-Electron)
- **Gmail Greasemonkey Scripts** (2005) - Added saved searches, preview bubbles, keyboard macros, label colors
- **Delicious to Google Bookmarks** (2006) - Simple migration tool that became popular during Yahoo shutdown rumors
- **Overplot** (2006) - Overheard in New York + Google Maps mashup, surprisingly still works

## Patterns

1. **Scratching own itches** - Most projects solve personal problems (archiving old code, downloading Instagram photos, navigating Chrome codebase)
2. **Technical depth in simple ideas** - Overplot looks simple but involved geocoding thousands of hand-entered addresses and plotting thousands of markers efficiently
3. **Long maintenance tail** - Many projects require ongoing upkeep as platforms change (Instagram Downloader, various Chrome extensions)
4. **Platform dependency risk** - Multiple projects died when underlying platforms changed (App Engine Python 2.5, Google App Engine XMPP, Chrome Apps deprecation)

## Blog
https://blog.persistent.info/ - Technical posts about the projects above
