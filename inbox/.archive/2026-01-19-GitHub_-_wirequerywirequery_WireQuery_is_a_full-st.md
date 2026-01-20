---
type: link
source: notion
url: https://github.com/wirequery/wirequery
notion_type: Software Repo
tags: ['Running']
created: 2024-03-24T04:27:00.000Z
---

# GitHub - wirequery/wirequery: WireQuery is a full-stack session replay tool. Using WireQuery, you can see how a user experiences an issue through a video-like frontend recording. Combined with an overview of the network calls to the backend (including network calls further upstream and their actual payload), you get a holistic overview of how an issue came into existence.

## AI Summary (from Notion)
- Overview of WireQuery: A full-stack session replay tool that allows users to visualize issues through video-like recordings and network call overviews.
- Holistic Issue Understanding: Combines frontend recordings with backend network calls, providing a comprehensive view of how issues arise.
- WQL (Network Query Language): Allows investigations starting from the backend, enabling users to find issues not visible to them through frontend recordings.
- Privacy Considerations: The SDKs are designed to minimize the risk of exposing sensitive information during recordings.
- Getting Started: Instructions for local installation using Docker, including necessary commands and initial login details.
- SDK Variants: Available in various technologies including JVM, JavaScript for browsers, Go, and a universal SDK for other languages.
- Community Engagement: Encourages users to give the project a star on GitHub to support its growth.
- Contributing and Licensing: Information about contributing to the project and licensing under AGPLv3 for WireQuery and MIT for the SDK.
- Resource Links: Includes links to the official website, documentation, Discord channel for support, and blog posts for further reading.

## Content (from Notion)

# WireQuery

WireQuery is a full-stack session replay tool. Using WireQuery, you can see how a user experiences an issue through a video-like frontend recording. Combined with an overview of the network calls to the backend (including network calls further upstream and their actual payload), you get a holistic overview of how an issue came into existence.

Some issues, however, can only be found on the backend, before users have reported them with a video-like recording. Through a specialized “network query language” called WQL, you can easily start your investigation from the backend as well. Like before, this includes all the network calls up- and downstream of your query result.

Since the video-like recordings and network calls may contain sensitive information, WireQuery’s SDKs are designed with privacy in mind. In most cases, minimum effort is required to strip all sensitive data from your frontend and backend systems.

⭐ If you like WireQuery, please consider giving it a star. Your support can help the project grow and deliver exciting features.

## Getting Started

If you want to try out WireQuery on your local machine:

1. Make sure Docker is installed and run the following commands in your terminal: 
1. Wait until both the backend and frontend are initialized and navigate to localhost:8090. Log in with admin / admin and update your password in the Settings.
1. Start using WireQuery by creating an application and connecting to WireQuery using one of the SDKs below.
If you wish to install WireQuery on a server, please follow the Server Installation instructions.

## SDKs

WireQuery's SDKs are offered in the following variants:

More SDKs will be added over time.

## Links

- Official Website
- Documentation
- Writing Queries
- Join our Discord Channel for questions and support.
- Quick Start Guide with Spring Boot
- WireQuery Introduction Blog Post
## Contributing

See CONTRIBUTING.md

## License

Unless otherwise specified, WireQuery is licensed under AGPLv3 and the SDK is licensed under MIT. For more information, see LICENSE.md.


