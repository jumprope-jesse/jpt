---
type: link
source: notion
url: https://www.bitsaboutmoney.com/archive/debanking-and-debunking/
notion_type: Political News
tags: ['Running']
created: 2024-12-10T14:40:00.000Z
---

# Debanking (and Debunking?)

## Content (from Notion)

Recently, noted VC Marc Andreessen kicked off a discussion about debanking, in a podcast with his co-founder Ben Horowitz (begins at 7:42) and in an appearance on Joe Rogan’s podcast. The venture firm they founded, a16z, also published a brief on this topic.

The central thrust, quoting a16z’s brief (ellipsis in original): “Debanking can therefore be used as a tool or weapon systemically wielded by specific political actors / agencies against private individuals or industries without due process. Imagine if the government decided who could or couldn’t get electricity merely because of their politics, or some arbitrary reason… without having to explain, notify, or offer recourse. That’s what’s happening with debanking.”

If you are new here, you are presently reading a column which routinely covers compliance-oriented topics at the intersection of the financial system and technology companies. This topic is pretty central to my beat, and I have some relevant personal knowledge.

“It’s not a conspiracy theory if people really are out to get you.” sums up part of my reaction to this, but only part. There exists some amount of conflation between what private actors are doing, what state actors have de facto or de jure commanded that they do, and which particular state and political actors have their fingers on the keyboard. These create a complex system; the threads are not entirely divorced from each other.

A few disclaimers:

I previously worked for Stripe, and am currently an advisor there. Stripe is not a bank, but many regulated financial institutions have similar considerations. I’m not speaking for them. Stripe does not necessarily endorse things I say in my own spaces.

The recent debanking discourse focuses (and overfocuses; see below) on crypto. I am (somewhat notoriously) a crypto skeptic. Arguments aren’t soldiers; the truth is the truth. The truth sometimes favors crypto advocates in this discussion, and where it does, I will cite sources extensively. Where it doesn’t, I will mostly cite sources extensively.

The debanking discussion arises from an explicitly political project. Moreover, questions of public policy are frequently political in a democracy. The ballot box is the ultimate check on government abuse of power. While I have no project here, and try to be non-partisan in professional spaces, to ease the fears of crypto fans: I’m definitely not a secret Warrenite.

## Closing bank accounts

“Debanking” describes a cluster of behaviors.

The most salient one is involuntarily closing a customer’s bank account, often a long-established one, optionally without presenting a reason. Because “debanking” is an advocacy term, that often gets conflated with declining to open an account for a person or a business.

These two things are very different in their impact on the person/firm and in our moral intuitions. It’s the difference between getting divorced and being turned down for a date.

Advocates often invoke a user-centric perspective of debanking, focusing on the impact on individuals/firms. Then, they conflate it with regulators’ decisions regarding bank supervision, in ways which are facially not about direct user impact. We will return to bank supervision later.

Industry doesn’t call it “debanking.” This is partly for the usual corporate euphemism reasons. This is partly because industry does not always share assumptions of how the world should work with advocates, and is concerned that “debanking” smuggles in those assumptions.

So when one discusses this with colleagues, one might use words like offboarding, derisking, closing the accounts of a customer, etc.

There is often an implication, and much rarer a reality, that the debanking decision is not one of a single financial institution. Sufficiently correlated “independent” decisions by financial institutions could deprive a firm or individual of access to banking services. We will explore some coordination mechanisms, which are overstated, and some correlation mechanisms, which are poorly understood.

We’re hearing about debanking because it sometimes affects socially established wealthy entrepreneurs and their companies. Some people it happened to are densely networked and also affiliated with talented communicators that have (in the parlance of our times) a platform. It is important to say from the jump that this is not the typical profile.

A huge majority of all people who find their accounts involuntarily closed will have been let go for credit risk or operational cost reasons. Overdraft your account repeatedly and look unlikely to be able to pay the fee for this service? Expect to lose that account, and probably all other accounts at that institution.

Do you know anyone with a parent advanced in years, who is dealing with challenges of aging, perhaps has gotten scammed a time or three, and might occasionally lash out at customer service employees? Debanking is more relevant to their interests than they might currently appreciate.

Decisions to debank an individual will often debank their controlled entities, and vice versa. Debanking will also not infrequently swiftly cascade to accounts in the same household, regardless of title (non-specialists can round this to “name on the account”; industry can’t). Banks institutionally consider those accounts in the same household to be highly likely to be under common control, regardless of what paperwork, account holders, or politically influential subcultures believe. This is an area in which the mores of the banking industry are much closer to the traditional middle class than to coastal elites.

Sometimes, though, one gets one’s accounts closed because one has activities which are outside a bank’s risk tolerance or contrary to their compliance posture. This was cited to me both times I was debanked.

### Two debanking anecdotes explained

Once upon a time, I had a U.S. checking account. One day, the bank called me, and asked me why I was averaging two incoming ACH transfers a day. I told them that I ran a sole proprietorship selling software over the Internet. The ACH transfers were from from my two payment providers, which paid me out my sales (less fees) once per business day. The bank thanked me for my explanation and told me they thought the business sounded legitimate. Then they said I had 30 days to move the business’ funds flow to a different bank, or they would close all my accounts.

“Banksplain that offboarding?” Typical retail consumer checking accounts are, on the spectrum of the full menu of banking services, extremely low-risk, not a focus of bank examiner time, and institutionally preferred by both banks and regulators because of core financial access concerns. Accordingly, the amount and degree of monitoring a bank invests in the consumer checking line of business will be relatively low, in line with a risk analysis it performed. Its regulator has read that analysis and decision, and expressed no objection to it.

This particular bank did not, at the time, have a small business practice within its personal banking division. Very many banks do, but this particular bank did not. And thus this bank had not built out the higher degree of policies and procedures that would support small business banking. A surprising example of a small business that demands drastically more thought than you would think is discussed in detail below. The bank, on learning I had a sole proprietorship banked with them, considered that behavior innocent but not supportable, not because it didn't like my business but because it knew it had no built out infrastructure to support any business.

At the second institution, I once checked my U.S.-organized individual retirement account from a Japanese IP address. I had done that many times, but I did it one last time, too. This caused a short phone call, where the bank’s affiliate confirmed that I indeed lived in Japan, then informed me the account would be immediately restricted and then closed. I would need to make arrangements to request my shares be transferred to a new (U.S.) brokerage account, or authorize them to sell and mail me a check.

“Banksplain that offboarding?” This was likely downstream of a procedure implemented to ensure that the institution’s affiliated securities firm did not act outside the scope of its broker-dealer licenses, which (the institution was aware) did not include any with Japanese regulators.

When these events happened, it was very annoying. I did not contemporaneously understand why they were happening. They required me to take time away from life, my day job, and business to make more phone calls, learn more things about the financial industry, and ultimately open new accounts.

That is the typical end to a debanking story. “And then, I opened a new account.”

Immigrant communities keep lists of which banks most want their business. So does the community of people who run small software businesses online. And so, while immigrants and small software companies deal with substantially more banking friction than the typical American working for Google or a university does, they are both very bankable.

Consider crypto entrepreneurs who have received an offer of investment of several million dollars. One might be able to hold the ideas in one mind simultaneously that a) there is some diversity of life experiences in that group but b) on average though, they are very socially advantaged, when considered on most of the usual axes. Despite those substantial advantages, it has been persuasively alleged that their companies and the entrepreneurs themselves routinely suffer debanking.

I also understand this to be true, in large part downstream of one risk factor that they hit more than almost all legal businesses of comparable scale and sophistication. There have been times and places where this challenge made crypto firms almost unbankable to the extent banks knew what they were doing. And it directly drives decisions against crypto founders and employees.

## Debanking specifically for AML risk

I’ve written extensively about KYC and AML and will not recap all of it here. Banks have a panoply of obligations under regulation. One of those is that they have to write AML policies, including policies which identify high-risk activities. Then they have to follow those policies. You can overpromise but you cannot underdeliver; after you’ve told a regulator you will do X, not doing X can result in fines and other punishments, even if the regulator did not tell you to do (specifically) X.

Before we reach crypto, consider AML risk and its consequences among money services businesses.

Running a money services business (MSB) is virtually universally called out as a high-risk activity by banks’ internal AML policies. Explaining why would require explaining the entire history and object of AML. Please just take as writ for the moment: all banks have a list, those lists rhyme with some variation, and MSBs are on all the lists.

Some banks have built out so-called enhanced due diligence (EDD) programs under which they will bank MSBs. Many banks have not; if a business banking at one identifies itself as an MSB, or if their ongoing monitoring of transactions suggests one is probably an MSB (for example, if there are ACH pull from Western Union for tens of thousands of dollars, which will suggest to an analyst that the business is probably a Western Union agent transaction above the de minimis threshold), the bank intends that business to get a letter.

Whether they successfully execute on the letter, and the decision the letter announces, varies, but in terms of intent, they intend to consistently reach the decision given similar facts.

That letter will, in all likelihood, not be candid as to what is happening or why. It may not cite that the customer is an MSB. It may not cite why the bank believes that. It will not recount the bank’s internal AML policies which identify being an MSB as a high-risk activity, though it might say four or five templated words about risk. It will not explain the bank’s strategic decision to not invest in a compliant EDD program that would allow it to service MSBs.

No, the letter will say that the bank is closing the customer's accounts.

It may describe this as a "business decision", using those two words, of the bank. It will often say that this decision is final. The decision is probably not actually final. That is an opening negotiating position, like “We don’t negotiate salaries.” If you don’t argue the point, it has achieved its objective. The grain of truth within it is “We probabilistically think that talking with the typical recipient of this letter is negative expected value.”

Why doesn’t the bank want to talk with the typical recipient about it? Because the typical MSB is a bodega with a sideline in alternative financial services.

You might think that it is absurd that the government would concern itself with MSBs that are clearly the sideline of the local bodega. Without reaching the question of whether this priority is absurd, I invite you to peruse the Financial Crime Enforcement Network’s Enforcement Actions For Failure To Register As A Money Services Business. These are a small sample of real enforcement actions. That sample was chosen by FINCEN and I think reasonable people understand it was not chosen by FINCEN with a goal of embarrassing FINCEN or the entire AML regime that ensures FINCEN employees will have a job tomorrow.

I will take the liberty of fictionalizing names here, to give you the flavor of real people with real businesses that FINCEN both a) prosecuted and b) posted trophies of pour encourager les autres : Bob Smith d/b/a Bob’s Fast Gas. Taro’s Snack Shop, Inc. Cheap Phonez 4 U, Inc. Ben Goldberg d/b/a Kosher Foods.

FINCEN has posted the full text of each settlement, frequently including a restatement of their alleged violations. In many of those documents (not all of them!), if one credits FINCEN’s narrative as Gospel truth, one will believe: yeah, this is absolutely a bodega. The Financial Crimes Enforcement Network has jammed up the guy behind the counter because he failed to have a written AML/KYC policy and because when he traveled overseas the person he hired to mind the store was not trained in AML. Having won the case, they fined him $10,000. Given that, a fair-minded reader immediately assumes the bodega is probably not actually a front for the Colombian drug cartels, Hamas, or a foreign intelligence operation.

With this well-evidenced understanding of FINCEN’s… quixotic interest in the crime of selling money orders and also laundry detergent and delicious sandwiches, you can understand why a bank, attentive to FINCEN’s desires here, is doing something that strikes many people as insane. It has employed teams of people whose job is to make sure it sifts the rogue bodegas from the garden-variety bodegas before FINCEN asks “Why did you move money for a rogue bodega!? How many times do we have to tell you people! BE ON THE LOOKOUT FOR ROGUE BODEGAS.”

Running EDD processes and ongoing monitoring is expensive. Banking a bodega isn’t very lucrative. And thus most banks won’t bank a bodega that is also an MSB, despite them having no particular malice against bodegas or the people who run them. This won’t change if the bodega owner calls to them to protest that he is a legitimate businessman, that this debanking is un-American, or that he feels like they are discriminating against him for being an immigrant. That’s a conversation the bank has had a thousand times and never want to have again… with a bodega owner.

Some MSBs are fintechs. They have teams of people who are extremely aware of financial regulation. Those professionals intentionally chose a bank which was capable of banking at least some MSBs. They then had a laborious bespoke conversation about risk tolerance and mutually agreed-upon compliance procedures.

More than zero fintechs have been debanked over the years, but they probably don’t first learn about it from a paper letter. Their team of people who do bank things all day would have heard from the team of people that do fintech things all day, likely beginning many moons ago. And if they got the letter, they would understand generally why they got the letter, and not be so oblivious as to trust the literal text of the letter.

Class is an interconnected set of culture, scripted behaviors, and the advantages and disadvantages that attach to them. The culture that is the American professional-managerial class has a relationship with truth which occasionally confounds outsiders to it. An American PMC member, particularly one with a professional specialization in banking, understands an offboarding letter to be a ritual object rather than something meant to be taken literally.

Many regular people who get the offboarding letter are confused and upset. Most people who get this letter are insufficiently expert in the financial system to understand what is going on. Many of them are (perhaps sensibly) enraged that the bank seems reluctant to offer answers. If they successfully pry answers out of the bank, the answers sound like nonsense or change constantly.

Here, advocates often say that banks lack fundamental humanity, regard for their customers, or simple competence. I’d tell them that is neither here nor there, but the challenges described in Seeing like a Bank drive far more of this than malice, apathy, or incompetence as such. It is a systems issue.

But AML-driven offboarding has one particular spectral signature which is worse than normal debanking, which will always be a confusing, unpleasant experience for most customers.

Some of these customers are getting the letter because the bank looked into their account after a transaction was flagged as suspicious. This generally happens because an automated system twinged on it. Most of the so-called “alerts” are false positives, but banks are required to have and follow a procedure to triage them. That procedure is typically “Send a tweet-length summary of the alert to an analyst and have them eyeball things.” Every bank needs at least one person triaging alerts; the largest banks have thousands.

What if the analyst, on the basis of their training, experience, and data available from the alert system and from the account history they can access, decides that a transaction has… more than nothing irregular about it? Then they compose a specially formatted memo.

That memo is called a Suspicious Activity Report (SAR). The bank files it with FINCEN, via a computer talking to a computer after the analyst pushes some buttons. Then the analyst goes back to triaging incoming alerts.

