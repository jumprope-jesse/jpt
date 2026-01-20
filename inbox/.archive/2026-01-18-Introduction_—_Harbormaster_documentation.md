---
type: link
source: notion
url: https://harbormaster.readthedocs.io/en/latest/
notion_type: Software Repo
tags: ['Running']
created: 2024-04-05T04:42:00.000Z
---

# Introduction — Harbormaster documentation

## AI Summary (from Notion)
- Introduction to Harbormaster: A lightweight container orchestrator designed for running multiple Docker Compose applications on a single host.
- Key Features:
- Automatic deployments and restarts by pushing to a Git repository.
- Ideal for users who find Kubernetes too complex for their needs.
- Getting Started:
- Users create a directory and configuration file (harbormaster.yml) to define applications and their sources.
- Running Harbormaster can be done via a Docker command without prior installation.
- Operational Overview:
- Harbormaster periodically checks the defined repository for changes and updates the application accordingly.
- Data Management:
- Applications can persist data neatly under a specified directory, provided by Harbormaster.
- Users can customize volume mounts in their Compose files for data and cache management.
- Limitations:
- Harbormaster does not provide ingress; users must set up their own.
- Useful Resources: Links to further documentation on data handling and installation are provided for user convenience.

## Content (from Notion)

A vector graphics man in naval uniform.

Do you have apps you want to deploy to a server, but Kubernetes is way too heavy? Harbormaster is for you.

Harbormaster is a small container orchestrator that lets you run multiple Docker Compose applications on a single host, with automatic deploys/restarts, simply by pushing to a git repo.

## Running your first app

Here’s how to get started with Harbormaster:

Create a new directory somewhere, and cd into it:

```plain text
$ mkdir mydir
$ cd mydir

```

Create a file in it called harbormaster.yml, with these contents:

```plain text
apps:
  hello_world:
    url: https://gitlab.com/stavros/harbormaster.git
    compose_config:
    - apps/hello_world/docker-compose.yml

```

This is the configuration file that tells Harbormaster what to run. This will run the “Hello world” app from the Harbormaster repository itself.

Then, run Harbormaster (no need to have it installed beforehand):

```plain text
$ docker run \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v (pwd):/config \
    -v (pwd):/main \
    stavros/harbormaster

```

You should see Docker pull down the Harbormaster container, start it, and then Harbormaster will look at its configuration file, pull the repo, and run the Compose app inside.

Now, visit http://localhost:8000, and Harbormaster will greet you.

You can press Ctrl-C to stop Harbormaster, and docker stop <container id> to stop the app. You will notice that Harbormaster has created various directories (cache, data, repos) in your directory. That’s where Harbormaster stores everything.

## How does it work?

Let’s say you have a bog-standard Compose-packaged app in a git repository:

```plain text
services:
  main:
    build: .
    volumes:
      - ./data:/app_data
    ports:
      - 8080:8080
    restart: unless-stopped

```

You want this deployed onto some server, but you want something that can check your repo every so often, see if there are any changes, and deploy/restart your app if so.

That’s what Harbormaster does. You run its Docker container on the server, and give it a config file:

```plain text
apps:
  myapp:
    url: github.com/yourusername/myapp.git

```

Harbormaster will look at its config file, clone the myapp repo, and run docker
compose up on it. Harbormaster will run periodically, pull the repo, and restart your Docker containers if there’s a change.

NOTE: Harbormaster does not provide ingress, you’ll need to bring your own. It just runs your apps.

## What about my data, though?

Excellent question, your application has data you want to persist. For tidiness, Harbormaster provides its own mountpoint where you should persist the data (for more information on this, see the handling data directories section).

All you need to do, is change your app’s Compose file to mount the app_data directory into the Harbormaster-provided directory instead:

```plain text
services:
  main:
    build: .
    volumes:
      - ${HM_DATA_DIR}/data:/app_data
    ports:
      - 8080:8080
    restart: unless-stopped

```

Harbormaster will ensure ${HM_DATA_DIR} expands to harbormaster-main/data/myapp, so all your apps’ data will be stored neatly under harbormaster-main/data/myapp/data. You don’t have to mount the volume under /data, you can mount it directly to ${HM_DATA_DIR} if you want. You can also use as many mounts as you want, just make sure each is a different subdirectory.

For example:

```plain text
services:
  main:
    build: .
    volumes:
      - ${HM_DATA_DIR}/data:/app_data
      - ${HM_DATA_DIR}/other_data:/more_data
      - ${HM_CACHE_DIR}/some_cache:/cache1
      - ${HM_CACHE_DIR}/some_other_cache:/cache2
    ports:
      - 8080:8080
    restart: unless-stopped

```

You can do this with any variable, there’s no magic (the variables above just straight-up expand to a dir name).

Now you can read on about how to install Harbormaster.


