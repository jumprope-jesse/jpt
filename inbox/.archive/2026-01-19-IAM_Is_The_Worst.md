---
type: link
source: notion
url: https://matduggan.com/iam-is-the-worst/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-03-15T13:22:00.000Z
---

# IAM Is The Worst

## Overview (from Notion)
- IAM Complexity: The struggles with Identity and Access Management (IAM) in cloud environments highlight frustrations that resonate in your tech career, where managing permissions can feel like a never-ending battle.
- Real-World Analogy: The janitor key metaphor is relatable; it mirrors the challenge of ensuring your team has the right tools without unnecessary clutter—something you might face while founding a startup or managing a team.
- Efficiency vs. Security: Balancing efficiency (getting things done quickly) with security is a common tension in tech. The document articulates this dilemma well, prompting you to think about how to streamline processes without compromising safety.
- Scalable Solutions: The proposed solutions for better IAM systems call for innovation—an opportunity for you to explore creating more efficient tools as a founder.
- Feedback Loop: The emphasis on understanding user needs through data aligns with your role in developing software that meets real-world demands, urging you to build systems that adapt and evolve based on actual usage.
- Alternate Viewpoints: Some may argue that strict IAM policies are necessary for security; however, the document suggests that overly complicated systems can hinder productivity, prompting a reevaluation of traditional approaches.
- Future of Work: As remote work becomes more common, the insights about IAM systems might influence how your team operates, emphasizing the need for agile, user-friendly access management.

## AI Summary (from Notion)
IAM in cloud environments is overly complex and inefficient, leading to excessive permissions and security risks. A better approach would involve tracking actual usage to streamline access management and reduce unnecessary permissions.

## Content (from Notion)

Imagine your job was to clean a giant office building. You go from floor to floor, opening doors, collecting trash, getting a vacuum out of the cleaning closet and putting it back. It's a normal job and part of that job is someone gives you a key. The key opens every door everywhere. Everyone understands the key is powerful, but they also understand you need to do your job.

Then your management hears about someone stealing janitor keys. So they take away your universal key and they say "you need to tell Suzie, our security engineer, which keys you need at which time". But the keys don't just unlock one door, some unlock a lot of doors and some desk drawers, some open the vault (imagine this is the Die Hard building), some don't open any doors but instead turn on the coffee machine. Obviously the keys have titles, but the titles mean nothing. Do you need the "executive_floor/admin" key or the "executive_floor/viewer" key?

But you are a good employee and understand that security is a part of the job. So you dutifully request the keys you think you need, try to do your job, open a new ticket when the key doesn't open a door you want, try it again, it still doesn't open the door you want so then there's another key. Soon your keyring is massive, just a clanging sound as you walk down the hallway. It mostly works, but a lot of the keys open stuff you don't need, which makes you think maybe this entire thing was pointless.

The company is growing and we need new janitors, but they don't want to give all the new janitors your key ring. So they roll out a new system which says "now the keys can only open doors that we have written down that this key can open, even if it says "executive_floor/admin". The problem is people move offices all the time, so even if the list of what doors that key opened was true when it was issued, it's not true tomorrow. The Security team and HR share a list, but the list sometimes drifts or maybe someone moves offices without telling the right people.

Soon nobody is really 100% sure what you can or cannot open, including you. Sure someone can audit it and figure it out, but the risk of removing access means you cannot do your job and the office doesn't get cleaned. So practically speaking the longer someone works as a janitor the more doors they can open until eventually they have the same level of access as your original master key even if that wasn't the intent.

That's IAM (Identity and access management) in cloud providers today.

### Stare Into Madness

AWS IAM Approval Flow

GCP IAM Approval Flow

It's Not Natural, It's Just Simple: Food Branding Co-Opts Another Mean

Honestly I don't even know why I'm complaining. Of course it's entirely reasonable to expect anyone working in a cloud environment to understand the dozen+ ways that they may or may not have access to a particular resource. Maybe they have permissions at a folder level, or an org level, but that permission is gated by specific resources.

Maybe they don't even have access but the tool they're interacting with the resource with has permission to do it, so they can do it but only as long as they are SSH'd into host01, not if they try to do it through some cloud shell. Possibly they had access to it before, but now they don't since they moved teams. Perhaps the members of this team were previously part of some existing group but now new employees aren't added to that group so some parts of the team can access X but others cannot. Or they actually have the correct permissions to the resource but the resource is located in another account and they don't have the right permission to traverse the networking link between the two VPCs.

Meanwhile someone is staring at these flowcharts trying to figure out what in hell is even happening here. As someone who has had to do this multiple times in my life, let me tell you the real-world workflow that ends up happening.