Busting bodegas is a sideline for FINCEN; receiving SARs is their main job.

A SAR is not a conviction of a crime. It isn’t even an accusation of a crime. It is an interoffice memo documenting an irregularity, about 2-3 pages long. Banks file about 4 million per year. (There are some non-bank businesses also obliged to file them, but nobody is presently complaining about decasinoing, so ignore that detail. Banks are the central filers of SARs.) For flavor: about 10% are in the bucket Transaction With No Apparent Economic, Business, or Lawful Purpose. FINCEN has ~300 employees and so cannot possibly read any significant portion of these memos. They mostly just maintain the system which puts them in a database which is searchable by many law enforcement agencies. The overwhelming majority are write-once read-never.

Banks are extremely aware that most SARs are low signal, and that a good customer might wander into getting one filed on them. But there are thresholds and risk tolerance levels. And SARs will sometimes, fairly mechanically, cause banks to decide that they probably don’t want to be holding a hot potato. It’s risky, plausibly, and expensive, certainly. At many institutions, for retail accounts, the institution will have serious questions about whether it wants to continue working with you on the second SAR. It will probably not spend that much time thinking deeply about the answer.

So can the bank simply explain to the customer that staff time preparing SARs is expensive and that routinely banking customers who turn out to be real money launderers is a great way to end up with billion dollar fines? No, they cannot.

The typical individual named in a SAR is low-sophistication and cannot meaningfully participate in a discussion with a Compliance officer, because they’re very probably at the social margins. Do you have a favorite axis of disadvantage? Immigrant, no financial background, limited English ability, small business owner, socioeconomic class, etc? The axis has non-zero relevance to one’s probability of getting a SAR filed on oneself due to innocent behavior. Very many people who have SARs filed on them are disadvantaged on several axes simultaneously.

No, the bank cannot explain why SARs triggered a debanking, because disclosing the existence of a SAR is illegal. 12 CFR 21.11(k) Yes, it is the law in the United States that a private non-court, in possession of a memo written by a non-intelligence analyst, cannot describe the nature of the non-accusation the memo makes. Nor can it confirm or deny the existence of the memo. This is not a James Bond film. This is not a farce about the security state. This is not a right-wing conspiracy. This is very much the law.

If you work at a regulated financial institution, in the U.S. or any allied country, you will be read into SAR (and broader AML) confidentiality within days of joining. You will be instructed to comply with it, very diligently. If you do not, your employer may suffer consequences. You personally are subject to private sanction by your employer (up to and including termination) and also the potential for criminal prosecution. If your trainer speaks with a British accent, they will phrase the offense as “tipping off.”

It’s not just illegal to disclose a SAR to the customer. It is extremely discouraged, by Compliance, to allow there to be an information flow within the bank itself that would allow most employees who interact directly with customers, like call center reps or their branch banker, to learn the existence of SAR. This is out of the concern that they would provide a customer with a responsive answer to the question “Why are you closing my account?!” And so this is one case where in Seeing like a Bank the institution intentionally blinds itself. Very soon after making the decision to close your account the bank does not know specifically why it chose to close your account.

This strikes many people as Kafkaesque. (Me, too!) It is the long-standing practice of banking in the U.S. and allied countries. It is downstream of laws passed by duly elected representatives. It was not capriciously developed as a political tool in the last few years. (We’ll get to those.)

Crypto-investing VCs are not low-sophistication operators of the corner bodega. They are extremely aware that crypto is on the high-risk list at many institutions. They would prefer this were not so.

Their preferences regarding the high-risk list at, say, portfolio fintech companies are sophisticated and nuanced. For example, they will (accurately!) say that the high-risk list authored by a company socially close to them did not arise in a vacuum. Certain entries were foisted upon them by financial partners. Their financial partners will, over drinks at the bar, very quietly, say that they can relate to occasionally feeling powerless. And, though many will find this dumbfounding, their regulators will frequently say the same thing.

Occasionally. About some entries. We shall return to the mechanisms.

### Debankings of founders as opposed to firms

Plausibly some crypto founders are low-sophistication about the finance industry in their early days as founders. This is not a judgement about one's character. Nobody is born knowing everything, and very few people will have a serious and informed encounter with this topic ever, not in school, not at work, not in being a generally well-read individual, unless and until it is professionally relevant to them.

Perhaps a founder might ask a friend: “I run a legitimate business which happens to be in crypto and suddenly found my personal accounts closed. Why did this happen? I did nothing wrong.”

Playing the odds? The bank thinks there is an unacceptable risk that you will use your personal accounts to launder money on behalf of the business (and/or its customers, etc). The bank has insufficient controls to give them an appropriate level of certainty as to whether you’re doing this or not. They are disinclined to find out the hard way, so they invite you to find another bank.

Why do they think you might launder on behalf of the business? In part because of the extensive history of crypto companies laundering funds through the accounts of their founders and employees, specifically, and the banking industry’s highly-evidenced belief that businesses and their owners routinely commingle funds, generally.

Tether maintained access to the banking system by, among other mechanisms, having their executives establish accounts in their own names, stashing funds in the name of a lawyer, and using their non-executive employees as money mules. SBF had many talents but one of the main ones was money laundering. A major mechanism for that was loaning money (mostly customer assets and mostly sham loans) to employees then representing to banks (and others) that the employee was making an independent transaction not affiliated with FTX/Alameda/etc.

One would have to be very new or very incurious to be interested in crypto companies and be unaware of this history. Banks were rarely incorporated yesterday, and certain varieties of incuriosity-with-benefits are extremely frowned upon.

## Presumption of innocence by commercial providers

But there is something to the critique, by advocates, that rampant lawlessness within crypto for a decade and a half shouldn’t cause an institution to stereotype an innocent crypto founder. Advocates want debanking to only follow an investigation uncovering a) strong evidence there exists b) a particular articulable risk which c) society actually cares about.

Part of it is philosophical: they believe they are entitled to something like individualized attention and a presumption of innocence. This assumption is deeply embedded in our legal system.

We do not have this assumption embedded in our banking system.

It would be laughable for credit accounts: “I have never defaulted on a loan from you, and therefore, you must give me the benefit of the doubt, and issue this loan.” No intellectually serious person expects that from banks. No, we construct probabilistic models about who is likely to repay based on observable factors, less some factors which society has disallowed us from using under the law. If we deem you insufficiently likely to repay the loan, even if you are still very likely to repay the loan, you don’t get the loan. Finance is not high school; 92% is not an A- anymore. We don’t have to wait for you to default, or have any individualized suspicion about you, or conduct a years-long fact-finding process.

One is prohibited in discrimination in lending on basis of, for example, race. Why? The American people feel quite strongly that they want this to be true, and so their representatives passed a series of laws. Those laws are well-established and uncontroversial. You also, as young data scientists quickly learn, can’t use customer zip codes, no matter how probative they are. This is because they have a very high risk of being an effective proxy for race. (Aside: this is why California used zip codes when it wanted to prioritize the delivery of lifesaving healthcare to patients of favored races, primarily for political reasons.)

One is not prohibited from using someone’s occupation or ownership of a business as underwriting criteria. Those happen to be incredibly probative and, not incidentally, separate rules literally require that we ask. (AML rules require a bank opening an account with ongoing transaction capability to ask for what your source of funds will be, which will often include wages and/or business income, and banks then generally need to know “... OK, wages for what?”)

Is there a built-out appeals process or higher authority with respect to being declined banking services? Don’t our moral intuitions require there to be one?

Many people with “capitalist” in their job title will tell you that there is, indeed, a higher authority to complain to if a capital allocator rejects your pitch. It is Mr. Market. That capital allocator has competitors. Go pitch them. Are there projects that no capital allocator will fund? Absolutely. That’s an important part of why we pay allocators: they assist us in not frittering away resources society expects to fund e.g. teachers' retirements on non-productive uses.

And so allocators will tell you: If you can’t find any allocator who will back you, despite your belief you have a good business plan, and your business plan requires capital to execute, you do not have a good business plan, and you should do something else with your life.

I have yet to meet a venture capitalist who believes that passing on a pitch should be subject to review by a higher authority than their partnership. Many do not, as routine practice, tell entrepreneurs why they passed. Pure downside. Passing is not an invitation for the founder to work their persuasive magic on you. The meeting was the opportunity for that; the meeting is over.

But banks are, certainly, not venture capitalists. There is an aspect to banks which is not exactly dissimilar in character to infrastructure providers. Utilities are frequently invoked as an example here. Why would we construct a society in which power companies needed to make investment decisions in supplying power?! (I think people surprised there may be surprised to do deep dives into e.g. negotiating power purchase agreements.)

Banks, in addition to providing infrastructure, are also neck deep in capital allocation. Some bits of the bank might be more like one's conception of a power company, and some bits of the bank might be more like one's conception of a venture capitalist. And some bits might be confusing hybrids of two intuitions.

It may surprise you that a simple vanilla deposit account is both infrastructure and also a capital allocation decision.

For one thing, typical deposit accounts in the U.S. are actually credit products. It's baked in and can't be baked out without making them unfit for purpose.

For another:

## Banking reputable, legal crypto businesses is a risky endeavor

Sources of credit risk to the bank are substantially broader than simple non-repayment of funds borrowed. A financial institution can take a credit loss on banking a business without having what most non-specialists would consider a credit relationship. This is particularly true when banking financial service providers.

Here’s a worked example:

Suppose a crypto exchange blows up out of nowhere, in an absolutely freak accident that happens in about 20% of all exchange-years. The last financial institution banking them can end up holding the bag.

Voyager Digital was a regulated institution that was publicly traded. It had adults at the helm, a Compliance department, some level of written risk processes, and legitimate backers, including well-known venture capitalists.

Voyager blew up, because none of the above are sufficient to prevent you from blowing up.

When they blew up, their bank (Metropolitan Commercial) received a slew of ACH reversals. Customers (often quite reasonably!) felt that they had sent in money to buy crypto, but they hadn’t received their crypto, which feels quite a bit like fraud, and so they complained to their (the customer’s) bank.

Metropolitan characterizes that complaint as fraudulent behavior. There are certainly fraudulent accusations of fraud made to abuse cryptocurrency exchanges, by paying for crypto, claiming you didn’t get the crypto, and then getting your money back while you keep the crypto. However, the customers Metropolitan wanted permission to stiff perceive themselves as having no money and also no crypto. The customers had traded money for a claim against a bankruptcy estate.

Crypto is a product with widespread adoption across the socioeconomic spectrum, I am told. Do you think a random person off the street would, on being asked "Define a claim against a bankruptcy estate?", have a really confident, automatic answer to that question? I think they would probably have a more confident answer to the question "Have you ever tried to buy a claim against a bankruptcy estate?"

So what happens if one calls one's bank and says “I opened an app on my phone. I tried to buy something. I didn’t get it. Those bastards kept my money.” Very frequently, your bank’s customer service rep will type some brief notes into a web application then hit a button. The customer service rep is trained to sound helpful when this happens. Their skill with that... varies. They make, oh, $15 an hour and are not trained like a district court judge. They will conduct no real investigation nor careful balancing of facts and circumstances. They are likely entirely unaware of notorious bankruptcies in the crypto industry, which are an infintessimally small portion of all complaints that reach their telephone queue. Customer didn’t get something from an Internet merchant? Push the button, read the script to the customer, disconnect, immediately serve next caller.

That button will, some steps later, mechanically cause Metropolitan to transfer back some money to Voyager’s now aggrieved customer, which (importantly) Voyager did not actually have to distribute, because it was in bankruptcy. Whose balance sheet did it come off of, then? Metropolitan’s. Their shareholders had just performed the sacred duty of equity: taking the credit loss so that depositors didn’t have to.

If you are banking a quickly growing financial services firm which has large daily funds flows, and charging small per-transaction fees and/or earning net interest on deposits, the total amount of money at risk (within the chargeback or reversal window) as of time T can be vastly larger than the total revenue charged for services at all times 0 through T inclusive. A handwavy approximation for it: number of days in the relevant chargeback/dispute window times average daily transaction volume times dispute percentage. (This will be in the low to high tens of percent. It depends on many factors, including the sophistication of your customer base, whether well-informed guides to consumer rights in banking go viral within it, and similar.)

And thus banks are very selective with respect to what financial services firms they bank. Because one blowing up, just one, can sink the entire related business line.

Voyager and Metropolitan ended up asking the court to change the rules of the ACH protocol in their favor. Then banking technologists told the court that the ACH protocol was computer code maintained in a decentralized fashion and thus beyond the purview of any court. Wait, no, that sentence is from my unpublished cyberpunk novel and somehow made it into this essay by accident; please disregard. No serious person would say courts cannot interact with software or the people who write it. The court ordered a protocol upgrade. The court’s order was swiftly carried out, like many court orders, by responsible professionals employed by several firms.

Metropolitan, of course, got sued over the whole Voyager fracas. A major aspect of the lawsuit: Voyager intimated to customers that they would be covered by FDIC insurance and so their funds on deposit were safe. Voyager’s CEO has alleged that Metropolitan’s management suggested this selling point. Voyager’s marketing department published objectively false statements regarding FDIC coverage. “[FDIC coverage] means that in the rare event your USD funds are compromised due to the company or our banking partner’s failure, you are guaranteed a full reimbursement (up to $250,000).”

Marketing departments frequently misunderstand fine distinctions here, which is why, at well-operated financial technology firms, Legal does not let marketing write one single word about FDIC insurance without their sign-off. The fateful two words above are “the company”: FDIC insurance does not and has never backstopped the obligations of non-insured clients of the banking system. It only backstops the obligations of insured financial institutions. (Had Metropolitan failed, Voyager’s customers may have had recourse to FDIC insurance, but Metropolitan did not fail.)

And so the FDIC has not paid Voyager’s customers one thin dime, nor will it ever. It has neither obligation nor legal authority to do so.

The FDIC is institutionally very opposed to fraudulently inducing customers to transact via claiming FDIC coverage. The FDIC is a banking regulator, among other things, and we’ll discuss them more in a moment. But they are, first and foremost, in charge of the deposit insurance fund. Crypto’s history of falsely promising that the FDIC will make customers whole for its own failures is one reason why the FDIC is institutionally wary of crypto.

