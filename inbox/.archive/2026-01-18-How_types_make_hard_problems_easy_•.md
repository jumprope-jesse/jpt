---
type: link
source: notion
url: https://mayhul.com/posts/type-driven-design/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-12-20T02:16:00.000Z
---

# How types make hard problems easy •

## Content (from Notion)

Over the last couple years, my programming brain has become increasingly warped around types, functional programming principles & Typescript. Most of it is influenced by the inordinate amount of time I’ve spent working on the Heartbeat codebase, a 300k+ line Typescript full-stack application that includes a React web app, a React Native mobile app and a Node.js server. My experience in this codebase has shown me that the more I lean into relying on the type system, the more I benefit.

Writing code in a codebase that has fully bought into types feels like cheating. I can often implement 80% of a new feature without ever running the code. I’ll start working on a large refactor that requires breaking an assumption made throughout the code & quickly discover that the type system makes the change trivial. Simple features practically code themselves because typos are caught instantly and half my code is autocompleted. Nuanced questions from the support team about how a certain feature works can be answered with a quick Ctrl+F in the code even when little written documentation exists. Entire categories of bugs that I used to deal with have vanished.

I’ve come to think of the style of coding that enables this as Type Driven Development. Below is a loose collection of thoughts & links to resources that have heavily influenced what type driven development means to me.

### 1) Let the types flow

Investing in type safety is much more effective when types are able to flow across every surface of our application. In a simple full-stack application, the data flow typically looks like: database -> server -> client. Changing our database schema should cause us to see errors in our frontend code. By achieving this level of type interconnectedness, we can make changes to one side of our codebase and feel confident that the type system will inform us about the implications of that change, even if those implications are happening on a completely different side of the codebase.

Enabling our types to flow through the system usually means:

1. Using the same language everywhere. Naturally, if we want to share type information as much as possible, we need to be using the same language. While not perfect, React Native and Node.Js are powerful for allowing us to use Typescript on mobile & server-side.
1. Making sure that type information is properly preserved across network boundaries. Using a well-typed ORM such as Prisma or Drizzle. Using a typed framework for API calls such as tRPC.
1. Using a monorepo. We want changes in one part of the system to alert us about changes that need to made in other parts of the system, which doesn’t work when those other parts are in a different repo.
1. Using any very rarely. Nothing breaks the flow of types more than any
This can often times be the hard part. Letting the types flow entails doing a lot of work architecting the system in a way that allows for a completely closed loop. At Heartbeat, we’ve gone to extensive lengths to make this flow as robust as possible. And sometimes doing this work can feel pointless because I’m knee-deep in arcane Typescript errors instead of working on a new feature. But for any codebase that’s going to be sticking around for a while, setting up good base-level infrastructure is invaluable.

### 2) Start with the types

Given that types act as a glue that tie the system together, the natural starting place for any new feature is the type definitions. The first thing I do when implementing a new feature is map out what are all the entities involved, what is their relationship, what properties do they have and how should they be represented as a type.

This video is a great example of this concept: https://www.youtube.com/watch?v=2JB1_e5wZmU

Some key takeaways from the video:

a) type definitions are a great way to make sure that my understanding of the domain is aligned with reality. The process of writing these type definitions forces me to map out & wrangle the different components of the project in a comprehensive way. Usually this process results in me discovering gaps or ambiguities in the feature spec that I can then hash with the rest of the team. Often times, these gaps/ambiguities are things that would otherwise go undiscovered until I’m halfway through the project. At which point resolving them might involve throwing away most of the work I’ve already done. Type driven development brings these questions up to the beginning of the process, gets them answered, and serves as a blueprint for the rest of the project.

b) type definitions are human-readable. They’re a great way for someone new (or me in the future) to get a high level understanding of how a feature is structured without having to dive into any actual code tracing.

c) type definitions are both a documentation of the domain model AND real code that is directly used by our implementation. They are a living document that is guaranteed to be an accurate reflection of the codebase.

d) an entity’s conceptual idea is more important than its representation. For example, an email address and a customer id are both represented by strings, but conceptually they are independent things and should not be considered the same type. This distinction should be reflected in our types.

### 3) Make illegal states unrepresentable

Another key takeaway from the video that deserves it’s own section. Making our types reflect the true nature of the data as closely as possible makes it almost impossible to mess up. Some concrete examples of what this can look like in Typescript:

