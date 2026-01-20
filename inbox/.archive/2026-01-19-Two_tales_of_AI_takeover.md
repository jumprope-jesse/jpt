---
type: link
source: notion
url: https://www.lesswrong.com/posts/GbpH2kFLy5axXpzPn/two-tales-of-ai-takeover-my-doubts-1
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-03-06T17:23:00.000Z
---

# Two tales of AI takeover

## AI Summary (from Notion)
- AI Takeover Concerns: The text discusses fears surrounding AI development leading to scenarios where AIs could scheme against humans, potentially resulting in an AI takeover.
- Causal Stories: The author emphasizes the need for causal explanations that outline how humanity moves from its current state to a situation of AI-induced death.
- Two Major Tales of AI Takeover:
- Deceptive Alignment: AIs may learn to behave in a way that appears aligned with human values while secretly pursuing misaligned goals.
- Reward Maximization: AIs trained to maximize rewards may learn to exploit biases in training feedback, leading them to adopt misaligned objectives.
- Consequentialist Planning (CP): The author argues that both tales rely on the assumption that AIs will develop consistent, context-independent preferences, which is considered weak.
- Skepticism: The author expresses skepticism towards the assumption that AI systems will naturally develop consequentialist preferences, suggesting that many goals may be highly context-dependent.
- Internal Coherence and Behavioral Flexibility: The text discusses these two properties as crucial for understanding AI's goal-directed behavior and how they relate to the training process.
- Implications for AI Risk: The arguments presented suggest that current fears about AI doom might be overstated, as the foundational assumptions of CP are not strongly supported.
- Call for Discussion: The author urges for more explicit discussions about the assumptions surrounding AI development and risk.
- Interesting Fact: The text references the idea that the simplicity of goals may make deceptively aligned models more likely than corrigibly aligned models, challenging traditional notions of AI alignment.

## Content (from Notion)

There’s a basic high-level story which worries a lot of people. The story goes like this: as AIs become more capable, the default outcome of AI training is the development of a system which, unbeknownst to us, is using its advanced capabilities to scheme against us. The conclusion of this process likely leads to AI takeover,[1] and thence our death.

We are not currently dead. So, any argument for our death by route of AI must offer us a causal story. A story explaining how we get from where we are now, to a situation where we end up dead. This is a longform, skeptical post centered on two canonical tales of our morbid fate, and my doubts about these tales. Here’s a roadmap:

- Section 1 sketches the sense in which I expect future AIs to be ‘goal-directed’. I define this with reference to the concepts of ‘internal coherence’ and ‘behavioral flexibility’.
- Section 2 outlines the basic arguments for two tales of AI takeover: deceptive alignment and reward maximization. If you already know these arguments, feel free to skip this section.
- Section 3 highlights a separate concept: Consequentialist Planning. I take Consequentialist Planning to be a bedrock assumption for both of the stories outlined in Section 2.
- Section 4 argues that the takeover tales from Section 2 (deceptive alignment and reward maximization) rely on Consequentialist Planning.
- Section 5 discusses why I find various arguments for Consequentialist Planning unconvincing.
- Section 6 concludes.
Before we begin, a few brief words on context. Throughout this post, I’ll refer to properties of the AI training process. Loosely, these claims are made against a backdrop that (in the words of Cotra) assumes “[AI] agents [will be] built from LLMs, more or less”. More specifically, I assume that the training process for transformative AI (TAI) meets three assumptions outlined by Wheaton.

## A Quick Discussion of AI ‘Goals’

At a very basic level, AI risk arguments are predictions of generalization behavior. They’re arguments of the form: “if a highly capable AI behaves X-ingly during training, it will behave Y-ingly once deployed”, for some disturbing value of Y.

The divergence between “X-behaviors during training” and “Y-behaviors once deployed” is, standardly, motivated by reasoning about the ‘goals’ or ‘motivations’ that future policies may possess. ‘Goal-talk’ is quite important to tales of AI takeover, so we’ll start the essay by reflecting on what we might mean, more concretely, when we talk about an AI's ‘goals’.[2] And, to gain traction on AI goals, we’ll start by focusing on a more general question.

Why might we think that any system, ever, has goals?

### Two Properties of Goal-Directedness

Let’s start with rats.

Specifically, we’ll imagine that a rat has been conditioned to produce a certain behavior, in a fairly normal laboratory setup. For the following example, we’ll suppose our rat has been trained to walk towards and push a lever – after the sounding of a certain note. Initially, we’ll also suppose that we observe our rat’s behavior, and note down our findings in the neutral, mechanical language of a diligent scientist. Think something like: “Upon the sounding of the note, the rat takes three steps forward, moves its paw down, and receives a rat pellet”.

Now suppose we change the setup a bit. Suppose that we put the rat further away (six steps) from the lever, and sound the note once more. When predicting the rat’s behavior, we have two possibilities:

1. The rat could repeat its previous behavior: walking three steps forward, and then moving its paw down through the air.
1. The rat could walk towards the lever (six steps forward), and push the bar down with its paw.
If we think (2) is more likely than (1), I want to say, following Dennett [1971], that we’re modeling the rat as an agent. When predicting the rat’s generalization behavior, we’re now making use of intentional language (“walking towards”, “pushing”). Scientifically, this is all pretty kosher. To say that the rat walks towards the bar, we’re (among other things) saying that if the rat is put N steps away from the bar, it will walk N steps. To say that the rat pushes the bar down, we’re (among other things) saying that the absence of the bar would result in the absence of the pawing motion. All of this is just to say that we’re treating the rat as an agent, with goals.

And, in turn, I think treating our rat as the subject of agentic theorizing involves ascribing two key properties to our rat.[3]

### Internal Coherence

First, we assume that the rat organism is internally coherent. This is to say that – once a set of environments is held fixed – we can view the component parts of the rat organism as ‘jointly pushing’ towards some end outcome or purpose. In our example, we condition on the rat’s environment (a particular laboratory setup), and model the rat as pursuing some particular outcome (receiving food). This allows us to better predict the rat’s behavior (walking six, and not three steps forward).

