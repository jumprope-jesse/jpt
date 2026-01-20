---
type: link
source: notion
url: https://www.yvesdennels.com/posts/docker-swarm-in-2022/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2025-08-09T13:34:00.000Z
---

# Docker Swarm in 2022 - Some tech notes

## Overview (from Notion)
- Docker Swarm offers a user-friendly approach to deploying web apps, which could save you time as a busy software engineer and father.
- Its simplicity allows you to quickly set up infrastructure without diving deep into complex systems like Kubernetes, making it ideal for small projects or personal experiments.
- The ability to use docker-compose.yml files for deployment means you can leverage existing projects, enhancing productivity and reducing overhead.
- While Docker Swarm may seem less active in terms of development, its ease of use can still provide value for straightforward deployments.
- Consider the balance between simplicity and scalability: Docker Swarm is great for smaller applications, but think about the long-term growth of your projects and whether a more robust solution might be needed later.
- Exploring alternate views: while some may argue for the latest technologies like Kubernetes, the practical benefits of Docker Swarm for rapid deployment shouldn't be overlooked.

## AI Summary (from Notion)
Docker Swarm is a viable option for simple web app deployments on a single server, offering ease of setup and quick deployment using docker-compose files. Despite concerns about its community size and development activity, it provides a straightforward solution for many users without the complexity of Kubernetes or other orchestration tools.

## Content (from Notion)

# Going with Docker Swarm in 2022

TL;DR: Docker Swarm is probably good enough in a lot of cases. See the update for 2023

Having worked professionally on setting up, customising and deploying Kubernetes (but without pretending to be a specialist), I didn’t want to go down that path for my personal infrastructure, even if using Jsonnet was of great help (see my Jsonnet course here). I tried Nomad which worked fine, but getting it to do what I wanted was taking more time than I hoped.

Then I relunctantly tried Docker Swarm. Reluctantly because I thought Docker Swarm was dead and unusable at this point. I thought that the community of users must be so small and shrinking that getting help would be hard. But that last point, if probably true, appeared irrelevant. Things are so easy to set up that every step worked at first try and I had multiple apps available in a couple of hours.

Sure, my requirements are simple: make it as easy as possible to deploy web apps on one server. No multi-node, no HA. Which is probably a good chunk of web app deployments out there. And in that case, Docker Swarm really shines. Read Single Node Swarms Are Awesome for more info.

I’ve deployed the setup described at Docker Swarm Rocks, with Traefik as reverse proxy. No need to duplicate that content here, so go there if you want to try it out.

The biggest advantage is that to deploy app to your Docker Swarm, you can use a docker-compose file. The great thing is that a majority of projects propose a docker-compose.yml file for deployment, making it readily available to you for deployment on your swarm. You might have to edit it slightly, but it is much more approachable than translating it to another format like K8s manifests.

Of course, Docker Swarm is not developed very actively, but the speed at which I could deploy my infrastructure makes it worth the bet. And if I have to migrate to another solution later on, I won’t have lost a lot of time anyway.

Take a look and decide for yourself!


