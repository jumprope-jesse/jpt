---
type: link
source: notion
url: https://allauth.org/news/2024/03/ngi-zero-grant-plan/?utm_campaign=Django%2BNewsletter&utm_medium=rss&utm_source=Django_Newsletter_223
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-03-15T15:28:00.000Z
---

# django-allauth

## AI Summary (from Notion)
- Grant Received: Django-allauth has received funding from NGI Zero, enabling significant project development beyond basic maintenance.
- Historical Context: The project started in 2010 to consolidate various authentication methods into a single, reusable solution.
- Evolution of Requirements: Over the years, the need for complex authentication features, such as two-factor authentication (2FA) and support for external providers, has increased.
- Challenges with External Projects: Integrating additional functionalities through external projects has proven difficult and often leads to compatibility issues.
- Shift in Approach: The project aims to incorporate essential features like 2FA and passwordless login directly into the core offering, rather than relying on external solutions.
- Value of Open Source: Emphasizes the importance of open-source solutions for authentication to avoid dependency on proprietary services and protect user data.
- Future Goals:
- First-class API support with OpenAPI specification and example applications for single-page applications (SPAs).
- Support for WebAuthn and Passkeys as part of enhancing security options.
- Acknowledgments: Gratitude expressed to NGI Zero, NLnet foundation, and smaller sponsors for their support in advancing the project.
- Call to Action: Encouragement for users and companies utilizing django-allauth to consider sponsorship to help sustain the project.

## Content (from Notion)

# Grand Plans for 2024

As you may have heard, django-allauth has received a grant from NGI Zero, which allows for the project to move forward well beyond the usual maintenance and incremental changes. In this post, I would like to outline the activities that will be performed as part of this grant.

## How did we get here?

First, a little trip down memory lane. Back in 2010, various packages existed, each targeting their own part of the authentication problem space. Trying to mix and match the various offerings, e.g. one for local accounts, another for social accounts, was far from trivial. This led to the start of the project. Its goal: to offer a free, secure, reusable authentication solution, covering all functionality related to local and social user accounts, in various configurations, with flows that just work. The integrated approach is the key reason the project became a popular choice within the Django ecosystem.

Over the years, the authentication problem space grew ever more complex, from only having local accounts, to having support for external providers, two-factor authentication, interfaces for single-page applications, and the more recently introduced WebAuthn/Passkey standard.

For a long time, anything other than local and social accounts was considered beyond scope. External projects came to life filling in these gaps, building on top of django-allauth. However, trying to offer integral functionality in external independent projects has proven to be challenging. Frequently, upgrades in one project cause trouble in the other and vice versa. Also, covering all of the allauth use cases and diversity is often missing.

Now, I want to stress that I do not want to badmouth any of the work developers building on top of django-allauth have done, on the contrary! Trying to bolt-on important flows on an external code base like that of django-allauth is not an easy feat.

Having said that, from an allauth point of view, times have changed. A decade ago 2FA was not that common, and was best explored in a project of its own. But these days, 2FA is a core authentication component that every project needs, which is why it was decided to offer support for that out of the box. The same needs to be done for single-page application support, as well as passwordless login.

## Why?

Now, you may wonder why go through this trouble at all? Why not just use $PROPRIETARY_SAAS_SOLUTION? Or, use a $PARTLY_OPEN_SAAS_SOLUTION and use their self-hosted option? Obviously, because the former is proprietary. The latter complicates your development and deployment environment from the start, the hassle of which is enough to drive developers more and more towards the proprietary solutions. Having an all integrated solution, where you can own your data, with less moving parts simplifies things, a lot.

Authentication is a crucial part of any web site. Given its complexity, it is vital that developers be given a high quality, open source, reusable building block. Without that, developers will be pushed towards integrating SaaS based and/or centralized authentication solutions, and as a consequence, their actual end users will also be pushed towards using such centralized solutions, which is detrimental to the Open Internet.

## What's the plan?

The main goals are the following:

- Add first-class API support. As part of the delivering the API, an OpenAPI specification and example React example application will be delivered, showcasing full SPA access to all of the django-allauth flows.
- Add support for WebAuthn. This will cover both Webauthn as a second factor (U2F), as well as support for Passkeys.
Work in both directions has already started. The API support is expected to arrive first. Besides these bigger topics, also expect to see movement in several long standing issues.

## Closing words

A big thanks to NGI Zero / the NLnet foundation for making this possible, and an equal thanks to the various smaller sponsors that have helped the project to come this far. Last but not least, if you or your company is using django-allauth, please consider sponsoring via Liberapay or Github Sponsors. Thanks!


