---
type: link
source: notion
url: https://tesseral.com/blog/b2b-auth-isnt-that-similar-to-b2c-auth
notion_type: Tech Deep Dive
tags: ['Running']
created: 2025-06-30T17:29:00.000Z
---

# Auth for B2B SaaS: it's not like auth for consumer software | Tesseral Blog

## Overview (from Notion)
- The article highlights the critical differences between B2B and B2C authentication, emphasizing how B2B software needs to manage user access at an organizational level, not just individual users.
- As a software engineer and founder, understanding these nuances can help you build products that better serve enterprise clients, which is essential for scaling your business in a competitive market.
- The emphasis on security, such as insider threats and role-based access control, aligns with the increasing importance of data protection in today's digital landscape.
- The discussion around support features, such as user impersonation and robust audit logs, can resonate with your experience in providing customer service and managing software systems.
- It challenges the conventional mindset that B2C design principles can be applied to B2B, suggesting a more tailored approach for enterprise needs.
- An alternative view is that some features traditionally seen as B2B, like user impersonation, might also find relevance in consumer applications as they scale and require more complex user management.
- The insights into identity providers and provisioning highlight the importance of integrating systems smoothly, which can inform your approach to software architecture and partnerships.

## AI Summary (from Notion)
B2B authentication differs significantly from B2C due to factors like logical isolation, user control, and organizational tenancy. Businesses prioritize user management and security features, requiring support for enterprise identity providers, single sign-on, and role-based access control. Additionally, B2B applications must address insider threats and provide comprehensive audit logs, reflecting the unique needs of enterprise software compared to consumer applications.

## Content (from Notion)

Back to Blog

Auth for business software (B2B) shouldn’t look the same as auth for consumer software (B2C). In many cases, it actually can’t work the same way.

I’ll cover three important buckets of differences between B2B auth and B2C auth:

1. Logical isolation and tenancy models
1. Priorities and trade-offs
1. Protocols and features
By the way – let’s use auth loosely here and let it subsume related stuff like user management. Similarly, let’s just imagine away the vague grey area between consumers and businesses (e.g., software for sole proprietors) and focus solely on obvious consumer apps and obvious enterprise products. A simplified model of the world helps make things clear.

## Logical isolation and tenancy models

In B2C software, your customers are your users. They’re individual people that control their own accounts. Things don’t work that way in B2B software. Businesses want to control their users’ access; and within a given business, not all users should work the same way. This has pretty significant implications for auth.

Let’s first look at tenancy in consumer software and then take a glance at business software.

### Users: First-class tenancy in consumer software

In a consumer application, we primarily care about individual users.

To illustrate what this looks like, I went to Club Penguin Legacy and created an account for myself. Signing up for a CPL account is pretty easy. Aside from email verification, all you need is a username and a password.

Club Penguin associates all of my data with my penguin. I get to edit some of my penguin’s data if I want. For example, each penguin gets an igloo. I get to edit my own igloo.

No one else gets to edit my igloo.

If I want to upgrade my igloo, Club Penguin checks to see how many coins I have. This is a property that’s associated with my user account. Regrettably, I do not have enough coins to purchase the undersea igloo theme.

None of what I’ve covered here should seem surprising. This all seems kind of obvious – kind of normal – doesn’t it?

I have an account for myself, and data lives on the account level. I alone exercise control over my account. My content is mine, at least in the sense that it doesn’t belong to another user. It’s just me and the penguin.

Isn’t this how pretty much all software works, you might wonder. This is how we learn to build software in school, right? It’s the most obvious way to implement logical isolation; it makes intuitive sense.

But this tenancy model doesn’t work for business software. If you use the Club Penguin tenancy model in business software, you’re going to have a very bad time.

### Organizations: First-class tenancy in business software

The tenancy model for business software doesn’t put end users first. When you’re selling B2B, your customer isn’t an end user. It’s more complicated than that. Your customer is a company. And the company wants control over its users.

I like to use Slack as an example here.

If you’ve ever used Slack, you have a sense for what it’s like. You can send passive aggressive GIFs to your coworkers. You can upload custom reactions that are just cropped pictures of your boss’s face lifted from college-era Facebook photos. You can scroll all the way up in #general to find gossip that HR hasn’t thought to remove.

