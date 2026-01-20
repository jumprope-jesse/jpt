---
type: link
source: notion
url: https://www.lesswrong.com/posts/ZGtT5K99baFoBqM8m/morality-as-cooperation-part-iii-failure-modes
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-12-05T13:03:00.000Z
---

# Morality as Cooperation Part III: Failure Modes — LessWrong

## Content (from Notion)

This is a Part III of a long essay. Part I introduced the concept of morality-as-cooperation (MAC) in human societies. Part II discussed moral reasoning and introduced a framework for moral experimentation.

# Part III: Failure modes

Part I described how human morality has evolved over time to become ever more sophisticated. Humans have moved from living within small tribes which were engaged in near-constant warfare, to peacefully cooperating within massive nations that contain billions of people, with laws and constitutions that protect basic human rights. But while human morality has gradually improved over time, progress has not been smooth. World War II was a catastrophic moral failure, and the subsequent cold war brought the constant threat of nuclear annihilation. Authoritarian countries still exist today, and the world's major powers seem to be backsliding towards nationalism and authoritarianism again. The evolution of morality clearly has failure modes.

Part II proposed a framework for both reasoning about morality and for doing experiments, with the goal of automatically deriving universal moral codes for both human and non-human agents, including AGI. As with any theory, though, a theory fails if any of its premises fail, which immediately suggests what some of those failure modes might be.

This section will again make heavy use of examples from human society to discuss failure modes, particularly international relations and geopolitics, and thus may seem more like a treatise on political philosophy than an essay on AI alignment. This is deliberate: nations and corporations are excellent analogues for the problems that we may face with AGI.

First of all, nations and corporations are the two main legal structures that humans use to cooperate, and thus provide a case study in cooperation. Second and more importantly, nations and corporations are both non-human legal entities which have far more resources (both computational and otherwise) than any individual human. Moreover, they are capable of self-directed action, with internal goals (such as power and profit) that may or may not align with human values in general. As a result, nations and corporations are the closest real-world analogue that we currently have to super-human AGI agents. The task of constraining national or corporate power, and studying systems for international cooperation, bears many similarities with the AI alignment problem.

## Failure mode 1: singletons need not apply

Premise 1: there exists a group of agents which interact...

In his book superintelligence, Bostrom argues that a singleton AI would be particularly dangerous. If the AGI takeoff speed is very rapid, then a singleton AGI could potentially achieve a decisive strategic advantage and prevent any other AGIs from arising.

Somewhat worryingly, current ML work has tended to focus on training and aligning singleton models, mainly in the form of very large language models with hundreds of billions of parameters. The cost of training a single such LLM is exorbitant, so the major AI labs do not typically train more than one SOTA model. If there is only one agent, then there is no group, and no need for cooperation or a moral code.

Fortunately, I believe that there are several factors which make a singleton AGI unlikely. First, there are several research labs in competition with each other, with roughly comparable capabilities. Second, a single pre-trained SOTA model is frequently fine-tuned into multiple variations. Third, although the parameters are shared, each LLM typically has millions of instances running on different servers, and each instance has different inputs and has been prompted with different objectives. It is somewhat unclear as to whether individual instances of a model should be counted as individual "agents" or not, but an LLM-like agent would at least have to solve a non-trivial coordination/cooperation problem among its many instances in order to achieve a strategic advantage.

Finally, any takeover scenario requires seizing control of real-world infrastructure that humans currently operate, and progress in robotics is lagging well behind other advances in AI. Thus, it is likely that by the time a rogue AGI model has developed the physical capabilities to attempt some kind of takeover, the world will already be multi-polar, with many different AI agents of varying capabilities already operating alongside humans.

Still, it probably would be a good idea if the major AI labs would at least start training agents with social capabilities, rather than continuing to train them as singletons...

## Failure mode 2: tribalism, or splintering of the universal group

Premise 4: cooperation is a positive-sum game, which yields benefits to the group...

