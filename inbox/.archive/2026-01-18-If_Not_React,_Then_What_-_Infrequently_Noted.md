---
type: link
source: notion
url: https://infrequently.org/2024/11/if-not-react-then-what/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-12-01T02:12:00.000Z
---

# If Not React, Then What? - Infrequently Noted

## Content (from Notion)

Over the past decade, my work has centred on partnering with teams to build ambitious products for the web across both desktop and mobile. This has provided a ring-side seat to a sweeping variety of teams, products, and technology stacks across more than 100 engagements.

While I'd like to be spending most of this time working through improvements we could make to web APIs, the vast majority of time spent with partners goes to remediating issues caused by "modern" frontend frameworks (React, Angular, etc.) and the culture surrounding them. These issues are most pronounced today in React-based stacks.

This is upsetting because React is legacy technology, but it continues to appear in greenfield applications. Surprisingly, some continue to insist that React is "modern." This correct if we understand "modern" to apply to React the way it applies to art. Neither demonstrate contemporary design or construction techniques. They are not built to meet current needs, but stand as expensive objets that harken back to an earlier era's now-antiquated methods.

- The Rule Of Least Client-Side Complexity
- OK, But What, Then?
- And Nothing Of Value Was Lost
- Vignettes
- "But..."
- References
In the hope of steering the next team away from the rocks, I've found myself penning advocacy pieces and research into the state of play, as well as giving talks to alert managers and developers of the dangers of today's misbegotten frontend orthodoxies.

In short, nobody should start a new project in the 2020s based on React. Full stop.[1]

## The Rule Of Least Client-Side Complexity #

Code that runs on the server can be fully costed. Performance and availability of server-side systems are under the control of the provisioning organisation, and latency can be actively managed by developers and DevOps engineers.

Code that runs on the client, by contrast, is running on The Devil's Computer.[2] Nothing about the experienced latency, client resources, or even available APIs are under the developer's control.

Client-side web development is perhaps best conceived of as influence-oriented programming. Once code has left the datacenter, all a web developer can do is send thoughts and prayers.

As a result, an unreasonably effective strategy is to send less code to clients. In practice, this means favouring HTML and CSS over JavaScript, as they degrade gracefully and feature higher compression ratios. Declarative forms generate more functional UI per byte sent. These improvements in resilience and reductions in costs are beneficial in compounding ways over a site's lifetime.

Stacks based on React, Angular, and other legacy-oriented, desktop-focused JavaScript frameworks generally take the opposite bet. These ecosystems pay lip service the controls that are necessary to prevent horrific profliferations of unnecessary client-side cruft. The predictable consequence are NPM-algamated bundles full of redundancies like core-js, lodash, underscore, polyfills for browsers that no longer exist, userland ECC libraries, moment.js, and a hundred other horrors.

This culture is so out of hand that it seems 2024's React developers are constitutionally unable to build chatbots without including all of these 2010s holdovers, plus at least one extremely chonky MathML or TeX formatting library to display formlas; something needed in vanishingly few sessions.

Tech leads and managers need to break this spell and force ownership of decisions affecting the client. In practice, this means forbidding React in all new work.

## OK, But What, Then? #

This question comes in two flavours that take some work to tease apart:

- The narrow form:"Assuming we have a well-qualified need for client-side rendering, what specific technologies would you recommend instead of React?"
- The broad form:"Our product stack has bet on React and the various mythologies that the cool kids talk about on React-centric podcasts. You're asking us to rethink the whole thing. Which silver bullet should we adopt instead?"
Teams that have grounded their product decisions appropriately can productively work through the narrow form by running truly objective bakeoffs. Building multiple small PoCs to determine each approach's scaling factors and limits can even be a great deal of fun.[3] It's the rewarding side of real engineering, trying out new materials under well-understood constraints to improve user outcomes.

> 

