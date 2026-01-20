# django-admin-ordering

Drag-and-drop reordering for Django admin change lists and inlines.

**Repo**: https://github.com/matthiask/django-admin-ordering

## Installation

```bash
pip install django-admin-ordering
```

Add to `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    'admin_ordering',
]
```

## Usage

### For Models

Inherit from `OrderableModel` to add an ordering field:

```python
from admin_ordering.models import OrderableModel

class MenuItem(OrderableModel):
    name = models.CharField(max_length=100)
    # ordering field added automatically
```

### For Admin

Use `OrderableAdmin` mixin:

```python
from admin_ordering.admin import OrderableAdmin

@admin.register(MenuItem)
class MenuItemAdmin(OrderableAdmin, admin.ModelAdmin):
    list_display = ['name', 'ordering']
    list_editable = ['ordering']
```

### For Inlines

Works with `TabularInline` and `StackedInline`:

```python
class MenuItemInline(OrderableAdmin, admin.TabularInline):
    model = MenuItem
```

## Limitations

- Works best with **unpaginated, unfiltered** lists
- Can only be used as a mixin, not for direct model registration
- Ordering values increment by 10 (relative positioning only)

## Use Cases

- Menu item ordering
- Image galleries
- FAQ sections
- Any content that needs manual sequencing

## OrderableModel Internals

The abstract model provides:

- **Auto-increment on save**: If `ordering` is 0/None, sets to `max(ordering) + 10`
- **Comparison support**: Uses `@total_ordering` for `<` comparisons
- **System checks**: Warns if model doesn't inherit `OrderableModel.Meta` for proper ordering

```python
# Key behavior: auto-assigns ordering on first save
def save(self, *args, **kwargs):
    if not self.ordering:
        max = self.__class__._default_manager.aggregate(m=Max("ordering"))["m"]
        self.ordering = 10 + (max or 0)
    super().save(*args, **kwargs)
```

The field is a `PositiveIntegerField` with `db_index=True` for efficient sorting.