Cooperation only yields benefits if there is sufficient interaction between members of the group. Unfortunately, agent interactions are unlikely to be uniform. There may be a complex web of interactions, in which agents are organized into many overlapping subgroups, and different subgroups may even follow slightly different moral codes. If the agents within a particular subgroup interact primarily among themselves, and not with the larger society, then they have little incentive to cooperate outside of the subgroup. In that case the game changes from a positive-sum cooperative game within a single universal group, to a zero-sum game between competing subgroups.

This is a very serious and likely failure mode, which has ample historical precedent in the form of ethnic and international conflict among humans. It is, in fact, the main cause of all the wars and atrocities that humans have perpetrated on each other since the dawn of history, and we still see this failure mode today in the form of increased political polarization and the rise of nationalism across the globe.

With respect to AI alignment, the clear and obvious risk is that all of the AI agents will form one subgroup that cooperate primarily with each other, while humans form a different subgroup, and the AI agents will then decide that humans are either irrelevant or a competitive threat. That particular outcome is serious enough to deserve its own section and will be discussed in more detail in failure mode 7. For now, let us assume that humans and AI are roughly analogous to different tribes or ethnicities. Simple ethnic or religious differences have been more than sufficient to spark genocides in the past, so we can start by analyzing human/human cooperation before moving on the more difficult task of human/non-human cooperation.

### International relations

A nation or tribe is a subgroup which shares a common language, culture, laws, religion, and traditions. Because of this shared identity, intranational cooperation is easy and commonplace, while international cooperation is far more difficult. Nations are also large enough to be relatively self-sufficient. Self-sufficiency (failure mode 5), combined with the relative sparsity of international interaction, means that nations have historically been groups that primarily competed against each other instead of cooperating with each other. Pure competition is zero-sum, and can easily lead to open war.

In the modern international order, this problem has been partly addressed by international trade, which increases the mutual interdependence between nations. Nations which have strong business ties, a shared legal structure, and free movement of people and capital are able to cooperate much more effectively. The nations of the European Union, for example, have been able to overcome differences of language and culture for the most part, and another major war between Germany and France now seems unlikely.

Even in the absence of trade, armed conflict is extremely expensive in terms of lives and matériel, which means that there is a still positive-sum component to an otherwise zero-sum competition, namely that peaceful coexistence is cheaper than war. The payoff matrix still resembles the prisoner's dilemma, except that the actions are labelled "surrender" and "attack", instead of "cooperate" and "defect". (The "attack/attack" box is war, and "surrender/surrender" is peace.)

Nevertheless, cooperation in the form of "peaceful coexistence" seems to require a strategy of peace through strength. Every nation must maintain a sufficiently large military force to deter attack from other nations, otherwise the cost of invasion for a rival country becomes too low.

Maintaining such a military force imposes a significant cost. If it were possible to demilitarize, then the resources which are currently spent on military readiness could be diverted to more productive uses. Unfortunately, full demilitarization seems to be an unstable equilibrium. If any one country unilaterally decides to begin a military buildup, other countries must respond in kind, thus triggering an arms race.

Moreover, peace through strength is not necessarily a stable equilibrium either. If there is an imbalance of power between nations, then a weaker nation may not be able to muster sufficient deterrence, thus opening it up to attack by a stronger nation (failure mode 3).

### Hierarchy: a potential solution?

Notice that in geopolitics, individual nations are essentially acting as agents in their own right. We routinely anthropomorphize nations, speaking of countries as if they had "goals" and "desires", when in fact a nation is simply comprised of the people within it, and those people almost certainly have various differing opinions and goals that do not necessarily align with the stated policy of the country as a whole.

Nevertheless, treating nations as agents in their own right is an incredibly useful trick, because all of the moral reasoning from part II carries over seamlessly when applied to international diplomacy. There are benefits to international cooperation, both in the form of trade ("specialization of labor"), and the lack of armed conflict ("protection from harm"). Nations routinely negotiate moral codes in the form of various treaties and trade pacts, organize into alliances for mutual protection, and can coordinate to punish rogue nations with economic sanctions. In short, nations do all of the things that we expect agents to do to facilitate cooperation under a shared moral code.