1. We have Product entity. Every product must have at least one price associated with it:
```plain text

type NonEmptyArray<T> = [T, ...T[]];

type Price = //something

interface Product {
	//...
    prices: NonEmptyArray<Price>;
    //...
}

function createProduct(product: Product) {
   //...
}

//If I try to create a product with no prices, I get a type error
createProduct({
	prices: [],
})
```

1. Our users can optionally choose to give us their address:
```plain text
//Bad implemenation
type User = {
	//...
	addressLine1?: string;
	addressLine2?: string;
	city?: string;
	state?: string;
	country?: string;
	//...
};

function createUser(user: User) {
	//...
}

//It's possible for me to create a user & forget to include parts of their address
createUser({
	//...
	addressLine1: "123 Example St",
	//...
});

/*-------------------------------------------*/

//Good implemenation
type User = {
	//...
	address: {
		line1: string;
		line2: string;
		city: string;
		state: string;
		country: string;
	} | null;
	//...
};

//The type system makes sure that we provide everything if we choose to
createUser({
	//...
	address: {
		line1: "123 Example St",
		line2: "Apt 1D",
		city: "Seattle",
		state: "Washington",
		country: "USA",
	},
	//...
});
```

Structuring our types in this way removes a complete category of bugs from ever occurring. Every single state that we make illegal via our type system was a bug waiting to happen in an alternate universe. Additionally, the process of making illegal states unrepresentable is valuable too. Making our types represent the “truth” as closely as possible forces us to ask a lot of questions about what the truth is.

- Are there cases where it makes sense for a product to have no prices?
- How many possible states are there? Are state X and Y actually different, or are they essentially the same thing?
And those questions are vital to understanding the full expanse of the problem we’re trying to solve.

### 4) Parse, don’t validate

Reading this article crystalized so many loose thoughts that I had into a clean slogan: https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/.

The key insight of the article is that types can be interpreted as a vehicle to “store” validation. Having validation work encoded in our types means that:

- the rest of our code is allowed to make assumptions about data without having to constantly validate those assumptions
- the type system enforces that validation happens when needed
- changing these assumptions is much easier. We can change the types to reflect a new assumption & the type system will point us to the implications of this change
(The only reason this section is so short is that the article explains things perfectly. Definitely go read it!)

### 5) Be honest

In many ways, I’ve come to think of programming as finding the truth. The goal is to find the purest, rawest, deepest essence of what an entity represents and express that as a type. And if my goal is truth, then I need to value being honest in my code. This can manifest itself via “make illegal states unrepresentable” — I don’t want to lie and say that something is possible when it isn’t. Or, if I dive down and discover that two things I thought were the same are actually different, I shouldn’t lie and refer to them with the same type. I should do the extra work to split them into different types because that would be a more honest representation of the truth.

To contrast that grandiose description, here’s a mundane example. We have a calendar app where users can create events & see a list of their events:

```plain text

type Event = {
  id: EventId;
  title: string;
  description: string;
  startTime: Date;
  endTime: Date;
  duration: number;
}

function EventList(props: { events: Event[] }) {
  return (
    <div>
      <h1>My Events</h1>
      {props.events.map((ev) => (
        <EventListItem event={ev} />
      ))}
    </div>
  )
}

function EventListItem(props: { event: Event }) {
  return (
    <div>
      <h3>{props.event.name}</h3>
      <p>{props.event.description}</p>
      <p>Start: {props.event.startTime}</p>
      <p>End: {props.event.endTime}</p>
    </div>
  )
}

```

We decide to add a new feature. Users can now create recurring events! Users define a recurring event using a recurrence rule, which specifies when & how often the event repeats. We want our event list to show all instances of upcoming recurring events. To do this we create a getExpandedEvent function which takes in an event. If the event is recurring, the event gets expanded to include all of the instances. Otherwise we return the single event. Once we create this function, all we need to do is call it in our EventList component and then we can continue as usual.

```plain text

type Event = {
  id: EventId;
  title: string;
  description: string;
  startTime: Date;
  endTime: Date;
  duration: number;
  //New field added
  recurrenceRule: string | null;
}

function getRecurringDates(startTime: Date, recurrenceRule: string): Date[] {
  //calculate all the recurring dates according to the recurrence rule
}

function getExpandedEvent(event: Event): Event[] {
  if (event.recurrenceRule !== null) {
    const recurringDates = getRecurringDates(
      event.startTime,
      event.recurrenceRule
    )
    return recurringDates.map((date) => ({
      ...event,
      startTime: date,
    }))
  } else {
    return [event]
  }
}

function EventList(props: { events: Event[] }) {
  const expandedEvents = getExpandedEvent(props.events).flat()

  return (
    <div>
      <h1>My Events</h1>
      {expandedEvents.map((ev) => (
        <EventListItem event={ev} />
      ))}
    </div>
  )
}

```

