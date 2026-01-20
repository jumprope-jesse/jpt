---
type: link
source: notion
url: https://blog.swgillespie.me/posts/monorepo-ingredients/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2025-05-29T02:38:00.000Z
---

# The Ingredients of a Productive Monorepo

## Overview (from Notion)
- Efficiency in Work: The concept of a monorepo can resonate with your desire for streamlined workflows in both personal and professional life. It emphasizes the importance of consistency and coherence, which can lead to increased productivity.

- Team Collaboration: As a founder, promoting a culture of collaboration through shared tooling and practices can enhance team dynamics, making it easier for engineers to contribute across projects.

- Adaptability: The challenges of transitioning to a monorepo highlight the need for flexibility and adaptability in your approach to software development, reminding you that growth often involves overcoming initial setbacks.

- Tooling Investment: The emphasis on building custom tools for specific needs may inspire you to invest in developing bespoke solutions that cater precisely to your team's requirements rather than relying solely on off-the-shelf software.

- Failure Management: The discussion around flaky tests and CI systems can offer insight into managing reliability in your products, encouraging a proactive approach to quality assurance that can save time and resources.

- Perspective on Growth: The caution against expecting outcomes similar to big tech giants serves as a reminder to set realistic goals based on your unique context, focusing on sustainable growth rather than chasing unattainable benchmarks.

- Work-Life Balance: The challenges of a monorepo can parallel personal life, where managing multiple responsibilities requires prioritization and smart allocation of resources, resonating with your experiences as a father.

- Alternative Views: Some may argue against monorepos due to their complexity and the overhead they introduce. Exploring these viewpoints can help you weigh the pros and cons of adopting similar strategies in your organization.

## AI Summary (from Notion)
Transitioning to a monorepo can enhance consistency and collaboration, but requires careful planning, the right tools, and an understanding of potential challenges, including source control and build system limitations. Prioritize efficiency and adapt testing and CI processes to manage the complexities of a large codebase effectively.

## Content (from Notion)

So! Suppose you’re an intrepid engineer in a nascent Developer Productivity team. Your engineering organization has decided that it wants to move towards a monorepo. You’ve heard the stories told of Google, Meta, Uber - each a large technology company with developer productivity organizations consisting of hundreds of engineers - and you want to capture some of their magic in a bottle and give it to your users. You wonder - what work lies ahead of you?

I’ve worked in a variety of companies, from gigantic titans to small startups and everything in-between, and I’ve worked in developer infrastructure for almost all of them. My experience is informed by my own successes and failures operating within these companies and trying to solve productivity problems of the developers I served. I’ve observed that a functioning monorepo environment demands the existence of a number of tools that you, dear Developer Productivity engineer, will likely need to write yourself for your company. I have yet to witness a suite of tools that fully solves the set of problems that you will encounter when setting up a monorepo. In this blog post I’m going to enumerate these tools and discuss implementation strategies for them, in the hopes of painting a clear picture of the path that lies ahead for any organization that walks the monorepo path.

The absolute first question you must ask yourself, though, is:

## Why do you want a monorepo?

You and your engineering organization must stare at this question deeply and answer it using language that is firmly anchored in your organization’s culture and values. Those blog posts that you read from Google, Facebook, or Uber engineers about how great their monorepo is, and how effective their developers are, and how everybody will be a 10x engineer when you’re done?

Purge them from your mind.

You WILL NOT end up with an experience as tight as google31 or fbsource2. You WILL inherit a new set of problems that many-repo setup did not have. You will take steps backward before you take steps forward. These blog posts and the wins they promise are not good reasons to embark on this journey. The cool engineering blogs from these big companies are discussing end states that, while very interesting, are far beyond the capabilities of your company and your small team. You will not have the same outcomes if you attempt to do what they have done.

Better reasons to embark on this journey are consistency, organizational coherence, and shared tooling efforts. Your developer productivity gets to focus on improving the experience of working in a single place and can reach more users in the process. Your engineering leadership gets to define and enforce engineering conventions. Engineers working in different organizations can contribute to each other’s codebases with the knowledge that they look and operate the same way.

