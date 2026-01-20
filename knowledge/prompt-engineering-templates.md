# Prompt Engineering Templates & Patterns

Quick-reference templates and patterns for structuring LLM prompts.

---

## General Prompt Template (7-Part Structure)

A systematic approach to constructing prompts:

```
Act like a [Specify a role],

I need a [What do you need?],

you will [Enter a task],

in the process, you should [Enter details],

please [Enter exclusion],

input the final result in a [Select a format],

here is an example: [Enter an example]
```

**Example:**
```
Act like a senior Python developer,

I need a function to parse CSV files with error handling,

you will read the file and return a list of dictionaries,

in the process, you should validate each row has the expected columns,

please don't use pandas (stdlib only),

input the final result in a code block with docstring,

here is an example:
def parse_users(filepath):
    """Parse users.csv and return list of user dicts."""
    ...
```

*Source: https://mitenmit.github.io/gpt/ - Added: 2026-01-19*

---

## Related Resources

- See `anthropic-prompt-engineering-fundamentals.md` for comprehensive Claude-specific techniques
- See `aws-bedrock-prompt-management.md` for production prompt versioning
