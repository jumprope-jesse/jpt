---
type: link
source: notion
url: https://www.lesswrong.com/posts/zbDh4qS6ABHBp2tis/morality-as-cooperation-part-ii-theory-and-experiment
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-12-05T13:03:00.000Z
---

# Morality as Cooperation Part II: Theory and Experiment — LessWrong

## Content (from Notion)

This is a Part II of a long essay. Part I introduced the concept of morality-as-cooperation (MAC), and discussed how the principle could be used to understand moral judgements in human societies. Part III will discuss failure modes.

# Part II: Theory and Experiment

The prior discussion of morality was human-centric, and based on historical examples of moral values that human societies have traditionally adhered to. This section will try to expand that reasoning to derive universal moral values from first principles, following a chain of logic that any rational intelligent agent should be able to follow.

The ideas presented here were influenced by Through the Moral Maze, By Robert Kane, the Kantian categorical imperative, and a dash of social contract theory. The particular setup described here also firmly follows the principle of Morality as Cooperation (MAC), as described in Part I.

In short, we wish to show that if there are tangible benefits to cooperation, then a group of intelligent agents will be forced to derive a protocol for cooperating in order to obtain those benefits. We will call this protocol a moral code. It is possible to reason about moral codes by using hypothetical thought experiments, following a process that will be described below.

It is also possible to test moral codes using real experiments. The "best" moral codes are those which provide the highest expected value to individual agents, within a group of cooperating agents that choose to adopt the code. Just as with human morality, moral codes can change and evolve over time. As a result, it is even possible to learn better moral codes by hillclimbing, e.g. by using evolutionary algorithms or gradient descent. In other words, we can use the same techniques to answer moral and alignment questions (i.e. simple optimization methods and lots of compute) that we use to train the AI agents themselves.

Finally, moral codes operate as a social contract which agents voluntarily agree to, in order to obtain the benefits of cooperation. Thus, the agents themselves may even provide a hillclimbing mechanism, by negotiating tweaks to the moral code among themselves in order to improve their own individual fitness.

We would further like to show that good moral codes are stable Nash equilibria. And if at all possible, we would like to show that hillclimbing on moral codes will result in a stable equilibrium that humans would generally regard as "good", and in which humans and AI can peacefully coexist and cooperate, thus solving the AI alignment problem. To be clear, alignment is not yet "solved"; failure modes will be the subject of Part III.

## Basic setup

Assume the following:

1. There is a group of intelligent agents which interact and can negotiate with each other.
1. Each agent has one or more objectives, and different agents may have different objectives. Agents will generally act selfishly in order to maximize the payoff from their personal objective functions.
1. It is possible for agents to either cooperate with each other, or to defect. Cooperation involves choosing actions that are mutually beneficial to agents within the group (e.g. trade). Defection involves choosing actions that may involve personal gain, but where that gain comes at the expense of other agents (e.g. theft). It is safe to assume that the payoff matrix broadly resembles the Prisoner's Dilemma.
1. Cooperation is a positive-sum game. As in the Iterated Prisoner's Dilemma, agents which consistently choose to cooperate with each other will obtain greater benefits over time (jointly, in expectation) than agents which do not cooperate. Following the principle of instrumental convergence, "benefits" in this case are assumed to be somewhat universal (e.g. money, power, status, compute), and thus are valuable in the pursuit of most objectives. In other words, even though the agents may have different objectives, there is still a universal incentive to cooperate. The most obvious "benefit" is protection from harm; the ability to pursue an objective with minimal interference from other agents. Another example is access to additional resources due to trade and specialization of labor.
1. Agents may choose to follow a moral code, and different agents may follow different codes. A "moral code" defines the set of actions or behaviors that the agent is willing to take in pursuit of its objectives. Some actions (e.g. "killing humans") may be prohibited, while others (e.g. "pay taxes") may be obligatory. The moral code does not define which particular actions an agent may choose to take at any point in time; it merely provides a framework that constrains the set of allowable options. Note that we do not initially make any judgements about which moral codes are "right" or "wrong". These judgements will be derived later from first principles or experimentation. Moral codes should also be expressed in such a way that agents can communicate and negotiate over codes.
### Discussion