You, intrepid Developer Productivity engineer, have the opportunity and responsibility to pave a path for your colleagues. Let’s get to work.

## The Golden Rule

If you can forgive this abuse of big-O notation, this principle guides all engineering for monorepo-related developer tools:

Any operation over your repository that needs to be fast must be O(change) and not O(repo).

As you begin to use your normal sets of tools in a large monorepo, you will find that many tools and processes do not have this property and will cause you problems as your monorepo grows. We will repeatedly come back to this design principle in every section that this blog post discusses. When you see a blog post from a big company talking about some engineering that they did on a developer tool, it is almost always the implementation of this principle in a space in which an O(repo) operation has become a problem.

## Source Control

Perhaps the most obvious consequence of storing all of your source code together in one repository is that, well, all of your source code is stored together. git is the default choice for many software companies today and, despite git being designed as decentralized source control system, many users use git through a software forge such as GitHub or GitLab. The reality is that git was never designed for the centralized monorepo and runs into substantial performance problems when your history gets large or your repo contains many, many files3.

Your repo probably isn’t big enough to have problems with git. You can push git and GitHub pretty far these days. However, git is (by design) a O(repo) system, and operations such as git status will slow down rapidly as the size of the repository grows.

If your monorepo begins to push the limits of git (or GitHub!), you have several paths available to you, each walked by a company that came before you:

- You walk the path of Microsoft and fork git.
- You walk the path of Meta and fork Mercurial.
- You walk the path of Google and write your own, although Google also managed to get pretty far by running Perforce on the most powerful servers that money could buy.
These companies chose different technical paths but all chose the same underlying idea. Your scaled-up source control system MUST be able to check out subsets of the repository and be able to operate on those subsets independently of the whole repository. There are essentially two ways to do this:

1. Your source control system subsets the repository and only clones files in that subset whenever you fetch. Files outside of your subset are not present on disk. If you need one of those files, you need to update your subset configuration to include it. Git calls this a sparse checkout. A similar Mercurial extension hg sparse also exists, originally authored by Meta, who used it for many years.
1. Your source control system logically checks out a revision of your repository but does not download anything eagerly. Instead, it presents a virtual filesystem that lazily downloads files on-demand from a central source control server. Repository tools “see” the full repository, but the contents of directories and files are only resolved when accessed. Google, Meta, and Microsoft have implemented this for their respective source control systems.
But you probably don’t work at these companies and your repo isn’t going to be this large for a while. Just use git for now and know that, as your company grows, so does your source control problem. The newer source control system Jujutsu is very promising in that it has the extension points in place to admit an open-source implementation of a virtual filesystem; I hope that this comes to life one day.

Finally, a practical consideration that amplifies your source control problems is the proliferation of generated code, particularly source generated by IDLs such as protobuf or thrift. If you choose to check-in generated source (which is a practical choice that I’ll go over in the next section), your source control footprint will grow at a rate that’s much larger than the sum total of new code output of your engineers.

## Building

“Aha! This part’s easy - this is what Bazel does!”

It’s true that Bazel, the open-source version of the Google-internal Blaze4, bills itself as a monorepo build tool that supports a myriad of languages. From a technical perspective, this is generally true. You can, and people do, get Bazel to build monorepos that consist of a bunch of different languages, toolchains, target architectures, and operating systems. The people that do this, though, work on a team that has a name like “The Build Team” and this is their full-time job.

My best advice to you is… don’t do that if you can avoid it. Keep your monorepo single-language if you can. Remember, one of our goals for having a monorepo in the first place is consistency, and it’s hard to do that if your engineers are writing code in multiple languages.

If you can use your language ecosystem’s build system (if it has one), do it. DO IT. Do it for as long as you POSSIBLY can. You will find that many build tools are O(repo) and tend to scale poorly as repositories grow, but these tools also will work up to scales that will surprise you. You can push Maven/Gradle, CMake, Cargo, and the Go build systems very, very far. Furthermore, if you check-in generated code generated by tools such as protobuf and thrift, you will be able to use your ecosystem’s IDE tools without modification5.

