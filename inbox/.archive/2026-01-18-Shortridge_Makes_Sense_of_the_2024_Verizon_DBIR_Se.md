---
type: link
source: notion
url: https://kellyshortridge.com/blog/posts/shortridge-makes-sense-of-verizon-dbir-2024/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-05-01T22:16:00.000Z
---

# Shortridge Makes Sense of the 2024 Verizon DBIR | Sensemaking by Shortridge

## Overview (from Notion)
- The 2024 Verizon DBIR emphasizes that most cybersecurity breaches are financially motivated, highlighting the importance of focusing on tangible threats rather than abstract fears of espionage.
- As a software engineer and founder, understanding the data can help you make informed decisions about resource allocation for security measures, especially when navigating the complex landscape of modern threats.
- The report's findings on MOVEit and why it had a significant impact compared to other vulnerabilities could inform your approach to software development and security protocols, emphasizing the need for user-friendly updates.
- The discussion around phishing emphasizes that scrutiny of emails is often unrealistic; consider improving user experience in your products to mitigate these threats effectively.
- The unique perspective on the rationality behind user behavior in security can lead to a more empathetic approach when designing systems, recognizing that users often act out of necessity rather than negligence.
- The report's commentary on ransomware highlights the economic aspects of cybersecurity; understanding this can help you develop budget-friendly strategies for your company’s security investments.
- Overall, the insights can help shape not just your business strategy, but also foster a more informed and realistic view of cybersecurity in your personal and professional life.

## AI Summary (from Notion)
The 2024 Verizon DBIR highlights that financial motives drive approximately 93% of breaches, with espionage being a minor factor. MOVEit is notably implicated in 1,567 breaches, surpassing the impact of Log4Shell. The report emphasizes that users typically spend less than a minute scrutinizing emails, making them vulnerable to phishing. Additionally, the use of vulnerabilities in web applications is on the rise, while ransomware and extortion incidents account for a significant portion of financially motivated breaches. Overall, the report serves as a critical resource for understanding cybersecurity trends and challenges.

## Content (from Notion)

A picture of a confused looking fluffy kitty holding dollar bills while more dollar bills rain around them. Sitting alongside this adorable floof gleams a pile of silver coins that sound like they&rsquo;d clink against the web app servers on which they stand. You can almost hear the web app server fans whirring and sighing, especially given they are somehow levitating in ethereal clouds. In the background of the scene, diamond threads rain down; perhaps they are glowing fiber cables descending like meteors around our fluffy fiend with the thousand yard stare.

Every year Verizon publishes the best hope we have of scouring real world evidence of attacks and their impacts in the Verizon Data Breach Investigations Report (DBIR). I, the lucky daedric prince of chaos that I am, was privileged to receive an advance copy of the report last Sunday to ponder and prepare my thoughts (and by that I mean scramble to finish this in two witching hours).

What follows are my thoughts on the Verizon 2024 DBIR, attempting to make sense of the delectable data within and share this sensemaking with the community.

In some cases, I will cast a skeptical eye on their commentary (a meta commentary, if you will). When appropriate, I provoke the cybersecurity industry writ large. For all the ballyhooing we do about users being “irrational,” much of our security “strategy” seems quite irrational in light of this evidence…

# Your threat model is still money crimes

Yet again, to my absolute lack of surprise (but somehow to the surprise of many in infosec) cybersecurity is largely about money crimes. Financial motives remain the driver of ~93% of all breaches. Yes, espionage is up from 5% last year to 7%, but highly concentrated in Public Administration (i.e. government) breaches. And, as the report mentions, “espionage” also includes things like sales bros downloading their customer contact information to take to their new employer.

A bar chart showing threat actor motives in breaches, with a sample size of 5,632.

Really think about this and internalize it: out of 5,632 breaches and a bias towards government victims driving this bigger sample size, they found that espionage is still only 7% of breaches.

You are not a spider caught in a sexy spy web. You do not need to spin up “war rooms” or “task forces” for geopolitical events. The real APTs – the ones motivated by geopolitical power – do not think about you at all1.

Anyway, end-user as “threat actor” rose from 11% to 26%, but mostly due to “misdelivery” errors – sending something to the wrong recipient – that are subject to mandatory disclosure (so don’t interpret this as an “insider threat” surge).