There are two main differences between this framework and most prior work on cooperation in game theory. First, we assume that different agents have different objectives. In other words, different agents may be playing entirely different games, which complicates the analysis.

Second, we have introduced the concept of a moral code. A moral code is not a strategy in the traditional game-theoretic sense, because it does not prescribe a particular action. Instead, it merely defines constraints on actions. The simplest moral code is the empty set, meaning no constraints, or in a group setting, total anarchy. Different agents may employ different strategies (or indeed, pursue entirely different objectives) while still obeying the same moral code. Instead of searching for a Nash equilibria over strategies, we hope to find equilibria over moral codes.

### Obligatory cheesy example

Assume there is a group of interacting agents, which contains the following 3 members. One agent wishes to turn the universe into paperclips, which means killing or subjugating all other agents that are a threat to its power, using any available means. A second agent may wish to maximize profit, where profit is obtained by selling goods and services at consensually negotiated prices to other agents. A third agent may wish to preserve biodiversity, using any non-violent means. The objectives here are { paperclips, profit, biodiversity }, and the moral codes are { none, consensual trade, nonviolence }.

As should be obvious from the example, some objectives and behaviors will necessarily be incompatible, leading to a conflict between agents. Profit may conflict with biodiversity, and being turned into paperclips conflicts with pretty much everything. As a result, the agents within an interacting group must make a moral judgement to arbitrate the conflict between them. A moral judgement will label certain actions as being "morally acceptable", while other actions are labelled as "morally wrong", and thus prohibited. Failure to arbitrate will result in a failure to cooperate, possibly to the point of open warfare between agents, which is detrimental (jointly, in expectation) to all members of the group.

Ideally, the moral reasoning process should generate the following judgements:

First, the paperclip maximizer is clearly evil. This is not because paperclips are bad -- we do not value biodiversity over paperclips a priori. Rather, a moral code which allows the killing and subjugation of other agents is logically inconsistent, because it violates the Kantian principle of universalizability, as will be described below. This is a total moral failure on the part of agent 1, and other agents in the group would thus be morally justified (and indeed obligated) in taking any necessary action to eliminate agent 1 as a threat to the group. Agent 1 presumably knows this, and could choose to update its moral code to avoid such retribution.

For agent 2, maximizing profits is usually fine, so long as the negotiated prices are consensual. However there are various potential complications, e.g. attempting to corner the market and establish a monopoly, engaging in coercion and blackmail, selling addictive substances that hijack other agents' prior objectives, sales based on deceptive or false information, negative externalities, etc. These are more subtle failures that require additional moral reasoning. In the end, agent 2 may also be compelled by the group to adopt additional restrictions beyond just "consensual prices."

Similarly for agent 3, non-violence is also not a sufficient constraint, because it does not rule out theft, election hacking, etc.

Thus, in all three cases, the moral reasoning process should result in a refinement to the moral code that each agent holds, with the goal of establishing a consensus: a universal moral code that all agents agree to follow. Moreover, the basic pattern of refinement is to restrict those actions which would violate the basic rights of other agents to pursue their own objectives. This process of ever-increasing restriction is self-limiting, because an overly restrictive and draconian moral code would also prevent agents from pursuing their own objectives.

The expected equilibrium from this process should thus be a moral code that provides each agent (in expectation) the maximum ability to pursue its own objective, while still respecting the ability of other agents to purse their own objectives. Agent 1 will make as many paperclips as possible, so long as it does not interfere with Agent 2's desire to make as much profit as possible. Perhaps Agent 2 will sell steel to Agent 1, while Agent 3 looks on helplessly from the sidelines.

## Reasoning about moral codes: the principal of universalizability

In a world of imperfect information, the ultimate objective of an agent is generally not visible to other agents, and it is thus impossible to make moral judgements about the objectives themselves. What is visible are the actions that an agent has taken in pursuit of its objective, so it is actions that we wish to judge. Moral judgements about actions proceed in three phases:

1. A naive judgement selfishly assigns an initial score of "good" or "bad" to a particular action in a particular situation.
1. A categorical judgement generalizes naive judgements to general logical rules over types (or categories) of actions.
1. A moral judgement determines whether the general rule is universalizable.
Each agent continually makes naive judgements about the actions of other agents. These naive judgements are selfish; each agent is evaluating whether the particular actions taken by other agents are good or bad for it personally. E.g. if a competitor gets killed by another agent, that might be "good", but if a valued trade partner gets killed, it might be "bad".

Given a set of observations and naive judgements about specific actions in specific circumstances, it is possible to start deriving simple logical rules that determine whether some types of actions are good or bad in general. For example, within a group of cooperating agents, murder is generally bad in expectation, because it disrupts patterns of cooperation. Generalization abstracts away from the particular details of an action as much as possible, in favor of simple "rules of thumb" that can be easily communicated to other agents. These simple rules of thumb will then form the basis for moral codes.

Generalization by itself is not sufficient for moral reasoning, however, because it is still purely selfish. To determine whether a candidate rule is truly "good" or "bad" in a moral sense, agents must perform a hypothetical thought experiment. If all other agents were allowed to take similar actions in similar situations, what would be the result? In other words, if a particular action was made universally admissible, or universally required, would it generally help or hinder other agents in the pursuit of their objectives? Actions which are generally helpful to other agents are "good", actions which generally hinder other agents are "bad", and all other actions are "neutral".

The idea of universalizability comes from Kant's categorical imperative. It is what transforms selfish judgements (what is good for me personally), into moral judgements (what is good for the group or society as a whole). This change of focus from "good for me" to "good for the group" is also the crux of reasoning about Morality as Cooperation. The golden rule -- "do unto others as you would have them do unto you" -- is a simpler way of stating the same principle, which considers only bilateral relationships.

By performing a number of hypothetical thought experiments, it is possible to derive a universal moral code: a comprehensive set of rules that can be universally adopted by all agents within the group.

### Further examples

Communal obligations. In addition to prohibiting certain actions that are harmful to other agents, a moral code may establish obligations, for which the same reasoning applies. If all agents were hypothetically required perform an action, would that help or hinder the ability of other agents to achieve their objectives? Obligations are subject to a cost/benefit analysis. For example, levying a tax to support a formal government and legal system will likely yield benefits greater than the cost.

Enforcement. In any positive-sum cooperative game, free riders are a potential problem. A moral code that does not include any enforcement mechanism is vulnerable to exploitation by free riders, and is thus not a stable equilibrium, which is bad for the group. Thus, a cooperating group of agents necessarily have a moral obligation, built into the code itself, to detect violations of the code and ostracize or punish criminals.

Parsimony. While moral codes provide benefits, they also impose costs in terms of both regulations that restrict what agents can do, and regulatory overhead in enforcing the code. Moreover, moral reasoning involves hypothetical thought experiments where uncertainty is high and the margin of error is wide. The optimum moral code is thus one which is as simple as possible, and contains only those prohibitions and obligations for which the evidence is strong.

Based on simple logical reasoning, we expect that any universal moral code will include many of the observed human morals described in Part I.

- Liberty: the freedom to pursue private objectives.
- Prohibitions against harming other agents.
- Private property rights and prohibitions against theft, in order to facilitate trade.
- A commitment to truth and honesty, to facilitate negotiation and business deals.
- Legal enforcement mechanisms to protect against free riders.
- Respect for authority, assuming decision-making is hierarchically structured.
### Example: resolutions to a moral paradox

Universalizability neatly resolves several moral paradoxes that would otherwise occur within a strictly utilitarian or consequentialist framework. Consider the following scenarios.

(A) A firefighter rushes into a burning building. In one part of the building, a single person is trapped in a room, while in another part of the building, 5 people are trapped in a room together. The firefighter only has time to clear the debris from one doorway before the building collapses, and thus chooses to save 5 people instead of 1.

(B) The infamous trolley problem. A runaway train is hurtling down the tracks towards a group of 5 people. An engineer chooses to pull a lever to divert the trolley onto a different track, where it only kills one person instead.