Metropolitan then ceased crypto banking. Several banks which had major or incipient crypto practices ceased crypto banking roughly contemporaneously.

Was Metropolitan within its rights to do so? Ab-so-lutely.

Was it within its power to not exit crypto banking? Some thumbs were placed on the scale, and Metropolitan acknowledges this, though they probably were not dispositive for Metropolitan specifically. Their incipient crypto business blew up in their face. Heads would likely have rolled in any event.

Metropolitan characterized their decision as influenced by commercial and regulatory concerns, but long coming. Quote:

Today’s announcement of our exit from the crypto-currency related asset vertical represents the culmination of a process that began [six years earlier] in 2017, when we decided to pivot away from crypto and not grow the business.

Suppose you are an internal advocate for crypto at a mid-sized bank in the U.S. When you bring your proposals to management, one of the things that will cause a chilly reception is the regulatory environment, certainly. Another one is that management can read the newspaper. Other banks which got this pitch and greenlit it took huge losses, ate months of negative headlines, and will be under examiner’s microscopes for at least the next year. This happened over almost no revenue. Why should management say “Yes, as long as it is only the high-quality crypto companies, as long as you cross your Is and dot your Ts, this seems like a low-risk business to be in? Yeet me some Shiba, bro.”

Anyhow, when a crypto founder couldn’t find a bank in 2011, one could be excused for blaming reflexive banker conservatism and low levels of technical understanding. Crypto has had a decade and a half to develop a track record to be judged on. Crypto is being judged on that track record.

Some advocates consider this unfair. Sure, sure, there was some… cowboy behavior in the early days, but that’s just the price of innovation. The freaks and geeks are always on the cutting edge of technology, and well, you know, I suppose they might not always listen to lawyers. But the early days are basically over. We bring something completely new to the table. We are responsible professionals with a compliance-first mindset. We are thoroughly committed to working with partners in finance and government to assuage all concerns. We have impeccable pedigrees. We say all the right things, in all the right accents. We are capable of hiring lobbyists, making campaign contributions, and engaging in a considered media strategy, too!

## Some chill felt is caused by the long shadow of SBF

Much has been written about Sam Bankman-Fried and his co-conspirators and enablers. That story remains extensively misunderstood and undercovered relative to its importance.

SBF et al orchestrated a sequential privilege escalation attack on the system that is the United States of America, via consummate skill at understanding how power works, really works, in the United States. They rooted trusted institutions and used each additional domino’s weight against the next. A full recounting of the political strategy alone could easily fill a book. The forfeiture allegations fill 26 printed pages at 1-2 lines per targeted politician. The United States has also alleged that he tried to buy the Bahamas.

SBF and most of the co-conspirators were focused on the Democratic side of the aisle. His cutout Ryan Salame was the bagman for the Republican side of the aisle. Salame’s own lawyers, in their sentencing memo (pg 11), in what is a unique legal strategy, disclaimed any good intent: “Whatever the topic, Ryan’s ultimate purpose for [meetings with government officials including including Senator Mitch McConnell and then-Congressman Kevin McCarthy, focused on pandemic preparedness] was eventually to influence cryptocurrency policy.”

SBF was not charged for the bribing officials part of the crime tapestry, putatively due to treaty commitments to the Bahamas. C.f. the extradition treaty, Article 3. (I absolutely believe that that was a complication and disbelieve it was a hard constraint.) It was an element of plea deals by several co-conspirators, most of whom got lesser sentences for cooperating with the government. Salame was uncooperative and sentenced to 90 months. SBF’s parents appear unlikely to be charged. This is despite them being active and knowing participants in crime, including providing their son with extensive advice, in writing, on topics germane to their professional expertise. For example, his mother, a Stanford law professor and Democratic bundler, advised him to use his coworkers as straw donors to avoid compromising optics via mandatory disclosure laws. IANAStanfordLawProfessor, but that is plainly illegal.

SBF was considered, for a time, the heir apparent to George Soros. He was the next generation’s well-monied Democratic standard bearer in Washington. One major reason why crypto has experienced what feels like performative outrage from Democrats since 2022 is that they are trying to demonstrate that crypto did not successfully buy them.

Many in Washington, like many in crypto, have… selective memories of what meetings they took, transactions they entered, calls they made, and cookies they noshed on in 2020 and 2021.

But to remove the beam in my own eye before casting out the mote in another’s: SBF struck me as whip-smart, extremely cynical, but sincere with respect to his motivations. I thought him likely one of the most competent operators in crypto. (Don’t assume that I meant that as high praise, please.) Also I understood him contemporaneously to be Tether’s bagman and told people, privately, “Don’t get too close; 5% chance he goes to prison.”

In hindsight, I overrated the competence in several important domains, and totally missed the massive fraud. This was in no small part because of a strong sense of fellow-feeling. We have blind spots the size of Jupiter for people who remind us of ourselves and our closest friends. It’s hardwired into humanity, I think.

Anyhow, Tether’s current most important bagman is Howard Lutnik, who may be stepping back from the position, as he’s currently leading Trump’s transition team and has his eyes on bigger prizes. Forget MicroStrategy’s high implied volatility. Lutnik convertible arb would be the trade of the century.

Some crypto advocates believe it’s unfair to tar the industry with the SBF brush, for either industry internal reasons (“He was CeFi not true DeFi, and tried to force the rest of us along with it! Nuts to him!”) or political reasons (“Not my side of the aisle! Salami, you said? Never heard of him neither!”)

Here we are again at the tension between a) democracies should practice careful consideration of individuals on their merits and reject collective punishment but b) the political system shouldn’t have the memory span of a squirrel.

## Operation Choke Point

Once upon a time there was an impressively unprincipled set of decisions made. Like many such tales, it didn’t happen as one discrete event in a smoky backroom. It started small and then cascaded, was covered up, and then came to light. Then, it was roundly and justly castigated.

There are certain incredibly non-salubrious businesses that make routine, intense use of banking rails and which simultaneously generate many customer complaints. Debt collectors are one such business.

Full disclosure: I was an unpaid advocate for consumers with issues with debt collectors (and banks, FWIW) for many years, and have described debt collectors as “among the most odious hives of scum and villainy as exist in the United States.” I’m also grouping a few clusters of consumer credit bottom feeders under “debt collector” or we’d be here all day: payday lenders, so-called “credit repair” companies, and debt-adjacent telemarketing.

Banking regulators, in response to customer complaints (which savvy customers, such as customers who listen to advocates like yours truly, will sometimes route through regulators because that achieves better outcomes than routing through CS), warned banks that debt collectors appeared to be at grossly disproportionate risk of ACH transfers that customers claimed were unauthorized. Customers claiming this are not always being candid. However, debt collectors do routinely abuse one’s common intuitions about how banking rails work as an intentional strategy. See the above piece for elaboration at length.

Now, banks who bank debt collectors can math out how many of their ACH payments are complained about. One can make an argument that those banks might not have institutional knowledge that complaints about debt collectors are structurally anomalously high, for Seeing like a Bank reasons. One could further argue that a regulator can licitly tell a bank something they don’t know. That sounds reasonable and an appropriate use of a public servant’s time.

Those banks that would open accounts for debt collectors (n.b. not all banks!) are OK with having that business. Debt collection, while not salubrious, is legal and regulated in the United States. Banks are not one-stop monitoring shops for all of their customers’ various obligations under the law.

But working through legislatures and courts is slow and expensive. Why not simply deputize the banks? We already have them run private intelligence agencies! How much of a reach is it for them to also run private consumer protection bureaus?

The Obama administration didn’t like debt collectors, for very similar reasons to why I don’t like debt collectors. And so they broadened the critique: the risk in banking bad guys was broader than the (known, accepted, controlled, and certainly not existential) risk of ACH reversals. Those customer complaints, those complaints could harm the bank’s standing in the community. That could result in e.g. a withdrawal of customer deposits. This would imperil the bank, for the usual reason. And if something could imperil banks, why, that should naturally cause the FDIC to make its opinions known.

Get out of peril, by kicking debt collectors to the curb.

But the FDIC had to be persuaded into that point of view, by a cadre of very talented people.

The Department of Justice had a legal theory, which it was quite proud of. The Financial Institutions Reform, Recovery, and Enforcement Act of 1989 (FIRREA) gives the DOJ a hunting license for any fraud (and many other crimes) which affects a federally insured financial institution. FIRREA was passed after the savings and loan crisis, to protect small financial institutions from peril and thereby avoid another crisis.

Now your common sense understanding might be “Oh, Congress probably intended on cracking down on fraud targeting banks which, I don’t know, was big enough to imperil a small community institution? I could see a really large fraudulent bank loan imperiling a small bank. And checking the history books, there were some wildly fraudulent bank loans mixed up in the S&L crisis. OK, so we federalized prosecution of defrauding a bank like that? Sounds reasonable.”

If you have that intuition, you are apparently not creative enough to have worked as a lawyer in the Obama admin DOJ. No, their thought was that if you provide rails which facilitate fraud, such as giving a fraudster a bank account, you are affecting a financial institution: yourself. And so, the DOJ can go after you, for self-harm. Note that you do not need to lose money, oh no, the DOJ can also go after you because the way you affected yourself was to cause your regulator to like you less. When you settle with the DOJ, it will extract an enforceable promise in writing that you will stop your campaign of self-harm, and also stop banking specifically enumerated industries, like payday loans.

I realize that this sounds unlikely. The following is a direct quote (expanding acronyms) from the DOJ Office of Professional Responsibility, in the report (pg 16) where they exonerated DOJ lawyers.

As more fully explained below, the [Consumer Protection Branch] has relied on the “self-affecting” theory, as well as additional theories of liability, in three cases arising from the Operation Choke Point initiative.

Now when the DOJ or FDIC tells you, a bank, to do something, or strongly suggests that you do something, that usually isn’t the end of the argument. You can certainly haggle. You can even fight… to a degree.

This is a multi-year iterated game with repeat players, each of whom has limited resources and very complicated preferences. Both sides are constantly picking their battles. There is give and take. When your counterparty is happy with you, your emails get returned faster, you get more of your asks, and you can report smooth sailing to your boss. Both banks and regulators are ultimately made up of people, with emotions, career paths, and annual performance reviews.

Banks do not actually make a lot of money from servicing debt collectors. The culture that is banking looks at the culture that is debt collection and sees slimy people who are beneath it. And so the banks frequently obliged. Many of them, in their offboarding letters to debt collectors, were unusually candid relative to the standards of offboarding letters: it’s not you, and we apologize for this, but we’ve received regulatory guidance about your industry, and as a result our appetite to serve your industry no longer exists.

As it turns out, the Obama administration had many diverse policy preferences.

It wasn’t particularly in favor of guns, for example.

Gun sellers don’t use banks in the way that debt collectors use banks. They do not routinely trick customers into the gun-for-money transaction. They don’t make particularly intense use of ACH pulls (confidence: 99%, on general industry knowledge) and don’t have particularly high dispute rates (confidence: 95%, same).

But regulators, having discovered that “reputational risk” attached to anyone you didn’t like with nary a whisper of complaint, believed that banking gun sellers was high-risk. Haven’t you read the newspapers? School shootings. Do you want any of that sticking to you? You are imperiling your good name, and therefore the stability of your deposit base, and therefore your bank, and therefore the insurance fund, by accepting the business of gun sellers.

In Congressional testimony, the FDIC said that it hadn’t ordered anyone to debank disfavored businesses.

What we have done is we have tried to be very clear in putting out our guidance to say very publicly and clearly that as long as banks have appropriate risk mitigation measures in place, we are not going to prohibit or discourage them from doing business with anyone with whom they want to do business.

One may be surprised that this individual might perceive themselves as telling the truth here. Because “Justify to me why the payday lenders are not on your high-risk list.” and then “Do you have a built-out EDD program for the deposit risk caused by payday lenders?” followed by “Then are you sure you should accept that business?” are consistent with this statement, individually and as a script. (Those are not quotes, but rather indicative summaries of stages in a conversation. I believe them to fairly characterize conversations that the record abundantly shows happened.)

The FDIC Office of the Inspector General, in an investigatory report, attempted to shift all blame for Operation Choke Point to the DOJ.

We found no evidence that the FDIC used the high-risk list to target financial institutions. However, references to specific merchant types in the summer 2011 edition of the FDIC’s Supervisory Insights Journal and in supervisory guidance created a perception among some bank executives that we spoke with that the FDIC discouraged institutions from conducting business with those merchants. This perception was most prevalent with respect to payday lenders

When a regulator publishes position papers that it wants you to do something, and reiterates this in individualized supervisory guidance, that tends to create a perception in this author that the communicated policy direction was not YOLOed onto the Internet by a room full of monkeys banging keyboards randomly.

As frequently happens, the individual officials who had instructed banks to debank the targeted industries ignored Stringer Bell’s dictum on taking notes on a criminal conspiracy. Emails sent within the FDIC and DOJ were routinely archived, and banks (of course) keep copies of correspondence from their regulators. Those emails said what they said, and what they said was pretty damning.

For example, the Department of Justice’s internal Six Month Status Report On Operation Choke Point (excerpted in Congressional reporting) said:

Finding substantial questions concerning the legality of the Internet payday lending business models and the loans underlying debits to consumers’ bank accounts, many banks have decided to stop processing transactions in support of Internet payday lenders. We consider this to be a significant accomplishment and positive change for consumers . . . Although we recognize the possibility that banks may have therefore decided to stop doing business with legitimate lenders, we do not believe that such decisions should alter our investigative plans.

Not once, not twice, not a handful of times, not a loose confederation of rogue examiners. Three of six regional directors of the FDIC offices told the OIG that they understood Washington to want payday lending discouraged and two of them said there was an expectation to, in the words of the OIG, direct institutions that facilitated payday lending to “pursue an exit strategy.”

Did that require top-down direction? You can, in fact, generate nationwide programs with local offices doing strikingly similar things without top-down direction. The combination of a monoculture plus a policy direction that lower-level staffers believe in is often sufficient to make it happen. We have extensive experience of this in tech and finance, as discussed later.

