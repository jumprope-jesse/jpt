# Decision Theory & Social Dynamics

Insights on game theory, decision theory, and social equilibria from various sources.

---

## The Cooperate-Bot Strategy (Scott Alexander via Zvi)

*Source: LessWrong Monthly Roundup #24, November 2024 - Added: 2026-01-18*

### Why Early Christianity's Cooperate-Bot Won

Scott Alexander asked why early Christianity's strategy of essentially Cooperate-Bot won out over mystery cults' Tit-for-Tat. The strategy was extreme: not only helping those who couldn't reciprocate, but those actively persecuting Christians.

**Theories for why it worked:**
- Advertising, heroic appeal, and recruitment
- Competitive advantage of afterlife promises
- Access to the Jewish network (millions of Jews, extensive traditions, structures)
- Christians could proselytize where Jews couldn't

**The pivot:** Once Christians got sufficient numbers, they fully pivoted—started gathering armies and persecuting non-believers. This suggests:
- Cooperate-bot succeeds early via advertising and recruitment
- Too many unconditional cooperators isn't a stable equilibrium
- If 75%+ of population is cooperate-bot, defectors win
- Thus, the Spanish Inquisition

### Strategic Implications

When asked about the right strategy today for rationalists or EAs:

**Distinction matters:**
- Helping those who **can't** pay you back → mostly great
- Tolerating those **actively defecting** in bad faith → different

**Key considerations:**
- Give everyone epistemic fairness
- Check how much you and yours are correlated with other decisions
- Avoid creating bad incentives for others
- Take care of you and yours first
- Help, but not beyond sustainable means

**"Take all you have and give it to the poor"** is at best a Ponzi scheme—it destroys your means of production. Over-the-top generosity can work if and only if it inspires sustained exponential growth of that pattern.

---

## Credible Commitments and Causal Decision Theory

*Source: LessWrong Monthly Roundup #24, November 2024 - Added: 2026-01-18*

### The Cat-Killing Pact Problem

> "You've made a pact with a friend that if they commit suicide, you will kill their cat (to disincentivize their suicide). The friend has committed suicide. Would you follow through?"

**Result:** 83% said let the cat live.

**The game theory response:**
> "Only if I had at least one other suicidal friend I'd made the same pact with."

### The Credible Commitment Problem

We lose a lot through ubiquitous use of Causal Decision Theory and our inability, as a society and individually, to make credible commitments.

**The tension:**
1. If you say you're killing the cat, you should kill the cat
2. Because of this commitment, you wouldn't get into the situation
3. But if put in a situation where you've made a promise you'd never make, should you honor it?

---

## Unpredictability as Social Foundation

*Source: Paul Crowley via Zvi's LessWrong Monthly Roundup #24, November 2024 - Added: 2026-01-18*

### Why Waymos Get Bullied

People are gradually figuring out that Waymos are incredibly docile and careful, and taking advantage:

> "I once had someone sit on my Waymo for a few minutes to prevent it from moving. Waymos are programmed to be very cautious and careful drivers. They are completely unable to deal with someone sitting on the car's hood."

This means any person on the street can indefinitely stall a Waymo.

### The Deeper Point About Social Equilibria

**Our norms and equilibria absolutely rely on:**
- Human unpredictability
- Low possibility of completely unhinged response
- Dramatically oversized reactions we can't reliably predict
- Meta-level unpredictability: "I don't know what might happen but I sense I'm not supposed to Go There"

**What does most of the work:**
- Not knowing where the lines actually are
- Not being willing to risk the tail
- Many interactions are effectively stochastic chicken

**Those who succeed despite this:**
- Act confident and Just Do Things
- Have figured out where lines actually are
- Are willing to risk some negative but ultimately harmless feedback
- Take on minimal tail risk

**The problem:** We don't want and won't tolerate AI or self-driving cars having that tiny chance of going bonkers. So autonomous systems become predictable, and predictable systems get exploited.

---

## Social Information and Cognitive Bias

