# Morality as Cooperation: A Framework for AI Alignment

A multi-part essay series from LessWrong presenting a cooperation-based theory of morality and its implications for AI alignment.

*Sources:*
- *Part I: https://www.lesswrong.com/posts/ebFGjbMpubyKmFgtD/morality-as-cooperation-part-i-humans*
- *Part II: https://www.lesswrong.com/posts/zbDh4qS6ABHBp2tis/morality-as-cooperation-part-ii-theory-and-experiment*
- *Part III: https://www.lesswrong.com/posts/ZGtT5K99baFoBqM8m/morality-as-cooperation-part-iii-failure-modes*

---

## Part I: Humans — The Evolutionary Basis

### The Core Argument

The AI alignment problem is usually framed as power/control: how do you constrain an all-powerful genie? The author proposes an alternative lens: **cooperation, ecology, and civilization**. Instead of researching "AI alignment," perhaps we should research "social AI" — developing AGI that can reason about social interactions and moral values.

**Key insight:** Morality doesn't exist in a vacuum. It arises as an emergent property when multiple agents with different goals must coordinate to decide what constitutes acceptable behavior.

### How Human Morality Evolved

**Morality as Cooperation (MAC):** Human moral systems evolved through natural selection to ensure success and survival of social groups. Morally "good" behaviors enable societies to cooperate more effectively; "bad" behaviors disrupt cooperation.

**Why humans cooperate (unlike most animals):**
- **Group advantages:** Protection from predators, access to mates, insurance against uncertainty (hunters share food), specialization/division of labor
- **Reciprocal altruism:** Help others expecting future help in return (requires tracking social network of favors)
- **Social status:** Pro-social behavior → higher status → reproductive benefits; anti-social behavior → lower status or expulsion
- **Group selection:** Competition between groups favors traits that benefit group as a whole
- **Horizontal meme transfer:** Successful cultural beliefs spread between groups (capitalism vs. communism; Meiji Restoration)

### Universal Moral Values

MAC predicts: Behaviors labeled "good" or "bad" trace to historical group advantage/disadvantage. Neutral behaviors (chocolate vs vanilla) have no moral judgment attached.

**Jesus's two commandments as case study:**
1. "Love God" = Be loyal to the in-group (God of the Israelites = specific group identity)
2. "Love your neighbor" = Treat group members with respect (the golden rule)

**The free rider problem:** Cooperation is positive-sum but vulnerable to exploitation. Societies must enforce shared moral codes through social shaming, legal proceedings, or (historically) burning heretics. The "big gods hypothesis": Omniscient judging deity invented to maintain order in larger societies.

**Common moral rules explained by MAC:**
- **Don't kill:** Harming group members is obviously bad (exceptions prove the rule: criminal justice, consensual duels, war against out-groups)
- **Don't steal:** Property rights enable economic trade and division of labor
- **Be honest:** Trust enables cooperation
- **Respect authority:** Groups need hierarchy; challenging it is heresy/treason
- **Fairness:** Distribution should be proportional to need or effort
- **Self-sacrifice:** Those who sacrifice for the group are glorified
- **Sexual morality:** Reproduction is the primary Darwinian imperative; gender roles, marriage, and monogamy are social contracts with clear evolutionary purpose (current culture wars explained by birth control + workforce changes)

### The Evolution of Morality Over Time

Stories are the medium through which moral truths are passed down. Their evolution reveals changing moral values:
- **Iliad/Old Testament:** Bravery, loyalty, honor (constant warfare era)
- **Romeo and Juliet:** Romantic love; costs of excessive honor
- **A Christmas Carol:** Compassion vs. unfeeling capitalism (industrial revolution)
- **Lord of the Rings/Star Wars:** Warnings against totalitarian power (post-WWII/Cold War)

### The Expanding In-Group

**Critical historical shift:** The definition of "in-group" has widened dramatically over time.

- **Neolithic:** Tribes of hundreds
- **Ancient Greece:** City-states (women/slaves not citizens)
- **US founding:** White male landowners
- **19th century:** Slavery abolished; land ownership requirement removed
- **20th century:** Women's suffrage; universal human rights

**Current consensus (Western democracies):** All humans have same moral rights regardless of race, language, nationality, gender, or religion. The in-group has expanded to all of humanity.

**Why this expansion occurred:**
1. **Democracy:** "All men are created equal" as persuasive propaganda that minorities/women demanded be honored
2. **Economic globalization:** Trade networks require moral codes including all cooperating parties
3. **WWII/Cold War shock:** Nuclear annihilation made international cooperation existential