In almost every case, the constraints on tech stack decisions have materially shifted since they were last examined, or the realities of a site's user base are vastly different than product managers and tech leads expect. Gathering data on these factors allows for first-pass cuts about stack choices, winnowing quickly to a smaller set of options to run bakeoffs for.[4]

But the teams we spend the most time with aren't in that position.

Many folks asking "if not React, then what?" think they're asking in the narrow form but are grappling with the broader version. A shocking fraction of (decent, well-meaning) product managers and engineers haven't thought through the whys and wherefores of their architectures, opting instead to go with what's popular in a sort of responsibility fire brigade.[5]

For some, provocations to abandon React create an unmoored feeling, a suspicion that they might not understand the world any more.[6] Teams in this position are working through the epistemology of their values and decisions.[7] How can they know their technology choices are better than the alternatives? Why should they pick one stack over another?

Many need help orienting themselves as to which end of the telescope is better for examining frontend problems. Frameworkism is now the dominant creed of frontend discourse. It insists that all user problems will be solved if teams just framework hard enough. This is non-sequitur, if not entirely backwards. In practice, the only thing that makes web experiences good is caring about the user experience — specifically, the experience of folks at the margins. Technologies come and go, but what always makes the difference is giving a toss about the user.

In less vulgar terms, the struggle is to convince managers and tech leads that they need to start with user needs. Or as Public Digital puts it, "design for user needs, not organisational convenience"

The essential component of this mindset shift is replacing hopes based on promises with constraints based on research and evidence. This aligns with what it means to commit wanton acts of engineering because engineering is the practice of designing solutions to problems for users and society under known constraints.

The opposite of engineering is imagining that constraints do not exist or do not apply to your product. The shorthand for this is "bullshit" (pdf).

Rejecting an engrained practice of bullshitting does not come easily. Frameworkism preaches that the way to improve user experiences is to adopt more (or different) tooling from the framework's ecosystem. This provides adherents with something to do that looks plausibly like engineering, except it isn't. It can even become a totalising commitment; solutions to user problems outside the framework's expanded cinematic universe are unavailable to the frameworkist. Non-idiomatic patterns that unlock significant wins for users are bugs to be squashed. And without data or evidence to counterbalance the bullshit artists's assertions of apostasy, who's to say that's wrong? Orthodoxy unmoored from measurements of user outcomes predictably spins into abstruse absurdities. Heresy, eventually, is perceived to carry heavy sanctions.

It's all nonsense.

Realists do not wallow in abstraction-induced hallucinations about user experiences; they measure them. Realism requires reckoning with the world as it is, not as we wish it to be, and in that way, it's the opposite of frameworkism.

The most effective tools for breaking this spell are techniques that give managers a user-centred view of their system's performance. This can take the form of RUM data, such as Core Web Vitals (check yours now!), or lab results from well-configured test-benches (e.g., WPT). Instrumenting critical user journeys and talking through business goals are quick follow-ups that enable teams to seize the momentum of change and formulate business cases for change.

RUM and bench data sources are essential antidotes to frameworkism because they provide data-driven baselines to argue about. Instead of accepting the next increment of framework investment on faith, teams armed with data can begin to weigh up the actual costs of fad chasing versus their likely returns.

## And Nothing Of Value Was Lost #

Prohibiting the spread of React (and other frameworkist totems) by policy is both an incredible cost-saving tactic and a helpful way to reorient teams towards delivery for users. However, better results only arrive once frameworkism itself is eliminated from decision-making. Avoiding one class of mistake won't pay dividends if we spend the windfall on investments within the same error category.

A general answer to the broad form of the problem has several parts:

- User focus: decision-makers must accept that they are directly accountable for the results of their engineering choices. No buck-passing is allowed. Either the system works well for users, including those at the margins, or it doesn't. Systems that are not performing are to be replaced with versions that do. There are no sacred cows, only problems to be solved with the appropriate application of constraints.
- Evidence: the essential shared commitment between management and engineering is a dedication to realism. Better evidence must win.
- Guardrails: policies must be implemented to ward off hallucinatory frameworkist assertions about how better experiences are delivered. Good examples of this include the UK Government Digital Service's requirement that services be built using progressive enhancement techniques. Organisations can tweak guidance as appropriate (e.g., creating an escalation path for exceptions), but the important thing is to set a baseline. Evidence boiled down into policy has power.
- Bakeoffs: no new system should be deployed without a clear set of critical user journeys. Those journeys embody what we expect users to do most frequently in our systems, and once those definitions are in hand, we can do bakeoffs to test how well various systems deliver, given the constraints of the expected marginal user. This process description puts the product manager's role into stark relief. Instead of suggesting an endless set of experiments to run (often poorly), they must define a product thesis and commit to an understanding of what success means. This will be uncomfortable. It's also the job. Graciously accept the resignations of PMs who decide managing products is not in their wheelhouse.
## Vignettes #

To see how realism and frameworkism differ in practice, it's helpful to work a few examples. As background, recall that our rubric[8] for choosing technologies is based on the number of manipulations of primary data (updates) and session length. Some classes of app feature long sessions and many incremental updates to the primary information of the UI. In these (rarer) cases, a local data model can be helpful in supporting timely application of updates, but this is the exception.

  Sites with short average sessions cannot afford much JS up-front.

It's only in these exceptional instances that SPA architectures should be considered.

And only when an SPA architecture is required should tools designed to support optimistic updates against a local data model — including "frontend frameworks" and "state management" tools — ever become part of a site's architecture.

The choice isn't between JavaScript frameworks, it's whether SPA-oriented tools should be entertained at all.

For most sites, the answer is a clearly "no".

### Informational #

Sites built to inform should almost always be built using semantic HTML with optional progressive enhancement as necessary.

Static site generation tools like Hugo, Astro, 11ty, and Jekyll work well for many of these cases. Sites that have content that changes more frequently should look to "classic" CMSes or tools like WordPress to generate HTML and CSS.

Blogs, marketing sites, company home pages, public information sites, and the like should minimise client-side JavaScript payloads to the greatest extent possible. They should never be built using frameworks that are designed to enable SPA architectures.[9]

### Why Semantic Markup and Optional Progressive Enhancement Are The Right Choice #

Informational sites have short sessions and server-owned application data models; that is, the source of truth for what's displayed on the page is always the server's to manage and own. This means that there is no need for a client-side data model abstraction or client-side component definitions that might be updated from such a data model.

> 

### E-Commerce #

E-commerce sites should be built using server-generated semantic HTML and progressive enhancement.

  A large and stable performance between Amazon and its React-based competitors demonstrates how poorly SPA architectures perform in e-commerce applications. More than 70% of Walmart's traffic is mobile, making their bet on Next.js particularly problematic for the business.

Many tools are available to support this architecture. Teams building e-commerce experiences should prefer stacks that deliver no JavaScript by default, and buttress that with controls on client-side script to prevent regressions in material business metrics.

### Why Progressive Enhancement Is The Right Choice #

The general form of e-commerce sites has been stable for more than 20 years:

- Landing pages with current offers and a search function for finding products
- Search results pages which allow for filtering and comparison of products
- Product-detail pages that host media about products, ratings, reviews, and recommendations for alternatives
- Cart management, checkout, and account management screens
Across all of these page types, a pervasive login and cart status widget will be displayed. This widget, and the site's logo, are sometimes the only consistent page elements across an e-commerce site.

Consistent experience has demonstrated that the commonality of UI elements is low, that sessions have highly variable lengths, and that content freshness is paramount. These factors argue for server-owned data models and application state. The best way to reduce latency in these experiences is to optimise for lightweight individual pages. Aggressive asset caching, image optimisation, and server-side page-weight reduction strategies can all help.

### Media #

Media consumption sites vary considerably in session length and data update potential. Most should start as progressively-enhanced markup-based experiences, adding complexity over time as product changes warrant it.

### Why Progressive Enhancement and Islands May Be The Right Choice #

