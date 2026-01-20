# TanStack Libraries

Source: https://tanstack.com/

Collection of headless, type-safe utilities for web development. Framework-agnostic (works with React, Vue, Solid, Svelte, Angular, etc.).

## Core Libraries

### TanStack Query (formerly React Query)
- Asynchronous state management and data fetching
- Handles fetch, cache, update for async data
- No global state needed
- Available for React, Vue, Solid, Svelte, Angular
- Zero dependencies, lightweight

**Key Features:**
- Auto caching & garbage collection
- Background updates & stale data handling
- Window focus refetching
- Polling/realtime queries
- Parallel & dependent queries
- Paginated/cursor & infinite scroll queries
- Mutations API
- Prefetching & SSR support
- Suspense ready
- Offline support
- Dedicated devtools

**Used by:** Google, Walmart, Facebook, PayPal, Amazon, Microsoft, Target, eBay

**Learning:** Official course at query.gg (by Dominik Dorfmeister and ui.dev)

### TanStack Router
- Type-safe routing for React applications
- First-class search-params for URL state management
- Works for client-side and full-stack apps

### TanStack Table
- Headless UI for tables and datagrids
- 100% control over markup and styles
- Works with React, Vue, Solid, Svelte, Qwik, Angular, Lit

### TanStack Form
- Headless, performant, type-safe form state management
- Works with React, Vue, Angular, Solid, Lit

### TanStack Virtual
- Virtualization for large scrollable lists
- 60 FPS performance with massive DOM nodes
- Works with React, Vue, Solid, Svelte

### TanStack Start (coming soon)
- Full-stack React framework powered by TanStack Router
- SSR, streaming, server functions, bundling
- Built on Vinxi and Nitro

## Design Philosophy

- **Headless**: Full control over styling and markup
- **Type-safe**: First-class TypeScript support
- **Framework-agnostic**: Same API patterns across frameworks
- **Focused**: Each library does one thing well

## When to Use

- Query: Replace Redux/global state for server state management
- Table: Complex data tables without fighting a component library's opinions
- Form: When you need granular control over form UX
- Virtual: Long lists (1000+ items) that need to remain performant

## Related

See also: frontend-framework-critique.md for perspective on framework choices
