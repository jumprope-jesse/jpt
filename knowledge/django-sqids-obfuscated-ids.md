# django-sqids: Non-intrusive Obfuscated IDs for Django

A library that provides obfuscated IDs (sqids) for Django models without modifying the database schema.

**GitHub**: https://github.com/julianwachholz/django-sqids
**Install**: `pip install django-sqids`
**Compatibility**: Django 3.2, 4.2, 5.0; Python 3.8-3.12

## What It Does

- Proxies the internal model `pk` field without storing anything in the database
- Allows lookups and filtering by sqid string
- Works with Django REST Framework serializers
- Works with Django Admin search

Forked from `django-hashids` to use the newer Sqids library.

## Basic Usage

```python
from django_sqids import SqidsField

class Item(Model):
    sqid = SqidsField(real_field_name="id")
```

```python
instance = Item.objects.create()
instance.id    # 1
instance.sqid  # '1Z'

# Query by sqid
Item.objects.get(sqid="1Z")
Item.objects.filter(sqid__in=["1Z", "4x"])
Item.objects.values_list("sqid", flat=True)
```

## URL Integration

Use sqids as slugs in URLs:

```python
# urls.py
path("item/<slug>/", ItemDetailView.as_view(), name="item-detail")

# views.py
class ItemDetailView(DetailView):
    model = Item
    slug_field = 'sqid'
```

## Admin Search

```python
class ItemAdmin(admin.ModelAdmin):
    search_fields = ["sqid__exact"]
```

## Configuration

Global settings:
- `DJANGO_SQIDS_MIN_LENGTH` - minimum length of generated sqids
- `DJANGO_SQIDS_ALPHABET` - character set to use

Per-field customization with `min_length` and `alphabet` arguments.

## Alphabet Shuffling (replacing "salt")

Sqids removed "salt" for security reasons. Use `shuffle_alphabet` instead:

```python
from django_sqids import SqidsField, shuffle_alphabet

class MyModel(models.Model):
    sqid = SqidsField(alphabet=shuffle_alphabet(seed='randomSeed'))
```

## Use Cases

- Public-facing URLs where sequential IDs reveal business data
- API endpoints where you don't want to expose raw database IDs
- Any case where you want short, URL-safe identifiers
