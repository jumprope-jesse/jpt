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

## Related
- Author: Sarah Chen (VP of Engineering at Acme Corp) - see people/sarah-chen.md
- Author: Anna Shipman (CTO at Kooth) - guest writer on Refactoring.fm
- Author: Addy Osmani - Google engineer, 14 years at Google
- Author: Linus Akesson - programmer, writer
- Author: Lalit Maganti - Senior Staff Engineer at Google, Perfetto/trace tooling
- See also: [[software-project-failures]] for full case studies (Phoenix, Horizon, etc.)