Japanese has a beautiful world, sontaku, for the attitude and actions a diligent subordinate would take without his superior’s explicit instruction, believing them to anticipate his boss’ desires. Sontaku is a core skill in the American professional class. People possessing it are sometimes described as “motivated self-starters”, “high-agency”, “bold”, ”takes initiative”, ”acts like an owner”, etc. You are a very, very bad Compliance professional if you aren’t constantly sontaku-ing your regulator. You are also a bad Regional Director of the FDIC if you aren’t constantly sontaku-ing Washington.

But Operation Choke Point, specifically, simply was official policy. If it wasn't, no entity as complicated as the United States can ever be described as having even once had an official policy.

As the former Chairman of the FDIC wrote in a WSJ editorial:

Internal Justice Department papers released by the House Oversight and Government Reform Committee make it clear that Justice prefers coercing banks to drop customers through Operation Choke Point rather than prosecuting illegal or fraudulent businesses directly because it’s easier, faster and requires fewer resources.

Operation Choke Point wasn’t just targeting debt collectors, gun sellers, and payday lenders. No, the FDIC’s bullet-pointed list was 30 entries long. They range from clearly abusive and illegal (scams) to “One could construct a narrative by which banking that industry is challenging” (pornography) to “a grab bag of things we dislike” (racism and… fireworks? Really?)

Operation Choke Point, once it came to light, caused a media and Congressional furor, because it was arbitrary and lawless. (I am using that in the ordinary sense of an American who took civics, not in the specialized sense of a DOJ lawyer, who might bristle for being called “lawless” when they had three court cases and one 25 year old statute which are clearly explained in the memo as adding up to them being able to do everything they did.)

The architects of Operation Choke Point steadfastly denied it was designed to do what it was manifestly designed to do. They denied it did what it manifestly did.

The agencies were then pointedly accused of lack of candor with Congress. If you tell a Congressman he isn’t reading the WSJ right, but internally your bosses are high-fiving themselves over WSJ article, and they are high-fiving themselves because finally the WSJ is covering their important work accurately, Congress will not be pleased. Then they will show you a copy of your bosses’ emails, which they can subpoena, because they are Congress. (House Oversight Committee report, ibid, pg 10)

Some scholarly literature is sympathetic to the regulators’ point of view. (More is not.)

If you want a steelman, that’s the best one you’ll likely find. It acknowledges the DOJ’s efforts to interdict fraud by creatively interpreting FIRREA and targeting third-party payment processors and banks, accuses the financial industry of making a fuss over this for self-interested commercial reasons, performs a modified limited hangout of the high-risk list, and claims that the gun industry cynically glommed onto the news cycle for political reasons despite no actual enforcement specifically addressed against it.

My point of view? I can read emails. They say what they say, even when acknowledging what they say would cost a public servant their job. I read the postmortems (including many years ago; this sort of thing was my hobby before it was my job). I view them as face-saving exercises written, in no small part, by civil servants mortified that their peers could lose jobs and pensions simply for implementing the Administration’s policy preferences using colorable authority.

Sometimes, people have been known to lie in politics. Sometimes justice is not done. I know, try to weather the shock you must feel.

Operation Choke Point was mostly forgotten, except by banking nerds.

Until…

## So-called Choke Point 2.0

Nic Carter, a crypto VC and podcaster, who occasionally does very good work, has been steadfastly attempting to brand a constellation of regulatory activities regarding crypto as Choke Point 2.0. This branding is an attempt to delegitimize them by associating them with politically-motivated lawlessness. It has since become popular among crypto advocates.

Unlike Operation Choke Point, which actually was a centrally directed operation with written project plans, status meetings, ongoing progress reports, and a code name decided by the participants (who, in hindsight, should have talked to their own Comms department and picked something that didn’t sound nefarious to describe their plans), Choke Point 2.0 stretches like taffy to attach to any recent regulatory activity crypto advocates don’t like. So we’ll have to review quite an involved history of very disparate issues to give advocates a fair hearing.

Carters' work, which is extensive on this topic, exists in pieces like Did the government start a global financial crisis to destroy crypto?

To answer the question in the title: no, it did not. We started a financial crisis which to-date is mercifully narrow as an underappreciated side effect of interest rate hikes to tame inflation.

Silvergate: Crypto had a bank, doesn’t now, and misses the good days

Crypto advocates have specific and general concerns about banking supervision at a small cadre of banks acutely relevant to their interests. They have tied these concerns to the debanking narrative.

They do not evince attention to detail or familiarity with the procedural history of specific examples they invoke, though some have attempted some original reporting with respect to these issues. That is to their credit.

As we’ve established, almost all banks consider crypto businesses to be high-risk, and avoid them. There was a small cadre of banks which had active crypto practices. Those banks purported, to the public and their regulators, to have the EDD required to bank them compliantly. This was incredibly operationally useful for crypto, for one very obvious reason (substantially every business needs a bank account) and one less obvious one.

Crypto talks a great game about decentralization, but centralized systems are more efficient than decentralized systems. When riding banking rails, making transfers outside of regular banking hours (which have five twos of uptime) is difficult. This exposes firms to risk and acts as a constant cost of capital.

Crypto trades 24/7. Crypto firms would like to settle crypto trades, particularly between stablecoins and the USD backing them, 24/7. Crypto’s solution to this was to all bank at the same bank, Silvergate, which I described (with some surprise, when they IPOed) as the First National Bank of Crypto.

Silvergate had a particular product called the Silvergate Exchange Network (SEN). SEN was both a) boring infrastructural plumbing and b) extremely important to the crypto industry. Oh boy, do crypto companies miss SEN. In sum, SEN would allow substantially 24/7 book transfers between Silvergate customers to shift USD balances between their bank accounts. This would let them constantly settle the USD leg of crypto trades between each other.

This was particularly important for stablecoin issuers, like Circle, which issues USDC. Circle’s main custodial bank for USDC was SVB. Circle wanted to be able to issue marketmakers like DRW and Alameda Research hundreds of millions of USDC 24/7 at any hour on any day with no more than a few minutes of latency, or redeem USDC for greenbacks in a similar fashion.

Now, a thing you will frequently see in fintech banking, and which is not itself at all inappropriate, is a fintech having multiple banks with a division of labor. One of those banks might agree to have a fintech’s customer-facing high-velocity low-EOD-balance transactional activity. And one of those banks might agree to have a fintech’s low-velocity high-EOD-balance deposits. These are very different business propositions for the banks! They imply different risks, different core competencies, and different revenue opportunities.

If you are running businesses which both a) have high daily inflows and outflows and also b) want to keep billions of dollars in the regulated banking perimeter, you very much need partners comfortable with both halves.

The argument you make, as a fintech, to the bank with your deposit business is that the other bank is also a competent, U.S.-regulated financial institution, with good AML and KYC controls (among others). Therefore, when your business makes one wire at the end of the day to settle up with its omnibus account at that bank, netting over several hundred thousand customer transactions, perhaps for several hundred million dollars, your bank should be comfortable, even if it has very little exact knowledge about what happened today.

Probably the same story as yesterday, and tomorrow, and Compliance can sleep the sleep of the righteous, because their trusted peers have an appropriate degree of controls in place. The bank custodying the money mountain is thus certainly not aiding and abetting money laundering. It can rely on the second bank’s own surveillance and controls, in addition to the crypto firm’s compliance department. There will be many formal contractual promises and informal verbal or written assurances made about this. And this works and serious people can accept it but the factual probity of the high-velocity transactional bank is extremely load-bearing.

Silvergate was not a competently run institution.

SEN did not, in fact, have a robust controls environment. It, in fact (para 70), had functionally no transaction monitoring. Silvergate had bought a standard package that a lot of banks use for automated monitoring, but due a configuration issue, it was off for SEN transactions.

Carter describes this state of affairs as follows: “Silvergate’s transaction monitoring system for SEN had gone through an upgrade and experienced an outage.”

Silvergate was institutionally aware of the “outage” but unable to remediate it.

I have an engineering degree, have founded five software companies, have worked in the tech industry, and in my entire career, I have never described an engineering investment I failed to make for fifteen months as an “outage.” After a day it is an outage, after a week it’s a human competence issue, but after a year it ferments into sparkling tech strategy.

During that period, SEN transacted over a trillion dollars. Silvergate was not unaware that SEN had an up-and-to-the-right usage graph (congratulations!). They were just routinely ignorant of funds flows they were facilitating with their banking license, sized in the billions of dollars per day. We know this because of Silvergate’s contemporaneous internal communications, the technical reality of the artifacts they had purchased and implemented, and sworn statements in litigation and to regulators. It is beyond intellectually serious dispute.

What of it, though? Is that just a harmless paperwork glitch? I'm glad you asked.

Intrabank book transfers are historically low-risk for money laundering because they’re ineffective at accomplishing layering: the same Compliance department can see both legs. Moreover, the majority of them are between entities known to be under common control. The purpose of layering is to break the chain of surveillance; swapping between your left pocket and your right pocket in front of a Compliance officer doesn’t accomplish this. This assumption of low-risk was apparently, per Silvergate’s employees, baked very hard into ATMS-B, the new-and-improved monitoring suite Silvergate had implemented.

However, SEN transactions, while implemented as intrabank book transfers, are in fact high-risk. The designed intent of SEN is to allow counterparties not under common control to settle one half of a transaction, at very high velocity. The other half generally occurs on a blockchain, unsurveilled by the bank. If you can’t see that half, and you can’t see your half, why, that sounds like you are swapping bank deposits for cash equivalents sized in the billions of dollars per day with no functional AML monitoring program in place.

This is not just me saying it. Kathleen Fischer, Chief Risk Office of Silvergate, said internally, of the lack of SEN monitoring: “We have known of this issue and either we have established other controls to account for it or we haven’t, and we have to take our lumps.”

Silvergate had not, in fact, established other controls.

Carter claims that all clients of the bank had gone through rigorous KYC and onboarding processes. Silvergate may have consistently conducted KYC and onboarding processes, but one could forgive a skeptic for believing them to be pro forma.

Silvergate onboarded several entities relating to Binance, a confessed criminal conspiracy which extensively engaged in money laundering. Binance and its management are Bond villains; they gleefully flouted the law and engaged in jurisdictional gamesmanship to avoid financial regulation, for years. Binance et al transacted $22 billion through Silvergate.

Mandatory compliance training is such a drag, and sometimes we like to spice it up with fun games. Let's play Spot the Red Flags together.

We have just received an account application from a Seychelles-docimiled corporation beneficially owned by a globally notorious billionaire. He disclaims any permanent address. The beneficial owner receives regular negative news coverage. He and his company have received multiple orders to cease business from peer nations. Those orders cite offering financial services without a license, suspicion of money laundering, willfully non-compliant posture, and extensive documented lies to regulators. The corporation has no operations or employees; it is strictly a shell. The planned funds flow is receiving inbound wire transfers, including international wire transfers, from counterparties which the bank will have only fragmentary third degree knowledge of. The corporation intends to immediately transfer those deposits to a third-party financial institution. This is to facilitate those counterparties’ purchase of pseudonymous bearer instruments, specifically, cash equivalents. The corporation anticipates billions of dollars of volume, in transaction sizes up to eight figures.

Silvergate happily opened an account (pg 4) for Key Vision Development Limited, the above-described shell company, and allowed it to deposit and withdraw over $11 billion. Now, credit where credit is due, Silvergate did debank Key Vision Development Limited in 2021. The record doesn’t say why, but perceptive readers may be able to hazard a guess. But Binance’s main entities still enjoyed attentive service, or perhaps more to the point they enjoyed all the inattention they were getting with their service, until the bank folded.

But the main rake Silvergate stepped on, repeatedly, was its relationship with FTX/Alameda and its executives. They were collectively the bank’s largest client and comprised tens of percent of its deposits. Silvergate’s monitoring of their usage was minimally grossly inadequate, as the bank and its executives admit.

Carter quotes an unnamed Silvergate executive as saying the following, which is roughly consistent with their prior statements to the media and to regulators.

Where we were not as buttoned up as we should have been was in regards to the FTX/Alameda clients. That was a function of the bank growing incredibly quickly[.] … Probably we could have figured out FTX was brokering deposits via Alameda. In retrospect I think we could have pieced this together and figured it out. But this is not a legal failure and we’re not required to catch everything. Our program passed legal muster. That’s something we could have done a better job of. But there was no intentional wrongdoing or cooperation with the bad guys.

This is consistent with things they have said previously, but does not demand unlimited deference.

Ryan Salame, a subject matter expert in laundering crypto money through the banking system (skills described by his lawyers, see pg 7 and onwards), tweeted that it beggars belief that Silvergate did not know that Alameda Research and North Dimension were in fact receiving FTX customer funds flow. Salame has repeatedly stated that Silvergate intentionally orchestrated that funds flow in concert with him. Even if it had not, Salame is just right: even if FTX concocted the scheme internally and even if Salame somehow managed to push all the buttons himself, Silvergate had to know.

But suppose you credit neither Salame nor I with understanding how banks work, or you demand unquestioning deference to executives’ denials, perhaps because one believes that a bank executive would never ever lie. The picture most favorable to Silvergate is that, during multiple years of being monomaniacally focused on growth to the neglect of its responsibilities under the law, it routinely underperformed the competence bar required of regulated financial institutions in the United States.

Silvergate voluntarily liquidated in the wake of the FTX implosion. Limited props for them here: they managed to do this in a mostly orderly fashion, as opposed to Signature, which had substantially less crypto exposure but blew up. (Signature had an analogous book transfer API product, called Signet. It is a smaller part of their story.)

Carter has a number of complaints with regards to supervisory activities relating to Silvergate Bank. One of those is that he alleges the Office of the Comptroller of the Currency disallowed Silvergate from selling SEN. I find this allegation very plausible, if not specifically evidenced. Silvergate was operating a trillion dollar laundering machine which had drawn immediate demands for corrective action for an extended period, had not taken aggressive corrective action, and then had proximately caused enormous consumer harm in a way which was maximally embarrassing to many policy actors. When the bank’s Chief Risk Officer predicted incoming lumps, these were the sort of lumps she was predicting.

Carter further alleges, and I think this is substantially original reporting (and good on him for it), that the FDIC and other banking regulators gave verbal guidance that banks should get crypto deposits below 15% to be “safe and sound.” If a banking regulator invokes those words, they are not making a suggestion. Carter complains that there is no statutory authority to pick this arbitrary number, that this threshold makes banking crypto functionally impossible, and that it is specifically chosen to kill targeted banks.