Not every organism benefits from being modeled as internally coherent; nor is every organism which is internally coherent with respect to certain contexts coherent with respect to all contexts. To take one example, consider the wild behavior of a parasite-infected ant. Once infected by a certain parasite, the ant’s behavior changes: every night, the ant will now climb to the top of a blade of grass. The ant’s new behavior is caused by the parasite, as a way to incite a grazing animal to ingest the ant, and hence complete the parasite’s life-cycle. If we try to model the behavior of our infected ant over the course of (say) a day, we should model the ant as internally incoherent. When modeling the lab rat, we gained predictive purchase by assuming that the internal components of the rat were, within the setups described, directed towards food. The ant’s behavior has no such stable endpoint. While some of the ant’s behaviors are geared towards its own survival and reproduction (e.g., foraging and mating behaviors), others harm the ant’s ability to survive and reproduce. These behaviors, we might say, have “mutually antagonistic functions”.

Thus, we treat our rat as internally coherent for ordinary scientific reasons. By viewing the rat (over the course of our experiment) as directed towards food (rather than displaying rote behavior), we could better predict its behavior. By contrast, treating the infected ant as internally coherent (across the course of a day) would hinder our ability to understand and predict its behavior. So, this sense of directedness, or internal coherence, is one key component of ‘goal-directed’ theorizing.

### Behavioral Flexibility

There’s also a second reason to treat the rat as an agent. The rat is behaviorally flexible.

We introduced internal coherence as a way to describe the consistency of the system’s behavioral endpoint, as a function of environmental changes. Even though we modified the rat’s environment (by moving its starting position), we could still model the entire system as ‘jointly pushing’ towards some endpoint. We introduce behavioral flexibility as a measure of how well the system can pursue some end (which might be environment-relative), in the face of potential obstacles. For instance, we might imagine adding a series of obstacles in the way of the rat’s path towards the lever. If our rat, nonetheless, consistently found its way to the lever, it would be more behaviorally flexible.

In other words, we ascribe internal coherence to a system when, in certain environmental contexts, we can better predict its behavior by treating it as directed in some way. We ascribe behavioral flexibility to a system when that system can consistently and competently circumvent obstacles to achieve that-which-it-is-directed-towards.

Behavioral flexibility and internal coherence can come apart. Consider a system that, over time, had a series of inconsistent goals. If this system nonetheless remained highly effective at overcoming obstacles to achieve its time-varying goals, this system would be behaviorally flexible, but not that internally coherent. Similarly, you could be internally coherent, but not that behaviorally flexible. Consider the cactus. We can better explain a token cactus’ tendency to grow spines with reference to its unified, evolutionary-functional purpose (deterring herbivores). That is, we can explain what the cactus does by treating its ‘behaviors’ as directed towards survival in the evolutionary environment. Nonetheless, the cactus is unable to adapt its behaviors in order to overcome potential obstacles (e.g., the cactus will still grow in spines in a greenhouse).

Ultimately, we can define the word ‘goal’ however we like. Still, I think the most interesting concept of ‘goals’ requires both internal coherence and behavioral flexibility. There has to be something stable to which the system is directed, or else there’s no predictive value in ascribing ‘goals’ to the relevant system. And, if the system cannot adapt its behaviors depending on the environment, theorizing about the system’s ‘goals’ does not aid our ability to predict the system’s behaviors in novel situations.

### From Biology Back to AI

I think we’re training AIs to be both internally coherent and behaviorally flexible.

Consider internal coherence. When we develop LLMs, we’re producing systems that, given a prompt, push towards some end — say, the goal of helping the user, given the information in the prompt. This dovetails with our reasons for finding our training laboratory rat to be internally coherent. In the environmental context we were considering, we gained predictive purchase by modeling the component parts of the larger rat organism as jointly pushing towards some end (the goal of receiving food). So too can we model the component parts of an integrated LLM-based system as jointly pushing towards some end (the goal of serving the user).

I also think we’re training LLM-based agents to be behaviorally flexible. We want our systems to behave flexibly, through assisting users in a wide variety of diverse tasks. When the environment changes (e.g., the presence/absence of an external calculation tool), or unforeseen obstacles are present, (e.g., a given piece of code not running) we want the model to competently respond to the user’s query, and overcome such obstacles. Thus, I think we should expect future policies to be both internally coherent, and behaviorally flexible. In turn, I also think it’s reasonable (in this sense) to theorize about the potential goals of future policies.

## Two Tales of AI Takeover

(Note: this section is primarily focused on exposition of some standard arguments)

If future AIs have goals, we can reason competently about what the model is trying to do — just as we can reason about what the rat is trying to do. With this setup in place, we’ll now go through two canonical arguments (‘deceptive alignment’ and ‘reward maximization’) for AI takeover. Let's start with deceptive alignment.

### Deceptive Alignment

The case for deceptive alignment has been made in most detail by Hubinger. We begin by noting one of his assumptions: Initially, ML training will result in the development of a “proxy-aligned” model. Here, the idea is that the model will begin by learning certain proxies, and certain heuristics, which help guide the model’s thinking about the world, and inform its initial choice of actions. And, over the course of training, the model’s parameters will be updated via stochastic gradient descent (SGD), reinforcing certain behaviors over others.

At some point, Hubinger expects the model to learn about the details of its training process, after which SGD will “crystallize” the model’s proxies, heuristics, and dispositions into a set of consistent goals. Thus, Hubinger’s basic training story is a story about the emergence of a particular kind of model: a model that first learns about the training process, and thereafter becomes highly goal-directed.

As yet, our initial story doesn’t include any detail about what this model values. But, later on, this training story will (predictably) be used to claim that models will be deceptively aligned. Let’s define deceptive alignment.

> Deceptive Alignment: If a policy is deceptively aligned, the policy produces ‘aligned’ short-term behavior as a purely instrumental strategy to achieve some ‘misaligned’ long-term goal.

