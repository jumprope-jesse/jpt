# Engineering Leadership Principles

## Source
- [Test Article: Engineering Leadership Principles](https://example.com/engineering-leadership)
- Added: 2025-01-18

## Key Principles

### Communicate the "Why"
Always communicate the "why" behind decisions. Context and rationale help teams understand and buy into choices.

### Trust and Verify
Trust your team but verify outcomes. Balance autonomy with accountability.

### Technical Debt as Business Decision
Technical debt is a business decision, not just a tech one. Frame tech debt discussions in terms of business impact, velocity, and risk.

## Communicating with Executives (Translation Layer)

*Source: [The Engineer → Executive Translation Layer](https://refactoring.fm/p/the-engineer-executive-translation) by Anna Shipman (CTO at Kooth) via Refactoring.fm - Added: 2026-01-18*

### How Executives Think

1. **Your boss has a boss** - CEOs answer to boards, shareholders, customers, and sometimes regulators. Understand the drivers for your company.

2. **Execs are short on time** - Not busier than you, but their span of responsibility is wider, so proportionally less time per topic. Make your time with them count.

3. **Execs optimize for company-wide impact** - They weigh how proposals affect customers, other teams, and financials across the company, not just engineering.

4. **Execs will have questions** - Anticipate and answer these upfront:
   - How much will it cost?
   - What will I get for the money?
   - What other options have you considered?
   - Why now, and what happens if we don't do it?
   - How will success be measured, and on what timeline?
   - What are the key risks, and how do we mitigate them?
   - Who owns delivery, and how confident are we in execution?
   - How might this affect other areas of the business?

### The Translation Layer

- **Speak business, not engineering** - Terms like API, CI/CD, latency, blue-green deployment don't translate. Use language tied to business outcomes.
- **Time horizons differ** - Engineering goals are days/weeks/months. Exec goals (EBITDA, CAC, brand reputation) are years. Map your work up to those longer horizons.
- **Engineering is expensive** - Often one of the largest company investments. Execs will scrutinize tech investments closely.
- **Make proposals about the business** - Not about improving engineering for its own purposes.

### Useful Question to Ask Execs

> "What would you say are the two or three forces or stakeholders that most shape our company's direction right now?"

Shows strategic curiosity and provides useful context for future proposals.

## 21 Lessons from 14 Years at Google (Addy Osmani)

*Source: [AddyOsmani.com - 21 Lessons](https://addyosmani.com/blog/21-lessons/) - Added: 2026-01-18*

Hard-won wisdom from a senior Google engineer. The engineers who thrive aren't necessarily the best programmers—they're the ones who've figured out how to navigate everything around the code: people, politics, alignment, ambiguity.

### On User Focus

1. **Solve user problems, not technology problems** - Work backwards from user problems, let solutions emerge. The engineer who truly understands the problem often finds the elegant solution is simpler than expected.

### On Collaboration & Alignment

2. **Being right is cheap; getting to right together is the real work** - You can win every technical argument and lose the project. The skill isn't being right—it's entering discussions to align on the problem, creating space for others, and remaining skeptical of your own certainty.

3. **If you win every debate, you're accumulating silent resistance** - People stop fighting you not because you're convinced them, but because they've given up trying. Real alignment takes longer but builds willing collaborators.

14. **Admitting what you don't know creates more safety than pretending you do** - When a leader admits uncertainty, it signals the room is safe for others to do the same. Model curiosity, and you get a team that actually learns.

### On Execution

3. **Bias towards action. Ship.** - "You can edit a bad page, but you can't edit a blank one." First do it, then do it right, then do it better. Momentum creates clarity; analysis paralysis creates nothing.

4. **Clarity is seniority. Cleverness is overhead.** - Your code is a strategy memo to strangers who will maintain it at 2am during an outage. Optimize for their comprehension, not your elegance.

5. **Novelty is a loan you repay in outages, hiring, and cognitive overhead** - Innovate only where you're uniquely paid to innovate. Everything else should default to boring, because boring has known failure modes.

### On Career & Influence

6. **Your code doesn't advocate for you. People do.** - Decisions get made in meetings you're not invited to, using summaries you didn't write, by people who have five minutes and twelve priorities. If no one can articulate your impact when you're not in the room, your impact is effectively optional.

17. **Your network outlasts every job you'll ever have** - Colleagues who invested in relationships reaped benefits for decades. Your job isn't forever, but your network is.

### On Technical Decisions

7. **The best code is the code you never had to write** - Before you build, exhaust the question: "What would happen if we just… didn't?"

8. **At scale, even your bugs have users** - With enough users, every observable behavior becomes a dependency. Compatibility is product. Design your deprecations as migrations with time, tooling, and empathy.

18. **Most performance wins come from removing work, not adding cleverness** - The fastest code is code that never runs. Before you optimize, question whether the work should exist at all.

### On Teams & Process

9. **Most "slow" teams are actually misaligned teams** - Most slowness is alignment failure—people building the wrong things, or the right things in incompatible ways. Senior engineers spend more time clarifying direction than "writing code faster."

15. **When a measure becomes a target, it stops measuring** (Goodhart's Law) - Every metric you expose to management will eventually be gamed. Respond to every metric request with a pair: one for speed, one for quality or risk.

19. **Process exists to reduce uncertainty, not to create paper trails** - If you can't explain how a process reduces risk or increases clarity, it's probably just overhead.

### On Knowledge & Growth

11. **Abstractions don't remove complexity. They move it to the day you're on call.** - Keep learning "lower level" things even as stacks get higher. Respect the moment when the abstraction fails.

12. **Writing forces clarity. The fastest way to learn something better is to try teaching it.** - The places where you stumble when explaining are the places where your understanding is shallow. Teaching is debugging your own mental models.

13. **The work that makes other work possible is priceless—and invisible** - Glue work (documentation, onboarding, coordination) is vital but can stall your technical trajectory. Timebox it. Rotate it. Turn it into artifacts. Make it legible as impact.

### On Career Sustainability

10. **Focus on what you can control. Ignore what you can't.** - Energy spent on what you can't change is energy stolen from what you can.

20. **Eventually, time becomes worth more than money. Act accordingly.** - Know what you're trading, and make the trade deliberately.

21. **There are no shortcuts, but there is compounding** - Learning compounds when it creates new options, not just new trivia. Build reusable primitives. Collect scar tissue into playbooks.

### The Takeaway

> "A career in engineering is long enough to make plenty of mistakes and still come out ahead. The engineers I admire most aren't the ones who got everything right—they're the ones who learned from what went wrong, shared what they discovered, and kept showing up."

## Kernighan's Lever: Debugging as Growth

*Source: [Kernighan's lever](https://linusakesson.net/programming/kernighans-lever/index.php) by Linus Akesson - Added: 2026-01-18*

### The Original Quote

Brian Kernighan wrote in *The Elements of Programming Style*:

> "Everyone knows that debugging is twice as hard as writing a program in the first place. So if you're as clever as you can be when you write it, how will you ever debug it?"

### The Reframe

The common interpretation treats this as a warning against clever code. But Akesson offers a more interesting reading: cleverness is not static.

The answer to "how will you ever debug it?" is straightforward: **By tackling the problem, thereby gaining valuable experience and becoming more clever in the process.**

### The Mechanism

**Kernighan's lever**: By putting in a small amount of motivation towards a short-term goal (implementing functionality), you end up with a much larger amount of motivation towards long-term growth (becoming a better programmer).

When you work at your current skill level:
1. Writing code puts you in the "flow" zone
2. Debugging that same code pushes you into the "frustration" zone
3. Pride, stubbornness, and curiosity drive you to solve it
4. Solving it increases your skill level
5. Your new skill level becomes the baseline for the next challenge

### The Flow Connection

Using Csikszentmihalyi's flow concept:
- **Implement below your ability** → Debug in "flow" (comfortable but no growth)
- **Implement at your ability** → Debug in "frustration" (uncomfortable but growth)

Deliberately staying away from clever techniques to avoid hard debugging means dodging the lever and missing the improvement.

### The Counterpoint

One commenter argues programming and debugging are subtly different skills—not inherently easier/harder:
> "Debugging is in part a process of learning how complex your design intent really is, when translated into a language of a complex machine. They are not really separate things, programming and debugging."

### Key Insight

The moment you realize "Oh, look at how stupid I was!" is proof that your skill has increased. The more accurate sentiment: "Oh, look at how clever I've become!"

### Connection to AI-Assisted Development

In the AI era, this raises an interesting question: if AI handles the debugging, do we lose the lever? Or does the challenge simply shift—from debugging code to understanding and directing AI output?

The parallel to parenting (from the Notion notes): both require patience, problem-solving, and the realization that mistakes lead to growth.

## Competition, Rivalry, and Eventual Collaboration

*Source: [Watson and Wilson: An Intellectual Entente](https://www.harvardmagazine.com/2009/09/james-watson-edward-o-wilson-intellectual-entente) - Harvard Magazine, 2009 - Added: 2026-01-18*

James Watson (DNA co-discoverer) and E.O. Wilson (sociobiologist) were bitter rivals at Harvard in the 1950s-60s. Watson dismissed Wilson's field as "stamp collecting" and said "anyone who would hire an ecologist is out of his mind." Wilson called Watson "the most mean-spirited academic" he knew.

### On the Value of Enemies

Watson believed: "To be good, you have to have an enemy... It works with boys, anyway."

Wilson: "I have been blessed with brilliant enemies... Ambition and competitiveness are essential to do really good work."

### On Reconciliation

Watson attributed their eventual friendship to: "I hated Ed's enemies." Shared opposition can create unexpected alliances.

### On Field Unification

Over time, molecular biologists and "stamp collectors" adopted each other's methods. Wilson noted: "The glory of late twentieth-century biology is that it is unifying." This parallels how initially opposing technical approaches (waterfall vs agile, monoliths vs microservices) often converge into hybrid best practices.

### Wilson's Warning (Notable Quote)

> "The real problem of humanity is the following: we have paleolithic emotions; medieval institutions; and god-like technology. And it is terrifically dangerous, and it is now approaching a point of crisis overall."

This applies directly to building technology products: our tools outpace our wisdom in using them. Technical capability needs ethical and institutional maturity to match.

## Stewardship Over Spotlight (Lalit Maganti)

*Source: [Why I Ignore The Spotlight as a Staff Engineer](https://lalitm.com/software-engineering-outside-the-spotlight/) by Lalit Maganti (Senior Staff Engineer at Google, Perfetto team) - Added: 2026-01-18*

A counter-narrative to advice about chasing visibility and executive attention. For infrastructure/developer tools engineers, depth and stewardship often matter more than spotlight.

### Two Different Worlds

**Product teams** (Sean Goedecke's context): Business goals pivot quarterly, success measured by revenue/MAU. Optimizing for "Spotlight" makes sense—crowded room of VPs, PMs, designers with strong opinions. Must be agile and work on what executives are currently looking at.

**Infrastructure/DevEx teams** (Maganti's context): Customers are internal engineers. Never the "hot project." Operate bottom-up: figure out what has most impact, then build it. Execs verify impact through downstream product teams.

### Compounding Returns of Stewardship

**Context is the currency** in infrastructure (vs. speed in product):

1. **Efficiency via pattern matching** - Years in one domain means new requests are rarely truly "new." Can reach back: "We tried this in 2021 with Team X; here's why it failed, here's what works."

2. **Systemic innovation** - Some problems only reveal their shape over long horizons. Bigtrace example: observed pattern (2023) → researched quietly (most of 2023) → built and launched (late 2023-2024). Only possible because he stayed long enough to see the whole picture.

### The Power of "No"

High-visibility projects are volatile: shifting exec whims, political maneuvering, quality sacrificed for survival.

Stewardship generates **trust as capital** - the political standing to say "no" to spotlight when it threatens the product.

Example: AI pressure to add LLMs to Perfetto. Easy career win to build an LLM wrapper. But Perfetto's core value is precision—kernel developers debugging race conditions need exact timestamps, not hallucinations. "Not no forever, but not until it can be done right."

### Alternate Currencies of Impact

**Shadow Hierarchy**: Don't need your VP to understand your code. Need Staff+ engineers in other orgs to need your tools. When a Senior Staff in Pixel tells their VP "We cannot debug the next Pixel without Perfetto"—that travels up their chain, crosses at Director/VP level, and comes back down to you.

This advocacy is technical, not political. Hard to fake.

**Utility Ledger** metrics:
- **Utility**: Bugs fixed using your tools = engineers finding you useful
- **Criticality**: VIP teams depend on you for launch-blocking issues
- **Ubiquity**: Significant engineering population using your tools as "lingua franca"
- **Scale**: Petabytes processed = architectural resilience proven

Criticality + Utility = promotion case immune to reorgs.

### Staff Engineer Archetypes (Will Larson)

From *Staff Engineer* book:
- **Solver / Right Hand**: Agents of executive will, drop into fires, move on
- **Architect / Tech Lead**: Long-term domain ownership, deep technical context

Spotlight-seeking aligns with Solver/Right Hand. Stewardship aligns with Architect/Tech Lead.

### Caveats

1. Requires company profitable enough to sustain long-term infrastructure (Big Tech, not startups)
2. Finding a good team involves luck, but staying is a choice
3. Teams like this seem rare because they're ignored—no rapid visible wins, no shiny features, less competition

### The Trade-off

If motivated by "shipping to billions of users" or seeing friends/family use what you built—won't find that here. That's the price of admission.

But if you want to build long-term systems and trade external validation for deep technical ownership, look behind the curtain.

### Key Quote

> "You don't have to chase the spotlight to have a meaningful, high-impact career at a big company. Sometimes, the most ambitious thing you can do is stay put, dig in, and build something that lasts."

## Transparent Leadership Over Servant Leadership

*Source: [Transparent Leadership Beats Servant Leadership](https://entropicthoughts.com/transparent-leadership-beats-servant-leadership) - Added: 2026-01-18*

A critique of servant leadership as "curling parenting"—leaders who anticipate problems and sweep the way for their reports. The result: an overworked single point of failure who leaves behind people isolated from the organization with no idea how to handle obstacles themselves.

### The Problem with Servant Leadership

- Leader becomes overworked SPOF
- Reports never learn to handle obstacles
- When leader leaves, team is isolated and lost
- Feels good initially but creates dependency

### Transparent Leadership Principles

A good leader:
1. **Coaches people** - develops their skills, not does the work for them
2. **Connects people** - creates direct links between supply and demand (not making yourself a middleman)
3. **Teaches methodical problem solving** - "teach a man to fish"
4. **Explains values and principles** - so people can make aligned decisions independently
5. **Allows career growth** - direct reports gradually take over leadership responsibilities
6. **Continuously trains their replacement** - always working toward redundancy
7. **Generally makes themselves redundant**

### What to Do When Redundant

The "middle manager that doesn't perform any useful work" is a fun stereotype—but also a good target to aim for. The difference is what you do once redundant:

**Bad response**: Invent new work, ask for status reports, add bureaucracy.

**Good response**: Go back to working on technical problems. This:
- Keeps your skills fresh
- Earns more respect from reports
- Makes you a "high-powered spare worker" rather than a paper-shuffler

### Connection to Parenting

The author draws a direct parallel: curling parents anticipate problems and sweep them away, leaving children unprepared. Transparent parenting teaches children to navigate life's challenges independently—the same skill transfer should happen in leadership.

### Key Insight

> "The middle manager that doesn't perform any useful work is a fun stereotype, but I also think it's a good target to aim for."

The goal is to become redundant through teaching and enabling—then return to valuable technical contribution rather than inventing bureaucracy.

## Trillion-Dollar IT Failures: The Pattern That Won't Die

*Source: [Software Failures and IT Management's Repeated Mistakes](https://spectrum.ieee.org/it-management-software-failures) - IEEE Spectrum, November 2025 - Added: 2026-01-18*

*Full analysis: [[software-project-failures]]*

Despite IT spending tripling since 2005 ($1.7T to $5.6T), software success rates have not improved. The US loses $1.81 trillion annually to operational software failures.

### The Core Problem

Most failures are not unique—they repeat the same documented mistakes. Project managers claim "our project is different" and ignore lessons from prior failures. That is "the excuse of the arrogant."

### Essential Questions Before Any Large Project

1. What do you know, what should you know, and how big is the gap?
2. If no one has successfully built this with your schedule/budget/functionality, why do you think you can?

### Why AI Won't Fix Management

> "IT projects suffer from enough management hallucinations and delusions without AI adding to them."

AI cannot manage: organizational politics, project/financial trade-offs, or rational decision-making (rare in IT projects anyway).

### The Honesty Requirement

> "It is a common 'secret' that it is far easier to get funding to fix a troubled software development effort than to ask for what is required up front to address the risks involved."

Honesty begins with forthright risk accounting, not rationalization. Vendor puffery is legal, so customers need healthy skepticism.

### The Quote to Remember

> "Anyone can make a mistake, but only an idiot persists in his error." —Cicero

## Product Bets: Accountability Through Estimated Value

*Source: [The Accountability Problem](https://www.jamesshore.com/v2/blog/2025/the-accountability-problem) by James Shore (VP Engineering at OpenSesame, 23 years consulting) - Keynote at Cambridge conference, 2025 - Added: 2026-01-18*

A framework for engineering accountability that shifts from "deliver feature X by date Y" to "deliver estimated value through product bets."

### The Business Misconception

Non-technical colleagues interpret software through the lens of their experience—like homework assignments with clear paths from A to B. This leads to assumptions that:
- You just need to define the assignment correctly
- There's one right answer with a clear path
- People can tell you how long the path takes
- When behind, pressure will speed things up

Reality: Software development is discovery and exploration, not a straight line.

### Why Features-and-Dates Accountability Fails

Other departments are accountable for *results*, not specific activities:
- Sales: "We'll generate $10M revenue" (not "we'll close Account X on Date Y")
- Marketing: "We'll generate N qualified leads"
- Customer Success: "We'll hit X% retention"

Engineering is the only function asked to predict exactly *what* and *when*. But that's accountability for the wrong thing.

### What Engineering Actually Creates

Engineering creates **new opportunities**—changes to the company's trajectory:
- Open new markets → Marketing can generate more leads
- Provide useful APIs → Partners can build new relationships
- Respond to market trends → Sales can convert more leads
- Fix customer problems → Reduce churn and enable upsell

### Product Bets Framework

A **product bet** is a strategic investment in a business result:

1. **Headline**: Business outcome + high-level mechanism
   - "Strike fear into the hearts of Roman infantry by fielding a battalion of war-capable elephants"
   - Result first ("strike fear"), mechanism second ("war elephants")

2. **Sponsor**: Which leadership team member advocates for this

3. **Estimated Present Value**: The quantified expected value
   - Uses present value calculations with cost of capital
   - Combines: new sales + upsells + retention improvements + cost savings - expenditures
   - Credit based on *estimated* value, not measured value (validation is separate)

4. **Maximum Wager**: How much leadership is willing to lose if the bet fails
   - Based on gut feel of risk and value, NOT cost estimates
   - If total spending < present value at cost of capital, still a good investment

### Why Estimate Value Instead of Measuring It

- Actual value takes months to appear
- Too many confounding factors to isolate feature impact
- Saves enormous time vs. proving actual value
- Enables apples-to-apples comparison between bets
- Leadership decides if bet succeeded, then credit the estimated value

### The Build-Measure-Learn Connection

Use iterative development to validate bets early:
- Design loops to test for *failure* early (not just success)
- Weed out unsuccessful bets quickly
- Spend more time on successful ones
- Example: Test war elephants in mountain conditions before battle

### Present Value Calculation Categories

1. **Sales to new customers**: Service obtainable market × sales rate
2. **Upsells to existing customers**: Existing customer market × conversion rate
3. **Retention improvements**: ARR × retention rate change
4. **Cost savings**: Work eliminated + expenses eliminated
5. **Expenditures**: Ongoing operational costs (not development wager)

All numbers are educated guesses—the model's value is shifting conversation to value, not precise prediction.

### The Political Reality: 18-24 Months

> "You have 18-24 months after becoming VP of Engineering to make a difference. After that, the organization's problems become your problems."

Product bets require leadership participation. Before they'll engage, they need to trust you. Before they trust you, you need to demonstrate some form of accountability.

### Shore's Journey at OpenSesame

1. **Product-centric teams with FaST** (Fluid Scaling Technology)
   - Combined siloed tech teams into product-centric "collectives"
   - Single queue of work per product line
   - Self-organizing teams tackle highest priority work

2. **Results focus with Valuable Increments (VIs)**
   - Like epics but focused on standalone value
   - Each VI: releasable, valuable even if nothing else follows, incremental

3. **Reliability with forecasts**
   - Stopped providing estimates to stakeholders (caused friction)
   - Collected "wisdom of the crowd" estimates (median of team gut feels)
   - Stunningly accurate median, but ~2x variance on individual VIs
   - Now forecast at 75% confidence (early 75%, late 25% of the time)

4. **Visibility with muda tracking**
   - Reported percentage of time on value-add vs. muda (waste)
   - Muda: bugs, maintenance, on-call, incidents
   - Eye-opening for leadership—they thought capacity was much higher
   - Accountability reframed: "reduce the grey, increase the blue"

5. **Ongoing push for product bets**
   - Introduced Jan 2024, fizzled. March 2024, sort of tried, fizzled
   - Kept pushing. Got CPO support. CEO support.
   - March 2025: Created five bets, leadership filled in spreadsheet
   - Now working, conversation shifted from "when done" to "how do more bets"

### The TDD Analogy

Microsoft's 2000s "TDD guidelines" got TDD completely backwards—they interpreted it through their waterfall lens:
1. Gather requirements
2. List tests
3. File work items
4. Generate all interfaces/classes
5. Write all tests
6. Write all code

They missed: iteration, refactoring, learning as you go—the entire point.

> "XP is a foreign country. We do things differently here."

Business partners make the same mistake with engineering accountability—they can only interpret through their experience.

### Key Quotes

> "Software development is a foreign country. We do things differently here."

> "People who aren't software developers have probably seen more 'programming' in movies and TV shows than in real life."

> "Features are a means to an end, not the end itself. There's an old cliché that people don't want a shovel, they want a hole in the ground."

> "The numbers are there to feed a conversation: to get people thinking. They're not there to substitute for experience and judgment."

> "We may be a foreign country, but we can still speak our business partners' language."

### Connection to Other Principles

- Complements **Executive Communication** section: Speaks business, not engineering
- Extends **Trillion-Dollar IT Failures**: Addresses root cause of feature/date accountability
- Aligns with **Stewardship Over Spotlight**: Long-term value creation over visible activity
- Supports **Transparent Leadership**: Reduces dependency on "dates and features" promises

## Value-Add Capacity: A Practical Productivity Measure

*Source: [A Useful Productivity Measure?](https://www.jamesshore.com/v2/blog/2024/a-useful-productivity-measure) by James Shore - Added: 2026-01-18*

*Note: This is an earlier piece (2024) that shows Shore's progression toward the Product Bets framework above. It documents his initial solution to the "how do you measure productivity?" question.*

### The Impossible Question

Martin Fowler in 2003: "Cannot Measure Productivity." Kent Beck more recently: "Measure developer productivity? Not possible." Yet VPs of Engineering still face the question: "How are you measuring productivity?"

### Shore's Initial Approach: Accountability Review

When his CEO asked about productivity and things got heated, Shore pivoted to accountability. He led leadership through an exercise: "Imagine we've built the best product engineering organization in the world. What does that look like?"

They developed six categories of indicators. Blissfully, none were "productivity." He presented a "Product Engineering Accountability Review" based on qualitative discussion of engineering progress, not just numbers.

### The Profitability Indicators

One category was "profitability" with three indicators:
1. **Actual RoI** - Best in theory, possibly unmeasurable in practice
2. **Estimated RoI** - Based on Product Bets (see section above)
3. **Value-add capacity** - Usable immediately

The first two require Product Bets to be established. The third was usable right away.

### Value-Add Capacity as Proxy

Engineering time splits between:
- **Value-add work**: Features, improvements customers/users pay for
- **Muda** (waste): Bugs, maintenance, on-call, incident response, deployments

If 100% value-add work at 10x RoI = productivity of 10, then 80% value-add work = productivity of 8.

**In the absence of RoI measures, the percent of engineering time spent on value-add activities is a pretty good proxy for productivity.**

### How It Changed Conversations

Shore presented a stacked bar chart: muda on bottom, value-add on top. Then expanded muda to show time spent on deferred maintenance, bugs, on-call, incident response, deployments.

**The shift:** From "how can we get stuff we want sooner" to "how can we decrease muda and spend more time on value-add work?"

His pitch to leadership: "My job is to double our value-add capacity over the next three years. Essentially, double our output without increasing spending."

### The Fatal Flaw: Goodhart's Law

> "It's ridiculously easy to cheat this metric."

Even with honest categorization, you can:
- Stop fixing bugs
- Defer needed upgrades
- Ignore security vulnerabilities
- ...and poof! Happy numbers. At horrible cost.

**The delay is dangerous:** You can cheat this metric for years. It's not like you cut quality one month and truth emerges the next. This metric only works with scrupulous honesty.

Shore's current org had exactly this problem—prior teams deferred maintenance and took shortcuts under pressure to deliver. Now paying the price.

### When to Use This Metric

**It works when:**
- You're aggressively honest about categorization
- You can police teams' data integrity
- You refuse to skew numbers for appearance
- You're watching closely for gaming

**It doesn't scale:** Once people optimize for the metric, it ceases to be a good measure.

### The Better Path: Product Bets

Shore acknowledges value-add capacity is a stopgap. The real solution is Product Bets with estimated/actual RoI (see section above). But that requires:
- Establishing a bet system
- Getting leadership participation
- Building trust first

Value-add capacity buys time while building toward that.

### Key Quote

> "Deliver valuable software. Do it often. And write it well."

All the productivity metric stuff is a sideshow to what really matters.

### Connection to Other Principles

- **Product Bets** (above): This metric is a stepping stone toward the full framework
- **Organizational Legibility**: Value-add capacity provides legibility without the harm of feature/date accountability
- **AI, Agile, and Invisible Work**: Muda tracking makes invisible maintenance work visible
- **Goodhart's Law** (Osmani #15): "When a measure becomes a target, it stops measuring"

## Resource Library: Debugging Leadership stdlib

*Source: [stdlib | Debugging Leadership](https://debuggingleadership.com/stdlib) - Added: 2026-01-18*

Community-curated collection of 1,000+ practical resources for technical leadership. Categories include:

- **Delegation & Incident Response**: How clearer delegation improves incident handling
- **Agile & Unplanned Work**: Managing sprint disruptions while maintaining flow
- **People Over Process**: Team dynamics and capabilities as the true drivers of success
- **Strategic Thinking**: Helping tech leaders adopt business mindset
- **Individual Recognition**: Why treating engineers as interchangeable leads to attrition
- **Organizational Politics**: Why technical leaders should engage rather than avoid
- **Over-engineering**: Recognizing and avoiding solution bloat
- **Software Maintenance**: "With proper love and attention, it can serve you well for years"

### Key Books Referenced

| Book | Focus |
|------|-------|
| *Atomic Habits* | Evidence-based habit transformation |
| *The Phoenix Project* | DevOps principles via narrative |
| *The Unicorn Project* | DevOps + leadership + collaboration |
| *Accelerate* | Software delivery performance metrics |
| *Team Topologies* | Team structure for fast flow |
| *Domain-Driven Design* (intro guide) | Managing complex software projects |
| *Drive* | Autonomy, mastery, purpose as motivators |
| *Difficult Conversations* | Communication and conflict resolution |
| *Thinking in Systems* | Systems thinking for decision-making |

### Notable Frameworks

- **Mind the Gap Model**: Three categories of challenges when closing the gap between current and desired state
- **Value Flywheel**: Continuous improvement through systematic value creation
- **Continuous Improvement Guide**: Embedding improvement into everyday work

### Connection to Other Principles

Complements many sections in this file:
- Delegation topics connect to **Transparent Leadership** section
- Individual recognition aligns with **Stewardship Over Spotlight**
- Business mindset covered in **Executive Communication**
- Team dynamics addressed in **Addy Osmani's 21 Lessons**

## The Expert-Layman Problem: Hiring Outside Your Expertise

*Source: [The Expert-Layman Problem](https://vonnik.substack.com/p/the-expert-layman-problem) - Vonnik's Newsletter - Added: 2026-01-18*

How do you recognize expertise in a domain you haven't mastered? Every founder and leader faces this when hiring outside their core competency.

### Expert-Layman vs. Principal-Agent

**Principal-Agent Problem**: Managing someone who has information advantages over you. Agents are closer to the action and can deliver suboptimal results while concealing conflicts of interest.

**Expert-Layman Problem**: The *moment of choice*—hiring or selecting someone outside your expertise. The reasons you need an expert are the same reasons you can't recognize a good one.

### Common Approaches to the Problem

1. **The Easy, Bad Way** - Social proof. "Let's just hire McKinsey." Outsources judgment to brand recognition.

2. **The Lucky Way** - Tap networks. Ask people you trust for recommendations. Not everyone has these networks; this is partly why good investors add value beyond capital.

3. **The Hard Way** - Rigorous interviewing technique.

### Interviewing Outside Your Expertise

**What good candidates can do:**
- Explain clear mental models of how things work
- Describe what they need to do to get things done
- Explain how they measure success or failure
- Illustrate anything they say with a concrete instance
- Walk through their workflows and why they make certain decisions

**What better candidates can do:**
- Go into granular detail about every aspect of their work
- Explain their work to outsiders (great communicators)
- Zoom in and zoom out fluidly
- Teach you something valuable and new during the conversation

**What the best candidates can do:**
- Have invented terms to describe things they encounter in professional rabbit holes
- Talk about their work with humor
- Show signs of extracurricular interest (recreational reading shows work is a passion project)

### The Interview Technique

Set the expectation that you will lead a "gentle but persistent interrogation":

1. **Go deep** - When you ask a question, expect to ask several follow-up questions on the same topic. Interrupt long, prepared monologues.

2. **Demand concrete examples** - If they make a general statement, ask for a specific instance. "We were targeting engineering directors" → "Why? What's the maximum they can spend without external permission? Credit card or procurement? Have you tried selling to other roles?"

3. **Test their decision trees** - They should be able to break down their workflow into distinct stages and explain the reasoning that leads to next steps.

### Dealbreakers

- **Hand-waving** after you've signaled you want to go deep
- **Lack of concrete examples** - Universal dealbreaker
- **Inability to reason about hypotheses** - Can't explain why they chose one path over another

> "If a candidate can't break down their workflow into distinct stages, and talk about the decision tree that leads them to next steps, they don't know their business well enough to do it for you."

### Key Insight

The technique works because it tests *depth of understanding*, not domain knowledge. You don't need to evaluate whether their answer is correct—you're evaluating whether they can navigate their own expertise with fluency and precision.

### Connection to Other Principles

- **Executive Communication**: The "zoom in and zoom out" skill applies to exec communication too
- **Stop Avoiding Politics**: Hiring decisions are inherently political—network-tapping is a form of good politics
- **Transparent Leadership**: Good hires can explain their reasoning, enabling knowledge transfer

## Related
- Author: Sarah Chen (VP of Engineering at Acme Corp) - see people/sarah-chen.md
- Author: Anna Shipman (CTO at Kooth) - guest writer on Refactoring.fm
- Author: Addy Osmani - Google engineer, 14 years at Google
- Author: Linus Akesson - programmer, writer
- Author: Lalit Maganti - Senior Staff Engineer at Google, Perfetto/trace tooling
- Author: James Shore - VP Engineering at OpenSesame, author of "The Art of Agile Development"
- Author: Sean Goedecke - Software engineer, writer on tech company dynamics
- See also: [[software-project-failures]] for full case studies (Phoenix, Horizon, etc.)
- Colin Percival - FreeBSD developer, AWS Hero for 6 years, long-time AWS/Amazon customer
- James Shore - VP Engineering at OpenSesame, 23 years consulting - see "Product Bets" and "Best Engineering Org" sections
- Dan McKinley - Engineering leader, early Etsy employee, speaker on org dysfunction - see "Egoless Engineering" section
- Erik Dietrich - Management consultant, founder of Hit Subscribe - see "Effective Delegation" section

## Effective Delegation: From Micromanagement to Accountability

*Source: [How to Delegate Effectively as Your Responsibility Grows](https://www.hitsubscribe.com/how-to-delegate-effectively-as-your-responsibility-grows/) by Erik Dietrich (management consultant, founder of Hit Subscribe) - Added: 2026-01-18*

A framework for understanding delegation styles and evolving beyond micromanagement. Key insight: successful delegation involves both tasks AND accountability—unsuccessful delegation cedes only tasks while retaining a vice grip on all accountability.

### Delegation Styles by Level

| Level | What You Delegate | Expected Deliverable |
|-------|-------------------|---------------------|
| **Executives** | Organizational goals | A plan and overseeing execution |
| **Middle Management** | Execution of plans | Judgment-based execution in fluid environments |
| **Supervisors** | KPIs | Task execution that generates KPIs |
| **ICs (Micromanagement)** | Nothing—only tasks | Exact specification compliance |

### When Micromanagement (IC-Style Delegation) Is Appropriate

Surprisingly, detailed runbooks have legitimate uses:
- No contact with inexperienced executor (e.g., microwave instruction manual)
- High-stakes tasks rarely executed (e.g., offboarding senior employees)
- Endless turnover in the executing role
- Programming a computer (which takes things extremely literally)

**Key insight**: These are all suboptimal situations. IC-style delegation to humans is usually a placeholder until someone automates or eliminates the task.

**Why programmers struggle**: They've spent careers learning how to delegate to computers—extremely detailed, exact specifications. This makes them bad at delegating to humans.

### The Pain of Micromanagement

**1. Scale Will Crush You**
You become a collaborator on all work. Team of 3 doesn't produce 3x work—you're assigning multiple people to every task the outside world thinks is single-person.

**2. Innovation and Change Are Terrifying**
Detailed runbooks calcify your group. Every variance requires manual updates. Eventually you get irrationally upset when anything new appears.

**3. Permanent Juniority**
You create learned helplessness. People can't operate the microwave without your guidance. Then you get frustrated: "Can't you figure this out yourself?" But you've created an environment where the answer is "nope."

**4. Bad Results Despite Control**
Humans can't faithfully execute lengthy, complex tasks by rote. People operating in good faith won't remember everything on page 45, section 2B. And eventually talented people start maliciously complying with your inherently flawed instructions.

**5. Talent Exodus**
Talented people quit—or ignore you. The only people who stay are happy to say "whatever, you're the boss."

### Self-Assessment Heuristics

Signs you're in the micromanagement weeds:
- Delegation takes the form of numbered step lists
- Runbooks focus on "how" not "what," never mention "why"
- You can't answer "What decisions are your reports empowered to make?"
- All unusual events come as "What should we do?"
- You orchestrate interaction protocols between reports
- You're constantly updating documentation people live in
- Increase in their workload feels like increase in YOUR workload
- You evaluate people on how reliably they do exactly what you would have done

### Moving Toward Effective Delegation

**1. "I Wouldn't Have Done That, and That's Okay"**
Accept that people will do things differently. You're not the boss because you unlocked optimal task execution. The inefficiency of micromanagement far outweighs any gains from forcing your "better" way on everyone.

**2. Differentiate What and How**
Go through everything you're about to delegate. Identify which parts define what you want done vs. how to do it. Don't need to change yet—just become aware.

**3. Define Success Criteria and Explain Why**
Move from "I don't like this editor" to "We're doing this to enable people to come with questions to the kickoff meeting." This lets people work however they'd be most productive—and propose alternatives you didn't think of.

**4. Create Safe Failure Zones**
Stop neurotically trying to prevent mistakes. Create situations where mistakes are okay. Example: Let people draft in whatever tool they want; have a "formatting sanity checker" catch issues before publish.

**5. Cap Your Requirements**
If you're adding item 74 to the checklist, stop. Nobody will remember all of that. When cognitive burden gets too high, rethink the whole approach—get out of "how" weeds, go back to what and why.

**6. Favor Reference Material Over Runbooks**
Reference cheat sheets for common situations (e.g., microwave settings for foods) vs. instruction manuals for every scenario. Enable rather than order.

**7. Favor Checklists Over Instructions**
Checklists are "what" (outcomes to verify); instructions are "how" (steps to follow). "I optimized for the target keyword" doesn't specify how—puts onus on the person. If they don't know, it's a training need, not a runbook need.

**8. Differentiate Training from Standing Instructions**
Detailed, screenshot-heavy material is great for onboarding. It's not meant to be memorized and followed precisely forever. Make purpose clear.

**9. Ask "Why Are You Asking Me This?"**
When reports ask what to do, respond: "Why are you asking me this? I'm asking literally, not to suggest you're wrong."

Two possibilities:
- **Empowerment gap**: You haven't empowered them to decide. Consider whether you should.
- **Confidence gap**: They don't know enough or are worried about responsibility. Arm them with more knowledge.

This is an iterative path toward delegating more decisions.

### The Philosophy

> "Hire good people and trust them."

Most people operate in good faith and will pleasantly surprise you when trusted and empowered. The occasional person who doesn't—having a solid delegation approach exposes those shortcomings in ways micromanagement never could.

### Connection to Other Principles

- **Transparent Leadership**: Both advocate for making yourself redundant through teaching and enabling
- **Stewardship Over Spotlight**: Effective delegation enables long-term stewardship rather than heroic individual contribution
- **Organizational Legibility**: Micromanagement creates false legibility—detailed documentation that doesn't improve outcomes
- **Egoless Engineering**: "Domain experts, not domain owners" parallels the supervisor vs. IC delegation distinction
- **Defense/Offense Engineering**: Requires trust in the "fortress" team to handle their domain without micromanagement

## Organizational Legibility: The Hidden Cost of Process

*Source: [Seeing Like a Software Company](https://www.seangoedecke.com/seeing-like-a-software-company/) by Sean Goedecke - Added: 2026-01-18*

*Background: [[legibility-high-modernism]] - James C. Scott's foundational concept of legibility and high-modernist failure*

Drawing on James C. Scott's *Seeing Like A State*, this framework explains why large tech companies do things that seem obviously counter-productive, and why rule-breaking is tolerated in some contexts.

### The Legibility/Illegibility Dichotomy

**Legible work**: Predictable, well-estimated, has a paper trail, doesn't depend on specific people. Quarterly planning, OKRs, Jira—all exist to make work legible.

**Illegible work**: Asking for favors, using tacit knowledge, fitting unscheduled changes, drawing on relationships. Essential but can't be tracked or planned for.

### Scott's Core Insight (From German Forestry)

The "efficient" 19th-century German forests were actually *less* efficient than messy natural forests:
- Produced less wood per year
- Required more effort to fight disease
- Could be wiped out by single parasites

But legibility's advantages were enormous: planning ahead, making trade deals, avoiding graft. Organizations continued pursuing legibility even when it clearly reduced efficiency, because other benefits were too powerful.

### Why Legibility Matters to Tech Companies

1. **Enterprise deals require legibility** - Large customers won't trust companies that can't make long-term feature commitments
2. **Highly legible orgs struggle to communicate with illegible ones** - Different language, different bona fides
3. **Growing companies face pressure to become more legible** - Even if it hurts software delivery

What legibility enables:
- Department heads know all current projects to the engineer
- Comprehensive ship lists for any quarter
- Ability to plan work one+ quarters ahead
- Emergency resource redirection

Note: "Shipping high quality software" is NOT on this list.

### The Simplifying Assumptions (All False)

Large companies assume:
- Engineers with same title perform roughly the same
- Engineers can be shuffled without productivity loss
- Team productivity correlates with headcount
- Projects can be estimated; more estimation = more accuracy

All false. But *true enough* for providing legibility to executives. Project estimates are performative—they determine the engineering approach, not the other way around.

### Temporary Zones of Sanctioned Illegibility

When urgent problems arise (database overflows, show-stopping customer bugs), companies create "tiger teams" or "strike teams":
- Hand-picked trusted engineers
- Often no manager, just a senior engineer
- Loose mandate ("stop the database falling over")
- Allowed to bypass normal process

These are smart compromises—but almost always temporary. Engineers outside resent the freedom; managers don't like extending trust.

### Permanent Unsanctioned Illegibility: Backchannels

The formal way to get cross-team work done:
1. Create issue in their planning backlog
2. Wait for 12-step process
3. Hope it enters a sprint eventually

**Takes weeks to months for a one-line change.**

The actual way: "Hey, can you make this one-line change for me?" Done immediately, maybe with a ticket, maybe not.

Backchannels are relationship-dependent—illegible by nature. A well-liked engineer can pull on them far more than a newcomer. Companies can't plan for this, but it's load-bearing.

Backchannels exist at all levels: engineer-engineer, manager-manager, product-product. Formal public questions are often pre-rehearsed through private channels.

### The Three Organizational Personas (Venkatesh Rao's Gervais Principle)

1. **"Sociopaths"** (top): Cynically use organizational rules for personal benefit. Engaged with illegible world to climb the ladder.

2. **"Clueless"** (middle management): Bought into formal rules, don't realize there's a deeper game. Only engaged with legible processes. When faced with illegibility, try to draft updates to formal process.

3. **"Losers"** (bottom, not pejorative): Realize there's a game but don't want to play. Use illegible world to carve out comfortable niches.

**Friction between these groups explains many software company conflicts.**

### The Naive View to Avoid

> "If a process needs changing, change the process instead of going around it. Everything should be legible."

This is naive. All organizations have both legible and illegible sides:
- **Legible side**: Enables long-term planning, coordination with other large orgs
- **Illegible side**: Allows high-efficiency work, release valves for process failures, human need for gossip and soft consensus

### Dangerous Advice

Advice about using illegibility is "dangerous advice"—if you announce publicly you're using backchannels instead of formal process, you'll be punished even if management wanted you to do it. It has to stay illegible.

### Connection to Other Principles

- **Executive Communication**: Executives value legibility highly—frame proposals accordingly
- **Stewardship Over Spotlight**: Infrastructure teams often operate more illegibly, building trust through utility rather than process
- **Transparent Leadership**: The best leaders enable both legible accountability AND illegible effectiveness
- **Product Bets**: Shifts accountability to value (more legible to business) from features/dates (legible but wrong thing)

### Key Quote

> "It should be obvious to any practicing engineer that engineer-driven work goes far more swiftly than work mandated from above. Engineer-driven work doesn't need to be translated into something that makes sense, doesn't need to be actively communicated in all directions, and can in general just be done in the most straightforward and efficient way."

## Stop Avoiding Politics: Organizational Influence for Engineers

*Source: [Stop Avoiding Politics](https://terriblesoftware.org/2025/10/01/stop-avoiding-politics/) by Terrible Software - Added: 2026-01-18*

A direct challenge to the "I'm above politics" mindset common among engineers. Politics isn't dirty—it's how humans coordinate in groups. Refusing to participate just means decisions get made without you.

### The Anti-Politics Fallacy

Many engineers wear hatred of politics as a badge of honor—"I just want to ship code." But this is self-defeating:

> "You can refuse to participate, but that doesn't make it go away. It just means decisions get made without you."

When terrible technical decisions get pushed through, it's usually not because decision-makers were stupid. It's because the people with the right information weren't in the room—they "didn't do politics."

### Ideas Don't Speak. People Do.

The people who understand how to navigate organizational dynamics, build relationships, and play politics? Their ideas get heard. Not because their ideas are better, but because they showed up to play while everyone else stayed "pure."

### What Good Politics Actually Looks Like

It's not becoming a scheming backstabber. Same trait, different application:
- **Bad politics**: Manipulation, self-promotion, zero-sum games
- **Good politics**: Getting good ideas implemented, protecting your team from bad decisions

Practical examples of good politics:

1. **Building relationships before you need them** - That random coffee with someone from the data team? Six months later, they're your biggest advocate for getting engineering resources.

2. **Understanding real incentives** - Your VP doesn't care about your beautiful microservices architecture. They care about shipping features faster. Frame technical proposals in terms of what they actually care about.

3. **Managing up effectively** - Your manager is juggling competing priorities you don't see. Keep them informed, flag problems early with solutions, help them make good decisions. When they trust you, they'll fight for you.

4. **Creating win-win situations** - Instead of fighting for resources, find ways to help other teams while getting what you need. Not zero-sum.

5. **Being visible** - If you do great work but nobody knows about it, did it really happen? Share wins, present at all-hands, write design docs that everyone references.

### The Stakes

The alternative to good politics isn't no politics—it's bad politics winning by default:
- The loud person who's wrong gets their way because the quiet person who's right won't speak up
- Good projects die because nobody advocated for them
- Talented people leave because they couldn't navigate organizational dynamics

### The Reframe

"Stakeholder management," "building alignment," "organizational awareness"—these are just politics by another name. The best technical leaders are incredibly political. They just don't call it that.

### Key Quote

> "Stop pretending you're above politics. You're not. Nobody is. The only question is whether you'll get good at it or keep losing to people who already are."

### Connection to Other Principles

- **Osmani Lesson #6**: "Your code doesn't advocate for you. People do."
- **Executive Communication**: Speaking business, understanding stakeholder incentives
- **Organizational Legibility**: Understanding when to use formal vs. informal (backchannel) influence
- **Stewardship Over Spotlight**: Building trust capital through competence, then using it politically when needed

## Delete Your Tests: When Tests Harm Confidence

*Source: [You should delete tests](https://andre.arko.net/2025/06/30/you-should-delete-tests/) by André Arko - Added: 2026-01-18*

A counter to the folk wisdom that "it is blasphemy to delete a test." The consensus beliefs around testing ("include tests for changes," "write tests when fixing bugs") are helpful—but treating tests as sacred is actively harmful.

### Why Tests Exist

Tests exist to increase **confidence** that a change will succeed. Not to prove correctness, not to satisfy process, but to give humans confidence when opening PRs, merging, and deploying.

> "Confidence is the point of writing tests."

### When Tests Decrease Confidence

Any test that decreases confidence in a change should be deleted:

**Flaky tests** - The biggest confidence killer. Random failures lead to "Oh, it's that flaky test, it's fine" reasoning—even when the code is actually broken. A test creating false confidence in broken code would be better if it didn't exist.

The argument for keeping flaky tests ("what if it catches something someday") doesn't hold up. Flaky tests cost days or weeks of derailed work; a future bug won't take that long to fix. Delete the test, allow the possibility of a bug, fix it when it occurs with a test that doesn't flake.

**Tests requiring excessive updates** - If a one-line code change requires updating 150 tests, do those 150 checks really add more confidence than 2-3 well-placed tests? Delete the tests.

**Tests that don't get run** - When the suite is too slow and chunks get skipped "because they always pass," that's another kind of false confidence. A test that doesn't get run but people act like it's green will bite you. Delete the tests.

**Tests for outdated requirements** - When business requirements change and thousands of tests fail because they test the wrong thing, updating them to pass doesn't increase confidence in the new behavior. You need to test the new behavior directly. Delete the tests.

### The Key Insight

Tests aren't a historical record or proof of correctness. They're a tool for confidence. When they stop serving that purpose—through flakiness, maintenance burden, or irrelevance—they should go.

### Connection to Other Principles

- **Osmani's "The best code is the code you never had to write"**: Applies to tests too
- **Over-engineering critique**: Tests can become over-engineered just like code
- **Bias for Action**: Sometimes the action is deletion, not addition
- **Kernighan's Lever**: Tests should help you debug, not create debugging work

## Amazon's Leadership Principles: A Critique From the Outside

*Source: [Thoughts on (Amazonian) Leadership](https://www.daemonology.net/blog/2025-09-01-Thoughts-on-Amazonian-Leadership.html) by Colin Percival (FreeBSD developer, 20+ year AWS customer, 6-year AWS Hero) - Added: 2026-01-18*

Amazon's Leadership Principles are famous and often mocked—but generally sensible rules by which to run a company. Commentary from someone who's seen behind the curtain without working there:

### Customer Obsession: Don't Just Build Faster Horses

> "Leaders start with the customer and work backwards. They work vigorously to earn and keep customer trust."

The principle is great, but Amazonians often take it too simplistically. "Start with the customer" doesn't have to mean "ask customers what they want and then give them faster horses."

**The Shift Percival Observed:**
- **Early AWS (pre-2012)**: "Cool engineering driven" products. EC2 launched without a clear use case—just very cool building blocks that could be a big deal.
- **~2012 shift**: From "provide cool building blocks" to "build what customers are asking for" (a step backward)
- **~2020 shift**: From customers to "build what analysts are asking for in quarterly earnings calls" (even worse)

### Ownership: Think Beyond Your Company

> "Leaders are owners. They think long term and don't sacrifice long-term value for short-term results. They act on behalf of the entire company, beyond just their own team."

**The principle is too narrow.** It's not enough to act on behalf of the entire company—you should act on behalf of the entire technological ecosystem.

**Example of doing it right:** An Amazonian putting together a standard for interrupt handling in large VMs reached out to FreeBSD's bhyve (which Amazon doesn't use). He understood the importance of getting standards widely accepted across the entire virtualization space, not just in the code Amazon relied upon.

**The Security Analogy:** "Anything which makes one of us less secure makes all of us less secure." While not directly applicable in other fields, working with others to produce the best results for everyone beats focusing solely on what your company needs right now.

### Bias for Action: The Hidden Tension with Trust

> "Speed matters in business. Many decisions and actions are reversible and do not need extensive study. We value calculated risk taking."

Amazonians talk about "one-way doors" and "two-way doors." Many decisions can be reversed—but that doesn't mean there's no cost to reversing them.

**Three tensions:**
1. Bias for Action vs. Insist on the Highest Standards (widely recognized)
2. Bias for Action vs. earning and keeping customer trust (underappreciated)
3. Speed vs. memory—when AWS ships a half-baked service, it diminishes customer trust in AWS as a whole. Even if problems get corrected, the memory of a failed launch lives on in customers' minds for years.

### The Advice to Amazon

Werner Vogels famously said at re:Invent 2024: "Listen to the AWS Heroes." Percival suggests Amazon might benefit from listening to this critique too.

> "We criticize because we care."

### Connection to Other Principles

- **Product Bets Framework**: Both critique the "build what customers/analysts ask for" approach in favor of strategic value creation
- **Osmani's "Solve user problems, not technology problems"**: Similar to "don't build faster horses"
- **Stewardship Over Spotlight**: Ownership extending beyond your org/company to the broader ecosystem
- **Organizational Legibility**: The shift from "cool engineering" to "what analysts want" is a shift toward excessive legibility

## Game Theory at Work: Strategic Communication

*Source: [Game Theory at Work: When to Talk and When to Shut Up](https://swaits.com/game-theory-at-work-and-when-to-shutup/) by swaits.com - Added: 2026-01-18*

Every workplace conversation is a strategic decision. Game theory provides a framework for evaluating when to speak and when to stay silent based on potential outcomes.

### The Core Framework

Before speaking, evaluate the payoff matrix:
- **If you speak and it goes well**: What's the gain?
- **If you speak and it goes poorly**: What's the loss?
- **If you stay silent**: What's the outcome?

When potential losses significantly outweigh potential gains, silence is the strategic choice.

### Scenario Analysis

**Politics at Work**: Never discuss political views at work.
- Best case (agreement): Small gain (nod of approval)
- Worst case (disagreement): Massive loss (damaged relationships, HR issues)
- Staying quiet: No loss, potential gain (seen as professional)
- **Verdict**: Nothing to gain, lots to lose. Universal rule.

**Raising Project Concerns**: Generally speak up.
- Right and you speak: Moderate gain (project improves, credibility)
- Wrong and you speak: Small loss (mild embarrassment)
- Stay quiet when flaw is real: Large loss (project fails, you knew and said nothing)
- **Verdict**: Potential gain outweighs risk. Speak up thoughtfully.

**Gossip About Leadership**: Never participate.
- Join and it stays secret: Tiny gain (fleeting social connection)
- Join and it gets back to the boss: Massive loss (lost trust, career damage)
- Stay quiet: No loss, potential gain (seen as trustworthy)
- **Verdict**: Asymmetric risk. Stay out.

### The Meta-Game: Reputation Building

Each interaction plays into a larger game—building your professional reputation. Every choice to speak or stay quiet sends signals:
- The person who always has something to say
- The quiet observer who speaks only when it truly matters
- The gossip
- The level-headed professional

Reputation is the sum of all these small games, with long-lasting career effects.

### Practical Implementation

1. **Pause before speaking** - Consider best-case, worst-case, and risk/reward ratio
2. **Consider the long game** - How will this affect reputation over time?
3. **Observe the winners** - When do respected colleagues choose to speak or stay quiet?
4. **Practice strategic silence** - Sometimes the most powerful move is saying nothing
5. **When you do speak, make it count** - Choose moments carefully, ensure it adds real value

### Connection to Other Principles

- **Stop Avoiding Politics**: Game theory supports engaging with organizational politics (high upside) while avoiding partisan politics (high downside, no upside)
- **Executive Communication**: Speaking to executives has asymmetric payoffs—prepare thoroughly
- **Organizational Legibility**: Legible work (speaking in meetings) vs. illegible work (backchannels) have different risk profiles
- **Osmani's "If you win every debate, you're accumulating silent resistance"**: Even when the payoff matrix favors speaking, there's a long-term reputation cost to winning every argument

## AI, Agile, and the Invisible Work of Engineering

*Source: [AI is going to hack Jira](https://thoughtfuleng.substack.com/p/ai-is-going-to-hack-jira) by Christine Miao - Added: 2026-01-18*

A critique of how the "Agile Industrial Complex" has scrambled our understanding of engineering work, and why AI code generation will make the problem worse.

### The Fundamental Measurement Error

Engineering productivity cannot be measured by tracking new features or deployment velocity. This is like managing a company by only looking at margins—absent context, you can't tell if high margins mean healthy efficiency or reckless cost-cutting.

**What engineering actually is:** Building, maintaining, and evolving an interconnected system. The work of managing dependencies, resourcing, and architecture keeps you alive.

**What Big Agile tracks:** Byproducts (features, story points, t-shirt sizes, deployments per day).

The existential work of maintaining systems is invisible and taken for granted. This leads to absurdities like:
- Tiny startups copying DevOps practices of huge enterprises
- PMs allocating exactly 20% to maintenance regardless of actual need
- The top response from engineers on how to prioritize critical maintenance: "Wait until it becomes an emergency"

### Why AI Code Gen Makes This Worse

AI excels at producing byproducts—the exact things the Agile Industrial Complex already over-values.

**The construction analogy:** Imagine believing house-building is a series of disconnected tasks (wallpapering, installing toilets, cabinets). Now imagine an AI that does all of this for free, instantly. You fire your expensive human team. The AI keeps adding rooms.

Then you realize:
- Your new powder room was never connected to the water main
- When the AI "fixes" it, it breaks the kitchen plumbing
- The AI can't explain why (neural systems can't recognize their own hallucinations)
- While building haphazardly, the city updated electric/water/fire codes
- Your old human team can't help—the house changed beyond recognition

**This is already playing out:** CEOs fire competent engineering teams. The team's high skill ensures nothing bad happens *in the near term*—well-built foundations take work to screw up. EBITDA and "productivity" look great. By the time the bill comes due, the CEO is off replicating their "success" elsewhere.

### The Infrastructure Threat

Software is the backbone of health services, financial services, government infrastructure, military systems. We're rushing to replace roles we don't understand with technology we understand even less.

### The Antidote: Common Sense

Most non-technical leaders have never engaged with the real work of software:
- Updating major dependencies
- Completing a refactor
- Learning a new language

Instead, they deal in disconnected artifacts: "t-shirt sizing" their "user stories" before "poker planning" their "sprint" with their "scrum master."

**The parallel:** If someone sold you an AI robot cleaner, you have an intuitive grasp of what cleaning entails. You'd know when the AI puts paper plates in the dishwasher. This common sense is what Big Agile has robbed us of for engineering.

### Technical Accounting (Miao's Framework)

Miao proposes "technical accounting"—tracking engineering maintenance, resourcing, and architecture rather than byproducts. Built on 200+ CTO interviews. Claims anyone can build a common-sense understanding of their engineering org in 15 minutes.

The goal: Leaders who understand the actual work can leverage AI with finesse instead of being played for chumps by metrics theater.

### Key Quote

> "Decorating is only possible if you have a standing structure to work with."

### Connection to Other Principles

- **Trillion-Dollar IT Failures**: Same root cause—measuring visible outputs instead of systemic health
- **Organizational Legibility**: The Agile Industrial Complex is extreme legibility—tracking only what can be counted, ignoring what actually matters
- **Product Bets Framework**: Both argue against feature/date accountability in favor of value
- **Stewardship Over Spotlight**: Infrastructure maintenance is exactly the "invisible work" that doesn't get credited but keeps everything running
- **Delete Your Tests**: The confidence/measurement distinction applies here—metrics should increase confidence in system health, not just count activities

## Richard Garwin: The Invisible Giant of Nuclear Arms Control

*Source: [Dick Garwin Fought Nuclear Armageddon. He Hid a 50-Year Secret](https://archive.ph/16i0Y) - The New York Times, 2025 - Added: 2026-01-18*

Richard Garwin (1928-2025) designed the hydrogen bomb at age 23, then spent his life countering his creation. His story illustrates the relationship between technical expertise, moral responsibility, and long-term influence.

### The Ultimate Stewardship Over Spotlight

Garwin was "the most influential scientist you've never heard of." He told newcomers to the federal apparatus:

> "You can get something done or get credit, but not both."

For 50 years, he hid his role as the bomb's designer. His family didn't know until 2001 when a journalist found the information. His reasoning: protecting family from foreign intelligence agencies—not seeking anonymity for its own sake, but practical security.

### Technical Expertise as Policy Leverage

Garwin advised 13 consecutive U.S. presidents from Eisenhower to Trump. President Obama described him as advising White House occupants "rather bluntly."

Key contributions:
- **1962**: Warned Kennedy that high-altitude nuclear tests would create radiation belts dangerous to Apollo astronauts. Led to Partial Nuclear Test Ban Treaty.
- **1971**: Designed architecture for new spy satellites that enabled arms control verification. Received CIA and NRO awards.
- **1995**: Resolved technical dispute threatening Comprehensive Test Ban Treaty negotiations.

### Long-Term Thinking and Persistence

After the Senate rejected the Comprehensive Test Ban Treaty in 1999, Garwin reflected:

> "You do these things. And if you keep at it for a long time, sometimes you win."

The treaty never entered into force, but the process created a global norm. Since then, major nuclear powers have tested no weapons—a new kind of silence.

### The Fermi Legacy: Speaking Out

Garwin's mentor Enrico Fermi (who called Garwin "the only true genius I have ever met") confided on his deathbed that he regretted too little participation in public policy. Garwin modeled himself after Fermi and took the lesson:

> "I modeled myself to whatever extent I could after Fermi."

### On Personal Responsibility for Creation

Garwin took no personal responsibility for creating the H-bomb, arguing its birth was inevitable:

> "Maybe I sped up its development by a year or two. That's all."

But this didn't diminish his commitment to countering it. The inevitability argument freed him to focus on what he *could* control: arms control, verification, policy advice.

### The Real Danger (A Reframe)

In his final interview, Garwin said Fermi was wrong about the H-bomb's danger:

> "That's not the threat. The great danger is so many nuclear weapons—which raise the risk of theft, missteps, accidents, unauthorized use."

The system is the problem, not the individual component.

### Connection to Other Principles

- **Stewardship Over Spotlight**: Exemplified by Garwin's anonymous influence across administrations
- **Stop Avoiding Politics**: Technical experts must engage with policy—the alternative is decisions made without expertise
- **Wilson's Warning**: "Paleolithic emotions, medieval institutions, god-like technology"—Garwin embodied the effort to close this gap
- **Product Bets / Long-term Value**: The Comprehensive Test Ban failed politically but succeeded in establishing norms—sometimes the value isn't what you planned

### Key Insight for Engineers

The creator of the world's most destructive weapon became its most persistent counterweight. Technical expertise creates moral obligation to engage with the consequences of your work—not guilt, but responsibility to participate in guiding how your creations are used.

## The Cannae Problem: When Success Breeds Failure

*Source: [The Cannae Problem](https://www.joanwestenberg.com/the-cannae-problem/) by Joan Westenberg - Added: 2026-01-18*

When an organization's conventional wisdom—its tried-and-true methodologies, its fundamental understanding of how the world works—becomes the very thing that destroys it.

### The Pattern

At Cannae (216 BCE), Rome fielded its largest-ever army (80,000 men) against Hannibal's force of half that size. By sunset, 50,000-70,000 Romans were dead. The Roman military system—standardized equipment, training, tactics—had worked brilliantly for centuries. That very success created the blind spots Hannibal exploited.

**The trap:** Success reinforces belief in the system. Victory after victory proves you're right. Why change what works?

### The Cognitive Biases

1. **Confirmation bias**: Centuries of evidence confirmed Roman superiority. Earlier defeats (Trebia, Lake Trasimene) were rationalized as anomalies—bad terrain, poor leadership—not fundamental flaws.

2. **Curse of expertise**: Expert practitioners become blind to alternative approaches. Mental maps of "how things work" become so ingrained you can't recognize when the territory has changed.

3. **Normalization of deviance**: When Hannibal's center retreated unusually, Romans normalized it to fit their model: "The enemy is breaking, just as expected."

4. **Groupthink**: Roman doctrine was so established that questioning it marked you as ignorant or cowardly. Social pressure prevented concerns from altering the approach.

### Modern Cannae Moments

**Kodak**: Invented the first digital camera in 1975, but their mental model—"We sell film"—prevented them from seeing they were in the memory business. By the time they realized, they were surrounded.

**Blockbuster**: Saw late fees as vital revenue rather than customer pain. Had the chance to buy Netflix for $50 million in 2000. Their conventional wisdom about video rental prevented them from seeing Netflix as a serious threat.

**Nokia**: 50% mobile market share in the early 2000s. Mental model built on hardware expertise and incremental innovation. Dismissed the iPhone in 2007. By the time they recognized the paradigm shift, they were surrounded.

**DEC**: Dominated minicomputers, then dismissed PCs as toys. "There is no reason for any individual to have a computer in his home." Sold to Compaq for a fraction of their peak value.

### The Disruptor's Playbook

Disruptors specifically look for gaps between established players' mental models and reality. They don't play the same game better—they change the game entirely.

> "Hannibal didn't get lucky at Cannae. He deliberately engineered a situation that would exploit Roman orthodoxy."

### Breaking Free

1. **Implement red teams**: Institutionalize skepticism. Task people specifically with challenging assumptions and developing strategies that would defeat current approaches.

2. **Study near-misses, not successes**: We study successes and ignore close calls. Near-misses contain valuable information about weaknesses that were just lucky enough not to be catastrophic... yet.

3. **Reward productive dissent**: When everyone agrees, something is wrong. Actively reward people who challenge conventional wisdom productively.

4. **Develop multiple mental models**: Cultivate multiple ways of understanding your work. Regularly test them against each other.

5. **Practice temporal displacement**: "If I were starting from scratch today, knowing what I know now, would I do things the same way?" If no, that's a red flag.

### The Identity Trap

The hardest mental models to change are those tied to identity. Rome's aggressive military approach wasn't just strategy—it was part of Roman identity. Kodak's film, Blockbuster's stores, Nokia's hardware weren't just business models—they were who these organizations understood themselves to be.

Breaking free often requires feeling like a traitor to your identity in the short term to ensure survival in the long term.

**The Fabian Strategy**: After Cannae, Romans stopped trying to defeat Hannibal directly. Fabius Maximus adopted delay and attrition. It felt wrong—contradicted centuries of conventional wisdom, appeared cowardly. Fabius was mocked as "Fabius the Delayer." But it worked. Only later was he recognized as Rome's salvation.

### The Fundamental Attribution Error

When organizations fail, we look for scapegoats. At Cannae, Romans blamed Varro. At Kodak, they blamed the CEO. But the Cannae Problem is primarily systemic, not individual.

> "The issue isn't just bad decisions; it's that the entire decision-making framework—the mental model itself—has become obsolete while still appearing valid."

### The Final Blind Spot

Sometimes you lose because someone like Hannibal is on the other side. The belief that all failure is self-inflicted—that with the right tweaks you could've won—is comforting but false.

Pickett, asked why the South lost at Gettysburg:

> "I always thought the Yankees had something to do with it."

### Key Questions

How many organizations today are standing at their own Cannae, confident in their conventional wisdom, unaware they're about to be surrounded?

What mental models in your organization are so successful, so proven, so obviously correct that no one questions them anymore?

**Those are exactly the ones you should examine first.**

### Connection to Other Principles

- **Trillion-Dollar IT Failures**: Project managers who claim "our project is different" exhibit the same pattern—ignoring documented lessons because their mental model says they're unique
- **Organizational Legibility**: Success creates legible processes that become orthodoxy, creating blind spots for illegible disruption
- **Product Bets**: Challenges the mental model that features/dates accountability works, proposing value-based alternatives
- **Stop Avoiding Politics**: Organizational dynamics can prevent dissent from reaching decision-makers—politics as a skill helps surface concerns
- **Stewardship Over Spotlight**: Long-term stewards often see pattern shifts that spotlight-seekers miss—they've been watching longer

## Egoless Engineering: Breaking Down Silos

*Source: [Egoless Engineering](https://egoless.engineering/) by Dan McKinley - Added: 2026-01-18*

A talk on organizational dysfunction in engineering teams, identifying parochialism and ego as the root causes of coordination failures, and offering a framework for building more effective teams.

### The Universal Dysfunction

Every struggling engineering organization Dan has worked at shared common patterns:
- **Role proliferation**: Creating new job descriptions for every new thing (AI engineers, release managers, etc.)
- **Assembly line thinking**: Once roles subdivide, work gets serialized through queues
- **Ops/dev divide**: Despite claiming to "do devops," most companies maintain strict separation

### Why Queues Kill Velocity

Simple math proves why serializing work across specialized teams destroys velocity:

If engineers produce work requiring analysis at rate R, and analysts process at rate A, adding engineers without analysts creates nonlinear wait times. A few extra engineers can doom individual features to infinite queues—even when analysts aren't yet at full capacity.

> "We added a few engineers and wound up with a nonlinear increase in how long people need to wait before they can ship things."

**Poorly factored organizational boundaries create work.** Ticketing things can generate more work than talking to each other.

### The Security Team Anti-Pattern

One company tried to have the security team do all security remediation work. The hope: same total volume, fewer context switches.

The reality: Development teams unconcerned about security generate exponentially more security work. The wall between security and development created a humanitarian catastrophe of vulnerabilities.

### Parochialism and Ego: The Twin Dysfunctions

Every breakdown traces back to:
- **Parochialism** (positive spin: deference; negative: lack of curiosity, turf protection)
- **Ego** (positive spin: pride in work; negative: territoriality, dismissiveness of others)

The "brilliant jerk" problem isn't just about being a jerk—from a systemic perspective, driving other workers out reduces total throughput. **They aren't even brilliant. They're dumb.**

### The Miracle: Giving Away Power

At one company, after years of chaos, the engineering team achieved infrastructure stability and found themselves with free time and organizational permission.

**What they didn't do:**
- Rewrite things they hated (already tried this)
- Buy merch and strut

**The turning point:** A designer broke the build at night. The temptation was to rebuild fiefdoms—put a wall between designers and CSS, make designers "just design."

Instead, someone yolo'd giving the designer the deploy keys. Designers started shipping code. Engineering spent their free time building monitoring, test suites, and everything needed to make that safe.

> "The thing we were actually going to do was use our rare and precious organizational power, and the free time that came with it, to lift up other teams and make them more effective."

### Domain Experts, Not Domain Owners

The critical distinction:
- **Domain owner**: Responsible for all work in that domain, creating queues
- **Domain expert**: Focused on leveling everyone up, helping others work in the discipline

Everyone should be responsible for security. The security team helps everyone get there.

Same with frontend/backend—you want experts, but probably not people with "frontend" or "backend" in their title. Otherwise they build entire GraphQL monstrosities to avoid talking to each other.

### Sustaining the System

Building cooperative culture requires intentional investment:

**Expanding in-groups:** Psychological safety, experimentation, and curiosity exist within your in-group. Make people's in-groups larger through:
- **Bootcamps**: Force people to work on other teams occasionally
- **Hack weeks**: Cross-functional collaboration

**Slack time:** Domain experts need time devoted to helping others, not just their own work. The system needs sustaining energy.

### The Values

Two principles that made cooperation work:
1. **Elitism is poison**: "We do windows here. If a ditch needs digging, our tech leads will line up to dig it."
2. **Leave things better**: Strong expectation that you improve other people's stuff as you touch it. This makes people overjoyed to have you messing with their code.

### The Missing Ingredient: Permission

> "Mainly what I needed to do was give people the permission they needed to be curious, and to cooperate."

You can't grassroots this. **It's on leaders to value cooperation and reward curiosity.**

### Slack in the System

> "We don't let our machines run at 100% utilization. But we have a tendency to love our computers more than ourselves."

When you start skipping bootcamps, they die as a practice. Sustaining cooperation requires persistent commitment to slack.

### The Misery Myth

Most CEOs try to kill "feel-good programs" (bootcamps, hack weeks) but never try to end "feel-bad programs" (mandatory code review).

> "There's an industry instinct that misery gets results. I think this is mistaken. Misery is a shitty proxy metric for results."

### Key Quotes

> "Inside and outside of tech the world is rife with cult leaders who lack the gene for humility. At a certain genetic equilibrium, NPD is evolutionarily adaptive, so these people are out there. But in tech we've grown a tendency to see it as useful rather than parasitic. The industry believes in assholes."

> "Valuing others around you should not be a radical act, but that's where things are unfortunately."

> "Results are better if we can cooperate. And life is better without cult leaders."

### Connection to Other Principles

- **Organizational Legibility**: Role proliferation is excessive legibility—making work trackable at the cost of actual throughput
- **Stewardship Over Spotlight**: Lifting up other teams is stewardship; building fiefdoms is spotlight-seeking
- **AI, Agile, and Invisible Work**: Both critique how orgs measure visible outputs (features through queues) instead of systemic health
- **Game Theory at Work**: The "brilliant jerk" loses the long game—systemic throughput beats individual heroics
- **Transparent Leadership**: Domain experts who teach others vs. domain owners who hoard responsibility

## Defense/Offense Engineering: Team Structure for Small Teams

*Source: [Splitting engineering teams into defense and offense](https://www.greptile.com/blog/how-we-engineer) by Daksh (Greptile co-founder) - Added: 2026-01-18*

How a 4-person engineering team manages both customer support/bugs and ambitious feature work. The key insight: isolating interruptions to fewer people is more productive than distributing them "fairly."

### The Problem: Event-Driven vs. Long-Running Work

Paul Graham's "maker vs. manager schedule" addressed the meeting problem. Small startups face a different challenge: **customers**.

Without dedicated support teams and with immature products, engineers handle:
- Hotfixes
- Small features for large customers
- Customer navigation support

This creates two types of work at odds with each other:
- **Event-driven**: Support, bugs, customer requests (unpredictable, interrupting)
- **Long-running**: Ambitious projects, refactors, big features (requires focus, 1+ weeks)

### The Fortress Model

**Half the team (2 engineers)**: Work on long-running tasks in 2-4 week blocks. No support tickets, no bugs. Only job is focus on their big PR.

**Other half**: Protect the first two by catching all event-driven work. Maintain a "fortress" around the long-running processes.

**At the end of each cycle, swap.**

### Why Isolation Works

It takes only 1-2 short interruptions to dramatically reduce an engineer's daily output. The productivity loss from interruption is nonlinear—someone already handling support loses little additional productivity from more support. Someone in deep work loses enormously from even brief interruptions.

> "It's far more useful to isolate interruptions to a few people rather than disperse them to 'keep everyone productive'."

### Defense vs. Offense Mental Model

| Type | Purpose | Correlates With |
|------|---------|-----------------|
| **Defensive** (event-driven) | Maintain the product | Retention, customer satisfaction |
| **Offensive** (long-running) | Expand the product | New customer acquisition |

### Caveats

The author explicitly notes this isn't advice—it's an observation about a specific situation:
- Very small team (4 engineers)
- Fast-growing product
- Hyper-competitive, fast-evolving space
- Product "covered in warts" due to scope exceeding headcount

### Connection to Other Principles

- **Organizational Legibility**: The fortress model is deliberately illegible—it doesn't optimize for everyone being "busy"
- **Stewardship Over Spotlight**: Defense work is maintenance/stewardship; offense work creates new value
- **AI, Agile, and Invisible Work**: Support and maintenance are exactly the "invisible work" that Big Agile undervalues
- **Egoless Engineering**: Requires ego-free willingness to rotate into defense role, protecting teammates rather than building features

## Architecture Modernization: Estimates vs. Deadlines

*Source: [Architecture Modernization Execution: When did estimates turn into deadlines?](https://domainanalysis.io/p/architecture-modernization-execution) by DomainAnalysis.io - Added: 2026-01-19*

Legacy software modernization exposes the fundamental disconnect between how estimates work and how organizations treat them. The auto body repair analogy makes this viscerally clear.

### The Car Repair Analogy

When a car gets rear-ended:
1. Insurance adjuster estimates damage ($15,000)
2. Repair shop re-estimates ($18,000, 30 days)
3. Shop starts work, finds hidden damage (additional $20,000)
4. Shop submits supplemental repair for approval
5. Insurance decides: proceed or total loss

**The absurdity:** Imagine if the insurance company said "No, we'll only pay $18,000 because that was the original estimate." Reality doesn't work this way.

**But software does:** When modernization projects discover emergent complexity, organizations often react exactly this way—holding teams to original estimates despite fundamentally changed circumstances.

### Complex vs. Complicated Contexts (Cynefin Framework)

Using Snowden & Boone's "A Leader's Framework for Decision Making":

| Context | Characteristics | Appropriate Response |
|---------|-----------------|---------------------|
| **Complicated** | Expert analysis reveals best practice. Cause-effect discoverable through investigation. | Sense → Analyze → Respond |
| **Complex** | Cause-effect only visible in retrospect. No rulebook to follow. | Probe → Sense → Respond |

Auto repair is complicated—experts can analyze and determine best course of action.

Legacy modernization is complex—you try something, learn it doesn't work, uncover behaviors you never knew existed, and adapt. There's no fixed path, no rulebook.

### Emergent Solutions Are Normal

When modernizing applications:
- Look from outside → see obvious things → make initial estimate
- Start working → uncover additional complexity
- Hidden complexity = "damage you can't see yet"
- Requires approval to proceed at new cost

**Healthy environments ask:** How complex is this? What are the different solutions? What are the tradeoffs? Are there workarounds?

**Unhealthy environments ask:** Why didn't you see this earlier? Why is it taking so long? (Beholden to original estimates)

### To Proceed or Call It a Total Loss?

Just like insurance companies deciding whether to repair or total a car, organizations must sometimes abandon modernization projects when:
- Supplemental costs exceed remaining value
- Original business case no longer holds
- Simpler alternatives emerge

This is legitimate—not failure, just rational reassessment.

### Leadership in Complex Contexts

From Snowden & Boone:

> "Leaders who don't recognize that a complex domain requires a more experimental mode of management may become impatient when they don't seem to be achieving the results they were aiming for. They may also find it difficult to tolerate failure, an essential aspect of experimental understanding. If they try to overcontrol the organization, they will preempt the opportunity for informative patterns to emerge. Leaders who try to impose order in a complex context will fail. Still, those who set the stage, step back a bit, allow patterns to emerge, and determine which ones are desirable will succeed."

### Organizational Culture (Ron Westrum Model)

When curveballs hit, which culture does your organization adopt?

| Culture | Response to Messengers | Response to Failure |
|---------|----------------------|---------------------|
| **Power-Oriented** | Shot | Scapegoated |
| **Rule-Oriented** | Ignored | Justice (blame process) |
| **Performance-Oriented** | Trained | Inquiry (learn from it) |

### Key Insight

> "An estimate means an approximate of the actual."

The industry practice of treating estimates as deadlines—while knowing full well that emergent complexity is the norm—is a fundamental category error.

### Connection to Other Principles

- **Trillion-Dollar IT Failures**: Both argue that ignoring lessons and claiming "our project is different" leads to disaster
- **Product Bets Framework**: Shifts accountability from features/dates to value—avoids the estimate-as-deadline trap
- **Organizational Legibility**: The desire for predictable timelines (legibility) conflicts with the nature of complex work
- **The Cannae Problem**: Success with simple projects can blind organizations to the different dynamics of complex modernization

## The Best Product Engineering Org: Shore's Six Dimensions

*Source: [The Best Product Engineering Org in the World](https://www.jamesshore.com/v2/blog/2025/the-best-product-engineering-org-in-the-world) by James Shore - Added: 2026-01-18*

A comprehensive framework for building excellent engineering organizations, centered on six interconnected dimensions. "The best" isn't literal perfection but continuous, principled improvement across all dimensions simultaneously.

### 1. People

- **Hire for teamwork, peer leadership, and ownership** - not prestigious credentials
- **Career ladders emphasizing communication, collaboration, and XP skills** - technical excellence alone isn't enough
- **Senior coaches (1 per 11 engineers)** who model best practices alongside teams daily, not from a distance

### 2. Internal Quality

Combat "muda" (waste) through:
- **Simplified technology stacks** - fewer moving parts, easier maintenance
- **Fast feedback loops** - sub-5-second builds enable flow state
- **Test-driven development** - confidence to change code
- **Avoid big-bang rewrites** - improve systems incrementally as you work on features

### 3. Lovability

Shift from predictive project planning to product-based governance:
- **Build-measure-learn cycles** - validate hypotheses cheaply before committing resources
- **Test for failure early** - not just success
- **Strategy adaptation based on real data** - not roadmap commitments made months ago

### 4. Visibility

Build stakeholder trust through:
- **Transparency about capacity constraints** - don't hide the reality
- **Educated decision-making** - help stakeholders understand trade-offs
- **Honest forecasting based on historical data** - not false date promises
- **Muda tracking** - show percentage of time on value-add vs. waste

### 5. Agility

Enable tactical agility through:
- **Extreme Programming practices** - simultaneous design, coding, and testing
- **FaST (Fluid Scaling Technology)** - teams reorganize dynamically every few days around shifting priorities
- **Single queue of work per product line** - self-organizing teams tackle highest priority work

### 6. Profitability

Ensure products serve business needs:
- **Close collaboration with Sales, Marketing, Support, Finance**
- **Permanent improvement to company's growth trajectory** - not just feature delivery
- **Product bets framework** - accountability for estimated value, not features/dates

### The Integration

These six dimensions are interconnected:
- **People** enables all other dimensions—you need the right skills and mindset
- **Internal Quality** enables **Agility**—you can only move fast if the codebase allows it
- **Visibility** enables **Profitability**—leadership needs accurate information to make good bets
- **Lovability** validates **Profitability**—build-measure-learn proves whether bets are paying off

### Connection to Other Principles

- **Product Bets Framework** (earlier in this file): Detailed methodology for the "Profitability" dimension's accountability model
- **Muda Tracking**: Mentioned in Product Bets section—Shore uses this at OpenSesame to show capacity reality
- **Transparent Leadership**: The "Visibility" dimension aligns with transparent over servant leadership
- **Delete Your Tests**: The "Internal Quality" dimension requires tests that enable change, not hinder it

## Effective Delegation: IC to Supervisor Transition

*Source: [How to Delegate Effectively as Your Responsibility Grows](https://www.hitsubscribe.com/how-to-delegate-effectively-as-your-responsibility-grows/) by Erik Dietrich - Added: 2026-01-18*

A practical framework for moving from "IC-style delegation" (micromanagement) to scalable supervisor-style delegation.

### Delegation by Org Level

| Level | Accountability Given | Deliverable Expected |
|-------|---------------------|---------------------|
| Executive | Organizational goal | Plan + overseeing execution |
| Middle Manager | Execute the plan | Judgment-based execution in fluid environment |
| Supervisor | KPIs | Tasks that generate KPIs |
| IC/Micromanager | Nothing | Tasks executed to exact specification |

**Key insight**: Successful delegation involves both tasks AND accountability. IC-style delegation cedes only tasks while gripping accountability—that's micromanagement.

### When IC-Style Delegation (Micromanagement) Is Appropriate

1. No contact with inexperienced executor (e.g., appliance manuals)
2. High-stakes, rarely-executed tasks (e.g., offboarding senior employees)
3. Endless turnover in executing role
4. Dictating to literal systems (programming computers)

Note: These situations are philosophically suboptimal—usually placeholders until automation or elimination occurs.

**Why programmers struggle to delegate**: They've spent careers learning to be maximally precise for literal interpreters (computers). That skill is counterproductive with humans.

### Problems with Pervasive Micromanagement

1. **Scale crushes you** - Collaborating heavily on all reports' work means team of 3 doesn't deliver 3x output
2. **Innovation becomes terrifying** - Detailed runbooks calcify processes; any variance triggers manual updates
3. **Permanent juniority** - Learned helplessness from "can't operate without guidance"
4. **Bad results anyway** - Knowledge work requires judgment; lengthy rote processes fail inevitably
5. **Malicious compliance** - Eventually, people follow flawed instructions exactly to prove a point
6. **Talented people quit** - Only those happy to not think will stay

### Self-Assessment: Signs You're Micromanaging

- Delegation takes form of numbered step lists
- Instructions heavy on "how," light on "what," silent on "why"
- Can't answer "What decisions are your reports empowered to make?"
- Everything unusual comes as "What should we do?"
- Constantly updating documentation reports live in
- Increased report workload = increased your workload
- Evaluate people on prompt task completion, not outcomes delivered
- Secretly measure people by "how reliably they do what I would have done"

### Moving Toward Effective Delegation

**1. "I wouldn't have done that, and that's okay"**
Accept different approaches. Your success as IC wasn't from optimal task execution—it was broader. Efficiency lost from "suboptimal" approaches is dwarfed by micromanagement inefficiency.

**2. Differentiate What and How**
Review everything you're about to hand off. Identify which parts define the outcome (what) vs. define the method (how). Just become aware initially.

**3. Define success criteria and explain Why**
"We're doing X to enable Y. Success means Z happens." This lets people work however they're productive AND propose alternatives.

**4. Create safe failure zones**
If mistakes in a process are non-catastrophic, create checkpoints (e.g., "formatting sanity checker" before publish). Now people can experiment freely in the safe zone.

**5. Set caps on requirements**
If your checklist has 74 items, nobody will remember them all. When cognitive burden grows too high, rethink the process wholesale—back to what/why.

**6. Favor reference material over runbooks**
Instruction manuals are for novices. Reference cheat sheets enable experienced people. Documentation should enable, not order around.

**7. Favor checklists over instructions**
Checklists are "what" (verify optimization happened). Instructions are "how" (do optimization this way). Checklists trigger self-quality-control or surface training needs.

**8. Differentiate training from standing instructions**
Screenshot-heavy walkthroughs are great for onboarding. Expecting people to memorize and follow them forever is micromanagement. Make purpose clear.

**9. Ask "Why are you asking me this?"**
(Follow with: "I'm asking literally, not suggesting you're wrong to ask.")

Two answers:
- **Empowerment gap**: You haven't empowered them to decide. Fix by defining thresholds (e.g., "anything under $X, do what makes client happy").
- **Confidence gap**: They lack knowledge or fear responsibility. Fix by providing more context.

### The Philosophical Foundation

> "Hire good people and trust them."

- Overwhelming majority operate in good faith
- People pleasantly surprise you when trusted and empowered
- When someone doesn't, solid delegation exposes shortcomings that micromanagement hides
- Reports won't do things your way, and will sometimes be wrong
- Your life will be better for it

### Connection to Other Principles

- **Transparent Leadership** (earlier in this file): Both reject over-protection in favor of developing people
- **Stewardship Over Spotlight**: Long-term trust-building vs. short-term control
- **"Being right is cheap"** (Addy Osmani): Winning debates creates silent resistance; alignment > correctness

## The Caucus Problem and Meeting Moderation

*Source: [How do we make remote meetings not suck?](https://chelseatroy.com/2018/04/05/how-do-we-make-remote-meetings-not-suck/) by Chelsea Troy - Added: 2026-01-18*

### The Core Problem

Remote meetings suck because they exacerbate the **caucus problem**—not because of technical issues. The caucus problem affects all meetings, but remoteness makes it universal rather than isolated.

**What is a caucus?** An unmoderated discussion where the floor goes to whoever takes it. This rewards:
- Jumping in and interrupting
- Speaking loudly and confidently
- Having low inhibition

This penalizes:
- Listening carefully before responding
- Composing thoughtful answers
- Having any hesitation

### Why Common Solutions Fail

**"One-remote, all-remote" doesn't solve it**: Everyone dialing in separately equalizes the *frustration* but not the *participation*. You're still back to caucus dynamics determining who contributes.

**Limiting remote meetings doesn't solve it**: Colocated meetings still have the caucus problem. You're just excluding fewer people from problems that already exclude many.

**Telling people not to interrupt doesn't solve it**: You're addressing an individual symptom, not the systemic incentive structure. The meeting still rewards "jumping in." Per Steven Kerr's "On the Folly of Rewarding A While Hoping for B"—if you reward one behavior while hoping for a different behavior, you'll get the rewarded behavior.

### The Solution: Moderated Meetings

Appoint a **moderator** for each discussion. A moderator sits between:
- **Chair** (Robert's Rules): Enforces formal rules, doesn't participate in discussion
- **Facilitator**: Makes up rules, often participates and editorializes

A moderator combines informal style with chair-like non-involvement in the topic itself.

**Moderator's one job**: Give people the opportunity to listen by safeguarding their opportunities to speak.

### Moderator Techniques

1. **Share agenda beforehand** - So people can prepare what to say
2. **Keep agenda visible during meeting** - No surprises about direction
3. **Maintain speaker list** - Ask who wants to talk, add them to list
4. **Collect names via chat for remote meetings** - Most inclusive method
5. **Stop interrupters** - Calmly hand floor back to previous speaker
6. **Actively solicit quiet voices** - "This side hasn't spoken much. Anyone want to comment?" or "Maria, I know you worked on this. Any thoughts?"
7. **Optional time limits** - Remaining time can go to questions if speaker chooses
8. **Manage overflow** - Extend time or schedule separate meeting for deep topics

### Key Insight: Structure Is Always Present

Human relationships always have structure. Without formal rules, we follow emergent social rules. Caucus rules are emergent rules that give more influence to those who already have influence.

Since there will be rules anyway, you might as well have rules that achieve the meeting's goal: gathering valuable contributions from all attendees.

### Self-Moderation Emerges

With good moderation, groups begin to self-moderate:
- Speakers explicitly yield to next person: "That's what I think—I know Sarah has a great perspective on this"
- Group members stop interrupters: "Let Kat finish her thought"
- Moderator does less and less over time

### Meetings That Already Have Moderation

**Iteration planning meetings**: Product manager controls the floor. Engineers ask questions of PM, not each other. Clear procedure for who speaks when. These work seamlessly for remote attendees.

**Retrospectives**: Moderator (often newest team member) goes through items. Person who wrote item explains, brief conversation, action item if needed, move on. Clear procedure that everyone follows.

### The Inclusion Connection

The caucus problem is an inclusion problem. It systematically excludes potential contributors. Moderation isn't "formal" or "restrictive"—it feels liberating to those with lower caucus scores who previously had to compete for speaking opportunities.

The tradeoff of more restriction for high-caucus-score individuals is worth the additional perspective you gain in decision-making.

## Decision-Making Culture: Debate vs. Directive

*Source: [HN Discussion on Engineering Cultures](https://news.ycombinator.com/item?id=39112848) - Added: 2026-01-19*

### Common Failure Modes

**1. Unclear Decision Authority**
- Growing companies reach a point where product managers, program managers, engineers, engineering managers, and stakeholders all exist—but nobody can identify who actually makes decisions
- Weak leadership pushes "we all have to work together" without clarifying roles
- Consensus-seeking leads to endless debate and progress slows to a crawl

**2. Process-Obsessed Product Management**
- PMs view themselves as "facilitators" who get others to figure out what to build
- Produces meetings, slide decks, Figma charts, process documents, Notion pages, summary emails
- Afraid to be prescriptive—only asks questions and provides frameworks
- Never actually concludes what should be built

### The Critical Principle

> "A critical piece of avoiding endless debate is to know who makes the final decision and how it gets made. Consensus-seeking leads to endless debate."

### Balancing Act

The tension isn't between "debate everything" vs. "just tell me what to build"—it's between:
- **Structured decision-making** with clear ownership
- **vs. Democratic process** that values all input equally

Successful teams need:
1. **Clear decision-makers** for accountability and speed
2. **Welcome feedback** without letting it block progress
3. **Prescriptive guidance** from PMs when needed, not just facilitation

### Connection to Other Principles

This complements:
- **The Caucus Problem** (above): Without moderation/clear process, loudest voices dominate
- **Stewardship Over Spotlight**: Clear ownership enables delegation, not micromanagement
- **"Being right is cheap"**: Once decision is made, alignment > continuing to debate

## The Power of Vulnerability in Engineering Teams

*Source: [Death to the Invincible Engineer](https://juraj.hashnode.dev/death-to-the-invincible-engineer) by Juraj Malenica - Added: 2026-01-19*

> "No vulnerability, no creativity. No tolerance for failure, no innovation. It is that simple. If you're not willing to fail, you can't innovate. If you're not willing to build a vulnerable culture, you can't create." — Brené Brown

### The Two Types of Engineers

1. Those who believe **vulnerability is weakness** that will be used against them
2. Those who **stay vulnerable and authentic** despite past experiences, betting on long-term payoff

### The "Me Against the World" Trap

Current market conditions encourage defensive behavior:
- Average software engineer tenure: 2 years per company
- Remote work enables multiple simultaneous positions
- Mass layoffs with little notice

This creates a mentality of:
- Constant competition for superiority and recognition
- Reduced meaningful connections
- False sense of security through emotional shutdown
- Paranoia and inability to trust

**Personal Pattern**: Early career coping mechanism = shutting down emotionally when frustrated or ashamed. This prevents judgment but also prevents growth.

**The Wake-Up Call**: A mentor pointed out the unsustainability of bottling emotions. The choice: adapt instincts and show real vulnerability, or continue shutting down.

**Result**: Staying authentic and honest gives power to words and helps connect with people more easily.

### Vulnerability Builds Trust in Teams

**Great companies measure team output, not individual output**. This:
- Incentivizes collaboration
- Disrupts "me vs. world" mentality
- Shifts focus to collective success

**Trust is the glue** that holds teams together when:
- Communication breaks down
- People have bad days
- Frustrations arise
- Misunderstandings happen

With trust, team members:
- Give benefit of the doubt
- Communicate honestly about problems
- Assume good intent

### Addressing Toxic Team Members

**Critical principle**: Address toxic behavior directly, **regardless of individual brilliance**.

Toxicity affects:
- Communication quality
- Cooperation levels
- Delivery speed
- Overall team spirit

**First step**: Direct, honest conversation about observations and feelings.

**Core belief**: People are inherently good. Toxicity comes from:
- Unaddressed past issues
- Personal insecurities

**The scary conversation**: Talking privately about negative feelings is incredibly hard, especially with senior peers. But it can be:
- Long and intense
- Honest and constructive
- Non-judgmental
- Relationship-building

**Possible outcomes**:
1. **Best case**: Find common language, shift to "mending relationships," re-establish trust
2. **Worst case**: It doesn't work out, but you gave it your best effort

### Building a Culture of Vulnerability

**What vulnerability enables**:
- Authenticity
- Speaking up without fear
- Making suggestions
- Agreeing and disagreeing openly
- Admitting mistakes
- Learning through sharing
- Genuine team connections

**How to create it**:
1. **Lead by example** - Don't compromise on honesty, embrace uncomfortable conversations
2. **Educate** - Share benefits and address the "weakness" misconception
3. **Create safety** - People must care about one another
4. **Focus on learning over outcomes**

**You cannot enforce vulnerability** - it would backfire. It must emerge from safety.

### Filtering for Cultural Fit Through Vulnerability

**Startup challenges**: Long hours, lower pay, lacking documentation, semi-defined processes.

**Interview strategy**: Be completely open about downsides. Emphasize challenges.

**Results**:
- Best candidates see challenges as growth/impact opportunities
- Most candidates say "no thank you"
- This is OK—saves everyone time
- Might miss some great engineers, but cultural fit matters more

**Real-world test**: During vacation, team had 2 production outages. Without leader present, they:
- Detected issues
- Alerted clients
- Controlled damage
- Fixed mistakes
- Prevented recurrence
- Supported each other
- No shaming or finger-pointing
- People spoke up about failures instead of hiding

**This wouldn't happen** if sole priority was engineering excellence over cultural fit.

### Being a Champion of Vulnerability

**If you lack high influence**, you can't change:
- Entire company culture
- Hiring processes
- Core principles

**But you CAN influence your immediate team**:
- Share feelings and ideas honestly
- Talk openly about improvements
- Listen actively
- Be vulnerable yourself
- Model behavior for others

### The Two Paths

1. **Feel alone and threatened** by others (invincible engineer)
2. **Treat work as net-positive game** (vulnerable leader)

**Vulnerability demonstrates**:
- Strength of character
- Self-awareness
- Ability to build trust and connection
- Empathy for struggling colleagues

**The foundation of great teams**: Trust, connection, empathy, and vulnerability.

**For leaders**: Create environments where people feel:
- Appreciated
- Included
- Relied upon
- Safe to fail and learn

**For individual contributors**: Find places where:
- Your potential is cherished
- Your passion is valued
- Failures are learning opportunities

**The payoff**: Requires courage and grit to be vulnerable. Everyone knows you for your authentic, honest self. This pays off long-term.

**Acting invincible just doesn't pay off.**

### Recommended Reading

*Daring Greatly* by Brené Brown - Helps understand vulnerability patterns in everyday life