*Source: LessWrong Monthly Roundup #24, November 2024 - Added: 2026-01-18*

### When to Trust Social Information

Study found participants who formed opinions before seeing others' estimates did worse on calorie estimation—they put too much weight on their own opinions.

**The laboratory insight:** When you have no reason to think your estimate is more accurate than others', a straight average is optimal.

**The real-world caveat:** Outside laboratories:
- You can't be confident others' opinions are as trustworthy as yours
- There are plausible points of failure for others' information that don't apply to your own
- If everyone weights others' info equally, information cascades become inevitable and devastating
- You need to worry that others got their information socially (not independently)

**The generalized rule of full indifference between information sources is "utterly insane"** as a principle, even if it's right in controlled experiments.

---

## Honesty and Dishonesty Patterns

*Source: LessWrong Monthly Roundup #24, November 2024 - Added: 2026-01-18*

### Measuring Dishonesty: Impossible Task Completion

One measure: How many people claim to have completed an impossible five-minute task?

**Results by country (percentage who lied):**
- Dramatic differences exist
- Clear geographic patterns
- Different from lost wallet reporting rate (which involves other dynamics)

### Reddit Toxicity Study

Those who are toxic in political contexts are also toxic in non-political contexts (r=0.47).

**Less trivial findings:**
- Those who comment on political contexts at all are more toxic in general
- Those who comment in both left-wing and right-wing contexts are more toxic still

---

## Related Concepts

- **Causal Decision Theory** - Standard decision theory with credible commitment problems
- **Tit-for-Tat** - Cooperative strategy that reciprocates
- **Information Cascades** - When people follow social signals over private information
- **Stochastic Chicken** - Repeated games with unpredictable escalation

---

## Updateless Decision Theory (UDT)

*Source: "UDT1.01: The Story So Far (1/10)" by Vanessa Kosoy via LessWrong, March 2024 - Added: 2026-01-19*

### Why UDT Matters

Standard decision theory works great in single-player environments. But in multiplayer settings where things can **predict your actions** and select their behavior based on what you will do (or would do in different situations), things get complicated.

**Examples of "predicting what you will do":**
- A human helping you gain power iff you'll likely reciprocate
- A bank with brain scanner giving loans to those who'd predictably repay
- An AI reasoning about another AI's source code to predict future conflict
- "I don't want to brush my teeth but there are future-mes in the same situation making the same decision"

**Examples of "predicting what you would do":**
- Scott Garrabrant never answering questions about whose team he's on in social deception games (whether Werewolf or Villager)
- A hacker who threatens an AI only if they see flaws in its threat-resistant decision theory
- An AI coordinating with clones on underwater construction (bad radio comms) by reasoning "if I was in that alternate situation, I'd do X"

**The insight:** The best action looks like "act according to the policy you would have wanted to precommit to." Just because you lose in a certain scenario doesn't make it wrong—other things predicting your decision (in your past, future, or far-distant in space) must be taken into account.

### Standard Toy Problems

**Counterfactual Mugging:** Omega flips a coin. Tails = asks for $10. Heads = gives you $100 iff you would have paid on tails. Coin was tails. Pay? Policies that pay get $45 more in expectation.

**Parfit's Hitchhiker:** Stranded in desert, Omega gives you a ride iff it predicts you'd pay $10K upon reaching civilization. You got a ride. Pay? Policies that pay get (value of life - $10K) more.

**XOR Blackmail:** 1% chance your house has termites ($10K remediation). Letter from Omega: "I predicted termites XOR you send $100." Pay = 99% chance of getting letter (-$199 EV). Don't pay = 1% chance (-$100 EV). Don't pay.

### Key Terminology

- **Acausal effects** - Effects of decisions on timelines you're not in (because something predicts what you *would* do)
- **Retrocausal effects** - Effects of decisions on your past (because something predicted what you *will* do)
- **UDT1.0** - "In a situation, select the action maximizing a-priori expected utility"
- **UDT1.1** - "Pick a policy at start maximizing a-priori expected utility, then just follow it"