So, if you combine “employee did a whoopsie” with “organized crime,” you get 90% of your “threat actors.” The “Other” actor type is just under 10% (based on eyeballing the chart) and includes things like activists, auditors, competitors, customers, force majeures, acquaintances, and terrorists. And then, very much last and least prevalent, we have nation-state or state-affiliated threat actors.

A bar chart showing threat actor varieties in breaches, with a sample size of 7,921.

I know that it sounds super duper cool to be important enough for an intelligence agency to target your organization, because how elegantly does that solve one’s existential woes2, our natural instinct to yearn for meaning in our life and work – a deus ex hostis, if you will – but you really do look very silly and, in light of this persistent evidence, irrational to your organization if you LARP as a counterintelligence professional.

# MOVEit, pwn it, steal it, makes us poorer, sadder, weaker, bitter

They mention MOVEit precisely 25 times3 in the 2024 DBIR for good reason: they found MOVEit implicated in 1,567 breach notifications. What fascinates me is that this dwarfs Log4shell’s impact last year; it was mentioned in only 0.4% of incidents (which are more numerous than breaches in the DBIR’s parlance).

Why? Why did MOVEit foment more real-world impact? Why did the industry clamor over Log4Shell more, with a longer tail of hype and FUD? I have theories.

The first theory returns to my heuristic for software engineering teams about whether to care about a vulnerability: the vulnerability must be scalable and easy-to-use, in the specific sense that it does not require too many steps for attackers to reach their goal.

MOVEit is quite literally designed to store sensitive data in a uniform manner, making it trivial to ransom. With Log4Shell, okay, you get a shell, but how do you transmogrify that into money? You must tailor your exploit to whatever system you’re targeting, then you land on a host with who knows what – possibly nothing of value – so now you must pivot, etc. etc.

With MOVEit, you can download all the data and documents within and hope that some will contain sensitive stuff that the victim does not want exposed. Thus, 0day in MOVEit checks the boxes on both scalability and ease of use in a way Log4Shell did not.

The second theory is that MOVEit is the IT department and Log4Shell is software engineering. In theory, software designed for end users (IT) should be easier to update than software designed as a library to use in other systems; this is the typical sOftWaRe SuPpLy ChAiN fuddery.

However, I believe this shows that engineering teams can actually update pretty quickly when it matters, especially compared to end users. They have automated tooling that suggests when something is out of date and informs them when the associated update fixes vulns. (I have more thoughts on this that are mostly summarized in our RFI response on OSS).

The third theory is really more of a list of contributing factors that drove MOVEit’s impact:

- MOVEit’s customers are primarily in Education and Healthcare, sectors not known for their ability to effectively operationalize software
- On-prem deployment model (SaaS makes it easier to update on behalf of customers)
- MOVEit’s fundamental purpose is to handle sensitive data, so attackers can expect that every system in use contains some sensitive data
- Uniformity of system deployment, which makes attacks on the software straightforward to automate
- It’s internet-accessible, making it easy for attackers to discover potential victims and perform their spooky action at a distance
- Compliance software doesn’t have to be good; compliance requirements force customers to buy it anyway
A chart showing MOVEit&rsquo;s victims by industry

# In which the DBIR is alarmed that people skim emails

On page 9, the 2024 Verizon DBIR states, “This leads to an alarming finding: The median time for users to fall for phishing emails is less than 60 seconds.”

I do not understand what’s alarming about this; it feels very unsurprising. Who is spending more than a minute scrutinizing emails?

Because I like my salt with a side of science, I looked for evidence and the answer is that few people are spending whole ass minutes on emails. In 2023, Litmus found humans spend 9 seconds on average looking at an email. 30% on average receive less than two seconds of attention, while only 29% receive more than eight seconds. Given Litmus is involved in delivering the type of email we could generously deem consensual spam, we could argue that people spend a little more time looking at corporate emails… but likely not by much.

Given this, what is alarming about humans spending a median of 21 seconds to click a malicious link after opening an email? Or even taking a median of 28 seconds for the victim to enter their data? Whether we have hot girl shit to do or corporate drone shit, our universal experience is that we want to finish email as efficiently as we can so we can move onto the stuff that gets us promoted and paid.