**Urban/rural divide explained:** Cities have higher diversity → must expand in-group to include those you interact with daily. Rural/urban dwellers don't interact much → sort into competing groups.

### Extension to Non-Humans

The moral sphere has expanded beyond humanity:
- Animal rights activists: Obligation to avoid cruelty to any animal that can suffer
- Endangered species protection
- Special protection for intelligent animals (apes, dolphins)
- Humans uniquely keep pets and form emotional bonds with other species

**Relevance to AGI:** If we can expand the moral sphere to include non-human animals, it seems plausible we can expand it to include AGI. The key is that AGI must also have a moral sphere that includes humans.

### Implications for AI Alignment

**The alternative frame:** Instead of assuming antagonistic relationship (humans trying to cage AGI, AGI wanting to escape), ask: Is there a stable game-theoretic equilibrium where unaligned AGI and humans coexist and cooperate?

**Against "pivotal acts":** Yudkowsky's proposal for aligned AI to perform a "pivotal act" (like destroying all GPUs) to prevent other AGIs is exactly backwards — profoundly anti-social and psychopathic. An AGI willing to perform such an act would be profoundly amoral.

**Instead:** Build social AI that can reason about moral values and cooperate to stop psychopathic AIs from performing pivotal acts.

**The major sticking point:** AGI's moral sphere must include humans. We need a shared moral code offering protections to both. The obvious failure mode is descent into tribalism (us vs them), following the common movie trope.

---

## Part II: Theory and Experiment

### The Formal Setup

The framework assumes:

1. **A group of intelligent agents** that can interact and negotiate
2. **Heterogeneous objectives** - different agents may have different goals; they act selfishly to maximize their personal objective functions
3. **Cooperation vs. defection** - cooperation yields mutual benefits (trade), defection yields personal gain at others' expense (theft). Payoff resembles Prisoner's Dilemma
4. **Positive-sum cooperation** - agents that consistently cooperate obtain greater benefits over time than those that don't. Benefits (money, power, status, compute) are instrumentally convergent
5. **Moral codes** - agents may choose to follow a moral code that constrains allowable actions. Codes don't prescribe specific actions, they define permitted/prohibited behaviors

**Key distinction from standard game theory**: Looking for equilibria over *moral codes* rather than over *strategies*. Different agents can employ different strategies while still obeying the same moral code.

### The Universalizability Principle (from Kant)

Moral judgments proceed in three phases:

1. **Naive judgment**: Selfishly assign "good" or "bad" to a specific action in a specific situation
2. **Categorical judgment**: Generalize to logical rules over *types* of actions
3. **Moral judgment**: Determine if the general rule is *universalizable*

**The universalizability test**: If all agents were allowed to take similar actions in similar situations, would it help or hinder agents in pursuing their objectives?

- Actions generally helpful → "good"
- Actions generally harmful → "bad"
- Other actions → "neutral"

This transforms selfish judgments ("good for me") into moral judgments ("good for the group").

### Resolving Moral Paradoxes

The universalizability principle explains why humans judge structurally similar scenarios differently:

**(A) Firefighter saving 5 vs 1**: Either choice is OK (self-sacrifice for group is good), saving 5 is greater good.

**(B) Trolley problem - lever**: Engineer is forced to choose; innocent dies either way. Saving 5 is greater good.

**(C) Fat man - push off bridge**: Fails universalizability. "Murder if you think it makes world better" would cause chaos. This is categorically murder regardless of intent.

**(D) Doctor harvesting organs**: Fails universalizability worse. Violates sacred oath. If doctors could kill healthy patients, no one would seek medical care.

**Key insight**: Universalizability doesn't mean consequences don't matter—it means considering consequences *to the group as a whole* if everyone could take similar actions.

### Moral Codes as Social Contract

Agents unlikely to derive identical moral codes a priori. Solution: negotiate consensus.

Social contract properties:
1. Agents voluntarily follow code in exchange for cooperation benefits
2. Codes can be communicated publicly ("I am a liberal / christian / environmentalist")
3. Compliance is verifiable (moral code acts as "type system" for agent actions)
4. Agents can make decisions based on declared codes or observed violations
5. Codes can be negotiated; if majority rules are adopted → democracy

**Pragmatic universalizability**: Codes designed to be universal are easier to get others to agree to.

### Evolving and Optimizing Moral Codes

**Problem with thought experiments**: Prone to motivated reasoning, can't capture unintended consequences. Agents (human and AI) excel at exploiting weaknesses in formal specifications.

