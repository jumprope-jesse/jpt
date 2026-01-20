# Monorepo Infrastructure

Comprehensive guide to building and operating a productive monorepo, from a developer productivity perspective.

Source: [The Ingredients of a Productive Monorepo](https://blog.swgillespie.me/posts/monorepo-ingredients/)

## The Golden Rule

> Any operation over your repository that needs to be fast must be O(change) and not O(repo).

As monorepos grow, tools that are O(repo) will break. Most blog posts from big companies about developer tooling describe implementing this principle.

## Why Monorepo?

Good reasons:
- Consistency and organizational coherence
- Shared tooling efforts
- Dev productivity can focus on improving one place
- Engineering leadership can define and enforce conventions
- Engineers can contribute across codebases knowing they work the same way

Bad reasons:
- "Google/Meta/Uber does it" - you won't achieve their outcomes with a small team
- Their blog posts describe end states far beyond most companies' capabilities

## Source Control

Git is O(repo) by design - operations like `git status` slow as repo grows.

**Scaling strategies when git breaks:**
1. **Sparse checkout** - Only clone files in a configured subset. Git and Mercurial (hg sparse) support this.
2. **Virtual filesystem** - Present full repo but lazily download files on-demand. Google, Meta, Microsoft all implemented this.

**Practical note:** Generated code (protobuf, thrift) grows your repo faster than developer output.

**Future:** Jujutsu has extension points for virtual filesystem support - promising for open-source monorepos.

## Building

**Key advice:** Keep monorepo single-language if possible. Use your language ecosystem's build system (Maven/Gradle, CMake, Cargo, Go build) for as long as you can. They scale further than you expect.

**Build system requirements:**
1. Given a target, build it efficiently and produce an artifact
2. Given dirty files, produce the list of targets that need rebuilding

**Target Determinators** - programs that inspect build graphs and determine what to build:
- Rust: `guppy` crate
- Go: `golang.org/x/tools/go/packages`
- Bazel: `target-determinator` CLI

**On Bazel/Buck2:** They work, but require a dedicated "Build Team" as a full-time job. Avoid if possible.

**On checking in generated code:** Enables IDEs to work without modification - a practical tradeoff.

## Testing

**The flakiness problem:** If each test has 4 9s reliability (flakes 1/10000), running 1000 tests gives 90% pass rate on no-op changes. 10000 tests = 60%.

**Required capabilities:**
1. **Automatic retries** - Test that flakes with low probability is much less likely to fail if retried once. Diminishing returns beyond 2 retries.
2. **Targeted test selection** - Only run tests that could be affected by changes (via target determinator)

**Optional:** Quarantine known flaky tests

**Tools:** Rust's nextest, Java's JUnit have these capabilities.

## Continuous Integration

CI must:
1. Produce build artifacts for the change scope
2. Run validations for the change

**The merge queue problem:** Running tests on a branch then merging isn't enough to prevent main breakages. Need to test rebased against latest main.

The merge queue is a serialization point - long CI = queued changes languish or get booted.

**Tradeoff triangle: throughput, correctness, tail latency**

| Trade off | Strategy | Cost |
|-----------|----------|------|
| Throughput | Run all jobs for every land | Merge queue clogs during peak |
| Correctness | Probabilistically select jobs, bisect failures in nightlies | Main not always green |
| Tail latency | Batch commits and land together | One failure blocks entire batch |

**Tools:**
- bors/homu - batch changes
- GitHub Merge Queue - automatic rebasing
- Custom solutions (Uber) - concurrent landing based on build graph analysis

## Continuous Delivery

**The dangerous lie:** Atomic commits are possible in the repo, but not in deployment.

A PR can change a service interface, implementation, AND clients - but they don't deploy atomically, so it will break.

**CI job:** Validate service contracts aren't broken without deliberate justification.

## Related

- [Jujutsu version control](jujutsu-version-control.md) - Modern VCS with monorepo potential
- [Haystack code review](haystack-code-review.md) - PR merge queue tooling
