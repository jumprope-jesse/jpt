# shadcn/ui

Copy-paste component library for React applications built on Radix UI and Tailwind CSS.

## Overview

- **URL**: https://ui.shadcn.com/
- **License**: Open Source
- **Foundation**: Radix UI primitives + Tailwind CSS
- **Philosophy**: Not a traditional npm package - you copy components into your project

## Key Differentiators

Unlike traditional component libraries (Material UI, Chakra, etc.):
- Components are copied into your codebase, not installed as dependencies
- Full ownership and customization of component code
- No version lock-in or breaking changes from upstream
- Uses a CLI to add components: `npx shadcn@latest add button`

## Features

- Accessible by default (built on Radix UI)
- Beautifully designed defaults
- Dark mode support
- TypeScript support
- Highly customizable (you own the code)

## Common Components

- Buttons, inputs, forms
- Dialogs, popovers, tooltips
- Data tables, cards
- Navigation menus
- And many more via the registry

## Usage

```bash
# Initialize in a project
npx shadcn@latest init

# Add specific components
npx shadcn@latest add button
npx shadcn@latest add dialog
npx shadcn@latest add table
```

## Ecosystem

shadcn/ui has become a foundation for other libraries:
- AI Elements (AI-native components)
- Various community extensions via the registry system

## When to Use

- Building React/Next.js applications
- Want accessible, well-designed components
- Need full control over component styling and behavior
- Prefer owning code over depending on external packages