### Why UDT1.0 Isn't Enough

If Omega can predict your actions in various scenarios, it can implement payoffs depending on what you do across all scenarios. With 4 scenarios and 2 actions each, Omega can set up any {0,1}⁴ → ℝ payoff function.

**The problem:** Local optimality doesn't imply global optimality. You've gotta figure out a policy for all possible situations—like a multi-player game where all players are you in different situations, sharing the same utility function.

Even with identical utility functions, Nash equilibria aren't always globally optimal. To get global optimality, you must coordinate all moves at once.

### Computational Intractability

**The brutal truth:** UDT1.1 runs in double-exponential time.

- ~|O|ⁿ elements in O<n (histories)
- ~|A|^(|O|ⁿ) policies to check
- Runtime ≈ |A|^(|O|ⁿ) × T(n)

For any policy π, you can construct a perverse environment that gives good outcomes only for that exact policy. "Do exactly what I say in all conceivable circumstances and you win, anything else means you lose."

**This is where all previous UDT research stalled.**

### The Learning Theory Path Forward

The Bayesian story: prior over environments, update as you observe, act to optimize.

The learning theory story: have a set of environments where, no matter which one you're in, you converge to decent behavior. Worst-case guarantees rather than "average according to prior."

**Key insight:** Not every set of environments is learnable. Some are so rich that no strategy converges on all of them. You need:
- Rich enough to contain the thing you want to learn
- Not so rich you sacrifice ability to learn anything

**Diagnosis of the stall:** UDT researchers implicitly ran face-first into the No Free Lunch Theorem by considering all policy-prediction environments—far too rich a class.

**To make progress:** Restrict to environments with more structure to exploit, and have the algorithm figure out what setting it's in.

**The "isn't that updating?" objection fails** because everyone is being unacceptably vague about what the "prior over policy-selection environments" consists of. The entire problem got stuffed into the prior and argmax computation.

**Prediction:** If the Bayesian side ever shows a "prior on policy-selection problems with nice properties," it will implicitly be because that prior puts mass on a substantially more restricted, learnable class of environments.

### Practical Implications

The series continues with: "If you're willing to make simplifying assumptions that rule out most possible policy-selection environments, and look for a UDT1.0-style algorithm to climb to a local optimum in policy-space, how far can you get?" Apparently, a lot further than expected.

---

## Bargaining Theory & Boundaries

*Source: "«Boundaries», Part 1: a key missing concept from utility theory" by Andrew Critch via LessWrong, March 2024 - Added: 2026-01-19*

### The Missing Zero Point in Utility Theory

Most game theory represents players with utility functions, but the von Neumann–Morgenstern rationality axioms only determine utility functions **modulo a positive affine transformation** (x ↦ ax + b, a > 0). There's no canonical "zero" utility.

**The problem:** When games allow communication and repeated interaction ("folk theorems"), there are often **zillions of possible equilibria**. Bargaining theory tries to pick special points, but these depend on a critical concept: the **disagreement point**.

### Disagreement Points (BATNAs)

The **Best Alternative to Negotiated Agreement (BATNA)** is what each player falls back to if negotiation fails.

**Key bargaining solutions:**
- **Nash Bargaining Solution** - picks a point on the Pareto frontier based on disagreement point d
- **Kalai-Smordinsky Solution** - similar, also depends on d

**Critical limitation:** BATNAs are only meaningful if they're **constant** (protected from what happens during negotiation).

**Nash's own critique (1953):** In reality, payoffs outside negotiations depend heavily on behavior inside them. Examples:
- If someone threatens you → go to police (not just go home)
- Unacceptable negotiation behavior → changes what you do if talks fail
- You can affect their payoff outside negotiation based on what you observe inside it

### Boundaries as Protected Disagreement Points

**The core insight:** To have a meaningful BATNA, you need a **safe/protected/stable place to walk away to**. For many people, this is literally their home.

