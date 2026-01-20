---
type: link
source: notion
url: https://github.com/gristlabs/grist-core?tab=readme-ov-file
notion_type: Software Repo
tags: ['Running']
created: 2024-04-05T04:14:00.000Z
---

# GitHub - gristlabs/grist-core: Grist is the evolution of spreadsheets.

## AI Summary (from Notion)
- Overview of Grist: Grist is a modern relational spreadsheet that merges spreadsheet flexibility with database robustness.
- Repositories:
- grist-core: Core repository for running a powerful spreadsheet hosting server.
- grist-electron: Desktop app for viewing/editing spreadsheets.
- grist-static: In-browser build for displaying spreadsheets without back-end support.
- Open Source: All repositories are open source under the Apache License, promoting transparency and community contributions.
- Job Opportunity: Grist is hiring a Systems Engineer to facilitate installation and maintenance.
- Key Features:
- Column functionality similar to databases.
- Supports Python formulas and many Excel functions.
- Self-contained format based on SQLite.
- Drag-and-drop dashboards and visualization tools.
- Access control and user permissions.
- Translations available in multiple languages.
- Integration Capabilities: REST API, Zapier actions, and various import/export options including Google Drive and CSV.
- Community Focus: Emphasizes the importance of community contributions and data portability, maintaining independence from business fluctuations.
- Environment Variables: Numerous configurable options for customization and integration.
- Testing and Development: Automated tests run in CI, with guidance for local testing.
- License: Released under the Apache License, ensuring users can modify and distribute the software.

## Content (from Notion)

# Grist

Grist is a modern relational spreadsheet. It combines the flexibility of a spreadsheet with the robustness of a database.

- grist-core (this repo) has what you need to run a powerful spreadsheet hosting server.
- grist-electron is a Linux/macOS/Windows desktop app for viewing and editing spreadsheets stored locally.
- grist-static is a fully in-browser build of Grist for displaying spreadsheets on a website without back-end support.
The grist-core repo is the heart of Grist, including the hosted services offered by Grist Labs, an NYC-based company 🇺🇸 and Grist's main developer. The French government agency ANCT Données et Territoires 🇫🇷 has also made significant contributions to the codebase.

The grist-core, grist-electron, and grist-static repositories are all open source (Apache License, Version 2.0).

> 

grist.mp4

## 2024 - We're hiring a Systems Engineer!

We are looking for a friendly, capable engineer to join our small team. You will have broad responsibility for the ease of installation and maintenance of Grist as an application and service, by our clients, by self-hosters, and by ourselves. Read the full job posting or jump into the puzzle that comes with it by just running this:

```plain text
docker run -it gristlabs/grist-twist

```

## Features

Grist is a hybrid database/spreadsheet, meaning that:

- Columns work like they do in databases: they are named, and they hold one kind of data.
- Columns can be filled by formula, spreadsheet-style, with automatic updates when referenced cells change.
This difference can confuse people coming directly from Excel or Google Sheets. Give it a chance! There's also a Grist for Spreadsheet Users article to help get you oriented. If you're coming from Airtable, you'll find the model familiar (and there's also our Grist vs Airtable article for a direct comparison).

Here are some specific feature highlights of Grist:

- Python formulas. 
- A portable, self-contained format. 
- Can be displayed on a static website with grist-static – no special server needed.
- A self-contained desktop app for viewing and editing locally: grist-electron.
- Convenient editing and formatting features. 
- Drag-and-drop dashboards. 
- Incremental imports. 
- Integrations. 
- Many templates to get you started, from investment research to organizing treasure hunts.
- Access control options. 
- Self-maintainable. 
- Sandboxing options for untrusted documents. 
- Translated to many languages.
- F1 key brings up some quick help. This used to go without saying, but in general Grist has good keyboard support.
- We post progress on 𝕏 or Twitter or whatever and publish monthly newsletters.
If you are curious about where Grist is heading, see our roadmap, drop a question in our forum, or browse our extensive documentation.

## Using Grist

If you just want a quick demo of Grist:

