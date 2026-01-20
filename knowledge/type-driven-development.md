# Type-Driven Development

Principles for using type systems as the foundation of software design, particularly in TypeScript.

---

## How Types Make Hard Problems Easy (Mayhul)

*Source: https://mayhul.com/posts/type-driven-design/ - Added: 2026-01-18*

A practitioner's guide to type-driven development from experience on a 300k+ LOC TypeScript full-stack application (Heartbeat). The thesis: leaning into the type system transforms coding—features practically code themselves, entire categories of bugs vanish, and refactors become trivial.

### 1) Let the Types Flow

Invest in type safety across every surface of the application. Data flow: database → server → client. Changing your database schema should cause errors in your frontend code.

**Enabling type flow requires:**
- Using the same language everywhere (TypeScript on mobile + server via React Native + Node.js)
- Typed ORMs (Prisma, Drizzle) and typed API frameworks (tRPC)
- Monorepos (changes in one part alert you about implications elsewhere)
- Using `any` very rarely

### 2) Start with the Types

The natural starting place for any new feature is type definitions. First map out: what entities are involved, their relationships, their properties.

**Benefits:**
- Forces you to wrangle components comprehensively before implementation
- Discovers gaps/ambiguities in specs early (before you're halfway through)
- Human-readable documentation that's guaranteed to be accurate
- Type definitions are both documentation AND real code

**Key insight:** An entity's conceptual idea is more important than its representation. Email address and customer ID are both strings, but they're independent things—reflect this in types.

### 3) Make Illegal States Unrepresentable

Structure types so invalid states cannot exist:

```typescript
// Product must have at least one price
type NonEmptyArray<T> = [T, ...T[]];
interface Product {
    prices: NonEmptyArray<Price>;
}

// Address is all-or-nothing, not partially filled
type User = {
    address: {
        line1: string;
        line2: string;
        city: string;
        state: string;
        country: string;
    } | null;
};
```

**Every illegal state you eliminate was a bug waiting to happen in an alternate universe.** The process forces questions: Are there cases where a product has no prices? How many possible states exist?

### 4) Parse, Don't Validate

From Alexis King's influential article: types can "store" validation work.

**Benefits of encoding validation in types:**
- Rest of code can make assumptions without re-validating
- Type system enforces validation happens when needed
- Changing assumptions is easier—types point to implications

**Key insight:** Parsing converts less-typed data (raw input) into more-typed data (validated structures). Once parsed, you know the data is valid by construction.

### 5) Be Honest

Programming is finding the truth—the purest essence of what an entity represents. If two things you thought were the same are actually different, split them into different types.

**The calendar example:** An `Event` is stored in the database. An `EventInstance` is generated from recurring rules. They're similar but distinct:
- Events can be created/deleted; instances are ephemeral
- Editing an event changes all occurrences; editing an instance changes one
- Conflating them causes bugs (clicking delete on a recurring event instance deletes the whole event)

Being lazy with the first implementation "introduced a subtle lie into our type system that corrupted it."

### 6) Be Specific

Use branded types for specificity beyond structural typing:

```typescript
type CommunityID = string & { readonly _: "__CommunityID__" };
type UserID = string & { readonly _: "__UserID__" };

// Now the type checker catches wrong-ID errors:
function getIsUserAdmin(userID: UserID) { /*...*/ }
getIsUserAdmin(post.communityID); // Type error!
```

### 7) Pure Functions as a Type Bridge

Any user action reduces to a series of type jumps. Pure functions are how you convert one type to another cleanly.

**Pattern for full-stack apps:**
1. Define types for core entities (stored in database)
2. Define intermediate types (UI state, computed values)
3. Fetch core entities from database
4. Run through pure functions, jumping type to type, until you have UI to show

React components are the final pure function: convert state type to JSX.

### 8) Ask and You Shall Receive

When a function needs additional context: add it to the input type, see what errors you get, trace up the call stack until you find where the value originates.

> "Rather than proactively trying to map out all cases, I just tell the type system that I need a certain value and let it guide me to where I need to go next."

### 9) If It Compiles, It Works

Inverse relationship: more expressive types → fewer programs that type check → higher probability that type-checking code does what you want.

The author's productivity test: implementing features on airplanes with no wifi. "When I eventually land and run the code, I'm usually good to go after some UI work & maybe 2-3 quick bug fixes."

### 10) Types as an Introspection Tool

Use types to understand your codebase. Want to find everywhere a price is displayed?

```typescript
// Temporarily delete the amount field:
type Price = {
    id: PriceId;
    interval: "month" | "year";
    // amount removed
};
```

Now every reference to `amount` becomes a type error, pointing you to exactly where prices are used.

### 11) Hard Mode and Easy Mode

Type-driven development splits coding into phases:
- **Hard:** Setting up scaffolding, defining types (arcane TypeScript, deep domain thinking)
- **Easy:** Actual implementation (editor guides you, typos caught instantly, autocomplete everywhere)

This gels with creative workflows: channel short bursts of energy into type design, then sustain long coding sessions because the hard thinking is done.

### 12) Know When to Opt Out

It's OK to cheat occasionally with `any` or type assertions when:
- You genuinely know better than the type system
- The scope of the assertion is small
- You're dealing with external dependencies or legacy code

**Example:** PostHog feature flags return `string | boolean | undefined`, but you know your specific flags only return certain variants. A controlled type assertion gives better downstream types.

**"Make illegal states unrepresentable" can also be broken** when the work isn't worth it or you need flexibility for future changes.

> "We're here to use the tool, not let the tool use us."

---

## Key Quotes

On the experience of type-driven coding:
> "Writing code in a codebase that has fully bought into types feels like cheating. I can often implement 80% of a new feature without ever running the code."

On honesty in types:
> "By being lazy the first time, we introduced a subtle lie into our type system that corrupted it, causing it to deviate slightly from being a true representation of the underlying domain."

On the hard/easy split:
> "I'm able to channel short bursts of creative energy into precisely mapping the domain. And then I'm able to sustain long coding sessions because the scaffolding means I rarely have to think too hard."

---

## Connections

- **Relates to "Do The Simplest Thing"** - Type-driven design finds the simplest representation of the domain; the types ARE the simple solution
- **Relates to "Theory Building"** - Type definitions are a form of theory about the domain; they force you to understand before implementing
- **Relates to "Make Illegal States Unrepresentable"** - Core principle shared with Elm community and functional programming broadly
- **Relates to "How I Build Software Quickly"** - "Data modeling is worth spending time on" echoes type-driven design's emphasis
- **Relates to "The Magic of Software"** - Deep understanding of the type system yields vision (new ways to solve problems)
- **Relates to "Parse, Don't Validate"** (Alexis King) - The foundational article this approach builds on
- **Relates to tRPC, Prisma, Drizzle** - Practical tools that enable end-to-end type flow

---

## Recommended Reading

- **"Parse, Don't Validate"** by Alexis King: https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/
- **"Domain Modeling Made Functional"** (F#/DDD book applying similar principles)
- **Scott Wlaschin's talks on "Making Illegal States Unrepresentable"**
