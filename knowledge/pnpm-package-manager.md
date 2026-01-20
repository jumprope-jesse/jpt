# pnpm Package Manager

## Security: Delayed Dependency Updates (v10.16+)

The `minimumReleaseAge` setting delays installation of newly released packages to reduce risk from compromised versions (most attacks are discovered and removed within an hour).

```yaml
# .npmrc or pnpm-workspace.yaml
minimumReleaseAge: 1440  # minutes - only install packages released 1+ day ago

# Exclude specific packages from this restriction
minimumReleaseAgeExclude:
  - webpack
```

## Advanced Dependency Filtering with Finder Functions (v10.16+)

Search dependencies by any property (not just name) using custom finder functions in `.pnpmfile.cjs`:

```javascript
// .pnpmfile.cjs
module.exports = {
  finders: {
    // Find packages with React 17 in peer dependencies
    react17: (ctx) => {
      const manifest = ctx.readManifest();
      if (manifest.peerDependencies?.react === "^17.0.0") {
        return `license: ${manifest.license}`;  // return string for extra output
      }
      return false;
    },
  },
};
```

Usage:
```bash
pnpm why --find-by=react17
```

## Sources
- [pnpm 10.16 release notes](https://pnpm.io/blog/releases/10.16)