- You can try Grist out at the hosted service run by Grist Labs at docs.getgrist.com (no registration needed).
- Or you can see a fully in-browser build of Grist at gristlabs.github.io/grist-static.
- Or you can download Grist as a desktop app from github.com/gristlabs/grist-electron.
To get grist-core running on your computer with Docker, do:

```plain text
docker pull gristlabs/grist
docker run -p 8484:8484 -it gristlabs/grist
```

Then visit http://localhost:8484 in your browser. You'll be able to create, edit, import, and export documents. To preserve your work across docker runs, share a directory as /persist:

```plain text
docker run -p 8484:8484 -v $PWD/persist:/persist -it gristlabs/grist
```

Get templates at templates.getgrist.com for payroll, inventory management, invoicing, D&D encounter tracking, and a lot more, or use any document you've created on docs.getgrist.com.

If you need to change the port Grist runs on, set a PORT variable, don't just change the port mapping:

```plain text
docker run --env PORT=9999 -p 9999:9999 -v $PWD/persist:/persist -it gristlabs/grist

```

To enable gVisor sandboxing, set --env GRIST_SANDBOX_FLAVOR=gvisor. This should work with default docker settings, but may not work in all environments.

You can find a lot more about configuring Grist, setting up authentication, and running it on a public server in our Self-Managed Grist handbook.

## Activating the boot page for diagnosing problems

You can turn on a special "boot page" to inspect the status of your installation. Just visit /boot on your Grist server for instructions. Since it is useful for the boot page to be available even when authentication isn't set up, you can give it a special access key by setting GRIST_BOOT_KEY.

```plain text
docker run -p 8484:8484 -e GRIST_BOOT_KEY=secret -it gristlabs/grist

```

The boot page should then be available at /boot/<GRIST_BOOT_KEY>. We are starting to collect probes for common problems there. If you hit a problem that isn't covered, it would be great if you could add a probe for it in BootProbes. Or file an issue so someone else can add it, we're just getting start with this.

## Building from source

To build Grist from source, follow these steps:

```plain text
yarn install
yarn run build:prod
yarn run install:python
yarn start
# Grist will be available at http://localhost:8484/

```

Grist formulas in documents will be run using Python executed directly on your machine. You can configure sandboxing using a GRIST_SANDBOX_FLAVOR environment variable.

- On macOS, export GRIST_SANDBOX_FLAVOR=macSandboxExec uses the native sandbox-exec command for sandboxing.
- On Linux with gVisor's runsc installed, export GRIST_SANDBOX_FLAVOR=gvisor is an option.
- On any OS including Windows, export GRIST_SANDBOX_FLAVOR=pyodide is available.
These sandboxing methods have been written for our own use at Grist Labs and may need tweaking to work in your own environment - pull requests very welcome here!

## Logins

Like git, Grist has features to track document revision history. So for full operation, Grist expects to know who the user modifying a document is. Until it does, it operates in a limited anonymous mode. To get you going, the docker image is configured so that when you click on the "sign in" button Grist will attribute your work to you@example.com. Change this by setting GRIST_DEFAULT_EMAIL:

```plain text
docker run --env GRIST_DEFAULT_EMAIL=my@email -p 8484:8484 -v $PWD/persist:/persist -it gristlabs/grist

```

You can change your name in Profile Settings in the User Menu.

For multi-user operation, or if you wish to access Grist across the public internet, you'll want to connect it to your own Single Sign-On service. There are a lot of ways to do this, including SAML and forward authentication. Grist has been tested with Authentik, Auth0, and Google/Microsoft sign-ins via Dex.

## Translations

We use Weblate to manage translations. Thanks to everyone who is pitching in. Thanks especially to the ANCT developers who did the hard work of making a good chunk of the application localizable. Merci bien!

## Why free and open source software

This repository, grist-core, is maintained by Grist Labs. Our flagship product available at getgrist.com is built from the code you see here, combined with business-specific software designed to scale to many users, handle billing, etc.

Grist Labs is an open-core company. We offer Grist hosting as a service, with free and paid plans. We also develop and sell features related to Grist using a proprietary license, targeted at the needs of enterprises with large self-managed installations.

