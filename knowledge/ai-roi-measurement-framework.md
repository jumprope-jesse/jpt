# AI ROI Measurement Framework: Initial Thoughts

*Prepared for discussion with Randy - January 2026*

## Context

Per the 1/16 leadership meeting: JumpRope has approval for a trial quarter of AI tools ($1-2K/month ceiling) with the goal of replacing offshore developer needs. Randy has oversight, and we need a framework to measure effectiveness.

The stated thesis: AI tools can provide better predictability than offshore developers. The challenge: "All the people talking at conferences saying they 10x themselves - you gotta have a rigorous way to measure that."

---

## Why This Is Hard

### The Productivity Measurement Problem

James Shore (VP Engineering, formerly ThoughtWorks) summarizes the core issue: "Software productivity is famously unmeasurable." Kent Beck and Martin Fowler agree.

The naive approaches fail:
- **Lines of code**: Penalizes clean, simple solutions
- **Story points**: Inflates over time; easy to game
- **Velocity**: Only measures output, not value
- **Hours worked**: Obvious problems

AI makes this worse because:
1. Speed gains may not translate to value delivered
2. AI output requires human review (new bottleneck)
3. Technical debt from AI code may be invisible initially
4. Easy tasks get automated; hard judgment calls remain

### The Ironies of Automation

Bainbridge's 1983 research (still relevant) warns:
- **Deskilling**: People who stop coding lose ability to evaluate AI output
- **Monitoring fatigue**: Can't stay vigilant when AI mostly works correctly
- **Next-generation problem**: New hires who never coded can't supervise AI

We're early enough that these aren't problems yet - but they will be.

---

## Proposed Measurement Approaches

### Tier 1: Direct Cost Comparison (Easy but Incomplete)

| Metric | How to Measure |
|--------|---------------|
| Tool cost vs offshore cost | Monthly spend comparison |
| Tasks completed solo vs tasks requiring offshore | Count of tickets/PRs |
| Time-to-completion | Story start to deploy |

**Pros**: Easy to track, speaks to CFO concerns
**Cons**: Doesn't measure quality, technical debt, or learning

### Tier 2: Value-Add Capacity (Shore's Approach)

Measure the **percentage of engineering time spent on value-add activities** vs. muda (waste):

| Category | Value-Add? |
|----------|-----------|
| New feature development | Yes |
| Bug fixes | No (fixing past work) |
| Maintenance/upgrades | No (necessary but not new value) |
| Incident response | No |
| Documentation | Depends |
| AI-generated rework | No |

Track this over time. If AI genuinely helps, value-add capacity should increase.

**Pros**: Focuses on real output, sparks right conversations
**Cons**: Easy to game; requires honest categorization

### Tier 3: Judgment/Review Bottleneck (The Real Constraint)

As AI generates more code, humans become the bottleneck for judgment calls. Track:

| Metric | What It Shows |
|--------|--------------|
| PR review queue depth | Is AI creating more than we can review? |
| Time from PR open to merge | Are we drowning in AI output? |
| Rework rate on AI-generated code | Is quality suffering? |
| Human intervention rate | How often does AI need steering? |

**Pros**: Measures the actual constraint in AI-augmented work
**Cons**: Harder to track; may require new tooling

### Tier 4: Skill Retention & Knowledge (Long-term Health)

If AI works, we need to ensure humans retain ability to:
- Understand the codebase
- Fix complex issues AI can't handle
- Onboard new people

Potential indicators:
- Time to resolve AI-assisted incidents
- Ability to explain recent code changes
- Confidence ratings on codebase knowledge (survey)

**Pros**: Addresses the automation ironies
**Cons**: Soft metrics; hard to quantify

---

## Recommended Starting Framework

For the trial quarter, propose tracking:

### Weekly Check-in Metrics (with Randy)

1. **AI tool spend** - Are we under ceiling?
2. **Tasks completed** - Throughput without offshore
3. **PR rework rate** - Quality indicator
4. **Blocking issues** - What AI couldn't handle

### Monthly Assessment

1. **Value-add capacity** - % time on new features vs. maintenance/bugs
2. **Offshore comparison** - What would this have cost with GlobalLogic?
3. **Knowledge check** - Can I still explain what the code does?

### End of Quarter Evaluation

1. **Total cost** - AI tools vs. offshore equivalent
2. **Delivered value** - Features shipped, quality metrics
3. **Sustainability** - Did skills atrophy? Is this maintainable?
4. **Decision** - Continue, adjust, or abandon

---

## Discussion Questions for Randy

1. **Baseline**: What's the current offshore spend we're comparing against? Per month? Per task type?

2. **Value definition**: How do we define "value delivered"? Story points? Features? Customer impact?

3. **Quality bar**: What's acceptable rework rate for AI-generated code? 10%? 20%?

4. **Scope**: Are we measuring just my JumpRope work, or developing a framework for org-wide use (with Alicia)?

5. **Reporting**: What format/frequency works for oversight? Dashboard? Weekly summary?

6. **Failure conditions**: What would make us stop the trial early? Cost overrun? Quality issues?

---

## Risks to Flag

1. **Goodhart's Law**: "When a measure becomes a target, it ceases to be a good measure." Any metric we track will get gamed.

2. **Invisible tech debt**: AI code that works now may create maintenance burden later.

3. **Selection bias**: Easy wins early may not represent steady-state performance.

4. **The 10x claim**: Most "10x" claims at conferences are measuring the easy parts. We should be skeptical of our own optimism.

---

## Next Steps

1. Review this framework with Randy (this week)
2. If aligned, set up simple tracking (spreadsheet or similar)
3. First data point: end of Week 1
4. If company-wide framework desired, involve Alicia after initial validation

---

*References: James Shore "A Useful Productivity Measure", Bainbridge "Ironies of Automation", Anthropic Economic Index*