This works great. Users can see all their recurring events with no issues. A month later, we decide to finally add a button for users to delete their events. So we do something like this:

```plain text

function EventListItem(props: { event: Event }) {
  //If you aren't familiar with tRPC, all you need to know is that deleteEvent.mutateAsync is a function that makes an API request to our server. On the server, we delete the event
  const deleteEvent = trpc.deleteEvent.useMutation()

  return (
    <div>
      <h3>{props.event.name}</h3>
      <p>{props.event.description}</p>
      <p>Start: {props.event.startTime}</p>
      <p>End: {props.event.endTime}</p>
      <button onClick={() => deleteEvent.mutateAsync(props.event.id)}>Delete</button>
    </div>
  )
}


```

Seems pretty straightforward, so we go ahead and ship it. Soon, the customer bug reports come in: “I was trying to delete the May instance of my monthly event, but the whole thing disappeared!?!?!” As you may have noticed, the issue with this implementation is that clicking delete on an instance of a recurring event will delete the entire event. Probably not the behavior that we want. There’s a couple things that went wrong to get here:

- Whoever was speccing the delete event feature should have called out how it should work for non-recurring vs recurring events
- We probably would have realized this was weird if we had more tests or QA before releasing
And while those might be true, I’d argue that one of the underlying reasons we got here was because we weren’t fully honest when we implemented the getExpandedEvent function. At the time, it was convenient to continue using the Event type. All we needed to do is call the function and everything else would remain the same. But if we were honest, we would have recognized that while very similar, events & event instances are different concepts.

An Event is the core object that gets stored in the database. When someone creates a recurring event - say a meeting every Monday for a year - we don’t store 52 different events in the database. Instead, we store a single Event with a recurrence rule. Then, whenever someone needs to see their upcoming events, we use that rule to generate the appropriate EventInstances, each representing one occurrence of the meeting. Events are stored in the database, while event instances are ephemeral. Events can be created, while event instances cannot. Editing an Event (changing the meeting from Mondays at 2pm to Mondays at 3pm) is a completely different action from editing an EventInstance (rescheduling just one specific Monday’s meeting to Tuesday). A more honest representation might look like this:

```plain text
type EventInstance = Omit<Event, "id"> & {
	id: EventInstanceId;
	eventId: EventId;
};

function getEventInstanceId(eventId: EventId, startTime: Date) {
	return `${eventId}-${startTime.toISOString()}` as EventInstanceId;
}

function getEventInstances(event: Event): EventInstance[] {
	if (event.recurrenceRule !== null) {
		const recurringDates = getRecurringDates(event.startTime, event.recurrenceRule);
		return recurringDates.map((date) => ({
			...event,
			startTime: date,
			id: getEventInstanceId(event.id, date),
			eventId: event.id,
		}));
	} else {
		return [
			{
				...event,
				id: getEventInstanceId(event.id, event.startTime),
				eventId: event.id,
			},
		];
	}
}

function EventListItem(props: { eventInstance: EventInstance }) {
	//Render event instance
}
```

The exact implementation of EventInstance would vary depending on what behavior we wanted. But the key point is differentiating event instances from events. If we had done this we never would have ran into the deletion issue because it would be clear that the deleteEvent endpoint is not applicable to event instances. In fact, going back to Start with the types, the EventInstance type in our codebase likely would have made us realize during the feature speccing phase that we needed to handle deleting events and deleting event instances separately.

It’s easy to see why we wouldn’t want to make this change. It’s more work for no immediate payoff. Adding the new type requires changing EventListItem as well. In a larger project, the new type might require even more refactoring across the codebase. But by being lazy the first time, we introduced a subtle lie into our type system that corrupted it, causing it to deviate slightly from being a true representation of the underlying domain. This prevented the types from helping us when we needed them later.

### 6) Be specific

A companion to being honest is being specific. We don’t want to lie by omission. So as much as possible, we want our types to be the narrowest possible expression of the truth.

Branded types are a great example of this. We could use a string to represent the id of a user and it would be an honest representation. But by using a branded UserID type instead, we can be even more specific about what a user id truly represents. And the more specific we are, the more the type checker is able to help us out:

```plain text
type CommunityID = string & { readonly _: "__CommunityID__" };
type UserID = string & { readonly _: "__UserID__" };
type PostID = string & { readonly _: "__PostID__" };

interface Post {
	id: PostID;
	createdBy: UserID;
	communityID: CommunityID;
	//...
}

function getIsUserAdmin(userID: UserID) {
	//...
}

function getShouldShowPost(post: Post) {
	//If we accidentally call this function with the wrong id, we get a type error
	const isAdmin = getIsUserAdmin(post.communityID);

	const isAdmin = getIsUserAdmin(post.createdBy);

	//...
}
```

### 7) Pure functions as a type bridge

Once you start to see everything in your codebase through the lens of types, any action a user takes can be reduced down to a series of type jumps. Define the starting types. Define the ending type. Find a way to go from the starting types to the ending type. What’s the best way to convert one type to another with no distractions? A pure function. That’s quite literally what the mathematical definition of a function is.

Let’s say that we’re implementing a payment page. Our domain looks like this:

```plain text
type Price = {
	id: PriceId;
	amount: number;
	interval: "month" | "year";
};

type Product = {
	id: ProductId;
	name: string;
	prices: NonEmptyArray<Price>;
};

type Subscription = {
	id: SubscriptionId;
	status: "active" | "canceled";
	productId: ProductId;
	priceId: PriceId;
};

type User = {
	id: UserId;
	subscriptions: Subscription[];
};
```

Our payment page has 3 different possibilities:

1. The user has not purchased the product yet, in which they can choose a price point & make the purchase
1. The user is currently subscribed, in which case we show a Cancel Subscription button. When the user clicks on this button: 
1. The user has canceled their subscription, in which case we prompt them to restart their subscription
Representing this as a type, we get:

```plain text
type Discount =
	| {
			type: "PERCENTAGE";
			percentage: number;
	  }
	| {
			type: "FLAT_AMOUNT";
			amount: number;
	  };

type CheckoutPageState =
	| {
			type: "INITIAL_PURCHASE";
			product: Product;
	  }
	| {
			type: "CANCELED";
			subscriptionId: SubscriptionId;
	  }
	| {
			type: "ALREADY_SUBSCRIBED";
			product: Product;
			cancelationDiscount: Discount;
	  };
```

A user visits the payment page for a particular product. We need to render the page. How do we do this? Well, given that we have these types established, the task at hand is clear. We need to convert a Product and a User into a CheckoutPageState. If the user has an active subscription, we need to convert a Subscription to a Discount. So…we write two pure functions to do the conversion & we’re done.

```plain text
//We pass in now as a parameter to make the function fully pure
//This makes testing the function easy
function getDiscount(subscription: Subscription, now: Date): Discount {
	const numMonths = differenceInMonths(now, subscription.createdAt);

	if (numMonths > 12) {
		return {
			type: "PERCENTAGE",
			percentage: Math.min(50, numMonths),
		};
	} else {
		return {
			type: "FLAT_AMOUNT",
			amount: 5,
		};
	}
}

function getCheckoutPageState(product: Product, user: User, now: Date): CheckoutPageState {
	const existingSubscription = user.subscriptions.find((x) => x.productId === product.id);
	if (existingSubscription !== undefined) {
		if (existingSubscription.status === "canceled") {
			return {
				type: "CANCELED",
				subscriptionId: existingSubscription.id,
			};
		} else if (existingSubscription.status === "active") {
			const discount = getDiscount(existingSubscription, now);
			return {
				type: "ALREADY_SUBSCRIBED",
				product: product,
				cancelationDiscount: discount,
			};
		} else {
			assertNever(existingSubscription.status);
		}
	} else {
		return {
			type: "INITIAL_PURCHASE",
			product: product,
		};
	}
}

//***** CheckoutPage.tsx *****\\

function CheckoutPage(props: CheckoutPageState) {
	if (props.type === "INITIAL_PURCHASE") {
		//render initial purchase
	} else if (props.type === "ALREADY_SUBSCRIBED") {
		//render already subscribed
	} else if (props.type === "CANCELED") {
		//render canceled
	} else {
		safeAssertNever(props.type);
		return null;
	}
}
```