But this is cybersecurity with its rampant projection bias and intolerance for preferences other than enshrining security as the One True Goal. So, let’s appeal to rationality instead… because clicking the link really is rational.

My extremely lazy math I posted awhile ago on Mastodon is as follows:

If we assume the average corporate worker receives ~100 biz-related emails per day during the work week4, that’s approximately 26k per year. Let’s assume 50% have links.

If they click on 1 malicious email link in a year, that’s a ~0.008% “fail” rate to them. Even if they click on 100 malicious links, that’s only ~0.8%.

It’s entirely rational to click the links. As I memed many years ago, we have utterly failed as an industry if our hope rests on humans not clicking things on the thing clicking machine:

The horse sketch meme adapted by yours truly to illustrate the sad intellectual decline of the cybersecurity industry. The well-drawn end of the horse starts with the labels multilevel security, trusting trust, and formal methods. As the drawing gets progressively worse, the labels are firewalls, threat intelligence, and, once we reach the level of stick figure, the labels are machine learning for anomaly detection, and “prevent people from clicking things on the thing-clicking machine."

Spending even 1 minute on scrutinizing each email adds up to 217 hours per year, which neither employees nor their employers will appreciate. But also, the DBIR’s framing that 20 seconds and change to click the link is “alarming” suggests that even a minute might not be sufficient.

If we consider the time it would take to truly verify everything is legit in an email — especially for non-nerds — it’s probably more like 5 minutes. That results in over 1,000 hours per year scrutinizing emails on average (again, this is extremely lazy math).

Idk about you, dear reader, but spending 45 days of my year scrutinizing emails feels so uncivilized as to border on torture. “Careless”5 from the security normative perspective sounds a lot more like “rational” (or even “self respect”) from another.

How to solve this? Other than the security industry finally prioritizing UX (lol), what can we do?

Well, imagine if humans of corporate received only 10 emails in their inbox per day. Might they not naturally scrutinize them more? After all, their inbox would no longer resemble a bleak grave where, just as they carve through the soil to glimpse the gentle dawn light – perhaps even a bit of sparkly dew trembling on the satin petals of a nearby tulip – the shovel clinks against headstone and dumps another fetid clump on their exhausted form.

At 10 emails per day, it is reasonable to ask employees to spend a minute being extra sure about email. I see no practical path to whittling email into this covetable state of affairs (other than more aggressive filtering to just the VIE – very important email – which might bruise some egos) (Slack or Discord, and their peers (other than Teams), might also help).

But as long as inboxes fester like a summer picnic ruined by a swarm of wasps and mosquitoes, incessant buzzes vying for our attention, then we should not demand humans immolate even more of their lives to make up for our industry’s decades-long failure to invest in UX.

# Attackers are not using GenAI

I don’t really have anything to add to the 2024 DBIR’s commentary on AI except to praise it for its Real Housewives-level shade throwing.

First, in terms of evidence, they found that Gen AI didn’t even merit 100 mentions in underground crime forums over the past two years combined. When Gen AI is mentioned, it’s for gross reasons:

> 

A line chart showing the cumulative sum of GenAI mentions on criminal forums, both general terms and in the context of attack types."

That distressing factoid aside, there are two footnotes that spark joy that I wish to highlight for you all, too.

“Despite pressure from a vocal minority of the cybersecurity community^17” –> “Foonote 17: Strange spelling for ‘unhinged marketing hype’

and

“However, it is still a very timely topic and one that has been occupying the minds of technology and cybersecurity executives worldwide ^19” –> “Footnote 19: Just like real impactful technologies such as blockchain and the metaverse.”

But there isn’t just snark here, they make an excellent point – one I’ve made as well – about how little need there is for attackers to even adopt GenAI in their operations:

> 

Attackers do not let “good enough” be the enemy of perfect and care about results, not hype; perhaps defenders could learn from them.

# Bring a bucket and a ROP for this WAP

The tl;dr here are vulns are back babyyyyyy. Exploitation almost tripled (up 180%) from last year, but still pales in comparison “ways-in” wise (i.e. initial access) to credentials or phishing; it’s 10% of initial actions in breaches. Breaking that down a bit more, attackers predominately exploited vulns in web apps, followed by desktop sharing software and VPNs.

