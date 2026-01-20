# How Complex Systems Fail

## Source
- [How Complex Systems Fail](https://how.complexsystems.fail/) by Richard I. Cook, MD
- Originally published: 1998 (Cognitive Technologies Laboratory, University of Chicago)
- Classic paper on systems thinking and failure analysis
- Added: 2026-01-18

## The 18 Principles

### Nature of Complex Systems

1. **Complex systems are inherently and unavoidably hazardous**
   - All interesting systems (healthcare, aviation, software) carry intrinsic risk
   - Hazard is a core property, not an aberration

2. **Complex systems are heavily and successfully defended against failure**
   - Multiple layers of defense: technical, human, and organizational
   - Redundancy, training, regulations, and continuous oversight

3. **Catastrophe requires multiple failures—single point failures are insufficient**
   - No single flaw causes system breakdown
   - Catastrophe emerges from the *combination* of small failures

4. **Complex systems contain changing mixtures of latent failures**
   - Undetected flaws always exist
   - Any one flaw is insufficient alone; they wait dormant for conditions to align

5. **Complex systems run in degraded mode**
   - Systems function despite numerous flaws
   - Redundancy and human adaptation keep them running

6. **Catastrophe is always just around the corner**
   - The potential for catastrophic failure cannot be eliminated
   - Constant vigilance is required because risk is perpetual

### The Nature of Failure

7. **There is no "root cause" of accidents**
   - Post-accident attribution of single causes is fundamentally wrong
   - Multiple insufficient factors jointly produce accidents
   - "Root cause" is a social/political construct, not technical reality

8. **Hindsight biases post-accident assessments**
   - Knowing the outcome distorts how we judge operator decisions
   - Actions that seemed reasonable become "obvious mistakes" in retrospect
   - This bias leads to unfair blame and unhelpful remedies

9. **Human operators have dual roles: production AND safety**
   - Practitioners simultaneously produce output and defend against failure
   - These goals are often in tension

10. **All practitioner actions are gambles**
    - Outcomes are uncertain; success results from successful gambles too
    - After-the-fact judgment ignores this fundamental uncertainty

### Human Adaptation

11. **Actions at the sharp end resolve all ambiguity**
    - Front-line workers make the actual risk/production tradeoffs
    - Policies and procedures can't capture all real-world situations
    - The "sharp end" bears the burden of uncertainty

12. **Human practitioners continuously adapt to maintain safety and production**
    - Operators actively manage dynamic situations
    - They adjust based on incomplete, shifting information
    - This adaptation is *how* systems stay safe

13. **Human expertise in complex systems is constantly changing**
    - Technology changes, personnel turn over
    - Expertise must be continuously rebuilt and transferred

### System Evolution

14. **Change introduces new forms of failure**
    - New technology eliminates old failures but creates novel ones
    - New failures may have worse effects than the old
    - "Fixes" often trade known risks for unknown ones

15. **Post-accident remedies usually increase coupling and complexity**
    - Adding safeguards after failures often makes systems more complex
    - More complexity can create new failure modes
    - Band-aids accumulate over time

### The Nature of Safety

16. **Safety is a system property, not a component property**
    - Safety emerges from the complete system
    - It cannot be purchased or manufactured as a component
    - No single element "contains" safety

17. **People continuously create safety**
    - Safety is an active, ongoing process
    - Practitioners create it through normal adaptive work
    - Without this continuous effort, systems fail

18. **Failure-free operation requires experience with failure**
    - Operators need contact with system limits to calibrate their responses
    - Experiencing hazards trains practitioners to recognize and avoid them
    - Too much insulation from failure reduces competence

## Applications

### Software Engineering
- Production systems always run in "degraded mode" with known bugs
- Incident response requires avoiding hindsight bias
- "Root cause analysis" should really be "contributing factor analysis"
- Adding safeguards after outages can increase system complexity

### Team Leadership
- Front-line engineers (sharp end) make the real tradeoffs
- Safety culture requires psychological safety to report near-misses
- Blame-focused retrospectives miss the systemic picture
- New team members need exposure to edge cases to build expertise

### Personal Life
- Family systems are complex—resilience comes from redundancy and adaptation
- Balance between "production" (work, goals) and "safety" (relationships, health)
- Building support systems is an ongoing practice, not a one-time setup

## Key Insight

> Safety is not a property that can be added to a system. It emerges from continuous human adaptation to hazards. The same operators who "cause" accidents are the ones who normally prevent them.

## Case Study: Canva Outage (December 2024)

Source: [Surfing Complexity analysis](https://surfingcomplexity.blog/2024/12/21/the-canva-outage-another-tale-of-saturation-and-resilience/) of Brendan Humphries's writeup

### The Incident Chain

1. **Trigger**: Deployed new editor page (nothing wrong with the code itself)
2. **Latent pathogen**: Stale Cloudflare rule routed Singapore↔Virginia traffic over public internet instead of private backbone, causing packet loss
3. **Synchronization**: CDN's "Concurrent Streaming Acceleration" caused all clients to simultaneously download assets, creating a thundering herd
4. **Amplification**: Known performance bug in API gateway (blocking calls to telemetry library) reduced throughput - fix was scheduled for *that same day*
5. **Positive feedback loop**: Load balancer marked overloaded tasks unhealthy, shifted load to remaining tasks, which then also went unhealthy
6. **Autoscaler outpaced**: OOM killer destroying tasks faster than autoscaler could provision new ones

### Principles Illustrated

| Principle | How It Appeared |
|-----------|-----------------|
| #4 Latent failures | Stale routing rule sat dormant until deploy |
| #3 Multiple failures required | Neither the routing bug nor the telemetry lock alone caused outage |
| #7 No root cause | Was it Cloudflare? The lock? The deploy timing? All contributed |
| #14 Change introduces failure | Deploy triggered cascade, even though code was correct |
| #12 Human adaptation | Engineers improvised load shedding via Cloudflare firewall |
| #17 People create safety | Manual intervention restored service when automation failed |

### Key Concepts

**Decompensation**: When a system can't keep up with the rate of degradation. The autoscaler couldn't provision tasks faster than the OOM killer destroyed them.

**Competence envelope**: The range of inputs a system can handle. Incidents push systems outside this envelope. Resilient systems can adapt to extend the envelope; brittle systems collapse.

**Robustness vs resilience**:
- Robustness = larger competence envelope (handles more scenarios)
- Resilience = ability to adapt when pushed *outside* the envelope
- A system can be robust but brittle (handles many cases, but fails hard on edge cases)

### Recovery Strategy

1. **Reduce load**: Blocked all traffic at CDN layer (Cloudflare firewall)
2. **Increase capacity**: Manual scaling (but OOM killer outpaced it)
3. **Incremental restore**: Ramped traffic back gradually (9:45-10:04 AM)

### Irony of Observability

The performance bug was in telemetry code—observability logic. Similar pattern in OpenAI and Netflix incidents. "Observability giveth reliability, and observability taketh reliability away."

### Operational Insight

> The more powerful and generic dynamic configuration features are, the more room for maneuver we have during incidents. But operators must be *familiar* with them. Changing an unhealthy system is dangerous—you can always make things worse.

## Related
- [[software-project-failures]] - Specific patterns of software project failures
- [[engineering-leadership-principles]] - Team culture and psychological safety
