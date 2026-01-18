# Software Project Failures: Patterns and Prevention

## Source
- [Software Failures and IT Management's Repeated Mistakes](https://spectrum.ieee.org/it-management-software-failures) - IEEE Spectrum, November 2025
- Author: Robert Charette (IEEE Spectrum contributor since 2005)
- Added: 2026-01-18

## The Scale of the Problem

- Global IT spending tripled since 2005: $1.7T to $5.6T (constant 2025 dollars)
- Software success rates have NOT markedly improved despite increased spending
- CISQ estimates for US in 2022:
  - $1.81 trillion: annual cost of operational software failures
  - $260 billion: spent on software-development failures
  - $520+ billion: annual legacy system support costs
  - 70-75% of IT budgets devoted to legacy maintenance
- IT projects are the riskiest from a cost perspective (per Bent Flyvbjerg, Oxford)

## Why AI Won't Save Us

"For those hoping AI software tools and coding copilots will quickly make large-scale IT software projects successful, forget about it."

Hard limits on AI's ability to manage:
- Systems engineering trade-offs
- Project and financial management intersections
- Organizational politics
- Rational decision-making (rare in IT projects)

Key insight: "IT projects suffer from enough management hallucinations and delusions without AI adding to them."

## The Recurring Drivers of Failure

From Stephen Andriole (Villanova):
- Failures of human imagination
- Unrealistic or unarticulated project goals
- Inability to handle project complexity
- Unmanaged risks
- Poor requirements gathering
- Inadequate testing
- Lack of skilled personnel
- Organizational politics

Most failures involve **avoidable, known failure-inducing factors** documented for decades. Unique failures are rare.

## Case Studies

### Canadian Phoenix Payroll System (2016)
- Budget: CA $310 million
- Attempted: 80,000 pay rules, 105 collective agreements, 34 HR interfaces across 101 agencies
- Mistakes:
  - Bid 60% below vendor's estimate
  - Removed/deferred critical functions
  - Reduced testing
  - Forewent pilot testing
- Results:
  - 70% of 430,000 employees experienced paycheck errors over 9 years
  - 349,000+ unresolved errors by March 2025
  - Total cost: CA $5.1B+ ($3.6B USD)
  - At least one documented suicide from financial stress
  - **Second payroll failure**—ignored lessons from 1995 attempt

Auditor General: "An incomprehensible failure of project management and oversight."

### UK Post Office Horizon System (1999-present)
- Fujitsu EPOS system riddled with hidden software errors
- 3,500 branch managers falsely accused of fraud/theft
- 900 convicted, 236 incarcerated
- ~350 accused died before receiving compensation (13+ by suicide)
- Took until 2015 for public to learn something was wrong
- ITV miniseries required to finally expose scandal
- Replacement attempts in 2016 and 2021 both failed
- System still in use; £410M new system planned

Failures included:
- Buggy middleware foundation
- Uncontrolled scope creep
- Missing development processes
- Inadequate testing
- Hostile leadership toward questioning postmasters
- Active suppression of exculpatory evidence
- "World-class cover-up"

### Other Notable Failures Mentioned
- Michigan MiDAS unemployment system: Falsely accused tens of thousands of fraud
- Australia Centrelink Robodebt: Falsely accused hundreds of thousands of welfare fraud
- Minnesota MNLARS (2019): $100M total after $41M plan, deemed "too hard to fix"
- Australia business register modernization: Cancelled at AU $530M spent, projected to cost AU $2.8B
- Louisiana OMV: 50-year-old mainframe, governor declared state of emergency
- Lidl SAP: €500M ERP abandoned after 3 years, reverted to legacy

## The Failure Déjà Vu Problem

> "IT project managers routinely claim that their project is somehow different or unique and, thus, lessons from previous failures are irrelevant. That is the excuse of the arrogant."

Phoenix managers ignored documented reasons for the 1995 failure because "lessons were not applicable"—then repeated them.

> "We learn more from failure than from success, but repeated failures are damn expensive."

## Agile/DevOps Aren't Silver Bullets

Claims of 65% Agile failure rates and 90% DevOps initiatives failing to meet expectations. Success requires:
- Consistent leadership
- Organizational discipline
- Patience
- Investment in training
- Culture change

"Given the historic lack of organizational resolve to instill proven practices, it is not surprising that novel approaches...will also frequently fall short."

## The Algorithmic Decision-Making Risk

MiDAS and Robodebt examples show what happens when:
- Questionable algorithms deployed without human oversight
- Officials trust systems blindly
- Errors are downplayed when discovered
- Compensation is fought against

> "If this behavior happens in government organizations, does anyone think profit-driven companies whose AI-driven systems go wrong are going to act any better?"

Recommendation: Transparency and accountability for all automated systems should become a fundamental, global human right.

## What Would Actually Help

### Organizational Requirements
- Honest accounting of risks (not rationalization)
- Healthy skepticism of vendor promises
- Ethical considerations built in from the start
- Senior management treating software with the respect it deserves

### Essential Questions Before Starting
1. What do you know, what should you know, and how big is the gap?
2. If no one has successfully built this with your schedule/budget/functionality, why do you think you can?

### Human-Centered Approach
- Anticipate where systems can go wrong
- Eliminate those situations where possible
- Build in mitigation for inevitable failures
- Consider financial and emotional distress on end users

### The Accountability Gap
Financial incentives reward building flawed software. The industry has:
- Addiction to "failure porn"
- Lack of accountability for foolish management decisions
- Resistance to software liability laws
- Resistance to professional licensing

## Key Quotes

> "Software is inherently fragile; building complex, secure, and resilient software systems is difficult, detailed, and time-consuming."

> "Anyone can make a mistake, but only an idiot persists in his error." —Cicero

> "It is well known that honesty, skepticism, and ethics are essential to achieving project success, yet they are often absent."

> "We have paleolithic emotions; medieval institutions; and god-like technology. And it is terrifically dangerous." —E.O. Wilson (also in engineering-leadership-principles.md)

## Related
- [[engineering-leadership-principles]] - Complements the executive communication and accountability themes
- E.O. Wilson quote appears in both files—the paleolithic emotions/god-like technology warning