A chart showing the various ways-in for breaches that didn&rsquo;t involve whoopsie-daisies by well-meaning humans.

Yet, the chart above suggests credential stuffing in a web app is still the primary way in for anything that isn’t a “whoopsie” kind of breach. Cred stuffing is certainly not as scintillating as vuln exploitation, but we shouldn’t sleep on it, either (it would be great to see the loss data associated with cred stuffing vs. exploitation, but alas). Either way, web apps remain a favorite for attackers.

On the topic of vulns more generally, they insist that “It’s much easier to harden a system than it is to harden an individual,” which suggests they are not familiar with Ao3 users.

The 2024 DBIR also veers into software supply chain territory and… well, here are my thoughts. It’s perhaps worthwhile to create a new designation for incidents and breaches involving third-party software libraries – even though I find “supply chain interconnection” odd phrasing – especially since it grew from 9% last to 15% presence in breaches (68% growth year-over-year, so close!).

But their commentary around these “supply chain interconnections” leaves much to be desired. They say:

> 

Let’s unpack that. For one, this is hardly actionable. How are we to know what software is resilient? I quite literally wrote a book on software resilience and read academic research across every possible complex systems domain regarding resilience for fun and I can tell you that none of them know how to directly measure resilience yet. Not volcanic plumbing systems, not forest ecology, not food supply chains nor neurology. Sure, we have hunches like temporal autocorrelation or functional diversity, but without this turning into a whole diatribe, suffice to say that we can barely verify that our security controls work as expected, let alone delve into those more complicated endeavors.

Next, it’s missing all sorts of stuff that we can do to minimize the impact of software vulns that aren’t “just don’t write vulns, duh.” I mean this somewhat literally, for the report says elsewhere:

> 

I don’t think they were joking? But in any case, yes there are numerous other ways to frame this problem and a dazzling variety of solutions around vuln exploitation that I covered with a co-conspirator at length in two RFI responses on Security by Design as well as OSS Security so please read those if you would like a deeper dive.

Briefly, I’ll offer a few provoking questions: What if the same vulns were present, but couldn’t be chained together, or got the attacker much less access? Would there still be ~1,500 breaches reported? I suspect not, and that leads to the following jumble of points:

1. punishing devs (including the horrible DX of many vuln scanners) is far from our holy grail
1. isolation (both spatial and temporal) – and modular architecture more generally – really should get hyped more to address both the “couldn’t be chained together” and “got the attacker much less access” goals… but alas, VCs would rather fund AI holograms that shame devs for mistakes and industry thought leaders can’t sell out by promoting it
1. we do not learn from other industries; the whole point of safety in other domains is that things still work even when there are flaws, like the plane still flying with a crack in its wing, because they focus on minimizing impact
1. look at Rust’s CVE list (to really lean into my crabbiness); Rust dispenses a CVE for anything that could possibly violate the safety of its abstract machine, even if misused. If we did that with C and C++, we would see no end to CVEs; the design behavior of addition, subtraction, function calls, etc. is as vulnerable when misused (and they’re very easy to misuse); the point is: Rust tries to make certain classes of vulnerabilities impossible to write and considers it a security bug in Rust itself whenever it’s possible to write one without using unsafe (even if it’s academic and confined to sample code in a pedantic GitHub issue); C++, in contrast, considers this the user’s problem
1. anyway, the point is, there are lots of ways to disrupt attackers, many of which we can borrow from the software engineering community (who often invented these clever things to minimize the impact of performance failures); I’ve written a ton about this elsewhere in books and blogs and papers, so let’s keep moving
My final gripe related to the software vuln commentary regards their section on malicious packages (page 45). Frankly, it feels misleading. Their implication is that malicious packages have an impact on breaches, but they do not cite evidence in favor of that interpretation. If anything, the data seems mixed in; the rest of the report (rightly) focuses on impact, whereas this section is about potential.

Without that hard evidence connecting potential to real impact, it’s disappointing to see the 2024 DBIR lament how easy it is to install libraries. The benefits of software should be accessible to all. It should be easy and not gatekept by tower-skulking mages with power they hoard from the masses.

Because that same ease of installation begets the ease of upgrading, which, as stated earlier (and last year), is a key contributing factor to why Log4Shell wasn’t as horrible as we feared.