Some regulators are disclosure regulators. The SEC comes to mind. Some regulators are prudential regulators. The ordinary operation of prudential regulators is to take broad statutory direction and transform it, sometimes via the rulemaking process and sometimes via more informal guidance (and, even the FDIC will tell you, “moral suasion”). This process yields both concrete asks and fuzzier spectral ranges subject to ongoing negotiation between regulators and the regulated.

Does the FDIC have statutory authority to pick magic numbers? Yes, in the political system of the United States, it does, and it can cite that authority to you at length. The FAA has statutory authority to pick magic numbers for bolt torque. The FDA has statutory authority to pick magic numbers for permissible flow rates for ketchup.

Are regulators overreaching here? Not obviously so! Look at the above description of Operation Choke Point and their theory of regulatory authority there. It requires magical thinking to connect banking a payday lender, reputational risk, a run on your bank, and endangering the deposit insurance fund. It very much does not require magical thinking to think that crypto deposits are flighty, correlated, and could cause a run! We were experiencing actual crypto-induced runs!

A reasonable argument can be made that the problem with regulators was not abuse of discretion. It was needing to pay for past regulatory mistakes and/or missed opportunities with overcorrection following substantial consumer harm. Examiners (stunningly) missed that Silvergate’s new business model, which they had IPOed on the strength of, had materially changed from its days as a sleepy two-branch real estate bank! That reasonable argument has been alluded to… by the Federal Reserve! See Findings, pg 2.

Does the 15% threshold make it generally impossible to bank crypto? Empirically not; other bank’s crypto practices are well beneath that threshold, which likely informed how it was chosen. Metropolitan, for example, had about 25% at the peak and then drew down to 6%. It fairly persuasively told stakeholders that it had done a good job of risk management. And, not incidentally, Metropolitan is still with us. And so regulators could very reasonably say: “OK! 6% is all-else-equal green, 14% is yellow, we don’t want you spiking to 25% anymore, 96% is deep #%*(#(ing don’t even think about it red.”

And you could make this same observation about many banks with a crypto practice. Coinbase doesn’t keep customers' money in a mattress. Their main bank’s crypto exposure is… <Jamie Dimon grabs the keyboard>FORTRESS BALANCE SHEET</Dimon not actually grabbing the keyboard>.

Carter further alleges or insinuates (it’s a bit unclear at times which he is going for) that Senator Warren and/or regulators colluded with short sellers to intentionally kill Silvergate, via sparking a liquidity crisis.

He specifically cites a this letter by Warren et al, which includes the sentence “Should it need extra liquidity, your bank has access to taxpayer dollars through the Federal Reserve Bank of San Francisco and the Federal Home Loan Bank of San Francisco.”.

Carter argues that sentence was intentionally inserted to put pressure on FHLBSF to demand repayment of advances. That would force Silvergate to find liquidity at a time where that would be incredibly difficult. Silvergate, subsequent to that letter, did repay those advances, and said in a securities filing that this required them to accelerate securities sales, leading to rumors in the industry that this forced their hand on deciding to close. FHLBSF has squarely denied pressuring them to accelerate repayment.

Short sellers made a killing on Silvergate, certainly. I absolutely believe that short sellers communicated with Senator Warren and regulators and additionally would credit that they did this strategically to bring pressure to bear against the bank. Evidence in favor: they say they did and bragged about it, while nailing Silvergate's hide to the wall.

But the reason short sellers made billions shorting Silvergate is primarily because they were right and early about Silvergate.

Marc Cohodes (a noted short who was deeply short Silvergate) and Ram Ahluwalia (a crypto investor with a very good understanding of bank regulation) had a debate about Silvergate prior to its collapse. I will not recount it for you on a line-by-line basis, but on listening to it at release, I felt “Cohodes is winning this by a mile, despite Ahluwalia being better calibrated on whether banking a single money launderer would indict a compliance program in the eyes of a regulator.” (I was at the time effectively constrained from trading in bank stocks, but I took professionally significant action after listening to that podcast.)

I think one could make some criticisms of Cohodes, or of short sellers generally, but “They were fundamentally wrong more wrong than right about the short thesis, and needed government intervention to make it pay out” requires ignoring mountains of evidence. You are invited to look back, with full oracular hindsight, on what Cohodes said in that presentation.

A heuristic I have long used, as a once-upon-a-time debater: if one side is impressively detail oriented, and randomly selected details are trivially sustained, and the other side doesn’t allege details but pounds the table a lot, bet on the first team.

Or, if you want, you can bet on their former executives. Their former CTO (after being Chief Operations Officer), who is also the CEO’s son, has a Twitter account. You can find his side of the story on it. For a bank executive he is remarkably cavalier with characterizing the contents of communications from his regulators.

For example, he writes “The Sunday after Thanksgiving in 2022, regulators went after 5 banks simultaneously[.] Up to that point the regulators were not objecting, Silvergate brought them along, and suddenly everything changed[.]”

In fact, in April 2022, Silvergate had received a Matters Requiring Immediate Attention (MRIA) from the Federal Reserve specifically concerning the adequacy of its BSA/AML monitoring program. They received a similar MRIA in November, but by that time, they were cooked. See SEC complaint, para 80, substantially confirming representations made in a deposition by “Former Employee 5” (a Compliance official) in this lawsuit, which explicitly allege MRIAs. A MRIA, as distinct from a Matters Requiring Attention (MRA; a formalized supervisory directive which they expect you to pay substantial attention to in the ordinary course of business), is a drop-everything-and-fix-immediately command.

The Federal Reserve has required language (pg 3) for when it communicates MRIAs. The Federal Reserve supervises many banks, at all levels of scale and sophistication. This includes small town community banks where board members are typically local real estate developers. To ensure that low-sophistication bank executives or board members do not miss the fact that an MRIA is both an order and a shot across the bows and should be understood as such, that language is: “The board of directors (or executive-level committee of the board) is required to immediately…” (bolded in original)

The SEC has since charged Silvergate executives with misrepresenting the truth to investors about the depth of their liquidity problems in the immediate wake of the FTX collapse.

Suppose one believes, arguendo, the protestations of Silvergate management that it had seen the implosion of their largest customer, and a ~70% outflow of deposits, and was still ready to keep chugging along.

In that world, is the regulator saying (approximately) “We support banking legal industries, given an adequate controls environment. However, you must get your crypto deposit concentration to below 15%?” compatible with the continued existence of Silvergate specifically, after early November 2022?

I agree here with Carter and crypto advocates: no meaningful concentration limit on crypto is compatible with the continued existence of Silvergate after early November 2022. Even a 50% concentration limit is impossible; 15% is worse.

Simple math: for each dollar of deposits that you don’t bleed off, and you really can’t bleed off many post-run, you need to find someone willing to deposit about $5. Even if your sales pitch made angels weep to hear it, that is an impossibly tall order. Silvergate had no path to swiftly raising many billions of dollars of deposits from non-crypto depositors.

Silvergate had attracted its existing deposits via what would most charitably be described as intense attention to the needs of the crypto industry. It had no advantage over any bank in the U.S. vis banking any other individual or industry, and it had many disadvantages. It was under a PR cloud, because facts about its behavior over the last few years were being reported. It was obviously wobbling as an enterprise.

Most deposits are attracted by offering routine bank services (the sort that Silvergate had no edge on providing to non-crypto clients). This is referred to in industry as the “deposit franchise.” Banks have an immediate option to raise deposits in a hurry, forgoing years of sponsoring Little League teams, showing up for the annual town festival, and asking about your holiday plans over a coffee. You can skip the sweat-and-smiles business and proceed directly to paying through the nose, by attracting the custom of sophisticated financial professionals who place money at the banks bidding highest for it in the country. This is called deposit brokering.

At any price Silvergate was capable of paying for deposits, there was a regional bank that would have matched or exceeded it, because (unlike Silvergate) many regional banks have a material first-party loan book (and ongoing origination apparatus) which they reasonably believed would continue to exist, and deposits are a funding source for that loan book (and apparatus).

A deposit broker would reasonably model that hypothetical replacement bank as being a higher priority for receiving extraordinary backstopping if that ended up being necessary. This would play into their credit analysis of that replacement bank if the deposit broker was trying to place, for example, a $200 million certificate of deposit, almost all of which is uninsured (subject to bank credit risk) absent extraordinary government backstop.

Crypto advocates are notably incurious about non-crypto banking and don’t seem to understand why non-crypto regional banks were being heavily shorted in late 2022 and early 2023. I believe that, for many crypto advocates, including some who are well-educated financial service professionals, including some whose portfolio include many financial services companies, this is not very cynically ignoring background unfavorable to their narrative. Rather, it is because they genuinely do not understand what a sudden hike in interest rates would do to the balance sheet of a bank, in the same way that many software engineers do not understand what a sudden interest rate hike will do to the value of their equity. I would credit the possibility that some crypto advocates do understand how bank balance sheets are affected by interest rates, and are choosing to not contradict their standard bearers in public.

I am unconvinced that the concentration limit was the but-for cause of Silvergate’s demise, though I could be persuaded to that view.

My default view is that if every government employee had been furloughed on Thanksgiving Silvergate would likely still have closed. Its regulators had utterly lost confidence in it, true, but its customers had also lost confidence in it, in no small part because a) they knew they had wired money to Silvergate and b) they knew they now didn’t have their money. That’s a bad set of facts for a long, happy banking relationship.

I also think, and won’t ask advocates to acknowledge this, that a post-investigation Silvergate which managed to exist would be unable to offer the product that people were really buying. It was the Schelling point for everybody in crypto. That is why SEN worked. In no conceivable universe does Silvergate keep Binance as a client after it gets put under the microscope. A crypto Schelling point which Binance can’t touch is not a crypto Schelling point. Absent that Schelling point, if Silvergate was simply a bank that would let you park a $3 million seed round and cut paychecks while you worked on your solidity… that Silvergate is not a business. And it’s a bad time to not be a business while you’re sitting on a portfolio of MBS in late 2022 and early 2023.

But suppose arguendo that the government intentionally precipitated conditions incompatible with Silvergate continuing to remain in business and also that this was the but-for cause of Silvergate’s demise.

Is that a norms violation? Do we allow the government to close banks?

If you’ve worked in the financial industry in any capacity, you went to mandatory Compliance training. Attendance is taken and you likely had a refresher annually. And there were smirks, and jokes. And your trainer said, very seriously, “Pay attention. This is important. If we eff this up, they can do anything to us, most likely large fines but up to and including closing this firm. You, personally, could go to jail.”

Most people in finance heed this lesson. Every year, some don’t, and they learn why this training is mandatory.

Should we allow government to close banks? Yes.

Reasonable people can disagree as to the thresholds that extraordinary remedy should require and the procedural form it should take.

If we were still on debate team, you might ask me for a concession “Government needs to specifically admit that Silvergate was intentionally closed” and I’d counter “Sure, will trade you: opposition needs to concede that Silvergate was actively aware including at the executive level that Alameda and North Dimension were intentionally receiving incoming FTX customer funds flows.” About fifteen minutes later, I think neither side is thrilled, both sides learned something they find edifying, and there probably exists mutual agreement that either Silvergate had to go. or in the alternative Absent extraordinary government support, Silvergate was doomed after the FTX fiasco.

Complaints that Signature Bank did not need to be placed in receivership

Carter believes Signature was targeted in an analogous fashion. In part this is in reliance on their board member Barney Frank, who maintained (in media interviews contemporaneous with the collapse, and after it) that Signature was solvent and had sufficient liquidity at the end of a week which had seen a bank run.

Perhaps some have forgotten the context of that week. On March 8, Wednesday, Silvergate announced it was closing. On March 10th, Friday, SVB was placed into receivership, after the most explosive bank run in history. On March 10th, still that same Friday, Signature experienced a run of $18.6 billion of deposits in the space of hours.

That context refreshed, let’s review where Signature believed its business was on March 11th and 12th, over that weekend.

Signature experienced difficulties telling a plausible story involving numbers which added up  (pg 35) that weekend. Quoting that postmortem:

Signature needed to provide reliable and realistic data, particularly concerning immediately available liquidity and ongoing deposit withdrawals, to inform the analysis the Regulators and Signature needed to perform to understand the Bank’s liquidity position. Once Signature began providing any data on these key issues, the Regulators found the data was inconsistent and that it continuously changed in material ways.

Signature execs, et al, were on a series of conference calls with regulators for an entire weekend. They began with regulators taking note of the bank run and candidly announcing the bank was in mortal peril. Signature proceeded, in the regulators’ view, to confabulate about liquidity sources, composition and quality of assets, and current withdrawal requests pending, through either malfeasance or spectacularly poorly timed technical incompetence. Regulators felt that, at this pivotal moment, Signature was dangerously disconnected with reality, like an executive describing the weekend as (this is a quote) “uneventful thus far.”

It is a serious accusation to say Signature was confabulating. Banking regulators are (mostly) serious people.

Quoting the postmortem again:

For example, through Sunday afternoon, Signature represented to the Regulators that nearly $6 billion in liquidity from its commercial real estate portfolio would “Very Likely” be available to the Bank on Monday. The Regulators were aware, however, that it would take weeks for the FRBNY to review and value that portfolio.

Was Signature aware that its commercial real estate portfolio could not possibly be good collateral on Monday? Manifestly so.

A brief explanation for the benefit of readers unfamiliar with commercial real estate (CRE) banking:

Signature’s plan was to pledge portions of its CRE loan portfolio to the Federal Reserve Bank of New York the Monday after the critical weekend. It thought that the Fed would credit them for the value of the portfolio less some haircut. Signature would then immediately wire what the Fed credited them to the customers demanding their deposits. Simple as.

However, CRE loans are not fungible, easy-to-analyze assets like e.g. Treasury bills or even mortgage-backed securities. They’re complex, bespoke legal agreements, in the best of times. 2023 was not the best of times for the New York commercial real estate market, as anyone who reads the newspaper is aware, and so you can’t simply value those loans by copying outstanding balances into Excel then chugging a tiny bit of math. You’ve got to read the darn things, construct a model (which, if you were someone with skin in the game, would asymptotically approach re-underwriting those loans because New York CRE is that bad), come up with your impaired valuation, and then, haircut that.