Many interactive elements on media consumption sites can be modeled as distinct islands of interactivity (e.g., comment threads). Many of these components present independent data models and can therefore be modeled as Web Components within a larger (static) page.

### When An SPA May Be Appropriate #

This model breaks down when media playback must continue across media browsing (think "mini-player" UIs). A fundamental limitation of today's web platform is that it is not possible to preserve some elements from a page across top-level navigations. Sites that must support features like this should consider using SPA technologies while setting strict guardrails for the allowed size of client-side JS per page.

Another reason to consider client-side logic for a media consumption app is offline playback. Managing a local (Service Worker-backed) media cache requires application logic and a way to synchronise information with the server.

Lightweight SPA-oriented frameworks may be appropriate here, along with connection-state resilient data systems such as Zero or Y.js.

### Social #

Social media apps feature significant variety in session lengths and media capabilities. Many present infinite-scroll interfaces and complex post editing affordances. These are natural dividing lines in a design that align well with session depth and client-vs-server data model locality.

### Why Progressive Enhancement May Be The Right Choice #

Most social media experiences involve a small, fixed number of actions on top of a server-owned data model ("liking" posts, etc.) as well as distinct update phase for new media arriving at an interval. This model works well with a hybrid approach as is found in Hotwire and many HTMX applications.

### When An SPA May Be Appropriate #

Islands of deep interactivity may make sense in social media applications, and aggressive client-side caching (e.g., for draft posts) may aid in building engagement. It may be helpful to think of these as unique app sections with distinct needs from the main site's role in displaying content.

Offline support may be another reason to download a data model and a snapshot of user state to the client. This should be done in conjunction with an approach that builds resilience for the main application. Teams in this situation should consider a Service Worker-based, multi-page app with "stream stitching" architecture which primarily delivers HTML to the page but enables offline-first logic and synchronisation. Because offline support is so invasive to an architecture, this requirement must be identified up-front.

> 

### Productivity #

Document-centric productivity apps may be the hardest class to reason about, as collaborative editing, offline support, and lightweight (and fast) "viewing" modes with full document fidelity are all general product requirements.

Triage-oriented data stores (e.g. email clients) are also prime candidates for the potential benefits of SPA-based technology. But as with all SPAs, the ability to deliver a better experience hinges both on session depth and up-front payload cost. It's easy to lose this race, as this blog has examined in the past.

Editors of all sorts are a natural fit for local data models and SPA-based architectures to support modifications to them. However, the endemic complexity of these systems ensures that performance will remain a constant struggle. As a result, teams building applications in this style should consider strong performance guardrails, identify critical user journeys up-front, and ensure that instrumentation is in place to ward off unpleasant performance surprises.

### Why SPAs May Be The Right Choice #

Editors frequently feature many updates to the same data (e.g., for every keystroke or mouse drag). Applying updates optimistically and only informing the server asynchronously of edits can deliver a superior experience across long editing sessions.

However, teams should be aware that editors may also perform double duty as viewers and that the weight of up-front bundles may not be reasonable for both cases. Worse, it can be hard to tease viewing sessions apart from heavy editing sessions at page load time.

Teams that succeed in these conditions build extreme discipline about the modularity, phasing, and order of delayed package loading based on user needs (e.g., only loading editor components users need when they require them). Teams that get stuck tend to fail to apply controls over which team members can approve changes to critical-path payloads.

### Other Application Classes #

Some types of apps are intrinsically interactive, focus on access to local device hardware, or center on manipulating media types that HTML doesn't handle intrinsically. Examples include 3D CAD systems, programming editors, game streaming services), web-based games, media-editing, and music-making systems. These constraints often make complex, client-side JavaScript-based UIs a natural fit, but each should be evaluated in a similarly critical style as when building productivity applications:

- What are the critical user journeys
- How deep will average sessions be?
- What metrics will we track to ensure that performance remains acceptable?
- How will we place tight controls on critical-path script and other resources?
Success in these app classes is possible on the web, but extreme care is required.