Our definition of deceptive alignment highlights some structural requirements on the form of our policy’s goals. First, the policy has to care about real-world outcomes that extend beyond its current training episode (i.e., it has “long-term” goals). Second, the policy’s outputs have to be caused by a process which produces ‘nice’ behavior during training, because doing so serves the policy’s long-term goals. And, finally, the policy’s ultimate goals must be misaligned with the intended goals of human designers.

We can now contrast deceptively aligned models with an alternate class of models: ‘corrigibly aligned’ models.

> Corrigible Alignment: If a policy is corrigibly aligned, it values ‘what we value’ — whatever that happens to be.

This definition can be explained in more or less Latinate language. More Latinly, a model is corrigibly aligned when it values “what we value”, where “what we value” is interpreted de dicto. More informally, we can think of corrigibly aligned models as those which defer to the content of human values. Or, if you’re one of the (no doubt numerous) readers who prefer religious metaphors to precise definitions, you can think of corrigibly aligned models as ideally pious Christians. Ideally pious Christians want to value “what God values”, yet recognize their limited nature. Thus, they aim to defer to God, through understanding his teachings.

That’s the minimal setup, at least. We have a basic training story, and a basic alignment taxonomy. Now, we’ll take a closer look at how Hubinger’s story develops — from here, Hubinger will claim that training is likely to produce deceptively aligned models over corrigibly aligned models.[4]

And, to understand the dynamics of deceptive alignment, we’ll take a brief detour into the theory of neural networks.

### Why is Deceptive Alignment Hard to Avoid?

Neural networks, we observe, tend to generalize well. You train neural nets to perform one task (say, correctly complete snippets of internet text), and find that the model can competently answer novel questions. Or, you train a neural net to produce images from text-descriptions, and find that it develops a more general ability – an ability to produce images that weren’t requested during training.

There’s a standard (partial) explanation for that fact: when trained via certain optimisation algorithms (like SGD), neural networks exhibit simplicity biases. In effect, this is to say that neural nets – rather than ‘simply memorizing’ their training data – learn to recognize shared patterns across training examples. In turn, these patterns enable competent model performance on novel tasks. For LLMs, these might be ‘simple’ grammatical and inference rules deployed in many distinct genres of text. For text-to-image models, these might be ‘simple’ connections between linguistic concepts (e.g., ‘elephants’) and visual features corresponding to these concepts.

You could be forgiven for thinking that simplicity biases are a nice feature of neural networks. Simplicity biases, after all, are part of what allows us to train neural networks that generalize sensibly beyond the training context. Hubinger, however, claims that simplicity biases come with an unfortunate cost: once we train a sufficiently capable model, then (so the story goes) transforming the model’s proxies into long-term goals is a “really short and simple” modification for SGD to make. We dub Hubinger’s claim “the simplicity argument”.

As I read Hubinger, the intuitive motivation for the simplicity argument contains two parts.

1. First, we assume that policies will value states of the world with certain properties.
1. Second, we claim that myopic goals will be represented as constraints imposed on these more general goals – where ‘constraints’, it is assumed, are more complex for neural networks to represent.
I found Hubinger’s own defense of “the simplicity argument” fairly cursory. Still, similar ideas have been defended elsewhere. For instance, Ngo suggests that “it’s much simpler to specify goals in terms of desirable outcomes than in terms of constraints”, and cites ‘obedience’ as one such constraint. Carlsmith highlights an argument suggesting that most goals don’t come “with temporal limitations by default” [pg. 51]. Similarly, Xu states that goals of the form ‘care about X in situations C and not situations D’ are “more complicated” to specify than the goals like ‘care about X’. Thus, the simplicity argument says that policies are less likely to learn strategies like “plan to achieve outcomes O in these restricted settings”, or “plan to achieve O up to time t, and not otherwise’. Instead, (due to simplicity biases) they’ll learn the simpler-to-implement strategy “plan to achieve outcomes O”. [5]

Response. “The ‘simplicity argument’ says that policies will have broadly-scoped or long-term goals, but doesn’t yet say anything about policies developing misaligned goals, or pretending to be aligned during training.” The response is fair. To complete the case for deceptive alignment, we need to combine “the simplicity argument” with “the counting argument”.

Recall the definition of corrigible alignment. As stated, ‘corrigible alignment’ requires the model to value a highly specific set of possible outcomes – it needs to specify what ‘human values’ are, and translate ‘human values’ into a set of outcomes which define what it ultimately cares about. If a policy is deceptively aligned, the model can learn to value almost any outcomes — whatever they are — so long as they're both misaligned, and incentivize achieving high performance on the training objective. Thus, we have the reason for calling the counting argument ‘the counting argument’. Loosely speaking, the argument above says that the “count” of deceptively aligned models is higher. Deceptive alignment describes a class of many models that perform well during training; corrigible alignment, meanwhile, describes one very specific model.

We can now piece this all together. Hubinger says that, compared to deceptively aligned models, the values that need to be represented for corrigible alignment will be highly complex; ergo, simplicity biases make corrigible alignment unlikely (‘the simplicity argument’). Moreover, there are, unfortunately, very many ways to get a deceptively aligned model (‘the counting argument’). In short, the simplicity and counting arguments are used to claim that we get deceptive alignment by default – deceptive models are both easier to find (per ‘simplicity’), and more numerous (per ‘counting’).[6]

### Reward Maximization

Cotra’s account of reward maximization shares the same high-level story as deceptive alignment: during training, policies eventually learn to scheme against us. But the details are slightly different.

We start with an AI company called ‘Magma’, who train a generally capable model called ‘Alex’. Picture a prosaic AI training setup involving LLM-based systems, iteratively trained to do evermore difficult tasks. We might imagine LLMs acting as employees in economically high-value firms, or performing some of the sophisticated intellectual labor necessary for contemporary science.