- Developer wants to launch a new service using new cloud products. They put in a ticket for me to give them access to the correct "roles" to do this.
- I need to look at two elements of it, both what are the permissions the person needs in order to see if the thing is working and then the permissions the service needs in order to complete the task it is trying to complete.
- So I go through my giant list of roles and try to cobble together something that I think based on the names will do what I want. Do you feel like a roles/datastore.viewer or more of a roles/datastore.keyVisualizerViewer? To run backups is roles/datastore.backupsAdmin sufficient or do I need to add roles/datastore.backupSchedulesAdmin in there as well?
- They try it and it doesn't work. Reopen the ticket with "I still get authorizationerror:foo". I switch that role with a different role, try it again. Run it through the simulator, it seems to work, but they report a new different error because actually in order to use service A you need to also have a role in service B. Go into bathroom, scream into the void and return to your terminal.
- We end up cobbling together a custom role that includes all the permissions that this application needs and the remaining 90% of permissions are something it will never ever use but will just sit there as a possible security hole.
- Because /* permissions are the work of Satan, I need to scope it to specific instances of that resource and just hope nobody ever adds a SQS queue without....checking the permissions I guess. In theory we should catch it in the non-prod environments but there's always the chance that someone messes up something at a higher level of permissions that does something in non-prod and doesn't exist in prod so we'll just kinda cross our fingers there.
### GCP Makes It Worse

So that's effectively the AWS story, which is terrible but at least it's possible to cobble together something that works and you can audit. Google looked at this and said "what if we could express how much we hate Infrastructure teams as a service?" Expensive coffee robots were engaged, colorful furniture was sat on and the brightest minds of our generation came up with a system so punishing you'd think you did something to offend them personally.

Google looked at AWS and said "this is a tire fire" as corporations put non-prod and prod environments in the same accounts and then tried to divide them by conditionals. So they came up with a folder structure:

The problem is that this design encourages unsafe practices by promoting "groups should be set at the folder level with one of the default basic roles". It makes sense logically at first that you are a viewer, editor or owner. But as GCP adds more services this model breaks down quickly because each one of these encompasses thousands upon thousands of permissions. So additional IAM predefined roles were layered on.

People were encouraged to move away from the basic roles and towards the predefined roles. There are ServiceAgent roles that were designated for service accounts, aka the permissions you actual application has and then everything else. Then there are 1687 other roles for you to pick from to assign to your groups of users.

The problem is none of this is actually best practice. Even when assigning users "small roles", we're still not following the principal of least privilege. Also the roles don't remain static. As new services come online permissions are added to roles.

The above is an automated process that pulls down all the roles from the gcloud CLI tool and updates them for latest. It is a constant state of flux with roles with daily changes. It gets even more complicated though.

You also need to check the launch stage of a role.

> Custom roles include a launch stage as part of the role's metadata. The most common launch stages for custom roles are ALPHA, BETA, and GA. These launch stages are informational; they help you keep track of whether each role is ready for widespread use. Another common launch stage is DISABLED. This launch stage lets you disable a custom role.

> We recommend that you use launch stages to convey the following information about the role:

> EAP or ALPHA: The role is still being developed or tested, or it includes permissions for Google Cloud services or features that are not yet public. It is not ready for widespread use.

### Who Cares?

Why would anyone care if Google is constantly changing roles? Well it matters because with GCP to make a custom role, you cannot combine predefined roles. Instead you need to go down to the permission level to list out all of the things those roles can do, then feed that list of permissions into the definition of your custom role and push that up to GCP.

In order to follow best practices this is what you have to do. Otherwise you will always be left with users that have a ton of unused permissions along with the fear of a security breach allowing someone to execute commands in your GCP account through an applications service account that cause way more damage than the actual application justifies.

So you get to build automated tooling which either queries the predefined roles for change over time and roll those into your custom roles so that you can assign a user or group one specific role that lets them do everything they need. Or you can assign these same folks multiple of the 1600+ predefined roles, accept that they have permissions they don't need and also just internalize that day to day you don't know how much the scope of those permissions have changed.

### The Obvious Solution

Why am I ranting about this? Because the solution is so blindly obvious I don't understand why we're not already doing it. It's a solution I've had to build, myself, multiple times and at this point am furious that this keeps being my responsibility as I funnel hundreds of thousands of dollars to cloud providers.

What is this obvious solution? You, an application developer, need to launch a new service. I give you a service account that lets you do almost everything inside of that account along with a viewer account for your user that lets you go into the web console and see everything. You churn away happily, writing code that uses all those new great services. Meanwhile, we're tracking all the permissions your application and you are using.

At some time interval, 30 or 90 or whatever days, my tool looks at the permissions your application has used over the last 90 days and says "remove the global permissions and scope it to these". I don't need to ask you what you need, because I can see it. In the same vein I do the same thing with your user or group permissions. You don't need viewer everywhere because I can see what you've looked at.

Both GCP and AWS support this and have all this functionality baked in. GCP has the role recommendations which tracks exactly what I'm talking about and recommends lowering the role. AWS tracks the exact same information and can be used to do the exact same thing.

What if the user needs different permissions in a hurry?

This is not actually that hard to account for and again is something I and countless others have been forced to make over and over. You can issue expiring permissions in both situations where a user can request a role be temporarily granted to them and then it disappears in 4 hours. I've seen every version of these, from Slack bots to websites, but they're all the same thing. If user is in X group they're allowed to request Y temporary permissions. OR if the user is on-call as determined with an API call to the on-call provider they get more powers. Either design works fine.

That seems like a giant security hole

Compared to what? Team A guessing what Team B needs even though they don't ever do the work that Team B does? Some security team receiving a request for permissions and trying to figure out if the request "makes sense" or not? At least this approach is based on actual data and not throwing darts at a list of IAM roles and seeing what "feels right".

### Conclusion

IAM started out as an easy idea that as more and more services were launched, started to become nightmarish to organize. It's too hard to do the right thing now and it's even harder to do the right thing in GCP compared to AWS. The solution is not complicated. We have all the tools, all the data, we understand how they fit together. We just need one of the providers to be brave enough to say "obviously we messed up and this legacy system you all built your access control on is bad and broken". It'll be horrible, we'll all grumble and moan but in the end it'll be a better world for us all.

Feedback: https://c.im/@matdevdug


