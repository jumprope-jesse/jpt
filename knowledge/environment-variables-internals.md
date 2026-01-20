# Environment Variables Internals

Source: https://allvpv.org/haotic-journey-through-envvars/

## Overview

Environment variables are a legacy Unix mechanism for passing configuration from parent to child processes. They're a flat, untyped dictionary of strings with no namespaces.

## How They Propagate

Environment variables are passed from parent to child via the `execve` syscall:

```c
SYSCALL_DEFINE3(execve,
    const char __user *, filename,
    const char __user *const __user *, argv,
    const char __user *const __user *, envp)
```

The three arguments:
1. `filename` - executable path (e.g., `/usr/bin/ls`)
2. `argv` - command line arguments (e.g., `['ls', '-lah']`)
3. `envp` - environment variables (e.g., `['PATH=/bin:/usr/bin', 'USER=allvpv']`)

By default, all envvars are inherited by child processes. A parent can pass a completely different or empty environment if desired.

## Storage After Launch

The kernel dumps variables onto the stack as null-terminated strings. Since this static layout can't easily be modified, programs copy them into internal data structures:

**Bash**: Stack of hashmaps. When spawning a process, traverses the stack to find exported variables.

**glibc**: Dynamic `environ` array managed via `putenv` and `getenv`. Linear time complexity (O(n)) - not a high-performance dictionary.

**Python**: `os.environ` is built from C library's `environ` array on startup. Changes to `os.environ` invoke `os.putenv`, which calls the C library's `putenv`.

## Format Rules

The Linux kernel is very liberal:
- Variables can have duplicated names with different values
- Entries don't require `=` sign
- Only strict requirement: name cannot contain `=`
- Size limitations enforced by kernel

### Quirks by Shell

- **Nushell**: Allows spaces in variable names (`$env."Deployment Environment" = "prod"`)
- **Python**: Also handles spaces fine
- **Bash**: Can't reference variables with whitespace in names, but stores them in `invalid_env` hashmap and passes them to child processes

## Naming Convention Myth

Common misconception: POSIX only permits uppercase envvars.

Reality: POSIX-specified *utilities* use uppercase, but you're encouraged to use lowercase for your own envvars to avoid collisions. The only strict rule is no `=` in names.

## Practical Recommendation

- Names: `^[A-Z_][A-Z0-9_]*$` (uppercase with underscores)
- Values: UTF-8 encoding
- For maximum safety: Use POSIX Portable Character Set (ASCII without control characters)

## Relevance for launchd

This explains why launchd services don't inherit shell PATH - they don't have a parent shell process passing environment. Must explicitly set `EnvironmentVariables` in plist files.
