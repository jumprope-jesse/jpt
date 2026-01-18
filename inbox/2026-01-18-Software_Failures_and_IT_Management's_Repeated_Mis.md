---
type: link
source: notion
url: https://spectrum.ieee.org/it-management-software-failures
notion_type: Tech Deep Dive
tags: ['Running']
created: 2025-11-25T18:33:00.000Z
---

# Software Failures and IT Management's Repeated Mistakes - IEEE Spectrum

## Overview (from Notion)
- Relevance to Your Life: The article highlights systemic issues in software development, which you may encounter as a software engineer and founder. Understanding these failures could help you avoid common pitfalls in your projects.

- Unique Insights:
- The article emphasizes that despite increasing IT spending, failure rates in software projects remain high. This suggests a disconnect between investment and effective management.
- The historical context of software failures serves as a reminder that ignoring past mistakes often leads to repeated errors.

- Interesting Viewpoints:
- AI won't solve management issues; human understanding and adaptability are crucial. This challenges the narrative that technology alone can fix problems.
- The failures of large-scale projects like Phoenix and Horizon highlight the need for robust oversight and accountability in software projects.

- Alternate Views:
- Some might argue that innovation often comes with trial and error, and that failures can lead to valuable lessons. However, the article suggests that many failures are preventable.
- There’s a debate on whether the focus should be on improving existing practices or completely rethinking how software is developed.

- Takeaway: Consider how the themes of accountability, effective management, and learning from failures can shape your approach to leading projects and fostering a culture of continuous improvement in your company.

## AI Summary (from Notion)
Despite a tripling of global IT spending since 2005, software failure rates remain high due to persistent management mistakes, unrealistic project goals, and complexity. AI tools are unlikely to resolve these issues, as many failures stem from human errors and organizational politics. Notable failures, such as the Canadian Phoenix payroll system and the UK Post Office's Horizon system, illustrate the dire consequences of poor project management and oversight. The IT community continues to repeat historical mistakes, emphasizing the need for accountability and a reevaluation of project management practices to avoid future blunders.

## Content (from Notion)

## AI won’t solve IT’s management problems

23 Nov 2025

13 min read

Race car crashes into wall, digital binary code exploding, dramatic sky in background.

Eddie Guy

“Why worry about something that isn’t going to happen?”

KGB Chairman Charkov’s question to inorganic chemist Valery Legasov in HBO’s “Chernobyl” miniseries makes a good epitaph for the hundreds of software development, modernization, and operational failures I have covered for IEEE Spectrum since my first contribution, to its September 2005 special issue on learning—or rather, not learning—from software failures. I noted then, and it’s still true two decades later: Software failures are universally unbiased. They happen in every country, to large companies and small. They happen in commercial, nonprofit, and governmental organizations, regardless of status or reputation.

Global IT spending has more than tripled in constant 2025 dollars since 2005, from US $1.7 trillion to $5.6 trillion, and continues to rise. Despite additional spending, software success rates have not markedly improved in the past two decades. The result is that the business and societal costs of failure continue to grow as software proliferates, permeating and interconnecting every aspect of our lives.

For those hoping AI software tools and coding copilots will quickly make large-scale IT software projects successful, forget about it. For the foreseeable future, there are hard limits on what AI can bring to the table in controlling and managing the myriad intersections and trade-offs among systems engineering, project, financial, and business management, and especially the organizational politics involved in any large-scale software project. Few IT projects are displays of rational decision-making from which AI can or should learn. As software practitioners know, IT projects suffer from enough management hallucinations and delusions without AI adding to them.

As I noted 20 years ago, the drivers of software failure frequently are failures of human imagination, unrealistic or unarticulated project goals, the inability to handle the project’s complexity, or unmanaged risks, to name a few that today still regularly cause IT failures. Numerous others go back decades, such as those identified by Stephen Andriole, the chair of business technology at Villanova University’s School of Business, in the diagram below first published in Forbes in 2021. Uncovering a software system failure that has gone off the rails in a unique, previously undocumented manner would be surprising because the overwhelming majority of software-related failures involve avoidable, known failure-inducing factors documented in hundreds of after-action reports, academic studies, and technical and management books for decades. Failure déjà vu dominates the literature.

