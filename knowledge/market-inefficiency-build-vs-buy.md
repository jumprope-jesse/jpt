# Market Inefficiency and the Build vs. Buy Decision

*Source: [Why is it so hard to buy things that work well?](https://danluu.com/nothing-works/) by Dan Luu - Added: 2026-01-18*

A comprehensive analysis of why markets often fail to produce good products, and why "build" frequently beats "buy" even when conventional wisdom says otherwise.

## The Efficient Market Myth

The cocktail party version of efficient markets: "If it were possible for products to be better, someone would've outcompeted and done it already."

This is demonstrably false. Inefficiencies persist for decades because:
- Information asymmetry (consumers can't evaluate quality)
- No mechanism to directly convert knowledge of inefficiency into profit
- Companies can win through marketing instead of quality

**Example:** People migrated from iPhones to Android due to Apple PR snafus, believing iPhones were terrible at something when they were actually *better* at it than Android. Many got a device better suited to them anyway—but for the wrong reasons. Decisions driven by marketing, not information.

## The Lemons Problem (Beyond Cars)

Economists debate whether cars are a "market for lemons." But the real issue: there's maybe one car manufacturer (Volvo) that seriously tries to make structurally safe cars beyond what standards bodies test. Consumers can't tell the difference, so most manufacturers optimize for passing tests rather than actual safety.

> "That's a market for lemons, as is nearly every other consumer and B2B market."

The same applies to:
- Home renovation contractors (grievous errors are common)
- Accountants (brand-name firms have higher error rates at higher prices)
- Air conditioners (experts give bad advice about their own field)
- Software products (design flaws that make them fundamentally broken)

## The Build vs. Buy Reality

### The Conventional Wisdom

"Focus on core competencies and outsource everything else." Repeated by Joel Spolsky, Gene Kim, Will Larson, Camille Fournier, etc.

### The Reality

At mid-sized tech companies, you often need in-house expertise far outside any "core competency":
- Kernel expertise that consultants can't provide
- Custom tooling that saves millions
- In-house shipping because commercial shippers don't actually deliver

**Ben Kuhn's (Wave CTO) key insight:** One of his biggest mistakes was not putting more effort into vendor selection and not considering in-house solutions sooner. Even the "consensus best product" from the "leading firm" often doesn't work by design.

### Case Study: Data Sync Product

A leading data sync company's main offering (Postgres to Snowflake):
- Loses data
- Duplicates data
- Corrupts data

**Root cause:** The design relies on data sources being able to seek backwards on changelogs. Postgres can't do this. The product has a fundamental design flaw that means it literally cannot work.

This isn't different from MongoDB's early data loss issues—except there's no Kyle Kingsbury publishing Jepsen tests for data sync products. Without that pressure, most software products basically don't work.

### The Wafer Saw Example

At a chip startup, having in-house capability to go from wafer to working chip seemed absurd—the equipment and expertise is idle 99% of the time. Classic case for outsourcing.

But pricing it out: cheaper to do in-house even at 1% utilization, and you get faster turnaround enabling faster shipping. Competitors who outsourced got slower, less reliable service at higher cost.

### The Simulator Example

A custom simulator maintained by one person saved millions per year in licensing costs. "You might think that if a single person can create or maintain a tool worth millions, competitors would do the same thing." But they didn't.

## The Cultural Factor

### The "Focus on Core Competencies" Culture Shift

The author watched a company decide to abandon custom software for infrastructure. Leadership didn't mandate specific migrations. Instead:
- People bought into the idea
- Migrations were justified for "vaguely plausible sounding reasons that weren't connected to reality"
- Moving to open source "to save money" when the new system was less efficient
- Cost savings from "shrinking the team" dominated by increased operational costs

**Key insight:** Once people absorbed the cultural idea, migrations were driven by that idea, not technical reasons.

### Why Selection Pressure on Companies Is Weak

Technical decisions made without serious technical consideration are pervasive. Successful companies often route around making products that work:

> "Mongo's decision to loudly repeat demonstrably bogus performance claims and making demonstrably false correctness claims was, from a business standpoint, superior to focusing on actual correctness and performance."

### The Role of "Unusually Unreasonable" People

From Yossi Kreinin: some people refuse to accept orders from above and push back on issues despite the system being aligned against them.

**Kyle Kingsbury (Jepsen):** Spent years publishing correctness tests, patiently responding to bogus claims, enduring personal attacks. Eventually Jepsen brought in good money—but only after years of below-market rates on uncertain work.

A system that requires someone like Kyle to take a stand before firms will put effort into correctness instead of "correctness marketing" is going to produce a lot of marketing without substance.

**Volvo:** The one car manufacturer that tried to produce safety beyond what tests measure. Fared so poorly they had to move upmarket to become a niche luxury automaker. "Safety isn't something consumers are really interested in despite car accidents being a leading cause of death."

### The Cultural Expectations Problem

Americans often think their cultural expectations are laws of nature:
- "You can't leave a laptop unattended in a cafe" (but you can in Korea)
- "You can't stop the spread of covid" (but Taiwan and Vietnam did)
- "You can't trust vendors to follow through" (but in some cultures you can)

The inability to trust other firms is a *cultural* problem, not an inherent one. If you can't trust other firms, you frequently have no choice but to build in-house if you want things to work.

### The Intra-Firm Trust Problem

A director's response when the author complained about a VP breaking a promise:

> "Unless you get it in a contract, it wasn't a promise."

The rate at which VPs lie is high enough that only legally binding commitments have meaning. This creates the same empire-building dynamics as inter-firm distrust—teams bring things in-house because they can't trust other teams.

**Intel and Google under Andy Grove and Eric Schmidt:** Leadership enforced trustworthiness. Stamping out dishonesty was a major reason for success. When leadership changed and stopped enforcing honesty, standard BigCo culture seeped in—but it wasn't inevitable.

## The Downsides of Build

Building isn't a panacea:
- Internal designs can be just as broken as vendor products
- Dysfunctional teams in dysfunctional orgs make products that don't work
- Companies that kill "duplicate" projects to avoid inefficiency create internal monopolies with the same problems as external vendors

**Steve Jobs:** "The company does a great job, the press writes about it, the marketing people use the press clippings... Product people get driven out by the sales and marketing people because the products become less relevant."

This applies at the team level too. Without competition, internal products rot.

## Key Quotes

On markets:
> "In capital markets, we don't need all that many informed participants to think that some form of the efficient market hypothesis holds... But with the job market examples, even though firms can take advantage of mispriced labor, inefficiencies can persist for decades."

On trust:
> "If you can't trust other firms, you frequently don't have a choice with respect to bringing things in house if you want them to work."

On culture:
> "It's often difficult to see how absurd a system is from the inside."

On quality:
> "It's rare that people are willing to expend a significant amount of personal capital to do the right thing, whatever that means to someone, but it's even rarer that the leadership of a firm will make that choice."

## Connections

- **Relates to Organizational Legibility** (engineering-leadership-principles.md): The cultural expectation that everything should be legible and contractual is itself a cultural choice, not a law of nature
- **Relates to Do The Simplest Thing** (programming-philosophy.md): Sometimes the simple thing is to build it yourself rather than fight with broken vendor products
- **Relates to Software Project Failures**: "Buy" decisions fail when buyers can't evaluate quality—the expert-layman problem at the organizational level
- **Relates to The Cannae Problem**: Organizations that buy into "focus on core competencies" orthodoxy can't see when it's leading them to disaster
- **Relates to Stewardship Over Spotlight**: The "unusually unreasonable" individuals who produce quality (Kyle Kingsbury, Volvo engineers) often operate without recognition

## Practical Implications

1. **Don't assume consensus best products work** - Even leading vendors' main offerings can have fundamental design flaws
2. **Price out in-house vs. buy honestly** - Include the cost of fighting with vendors, contract negotiation, and degraded service
3. **Recognize cultural factors** - Your assumptions about what's possible are often cultural, not universal
4. **Value "unusually unreasonable" people** - They're the ones who produce things that actually work
5. **Be skeptical of "focus on core competencies"** - It's often a cultural meme, not a reasoned decision
