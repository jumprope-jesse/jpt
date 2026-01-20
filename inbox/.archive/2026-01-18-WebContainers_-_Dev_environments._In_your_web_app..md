---
type: link
source: notion
url: https://webcontainers.io/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-07-13T14:35:00.000Z
---

# WebContainers - Dev environments. In your web app. | WebContainers

## AI Summary (from Notion)
- WebContainers Overview: A browser-based runtime that allows for instant, interactive coding experiences.
- Integration: Facilitates building fully branded products without reliance on external servers.
- User Testimonials: Positive feedback from prominent developers and organizations highlighting its ease of use and transformative potential for educational tools and development environments.
- Performance: Claims to run native package managers (npm, pnpm, yarn) up to 10x faster than local environments.
- Framework Support: Supports major frameworks and allows for disposable environments for development.
- Wasm Compatibility: Can run WebAssembly (Wasm) applications out of the box.
- API Simplicity: The WebContainer API is noted for its clarity and effectiveness in creating interactive documentation and learning materials.
- Cost Efficiency: Eliminates server costs by leveraging local CPU and browser resources for development.
- Market Versatility: Beneficial for a range of users from startups to Fortune 500 companies, emphasizing its scalability and robust support.
- Future Potential: Seen as a fundamental shift in browser capabilities, with opportunities for AI-native development environments and enhanced learning experiences.

## Content (from Notion)

From interactive tutorials to full-blown IDEs, build instant, interactive coding experiences backed by WebContainers: the trusted, browser-based runtime from StackBlitz.

Get startedBook a demo

index.js

### Battle-tested by cutting-edge teams

On the SvelteKit team, we've fantasized for years about being able to build fully interactive learning material for full stack frameworks.
With WebContainers it went from 'impossible' to 'easy' almost overnight.

Rich Harris

Principal Software Engineer, Vercel

As a team working on educational products, StackBlitz WebContainers has been an invaluable tool for us. The ability to embed full-stack applications with customisable, interactive coding environment directly into our products has greatly enhanced the learning experience for our users.

Vojta Holik

Designer & Developer, Egghead.io

WebContainers solve the final frontier in JavaScript developer experience - making full-stack Node.js projects run in the browser as lightweight and disposable and secure as frontend REPLs.

Every PR, every npm library maintainer, every devtool company with a Node.js SDK, can benefit from this!

swyx

I have worked with Web container API for a couple of weeks at Scrimba to make a pooc of backend support. And I can say it's a solid piece of technology. Things just work, and it's also quite fast. I'm super excited about the GA since it will unlock so much opportunities for OSS projects and the industry at large.

Abdellah Alaoui

Fullstack hacker, Scrimba

The WebContainer API is a landmark on the way we think docs. Creating interactive docs and snippets just became so much more feasible! With Server-side code running on the browser, setting up a playground to securely learn Node.js SDKs and compilers became feasible and even fun!

Atila Fassina

DX Engineer at Xata

WebContainers represent a fundamental shift in what is possible in the browser. I'm incredibly excited about the potential this tech unlocks, from secure, browser-based development environments to highly interactive educational content.

Nate Moore

Senior Software Engineer, The Astro Technology Company

For such a powerful piece of tech I was so impressed by how clear to use the API is. Also running WebContainers inside WebContainers had me 🤯

Ramón Huidobro

Developer Advocate at Suborbital Software Systems

At re:tune, we have been building the missing frontend for GPT-3, on a mission to empower everyone to build AI-first software at the speed of thought. WebContainers set the stage for our AI-native IDE - with a copilot that can not only read and write code, but can also understand and operate in the full runtime context across server and client!

DJ

Founder & CEO @ re:tune

Running chess in a terminal, running a terminal in the browser, check mate!

The best position to be in is a creative one and the StackBlitz WebContainers allow that.

Manus Nijhoff

Co-founder at Touchy Studios & full-stack developer at 100k

## Power your web app withthe WebContainer API

Create unmatched user experiences by integrating Node.js directly into your web app.

Build fully-branded products without connecting to external servers or directing users away to third-party apps.

### Run native package managers

Run the native versions of npm, pnpm, and yarn, all in the browser, all in your app, up to 10x faster than local.

### Full browser support

Run WebContainer in all major browsers, from Chromium-based, to Firefox or Safari TP.

### All major frameworks

Instantly spin up disposable environments running any major modern framework.

### Run Wasm out of the box

Port your favorite language or framework to Wasm to run it in WebContainers. Yes, really.

### Set up in only a few steps

- Boot a WebContainer.
- Populate the container's file system.
- Programmatically install packages.
- Run your development server in-browser.
Read more about setting up WebContainer in your web app.

hello-world.ts

project-files.ts

```plain text
import { WebContainer, FileSystemTree } from '@webcontainer/api';
import { projectFiles } from './project-files.ts';

async function main() {
  // First we boot a WebContainer
  const webcontainer = await WebContainer.boot();

  // After booting the container we copy all of our project files
  // into the container's file system
  await webcontainer.mount(projectFiles);

  // Once the files have been mounted, we install the project's
  // dependencies by spawning `npm install`
  const install = await webcontainer.spawn('npm', ['i']);

  await install.exit;

  // Once all dependencies have been installed, we can spawn `npm`
  // to run the `dev` script from the project's `package.json`
  await webcontainer.spawn('npm', ['run', 'dev']);
}
```

### Build rich development experiences not possible before

Interactive tutorials

Learn SvelteKit, a full stack framework, within their custom editor, running on WebContainers, all in the browser.

learn.svelte.dev

Low code / no code

A stress-free editor enabling non-technical contributors to make their own PRs with a live, disposable preview to confirm an error-free build.

Web Publisher by StackBlitz

AI applications

re:tune is setting the stage for AI-native IDEs - with a copilot that can understand and operate in the full runtime context across server and client.

retune.so

## Support for every team

Small startups, open source maintainers, and Fortune 500 enterprises all enjoy access to StackBlitz's committed product support, features and improvements.

## Slash server costs

WebContainer API only requires the compute power of your local CPU and browser, eliminating the cost and overhead of managing remote servers.

## Ship faster

No additional teams to build or maintain. Leave the technical support to us and focus on actually shipping your product.

## Leverage the tech we use in our own products.

Years of development by our full-time engineering team, front-line feedback from leading community partners, and funded R&D into future technological possibilities make WebContainer more robust by the day.

Get started!


