---
type: link
source: notion
url: https://bucket.co/blog/trunk-based-development
notion_type: Tech Deep Dive
tags: ['Running']
created: 2025-02-13T03:34:00.000Z
---

# Trunk-based development: Increasing engineering velocity and reducing frustration | Bucket

## Content (from Notion)

When working on large projects, there’s a natural tendency to create a branch and start hacking away. When you have a separate branch like this, things tend to balloon. As a developer, you get the urge to refactor all sorts of adjacent things that’ll make your changes cleaner. Before you know it, the scope of your branch is significantly larger than you had originally planned.

Even if you stay vigilant about the scope of your branch, you often run into frustrating merge conflicts that can introduce new errors or accidentally roll back other people’s changes if you’re not careful. Scoping features into the smallest possible size that makes sense for the end-user is good practice, but even when doing so, you often have new features or refactoring that can take several weeks or even months to finish.

The longer your branch has been living on its own, the harder it is to merge back into the main branch when the time comes because the main branch (“trunk”) has had plenty of changes happen since then.

On top of that, once you finally get a feature merged and deployed, it can often happen that there’s a bug causing users to have a poor experience. Since your new feature lives directly in the code, deactivating it requires rolling back the code you merged, building it, waiting for the tests to run, and redeploying the application - all the while, users are having a bad experience!

What if your whole team could just work on the same code at the same time to avoid these merge conflicts AND there was a quick way to deactivate features that aren’t behaving without needing to deploy?

This is where trunk-based development comes into play.

## Trunk-based development

Trunk-based development is the seemingly radical idea of a team working together on the same code base at the same time. At its most radical, team members push directly to the main branch.

You’ll want to make sure that the tests run on the whole integrated code base before hitting main. If your tests can all run on the developer machines, this is a very low-friction way to get started with trunk-based development. Ensuring that tests run locally before being merged into main can happen through pre-push/pre-commit hooks in Git.

In practice, many teams will use a pull request-based workflow because the tests could be too complicated to run locally or need to facilitate code reviews. For trunk-based development to fulfill its promise, it’s imperative that pull requests are kept small and that the team is committed to reviewing them quickly.

But how do you make it possible to manage these half-finished features that are suddenly living in the code base?

Trunk-Based Development

## Branching in the code

With trunk-based development, you move the branching out of the version control system like Git and into the code (or adjacent configuration). But introducing branches in the code sounds like a dirty concept at first:

Does that mean I’ll have a bunch of if-statements throughout the code?

In many cases: yes - actually. But with the right tooling and a little bit of caretaking, it’s well worth the complexity.

The basic form is very … well, basic:

```plain text
import React from 'react';‍

// Simulating a feature toggle/flag (this could be from a config file or context)const featureFlagEnabled = true;‍

const NewComponent = () => <div>New component is now enabled!</div>;
const OldComponent = () => <div>Old component is still active.</div>;‍

const MyComponent: React.FC = () => {
	return (
      <div>        {featureFlagEnabled ? <NewComponent /> : <OldComponent />}
      </div>
    );
};‍

export default MyComponent;
```

‍

The value of featureFlagEnabled can be hardcoded. That’s the most basic branching mechanism called a static feature flag.

On the other hand, dynamic feature flags can provide flexibility by enabling real-time control over feature activation without requiring redeployment.

Using dynamic feature flags is also straightforward, and they resemble their static cousins:

```plain text
import { useFeature } from "@bucketco/react-sdk";‍

const MyFeature = () => {
	const { isEnabled, track } = useFeature("new-feature");

    // check if new feature is enabled      return isEnabled ? <NewComponent /> : <OldComponent />}
```

‍

The value isEnabled can be managed externally through a feature management system like Bucket. Dynamic toggles allow teams to test features in production with real users, roll out features gradually, and quickly revert if issues arise—all of which are key advantages for continuous delivery.

## Continuous Delivery and Faster Releases

Trunk-based development aligns perfectly with continuous delivery. By keeping the mainline deployable at all times and using feature flags to manage branches, teams can release features incrementally without waiting for everything to be fully completed. Code can be deployed even when some features are still behind a flag, reducing risk and accelerating the feedback loop.

This means features can be tested and refined in production, allowing teams to release new capabilities faster without deploying new versions. With dynamic feature toggles, changes can be rolled out or reverted instantly, enabling faster, safer releases.

## In Summary

Trunk-based development helps teams avoid merge conflicts, streamline integration, and deliver software faster. By committing small, frequent changes to a shared main branch and using feature flags to manage incomplete code, developers can keep both active and inactive features in sync. Whether in small or large teams, trunk-based development promotes faster, more reliable software delivery through continuous integration and feature flagging.

For teams looking to improve their workflow and accelerate delivery, trunk-based development is a practice worth embracing.