> 

## "But..." #

Managers and tech leads that have become wedded to frameworkism often have to work through a series of easily falsified rationales offered by other Over Reactors in service of their chosen ideology. Note, as you read, that none of these protests put the lived user experience front-and-centre. This admission by omission is a reliable property of the sorts of conversations that these sketches are drawn from.

### "...we need to move fast" #

This chestnut should always be answered with a question: "for how long?"

This is because the dominant outcome of fling-stuff-together-with-NPM, feels-fine-on-my-$3K-laptop development is to cause teams to get stuck in the mud much sooner than anyone expects. From major accessibility defects to brand-risk levels of lousy performance, the consequence of this sort of thinking crosses my desk every week (and has for a decade now), and the one thing I can tell you that all of these teams and products have in common is that they are not moving faster. The inevitably necessary, painful, and expensive remediations come with little support (owing to the JS-industrial-complex's omerta) and a sinking realisation that choices which were made in haste are not so easily revised. Complex, inscrutable tools introduced in the "move fast" phase are now systems that teams must dedicate time to learn, understand deeply, and affrimatively operate. All the while the pace of feature delivery is dramatically reduced.

This isn't what managers think they're signing up for when acccepting "but we need to move fast!"

But let's take the assertion at face value and assume a team that won't get stuck in the ditch (🤞): the idea embedded in this statemet is, roughly, that there isn't time to do it right (so React?), but there will be time to do it over. But this is in direct contravention with the idea of identifying product-market-fit.

Contra the received wisdom of valley-dwellers, the way to find who will want your product is to make it as widely available as possible, then to add UX flourishes.

Teams I've worked with are frequently astonished to find that removing barriers to use opens up new markets, or improves margins and outcomes in parts of a market they had under-valued.

Now, if you're selling Veblen goods, by all means, prioritise anything but accessibility for folks on the margins. But in literally every other category, the returns to quality can be best understood as clarity of product thesis. A low-quality experience — which is what is being proposed when React is offered as an expedient — is a drag on the core growth argument for your service. And if the goal is scale, rather than exclusivity, building for legacy desktop browsers that Microsoft won't even sell you is a strategic error.

### "...it works for Facebook" #

To a statistical certainty, you aren't making Facebook. Your problems likely look nothing like Facebook's early 2010s problems, and even if they did, following their lead is a terrible idea.

And these tools aren't even working for Facebook. They just happen to be a monopoly in various social categories and so can afford to light money on fire. If that doesn't describe your situation, it's best not to overindex on narratives premised on Facebook's perceived success.

### "...our teams already know React" #

React developers are web developers. They have to operate in a world of CSS, HTML, JavaScript, and DOM. It's inescapable. This means that React is the most fungible layer in the stack. Moving between templating systems (which is what JSX is) is what web developers have done fluidly for more than 30 years. Even folks with deep expertise in, say, Rails and ERB, can easily knock out Django or Laravel or Wordpress or 11ty sites. There are differences, sure, but every web developer is a polyglot.

React knowledge is also not particularly valuable. Any team familiar with React's...baroque...conventions can easily master Preact, Stencil, Svelte, Lit, FAST, Qwik, or any of a dozen faster, smaller, reactive client-side systems that demand less mental bookkeeping.

### "...we need to be able to hire easily" #

The tech industry has just seen many of the most talented, empathetic, and user-focused engineers I know laid off for no reason other than their management couldn't figure out that there would be some mean reversion post-pandemic. Which is to say, there's a fire sale on talent right now, and you can ask for whatever skills you damn well please and get good returns.

If you cannot attract folks who know web standards and fundamentals, reach out. I'll personally help you formulate recs, recruiting materials, hiring rubrics, and promotion guides to value these folks the way you should: as underpriced heroes that will do incredible good for your products at a fraction of the cost of solving the next problem the React community is finally acknowledging that frameworkism itself caused.

### Resumes Aren't Murder/Suicide Pacts #

Even if you decide you want to run interview loops to filter for React knowledge, that's not a good reason to use it! Anyone who can master the dark thicket of build tools, typescript foibles, and the million little ways that JSX's fork of HTML and JavaScript syntax trips folks up is absolutely good enough to work in a different system.

Heck, they're already working in an ever-shifting maze of faddish churn. The treadmill is real, which means that the question isn't "will these folks be able to hit the ground running?" (answer: no, they'll spend weeks learning your specific setup regardless), it's "what technologies will provide the highest ROI over the life of our team?"

Given the extremely high costs of React and other frameworkist prescriptions, the odds that this calculus will favour the current flavour of the week over the lifetime of even a single project are vanishingly small.

### The Bootcamp Thing #

It makes me nauseous to hear managers denigrate talented engineers, and there seems to be a rash of it going around. The idea that folks who come out of bootcamps — folks who just paid to learn whatever was on the syllabus — aren't able or willing to pick up some alternative stack is bollocks.

Bootcamp grads might be junior, and they are generally steeped in varying strengths of frameworkism, but they're not stupid. They want to do a good job, and it's management's job to define what that is. Many new grads might know React, but they'll learn a dozen other tools along the way, and React is by far the most (unnecessarily) complex of the bunch. The idea that folks who have mastered the horrors of useMemo and friends can't take on board DOM lifecycle methods or the event loop or modern CSS is insulting. It's unfairly stigmatising and limits the organisation's potential.

In other words, definitionally atrocious management.

### "...everyone has fast phones now" #

For more than a decade, the core premise of frameworkism has been that client-side resources are cheap (or are getting increasingly inexpensive) and that it is, therefore, reasonable to trade some end-user performance for developer convenience.

This has been an absolute debacle. Since at least 2012 onward, the rise of mobile falsified this contention, and (as this blog has meticulously catalogued) we are only just starting to turn the corner.

Frameworkist assertions that "everyone has fast phones" is many things, but first and foremost it's an admission that the folks offering this out don't know what they're talking about, and they hope you don't either.

No business trying to make it on the web can afford what these folks are selling, and you are under no obligation to offer your product as sacrifice to a false god.

### "...React is industry-standard" #

This is, at best, a comforting fiction.

At worst, it's a knowing falsity that serves to omit the variability in React-based stacks because, you see, React isn't one thing. It's more of a lifestyle, complete with choices to make about React itself (function components or class components?) languages and compilers (typescript or nah?), package managers and dependency tools (npm? yarn? pnpm? turbo?), bundlers (webpack? esbuild? swc? rollup?), meta-tools (vite? turbopack? nx?), "state management" tools (redux? mobx? apollo? something that actually manages state?) and so on and so forth. And that's before we discuss plugins to support different CSS transpilation or the totally optional side-quests that frameworkists have led many of the teams I've consulted with down; "CSS-in-JS" being one particularly risible example.

Across more than 100 consulting engagements, I've never seen two identical React setups save smaller cases where developers have yet to add to the defaults of Create React App (which itself changed dramatically over the years before it finally being removed from the React docs as the best way to get started).

There's nothing standard about any of this. It's all change, all the time, and anyone who tells you differently is not to be trusted.

### The Bare (Assertion) Minimum #

Hopefully, you'll forgive a digression into how the "React is industry standard" misdirection became so embedded.

Given the overwhelming evidence that this stuff isn't even working on the sites of the titular React poster children, how did we end up with React in so many nooks and crannies of contemporary frontend?

Pushy know-it-alls, that's how. Frameworkists have a way of hijacking every conversation with bare assertions like "virtual DOM means it's fast" without ever understanding anything about how browsers work, let alone the GC costs of their (extremely chatty) alternatives. This same ignorance allows them to confidently assert that React is "fine" when cheaper alternatives exist in every dimension.

These are not serious people. You do not have to take them seriously. But you do have to oppose them and create data-driven structures that put users first. The long-term costs of these errors are enormous, as witnessed by the parade of teams needing our help to achieve minimally decent performance using stacks that were supposed to be "performant" (sic).

### "...the ecosystem..." #

Which part, exactly? Be extremely specific. Which packages are so valuable, yet wedded entirely to React, that a team should not entertain alternatives? Do they really not work with Preact? How much money exactly is the right amount to burn to use these libraries? Because that's the debate.

Even if you get the benefits of "the ecosystem" at Time 0, why do you think that will continue to pay out?

Every library is presents stochastic risk of abandoment. Even the most heavily used systems fall out of favour with the JS-industrial-complex's in-crowd, stranding you in the same position as you'd have been in if you accepted ownership of more of your stack up-front, but with less experience and agency. Is that a good trade? Does your boss agree?

And if you don't mind me asking, how's that "CSS-in-JS" adventure working out? Still writing class components, or did you have a big forced (and partial) migration that's still creating headaches?

The truth is that every single package that is part of a repo's devDependencies is, or will be, fully owned by the consumer of the package. The only bulwark against uncomfortable surprises, then, is to consider NPM dependencies like a sort of high-interest debt collateralized by future engineering capacity.

The best way to minimize costs, then, is to fully examine and approve the entire chain of dependencies that are constitute your UI and all of the build systems that participate in app construction. If your team is not comfortable agreeing to own, patch, and improve every single one of those systems, they should not be part of your stack.

### "...Next.js can be fast (enough)" #

Do you feel lucky, punk? Do you?

Because you'll have to be lucky to beat the odds.

Sites built with Next.js perform materially worse than those from HTML-first systems like 11ty, Astro, et al.

It simply does not scale, and the fact that it drags React behind it like a ball and chain is a double demerit. The chonktastic default payload of delay-loaded JS in any Next.js site will compete with ads and other business-critical deferred content for bandwidth, and that's before any custom components or routes are added. Which is to say, Next.js is a fast way to lose a lot of money while getting locked in to a VC-backed startup's proprietary APIs.

Next.js starts bad and only gets worse from a shocking baseline. No wonder the only Next sites that seem to perform well are those that enjoy overwhelmingly wealthy userbases, hand-tuning assistance from Vercel, or both.

So, do you feel lucky?

### "...React Native!" #

React Native is a good way to make a slow app that requires constant hand-tuning and an excellent way to make a terrible website. It has also been abandoned by it's poster children.

Companies that want to deliver compelling mobile experiences into app stores from the same codebase as their web site are better served investigating Cordova, Trusted Web Activities, and PWABUilder. This approach leaves most native capabilities available, but centralises UI investment in the web side of the stack, providing visibility and control via a single execution. This, in turn, reduces duplicate optimisation and accessibility headaches.

## References #

These are essential guides for frontend realism. I recommend interested tech leads, engineering managers, and product managers digest them all:

- "Building a robust frontend using progressive enhancement" from the UK's Government Digital Service. "JavaScript dos and donts" by Github alumnus Mu-An Chiou.
- "Choosing Your Stack" from Cancer Research UK
- "The Monty Hall Rewrite" by Alex Sexton, which breaks down the essential ways that a failure to run an honest bakeoff harms decision-making.
- "Things you forgot (or never knew) because of React" by Josh Collinsworth, which enunciates just how baroque and parochial React's culture has become.
- "The Frontend Treadmill" by Marco Rogers explains the costs of frameworkism better than I ever could.
- "Questions for a new technology" by Kellan Elliott-McCrea and Glyph's "Against Innovation Tokens". Together, they set a well-focused lens for thinking about how frameworkism is antithetical to functional engineering culture.
These pieces are from teams and leaders that have succeeded in outrageously effective ways by applying the realist tentants of looking around for themselves and measuring things. I wish you the same success.

Thanks to Mu-An Chiou, Hasan Ali, Josh Collinsworth, Ben Delarre, Katie Sylor-Miller, and Mary for their feedback on drafts of this post.