In a monorepo, you need the following properties from your build system:

1. Given a build target, build that target as efficiently as possible and produce an artifact.
1. Given a list of dirty files, produce the list of build targets that are directly or indirectly dirtied by those changes and need to be re-built.
Going back to the O(repo) principle, your build system SHOULD be capable of doing this without interacting with every file in the build graph (as e.g. Make does, when evaluating file modification times). Despite their complexity, Bazel and Buck2 do provide both of these capabilities to those who take the time to invest in their build. If your monorepo consists of a single language (like I said - keep it single language, if you can!) you can write your own program that inspects the build graph of your language ecosystem’s build and performs this calculation. This program is often called a “determinator” or “target determinator”:

- The guppy Rust crate provides means to traverse the Cargo build graph and build a determinator
- The golang.org/x/tools/go/packages library provides the means to traverse the package graph of a Go application, making it possible to write a determinator for Go packages
- If you are using Bazel, this target-determinator CLI and Go library is a determinator.
- Meta has a sophisticated implementation of a target determinator on top of buck2, but I don’t believe it is open-source.
Bazel and Buck2 offer sophisticated remote execution and caching capabilities, but realistically you aren’t going to need these unless your builds are really, really huge. If they are, go talk to EngFlow or something. The target determination property is more useful to the average company, because…

## Testing

… when developers are working in your monorepo, they need to know which tests to run to properly evaluate the changes they’ve made. Now that your company has a monorepo, running all of the tests isn’t a feasible option, because you suddenly have a lot of tests.

Anyone that has dealt with a large test suite before has lived the experience of chasing down flaky tests - tests that just fail sometimes. As the number of tests that you run to validate a change increases, your margin for flakiness decreases. If each test in your repository has 4 9s of reliability, in that they flake only one time every 10000, running 1000 tests gives a no-op change a 90% chance of passing CI. If you run 10000 tests, this probability goes down to 60%. If you run enough tests, you can end up with a mathematical near-certainty that your users’ CI test runs fail and they will be very upset with you.

Your unit testing system needs to get a bit smarter. It now needs to:

- Automatically retry test failures. A test that flakes with a low probability is substantially less likely to fail a test run if you retry it once. Test retries have substantially diminishing returns; a test that has failed twice in a row is likely to fail a third time. (Example)
- Only run tests that need to be run. Using the build system’s target determinator, the testing system can figure out the minimal set of tests that need to be run and only run those. (Example)
Optionally, your testing system can also quarantine tests that are known to be flaky, although that’s an added bonus that can come with time.

Your language ecosystem’s default test system (if it has one) likely does not support the features that you’re going to need out of this testing system. Some ecosystems (like Rust’s nextest, Java’s venerable JUnit, and many others) do have these capabilities.

## Continuous Integration

When a user submits a pull request to your monorepo, your CI system has to accomplish two things:

1. Given the scope of the change, produce any build artifacts that need to be produced to include said changes, and
1. Run any validations necessary to validate the change.
Like the testing system, the CI system needs to inspect the proposed change and trigger jobs that perform the required build and validation steps for a particular change. This is deeply tied to the build and test system’s idea of target determination from previous sections; for many large monorepo CI systems, the very first job triggered is a target determinator job that figures out based on the change what other jobs it needs to trigger.

Solving this problem in full generality in a multi-language repository is challenging, but at its core the algorithmic idea is to attach metadata to the build graph in such a way that if a node on the build graph is dirtied, a particular job should6 be run (e.g. with Bazel or Buck2). It can also be as simple as a mapping of target names to job names. The first CI’s job’s task is now to produce a set of jobs that must run based on how the changes submitted alter the build graph.