Signature Bank had a crypto sideline but its beating heart was the New York CRE market. This is a bank that breathed New York real estate. It beggars belief that they thought that portfolio would be Very Likely to be good collateral in merely wall-clock hours of work.

You know what this reminds me of? This reminds me of one Sam Bankman-Fried who, on finding himself in what he believed to be a survivable liquidity crisis, began wildly writing indicative numbers down on napkins and/or Google Sheets. SBF still doesn’t understand why nobody believed him. Just look at the napkins!

We are not required to believe your napkins, Signature, if they contain obvious untruths, or if the napkins evolve wildly in inconsistent ways over the course of a single meeting.

The most critical question for Signature’s liquidity position was “How much money will customers wire out on Monday?” This is straightforward banking, which regulators pressed them to do all weekend: a) sum up how much money customers have asked for on Monday, in the hundreds of current pending wire requests b) project a worst case scenario for how that number will evolve, as more customers put in wire requests, before Monday morning.

Here is the time series (taken from above report, pg 40) of those two questions being asked repeatedly in a 48 hour window. Observe how often, a few hours after Signature has made a (new, even-more-worst-than-previous) worst case scenario, the known wire requests have already exceeded that worst case scenario.

Signature then communicated a new worst case scenario, which felicitously was only as far away from known wire requests as their previous worst case scenario had been, almost as if they were learning nothing from repeatedly being wrong.

This played out multiple times.

Signature believes it understood where it was that weekend. The above picture is almost proof positive that it did not. They also understood their experience of the weekend to be signaling how the worst was over.

Quoting postmortem again (pg 6):

Over the weekend, Signature’s estimates of pending deposit withdrawals increased, going from $2 billion on Saturday evening to $4 billion Sunday morning, and then to $7.4 billion to $7.9 billion by Sunday evening. These numbers represented known deposit withdrawals. Despite the run on Friday, March 10 and the negative news over the weekend, Signature insisted that additional withdrawals would be minimal on Monday. The Regulators assessed this projection as unrealistic and that the Bank needed to be prepared to handle another significant deposit run. (emphasis added)

Signature believes it could have white knuckled through the hurricane and emerged victorious on Monday. Then it had projections by which it would suddenly, indeed miraculously, have sufficient liquidity on Tuesday, Wednesday, Thursday, and Friday. And then the hard work would start. It would bank the heck out of its remaining customers, start finding buyers for its valuable assets over the ensuing months, and somehow pull this off. Because it was solvent!

Signature had critical liquidity issues, no real path to solving them, and lost the confidence of its regulators, during a bank run which was worsening by the hour. That is a recipe for receivership. No conspiracy is necessary to explain what happened.

The rest of the postmortem is worth reading, too, and deeply wonky in the way that excites banking nerds. Where else can you read a scintillating discussion on what capital call loans are acceptable collateral at the Fed emergency window?

Crypto likes novel crypto-using banking products

In 2022, the FDIC sent out a wave of letters to banks. Prying these letters from the FDIC has been a bit of a project, requiring Coinbase and other interested parties to do quite a bit of arm wrestling. The letters which have been released, grudgingly, are heavily redacted.

A brief commentary on transparency: democratic governance simultaneously requires substantial transparency and also requires the government to be able to have private conversations.

Curtains of secrecy are frequently invoked cynically to cover abuses. For example, you could say “That protest is a foreign influence operation! I cannot disclose my basis for thinking that, for reasons of national security! You should therefore act as my proxy to suppress this protest!” (Uh, spoiler alert, we will return to this later.)

In the culture that is banking supervision, however, privilege will frequently be asserted fairly maximally on routine supervisory communications with banks. This is because they are institutionally wary of causing risk to banks by signaling to the market or depositors that those banks have lost the confidence of regulators. Banking regulators are terrified of “self-fulfilling prophecies.”

You need to be able to have candid conversations with regulated entities for the same reason coworkers need to be able to have candid conversations with each other. Privacy enhances candor, even when those conversations implicate third parties, even when third parties would really love to be a fly on the wall.

And so I think there is a legitimate balancing act to be done here. But I’m sympathetic to crypto advocates who say (paraphrase) “This is backroom maneuvering to do something we don’t like. You won’t even admit the thing you are doing! And, confound you, after you are dragged kicking and screaming to admitting the thing, you’ll probably claim it is good! Like they did after Operation Choke Point!”

Conversely, when the government is capable of publishing extensively researched position papers and extensively footnoted indictments, that should give you more confidence that it is less likely to be engaged in lawless, arbitrary behavior. Not limitless confidence, certainly, but it is evidence in a direction.

Carter surmises that the expurgated supervisory letters are regarding NYDIG’s proposed product which would allow banks and credit unions to offer customers direct Bitcoin exposure. You can analogize this to the feature in Cash App which allows you to buy Bitcoin, without being able to transfer it, except it would happen in your banking app.

I think Carter is very likely (90%+) correct with respect to identifying the subject of these letters. Much of the pack is dated shortly before the FDIC did, indeed, publish public guidance about banks directly offering crypto products. NYDIG was the firm with the most progress against the opportunity (source: general industry knowledge) that otherwise fits with what we can read of the letters.

So: is this a stunning inversion of our democratic norms? No. Banking regulators get to weigh in on proposed banking products. That is the absolute core of the job. That will extremely routinely result in saying something which rounds, like many of the letters do, to “We are going to have a considered think about this and get back to you, but in the meanwhile, please don’t roll this out widely.” (The think was had; the results were published. Many crypto advocates do not like those results, and are asserting procedural irregularities because of that.)

Does this meaningfully prohibit the crypto industry from offering retail users financial services? No. You can buy Bitcoin exposure in Cash App, Venmo, Robinhood, Coinbase, Fidelity, Interactive Brokers, any brokerage account capable of trading U.S. ETFs, and many more places besides. Crypto advocates cheerfully blast out press releases about how many ways are coming online every week to buy their tokens from them at very reasonable prices prior to lunar travel .

Is there a facially plausible reason for attempting to institute a consistent policy among regulated banks, in a way there was not for Operation Choke Point? Again, a core concern for the FDIC is that unsophisticated customers don’t assume that their risk assets get FDIC insurance. Customers naturally assume their bank app gives them FDIC protected things. For those bank apps which include non-FDIC insured products, like insurance offerings or e.g. affiliated brokerage accounts, the disclosures are bespoke and extensive.

Some crypto advocates would prefer to have screen real estate in community banking apps. I bet FanDuel would, too. But them being disappointed is not the claimed threat to democracy.

Some politicians exercised extraprocedural influence

Some readers might remember Libra, Facebook’s attempt at creating a (substantially) worldwide economic network with a token which was variously described as a USD stablecoin or perhaps some sort of currency basket. Libra was a consortium project, with Facebook as the de facto anchor and a number of industry partners. (Stripe, my former employer, was a consortium member at one time. I reiterate the above disclaimer that they do not necessarily endorse things I say in my personal spaces.)

Libra did not live to see the light of day. Some time later the project was abandoned by Facebook and the technology was sold. It sold to Silvergate, back when Silvergate felt like despite the stupendous growth in the core business, sure, it had managerial attention to devote to M&A, what else would bank management possibly find to fill its time?

David Marcus, who lead Libra, recently wrote that Libra was killed by extraprocedural influence aimed at consortium members. He specifically identified Secretary of the Treasury Janet Yallen as directing the Chair of the Federal Reserve Jay Powell to kill the project. He then alleges that, quote:

Shortly thereafter, the Fed organized calls with all the participating banks, and the Fed’s general counsel read a prepared statement to each of them, saying: “We can’t stop you from moving forward and launching, but we are not comfortable with you doing so.” And just like that, it was over.

I have never worked at a bank and so never been a fly on the wall with a conversation with the Fed’s general counsel. I can, however, read. I have read many letters in my life written by serious people in positions of authority. And I once happened to read one which threatened the recipients in a clumsy, unambiguous way.

That letter was sent to all members of the Libra consortium. The letter is mostly about Facebook, rather than Libra. A representative sample:

Facebook is currently struggling to tackle massive issues, such as privacy violations, disinformation, election interference, discrimination, and fraud, and it has not demonstrated an ability to bring those failures under control. You should be concerned that any weaknesses in Facebook’s risk management systems will become weaknesses in your systems that you may not be able to effectively mitigate.

This was written after the Cambridge Analytica affair, when the security state and New York media mutually convinced each other that it is possible to steal a U.S. presidential national election with a copy of the social graph and an advertising budget of approximately $180,000. They seemed quite sure Russia had already shipped a working proof of concept. Of course, after 2020, we know that only enemies of democracy make specious and unevidenced accusations of fraud in U.S. elections. The rules change so quickly in Washington, it sometimes confounds my poor techie mind.

But this letter was written in 2019 and democracy still hung in the balance like an embattled chad (apologies to younger readers: your central association with that word is not the central association of older millennials). And so the authors of that letter, Senators Schatz and Brown (who sits on the Financial Services Committee), observed that the recipients had an excellent business and it would be a shame if something happened to it. And something would certainly happen to it if they went forward with Libra.

I realize this sounds like paranoiac ramblings. Here’s the exact money quote:

If you take this on, you can expect a high level of scrutiny from regulators not only on Libra-related payment activities, but on all payment activities.

It would be grossly improper for me to use non-public information about what a particular payments company understood that to mean. But, in my capacity as your friendly neighborhood financial infrastructure commentator, I predict that a typical financial industry CEO, threatened in that fashion by two senators, would be appropriately alarmed.

Threatening the core business over Libra hits partners with reverse operating leverage, a concept which more people in startups and finance should be aware of. One reason for the Innovator’s Dilemma isn’t within the four corners of the innovation itself, and it isn’t simply that the incumbent firm has gotten fat and happy, and wants to enjoy its margins rather than cannibalize them. It is that the innovation may require taking a risk that, if it blows up, blows up not just the (tiny, at the margins) innovation but the (gigantic) existing business which incubated it.

Google invented transformers, and they are more interesting than anything Google has done since Search, but you use ChatGPT and Claude because no Google exec was willing to blow up Search or AdWords over the geeks’ shiny new toy. It was the largest missed opportunity in the history of capitalism and they did it entirely to themselves, in (relatively tiny) part out of fear of what Washington would say. In the worst scenario of the government relations team, I doubt they conjured up “Oh two U.S. senators will explicitly threaten us with being dismantled brick by brick before this even gets to alpha.”

It is sometimes said that the dictionary definition of chutzpah is murdering your parents and then begging clemency from the judge because you are an orphan. A close runner up: when you threaten consortium members to peel them from the consortium then cite the consortium’s declining membership as a reason to threaten the consortium.

Quoting a Hill staffer, who believes that (in hopefully fair paraphrase) Facebook was simply wildly underprepared for political reality and that there was nothing improper done:

[Libra’s extremely cold reception] could be because it was tied to Facebook or could be the consortium bleeding members (each leave prompted a NYT/WSJ story which every Member of Congress read).

So yeah, that’s what the naked exercise of power looks like. And yeah, it happened. I have no strong view on whether the Fed calls also happened but, uh, that claim sort of rhymes with the letter, doesn’t it.

I will say one positive thing about the Senators writing the letter: they were sufficiently proud of their work that they posted a contemporaneous press release with the full text. Transparency is not dispositive proof of virtue. The extraprocedural threat is right there in the text. But a democracy should naturally prefer transparency, and for political decisions to be made by elected officials, over secret decisions by people who will, even in the event of extraordinary malfeasance, still have a job, a pension, and power after the inquiry.

### The CFPB

Andreessen also claimed (to Rogan) that Senator Warren created the Consumer Financial Protection Bureau and that its purview is doing, quote, “Whatever [she] wants.”

… Yeah, that’s pretty much my read, too.

I agree with some of their substantive positions and disagree with others, but it seems like a cadre of young, ambitious acolytes who understand their founder’s vision and are eager to implement it. I’ve been orbiting Silicon Valley for a long time and know the type of organization. I didn’t realize official Washington also had them. I am insufficiently politically aware to name another agency in Washington which demonstrates such a pronounced founder effect.

The CFPB’s interaction with debanking, however? De minimis.

The CFPB wrote a position paper against it. I expect people sympathetic to the CFPB to use that position paper as political/PR armor against their opponents, who are banging the drum about the broader debanking issue.

That position paper and $5 will buy you a cup of coffee at Starbucks, because the debanking bits are buried under issues the CFPB actually cares about, like taking a stick to Big Tech companies. Have you ever wondered about the consumer harm caused by… Apple Pay? Then you’ll be happy to know that they’re on the case.

### Specifically commanded politically-motivated debanking of individuals

It has been alleged that there were top-level decisions to debank individuals on the basis of their political views. There is overwhelming evidence that this happened systemically at the formal direction of national political authorities… in Canada.

Briefly, 2020 and 2021 saw substantial disruptive political protests. One of them, chiefly targeted at pandemic lockdowns, was conducted by truckers in Canada. It was unusually effective, in part because the so-called Freedom Convoy physically blocked roads in Ottowa, the capital, and at at least one border crossing to the U.S.

Blocking roads is a protesting tactic frequently employed by a variety of (mostly left-wing) activists. It is extremely annoying, arguably ineffective, and sometimes results in punishment. Punishment in a democracy customarily follows the ordinary operation of the judicial process. In the classical case, there is a formal particularized accusation, a trial, and a conviction, and only then, punishment.

Blocking roads sometimes suffers no real sanctions, because annoying and ineffective left-wing protesters still have expressive rights. Sometimes, prosecutors exercise their discretion to favor those rights over the freedom of movement and economic activity implicitly granted to other members of society.

So that was two scenarios for how things normally play out: punishment under the law, or, no punishment. Not this time, though.

Prime Minister Trudeau reacted to this protest as if it were a prompt national emergency and/or state-sponsored terrorism (a claim which was contemporaneously made about it, out of the side of officials’ mouths). He invoked the Emergencies Act, which would have the effect of awarding temporary, extraordinary executive power. The government then directed the immediate freezing of the financial accounts anyone connected to the protests, at banks and non-bank financial platforms which Canada believed had been used to fund the protest. There were also some ancillary actions, like directing the truckers’ insurance companies to suspend their driving insurance.

