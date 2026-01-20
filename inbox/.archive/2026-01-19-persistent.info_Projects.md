---
type: link
source: notion
url: https://blog.persistent.info/p/projects.html?m=1
notion_type: Software Repo
tags: ['Running']
created: 2024-03-28T03:04:00.000Z
---

# persistent.info: Projects

## AI Summary (from Notion)
- The document is a comprehensive list of various projects the author has been involved in, organized by year from 2003 to 2024.
- Key Projects:
- 2023: Shortcuts automation for Tailscale.
- 2022: Implemented Fast User Switching for Tailscale and contributed to Infinite Mac emulators.
- 2021: Created Git Resource Fork Hooks to preserve resource forks in Git.
- 2019: Led TypeScript migration efforts at Quip.
- 2018: Developed Quip Slides for Dreamforce 2018.
- 2016: Created Instagram Downloader for easier photo downloads.
- 2015: Developed Closure Compiler support for React.
- 2011: Intersquares, a finalist in Foursquare's hackathon.
- 2006: Delicious to Google Bookmarks tool became popular during the shutdown rumors of Delicious.
- Major Themes:
- Continuous innovation in software development, particularly in user experience and automation.
- The evolution of technology, with a focus on adapting to new frameworks (e.g., moving from JavaScript to TypeScript).
- Contributions to both personal projects and larger organizational initiatives (e.g., Quip).
- Interesting Facts:
- The author has a history of developing tools that enhance existing platforms (e.g., Chrome extensions, APIs).
- Many projects reflect a response to industry trends, such as the shift from Flash to HTML5.
- The longevity and adaptation of projects like RetroGit and Overplot highlight ongoing relevance despite platform changes.
- Takeaways:
- There is a strong emphasis on open-source contributions and sharing knowledge through blog posts and source code availability.
- The narrative showcases a blend of individual initiative and collaborative efforts within teams across various tech companies.

## Content (from Notion)

An incomplete list of projects I have been involved in, currently being back-filled.

## 2023

Shortcuts automation to turn on Tailscale when leaving an address

### Tailscale Shortcuts Actions

I implemented Shortcuts support for Tailscale's iOS and macOS apps. In addition to the feature work, this required some app modernization (doing in-app intent handling depends on migrating to the UIScene APIs). This blog post has more details, but all of the interesting work was on the closed source side of Tailscale.

Current status: Alive and well.

## 2022

Tailscale user switching UI screenshot

### Tailscale Fast User Switching

I implemented the API endpoints, Mac UI and related Mac infrastructure for Tailscale's fast user switching. This blog post has more details, and the open source part of the work is attached to this GitHub issue.

Current status: Alive and well.

Infinite Mac emulating System 7.5.3

### Infinite Mac

WebAssembly/Emscripten port of classic Mac emulators, along with integration with web APIs to allow fast loading, data import and export, and networking support. Initially launched at system7.app and macos8.app, there is now a full collection of system software versions available at infinitemac.org. There's a launch blog post with more details, as well as several subsequent ones with follow-up work. Source code (including for the emulator forks) is also available.

Current status: Alive and well.

## 2021

Example diff of a STR# resource

### Git Resource Fork Hooks

Born out of a desire to archive to a Git repo the Mac software that I wrote under the "Mscape Software" label. Being from the late-90s-to-early-2000s, resource forks were heavily used, and I was unhappy with any of the existing ways of preserving them. I ended up implementing my own pre-commit and post-checkout hooks that extract out resork forks into parallel .r files that can have structured diffs. This blog post has more details, and source code is available. There's also a post about archiving Mscape Software to GitHub and that repo is public as well.

Current status: Alive and well.

## 2019

Quip TypeScript migration documents

### Quip TypeScript Migration

I led the efforts of Quip's client infra team (Rafael Weinstein, Shrey Banga and Erik Arvidsson) to modernize our frontend codebase. We started out with a JSDoc-type-annotated JavaScript codebase that used React.createClass, mixins and global scoping and was type checked, bundled and minified with Google's Closure Compiler. Over a series of "flag day" migrations in mid-2019 we gradually transformed it into a TypeScript codebase that used ECMAScript modules and classes and a Vite- and Rollup-based toolchain. There are a couple of entries on Quip's blog with more details: part one describes the process that we chose, and part two has some anecdotes about how it worked out in practice.

Current status: The same infrastructure was still in place when I left Quip in early 2022.

## 2018

Stylized depiction of Quip Slides

### Quip Slides

