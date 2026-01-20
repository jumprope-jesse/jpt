---
type: link
source: notion
url: https://jordaneldredge.com/blog/grats/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-03-07T23:42:00.000Z
---

# Grats: A More Pleasant Way to Build TypeScript GraphQL Servers / Jordan Eldredge

## AI Summary (from Notion)
- Grats Overview: A tool designed to enhance the developer experience of building GraphQL servers in TypeScript.
- Key Functionality: Utilizes docblocks to annotate TypeScript code, allowing Grats to automatically derive a fully type-safe GraphQL schema without explicit type declarations.
- Implementation-First Development: Grats adopts an "implementation-first" approach, leveraging static analysis instead of runtime introspection or compile-time macros, which are not feasible in TypeScript.
- Pros of Using Grats:
- Automatic type safety: TypeScript types directly map to GraphQL types.
- No runtime overhead: Functions as a development-only tool, maintaining performance.
- User-friendly error messages: Offers precise and helpful feedback on errors.
- Encourages best practices: Defaults to nullable typing, aligning with GraphQL best practices.
- Cons of Using Grats:
- Introduces a build step, adding friction to the development process.
- Lacks a plugin ecosystem, unlike more established tools.
- Requires developers to mentally design their schema without forced design structures.
- Conclusion: Grats aims to create a more pleasant and lightweight experience for TypeScript GraphQL server development, advocating for its innovative approach.
- Resources: The article includes links to the Grats website, quick start guide, playground, migration guides, and design principles for further exploration.

## Content (from Notion)

For the last year I’ve been building Grats with the goal of demonstrating what I believe to be a fundamentally better developer experience for building GraphQL servers in TypeScript.

The idea is that you simply annotate your existing TypeScript code with docblocks to indicate which constructs you want to expose and let Grats leverage your code’s existing names and types to extract a fully type-safe, executable, GraphQL schema.

Let’s look at an example of a simple model that’s been annotated:

```plain text
/**
 * A user in our system
 * @gqlType
 */
type User = {
/** @gqlField */
  name: string;
};

/** @gqlField */
export function greeting(user: User): string {
return `Hello ${user.name}`;
}
```

From this, Grats derives this GraphQL schema:

```plain text
"""
A user in our system
"""
type User {
  name: String!
  greeting: String!
}
```

Playground link

Note that we didn’t have to explicitly declare any of the types or names that we wanted to appear in our schema. Grats simply derives them directly from our TypeScript code. People who have adopted Grats report that it makes the development of GraphQL servers feel more lightweight, and that much of the mental overhead of GraphQL seems to melt away.

## Bringing implementation-first development to TypeScript

This method of schema development, which I call implementation-first, is not new in the GraphQL ecosystem. Python has Strawberry, C# has Hot Chocolate, and Rust has Juniper, and Meta's internal GraphQL server (written in Hack/PHP) operates very similarly. However those tools all depend upon either runtime type introspection or compile-time macros, neither of which is possible in TypeScript.

Enabling implementation-first GraphQL for TypeScript requires a novel approach. Grats’ innovation is that it implements schema extraction using static analysis*.* Grats analyzes your code as a collection of ASTs and from that is able to infer your GraphQL schema.

## Pros

In addition to the improved developer experience, Grats has a number of other advantages relative to existing TypeScript offerings:

- Automatic type safety — Your TypeScript types are your GraphQL types. No need to keep your schema declarations in sync with your implementation.
- No runtime overhead — Grats is a development-only build tool, it does not introduce any runtime overhead or increase bundle size. This can be especially impactful when used at the edge or in the browser.
- Friendly error messages — Instead of relying on sophisticated TypeScript types which often report verbose and cryptic errors, Grats has an exact understanding of each issue it reports and has customized and helpful error messages for each.
- Encourages best practices — Grats defaults to typing all fields as nullable, a GraphQL best practice which helps enable more resilient responses.
## Cons

No solution is without tradeoffs. Here are some reasons why reasonable people might choose not to use Grats:

- Grats introduces a build step — Build steps introduce friction into your development process which must be weighed against the pros enumerated above.
- No existing plugin ecosystem — Well-established tools like Pothos come with an ecosystem of plugins which can provide significant value. Grats does not (yet?) have a comparable ecosystem.
- Schema design is not forced — Schema-first solutions provide a forcing function to explicitly and intentionally design your schema. With Grats, you must mentally design your schema as you implement it, and then confirm that design with the generated schema.
## Conclusion

Grats leverages a novel static analysis approach to enable a lighter weight and overall more pleasant developer experience for building GraphQL servers with TypeScript. If it sounds interesting to you, please check out the Grats website. Some places to start might be:

- Quick Start
- Playground
- Incremental Migration
- Design Principles
If you have questions or comments I’d love to hear from you on Twitter, Threads, or in the Grats Discord server.