That sounds simple at first. For a long time, it is! However, it has long been known that a workflow that runs tests off a branch and merges the branch if they pass is not sufficient to prevent breakages in main. Open-source tools like homu and the more recent GitHub Merge Queue will actually run your CI twice; first, to validate the changes on your pull request, and then again when the CI system has rebased your changes against the latest change on main (an operation sometimes called “land”). The merge queue is a serialization point for all developers operating in this repository. If your CI jobs are long, users will have their changes languish in the queue for long periods of time or (worse) booted out of the queue when another engineer introduces a change that conflicts with their own.

Different projects choose different approaches here. The Rust project utilizes bors, a cousin of homu, to batch up changes and land them all at once, based on the assumption that changes that have passed some level of validation already are likely to continue passing automation at land time. Chromium does something similar. Uber uses knowledge of the build graph to determine whether or not two changes can be landed concurrently and will do so if it believes it to be safe.

No matter what you choose to do, though, you have a strong incentive to keep your CI as fast as possible to keep the merge queue moving along as quickly as possible. This is fundamentally at odds with CI’s general goal of catching problems before they reach the mainline. This design space is full of tradeoffs and you’ll want to think hard about what your organizational priorities are. In general you can trade off throughput, correctness, and tail latency.

Trading off throughput is relatively straightforward - you run all build and validation jobs as part of the land, for every commit. This might take a while and your merge queue might get clogged up during peak working hours, but your main will remain green at all times.

Trading off correctness is also relatively straightforward. Your CI’s target determinator can choose not to run all jobs but instead probabilistically select some of them, perhaps guided by some Bayesian analysis of which jobs are most likely to catch issues. You lose the guarantee that main is green all the time, but in exchange your developers can land code quickly. This tradeoff is often paired with CI jobs that run all of your tests at a regular cadence (sometimes called “trunk-time testing”, “nightlies”, or “hourlies”) and automatically bisect failures that arise in main.

Trading off tail latency is best seen in systems that batch up a bunch of changes and attempt to land them all at once. If the batch passes validation, you’ve saved a substantial amount of time in that you don’t have to run this validation for every commit in the batch; however, if it doesn’t, the entire batch fails the land and results in a false-positive failure for everyone in the batch that didn’t cause the breakage.

There’s no silver bullet here. The big monorepo companies all still wrestle with this problem. You’ll need to navigate the tradeoffs yourself and decide as an organization which costs you’re willing to tolerate.

## Continuous Delivery

The greatest power and biggest lie of the monorepo is that it is possible to make atomic commits across your entire codebase. While this is objectively true from a code perspective (you certainly can land a PR that, for example, renames a function across your entire codebase), this is not true from a deployment perspective, and this dangerous lie will cause incidents.

Your monorepo now contains many different deployable artifacts that deploy at different times. It is also technically possible to make, for example, a breaking change to a service’s interface, a service’s implementation, and the service’s clients all in one PR. However, this PR will break when you deploy it because you do not deploy your service and all of its clients atomically. While this is also possible in a world with many repositories, the requirement to do this change in multiple pull requests is often enough to remind engineers that breaking changes to a service contract are not safe to make.

Your users must understand that your deployment system operates asynchronously with respect to what happens in the monorepo. Its primary interaction with the monorepo is to go and pick up the “latest” build artifacts for a particular service; everything else happens on timetables that are potentially not under your control and can happen arbitrarily far in the future.

A common CI job in a monorepo is to validate service contracts and make sure that they are not broken unless the author deliberately intended to do so, and they are required to provide a justification as to why such a change is OK.

## Conclusion

A monorepo is a powerful tool for institutional consistency. An organization can use their monorepo to enforce engineering culture, organizational standards, and build a culture of code sharing and a willingness to cross organizational boundaries to solve problems. It does not come for free. You should be aware of the engineering lifts that you will need to do to achieve a productive monorepo and be aware that this is a continuous process as you continue to scale and your tools begin to break.

In my experience - it’s worth it, if you’re willing to commit to it.

1. 
1. 
1. 
1. 
1. 
1. 

