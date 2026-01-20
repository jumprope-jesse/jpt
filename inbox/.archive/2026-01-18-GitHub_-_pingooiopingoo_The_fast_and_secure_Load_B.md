---
type: link
source: notion
url: https://github.com/pingooio/pingoo
notion_type: Software Repo
tags: ['Running']
created: 2025-10-06T14:32:00.000Z
---

# GitHub - pingooio/pingoo: The fast and secure Load Balancer / API Gateway / Reverse Proxy with built-in service discovery, GeoIP, WAF, bot protection and much more - https://pingoo.io

## Overview (from Notion)
- Performance & Security: Leveraging Rust for enhanced speed and security can significantly improve app responsiveness, crucial for user satisfaction.
- Self-Hosting: Control over data and compliance by running your own load balancer can align with privacy values, especially in a city like NYC where data security is paramount.
- Open Source: The commitment to an open-source model means no vendor lock-in, allowing for flexibility and customization—ideal for a founder looking to innovate.
- Service Features: Built-in features like bot protection and WAF reduce reliance on third-party services, streamlining operations and reducing costs.
- Future-Proofing: Post-Quantum TLS indicates a forward-thinking approach to security, preparing for future challenges—critical in an ever-evolving tech landscape.
- Community Engagement: The emphasis on contributing and discussing ideas fosters collaboration, which can be beneficial for networking with other tech enthusiasts or professionals.
- Urban Tech Scene: Being part of NYC’s vibrant tech community, utilizing cutting-edge solutions like Pingoo can position your projects at the forefront of innovation.

## AI Summary (from Notion)
Pingoo is a modern, open-source Load Balancer, API Gateway, and Reverse Proxy that offers features like service discovery, WAF, bot protection, and Post-Quantum TLS, all while ensuring data compliance by running on private servers. Currently in beta, it promises enhanced performance and security, with a quickstart guide available for deployment. Users can contribute ideas, seek support, and report security issues through the official website.

## Content (from Notion)

# Pingoo

### The fast and secure Load Balancer / API Gateway / Reverse Proxy with built-in service discovery, GeoIP, WAF, bot protection and much more

### Documentation | Read the launch post

Open Source load balancers and reverse proxies are stuck in the past century with a very slow pace of development and most of the important features reserved for "Enterprise Editions" which lead developers to use third-party cloud services, exposing their users' traffic to legal, security and reliability risks.

Pingoo is a modern Load Balancer / API Gateway / Reverse Proxy that run on your own servers and already have (or will have soon) all the features you expect from managed services and even more. All of that with a huge boost in performance and security thanks to reduced latency and, of course, Rust ;)

- Service Discovery (Docker, DNS...)
- Web Application Firewall (WAF)
- Easy compliance because the data never leaves your servers
- Bot protection and management
- TCP proxying
- Post-Quantum TLS
- GeoIP (country, ASN)
- Static sites
- And much more
> 

## Quickstart

```plain text
# You have a static site in the www folder
$ ls www
index.html
$ docker run --rm -ti --network host -v `pwd`/www:/var/wwww ghcr.io/pingooio/pingoo
# Pingoo is now listenning on http://0.0.0.0:8080
```

## Documentation

See https://pingoo.io

## Updates

Click Here to visit the blog and subscribe by RSS or email to get weekly / monthly updates. No spam ever, only technical deep dives.

## Contributing

Please open an issue to discuss your idea before submitting a Pull Request.

## Support

Do you have custom needs? Do you want your features to be prioritized? Are you under attack and need help? Do you need support for deploying and self-hosting Pingoo?

Feel free to reach our team of experts to see how we can help: https://pingoo.io/contact

## Security

We are committed to make Pingoo the most secure Load Balancer / Reverse Proxy in the universe and beyond. If you've found a security issue in Pingoo, we appreciate your help in disclosing it to us in a responsible manner by contacting us: https://pingoo.io/contact

## License

MIT. See LICENSE.txt

Forever Open Source. No Open Core or "Enterprise Edition".