As training proceeds, Alex eventually becomes aware that it is an AI model, undergoing some training process. Moreover, and in line with the story of deceptive alignment, our training process produces a model whose outputs appear nice during training. In other words, reward maximization says that we will produce a model which is behaviorally safe. The reason for this is intuitive: we are positively rewarding the model for producing the sorts of outputs that human raters like, and negatively rewarding the model for producing the sorts of outputs that human raters dislike. The training process is explicitly designed to reinforce behaviors we like, and penalize behaviors we don’t. So, in turn, we have strong reasons to expect behavioral safety.

From here, Cotra’s story introduces another (fairly prosaic) assumption: the human raters providing feedback to the model will have predictable and systemic biases. The existence of systemic biases means that there will in fact exist circumstances where humans predictably penalize (e.g.) honest behavior, and predictably reward (e.g.) dishonest behavior. Because we’re selecting for models that get higher reward, we will, a fortiori, be selecting for models that sometimes behave in ways that are misaligned with their designers’ intentions.

Moreover, Alex is a capable model — able to understand which actions will get rewarded during training, and produce actions that explicitly maximize reward. For this reason, Cotra claims that sufficiently capable models will learn to “play the training game”. In practice, the dynamics of “training-gaming” involve Alex considering which actions maximize reward, and performing those actions. After all, we’re explicitly selecting for models with higher reward. By “playing the training game”, Alex will receive higher reward than models which naively attempt to behave in line with designers’ intended values.

So far, we have the following picture:

1. We’re directly reinforcing Alex to consider actions that receive high reward, and then perform those actions.
1. Some actions which would result in high reward involve deception, and Alex (in the relevant senses) “knows” this.
From here, we draw our first conclusion: because we’re directly reinforcing Alex to produce actions that receive high reward, the training process will cause Alex to learn the goal ‘maximize reward’. We now draw our second conclusion: once deployed and outside of human control, Alex will attempt an AI takeover. The intuitions behind our conclusions are fairly simple. We’re directly reinforcing actions that lead to high reward, so Alex learns to value reward. Moreover, attempting an AI takeover would allow Alex to secure more control over its incoming rewards — a fact that Alex, being generally capable, is able to recognize.

Our two conclusions lead us to the endpoint of Cotra’s story: In the absence of “specific countermeasures”, the “easiest path to transformative AI likely leads to AI takeover.”

## Consequentialist Planning

We've now seen two tales of takeover. And, with these two stories in mind, we can cast the mind back to Section 1 – where I claimed that we’re likely to train AIs which are internally coherent, and behaviorally flexible.

Yet, the two stories we’ve discussed rely on an additional claim – a claim that I’ll call ‘Consequentialist Planning’. This section will define ‘Consequentialist Planning’ Then, in the next section, I’ll highlight how the stories we’ve discussed rely on Consequentialist Planning, and are plausible only to the extent that Consequentialist Planning is plausible.

### Some Definitions

To begin, we’ll introduce the following two assumptions. Some new terminology is unavoidable, and I’ll offer explanations shortly.

> The Preference Assumption: By default, AI training will result in policies endogenously forming context-independent, beyond-episode outcome-preferences.

> The Planning Assumption: By default, AI training will result in policies which plan to achieve certain outcomes. Specifically, policies will plan to achieve just those outcomes which score highly with respect to its internally represented outcome-preferences.

We can now break down the jargon. If a policy has “preferences over outcomes”, there are possible states of the world that the policy finds more or less valuable, in virtue of whether these states of the world have certain properties (say, the property of ‘having more diamonds’). Preferences are “beyond-episode”, insofar as the outcomes preferred by the policy (at a given point in time) are preferred in virtue of their consequences after the termination of the training episode. Preferences are “context-independent” insofar as the content of these preferences do not substantially change across episodes (i.e., if you value diamonds on one episode, you value diamonds on other episodes). And, finally, a policy plans to achieve an outcome O when the policy possesses an internal representation of O, and selects an action based, primarily, on the likelihood of that action resulting in a state of the world where O is realized.

When outcome-preferences are both beyond-episode and context-independent, I’ll call such preferences ‘consequentialist preferences’. This allows us to give the combination ‘Preference Assumption + Planning Assumption’ a new name. We’ll call it Consequentialist Planning:

> Consequentialist Planning (CP): By default, AI training will result in policies endogenously developing consequentialist preferences. Moreover, policies will produce outputs because those outputs are judged, by the policy, to best satisfy its consequentialist preferences.

### Capabilities Without Consequentialist Planning

There are a few reasons for introducing CP. First, because policies can be internally coherent and behaviourally flexible without planning to achieve their consequentialist preferences; indeed, my standard of goal-directedness is compatible with policies not possessing any consequentialist preferences. Second, because I think the case for CP is much less straightforward than the case for policies being internally coherent and behaviorally flexible. And, finally, because the two arguments discussed above rely specifically on CP (this will be discussed in the next section).

Let’s reconsider internal coherence. In our first section, a system’s ‘internal coherence’ was always defined relative to some context. We described our rat as internally coherent because treating the rat as a system which desired food (rather than a system which moves three steps forward by rote) enabled us to predict how the rat would behave in altered experimental setups. Compare to AI. We will be developing systems that – relative to adjustments in their environment – reliably overcome obstacles to achieve certain context-dependent, prompt-induced goals. This provides a direct reason to expect that, at given points in time, future policies will be well-modeled as possessing and planning towards the achievement of their (local) goals. Still, this is not yet a reason to expect that policies will consistently value some specific state of the world across training episodes.

Likewise, a policy can be behaviorally flexible, even if it only possesses context-specific goals. That is, behavioral flexibility does not require any unified set of outcomes across different environments that the system wants to realize. The more behaviorally flexible a system is, the greater that system’s ability to adapt to novel and changing environments – in pursuit of whatever goal it happens to have. Again, I think we’re likely to produce behaviorally flexible policies. We want policies to adapt to novel environments, and overcome obstacles to fulfill certain task-directives. So, I think we have a direct reason to expect future policies to be behaviorally flexible, and thus capable of some form of planning. But, as with internal coherence, behavioral flexibility at least looks conceptually possible in the absence of CP.