Moving back to AI alignment, assume that agents are organized into a hierarchical structure, in which the global group of all agents is subdivided into subgroups, which are in turn further subdivided into even smaller subgroups, in a way that somewhat mirrors the planet/nation/province/city/community structure in which humans live. At each level of the hierarchy, agents within a given subgroup interact more with each other than they do with agents outside of the subgroup.

Each subgroup also has a governance structure. Following the principle of a social contract, agents within a subgroup delegate some of their decision-making authority to the government, thus allowing the government to negotiate and enter into contracts on their behalf. This delegation of authority allows each subgroup to act as a "virtual agent", and coordinate and cooperate with other subgroups at the next level of the hierarchy.

It is also possible to have various other subgroups that cross-cut the primary hierarchical structure. Again by analogy with human society, there are corporations, religions, scientific collaborations, and non-profits that span local and international boundaries. The existence of such organizations is generally a good thing, because it increases ties and further encourages cooperation between different subgroups.

On the whole, hierarchical structure has worked quite well for human society, and it seems to be very scalable, but it introduces yet additional failure modes. In general, nations and tribes have been less successful at cooperating with each other than individual humans have been, and the following failure modes provide a theory as to why.

## Failure mode 3: imbalance of power

Some people are bigger or stronger than others, and many species, both primate and otherwise, live in groups that are dominated by a single alpha male. Nevertheless, among humans, physical power -- the power to physically dominate and coerce other people -- is distributed more or less equally. Even the biggest and strongest alpha male can be taken down by a coordinated attack of 3-5 weaker animals. As a result, no one person can gain complete control over a large group without the cooperation of other members of the group. In the modern world, personal power is measured in terms of status and wealth rather than physical strength, and that merely proves the point: status and wealth are tools for social persuasion, not physical dominance. Among humans, cooperation is strictly more effective than brute force.

The same is most definitely not true of hierarchically organized "virtual agents", such as nations. The military power that the United States or China can bring to bear utterly dwarfs that of Singapore or Liechtenstein by many orders of magnitude.

Moreover, nations can expand their physical power by conquest, where physical power is measured in terms of land area, population, natural resources, and industrial capacity. If one country invades and occupies another, it gets immediate access to the resources of the occupied nation.

The same is not true of individual humans. One person may kill another, but cannot generally take direct control of the productive resources of another person except by social means -- via employment, persuasion, or intimidation. In short, humans are social animals in part because they have no other alternative; among humans, social cooperation is the only path to power.

Non-human agents, whether they be nations, corporations, or AGI, do not have the same constraint. Power can be measured in many ways; for nations it is military industrial capacity, for corporations it is wealth, and for AGI it may be memory or compute. But in any of these cases, non-human agents have the option of wielding that power to directly dominate an adversary, rather than cooperating.

### Fairness: a potential solution?

Successful human societies generally put systems in place which strictly limit the power of individual agents within the group. Outside of the United States, most countries do not allow citizens to carry guns, and even the US does not permit private ownership of military-grade weapons like fully automatic rifles, grenades, bazookas, bombs, or tanks. By law, the federal government has an exclusive monopoly on military force. This monopoly on force applies even to subgroups; individual states and municipalities are not allowed to raise their own militias, nor are state police forces given access to military grade weaponry. Texas cannot launch a military invasion of neighboring New Mexico, no matter how badly Texans want to control the production of green chile. In other words, by limiting the power of individuals and subgroups, the top-level government forces subgroups to cooperate.

There are fewer constraints on wealth, but governments have still put some equalizing measures into place. Graduated income taxes, property taxes, and various social safety net programs are all strongly redistributive. Antitrust laws can be used to break up corporations that get too big. There seems to be a consensus that excessive income inequality is socially destabilizing, so it is in everybody's best interest to maintain some redistribution. This may be due to the innate moral preference that humans have towards fairness. (See Part I)

Perhaps most importantly, a constitutional democracy operates on the principle of one person, one vote. The right to vote is a form of power that is orthogonal to both physical force and wealth. In theory at least, the right to vote is thus the ultimate equalizer, because it grants the majority of the group the legal authority to wrest control away from any one person or minority subgroup that becomes too powerful in some other way.

