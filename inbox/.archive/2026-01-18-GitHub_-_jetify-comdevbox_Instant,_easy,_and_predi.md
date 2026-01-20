---
type: link
source: notion
url: https://github.com/jetify-com/devbox
notion_type: Software Repo
tags: ['Running']
created: 2024-07-10T15:23:00.000Z
---

# GitHub - jetify-com/devbox: Instant, easy, and predictable development environments

## AI Summary (from Notion)
- Project Overview: Devbox is a command-line tool for creating isolated development environments tailored to specific project needs.
- Key Features:
- Allows definition of packages required for development, similar to a package manager at the OS level.
- Supports over 400,000 package versions from the Nix Package Registry.
- Provides a consistent shell for all team members using a devbox.json file.
- Enables trying new tools without affecting the local system.
- Isolates environments to avoid conflicts between different project dependencies.
- Offers portability across local shells, Docker containers, and cloud environments.
- Quickstart Guide: Steps to initialize and use Devbox for creating a development shell with specific tools.
- Community and Contribution: Encourages community interaction through Discord, GitHub Issues for reporting bugs or features, and welcomes contributions to the open-source project.
- Additional Resources: Links to documentation, CLI commands, and community channels provided for further learning and engagement.
- License: The project is open-source under the Apache 2.0 License.

## Content (from Notion)

# Devbox

### Instant, easy, and predictable development environments

## What is it?

Devbox is a command-line tool that lets you easily create isolated shells for development. You start by defining the list of packages required by your development environment, and devbox uses that definition to create an isolated environment just for your application.

In practice, Devbox works similar to a package manager like yarn – except the packages it manages are at the operating-system level (the sort of thing you would normally install with brew or apt-get). With Devbox, you can install over 400,000 package versions from the Nix Package Registry

Devbox was originally developed by Jetify and is internally powered by nix.

## Demo

You can try out Devbox in your browser using the button below:

The example below creates a development environment with python 2.7 and go 1.18, even though those packages are not installed in the underlying machine:

## Installing Devbox

Use the following install script to get the latest version of Devbox:

```plain text
curl -fsSL https://get.jetify.com/devbox | bash
```

Read more on the Devbox docs.

## Benefits

### A consistent shell for everyone on the team

Declare the list of tools needed by your project via a devbox.json file and run devbox shell. Everyone working on the project gets a shell environment with the exact same version of those tools.

### Try new tools without polluting your laptop

Development environments created by Devbox are isolated from everything else in your laptop. Is there a tool you want to try without making a mess? Add it to a Devbox shell, and remove it when you don't want it anymore – all while keeping your laptop pristine.

### Don't sacrifice speed

Devbox can create isolated environments right on your laptop, without an extra-layer of virtualization slowing your file system or every command. When you're ready to ship, it'll turn it into an equivalent container – but not before.

### Good-bye conflicting versions

Are you working on multiple projects, all of which need different versions of the same binary? Instead of attempting to install conflicting versions of the same binary on your laptop, create an isolated environment for each project, and use whatever version you want for each.

### Take your environment with you

Devbox's dev environments are portable. We make it possible to declare your environment exactly once, and use that single definition in several different ways, including:

- A local shell created through devbox shell
- A devcontainer you can use with VSCode
- A Dockerfile so you can build a production image with the exact same tools you used for development.
- A remote development environment in the cloud that mirrors your local environment.
## Quickstart: Fast, Deterministic Shell

In this quickstart we’ll create a development shell with specific tools installed. These tools will only be available when using this Devbox shell, ensuring we don’t pollute your machine.

1. 
1.   
1.   
1.  
1.   
1.   
1.  
1.  
Read more on the Devbox docs Quickstart.

## Additional commands

devbox help - see all commands

See the CLI Reference for the full list of commands.

## Join our Developer Community

- Chat with us by joining the Jetify Discord Server – we have a #devbox channel dedicated to this project.
- File bug reports and feature requests using Github Issues
- Follow us on Jetify's Twitter for product updates
## Contributing

Devbox is an opensource project so contributions are always welcome. Please read our contributing guide before submitting pull requests.

Devbox development readme

## Related Work

Thanks to Nix for providing isolated shells.

## Translation

- Chinese
- Korean
## License

This project is proudly open-source under the Apache 2.0 License