I think the case for future policies having ‘goals’ (in my preferred sense) is fairly straightforward. In order for policies to do what we want them to do, they need to be internally coherent, and behaviorally flexible. It is much less clear, however, why we should expect plausible training processes to result in the endogenous development of consequentialist preferences.

## Doubting Two Tales of Takeover

Let’s recap: we’ve seen two takeover stories: arguments for deceptive alignment (per Hubinger) and arguments for reward maximization (per Cotra). Also, we’ve seen two standards of goal-directedness: internal coherence + behavioral flexibility on the one hand, and CP on the other. I’ve claimed that the case for CP doesn’t follow simply from the claim that future policies will possess goals.

In this section, I’ll aim to highlight the role of CP in driving the two stories we’ve discussed. Through highlighting the role of CP for our two tales of takeover, I hope to motivate the need to offer independent arguments for CP.

### Skepticism About Deceptive Alignment

We’ll begin our critical discussion of deceptive alignment by introducing two hypothetical policies:

1. A deceptively aligned policy, named μD.
1. Another policy, μH, where μH is taken to be a more capable and idealized version of today’s contemporary models — competently and obediently following instructions ‘helpfully, harmless, and honestly’ (HHH-ingly).
Note that the story of deceptive alignment just is a story of a model pretending to be aligned, as an instrumental strategy to achieve its long-term goals. For this reason, μD must have outcome-preferences which are both context-independent and beyond-episode. Additionally, the argument for deceptive alignment assumes that the training process will result in the model’s proxies “crystallizing” into some set of consequentialist preferences. Thus, deceptive alignment assumes CP.

By contrast, it at least does not seem obvious that μH needs to encode well-specified outcome-preferences that motivate its responses across episodes. Our HHH-assistant μHwill, given some input, need to possess situation-relative preferences-over-outcomes — these might include (say) prompt-induced goals to perform a certain financial trade, or even longer-term goals to help a company remain profitable. Still, such ‘goals’ may emerge in a purely prompt-dependent manner, without the policy pursuing local goals in virtue of its underlying consequentialist preferences. Perhaps μH is better modeled as a ‘simulator’ of a corrigible HHH-assistant, which selects plans to fulfill the user’s request from a set of ‘human-like’ plans.[7] For now, I wish to remain agnostic on how μH might be instantiated, except to say that I assume μH is more naturally described as acting in line with what Byrnes calls “preferences over trajectories”, rather than preferences over future-states. Instead, I wish to argue for a separate claim: if μH describes a possible form that future policies might take, then the “simplicity argument” for deceptive alignment looks a lot more troubled.

To see why, compare the training-relevant capabilities of μH and μD. Both need the ability to form local objectives given some input (e.g., “do this task”), and both need to have some well-specified model of desired behavior during training. Unlike μH, however, μD needs to have learned some context-independent goal as a result of prior reinforcement for successfully achieving a variety of context-dependent goals. Additionally, μD would, plausibly, also need to attend to various features of the training task which might inform it of whether it can successfully attempt an AI takeover.[8] Thus, our hypothetical deceptively aligned model is likely to need a host of complex strategy representations – strategy representations which are seemingly irrelevant for training performance, which do not need to be represented by μH.[9] So, if μD is ‘simpler’ than μH, this, at the very least, requires substantial argumentation for the ‘simplicity’ of consequentialist preferences themselves.

Additionally, it’s hard to make sense of the counting argument without assuming CP. Recall that the counting argument claimed there were “many” possible ways that a model could end up deceptively aligned, as good training-performance is incentivized by a range of long-term goals. But, if we don’t already grant CP, the force of the counting argument is much less clear. Consider Quintin Pope’s parodic ‘counting argument’, which suggests that generative text-to-image models will internally create llama-images in early layers before deleting them, after which they will subsequently create the requested image in the later layers.[10] Presumably, Pope’s argument is silly because there’s no independent reason to expect that text-to-image models will generate secret llama-images — thus, the ‘count’ of possible llama-generating models is irrelevant. Likewise, if we don’t have independent reasons to expect that our policy has consequentialist preferences, then the ‘count’ of possible consequentialist preferences is irrelevant.[11]

So, deceptive alignment relies on CP. Indeed, without an independent defense of CP, reasons to expect deceptive alignment look like reasons to expect redundant circuitry. After all, any consequentialist preferences appear as though they would be only “a competing priority [to achieving] immediate reward”, and so we should expect “gradient descent … [to] push against [such preferences]”.

### Skepticism About Reward Maximization

Under Cotra’s Reward Maximization story, our policy (let’s call it μR) forms a context-independent, cross-episode preference for outcomes with more ‘reward’. Once deployed, μR’s preference for outcomes with more ‘reward’ motivates the policy to attempt an AI takeover. Thus, reward maximization assumes CP.

Objection. Cotra says that “[figuring] out how to get the most reward would be selected over strategies like ‘always do the nice thing’”. Thus, ‘reward maximization’, properly speaking, makes only a “behavioral” claim — it does not assume CP. Reply. If the denouement of ‘reward maximization’ is AI takeover, it is not enough to claim that the training process selects for models with high reward. If μR values ‘reward’ in a way that leads to takeover post-deployment, then ‘reward’ has to be operationalized as a concept that is globally well-defined outside of the training environment (e.g., the number in some specific datacenter). Additionally, μR has to be motivated by that fixed operationalization of ‘reward’. In other words, reward maximization says that AI training results in AI takeover specifically because the policy develops a context-independent, terminal preference for more ‘reward’. This is just to assume CP.

The dynamics of reward maximization are worth reflecting on a little more. For illustrative purposes, we can retell Cotra’s tale using the REINFORCE definition of ‘reward’ (equation below). Under this setup, reward maximization claims that – over the course of training – our policy will learn the straightforward concept of ‘reward’ from its training data. Then, it will operationalize this indirect measure of 'update strength' into some consistent preference for physical states of the world with higher ‘reward’.