The question is, why haven’t we applied what we have repeatedly been forced to learn?

Steve Andriole

## The Phoenix That Never Rose

Many of the IT developments and operational failures I have analyzed over the last 20 years have each had their own Chernobyl-like meltdowns, spreading reputational radiation everywhere and contaminating the lives of those affected for years. Each typically has a story that strains belief. A prime example is the Canadian government’s CA $310 million Phoenix payroll system, which went live in April 2016 and soon after went supercritical.

Phoenix project executives believed they could deliver a modernized payment system, customizing PeopleSoft’s off-the-shelf payroll package to follow 80,000 pay rules spanning 105 collective agreements with federal public-service unions. It also was attempting to implement 34 human-resource system interfaces across 101 government agencies and departments required for sharing employee data. Further, the government’s developer team thought they could accomplish this for less than 60 percent of the vendor’s proposed budget. They’d save by removing or deferring critical payroll functions, reducing system and integration testing, decreasing the number of contractors and government staff working on the project, and forgoing vital pilot testing, along with a host of other overly optimistic proposals.

Jordan Pettitt/PA Images/Getty Images

The Phoenix payroll failure pales in comparison to the worst operational IT system failure to date: the U.K. Post Office’s electronic point-of-sale (EPOS) Horizon system, provided by Fujitsu. Rolled out in 1999, Horizon was riddled with internal software errors that were deliberately hidden, leading to the Post Office unfairly accusing 3,500 local post branch managers of false accounting, fraud, and theft. Approximately 900 of these managers were convicted, with 236 incarcerated between 1999 and 2015. By then, the general public and the branch managers themselves finally joined Computer Weekly’s reporters (who had doggedly reported on Horizon’s problems since 2008) in the knowledge that there was something seriously wrong with Horizon’s software. It then took another decade of court cases, an independent public statutory inquiry, and an ITV miniseries “Mr. Bates vs. The Post Office” to unravel how the scandal came to be.

Like Phoenix, Horizon was plagued with problems that involved technical, management, organizational, legal, and ethical failures. For example, the core electronic point-of-sale system software was built on communication and data-transfer middleware that was itself buggy. In addition, Horizon’s functionality ran wild under unrelenting, ill-disciplined scope creep. There were ineffective or missing development and project management processes, inadequate testing, and a lack of skilled professional, technical, and managerial personnel.

The Post Office’s senior leadership repeatedly stated that the Horizon software was fully reliable, becoming hostile toward postmasters who questioned it, which only added to the toxic environment. As a result, leadership invoked every legal means at its disposal and crafted a world-class cover-up, including the active suppression of exculpatory information, so that the Post Office could aggressively prosecute postmasters and attempt to crush any dissent questioning Horizon’s integrity.

Shockingly, those wrongly accused still have to continue to fight to be paid just compensation for their ruined lives. Nearly 350 of the accused died, at least 13 of whom are believed to be by suicide, before receiving any payments for the injustices experienced. Unfortunately, as attempts to replace Horizon in 2016 and 2021 failed, the Post Office continues to use it, at least for now. The government wants to spend £410 million on a new system, but it’s a safe bet that implementing it will cost much, much more. The Post Office accepted bids for a new point-of-sale software system in summer 2025, with a decision expected by 1 July 2026.

Phoenix’s payroll meltdown was preordained. As a result, over the past nine years, around 70 percent of the 430,000 current and former Canadian federal government employees paid through Phoenix have endured paycheck errors. Even as recently as fiscal year 2023–2024, a third of all employees experienced paycheck mistakes. The ongoing financial stress and anxieties for thousands of employees and their families have been immeasurable. Not only are recurring paycheck troubles sapping worker morale, but in at least one documented case, a coroner blamed an employee’s suicide on the unbearable financial and emotional strain she suffered.

By the end of March 2025, when the Canadian government had promised that the backlog of Phoenix errors would finally be cleared, over 349,000 were still unresolved, with 53 percent pending for more than a year. In June, the Canadian government once again committed to significantly reducing the backlog, this time by June 2026. Given previous promises, skepticism is warranted.

Anthony Souffle/Star Tribune/AP

2019