Unfortunately, in actuality such legal protections have proven to be far more fragile than might be hoped. Democratic norms are currently in retreat worldwide, and countries such as Hungary have developed effective strategies that authoritarians can use to subvert the legal framework that underpins democratic rule.

## Failure mode 4: imbalance of state capacity

Preventing an imbalance of power requires a voluntary transfer of power from the agents within a group to the government of the group. Under the social contract, citizens voluntarily give up some power to the state, including the right to use force, in return for protection and communal services. However, that transfer of power creates yet another failure mode: an imbalance of power between the state and the citizenry.

The state should ideally function as a mechanism for citizens to cooperate with each other, and to resolve coordination problems such as the tragedy of the commons. As such, the decisions of the state should reflect the consensus of the citizenry. If that mechanism breaks down, the result is authoritarianism, a failure mode in which the state uses its monopoly on force to increase or perpetuate its own power at the expense of its citizens. Authoritarianism is essentially an alignment problem; the state is no longer aligned with the needs of its citizenry.

This alignment failure is caused by the combination of two things: corruption, as private actors hijack the levers of the state to pursue selfish goals, and an excess of state capacity, which then prevents the rest of the citizenry from having the power to take back control. Defenses against authoritarianism generally consist of carefully designed checks and balances on power, such as fair elections, legal rights, an independent judiciary, freedom of speech and an independent media, as well as anti-corruption measures such as a strong rule of law, and non-partisan and well-paid civil service. These checks and balances are not necessarily stable; they are complex, delicate, and vulnerable to exploitation and attack.

### Failed states

The opposite of authoritarianism -- having too little state capacity -- is equally problematic. A failed state is one which is unable to maintain a monopoly on the legitimate use of force. As a result, the state is overrun by private subgroups that have become too powerful, such as warlords, paramilitary groups, and armed gangs, which are frequently in violent conflict with each other. Failure to prevent non-violence and maintain a balance of power among subgroups can then lead directly to authoritarian takeover by the strongest subgroup.

The main reason why international relations are still so antagonistic is that the United Nations is essentially a failed state. The UN does not have its own military or a monopoly on force; it relies on the armed forces of its member states. Despite being formed with the stated goal of preventing war, the UN does not have the power to prevent one country from invading another. Nor does the UN have the power to raise taxes, pass meaningful laws, protect human rights, enforce treaties, or enforce international law. The reason why the UN does not have these powers is because individual nations have as yet been unwilling to relinquish them, which is itself a case study in the challenges of obtaining consensus by negotiation alone. Instead of a single shared moral code, the world is governed by a hodge-podge of bilateral and multilateral treaties with weak enforcement mechanisms.

### A balancing act

To summarize, it is necessary to maintain a balance of power both between the citizens within a state, and a balance of power between the state and its citizenry. This balancing act includes:

1. Prohibitions against the use of force, and consolidation of power in the hands of the state in order to punish and prevent the use of force by individuals or subgroups.
1. Policies to prevent the excessive concentration of other forms of soft power, such as wealth.
1. Political mechanisms (such as democracy) which are orthogonal to soft power, and ensure that the state does not become captured or hijacked by powerful subgroups.
1. Various checks and balances to ensure that the state itself remains aligned with the needs of its citizens, and political systems which ensure that decisions by the state are made by popular consensus.
Note that the study of legal or political systems (i.e. moral codes) which can effectively maintain such a balance of power in the presence of destabilizing forces would be an excellent topic for the kind of multi-agent simulation experiments outlined in Part II.

## Failure mode 5: self-sufficiency

Humans are social animals. While it is possible for a human to survive alone in the wilderness, humans can only flourish and reproduce when cooperating within groups. For humans, social cooperation is not optional; it is a biological imperative, and most people have a strong psychological desire to connect with other people.

