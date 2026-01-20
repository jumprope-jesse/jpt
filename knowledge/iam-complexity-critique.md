# IAM Complexity Critique

## The Problem

IAM (Identity and Access Management) in cloud providers has become a nightmare of complexity that violates the principle of least privilege while simultaneously making it nearly impossible to do the right thing.

## The Janitor Key Metaphor

The perfect analogy: A janitor needs one master key to clean a building. Then security hears about stolen keys, so they implement a byzantine system where:

1. Janitor must request specific keys from security engineer
2. Keys have meaningless names (`executive_floor/admin` vs `executive_floor/viewer`)
3. Janitor accumulates a massive keyring through trial and error
4. Keys open things they don't need (security risk remains)
5. New system adds per-door restrictions, but office moves make lists outdated
6. Eventually janitor has master key equivalent through accumulation, but nobody knows exactly what they can access

**This is cloud IAM today.**

## Why It's Broken

### The Guessing Game

When developers need permissions:

1. Security/Ops team guesses what roles are needed based on names
2. Developer tries it, gets `authorizationerror:foo`
3. Switch role, try again
4. Discover service A requires role in service B
5. Cobble together custom role with 90% unused permissions sitting as security holes
6. Hope nobody adds resources without updating scoped permissions

### AWS: Bad But Manageable

- 100+ predefined roles to choose from
- Can cobble together something that works
- At least auditable
- Major issue: `/*` permissions are Satan's work, need to scope to specific instances and hope nothing gets added without permission updates

### GCP: Aggressively Worse

Google looked at AWS's tire fire and said "hold my expensive coffee robot."

**The Folder Structure Trap:**
- Encourages setting basic roles at folder level (Viewer, Editor, Owner)
- Seems logical at first
- Breaks down as GCP adds services - each basic role encompasses thousands of permissions
- Led to 1,687+ predefined roles

**The Custom Role Nightmare:**
- Cannot combine predefined roles
- Must list individual permissions
- Predefined roles change DAILY with new services
- Must build automation to track role changes over time
- Or accept users have unknown, changing permissions

**Launch Stages Make It Worse:**
- Roles have metadata: ALPHA, BETA, GA, DISABLED
- Roles you depend on can be in development or testing
- Permissions included in roles are constantly in flux

## The Obvious Solution (That Nobody Implements)

**Track actual usage and scope accordingly:**

1. Give new developers broad permissions + viewer access
2. Track what they actually use for 30-90 days
3. Automatically scope down to only used permissions
4. Both AWS and GCP already have this data and functionality (Role Recommendations, Access Analyzer)

**For urgent permission needs:**
- Expiring temporary permissions (4-hour grants)
- On-call rotation gets elevated access automatically
- Slack bot or web interface for requests
- Based on actual data, not guessing

## Why This Isn't a Security Hole

**Current approach:** Team A guesses what Team B needs without doing Team B's work, or security team tries to figure out if requests "make sense"

**Data-driven approach:** Based on actual usage patterns, with time-limited elevation for emergencies

At least one is grounded in reality instead of dart-throwing at IAM role lists.

## The Real Issue

- IAM started simple, became nightmarish as services proliferated
- GCP is worse than AWS
- All the tools and data exist to fix this
- Needs a provider brave enough to say "we messed up, let's break the legacy system"
- Migration will be painful but the end state will be better

## Key Insights

1. **Complexity defeats security**: When doing the right thing is too hard, people take shortcuts
2. **Permission accumulation is inevitable**: Longer someone works, more permissions they accumulate
3. **Nobody really knows what anyone can access**: Too complex to audit effectively
4. **The tools exist**: Cloud providers have usage tracking, they just don't use it for automatic scoping
5. **Best practice is practically impossible**: Following "principle of least privilege" requires building custom automation on top of cloud IAM

## Implications for Startups/Teams

- Budget significant time for IAM setup and maintenance
- Accept that you'll either have security holes or blocked developers
- Consider building automation around usage-based permission scoping early
- GCP IAM complexity is a real cost consideration vs AWS
- Temporary elevated permissions system is table stakes for developer velocity

## Source

https://matduggan.com/iam-is-the-worst/