We see data portability and autonomy as a key value, and grist-core is an essential part of that. We are committed to maintaining and improving the grist-core codebase, and to be thoughtful about how proprietary offerings impact data portability and autonomy.

By opening its source code and offering an OSI-approved free license, Grist benefits its users:

- Developer community. The freedom to examine source code, make bug fixes, and develop new features is a big deal for a general-purpose spreadsheet-like product, where there is a very long tail of features vital to someone somewhere.
- Increased trust. Because anyone can examine the source code, “security by obscurity” is not an option. Vulnerabilities in the code can be found by others and reported before they cause damage.
- Independence. Grist is available to you regardless of the fortunes of the Grist Labs business, since it is open source and can be self-hosted. Using our hosted solution is convenient, but you are not locked in.
- Price flexibility. If you are low on funds but have time to invest, self-hosting is a great option to have. And DIY users may have the technical savvy and motivation to delve in and make improvements, which can benefit all users of Grist.
- Extensibility. For developers, having the source open makes it easier to build extensions (such as Custom Widgets). You can more easily include Grist in your pipeline. And if a feature is missing, you can just take the source code and build on top of it.
For more on Grist Labs' history and principles, see our About Us page.

## Sponsors

## Reviews

- Grist on ProductHunt
- Grist on AppSumo (life-time deal is sold out)
- Capterra, G2, TrustRadius
## Environment variables

Grist can be configured in many ways. Here are the main environment variables it is sensitive to:

### AI Formula Assistant related variables (all optional):

At the time of writing, the AI Assistant is known to function against OpenAI chat completion endpoints for gpt-3.5-turbo and gpt-4. It can also function against the chat completion endpoint provided by llama-cpp-python.

### Sandbox related variables:

### Forward authentication variables:

Forward authentication supports two modes, distinguished by GRIST_IGNORE_SESSION:

1.   
1.  
- GRIST_IGNORE_SESSION: set to true. Grist sessions will not be used.
- Make sure your reverse proxy sets the header you specified for all requests that may need login information. It is imperative that this header cannot be spoofed by the user, since Grist will trust whatever is in it.
When using forward authentication, you may wish to also set the following variables:

- GRIST_FORCE_LOGIN=true to disable anonymous access.
### Plugins:

Grist has a plugin system, used internally. One useful thing you can do with it is include custom widgets in a build of Grist. Custom widgets are usually made available just by setting GRIST_WIDGET_LIST_URL, but that has the downside of being an external dependency, which can be awkward for offline use or for archiving. Plugins offer an alternative.

To "bundle" custom widgets as a plugin:

- Add a subdirectory of plugins, e.g. plugins/my-widgets. Alternatively, you can set the GRIST_USER_ROOT environment variable to any path you want, and then create plugins/my-widgets within that.
- Add a manifest.yml file in that subdirectory that looks like this:
```plain text
name: My Widgets
components:
  widgets: widgets.json

```

- The widgets.json file should be in the format produced by the grist-widget repository, and should be placed in the same directory as manifest.yml. Any material in plugins/my-widgets will be served by Grist, and relative URLs can be used in widgets.json.
- Once all files are in place, restart Grist. Your widgets should now be available in the custom widgets dropdown, along with any others from GRIST_WIDGET_LIST_URL.
- If you like, you can add multiple plugin subdirectories, with multiple sets of widgets, and they'll all be made available.
### Google Drive integrations:

### Database variables:

### Testing:

## Tests

Tests are run automatically as part of CI when a PR is opened. However, it can be helpful to run tests locally before pushing your changes to GitHub. First, you'll want to make sure you've installed all dependencies:

```plain text
yarn install
yarn install:python

```

Then, you can run the main test suite like so:

```plain text
yarn test

```

Python tests may also be run locally. (Note: currently requires Python 3.9 - 3.11.)

```plain text
yarn test:python

```

For running specific tests, you can specify a pattern with the GREP_TESTS variable:

```plain text
env GREP_TESTS=ChoiceList yarn test
env GREP_TESTS=summary yarn test:python

```

## License

This repository, grist-core, is released under the Apache License, Version 2.0, which is an OSI-approved free software license. See LICENSE.txt and NOTICE.txt for more information.