Officials in Canada claimed that they were selectively targeting the ring leaders or organizers of the protest narrowly, and were not attempting to consequence people for protected political speech. These claims were lies.

The orders were, in fact, not narrowly drafted.

The assistant deputy finance minister admitted to an inquiry that the government had contemporaneous knowledge that it named accountholders who were not present at the protests, and ignored this to prioritize speed of implementation. She further said, and this is a quote, “The intent was not to get at the families”, and when a democratic government starts a sentence that way something deeply #*&$#ed up has happened. Canada believes more than 200 accounts were frozen, and that is an interesting selectivity for “ringleaders” or “organizers” of a protest. (By my count, Canada itself has only a few hundred ringleaders.)

This is almost certainly an undercount, and if one does not understand the mechanism, one is not competent to work in or regulate the financial industry.

Pop quiz to see you whether you were paying attention in Compliance training: Abel transfers Bob $25, ostensibly for charitable or political purposes. Bob is specifically identified to you by the government as a terrorist later that week, his charitable fundraising apparatus is specifically called out as a concern, and you are directed to move with the utmost urgency to interdict all financial activities of Bob in any form whatsoever. Abel is not mentioned to you by name. And thus the question: this a) should have no impact on your relationship with Abel, b) should have an immediate, profound impact on your relationship with Abel, or c) I don’t know.

The government’s answer whether individuals not named by the government specifically were impacted was (paraphrasing) “I don’t know.” I don’t know whether any donors were impacted. I certainly wouldn’t expect anyone to have understood our intent to be applying the text of the order to the sender of a $25 donation. I don’t know if anyone did.

I don’t know if shooting someone will injure them or not. One might miss. I do know that my estimate of them being severely injured that day moves substantially up relative to similarly situated individuals one did not shoot. That is, presumably, why one chose to shoot them.

The invocation of a national emergency was pretextural. In the parliamentary inquiry, the deputy minister of finance said that the protests were a, this is a quote, “first-tier issue” because they… threatened U.S./Canadian negotiations on subsidies for electric vehicles.

And so when people say that targeted debanking can be used, even in a democracy, for arbitrary and capricious punishment of disfavored individuals on the political speech, laundered through the banking system, with no substantial procedural recourse, I agree with those people that that is a risk.

We just watched it happen.

### Politically-motivated debanking of individuals by firms

Some people claim politically-motivated debanking is not merely a risk but is, in fact, the ordinary practice of the United States.

It is not.

Some people claim it is the ordinary practice within the United States to debank political conservatives, to cause them to be unable to purchase food, to interdict their child support payments (as happened in Canada).

This does not happen as a matter of routine in the United States. Some people passionately believe that unarmed black men are routinely murdered by police officers. That is untrue, no matter how passionately it is believed, no matter how central that narrative is to a political project, no matter whether one supports the broader aims of that political project. That is not to say that it has never happened.

Michael Jordan once had a great line, explaining his political neutrality: “Republicans buy sneakers.” Imagine, for just one moment, what it would look like to live in a nation where Republicans actually were at constant and material risk of being debanked for their political views.

Republicans would, notoriously, only buy their sneakers in cash. Fundraising dinners would customarily have large burlap sacks next to the swanky tablecloths. You yourself, because you have at least one conservative friend, would have had an awkward conversation at some point where you suggested splitting a dinner with Venmo or tried to swap investing tips, and then realized this was a faux paus, because as everyone knows, conservatives are routinely denied access to the financial system.

This is not the world you live in. You would only need to trust your own eyes and common sense to comfortably exclude it.

There exist occasional abuses by individuals at private actors which are politically motivated. There exist some private actors who have made policy decisions, sometimes accidentally and sometimes because they have corporate (or influential-subgroup-within-the-corporation) preferences, which structurally disadvantage certain relatively narrow segments of the political spectrum.

In a world where that much more limited claim is happening, one will be able to assemble some data points to tell a story about the much larger claim. It’s important to understand what the actual true story is, because we should want to invest our collective efforts in avoiding abuses, and that requires one to know how they actually happen.

### Politically exposed persons

Andreessen said the following to Joe Rogan:

“Here’s a great thing. Under current banking, regardless, regulations, after all the reforms of the last 20 years, there's now a category called a Politically Exposed Person (PEP). And if you were a PEP, you are required by financial regulators to kick them off, to kick them out of your bank. You're not allowed to have…”

Rogan interjected:

“What if you're politically on the left?”

Andreessen answered:

“Well, that's fine. No, because they're not politically exposed.”

I have some challenges in life. One of those is that sometimes I am unable to tell if someone is making a claim about the reality we live in, or if they’re bullshitting with a bro. This has, over the years, caused me much embarrassment. You obviously do not want to intrude on a bullshitting session and say “That isn’t true!”, because truth is not the point of a bullshitting session. And you don’t want to say “And once a monkey flew out of my butt!” if someone is trying to describe reality. They will not laugh, and you will be sad.

So I recuse myself from the above conversation, that I have no usable bead on, and will take this opportunity to lecture the Internet about PEPs.

Politically Exposed Person (PEP) is a term of art in Compliance, arising from Bank Secrecy Act (BSA) reporting requirements. It means a national-level senior official, most typically in U.S. usage, one attached to a foreign government. Quote: “The Agencies do not interpret the term ‘politically exposed persons’ to include U.S. public officials.” (Like many financial regulations, the U.S. has intentionally caused its concern with PEPs to metastasize to aligned countries. In some of those countries, financial institutions are obliged to treat from-their-perspective-domestic senior political officials/etc as PEPs.)

PEP status also attaches to the close family members and close associates of a PEP. Who is a “close associate”? Write down your understanding of that, run it by your regulator, and then comport your affairs consistently with your written understanding. Lots of banking regulation works like this: plodding, iterative development of internal policies, with occasional spot checks on performance under those policies, including as part of scheduled bank examinations.

PEPs are believed to present elevated money laundering risk. Some of them control national resources directly, and others may be at risk of e.g. bribery.

There is not an official regulator-blessed list of which positions are presumptive proof of PEPiness. This is one of those things that banks need to write down in their procedures then run past their regulator, who will either say “Sounds good! Definitely EDD those PEPs!”, or “I dunno. I know it’s a schlep but you’ll want to grep more PEPs.”

A typical list will include e.g. president, head of state, national members of the legislature, cabinet officials, supreme judiciary body judges, head of the central bank, cabinet-equivalent ministers, etc etc.

You can absolutely bank PEPs, just like you can bank high-risk businesses. You need to EDD them. Certain banks, largely ginormous money center banks with worldwide operations, put in the specialized work to do this. This is because (with absolutely no insinuation of impropriety here!) private banking benefits from paying attentive service to rich and powerful people so that they talk you up to their rich and powerful friends.

Now, an individual private banker might be tempted to give more than attentive service. Regulators frown on that, hence PEP status and PEP screening tools.

What is a PEP screening tool? I’m glad you asked. Many people will open accounts with you every day. You can, if your policies and regulator allow it, ask all of them “Pardon me sir/madam: are you the president of a foreign nation? Answer quickly because I’ve got about 15 more of these.” But the vast majority of new customers will think you are very stupid. You can’t not know, though. Very plausibly, you don’t trust a 22 year old drawn at random from your employee base to have comprehensive knowledge of the spouses of the current membership of the Sąd Najwyższy.

Since software is eating the world, you can buy a product from any of a number of firms that will ask software these questions. You run an identity by it, and it says “Elected to the upper house of the Japanese Diet in 2022; likely a PEP” or “Unlikely to be a PEP.”

This will allow you to decrease customer and employee friction in many of your product lines, while having a responsive answer to your bank examiner when they ask about your PEP program. The other parts of your PEP program will be dreadfully boring. You will write a procedure which says that e.g. that if news reporting or facts available the bank cause it to understand an existing customer to be newly a PEP (or uncover previously missed PEPness), this will trigger a review of their account relationship, which you would duly document. Then, you would add them to your EDD process for PEPs.

EDD for PEPs is (bottom line here) going to require someone to write a quarterly memo saying “Uneventful quarter. The $1.2 million incoming wire was sale of private residence. We commissioned an appraisal (attached) and, based on comps, seems reasonable. Account holder’s title to property confirmed via title search (attached); it substantially predates most recent election. No other items of note.”

And that’s all you need to know about PEPs.

PEPs are extremely uncommon in the world relative to all people/firms. My one professional encounter with the concept when a particular bank claimed a European mayor of a small city was a PEP, on basis of being a politician, and would require EDD to onboard. I protested on behalf of the user. Compliance got annoyed at me for PEPsplaining them.

### Politically motivated debanking of individuals, redux

Earlier we mentioned that the combination of a monoculture plus a plainly stated or implied policy directive can cause ambitious or ingratiating individuals to take action in the absence of any order to do so. This is very much a risk.

And if you care about debanking, you should care about this mechanism a lot more than you care about PEP minutiae.

Permit me a brief detour from banking to the Internet companies that run so much of our modern world.

It is fairly well understood by people that closely follow the tech industry that Trust and Safety teams were for years a locus of micropolitical action, some of it originating with uninvolved users on Twitter, and some of it originating within the house.

The prevailing political culture of Trust and Safety teams was, well… look, let me level with you. Get a group of twentysomething San Franciscans with college degrees together. Now, filter out all the ones who can get a high-paying engineering job or would be reasonably fundable. Now, select of the remainder those who would want to stay, for several years, in a position where they are in charge of being a hall monitor on every human utterance which travels over electrons.

I think fairminded individuals of many political persuasions will understand that the population who gets through these filters uses the spelling “freeze peach” instead of “free speech” at a much higher base rate than the American population does.

Individuals in Trust and Safety, and sometimes Trust and Safety as a system, at various times in various places, may have engaged in some shenanigans. That isn’t a load-bearing claim to how this has relevance for debanking, but it happens to be true, and I’d be remiss if I didn’t say it.

If you didn’t keep a really close eye on them, and senior management at AppAmaGooFaceSoft doesn’t really keep a close eye on low-paid operational employees making decisions unless they cause substantial PR or government relations backlash, Trust and Safety would happily “deplatform” people whose politics they disliked for fairly benign reasons, while zealously defending people whose politics they liked.

This is an iterated game, and people realized you could just ask Trust and Safety to deplatform someone. Product teams built some flows to expedite this. You could “brigade” those automated tools (e.g. act in concert with friends to mass report a social media post), or make a fuss on Twitter (and wait for a company to perceive brand risk), or just ask an individual Trust and Safety person at a party.

And thus, shenanigans.

This was substantially exacerbated once government actors realized they could make Trust and Safety feel really special by having them have monthly meetings with Certifiably Important People. Eventually, at and around these meetings, those attendees began to ask Trust and Safety “Will no one rid me of this turbulent priest?” And then after having done that for a while, we slouched into a situation where there was an official at the White House who understood his job to be the Illegal Orders Czar. He badgered Facebook, Twitter, and similar on a post-by-post basis and also zealously advocated at the platform-wide policy level. I’ve never met him but I bet he thinks he is a good person and very good at his job.

We had a number of officials, in various government departments, who believed they could enact policy preferences more effectively by working through catspaws than by the ordinary operation of the government. But it is a singular fact that one of them was in the White House. He once invoked direct personal interest, from POTUS, explicitly, in writing, to jawbone Youtube to up its censorship game. Citation (pg 19).

Andreessen, who is on the board of Facebook, has discussed the perception and mechanisms of the shenanigan era and then the attempts-at-explicit compulsion era. I refer interested readers to his words in other places, because I really do want to get back to banking regulation.

I only know what I read in court documents, hear on the grapevine, and very occasionally see with my own two eyes. What I know is sufficient to agree with Justice Alito: “If the lower courts’ assessment of the voluminous record is correct, this is one of the most important free speech cases to reach [the Supreme Court] in years.”

The weaponization of Trust and Safety by the “misinformation” industrial/academic/NGO complex and partners in government is a scandal. Tech was… complicit? I think that is a fair characterization. We were complicit for a few years. We have since found our spine, and expressed some amount of regret for decisions made contemporaneously with the demands.

One notable specific example of this change: Mark Zuckerberg, in a letter to Congress: “I believe that the government pressure was wrong, and I regret we weren’t more outspoken about it. I also think that we made some choices that, with the benefit of hindsight and new information, we wouldn’t make today.”

What do Trust and Safety decisions on e.g. misinformation or hate have to do with debanking? Regrettably, more than one would think.

Compliance is also a monoculture. Good news: Compliance across the banking industry and related companies is substantially more politically diverse than Trust and Safety was in San Francisco. Compliance decisions are also much more commercially meaningful, directly, than Trust and Safety decisions are. Compliance has to sacrifice a paying customer; Trust and Safety just needs to sacrifice advertising inventory. It's hard to recruit customers but ginning up more advertising inventory is fairly straightforward: you can do it simply by making different product decisions about ad load, for example.

Bad news: Compliance is designed to be a monoculture. First among all things, if you work in Compliance, you must be good at being an ingratiating rule-follower. I do not mean the word “ingratiating” as a criticism. I mean it as a description of an affect. You must perform compliance to work in Compliance. If you do not, if you have a rebellious streak, if you throw elbows in meetings with your regulator, you will be replaced by someone who is not incompetent at the job they were hired to do.

Compliance staff, particularly at senior levels (where they are deciding policy instead of merely clicking on alerts), are central members of the American professional-managerial class. And the culture that is the American PMC has some quirks.

### The Current Thing is dead; long live the Current Thing

The American PMC has is periodically seized by… maniac moral fascination. Andreessen has previously called this the Current Thing. Scholarly literature has sometimes used the phrase “moral panics” but generally that is about the population generally. I prefer Andreessen’s formulation to capture the distinctive way the PMC—his class, my class, and (very probably, since you voluntarily read several thousand words about banking regulation) your class—performs itself.

If one is worried about extraordinary debanking, worry less about formal guidance, and worry more about the Current Thing. Because Compliance doesn’t need to get an email from a regulator or read a position paper to get the Current Thing. The Current Thing was in the New York Times this morning. The Current Thing is all over Twitter. The Current Thing is in the air we breathe. Who could possibly be so oblivious as to not understand the Current Thing? Certainly not a competent professional in a bank or fintech Compliance department.

