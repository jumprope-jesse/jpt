---
type: link
source: notion
url: https://supabase.com/blog/supabase-bootstrap
notion_type: Software Repo
tags: ['Running']
created: 2024-04-16T02:36:00.000Z
---

# Supabase Bootstrap: the fastest way to launch a new project

## AI Summary (from Notion)
- Supabase Bootstrap: A tool for quickly launching new hosted Supabase projects using starter templates.
- Easy Setup: Users can start a project without installing the CLI, requiring only npm or bun.
- Command: The primary command to initiate is npx supabase bootstrap, which prompts for a starter template.
- Template Repository: Starter templates are available on GitHub and automatically updated for users.
- Local Development: The CLI downloads template files to a local directory upon selection.
- GitHub Rate Limits: Downloading templates too frequently may hit rate limits; setting a GITHUB_TOKEN can help.
- Production Deployment: The bootstrap process creates a new Supabase project and links it to the local environment.
- Migration Files: Users are prompted to push migration files to set up the remote database schemas.
- Credentials Management: Important to store database credentials securely to prevent unauthorized access.
- Local Application Launch: The CLI suggests a start command to run the application locally after setup.
- Future Development: More templates and community contributions are expected to enhance the Supabase Bootstrap experience.

## Content (from Notion)

Supabase bootstrap is the fastest to spin up a new hosted Supabase project from existing starter templates:

1npx supabase bootstrap

This brings a “shadcn”-like experience to Supabase, creating a project locally and launching a remote database ready for deployment.

## Getting started

From any local directory, run supabase bootstrap and you will be prompted to choose a starter template. And the best thing is, you don't even need to install the CLI to get started! As long as you have npm or bun installed, you're ready to go!

- CLI: supabase bootstrap
- NPM: npx supabase@latest bootstrap
- Bun: bunx supabase@latest bootstrap
Bootstrap getting started

## How templates work

The list of starter templates is published on GitHub as samples.json. Whenever we (and in the future the community) add a new starter, it will automatically become available to all Supabase users.

The template repository typically includes the full frontend code, following the file structure below:

- A supabase directory with config.toml and migrations files (if any).
- A .env.example file that defines a list of environment variables for CLI to populate project credentials. We currently support the same list of credentials as our Vercel integration. If a .env file doesn't exist, the CLI will create it for you.
### Local development

After selecting a starter, the Supabase CLI downloads all files from the template repository to your chosen local directory.

### GitHub rate limits

You may run into GitHub rate limit when downloading too frequently from template repository. This can be avoided by setting GITHUB_TOKEN environment variable locally to your GitHub personal access token.

This model is very similar to the popular shadcn workflow. After files are creating in your local repo, you can modify them and check them into source control.

### Deploying to production

During the supabase bootstrap process, a new project will be created on the Supabase platform and linked to your local environment. This command will run you through the account creation flow if you don't already have one.

Bootstrap getting started

### Some patience required

Linking to your new hosted project may take a short while as it needs to spin up a new database in the cloud.

Once the linking is completed, you will be prompted to push any template migration files to your new hosted project. These migration files will setup your remote database with the necessary schemas to support the starter application.

Bootstrap getting started

After pushing the migrations, your project credentials will be exported to a .env file for you to connect from any frontend or backend code. The default environment variables include:

- POSTGRES_URL
- SUPABASE_URL
- SUPABASE_ANON_KEY
- SUPABASE_SERVICE_ROLE_KEY
Other custom variables from .env.example file defined by your chosen template will also be merged to your local .env file.

### Store credentials securely

It is important to store these credentials securely as anyone can connect to your remote database using the POSTGRES_URL.

## Start developing

Finally, the CLI will suggest a start command to launch your application locally. Starting the local app will use credentials defined in .env file to connect to your new hosted project.

Bootstrap getting started

## Template library

And that's it, with a single command, you can get a new project up and running end to end.

Supabase Bootstrap makes it even easier to get started with Supabase, mobile app tools, and web development frameworks like Next.js, Expo React Native, Flutter, Swift iOS.

We have many many more templates coming soon, and we'll be opening it up to community contributions. Stay tuned!

## Get started

Visit the Supabase CLI docs to get started with supabase bootstrap.