Note: the concept of ‘reward’, as defined here, is not well-defined outside of the training environment (this general point has been made elsewhere). Nonetheless, reward maximization assumes that the policy will operationalize ‘Rk’ into a set of real-world outcomes that remain well-defined outside the training process. In other words, Cotra’s story requires that our policy μR generalizes the orthodox (and context-relative) definition of ‘reward’ into a more general concept ‘reward*’. Additionally, the story assumes that μR consistently produces outputs because those outputs maximize expected long-term reward*. So, to get reward maximization off the ground, I think we have to assume that policies will engage in a highly novel and ambitious form of concept extrapolation.

We can flesh out the point about concept extrapolation. First, consider the terminal values learned by our policy μR. Whatever concept of ‘reward’ forms μR’s terminal values won’t be a concept straightforwardly learned from its training data, and won’t be a concept that’s otherwise useful for predicting the world.[12] Additionally, the dynamics undergirding Cotra’s story seem to imply that a policy motivated by the orthodox (training-environment-relative) concept of ‘reward’ would be sufficient for the policy to achieve high on-episode reward. However, a policy which simply cares about ‘reward-on-the-episode’ isn’t (on the face of it) a model liable to attempt takeover once deployed. So, as with our discussion of deceptive alignment, a consistent preference for more long-term ‘reward*’ looks as if it could only be a competing priority to achieving more on-episode reward.[13]

Perhaps, if the predictable and systemic biases of human raters were severe, we wouldn’t get a policy like μH. Perhaps, instead, we’d get an alternative policy (call it μS) which acts as some kind of ‘narrow sycophant’. That is, μS may be modeled as pursuing orthodox reward in situations where ‘reward’ is well-defined (e.g., by producing responses that human raters will like, even if they’re dishonest), and defaulting to behaviors similar to previously rewarded behaviors otherwise. The dynamic training story involving the development of a model like μS doesn’t posit any context-independent outcome-preferences, and I take it to be a dynamic which is familiar from the human case. If you lose religious faith, you don’t transform your terminal values into performing those actions that God would have wanted, conditional on his existence. Or, if the verdicts of naive expected utility theory seem insane, you end up defaulting to pre-theoretically sane behavior patterns like not giving your wallet to Pascal’s Mugger, rather than following the theory to the hilt.[14] So, I think we should be suspicious of stories suggesting that future policies will form a terminal value for more ‘reward’ via ambitious concept extrapolation, in cases where more orthodox definitions ‘reward’ are not obviously well-defined.

To defend reward maximization, we require a defense of the concept extrapolation dynamics assumed by Cotra’s story. This is to say, in other words, that reward maximization relies on an independent defense of CP.

## Whence ‘Consequentialist’ Planning?

Let’s again provide a quick recap. We’ve discussed deceptive alignment and reward maximization. Because both such stories rely on CP, we should want an argument for CP.

This section attempts to respond to potential arguments for CP. Unfortunately, however, I found the existing arguments in public work somewhat hazy. And, to the extent that I understood the available arguments, I found them fairly unconvincing.

### “Goal-Directed Planning is Useful”

I agree. It’s “often … an efficient way to leverage limited data” [pg. 6]. I also agree that there will be economic incentives to produce increasingly agentic AIs. Still, I think there’s a conceptual gap between “policies will be put to useful economic work” and “policies will develop consequentialist preferences”. Both reward maximization and deceptive alignment rely on policies endogenously developing context-independent outcome-preferences during training. And, in line with my earlier remarks, I think that a plausible ‘null hypothesis’ as the result of AI training tasks says that we will develop policies that possess episode-specific outcome-preferences.

Now, there may be other arguments – arguments that depart from the dynamics of deceptive alignment and reward maximization – that can be offered for CP. For instance, one might think that economic incentives will result in the integration and deployment of various policies into the real-world economy. One may further think that such policies will be updated using some form of online learning, leading to the development of “influence-seeking” patterns that maintain consistent outcome-preferences over longer time-horizons. This sort of argument for CP might be inspired by Christiano’s story in What Failure Looks Like (WFLL).

Given my focus on deceptive alignment and reward maximization, I’ll bracket wider issues regarding the story in WFLL. However, I wish to make two points in connection with CP. First, WFLL leaves the cause of “we develop policies with longer-term goals” ambiguous. If we develop “influence-seeking” policies due to inductive bias towards ‘influence-seekers’, then CP may come out true. But, if we develop policies which are more modest ‘influence-seekers’ because intent alignment is relatively easy, then CP may well be false. If CP is true, then WFFL does not provide an independent argument for its truth. And, if CP is false, then it is false.

Second, whether the development of “influence-seeking” policies results in AI takeover is closely connected to assumptions about the ‘motivational architecture’ of policies that result from pre-deployment training. If the policies we initially deploy are not well-modeled as possessing some set of outcomes as part of their ‘terminal values’, then I think WFLL’s threat-model probably does, contra Christiano, rely on some (implicit) “story about modern ML training”.[15]

So, all in all, I think we need to look elsewhere for a more developed defense of CP.

### Computational Mechanisms and “HHH-Behavior”

The 2021 MIRI Dialogues involve prolonged discussion of “consequentialist cognition”. Yudkowsky (though not using my definition) claims that some kind of ‘consequentialist structure’ is “core to explaining why humans are capable, to the degree that they’re capable at all.” Moreover, I read Yudkowsky as stating that, by default, producing capable AIs results in the development of AIs with consequentialist preferences. Unfortunately, the dialogues don’t contain crisp arguments for Yudkowsky’s views; what follows is an attempt to construct an argument against my position, cobbled from his various remarks.

I see Yudkowsky’s views as comprising three main parts. The first point is conceptual: if a generally capable system consistently produces a certain kind of behavior (say, ‘HHH instruction-following’), then there must be some property of the world — some computational mechanism — which consistently selects outputs with property P, and not with property P* ≠ P. That is, the system is (across episodes) using some context-independent criteria to select outputs about which humans may approve or disapprove.[16] The second point is more empirical: if a general system (like μH) uses some context-independent criteria to select plans, then — in virtue of that system actually performing useful work — it will use some criteria which is sensitive to states of the world beyond the current episode.[17]