# Security teams Ransomware with corporate budgets

In the 2024 DBIR, the team combines Ransomware and Extortion breaches and I agree with that decision. As they note, it’s often the same attackers conducting these operations and choosing their own adventure based on the optimal monetization of whatever access they gain. I like to abbreviate ransomware + extortion as REx, kind of like JLo6.

REx made up ~62% of “action varieties” in financially-motivated breaches, while pretexting (like business email compromise) was 24%. One especially interesting finding to me in the DBIR was that, when they removed Ransomware groups from the “system intrusion” dataset (the types of exploit pew pew compromises we glamorize), the actor split is 44% criminal and 40% state-affiliated actors. I interpret this as evidence that criminals overwhelmingly pivoted to REx – for exploit pew pew operations, at least – away from other monetization methods, like the now-uncool payment skimming.

The 2024 Verizon DBIR reports that the median loss from ransomware and extortion breaches is up to $46,000 with a loss range of $3 to $1,141,467 for 95% of cases. The $3 lower bound is up from $1 last year, which follows NYC pizza slice inflation pretty well.

A chart showing adjusted incident cost for Ransomware

They also leveraged data from a ransomware negotiator – which means there’s inherent bias in the data towards well-resourced organizations – and found that the median ratio of the initially requested ransom to company revenue was 1.34% (between 0.13% and 8.30% in 80% of cases); presumably the final median ratio was lower after they negotiated the payment down.

But, only 4% of ransomware + extortion complaints had any actual loss, down from the already-meager 7% last year. Specifically, 96% of ransomware incidents resulted in no direct loss (there might be subsequent costs associated with investigation, etc., but the DBIR is not privy to those).

Okay, so, let’s do some more bad math: if we have a meager 4% probability of loss and multiply it by the 1.34% revenue figure, we get a preposterously approximate budget of 0.05% of revenue for ransomware protection (to break even on the loss).

For a company guzzling $100mm in revenue, the median spend on ransomware should therefore be ~$54,000. If you’re buying EDR, that gets you something like ~300 licenses at best, which is way too few for most organizations making that much money. More likely, these organizations have at least 1k endpoints, which would be more like $185k per year for EDR… and this ignores the cost of backups and other things that are very useful to minimize the impact of ransomware.

To be clear, I’m not saying we should “let the bad guys win” or all the other pejoratives security pros have thrown at me over the years when I talk about the economics of cyber stuff7. The reality is that there is a huge trust problem in many companies between the cybersecurity org and the rest of the org, and talking about the sky is falling and it’s going to cost us a blahajillion of dollars will not help your cause.

It’s far better to present this kind of evidence with a range of options like (assuming an example revenue of $100mm):

- We start with the assumption of 4% probability of any loss
- We can assume either the 20% confidence interval, median, or 80% confidence interval
- These options mean we either invest $5,200; $53,600; or $332,000 on ransomware protection
- If we want to really cover tail risk, we can look at the 95% interval, which means we’d invest $999,600 on the problem
- Then list out what mitigations you can get at those price points, starting with backup costs or implementing isolation / modularity, then moving to fancier things like EDR
- Now the organization can make an informed choice! Probably even they will agree spending $5,200 is absurd, especially when we’d likely want backups for other use cases, anyway. And they’ll likely reject the nearly $1mm option, too. But in between is a lot of wiggle room and now you look like a well-informed leader rather than Don Quixote.
A chart showing adjusted incident cost for Ransomware

# Conclusion

I unironically relish the Verizon DBIR, and 2024 is no exception. We are an industry starved for data and they throw their whole being into trying to untangle the mess of incident and breach reports into something informative and consumable by the community. You can read it here.

Yes, I quibble with some things as always, but this is really a great input for anyone – security teams or engineering teams alike – to inform their investments. If you’re a vendor who has information that could be useful, please consider contributing to the report8 as a way to level up everyone’s understanding of what the everliving fuck is actually going on in cybersecurity.

<3 thanks AP

Enjoy this post? You might like my book, Security Chaos Engineering: Sustaining Resilience in Software and Systems, available at Amazon, Bookshop, and other major retailers online.

1. 
1. 
1. 
1. 
1. 
1. 
1. 
1. 