I started the initial explorations and ended up leading the team that delivered Quip Slides for Dreamforce 2018. The most interesting parts involved finding ways to take the work from the previous 6 years in building Quip text and spreadsheets and making it work in this new environment. I did not get a chance to write any technical blog posts, but I did keep some notes on the different approaches we considered for doing content scaling (one of ways in which slides differed from other content). This page shows 4 different techniques and the commits have few more details.

Current status: Quip slides was retired in early 2021 (as the team priorities changed).

## 2017

Example Quip document with embedded live apps

### Quip Live Apps

I was a "pathfinder" for the team that developed Quip's Live apps capability. Live Apps allow embedding of interactive, offline-capable, mobile-friendly third-party content into documents. This included research into making the Quip rich text editing component available to third-party apps, exploring ways of allowing iframed content to extend beyond a simple rectangle, making demo apps, tracking down (and working around) browser issues and many other things that culminated in a Dreamforce 2017 launch.

Current status: Live Apps are still the primary way to extend Quip's functionality.

## 2016

Instagram Downloader screenshot

### Instagram Downloader

My wife wanted an easy way to download photos from Instagram, ideally in a less lossy and tedious way than taking screenshots. While there were existing Chrome extensions that seemed to do this, they seemed shady and/or inefficient (as far as which permissions they required). I had not written an extension for a few years, and this was a good exercise in using the new-at-the-time activeTab and declarativeContent APIs to minimize the permissions needed. Source code is available.

Current status: I had to change the name and it's required some upkeep over the years as Instagram's markup has changed, but it still appears to work as of early 2023.

## 2015

React.createClass component with JSDoc

### Closure Compiler support for React

Quip started to heavily adopt React in late 2014, and a few months into it we realized that we were giving up a lot of type safety in the process. We had been heavily reliant on Closure Compiler to do type checking, but React's API at the time (with React.createClass and mixins) did a lot of runtime type generation that the compiler did not know about. I ended up writing a custom compiler pass that extracted component type definitions and applied them at creation time. This blog post has more details, and source code is available.

Current status: in addition to track React releases, the compiler pass was extended over the years, gaining support for type checking props in 2016, size optimizations in 2017, state in 2018, ES6 modules and classes in 2019. However, Quip completed the migration to TypeScript in late 2019, at which point this tooling was no longer needed.

## 2014

RetroGit screenshot

### RetroGit

RetroGit is a simple tool that sends you a daily (or weekly) digest of your GitHub commits from years past. Use it as a nostalgia trip or to remind you of TODOs that you never quite got around to cleaning up. Think of it as Timehop for your codebase. This blog post has more details, and source code is available.

Current status: Alive and well.

Sample output of dex-method-counts tool, showing per Java package method counts

### dex-method-counts

dex-method-counts is a simple tool to parse Android APK or DEX archives and output per-package method counts. The DEX file format has a 64K method limit that we were running into at Quip, mostly due to code generated from protocol buffer definitions. We needed to know which packages were the biggest culprits (so that we could do some shor-term bandaid fixes), and none of the existing tools of the time had useful output. I wrote a quick-and-dirty tool using an existing DEX format parser. It was enough to unblock us, but we released it in case it was useful to others. This blog post has more details, and source code is available.

Current status: I didn't do much Android development after 2014, so I have not maintained the tool — there are quite a few forks so it must still be useful to some. multidex is also still a thing, though it's mostly transparent to developers.

## 2013

Screenshot of Quip's initial iPad app

### Quip

I was a founding engineer of Quip, and worked on many things leading up to the initial launch in July 2013. These ranged from core product features (lists, tables, images) to infrastructure (Closure Compiler integration and other build tooling, error reporting) to sundry debugging.

Current status: Quip was acquired by Salesforce in 2016. It continues to live on as a product, and is also powering Slack's canvas.

## 2012

Cilantro screenshot

### Cilantro

Cilantro was a Chrome extension to share pages via Avocado. Ann and I had been using the app for shared tasks lists, and after the removal of social features from Google Reader, we wanted to give it a shot for sharing of links too. This blog post has more details, and source code is available.

Current status: We stopped using the app sometime in 2013, Avocado itself shut down in 2017, and the Chrome Web Store took down the extension in 2023.

Chrome packaged appss introduction slide

### Chrome Apps