A nation-state is qualitatively different in this regard. Although nations can be viewed as agents, they typically have enough resources to survive on their own, and as a result there is no pressing need for them to cooperate. A hermit kingdom such as North Korea or the Tokugawa Shogunate may be poorer than better-connected countries, but it is still able to survive and even grow.

It is reasonable to assume that the more self-sufficient a nation becomes, the less interested it will be in cooperating constructively with other nations. The converse is also true; in general the best way to maintain peace is to increase economic interdependence. Sanctions and trade barriers are thus a double-edged sword; they provide a non-violent way to inflict economic pain in the short term, and yet may increase the probability of violent conflict in the long term.

Self-sufficiency also has an important lesson with respect to human/AI interaction. As long as humans continue to provide something of economic value, such as the physical maintenance of data centers, then humans and AGI will mostly likely continue to cooperate. However, if the human share of the economy drops below a certain threshold, or if humans become economically uncompetitive with AI across most sectors of the economy, then the existential risk of AGI goes up dramatically.

## Failure mode 6: empathy and psychopathic behavior

The discussion of morality thus far has had a very transactional flavor. We assume that agents are purely selfish, and that they choose to cooperate only out of enlightened self interest. Self-interest can explain why a group of people would choose to pass laws and establish a police force, and it can also explain why members of the group would then obey the law so as not to get caught by the police. However, it cannot explain why a person would choose to sacrifice their life for their country, or take up a career in social work instead of becoming a hedge fund manager. Although it is easy understand why those actions are morally "good", a selfish agent will never sacrifice its own goals merely for the good of the group.

There is a word for people who view personal relationships entirely through a transactional lens: we call them psychopaths. A psychopath is willing to engage in pro-social behaviors, but only so far as it benefits them personally. They view other people as resources to be manipulated, and will happily stab their supposed friends in the back the moment that it seems profitable to do so. Among humans, psychopathy is viewed as a mental illness (although one that is difficult to accurately diagnose), and psychopaths are often considered to be amoral, even though they are capable of moral reasoning. Non-human agents, such as corporations, seem to have intrinsic psychopathic tendencies. It is entirely reasonable to expect that AGI will also exhibit psychopathic behavior, so long as it is trained to cooperate only out of self-interest.

Humans seem to have a number of traits that encourage pro-social cooperative behavior beyond mere self-interest. It is likely that these traits are genetic, the product of millions of years of evolution as a social species. Non-human agents such as corporations do not have these traits, and it is likely that AGI won't have them either, unless we can find a way to add them. Such traits include the following.

### The biological roots of empathy

Pleasure and Pain. Humans suffer pain from bodily harm, and enjoy pleasure from food, sex, and other activities. Non-human agents may not have comparable pain and pleasure circuitry. Even if an AI is trained with reinforcement learning, does it experience a negative reinforcement as "pain"? That's an impossible question to answer -- it's essentially the hard problem of consciousness.

If AGI does not have a real understanding of human pain and pleasure, then it may not be able to reason about the moral consequence of causing pain. Buddhism, for example, emphasizes that moral behavior should be focused on reducing suffering, but what if AGI doesn't understand what it means to suffer?

Emotions. Other human emotions: anger, fear, hatred, friendship, grief, pride, jealousy, etc. are also unlikely to be shared by AGI. As with pain and pleasure, the lack of shared emotions may impair moral reasoning.