All of Slack’s useful features require that you and your colleagues can exchange messages, so you all need to be clustered together in the same software-defined place. Slack calls these places Workspaces. Normally, each Workspace maps onto a unique business customer. And end users – employees of business customers – all belong to Workspaces. We can say that the Workspace is the first-class tenant. We can say that a tenancy firewall exists between such tenants.

Business software pretty much always implements tenancy like this. You need some concept of company-level tenancy to support the features that business customers expect. (More on this later.)

Now, in the real world, this actually ends up being a bit complicated. Keeping Slack as an example, one of my former employers actually had dozens of Workspaces across the company; IT had some convoluted enterprise-y way of managing these in a hierarchy. Plus, Slack now has its Connect feature that allows you to communicate across tenants. But let’s imagine all of these wrinkles away.

It’s certainly possible to bolt-on a B2B multitenancy model when you already have some users. We see this from time to time. However, it's usually complicated and laborious. A lot of sensitive code needs to get rewritten when you change your tenancy model.

Life is easier when you get this right from the start.

## Different priorities

### Performance at scale

Consumer software must always anticipate the possibility of many users.

At the extreme end of scale, Meta, reports 3.35 billion Daily Active People (DAP) across its different applications (Instagram, WhatsApp, Facebook, etc.). Even a relatively niche app like chess.com reports more than 200 million users; it’s normal at any time for several hundred thousand users to be active.

Maintaining any reasonable standard of performance can force a major consumer software application to do complicated things. An example from a Meta whitepaper:

> 

These performance considerations aren’t often relevant in business software. Immense B2B companies like Salesforce or Zoom aside, control planes for business software applications tend not to operate at such extreme scale. And even when they do, sharding’s an option (not so for Facebook – everyone needs to live in the same Facebook.com!).

Consequently, B2B applications rarely need to invent new, bespoke things.

### End user experience

End user experience is everything in consumer software. Consumers use products that they like, and they’re often picky.

Teams that build consumer software try very hard to prevent users from churning – or even failing to activate altogether. Consider that a freemium product will consider itself unusually successful if it converts ~1% of users to its paid tier. Against that low base rate, even very subtle optimizations can be powerful.

Consumer applications have strong incentives not to introduce friction into sign-up or log-in flows. For example, Reddit doesn’t try very hard to get users to adopt multi-factor authentication.

By contrast, end users of business software don’t get to pick their software – at least not very often. They generally use the software that their employers choose. As a consequence, end user experience tends not to matter quite as much as in consumer software. Little speed bumps are okay if they serve a business need.

This means that business software can force annoying – but important – security onto end users. We can make people eat their metaphorical vegetables.

### Support as an escape hatch

Consumer software and business software have pretty different unit economics. A typical user of consumer software is worth a lot less than a typical user of business software. The different unit economics have design implications throughout entire products, of course, but for the purposes of this article, we’ll just focus on user auth.

Consider Pinterest. That’s a pretty successful consumer software company, right? I mean, at time of writing, Pinterest trades at roughly a $25B market cap. Even for a company as successful as Pinterest, the average user isn’t worth much. For FY24, average revenue per user (ARPU) for Pinterest came in at $6.94. I’m not missing a digit here. An average Pinterest user is worth about as much to Pinterest as a San Francisco cold brew.

That’s pretty different from a B2B app like Zendesk, which charges $1,380 per user per year for its Suite Professional product. I’m handwaving a bit with this comparison, but still. That’s almost exactly 200x the value of a Pinterest user.

That huge disparity in the value of an average user means you can do some pretty different things in business software.

If you’re locked out of consumer software, you’re usually left to navigate some labyrinthine bureaucracy. Sometimes you won’t succeed at all; for example, there are many posts online of people interminably locked out of their Apple accounts.

In business software, life can be pretty simple. Business software vendors don’t really need a lot of process; they’re just not dealing with the same sort of support volume. You can plausibly even have an engineer run a one-off script for a customer.

Business software vendors can afford to take shortcuts, provided their auth systems come with the right features. For example, it’s common for a business software vendor to guide a customer through implementation or to tweak some settings. To do this, business software vendors often turn on user impersonation. This means that a support person can grant himself a session, logging in as his customer. It’s a pretty neat trick that circumvents long email chains.

### Threat model: outsiders vs. insiders