(C) The fat man. A trolley is hurtling down the track towards a group of 5 people. A bystander notices that the trolley can be stopped by something heavy enough. As it so happens, a fat man is standing on a bridge, so the bystander pushes the fat man off the bridge, into the path of the trolley, and thus saves the 5 people.

(D) A doctor has six patients. Five of the patients are in immediate need of an organ transplant or they will die. The sixth is healthy, and a universal donor. The doctor kills the sixth patient, and harvests her organs to save the lives of the other 5.

Notice that in each case, one person decides to sacrifice the life of another person, in order to save the lives of 5 other people. According to utilitarianism or consequentialism, all four scenarios are equivalent, and the action in each case is an unalloyed good, because the net effect is to save 4 lives. However, in surveys, most people do not find these situations to be equivalent at all. Most people believe that (A) is clearly good, (B) is probably good, (C) is clearly wrong, and (D) is absolutely wrong. As it turns out, the principle of universalizability matches human intuition, and logically explains why these four situations are distinct.

In the case of (A), the firefighter is risking his own life to save the life of another, which is clearly a "good" action, no matter what he decides. According to MAC, self-sacrifice for the group is always good, and if the firefighter does nothing then all 6 people will die. Thus, either decision would be actually be OK, but saving 5 people is the greater good.

In the case of (B), the engineer is not making a personal sacrifice. However, the trolley problem has been contrived so that the engineer is forced to make a decision. She must either choose to either pull the lever or not, and an innocent person is going to die either way. Thus, saving 5 people is again the greater good.

The scenario of (C) at first seems similar to (B), but the action of pushing an otherwise innocent person off of a bridge is qualitatively different, because it is the exactly kind of action that would generally be classified as "murder" in any other circumstance (see generalization, above). As a result, it fails the universalizability test. If anybody was allowed to murder somebody else, just because they personally thought that killing them would make the world a better place, then the result would be chaos. In most legal systems, the only justification for murder is self-defense.

Scenario (D) is even worse, because in addition to committing murder, the doctor is violating a sacred oath to care for the lives of his patients. If doctors were allowed to routinely kill otherwise healthy patients, then everybody would be too terrified to seek medical care.

Note that universalizability does not mean that consequences don't matter. It just means that in order to determine whether an action is right or wrong, you must consider what the consequences would be to the group as a whole, if everyone were allowed to take similar actions in similar circumstances. This is why moral codes are distinct from individual actions.

## Negotiating moral codes: introducing the social contract

Every agent can use the reasoning process outlined above to derive its own version of a "universal moral code" -- a set of rules which that particular agent believes that all agents (including itself) should follow. We further expect most agents to agree on certain universal moral principles, such as protection from harm.

Nevertheless, different agents do have different objectives and priorities, and hypothetical thought experiments are always prone to error. As a result, agents are unlikely to agree on all of the details. After all, humans have been arguing about morality for thousands of years; non-human agents will doubtless be similar.

The principle of universalizability demands that a given moral rule must apply to all agents, otherwise it is not universal. As a practical matter, this means that all agents within a group must agree to follow the same moral code in order to cooperate effectively. If agents do not agree on a moral code a priori, then they must negotiate with one another to establish a consensus. This is why the generalization requirement above specifies "simple 'rules of thumb' that can be easily communicated to other agents".

The idea that supposedly "universal" moral codes can vary, and are open to negotiation, deviates sharply from Kant's philosophy. Negotiable moral codes instead resemble a social contract:

1. Agents voluntarily choose to follow a moral code, in exchange for the benefits of cooperation. In general, an agent will choose to follow a code only if the benefits (e.g. not being killed) outweigh the costs (e.g. not being able to kill). For a less violent example, the cost of paying taxes is less than the expected benefit of having an orderly society with public goods and a social safety net.
1. Moral codes can be communicated, and agents can publicly declare to other agents which moral codes they follow. E.g. "I am a christian / liberal / communist / environmentalist etc."
1. Compliance with any given moral code is verifiable by other agents, because moral codes consist of easily-interpretable rules. If Judaism says "thou shalt not kill", and an agent kills another agent, then it is easy for other agents to determine that the first agent has violated the code of Judaism. To use a programming-language analogy, a moral code acts as a type system for agent actions.
1. Agents may make decisions based on declared moral codes, or on observed violations of a moral code. For example, "I will only do business with other environmentalists." Or, "If I see other agents violating the law, I will call the police, and help to ostracize and punish them."
1. Agents can negotiate over what rules should be in a given moral code. If all agents agree (as part of adopting the moral code) to be bound by the decisions of the majority, then the result is a democracy.
When viewed as a social contract, the principle of universalizability serves a pragmatic role. If a moral code is designed from the outset to be universal, meaning beneficial in expectation for all agents in a group, then it will be much easier to get all of the other agents to agree to it.

