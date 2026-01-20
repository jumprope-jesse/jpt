---
type: link
source: notion
url: https://stratechery.com/2024/nvidia-waves-and-moats/
notion_type: Tech Announcement
tags: ['Running']
created: 2024-03-20T04:00:00.000Z
---

# Nvidia Waves and Moats

## AI Summary (from Notion)
- Event Overview: Jensen Huang, CEO of Nvidia, unveiled new AI-focused chips at an event dubbed “AI Woodstock,” attracting significant attention and attendance.

- Spectacle vs. Announcements: The event emphasized the spectacle of the launch rather than just the technical announcements, drawing comparisons to major product launches like Apple's iPhone and Windows 95.

- Keynote Focus: The keynote was more focused on the new Blackwell B200 generation of GPUs, highlighting their features, partnerships, and performance, contrasting with previous events that covered broader topics.

- Blackwell Architecture: The Blackwell chip architecture includes two dies fused into one, promising significant performance improvements over its predecessor, the Hopper series.

- Performance Metrics: Blackwell is noted for increasing parallelism, enabling larger AI models, while maintaining similar calculation speeds to previous generations.

- Market Strategy: Nvidia is reportedly lowering the price increase on B200 chips to maintain market share against competitors like AMD and to counter customers developing their own chips.

- Nvidia Inference Microservices (NIM): NIM is introduced as a set of optimized microservices for deploying AI models, aimed at simplifying the development and deployment of generative AI applications.

- Future of Software Development: Huang envisions a future where software is assembled from pre-built NIMs, allowing AI to execute complex tasks collaboratively, emphasizing the potential for AI to revolutionize software creation.

- Software Moat: Nvidia is building a software ecosystem around its GPUs to ensure they remain a preferred choice in AI applications, despite increasing competition.

- Takeaway: The event and product unveilings signify Nvidia's strategic positioning in the rapidly evolving AI landscape, focusing on both hardware and integrated software solutions to maintain dominance.

## Content (from Notion)

> The Nvidia frenzy over artificial intelligence has come to this: Chief Executive Jensen Huang unveiled his company’s latest chips on Monday in a sports arena at an event one analyst dubbed the “AI Woodstock.”

Or, as Nvidia Research Manager Jim Fan put it on X:

> 

I’m disappointed that the Wall Street Journal used this lead for their article about the event, but not because I thought they should have talked about the actual announcements: rather, they and I had the exact same idea. It was the spectacle, even more than the announcements, that was the most striking takeaway of Huang’s keynote.

I do think, contra the Wall Street Journal, that iPhone announcements are a relevant analogy; Apple could have, particularly in the early days of the iPhone, easily filled an 11,000 seat arena. Perhaps an even better analogy, though, was the release of Windows 95. Lance Ulanoff wrote a retrospective on Medium in 2001:

> It’s hard to imagine an operating system, by itself, garnering the kind of near-global attention the Windows 95 launch attracted in 1995. Journalists arrived from around the world on August 24, 1995, settling on the lush green, and still relatively small Microsoft Campus in Redmond, Washington. There were tickets (I still have mine) featuring the original Windows Start Button (“Start” was a major theme for the entire event) granting admission to the invite-only, carnival-like event…It was a relatively happy and innocent time in technology. Perhaps the last major launch before the internet dominated everything, when a software platform, and not blog post or a piece of hardware, could change the world.

One can envision an article in 2040 looking back on the “relatively happy and innocent time in technology” as we witnessed “perhaps the last major launch before AI dominated everything” when a chip “could change the world”; perhaps retrospectives of the before times will be the last refuge of human authors like myself.

### GTCs of Old

What is interesting to a once-and-future old fogey like myself, who has watched multiple Huang keynotes, is how relatively focused this event was: yes, Huang talked about things like weather and robotics and Omniverse and cars, but this was, first-and-foremost, a chip launch — the Blackwell B200 generation of GPUs — with a huge chunk of the keynote talking about its various features and permutations, performance, partnerships, etc.

I thought this stood in marked contrast to GTC 2022 when Huang announced the Hopper H100 generation of GPUs: that had a much shorter section on the chips/system architecture, accompanied by a lot of talk about potential use cases and a list of all of the various libraries Nvidia was developing for CUDA. This was normal for GTC, as I explained a year earlier:

> This was, frankly, a pretty overwhelming keynote; Liberty thinks this is cool:

I then went on an extended explainer of CUDA and why it was essential to understanding Nvidia’s long-term opportunity, and concluded:

> This is a useful way to think about Nvidia’s stack: writing shaders is like writing assembly, as in its really hard and very few people can do it well. CUDA abstracted that away into a universal API that was much more generalized and approachable — it’s the operating system in this analogy. Just like with operating systems, though, it is useful to have libraries that reduce duplicative work amongst programmers, freeing them to focus on their own programs. So it is with CUDA and all of those SDKs that Huang referenced: those are libraries that make it much simpler to implement programs that run on Nvidia GPUs.

Those GTCs were, in retrospect, put on by a company before it had achieved astronomical product-market fit. Sure, Huang and Nvidia knew about transformers and GPT models — Huang referenced his hand-delivery of the first DGX supercomputer to OpenAI in 2016 in yesterday’s opening remarks — but notice how his hand-drawn slide of computing history seems to exclude a lot of the stuff that used to be at GTC:

Suddenly all that matters in those intervening years was transformers!

I am not, to be clear, short-changing Huang or Nvidia in any way; quite the opposite. What is absolutely correct is that Nvidia had on their hands a new way of computing, and the point of those previous GTC’s was to experiment and push the world to find use cases for it; today, in this post-ChatGPT world, the largest use case — generative AI — is abundantly clear, and the most important message for Huang to deliver is why Nvidia will continue to dominate that use case for the foreseeable future.