Hopefully, you can imagine how this small example could expand to a production application with dozens of types & hundreds of business logic rules encoded in a network of pure functions. The magic of pure functions is that they turn something intimidating into something approachable. We could have the gnarliest, most complicated domain with tons of intersecting edge cases and unintuitive logic. But if we’ve broken it down into the constituent types, then at any given moment all I need to worry about is converting IntermediateType5 to IntermediateType6. I don’t need to think about anything else. That level of clarity & focus does wonders for easing my mental burden while working on large project.

For a full-stack application, the pattern is simple:

1. Define types for my core entities, the ones that get stored in the database (Product, Price, User, Subscription)
1. Define my intermediate types (Discount, CheckoutPageState)
1. Fetch the relevant core entities from the database
1. Run my entities through a series of pure functions, jumping from type to type, until I have a UI to show
Even React, the final piece of the puzzle in this example, is built on functional programming principles. Our CheckoutPage React component is one last pure function that converts the CheckoutPageState type to JSX that gets rendered on the screen.

### 8) Ask and you shall receive

One of the most common changes required by a new feature is something that used to be simple gets just slightly more nuanced. Before the feature, we call a function and it does the thing. But now, that function needs a little bit more context. And based on that context, it does something a little bit different. For example, let’s say we have a generateInvoice function that takes in various values and uses them to generate an Invoice object. The details of the function itself are irrelevant.

```plain text
function generateInvoice(params: {
	customerId: string;
	currency: string;
	items: InvoiceItem[];
	//...
}): Invoice {
	//Generate the invoice
}
```

But now the time has finally come for us to stop ignoring the IRS’ emails and start properly collecting tax from our users. To do so, our invoices will need to look different depending on what the tax rate is.

With types, my approach for a change like this is straightforward. I go to the function that needs the additional context and I edit the input type to include the new context that I need. And then I see what type errors I get. If the function that’s calling generateInvoice doesn’t know what the taxRate should be, then I add taxRate to the input for that function and continue up the call stack. Eventually, I reach a function that is able to either pull the necessary context from a stateful source (a database, endpoint, etc) OR I’m able to calculate the necessary value and pass it in.

So in this case, let’s say I add the taxRate field to params and see the following two errors:

1. One that’s happening on the backend when we call generateInvoice from generateInvoiceForCustomer. To fix it, I call calculateTaxRateForCustomer inside generateInvoiceForCustomer and pass the result of that function into generateInvoice.
1. One that’s happening on the frontend when we call generateInvoice from previewInvoice. In this case, we’re generating a preview invoice for a sample customer, so there’s no tax rate to be calculated. Instead, I just pass in a static value of 0.1 to use as the example tax rate.
This approach saves a lot of time and headache. In a larger application, it’s possible that generateInvoice is being called from 7 different contexts. Rather than proactively trying to map out all of these different cases, I just tell the type system that I need a certain value and let it guide to me where I need to go next.

### 9) If it compiles, it works

Haskell developers have a refrain that if the code compiles, it probably works. While Haskell is on the extreme side of the spectrum, I’ve found this to also be quite true for any system that relies heavily on types. Having types embedded in our codebase means the feedback loop for our code comes directly from the editor & type errors. I don’t need to run the code to see if I messed up, because my editor lets me know as I type.

There’s an inverse relationship between the expressiveness of the types and the number of possible programs that type check successfully. So when our types are honest & specific, it can be hard to write code that type checks without doing what we want it do.

The best example of this is how productive I’ve become on airplanes. Despite being a full-stack application that needs Internet to run locally, I can get on a flight with no wifi, pull out my laptop & implement a new Heartbeat feature with zero distractions — just me and my type checker. When I eventually land and run the code, I’m usually good to go after some UI work & maybe 2-3 quick bug fixes.

### 10) Types as an introspection tool

One of the most underrated aspects of Typescript is how it can be used as a tool to understand your codebase. If I’m trying to understand how a certain feature works, I can play around with the types to help me learn about how parts of that feature interact with the rest of the codebase.

For instance, let’s say I’m working on an update where I want to standardize how we can display prices in the product. Right now the only currency that we support is USD, and all of our prices are displayed like this: $100.00. But we’re getting some confusion from people in Canada about whether we’re referring to USD or CAD, so we want to update the UI to clarify that we mean USD. We show prices on a lot of different components in various contexts, so tracking down everything will be difficult.

What can I do is temporarily delete the amount field from the Price type:

```plain text
type Price = {
	id: PriceId;
	interval: "month" | "year";
};
```

