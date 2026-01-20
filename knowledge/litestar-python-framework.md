# Litestar Python Web Framework

Async-first, type-hint-driven Python web framework. Alternative to FastAPI with better architecture for scaling codebases.

Source: https://www.b-list.org/weblog/2025/aug/06/litestar/

## Why Litestar Over FastAPI

### Standalone Route Decorators
FastAPI/Flask route decorators are bound to the app object, causing circular import issues in multi-file apps. Litestar's decorators are standalone functions.

```python
# Litestar - route decorator is standalone
from litestar import Litestar, get

@get("/greet")
async def greet(name: str) -> str:
    return f"Hi, {name}!"

app = Litestar([greet])
```

No need for "API router" or "blueprint" workarounds when splitting code across files.

### Composable Router Architecture
Routers can be nested with shared configuration:

```python
from litestar import Router
from litestar.di import Provide

_write_router = Router(
    guards=[some_auth_function],
    route_handlers=[create_widget, delete_widget, update_widget]
)

widget_router = Router(
    dependencies={"widget_dep": Provide(some_dependency)},
    path="/widgets",
    route_handlers=[get_widget, get_widget_list, _write_router]
)
```

Same route can be registered multiple times with different auth/dependencies.

### Not Coupled to Pydantic
Supports Pydantic, dataclasses, msgspec, attrs, and SQLAlchemy models. Plugins available for custom serialization.

### DTO System for SQLAlchemy
Automatically derive DTOs from SQLAlchemy models instead of duplicating field definitions:

```python
from litestar.dto import DTOConfig
from litestar.plugins.sqlalchemy import SQLAlchemyDTO

class ReadWidget(SQLAlchemyDTO[Widget]):
    config = DTOConfig(exclude={"id", "internal_notes"})
```

Fields derived automatically from ORM model - no manual transcription.

## Advanced Alchemy Integration

Litestar team maintains Advanced Alchemy library with:

- Generic repository implementations (sync/async) derived from SQLAlchemy models
- Service-layer abstractions
- Database-agnostic types (big-integer PKs, UTC timestamps, JSON)
- Automatic create/update timestamps
- UUID-keyed models
- CLI helpers for migrations (Alembic), seeding, dumping

```python
from litestar.plugins.sqlalchemy import repository

class WidgetRepository(repository.SQLAlchemyAsyncRepository[Widget]):
    model_type = Widget
# Now has list(), get_one(), add(), delete(), paginated fetches...
```

## Built-in Features

- Auth system (guard functions + middlewares)
- "Stores" framework for caching
- Logging integration (stdlib + structlog)
- Problem details error responses
- Prometheus/OpenTelemetry metrics
- htmx support

## History

Originally named "Starlite" (built on Starlette). Renamed to Litestar in v2.0 (2023) after dropping Starlette dependency.

## When to Use

- Building async Python web apps
- Multi-file applications (avoids circular import dance)
- Heavy SQLAlchemy usage (better integration than FastAPI)
- Want Django-like conveniences in a microframework
- Need composable route configuration (different auth per registration)