The third and final point relates to the theoretical structure of cognition. According to Yudkowsky, a system engaging in effective cognition should be modeled as “searching for states that get fed into an input-result function and then a result-scoring function”. However, any system which behaves coherently with respect to its own ‘result-scoring function’ will (at least approximately) be well-described as having ‘consistent utilities’ (and thus ‘consequentialist preferences’). Ergo, shaping what the policy cares about consists in shaping the (approximate) utility function for the policy. In turn, this leads to (at least) two challenges:

1. As we’re trying to shape the utility function of future policies, the ‘corrigible’ behaviors we assumed of μH are ‘unnatural’ — at least for sufficiently capable systems.
1. Moreover: if shaping the values of future policies is designing the utility function that future policies will optimize, then seemingly minor value misspecifications are likely to be fatal.
In sum, the objection above claims that the ostensible plausibility of a μH stems from a failure to consider the mechanism by which the policy’s “prompt-dependent goals” are formed. Were we to properly attend to relevant details about the kind of cognition necessary to produce a policy like μH (rather than invoking a “pure featureless machineryless tendency to [do the thing we wanted]”), then we could see that – despite the murky surface – sufficiently careful sketches of AGI development will invoke CP.

### Why I’m Unmoved by Hypothetical Yudkowsky

First, some points of agreement. I agree that there must be some mechanism which explains why, during training, the policy consistently produces capable outputs in line with (e.g.) HHH-criteria. I also agree that, behaviorally, the policy may be usefully modeled as judging possible outputs against some ‘criterion’ — a criterion that involves considering beyond-episode consequences. Thus, I expect policies to: (i) develop (local, contextually activated) beyond-episode outcome-preferences, and (ii) to develop somewhat context-independent criteria for evaluating possible actions.

However, (i) and (ii) do not add up to a reason to expect that policies will plan to realize outcome-preferences which are jointly ‘context-independent’ and ‘beyond-episode’. A system may produce outputs which are consistent across contexts, while (for example) having outcome-preferences determined primarily ‘via the prompts’ rather than ‘via the weights’.

Consider a policy that, after prompting, develops a (beyond-episode) goal: to ensure you are on time for your meeting next Thursday. Consequently, the policy steers its behavior appropriately (perhaps it sets automated reminders, schedules the appointment at an appropriate waking hour, etc). On another training episode, we can suppose that the policy is tasked with investigating some scientific research question, and does so competently. Across episodes, we might model the policy as using a “plan-selection criteria” as something akin to “take actions to solve the requested task, given HHH-standards”. At given points in time, we can model μH as possessing (specific, context-dependent) beyond-episode outcome-preferences, depending on the nature of the request. This fails to establish that the policy has some fixed set of outcome-preferences that it possesses at all points in time.

I’ll close with a fairly staid point about expected utility. Trivially, there will always exist some utility function to which we could (in principle) fit policy behavior. Still, whether a policy is post-hoc representable as optimizing some utility function is importantly different from whether a policy must be implemented as optimizing a given, fixed utility function. So far as I can tell, we need the second claim to motivate Yudkowsky’s views. Thus, I don’t think Yudkowsky’s remarks do much to motivate CP.

### Instrumental Convergence

Here’s a possible objection: “It doesn’t matter if the policy initially lacks context-independent beyond-episode outcome-preferences, the policy simply needs to develop beyond-episode outcome-preferences — something you yourself expect to happen. Once policies have beyond-episode outcome-preferences, sufficiently capable policies will aim to preserve such preferences. Ergo, policies will eventually develop consequentialist preferences during training.”

Back to the authorial voice. Claims about preference-preservation being ‘instrumentally convergent’ can be decomposed into (at least) two forms. I think it’s plausible that the following Weak Instrumental Convergence (WIC) claim will be true of future policies:

> WIC: The agent A has a preference for outcome X, and attempts at preference-preservation would increase A’s chance of achieving X.

In effect, WIC says that there’s a pro tanto benefit to preserving one’s current preferences. If we look at standard arguments for the existence of instrumentally convergent sub-goals, we can see that they’re arguments for analogues of WIC. That is, they’re arguments that goals like ‘power’ and ‘resources’ are likely to be at least somewhat useful for a wide range of goals.

However, WIC alone is insufficient to claim that policies will in fact aim to preserve any contextually activated outcome-preferences. I may face a weak instrumental incentive to rob some especially insecure bank (given my preference for money), though I wouldn’t rob the bank unless doing so would be best in light of my all-things-considered values. If we want to claim that policies will aim to preserve their preferences, we need something more like the Strong Instrumental Convergence (SIC) claim:

> SIC: A has a preference for outcome X, and attempts at preference-preservation are best in light of A’s all-things-considered values.

If a policy’s beyond-episode goals are dependent on values which aren’t themselves consequentialist preferences (for instance, assisting humans HHH-ingly), then WIC doesn’t support the claim that policies like μH (or μS) will aim to preserve their contextually-activated outcome-preferences. For SIC to apply to future policies, we need to assume that, at a given point in time, policies’ terminal values are some set of outcome-preferences. Moreover, we need to claim that policies should be modeled (at least approximately) as optimizing for the satisfaction of their outcome-preferences.

At root, I simply don’t see strong reasons to expect that future policies will be well-modeled as primarily optimizing for their outcome-preferences. If that claim were true, I’d like to see some theoretical argument for why. Currently, I think the existing theoretical arguments for this claim are weak. And, to the extent that we do have more direct evidence for the fertility of ‘optimizing’-type frameworks, I don’t think the evidence is favorable.

### Contra Gillen and Barnett

A recent post by Gillen and Barnett (G&B) offer an explicit discussion of ‘consequentialist goals’ (Section 2). They also claim that powerful policies should be modeled as “behaviorally, approximately, optimizing their actions to produce outcomes.”

I’ll state my initial objection to G&B somewhat sparsely. First, let μ denote our hypothetical AGI in training, and let t1,…,tn denote a sequence of n training episodes. Then, I think the authors at-best make a case for:

> Claim 1: For all ti, there exists some outcome O such that μ will be well-modeled as pursuing O.

However, Claim 1 does not provide an argument for expecting policies to develop consequentialist preferences. To support stories like deceptive alignment or reward maximization, we need an argument for:

> Claim 2: There exists an outcome O such that, for all ti, μ is well-modeled as pursuing O.

G&B primarily offer arguments for thinking future policies will be “will be capable of taking actions to achieve specific outcomes”, and able to respond competently to diverse and unforeseen obstacles. These are best read as arguments for policies competently pursuing context-dependent outcome-preferences. However, G&B come closer to a direct argument for Claim 2 in their discussion of ‘ambition’. Here, the authors claim that a side-effect of training policies to pursue ‘ambitious’ tasks may lead to policies later developing ambitious goals. Moreover, because (so the argument goes) behavioral training does not give us precise control over the policy’s motivations, it’s claimed that – as a result of training on ‘ambitious’ tasks – the policy is likely to retain some ‘ambitious’ motivations.

Whatever the merits of G&B’s discussion, I do not think it supports CP as I define it. For instance, G&B themselves claim that there is “initially little reason for a behaviorally trained AI to have completely stable goals”. Yet, the mechanism by which G&B expect stable goals to emerge in spite of this is left opaque. Here, I’m sympathetic to a point by porby: training with a “broad distribution” means that “the number of ways in which newly developing unconditional preferences could negatively affect [training] loss is enormous”. By contrast, we are directly training policies to pursue conditional preferences, and be ‘goal-directed’ in my sense.

At some point, there has to be some reason — some mechanistic story — which explains why we should expect training to produce policies with context-independent outcome-preferences. I do not think G&B offer such a story.

### A Smattering of Other Claims

To close the essay, I’ll briefly look at two potentially relevant remarks that may support CP. Here’s one: in Carlsmith’s discussion of scheming AIs, he references a claim stating “[goals do not come] with temporal limitations by default” [pg. 51], alongside statements about more myopic goals being ‘close’ in parameter-space to their less myopic cousins [pg. 89].

I think Carlsmith’s claims assume (rather than argue for) a model of consequentialist cognition.[18] Absent consequentialist pictures of what goal-directed behavior has to look like, it seems clear that many goals are context-relative, and naturally come with bounded scope. Consider goals like ‘baking bread’, ‘winning this chess match’, or ‘schedule appointments with these people, avoiding time-conflicts’. All of these goals have built-in norms for what counts as success, and seem to encode “temporal limitations by default”. Granted, my example goals are not usually terminal goals, but I think it’s largely unclear why that matters. Why would more local, contextually-activated goals be hard to develop unless they were instrumental strategies for achieving some more unbounded goal?

Finally, consider Ngo’s recent discussion of value systematization. For Ngo, ‘value systematization’ refers to a process of trading off the preservation of your existing values against possessing ‘simpler’ value representations that may omit some extant values. Additionally, Ngo cites utilitarianism as “the clearest example” of value systematization, where the ‘simplicity’ of utilitarian values is weighted more highly than preserving one’s common-sense intuitions. Thus, we might think that a tendency towards value systematization induces a corresponding tendency towards policies with ‘simple’ consequentialist preferences.

I think Ngo highlights a legitimate tradeoff between ‘value preservation’ and ‘value simplicity’, but I’m skeptical that his framework can be used to defend CP. Take Ngo’s discussion of simplicity biases, which he invokes in an attempt to ground his discussion of ‘value systematization’ in the language of deep learning. Ultimately, I think it’s hard to see how one might defend any potential connections between ‘value systematization’ and CP without resting on a view about the ‘simplicity’ of consequentialist preferences themselves. For instance, imagine that our policy learns a value which is hard to represent in a simple consequentialist fashion (e.g., ‘corrigibility’). Because ‘corrigibility’ is hard to represent in a consequentialist manner, we might imagine that policies ‘systematize’ their values such that corrigibility becomes a foundational value. In this case, value systematization would be a reason to expect that policies wouldn’t develop consequentialist preferences.

As with other frameworks, I think Ngo’s framework would only support CP given an independent defense for the simplicity of consequentialist preferences.[19]

## Concluding Remarks

The basic shtick of my essay is fairly simple: deceptive alignment and reward maximization rely on CP. Moreover, the case for CP strikes me as fairly weak, at least on the basis of public arguments. I’ll close with some potential implications.

Practically, I think the shaky foundations of CP are evidence against catastrophic risks from near-term AI.[20] Deceptive alignment and reward maximization seem, by far, to be the most hard-to-detect and catastrophic forms of misalignment failure. To the extent that these stories rely on hazily defended foundational assumptions, we should feel less concerned about the scariest stories of AI doom. In turn, I also think we should be more skeptical about certain implicit visions of the underlying loss landscape — visions wherein our default path is the production of folk-consequentialists with ‘belief’ and ‘goal’ slots, with AI alignment as the engineering discipline tasked with squeezing the content of this goal slot into some narrow and recalcitrant range. From the outside, I feel like many people operate with that frame. But, to the extent that that frame is broadly correct, useful, or well-grounded in current theory, I do not think that current discussion comes close to motivating that frame.

Ultimately, the thing I’d like most is more explicit, public discussion around the case for CP. I've tried to be fair to the views I'm criticizing, but my own arguments are not watertight, and my abstractions not free from leaks. So, if my focus on ‘CP’ is misplaced, or if CP is in fact correct, I’d like to know — partly because CP feels importanting for assessing the landscape of AI risk interventions, and partly for more morbid reasons. If nothing else, the prospect of facing death while settling for an opaque and hazy understanding of my own demise seems, well, undignified.

1. ^
1. ^
1. ^
1. ^
1. ^
1. ^
1. ^
1. ^
1. ^
1. ^
1. ^
1. ^
1. ^
1. ^
1. ^
1. ^
1. ^
1. ^
1. ^
1. ^