### Blackwell

So about Blackwell itself; from Bloomberg:

> Nvidia Corp. unveiled its most powerful chip architecture at the annual GPU Technology Conference, dubbed Woodstock for AI by some analysts. Chief Executive Officer Jensen Huang took the stage to show off the new Blackwell computing platform, headlined by the B200 chip, a 208-billion-transistor powerhouse that exceeds the performance of Nvidia’s already class-leading AI accelerators. The chip promises to extend Nvidia’s lead on rivals at a time when major businesses and even nations are making AI development a priority. After riding Blackwell’s predecessor, Hopper, to surpass a valuation of more than $2 trillion, Nvidia is setting high expectations with its latest product.

The first thing to note about Blackwell is that it is actually two dies fused into one chip, with what the company says is full coherence; what this means in practice is that a big portion of Blackwell’s gains relative to Hopper is that it is simply much bigger. Here is Huang holding a Hopper and Blackwell chip up for comparison:

Huang holding a Hopper GPU and a Blackwell GPU

The “Blackwell is bigger” theme holds for the systems Nvidia is building around it. The fully integrated GB200 platform has two Blackwell chips with one Grace CPU chip, as opposed to Hopper’s 1 to 1 architecture. Huang also unveiled the GB200 NVL72, a liquid-cooled rack sized system that included 72 GPUs interconnected with a new generation of NVLink, which the company claims provides a 30x performance increase over the same number of H100 GPUs for LLM inference (thanks in part to dedicated hardware for transformer-based inference), with a 25x reduction in cost and energy consumption. One set of numbers I found notable were on these slides:

Blackwell's increased performance in training relative to Hopper

What is interesting to note is that both training runs take the same amount of time — 90 days. This is because the actual calculation speed is basically the same; this makes sense because Blackwell is, like Hopper, fabbed on TSMC’s 4nm process,

and the actual calculations are fairly serial in nature (and thus primarily governed by the underlying speed of the chip). “Accelerated computing”, though, isn’t about serial speed, but rather parallelism, and every new generation of chips, combined with new networking, enables ever greater amounts of efficient parallelism that keeps those GPUs full; that’s why the big improvment is in the number of GPUs necessary and thus the overall amount of power drawn.

That, by extension, means that a Hopper-sized fleet of Blackwell GPUs will be capable of building that much larger of a model, and given that there appears to be a linear relationship between scale and model capability, the path to GPT-6 and beyond remains clear (GPT-5 was presumably trained on Hopper GPUs; GPT-4 was trained on Ampere A100s).

What is interesting to note is that there are reports that while the B100 costs twice as much as the H100 to manufacture, Nvidia is increasing the price much less than expected; this explains the somewhat lower margins the company is expecting going forward. The report — which has since disappeared from the Internet (perhaps because it was published before the keynote?) — speculated that Nvidia is concerned about preserving its market share in the face of AMD being aggressive in price, and its biggest customers trying to build their own chips. There is, needless to say, tremendous incentives to find alternatives, particularly for inference.

### Nvidia Inference Microservices (NIM)

I think this provides useful context for another GTC announcement; from the Nvidia developer blog:

> The rise in generative AI adoption has been remarkable. Catalyzed by the launch of OpenAI’s ChatGPT in 2022, the new technology amassed over 100M users within months and drove a surge of development activities across almost every industry. By 2023, developers began POCs [Proof of Concepts] using APIs and open-source community models from Meta, Mistral, Stability, and more.

NIM’s are pre-built containers that contain everything an organization needs to get started with model deployment, and they are addressing a real need not just today, but in the future; Huang laid out a compelling scenario where companies’ use multiple NIMs in an agent-type of framework to accomplish complex tasks:

> Think about what an AI API is: an AI API is an interface that you just talk to. So this is a piece of software that in the future that has a really simple API, and that API is called human. These packages, incredible bodies of software, will be optimized and packaged and we’ll put it on a website, and you can download it, you can take it with you, you can run it on any cloud, you can run it in your datacenter, you can run it on workstations if it fits, and all you have to do is come to ai.nvidia.com. We call it Nvidia Inference Microservices, but inside the company we all call it NIMs.

Did you notice the catch? NIMs — which Nvidia is going to both create itself and also spur the broader ecosystem to create, with the goal of making them freely available — will only run on Nvidia GPUs.

NIM's only run on Nvidia GPUs

This takes this Article full circle: in the before-times, i.e. before the release of ChatGPT, Nvidia was building quite the (free) software moat around its GPUs; the challenge is that it wasn’t entirely clear who was going to use all of that software. Today, meanwhile, the use cases for those GPUs is very clear, and those use cases are happening at a much higher level than CUDA frameworks (i.e. on top of models); that, combined with the massive incentives towards finding cheaper alternatives to Nvidia, means both the pressure to and the possibility of escaping CUDA is higher than it has ever been (even if it is still distant for lower level work, particularly when it comes to training).

Nvidia has already started responding: I think that one way to understand DGX Cloud is that it is Nvidia’s attempt to capture the same market that is still buying Intel server chips in a world where AMD chips are better (because they already standardized on them); NIM’s are another attempt to build lock-in.

In the meantime, though, it remains noteworthy that Nvidia appears to not be taking as much margin with Blackwell as many may have expected; the question as to whether they will have to give back more in future generations will depend on not just their chips’ performance, but also on re-digging a software moat increasingly threatened by the very wave that made GTC such a spectacle.