Our model for conspiracies frequently supposes some central actor. The Current Thing has no central actor. When it is no longer the Current Thing, when sanity reasserts itself, we will look for evidence that it was the CIA or the Russians or the Soros network or the Kochs or misinformation or any of the thousand excuses we have used to protest our innocence. We will break out scanning tunneling microscopes to go over the audit logs.

And we will discover that, at worst, there was a trivial halfhearted attempt to bootstrap coordination, but it cannot possibly explain the firestorm, which kicked off faster and had more lockstep alignment than we could accomplish on our best day with the utmost of our capabilities.

My goodness, can you imagine what our companies would achieve, can you imagine how effective at its aims the government would be, can you imagine how much money would be made, if we could simply declare a Current Thing at will.

There exist past Current Things.

The United States had a rough few years with destructive political protests at which people sometimes died. And the Current Thing demanded you make very fine distinctions indeed between destructive political protests at which people sometimes died.

For example: sometimes exuberant political speech on issues of obvious national import devolves into destructive political protests at which people sometimes died. Can you fund protesters’ legal expenses, or advocate for them? What if you are, say, a national-level U.S. politician? What is the exact decisioning flowchart here?

Now some people might think: “Would Compliance debank you over that? Of course not. That is mainstream political speech; we don’t debank people for mainstream political speech. And of a national-level U.S. politician no less?! Goodness, can you imagine the headline risk? Can you imagine the government relations risk!?”

And other people might think: “A U.S. politician is carrying water for political violence!? That is a shocking violation of norms, and must be opposed by all right-thinking people! Granted, we will certainly eat headline risk for this, because we are in a deeply divided nation, but we should swiftly withdraw all financial services! And technical services and social media services and if they get their underwear laundered by a service turn that one off too!”

These two models have very different ex ante prediction of the behavior of corporations.

Which produces the right output? Neither. It turns out that behavior is very context-dependent.

Sometimes you’re uncontroversially allowed to fundraise for people who got arrested at a riot. Sometimes, while it might make people uncomfortable, you will be allowed back into polite society if you staff or fund the storming of a Capitol building. Sometimes, after destructive political protests at which people (including cops) died, tech companies donate money to the organizers, because the political project seems to be of ongoing importance, and clearly nobody intends for there to be deaths at a political protest.

But sometimes, after destructive political protests at which people died, the Current Thing breaks the other way. Sometimes, this causes the great and the good, and also Compliance officers, to immediately throw all levers in their power.

The Current Thing requires no top-down direction. The White House doesn’t need to call. A senator’s letter will arrive days too late to matter.

Some people passionately believe the Current Thing from four years ago. But it seems like the consensus on it, and it was an automatic consensus in many places professionally relevant, is shifting under our feet.

What is the consensus in Washington right now? I’m pretty good at reading tea leaves in Japanese but have limited ability to decode Washingtonese. My present model for the new consensus: “It’s a shame when people die, of course, and political protests should probably not be destructive, of course, but the political leadership of the U.S. is acceptable in polite society, of course, and it would be irresponsible to support a coup, of course, because all Presidents of the U.S. have been legitimately elected, of course, and because there has never been an attempted coup in the United States, of course, and if anyone ever said anything different well sometimes political speech gets feisty, of course.”

The Current Thing does not always favor the political left. “Russian sympathizers have taken over the highest levels of the U.S. government! We need to...!” seems to have sharply different political valence depending on exactly what tone of voice you say it in.

The Current Thing is not always even conveniently describable by the left/right axis, though sometimes it gets drafted. At no point prior to it becoming a Current Thing did anyone anywhere on the U.S. political spectrum care about drinking straws. I think ostentatiously using a plastic drinking straw might be a right-aligned signifer now in some circles. Ponder that statement. Ostentatiously. Using. A. Plastic. Drinking. Straw.

Sometimes, the alignment of the parties pivots on a dime while a new Current Thing is developing. Understanding that that happens is one of the most important contributions the Current Thing concept offers.

One of the few blessings of middle age is that one has lived through many Current Things. If one is reflective about it, even if one has fairly strong and fairly stable convictions, even if one remembers on occasion enthusiastically supporting the position that happens to be one that is one’s party’s line on an individual Current Thing, one has distinct, vivid memories. One remembers what everyone around you once believed about a thing, and they believed it with passionate intensity, and now they believe literally the opposite thing, with equally passionate intensity. And they seem to not remember and they don’t seem to be insane. You can easily have a concept about any work-relevant issue which isn’t the Current Thing. They demonstrate object permanence in those other conversations.

I will leave debating individual examples to people who write about politics for a living or follow it for the vicarious thrill some people get from team sports.

I don’t know what to do with the Current Thing observation, generally. I just want to get back to writing about wire transfer compliance. But if the next Current Thing happens to arrive, and it is… squirrels, then there exists the risk that Compliance will develop an intense interest in squirrels. And fifteen years from that day, Compliance will still take the time, once a year or so, to review the necessity of updates to the squirrel interdiction policy.

### What to do about debanking

Some people reading this are very, sincerely concerned with debanking.

Permit me to give you tactical advice to advance your values: put as many calories as possible into designing countermeasures to the Current Thing causing swift, arbitrary action against (primarily) existing accounts by Compliance. You probably won’t abolish Compliance departments as an institution. You probably won’t convince banks to bear the stupendous losses they’d get if they had to open accounts for substantially all comers. Bury Compliance in paperwork and delays for closing an account. You can tell your friends (or enemies) “Well, it’s as serious as evicting someone, so it should be as rigorously documented as evicting someone is in a reasonable city. Like, say, Chicago or New York.”

If you do this, there will be tradeoffs. You will see them most directly in unwillingness to bank marginal prospects for accounts, and indirectly in measurements of unbanked/underbanked in populations you care about. But this will, very effectively, cut down specifically on disruption caused to people and companies by the offboarding letter.

Now plausibly you might say there is a free lunch: just be morally righteous and have a backbone. And I agree, in a limited sense. Some virtues are free lunches. We want more of them.

But those virtues are empirically insufficient to guarantee behavior. Tomorrow’s Current Thing is very, very powerful, and it might even be aligned with your inclinations. And look back at history: the voluminous history of humanity, the recent history of one’s nation or industry, or even one’s personal Twitter archives. Look how many times righteous people with substantial backbone heard about the Current Thing and said “... Nah, not the hill I want to die on.”

### The policy program crypto advocates will use claims of debanking to advance

Sometimes rich, powerful people just tweet things. (I can relate; I just tweet things all the time.)

But sometimes there is an agenda. “You’ve got an agenda!” is sometimes used as a cynical attack in politics. Democratic governance necessarily requires at least some people to have agendas.

Agendas are frequently published, much more frequently than they are secretly swapped in back rooms. Telling people what you want is a necessary step in getting what you want. Talking about the agenda is really useful for coordinating support for the agenda.

Crypto, like any industry, has people with a diversity of views in it. But one can’t losslessly describe the world without being the world, and some lossy models are still useful.

I have taken the liberty of writing a compressed version of what crypto wants, for the benefit of readers who might not geek out on this stuff. If you’d prefer hearing it from them directly, out of concern I’m being unfair, see this thread. Alternatively, you can read the writings of the advocates already namechecked, or spend a few days digesting the policy papers of their lobbyists.

Crypto wants all banks to be directed to bank “all legal businesses”, by which they mean crypto companies and crypto founders. They will want an end to banks having discretion in onboarding clients to “vanilla” deposit products, first. They will claim they want this pretty much across the board; their exception will be e.g. Hamas. You get a corporate checking account, you get a corporate checking account, everybody gets a corporate checking account.

Having achieved this for low-risk vanilla products, they will want sharply less resistance for e.g. high velocity facilitation of funds flows by financial services firms, as long as those financial services firms say the usual things about playing ball, even if those financial services firms are crypto native. Their most immediate concern is exchanges, but they also want less resistance to novel products and use cases.

Crypto wants their bank back. They don’t care what the name on the door is, but they want a bank which can do instantaneous book transfers and will accept basically all comers. Not Hamas, no, but if you would not onboard an entity controlled by CZ, Justin Sun, or someone understood to be Tether’s new best friend, you do not understand the assignment.

They want it to ask the minimum number of questions required to continue servicing high volumes compliantly in the United States, primarily. Their secondary priority will be serving as wide a footprint as can be reached without endangering the business within the United States. The U.S. is where the money is and they know this.

Crypto, nominally, would be happy with changes to U.S. financial plumbing that allowed you to stitch a SEN-equivalent product out of other banks. But they think they’ll probably need a bank, and they think that bank will probably not be their bank if they are just a quickly growing startup business within a ginormous bank. No, they want a bank with 100%-or-as-close-as-makes-no-difference crypto deposit concentration, which will cater assiduously to their needs, and which will fight the good fight if they ever need it to.

Crypto will compromise on (read: sacrifice the chance of directly doing business with firms or individuals from) Russia, without notable complaint. When the conversation turns to China… well, you know, a lot of financial innovation was forced to flee to… many countries in East Asia, including some of our truest friends, under the previous regime. It would be a shame if you sacrificed American competitiveness and national security by not inviting those dollars back to where we can see them.

Crypto will be very in favor of U.S. national interests vis China, and some crypto investors have any number of proposals on how NatSecTech will help close the technical capabilities gap on e.g. manufacturing drone components. They have a number of portfolio companies to introduce you to, Washington, and plan to have more shortly.

If you are a regulator and don’t want crypto to have a bank, they want you to be promoted to private citizen as early as possible. And they want to make it very, very, very clear to junior staff that the same awaits them if they get out of line.

If you engage crypto in Washington and present as clueful, perhaps by saying “Aren't most of the fruits of the innovation you just described as having departed the U.S. due to the previous administration actually custodied in New York right now? At Cantor Fitzgerald, right?”, crypto will say “Yes, I am glad you brought that up. Stablecoins are one of the world’s largest users of U.S. Treasuries. We have a position paper about this. It is critically important to maintain the U.S.’s lead in stablecoins. You should prefer them be custodied within the United States. We think we have workable solutions for doing them within the regulated perimeter.”

And what about the elephant in the room? "Is that a Republican joke?!"

Crypto wants full unreserved repudiation of all guidance that suggests cryptocurrencies are high-risk. Pause letters, position papers, informal guidance, supervisory questions, they want it all swept clean with a broom. They don’t care all that much about what banking regulators do after that, but if you want a suggestion, it should be asking banks about their crypto strategy, listening attentively, then exercising moral suasion if they don’t have one. If banks identify barriers to adoption of blockchain technology, advocates want regulators to react to that like the emergency it is.

Crypto wants banks to be able to custody cryptoassets. There is a highly technical accounting standard that you probably don’t care about, which governs how much capital a bank needs to back assets it custodies. A bank needs $1 in equity capital to custody $1 in digital assets. This makes running a crypto custody business within the banking perimeter a non-starter.

Crypto already has crypto custody products available, but they are at places like e.g. Coinbase and not e.g. State Street. Crypto wants a custody business within the banking perimeter, because they perceive this as necessary to ease institutional adoption. They want parity with traditional risk assets (like equities), minimally. If they get that they’ll pivot to asking for a thumb on the scale. Crypto is not wrong that capital requirements place a thumb on the scale for some politically preferred assets (e.g. MBS).

Crypto wants to rewrite the formal history of the 2023 banking crisis. There are several supervisory reports which lay out a narrative, some linked above. You will replace and repudiate those reports. The new ones will claim that the failure of the banks was proximately caused by explicitly directed political action by the prior administration. You will aver that this and similar supervisory actions are against the policy of the United States. You will look the camera in the eye and, very sternly, say that banks acting contrary to this instruction will feel the full weight of the federal government arrayed against them.

Crypto doesn’t really care about what you say about SVB or First Republic.

Crypto wants Fed master accounts for state-chartered crypto-native financial services companies. Simple enough. They want them with the automaticity that a community bank gets them. We show our charter and ask; you issue.

Crypto wants the SEC to provide a repeatable, predictable path for selling tokens to ordinary Americans as early in the issuer’s lifecycle as reasonably feasible. The existing registration and exemption regime that non-crypto startups are under is, pointedly, one cross crypto/tech investors are extremely familiar with. They do not want parity with that regime.

They want to be able to sell tokens to retail, because retail is where the money is.

They are actually pretty sincere that as long as you give them carte blanche to sell to retail, they will follow the procedures you outline to unlock that. $1 million in compliance cost for an unrestricted offering is fine, and will cut down on headline risk by chasing away some of the 2017-era-ICO nonsense. Venture firms will be happy to underwrite the ante.

After you give them this, crypto will industrialize and blitzscale efforts to market crypto investment opportunities as investment opportunities to all Americans who currently invest in any capacity whatsoever and many who do not. They know (to a mortal certainty) they can sell tens of billions of dollars of these products if allowed to. That would be a failure, because crypto has required so much infra investment to get to the present day. Crypto's ambitions are much higher. They do not think trillions of dollars are out of reach. Trillions would be a success.

Crypto is starting to get just smidge impatient about when they get their trillions. Some crypto investors are on a shot clock, because they have made promises to capital partners. For many of them, Bitcoin at $100,000 is amazingly good news but not by itself a victory condition. They need that path to a trillion dollars of token sales.

Crypto wants permissive guidance about novel crypto-adjacent banking products. Banks should be able to issue crypto-backed loans at parity to public equity-backed loans, for minimally the majors (BTC/ETH). Stablecoins should get treatment similar to a CD- or moneymarket-backed loan. (These are all very niche products, yes, but what is finance if not people who are very creative at imagining circumstances where you'd want very niche products.)

Everything else banks offer? We want it, too, on equal footing.

Crypto wants some institutional examples made. They want at least one regulator canceled-without-replacement and they want the world to understand that crypto did it. They don’t expect it to be the Fed (not realistic) or the FDIC (indispensable infrastructure; keeps retail happy). The CFPB though? They’d take the CFPB.

And now you know why we’re having a sudden conversation about debanking.

Fiction and Finance →

## Want more essays in your inbox?

I write about the intersection of tech and finance, approximately biweekly. It's free.


