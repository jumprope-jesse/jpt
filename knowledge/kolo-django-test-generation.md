# Kolo - Django Test Generation from Traces

Kolo is a tracing, visualization, and test generation tool for Python and Django that automatically generates integration tests by inverting execution traces.

## Core Concept: Trace Inversion

When Kolo is enabled, it captures everything that happens during code execution:
- Function calls and return values
- HTTP requests and responses
- SQL queries and their results
- Variables and state changes

This trace data can then be "inverted" to generate an equivalent integration test.

## How Test Generation Works

1. **Capture a trace** - Enable Kolo middleware and make a request to your Django app
2. **Generate test** - Run `kolo generate-test {trace_id} > test_example.py`
3. **Refine** - Tweak the generated test as needed (delete unnecessary assertions, etc.)

### What Kolo Generates

For each frame in the trace:
- HTTP requests → Django test client calls
- SQL SELECTs → Seed data setup (using factories if available)
- SQL UPDATEs/INSERTs → Post-request assertions
- Status codes → Response assertions

### Example Output

```python
class MyTestCase(TestCase):
    def test_my_view(self):
        # Seed data from SQL queries
        todo, _created = Todo.objects.get_or_create(
            title="Give a talk at Django Day Copenhagen",
            defaults={"id": 50}
        )

        # HTTP request from trace
        response = self.client.get("/")

        # Assertions from response
        self.assertEqual(response.status_code, 200)
```

## Installation & Usage

```bash
pip install kolo
```

Add middleware to `settings.py`:
```python
MIDDLEWARE = [
    'kolo.middleware.KoloMiddleware',
    # ... other middleware
]
```

Generate tests:
```bash
kolo trace list --count 1  # Get latest trace ID
kolo generate-test trc_XXXXX > test_example.py
```

## Why Integration Tests?

Kolo focuses on integration tests (full HTTP stack via test client) rather than unit tests because they provide the most confidence that "everything still works." Reference: "Write tests. Not too many. Mostly integration."

## Customization

- Can use existing factoryboy factories
- Custom trace processors for specialized context
- Fully customizable test templates

## Limitations

- VSCode extension for visualization (web version in development)
- Some generated code is conservative (e.g., specifying IDs explicitly) and may need cleanup
- Not smart enough to distinguish between "loaded by ID in request" vs "loaded by query"

## Links

- Docs: https://kolo.app
- Blog post: https://blog.kolo.app/tests-no-joy.html
- Built by the Simple Poll team
