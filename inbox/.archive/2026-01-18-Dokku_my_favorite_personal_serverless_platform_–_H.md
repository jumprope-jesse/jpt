---
type: link
source: notion
url: https://hamel.dev/blog/posts/dokku/
notion_type: Software Repo
tags: ['Running']
created: 2024-08-26T16:54:00.000Z
---

# Dokku: my favorite personal serverless platform – Hamel’s Blog

## AI Summary (from Notion)
- Dokku Overview: Dokku is an open-source Platform as a Service (PaaS) that allows users to turn a VPS into a serverless platform, similar to Heroku but without the associated costs.
- Cost-Effective Solution: The author uses a $7/month VPS from OVHcloud for non-GPU workloads, highlighting the affordability of Dokku for deploying applications.
- Key Features:
- User-friendly interface similar to Heroku.
- Automatic SSL management via Let’s Encrypt.
- Basic Auth support for password protection.
- Flexibility to handle various application types (Node, Python, etc.) with Docker containers.
- Extensive plugins for enhanced functionality.
- Deployment Methods:
- Applications can be deployed as Docker containers using a Dockerfile.
- Static sites can also be easily deployed from private GitHub repositories.
- Security: Basic authentication can be implemented for static sites, and HTTPS can be managed via Let’s Encrypt.
- Automated Deployment: GitHub Actions can be utilized for automatic deployment to Dokku apps, streamlining the process.
- Remote Command Execution: Users can execute commands on the Dokku host without SSH, which enhances convenience.
- Miscellaneous Tips:
- Commands for purging Docker cache and rebuilding apps without pushing are provided.
- The author emphasizes the importance of documenting these details for personal reference and for others' benefit.
- Intended Audience: The content serves developers looking for a cost-effective and flexible platform for deploying applications, particularly those familiar with Docker and Git.

## Content (from Notion)

With Dokku, you can turn a VPS into a powerful serverless platform

## What is Dokku?

Dokku is an open-source Platform as a Service (PaaS) that runs on a single server of your choice. It’s like Heroku, but you own it. It is a great way to get the benefits of Heroku without the costs (Heroku can get quite expensive!). I need to deploy many applications for my LLM consulting work. Having a cost-effective, easy-to-use serverless platform is essential for me.

I run a Dokku server on a $7/month VPS on OVHcloud for non-gpu workloads. These applications include things like nbsanity and data cleaning tools for LLMs.

Some of the features I love about Dokku:

- Easy to use (like Heroku).
- Automatic SSL certificate management via Let’s Encrypt.
- Basic Auth support so I can password-protect sites.
- Scale up and down with a single command.
- Flexibility to handle any application (Node, Python, etc), including defining a Docker container.
- Lots of official plugins that do almost anything I want.
- Easily deploy with git commands.
# Minimal Dokku Examples

Make sure you install Dokku on your VPS. As I mentioned, I use OVH.

## Deploying Apps as A Docker Container

An easy way to deploy applications is with a Docker container.

To deploy a Docker container, I put a Dockerfile in the root of my git repo like this:

```plain text
Dockerfile
```

```plain text
FROM python:3.10

COPY . /app
WORKDIR /app

# Install the local package
RUN pip install .

# This directory contains app.py, a FastApi app
WORKDIR /app/

ENTRYPOINT ["./entrypoint.sh"]
```

Tip

The entrypoint.sh script allows me to easily run the app locally or in a Docker container. It looks like this:

```plain text
entrypoint.sh
```

```plain text
#!/bin/bash
exec uvicorn main:app --port "$PORT" --host 0.0.0.0
```

On the Dokku host, create the app:

```plain text
dokku apps:create myapp
```

Locally, set up access to the Dokku host and name it dokku in your ~/.ssh/config file. For example, here is mine:

```plain text
Host dokku
  HostName <The external IP address of your Dokku host>
  User ubuntu
  IdentityFile /Users/hamel/.ssh/dokku
```

Locally, add the Dokku host as a remote and push to it:

```plain text
git remote add dokku dokku@dokku:myapp
git push dokku main
```