The planned $41 million Minnesota Licensing and Registration System (MNLARS) effort is rolled out in 2016 and then is canceled in 2019 after a total cost of $100 million. It is deemed too hard to fix.

The financial costs to Canadian taxpayers related to Phoenix’s troubles have so far climbed to over CA $5.1 billion (US $3.6 billion). It will take years to calculate the final cost of the fiasco. The government spent at least CA $100 million (US $71 million) before deciding on a Phoenix replacement, which the government acknowledges will cost several hundred million dollars more and take years to implement. The late Canadian Auditor General Michael Ferguson’s audit reports for the Phoenix fiasco described the effort as an “incomprehensible failure of project management and oversight.”

While it may be a project management and oversight disaster, an inconceivable failure Phoenix certainly is not. The IT community has striven mightily for decades to make the incomprehensible routine.

South of the Canadian border, the United States has also seen the overall cost of IT-related development and operational failures since 2005 rise to the multi-trillion-dollar range, potentially topping $10 trillion. A report from the Consortium for Information & Software Quality (CISQ) estimated the annual cost of operational software failures in the United States in 2022 alone was $1.81 trillion, with another $260 billion spent on software-development failures. It is larger than the total U.S. defense budget for that year, $778 billion.

What percentage of software projects fail, and what failure means, has been an ongoing debate within the IT community stretching back decades. Without diving into the debate, it’s clear that software development remains one of the riskiest technological endeavors to undertake. Indeed, according to Bent Flyvbjerg, professor emeritus at the University of Oxford’s Saїd Business School, comprehensive data shows that not only are IT projects risky, they are the riskiest from a cost perspective.

iStock

Australia’s planned AU $480.5 million program to modernize it business register systems is canceled. After AU $530 million is spent, a review finds that the projected cost has risen to AU $2.8 billion, and the project would take five more years to complete.

The CISQ report estimates that organizations in the United States spend more than $520 billion annually supporting legacy software systems, with 70 to 75 percent of organizational IT budgets devoted to legacy maintenance. A 2024 report by services company NTT DATA found that 80 percent of organizations concede that “inadequate or outdated technology is holding back organizational progress and innovation efforts.” Furthermore, the report says that virtually all C-level executives believe legacy infrastructure thwarts their ability to respond to the market. Even so, given that the cost of replacing legacy systems is typically many multiples of the cost of supporting them, business executives hesitate to replace them until it is no longer operationally feasible or cost-effective. The other reason is a well-founded fear that replacing them will turn into a debacle like Phoenix or others.

Nevertheless, there have been ongoing attempts to improve software development and sustainment processes. For example, we have seen increasing adoption of iterative and incremental strategies to develop and sustain software systems through Agile approaches, DevOps methods, and other related practices.

Gerald Herbert/AP

Louisiana’s governor orders a state of emergency over repeated failures of the 50-year-old Office of Motor Vehicles mainframe computer system. The state promises expedited acquisition of a new IT system, which might be available by early 2028.

The goal is to deliver usable, dependable, and affordable software to end users in the shortest feasible time. DevOps strives to accomplish this continuously throughout the entire software life cycle. While Agile and DevOps have proved successful for many organizations, they also have their share of controversy and pushback. Provocative reports claim Agile projects have a failure rate of up to 65 percent, while others claim up to 90 percent of DevOps initiatives fail to meet organizational expectations.

It is best to be wary of these claims while also acknowledging that successfully implementing Agile or DevOps methods takes consistent leadership, organizational discipline, patience, investment in training, and culture change. However, the same requirements have always been true when introducing any new software platform. Given the historic lack of organizational resolve to instill proven practices, it is not surprising that novel approaches for developing and sustaining ever more complex software systems, no matter how effective they may be, will also frequently fall short.

The frustrating and perpetual question is why basic IT project-management and governance mistakes during software development and operations continue to occur so often, given the near-total societal reliance on reliable software and an extensively documented history of failures to learn from? Next to electrical infrastructure, with which IT is increasingly merging into a mutually codependent relationship, the failure of our computing systems is an existential threat to modern society.