In consumer software, we mostly worry about managing scams, fraud, and abuse.

Phishing scams are a big problem – someone tries to trick you into handing over your bank login or your Gmail. Account sharing can be an issue: if you want to make Uber Eats deliveries, you need to pass a background check; it’s a problem for Uber if drivers can share accounts, because a person can circumvent the background check by simply using someone else’s account.

Consumer software also has to battle bots and ban users that can’t abide by content moderation policies. This often means that consumer auth systems often need to support identity resolution. They need to link different accounts using incomplete information. If I’ve been banned from Facebook on an account linked to the phone number (800) 867 5309, Facebook should likely extend the ban on my account to any subsequent sign-ups using the same phone number. Even if I change the email address and use a different name, Facebook can still correctly link me to the original banned account.

Now, business software developers share some problems with their peers building consumer software. We still have to be paranoid. Phishing is still a problem. Attackers will still try credential stuffing attacks, and the man in the middle isn’t going anywhere. It’s just that the dynamics are a little different.

One unique dynamic in business software is the focus on insider attacks.

Consider what happens if a company parts ways with an employee on less-than-amicable terms. That employee might surreptitiously hold on to old credentials and commit sabotage. Or we might see a repeat of the 2008 Terry Childs incident: a man locked out all other San Francisco municipal employees from accessing parts of their internal network.

We need to build resilience from insider attacks into business software. That generally means we need to build different features into our auth systems (more on this later).

## Features and protocols

In general, business software requires auth features that aren’t relevant in consumer software. Previously, I mentioned user impersonation as an example. That certainly counts, but it’s honestly a small detail. It’s kind of a nice-to-have. There are other features that just aren’t especially negotiable.

### Support for enterprise identity providers

Businesses of scale have thousands of employees, and each employee needs some relatively unique subset of enterprise software. These large companies can’t handle access management by hand. Instead, they use centralized IT software applications called identity providers (IDPs) to manage employees' access to software.

To a first approximation, businesses use IDPs as if they were databases. IDPs maintain lists of employees and lists of software applications that a company pays for. They maintain associations between employees and software, e.g. Jerry in the Omaha office gets to use Netsuite.

On top of that database-esque functionality, IDPs centralize the company’s control over software applications. If a company revokes an employee’s access to software, the IDP enforces that revocation. If a company promotes an employee, the IDP propagates the employee’s updated job title and any relevant permissions (e.g. becoming an admin) to all of the relevant software applications.

If you sell business software, you will eventually need to support a broad range of different identity providers. Sure, support for Okta and Entra gets you pretty far, but people use all kinds of IDPs in the real world, from reasonable options like old-school ADFS or Sailpoint to chaotic custom builds that no one’s touched since 2005.

### Enterprise single sign-on (SSO)

Enterprise customers will almost universally want their vendors to offer enterprise single sign-on.

They want their employees to authenticate once in an identity provider (e.g., Okta, Entra) and extend that authentication context into third party software (e.g., Slack, Zoom). If you’ve worked at a big company, you’ve probably accessed software using enterprise single sign-on.

Enterprise single sign-on nearly always relies on a strange, archaic protocol called SAML. That’s not because SAML is a uniquely great standard. It’s more like an accident of history. SAML’s been around a really long time, and people are just accustomed to it. That’s especially true in industries like healthcare that tend to be a bit risk-averse and slow to adopt new technologies.

A detailed treatment of SAML isn’t really in-scope here. I’d just highlight the following:

1. SAML is weird. Just brace yourself for the first customer that asks for SAML. You’ll figure out how it works eventually, but know that it takes some time to really understand.
1. You have to be really careful with a SAML implementation. It’s very easy to introduce major security problems. We’ve written a bit about this here.
1. SAML isn’t like Login with Google. Every one of your business customers that uses SAML will need its own manual configuration – and therefore time from your engineering team.
Whether you like it or not (you probably don’t), business software usually needs to support SAML SSO.

### Provisioning (SCIM)

Enterprise customers often want to control their user data in your software. They’ll want to set up an integration between your software and their identity provider (again, e.g., Okta, Entra). In particular, they’ll want to (a) provision new users and (b) deprovision existing users. They’ll also want to update certain users’ attributes (e.g., if someone gets promoted), but that’s not generally critical.