Now, anywhere that I attempt to reference the amount field, I’ll get a type error instead. So if I have 10 different components that display a price in some way, Typescript will point me towards each of those components. I can go to each of them, make the changes I need to and undo the change I made to the type.

Or, let’s say we have a Button component in our design system and we’re considering getting rid of the success variant because it feels unnecessary. To help us make the decision, we want to identify all the screens in our product where we use a success button.

```plain text
interface Props {
	//...
	variant?: "primary" | "secondary" | "success";
	//...
}

function Button(props: Props) {
	//button
}
```

I could do a Ctrl-F for success and try to find examples that way — but predictably it will lead to lots of unrelated results popping up. My approach in these situations is to just delete success as one of the options in Props. By doing this, I’ll immediately get type errors that point me to the exact location of every success button in the product. From there, I can click through the results and evaluate whether the success button is necessary or if it can be replaced with an alternative. The ability to quickly answer questions like “Where does every success button in our product live?” means that I can even use the codebase as a tool in design/product planning meetings.

### 11) Hard mode and easy mode

Using types extensively splits coding into 2 phases. A short period of intense & difficult work followed by a longer period of straightforward work that’s hard to mess up.

The hard part is setting up the scaffolding & defining the types. In Typescript, scaffolding can involve delving into arcane type-level programming or setting up complex frameworks to make sure that types are propagated robustly. As we’ve talked about above, defining types involves deep rumination to figure out what states are valid, how to be honest, where to draw the line between entities, etc. Figuring all of this out can be intimidating and cumbersome.

But, the hard work pays off because coding with types on is astoundingly EASY. The editor is constantly guiding me down the right path. Typos, misused variables, forgotten validation checks are all caught instantly. Autocomplete means I don’t even need to type that much. In the age of AI code completion, type definitions provide a valuable source of documentation to help the AI provide more accurate suggestions. And the type checker makes it harder for invalid AI-suggested code to go unnoticed.

This dichotomy gels really well with the way my brain works. I’m able to channel short bursts of creative energy into precisely mapping the domain or getting type scaffolding set up. And then I’m able to sustain long coding sessions to actually implement the feature because the scaffolding means I rarely have to think too hard.

### 12) Know when to opt out

This one might be controversial for some — but I really like that Typescript allows us to cheat every now and then. Knowing when it’s ok to throw our hands up and use an any is important. If we’re thoughtful, we can maintain 99.9% of the benefits of the type system without wasting days trying to cover the last 0.1%.

Typically using any or type assertions such as as string are a bad idea because they’re a form of lying to the type system. But in situations where we genuinely know better than the type system and the scope of the assertion is small, a small lie is acceptable. A common time where we might know better than the type system is when dealing with external dependencies or legacy code. For example, this is the helper function we use for getting feature flags from Posthog:

```plain text
export const POSTHOG_FLAGS = {
	"longer-free-trial": ["control", "30-days"],
	"checkout-page-design": ["control", "variant-a", "variant-b"],
} as const;

export type PosthogFlag = keyof typeof POSTHOG_FLAGS;

export async function getPosthogFlagVariant<T extends PosthogFlag>(userID: UserID, flagName: T) {
	const variant = await posthog.getFeatureFlag(flagName, userID);
	return variant as (typeof POSTHOG_FLAGS)[T][number] | undefined;
}
```

The default return type for posthog.getFeatureFlag is string | boolean | undefined. But we have more precise knowledge. If we’re getting a value for longer-free-trial then the return type must be either control or 30-days. So we can use the type assertion to assert our knowledge onto Typescript. And by doing so, anyone calling the getPosthogFlagVariant will have much more accurate & specific types. Because POSTHOG_FLAGS is edited in a very controlled context (only when we’re adding or changing a feature flag), we can feel confident that unrelated changes to the codebase are unlikely to cause this lie to backfire.

Make illegal states unrepresentable is another rule that’s helpful to know when to break. There are times when the work it would take to make an illegal state fully unrepresentable is just not worth it. And if I know that changes to what a legal state is are possible in the future, I might not want to cut off all our options too forcefully. Building an intuition for when to leave the door open is difficult and mostly comes from experience. A great example of this is preemptive pluralization.

At the end of the day, it’s important to remember that all of these rules are in place to help us be more productive. We’re here to use the tool, not let the tool use us.

Have thoughts? Want to work with me at Heartbeat? Reach out at mayhul99@gmail.com! I'd love to hear from you.

Want to get emails for new posts?