Note that it is not necessary for agents to agree about why certain actions are good or bad; they just need to agree. It is also not necessary for agents to have identical moral codes, so long as they agree to a certain minimal common subset. As with any negotiated agreement, some horse-trading may be involved in order to arrive at a consensus, and some agents may reluctantly decide to follow a moral code they disagree with, in order to obtain the benefits of cooperation.

## Evolving and optimizing moral codes

The fundamental weakness of moral reasoning is that it relies on hypothetical thought experiments. Thought experiments are useful for building intuition, and it is possible to figure out the broad outlines of what we expect a universal moral code to look like. However, thought experiments can also be wildly inaccurate, and are prone to motivated reasoning and unintended consequences. Intelligent agents (both human and AI), are also exceedingly good at exploiting weaknesses in formal specifications to do reward hacking of various kinds. There no reason to expect that exploitation of moral codes would be any different.

The alternative to hypothetical thought experiments is to do real experiments. The fundamental hypothesis that underlies Morality as Cooperation is that human notions of "right" and "wrong" have evolved over time according to the principle of natural selection. Different groups of people have held different moral codes, expressed as combination of genetics, cultural beliefs, religious beliefs, traditions, and written laws. This situation created a natural experiment in which the efficacy of different moral codes could be compared against each other. Those groups which had "better" moral codes were able to cooperate more effectively, and were thus more successful. They either outcompeted other groups entirely, via group selection, or their ideas were adopted by other groups, via horizontal meme transfer. (See Part I -- "The evolution of cooperation.")

Moreover, moral codes can evolve even within the context of a single group. A moral code is a collection of rules, and individual rules can be added, removed, or altered at any time. Adding or changing a single rule is itself a natural experiment, by observing the effect of the rule on society before and after the change. Studying those effects is the domain of the social and economic sciences. For example, "Does increasing criminal penalties reduce crime?" Or "Does increasing the minimum wage increase unemployment?" A modern representative democracy has an entire branch of government dedicated to creating, refining, or repealing laws on a continual basis, and a well-functioning government is one which uses evidence-based reasoning to decide which laws to pass or repeal. (The question of whether or not our current governments are well-functioning is left as an exercise for the reader.)

### Multi-agent simulation

Real-world experiments are time-consuming, expensive, and in some cases (e.g. nuclear proliferation or AI alignment), potentially catastrophic for the human species. Simulation provides a middle ground between purely hypothetical thought experiments, and real-world experiments. Simulation abstracts away from some of the complexity of the real world, while still providing the opportunity to observe emergent phenomena that are not necessarily obvious from first principles. From the perspective of AI alignment, the overwhelming advantage is that many simulations can be run with simple agents that do not have super-human intelligence.

The iterated prisoner's dilemma (IPD) has been widely studied in the literature as a model of social cooperation, and is a good example of how to use simulation to do meaningful experiments into cooperation and morality. Strategies like tit-for-tat usually perform well; such strategies both cooperate by default, and include mechanisms for enforcement that punish defectors (free riders). Similar strategies have been shown to spontaneously evolve using a variety of evolutionary or reinforcement-learning approaches.

Unfortunately, IPD is overly simplistic for a number of reasons:

- The payoff matrix is extremely simple. Unlike the real world, IPD agents don't need to coordinate their actions in order to perform complex tasks.
- Agent interactions are always bilateral. There is no way for multiple cooperating agents to band together in order to punish defectors, which is a crucial component of real-world enforcement mechanisms.
- Agents are not divided into groups, so there is no distinction between in-group and out-group. As mentioned in Part I, humans typically operate within a number of overlapping and concentric groups which have different moral precedence. Furthermore, as will be discussed in Part III, group fragmentation is perhaps the single most important failure mode for cooperation, so this is a crucial area for experimentation.
- There is no mechanism for agents to communicate, which has been shown to dramatically improve cooperation, especially in human-machine interaction.
- Since there is no communication, there is also no way to investigate issues related to honesty and trust which are also critical for AI alignment in general.
- IPD does not distinguish between strategy (which actions to take) and the moral code (which actions are permitted). Thus, there is no way to study how agents with different strategies can agree to follow the same moral code, or to study how moral systems can accommodate agents which have different objectives. There is also no way to study how agents can "game the system" by exploiting weaknesses in the moral code, another issue which is highly relevant to AI alignment.
### A proposed framework for studying morality

For the most part, the weaknesses of IPD could be resolved simply by switching to a more complex simulation environment. I propose the following:

1. A simulated world in which agents can pursue various open-ended objectives. There should be opportunities for multi-lateral group interactions, agent-agent communication, trade, and specialization of labor. As with IPD, there should be opportunities to both cooperate (perhaps via trade) and defect (perhaps via combat). Computer games provide a wealth of inspiration as to how such environments can be constructed. Unlike most games, there is no need for accurate physics or graphics.
1. Intelligent agents are trained via reinforcement learning (RL) to maximize individual objective functions. There is a large literature on training RL agents in simulated environments. For the purpose of studying morality as cooperation, agents must have the ability to communicate with other agents, organize into groups, and advertise group identity.
1. Moral codes are specified via a domain-specific language (DSL) which establishes logical constraints on agent behavior. The main requirement of the DSL is that it must be possible to programmatically detect when a particular agent action violates the code, and for other agents to observe the violation.
In the real world, agents must be intelligent enough to perform moral reasoning, and to negotiate a consensus over moral codes. However, reasoning and negotiation require a very high degree of intelligence, which is probably beyond the capability of current LLMs, and would be expensive to simulate in any case.

For the purpose of simulation, reasoning and negotiation are unnecessary. In order to ensure universalizability, it is sufficient to assign moral codes by fiat. Every agent is born into a group with a particular moral code, and all members of the group share the same code. Individual agents will then use RL to maximize their own fitness, conditional on the moral code. This setup is not unlike human morality; humans are similarly born into a particular society and religion, with proscribed rules which they must learn to follow.

Moral codes, in turn, are evaluated based on the overall fitness of the group, potentially in the presence of interaction with other groups. Because moral codes are specified symbolically, they can be optimized via genetic algorithms or evolutionary strategies.

Notice that this setup produces an adversarial relationship between the moral code, which evolves slowly to maximize the fitness of the group, and the strategies of individual agents, which are trained via RL to maximize individual fitness within the group, potentially by exploiting other agents or weaknesses in the moral code. This adversarial relationship is exactly what we want to study for the purposes of AI alignment.

## Comparison against other philosophical systems

Moral reasoning by means of a hypothetical thought experiment in which an action is somehow made "universal" is due to Kant. Unlike Kant, however, I do not assume that agents are rational, that agents will necessarily agree with each other, or that free will has anything to do with it. Like Kant, I assume that it is possible to reason about morality, but reason is not the only way to establish a universal moral code. Moral codes can be established via negotiation, horse-trading, and consensus building, in the same way that legislation is passed in modern democracies. Alternatively, moral codes can be derived experimentally, as part of an evolutionary process, even among a population of irrational or semi-intelligent agents.

Hofstadter uses the principle of universalizability to define super-rationality. A super-rational agent is one which takes rational actions, under the assumption that all other agents are also super-rational and will take the same action. Super-rational agents can solve the one-step (non-iterated) prisoner's dilemma, and other complex cooperation problems. However, super-rationality requires that all agents independently arrive at the same conclusion through logical reasoning alone, and that free riders don't exist, assumptions which are far too brittle to be practical. Hofstadter's experiments conclusively showed that humans are not super-rational, even if you select a small group of the most intelligent and logically-minded.


