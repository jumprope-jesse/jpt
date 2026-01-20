---
type: link
source: notion
url: https://j6b72.de/article/why-you-should-take-a-look-at-traefik/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-05-05T13:24:00.000Z
---

# Why you should take a look at traefik, even if you don't use containers

## Overview (from Notion)
- Simplified Deployment: Traefik's single binary makes it easy to manage network traffic without complex setups, allowing you to focus more on family time and less on server maintenance.
- Robust Security: With features like TLS passthrough and PROXY protocol, you can secure your home network, providing peace of mind for your family's online presence.
- Adaptability: Even if you're not using containers, Traefik can still be valuable. This means you can integrate it into your existing infrastructure without overhauling everything.
- Documentation: Traefik's clear documentation can help you quickly get up to speed, saving you time for coding or spending time with your kids.
- Community Insights: Engaging with the Traefik community can provide new ideas and perspectives on managing tech at home, which can inspire innovative solutions in your own projects.
- Alternate Views: Some might prefer traditional setups like NGINX for specific use cases. Weighing the pros and cons can lead to a more tailored solution for your software needs.

## AI Summary (from Notion)
Traefik is a popular reverse proxy that can be used without containers, offering features like TLS passthrough and easy configuration through static and dynamic files. It is written in Golang, compiles to a single binary, and can be deployed easily. While it supports configuration files, some features like authentication and user agent blocking may require third-party plugins. The documentation is comprehensive, making it accessible for users unfamiliar with its concepts.

## Content (from Notion)

Traefik got really popular over the last few years in the bubble of home-lab youtubers, that’s when I first heard about it.

Traefik is more comparable to HAProxy than to nginx/caddy/apache2 - it forwards requests to services and returns the responses, can even modify headers and other aspects of the request and response, but it can’t serve files.

This article states my experience with traefik in an environment without containers.

## What traefik is known for

Traefiks site states their mission to help the microservices world. All these youtubers share that they own some kind of container infrastructure, either docker or kubernetes. Traefik runs as container too, you mount the docker socket into the traefik container and gain the ability to auto-detect other containers that you might want to expose using traefik. You can configure the proxying behavior right on the specific container via labels. Traefik can automatically request a TLS certificate from Let’s Encrypt and makes your service available as soon as it detects the existence of new container.

As I don’t use linux containers that much right now, I thought traefik wasn’t for me. But I was wrong. It’s fantastic!

## Why it’s also viable for non-container usage

### Common Misconception: no container engine required

Traefik doesn’t need to run in a container engine, and your services don’t need to run in a container engine.

Traefik is written in Golang and compiles to a single executable file, which you can download from their releases page. I don’t know why, but I get a really good feeling when I encounter software that is written in Golang and compiles to a single binary. It makes it so easy to “deploy” the thing and you get to keep full control.

An example systemd service unit is contained in their repository, and that’s, apart from the configuration files, all you need. For security, you should create a user and correctly set the permissions on the your configuration files, though.

### Common Misconception: also supports config files

If you don’t use containers, you can’t use container labels - but I find these labels confusing and hard to read anyway.

The good thing: Traefik can also be configured with configuration files.

As a rule of thumb, Traefik splits its configuration in two parts - a “static” configuration that contains your certificate provider (e.g. Let’s Encrypt) and entrypoints (the ports traefik listens on) and a “dynamic” configuration that contains your routers, services and middlewares.

Traefik listens to file system events and can hot reload the dynamic part.

The config file isn’t thaaaat complicated. See my configuration at the bottom of this article.

### Their documentation is great!

It explains all the concepts that Traefik builds upon clearly, has a configuration example for whichever way of configuring your instance you took at the beginning of the relevant pages (which, let’s be real, is the thing we’re searching for most of the time) and their docs covered most of the demands that I had.

If you didn’t understand the terms I used earlier (certificate provider, entrypoint, routers, services & middlewares), the documentation will help you in sub-10 minutes. Try it out yourself. The sidebar is your friend.

### Traefik feels robust and well thought-out

Traefik warns you if your configuration doesn’t make sense and I haven’t run into random issues yet.

Traefik doesn’t seem to log much by default, but the way your request takes is easy to understand and I was up and running really fast without any frustration.

## Features I really like

### TLS Passthrough & PROXY protocol

Traefik supports TLS Passthrough and HAProxys PROXY protocol (in and out).

TLS passthrough means that you can forward traffic to web services that supply their own TLS certificate (even request it themselves from Let’s Encrypt, through Traefik, which just forwards everything to the service so that can work) without terminating TLS on the proxy. The proxy can’t see what’s being transmitted.

The decision which virtual host is selected normally happens via the “Host”-Header - but as that’s in the encrypted body, that’s not possible. TLS has a solution for that problem - the “Server Name Indication” (SNI), and Traefik and many other web servers / proxies use that to make the selection.

