---
type: link
source: notion
url: https://github.com/andymatuschak/orbit
notion_type: Software Repo
tags: ['Running']
created: 2024-02-18T13:50:00.000Z
---

# GitHub - andymatuschak/orbit: Experimental spaced repetition platform for exploring ideas in memory augmentation and programmable attention

## AI Summary (from Notion)
- Project Overview: Orbit is an experimental spaced repetition platform aimed at memory augmentation and enhancing user engagement with tasks over time.
- Focus: Primarily serves as a research vehicle with an emphasis on understanding spaced repetition systems rather than feature completion.
- Target Audience: Authors interested in integrating Orbit into their texts, offering preliminary documentation for guidance.
- Functionality:
- Manages a collection of tasks and their schedules.
- Tasks can be sourced from APIs, embedded iframes, or local services.
- Supports completion across web, desktop, and mobile applications.
- Technical Aspects:
- Developed as a mono-repo with various modular packages written in Typescript.
- Includes components for both backend and frontend operations.
- Licensing:
- Open-source under Apache License 2.0.
- Client applications available under AGPL3+ or BUSL1.1, allowing non-production use.
- Contributing:
- Currently focused on research; open to serious contributors but not seeking broad community engagement.
- Requires signing a Contributor Agreement for contributions.
- Acknowledgements:
- Created by Andy Matuschak with contributions from various patrons.
- Funded through a Patreon community to maintain a free service.
- Interesting Fact: The platform is inspired by the concept of a "mnemonic medium," a collaborative idea with Michael Nielsen.

## Content (from Notion)

# Orbit

Orbit is an experimental platform for publishing and engaging with small tasks repeatedly over time. In the short term, it's focused on supporting the "mnemonic medium", a way of augmenting texts so that readers can easily remember all the key details. For an example, see Quantum Country, a textbook on quantum computation. More abstractly, Orbit aspires to offer a more general form of spaced repetition systems like Anki, as part of a connected cloud service. Learn more on the home page.

Orbit stores a collection of tasks and manages their schedules. Tasks can be ingested from around the web, via APIs or embedded iframes, or through various services running on your local computer. You can complete scheduled tasks in desktop, mobile, and web applications. A backend service syncs user data and orchestrates notifications.

You should also understand that Orbit is (for now) first and foremost a vehicle for research. We hope that it's useful, of course, but the main goal is not implementing features or polishing loose screws. We're focused on trying to understand the scope of systems like this, and what they one day want to become.

If you’re an author interested in using Orbit in your own texts, please view the preliminary documentation.

## Packages

This is Orbit's mono-repo, comprising many modular packages. You'll want to run yarn install in the root to install dependencies before doing anything else.

While everything is written in Typescript, components of Orbit must run in Node, web browsers, and react-native environments, which can require some care. See the table below for an overview, and see Readme files in individual package folders for details on each package.

## Contributing

Thank you for your interest in contributing!

Orbit's just been open-sourced; we haven't yet created consistent processes and venues for discussing ongoing development plans. Those will come (hopefully) soon!

Please understand that (for now), Orbit does not aspire to be a typical open-source project, soliciting open-ended contributions and participation from a large community. Orbit is primarily a vehicle for research; its direction is determined by Andy Matuschak and direct collaborators. We'll strive to keep the process open to input and relatively transparent. But open-source community engagement can be extremely time-consuming, and we have to keep our focus on the research.

That said, we're excited to work with serious contributors! Let's just get to know each other, ease into the relationship. If you're interested in participating, a great way to start would be by engaging with existing issues on GitHub, particularly those marked "help wanted." If you're game for implementing something substantial that we've been putting off, we'll be excited to invest time into a collaboration. If you find a bug in Orbit, we'd be grateful for issues with accompanying pull requests. If you'd like to contribute substantively but you're not sure how to start, please email Andy.

One more thing: as with many open-source projects, you'll need to sign a Contributor Agreement to contribute to Orbit. A bot will prompt you to do this when you open your first pull request. The agreement asks you to jointly assign copyright; that is, you retain all your own rights to the contribution, but share them with us. And we pledge that your work will be released under an FSF/OSI-approved license. See this FAQ if you have questions (our agreement is the same as Oracle's, but with names swapped).

## License

Orbit is open-source. We use an unusual licensing strategy intended to be as permissive as possible while discouraging commercial copy-cats. Here's a summary; see the LICENSE files and details in each package for more:

- All libraries are provided under the permissive Apache License 2.0.
- The Orbit client application and cloud service sources are provided under your choice of two licenses: 
- Official compiled binaries of the Orbit applications will be distributed under the Apache License 2.0 (so that organizations terrified of AGPL can install the end-user binaries onto their machines).
## Acknowledgements

Orbit was created by Andy Matuschak. It continues to develop the concept of the "mnemonic medium" co-created with Michael Nielsen. Orbit is a free service; our Patreon community helps it stay that way. You can become a member to support the work, and to read regular patron-only articles and previews of upcoming projects.

Thanks in particular to my sponsor-level patrons: Adam Marblestone, Adam Wiggins, Andrew Sutherland, Ben Springwater, Bert Muthalaly, Boris Verbitsky, Calvin French-Owen, Dan Romero, David Wilkinson, fnnch, James Hill-Khurana, James Lindenbaum, Jesse Andrews, Kevin Lynagh, Lambda AI Hardware, Ludwig Petersson, Maksim Stepanenko, Matt Knox, Mickey McManus, Mintter, Nathan Lippi, Patrick Collison, Paul Sutter, Peter Hartree, Ross Boucher, Russel Simmons, Salem Al-Mansoori Sana Labs, Thomas Honeyman, Tim O’Reilly, Todor Markov, Tom Berry, Tooz Wu, William Clausen, William Laitinen, Yaniv Tal.