**Social norms that maintain BATNAs:**
- "Mind your own business"
- "Don't threaten to attack people"
- "People can do what they want in privacy of their own homes"

These norms **simplify bargaining dynamics** by maintaining a well-defined fallback: "go home and do your own thing."

### Identifying BATNAs via Boundaries

Since BATNAs need protection to be meaningful, ask: **What protections already exist going into negotiation?**

**Three levels of protection:**

1. **Physical boundaries** - Is there already a physically identifiable membrane (cell wall, skin, fence, firewall) separating agents? If yes, agents can disengage and focus resources inside the membrane ("taking your ball and going home").

2. **Social conventions** - Is there an existing social norm protecting the membrane? If so, it offers a BATNA.

3. **Veil of ignorance agreement** - Would agents have acausally agreed behind a veil of ignorance to respect each other's boundaries before entering negotiation?

### Boundaries in High-Stakes Negotiations

In real-world state-level negotiations (wars), almost the entire interaction is characterized by:
- Violation (or threat) of an existing boundary (e.g., "attack on American soil")
- What new boundaries will exist after the conflict (redefining territories)

**Examples:**
- WWII Eastern Front = states changing their boundaries
- International law = attempting to establish boundaries that protect BATNAs
- Nuclear deterrence = protecting national boundaries via threat

### Folk Theorems and the Space of Equilibria

**Folk theorems** show that when games have:
1. Potential for communication and commitments
2. Potential for repeated interaction (reputation)

...there are **vast spaces of possible equilibria**.

**The indeterminacy problem:** This gives us:
- No clear prediction about what will actually happen
- No clear normative prescription of what should happen

**Boundaries as solution:** They help select which equilibrium by defining what "zero utility" (walking away) means for each player.

### Living Systems Require Boundaries

With rare exceptions (embedded agency research), most utility-theoretic descriptions of rational agents are **missing the idea that living systems require and maintain boundaries**.

**What counts as a boundary (generalized membrane):**
- Cell membrane (separates inside from outside)
- Person's skin (body boundary)
- Fence around yard (family living space)
- Digital firewall (LAN vs internet)
- Sustained disassociation of social groups
- National borders

**Key property:** Not arbitrary constraints—they **'carve reality at the joints'** in ways that aren't purely subjective judgments.

### Comparison to Cartesian Boundaries

Similar to Scott Garrabrant's "Cartesian Frames" work, but with differences:

1. **Life-focus:** Focus on boundaries of "living systems" that might not be fully "agentic" (e.g., humans not behaving agentically, governments in internal disagreement)

2. **Flexibility-focus:** Cartesian Frames assumes fixed boundary; this framework models boundaries as potentially **flexible, pliable, or permeable** over time

### Social Norms as Boundary Maintenance

Certain norms exist to maintain separations between living systems:

**Personal space boundaries:**
- Asking permission before touching
- Protocol for crossing the boundary

**Information boundaries (groups):**
- Not discussing romantic life at work
- Workplace as living system protected from certain personal info

**Information boundaries (individuals):**
- Not expressing violent thoughts to targets
- Protecting others from sense of threat
- Can be viewed as either enclosing violent thoughts OR protecting rest of world

### Connection to AI Safety

**Critical question:** Will AI technology respect certain boundaries, such as:
- Boundaries of human body and mind (protecting individuals)
- Boundaries around physical territories
- Boundaries around cyberspace

Whether these can be maintained determines whether AI causes human extinction.

(See also: boundaries-membranes-ai-safety.md for full treatment)

### Key Takeaways

1. **Boundaries of living systems are important** - not just social constructs
2. **They have technical role in multi-agent theory** - defining disagreement points
3. **Missing from utility theory** - canonical "zero point" needs boundaries to be meaningful
4. **Simplify complex bargaining** - reduce infinite equilibria to tractable choices
5. **Apply across domains** - from cells to states to AI safety

**Further reading:** See Andrew Critch's full «Boundaries» Sequence on LessWrong (Parts 1-4)