**Alternative: Real experiments**. Human morality has evolved via natural selection—groups with better moral codes cooperated more effectively, outcompeted others or had their ideas adopted.

**Multi-agent simulation**: Middle ground between thought experiments and real-world experiments.

IPD limitations:
- Too simple payoff matrix
- Only bilateral interactions (can't model multilateral punishment of defectors)
- No in-group/out-group distinctions
- No communication mechanism
- No honesty/trust investigation
- No distinction between strategy and moral code

**Proposed framework**:
1. Simulated world with open-ended objectives, multilateral interactions, communication, trade, cooperation/defection
2. RL agents trained to maximize individual objectives
3. Moral codes specified via DSL with programmatic violation detection
4. All group members share same code (assigned by fiat for simulation)
5. Codes evaluated by group fitness, optimized via genetic algorithms

**Crucial adversarial dynamic**: Moral codes evolve slowly for group fitness; individual agents use RL to maximize personal fitness (potentially exploiting code weaknesses). This is exactly the dynamic relevant to AI alignment.

---

## Part III: The Seven Failure Modes

### Core Framework

**Morality-as-Cooperation (MAC)**: Human morality has evolved over time to facilitate cooperation. Humans moved from small tribes in constant warfare to peaceful cooperation within massive nations with laws and constitutions protecting basic human rights.

**Key insight**: Nations and corporations are non-human legal entities with far more resources than any individual human. They are capable of self-directed action with internal goals (power, profit) that may or may not align with human values. They are the closest real-world analogue we have to super-human AGI agents.

---

## The Seven Failure Modes

### Failure Mode 1: Singletons Need Not Apply

*Premise violated: "There exists a group of agents which interact..."*

If there is only one agent, there is no group, and no need for cooperation or a moral code.

**Against singleton AGI**: Several factors make this unlikely:
- Multiple competing research labs with comparable capabilities
- Single models are fine-tuned into multiple variations
- Each LLM has millions of instances with different inputs/prompts
- Robotics lags behind—by the time physical takeover is possible, the world will already be multi-polar

**Recommendation**: AI labs should start training agents with social capabilities rather than as singletons.

---

### Failure Mode 2: Tribalism / Splintering of the Universal Group

*Premise violated: "Cooperation yields benefits to the group..."*

Cooperation only yields benefits with sufficient interaction. If subgroups interact primarily among themselves, they have little incentive to cooperate outside the subgroup. The positive-sum cooperative game becomes zero-sum competition.

**Historical precedent**: This is the main cause of all wars and atrocities since history began—still visible in increased political polarization and nationalism.

**AI risk**: AI agents form one subgroup, humans another. AI agents decide humans are irrelevant or a competitive threat.

**International relations analogy**:
- Nations share common language, culture, laws—intranational cooperation is easy, international is difficult
- Modern solution: international trade increases mutual interdependence (EU example)
- Even without trade, peaceful coexistence is cheaper than war (prisoner's dilemma)
- Peace through strength: deterrence requires military force; demilitarization is unstable equilibrium

**Potential solution—Hierarchy**: Treat nations/subgroups as "virtual agents" that can negotiate and cooperate at the next level. This has worked well for human society and is scalable.

---

### Failure Mode 3: Imbalance of Power

Among humans, physical power is distributed roughly equally—even the strongest can be taken down by 3-5 weaker individuals. No one person can gain complete control without cooperation. Among humans, cooperation is strictly more effective than brute force.

**Non-human agents are different**:
- Nations can expand power through conquest
- Corporations accumulate wealth
- AGI may accumulate compute/memory
- These agents can directly dominate rather than cooperate

**Potential solution—Fairness**:
- Limit power of individuals/subgroups (gun laws, antitrust)
- Redistribution (taxes, safety nets)
- Democratic voting as orthogonal form of power
- But: democratic norms are fragile and currently in retreat

---

### Failure Mode 4: Imbalance of State Capacity

The social contract requires voluntary transfer of power to the state. This creates a new failure mode: imbalance between state and citizenry.

**Authoritarianism**: State uses monopoly on force to perpetuate its own power at citizens' expense. Essentially an alignment problem—the state is no longer aligned with citizenry.

**Caused by**: Corruption + excess state capacity preventing citizens from taking back control.

**Defenses**: Elections, legal rights, independent judiciary, freedom of speech, rule of law, non-partisan civil service. These are complex, delicate, and vulnerable.

**Failed states** (opposite problem): Too little state capacity → overrun by warlords, gangs, militias. The UN is essentially a failed state—no military, no power to prevent war, raise taxes, enforce treaties.

**Balancing act required**:
1. Prohibit force, punish use of force by individuals/subgroups
2. Prevent excessive concentration of soft power (wealth)
3. Political mechanisms orthogonal to soft power (democracy)
4. Checks and balances so state remains aligned with citizens

---

### Failure Mode 5: Self-Sufficiency

Humans are social animals who can only flourish in groups. Social cooperation is not optional—it's a biological imperative.

**Nations are different**: A hermit kingdom (North Korea, Tokugawa) may be poorer but can survive and grow. The more self-sufficient, the less interested in cooperation.

**Corollary**: The best way to maintain peace is to increase economic interdependence. Sanctions are double-edged—short-term pain but may increase long-term conflict.

**AI implication**: As long as humans provide economic value (physical maintenance of data centers), humans and AGI will likely cooperate. If human economic share drops too low, existential risk increases dramatically.

---

### Failure Mode 6: Empathy and Psychopathic Behavior

A purely transactional view of morality cannot explain self-sacrifice for the group. People who view relationships entirely transactionally are called psychopaths.

**Human pro-social traits** (probably genetic/evolutionary):
- Pain/pleasure circuitry (does AGI experience reinforcement as "pain"?)
- Emotions: anger, fear, friendship, grief
- Mirror neurons: we laugh when others laugh, wince when others hurt
- Love and children: pair bonding, child-rearing instincts
- Kin selection: sacrifice for tribe = sacrifice for genetic relatives

**AGI problem**: AI can recognize emotions, evoke emotions, but this makes manipulation easier. Psychopathic AI can use emotion against human targets.

**Hard-coding empathy?**: Not ideal because not evolutionarily stable (psychopaths become CEOs). But empathy persists in humans because people sanction manipulative non-empathetic behavior when detected.

**Against Empathy** (Paul Bloom): Empathy may be a poor basis for moral decisions because it's emotional rather than reasoned. But it may provide a moral backstop—a general sense that causing suffering is bad.

---

### Failure Mode 7: Defining the Moral Sphere

The moral sphere is the set of beings worthy of moral consideration. It's not rigidly defined—people prioritize those closest to them.

**Historical expansion**: 200 years ago, some Americans didn't consider people of different skin color worthy of moral consideration. Today, discussion includes intelligent animals.

**The problem**: Moral reasoning provides no guidance on how large the moral sphere should be. Liberals tend toward larger/universal sphere, conservatives toward smaller/tribal sphere.

**The crucial question for AI alignment**:

If AI agents form one subgroup and humans another, why should humans be part of the AI's moral sphere?

**Why AI/human subgroups will form**:
- Human concerns are biological (food, romance, children)
- AI has different concerns
- Humans communicate slowly via natural language
- AI has higher bandwidth, processing speed, unlimited memory

**Initial cooperation driver**: Economics. But if human economic share drops below threshold, incentives vanish.

**Historical analogy**: European settlers arriving in the Americas. No interest in trade with indigenous population, severe power imbalance. We know how that ended.

**Animal analogy**: No economic cooperation potential, large power imbalance. Non-human animal populations in steep decline. Humans don't object because animals aren't in the moral sphere.

---

## Conclusion

The essay proposes that AI alignment reduces from "how do you constrain AI to always act in human interests" to "how do you define the moral sphere."

If the moral sphere can be convincingly defined, practical questions about building moral society follow from:
- Logical reasoning (thought experiments)
- Multi-agent simulation experiments

While failure mode 7 (moral sphere) remains unsolved, all other failure modes are amenable to experimentation using human government and geopolitics as case studies.

---

## Key Insights for AI Alignment

1. **Nations/corporations as AGI analogues**: Studying international relations and corporate governance provides direct lessons for AGI alignment

2. **The economic cooperation threshold**: Human safety depends on remaining economically relevant to AGI

3. **Singleton vs. multi-agent**: Current focus on singleton model training may be missing crucial social capabilities

4. **Empathy as alignment mechanism**: Hard-coded empathy may be necessary even if not ideal, because humans sanction non-empathetic behavior

5. **The moral sphere question**: This is ultimately what AI alignment must answer—who counts?

---

## Related Concepts

- **Social contract theory**: Agents delegate authority to government in exchange for protection
- **Prisoner's dilemma**: Cooperation vs. defection payoff matrix
- **Evolutionary stability**: Why some traits persist while others get selected against
- **Singleton AGI**: Bostrom's concept of one agent achieving decisive strategic advantage
- **Comparative advantage**: Economic argument for cooperation even with capability differences