As an addition, HAProxys PROXY protocol is a more secure way of transmitting the info that gets lost due to the user first reaching the proxy - in the past, you would’ve used the “X-Forwarded-<…>” headers, but I always disliked those, as making them secure isn’t trivial and requires testing, as header handling often times isn’t well documented.

Note: the PROXY protocol has to be supported by the target service too - but for apache2 and nginx (and therefore, PHP) that’s the case, and the list of services that support the protocol is growing.

## Things I miss when using traefik

### Authentication

On NGINX, I use the great Vouch Proxy (also a Golang one-binary program :>) to secure certain services with Azure AD (sorry, Microsoft Entra…) Authentication. (If you know NGINX, you’ll understand how it works just by looking at this: https://github.com/vouch/vouch-proxy?tab=readme-ov-file#installation-and-configuration)

Traefik supports something similar to NGINX’s auth using ForwardAuth. Sadly, Vouch Proxy doesn’t work yet for Traefik (open issue).

You could roll your own keycloak instance, integrate that with AAD and use that for ForwardAuth. The internet says that works. But it also requires you to keep that keycloak instance secure and up-to-date and set it up in the first place. For bigger projects, that might be viable.

Often recommended is traefik-forward-auth. Sadly, that project has had its last update in June of 2020, the developer disappeared from GitHub and the dependencies need updating. There are open pull requests, which will probably never be handled. Not viable for me.

I’ve had a bad experience with oauth2-proxy in the past (but to give them credit: also golang and a single executable :>). I don’t want to proxy to a proxy, as things HTTP2/3, timeouts, body size and WebSockets require configuration on all proxies between the user and the service. Feels too error-prone to me.

But the Traefik ForwardAuth seems simple enough, so I might write my own simple tool for integrating with AAD. Or maybe someone should fork and audit traefik-forward-auth, and update its dependencies.

### Blocking of user agents and IP addresses

I don’t want my internal services to be archived by archive.org. As robots.txt and similar headers don’t work for disallowing Archive.org, there are only two possibilities to block their Crawler: Blocking the “archive.org_bot” user agent, or blocking their IP range.

In Traefik, you can only block user agents or IP addresses via a third-party plugin. I don’t like third-party plugins as I need to keep them in mind when updating, and they can introduce security vulnerabilities.

You could block IPs by using the IPAllowList middleware, and just allow everything but the IPs that you want to disallow. You can calculate the IP ranges. That’ll work and isn’t any worse than blocking directly, but doesn’t feel very elegant at all as you can’t see what subnets are exactly blocked just by looking at the ones that are left.

## Configuration example

The following example sets up:

- entrypoints on :80 and :443 
- Let’s Encrypt for certificates with the TLS challenge
- tls passthrough proxying for cloud.xx.xyz (service on another host) 
- tls-terminating proxying to git.xx.xyz (service on the local host)
- redirect middleware from https://xx.xyz/redirmepls to https://google.com
- header-adding middleware to add a x-robots-header
### /etc/traefik/traefik.yml

```plain text
providers:
  file:
    filename: /etc/traefik/dynamic.yml
    watch: true
entryPoints:
  https:
    address: :443
  http:
    address: :80
    http:
      redirections:
        entryPoint:
          to: https
          scheme: https
certificatesResolvers:
  le:
    acme:
      email: xx@xx.xyz
      storage: /etc/traefik/acme.json
      tlsChallenge: {} # Required as per https://blog.alexanderhopgood.com/traefik/letsencrypt/2020/12/09/traefik-http-challenge.html

```

### /etc/traefik/dynamic.yml

```plain text
tcp:
  routers:
    nextcloud-router:
      rule: "HostSNI(`cloud.xx.xyz`)"
      service: nextcloud
      entrypoints:
        - https
      tls:
        passthrough: true
  services:
    nextcloud:
      loadBalancer:
        servers:
          - address: 10.33.1.2:4433
        proxyProtocol:
          version: 2
http:
  routers:
    gitea:
      rule: "Host(`git.xx.xyz`)"
      entrypoints:
        - https
      service: gitea
      middlewares:
        - noindex
      tls:
        certResolver: le
    xx.xyz:
      rule: "Host(`xx.xyz`)"
      entrypoints:
        - https
      middlewares:
        - my-redirect
      tls:
        certResolver: le
      service: dummy
  middlewares:
    my-redirect:
      redirectRegex:
        regex: "https://xx.xyz/redirmepls"
        replacement: "https://google.com"
    noindex:
      headers:
        customResponseHeaders:
          X-Robots-Tag: noindex, nofollow, nosnippet, noarchive
  services:
    gitea:
      loadBalancer:
        servers:
          - url: http://127.0.0.1:3000
    dummy:
      loadBalancer:
        servers: []

```


