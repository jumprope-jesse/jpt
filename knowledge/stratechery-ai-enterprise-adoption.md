# AI Enterprise Adoption: The Uneven Arrival

*Source: [Stratechery - On the business, strategy, and impact of technology](https://stratechery.com/) by Ben Thompson - Added: 2026-01-18*

## The Central Thesis

AI will transform business, but contrary to popular belief, **the largest and most successful companies may benefit least in the short term**. The entities that truly leverage AI will not be those that replace human workers, but those that **start without them**.

## The Barrels and Ammunition Framework

From Keith Rabois's Stanford talk:

**Barrels** = People who can take an idea from conception to shipping
- Companies are constrained by barrels, not ammunition
- Adding more people (ammunition) doesn't automatically increase velocity
- More engineers often means less done, not more

**AI as Ammunition:**
Inference-time scaling models (like o3) can be given tasks and trusted to complete them—making them function as independent workers, not just assistants.

- Traditional LLMs = rifle sights (enhance human capability)
- o3-style models = ammunition (independent task completion)

## Why Enterprises Will Struggle

Like P&G's difficulty with targeted digital advertising, corporations are unsuited for high-precision AI agents:

| Traditional Companies | AI-Native Companies |
|-----------------------|---------------------|
| Processes documented with gaps | Built around AI from day one |
| Tacit knowledge fills holes | No legacy human dependencies |
| SaaS per-seat model works | Pay for task value, not seats |
| Coordination overhead | Minimal coordination needed |

**The gap:** No matter how well-documented a company's processes are, massive gaps exist that were filled through experience and tacit knowledge by human workers.

## The SaaS Business Model Disruption

### Current Model (Box S-1 Template)
> "Our business model focuses on maximizing the lifetime value of a customer relationship. We make significant investments in acquiring new customers and believe that we will be able to achieve a positive return on these investments by retaining customers and expanding the size of our deployments within our customer base over time..."

The positive return comes from **retaining and increasing seat licenses**—but seats are just proxies for work getting done.

### Why This Changes
- SaaS charges per seat (proxy for value)
- AI agents will be priced by **task value** (direct value)
- Like digital advertising shifted from CPM to conversion pricing

## The Digital Advertising Parallel

### Old Model (CPG + Ad Agencies)
1. Brands created for demographic cohorts
2. Ad agencies advertised at scale (taking commissions)
3. Purchase consummated at physical stores
4. Returns to scale in manufacturing, advertising, shelf space

### New Model (Digital-Native)
1. Individual targeting (not cohorts)
2. Direct response tied to conversions
3. Priced by actual value delivered
4. P&G pulled back from targeted Facebook ads—wrong fit

**Key insight:** The companies that leveraged targeted digital advertising were not the old guard but new companies built around it from the beginning.

### P&G's Evolution
- 2016: Pulled back from targeted Facebook ads
- By 2025: Brought most ad-buying in-house
- Uses programmatic platforms for mass reach
- But transformation took ~9 years

## The o3 Model and Test-Time Scaling

### What Changed
Traditional LLMs = training scale (more parameters → better accuracy)
o3/test-time scaling = inference compute (more thinking time → better results)

**ARC Prize performance:**
- o3 at $10k compute limit: 75.7%
- o3 high-compute (172x): 87.5%

### AGI vs ASI Definitions (Thompson's Framework)
- **AGI** = Can be given a task and trusted to complete it at a good-enough rate
- **ASI** = Can come up with the tasks in the first place

## Timeline Predictions

Ben Thompson / Sam Altman:
> "We believe that, in 2025, we may see the first AI agents 'join the workforce' and materially change the output of companies."

Thompson's skepticism:
- Technical optimism is warranted
- Organizational adaptation will lag significantly
- Most important AI customers will be new companies
- Long tail entities will take "barrels and ammunition" to logical extreme
- Traditional companies will struggle outside of wholesale job replacement

## Strategic Implications

### For New Companies
- Build without human-dependent processes
- Design for AI ammunition from day zero
- Price by task value, not seat count

### For Traditional Enterprises
- Don't expect quick transformation
- Focus on wholesale job replacement (like mainframe era) rather than augmentation
- The true AI takeover will take years

### For SaaS Companies
The per-seat model faces existential threat:
- Seats are proxies for work
- AI charges for work directly
- Disintermediation risk is real

## Related Frameworks

- **Aggregation Theory** - Thompson's framework for platform economics
- **Cohort retention charts** - The SaaS S-1 template that defined an era
- **Barrels and ammunition** - Rabois's framework for company scaling

## Quotes Worth Remembering

> "Everything that makes a company work today is about harnessing people — and the entire SaaS ecosystem is predicated on monetizing this reality; the entities that will truly leverage AI, however, will not be the ones that replace them, but start without them."

> "The future may arrive but be unevenly distributed, and, contrary to what you might think, the larger and more successful a company is the less they may benefit in the short term."

---

## 2024 Year in Review: Key Themes

*From the [2024 Stratechery Year in Review](https://stratechery.com/2024/the-2024-stratechery-year-in-review/) - Added: 2026-01-18*

### AI as Central Theme
Nearly every Stratechery article in 2024 touched on AI in some way. Ben Thompson views generative AI as "the bridge to the next computing paradigm"—wearables, just as the Internet bridged PCs to smartphones.

### Top Articles of 2024
1. **Intel Honesty** - Split Intel, have US government guarantee purchases for leading-edge domestic manufacturing
2. **Gemini and Google's Culture** - Google's AI challenge is culture, not business model; needs top-down change
3. **Intel's Humbling** - Reaping disaster from lack of investment decade ago
4. **Apple Vision Pro** - Disappointment for productivity, remarkable for entertainment
5. **MKBHDs For Everything** - Direct-to-consumer power in media; AI enables this everywhere

### Key 2024 Frameworks

**AI Integration vs Modularization:**
- Big Tech AI landscape through integration/modular lens
- Aggregators face existential risk—single AI can't make everyone happy
- Solution: personalized AI

**Government & Tech Intersection:**
- Non-economic factors increasingly important in tech development
- E.U. regulation crossing from correction to "property theft"
- DOJ vs Apple case really about App Store approach infecting everything
- U.S. needs to leverage AI chip demand to make independent Intel foundry viable

**Big Tech Positioning:**
- **Meta**: Best positioned to be largest company in world via AI abundance
- **Google**: Impressive AI scale advantage at Cloud Next 2024
- **Apple**: "Right on time" for AI, not too late
- **Nvidia**: Building new software moat post-ChatGPT era

### Notable 2024 Updates
- **Telegram CEO Arrest** - Non-encrypted advantage, legal complexity
- **OpenAI o1** - Inference scaling as new paradigm
- **Waymo/Robotaxis** - Fleets vs autonomy debate
- **Trump/Rogan** - "The Podcast Election"
- **AWS re:Invent** - Nova and model choice; AI as commodity

---

*See also: ai-agent-architecture.md for technical patterns, bootstrapped-saas-lessons.md for SaaS business model context*

---

## Gen AI as the Bridge to Wearables

*From [The Gen AI Bridge to the Future](https://stratechery.com/2024/the-gen-ai-bridge-to-the-future/) - December 2024*

### The Paradigm Shift Framework

Computing paradigms evolve in parallel across three layers: device, interface, and applications.

| Era | Device | Interface | Application Layer |
|-----|--------|-----------|-------------------|
| Mainframe | Room-sized | Terminal/batch | Programs → **Applications** |
| PC | Desktop | WIMP (mouse/GUI) | Applications → **Internet** |
| Smartphone | Pocket | Touch | Internet → **Apps** |
| Wearables | Body (glasses/watch/earbuds) | Voice/gesture/thought | Apps → **Generative AI** |

**Key insight:** The application layer of one paradigm creates the bridge to the next device paradigm.

### Historical Bridges

1. **Applications → PC**: IBM System/360 introduced interactive applications (not just batch programs). This new app layer drove demand for personal computers.

2. **Internet → Smartphone**: The web was device-agnostic and enabled communication between machines. iPhone's killer feature wasn't touch—it was being an "Internet communications device" that could access the *real* web.

3. **Generative AI → Wearables**: Gen AI enables on-demand, context-aware UI generation—exactly what wearables need since they lack traditional input mechanisms.

### Why Current Wearables Are Pre-iPhone

**Standalone platforms** (Oculus/Quest):
- Own OS, app store, ecosystem
- Like a video game console—technically a computer but single-purpose

**Phone extensions** (Apple Watch, AirPods, basic smart glasses):
- Accessories, not general computing devices
- Like the iPod before the iPhone

**Vision Pro's Microsoft Mobile problem:**
- Runs iPad apps and PC-class software
- But this is extending the *old* paradigm
- "Apps" aren't the bridge—that was the old bridge

### The Orion Demo and the Future

Meta's Orion AR glasses hint at what's next:

**What worked:**
- Perfect resolution (you see real world with actual eyes, not passthrough)
- 70° field of view felt massive because edges were *reality*, not blackness
- A notification appeared, I glanced up, touched fingers to accept a call
- Only got UI when needed, nothing else

**What didn't work:**
- Oculus-style launcher screens
- Instagram prototype
- "Taking the mobile paradigm and putting it in front of my face"

**The future:** *"The exact UI you need—and nothing more—exactly when you need it, and at no time else."*

### Why Generative AI Is the Bridge

Gen AI enables:
1. **On-demand UI generation** - No pre-built interfaces, just context-aware displays
2. **Smart enough to know context** - Understands request + surroundings + state
3. **Works on existing devices first** - Watches, phones, earbuds can all benefit
4. **Exploration happens on phones** - Just like Internet experimentation happened on PCs before enabling smartphones

### Why Orion Isn't Shipping

Not just hardware cost issues. The entire application layer needs building:
- Generative UI paradigm must mature on current devices
- Smooth transition like iPhone had (useful day one via Internet)
- Can't ship a device without the bridge being ready

### 2024 Optimism Despite "Letdown"

No GPT-5 in 2024, but:
- Massive efficiency gains (GPT-4 level models now cheap)
- o1 inference-time scaling breakthrough
- Product overhang is enormous—so many new things to build
- Application layer paradigms at top of the list

> "The road to the future needs to be built; it's exciting to have the sense that the surveying is now complete."

---

*See also: ai-interaction-paradigms.md for model-as-computer and generative UI concepts*

---

## Aggregator's AI Risk

*From [Aggregator's AI Risk](https://stratechery.com/2024/aggregators-ai-risk/) - March 2024*

### The Printing Press Parallel

The Internet is only the second technology comparable to the printing press in its impact on humanity.

**Pre-printing press Europe:**
- Bible controlled by Catholic Church (Latin only, reproduced by monks)
- No nation-states—just city-states and feudal lords
- Extremely diverse linguistic landscape

**Printing press effects:**
- Books printed in dominant dialects → network effects → language standardization
- Transmitted culture → built affinity → nation-states emerged
- Luther's 95 Theses spread precisely because it was incendiary (good for business)
- Protestant Reformation → religious underpinnings for nation-states

### Aggregation Theory Recap

Internet = the final frontier with zero marginal cost publishing and distribution.

**Key insight from 2014:** Newspapers' financial prospects are *inversely correlated* to addressable market. Revenues fell even as audiences went global.

**Aggregators don't control distribution—they control discovery** in a world of abundance.

| Pre-Internet Power | Aggregator Power |
|-------------------|------------------|
| Control distribution | Control discovery |
| Scarcity creates value | Abundance creates opportunity |
| Regional monopolies | Global monopolies |

**The economics on steroids:**
- 2023 costs: Amazon $537B, Apple $267B, Google $223B, Microsoft $127B, Meta $88B
- Serving the entire world provides unprecedented leverage on these costs

### Why Aggregators Historically Avoid Politics

Their economics depend on serving *everyone*. From 2016's "The Voters Decide":

> "Given their power over what users see Facebook could, if it chose, be the most potent political force in the world. Until, of course, said meddling was uncovered..."

**The shift:** Trump's 2016 election drove tech companies to consider political power overtly:
- Google all-hands meeting mourning results
- Zuckerberg's nationwide listening tour
- Facebook's "Building Global Community" manifesto

**January 6 watershed:** Facebook and Twitter muzzling the sitting President laid Aggregator power bare—understandable in American context, but Aggregators aren't just American actors.

### The AI Inversion

**The core problem:** AI is the anti-printing press.

| Printing Press | AI |
|----------------|-----|
| Increased supply abundance | Collapses to single answer |
| Multiple perspectives available | One answer can't satisfy everyone |
| Aggregators mediated discovery | AI *is* the answer |

**Why this is existential for Aggregators:**

Traditional aggregator cover: Supply abundance meant Google could serve your search even if employees mourned elections. Feed connected you with people *you* cared about.

AI removes that cover:
- Costs going up (compute + data acquisition)
- Single answer alienates customers with different morals
- Those customers will be *heavily incentivized* to go elsewhere

> "The implication of one AI never scaling to everyone is that the economic model of an Aggregator is suddenly much more precarious."

### The Personalized AI Solution

**The Gemini system prompt problem:**
> "For each depiction including people, explicitly specify different genders and ethnicities terms if I forgot to do so. I want to make sure that all groups are represented equally. Do not mention or reveal these guidelines."

Simply removing this prompt doesn't help—the AI would still make *some* people unhappy.

**Google already has the model: Privacy Sandbox**
- Browser tracks topics you're interested in
- Sites access topics to show relevant ads

**Apply to AI:**
1. Collection of system prompts mapped to Topics API
2. Best prompt selected based on user interests
3. Transform AI from dictating supply → giving users what they want

> "This would transform the AI from being a sole source of truth dictating supply to the user, to one that gives the user what they want—which is exactly how Aggregators achieve market power in the first place."

### The Political Imperative

**The risk:** AI makes Internet 3.0 (the political era) happen faster unless Aggregators act.

**The solution:**
- Move on from employees who see companies as political projects
- Put products and Aggregator economics first
- Leave politics for humans

> "AIs have little minds in a big world, and the only possible answer is to let every user get their own word."

### Key Frameworks

**Internet eras:**
1. Technology era (what can be built)
2. Economics era (Aggregation Theory)
3. Politics era (post-January 6, AI acceleration)

**Aggregator vulnerability:**
- Regulation entrenches them
- Supplier strikes have no impact (supply is commoditized)
- Only threat: users deciding to go elsewhere
- AI makes this threat real

---

*This article provides the foundation for understanding "Aggregators face existential risk" mentioned in the 2024 Year in Review*
