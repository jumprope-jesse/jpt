# Software Quality Philosophy

Perspectives on what quality means in software, organizational responsibility for it, and how it degrades over time.

---

## Death by a Thousand Cuts: How to Think About Software Quality

*Source: https://www.evalapply.org/posts/how-to-not-die-by-a-thousand-cuts/index.html - Added: 2026-01-19*

A philosophical take on software quality that frames it as an organizational responsibility, not just a QA function. Quality is "the experience of the process"—performing it with grace and leaving things better than found.

### The Nature of Software

Software is unique among machines:
- Pure concept, infinitely malleable and mutable
- Must change indefinitely because the world it serves changes
- Strong feedback loop: software changes the world fast, forcing software to change faster

Some "finished" software exists (Unix tools, ZeroMQ), but most must evolve. Emacs has evolved non-stop since 1976.

### Who Is Responsible for Quality?

Not just "QA." Consider scenarios where customers perceive "bad quality":
- App framework is performant, but app bombs
- Feature works exactly as designed, but people can't use it right
- Company ships a product customers never wanted
- Huge do-or-die update misbehaves and can't be rolled back
- Service fails to scale—turns out there were no benchmarks
- Deployment breaks production due to bad config
- Data leaks to unintended users, CEO blames a DevOps engineer
- Several-hour glitch goes unmonitored, causing data corruption

Each scenario involves different functions. The job of assuring quality belongs to **every function** involved in the product's life.

### The Linear Workflow Problem

Traditional workflows (Analysis → Product → Design → Dev → "QA" → Prod) have compounding risk:

```
                                                              ^   Feedback
 Analysis -> Product -> UX/Design -> Dev -> "QA" ->  Prod --./--> arrives
                                                           /      too late
                                                         /-
                                                       /-
                                                     /- ^
                                                  /--   | Price of fixing
                                               /--      | errors and
                                           /---   ^     | corner cuts.
                                       /---       |     |
                                  /----   ^       |     | ~ OR ~
                             /----        |       |     | Compounding
                     /------   ^          |       |     | software debt.
            /--------          |          |       |     |
  ----------      ^            |          |       |     | ~ OR ~
   ^              |            |          |       |     | Increasing odds
   |              |            |          |       |     | of being wrong.
---+--------------+------------+----------+-------+-----+---------------->
                            Time, Complexity, Sunk costs
```

Key insights:
- All risk is front-loaded at Analysis—if that's wrong, everything's wrong
- Linear workflow has compounding debt/risk profile
- Tasking a single group with "QA" maximizes odds of being too wrong too late
- Small batches don't fix this if the flow is still strictly linear
- **The risk is rooted in feedback delays.** Weak signals die when delivery pressure is high.

### The Death by a Thousand Cuts Metaphor

Every hotfix is a cut. Every complaint is a cut. Every crash is a cut. Every outage is a cut. Corner-cuts that added up—slowly as band-aids, then stitches and casts, then suddenly as gangrene.

### How to Destroy Quality

- Mislabel Testing as "Quality Assurance"
- Make all teams "responsible for QA" (really: make the least experienced people do it)
- Create blame culture
- Have designers, developers, testers work on priorities set by others
- Set up incentives that make departments compete
- Normalize deviance

(See also: CIA's Simple Sabotage Field Manual, part 11)

### How to Create Quality

No formula exists. High-quality products come from high-quality organization-wide systems and culture. No "best practice" or methodology can fix broken systems and people.

The way must be co-evolved:
- By collaborative stakeholders spread across the org
- Appropriate to the org's unique context
- Along with customers, partners, and the ecosystem

**The first skill: learn to suffer constructively.** "Why are we suffering?" is a valuable discussion because constructive suffering yields quality outcomes. The path to recovery is filled with discomfort before it gets easier.

### Recommended Resources

**Systems:**
- *Thinking in Systems* (Donella Meadows)

**Software Complexity:**
- Out of The Tar Pit
- No Silver Bullet
- The Architecture of Complexity
- Simple made Easy (Rich Hickey)

**Failure:**
- How Complex Systems Fail
- Human Error
- Safety Differently

**Doing Together:**
- The Mythical Man Month
- The Checklist Manifesto
- Critical Chain Project Management
- The Principles of Product Development Flow
- Mature Optimization

**Oneself:**
- On Being a Senior Engineer
- How to Be A Programmer
- Better: A Surgeon's Notes on Performance
- Hammock Driven Development (Rich Hickey)

### Related

- [[software-project-failures]] - Case studies of quality failures at organizational scale
- [[programming-philosophy]] - Individual craft perspectives
- [[engineering-leadership-principles]] - Organizational accountability themes
