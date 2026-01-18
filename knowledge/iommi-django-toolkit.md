# iommi - Django Power Tools

Source: https://iommi.rocks/

## What is iommi?

iommi is a productivity toolkit for Django that simplifies creating complex UIs (forms, tables, pages) without boilerplate code. It provides a declarative Python approach to building admin-like interfaces quickly.

## Key Features

- **Declarative page composition** - Build pages in Python, not templates
- **Tables** - Sorting, filtering, pagination with minimal config
- **Forms** - Complex form handling without repetitive code
- **Design system integration** - Works with existing CSS frameworks
- **Minimal configuration** - Sensible defaults, override what you need

## Why Consider It

- Reduces repetitive UI code significantly
- Good for internal tools, admin dashboards, CRUD interfaces
- Leverages existing Django knowledge - not a separate framework
- Active community and support

## Installation

```bash
pip install iommi
```

## When to Use

- Building admin interfaces or internal tools
- Projects with lots of data tables and forms
- When you want polished UI without frontend framework complexity
- Rapid prototyping of Django apps

## Tradeoffs

- Learning curve for the declarative API
- May be overkill for simple projects
- Less flexibility than custom frontend for highly custom UIs
- Another dependency to maintain

## Related

- Django Admin (built-in, less flexible)
- django-tables2 (tables only)
- django-crispy-forms (forms only)
