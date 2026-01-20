# Trunk-Based Development

Development practice where the entire team works on a shared main branch instead of long-lived feature branches.

## Core Principles

1. **Single shared branch** - Everyone commits to main/trunk
2. **Small, frequent commits** - Keep changes digestible
3. **Feature flags** - Manage incomplete features in code, not branches
4. **Fast CI** - Tests must run quickly to not block flow

## Why It Works

**Problems with long-lived branches:**
- Merge conflicts accumulate over time
- Scope creep ("while I'm here, let me refactor...")
- Risk increases with branch age
- Rolling back requires redeploy

**Trunk-based benefits:**
- No merge hell
- Continuous integration actually works
- Features can be disabled instantly via flags
- Code stays in sync across team

## Feature Flags

Move branching from git into code:

```javascript
// Static flag (hardcoded)
const featureFlagEnabled = true;

// Dynamic flag (from feature management system)
const { isEnabled } = useFeature("new-feature");
return isEnabled ? <NewComponent /> : <OldComponent />;
```

**Static flags**: Hardcoded, requires deploy to change
**Dynamic flags**: Controlled externally, instant changes without deploy

## Practical Implementation

- Pre-push/pre-commit hooks to run tests locally
- Small PRs if using PR workflow (must be reviewed quickly)
- Feature management tools: Bucket, LaunchDarkly, Flagsmith, etc.
- Clean up flags after features are fully rolled out

## When to Use

Works well for:
- Teams practicing continuous delivery
- Projects with good test coverage
- Teams committed to fast PR reviews

May be harder with:
- Complex local test environments
- Teams with slow review culture
- Massive features that can't be incrementally released

Source: https://bucket.co/blog/trunk-based-development