I was the tech lead of the Chrome Apps team from early 2011 to late 2012. I worked on a few things during that time, most notably packaged apps, which aimed to make it possible to build native-caliber apps using Chrome as a runtime (i.e. a proto-Electron). Chrome packaged apps were launched at Google I/O 2012 and I wrote a blog post around that time with more details. There is also a follow-up blog post about the Chrome Apps API REPL that I built as both a learning tool and to serve as a sample app.

Current status: Chrome Apps were deprecated in 2016. There have been multiple updates to the deprecation timeline over the years, and currently they are scheduled to be removed from Chrome OS (the last platform where they are supported) in 2025.

Playback Rate Screenshot

### Playback Rate

Playback Rate was a Chrome extension to easily control the playback rate of videos embedded in web pages, back when sites were starting to switch from Flash-based video playback to the HTML5 <video> tag. This blog post has more details, and source code is available.

Current status: The extension was swept up in a 2020 Chrome Web Store requirement requiring that privacy fields be filled out, and was eventually de-listed. It's still installable from source as an unpacked/developer mode extension. It could probably be redone to use the activeTab permission and thus have a much smaller permission footprint.

## 2011

Intersquares screenshot

### Intersquares

Intersquares was my entry into Foursquare's global hackathon (it ended up being a finalist). It computes the locations where two Foursquare users have been together, and has a social media integration for finding intersections with others. This was my first hackathon, and it was a lot of fun, though I did feel pretty exhausted coming into work on Monday after coding all weekend. This blog post has more details, and source code is available.

Current status: Though I dutifully renew the domain name, I never migrated the project off of the App Engine Python 2.5 runtime and thus it stopped working in 2017.

## 2010

Source Quicklinks screenshot

### Source Quicklinks

Source Quicklinks was a Chrome extension to help navigate Chrome's codebase. I first created it as I was joining on the Chrome team (and ending up with too many tabs), but it found a second life when I started to do more browser spelunking while at Quip. It made it easy to jump from code search results to blame views, and had pointers to upstream repositories for dependencies (e.g. V8). After the Blink/WebKit fork it also gained ability to view the equivalent file from one project in the other (when the divergence wasn't too great). This blog post has more details, and source code is available.

Current status: Though it has survived various Chrome Web Store extension purges, the sites that the extension stiched together either don't exist anymore (e.g. WebKit no longer uses Trac) or have changed significantly (Chromium's code search), thus the functionality has rotted over time.

## 2009

PuSH Bot screenshot

### PuSH Bot

PuSH Bot made it easy to subscribe to feeds and get notifications for new items a chat client. The subscription part relied on feeds supporting PubSubHubbub (a precursor to WebSub) that allowed webhook-like callbacks to be registered for RSS and Atom feeds. The chat notification used XMPP, an open protocol that was supported by Google App Engine and Google Talk. This blog post and follow-up have more details, and source code is available.

Current status: The site is still up, but Google App Engine deprecated XMPP support in 2016, and removed it in 2017.

## 2008

Mail Trends screenshot

### Mail Trends

Mail Trends is a tool to visualize various statistics about about an IMAP email account, especially a Gmail-hosted one. I was on a "if you can measure it, you can win it" kick, and though that having more insights into my email would allow me to better stay on top if it. This blog post has more details, and source code is available. There is also sample output from running it over the Eron Email corpus.

Current status: Archived, I have not tried to run it in over 10 years (as it turned out, getting more stats did not help with the firehose of email). Gmail still has an IMAP interface, but this is a Python 2 codebase that would require significant modernization.

## 2007

### plusplusbot

plusplusbot is a "karma bot" for Twitter. It monitors tweets about a topic with a ++ (plusplus) or -- (minusminus) operator and update a score for that target. This blog post has more details, and source code is available.

Current status: Archived, has not run since November 2009. The service relied on an "auto-friend" flag (where it would automatically follow anyone that followed it), which Twitter has since removed.

## 2006

delicious2google screenshot

### Delicious to Google Bookmarks