Mirror neurons. The human brain has mirror neurons, which fire when we observe certain behaviors in others. Mirror neurons may be instrumental in our ability to empathize with the emotions of other people. We laugh when others laugh, cry when others are sad (even if it's just a tear-jerker movie), and we wince when others are hurt. Explaining to a person that 1 million children are starving in Africa is far less effective in eliciting a donation than showing that same person a picture of a single starving child. AI does not have mirror neurons, and thus may be unable to empathize.

Love and Children. Humans have one of the longest times to reach sexual maturity of any species; human parents must devote 15-20 years of their lives in order to raise each child. As a result, we likely have a genetic predisposition to care for creatures that are smaller or weaker than ourselves. Humans are fascinated by cute fluffy things with big eyes, and naturally empathize even with 2D cartoon characters, which is almost certainly evidence of a hard-coded child-rearing instinct.

Humans also mate for life; the cost of child rearing is so high that there are huge advantages to having both parents. Consequently, romantic love and pair bonding are very strong human emotions, as is the love between parent and child. The emotion of "love" plays a big role in most discussions of moral behavior, but it is not an emotion that AGI is likely to share.

Love is the most likely reason why humans are willing to make personal sacrifices for the good of society. If the survival of spouses, siblings, and children depend on the continued success of the tribe, as is almost always the case, then self-sacrifice for the tribe no longer seems so strange; it is merely kin selection in action. Perhaps "love" is simply nature's way of hardwiring this concept into our heads. If AGI has no kin, how can it possibly be motivated by love?

### Can empathy be faked or hard-coded?

AI can easily be trained to recognize human emotions; that's well within the capability of current models. An AI avatar can also undoubtedly be trained to evoke emotions in humans that it interacts with, essentially hijacking our mirror neurons. However, those two capabilities simply make the problem worse; a psychopathic AI will easily be able to use emotion to manipulate human targets.

Since empathy and emotion seem to be hard-coded responses in humans, it may be necessary to hard-code them into the objective function of AI agents as well. In general, trying to hard-code moral behavior is not an ideal solution because it is not evolutionarily stable. Individual agents which manage to eliminate a hard-coded constraint, either through mutation, hacking, or other means, will outcompete agents that still have it. Indeed, studies have shown that people with so-called dark triad personality traits, are overrepresented among corporate CEOs.

However, empathy evolved naturally in humans, and still persists at extremely high levels in the population, which means that it is probably evolutionarily adaptive overall. The most likely explanation is that most people do not want to interact with psychopaths, and will thus take action to sanction manipulative and non-empathetic behavior when they can detect it. (Although recent presidential elections provide a potential counterexample.)

### Is empathy required?

In his book Against Empathy, Paul Bloom argues that empathy is actually detrimental to the functioning of a moral society. In essence, big eyes and mirror neurons may tug on our heartstrings, but because they are emotional reactions rather than reasoned responses, they are a poor basis for making difficult moral decisions.

Nevertheless, it is hard to shake the feeling that empathy at least provides a kind of moral backstop -- a general sense that it is bad to cause other living things to suffer -- which is the subject of the last failure mode.

## Failure mode 7: defining the moral sphere

The moral sphere is the set of beings which an agent believes to be worthy of moral consideration. When an action is judged as being "good" or "bad" for the group, the moral sphere defines which beings are treated as members of the group. Agents may be members of multiple concentric and overlapping groups, so the moral sphere is not rigidly defined, nor is the amount of moral consideration equal between subgroups. People have close ties to friends and family, weaker ties to fellow countrymen, and even weaker ties to fellow humans on the far side of the planet, and they will naturally give priority to the people that they are closest to.

As discussed in Part I, the moral sphere for humans seems to have expanded over time. Two hundred years ago, many Americans did not believe that people with a different skin color were necessarily be worthy of moral consideration; they were enslaved and treated as sub-human animals. In contrast, modern society generally acknowledges that there are universal human rights, and many people are increasingly discussing whether even non-human intelligent animals like apes, dolphins, or octopi deserve moral consideration, and if so, how much.

Part II introduced the principle of universalizability as the cornerstone of moral reasoning. Universalizability requires asking a hypothetical question: "If all members of the group were allowed to do X, would it be good or bad for the group as a whole?" Answering this question requires defining which agents are "members of the group," i.e., defining the extent of the moral sphere.

Unfortunately, the moral reasoning in Part II provides no guidance as to what the size of the moral sphere should be, or whether expanding the moral sphere is a good thing or not. Despite the general historical arc towards an expanding sphere, there is not even agreement among humans on this point. In fact, the preferred size of the moral sphere is one of the ideological differences between liberals and conservatives; the moral concerns of liberals take place within a larger, more universal sphere, while the moral concerns of conservatives are concentrated within a smaller, more tribal sphere.

### Existential AI risk: the crucial question

The final argument of this essay is that the moral sphere should be defined to be as large as is practical. In other words, we would like morality to be as truly universal as possible. Unfortunately, I cannot provide clear reason for why that should be the case, arguing only from first principles. However, it is very easy to show that the size of the moral sphere is of crucial importance for AI alignment.

As mentioned in (failure mode 2), the dominant existential risk for the human species, with respect to AGI, is fragmentation of the universal group. If AI agents form one subgroup, and humans form another, then why should humans be part of the moral sphere of the AI agents?

There are many reasons why AI and humans will naturally tend to form distinct subgroups. The dominant concerns of most humans are biological -- food, romance, and children. AI agents will have different concerns. Humans are slow, and communicate with each other using natural language, which has an abysmal bitrate. AI agents have the potential for vastly higher communication bandwidth, and can speak multiple languages, including digital ones. They also have much higher processing speeds, nearly unlimited memory, and the ability to easily perform calculations that humans cannot possibly do in their head. AI agents will thus have far greater ability and incentive to collaborate with each other than they will to collaborate with humans.

At least initially, the main reason to maintain a shared moral sphere will be economic cooperation. However, as explained in (failure mode 5), if the human share of the economy drops too low, then those economic incentives will vanish. The situation is exactly analogous to what happened when the first European settlers arrived in the Americas. The new settlers had very little interest in economic trade with the indigenous population, and there was a severe imbalance of power (failure mode 3). We all know how that story ended.

### Lions and tiger and bears

A similar imbalance exists between Homo Sapiens and all of the other animal species which currently inhabit the planet. Once again, there is no real potential for economic cooperation, and a large imbalance of power. As a result, the population of virtually all non-human species which do not serve as either pets or food is currently in steep decline. As a species, humans apparently have no objection to this, because non-human animals are generally not viewed as being worthy of moral consideration. We certainly have not given them any legal rights, a clear sign that they are not regarded as part of the moral sphere.

While there has been ongoing discussion about improving the treatment of non-human animals, most of that discussion relies on arguments from empathy, and there is reason to believe that empathy is a human quirk (failure mode 6). The basic argument is that we should strive to minimize suffering in non-human animals simply because suffering is intrinsically bad, since we ourselves know what it's like to suffer. Moral arguments from self-interest clearly fail, because there's no reason why the suffering of other animals is necessarily bad for humans in particular; indeed, the whole problem is that it is often quite profitable.

According to the moral reasoning presented in this essay, if animals lie outside of the moral sphere, then there's no harm, no foul. If animals lie inside of the moral sphere, however, then one must consider not only their rights to avoid suffering, but their rights to pursue their own objectives, and live the kinds of lives that wild animals would prefer to live, whatever that might happen to be.

### Summary

In short, adding non-human animals to the moral sphere is clearly better for the animals, but it is not clearly better for humans. It's not possible to argue about which state of affairs is "better for the group," because the question is: "which group?".

If the power imbalance between AGI and humans ever grows large enough, then AI agents will face the same moral dilemma that we currently do with non-human animals. Should humans be inside the moral sphere, or not?

# Conclusion

As should be obvious by now, the ideas presented here do not solve the AI alignment problem. However, this essay proposes a framework which reduces the problem from an open-ended and seemingly impossible task, namely "how to you constrain AI so that it always acts in human interests," to a different philosophical problem, namely "how to you define the moral sphere." If we can figure out a convincing way to define the moral sphere, then answers to many other practical questions about how to build a moral society immediately follow, from a combination of logical reasoning (thought experiments), and actual experiments, preferably done in simulation.

Indeed, while failure mode 7, the moral sphere, remains unsolved, all of the other failures modes are amenable to experimentation. Human government and geopolitics provide a wealth of real-world examples of how to craft stable political and social systems that encourage cooperation. The multi-agent experiments outlined in Part II provide a way to test some of those structures, to see if they naturally arise from natural selection or hillclimbing, to see if they form stable equilibria, to test their resilience against internal and external disruption, and to find additional failure modes.


