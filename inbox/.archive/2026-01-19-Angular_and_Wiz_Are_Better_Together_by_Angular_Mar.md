---
type: link
source: notion
url: https://blog.angular.io/angular-and-wiz-are-better-together-91e633d8cd5a?gi=83d008dc6f61&source=rss----447683c3d9a3---4
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-03-29T23:49:00.000Z
---

# Angular and Wiz Are Better Together | by Angular | Mar, 2024 | Angular Blog

## AI Summary (from Notion)
- Collaboration of Frameworks: Angular and Wiz are joining forces to combine the strengths of both frameworks, targeting both performance and developer experience.
- Distinct Focus Areas:
- Wiz: Primarily used for performance-critical apps, like Google Search, focusing on fast rendering with minimal JavaScript.
- Angular: Designed for highly interactive applications, prioritizing developer experience and ease of building complex UIs.
- Blending Requirements:
- The growing need for performant apps to deliver features quickly while maintaining interactivity has blurred the lines between the two frameworks.
- JavaScript usage has significantly increased over the past six years, complicating performance for developers.
- Incremental Improvements:
- The partnership aims to gradually introduce incremental improvements to both frameworks based on community feedback.
- Angular has already integrated features inspired by Wiz, such as deferrable views and partial hydration.
- Adoption of Technologies: Wiz has adopted Angular’s Signals library, enhancing performance for applications like YouTube by allowing fine-grained UI updates.
- Long-term Vision:
- The ultimate goal is to responsibly merge Angular and Wiz, with a commitment to open sourcing Wiz features through Angular.
- Emphasis on server-side rendering (SSR) as a crucial element for enhancing user experience in web applications.
- Community Engagement: The approach will involve active community participation through public RFC processes to gather feedback on proposed features.

## Content (from Notion)

You may know Angular as the web framework from Google, but Google actually has another web framework: Wiz. Both Angular and Wiz are used by thousands of engineers and thousands of apps inside of Google. Wiz is an internal framework that is used by some of the most popular Google products such as Search, Photos, Payments and many others. Over the last year we’ve been exploring ways for Angular to benefit from the performance of Wiz and Wiz to benefit from the developer experience of Angular.

Historically, Angular and Wiz have been serving different segments of apps:

- Wiz has been focused on performance-critical apps. A good example of this is Google Search, which aims to render the results as quickly as possible and has relatively low interactivity.
- Angular has been focused on serving highly interactive apps, prioritizing developer experience and quick delivery of complex UIs. Good examples are apps such as Gemini and Google Analytics.
Blending of features of Angular and Wiz

# What is Wiz?

Millions of users access large Google applications over slow networks and/or low-end devices. In such cases initial load latency and amount of JavaScript matters a lot. The Wiz framework meets these requirements in a couple of ways. Wiz always starts with server-side rendering. Everything on the page, including interactive components, is rendered on a highly optimizing streaming solution. This eliminates most JavaScript from the critical initial render path. To avoid loading too much JavaScript, Wiz only loads the code required by interactive components actually rendered on the page. To avoid dropping user events on the client side a small, inline library listens for user events at the root and replays them. This novel approach to make SSR-first applications leads to the best performance for end users, however, it comes with the tradeoff that it increases complexity for developers, especially for highly interactive applications.

# Blending requirements

Recently we’ve been seeing a blend of these two different segments. Highly performant apps need to ship more features faster to provide value to their users and keep them engaged. At the same time, highly interactive apps start shipping more and more JavaScript. According to HTTPArchive, JavaScript increased with over 37% on desktop and over 36% on mobile over the past 6 years, which significantly impacts performance.

Increase of JavaScript in the top 1m websites based on HTTPArchive

With these blending requirements it becomes harder for developers to decide which framework serves their needs better and we start seeing a larger overlap of use cases. To respond to the growing demand of a highly performant framework with great developer experience, Angular and Wiz joined together to bring the best of both worlds. Going forward Angular developers will no longer have to choose between developer experience and performance.

# Bringing both worlds together

The partnership between Angular and Wiz manifests our mission to enable developers to build web apps with confidence. Based on the developer feedback we receive we seek opportunities to open source some of the best Web development practices we discovered at Google. At the same time, we’d like to bring the great developer experience from our Angular community to all of Google.

In practice this appears as incremental and gradual improvements to each framework. You’ve probably seen the fruits of our collaboration with some of the latest changes to Angular such as deferrable views and our exploration of partial hydration. They are both highly inspired by Wiz’s fine grained code loading and an event delegation library.

At the same time, Wiz adopted Angular’s Signals library which is now powering the user interface of YouTube, running on billions of devices. Angular Signals allowed Wiz to adopt fine-grained UI updates. We switched away from an approach that relied on developers to carefully memoize code paths that run on every UI update. This resulted in demonstrable performance improvements. To learn more about this see the ng-conf keynote. We’re excited to see how Angular Signals will improve some of the biggest sites in the world, like Search and GMail.

# Where are we heading from here?

Our long-term goal is to gradually and responsibly merge Angular and Wiz over the coming years. Our strategy is to steadily open source Wiz features via Angular and follow our open model of development, allowing the community to both influence the roadmap and plan accordingly. We’ll use the public RFC process to ensure we gather community feedback on the relevant proposed features. The primary goal is to improve the Angular framework.

We believe server side rendering (SSR) is important for the web platform. Our experience building some of the most used web products in the world has taught us that SSR positively impacts end user experience when done correctly. We want to invite the community to innovate using key libraries powering applications like Google Search and YouTube.