Companies care about automating new employees’ access to systems. It’s just really inconvenient for an IT admin to manually click around adding people one-by-one to every different software application.

Companies care even more about making sure they can deprovision users. If someone parts ways with the company, it’s both practical and important for security to turn off his account. It seems silly, but recently departed employees retaining valid credentials remains a huge security problem for big companies. To use one example that recently made news, Disney let an employee go but neglected to revoke his access to their parks’ menu design system – he made a number of malicious edits that resulted in a prison sentence.

SCIM is a standardized protocol for these provisioning integrations between identity providers and service providers. If you want to learn more about SCIM, you can check out my explainer here.

### Role-based access control

Not every user within a given organization should be able to do the same things. Different people have different jobs – and different responsibilities.

I like to use expense management apps as an example for this.

Everyone in a company should probably have the ability to request reimbursement for a business expense. Someone in sales might take a client out to lunch. Someone in engineering might buy a new mechanical keyboard with cool LEDs.

But not everyone in a company should have the ability to approve or pay out an expense – especially large expenses. Intuitively, we should recognize that an intern shouldn’t be approving $100,000 invoices. That should probably be an executive’s responsibility.

In business software, we most commonly rely on an authorization pattern called role-based access control (RBAC). We define some list of actions (e.g., expense.submit, expense.approve, expense.pay_out). We map those actions to some number of roles (e.g., superadmin). Then, we assign roles to users. A given user’s authorization largely extends from his assigned roles.

RBAC is usually pretty simple, but it can get complicated. My favorite example of this is Salesforce. For those who aren’t acquainted, Salesforce is a pretty generic piece of software – you can make it do all kinds of crazy stuff. Consequently, it has a very complex permissions system that it exposes to its customers. A Salesforce admin can create arbitrarily complex custom roles.

At a certain level of maturity, it often becomes essential for business software to look like this. It’s a lot of work to get RBAC exactly right.

### Organization-level control

Some customers are pickier than others. They might have different compliance regimes to navigate. They might just be picky.

But you’ll eventually encounter support tickets that look like this:

- Can you make sure users can’t log in with their email?
- Can you make sure our users can’t invite people to our organization?
- Can you require all of our users to use Yubikeys for MFA?
- Can you make sure users never log in from [list of high-risk countries]?
Customers of a certain scale expect the answer to be yes.

If you’ve built your auth system to be the same for all users – irrespective of their organization – you’ll have a hard time accommodating those requests. You might end up writing some weird custom code. We’ve seen this before. It usually looks something like this.

```plain text
if (customer_id == “X”):
	# do stuff
else:
	# do something else
```

### API keys

Consumer software doesn’t often expose public APIs. After all, consumers don’t normally write code. A consumer app that exposes a public API has probably approached substantial scale.

By contrast, business software frequently needs to offer API keys even at a pretty small scale. And managing API keys is a bit of a pain, especially if you need them to be performant. It’s just another thing to worry about if you’re building business software.

### Audit logs

Enterprise customers often expect comprehensive logs of everything that happens in their organization. That means they need a record of their employees’ actions in your software. There are a few major reasons.

Sometimes, the motivation is legal. Companies need a long-lived archive of employees’ actions in case they wind up in litigation, a criminal enquiry, or some other unpleasant matter. I’m reminded of the Rippling-Deel espionage issues, in which Rippling’s logs of employees’ actions in Slack served as pretty convincing evidence. How does this relate to auth, you might wonder. Well, you really need to know who a user is for the logs to be very useful.

Audit logging is probably more relevant – and more closely tied to auth – for its security applications. Security teams often want to know what’s going on. For example, an attacker might try an incorrect username/password pair for john.doe@parnellaerospace.com, then try bob.jones@parnellaerospace.com and so on. In this case, Parnell Aerospace probably wants a heads-up that this is going on. For this reason, security-conscious organizations often request that vendors can pass audit logging events into SIEM systems.

### Wrapping up

B2B software and B2C software need different things from their auth systems. If you’re building your own auth system for B2B, you should be aware of the long list of annoying enterprise requirements you’ll run into. If you’re shopping for an auth vendor, try to make sure that your vendor focuses on business software – it’s rare for a vendor to do both B2B and B2C well.

Tesseral is an open source auth service designed uniquely for business software. You can learn more at https://tesseral.com/docs or visit us on GitHub.