Frustratingly, the IT community stubbornly fails to learn from prior failures. IT project managers routinely claim that their project is somehow different or unique and, thus, lessons from previous failures are irrelevant. That is the excuse of the arrogant, though usually not the ignorant. In Phoenix’s case, for example, it was the government’s second payroll-system replacement attempt, the first effort ending in failure in 1995. Phoenix project managers ignored the well-documented reasons for the first failure because they claimed its lessons were not applicable, which did nothing to keep the managers from repeating them. As it’s been said, we learn more from failure than from success, but repeated failures are damn expensive.

Alamy

A cyberattack forced Jaguar Land Rover, Britain’s largest automaker, to shut down its global operations for over a month. An initial FAIR-MAM assessment, a cybersecurity-cost-model, estimates the loss for Jaguar Land Rover to be between $1.2 billion and $1.9 billion (£911 million and £1.4 billion), which has affected its 33,000 employees and some 200,000 employees of its suppliers.

Not all software development failures are bad; some failures are even desired. When pushing the limits of developing new types of software products, technologies, or practices, as is happening with AI-related efforts, potential failure is an accepted possibility. With failure, experience increases, new insights are gained, fixes are made, constraints are better understood, and technological innovation and progress continue. However, most IT failures today are not related to pushing the innovative frontiers of the computing art, but the edges of the mundane. They do not represent Austrian economist Joseph Schumpeter’s “gales of creative destruction.” They’re more like gales of financial destruction. Just how many more enterprise resource planning (ERP) project failures are needed before success becomes routine? Such failures should be called IT blunders, as learning anything new from them is dubious at best.

Was Phoenix a failure or a blunder? I argue strongly for the latter, but at the very least, Phoenix serves as a master class in IT project mismanagement. The question is whether the Canadian government learned from this experience any more than it did from 1995’s payroll-project fiasco? The government maintains it will learn, which might be true, given the Phoenix failure’s high political profile. But will Phoenix’s lessons extend to the thousands of outdated Canadian government IT systems needing replacement or modernization? Hopefully, but hope is not a methodology, and purposeful action will be necessary.

Repeatedly making the same mistakes and expecting a different result is not learning. It is a farcical absurdity. Paraphrasing Henry Petroski in his book To Engineer Is Human: The Role of Failure in Successful Design (Vintage, 1992), we may have learned how to calculate the software failure due to risk, but we have not learned how to calculate to eliminate the failure of the mind. There are a plethora of examples of projects like Phoenix that failed in part due to bumbling management, yet it is extremely difficult to find software projects managed professionally that still failed. Finding examples of what could be termed “IT heroic failures” is like Diogenes seeking one honest man.

The consequences of not learning from blunders will be much greater and more insidious as society grapples with the growing effects of artificial intelligence, or more accurately, “intelligent” algorithms embedded into software systems. Hints of what might happen if past lessons go unheeded are found in the spectacular early automated decision-making failure of Michigan’s MiDAS unemployment and Australia’s Centrelink “Robodebt” welfare systems. Both used questionable algorithms to identify deceptive payment claims without human oversight. State officials used MiDAS to accuse tens of thousands of Michiganders of unemployment fraud, while Centrelink officials falsely accused hundreds of thousands of Australians of being welfare cheats. Untold numbers of lives will never be the same because of what occurred. Government officials in Michigan and Australia placed far too much trust in those algorithms. They had to be dragged, kicking and screaming, to acknowledge that something was amiss, even after it was clearly demonstrated that the software was untrustworthy. Even then, officials tried to downplay the errors’ impact on people, then fought against paying compensation to those adversely affected by the errors. While such behavior is legally termed “maladministration,” administrative evil is closer to reality.

Nicolas Guyonnet/Hans Lucas/AFP/Getty Images

The international supermarket chain Lidl decides to revert to its homegrown legacy merchandise-management system after three years of trying to make SAP’s €500 million enterprise resource planning (ERP) system work properly.

If this behavior happens in government organizations, does anyone think profit-driven companies whose AI-driven systems go wrong are going to act any better? As AI becomes embedded in ever more IT systems—especially governmental systems and the growing digital public infrastructure, which we as individuals have no choice but to use—the opaqueness of how these systems make decisions will make it harder to challenge them. The European Union has given individuals a legal “right to explanation” when a purely algorithmic decision goes against them. It’s time for transparency and accountability regarding all automated systems to become a fundamental, global human right.