A simple tool to export del.icio.us Delicious bookmarks to Google Bookmarks. Both sites had APIs (semi-public in Google's case), but there was no easy way to move data between them. This blog post has more details, and source code is available.

Current status: The tool suddenly became popular in 2010, when rumors that Yahoo! would be shutting down Delicious surfaced. Since the initial creation of the tool, Yahoo! had started a migration of user accounts, which meant that the authentication system would not work for this subset of users. I reworked the tool to handle both kinds of accounts, this blog post has more details. A few months later Google incorporated the functionality into its Bookmarks product directly. In the years that followed Delicious changed hands three more times before being shut down in 2017. The tool also stoopped working in 2017 because it ran on the App Engine Python 2.5 runtime which was end-of-lifed that year. Finally, Google Bookmarks itself was shut down in 2021. This tool is deader than a doornail.

Overplot screenshot

### Overplot

Overplot is a mashup between Overheard in New York and Google Maps. I was living in New York at the time, and wanted to visualize things around neighborhoods I knew. The project had surprising technical depth (plotting thousands of markers in Google Maps was hard back then, as was geocoding thousands of hand-entered addresses) and social discoveries (who even decides New York neighborhood boundaries). This blog post has more details, and source code is available.

Current status: Surprisingly, it still works. I had to do some up-keep in 2013 to port it to the more modern Google Maps API, but it has kept working since then. The quotes are still the ones from 2006 though, the scraping mechanism relied on the site's RSS feed being archived by Google Reader (RIP).

Charts in Sourcerer screenshot

### Sourcerer Charts

Sourcerer was an internal Google service created by Jorg Brown that provided very fast browsing of Google's monorepo, back when the source of truth was Perforce servers that always struggled under load. Jorg had the realization that all the metadata could fit in RAM, and built an alternate view that was very useful for browsing. I started using in 2005 (when I was on a build cop rotation and needed to quickly track down changes), and made some small improvements to it over the next few years.

My most significant contribution was using it to generate charts of change frequencies by author, directory or description matches. Besides being a navel-gazing sort of tool in the days before GitHub contribution graphs, it also allowed project activity to be tracked and patterns to be observed over time (e.g. how many changes mention "XSS").

Current status: Unknown, but presumably dead. Sourcerer (and its charts) were running when I left Google in 2012 (screenshot is from my last week week at Google), but ChartServer (the service used for rendering charts) was supposed to be turned off in 2019 and I would be surprised if Sourcerer was ported to Piper.

## 2005

Google Reader screenshot

### Google Reader 1.0

I was an initial member of the Google Reader team (this post has the backstory of how I came to join the team, and this one was posted shortly after the launch with a few more details). I worked mostly on frontend things leading up to its launch at the Web 2.0 conference. This blog post captures the initial UI, which deviated from the traditional multi-pane UI of the time in attempt to present a simpler view non-early adopters.

Current status: The initial UI of Google Reader was superseded by the relaunch the following year. Reader as a product was put into maintenance mode in 2010, and shut down in 2013.

Gmail macros screenshot

### Gmail Greasemonkey Scripts

I used the Greasmonkey Firefox extension to add features that I found missing in ealy versions of Gmail. Saved searches was the first feature I added, followed by preview bubbles, keyboard macros, label colors, and a Google Reader integration. While it might seem odd to write external scripts to modify Gmail (when I was working at Google at the time), it was much faster to hack on the product this way (versus trying to contribute officially in 20% time). Source code for all of the scripts is available, and they were even featured in a book.

Current status: There was a significant Gmail infrastructure change in late 2007, adding semi-official Greasemonkey support, and I ported my most popular script over. However, over time Gmail's feature set caught up with what the scripts provided (more keyboard shortcuts, colored labels, a preview pane, etc.) and the need for them lessened. They have rotted over time, and are no longer maintained.

## 2004

Gmail custom skin screenshot

### Gmail Skinning

I used Firefox's custom user stylesheet supported to develop an alternate appearance for Gmail shortly after it was launched. This was in a pre-Greasemonkey, pre-Firebug world, thus being able to reverse-engineer Gmail's DOM structure and inject CSS into it was more of a challenge. This blog post has more details, and skin stylesheet is available. Fun fact: the color scheme was inspired by Drew Olbrich's Garry project (which in turn was inspired by Edward Tufte).

Current status: The stylesheet targeted specific class names and DOM structure, which eventually changed (certainly with the late-2007 Gmail re-architecture), and thus the stylesheet stopped working.

## 2003

pTunes Screenshot

### pTunes

pTunes was a browsable catalog of music shared via SMB on the Princeton campus network. While other homegrown projects to crawl file shares existed, I wanted to experiment with an user-friendly iTunes-inspired UI, complete with cover art, cleaned up metadata, genre information, and de-duplication. I eventually turned my project into my junior year second semester indepedent work. The pTunes label on my blog is based on my status updates, and the final project writeup is also available.

Current status: The service was used internally at Princeton for a few months, but I removed public access to it in April 2003 when the RIAA sued another student for a similar search engine project. I explored resurrecting it as an iTunes Rendezvous/Bonjour shared music browser, but I never got around to completing that work.