That’s it - your app should be running on the Dokku host! Your local logs will print the URL that your application is served on, which by default will be myapp.yourdomain.com. You can also scale it up/down with the following command:

```plain text
#scale to two workers
dokku ps:scale myapp web=2
```

We are just scratching the surface. For more details, see the Dokku docs.

## Static Sites

GitHub Pages is annoying in that you can’t easily deploy private static sites without paying for an expensive Enterprise account. With Dokku, you can easily deploy a static site from a private GitHub Repo and password-protect it.

We will assume that you have a static site in a git repo in a folder named _site.

On the Dokku host, create an app named mysite and set the NGINX_ROOT environment variable to _site:

```plain text
dokku apps:create mysite
dokku config:set static-site NGINX_ROOT=_site
```

Also on the Dokku host, install basic auth and set permissions so the plugin can work properly.

```plain text
# do setup for the auth plugin that we will use later
sudo dokku plugin:install https://github.com/dokku/dokku-http-auth.git
sudo chmod +x /home/dokku
```

Then execute the following commands from the root of your git repo that contains the static site. :

```plain text
1touch .static
2echo BUILDPACK_URL=https://github.com/dokku/buildpack-nginx > .env
3git remote add dokku dokku@dokku:mysite
```

1  tells dokku that this is a static site  2  tells dokku to use the nginx buildpack for static sites (it will usually automatically detect this, but if you have a project with code and a static site, you need to tell it to use the nginx buildpack so it doesn’t get confused).  3  add the dokku host as a remote. For this to work, make sure dokku is a hostname in your ~/.ssh/config file as described in the previous section. 

Finally, deploy your application:

```plain text
git push dokku main
```

You can now add auth by running the following command on the Dokku host:

```plain text
dokku http-auth:enable mysite <username> <password>
```

Note

You can add multiple usernames/passwords and even filter specific IPs. See the docs.

SSL / HTTPS

It’s often desirable to have HTTPS for your site. Dokku makes this easy with the Let’s Encrypt Plugin, which will even auto-renew for you. I don’t use this, because I’m letting Cloudflare handle this with its proxy.

If you are using Cloudflare this way, activating this plugin will mess things up (don’t worry its easy to disable). Honestly, I think it’s easier to let Cloudflare handle it if you are already doing so.

# Deploying With GitHub Actions

You can automatically deploy Dokku apps with GitHub Actions, which is helpful if you don’t want to fiddle with pushing to the Dokku host. Here is an example GitHub Action workflow that does this:

```plain text
deploy-dokku.yml
```

```plain text
name: CI
on:
workflow_dispatch:
push:
branches: [main]

concurrency: # Cancel previous jobs to avoid deploy locks on dokku
group: ${{ github.ref }}
cancel-in-progress: true

jobs:
deploy-dokku:
runs-on: ubuntu-latest
steps:
- name: Checkout code
uses: actions/checkout@v2
with:
fetch-depth: 0

- name: Install SSH key
        run: |
          echo "${{ secrets.DOKKU_SSH_PRIVATE_KEY }}" > private_key.pem
          chmod 600 private_key.pem

- name: Add remote and push
        run: |
          git remote add dokku dokku@rechat.co:llm-eval
          GIT_SSH_COMMAND="ssh -i private_key.pem -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no" git push dokku main -f
```

# Miscellaneous Tips

These are things I often forget, so I’m writing them down here. For these examples, assume my app is named llm-eval and my host is rechat.co.

## Run commands remotely

You don’t have to ssh into the Dokku host just to execute commands. You can execute them remotely via the dokku user like this:

```plain text
# https://dokku.com/docs/deployment/application-management/
ssh dokku@rechat.co apps:list
```

## Docker cache

This is how you can invalidate the docker cache for a fresh build:

```plain text
ssh dokku@rechat.co repo:purge-cache llm-eval
```

## Rebuild without pushing

Sometimes you want to rebuild without pushing. There are many ways to do this, but one way is like this:

```plain text
ssh dokku@rehcat.co ps:rebuild llm-eval
```

# Why Did I Write This?

I had to dig up these details whenever I wanted to deploy a new app, so I had to write it up anyway. I hope you find it useful, too!