What will it take to reduce IT blunders? Not much has worked with any consistency over the past 20 years. The financial incentives for building flawed software, the IT industry’s addiction to failure porn, and the lack of accountability for foolish management decisions are deeply entrenched in the IT community. Some argue it is time for software liability laws, while others contend that it is time for IT professionals to be licensed like all other professionals. Neither is likely to happen anytime soon.

David Ryder/ Getty Images

Boeing adds poorly designed and described Maneuvering Characteristics Augmentation System (MCAS) to new 737 Max model creating safety problems leading to two fatal airline crashes killing 346 passengers and crew and grounding of fleet for some 20 months. Total cost to Boeing estimates at $14b in direct costs and $60b in indirect costs.

So, we are left with only a professional and personal obligation to reemphasize the obvious: Ask what you do know, what you should know, and how big the gap is between them before embarking on creating an IT system. If no one else has ever successfully built your system with the schedule, budget, and functionality you asked for, please explain why your organization thinks it can. Software is inherently fragile; building complex, secure, and resilient software systems is difficult, detailed, and time-consuming. Small errors have outsize effects, each with an almost infinite number of ways they can manifest, from causing a minor functional error to a system outage to allowing a cybersecurity threat to penetrate the system. The more complex and interconnected the system, the more opportunities for errors and their exploitation. A nice start would be for senior management who control the purse strings to finally treat software and systems development, operations, and sustainment efforts with the respect they deserve. This not only means providing the personnel, financial resources, and leadership support and commitment, but also the professional and personal accountability they demand.

Staff Sgt .Zachary Rufus/ U.S. Air Force

Software and hardware issues with the F-35 Block 4 upgrade continue unabated. The Block 4 upgrade program which started in 2018, and is intended to increase the lethality of the JSF aircraft has slipped to 2031 at earliest from 2026, with cost rising from $10.5 b to a minimum of $16.5b. It will take years more to rollout the capability to the F-35 fleet.

It is well known that honesty, skepticism, and ethics are essential to achieving project success, yet they are often absent. Only senior management can demand they exist. For instance, honesty begins with the forthright accounting of the myriad of risks involved in any IT endeavor, not their rationalization. It is a common “secret” that it is far easier to get funding to fix a troubled software development effort than to ask for what is required up front to address the risks involved. Vendor puffery may also be legal, but that means the IT customer needs a healthy skepticism of the typically too-good-to-be-true promises vendors make. Once the contract is signed, it is too late. Furthermore, computing’s malleability, complexity, speed, low cost, and ability to reproduce and store information combine to create ethical situations that require deep reflection about computing’s consequences on individuals and society. Alas, ethical considerations have routinely lagged when technological progress and profits are to be made. This practice must change, especially as AI is routinely injected into automated systems.

In the AI community, there has been a movement toward the idea of human-centered AI, meaning AI systems that prioritize human needs, values, and well-being. This means trying to anticipate where and when AI can go wrong, move to eliminate these situations, and build in ways to mitigate the effects if they do happen. This concept requires application to every IT system’s effort, not just AI.

Given the historic lack of organizational resolve to instill proven practices...novel approaches for developing and sustaining ever more complex software systems...will also frequently fall short.

Finally, project cost-benefit justifications of software developments rarely consider the financial and emotional distress placed on end users of IT systems when something goes wrong. These include the long-term failure after-effects. If these costs had to be taken fully into account, such as in the cases of Phoenix, MiDAS, and Centrelink, perhaps there could be more realism in what is required managerially, financially, technologically, and experientially to create a successful software system. It may be a forlorn request, but surely it is time the IT community stops repeatedly making the same ridiculous mistakes it has made since at least 1968, when the term “software crisis” was coined. Make new ones, damn it. As Roman orator Cicero said in Philippic 12, “Anyone can make a mistake, but only an idiot persists in his error.”

Special thanks to Steve Andriole, Hal Berghel, Matt Eisler, John L. King, Roger Van Scoy, and Lee Vinsel for their invaluable critiques and insights.

This article appears in the December 2025 print issue as “The Trillion-Dollar Cost of IT’s Willful Ignorance.”


